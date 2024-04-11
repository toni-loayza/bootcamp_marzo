from odoo import models, fields, api


class AcademyStudent(models.Model):
    _name = "academy.student"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = "Students"

    name = fields.Char(string="Name", required=True, default="New")
    partner_id = fields.Many2one("res.partner", string="Student", required=True, readonly=False, tracking=True)
    school_id = fields.Many2one("res.partner", string="School", tracking=True)
    employee_id = fields.Many2one("hr.employee", string="Student", tracking=True)
    hr_icon_display = fields.Selection(related="employee_id.hr_icon_display")
    resource_calendar_id = fields.Many2one("resource.calendar", string="Hour", tracking=True)
    date = fields.Date(string="Date", tracking=True)
    state = fields.Selection(string='State', tracking=True,
                             selection=[('draft', 'Draft'),
                                        ('posted', 'Posted'),
                                        ('cancelled', 'Cancelled')], default='draft')

    @api.onchange('partner_id')
    def onchange_partner(self):
        if self.partner_id:
            self.write({
                'school_id': self.partner_id.parent_id.id
            })
        else:
            self.write({'school_id': False})

    @api.onchange('resource_calendar_id')
    def onchange_resource_calendar(self):
        if self.resource_calendar_id and self.employee_id:
            self.employee_id.resource_calendar_id = self.resource_calendar_id.id

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            if val.get('name', "New") == "New":
                val['name'] = self.env["ir.sequence"].next_by_code("academy_student")
        return super(AcademyStudent, self).create(vals_list)

    def action_confirm(self):
        if not self.employee_id:
            employee = self.env["hr.employee"].create({'name': self.partner_id.name, 'employee_type': 'student'})
            self.write({'employee_id': employee.id, 'resource_calendar_id': employee.resource_calendar_id.id})
            employee.generate_random_barcode()
        else:
            self.write({'resource_calendar_id': self.employee_id.resource_calendar_id.id})

        self.state = 'posted'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'

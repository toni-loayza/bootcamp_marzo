from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.onchange('birthday')
    def compute_pin_student(self):
        if self.birthday:
            birthday = str(self.birthday)
            self.pin = birthday.replace("-", "")

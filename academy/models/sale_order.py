from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self.env["academy.student"].create(self.vals_student())
        return res

    def vals_student(self):
        return {
            'partner_id': self.partner_id.id,
            'date': self.date_order
        }

from odoo import models, fields


class SaleOder(models.Model):
    _inherit = 'sale.order'

    room_ids = fields.Many2many(comodel_name='hotel.room', string=' room_ids')

    def action_confirm(self):
        res = super(SaleOder, self).action_confirm()
        self.room_ids.action_busy()
        return res

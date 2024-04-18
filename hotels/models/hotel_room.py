from odoo import models, fields


class HotelRoom(models.Model):
    _name = 'hotel.room'

    name = fields.Char(string='Name', required=True)

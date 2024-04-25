from odoo import models, fields

STARS = [
    ('none', 'None'),
    ('one', 'One'),
    ('two', 'Two'),
    ('three', 'Three'),
    ('four', 'Four'),
    ('five', 'Five')
]


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = "Room"
    _order = "name"

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Char(string='Description', tracking=True)
    occupancy_date = fields.Datetime(string='Occupancy Date', tracking=True)
    state = fields.Selection(string='State', selection=[('free', 'Free'), ('busy', 'Busy')], default="free",
                             tracking=True)
    stars = fields.Selection(string='Stars', selection=STARS, tracking=True)

    def action_free(self):
        self.state = 'free'

    def action_busy(self):
        self.write({'state': 'busy', 'occupancy_date': fields.Datetime.now(self)})

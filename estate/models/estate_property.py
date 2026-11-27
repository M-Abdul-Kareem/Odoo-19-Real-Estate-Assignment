from odoo import api, models, fields
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    has_garden = fields.Boolean()
    garden_area = fields.Integer()

    offer_ids = fields.One2many("estate.property.offer","property_id")

    best_price = fields.Float(compute="_compute_best_price", string='Best Offer')
    
    total_area = fields.Integer(compute="_compute_total_area")

    state = fields.Selection(
        selection=[ 
            ('new','New'),
            ('offer_received','Offer Received'),
            ('offer_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled')], default = 'new'
    )

    buyer_id = fields.Many2one('res.partner')
    property_manager = fields.Many2one('res.users')



    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0.0

    def sell_property(self):
        for record in self:
            if record.state== 'cancelled':
                raise UserError ('Cancelled properties cannot be sold')
            else:
                record.state = 'sold'

    def cancel_property(self):
            for record in self:
                if record.state== 'sold':
                    raise UserError ('Sold properties cannot be cancelled')
                else:
                    record.state = 'cancelled'                
    _check_expected_price = models.Constraint(
        "CHECK(expected_price > 0)",
        " The Expected price must be greater than 0"
    )
    _check_name = models.Constraint(
        "UNIQUE(name)",
        "The name must be unique"
    )
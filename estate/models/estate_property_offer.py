from odoo import api, models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offer"

    price = fields.Float()
    property_id = fields.Many2one('estate.property')
    partner_id = fields.Many2one('res.partner')
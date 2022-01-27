from odoo import models, fields, api, _


class FlowerWatering(models.Model):
    _name = 'flower.watering'
    _description = 'Flower Watering History Item'

    date = fields.Date(readonly=True)
    lot_id = fields.Many2one('stock.production.lot', ondelete='cascade')

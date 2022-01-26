# -*- coding: utf-8 -*-
from odoo import models, fields


class MyAwesomeModel(models.Model):
    _inherit = 'product.template'

    # name = fields.Char() # no longer needed
    scientific_name = fields.Char()
    season_start = fields.Date()
    season_end = fields.Date()
    watering_frequency = fields.Integer()
    watering_amount_ml = fields.Float()
    is_flower = fields.Boolean()

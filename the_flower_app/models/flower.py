# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences

from odoo import models, fields


class MyAwesomeModel(models.Model):
    _name = 'flower.flower'
    _description = 'Flower'

    name = fields.Char()
    scientific_name = fields.Char()
    season_start = fields.Date()
    season_end = fields.Date()
    watering_frequency = fields.Integer()
    watering_amount_ml = fields.Float()

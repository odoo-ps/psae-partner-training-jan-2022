# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class Partner(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date('Date of Birth')
    age = fields.Integer(compute='_compute_age')

    @api.depends('dob')
    def _compute_age(self):
        for partner in self:
            partner.age = relativedelta(fields.Date.today(), partner.dob).years


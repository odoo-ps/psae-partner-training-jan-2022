# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.osv import expression

class MyAwesomeModel(models.Model):
    _inherit = 'product.template'

    # name = fields.Char() # no longer needed
    scientific_name = fields.Char()
    season_start = fields.Date()
    season_end = fields.Date()
    watering_frequency = fields.Integer()
    watering_amount_ml = fields.Float()
    is_flower = fields.Boolean()
    flower_sequence_id = fields.Many2one('ir.sequence')




class Product(models.Model):
    _inherit = 'product.product'

    needs_watering = fields.Boolean(compute='_compute_needs_watering')

    def _compute_needs_watering(self):
        all_flowers = self.env['stock.production.lot'].search([
            ('is_flower', '=', True),
            ('expected_next_watering_date', '<=', fields.Date.today()),
            ('product_id', 'in', self.ids)
        ])
        product_id_set = {flower.product_id.id for flower in all_flowers}
        for product in self:
            product.needs_watering = product.is_flower and product.id in product_id_set

    def action_show_plants(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("stock.action_production_lot_form")
        action['domain'] = [('product_id', '=', self.id)]
        action['context'] = {
            'default_product_id': self.id,
            'default_company_id': (self.company_id or self.env.company).id,
            'default_name': self.flower_sequence_id.next_by_id()
        }
        return action





# class Lead(models.Model):
#     _inherit = 'crm.lead'
#
#     additional_user_ids = fields.Many2many('res.users')
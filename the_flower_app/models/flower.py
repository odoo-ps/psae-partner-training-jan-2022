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

    def action_open_product_lot(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("stock.action_production_lot_form")
        action['domain'] = [('product_id', '=', self.id)]
        action['context'] = {
            'default_product_id': self.id,
            'default_company_id': (self.company_id or self.env.company).id,
        }
        return action


class Product(models.Model):
    _inherit = 'product.product'

    # def name_get(self):
    #     res = super(Product, self).name_get()
    #
    #     out = []
    #
    #     for r in res:
    #         out.append((r[0], '<ba6a6is>' + r[1]))
    #
    #     return out
    #
    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = [('min_age', '<', name)]
    #     return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)

from datetime import timedelta

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Lot(models.Model):
    _inherit = 'stock.production.lot'

    watering_ids = fields.One2many('flower.watering', 'lot_id')
    last_watering_date = fields.Date(compute='_compute_last_watering_date', store=True)
    is_flower = fields.Boolean(related='product_id.is_flower', store=True)
    watering_frequency = fields.Integer(related='product_id.watering_frequency')
    expected_next_watering_date = fields.Date(compute='_compute_last_watering_date', store=True)

    @api.constrains('watering_ids')
    def _could_only_water_on_time(self):
        for lot in self:
            if not lot.last_watering_date or len(lot.watering_ids) < 2:
                continue
            if (lot.last_watering_date + timedelta(days=lot.watering_frequency)) > fields.Date.today():
                raise ValidationError(_(f'Could only water a {lot.product_id.name} once every {lot.watering_frequency} days'))

    @api.depends('watering_ids')
    def _compute_last_watering_date(self):
        for lot in self:
            if lot.watering_ids:
                lot.last_watering_date = lot.watering_ids[-1].date
                lot.expected_next_watering_date = lot.watering_ids[-1].date + timedelta(days=lot.watering_frequency)
            else:
                lot.last_watering_date = False
                lot.expected_next_watering_date = fields.Date.today()

    def action_water(self):
        self.filtered(lambda lot: lot.is_flower).write({'watering_ids': [fields.Command.create({'date': fields.Date.today()})]})

    def action_show_watering_history(self):
        self.ensure_one()
        return {
            'name': _(f'{self.product_id.name} - {self.name} - Watering History'),
            'view_mode': 'tree',
            'res_model': 'flower.watering',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('lot_id', '=', self.id)],
            'context': {
                'create': False,
                'edit': False
            }
        }
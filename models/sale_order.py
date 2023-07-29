# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    operation_type = fields.Selection(
        [('BAT_146', 'BAT TH 146'), ('BAR_160', 'BAR TH  160'), ('BAT_103', 'BAT-EN-103')],
        string="Type d'operation", required=True)
    def get_total_qty(self):
        total_qty = sum(self.order_line.mapped('product_uom_qty'))
        return total_qty

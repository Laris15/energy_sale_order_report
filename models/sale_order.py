# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def get_total_qty(self):
        total_qty = sum(self.order_line.mapped('product_uom_qty'))
        return total_qty

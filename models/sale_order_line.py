# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    localisation = fields.Char('Localisation',  store=True)
    address = fields.Char('Address',  store=True)


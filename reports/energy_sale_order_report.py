# -*- coding: utf-8 -*-

from odoo import api, fields, models


class EnergySaleOrderReport(models.AbstractModel):
    _name = 'report.energy.sale.report'
    _description = 'Energy Sale Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.order',
            'docs': docs,
        }

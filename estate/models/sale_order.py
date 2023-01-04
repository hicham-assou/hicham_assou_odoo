from odoo import models, fields, api, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    state = fields.Selection(selection_add=[('quotation_approved', "Quotation Approved")])

    @api.one
    def action_quotation_approve(self):
        self.state = 'quotation_approved'


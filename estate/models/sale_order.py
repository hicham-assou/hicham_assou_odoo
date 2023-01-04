from odoo import models, fields, api, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('waiting_approval', 'En attente d\'approbation'),
        ('approved', 'Approuvé'),
        ('sent', 'Devis envoyé'),
        ('sale', 'Vente'),
        ('done', 'Terminé'),
        ('cancel', 'Annulé'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

    def action_waiting_approval(self):
        # Mettez la commande de vente en attente d'approbation
        self.state = 'waiting_approval'

    def action_approve(self):
        # Approuvez la commande de vente
        self.state = 'approved'
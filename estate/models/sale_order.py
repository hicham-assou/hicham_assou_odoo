from odoo import models, fields, api, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Ajoutez un champ "approval_level" pour stocker le niveau d'approbation de la commande
    approval_level = fields.Integer(string='Approval Level', default=0)

    def _check_approval_level(self):
        # Vérifiez le niveau d'approbation de la commande en fonction du montant de la commande
        if self.amount_total < 500:
            self.approval_level = 0
        elif self.amount_total < 2000:
            self.approval_level = 1
        elif self.amount_total < 5000:
            self.approval_level = 2
        else:
            self.approval_level = 3

    def action_confirm(self):
        # Vérifiez le niveau d'approbation de la commande avant de la confirmer
        self._check_approval_level()
        if self.approval_level == 0:
            # Pas besoin d'approbation, confirmez la commande
            return super(SaleOrder, self).action_confirm()
        else:
            # Vérifiez si l'utilisateur a le bon niveau de gestionnaire pour approuver la commande
            user_groups = self.env.user.groups_id.mapped('id')
            if self.approval_level == 1 and 1 in user_groups:
                # L'utilisateur est un gestionnaire de niveau 1, approuvez la commande
                return super(SaleOrder, self).action_confirm()
            elif self.approval_level == 2 and (1 in user_groups or 2 in user_groups):
                # L'utilisateur est un gestionnaire de niveau 1 ou 2, approuvez la commande
                return super(SaleOrder, self).action_confirm()
            elif self.approval_level == 3 and (1 in user_groups or 2 in user_groups or 3 in user_groups):
                # L'utilisateur est un gestionnaire de niveau 1, 2 ou 3, approuvez la commande
                return super(SaleOrder, self).action_confirm()
            else:
                # L'utilisateur n'a pas le bon niveau de gestionnaire, affichez un message d'erreur
                raise exceptions.ValidationError("Vous n'avez pas le niveau de gestionnaire requis pour approuver cette commande de vente.")

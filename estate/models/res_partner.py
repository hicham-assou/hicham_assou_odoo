from odoo import fields, models, exceptions

from estate.models.sale_order import SaleOrder


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Ajoutez un champ "approval_level" au modèle "res.partner" pour stocker le niveau d'approbation des partenaires
    class Partner(models.Model):
        _inherit = 'res.partner'
        approval_level = fields.Integer(string='Approval Level', default=0)

    # Ajoutez un champ "manager_level" au modèle "res.users" pour stocker le niveau de gestionnaire de chaque utilisateur
    class User(models.Model):
        _inherit = 'res.users'
        manager_level = fields.Integer(string='Manager Level', default=0)

    # Modifiez la fonction "action_confirm" du modèle "sale.order" pour vérifier le niveau d'approbation et de gestionnaire avant de confirmer la commande
    class SaleOrder(models.Model):
        _inherit = 'sale.order'

        def action_confirm(self):
            # Vérifiez le niveau d'approbation du partenaire et le niveau de gestionnaire de l'utilisateur avant de confirmer la commande
            if self.partner_id.approval_level <= self.env.user.manager_level:
                # Le niveau d'approbation du partenaire est inférieur ou égal au niveau de gestionnaire de l'utilisateur, confirmez la commande
                return super(SaleOrder, self).action_confirm()
            else:
                # Le niveau d'approbation du partenaire est supérieur au niveau de gestionnaire de l'utilisateur, affichez un message d'erreur
                raise exceptions.ValidationError("Vous n'avez pas le niveau de gestionnaire requis pour approuver cette commande.")

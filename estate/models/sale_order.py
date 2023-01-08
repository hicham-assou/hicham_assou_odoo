from odoo import models, fields, api, exceptions
from datetime import timedelta

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_waiting_approval(self):
        # Mettez la commande de vente en attente d'approbation
        self.state = 'waiting_approval'

    def action_approve(self):

        user_groups = self.env.user.groups_id
        if self.amount_total < 500:
            super().action_confirm()
        elif 500 <= self.amount_total < 2000:
            if any(group.name in ('Manager Level 1', 'Manager Level 2', 'Manager Level 3') for group in user_groups):
                super().action_confirm()
            else:
                raise exceptions.ValidationError(
                    "Vous n'avez pas le droit")
        elif 2000 <= self.amount_total < 5000:
            if any(group.name in ('Manager Level 2', 'Manager Level 3') for group in user_groups):
                super().action_confirm()
            else:
                raise exceptions.ValidationError(
                    "Vous n'avez pas le droit")
        else:
            if any(group.name == 'Manager Level 3' for group in user_groups):
                super().action_confirm()
            else:
                raise exceptions.ValidationError("Vous n'avez pas le droit")




def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        for line in self.order_line:
            if line.employee:
                start_datetime = fields.Datetime.to_string(line.training_date)
                end_datetime = fields.Datetime.from_string(start_datetime) + timedelta(hours=12)
                if line.employee.user_id:
                    user_id = line.employee.user_id.id
                else:
                    user_id = self.env.user.id

                values = {
                    'name': '%s' % line.name,
                    'start': start_datetime,
                    'stop': end_datetime,
                    'partner_ids': [(4, line.employee.id)],
                    'user_id': user_id,
                }
                event = self.env['calendar.event'].create(values)

        self.action_approve()

        #if self.amount_total > 500:
        #    self.state = 'waiting_approval'#
        #    if self.user_has_groups('base.manager'):
         #       self._set_state("done")
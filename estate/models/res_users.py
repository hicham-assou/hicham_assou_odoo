from odoo import fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'
    manager_level = fields.Integer(string='Manager Level', related='partner_id.manager_level')

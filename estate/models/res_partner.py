from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    manager_level = fields.Integer(string='Manager Level', default=0)

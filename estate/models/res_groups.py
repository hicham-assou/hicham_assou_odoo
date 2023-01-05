from odoo import fields, models


class ResGroups(models.Model):
    _inherit = 'res.groups'
    name = fields.Char(string='Group Name')
    category_id = fields.Many2one('ir.module.category', string='Application')
    manager_level = fields.Integer(string='Manager Level')


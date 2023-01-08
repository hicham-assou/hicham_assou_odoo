from odoo import fields, models


class ResGroups(models.Model):
    _inherit = 'res.groups'
    name = fields.Char(string='Name', required=True)
    category_id = fields.Many2one('ir.module.category', string='Module Category')

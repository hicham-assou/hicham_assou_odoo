from odoo import fields, models


class ResGroups(models.Model):
    _inherit = 'res.groups'

    name = fields.Char(translate=True)
    category_id = fields.Many2one('ir.module.category', string='Application')
    group_type = fields.Selection([
        ('manager_level_0', 'Manager Level 0'),
        ('manager_level_1', 'Manager Level 1'),
        ('manager_level_2', 'Manager Level 2'),
        ('manager_level_3', 'Manager Level 3')
    ], string='Type', required=True, default='manager_level_0')

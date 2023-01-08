from odoo import fields, models


class ResGroups(models.Model):
    _inherit = 'res.groups'
    name = fields.Char(string='Name', required=True)
    category_id = fields.Many2one('ir.module.category', string='Module Category')
    implied_ids = fields.Many2many('res.groups', 'res_groups_implied_rel', 'grp_id', 'implied_grp_id', string='Implied Groups')
    comment = fields.Text(string='Comment')
from odoo import fields, models, Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    employee = fields.Many2one('hr.employee', string="Employee")
    training_date = fields.Date(string="training date")


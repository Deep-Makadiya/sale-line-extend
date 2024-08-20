from odoo import models, fields, api, _
from odoo import models, api, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_lines_new =fields.One2many('sale.order.line.new','order_id',string="Order Line  New")
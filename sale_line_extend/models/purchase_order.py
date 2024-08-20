from odoo import models, fields, api, _
from odoo import models, api, exceptions


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchase_order_lines_new =fields.One2many('purchase.order.line.new','order_id',string="Purchase Order Line New")
from odoo import models, fields, api, _
from odoo import models, api, exceptions


class PurchaseOrderLineNew(models.Model):
    _name = 'purchase.order.line.new'

    product_id =fields.Many2one('product.product',string="Product Id")
    name =fields.Char(string="Name")
    quantity = fields.Float(default=1.0)
    uom_id =fields.Many2one('uom.uom',string="UOM ID")
    price = fields.Float(string="Price")
    total = fields.Float(string="Total", compute='_compute_total')
    order_id =fields.Many2one('purchase.order',string="Order Id")

    @api.depends('quantity', 'price')
    def _compute_total(self):
        for line in self:
            line.total = line.price * line.quantity

    @api.onchange('product_id')
    def _onchange_product(self):
        for line in self:
            if line.product_id:
                line.uom_id = line.product_id.uom_id
                line.name = line.product_id.name
                line.price = line.product_id.standard_price
from odoo import models, fields, api, _
from odoo import models, api, exceptions


class SaleOrderLineNew(models.Model):
    _name = 'sale.order.line.new'

    product_id = fields.Many2one('product.product', string="Product Id")
    name = fields.Char(string="Name")
    quantity = fields.Float(default=1.0, string="Quantity")
    uom_id = fields.Many2one('uom.uom', string="UOM Id")
    price = fields.Float(string="Price")
    total = fields.Float(string="Total",compute='_compute_totals')
    order_id = fields.Many2one('sale.order', string="Order Id")

    @api.depends('quantity', 'price')
    def _compute_totals(self):
        for line in self:
            line.total = line.price * line.quantity

    @api.onchange('product_id')
    def _onchange_product(self):
        for line in self:
            if line.product_id:
                line.uom_id = line.product_id.uom_id
                line.name = line.product_id.name
                line.price = line.product_id.standard_price

    @api.model
    def create(self, vals):
        # Create the sale.order.line.new record
        new_record = super(SaleOrderLineNew, self).create(vals)

        # Prepare the values for the sale.order.line record
        sale_order_line_vals = {
            'order_id': new_record.order_id.id,
            'product_id': new_record.product_id.id,
            'name': new_record.name,
            'product_uom_qty': new_record.quantity,
            'product_uom': new_record.uom_id.id,
            'price_unit': new_record.price,
            'price_subtotal': new_record.total,
        }

        # Create the sale.order.line record
        self.env['sale.order.line'].create(sale_order_line_vals)

        return new_record

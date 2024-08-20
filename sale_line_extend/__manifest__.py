
# -*- coding: utf-8 -*-
{
    'name': "Sale Line Extend",

    'summary': "Count the total price based on the price * quantity, if the product_id is changed than uom_id,name,price is also be changed"
               "if in sale line new a new line is created than by default a new line created on sale.order.line.",

    'description': """
In this model i have maded a 2 new model in which i have maded a 2 new page in sale.order,
and in purchase.order this 2 model i have inherited. I want to calculate the total = price * quantity.
if the i changed the product_id than the uom_id,name, price all be changed when the product_id is 
changed. 
In this when new line is added into the sale order line new than by  default the new line is 
also added into the sale.order.line
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'account', 'sale', 'purchase', 'stock', 'product'],

    # always loaded
    'data': [

        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',


    ],
    'installable': True,
    'application': True,
}

# -*- coding: utf-8 -*-

# Copyright © 2025 Jony Ghosh
{
    'name': "Product minimum order qty",

    'summary': """
        Set minimum order quantity for products in Odoo.
        """,

    'description': """
        This module allows you to set a minimum order quantity for products in Odoo.
        This is useful for businesses that want to ensure that customers order a minimum quantity of a product before they can proceed with the order.
        The minimum order quantity can be set on the product form view and will be enforced during the sales order process from website.
    """,

    'author': "Jony Ghosh",
    'maintainer': 'Jony Ghosh',
    'license': 'OPL-1',


    'category': 'Tools/Tools',
    'version': '18.0.0.1',

    "images": [
        "static/description/icon.png",
    ],
    
    'depends': ['base','sale_management','product', 'website_sale'],

    
    'data': [
        "views/product_view.xml",
        "views/web_product_view.xml",
    ],
    
    'demo': [],
    'sequence':-133,
    'price': 8.00,
    'currency':'EUR',
    'application': True,
    'installable': True,
    'auto_install': False,
}
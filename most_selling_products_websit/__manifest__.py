# -*- coding: utf-8 -*-
{
    'name': "Most Selling Products",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dino Varghese",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'website', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/add_to_template_product.xml',
        'views/badge_to_shop.xml',
        'views/templates.xml',
        'data/demo_add_pricelist.xml'

    ],
    'qweb': [],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

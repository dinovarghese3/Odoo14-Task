# -*- coding: utf-8 -*-
{
    'name': "Product Brand",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dino Varghese",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_brand_inherit_view.xml',
        'views/product_brand_js_view.xml',

    ],
    # only loaded in demonstration mode
    'qweb':['static/src/xml/pos_product_brand.xml',],
    'auto_install': True,
}

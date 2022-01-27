# -*- coding: utf-8 -*-
{
    'name': "The Flower App Solution",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Odoo PS",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'website_sale', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv', # no longer needed
        'data/ir_actions_server.xml',
        'views/view_my_awesome_model_form.xml',
        'views/view_production_lot_form.xml',
        'views/view_flower_watering.xml',
        'views/templates.xml'
    ],

    'app': True
}

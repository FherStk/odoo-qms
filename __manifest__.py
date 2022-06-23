# -*- coding: utf-8 -*-
{
    'name': "QMS",

    'summary': """
        QMS: Quality Management System
        SGQ: Sistema de Gestió de la Qualitat
    """,

    'description': """
        QMS: Quality Management System
        SGQ: Sistema de Gestió de la Qualitat
    """,

    'author': "Fernando Porrino Serrano",
    'website': "https://github.com/fherstk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}

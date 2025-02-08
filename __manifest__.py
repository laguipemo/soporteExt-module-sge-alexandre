# -*- coding: utf-8 -*-
{
    'name': "soporteExt",

    'summary': """
        Módulo de soporte extendido para la gestión de incidencias """,

    'description': """
        Descripción del módulo de soporte para la gestión de incidencias. Extensión para técnicos.
    """,

    'author': "Lázaro Guillermo Pérez Montoto -LGPM developments-",
    'website': "https://github.com/laguipemo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'soporte'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/incidencia.xml',
        'views/tecnico.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

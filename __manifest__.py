# -*- coding: utf-8 -*-
{
    'name': "Books",

    'summary': """
        Catalog and categorize all your books: 
        Writers, editors, genres and more""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Alexis Adam",
    'website': "http://www.github.com/degasjr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'sequence': 1,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/book_data.xml',
        # 'security/ir.model.access.csv',
        'views/artist_views.xml',
        'views/book_views.xml',
    ],
    
    'auto_install': False,
    'application': True,
    
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}

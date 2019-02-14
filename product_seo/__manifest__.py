# -*- coding: utf-8 -*-
{
    'name': "Product SEO",

    'summary': """
        This module add new Custom Link for Product for having a good SEO """,

    'description': """
        Adding new Custm Link for Product 
    """,

    'author': 'Fogits Solutions',
    'website': "https://www.fogits.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0',
    'images': ['static/description/banner.jpg'],
    # any module necessary for this one to work correctly
    'depends': ['base','product','website_sale'],

    # always loaded
    'data': [
        'views/ref_product.xml',
        'views/products.xml',
    ],

}
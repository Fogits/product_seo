# -*- coding: utf-8 -*-
{
    'name': "Product SEO",

    'summary': """
       You will be able to create a new link for your product(s). You only need to add a SEO name for the product that you want to change its link. """,

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
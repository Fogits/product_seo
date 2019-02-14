# -*- coding: utf-8 -*-
{
    'name': "Product SEO",

    'summary': """
        This module add new Custom Link for Product for having a good SEO """,

    'description': """
        Adding new Custm Link for Product 
    """,

    'author': "Fogits International",
    'website': "https://www.fogits.com/",
    'category': 'Uncategorized',
    'version': '11.0',
    'images': ['static/description/banner.png'],
    # any module necessary for this one to work correctly
    'depends': ['base','product','website_sale'],

    # always loaded
    'data': [
        'views/ref_product.xml',
        'views/products.xml',
    ],

}
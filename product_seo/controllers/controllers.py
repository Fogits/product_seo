# -*- coding: utf-8 -*-
from odoo.http import Controller, request
from odoo import http, tools
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website.controllers.main import QueryURL
from odoo import api, fields


class WebsiteSaleExtend(WebsiteSale):
    @http.route(['/shop/product/<model("product.template"):product>', '/shop/product/<string:test>'], type='http',
                auth="public", website=True)
    def product(self, product='', ref_product='', category='', search='', **kwargs):

        if ref_product:
            product = request.env['product.template'].search([('ref_product', '=', ref_product)])

        product_context = dict(request.env.context,
                               active_id=product.id,
                               partner=request.env.user.partner_id)
        ProductCategory = request.env['product.public.category']

        if category:
            category = ProductCategory.browse(int(category)).exists()

        attrib_list = request.httprequest.args.getlist('attrib')
        attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
        attrib_set = {v[1] for v in attrib_values}

        keep = QueryURL('/shop', category=category and category.id, search=search, attrib=attrib_list)

        categs = ProductCategory.search([('parent_id', '=', False)])

        pricelist = request.website.get_current_pricelist()

        from_currency = request.env.user.company_id.currency_id
        to_currency = pricelist.currency_id
        compute_currency = lambda price: from_currency._convert(price, to_currency, request.env.user.company_id,
                                                                fields.Date.today())

        if not product_context.get('pricelist'):
            product_context['pricelist'] = pricelist.id
            product = product.with_context(product_context)

        values = {
            'search': search,
            'category': category,
            'pricelist': pricelist,
            'attrib_values': attrib_values,
            'compute_currency': compute_currency,
            'attrib_set': attrib_set,
            'keep': keep,
            'categories': categs,
            'main_object': product,
            'product': product,
            'optional_product_ids': [p.with_context({'active_id': p.id}) for p in product.optional_product_ids],
            'get_attribute_exclusions': self._get_attribute_exclusions,
        }
        return request.render("website_sale.product", values)

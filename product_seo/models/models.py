# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateExtend(models.Model):
    _inherit = 'product.template'

    ref_product=fields.Char(string='Ref Product')

    _sql_constraints = [
        ('Reference product', 'unique(ref_product)', 'Reference Product already exists!')]

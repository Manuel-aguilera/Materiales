# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Manuel Aguilera Magaña


class Products(models.Model):
    _name = 'materiales.products'
    field_bool = fields.Boolean("Campo tipo boolean")
    field_int = fields.Integer("Campo tipo Integer")
    field_float = fields.Float("Campo tipo flotante")
    field_select = fields.Selection(
        [('a', 'A'), ('b', 'B')], "Campo tipo selection")
    field_date = fields.Date('Campo tipo Date')
    name = fields.Char("Producto Nombre")
    field_text = fields.Text("Campo tipo texto")
    field_HTML = fields.Html("Campo tipo HMTL")


# field_many2one = fields.Many2one(
#     'product.template', 'Campo Many2one')

# field_one2many = fields.One2many(
#     'materiales.products', 'field_many2one', 'Campo One2many')

# field_many2many = fields.Many2many(
#     'sale.order', string='Campo Many2Many')

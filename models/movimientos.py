# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Manuel Aguilera Magaña


class Movimientos(models.Model):
    _name = 'materiales.movimientos'
    check = fields.Boolean("Checar")


# field_many2one = fields.Many2one(
#     'product.template', 'Campo Many2one')

# field_one2many = fields.One2many(
#     'materiales.products', 'field_many2one', 'Campo One2many')

# field_many2many = fields.Many2many(
#     'sale.order', string='Campo Many2Many')

# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Inventario(models.Model):
    _name = "materiales.inventario"
    producto_id = fields.Many2one(
        'materiales.productos', 'Producto', required=True)
    cantidad = fields.Integer("Cantidad")

# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Manuel Aguilera Magaña


class Movimientos(models.Model):
    _name = 'materiales.movimientos'
    clave_mov = fields.Integer("Clave movimiento", required="True")
    producto_id = fields.Many2one(
        'materiales.productos', 'Producto', required=True)
    # producto_id = fields.One2many(
    #     'materiales.productos', 'producto', 'Producto')
    # departamento = fields.Integer("Departamento", required="True")
    departamento_id = fields.Many2one(
        'materiales.departamentos', 'Departamento', required=True)
    fecha_entrada = fields.Date("Fecha entrada", required="True")
    fecha_salida = fields.Date("Fecha salida", required="True")

# field_many2many = fields.Many2many(
#     'sale.order', string='Campo Many2Many')

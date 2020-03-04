# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Productos(models.Model):
    _name = 'materiales.productos'
    serie = fields.Integer("No Serie", required=True)
    name = fields.Char("Producto", required=True)
    fecha_adquisicion = fields.Date("Fecha compra", required=True)
    # departamento = fields.Selection(
    #     [('a', 'A'), ('b', 'B')], "Campo tipo selection")
    departamento = fields.Char("Departamento", required=True)
    costo = fields.Float('Costo', required=True)
    descripcion = fields.Text("Descripción")


# field_many2one = fields.Many2one(
#     'product.template', 'Campo Many2one')

# field_one2many = fields.One2many(
#     'materiales.products', 'field_many2one', 'Campo One2many')

# field_many2many = fields.Many2many(
#     'sale.order', string='Campo Many2Many')
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Productos(models.Model):
    _name = 'materiales.productos'
    foto = fields.Binary("Imagen")
    # serie = fields.Integer("No Serie", required=True)
    serie_id = fields.Many2one("materiales.series", "Serie")
    name = fields.Char("Producto", required=True)
    # fecha_adquisicion = fields.Date("Fecha compra", required=True)
    # departamento = fields.Selection(
    #     [('a', 'A'), ('b', 'B')], "Campo tipo selection")
    costo = fields.Float('Costo', required=True)
    descripcion = fields.Text("Descripción")
    cantidad = fields.Integer("Cantidad")
    # num_series_ids = fields.One2many(
    #     "materiales.series", serie_id, "No. Series")


# field_many2one = fields.Many2one(
#     'product.template', 'Campo Many2one')

# field_one2many = fields.One2many(
#     'materiales.products', 'field_many2one', 'Campo One2many')

# field_many2many = fields.Many2many(
#     'sale.order', string='Campo Many2Many')

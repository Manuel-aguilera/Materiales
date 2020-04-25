# -*- coding: utf-8 -*-
from odoo import fields, models, api, exceptions
from datetime import datetime


class Series(models.Model):
    _name = "materiales.series"
    name = fields.Char(string="Número de serie")
    producto_id = fields.Many2one('materiales.productos', string="Producto")
    ubicacion = fields.Many2one('materiales.ubicaciones', string="Ubicación")
    status = fields.Selection(
        [('NUEVO', 'NUEVO'), ('SEMINUEVO', 'SEMINUEVO'), ('USADO', 'USADO')], string="Status")
    vida_util = origen_recurso = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
         ('8', '8'), ('9', '9'), ('10', '10')], string="Años de vida útil")

    # @api.model
    # def create(self, vals):
    #     serie = self.env['ir.sequence'].next_by_code('series.productos')
    #     if not serie:
    #         raise exceptions.except_orm(
    #             'Error', 'Defina el número de serie')
    #     vals['name'] = serie
    #     if not vals.get('fecha'):
    #         vals['fecha'] = datetime.now()

    #     return super(serie, self).create(vals)

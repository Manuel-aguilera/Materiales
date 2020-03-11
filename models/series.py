# -*- coding: utf-8 -*-
from odoo import fields, models, api, exceptions
from datetime import datetime


class Series(models.Model):
    _name = "materiales.series"
    name = fields.Char("Número de serie")
    # num_serie = fields.Integer("Número de serie")
    # producto = fields.Many2one('materiales.productos', "Producto")
    caducidad = fields.Date("Caducidad")

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

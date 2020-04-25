# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Departamentos(models.Model):
    _name = "materiales.departamentos"
    clave_departamento = fields.Char(
        string="Clave departamento", required=True)
    name = fields.Char(string="Departamento", required=True)
    encargado = fields.Char(string="Encargado", required=True)
    ubicaciones_ids = fields.One2many(
        'materiales.ubicaciones', "departamento_id", string="Ubicaciones")


# class Detalle_departamentos(models.Model):
#     _name = "materiales.detalle_departamentos"
#     _rec_name = "departamento_id"
#     departamento_id = fields.Char(string="Departamento")
#     ubicacion = fields.Many2one("materiales.ubicaciones", string="Ubicación")
#     descripcion = fields.Char(
#         compute="_obtener_descripcion", string="Descripción", readonly=True)

#     @api.onchange("ubicacion")
#     def _obtener_descripcion(self):
#         for r in self:
#             r.descripcion = r.ubicacion.descripcion

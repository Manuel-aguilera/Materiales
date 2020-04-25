# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Ubicaciones(models.Model):
    _name = "materiales.ubicaciones"
    departamento_id = fields.Char(string="Departamento")
    name = fields.Char(string="Ubicación", required=True,
                       placeholder="Nombre ubicación")
    descripcion = fields.Char(string="Descripción", required=True)
    es_almacen = fields.Boolean(string="¿Es almacén?")

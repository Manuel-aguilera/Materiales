# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Departamentos(models.Model):
    _name = "materiales.departamentos"
    clave_depto = fields.Integer("Clave departamento", required=True)
    name = fields.Char("Departamento", required=True)
    encargado = fields.Char("Encargado", required=True)

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Departamentos(models.Model):
    _name = "materiales.departamentos"
    clave_depto = fields.Integer("Clave departamento")
    encargado = fields.Char("Encargado")

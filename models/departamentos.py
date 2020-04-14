# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Departamentos(models.Model):
    _name = "materiales.departamentos"
    name = fields.Char("Departamento", required=True)

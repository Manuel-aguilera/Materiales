# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Inventarios(models.Model):
    _name = "materiales.inventarios"
    name = fields.Char("Inventario", required=True)

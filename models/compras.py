# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Compras(models.Model):
    _name = "materiales.compras"
    name = fields.Char("Compra",  required=True)

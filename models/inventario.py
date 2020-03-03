# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Inventario(models.Model):
    _name = "materiales.inventario"
    check = fields.Boolean("Checar")

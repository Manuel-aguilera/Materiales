# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Movimientos(models.Model):
    _name = "materiales.movimientos"
    name = fields.Char("Movimiento", required=True)

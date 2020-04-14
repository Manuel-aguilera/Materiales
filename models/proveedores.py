# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Proveedores(models.Model):
    _name = "materiales.proveedores"
    name = fields.Char("Proveedor", required=True)

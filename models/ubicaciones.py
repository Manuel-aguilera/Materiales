# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Ubicaciones(models.Model):
    _name = "materiales.ubicaciones"
    name = "Ubicacion"
    descripcion = "Descripcion"

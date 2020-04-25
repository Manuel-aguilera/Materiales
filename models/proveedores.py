# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Proveedores(models.Model):
    _name = "materiales.proveedores"
    foto = fields.Binary("Imagen")
    name = fields.Char(string="Nombre", required=True)
    celular = fields.Char(string="Celular")
    correo = fields.Char(string="Correo")
    pais = fields.Char(string="Pais")
    estado = fields.Char(string="Estado")
    poblacion = fields.Char(string="Poblacion")

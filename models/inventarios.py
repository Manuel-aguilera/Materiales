# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Inventarios(models.Model):
    _name = "materiales.inventarios"
    name = fields.Char(string="Clave", readonly=True,
                       required=True, copy=False, default='New')
    producto = fields.Many2one(
        "materiales.productos", string="Producto")
    modelo = fields.Char(string="Modelo")
    serie = fields.Many2one("materiales.series", string="No. serie")
    descripcion = fields.Text(string="Descripción")
    departamento = fields.Many2one(
        "materiales.departamentos", string="Departamento")
    ubicacion = fields.Many2one(
        "materiales.ubicaciones", string="Ubicación")
    status = fields.Selection(
        [('NUEVO', 'NUEVO'), ('SEMINUEVO', 'SEMINUEVO'), ('USADO', 'USADO')], string="Status")
    vida_util = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
         ('8', '8'), ('9', '9'), ('10', '10')], string="Años de vida útil")
    presupuesto_estado = fields.Boolean(
        string="Presupuesto estado")
    origen_recurso = fields.Selection(
        [('PROPIO', 'PROPIO'), ('ESTADO', 'ESTADO'), ('FEDERAL', 'FEDERAL')], string="Origen Recurso")
    lugar_compra = fields.Char(string="Lugar de compra")
    proveedor = fields.Many2one(
        "materiales.proveedores", string="Proveedor")
    fecha_compra = fields.Date(string="Fecha de compra")
    costo = fields.Float(string="Precio compra")
    valoracion = fields.Float(string="Valor actual estimado")

    # @api.depends("producto")
    # def _ubicacion(self):
    #     for r in self:
    #         r.ubicacion = r.producto.series_ids.ubicacion

    @api.model
    def create(self, vals):
        # Para el numero de folio
        if vals.get('name', 'New') == 'New':
            codigo = self.env['ir.sequence'].next_by_code(
                'inventarios.servicio') or 'New'
            vals['name'] = codigo
        result = super(Inventarios, self).create(vals)
        return result

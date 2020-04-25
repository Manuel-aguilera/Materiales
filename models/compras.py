# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Compras(models.Model):
    _name = "materiales.compras"
    name = fields.Char(string="Número de compra", readonly=True,
                       required=True, copy=False, default='New')
    proveedor = fields.Many2one("materiales.proveedores", string="Proveedor")
    fecha_compra = fields.Date(string="Fecha de compra")
    total_compras = fields.Integer(
        compute="_total_compras", string="Total de compras", readonly=True)
    total_pagado = fields.Integer(
        compute="_total_monto", string="Total pagado", readonly=True)
    productos_ids = fields.One2many(
        "materiales.detalle_productos", "compra_id", string="Detalle productos")

    @api.multi
    def unlink(self):
        for producto in self.productos_ids:
            producto.unlink()
        return super(Compras, self).unlink()

    @api.multi
    def eliminar(self):  # borro todo lo que he creado por wey de una clase  jajaja
        borrar = self.env["materiales.detalle_productos"]
        quieroBorrar = borrar.search([])
        for b in quieroBorrar:
            b.unlink()

    @api.depends("productos_ids.cantidad")
    def _total_compras(self):
        for r in self:
            total = 0
            for p in r.productos_ids:
                total += p.cantidad
            r.total_compras = total

    @api.depends("productos_ids.total")
    def _total_monto(self):
        for r in self:
            total = 0
            for p in r.productos_ids:
                total += p.total
            r.total_pagado = total

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            codigo = self.env['ir.sequence'].next_by_code(
                'compra.servicio') or 'New'
            vals['name'] = codigo
        result = super(Compras, self).create(vals)
        return result

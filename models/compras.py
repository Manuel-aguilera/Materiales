# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Compras(models.Model):
    _name = "materiales.compras"
    name = fields.Char(string="Número de compra", readonly=True,
                       required=True, copy=False, default='New')
    proveedor = fields.Many2one("materiales.proveedores", string="Proveedor")
    fecha_compra = fields.Date(string="Fecha de compra")
    prueba = fields.Char(string="Valor")
    total_compras = fields.Integer(
        compute="_total_compras", string="Total de compras", readonly=True)
    total_pagado = fields.Integer(
        compute="_total_monto", string="Total pagado", readonly=True)
    productos_ids = fields.One2many(
        "materiales.detalle_productos", "compra_id", string="Detalle productos")

    @api.model
    def create(self, vals):
        # Para asignar proveedor, fecha y lugar de compra a inventarios
        inventarios = self.env["materiales.inventarios"]
        proveedores = self.env["materiales.proveedores"]
        p_ids = vals["productos_ids"]
        for dic in p_ids:
            inv = inventarios.search(
                [('producto', '=', dic[2].get("producto"))])
            proveedor = proveedores.browse(vals["proveedor"])
            lugar_compra = proveedor.poblacion + ", " + \
                proveedor.estado + ", " + proveedor.pais
            inv.write({"proveedor": vals["proveedor"],
                       "fecha_compra": vals["fecha_compra"],
                       "lugar_compra": lugar_compra})

        # Para el folio
        if vals.get('name', 'New') == 'New':
            codigo = self.env['ir.sequence'].next_by_code(
                'compra.servicio') or 'New'
            vals['name'] = codigo
        result = super(Compras, self).create(vals)
        return result

    # @api.multi
    # def write(self, vals):
        # inventarios = self.env["materiales.inventarios"]
        # proveedores = self.env["materiales.proveedores"]
        # productos = self.env["materiales.productos"]
        # prod_old = self.productos_ids
        # for dic in prod_old:
        #     prod = productos.browse(dic[2].get("producto")) #producto anterior
        #     inv = inventarios.search([("producto", "=", prod.name)], limit=1)
        # return super(Compras, self).write(vals)

    @api.multi
    def unlink(self):
        for r in self:
            for fila in r.productos_ids:
                fila.unlink()
        return super(Compras, self).unlink()

    @api.multi
    def eliminar(self):  # borro todo lo que he creado por wey de una clase  jajaja
        borrar = self.env["materiales.detalle_productos"]
        quieroBorrar = borrar.search([])
        prod_borrar = []
        for b in quieroBorrar:
            prod_borrar.append(b.producto)
            b.unlink()
        for p in prod_borrar:
            p.unlink()

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

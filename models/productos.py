# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Productos(models.Model):
    _name = 'materiales.productos'
    foto = fields.Binary(string="Imagen")
    name = fields.Char(string="Producto", required=True)
    modelo = fields.Char(string="Modelo")
    origen_recurso = fields.Selection(
        [('PROPIO', 'PROPIO'), ('ESTADO', 'ESTADO'), ('FEDERAL', 'FEDERAL')], string="Origen Recurso", required=True)
    presupuesto_estado = fields.Boolean(string="Presupuesto estado")
    cantidad = fields.Integer(compute="_cantidad",
                              string="Cantidad", readonly=True)
    costo = fields.Float(string="Costo c/u", required=True)
    descripcion = fields.Text(string="Descripción")
    series_ids = fields.One2many(
        "materiales.series", "producto_id", string="Series")
    cantidad_disponible = fields.Integer(compute="_cantidad_disponible",
                                         string="Cantidad disponible", readonly=True)

    @api.model
    def create(self, vals):
        productos = self.env['materiales.productos']
        inventarios = self.env['materiales.inventarios']
        det_prod = self.env['materiales.detalle_productos']
        valores_inv = {}
        # valores_inv["modelo"] = vals["modelo"]
        valores_inv["descripcion"] = vals["descripcion"]
        valores_inv["origen_recurso"] = vals["origen_recurso"]
        valores_inv["presupuesto_estado"] = vals["presupuesto_estado"]
        valores_inv["costo"] = vals["costo"]
        valores_inv["valoracion"] = vals["costo"]
        # obtenemos el numero de productos para por cada uno crear un registro en inventarios
        # series_producto = productos.browse(vals["series_ids"])
        valores_inv["modelo"] = vals["series_ids"]

        # n = len(series_producto)
        # for r in series_producto:  # para cada serie creamos un fila en inventarios
        #     valores = valores_inv.copy()
        #     valores["producto"] = r.producto_id
        #     valores["departamento"] = r.ubicacion.departamento_id
        #     valores["ubicacion"] = r.ubicacion
        #     valores["status"] = r.status
        #     valores["vida_util"] = r.vida_util
        #     # Ahora comprobamos si fue una compra, si es así asignamos  lugar de proveedor y fecha
        #     compra_producto = det_prod.browse(r.producto_id)
        #     if(compra_producto):
        #         valores["proveedor"] = compra_producto.compra_id.proveedor
        #         valores["fecha_compra"] = compra_producto.compra_id.fecha_compra
        #         valores["lugar_compra"] = compra_producto.compra_id.proveedor.poblacion.string + \
        #             ", " + compra_producto.compra_id.proveedor.estado.string + \
        #             ", " + compra_producto.compra_id.proveedor.pais.string
        inventarios.create([valores_inv])

        result = super(Productos, self).create(vals)
        return result

    @api.depends("series_ids")
    def _cantidad(self):
        for r in self:
            r.cantidad = len(r.series_ids)

    @api.depends("series_ids.ubicacion")
    def _cantidad_disponible(self):
        for r in self:
            c = 0
            for p in r.series_ids:
                if (p.ubicacion.es_almacen == True):
                    c += 1
            r.cantidad_disponible = c


class DetalleProductos(models.Model):
    _name = 'materiales.detalle_productos'
    producto = fields.Many2one(
        "materiales.productos", string="Producto", required="True")
    compra_id = fields.Many2one("materiales.compras", string="Compra")
    cantidad = fields.Integer(
        related="producto.cantidad", string="Cantidad", readonly=True)
    costo = fields.Float(related="producto.costo",
                         string="Costo", readonly=True)
    total = fields.Float(compute="_calcular_total",
                         string="Total", readonly=True)  # no veo necesario almacenarlo en la DB

    @api.depends("producto.cantidad", "producto.costo")
    def _calcular_total(self):
        for r in self:
            r.total = r.cantidad * r.costo

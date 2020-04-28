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
        inventarios = self.env['materiales.inventarios']
        ubicaciones = self.env["materiales.ubicaciones"]
        series = self.env["materiales.series"]
        valores_inv = {}
        # valores_inv["producto"] = vals["name"]
        valores_inv["modelo"] = vals["modelo"]
        valores_inv["descripcion"] = vals["descripcion"]
        valores_inv["origen_recurso"] = vals["origen_recurso"]
        valores_inv["presupuesto_estado"] = vals["presupuesto_estado"]
        valores_inv["costo"] = vals["costo"]
        valores_inv["valoracion"] = vals["costo"]
        # obtenemos el numero de productos para por cada uno crear un registro en inventarios
        series_producto = vals["series_ids"]
        invent_ids = []  # para cada producto guardamos el id del inventario
        for dic in series_producto:  # para cada serie creamos un fila en inventarios
            valores = valores_inv.copy()
            ubic_ic = dic[2].get("ubicacion")
            valores["ubicacion"] = ubic_ic
            ubi = ubicaciones.browse(ubic_ic)
            valores["departamento"] = ubi.departamento_id
            valores["status"] = dic[2].get("status")
            valores["vida_util"] = dic[2].get("vida_util")
            invent_ids.append(inventarios.create([valores]).id)
        result = super(Productos, self).create(vals)
        # Asignamos a inventarios el id_producto e id_serie
        for inv in invent_ids:
            inventarios.browse(inv).write({"producto": result.id})
        i = 0
        for serie in result.series_ids:
            inventarios.browse(invent_ids[i]).write({"serie": serie.id})
            i += 1
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
        # eliminamos la compra relacionada al producto
        det_prod = self.env["materiales.detalle_productos"]
        inventarios = self.env["materiales.inventarios"]
        for r in self:  # obtenemos el producto
            det_prod_borrar = det_prod.search([('producto', '=', r.id)])
            det_prod_borrar.compra_id.unlink()
        # eliminamos las filas en inventarios relacionadas al producto
            inv_borrar = inventarios.search([('producto', '=', r.id)])
            for inv in inv_borrar:
                inv.unlink()
        return super(Productos, self).unlink()

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

    @api.multi
    def unlink(self):
        # compras = self.env["materiales.compras"]
        # prod_borrar = []
        # for r in self:
        # r.compra_id.write({"prueba": r.id})
        #     prod_borrar.append(r.producto)
        result = super(DetalleProductos, self).unlink()
        # for p in prod_borrar:
        #     p.unlink()
        return result

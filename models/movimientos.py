# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Movimientos(models.Model):
    _name = "materiales.movimientos"
    name = fields.Char(string="Clave movimiento", readonly=True,
                       required=True, copy=False, default='New')
    tipo = fields.Selection(
        [("RECEPCION", "RECEPCION"), ("TRANSFERENCIA", "TRANSFERENCIA"), ("DEVOLUCION", "DEVOLUCION"), ("SALIDA", "SALIDA")], string="Tipo", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    movimientos_ids = fields.One2many(
        "materiales.detalle_movimientos", "movimiento_id", string="Detalle movimientos")

    @api.multi
    def eliminar(self):  # borro todo lo que he creado por wey de una clase  jajaja
        borrar = self.env["materiales.detalle_movimientos"]
        quieroBorrar = borrar.search([])
        for b in quieroBorrar:
            b.unlink()

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            codigo = self.env['ir.sequence'].next_by_code(
                'movimiento.servicio') or 'New'
            vals['name'] = codigo
        result = super(Movimientos, self).create(vals)
        return result


class Detalle_movimientos(models.Model):
    _name = "materiales.detalle_movimientos"
    movimiento_id = fields.Many2one(
        "materiales.movimientos", string="Movimiento")
    producto = fields.Many2one(
        "materiales.productos", string="Producto", required=True)
    series = fields.Many2one("materiales.series", string="Número de serie")
    cantidad = fields.Integer(string="Cantidad", default="1", readonly=True)
    # ubicacion_actual = fields.Many2one(
    #     "materiales.ubicaciones", related="series.ubicacion", string="Ubicación actual")
    ubicacion_texto = fields.Char(string="Ubicacion", readonly=True)
    ubicacion_destino = fields.Many2one(
        "materiales.ubicaciones", string="Ubicación destino")

    @api.model
    def create(self, vals):
        serie = vals['series']
        ubic = vals['ubicacion_destino']
        m = self.env['materiales.series']
        # hay que crear claves unicas para evitar que en la busqueda salga más de un numero de serie
        # recuerda que search no aplica con claves, pero browse y create si
        n_id = m.browse([serie])
        # antes de sobreescribir la ubicacion, extraemos la actual y la guardamos
        vals['ubicacion_texto'] = n_id.ubicacion.name
        if n_id:
            n_id.write({'ubicacion': ubic})
        result = super(Detalle_movimientos, self).create(vals)
        return result

    @api.onchange("producto")
    def _obtener_series(self):  # obtenemos series de acuerdo al producto seleccionado
        self.series = None
        return {'domain': {'series': [('producto_id', '=', self.producto.name)]}}

    @api.onchange("series")
    def _limpiar_cantidad(self):  # obtenemos series de acuerdo al producto seleccionado
        ubicacion_actual = self.series.ubicacion.name
        if (self.series):
            self.cantidad = 1
            self.ubicacion_texto = ubicacion_actual
        # 0 - Recepcion; 1 - Transferencia; 2 - Devolucion; 3 - Salida
        dominios = [('es_almacen', '=', True),
                    ('name', '!=', ubicacion_actual),
                    ('es_almacen', '=', False)]
        if (self.movimiento_id.tipo == "RECEPCION"):
            return {'domain': {'ubicacion_destino': [dominios[0]]}}
        elif (self.movimiento_id.tipo == "TRANSFERENCIA"):
            return {'domain': {'ubicacion_destino': [dominios[1]]}}
        elif (self.movimiento_id.tipo == "DEVOLUCION"):
            return {'domain': {'ubicacion_destino': [dominios[0]]}}
        elif (self.movimiento_id.tipo == "SALIDA"):
            return {'domain': {'ubicacion_destino': [dominios[2], dominios[1]]}}

    # @api.onchange("producto")
    # def _dominio_ubicacion(self):

    @api.onchange("cantidad")
    def _limpiar_serie(self):  # obtenemos series de acuerdo al producto seleccionado
        if (self.cantidad <= 0):
            raise exceptions.except_orm(
                'Error', 'La cantidad debe ser mayor a cero')
        elif (self.cantidad > 1):
            self.series = None

    class Selection(models.Model):
        _name = "materiales.selection"
        name = fields.Char(string="Campo", required=True)

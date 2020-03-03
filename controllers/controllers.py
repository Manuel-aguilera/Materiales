# -*- coding: utf-8 -*-
from odoo import http


# class Materiales(http.Controller):
#     @http.route('/materiales/', auth='public', website=True)
#     def index(self, **kw):
#         return http.request.render('materiales.index', {})

# #     @http.route('/materiales/materiales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('materiales.listing', {
#             'root': '/materiales/materiales',
#             'objects': http.request.env['materiales.materiales'].search([]),
#         })

#     @http.route('/materiales/materiales/objects/<model("materiales.materiales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('materiales.object', {
#             'object': obj
#         })

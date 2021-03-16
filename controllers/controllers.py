# -*- coding: utf-8 -*-
# from odoo import http


# class IutDevice(http.Controller):
#     @http.route('/iut_device/iut_device/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iut_device/iut_device/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iut_device.listing', {
#             'root': '/iut_device/iut_device',
#             'objects': http.request.env['iut_device.iut_device'].search([]),
#         })

#     @http.route('/iut_device/iut_device/objects/<model("iut_device.iut_device"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iut_device.object', {
#             'object': obj
#         })

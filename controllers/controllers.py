# -*- coding: utf-8 -*-
# from odoo import http


# class Qms(http.Controller):
#     @http.route('/qms/qms', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qms/qms/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qms.listing', {
#             'root': '/qms/qms',
#             'objects': http.request.env['qms.qms'].search([]),
#         })

#     @http.route('/qms/qms/objects/<model("qms.qms"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qms.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class QwebPartner(http.Controller):
#     @http.route('/qweb_partner/qweb_partner', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qweb_partner/qweb_partner/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qweb_partner.listing', {
#             'root': '/qweb_partner/qweb_partner',
#             'objects': http.request.env['qweb_partner.qweb_partner'].search([]),
#         })

#     @http.route('/qweb_partner/qweb_partner/objects/<model("qweb_partner.qweb_partner"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qweb_partner.object', {
#             'object': obj
#         })

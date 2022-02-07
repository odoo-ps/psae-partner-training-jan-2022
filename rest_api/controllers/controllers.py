# -*- coding: utf-8 -*-
from odoo import http, api, SUPERUSER_ID
from odoo.http import request
import json


class RestApi(http.Controller):
    @http.route('/api/v1/product', auth='public', type='json')
    def index(self, **kw):
        cr = request.cr
        env = api.Environment(cr, SUPERUSER_ID, {})
        PRODUCT = env['product.product'].sudo()

        return {
            'GET': self.handle_get,
            'POST': self.handle_post,
            'PUT': self.handle_put,
            'DELETE': self.handle_delete
        }.get(request.httprequest.method, self.passer)(PRODUCT)

    @http.route('/api/v2/<string:model>', auth='public', type='json')
    def index_v2(self, model, **kw):
        cr = request.cr
        env = api.Environment(cr, SUPERUSER_ID, {})
        PRODUCT = env[model].sudo()

        return {
            'GET': self.handle_get,
            'POST': self.handle_post,
            'PUT': self.handle_put,
            'DELETE': self.handle_delete
        }.get(request.httprequest.method, self.passer)(PRODUCT)

    def handle_get(self, model):
        queries = request.httprequest.query_string.decode('utf-8').split('&')
        queries_dict = {}

        for query in queries:
            k, v = query.split('=')
            queries_dict[k] = v

        ids = [int(id) for id in queries_dict['ids'].split(',')]

        return json.dumps(model.browse(ids).read(['name', 'id']))

    def handle_post(self, model):
        record = model.create(request.params)
        return json.dumps(record.read(['name', 'id']))

    def handle_put(self, model):
        record = model.browse(request.params['id'])
        params = dict(request.params)
        del params['id']
        record.write(params)
        return json.dumps(record.read(['name', 'id']))

    def handle_delete(self, model):
        record = model.browse(request.params['id'])
        record.unlink()
        return json.dumps({'delete': 'OK'})

    def passer(self, *args, **kwargs):
        return None



    @http.route('/hello_world', auth='public')
    def hello(self):

        if request.httprequest.method == 'POST':
            greeting = request.params.get('my_input')

            if greeting:
                return request.render('rest_api.hello', {
                    'title': f"Hello, {greeting}!",
                    'odoo': 42
                })

        return request.render('rest_api.hello', {
            'title': "Hello, World!",
            'odoo': 42
        })

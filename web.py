from jinja import Environment, FileSystemLoader
from webob import Request
import os

assets = [
    'app.js',
    'react.js',
    'leaflet.js',
    'D3.js',
    'moment.js',
    'math.js',
    'main.css',
    'bootstrap.css',
    'normalize.css',
    ]
js = []
css = []


def app(environ, start_response):
    response_code = '200 OK'
    response_type = ('Content-Type', 'text/HTML')
    start_response(response_code, [response_type])

    for item in assets:
        itemspl = item.split('.')
        if itemspl[1] == 'js':
            js.append(item)
        elif itemspl[1] == 'css':
            css.append(item)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')
    print(template.render(css0=css, js0=js))

req2 = Request.blank('index.html')
print(req2.get_response(app))

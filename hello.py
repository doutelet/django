import os


def wsgi_app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text-plain')])
    temp = []
    for el in environ.get['QUERY_STRING']:
        temp.append(el)
    return temp

# test

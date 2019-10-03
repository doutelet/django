import os


def wsgi_app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text-plain')])

    response = []
    for el in os.environ['QUERY_STRING']:
        response.append(str(el[0])+'='+str(el[1]))
    return response

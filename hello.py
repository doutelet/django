from os import environ


def wsgi_app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text-plain')])    
    return [(i + '\n') for i in environ['QUERY_STRING'].split('&')]

# test

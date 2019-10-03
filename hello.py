from os import environ


def wsgi_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text-plain')])    
    return "\n".join(environ['QUERY_STRING']).split('&')

# test

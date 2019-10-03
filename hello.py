import os


def wsgi_app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text-plain')])    
    return  "\n".join(os.environ.get('QUERY_STRING')).split("&")

# test

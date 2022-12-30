from server.webserver import *
from pylighting import highlight

@register(route='/',type=MIME_TYPE.HTML)
def main_page(args):
    try:
        qs = args['query_string']
        page = '0'
        if 'page' in qs:
            page = qs['page']
        vars = {'webapp':highlight('content/webapp.py'),
                'config':highlight('content/config.json'),
                'render_template':highlight('content/render_template.py'),
                'page':page}
        return render_page('/content/main.html',vars)
    except Exception as e:
        print(e)

@register(route='/main.css',type=MIME_TYPE.CSS)
def main_css():
    return load_file('/content/main.css')

@post_handler(route='/test',type=MIME_TYPE.TEXT)
def post_test(args):
    print(args)
    return 'lol'

start()

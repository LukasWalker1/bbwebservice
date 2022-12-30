from server.webserver import register, load_file, MIME_TYPE, start

@register(route='/',type=MIME_TYPE.HTML)
def main_page():
    return load_file('/content/index.html')

@register(route='/main.css',type=MIME_TYPE.CSS)
def main_css():
    return load_file('/content/main.css')

start()
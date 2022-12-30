from server.webserver import register, MIME_TYPE, render_page

@register(route='/',type=MIME_TYPE.HTML)
def main_page():
    return render_page('/content/index.html',{'test':'5'})
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    cap1_title="Красная кепка",
    cap1_text="$ 100.00",
    cap2_title="Чёрная кепка",
    cap2_text="$ 120.00",
    cap3_title="Ещё одна чёрная кепка",
    cap3_text="$ 90.00",
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

from jinja2 import Template
# t = Template("Hello {{ something }}!")
# print(t.render(something="World"))
#
# t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
# print(t.render())

import pathlib

html_template = pathlib.Path("email_template.html").read_text(encoding="utf-8")

t = Template(html_template)
print(t.render(name='Bert'))




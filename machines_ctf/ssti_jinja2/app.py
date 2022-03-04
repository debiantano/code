from flask import Flask, render_template_string

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def filtered(template):
  blacklist = ["self.__dict__","url_for","config","getitems","../","process"]

  for b in blacklist:
    if b in template:
      template=template.replace(b,"")
  
  return template


@app.route("/")
def index():
  return "Please find the flags on this site."

@app.route("/<path:template>")
def template(template):
  if len(template) > 500:
    return "too long input"

  while filtered(template) != template:
    template = filtered(template)

  return render_template_string(template)

if __name__ == '__main__':
  app.run()

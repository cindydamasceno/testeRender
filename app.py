from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
  return """E aí, princesas.<br> 
  Vamos testar htmls e renderes?
  """
  


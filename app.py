from flask import flask
app=Flask(__name__)

@app_route('/')
def hello_world():
  return 'Doremon'


if __name__=="__main__":
  app.run()

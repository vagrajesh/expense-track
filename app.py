from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
  return"Hello, Rajesh"

print(__name__)

if __name__ == "__main__":
  print("inside")
  app.run(host='0.0.0.0', debug=True)
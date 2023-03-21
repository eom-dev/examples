from flask import Flask

app = Flask(__name__)

@app.delete("/")
def delete():
	return "delete"

@app.get("/")
def get():
	return "get"

@app.patch("/")
def patch():
	return "patch"

@app.post("/")
def post():
	return "post"

@app.put("/")
def put():
	return "put"

if __name__ == "__main__":
	app.run(
		debug = True,
		host="127.0.0.1",
		port=8080
	)

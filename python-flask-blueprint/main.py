from flask import Flask
from blueprint import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)

if __name__ == "__main__":
	app.run(
			debug = True,
			host = "127.0.0.1",
			port = 8080
		)

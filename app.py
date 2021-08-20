from blueprints.routes import api_route
from blueprints.errorbp import error_bp
from flask import Flask


app = Flask(__name__)
app.register_blueprint(error_bp, url_prefix='/error')
app.register_blueprint(api_route)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host="0.0.0.0", port=5000)

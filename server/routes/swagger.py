
from flask import jsonify, render_template
from server import app

@app.route("/swagger/api")
def swagger_api():
    with open("public/swagger.yaml", "r") as f:
        content = f.read()
    return "<pre>"+content+"</pre>"

@app.route("/explorer")
def explorer():
    return render_template('swagger-ui/index.html')


@app.route("/twin")
def digitaltwin():
    return render_template('swagger-ui/twin.html')

@app.route("/twinbuilding")
def twinbuilding():
    return render_template('swagger-ui/twinbuilding.html')

from flask import Flask, request, jsonify
from data import data
app= Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"success"
    })

@app.route("/stars")
def stars():
    name=request.args.get("name")
    stars_data=next(item for item in data if item["name"]==name)
    return jsonify({
        "data":stars_data,
        "message":"success"
})

if __name__=="__main__":
    app.run()
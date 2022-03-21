from flask import Flask, redirect, render_template, request, jsonify, json
from shortener import short


app = Flask(__name__, template_folder="public")


@app.route("/")
def main():
    if request.args.get('query'):
        query = request.args.get('query')
    else:
        return render_template("index.html")
    results = short(query)
    if results is not None:
        return jsonify(results)
    else:
        return jsonify(
            {"error": "Something wrong"}
        )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

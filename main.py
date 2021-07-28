from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/cryptos/bitcoin")
def bitcoin():
    return render_template("bitcoin.html")


@app.route("/cryptos/dash")
def dash():
    return render_template("dash.html")

@app.route("/cryptos/monero")
def monero():
    return render_template("monero.html")


@app.route("/algorithms/pow")
def pow():
    return render_template("pow.html")


@app.route("/algorithms/pos")
def pos():
    return render_template("pos.html")


@app.route("/transactions")
def transactions():
    return render_template("transactions.html")


if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify, request
app = Flask(__name__)

# [Environment]::SetEnvironmentVariable("FLASK_APP", "server.py");
# py -m flask run

class BodyListBeer:
    def getBody(self):
        body=vars(BodyListBeer(self.beer, self.typeBeer,self.quantity))
        return body
    def __init__(self, b, tB, q):
        self.beer = b
        self.typeBeer = tB
        self.quantity = q

listBeer=[]
listBeer.append(BodyListBeer("Paix Dieux", "triple", 2).getBody())
listBeer.append(BodyListBeer("Chimay", "triple", 1).getBody())

@app.route("/list", methods=["GET"])
def choose_beer():
    beerChoose  = request.args.get('beerChoose', None)
    if beerChoose:
        filtered = [m for m in listBeer if m["beer"]==beerChoose]
        if not filtered:
            return jsonify({"error": "Don't have beer '{0}'".format(beerChoose)}), 400
        else:
            return jsonify(filtered), 200
    else:
        return jsonify(listBeer), 200

@app.route("/addBeer", methods=["POST"])
def add_Beer():
    r = request.get_json()
    for m in listBeer:
        if m["beer"]==r["beer"]:
            quantity = r["quantity"]+m["quantity"]
            listBeer.remove(m)
            listBeer.append(BodyListBeer(m["beer"], m["typeBeer"], quantity).getBody())
            return jsonify({"Add quantity": "Add quantity for this beer : '{0}'".format(r["beer"])}), 200
    listBeer.append(r)
    return jsonify({"Add beer": "Add this beer : '{0}'".format(r["beer"])}), 201

@app.route("/drinkBeer", methods=["POST"])
def drink_Beer():
    r = request.get_json()
    print(r)
    for m in listBeer:
        if m["beer"]==r["beer"]:
            quantity = m["quantity"] - int(r["quantity"])
            if quantity < 0:
                return jsonify({"error": "Don't have enough beer '{0}' in reserve, {1} beer(s) missing ...".format(r["beer"], abs(quantity))}), 400
            else:
                listBeer.remove(m)
                if quantity > 0:
                    listBeer.append(BodyListBeer(m["beer"], m["typeBeer"], quantity).getBody())
                else:
                    return jsonify({"warning": "There will be no more beer '{0}' in reserve after this one !!!".format(r["beer"])}), 401
    return jsonify({"error": "Don't have beer '{0}' in the reserve ....".format(r["beer"])}), 402

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from hotel import HotelFareCal

app = Flask(__name__)
CORS(app)

customers = {}

FOOD_MENU = {
    1: {"name": "Water", "price": 20},
    2: {"name": "Tea", "price": 10},
    3: {"name": "Breakfast", "price": 90},
    4: {"name": "Lunch", "price": 110},
    5: {"name": "Dinner", "price": 150}
}

LAUNDRY_MENU = {
    1: {"name": "Shorts", "price": 3},
    2: {"name": "Trousers", "price": 4},
    3: {"name": "Shirt", "price": 5},
    4: {"name": "Jeans", "price": 6},
    5: {"name": "Girlsuit", "price": 8}
}

GAME_MENU = {
    1: {"name": "Table Tennis", "price": 300},
    2: {"name": "Bowling", "price": 400},
    3: {"name": "Snooker", "price": 400},
    4: {"name": "Video Games", "price": 300},
    5: {"name": "Pool", "price": 250}
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create_customer", methods=["POST"])
def create_customer():
    data = request.json
    customer = HotelFareCal(data["name"], data["address"], data["checkin"], data["checkout"])
    customers[customer.rno] = customer
    return jsonify({"room_no": customer.rno})

@app.route("/book_room", methods=["POST"])
def book_room():
    data = request.json
    cust = customers[data["room_no"]]
    cust.book_room(data["room_type"], data["nights"])
    return jsonify({"message": "Room booked"})

@app.route("/food_menu")
def food_menu():
    return jsonify(FOOD_MENU)

@app.route("/add_food", methods=["POST"])
def add_food():
    data = request.json
    cust = customers[data["room_no"]]
    item = FOOD_MENU[data["item_id"]]
    cust.add_food(item["price"], data["qty"])
    return jsonify({"message": "Food added"})

@app.route("/laundry_menu")
def laundry_menu():
    return jsonify(LAUNDRY_MENU)

@app.route("/add_laundry", methods=["POST"])
def add_laundry():
    data = request.json
    cust = customers[data["room_no"]]
    item = LAUNDRY_MENU[data["item_id"]]
    cust.add_laundry(item["price"], data["qty"])
    return jsonify({"message": "Laundry added"})

@app.route("/game_menu")
def game_menu():
    return jsonify(GAME_MENU)

@app.route("/add_game", methods=["POST"])
def add_game():
    data = request.json
    cust = customers[data["room_no"]]
    item = GAME_MENU[data["item_id"]]
    cust.add_game(item["price"], data["hours"])
    return jsonify({"message": "Game added"})

@app.route("/bill/<int:room_no>")
def bill(room_no):
    cust = customers[room_no]
    return jsonify(cust.generate_bill())

if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, request, jsonify
from models.inventory import inventory
from services.external_api import fetch_product

inventory_bp = Blueprint("inventory", __name__)

# GET ALL
@inventory_bp.route("/inventory", methods=["GET"])
def get_all():
    return jsonify(inventory)

# GET ONE
@inventory_bp.route("/inventory/<int:id>", methods=["GET"])
def get_one(id):
    item = next((i for i in inventory if i["id"] == id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# POST
@inventory_bp.route("/inventory", methods=["POST"])
def add_item():
    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "product_name": data.get("product_name"),
        "brand": data.get("brand"),
        "price": data.get("price"),
        "stock": data.get("stock"),
        "barcode": data.get("barcode")
    }

    api_data = fetch_product(new_item["barcode"])
    if api_data:
        new_item.update(api_data)

    inventory.append(new_item)
    return jsonify(new_item), 201

# PATCH
@inventory_bp.route("/inventory/<int:id>", methods=["PATCH"])
def update_item(id):
    item = next((i for i in inventory if i["id"] == id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json

    item["price"] = data.get("price", item["price"])
    item["stock"] = data.get("stock", item["stock"])

    return jsonify(item)

# DELETE
@inventory_bp.route("/inventory/<int:id>", methods=["DELETE"])
def delete_item(id):
    global inventory
    inventory = [i for i in inventory if i["id"] != id]
    return jsonify({"message": "Deleted"})
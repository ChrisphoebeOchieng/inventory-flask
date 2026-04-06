import requests

def fetch_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == 1:
            product = data["product"]
            return {
                "product_name": product.get("product_name"),
                "brand": product.get("brands"),
                "ingredients": product.get("ingredients_text")
            }
        return None

    except Exception as e:
        return {"error": str(e)}
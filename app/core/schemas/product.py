def productEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "category_id": item["category_id"]
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]

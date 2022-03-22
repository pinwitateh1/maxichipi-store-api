def saleEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "comment": item["comment"],
        "categories": item["categories"],
        "products": item["products"],
        "total": item['total']
    }


def salesEntity(entity) -> list:
    return [saleEntity(item) for item in entity]

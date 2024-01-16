from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    PROGRAMMING = "Programming"
    DEVELOPMENT = "Development"
    DATA_SCIENCE = "Data Science"
    DESIGN = "Design"
    BUSINESS = "Business"


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


items = {
    0: Item(name="Python Basics", price=0.00, count=100, id=0, category=Category.PROGRAMMING),
    1: Item(name="Web Development", price=10.99, count=50, id=1, category=Category.DEVELOPMENT),
    2: Item(name="Machine Learning Fundamentals", price=19.99, count=30, id=2, category=Category.DATA_SCIENCE),
    3: Item(name="Advanced Python Programming", price=29.99, count=20, id=3, category=Category.PROGRAMMING),
    4: Item(name="UI/UX Design Principles", price=15.99, count=25, id=4, category=Category.DESIGN),
    5: Item(name="Business Strategy Fundamentals", price=24.99, count=40, id=5, category=Category.BUSINESS),
}


# FastAPI handles JSON serialization and deserialization for us.
# We can simply use built-in python and Pydantic types, in this case dict[int, Item].
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


# Path parameter equal to :item_id in JavaScript
# We can use the HTTPException to return a (status_code) if there is an error with a message (detail).
@app.get("/items/{item_id}")
# Handle the path parameter type
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


# Function parameters that are not path parameters can be specified as query parameters in the URL
# Here we can query items like this /items?count=20
Selection = dict[
    str, str | int | float | Category | None
]  # dictionary containing the user's query arguments


@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, Selection | list[Item]]:
    def check_item(item: Item):
        """Check if the item matches the query arguments from the outer scope."""
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }


@app.post("/")
def add_item(item: Item) -> dict[str, Item]:

    if item.id in items:
        HTTPException(status_code=400, detail=f"Item with {
                      item.id=} already exists.")

    items[item.id] = item
    return {"added": item}


@app.put("/update/{item_id}")
def update(
    item_id: int,
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
) -> dict[str, Item]:

    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {
                      item_id=} does not exist.")
    if all(info is None for info in (name, price, count)):
        raise HTTPException(
            status_code=400, detail="No parameters provided for update."
        )

    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {"updated": item}


@app.delete("/delete/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:

    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id=} does not exist."
        )

    item = items.pop(item_id)
    return {"deleted": item}

# test_requests.py

import requests

# Test 1: Get all learning items
response_1 = requests.get("http://127.0.0.1:8000/")
print(response_1.json())

# Test 2: Get details of a specific learning item by ID (replace "1" with the desired item_id)
response_2 = requests.get("http://127.0.0.1:8000/items/1")
print(response_2.json())

# Test 3: Query learning items based on category (replace "Design" with the desired category)
response_3 = requests.get("http://127.0.0.1:8000/items?category=Design")
print(response_3.json())

# Test 4: Add a new learning item
new_item = {
    "name": "New Topic",
    "price": 9.99,
    "count": 50,
    "id": 6,
    "category": "New Category"
}
response_4 = requests.post("http://127.0.0.1:8000/", json=new_item)
print(response_4.json())

# Test 5: Update details of a specific learning item by ID
update_data = {
    "name": "Updated Topic",
    "price": 19.99,
    "count": 30
}
response_5 = requests.put("http://127.0.0.1:8000/update/0", json=update_data)
print(response_5.json())

# Test 6: Delete a learning item by ID (replace "2" with the desired item_id)
response_6 = requests.delete("http://127.0.0.1:8000/delete/2")
print(response_6.json())

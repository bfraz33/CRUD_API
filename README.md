# CRUD_API
This project is a simple CRUD API built using FastApi
It's basic demonstration on how to Create, Read, Update and Delete items using the request methods (POST,GET,UPDATE,DELETE)


# FEATURES
POST (create) -> /item/ #creating item:

GET (read) -> /item/{item_id} #retrieving item by item_id:

PUT (update) ->  /item/{item_id} #updating item by item_id:

DELETE -> /item/{item_id} #deleting item by item_id:

This is using a fake database

# REQUIREMENTS
Python 3.8+

Install FastAPI

uvicorn

# INSTALLATION / TESTING

-Clone this repo https://github.com/bfraz33/CRUD_API.git

To test this you can add 2 items.

-In your project folder from the main.py, run "uvicorn main:app --reload" to start your server.

To add items, in powershell run:

ITEM 1:

$item = @{
    name = "Laptop"
    model = "Chromebook"
    price = 400
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/1" -Method POST -Body $item -ContentType "application/json"

ITEM 2:

$item = @{
    name = "Laptop"
    model = "Mac"
    price = 7000
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/2" -Method POST -Body $item -ContentType "application/json"

Using POST this adds the items.

In your IDE, upon starting your server it provided you with this, http://127.0.0.1:8000. In a browser you can paste that http, followed by an endpoint, for example. http://127.0.0.1:8000/items/1. This will return our first item.


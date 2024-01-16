# Tutorial FastAPI API Documentation

## Overview

This FastAPI Tutorial example API allows users to manage educational resources, providing functionality for retrieving, adding, updating, and deleting items related to learning.

## Base URL

`localhost`

## Authentication

No authentication is required

## Routes

| Method | Endpoint                | Description                                      |
|--------|-------------------------|--------------------------------------------------|
| GET    | `/`                     | Get all learning items.                          |
| GET    | `/items/{item_id}`      | Get details of a specific learning item by ID.   |
| GET    | `/items/`               | Query learning items based on various parameters.|
| POST   | `/`                     | Add a new learning item.                         |
| PUT    | `/update/{item_id}`     | Update details of a specific learning item.      |
| DELETE | `/delete/{item_id}`     | Delete a learning item by ID.                    |

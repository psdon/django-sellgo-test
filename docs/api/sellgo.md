## Create customer 

**Request**:

`POST` `/api/v1/customer/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
name       | string | Yes      | Customer name 
email      | string | Yes      | Customer email

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
    "id": 1,
    "name": "me",
    "email": "me@email.com",
    "created_date": "2020-09-30T22:49:10+0000"
}
```

## Create products based on uploaded CSV file

**Request**:

`POST` `/api/v1/csv-product/`

Parameters:

Name        | Type    | Required | Description
------------|---------|----------|------------
customer_id | integer | Yes      | Customer ID 
csv         | file    | Yes      | CSV file upload 

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

[
    {
        "title": "keyboard",
        "price": 9.24,
        "customer_id": 1
    },
    {
        "title": "Monitor",
        "price": 21.9,
        "customer_id": 1
    }
]
```

## Get Customer Latest Products 

**Request**:

`POST` `/api/v1/csv-product/<int:customer_id>`

Parameters:

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

[
    {
        "customer_id": 1,
        "customer_name": "me",
        "product_id": 1,
        "product_title": "keyboard",
        "product_price": "9.24",
        "last_uploaded": "2020-09-30T22:54:55+0000"
    },
    {
        "customer_id": 1,
        "customer_name": "me",
        "product_id": 2,
        "product_title": "Monitor",
        "product_price": "21.90",
        "last_uploaded": "2020-09-30T22:54:55+0000"
    }
]
```


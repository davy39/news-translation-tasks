---
title: Idempotence in HTTP Methods – Explained with CRUD Examples
subtitle: ''
author: Yemi Ojedapo
co_authors: []
series: null
date: '2023-12-22T21:19:43.000Z'
originalURL: https://freecodecamp.org/news/idempotency-in-http-methods
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/pexels-robert-lens-10382808.jpg
tags:
- name: http
  slug: http
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Idempotence refers to a program's ability to maintain a particular result\
  \ even after repeated actions. \nFor example, let's say you have a button that only\
  \ opens a door when pressed. This button does not have the ability to close the\
  \ door, so it stays..."
---

Idempotence refers to a program's ability to maintain a particular result even after repeated actions. 

For example, let's say you have a button that only opens a door when pressed. This button does not have the ability to close the door, so it stays open even when it's pressed repeatedly. It simply remains in the state it was changed to by the first press.

This same logic applies to HTTP methods that are idempotent. Operating on idempotent HTTP methods repeatedly won't have any additional effect beyond the initial execution. 

Understanding idempotence is important for maintaining the consistency of HTTP methods and API design. Idempotence has a significant impact on API design, as it influences how API endpoints should behave when processing requests from clients. 

In this tutorial, I'll explain the concept of idempotence and the role it plays in building robust and functional APIs. You'll also learn about what safe methods are, how they relate to idempotence, and how to implement idempotency in non-idempotent methods. 

## Prerequisites

Before understanding and implementing idempotence in API design, it's essential to have a solid foundation in the following areas:

* RESTful Principles
* Fundamentals of HTTP methods
* API Development 
* HTTP Status codes
* Basics of Web development.

## Idempotence Example  

Let's start off with an example of idempotence in action. We'll create a function that uses the DELETE method to delete data from a web page:

```python

from flask import Flask, jsonify, abort

app = Flask(__name__)

web_page_data = [
   {"id": 1, "content": "Row 1 data"},
   {"id": 2, "content": "Row 2 data"},
   # Add more rows as needed
]

@app.route('/delete_row/<int:row_id>', methods=['DELETE'])
def delete_row(row_id):
   # Find the row to delete
   row_to_delete = next((row for row in web_page_data if row["id"] == row_id), None)
   
   if row_to_delete:
       # Simulate deletion
       web_page_data.remove(row_to_delete)
       return jsonify({"message": f"Row {row_id} deleted successfully."}), 200
   else:
       abort(404, description=f"Row {row_id} not found.")

if __name__ == '__main__':
   app.run(debug=True)

```

This function is expected to delete the rows chosen by the user. Now because of the idempotent nature of the DELETE method, the data will be deleted once, even when called repeatedly. But subsequent calls will return a 404 error since the data has already been deleted by the first call.  

Let’s look at another example with the GET method. The GET method is used to retrieve data from a resource. Let’s create a function that uses the GET method to retrieve a username:

```python
import requests

def get_username():
    url = 'https://api.example.com/get_username'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['username']
        else:
            return None
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Usage
username = get_username()
if username:
    print(f"The username is: {username}")
else:
    print("Failed to retrieve the username.")

```

In this example, we define the `get_username()` function, which sends a GET request to the API endpoint to retrieve the username. If the request is successful, we extract the username from the JSON response and return it. But if any error occurs during the request, we handle it and return `None`.

Now the idempotent nature of the GET method ensures that even if you call `get_username()` multiple times, the same username will be fetched from the API each time. The result will always be the same which is to fetch the username from the resource.

### Idempotent vs. Non-Idempotent HTTP Methods:

HTTP methods play crucial roles in determining how data is fetched, modified, or created when interacting with APIs. And Idempotency is one of the important concepts that influences data consistency and reliability in the methods used . 

Here's a breakdown of the different methods based on their idempotency.

#### Idempotent methods:

* GET
* HEAD
* PUT
* DELETE
* OPTIONS
* TRACE

#### Non-idempotent methods:

* POST
* PATCH
* CONNECT

## Safe Methods

In our previous example, we used the GET method to retrieve a username and this had no side effect on the server. This is because it is a safe method. 

A safe method is a type of method that doesn’t modify the server’s state or the resource being accessed. In other words, they perform read-only operations used to retrieve data or for resource representation.

When you make a request using a safe method, the server does not perform any operations that modify the resource's state. Like in our previous example, we retrieved the username from the webpage which is the resource without changing anything in the server. 

All safe methods are automatically idempotent, but not all idempotent methods are safe. This is because while idempotent methods produce consistent results when called repeatedly, some of them may still modify the server's state or the resource being accessed.

Like in our first example, the DELETE method is idempotent, because deleting a resource multiple times will have the same effect. But it's not safe, as it changes the server's state by removing the resource.

Here’s a classification of HTTP methods based on their safe status:

#### Safe methods:

* GET
* OPTIONS
* HEAD

#### Unsafe methods:

* DELETE
* POST
* PUT
* PATCH

### Why is POST not idempotent?

POST is an HTTP method that sends information to a server. When you make a POST request, you typically submit data to create a new resource or trigger a server-side action. Therefore, making the same request multiple times can result in different outcomes and side effects on the server. This can lead to duplicated data, starting server resources, and reducing performance because of the repeated action.

Unlike idempotent methods like GET, PUT, and DELETE, which have consistent results regardless of repetition, POST requests can cause changes to the server's state with each invocation. 

POST requests often create new resources on the server. Repeating the same POST request will generate multiple identical resources, potentially leading to duplication.

This is similar to DELETE which is an idempotent method but not a safe method. Deleting the last entry in a collection using a single DELETE request would be considered idempotent. But if a developer creates a function that deletes the last entry, that would trigger DELETE multiple times. Subsequent DELETE calls would have different effects, as each one removes a unique entry. This would be considered non-idempotent.

## How to Achieve Idempotency with Non-Idempotent Methods

Idempotency isn't only a property inherent to certain methods – it can also be implemented as a feature of a non-idempotent method.  

Here are some techniques to achieve idempotency even with non-idempotent methods.

### Unique Identifiers

Adding unique identifiers to every request is one of the most common techniques used to implement idempotency. It works by tracking whether the operation has already been performed or not. If it's a duplicate (a repeat request), the server knows it's already dealt with that request and simply ignores it, ensuring that no side effects occur. 

Here's an example of how it works:

```python
from uuid import uuid4
 
def process_order(unique_id, order_data):
    if Order.objects.filter(unique_id=unique_id).exists():
        return HttpResponse(status=409)  # Conflict
    order = Order.objects.create(unique_id=unique_id, **order_data)
    return HttpResponse(status=201, content_type="application/json")

# Example usage
post_data = {"products": [...]}
headers = {"X-Unique-ID": str(uuid4())}
requests.post("https://api.example.com/orders", data=post_data, headers=headers)

```

In this code snippet, we define a function called `process_order` that creates orders in an API, using unique identifiers to implement idempotency. 

Here's a breakdown of the code:

#### Importing the Unique Identifier Generator:

`from uuid import uuid4`: The code snippet starts by importing the `uuid4` function from the `uuid` module. This function generates unique identifiers, which are used to achieve idempotency in this code.

#### Defining the `process_order` Function:

`def process_order(unique_id, order_data)`: This line defines a function named process_order that takes two arguments:

* `unique_id`: This is a string representing a unique identifier for the request. This ensures no duplicate orders are created with the same identifier.
* `order_data`: This is a dictionary containing the actual order data, like product information and customer details.

#### Checking for Existing Orders:

`if Order.objects.filter(unique_id=unique_id).exists()`: This line checks if an order with the same unique_id already exists in the database.

`Order.objects.filter(unique_id=unique_id).exists()` queries the Order model for orders with the matching unique_id and checks if any orders were found in the query result. If an order is found, it means the same request was already processed.

#### Handling existing orders:

`return HttpResponse(status=409)`: If an order with the same unique_id already exists, the function immediately returns an HTTP response with status code 409 indicating a conflict. This prevents duplicate orders from being created.

#### Creating a new order (if unique):

`order = Order.objects.create(unique_id=unique_id, **order_data )`: This line only runs if no existing order is found.

`Order.objects.create:` creates a new object in the Order model.

`unique_id=unique_id` sets the unique_id attribute of the new order to the provided unique_id.

`order_data`: spreads the dictionary order_data as keyword arguments to the order model's constructor, setting other relevant attributes like products and customer information.

#### Sending a success response:

`return HttpResponse(status=201, content_type="application/json")`: If the order creation is successful, the function will return an HTTP response with status code 201 which shows a successful creation. It also specifies the response content type as JSON, assuming the order data might be returned in JSON format.

`post_data = {"products": [...]}`: an example request, defines a dictionary containing the actual order data, like a list of products.

`headers = {"X-Unique-ID": str(uuid4())}`: This line creates a dictionary containing a custom header named X-Unique-ID. It generates a unique identifier string using uuid4() and adds it to the header.

`requests.post("https://api.example.com/orders", data=post_data, headers=headers`): This line sends a POST request to the API endpoint `https://api.example.com/orders`  with the provided `post_data` and headers.

#### How does this implement idempotence?

It does so by using a unique identifier `(unique_id)` for each order. 

It checks if an order with the same identifier already exists in the database. If it returns true, it returns a 409 Conflict status. Otherwise, it creates a new order and responds with a 201 Created status. The unique identifier prevents duplicate orders, making the system idempotent.

### Token-based Authorization

Token-based authorization is a form of authorization that assigns temporary tokens for each non-idempotent action. Once the action is completed, the token is invalidated. If the same request comes again with the same token, the server recognizes it as invalid and refuses the request, thereby preventing duplicate actions.

```javascript
// Generate a unique token for this action
const token = generateToken();

fetch("https://api.example.com/create-user", {
    method: "POST",
    body: JSON.stringify({ username, password }),
    headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
    },
})
    .then(response => {
        // Handle successful response
        if (response.ok) {
            // Do something with the successful response
        } else {
            // Handle non-successful response
        }
    })
    .catch(error => {
        // Handle error
        console.error("Error occurred:", error);
    })
    .finally(() => {
        // Invalidate token after successful action or in case of an error
        invalidateToken(token);
    });

// Simple implementation for generating a token
function generateToken() {
    return Math.random().toString(36).substr(2);
}

// Simple implementation for invalidating a token
function invalidateToken(token) {
    // Add your logic to invalidate the token, e.g., remove it from storage
}

```

Here's a breakdown of the code:

#### Generating a unique token:

`const token = generateToken()`: This line calls a function named `generateToken()` (which is assumed to be defined elsewhere) that generates a unique token string. This token will be used for authorization and idempotency.

#### Sending the `POST` request:

`fetch("https://api.example.com/create-user", { ... })`: This line uses the fetch API to send a POST request to the API endpoint `https://api.example.com/create-user`. 

`method: "POST"`: This specifies the HTTP method as POST, indicating the intention to create a new user.

`body: JSON.stringify({ username, password })`: This defines the request body with user details like username and password. The data is converted to JSON format before sending.

`headers: { Authorization:Bearer ${token}}`: This sets the Authorization header in the request. The header value includes the generated token prefixed with "Bearer ".

#### Handling the Response:

`.then(response => { ... })`: This block defines the code to execute if the request is successful. You would handle things like storing user information or redirecting the user upon successful user creation.

`.catch(error => { ... }):` This block defines the code to execute if the request encounters an error. You would handle any error messages or handle specific error scenarios here.

#### Invalidating the Token:

`invalidateToken(token)`: This line calls a function named `invalidateToken(token)` ( which is assumed to be defined elsewhere) which would likely mark the used token as invalid. This ensures the same token cannot be used for subsequent requests, adding to the idempotency guarantee.

#### How does this implement Idempotence?

This code snippet uses token-based authorization to implement idempotency in a POST request to create a user on an API. If a user creation request is accidentally sent multiple times, a new unique token is generated each time and used in the Authorization header.

The API server can recognize and verify the unique token, and since the user creation action has already been performed (assuming it's successful the first time), it won't create duplicate users due to subsequent identical requests.

### ETag Header:

An ETag header (Entity Tag) is an HTTP header used for web cache validation and conditional requests. It is mainly used for  PUT requests, that only update resources if they haven't changed since the last check.

When you want to update a resource, the server sends you its ETag which is then included in your PUT request along with the updated data. If the ETag hasn't changed (meaning the resource remains the same), the server accepts the update. But if the ETag has changed, the server rejects the update, preventing it from overwriting someone else's changes.

```python
def update_article(article_id, content):
    # Get existing article and its ETag
    article = Article.objects.get(pk=article_id)
    etag = article.etag
    
    # Check if ETag matches with request header
    if request.headers.get("If-Match") != etag:
        return HttpResponse(status=409)  # Conflict
    
    # Update article content and generate new ETag
    article.content = content
    article.save()
    new_etag = article.etag
    
    # Return success response with updated ETag
    return HttpResponse(status=200, content_type="text/plain", content=new_etag)

```

In this code snippet, we define a function called `update_article` that allows you to update the content of an existing article based on its ID and new content. It implements idempotency using the ETag header technique.

Here's a step-by-step explanation of how it works;

#### Getting the Existing Article and its ETag:

`article = Article.objects.get(pk=article_id):` This line fetches the article with the provided article_id from the database using the Article model.

`etag = article.etag:` This line extracts the ETag value from the retrieved article object. The ETag serves as a unique identifier for the article's current state.

#### Checking for a Match:

`if request.headers.get("If-Match") != etag:` This line checks if the ETag header provided in the request matches the ETag of the retrieved article.

`return HttpResponse(status=409)`: If the ETag doesn't match, it indicates that the article might have been updated by another request since the client retrieved its information. The function returns a 409 Conflict response, which prevents accidental data corruption.

#### Updating the Article Content and generating a new ETag:

`article.content = content:` This line updates the article's content with the new content received in the request.

`article.save():` This line saves the updated article back to the database.

`new_etag = article.etag:` This line retrieves the new ETag generated for the updated article after saving it.

#### Returning the Success Response with the new ETag:

`return HttpResponse(status=200, content_type="text/plain", content=new_etag)`: returns a successful 200 OK response, including the content type ("text/plain") and the updated ETag of the article in the response body.

#### How does this implement idempotence?

This code ensures that if the same update request is sent multiple times with the same ETag, the update will only be performed once, preventing duplicate updates and maintaining data consistency. The new ETag is then provided in the response to help the client keep track of the article's state for future interactions.

## Conclusion

In this tutorial, we highlighted the difference between safe methods like GET, which retrieves data without side effects, and non-idempotent methods like POST, which can have different outcomes with each repetition. 

We also explored techniques you can apply to achieve idempotence in non-idempotent methods, emphasizing the importance of designing APIs that prioritize consistency and reliability.


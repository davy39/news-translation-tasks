---
title: How to Add JWT Authentication in FastAPI – A Practical Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-07T23:28:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/fcc-fastapi-jwt-auth.png
tags:
- name: authentication
  slug: authentication
- name: FastAPI
  slug: fastapi
- name: JWT
  slug: jwt
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Abdullah Adeel

  FastAPI is a modern, fast, battle tested and light-weight web development framework
  written in Python. Other popular options in the space are Django, Flask and Bottle.

  And since it''s new, FastAPI comes with both advantages and disad...'
---

By Abdullah Adeel

[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast, battle tested and light-weight web development framework written in Python. Other popular options in the space are [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com/en/2.1.x/) and [Bottle](https://bottlepy.org/docs/dev/).

And since it's new, FastAPI comes with both advantages and disadvantages.

On the positive side, FastAPI implements all the modern standards, taking full advantage of the features supported by the latest Python versions. It has async support and type hinting. And it's also fast (hence the name FastAPI), unopinionated, robust, and easy to use.

On the negative side, FastAPI lacks some complex features like out of the box user management and admin panel that come baked in with Django. The community support for FastAPI is good but not as great as other frameworks that have been out there for years and have hundreds if not thousands of open-source projects for different use cases.

That was a very brief introduction to FastAPI. In this article, you'll learn how to implement JWT (JSON Web Token) authentication in FastAPI with a practical example.

## Project Setup

In this example, I am going to use [**replit**](https://replit.com) (a great web-based IDE). Alternatively, you can simply setup your FastAPI project locally by [following the docs](https://fastapi.tiangolo.com/tutorial/) or use this [replit starter template](https://replit.com/@abdadeel/FastAPIstarter) by forking it. This template has all the required dependencies already installed.

If you have the project setup on your local environment, here are the dependencies that you need to install for JWT authentication (assuming that you have a FastAPI project running):

```shell
pip install "python-jose[cryptography]" "passlib[bcrypt]" python-multipart
```

**NOTE:** In order to store users, I am going to use replit's built-in database. But you can apply similar operations if you are using any standard database like PostgreSQL, MongoDB, and so on. 

If you want to see the complete implementation, I have [this full video tutorial](https://www.youtube.com/watch?v=G8MsHbCzyZ4&) that includes everything a production ready FastAPI application might have.

%[https://replit.com/@abdadeel/FastAPIwithJWTauth]

## Authentication with FastAPI

Authentication in general can have a lot of moving parts, from handling password hashing and assigning tokens to validating tokens on each request. 

FastAPI leverages [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection#:~:text=In%20software%20engineering%2C%20dependency%20injection,leading%20to%20loosely%20coupled%20programs.) (a software engineering design pattern) to handle authentication schemes. Here is the list of some general steps in the process:

* Password hashing
* Creating and assigning JWT tokens
* User creation
* Validating tokens on each request to ensure authentication

## Password Hashing

When creating a user with a username and password, you need to hash passwords before storing them in the database. Let's see how to easily hash passwords.

Create a file named `utils.py` in the `app` directory and add the following function to hash user passwords.

```python
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)
```

We're using `passlib` to create the configuration context for password hashing. Here we are configuring it to use `bcrypt` . 

The `get_hashed_password` function takes a plain password and returns the hash for it that can be safely stored in the database. The `verify_password` function takes the plain and hashed passwords and return a boolean representing whether the passwords match or not.

## How to Generate JWT Tokens

In this section, we will write two helper functions to generate access and refresh tokens with a particular payload. Later we can use these functions to generate tokens for a particular user by passing the user-related payload.

Inside the `app/utils.py` file that you created earlier, add the following import statements:

```python
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
```

Add the following constants that will be passed when creating JWTs:

```python
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']    # should be kept secret
```

`JWT_SECRET_KEY` and `JWT_REFRESH_SECRET_KEY` can be any strings, but make sure to keep them secret and set them as environment variables. 

If you are following along on replit.com, you can set these environment variables from the `Secrets` tab on the left menu bar.

Add the following functions at the end of the `app/utils.py` file:

```python
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
```

The only difference between these two functions is that the expiration time for refresh tokens is longer than for access tokens.

The functions simply take the payload to include inside the JWT, which can be anything. Usually you would want to store information like USER_ID here, but this can be anything from strings to objects/dictionaries. The functions return tokens as strings.

In the end your `app/utils.py` file should look something like this:

```python
from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']     # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']      # should be kept secret

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
```

## How to Handle User Signups

Inside the `app/app.py` file, create another endpoint for handling user signups. The endpoint should take the username/email and password as data. It then checks to make sure another account with the email/username does not exist. Then it creates the user and saves it to the database.

In `app/app.py`, add the following handler function:

```
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas import UserOut, UserAuth
from replit import db
from app.utils import get_hashed_password
from uuid import uuid4

@app.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    # querying database to check if user already exist
    user = db.get(data.email, None)
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = {
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }
    db[data.email] = user    # saving user to database
    return user
```

## How to Handle Logins

FastAPI has a standard way of handling logins to comply with OpenAPI standards. This automatically adds authentication in the swagger docs without any extra configurations.

Add the following handler function for user logins and assign each user access and refresh tokens. Don't forget to include imports.

```python
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from app.schemas import UserOut, UserAuth, TokenSchema
from replit import db
from app.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from uuid import uuid4

@app.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.get(form_data.username, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user['email']),
        "refresh_token": create_refresh_token(user['email']),
    }
```

This endpoint is a bit different from the other post endpoints where you defined the schema for filtering incoming data. 

For login endpoints, we use `OAuth2PasswordRequestForm` as a dependency. This will make sure to extract data from the request and pass is as a `form_data` argument to the the `login` handler function. `python-multipart` is used to extract form data. So make sure that you have installed it.

The endpoint will reflect in the swagger docs with inputs for username and password. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-49.png)

On successful response, you will get tokens as shown here:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-50.png)

## How to Add Protected Routes

Now since we have added support for login and signup, we can add protected endpoints. In FastAPI, protected endpoints are handled using dependency injection and FastAPI can infer this from the OpenAPI schema and reflect it in the swagger docs. 

Let's see the power of dependency injection. At this point, there is no way we can authenticate from the docs. This is because currently we don't have any protected endpoint, so the OpenAPI schema does not have enough information about the login strategy we are using.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-51.png)
_No button in swagger docs to login._

Let's create our custom dependency. It's nothing but a function that is run before the actual handler function to get arguments passed to the hander function. Let's see with a practical example.

Create another file `app/deps.py`  and add include the following function in it:

```python
from typing import Union, Any
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .utils import (
    ALGORITHM,
    JWT_SECRET_KEY
)

from jose import jwt
from pydantic import ValidationError
from app.schemas import TokenPayload, SystemUser
from replit import db

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth)) -> SystemUser:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    user: Union[dict[str, Any], None] = db.get(token_data.sub, None)
    
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    
    return SystemUser(**user)
```

Here we are defining the `get_current_user` function as a dependency which in turn takes an instance of `OAuth2PasswordBearer` as a dependency.

```python
reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)
```

`OAuth2PasswordBearer` takes two required parameters. `tokenUrl` is the URL in your application that handles user login and return tokens. `scheme_name` set to `JWT` will allow the frontend swagger docs to call `tokenUrl` from the frontend and save tokens in memory. Then each subsequent request to the protected endpoints will have the token sent as `Authorization` headers so `OAuth2PasswordBearer` can parse it.

Now let's add a protected endpoint that returns user account information as the response. For this, a user has to be logged in and the endpoint will respond with information for the currently logged-in user.

In `app/app.py` create another handler function. Make sure to include imports as well.

```python
from app.deps import get_current_user

@app.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user: User = Depends(get_current_user)):
    return user
```

As soon as you add this endpoint, you will be able to see the `Authorize` button in the swagger docs and a 🔒 icon in front of the protected endpoint `/me`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-56.png)

This is power of dependency injection and FastAPI's ability to generate an automatic OpenAPI schema. 

Clicking the `Authorize` button will open the authorization form with the required fields for login. On a successful response, tokens will be saved and sent to subsequent request in the headers.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-57.png)
_Swagger integrated login form_

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-58.png)
_successfully logged in_

At this point, you can access all the protected endpoints. To make an endpoint protected, you just need to add the `get_current_user` function as a dependency. That's all you need to do!

## Conclusion

If you followed along, you should have a working FastAPI application with JWT authentication. If not, you can always run [this repl](https://replit.com/@abdadeel/FastAPI-with-JWT-authentication) and play around with it or visit [this deployed version](https://fastapi-with-jwt-authentication.abdadeel.repl.co/docs). You can find the GitHub code for this project [here](https://github.com/mabdullahadeel/fcc-fastapi-jwt).

If you found this article helpful, give me a follow at [twitter](https://twitter.com/abdadeel_) [@abdadeel_](https://twitter.com/abdadeel_). And don't forget that you can always watch [this video](https://www.youtube.com/watch?v=G8MsHbCzyZ4&ab_channel=ABDLogs) for detail explanation with a practical example.

Thanks ;)


---
title: Creating APIs with Python - Free 19-Hour Course
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-11-01T21:00:54.000Z'
originalURL: https://freecodecamp.org/news/creating-apis-with-python-free-19-hour-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pythonapi.png
tags:
- name: api
  slug: api
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'A lot of API tutorials just teach the absolute minimum. But a production-ready
  API is much more complicated than what most tutorials teach.

  We just published a massive 19-hour course on the freeCodeCamp.org YouTube channel
  that will teach you how to ...'
---

A lot of API tutorials just teach the absolute minimum. But a production-ready API is much more complicated than what most tutorials teach.

We just published a massive 19-hour course on the freeCodeCamp.org YouTube channel that will teach you how to build a full-fledged API using Python and the FastAPI library

Sanjeev Thiyagarajan developed this course. Sanjeev is a great teacher and really knows how to break things down for beginners.

The API built in this course is for a social-media-type application where users can create/read/delete/update posts as well as like other users posts.  It includes user registration and authentication.

First you will learn learn the fundamentals of API design including routes, serialization/deserialization, schema validation, and models. You will also learn about how to setup and use SQL databases. 

Then you will learn how to integrate the API with the database using both raw SQL queries and with the SqlAlchemy ORM. Postgres is used as the database but everything you learn will be applicable almost any other SQL database. 

Next you will learn how to set up testing for the application using the pytest library. You'll setup a test database and perform a good number of integration tests.

After creating the API, you will learn how to deploy the API using two different methods. The first is to deploy on an Ubuntu machine and the second is to deploy to Heroku. You will even learn how to dockerize the application.

Finally you will learn how to build out a CI/CD pipeline using GitHub actions.

Here is a full list of topics covered in this comprehensive course:

### Section 1: Intro

* Course Project
* Course Intro
* Course Project Overview

### Section 2: Setup & installation

* Mac Python Installation
* Mac VS Code install and setup
* Windows Python Installation
* Windows VS Code install and setup
* Python virtual environment Basics
* Virtual environment on windows
* Virtual environment on Mac

### Section 3: FastAPI

* Install dependencies w/ pip
* Starting Fast API
* Path operations
* Path Operation Order(yes it matters)
* Intro to Postman
* HTTP Post Requests
* Schema Validation with Pydantic
* CRUD Operations
* storing posts in Array
* creating posts
* Postman Collections & saving requests
* Retrieve One Post
* Path order Matters
* Changing response Status Codes
* Deleting Posts
* Updating Posts
* Automatic Documentation
* Python packages

### Section 4: Databases

* Database Intro
* Postgres Windows Install
* Postgres Mac Install
* Database Schema & Tables
* Managing Postgres with PgAdmin GUI
* Your first SQL Query
* Filter results with "where" keyword
* SQL Operators
* IN Keyword
* Pattern matching with LIKE keyword
* Ordering Results
* LIMIT & OFFSET
* Inserting Data
* Deleting Data
* Updating Data

### Section 5: Python + Raw SQL

* Setup App Database
* Connecting to database w/ Python
* Retrieving Posts
* Creating Post
* Get One Post
* Delete Post
* Update Post

### Section 6: ORMs

* ORM intro
* SQLALCHEMY setup
* Adding CreatedAt Column
* Get All Posts
* Create Posts
* Get Post by ID
* Delete Post
* Update Post

### Section 7: Pydantic Models

* Pydantic vs ORM Models
* Pydantic Models Deep Dive
* Response Model

### Section 8: Authentication & Users

* Creating Users Table
* User Registration Path Operation
* Hashing User Passwords
* Refractor Hashing Logic
* Get User by ID
* FastAPI Routers
* Router Prefix
* Router Tags
* JWT Token Basics
* Login Process  
* Creating a Token
* OAuth2 PasswordRequestForm
* Verify user is Logged In
* Fixing Bugs
* Protecting Routes
* Test Expired Token
* Fetching User in Protected Routes
* Postman advanced Features

### Section 9: Relationships

* SQL Relationship Basics
* Postgres Foreign Keys
* SQLAlchemy Foreign Keys
* Update Post Schema to include User
* Assigning Owner id when creating new post
* Delete and Update only your own posts
* Only Retrieving Logged in User's posts
* Sqlalchemy Relationships
* Query Parameters
* Cleanup our main.py file
* Environment Variables

### Section 10: Vote/Like System

* Vote/Like Theory
* Votes Table
* Votes Sqlalchemy
* Votes Route
* SQL Joins
* Joins in SqlAlchemy
* Get One Post with Joins

### Section 11: Database Migration w/ Alembic

* What is a database migration tool
* Alembic Setup
* Alembic First Revision
* Alembic Rollback database Schema
* Alembic finishing up the rest of the schema
* Disable SqlAlchemy create Engine

### Section 12: Pre Deployment Checklist

* What is CORS?????
* Git PreReqs
* Git Install
* Github

### Section 13: Deployment Heroku

* Heroku intro
* Create Heroku App
* Heroku procfile
* Adding a Postgres database
* Environment Variables in Heroku
* Alembic migrations on Heroku Postgres instance
* Pushing changed to production

### Section 14: Deployment Ubuntu

* Create an Ubuntu VM
* Update packages
* Install Python
* Install Postgres & setup password
* Postgres Config
* Create new user and setup python environment
* Environment Variables
* Alembic migrations on production database
* Gunicorn
* Creating a Systemd service
* NGINX
* Setting up Domain name
* SSL/HTTPS
* NGINX enable
* Firewall
* Pushing code changes to Production

### Section 15: Docker

* Dockerfile
* Docker Compose
* Postgres Container
* Bind Mounts
* Dockerhub
* Production vs Development

### Section 16: Testing

* Testing Intro
* Writing your first test
* The -s & -v flags
* Testing more functions
* Parametrize
* Testing Classes
* Fixtures
* Combining Fixtures + Parametrize
* Testing Exceptions
* FastAPI TestClient
* Pytest flags
* Test create user
* Setup testing database
* Create & destroy database after each test
* More Fixtures to handle database interaction
* Trailing slashes in path
* Fixture scope
* Test user fixture
* Test/validate token
* Conftest.py
* Failed login test
* Get all posts test
* Posts fixture to create test posts
* Unauthorized Get Posts test
* Get one post test
* Create post test
* Delete post test
* Update post
* Voting tests

### Section 17: CI/CD pipeline

* CI/CD intro
* Github Actions
* Creating Jobs
* Setup python/dependencies/pytest
* Environment variables
* Github Secrets
* Testing database
* Building Docker images
* Deploy to Heroku
* Failing tests in pipeline
* Deploy to Ubuntu

Watch the full course below or on [the freeCodeCamp.org YouTube channel](https://youtu.be/0sOvCWFmrtA) (19-hour watch). 

%[https://youtu.be/0sOvCWFmrtA]



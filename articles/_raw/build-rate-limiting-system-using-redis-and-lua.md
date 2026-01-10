---
title: How to Build a Distributed Rate Limiting System Using Redis and Lua Scripts
subtitle: ''
author: Birkaran Sachdev
co_authors: []
series: null
date: '2024-11-19T14:39:25.408Z'
originalURL: https://freecodecamp.org/news/build-rate-limiting-system-using-redis-and-lua
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/CGWK6k2RduY/upload/a5ac857cec1d18720a060fc5e3462cf3.jpeg
tags:
- name: Lua
  slug: lua
- name: Redis
  slug: redis
- name: Docker
  slug: docker
seo_title: null
seo_desc: 'In this comprehensive guide, you’ll build a distributed rate limiter using
  Redis and Lua scripting to control user requests in a high-traffic environment.

  Rate limiting is crucial in any system to prevent abuse, manage traffic, and protect
  your resou...'
---

In this comprehensive guide, you’ll build a distributed rate limiter using Redis and Lua scripting to control user requests in a high-traffic environment.

Rate limiting is crucial in any system to prevent abuse, manage traffic, and protect your resources. By leveraging Redis and Lua, you'll build an efficient, scalable rate limiting system that can handle a large number of requests while keeping your backend services safe.

We will also include an interactive demo where users can simulate traffic, observe rate limits being enforced, and view logs of blocked requests.

## What You Will Learn

* How to build a rate limiting system using Redis.
    
* How to use Lua scripts with Redis to achieve atomic operations.
    
* Understanding Redis data structures for efficient request tracking.
    
* Techniques for handling high traffic in a distributed system.
    
* Using Docker to simulate and scale a distributed rate limiter.
    

## Prerequisites

Before starting, ensure you have the following installed:

* Node.js (v14 or higher)
    
* Redis
    
* Docker (for simulating a distributed environment)
    
* Basic understanding of Node.js, Redis, and Lua scripting.
    

## Table of Contents

* [What You Will Learn](#heading-what-you-will-learn)
    
* [Prerequisites](#heading-prerequisites)
    
* [Project Overview](#heading-project-overview)
    
* [Step 1: How to Set Up the Project](#heading-step-1-how-to-set-up-the-project)
    
* [Step 2: How to Set Up Redis](#heading-step-2-how-to-set-up-redis)
    
* [Step 3: How to Implement the Rate Limiter with Redis and Lua](#heading-step-3-how-to-implement-the-rate-limiter-with-redis-and-lua)
    
* [Step 4: How to Create the Node.js API Server](#heading-step-4-how-to-create-the-nodejs-api-server)
    
* [Step 5: How to Test the Rate Limiter](#heading-step-5-how-to-test-the-rate-limiter)
    
* [Step 6: How to Visualize Rate Limiting Metrics](#heading-step-6-how-to-visualize-rate-limiting-metrics)
    
* [Step 7: How to Deploy with Docker](#heading-step-7-how-to-deploy-with-docker)
    
* [Conclusion: What You’ve Learned](#heading-conclusion-what-youve-learned)
    

## Project Overview

In this tutorial, you will:

1. Build a rate limiter using Redis and Lua to enforce request quotas.
    
2. Use Lua scripts to ensure atomic operations, avoiding race conditions.
    
3. Implement a token bucket algorithm for rate limiting.
    
4. Create an interactive demo to simulate high traffic and visualize rate limiting in action.
    

### System Architecture

You'll build the system with the following components:

1. **API Server**: Handles incoming user requests.
    
2. **Redis**: Stores request data and enforces rate limits.
    
3. **Lua Scripts**: Ensures atomic updates to Redis for rate limiting.
    
4. **Docker**: Simulates a distributed environment with multiple instances.
    

## Step 1: How to Set Up the Project

Let's start by setting up our Node.js project:

```javascript
mkdir distributed-rate-limiter
cd distributed-rate-limiter
npm init -y
```

Next, install the required dependencies:

```javascript
npm install express redis dotenv
```

* **express**: A lightweight web server framework.
    
* **redis**: For interacting with Redis.
    
* **dotenv**: For managing environment variables.
    

Create a **.env** file with the following content:

```javascript
REDIS_HOST=localhost
REDIS_PORT=6379
PORT=3000
RATE_LIMIT=5
TIME_WINDOW=60
```

These variables define the Redis host, port, rate limit (number of allowed requests), and the time window (in seconds).

## Step 2: How to Set Up Redis

Before we dive into the code, ensure that Redis is installed and running on your system. If you don’t have Redis installed, you can use Docker to quickly set it up:

```javascript
docker run -p 6379:6379 --name redis-rate-limiter -d redis
```

## Step 3: How to Implement the Rate Limiter with Redis and Lua

To efficiently handle rate limiting, we'll use a token bucket algorithm. In this algorithm:

1. Each user has a “bucket” of tokens.
    
2. Each request consumes a token.
    
3. Tokens refill periodically at a set rate.
    

To ensure atomicity and avoid race conditions, we'll use Lua scripting with Redis. Lua scripts in Redis execute atomically, which means they can’t be interrupted by other operations while running.

### How to Create a Lua Script for Rate Limiting

Create a file called **rate\_limiter.lua**:

```javascript
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local current = redis.call("get", key)

if current and tonumber(current) >= limit then
    return 0
else
    if current then
        redis.call("incr", key)
    else
        redis.call("set", key, 1, "EX", window)
    end
    return 1
end
```

1. **Inputs**:
    
    * **KEYS\[1\]**: The Redis key representing the user’s request count.
        
    * **ARGV\[1\]**: The rate limit (maximum number of allowed requests).
        
    * **ARGV\[2\]**: The time window (in seconds) for the rate limit.
        
2. **Logic**:
    
    * If the user has reached the rate limit, return `0` (request blocked).
        
    * If the user is within the limit, increment their request count or set a new count with an expiration if it's the first request.
        
    * Return 1 (request allowed).
        

## Step 4: How to Create the Node.js API Server

Create a file called **server.js**:

```javascript
require('dotenv').config();
const express = require('express');
const redis = require('redis');
const fs = require('fs');
const path = require('path');

const app = express();
const client = redis.createClient({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT
});

const rateLimitScript = fs.readFileSync(path.join(__dirname, 'rate_limiter.lua'), 'utf8');

const RATE_LIMIT = parseInt(process.env.RATE_LIMIT);
const TIME_WINDOW = parseInt(process.env.TIME_WINDOW);

// Middleware for rate limiting
async function rateLimiter(req, res, next) {
  const ip = req.ip;
  try {
    const allowed = await client.eval(rateLimitScript, 1, ip, RATE_LIMIT, TIME_WINDOW);
    if (allowed === 1) {
      next();
    } else {
      res.status(429).json({ message: 'Too many requests. Please try again later.' });
    }
  } catch (err) {
    console.error('Error in rate limiter:', err);
    res.status(500).json({ message: 'Internal server error' });
  }
}

app.use(rateLimiter);

app.get('/', (req, res) => {
  res.send('Welcome to the Rate Limited API!');
});

const PORT = process.env.PORT;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

1. **Rate Limiter Middleware**:
    
    * Retrieves the client's IP address and checks if they are within the rate limit using the Lua script.
        
    * If the user exceeds the limit, a `429` response is sent.
        
2. **API Endpoint**:
    
    * The root endpoint is rate-limited, so users can only access it a limited number of times within the specified window.
        

## Step 5: How to Test the Rate Limiter

1. **Start Redis**:
    
    ```basic
    docker start redis-rate-limiter
    ```
    
2. **Run the Node.js Server**:
    
    ```bash
    node server.js
    ```
    
3. **Simulate Requests**:
    
    * Use `curl` or Postman to test the rate limiter:
        
        ```bash
        curl http://localhost:3000
        ```
        
    * Send multiple requests rapidly to see rate limiting in action.
        

## Step 6: How to Visualize Rate Limiting Metrics

To monitor rate limiting metrics like cache hits and blocked requests, we'll add logging to the middleware in **server.js**:

```javascript
async function rateLimiter(req, res, next) {
  const ip = req.ip;
  try {
    const allowed = await client.eval(rateLimitScript, 1, ip, RATE_LIMIT, TIME_WINDOW);
    if (allowed === 1) {
      console.log(`Allowed request from ${ip}`);
      next();
    } else {
      console.log(`Blocked request from ${ip}`);
      res.status(429).json({ message: 'Too many requests. Please try again later.' });
    }
  } catch (err) {
    console.error('Error in rate limiter:', err);
    res.status(500).json({ message: 'Internal server error' });
  }
}
```

## Step 7: How to Deploy with Docker

Let’s containerize the application to run it in a distributed environment.

Create a `Dockerfile`:

```dockerfile
FROM node:14
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node", "server.js"]
```

Build and Run the Docker Container:

```bash
docker build -t rate-limiter .
docker run -p 3000:3000 rate-limiter
```

Now you can scale the rate limiter by running multiple instances.

## Conclusion: What You’ve Learned

Congratulations! You’ve successfully built a distributed rate limiter using Redis and Lua scripts. Throughout this tutorial, you’ve learned how to:

1. Implement rate limiting to control user requests in a distributed system.
    
2. Use Lua scripts in Redis to perform atomic operations.
    
3. Apply a token bucket algorithm to manage request quotas.
    
4. Monitor rate limiting metrics to optimize performance.
    
5. Use Docker to simulate a scalable distributed environment.
    

### Next Steps:

1. **Add Rate Limiting by User ID**: Extend the system to support rate limits per user.
    
2. **Integrate with Nginx**: Use Nginx as a reverse proxy with Redis-backed rate limiting.
    
3. **Deploy with Kubernetes**: Scale your rate limiter using Kubernetes for high availability.
    

Happy coding!

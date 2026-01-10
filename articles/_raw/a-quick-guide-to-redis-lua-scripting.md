---
title: A quick guide to Redis Lua scripting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-25T18:34:46.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-redis-lua-scripting
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/lua_script-1.jpg
tags:
- name: Lua
  slug: lua
- name: Redis
  slug: redis
- name: Scripting
  slug: scripting
seo_title: null
seo_desc: 'By Andrei Chernikov

  Redis is a popular in-memory grid used for interprocess communication and data storage.
  You might’ve heard that it lets you run Lua scripts, but you are still not sure
  why. If this sounds like you, read on.


  Prerequisites

  You shou...'
---

By Andrei Chernikov

Redis is a popular in-memory grid used for interprocess communication and data storage. You might’ve heard that it lets you run Lua scripts, but you are still not sure why. If this sounds like you, read on.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/lua_script.jpg)

## Prerequisites

You should have [Redis installed on your system](https://redis.io/topics/quickstart) to follow this guide. It might be helpful to check [Redis commands reference](https://redis.io/commands) while reading.

## Why do I need Lua Scripts?

In short: performance gain. Most tasks you do in Redis involve many steps. Instead of doing these steps in the language of your application, you can do it inside Redis with Lua.

* This may result in better performance.
* Also, all steps within a script are executed in an atomic way. No other Redis command can run while a script is executing.

For example, I use Lua scripts to change JSON strings stored in Redis. I describe this in detail closer to the end of this article.

## But I don’t know any Lua

![Image](https://www.freecodecamp.org/news/content/images/2019/09/dont-know-s.png)
_A person who doesn't know any lua_

Don’t worry, Lua is not very hard to understand. If you know [any language of the C family](https://en.wikipedia.org/wiki/List_of_C-family_programming_languages), you should be okay with Lua. Also, I am providing working examples in this article.

## Show me an example

Let’s start by running scripts via **redis-cli**. Start it with:

```shell
redis-cli
```

Now run the following command:

```redis
eval “redis.call(‘set’, KEYS[1], ARGV[1])” 1 key:name value
```

The **EVAL** command is what tells Redis to run the script which follows. The `”redis.call(‘set’, KEYS[1], ARGV[1])”`string is our script which is functionally identical to the Redis’s `set` command. Three parameters follow the script text:

1. The number of provided keys
2. Key name
3. First argument

Script arguments fall into two groups: **KEYS** and **ARGV**.

We specify how many keys the script requires with the number immediately following it. In our example, it is **1**. Immediately after this number, we need to provide these keys, one after another. They are accessible as **KEYS** table within the script. In our case, it contains a single value `key:name` at index **1**.

_Note, that Lua indexed tables start with index_ **_1,_** _not_ **_0_**_._

We can provide any number of arguments after the keys, which will be available in Lua as the **ARGV** table. In this example, we provide a single **ARGV**-argument: string `value`. As you already guessed, the above command sets the key `key:name` to value `value`.

It is considered a good practice to provide keys which the script uses as **KEYS**, and all other arguments as **ARGV**. So you shouldn’t specify **KEYS** as 0 and then provide all keys within the **ARGV** table.

Let’s now check if the script completed successfully. We are going to do this by running another script which gets the key from Redis:

eval “return redis.call(‘get’, KEYS[1])” 1 key:name

The output should be `”value”`, which means that the previous script successfully set the key `“key:name”`.

## Can you explain the script?

![Image](https://miro.medium.com/max/465/1*Utfw9sl2XFHDpyulDvoIvA.jpeg)
_Doge after seeing the script above_

Our first script consists of a single statement: the `redis.call` function:

```lua
redis.call(‘set’, KEYS[1], ARGV[1])
```

With`redis.call` you can execute any Redis command. The first argument is the name of this command followed by its parameters. In the case of the `set` command, these arguments are **key** and **value**. All Redis commands are supported. [According to the documentation](https://redis.io/commands/eval):

> _Redis uses the same Lua interpreter to run all the commands_

Our second script does a little more than just running a single command — it also returns a value:

```redis
eval “return redis.call(‘get’, KEYS[1])” 1 key:name
```

Everything returned by the script is sent to the calling process. In our case, this process is **redis-cli** and you will see the result in your terminal window.

## Something more complex?

![Image](https://www.freecodecamp.org/news/content/images/2019/09/man-looking-at-board.jpg)
_A person planning to build a complex Redis script_

I once used Lua scripts to return elements from a hash map in a particular order. The order itself was specified by hash keys stored in a sorted set.

Let’s first set up our data by running these commands in **redis-cli**:

```redis
hmset hkeys key:1 value:1 key:2 value:2 key:3 value:3 key:4 value:4 key:5 value:5 key:6 value:6
zadd order 1 key:3 2 key:1 3 key:2
```

These commands create a hash map at key `hkeys` and a sorted set at key `order` which contains selected keys from `hkeys` in a specific order.

_You might want to check_ [_hmset_](https://redis.io/commands/hmset) _and_ [_zadd_](https://redis.io/commands/zadd) _commands reference for details._

Let’s run the following script:

```redis
eval “local order = redis.call(‘zrange’, KEYS[1], 0, -1); return redis.call(‘hmget’,KEYS[2],unpack(order));” 2 order hkeys
```

You should see the following output:

```redis
“value:3”
“value:1”
“value:2”
```

Which means that we got values of the keys we wanted and in the correct order.

## Do I have to specify full script text to run it?

No! Redis allows you to preload a script into memory with the **SCRIPT LOAD** command:

```redis
script load “return redis.call(‘get’, KEYS[1])”
```

You should see an output like this:

```redis
“4e6d8fc8bb01276962cce5371fa795a7763657ae”
```

This is the unique hash of the script which you need to provide to the **EVALSHA** command to run the script:

```redis
evalsha 4e6d8fc8bb01276962cce5371fa795a7763657ae 1 key:name
```

_Note: you should use actual_ **_SHA1_** _hash returned by the_ **_SCRIPT LOAD_** _command, the hash above is only an example._

## What did you mention about changing JSON?

Sometimes people store JSON objects in Redis. Whether it is a good idea or not is another story, but in practice, this happens a lot.

If you have to change a key in this JSON object, you need to get it from Redis, parse it, change the key, then serialize and set it back to Redis. There are a couple of problems with this approach:

1. Concurrency. Another process can change this JSON between our get and set operations. In this case, the change will be lost.
2. Performance. If you do these changes often enough and if the object is rather big, this might become the bottleneck of your app. You can win some performance by implementing this logic in Lua.

Let’s add a test JSON string to Redis under key `obj`:

```redis
set obj ‘{“a”:”foo”,”b”:”bar”}’
```

Now let’s run our script:

```redis
EVAL ‘local obj = redis.call(“get”,KEYS[1]); local obj2 = string.gsub(obj,”(“ .. ARGV[1] .. “\”:)([^,}]+)”, “%1” .. ARGV[2]); return redis.call(“set”,KEYS[1],obj2);’ 1 obj b bar2
```

Now we will have the following object under key `obj`:

```
{“a”:”foo”,”b”:”bar2"}
```

You can instead load this script with the **SCRIPT LOAD** command:

```redis
SCRIPT LOAD ‘local obj = redis.call(“get”,KEYS[1]); local obj2 = string.gsub(obj,”(“ .. ARGV[1] .. “\”:)([^,}]+)”, “%1” .. ARGV[2]); return redis.call(“set”,KEYS[1],obj2);’
```

 and then run it like this:

```redis
EVALSHA <your_script_sha> 1 obj b bar2
```

**Some notes:**

* The `..` is the string concatenation operator in Lua.
* We use a RegEx pattern to match key and replace its value. If you don’t understand this Regular Expression, [you can check my recent guide](https://medium.freecodecamp.org/simple-regex-tricks-for-beginners-3acb3fa257cb).
* One difference of the Lua RegEx flavor from most other flavors is that we use `%` as both backreference mark and escape character for RegEx special symbols.
* We still escape `”` with `\` and not `%` because we escape Lua string delimiter, not RegEx special symbol.

## Should I always use Lua scripts?

No. I recommend only using them when you can prove that it results in better performance. Always run benchmarks first.

If all you want is atomicity, then [you should check Redis transactions instead](https://redis.io/topics/transactions).

Also, your script shouldn’t be too long. Remember that while a script is running, everything else is waiting for it to finish. If your script takes quite some time, it can cause bottlenecks instead of improving performance. The script stops after reaching a timeout (5 seconds by default).

![Image](https://miro.medium.com/max/940/1*KuCJoYrILg1eaBYHpEhQhg.jpeg)
_Redis scripts should not take too much time_

## Last Word

For more information on Lua check [lua.org](http://www.lua.org/start.html).

You can check [my node.js library on GitHub](https://github.com/aikei/redis-json) for some examples of Lua scripts (see `src/lua` folder). You can also use this library in node.js to change JSON objects without writing any Lua scripts yourself.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

**Thank you for reading this article. Questions and comments are much appreciated. You are also welcome to follow me** [**on Twitter**](https://twitter.com/aikei_en)**.**


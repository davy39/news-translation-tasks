---
title: What is Serialization?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-10T21:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-serialization
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/erica-steeves-G_lwAp0TF38-unsplash.jpg
tags:
- name: computer networking
  slug: computer-networking
- name: data
  slug: data
- name: network
  slug: network
seo_title: null
seo_desc: "By George Offley\nDuring a recent project update meeting, my team talked\
  \ about how we were going to use serialization to send data back and forth from\
  \ this application. \nAn engineer who was looking to get more into software projects\
  \ told me that they ..."
---

By George Offley

During a recent project update meeting, my team talked about how we were going to use serialization to send data back and forth from this application. 

An engineer who was looking to get more into software projects told me that they were unfamiliar with the term. 

It's easy to miss essential processes like these that don’t come up until you dive into more extensive projects. This was the case for this person, as it was for me at one point. 

So I wanted to write about it. I helped my colleague learn about serialization that day, and you’re going to learn about it today.

## What is Serialization?

Serialization is the process in which one service takes in a data structure, such as a dictionary in Python, wraps it up, and transmits it to another service for reading. That’s the simple definition. 

Imagine that I need to send a message to someone. So I write down the text on an already assembled puzzle. I take apart the pieces, add some instructions on how to reassemble the puzzle, and send it along. 

The message recipient then gets the pieces of the puzzle, puts them all back together, and now they have my message.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/serialization_basic.jpeg)
_Basic serialization flow of events_

The technical definition is a bit more fun. To wit, serialization is the process of converting a data object into a byte stream, and saving the state of the object to be stored on a disk or transmitted across a network. This cuts down the storage size needed and makes it easier to transfer information over a network.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/serialization_process.jpeg)
_Serialization Process_

### Marshaling and Serialization - what are the differences?

The process of [marshaling](https://en.wikipedia.org/wiki/Marshalling_(computer_science)) might come to mind. Marshaling is the process of transforming the memory representation of an object into a suitable form for transmission. 

Although marshaling and serialization are _loosely_ synonymous, there is a crucial difference. For example, when creating a Golang program to read JSON data into a Golang data structure, you might use marshaling to translate JSON key values into Golang key values. 

The difference is that marshaling might be used to translate data. In contrast, serialization sends or stores data in a byte stream and reassembles it in its original form. Both do serialization, but there is a difference in intent in these two processes.

You can see this struct I created for interacting with Twitter data below as an example of marshaling in action. In Golang, you can give hints called tags, easily converting this object into JSON data using Golang's built-in marshaling service.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/golang_marshall_example.png)
_Golang Struct using JSON tags_

### What is Endianness?

I’d also like to touch on the subject of [endianness](https://en.wikipedia.org/wiki/Endianness) lightly. Endianness is a term used to describe the order of bytes in memory. 

You can think of memory as a block where bites of data are stored. For serialization to work, the byte stream needs to transfer data types regardless of the changing endianness from one system to another. 

You can see the little and big-endian differences below. It is essential that the endianness matches from one system to another or be converted somehow, as not all systems order their bits the same way.

![Little and big endian courtesy of https://pvs-studio.com/en/blog/lessons/0019/ ](https://www.freecodecamp.org/news/content/images/2021/12/endian_dif.png)
_Little and big-endian Courtesy of https://pvs-studio.com/en/blog/lessons/0019/_

## Use Cases for Serialization

Our use case takes full advantage of these features. We plan to take in some information from the hardware we’re scanning, package up that information into a byte stream, and send it along with the network to another service that will reconstruct the data. 

The process of reversing the serialization process and reconstructing the data back into its original form is called **deserialization**.

There are other use cases for this. For example, REST APIs or messaging protocols such as AMQP can use serialization to compress and send data. 

AMQP is a messaging protocol where you send messages to an AMQP broker, and the receiving service is “listening” to this broker for a message. Backend engineers might know this well, as this is often used for sending data back and forth within distributed systems. 

Many programming languages include the ability to spin up some serialization easily. So it is a language-agnostic topic.

### Serialization Example

Let’s give a quick example. This code uses the library [kombu](https://github.com/celery/kombu) to send messages via AMQP. We’re using this to send messages from one software package to another over a network. This code is for a service sending a message to an AMQP broker:

```python
def send_message(self, payload, sender_serializer):
...
    try:
        producer.publish(
            {'payload': message},
            ...
            serializer = 'json',
            ...
        )
        return
```

Take note of the `publish` method. We are passing in the serialization method as an argument so that the library knows how to serialize the data we are passing in.

The data message is converted into a stream of bytes, which, if you look at it, just looks like a long string of letters and numbers, and we send the message. 

The corresponding service will use the same serialization method to reconstruct the data in its original state. This is a significant feature as we are creating a suite of tools that need to be able to send messages to each other for them to work.

## Serialization Data Formats

I use [JSON](https://www.json.org/json-en.html) for serialization whenever the task at hand calls for it. However, you can also use a few others. 

JSON has a lot of overhead, but the human readability makes it ideal for me. You can also use [Protobufs](https://developers.google.com/protocol-buffers), [YAML](https://en.wikipedia.org/wiki/YAML), or XML. Those are just some of the data object formats you can use.

## Conclusion

I’m glad I got this out of my system. I got to stop thinking about this, and, hopefully, someone learned something from it. 

Serialization becomes essential when you’re putting together your communication pipeline. It’s good to know about this topic to feel confident approaching whatever tool you are using with the proper background knowledge.

-George


---
title: What is Idempotence? Explained with Real-World Examples
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2024-02-29T00:44:58.000Z'
originalURL: https://freecodecamp.org/news/idempotence-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/cover--2-.png
tags:
- name: idempotence
  slug: idempotence
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'Idempotence is a property of an operation that ensures that, if the operation
  is repeated once or more than once, you get the same result.

  Apply it once or more and the outcome''s the same, idempotence is the name.

  All rhyming aside, idempotence is an...'
---

Idempotence is a property of an operation that ensures that, if the operation is repeated once or more than once, you get the same result.

Apply it once or more and the outcome's the same, idempotence is the name.

All rhyming aside, idempotence is an important concept often used in the design of everyday things. The underlying principle of idempotence – where repeated actions do not change the outcome, beyond the initial action – has been applied implicitly or explicitly both to the physical world and the digital world of cloud computing and software applications.

This article will show you some examples of idempotence in the physical world, as well as how it is used in software architectures to build reliable and fault-tolerant systems.

## Idempotence in the Physical World

Idempotent buttons are used in everyday systems, like traffic light buttons, the stop button on London buses, and elevator call buttons.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb07003d3-ffc7-4074-88d1-cee009fb7119_2374x1308.png align="left")

*Some examples of idempotence in the physical world: a traffic light button for pedestrians, a stop button in a London bus, and an elevator call button.*

Pressing a traffic light button multiple times does not make the light change faster – it simply registers the need for a pedestrian crossing once.

Similarly, pressing the stop button on a London bus signals the driver to stop at the next stop – but pressing it multiple times does not change the bus's route, make the bus stop faster, or cancel the initial stop request.

## Idempotence Patterns in Software Architectures

Different patterns of idempotence are used in software architectures. We'll discuss two popular ones here.

### API Design

In REST APIs, HTTP methods like GET, HEAD, PUT, and DELETE are inherently idempotent.

* GET: Used to retrieve data from a server. Multiple GET requests to the same resource are safe and should return the same data, assuming no changes have been made to the resource in the meantime.
    
* HEAD: Similar to GET, but it retrieves only the header information about a resource. Since it does not return a body, it's inherently safe and idempotent.
    
* PUT: Replaces a resource's current representation with the request payload. Repeatedly putting the same data to the same resource endpoint will leave the resource in the same state.
    
* DELETE: Removes a resource. Deleting the same resource multiple times results in the same outcome: the resource is removed after the first successful request, and subsequent DELETE requests typically return a 404 Not Found or 204 No Content status, indicating that there's no resource to delete.
    

A POST operation is not inherently idempotent, since it is typically used to create resources. But some implementations of POST can be designed to be idempotent.

A good example of this is the Post/Redirect/Get pattern, also referred to as the PRG pattern. This pattern is particularly useful for handling form submissions and can mitigate issues caused by users refreshing or bookmarking pages that make changes to the server's state. Let’s examine in detail how this works.

#### How to Make a POST Operation Idempotent

The sequence diagram below explains how the PRG pattern works to prevent duplicate orders in an e-commerce web application:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdf24083-d54b-4c97-8607-bebe4955fe71_1044x774.png align="left")

*Sequence diagram showing how the PRG pattern works to "convert" a POST operation to an idempotent GET operation*

1. **Post**: When the user submits a form to place an order, the browser sends a POST request to the server.
    
2. **Redirect**: After the server processes the POST request (for example, placing the order), it sends a redirect response to the browser, usually with a 303/302 HTTP status code, directing it to a new URL. This URL is typically an order confirmation page.
    
3. **Get**: The browser then makes a GET request to the URL provided by the redirect. The user sees the page that confirms their order or brings them back to a safe state where no duplicate orders can be accidentally created.
    

The key benefit of using the PRG pattern is that it turns the POST request into a GET request, which is idempotent. This means that refreshing the page at the end of the process will not cause the same order to be submitted more than once, because refreshing will only repeat the GET request, not the initial POST request that submitted the order.

This pattern enhances the user experience by preventing common mistakes, such as double-clicking a submission button or refreshing the page, creating unwanted duplicate orders.

It also makes the application more robust and user-friendly, as users can safely refresh the confirmation page or bookmark it without worrying about the order being duplicated.

### Message Queueing Systems

A message queue can contribute to making a system idempotent by ensuring that even if a message (representing a request) is delivered multiple times, the operation it triggers is executed only once, or its effect is the same regardless of how many times it's executed.

This is crucial in distributed systems where network failures, system crashes, or other issues can lead to the same message being processed multiple times.

Let’s look at an example that involves making a payment. No customer wants to be accidentally double-charged when making a purchase, so making sure the system is idempotent is very important.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37b5e26b-6892-48c7-8aa8-eaa0c2a39be5_1784x1530.png align="left")

*Sequence diagram showing how a message queue can make a system idempotent and prevent duplicate payments from happening*

1. The message queue sends a message to the payment system to debit an account.
    
2. This message has a unique Transaction ID. The Database of Processed IDs maintains a record of Transaction IDs that have been processed. The Payment System checks the Transaction ID against the Database of Processed IDs and checks if this payment has already been processed.
    
3. If the message has a transaction ID in the Processed ID Database, it is ignored and treated as already processed. The payment has already been made and does not need to be repeated. The Payment System sends an acknowledgement (ACK) back to the queue to inform it that the message has been ignored. The message queue needs to know that the message has been handled before it deletes the message on its side.
    
4. If the message does not have a Transaction ID in the Processed ID database, this means the payment has not been processed before. The payment is therefore processed and the transaction ID is added to the Database of Processed IDs. Ideally, these two steps should be done in a single [atomic transaction](https://lightcloud.substack.com/i/140524854/atomicity). This prevents an unwanted state where the payment is processed but the Transaction ID is never added to the Database of Processed IDs because of a database failure, networking issue or any other fault.
    
5. In the final step, the Payment System sends an acknowledgement (ACK) back to the queue to inform it that the message has been successfully processed. This acknowledgement informs the queue that the message has been successfully received, processed, and no longer needs to be kept in the queue for future delivery. This prevents the message from being sent again, ensuring that the system is idempotent.
    

In this example, the system ensures idempotency by:

* Checking Transaction IDs for new payments against a database of payments already made
    
* Sending the acknowledgement to the queue after the message is ignored or processed by the Payment System. Thus ensures that the same message is only sent to the Payment System once.
    

## Bringing it Together

Idempotence solves one fundamental problem: how do you handle operations that, intentionally or by accident, can be repeated? Idempotence ensures that no matter how many times an operation is applied, the outcome remains the same after the first application, mitigating the risks associated with repeated actions.

The underlying principle of idempotence is used in the design of everyday objects we interact with in the physical world, from traffic light buttons for pedestrians to elevator call buttons.

In the abstract world of software architecture, idempotence ensures that repeated operations have the same effect as performing that operation just once. Idempotence allows us to build reliable and fault-tolerant architectures.

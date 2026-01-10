---
title: How to Create Multiple Virtual Hosts on a Single RabbitMQ Instance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-26T21:25:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-multiple-virtual-hosts-on-one-rabbitmq-instance
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Untitled-design.png
tags:
- name: distributed systems
  slug: distributed-systems
- name: message broker
  slug: message-broker
- name: Python
  slug: python
- name: rabbitmq
  slug: rabbitmq
seo_title: null
seo_desc: "By Ridwan Yusuf\nHi, friends, and welcome to another tutorial. We'll be\
  \ talking about RabbitMQ, a tool that is widely used as a message broker in distributed\
  \ and Pub-Sub systems. \nWhile multiple applications can share a single RabbitMQ\
  \ instance, it's ..."
---

By Ridwan Yusuf

Hi, friends, and welcome to another tutorial. We'll be talking about RabbitMQ, a tool that is widely used as a message broker in distributed and Pub-Sub systems. 

While multiple applications can share a single RabbitMQ instance, it's a great approach to configure it to have different virtual hosts for each application. 

One practical usage in a Python application is using it as a Celery broker URL or simply as a message queue.

One benefit of this is that it saves the costs that comes with spinning up multiple instances of RabbitMQ. Creating RabbitMQ virtual hosts is similar both locally and when running in a self-managed solution such as AWS RabbitMQ

By the end of this guide, you will be able to:

1. Create multiple virtual hosts for a single RabbitMQ instance.
2. Test the connections using the correct credentials, that is user, password, and virtual host.

**Prerequisites to follow along**:

1. Ensure you have Docker and Docker Compose installed, or
2. Have a self-managed RabbitMQ instance from AWS, CloudAMQP, or any other service provider

Without any delay, let’s get started

## How to Run a RabbitMQ Instance Locally

To keep things simple, we are going to run the RabbitMQ instance in a Docker container.

Create a file named docker-compose.yml and update it with the following content:

_docker-compose.yml_

```yaml
version: "3.8"
services:
  rabbitmq:
    image: rabbitmq:3.8-management-alpine
    container_name: 'rabbitmq_test'
    environment:
      - RABBITMQ_DEFAULT_USER=sampleuser
      - RABBITMQ_DEFAULT_PASS=samplepassword
    ports:
        - 5672:5672
        - 15672:15672
    volumes:
      - ~/.docker-conf/rabbitmq/data/:/var/lib/rabbitmq/
      - ~/.docker-conf/rabbitmq/log/:/var/log/rabbitmq
```

To start the container, run this command in the terminal:

```yaml
docker-compose up
```

Once the container is up and running, access the GUI by visiting this link: [http://localhost:15672/](http://localhost:15672/)

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-2-5cc0fa8243.jpg)
_RabbitMQ GUI login page_

Use the credentials specified in the docker-compose file to gain access to the dashboard – “sampleuser” and “samplepassword” in my case.

**Note:** If you are using a self-managed RabbitMQ instance from AWS or CloudAMQP, the RabbitMQ connection string will look similar to this:

amqps://ausername:[apassword@32wewjijiokkoo.mq.eu-west-3.amazonaws.com](mailto:apassword@32wewjijiokkoo.mq.eu-west-3.amazonaws.com):5671

To access the RabbitMQ admin dashboard, follow these steps:

1. Visit the URL using the HTTPS protocol: [https://32wewjijiokkoo.mq.eu-west-3.amazonaws.com](https://32wewjijiokkoo.mq.eu-west-3.amazonaws.com)
2. Remove the username, password, and port from the URL.
3. After accessing the URL, the system will prompt you to enter the username and password specified in the RabbitMQ connection string (“ausername” and “apassword” in this case). Provide these credentials to log in to the admin dashboard.

## How to Create a Virtual Host

Once you are logged in, click on the ‘Admin’ tab, and then navigate to the ‘Virtual Hosts’ tab as shown in the image below.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-82232fd2b0.jpg)
_RabbitMQ Virtualhost tab_

Click on ‘Add a new virtual host’, and provide it with an appropriate name. Finally, click on the ‘Add virtual host’ button to create the new virtual host.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-26e9083f62.jpg)
_New Virtual Host created_

## How to Create a New User

On the Users tab, click on the ‘Add a user’ toggle. Specify a Username and Password for the new user. If you wish, you may grant the user access to the Admin (GUI) interface. Finally, click on the ‘Add user’ button to create the new user.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-e787f0c102.jpg)
_Create a new user_

## How to Assign the New User to the Created Virtual Host (Vhost)

On the Users tab, locate and click on the previously created user, which was named ‘user1’ in my case.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-cb6b620bdf.jpg)
_New user in users list_

For the new user, choose the virtual host as ‘new-virtual-host’, and then click the ‘Set permission’ button. This grants the user access to the specified virtual host. To confirm this, go back to the Users tab and verify that the user now appears with access to the ‘new-virtual-host'

![Image](https://www.freecodecamp.org/news/content/images/2023/07/WhatsApp-Image-2023-07-25-at-19.59.44.jpeg)
_Assign new user to the created virtual host_

By now, the new user 'user1' has been configured to access the vhost 'new-virtual-host'.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-26-06-22-12.png)
_New user assigned to the created virtual host_

## How to Test the Connection for the New User and Vhost

To test if the new user can access the new vhost, you can use the following sample Python script. Once everything is working correctly, you can use the URL string to connect to the RabbitMQ broker in any application.

_test_rabbit.py_

```python
import pika

def test_rabbitmq_url(url):

    try:
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        connection.close()
        print("Connection successful!")

    except pika.exceptions.AMQPError as e:
        print("Connection failed:", e)

test_rabbitmq_url('amqp://user1:password@localhost:5672/new-virtual-host')
```

Note how we have specified the RabbitMQ URL: it has the username as “user1” and password as “password9,” while the virtual host is named ‘new-virtual-host.’

Remember to install pika by running `pip install pika` on the command line.

To run this script on the terminal, enter the following command:

```bash
python test_rabbit.py
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-4dda3c97ef.jpg)
_Successfully connected to RabbitMQ_

This indicates a successful connection to the RabbitMQ instance.

Change the password in the utility function to an incorrect one, and you should see an outcome similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-85582a7c7f.jpg)
_Connection to RabbitMQ failed_

## Wrapping Up

In conclusion, creating multiple virtual hosts on a single RabbitMQ instance can significantly enhance your message queue management capabilities. 

By effectively segregating applications and resources, you ensure better organization, security, and scalability. With the step-by-step guide provided in this article, you now have the knowledge to harness the full potential of RabbitMQ

Thanks for reading, and I hope you enjoyed the article.

For more interesting content and tips, please feel free to check out my video collection on [YouTube](https://www.youtube.com/@ridwanray) and consider hitting the subscribe button.

You can also find me on [LinkedIn](https://linkedin.com/in/ridwan-yusufa/).


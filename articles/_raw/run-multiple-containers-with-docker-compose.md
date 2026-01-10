---
title: How to Run Multiple Containers with Docker Compose
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-27T19:31:29.000Z'
originalURL: https://freecodecamp.org/news/run-multiple-containers-with-docker-compose
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/docker-compose-scaled-1.jpeg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: null
seo_desc: "By Arjav Dave\nDocker has become increasingly popular over the last several\
  \ years. One reason for this is that you can create portable containers which are\
  \ fast and easy to deploy. \nAs described on Docker's website, a container is something\
  \ that packa..."
---

By Arjav Dave

Docker has become increasingly popular over the last several years. One reason for this is that you can create portable containers which are fast and easy to deploy. 

As described on Docker's [website](https://www.docker.com/resources/what-container/), a **container** is something that packages your code along with any other dependencies so that it can be deployed across multiple platforms reliably. 

These containers can be run locally on your Windows, Mac, and Linux. And major cloud systems like AWS or Azure support them out of the box. You can also use Docker on any hosting space where it can be installed and run. 

If you want to learn more Docker basics and need a cheat sheet for Docker CLI, I [wrote an introductory article about it here](https://www.daveops.co.in/post/docker-a-beginner-s-cheat-sheet-2022).

In this tutorial, we will go deeper so you can understand some of the more advanced features like how to run multiple containers.

## Why Docker Compose?

With Docker compose, you can configure and start multiple containers with a single yaml file. This is really helpful if you are working on a technology stack with multiple technologies. 

As an example, say that you are working on a project that uses a MySQL database, Python for AI/ML, NodeJS for real-time processing, and .NET for serving API’s. It would be cumbersome to setup such an environment for each team member. Fortunately, Docker makes this easier with the help of compose.

### How Does Docker Compose Work?

`docker compose` is a yaml file in which we can configure different types of services. Then with a single command all containers will be built and fired up. 

There are 3 main steps involved in using compose:

* Generate a Dockerfile for each project.
* Setup services in the docker-compose.yml file.
* Fire up the containers.

We are now going to see how using `docker compose` can help you set up an environment for a project that uses a bunch of different tools, like we discussed above.

### Prerequisites

You might think you have to have all the technologies installed to run this tech stack of MySQL, Python, NodeJS, .NET, and PHP. 

But actually, all you need is a Docker engine running. The latest versions of Docker come with Docker compose installed. For now you don't need to install anything else.

## What We'll Do in this Tutorial

Before we start, here is a brief overview of what we are going to do. We will be tackling each technology one by one. 

For each technology we will create a sample application (except MySQL) and create a Dockerfile for each. 

Then we will point these Dockerfiles in our `docker compose` yaml file. 

Lastly, we will configure `docker compose` so that each application does what it’s supposed to do.

Before we get started, create a folder named `super-app`. Next, create a `docker-compose.yml` file. In this file we will configure all our applications. So let’s get started.

For those of you interested in the code, you can visit the [repository here.](https://github.com/shenanigan/super-app-docker)

### How to Configure MySQL

Add the below content in your docker-compose.yml file:

    version: '3.4'
    services:
      super-app-db:
        image: mysql:8.0.28
        environment:
          MYSQL_DATABASE: 'super-app'
          MYSQL_ROOT_PASSWORD: '$SuperApp1'
        ports:
          - '3306:3306'
        expose:
          - '3306'

Under the `services` section we will list all the types of applications to be configured.

To start with we configure a `super-app-db` service which pulls a Docker image of MySQL with version 8.0.28. 

Next, we instruct the container to create a database name `super-app` with `root` as default user and it’s password set to _$SuperApp1_. 

Lastly, since the default port for MySQL is 3306, we are mapping it to the container’s port 3306 and exposing that port for access.

Once the above file is created, run the below command to get your Docker image created and run it as a container.

    docker compose up

The MySQL image will be pulled and then Docker will spin up a container to run this image. MySQL server can be verified by connecting it via a MySQL client. 

If not, don't worry – we will see below how to connect to it via one of our applications. As long as the container is not deleted the tables will be persisted.

Let’s configure our next application NodeJS.

### How to Configure NodeJS

We will create a very simple Express Node application. In order to do so, create a folder named node inside our super-app folder. 

Add the files server.js, package.json and Dockerfile in the node folder.

server.js:

    const server = require("express")();
    server.listen(3000, async () => { });
    server.get("/super-app", async (_, response) => {
        response.json({ "super": "app" });
    });

package.json:

    {
        "name": "super-app-node",
        "dependencies": {
            "express": "^4.17.1"
        }
    }

Dockerfile:

    # Download the slim version of node
    FROM node:17-slim

    # Set the work directory to app folder. 
    # We will be copying our code here
    WORKDIR /node

    #Copy package.json file in the node folder inside container
    COPY package.json .

    # Install the dependencies in the container
    RUN npm install

    # Copy the rest of the code in the container
    COPY . .

    # Run the node server with server.js file
    CMD ["node", "server.js"]

    # Expose the service over PORT 3000
    EXPOSE 3000

Here we are creating a Node application that returns JSON when we hit localhost:3000/super-app in the browser. Now, we are not directly going to run the project from this folder.

Instead, go back to your super-app folder and append the below lines to your docker-compose.yml file:

      super-app-node:
        build: ./node
        ports:
          - "3000:3000"

We are simply mentioning to create a service named super-app-node. We are also mapping the container port to the host port 3000. 

Finally run the below command to run your two containers (MySQL and NodeJS):

    docker compose up

Now if you hit localhost:3000/super-app you will see a response {“super”:”app”}. Simultaneously your MySQL service is also. Yay! We have successfully created two containers using a docker compose file.

On to the next application. Let’s create a .NET application which interacts with the database and returns a list of strings.

### How to Configure .NET 6.0

We want the .NET application to connect with the database. It will fetch data from the database via a GET API and display it in the browser. 

To do so create a folder named dotnet inside our super-app project.

### How to Set Up the Project

To get started, install [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) if you don't already have it installed. Fire the below command to create a new dotnet application:

    dotnet new webapi --name dotnet

It will create a new .NET project with controllers and a few other files. In order to support connection to MySQL we need to add a nuget package. We will also add Microsoft.EntityFrameworkCore which is basically an ORM for connecting to the database. 

To do so execute the below commands in the newly created _._NET project:

    dotnet add package Pomelo.EntityFrameworkCore.MySql --version 6.0.1
    dotnet add package Microsoft.EntityFrameworkCore --version 6.0.4
    dotnet add package Microsoft.EntityFrameworkCore.Design --version 6.0.4

Since we no longer require the WeatherForecast.cs file, you can remove it. Instead, create two other entities in Job.cs and User.cs as below:

    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;

    namespace dotnet;
    public class User
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        public string FirstName { get; set; }
    }


    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;

    namespace dotnet;
    public class Job
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        public string Name { get; set; }
        public int UserId { get; set; }
        [ForeignKey("UserId")]
        public virtual User User { get; set; }
    }

We will also need a DbContext subclass to access these entities. Create a file name MySQLDBContext.cs and add the below content:

    using Microsoft.EntityFrameworkCore;

    namespace dotnet;
    public class MySQLDBContext : DbContext
    {
        public DbSet<User> User { get; set; }
        public DbSet<Job> Job { get; set; }
        public MySQLDBContext(DbContextOptions<MySQLDBContext> options) : base(options) { }
    }

We want to configure .NET to use this DbContext class for O/RM mapping. Navigate to your Program.cs file and replace what's there with below content:

    using dotnet;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.EntityFrameworkCore;
    using Microsoft.Extensions.Hosting;
    using Microsoft.Extensions.Configuration;

    var builder = WebApplication.CreateBuilder(args);

    // Add services to the container.
    builder.Services.AddDbContext<MySQLDBContext>(options =>
        {
        var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
        options.UseMySql(connectionString, ServerVersion.AutoDetect(connectionString));
        });

    builder.Services.AddControllers();
    // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
    builder.Services.AddEndpointsApiExplorer();
    builder.Services.AddSwaggerGen();

    var app = builder.Build();

    // Configure the HTTP request pipeline.
    if (app.Environment.IsDevelopment())
    {
        app.UseSwagger();
        app.UseSwaggerUI();
    }

    // Remove this line
    // app.UseHttpsRedirection();

    app.UseAuthorization();

    app.MapControllers();

    app.Run();

Apps within containers don’t need HTTPS redirection. Since the HTTPS should be handled by the server, remove the line `app.UseHtttpsRedirecttion();` from Program.cs: 

Note: since .NET 6.0, the Startup.cs file is removed and instead Program.cs is used for all the configurations.

Since we are using a configuration which fetches the DefaultConnection from the ConnectionStrings we will have to add it to our appsettings file. 

To achieve that set the contents of appsettings.development.json and appsettings.json files as below. Please note that we are using super-app-db as the server name since it is our MySQL container name.

    {
      "Logging": {
        "LogLevel": {
          "Default": "Information",
          "Microsoft": "Warning",
          "Microsoft.Hosting.Lifetime": "Information"
        }
      },
      "AllowedHosts": "*",
      "ConnectionStrings": {  
        "DefaultConnection": "server=super-app-db; port=3306; database=super-app; user=root; password=$SuperApp1; Persist Security Info=False; Connect Timeout=300"  
      } 
    }super-app-db

Next we will create a GET API which returns a list of Job objects in the database. To do so remove the WeatherForecastController.cs and add a UserController.cs file with below content.

    using System.Collections.Generic;
    using System.Linq;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.EntityFrameworkCore;

    namespace dotnet.Controllers
    {
        [Route("api/[controller]")]
        [ApiController]
        public class JobController : Controller
        {
            private MySQLDBContext _dbContext;  

            public JobController(MySQLDBContext context)  
            {  
                _dbContext = context;  
            }  

            [HttpGet]  
            public IList<Job> Get()  
            {  
                return (this._dbContext.Job.Include(x => x.User).ToList());  
            } 
        }
    }

We are all set code-wise. But we still need to setup our database. In order to do so we will create a User and Job table in our super-app database.

### .NET EF Tool

.NET’s Entity Framework Core provides a very convenient way to achieve it. First install the dotnet-ef CLI tool by executing the below command:

    dotnet tool install --global dotnet-ef

Once installed we will use a code first approach and create a migration of our entities which will then be pushed to our database.

    dotnet ef migrations add InitialCreate
    dotnet ef database update

The above two statements once executed will create the database, the tables within, and also setup the relationship between the two tables.

### How to Add Data to MySQL

In order to fetch data from the database, we first need to add data in the tables. Install any MySQL client to connect to the database. My personal favourite is [DBeaver](https://dbeaver.io/). 

Now, you can add data from DBeaver by first adding a connection with details like Host=super-app-db, Port=3306, User=root & password=$SuperApp1.

Once connected, navigate to the super-app database, open User table, and add a row and save the data. Similarly, navigate to the Job table, add a row, and save the data. Our database is all set now. 

#### How to Configure Docker

Once the project is setup and running it is time to configure it to run inside Docker using Dockerfile and docker compose. 

In the dotnet folder create a Dockerfile with the below contents:

    #Get the SDK image to build and publish the project
    FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env
    WORKDIR /app

    # Copy everything
    COPY . ./

    # Restore as distinct layers
    RUN dotnet restore

    # Build and publish a release
    RUN dotnet publish -c Release -o out

    # Build runtime image
    FROM mcr.microsoft.com/dotnet/aspnet:6.0
    WORKDIR /app

    #Copy the build file to the app directory
    COPY --from=build-env /app/out .
    ENTRYPOINT ["dotnet", "dotnet.dll"]

    #Expose the port for communication
    EXPOSE 80

Now go back to the docker-compose.yml file and append the below content:

      super-app-dotnet:
        build: ./dotnet
        ports:
        - "8080:80"

Here we are binding port 8080 of host machine to container’s port 80. That’s all for now. Execute the below command to fire up all the containers:

    docker compose up

Finally, hit [localhost:8080/api/job](http://127.0.0.1:8080/api/job) in a browser. The GET api will fetch the list of jobs from the database.

### How to Configure Python with Docker

By now, you might have guessed that we'll need to create a python folder in our super-app folder 😊. 

Secondly, create the three files required for our project: ai-ml.py, requirements.txt and Dockerfile with the below contents:

ai-ml.py:

    import matplotlib.pyplot as plt
    import pandas as pd
    from scipy import signal

    if __name__ == "__main__":
        print("All working good")

requirements.txt:

    pandas
    scipy
    matplotlib

Dockerfile:

    # Get the python image
    FROM python:3.7.13-slim

    # Switch to app directory
    WORKDIR /app

    # Copy the requirements in to the app
    COPY requirements.txt ./

    # Install dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy everything else
    COPY . .

    #Run the python script
    CMD [ "python", "./ai-ml.py" ]

Finally, go back to the docker-compose.yml file and add the below content:

      super-app-python:
        build: ./python

It’s as simple as that. Since it’s just a simple script, it will run once and then the container will exit. But the logs for the container will show _All working good_ printed. That’s all for Python.

### How to Configure PHP with Docker

Setting up PHP with Docker is one of the easiest parts of all. Create two files index.php and Dockerfile as below:

index.php:

    <?php echo "I am running in a container."; ?>

Dockerfile:

    # Get the php apache image
    FROM php:8.0-apache

    # Switch to app directory
    WORKDIR /var/www/html

    # Copy everything
    COPY . .

    EXPOSE 80

Lastly, add the below content to docker-compose.yml.

      super-app-php:
        build: ./php
        ports:
        - "8000:80"

Finally, fire up all the containers again with `docker compose up`. When you hit [http://localhost:8000](http://localhost:8000) a nice message saying _“I am running in a container.”_ will appear.

Here is the final [repository](https://github.com/shenanigan/super-app-docker) with all the Dockerfiles and other setup info.

## Conclusion

Docker is a wonderful containerisation tool and it’s been made more powerful with docker compose. It allows you to run multiple containers side by side without interfering with each other. You should definitely have it in your arsenal of tools.

How did you like the article? What other use cases you can think for Docker? Any feedback or comments?

If you are starting with Docker you can find more about it [here](https://arjavdave.com/2022/04/12/docker-introduction-and-cheat-sheet/).


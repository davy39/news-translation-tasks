---
title: How to Connect your Microsoft SQL Server Docker Container with Azure Data Studio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T11:22:53.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-connect-your-microsoft-sql-server-docker-container-with-azure-data-studio
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-29-at-3.52.47-AM.png
tags:
- name: mssql
  slug: mssql-3
- name: database
  slug: database
- name: Docker
  slug: docker
- name: docker image
  slug: docker-image
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Clark Jason Ngo\nThis guide shows you how to use Docker to pull a MSSQL\
  \ Server image and run it. Azure Data Studio is a cross-platform database tool that\
  \ will be using to connect our Docker container with MSSQL and execute SQL statements.\
  \ \nAt the e..."
---

By Clark Jason Ngo

This guide shows you how to use Docker to pull a MSSQL Server image and run it. Azure Data Studio is a cross-platform database tool that will be using to connect our Docker container with MSSQL and execute SQL statements. 

At the end, I will show you how to import a database to the Docker file system so that you can access it through Azure Data Studio.

Check out other related guides here:

* _[How to Connect your AWS RDS Microsoft SQL Server using Azure Data Studio](https://www.freecodecamp.org/news/cjn-how-to-connect-your-aws-rds-microsoft-sql-server-using-azure-data-studio/)_
* [_How to Import a Sample Database to your AWS RDS Microsoft SQL Server using S3_](https://www.freecodecamp.org/news/cjn-how-to-import-a-sample-database-to-your-aws-rds-microsoft-sql-server-using-s3/)

We will be touching on the technologies shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-238.png)

* Database: Microsoft SQL Server
* Container to pull mssql-server-demo: Docker
* Installer for mssql-cli: Node.js (Run-time Environment) / Node Package Manager (NPM)
* Database tool and GUI: Azure Data Studio

## Building our Environment with Docker 

### Installing Docker

Full guide for this portion [here](https://database.guide/how-to-install-sql-server-on-a-mac/): 

1. Download Docker CE (Community Edition) for Mac [here](https://store.docker.com/editions/community/docker-ce-desktop-mac?tab=description).
2. To install, double-click on the .dmg file and then drag the Docker application icon to your Application folder.

#### What is Docker?

Docker is a platform that enables software to run in its own isolated environment. SQL Server (from 2017) can be run on Docker in its own isolated container. 

Once Docker is installed, you simply download — or “pull” — the SQL Server on Linux Docker Image to your Mac, then run it as a Docker container. This container is an isolated environment that contains everything SQL Server needs to run.

### Launch Docker

Open your Docker application, it should be located in the Applications folder.

### Increase the Memory

By default, Docker will have 2GB of memory allocated to it. SQL Server needs at least 3.25GB. To be safe, increase it to 4GB if you can. Since this is just a playground, 2GB should be enough.

### Optional - in case you want to increase memory size:

1. Select Preferences from the little Docker icon in the top menu
2. Slide the memory slider up to at least 2GB
3. Click Apply & Restart

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-245.png)

![Image](cid:E87AD92D-0D8E-48A7-BE61-59CD6832E27F@hsd1.wa.comcast.net.)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-246.png)



### Download SQL Server

Open a Terminal window and run the following command.

```terminal
sudo docker pull mcr.microsoft.com/mssql/server:2019-latest
```

This downloads the latest SQL Server 2019 for Linux Docker image to your computer.

You can also check for the [latest container version](https://hub.docker.com/_/microsoft-mssql-server) on the Docker website if you wish.

### Launch Docker Image

Run the following command to launch an instance of the Docker image you just downloaded:

```terminal
docker run -d --name sql_server_demo -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=really
```

Example output:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-254.png)

### Check the Docker container (optional)

You can type the following command to check that the Docker container is running.

```terminal
docker ps
```

If it’s up and running, it should return something like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-247.png)

If you accidentally closed your Docker App, open your terminal and type

```terminal
docker start sql_server_demo
```

### Install the Node.js and NPM

Check if you have Node.js and NPM. Run the following commands in your terminal.

```terminal
node -v
npm -v
```

If you get an output with a version number, skip the rest of this section.

Then visit the Node.js website by clicking the following link:

[https://nodejs.org/en/](https://nodejs.org/en/)

Click the LTS version (the version number may be various) download button to download the Node.js package:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-249.png)

Next click and run the package after downloading. MacOS and Windows will have different installation process. Please follow the instruction to install the Node.js.

Then test again if Node.js and NPM were installed successfully by running the following commands in the terminal:

```terminal
node -v
npm -v
```

An output should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-248.png)

#### 

### Install sql-cli

Run the following command to install the sql-cli command line tool. This tool allows you to run queries and other commands against your SQL Server instance.

```terminal
npm install -g sql-cli
```

If you get a permission error, use the `sudo` command:

```terminal
sudo npm install -g sql-cli
```

### 

## Connect to MSSQL Server

Connect to your SQL Server using the mssql command, followed by the username and password parameters. Syntax: -u <username> -p <password>

```terminal
mssql -u sa -p reallyStrongPwd123
```

Your output should look like this if you successfully connected:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-250.png)

### Run a Quick Test

Run a quick test to check if you can connect to your SQL Server. Use the following SQL statement to check your SQL Server version:

```sql
SELECT @@VERSION;
```

If it’s running, you should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-251.png)

## Download an SQL Server GUI - Azure Data Studio

[Azure Data Studio](https://database.guide/what-is-azure-data-studio/) (formerly SQL Operations Studio) is a free GUI management tool that you can use to manage SQL Server on your computer. You can use it to create and manage databases, write queries, backup and restore databases, and more.

Azure Data Studio is available on Windows, Mac and Linux.

### Install Azure Data Studio

To install Azure Data Studio onto your Mac:

1. Visit the [Azure Data Studio download page](https://docs.microsoft.com/en-us/sql/azure-data-studio/download), and click the .zip file for macOS
2. Once the .zip file has finished downloading, double click it to expand its contents
3. Drag the .app file to the Applications folder (the file will probably be called _Azure Data Studio.app_)

### Connect to SQL Server

Now that Azure Data Studio is installed, you can use it to connect to SQL Server.

1. Launch Azure Data Studio. It is located in your Applications folder.
2. Enter the login credentials and other information for the SQL Server instance that you’d like to connect to:

It should look similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-259.png)

It should look similar to this:

* **Server Name**: localhost, [port number]   
**Example**: localhost, 1433
* **Authentication Type**: SQL Login
* **User name**: [your SQL Server username] or sa
* **Password**: [your SQL Server password] or reallyStrongPwd123
* **Database Name**: <default>
* **Server Group**: <default>

If you use a port other than the default 1433, click Advanced and enter it in the Port field.

Alternatively, you can append it to your server name with a comma in between. For example, if you used port 1400, type in localhost,1400.

You can now go ahead and create databases, run scripts, and perform other SQL Server management tasks.

1. Click **New Query**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-253.png)

2.     Type **SELECT @@VERSION**, then Click **Run Query**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-241.png)



You should be able to see: _Microsoft SQL Server_ in the Results.

## Importing a sample database to your SQL Server using Azure Data Studio

### Download the sample database file AdventureWorks

To get the OLTP downloads of AdventureWorks, go to this [link](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15) and choose any sample database. In my example, I choose `AdventureWorks2017.bak`. We will upload this to the S3 Bucket.

### Copying the file to your docker

Type the following command in the terminal following this syntax:

```
docker cp <location_of_file> <container_id>:/var/opt/mssql/data
```

It should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-255.png)

If you forgot your container id, use the `docker ps` command.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-258.png)

### Importing the sample database in Docker

Go to Azure Data Studio, and click the **localhost, 1443**, then choose **Restore**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-265.png)

Then choose **Backup file** as the selection for _Restore from_. Next, click the blue button on the right of _Backup file path._

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-264.png)

Look for the sample database file. It should be located in 

```terminal
/var/opt/mssql/data/AdventureWorks2017.bak
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-260.png)

Choose **Restore**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-263.png)

Check your localhost, 1443. It should generated a Database named AdventureWorks2017 and have contents such as Tables and Views. If not, right-click on localhost, 1443 and choose Refresh. You can also restart your Azure Data Studio application. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-262.png)

### Testing the sample database

1. Choose **AdventureWorks2017** from the dropdown menu.
2. Write a SQL query:

```sql
SELECT * FROM HumanResources.Department;
```

3.   Click **Run** to run the query.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-266.png)

You should have an output like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-267.png)

Congratulations! ???

Resources:

* [How to Install SQL Server on a Mac](https://database.guide/how-to-install-sql-server-on-a-mac/)

Connect with me on LinkedIn [here](https://www.linkedin.com/in/clarkngo/)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-240.png)


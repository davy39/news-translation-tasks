---
title: How to backup your MySQL database programmatically using mysql-backup4j
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T05:01:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-backup-mysql-database-programmatically-using-mysql-backup4j-2b53a1cbf9b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2l8ivsdetW149P5ZT2rUEQ.jpeg
tags:
- name: database
  slug: database
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Seun Matt

  In this article, we’re going to be looking at mysql-backup4j, a very flexible Java
  library that we can use to back-up our database periodically.

  Once our app is in production, we can’t afford to not have a timely backup in case
  of eventu...'
---

By Seun Matt

In this article, we’re going to be looking at [mysql-backup4j](https://github.com/SeunMatt/mysql-backup4j), a very flexible Java library that we can use to back-up our database periodically.

Once our app is in production, we can’t afford to not have a timely backup in case of eventualities. Usually, what makes the process somewhat arduous is if we have to manually trigger the process all the time.

Imagine a scenario in which we have both automated and manual processes of database backup — that’s what we’re about to do.

### 2. Dependency Installation

Let’s add the dependency to our project’s _pom.xml_:

```
<dependency>   <groupId>com.smattme</groupId>   <artifactId>mysql-backup4j</artifactId>   <version>1.0.1</version></dependency>
```

The latest version can be found [here](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22com.smattme%22%20a%3A%22mysql-backup4j%22).

### 3. Exporting MySQL Database Programmatically

Exporting a MySQL database programmatically is very straightforward with mysql-backup4j. We only need to instantiate it and pass it a Java _Properties_ object that has the right configuration properties set:

```
//required properties for exporting of db Properties properties = new Properties(); properties.setProperty(MysqlExportService.DB_NAME, "database-name"); properties.setProperty(MysqlExportService.DB_USERNAME, "root"); properties.setProperty(MysqlExportService.DB_PASSWORD, "root"); 
```

```
//properties relating to email config properties.setProperty(MysqlExportService.EMAIL_HOST, "smtp.mailtrap.io"); properties.setProperty(MysqlExportService.EMAIL_PORT, "25"); properties.setProperty(MysqlExportService.EMAIL_USERNAME, "mailtrap-username"); properties.setProperty(MysqlExportService.EMAIL_PASSWORD, "mailtrap-password");properties.setProperty(MysqlExportService.EMAIL_FROM, "test@smattme.com"); properties.setProperty(MysqlExportService.EMAIL_TO, "backup@smattme.com"); 
```

```
//set the outputs temp dir properties.setProperty(MysqlExportService.TEMP_DIR, new File("external").getPath()); 
```

```
MysqlExportService mysqlExportService = new MysqlExportService(properties); mysqlExportService.export();
```

From the snippet above, we created a new _Properties_ object and then added the required properties for the database connection, which are: the database name, username, and password.

**Supplying just these properties will make _mysql-backup4j_ assume that the database is running on _localhost_ at port _3306_**_._ It will, therefore, attempt connection using these values alongside the supplied username and password.

At this point, the library can export our database and generate a zip file containing the SQL dump file. The file is named in the format:

```
randomstring_day_month_year_hour_minute_seconds_database_name_dump.zip
```

Since we have supplied complete email credentials as part of the properties used to configure it, the zipped database dump will be sent via email to the configured address. **If no email config is set, then nothing happens after backup.**

Another important config that we set is the _TEMP_DIR;_ this is the directory that will be used by the library to temporarily store the generated files while still processing. **This _dir_ should be writable by the running program**.

The _TEMP_DIR_ will be automatically deleted once the backup operation is complete. Sweet and simple right? Yeah.

### 4. Sending Generated Zipped File to any Cloud Storage

Though the library can send the backup to a pre-configured email address, it also provides a means for us to get the generated file as a Java _File_ object so we can do whatever we want with it.

For us to achieve that, we’ve got to add this configuration property:

```
//... properties.setProperty(MysqlExportService.PRESERVE_GENERATED_ZIP, "true");
```

This property instructs _mysql-backup4j_ to preserve the generated zip file so that we can access it:

```
File file = mysqlExportService.getGeneratedZipFile();
```

Now that we have a file object, we can upload it to any cloud storage of our choice using appropriate SDKs and libraries.

**Once we’re done, we have to manually clear the zip file from the _TEMP_DIR_ by calling:**

```
mysqlExportService.clearTempFiles(false);
```

This aspect is very important so we won’t have redundant files in our local storage. If we want to get the raw exported SQL dump as a String, we only need to call this method:

```
String generatedSql = mysqlExportService.getGeneratedSql();
```

I love the flexibility of this library. Other properties that can be set are:

```
properties.setProperty(MysqlExportService.DELETE_EXISTING_DATA, "true"); properties.setProperty(MysqlExportService.DROP_TABLES, "true");properties.setProperty(MysqlExportService.ADD_IF_NOT_EXISTS, "true"); properties.setProperty(MysqlExportService.JDBC_DRIVER_NAME, "root.ss");properties.setProperty(MysqlExportService.JDBC_CONNECTION_STRING, "jdbc:mysql://localhost:3306/database-name");
```

_DELETE_EXISTING_DATA_ will add a _DELETE * FROM table_ SQL statement before an _INSERT INTO table_ SQL statement(s).

_DROP_TABLES_ will add a _DROP TABLE IF EXISTS_ SQL statement before _CREATE TABLE IF NOT EXISTS_ statement.

_ADD_IF_NOT_EXISTS_ which is by default _true_ will add an _IF NOT EXISTS_ clause to _CREATE TABLE_ statements.

We can specify the _JDBC_DRIVER_NAME_ and the _JDBC_CONNECTION_STRING_ also via the properties.

If our database happens to be running on another host or port other than _localhost:3306_ then we can use the JDBC_CONNECTION_STRING property to configure the connection. The DB_NAME will be extracted from the supplied connection string.

**We can automate this process by using Java job schedulers like [quartz](http://www.quartz-scheduler.org/)** or other means. Moreover, in a typical web application, we can just create a path for it that will trigger the backup process in a _Service_ or a _Controller_.

We can even integrate it into a web application such that the backup will be triggered when the database has a significant record update. The possibilities are limited only by our creativity.

### 5. Importing the Database Dump

Yep! We’ve been able to backup our database and lock it away in a secure vault. But how do we import the database and do a restoration?

First, we have to unzip the generated zip file and extract the SQL dump into a folder. Then we can use database clients like [HeidiSQL](https://www.heidisql.com/) and [Adminer](https://www.adminer.org/) to import the database. Using a database manager client will provide a visual aid and other great tools that come with it.

However, let’s say we find ourselves in need of restoring the database programmatically, within the app, while it’s still running.

All we need to do is read the content of the generated SQL dump as a String and pass it to the _MySqlImportService_ of the library with minimum configurations:

```
String sql = new String(Files.readAllBytes(Paths.get("path/to/sql/dump/file.sql")));
```

```
boolean res = MysqlImportService.builder() .setDatabase("database-name") .setSqlString(sql).setUsername("root") .setPassword("root") .setDeleteExisting(true).setDropExisting(true) .importDatabase(); 
```

```
assertTrue(res);
```

From the snippet above, we read the SQL from a file system, and then we used the _MySqlImportService_ to perform the import operation.

We configured _MySqlImportService_ to delete any existing content in the table and to drop existing tables. We can always fine tune these parameters to suit our needs. The service will return true on successful operation or false otherwise.

What if our database is running on another server and port other than localhost:3306? We can configure that as well using the _setJdbcConnString()_ method.

Although we read the SQL file from a local file system, if we’re in a web interface, we can actually provide an interface that will allow the file be selected from the file system. Then the content can be read and sent as an HTTP POST request to the server.

### 6. Conclusion

Wheew! That’s some productivity tool we’ve just looked at. Remember to star mysql-backup4j on [Github](https://github.com/SeunMatt/mysql-backup4j) if you liked it.

Now, go and utilize it in your project. Questions? Contributions? Appreciation? Kindly drop them in the comment section below.

**Read my other technical posts and views of life from [https://smattme.com](https://smattme.com)**

> _If you find this post helpful, learned anything at all, clap for the article and share it with your friends on Facebook and Twitter. Be proud of the quality content you read._

_Originally published at [smattme.com](https://smattme.com/blog/technology/how-to-backup-mysql-database-programmatically-using-mysql-backup4j)._


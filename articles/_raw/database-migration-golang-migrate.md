---
title: How to Perform Database Migrations using Go Migrate
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-26T23:17:14.000Z'
originalURL: https://freecodecamp.org/news/database-migration-golang-migrate
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Blue-and-Pink-3D-Elements-Student-Part-Time-Graphic-Designer-Video-Resume-Talking-Presentation.png
tags:
- name: data migration
  slug: data-migration
- name: database
  slug: database
- name: golang
  slug: golang
seo_title: null
seo_desc: "By Rwitesh Bera\nSince its introduction, the programming language Go (also\
  \ known as Golang) has become increasingly popular. It is known for its simplicity\
  \ and efficient performance, similar to that of a lower-level language such as C++.\
  \ \nWhile workin..."
---

By Rwitesh Bera

Since its introduction, the programming language Go (also known as Golang) has become increasingly popular. It is known for its simplicity and efficient performance, similar to that of a lower-level language such as C++. 

While working with a database, schema migration is one of the most important tasks that developers do throughout the project lifecycle. In this article, I will explain what database migration is and how to manage it using [go-migrate](https://github.com/golang-migrate/migrate).

## What is a Database Migration?

A database migration, also known as a schema migration, is a set of changes to be made to a structure of objects within a relational database. 

It is a way to manage and implement incremental changes to the structure of data in a controlled, programmatic manner. These changes are often reversible, meaning they can be undone or rolled back if required. 

The process of migration helps to change the database schema from its current state to a new desired state, whether it involves adding tables and columns, removing elements, splitting fields, or changing types and constraints. 

By managing these changes in a programmatic way, it becomes easier to maintain consistency and accuracy in the database, as well as keep track of the history of modifications made to it.

## Setup and Installation

[migrate](https://github.com/golang-migrate/migrate) is a CLI tool that you can use to run migrations. You can easily install it on various operating systems such as Linux, Mac and Windows by using package managers like curl, brew, and scoop, respectively. 

For more information on how to install and use the tool, you can refer to the official documentation.

To install the migrate CLI tool using [scoop](https://scoop.sh/) on Windows, you can follow these steps:

```bash
$ scoop install migrate
```

To install the migrate CLI tool using **curl** on Linux, you can follow these steps: 

```bash
$ curl -L https://packagecloud.io/golang-migrate/migrate/gpgkey| apt-key add -
$ echo "deb https://packagecloud.io/golang-migrate/migrate/ubuntu/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/migrate.list
$ apt-get update
$ apt-get install -y migrate
```

To install the migrate CLI tool using on Mac, you can follow these steps: 

```bash
$ brew install golang-migrate
```

## How to Create a New Migration

Create a directory like `database/migration` to store all the migration files.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-263.png)
_Source files structure in GoLand IDE_

Next, create migration files using the following command:

```bash
$ migrate create -ext sql -dir database/migration/ -seq init_mg
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-267.png)
_Terminal output displaying successful creation of migration_

You use `-seq` to generate a sequential version and `init_mg` is the name of the migration.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-269.png)
_Source files structure in GoLand IDE_

A migration typically consists of two distinct files, one for moving the database to a new state (referred to as "up") and another for reverting the changes made to the previous state (referred to as "down"). 

The "up" file is used to implement the desired changes to the database, while the "down" file is used to undo those changes and return the database to its previous state.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Database-migration.jpg)
_Flow of database migration_

The format of those files for SQL are:

```bash
{version}_{title}.down.sql
{version}_{title}.up.sql
```

When you create migration files, they will be empty by default. To implement the changes you want, you will need to fill them with the appropriate SQL queries.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-282.png)
_SQL queries for migrating data_

### How to Run Migration Up

In order to execute the SQL statements in the migration files, migrate requires a valid connection to a Postgres database. 

To accomplish this, you will need to provide a connection string in the proper format.

```bash
$ migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" -verbose up
```

Now in your Postgres shell, you can check newly created tables by using the following commands:

```bash
\d+

\d+ table_name DESCRIBE TABLE
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-286.png)
_Displaying table data in Postgres_

### How to Rollback Migrations

If you want to revert back the migration, you can do that using the following `down` tag:

```bash
$ migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" -verbose down
```

It will delete the `email` column from both tables as mentioned in the `000002_init_mg.up.sql` file.

Now, let's check the database and see if `email` has been deleted or not:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot_20230126_102731.png)
_Displaying updated table data in Postgres_

### How to Resolve Migration Errors

If a migration contains an error and is executed, migrate will prevent any further migrations from being run on the same database. 

An error message like `Dirty database version 1. Fix and force version` will be displayed, even after the error in the migration is fixed. This indicates that the database is "dirty" and needs to be investigated. 

It is necessary to determine if the migration was applied partially or not at all. Once you've determined this, the database version should be forced to reflect its true state using the force command.

```bash
$ migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" force <VERSION>
```

### How to Add Commands in a Makefile

```makefile
migration_up: migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" -verbose up

migration_down: migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" -verbose down

migration_fix: migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" force VERSION
```

Now, you can run `$ make migration_up` for 'up', `$ make migration_down` for 'down', and `$ make migration_fix` to fix the migration issue. 

Before running the makefile, ensure that the correct version number is included in the `migration_fix` command.

## Conclusion

Migration systems typically generate files that can be shared across developers and multiple teams. They can also be applied to multiple databases and maintained in version control. 

Keeping a record of changes to the database makes it possible to track the history of modifications made to it. This way, the database schema and the application's understanding of that structure can evolve together.

That concludes our discussion on database migration. I hope you found the information to be useful and informative. 

If you enjoyed reading this article, please consider sharing it with your colleagues and friends on social media. Additionally, please follow me on [Twitter](https://twitter.com/RwiteshBera/) for more updates on technology and coding. Thank you for reading!


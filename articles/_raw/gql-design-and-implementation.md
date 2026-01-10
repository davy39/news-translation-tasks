---
title: How I Created a SQL-like Language to Run Queries on Local Git Repositories
subtitle: ''
author: Amr Hesham
co_authors: []
series: null
date: '2023-10-26T17:00:00.000Z'
originalURL: https://freecodecamp.org/news/gql-design-and-implementation
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/gitql_banner.png
tags:
- name: Git
  slug: git
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Hello everyone! I''m a Software engineer who''s interested in low-level
  programming, compilers, and tool development.

  Three months ago I decided to learn the Rust programming language and build a Git
  client that focuses on simplicity and productivity.

  ...'
---

Hello everyone! I'm a Software engineer who's interested in low-level programming, compilers, and tool development.

Three months ago I decided to learn the Rust programming language and build a Git client that focuses on simplicity and productivity.

‌I started to think about how I could build the Git client to provide some unique and useful features.

For example, I like the analysis page on GitHub that tells you how many commits each developer has made and how many lines they've inserted or deleted. But what if I want to get this analysis for some period of time, or order everything by inserted lines and not number of commits? Or order them by how many commits were made by week or month?

You can add a custom sorting option for the client, right? But I started thinking about how I could make it more dynamic. This motivated me to wonder if I could run SQL-like queries on the local .git files so I could query any information I wanted.

So imagine if you could run a query like this on your local git repositories:

```sql
SELECT name, COUNT(name) AS commit_num FROM commits GROUP BY name ORDER BY commit_num DESC LIMIT 10
```

I have implemented this idea with a project I made called **GQL** (Git Query Language). And in this article, I'm going to show you how I designed and implemented the functionality.

## How Can You Take a SQL-like Query and Run it on .git Files?

The first idea I had was to use SQLite. But there were some problems I couldn't resolve.

For example, I couldn't customize the syntax, and I didn't want to read .git files and store them on a SQLite database and then perform the query. I wanted everything to run on the fly.

I also wanted to be able to use not only the SELECT, DELETE, and UPDATE commands but also provide commands related to Git like `push`, `pull`, and so on.

I've created different tools like compilers before, so why not create a SQL-like language from scratch and make it perform queries on the fly and see if it works?

## How I Designed and Implemented a Query Language from Scratch

I wanted to start small by only supporting the `SELECT` command without advanced features such as aggregations, grouping, joining, and so on.

So I planned to parse the query into a data structure that would make it easy to perform validation and evaluation on it (like type checking and displaying helpful error messages if anything went wrong). After that, I would pass this data structure to the evaluator that would apply the query on my .git files.

### Choosing a data structure to use

The best data structure for this case is to represent the query using an [A**bstract Syntax Tree**](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (AST). This is a very common data structure used in compilers because it's fixable and make it easy to traverse and compose nodes inside others.

Also in this case, I didn't need to keep all the information about the query, only the information that needed for the next steps (this is why it's called Abstract).

### Deciding what validation to perform

The most important validation in this case would be type checking to make sure each value is valid and used in the correct place.

For example, what if the query wanted to multiply text by other text – would this be valid?

```sql
SELECT "ONE" * "TWO"
```

The multiplication operator expects both sides to be a number. So in this case, I wanted to inform the user that their query is invalid and try to help them understand the problem as much as possible.

So how would that work? When I see an operator like `*`, you need to check both sides to see if the values are valid types for this operator or not. If not then, report a message like this:

```sql
SELECT "ONE" * "TWO"
-------------^

ERROR: Operator `*` expects both sides to be Number type but got Text.
```

Beside operators, I knew that I needed to check whether each identifier was a table, field, alias of a function name, or if it should be undefined. I also needed to report an error if, for example, a branches table contained only 2 fields like the example below:

```sql
Branches {
   Text name,
   Number commit_count,
}
```

So I created a table that contained representations for all tables and fields so I could easily perform type checking. If the user tried to select a field which was undefined in this schema, then it reported an error:

```sql
SELECT invalid_field_name FROM branches
-------------^

Error: Field `invalid_field_name` is not defined in branches table.
```

I had to make sure the same checks would be performed on conditions, function names, and arguments. Then, if everything was properly defined and had the correct types, the AST would be valid and we could go to the next step.

### What happens after validating the Abstract Syntax Tree?

After making sure everything was valid, it was time to evaluate the query and how it fetched the result.

To do that, I just traversed the syntax tree and evaluated each node. After finishing, I should have the correct result in a list.

Let's go through that process step by step to see how it works.

For example, in a query like this:

```sql
SELECT * FROM branches WHEER name LIKE "%/main" ORDER BY commit_count LIMIE BY 5
```

The AST representation will look like this:

```python
AbstractSyntaxTree {
  Select(*, "branches") 
  Where(Like(name, "%/main"))
  OrderBy(commit_count)
  Limit(5) 
}
```

Now we need to traverse and evaluate each node but in a specific order. We don't just go start to end or end to start because we need to do this in the same order that SQL would do it to get the same result.

For example in SQL, the `WHERE` statement must be executed before `GROUP BY`, and `HAVING` must be executed after.

In the above example, everything is in the correct order to execute, so let's see what each statement will do.

* `Select(*, "branches")`
    

This will select all the fields from the table with the name `branches` and push them to a list – let's call it `objects`. But how can I select them from the local repository?

All information about commits, branches, tags, and so on is stored by Git on files inside a folder called `.git` in each repository. One option is to write a full parser from scratch to extract the needed information. But using a library to do this instead worked for me.

I decided to use the libgit2 library to perform this task. It's a pure C implementation of the Git core methods, so you can read all the information you need and to use it from Rust. There is a crate (Rust Library) created by the Rust official team called `git2`, so you can get the branch information easily like this:

```rust
let local_branches = repo.branches(Some(BranchType::Local));
let remote_branches = repo.branches(Some(BranchType::Remote));
let local_and_remote_branches = repository.branches(None);
```

and then iterate over each branch to get its information and store it like this:

```rust
for branch in local_and_remote_branches {
   // Extract information from branch and store it
}
```

Now we end up with list of all branches that we'll use in the next steps.

* `Where(Like(name, "%/main"))`
    

This will filter the objects list and remove all items that do not match the conditions – in our case, those ending with "/main".

* `OrderBy(commit_count)`
    

This sorts the objects list by the value of the field `commit_count`.

* `Limit(5)`
    

This takes only the first five items and removes the rest from the objects list.

That's it! And now we end up with a valid result, which you can see below:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/gql_demo.gif align="left")

The examples below are valid and run correctly:

```sql
SELECT 1
SELECT 1 + 2
SELECT LEN("Git Query Language")
SELECT "One" IN ("One", "Two", "Three")
SELECT "Git Query Language" LIKE "%Query%"

SELECT commit_count FROM branches WHERE commit_count BETWEEN 0 .. 10

SELECT * FROM refs WHERE type = "branch"
SELECT * FROM refs ORDER BY type

SELECT * FROM commits
SELECT name, email FROM commits
SELECT name, email FROM commits ORDER BY name DESC
SELECT name, email FROM commits WHERE name LIKE "%gmail%" ORDER BY name
SELECT * FROM commits WHERE LOWER(name) = "amrdeveloper"
SELECT name FROM commits GROUP By name
SELECT name FROM commits GROUP By name having name = "AmrDeveloper"

SELECT * FROM branches
SELECT * FROM branches WHERE is_head = true
SELECT name, LEN(name) FROM branches

SELECT * FROM tags
SELECT * FROM tags OFFSET 1 LIMIT 1
```

### How to support running on multiple repositories at the same time

After I published GQL, I got amazing feedback from people. I also got some feature requests, like wanting support for multiple repositories and filtering by repository path.

I thought this was a great idea, because I could get analysis for multiple projects and also because I could do it on multiple threads. It didn't seem like it would be very hard to implement, either.

So after finishing the validation step for the AST, it's time for the evaluation step but instead of evaluating it once, it will be evaluated once for each repository and then merging all results back in one list.

But what about supporting the ability to filter by repository path?

That was pretty easy. Do you remember the branches table schema? All I needed to do was introduce a new field with name `repository_path` to represent the repository local path for this branch and introduce it to other tables too.

So the final schema will look like this:

```sql
Branches {
   Text name,
   Number commit_count,
   Text repository_path,
}
```

Now we can run a query that uses this field:

```sql
SELECT * FROM branches WHERE repository_path LIKE "%GQL"
```

And that's it! 😉

### Thanks for reading!

If you liked the project, you can give it a star ⭐ on [github.com/AmrDeveloper/GQL](https://github.com/AmrDeveloper/GQL).

You can check the website [**github.io/GQL**](https://amrdeveloper.github.io/GQL/) for how to download and use the project on different operating systems.

The project is not done yet – this is just the start. Everyone is welcome to join and contribute to the project and suggest ideas or report bugs.

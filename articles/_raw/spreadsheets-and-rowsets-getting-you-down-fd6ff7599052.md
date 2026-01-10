---
title: Spreadsheets getting you down? Converting row data to JSON trees is a breeze.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-30T05:41:28.000Z'
originalURL: https://freecodecamp.org/news/spreadsheets-and-rowsets-getting-you-down-fd6ff7599052
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5Yrv4yG9LUeSmYrvZ_ZUMQ.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jeff M Lowery

  Like many of you, I often have to take the result of SQL queries and convert the
  rowsets to JSON data objects. Sometimes I have to do the same with CSV files from
  spreadsheets. The transformation process can be a hassle, though anyon...'
---

By Jeff M Lowery

Like many of you, I often have to take the result of [SQL queries](http://www.sqlcourse.com/intro.html) and convert the rowsets to [JSON data objects](http://www.json.org/). Sometimes I have to do the same with CSV files from spreadsheets. The transformation process can be a hassle, though anyone can do it. Yet, it can be time-consuming and error-prone. This post will show you how to use the [**treeize**](https://www.npmjs.com/package/treeize) Node.js package to simplify the process in very few lines of code.

Before going further, I’ll first need a dataset to base some examples on. The domain will be **Books**, which lend themselves to all sorts of categorization. I will use a fake data generator called [casual](https://github.com/boo1ean/casual), which I previously used for mocks in my post on [GraphQL testing](https://medium.freecodecamp.org/mocking-graphql-with-graphql-tools-42c2dd9d0364).

The book data will be of the following structure:

```js
casual.define('book', () => {
    const author = casual.random_element(authors);
    
const book = {
        first_name: author.first,
        last_name: author.last,
        title: casual.random_element(author.titles),
        category: casual.random_element(author.category)
    }

return book;
});
```

Every time I request a `casual.book` I get a book with a new set of values. It’s not entirely random. The generator uses some [predefined data](https://github.com/JeffML/rowsets2json/blob/master/src/mocks/index.js) for well-known authors, and more-or-less randomly generated data for other authors. Here’s a sample:

```json
{ dataset:
   [ { first_name: 'Barbara',
       last_name: 'Cartland',
       title: 'The Pirate and the Piano Teacher',
       category: 'thriller' },
     { first_name: 'Carlie',
       last_name: 'Haley',
       title: 'Digitized Global Orchestration',
       category: 'engineering' },
     { first_name: 'Arthur',
       last_name: 'Doyle',
       title: 'The Case of the Spotted Dick',
       category: 'mystery' },
     { first_name: 'Reinhold',
       last_name: 'Gutmann',
       title: 'Managed Directional Benchmark',
       category: 'management' },
     { first_name: 'Isaac',
       last_name: 'Asimov',
       title: 'Once in a Venusian Sun',
       category: 'science fiction' },
     { first_name: 'R. L.',
       last_name: 'Stein',
       title: 'Why are You Scared of Me?',
       category: 'childrens books' },
     { first_name: 'Alicia',
       last_name: 'Cruickshank',
       title: 'Balanced Local Database',
       category: 'engineering' },
     { first_name: 'Chase',
       last_name: 'Runte',
       title: 'Ergonomic Tertiary Solution',
       category: 'engineering' } ] }
```

If you’re interested in how this data was generated, the full source code used in this post can be found [here](https://github.com/JeffML/rowsets2json). For a little bit of added realism, this generated data will be thrown into an [in-memory SQL database](https://www.npmjs.com/package/alasql) for later retrieval. Here’s the format of the results for the SQL query:

```sql
SELECT title, category, first_name, last_name
FROM book
JOIN author ON author.id = book.author
```

This format is, for all intents and purposes, identical to the format of the **dataset** shown just previously, for example:

```json
[ { title: 'Proactive Regional Forecast',
    category: 'mystery',
    first_name: 'Arthur',
    last_name: 'Doyle' },
  { title: 'More Scary Stuff',
    category: 'suspense',
    first_name: 'Steven',
    last_name: 'King' },
  { title: 'Scary Stuff',
    category: 'occult',
    first_name: 'Steven',
    last_name: 'King' },
  { title: 'Persistent Neutral Info Mediaries',
    category: 'management',
    first_name: 'Maegan',
    last_name: 'Frami' },
  { title: 'Enhanced Background Frame',
    category: 'engineering',
    first_name: 'Winifred',
    last_name: 'Turner' },...
```

The main difference between the dataset and the rowset is that when populating the database from the casual-generated data, I eliminated duplicate authors (by name) and book titles (by category):

```js
const addEntities = (dataset) => {
    dataset.forEach(d => {
        d.title = d.title.replace(/'/, "''")

        const stmt =
            `
            IF NOT EXISTS (
                select * from author
                where first_name = '${d.first_name}'
                and last_name = '${d.last_name}')
            INSERT INTO author (first_name, last_name) VALUES('${d.first_name}', '${d.last_name}');
            IF NOT EXISTS (
                select * from book
                where title = '${d.title}'
                and category = '${d.category}')
            INSERT INTO book (title, category, author) VALUES('${d.title}', '${d.category}',
            (select id from author where first_name ='${d.first_name}' and last_name = '${d.last_name}'))
            `
        try {
            alasql(stmt)
        } catch (e) {
            console.error(stmt);
            throw (e);
        }

    })
};
```

### Converting to JSON

![Image](https://cdn-media-1.freecodecamp.org/images/5eHzM7anyF1JlIGM11bcKtslW6D1MVQ2b66g)
_Gratuitous kitten picture._

You might notice that the dataset results were in JSON format already. What this post aims for, though, is to build a containment hierarchy that shows the relationships between authors, books, and categories in a concise way. That’s not the case with the rowset values, where the results are glorified key-value pairs, where each pair is a column name and value from a table row.

So, for example, say I want to list authors, the categories they write in, and the titles of books in those categories that they authored. I want to show each category just once, and each book within each category should be listed only once, also.

This is a pretty common type of reducing operation that is often applied to rowset data. One way to conquer the problem is to declare a container object, then populate it by looping through the rowsets. A typical implementation might be:

```js
const handrolled = (rs) => {
    const authors = {}

    rs.forEach(r => {
        const authname = [r.last_name, r.first_name].join(',');
        if (!authors[authname]) {
            authors[authname] = {
                categories: {}
            }
        }
        var author = authors[authname];
        if (!author.categories[r.category]) {
            author.categories[r.category] = {
                titles: []
            }
        }
        var category = author.categories[r.category]
        if (!category.titles.includes(r.title)) {
            category.titles.push(r.title)
        }
    })

    return authors;
}
```

The `handrolled()`method gets a bit hairy the deeper the hierarchy. Local variables are used to reduce long path lengths. We have to keep the meta-structure in mind to write the proper initializations of properties in the JSON object. What could be simpler?

The results returned are:

```json
...
        "Doyle,Arthur": {
            "categories": {
                "thriller": {
                    "titles": [
                        "The Case of the Spotted Dick",
                        "The Case of the Mashed Potato"
                    ]
                },
                "mystery": {
                    "titles": [
                        "The Case of the Spotted Dick"
                    ]
                }
            }
        },
        "Asimov,Isaac": {
            "categories": {
                "science": {
                    "titles": [
                        "Once in a Venusian Sun",
                        "Total Multi Tasking Forecast"
                    ]
                },
                "general interest": {
                    "titles": [
                        "Total Multi Tasking Forecast",
                        "Once in a Venusian Sun",
                        "Fourth Foundation"
                    ]
                }
            }
        },
        "Kilback,Bradley": {
            "categories": {
                "management": {
                    "titles": [
                        "Mandatory Solution Oriented Leverage"
                    ]
                },
                "engineering": {
                    "titles": [
                        "Multi Layered Fresh Thinking Framework",
                        "Total Scalable Neural Net",
                        "Mandatory Solution Oriented Leverage"
                    ]
                },
                "reference": {
                    "titles": [
                        "Multi Layered Fresh Thinking Framework"
                    ]
                }
            }
        },...
```

### Building a tree with Treeize

The npm module treeize is designed to simplify the conversion of rowsets to structured JSON data through the use of descriptive keys. Installation through npm is per usual:

```bash
npm install --save treeize
```

#### JSON Rowsets

Treeize is able to recognize reoccurring patterns in the rowsets. It transforms them according to how the key names are defined in metadata passed in as the seed structure. Here’s the code:

```js
import Treeize from 'treeize'

const treeized = rs => {
    var authors = new Treeize();

    const seed = rs.map(r => ({
        name: [r.last_name, r.first_name].join(', '),
        'categories:type': r.category,
        'categories:titles:name': r.title
    }))

    authors.grow(seed);
    return authors.getData();
}
```

This is about a dozen lines of code compared to double that for the hand-rolled version. Notice the key values used in the mapping operation. Treeize recognizes plurals as collections, so `categories`and `titles`will be arrays. The colons (‘:’) in the names indicate nesting. `Type`will be a property of an object in the array of categories, and `name`will be a property in all objects in titles.

The tree is built when `authors.grow(seed)` is called, and the results retrieved through `authors.getData()`. However, it doesn’t _quite_ yield the same results as what we had from the hand-rolled method:

```json
...,
{
    "name": "Glover, Ashley",
    "categories": [
        {
            "type": "engineering",
            "titles": [
                {
                    "name": "Intuitive Full Range Capacity"
                },
                {
                    "name": "Organic Encompassing Core"
                }
            ]
        },
        {
            "type": "reference",
            "titles": [
                {
                    "name": "Distributed Client Server Service Desk"
                },
                {
                    "name": "Organic Encompassing Core"
                }
            ]
        },
        {
            "type": "management",
            "titles": [
                {
                    "name": "Organic Encompassing Core"
                }
            ]
        }
    ]
},...
```

One notable difference is that categories are not named objects (as before), but objects with a `name` property. `Title` is also not just an array of strings, but an array of objects with `name`as the title. Treeize interprets `categories` and `titles` as arrays of objects, not as maps (or arrays of primitives). For most use cases, this is not much of an issue. But, if you need to find a category by name quickly (rather than iterate through an array of categories), then you can take care of that [through a couple of reduce operations](https://gist.github.com/JeffML/1bbe228f271765d3ee3a917196e8a81c) to arrive at the same structure as before:

```json
,...   
    "Doyle, Arthur": {
        "categories": {
            "mystery": {
                "titles": [
                    "The Case of the Spotted Dick",
                    "Pre Emptive Needs Based Approach",
                    "The Case of the Mashed Potato"
                ]
            },
            "thriller": {
                "titles": [
                    "The Case of the Mashed Potato",
                    "The Pound Puppies of the Baskervilles"
                ]
            }
        }
    },...
```

#### Spreadsheets

Sometimes data comes from spreadsheets rather than relational databases. Treeize is adept at handling this case, too. Instead of using descriptive keys as we did with rowset data in JSON format, the same descriptive format is used as column values in a header row:

```js
var seed = [
['name', 'categories:type', 'categories:titles:name'], 
['Doyle, Arthur', 'mystery', 'The Adventure of the Gyring Gerbils'],
['Schuppe, Katarina', 'engineering', 'Configurable Discrete Locks'],
['Doyle, Arthur', 'mystery', 'Holmes Alone 2'],
['Asimov, Isaac', 'science fiction', 'A Crack in the Foundation']
];

// same as before...
var authors = new Treeize();
authors.grow(seed);
return authors.getData();
```

There are [quite a few options](https://www.npmjs.com/package/treeize#1-getset-options-optional) that treeize supports, and I’ve only shown the basics. It is a powerful tool that makes light work of transforming row-based data structures.

Complete source [can be found at my GitHub](https://github.com/JeffML/rowsets2json).


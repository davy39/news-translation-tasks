---
title: How to implement Elasticsearch in Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T20:00:00.000Z'
originalURL: https://freecodecamp.org/news/go-elasticsearch
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-from-2019-11-24-22-21-41-1.png
tags:
- name: elasticsearch
  slug: elasticsearch
- name: Go Language
  slug: go
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: 'By Pramono Winata

  Today, I am going to show you how to implement Elasticsearch in Go.But of course,
  before that I am going to give a small introduction to Elasticsearch.If you have
  already gained a basic understanding of Elasticsearch, you can skip t...'
---

By Pramono Winata

Today, I am going to show you how to implement Elasticsearch in Go.  
But of course, before that I am going to give a small introduction to Elasticsearch.   
If you have already gained a basic understanding of Elasticsearch, you can skip to the next part.

## **Elasticsearch** 

Elasticsearch has been gaining a lot of popularity lately. Searching in a Relational-Database always has issues around scalability and performance. 

Elasticsearch is a NoSQL database that has been very successful in tackling those issues. It provides great scalability and performance, and one of the most prominent features is the scoring system that allows a lot of flexibility in the search results. After all, it is not called Elastic-search for no reason!

### Installing Elasticsearch

First, you will need to install Elasticsearch on your local machine. You can go to their [website](https://www.elastic.co/guide/index.html) and get the [installation guide](https://www.elastic.co/guide/en/elasticsearch/reference/7.4/install-elasticsearch.html) for it. At the time I am writing this article, I am using Elasticsearch with the version number of 7.4.2 .

Elasticsearch has been making a lot of changes in their versions, one of them being the [removal of mapping type.](https://www.elastic.co/guide/en/elasticsearch/reference/master/removal-of-types.html) So do not expect this to fully work if you are using another version of Elasticsearch.

After finishing your installation, do not forget to run your elasticsearch service, which is mentioned quite clearly on their installation guide (for linux, in short do this `./bin/elasticsearch` ).

**Make sure your elasticsearch is running** by requesting into port 9200 in your local machine.   
  
GET `localhost:9200`

Hitting it should show something like below.

```json
{
  "name": "204371",
  "cluster_name": "elasticsearch",
  "cluster_uuid": "8Aa0PznuR1msDL9-PYsNQg",
  "version": {
    "number": "7.4.2",
    "build_flavor": "default",
    "build_type": "tar",
    "build_hash": "2f90bbf7b93631e52bafb59b3b049cb44ec25e96",
    "build_date": "2019-10-28T20:40:44.881551Z",
    "build_snapshot": false,
    "lucene_version": "8.2.0",
    "minimum_wire_compatibility_version": "6.8.0",
    "minimum_index_compatibility_version": "6.0.0-beta1"
  },
  "tagline": "You Know, for Search"
}
```

If it's showing correctly then congratulations! You have successfully run your elasticsearch service in your local machine. Give yourself a clap and take a cup of coffee, since the day is still young.

### Making your first index

In Elasticsearch, index is similar to a database. Whereas before, there was table in elasticsearch called type. But since type has been removed in the current version, there are only index now.

Confused now? Don't be. In a nutshell, just think that you only need index then afterwards you just need to insert your data into Elasticsearch.  
  
Now, we are going to make an index named `students` by doing the query below.  
PUT `localhost/9200/students`

```json
{
	"settings": {
    	"number_of_shards": 1,
    	"number_of_replicas": 1
	},
   "mappings": {
       "properties": {
         "name": {
               "type": "text"
         },
         "age": {
               "type": "integer"      
         },
         "average_score": {
               "type": "float"
         }
     }
   }
}
```

If nothing goes wrong, it should respond back by giving this.

```json
{
    "acknowledged": true,
    "shards_acknowledged": true
}

```

Your index should be created. Now we will proceed to our next step: playing around with our Elasticsearch index.

### Populating your Elasticsearch

First, what we will be doing now is filling in our Elasticsearch index with documents. If you are not familiar with that definition, just know that it is very similar to rows in a database.

In a NoSQL database, it's actually possible for every document to contain different fields that don't match with the schema.

But let's not do that – let's construct our column with a schema that we have defined before. The previous API will allow you to fill the document in your index.

POST `localhost:9200/students/doc`

```json
{
	"name":"Alice",
	"age":17,
	"average_score":81.1
}

```

Your Elasticsearch should have one document by now. We will need to insert several more data into our Elasticsearch.  And of course, we are not going to insert our student data one by one - that would be quite a hassle!  
  
Elasticsearch has specifically prepared a bulk API in order to send multiple requests at once. Let's use that to insert multiple data at once.  
  
POST `/students/_bulk`

```json
{ "index":{"_index": "students" } }
{ "name":"john doe","age":18, "average_score":77.7 }
{ "index":{"_index": "students" } }
{ "name":"bob","age":16, "average_score":65.5 }
{ "index":{"_index": "students" } }
{ "name":"mary doe","age":18, "average_score":97.7 }
{ "index":{"_index": "students" } }
{ "name":"eve","age":15, "average_score":98.9 }
```

### Let's query for the data

We have finally populated our Elasticsearch with several more students' data. Now let's do what Elasticsearch is known for: we will try to search our Elasticsearch for the data that we just inserted.

Elasticsearch supports many types of search mechanisms, but for this example we will be using a simple matching query. 

Let's start our search by hitting this API:

 POST `localhost:9200/_search`

```json
{
    "query" : {
        "match" : { "name" : "doe" }
    }
}

```

You will get back your response together with the students' data that matched with your corresponding query. Now you are officially a Search Engineer!

```json
{
    "took": 608,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 2,
            "relation": "eq"
        },
        "max_score": 0.74487394,
        "hits": [
            {
                "_index": "students",
                "_type": "_doc",
                "_id": "rgpef24BTFuh7kXolTpo",
                "_score": 0.74487394,
                "_source": {
                    "name": "john doe",
                    "age": 18,
                    "average_score": 77.7
                }
            },
            {
                "_index": "students",
                "_type": "_doc",
                "_id": "sApef24BTFuh7kXolTpo",
                "_score": 0.74487394,
                "_source": {
                    "name": "mary doe",
                    "age": 18,
                    "average_score": 97.7
                }
            }
        ]
    }
}
```

## Now let's get to Go!

![Image](https://www.freecodecamp.org/news/content/images/2019/11/download--2-.png)
_Go in action!_

If you have reached this part, you should have grasped the very minimum concepts of using Elasticsearch. Now, we are going to implement Elasticsearch in Go.

A very primitive way of implementing Elasticsearch is that you can keep doing http requests into your Elasticsearch IP. But we are not going to do that. 

I found [this](https://github.com/olivere/elastic) very helpful library for implementing Elasticsearch in Go. You should install that library before you proceed in your Go modules.

### Make your struct

First of all, you will definitely need to make a struct for your Model. In this example, we are going to use the same modeling as in our previous example which in this case is the `Student` struct. 

```go
package main

type Student struct {
	Name         string  `json:"name"`
	Age          int64   `json:"age"`
	AverageScore float64 `json:"average_score"`
}
```

### Making a Client Connection

Now, let's make a function that'll allow us to initialize our ES Client connection.   
If you have a running instance of Elasticsearch outside of your localhost, you can simply change the part inside `SetURL`.

```go
func GetESClient() (*elastic.Client, error) {

	client, err :=  elastic.NewClient(elastic.SetURL("http://localhost:9200"),
		elastic.SetSniff(false),
		elastic.SetHealthcheck(false))

	fmt.Println("ES initialized...")

	return client, err

}
```

### **Data Insertion**

After that, the first thing we can do is try to insert our data into Elasticsearch via Go. We will be making a model of `Student` and inserting it into our Elasticsearch client.

```go
package main

import (
	"context"
	"encoding/json"
	"fmt"

	elastic "gopkg.in/olivere/elastic.v7"
)

func main() {

	ctx := context.Background()
	esclient, err := GetESClient()
	if err != nil {
		fmt.Println("Error initializing : ", err)
		panic("Client fail ")
	}

	//creating student object
	newStudent := Student{
		Name:         "Gopher doe",
		Age:          10,
		AverageScore: 99.9,
	}

	dataJSON, err := json.Marshal(newStudent)
	js := string(dataJSON)
	ind, err := esclient.Index().
		Index("students").
		BodyJson(js).
		Do(ctx)

	if err != nil {
		panic(err)
	}

	fmt.Println("[Elastic][InsertProduct]Insertion Successful")

}
```

### **Querying our Data**

Finally, we can do some searching. The below code might look a bit complex. But rest assured, it will make more sense to you after you go through it carefully. I will be using a basic matching query in the below example.

```go
package main

import (
	"context"
	"encoding/json"
	"fmt"

	elastic "gopkg.in/olivere/elastic.v7"
)

func main() {

	ctx := context.Background()
	esclient, err := GetESClient()
	if err != nil {
		fmt.Println("Error initializing : ", err)
		panic("Client fail ")
	}

	var students []Student

	searchSource := elastic.NewSearchSource()
	searchSource.Query(elastic.NewMatchQuery("name", "Doe"))

	/* this block will basically print out the es query */
	queryStr, err1 := searchSource.Source()
	queryJs, err2 := json.Marshal(queryStr)

	if err1 != nil || err2 != nil {
		fmt.Println("[esclient][GetResponse]err during query marshal=", err1, err2)
	}
	fmt.Println("[esclient]Final ESQuery=\n", string(queryJs))
    /* until this block */

	searchService := esclient.Search().Index("students").SearchSource(searchSource)
    
	searchResult, err := searchService.Do(ctx)
	if err != nil {
		fmt.Println("[ProductsES][GetPIds]Error=", err)
		return
	}

	for _, hit := range searchResult.Hits.Hits {
		var student Student
		err := json.Unmarshal(hit.Source, &student)
		if err != nil {
			fmt.Println("[Getting Students][Unmarshal] Err=", err)
		}

		students = append(students, student)
	}

	if err != nil {
		fmt.Println("Fetching student fail: ", err)
	} else {
		for _, s := range students {
			fmt.Printf("Student found Name: %s, Age: %d, Score: %f \n", s.Name, s.Age, s.AverageScore)
		}
	}

}
```

The query should be printed out like this:

```
ES initialized...
[esclient]Final ESQuery=
 {"query":{"match":{"name":{"query":"Doe"}}}}
```

And yes that query is what will be posted into the Elasticsearch.

The result of your query should also come out like this if you have followed my example since the very start:

```
Student found Name: john doe, Age: 18, Score: 77.700000 
Student found Name: mary doe, Age: 18, Score: 97.700000 
Student found Name: Gopher doe, Age: 10, Score: 99.900000 
```

And there you go!

That's the end of my tutorial about how to implement Elasticsearch in Go. I hope I have covered the very basic parts of using Elasticsearch in Go. 

To get further info on this topic, you should read about [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) and [Function Scoring](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html) in Elasticsearch, which in my opinion one of the best things about Elasticsearch.

And fret not, the library used in this example also supports a lot of Elasticsearch features, even the Function Scoring query in Elasticsearch.

Thanks for reading through my article! I do hope it will be useful and can help you getting started using Elasticsearch. 

> Never stop learning; knowledge doubles every fourteen months. ~Anthony J.D'Angelo


---
title: How to Build a Real-time React and Express Fullstack search engine with Postgres
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-16T19:05:00.000Z'
originalURL: https://freecodecamp.org/news/react-express-fullstack-search-engine-with-psql
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/photo-1525278070609-779c7adb7b71.jpg
tags:
- name: Express
  slug: express
- name: postgres
  slug: postgres
- name: React
  slug: react
seo_title: null
seo_desc: "By Mohammad Iqbal\nIn this tutorial we will go through and setup a full\
  \ stack search engine with React as the front end, Node and Express for the server,\
  \ and PostgreSQL for the database. \nThis search engine will be slightly more complex\
  \ than a simple ..."
---

By Mohammad Iqbal

In this tutorial we will go through and setup a full stack search engine with React as the front end, Node and Express for the server, and PostgreSQL for the database. 

This search engine will be slightly more complex than a simple text search setup. For example, a user will be able to get pluralized forms of words as well as past and present tenses of words. A search of "cats" will also return results for "cat". A search of "walked" will return a result of "walk", and so on.

Instead of starting from scratch, we can use a simple starter project:

[https://github.com/iqbal125/react-hooks-complete-fullstack](https://github.com/iqbal125/react-hooks-complete-fullstack)

You can watch a fullstack video version of this tutorial here  
[https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5](https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5)

### PostgreSQL's TS vector and TS query

To accomplish this complex search functionality we will use PostgreSQL's [built in text search functionality](https://www.postgresql.org/docs/10/datatype-textsearch.html). 

The 2 data types that will make this possible are be PSQL's `tsvector` and `tsquery` datatypes.

`tsvector`: a list of **lexemes**. A **lexeme** is a word that allows you to merge different variations of that word.  For example, a text of "walked" will be converted and saved as a lexeme of "walk". This will return results for text searches of "walk", "walking" and "walked".  

`tsquery`: is list of lexemes that are compared with tsvectors. A piece of text is first converted to a tsquery then compared with a tsvector to see if there is a match. 



![Image](https://www.freecodecamp.org/news/content/images/2019/09/image.png)

This diagram explains essentially how TS vectorization occurs. When a user submits a post, the post along with the author of the post is converted into a single array of TS vectors and saved as 1 row. 

Also duplicates are removed and the base form of the word is used as the lexeme. 

### Real World Example 

Say you submit a post with the title of "cats" and body of "fishes". 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-73.png)

"cat" will return a search result of "cats"

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-74.png)

This will also work with non standard pluralization as well, "fish" will return a result for "fishes". 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-75.png)

This also applies to present and past tenses of words. Say we have this post of "walking" and "acted": 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-76.png)

"walk" will return a search result of "walking": 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-77.png)

Same with "act" and "acted".

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-78.png)

If you want to look under the hood, the lexemes look like this in the PSQL database. 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-79.png)

The search vector column is 'cat': 1 'fish':2 'test91': 3. Notice that even though we submitted our post with the title "cats" and body "fishes", the words are converted into the root form. 

This is essentially what allows for comparisons with other forms of the word and makes this complex searching possible.  

If that sounds good we can get started with the code setup.  

### React setup

```jsx

//posts.js

.... 
const handleSearch = (event) => {
   setState({posts_search: []});
   const search_query = event.target.value
   axios.get('/api/get/searchpost', {params: {search_query: search_query} })
     .then(res => res.data.length !== 0
                    ? setState({posts_search: [...res.data]})
                    : null )
     .catch(function (error) {
       console.log(error);
       })
   }
   
....

    <TextField
      id="search"
      label="Search"
      margin="normal"
      onChange={handleSearch}
    />
    
 ...
```

We only really need 2 main parts on our front end to make this happen. The function that makes the API call to the server and the input element that fires the function on every keystroke. 

the `handleSearch()` function essentially extracts the text from the input element and sends it as a parameter in an **axios get** request.

This can easily be inserted into any React component. 

This is really it for the React setup. The real magic happens on the Server and database side.

### Database Setup

Here is the **SQL** schema for the posts. Notice that we only have one column `search_vector` of data type `TSVECTOR`. We dont have a `TSQUERY` column since the query is not stored in our database it is just used as a comparison. 

```sql
CREATE TABLE posts (
  pid SERIAL PRIMARY KEY,
  title VARCHAR(255),
  body VARCHAR,
  search_vector TSVECTOR,
  user_id INT REFERENCES users(uid),
  author VARCHAR REFERENCES users(username),
  date_created TIMESTAMP,
  like_user_id INT[] DEFAULT ARRAY[]::INT[],
  likes INT DEFAULT 0
);
```

This search vector column will contain the lexemes for the title, body and author of the post combined into 1 array. We can see how this is used on the server setup. 

### Server setup

```javascript

//Search Posts
router.get('/api/get/searchpost', (req, res, next) => {
  search_query = String(req.query.search_query)
  pool.query(`SELECT * FROM posts
              WHERE search_vector @@ to_tsquery($1)`,
    [ search_query ], (q_err, q_res) => {
    if (q_err) return next(q_err);
    res.json(q_res.rows);
  });
});

//Save posts to db
router.post('/api/post/posttodb', (req, res, next) => {
  const body_vector = String(req.body.body)
  const title_vector = String(req.body.title)
  const username_vector = String(req.body.username)

  const search_array = [title_vector,
                         body_vector, 
                         username_vector]
  
  const values = [req.body.title, 
                  req.body.body, 
                  search_array, 
                  req.body.uid, 
                  req.body.username]
  
  pool.query(`INSERT INTO
              posts(title, body, search_array, user_id, author, date_created)
              VALUES($1, $2, to_tsvector($3), $4, $5, NOW())`,
    values, (q_err, q_res) => {
    if (q_err) return next(q_err);
    res.json(q_res.rows);
  });
});

```

The search engine works because of what we do at the time we save the posts not when the search is taking place. 

You can see in our second function we start by turning our title, body and author of our post into strings then we combine them in an array called `search_array`. 

Then we use a simple SQL insert command to insert the entire post into the database. While we do this we also run the `to_tsvector()` function on our `search_array`. 

`to_tsvector()` is a given PSQL function and is what turns our array into a `tsvector` and allows for search later on. 

Then searching becomes simple at this point. We just get our text from the front end and convert it into a string. 

Then we use the `to_tsquery()` function to turn it into a `tsquery` data type. We can then use this `ts_query` to check the `search_vector` column and see if there is a match with the `@@` operator.

If yes we return the matching posts. Then the matching posts will be returned to our front end as a regular API request and will resolve as a promise. 

Since React is a Single page app the browser will not reload and the search will feel real time.  

Thanks for Reading!

> Connect with me on Twitter for more updates on future tutorials: [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)


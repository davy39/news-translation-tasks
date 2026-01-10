---
title: 'Firestore: How to stay within the limits of Firebase''s new database free
  tier'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-11T21:48:00.000Z'
originalURL: https://freecodecamp.org/news/firestoreliving
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ec5740569d1a4ca3ef8.jpg
tags:
- name: Cloud Services
  slug: cloud-services
- name: database
  slug: database
- name: Firebase
  slug: firebase
- name: Free Software
  slug: free-software
seo_title: null
seo_desc: "By Jeff M Lowery\nI recently started a personal project where I wanted\
  \ to use a database in the cloud. There are quite a few to choose from. My main\
  \ criteria was that it be something low or no cost. \nEventually I decided on Firestore,\
  \ using the Spark ..."
---

By Jeff M Lowery

[I recently started a personal project](https://www.freecodecamp.org/news/netlify-functions-firebase-and-graphql-working-together-at-last/) where I wanted to use a database in the cloud. There are quite a few to choose from. My main criteria was that it be something low or no cost. 

Eventually I decided on [Firestore](https://firebase.google.com/docs/firestore), using the [Spark Plan](https://firebase.google.com/pricing). This plan gives me 5Gb of storage, with 50K reads and 20K writes per day for free, which at the time seemed like plenty. I soon learned that a little carelessness can blow past those transaction limits pretty fast.

Firestore is a NoSQL document store database. Each NoSQL database is different and my a learning curve was steeper than expected. As you know, the best teacher is adversity, and I made my share of mistakes early on. One too many, though, and I’d hit the read or write limit of the plan, which sometimes could happen within an hour or two. Then it was time to call it a day.

Things are better now, so I offer these lessons learned:

### *Do* start with the free plan

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-198.png)
_Photo by [Unsplash](https://unsplash.com/@frankiefoto?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">frank mckenna</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Yes, it is easy to overshoot the plan’s limits, but those occurrences will force you to learn to be efficient with your reads and writes. You will become more cost-conscious of sequencing multiple database operations in an efficient way.

### Start with a small dataset

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-199.png)
_Photo by [Unsplash](https://unsplash.com/@rayhennessy?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Ray Hennessy</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

This may seem obvious, but by **small** I mean less than 100 documents total. On my project, I first created a collection with 10K documents. I later realized that I made a mistake in the data I loaded, fixed that, found another, went to fix that, but… TRANSACTION_RESOURCE_LIMIT_EXCEEDED. Welp, done for the day.

### Take time in the design of your data model

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-200.png)
_Photo by [Unsplash](https://unsplash.com/@kellysikkema?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Kelly Sikkema</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Like the carpenter’s axiom: “Measure twice, cut once”, you don’t want to be adjusting your JSON document fields and structure piecemeal. Oh, you _will_ of course, but you’ll save yourself some transactions by practicing a little foresight. Write out a schematic of documents, their fields, and their relationships first. [Visualization is the key to happiness.](https://www.freecodecamp.org/news/inserting-uml-in-markdown-using-vscode/)

### Test and verify your data loading scripts

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-201.png)
_Photo by [Unsplash](https://unsplash.com/@nasa?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">NASA</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

You’ll need scripts to populate the database from some other source. That is the time to:

* verify what you loaded is what you expected
* correctly handle the no-data case for fields

I made mistakes in both cases. First, when I loaded some string data into a document field, I hadn’t immediately noticed that those strings had quotes already, so the stored strings had embedded quotes. It didn’t seem that serious an issue, but it became a pain later when writing and testing searches on that field. Because there were a lot of documents, I spent a sizable portion of my daily write quota to clean that up.

In the second case, I discovered that Firestore has no mechanism for determining the [existence of a property in a document](https://stackoverflow.com/questions/46806860/how-to-query-cloud-firestore-for-non-existing-keys-of-documents) (there is no _undefined_ check). There _is_ an [**exists** test for documents](https://firebase.google.com/docs/firestore/query-data/get-data#get_a_document), but not for document fields. The best practice is to populate missing data fields with **null**, and then do null equivalence tests in a where clause to find documents with “missing” properties.

### What a small dataset won’t teach you

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-202.png)
_Photo by [Unsplash](https://unsplash.com/@goodfreephoto_com?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Good Free Photos</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Once you worked out kinks on the small dataset, it is time to graduate to a larger one. With more documents to process, things like query efficiency, pagination and batch requests become important.

### Read in chunks, write in chunks

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-203.png)
_Photo by [Unsplash](https://unsplash.com/@picoftasty?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Mae Mu</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

[Batch operations](https://firebase.google.com/docs/firestore/manage-data/transactions) allow for multiple read/writes on the database in a single transaction. This means that if any write operation fails, then all writes fail, and the database data retains its original state. Each operation in a batch counts toward the total read/write quotas, so as such it doesn’t help usage quotas. Also, when writing via batch operations, be aware there’s a 500 operation limit per batch.

Be careful when correlating two documents (i.e., for every A document, there is an association by reference to a B document). Don’t fetch all of one first, then iterate through the other. That’s a good way to chew up the transaction quota when debugging.

It is better to fetch a subset of the first collection, then iterate through it document by document. Associate these documents with document in the second collection by fetching **one** that matches criteria. Continue to do this until the entire first collection has been fetched. When debugging, you can verify everything looks like it is working correctly and, if not, kill the process before a lot of transactions are run.

### How to limit query results

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-204.png)
_Photo by [Unsplash](https://unsplash.com/@will0629?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Will Porada</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Firestore’s query language isn’t as richly expressive as SQL is, but there are still a number of ways to restrict your queries so that you don’t overfetch data. Although technically there is no size limit for a POST response body, in practical terms there is.

Some mechanisms for limiting query results:

**where and compound where**

You can chain multiple where clauses together, similar to adding conditional expressions to a single where clause in SQL.

```
citiesRef.where('state', '==', 'CO').where('name', '==', 'Denver');
```

**limit and ranges**

You can limit the number of documents returned by a query by using chaining a limit clause at the end of the query object.

```
let biggest = citiesRef.where('population', '>', 2500000)  .orderBy('population').limit(2);
```

You can also specify a range of records to retrieve via startAt/endAt or startBefore/endBefore constraints, which allows you to do cursor-based pagination.

```
let docRef = db.collection('cities').doc('SF');
```

```
return docRef.get().then(snapshot => {  let startAtSnapshot = db.collection('cities')    .orderBy('population')    .startAt(snapshot);  return startAtSnapshot.limit(10).get();});
```

**in array query**

You can look for specific matches in an array. This is good for enumerated values.

```
const usaOrJapan = citiesRef.where('country', 'in', ['USA', 'Japan']);
```

As demonstrated, it is possible to work within the limitations of the Spark Plan as you learn about Firestore. It’s free, which is always a good place to start.


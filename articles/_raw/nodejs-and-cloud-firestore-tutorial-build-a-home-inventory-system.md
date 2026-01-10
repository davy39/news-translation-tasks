---
title: Node.js and Cloud Firestore Tutorial – How to Build a Home Inventory System
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-30T16:26:24.000Z'
originalURL: https://freecodecamp.org/news/nodejs-and-cloud-firestore-tutorial-build-a-home-inventory-system
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/home-inventory-system-article.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Firebase
  slug: firebase
- name: '#firebase-cloud-functions'
  slug: firebase-cloud-functions
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: null
seo_desc: "By Suchandra Datta\nIn this article, you'll practice your JavaScript skills\
  \ while streamlining your household chores by creating your very own home inventory\
  \ system. \nI've often found that it's hard to keep track common household items\
  \ that I buy freq..."
---

By Suchandra Datta

In this article, you'll practice your JavaScript skills while streamlining your household chores by creating your very own home inventory system. 

I've often found that it's hard to keep track common household items that I buy frequently such as food, spices, medicine, and the like. It's annoying at best and frustrating at worst when I uncover a long-forgotten packet of chips from the depths of the cupboard. 

Tired of keeping track manually, I decided to make my own home inventory system. This system would allow me to:

* create records for each item, along with helpful information such as price and quantity
* filter items on the basis of different criteria such as price, quantity and expiration date
* sort items based on given criteria
* delete items no longer in use
* edit existing records

In this tutorial I'll walk you through the process of how I built this system. Let's get started.

## How to Define the Database Schema

[Cloud Firestore](https://firebase.google.com/docs/firestore) is a cloud-hosted, scalable, flexible NoSQL database offered by Firebase. Data is stored in documents, and documents are grouped together into collections, similar to storing pages of information in a file and keeping multiple files together in a drawer. 

Firestore offers powerful querying options ranging from simple sorting to adding limits to query results. 

For our purposes, we'll define a Collection for a specific category. Each Document will correspond to a product within that category and the contents of a Document will be each field of information along with it's data value. For example: 

```python
"Snacks" : {
	"Food_Item_1" : { "Price":P1, "Quantity":Q1, "ExpiryDate":D1},
	"Food_Item_2" : { "Price":P2, "Quantity":Q2, "ExpiryDate":D2},	
    .
    .
	"Food_Item_N" : { "Price":PN, "Quantity":QN, "ExpiryDate":DN}
}
```

Our Collection name would be Snacks, our Document names would be Food_Item_1, Food_Item_2 and so on, and the contents of each document would be price, quantity and expiry date.

## How to Get Input from the User

Let's first create a few routes and views and import the required node modules. 

```
const express = require("express")
const app = express()
//Middleware to parse data in body portion of incoming request, like POST //request
const body_parser = require("body-parser")

objForUrlencoded = body_parser.urlencoded({extended:false})

app.set("view engine", "ejs")
app.use("/assets", express.static("assets"))
app.use(objForUrlencoded)

app.get("/", (req,res,next)=>{//Show the homepage
	res.render("homepage")
})
app.get("/save_data.ejs", (req,res,next)=>{//Show the form for saving data
	res.render("save_data")
})
app.get("/search_data.ejs", (req,res,next)=>{//Show the form for searching data
	res.render("search_data")
})

app.listen(1337, ()=>{ console.log("Listening on port 1337")})
```

Here we define a simple Express app which listens on port 1337 and renders pages as specified by the HTTP method (GET, POST) and URL. We create a simple form for user input. 

Keep in mind that each HTML input field must have a name attribute which will later on serve as a key to access the corresponding values of the input field. For example:

```
<input type="text" name="productName">
<br/><br/>
<label for="productCategory">Product Category:</label>
<select name="productCategory">
	<option value="Snacks">Snacks</option>
	<option value="Biscuits">Biscuits</option>
     <option value="Spices">Spices</option>
</select>
<br/><br/>
<label for="price">Price:</label>
  <input type="number" name="price">
<br/><br/>
<label for="quantity">Quantity:</label>
  <input type="number" name="quantity">
```

Later we can access the name of the product as the value of key "productName", the category of the product as the value of the key "productCategory", and so on.

## How to Save Data to the Database

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-124.png)
_Simple UI of the home inventory system_

Okay then, now that we've got some data, let's save it to Firestore! This involves setting up a service account, obtaining a secret key, and using that to initialize the Credentials object to connect the database to our app using the Firebase Admin API. 

For a more in-depth explanation of the process, you can check out their [docs](https://firebase.google.com/docs/database/admin/start). 

```
/*Set up Admin API for Firebase*/
const admin = require('firebase-admin');
//Define path to secret key generated for service account
const serviceAccount = require(PATH TO KEY);
//Initialize the app
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});
```

Here, we've used the path to the secret key which is a JSON file. You can do the same by defining environment variables as described [here](https://firebase.google.com/docs/admin/setup#prerequisites). 

Next, we save our data to Firestore using the set method as follows:

```
let db = admin.firestore()

//Depending on your schema, save data by specifying the collection name, //document name and data contents as follows
await db.collection(key).doc(prod).set(save_to_database[key][prod])
```

Here are a few terms you should be familiar with while navigating the Firestore docs, particularly the [API reference](https://firebase.google.com/docs/reference/js/firebase.firestore.CollectionReference):

* **CollectionReference** – this object is used for adding documents, getting DocumentReferences, and querying documents.
* **DocumentReference** – this refers to a document location in the database used to read/write/listen to that location.
* **QuerySnapshot** – an object that contains the results of a query
* **DocumentSnapshot** – contains data read from a document. You can extract the data using the .data() method.

## How to Query the Data

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-125.png)
_Simple UI for searching/filtering the data_

Once Firestore is packed with data, we can perform all sorts of complex queries on it. 

Let's say we want to know how many items we have with the Category "Snacks". Whenever we execute a query, we get a QuerySnapshot which is a list of DocumentSnapshots. 

```
//Get all docs under the given category
helper_func_get_data = async (category, db) => {
	const data = await db.collection(category).get()
	if(data.empty)
		{
			return -1
		}
	else return data

}
```

We can check if the query returned any data at all using the .empty property and iterate over all received documents using the forEach function like this:

```
data.forEach((doc) => { Product_Info[doc.id] = doc.data()})

//Here data is a QuerySnapshot and Product_Info is a JavaScript object 
//with document names as keys and their corresponding values. We can pass this 
//object as an argument in render() method to display the received contents
```

Here's how to figure out the total price of all Snacks:

```
total_agg = 0
data.forEach((doc) => { total_agg+=doc.data()[aggregate_over]

//aggregate_over is a variable which defines criteria to sum over like price //or quantity
```

To sort all Snacks on the basis of their price, do this:

```
const data = await db.collection(category).orderBy(filter_criteria).get() 
```

where filter_criteria = "Price".

## How to Delete Items from the Database

Over time, our household items that we consume daily are depleted and we'll need to delete them from the database to maintain consistency. 

Until there's a feasible mechanism to connect the refrigerator to Cloud Firestore, we'll have to manually delete our records for Snacks once we've eaten them.

```
firebase_delete_data = async (category, response, product_name) => {
	try
	{ 
	  let db = admin.firestore()
	  await db.collection(category).doc(product_name).delete()
	  response.render("search_data")
	   }
	catch(err)
	{console.log(err)}
}
```

## How to Update Items in the Database

```
firebase_update_data = async (category, response, reqbody) => {
	try
	{
		let db = admin.firestore()
		await db.collection(category).doc(reqbody["productName"]).update({"Price": parseFloat(reqbody["price"]), "Quantity": parseFloat(reqbody["quantity"]), "ExpiryDate": reqbody["expiryDate"]})
		response.render("successpage")
	}
	catch(err)
	{
		console.log(err)
		response.render("failurepage")
	}
}
```

Another common functionality we'll want to have is to update existing records in the database. 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-126.png)
_Simple UI for updating product details_

Once our functionalities are implemented, we export the functions to use from our Express app like this:

```
module.exports = {
	"firebase_save_data" : firebase_save_data,
	"firebase_retrieve_data": firebase_retrieve_data,
	"firebase_delete_data": firebase_delete_data,
	"firebase_update_data": firebase_update_data
	}
```

and import the required module as follows:

```
const firebase_functions = require("./firebase_CRUD_custom_code/firebase_functions.js")
```

Then we can use our functions as required. For example, if we want to update any items we can do the following:

```
app.post("/update", objForUrlencoded, (req,res) => {
	
	firebase_functions.firebase_update_data(req.body["category"], res, req.body)
})
```

## Wrapping up!

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-127.png)

To wrap up, in this article we learned about the data model of Cloud Firestore, how to save data, the mechanism for retrieving data, how to work with QuerySnapshots, sorting data on different filters, deleting items, and updating items through our Express app. 

In this way, we can automate the task of tracking frequently used products in our households. We can also check which products are out of stock and so much more to make our busy lives easier. 

I hope you enjoyed reading this article just as much as I enjoyed writing it. Thank you for your time, have a good day and happy coding!


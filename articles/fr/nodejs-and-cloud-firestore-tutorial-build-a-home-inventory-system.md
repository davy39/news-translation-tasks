---
title: Tutoriel Node.js et Cloud Firestore – Comment créer un système d'inventaire
  domestique
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
seo_title: Tutoriel Node.js et Cloud Firestore – Comment créer un système d'inventaire
  domestique
seo_desc: "By Suchandra Datta\nIn this article, you'll practice your JavaScript skills\
  \ while streamlining your household chores by creating your very own home inventory\
  \ system. \nI've often found that it's hard to keep track common household items\
  \ that I buy freq..."
---

Par Suchandra Datta

Dans cet article, vous mettrez en pratique vos compétences en JavaScript tout en simplifiant vos tâches ménagères en créant votre propre système d'inventaire domestique. 

J'ai souvent trouvé qu'il était difficile de suivre les articles ménagers courants que j'achète fréquemment, comme la nourriture, les épices, les médicaments, etc. C'est au mieux agaçant et au pire frustrant de découvrir un paquet de chips oublié depuis longtemps au fond du placard. 

Lassé de faire le suivi manuellement, j'ai décidé de créer mon propre système d'inventaire domestique. Ce système me permettrait de :

* créer des enregistrements pour chaque article, avec des informations utiles telles que le prix et la quantité
* filtrer les articles sur la base de différents critères tels que le prix, la quantité et la date d'expiration
* trier les articles en fonction de critères donnés
* supprimer les articles qui ne sont plus utilisés
* modifier les enregistrements existants

Dans ce tutoriel, je vais vous guider à travers le processus de construction de ce système. Commençons.

## Comment définir le schéma de la base de données

[Cloud Firestore](https://firebase.google.com/docs/firestore) est une base de données NoSQL flexible, évolutive et hébergée dans le cloud, proposée par Firebase. Les données sont stockées dans des documents, et les documents sont regroupés dans des collections, un peu comme si l'on stockait des pages d'informations dans un dossier et que l'on conservait plusieurs dossiers ensemble dans un tiroir. 

Firestore offre des options de requête puissantes allant du simple tri à l'ajout de limites aux résultats de la requête. 

Pour nos besoins, nous définirons une Collection pour une catégorie spécifique. Chaque Document correspondra à un produit au sein de cette catégorie et le contenu d'un Document sera chaque champ d'information accompagné de sa valeur de données. Par exemple :

```python
"Snacks" : {
	"Food_Item_1" : { "Price":P1, "Quantity":Q1, "ExpiryDate":D1},
	"Food_Item_2" : { "Price":P2, "Quantity":Q2, "ExpiryDate":D2},	
    .
    .
	"Food_Item_N" : { "Price":PN, "Quantity":QN, "ExpiryDate":DN}
}
```

Le nom de notre Collection serait Snacks, nos noms de Documents seraient Food_Item_1, Food_Item_2 et ainsi de suite, et le contenu de chaque document serait le prix, la quantité et la date d'expiration.

## Comment obtenir les entrées de l'utilisateur

Créons d'abord quelques routes et vues et importons les modules Node requis. 

```
const express = require("express")
const app = express()
// Middleware pour analyser les données dans le corps de la requête entrante, comme une requête POST
const body_parser = require("body-parser")

objForUrlencoded = body_parser.urlencoded({extended:false})

app.set("view engine", "ejs")
app.use("/assets", express.static("assets"))
app.use(objForUrlencoded)

app.get("/", (req,res,next)=>{// Afficher la page d'accueil
	res.render("homepage")
})
app.get("/save_data.ejs", (req,res,next)=>{// Afficher le formulaire pour sauvegarder les données
	res.render("save_data")
})
app.get("/search_data.ejs", (req,res,next)=>{// Afficher le formulaire pour rechercher des données
	res.render("search_data")
})

app.listen(1337, ()=>{ console.log("Listening on port 1337")})
```

Ici, nous définissons une application Express simple qui écoute sur le port 1337 et affiche les pages comme spécifié par la méthode HTTP (GET, POST) et l'URL. Nous créons un formulaire simple pour la saisie de l'utilisateur. 

Gardez à l'esprit que chaque champ de saisie HTML doit avoir un attribut name qui servira plus tard de clé pour accéder aux valeurs correspondantes du champ de saisie. Par exemple :

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

Plus tard, nous pourrons accéder au nom du produit via la clé "productName", à la catégorie du produit via la clé "productCategory", et ainsi de suite.

## Comment sauvegarder des données dans la base de données

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-124.png)
_Interface utilisateur simple du système d'inventaire domestique_

Très bien, maintenant que nous avons des données, sauvegardons-les dans Firestore ! Cela implique de configurer un compte de service, d'obtenir une clé secrète et de l'utiliser pour initialiser l'objet Credentials afin de connecter la base de données à notre application en utilisant l'API Firebase Admin. 

Pour une explication plus approfondie du processus, vous pouvez consulter leur [docs](https://firebase.google.com/docs/database/admin/start). 

```
/* Configurer l'API Admin pour Firebase */
const admin = require('firebase-admin');
// Définir le chemin vers la clé secrète générée pour le compte de service
const serviceAccount = require(PATH TO KEY);
// Initialiser l'application
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});
```

Ici, nous avons utilisé le chemin vers la clé secrète qui est un fichier JSON. Vous pouvez faire de même en définissant des variables d'environnement comme décrit [ici](https://firebase.google.com/docs/admin/setup#prerequisites). 

Ensuite, nous sauvegardons nos données dans Firestore en utilisant la méthode set comme suit :

```
let db = admin.firestore()

// Selon votre schéma, sauvegardez les données en spécifiant le nom de la collection, 
// le nom du document et le contenu des données comme suit
await db.collection(key).doc(prod).set(save_to_database[key][prod])
```

Voici quelques termes avec lesquels vous devriez vous familiariser en naviguant dans la documentation Firestore, en particulier la [API reference](https://firebase.google.com/docs/reference/js/firebase.firestore.CollectionReference) :

* **CollectionReference** – cet objet est utilisé pour ajouter des documents, obtenir des DocumentReferences et interroger des documents.
* **DocumentReference** – cela se réfère à l'emplacement d'un document dans la base de données utilisé pour lire/écrire/écouter cet emplacement.
* **QuerySnapshot** – un objet qui contient les résultats d'une requête.
* **DocumentSnapshot** – contient des données lues à partir d'un document. Vous pouvez extraire les données en utilisant la méthode .data().

## Comment interroger les données

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-125.png)
_Interface utilisateur simple pour rechercher/filtrer les données_

Une fois que Firestore est rempli de données, nous pouvons y effectuer toutes sortes de requêtes complexes. 

Disons que nous voulons savoir combien d'articles nous avons avec la catégorie "Snacks". Chaque fois que nous exécutons une requête, nous obtenons un QuerySnapshot qui est une liste de DocumentSnapshots. 

```
// Récupérer tous les documents sous la catégorie donnée
helper_func_get_data = async (category, db) => {
	const data = await db.collection(category).get()
	if(data.empty)
		{
			return -1
		}
	else return data

}
```

Nous pouvons vérifier si la requête a renvoyé des données en utilisant la propriété .empty et itérer sur tous les documents reçus en utilisant la fonction forEach comme ceci :

```
data.forEach((doc) => { Product_Info[doc.id] = doc.data()})

// Ici, data est un QuerySnapshot et Product_Info est un objet JavaScript 
// avec les noms de documents comme clés et leurs valeurs correspondantes. Nous pouvons passer cet 
// objet comme argument dans la méthode render() pour afficher le contenu reçu
```

Voici comment calculer le prix total de tous les Snacks :

```
total_agg = 0
data.forEach((doc) => { total_agg+=doc.data()[aggregate_over]

// aggregate_over est une variable qui définit le critère sur lequel faire la somme comme le prix 
// ou la quantité
```

Pour trier tous les Snacks sur la base de leur prix, faites ceci :

```
const data = await db.collection(category).orderBy(filter_criteria).get() 
```

où filter_criteria = "Price".

## Comment supprimer des éléments de la base de données

Au fil du temps, nos articles ménagers que nous consommons quotidiennement s'épuisent et nous devrons les supprimer de la base de données pour maintenir la cohérence. 

Tant qu'il n'y a pas de mécanisme réalisable pour connecter le réfrigérateur à Cloud Firestore, nous devrons supprimer manuellement nos enregistrements pour les Snacks une fois que nous les aurons mangés.

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

## Comment mettre à jour des éléments dans la base de données

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

Une autre fonctionnalité courante que nous voudrons avoir est la mise à jour des enregistrements existants dans la base de données. 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-126.png)
_Interface utilisateur simple pour mettre à jour les détails du produit_

Une fois nos fonctionnalités implémentées, nous exportons les fonctions pour les utiliser depuis notre application Express comme ceci :

```
module.exports = {
	"firebase_save_data" : firebase_save_data,
	"firebase_retrieve_data": firebase_retrieve_data,
	"firebase_delete_data": firebase_delete_data,
	"firebase_update_data": firebase_update_data
	}
```

et importons le module requis comme suit :

```
const firebase_functions = require("./firebase_CRUD_custom_code/firebase_functions.js")
```

Ensuite, nous pouvons utiliser nos fonctions selon les besoins. Par exemple, si nous voulons mettre à jour des articles, nous pouvons faire ce qui suit :

```
app.post("/update", objForUrlencoded, (req,res) => {
	
	firebase_functions.firebase_update_data(req.body["category"], res, req.body)
})
```

## Conclusion !

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-127.png)

Pour conclure, dans cet article, nous avons découvert le modèle de données de Cloud Firestore, comment sauvegarder des données, le mécanisme de récupération des données, comment travailler avec les QuerySnapshots, le tri des données sur différents filtres, la suppression d'éléments et la mise à jour d'éléments via notre application Express. 

De cette façon, nous pouvons automatiser la tâche de suivi des produits fréquemment utilisés dans nos foyers. Nous pouvons également vérifier quels produits sont en rupture de stock et bien plus encore pour faciliter nos vies bien remplies. 

J'espère que vous avez apprécié la lecture de cet article autant que j'ai aimé l'écrire. Merci pour votre temps, passez une bonne journée et bon codage !
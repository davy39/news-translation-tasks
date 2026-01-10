---
title: Comment commencer avec Firebase en utilisant Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T20:32:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-firebase-using-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6015593f0a2838549dcbb3b9.jpg
tags:
- name: database
  slug: database
- name: Firebase
  slug: firebase
- name: Python
  slug: python
seo_title: Comment commencer avec Firebase en utilisant Python
seo_desc: "By Suchandra Datta\nThis article a detailed guide that'll help you set\
  \ up your Firebase database and perform simple CRUD operations on it using Python.\
  \ \nFirebase, as you might know, is a platform provided by Google to accelerate\
  \ app development. It of..."
---

Par Suchandra Datta

Cet article est un guide détaillé qui vous aidera à configurer votre base de données Firebase et à effectuer des opérations CRUD simples dessus en utilisant Python. 

Firebase, comme vous le savez peut-être, est une plateforme fournie par Google pour accélérer le développement d'applications. Elle offre du BaaS ou backend en tant que service, ce qui signifie que Firebase prend en charge l'infrastructure cloud et tous vos besoins backend. Cela vous permet de développer et de déployer plus rapidement. 

Firebase offre plusieurs produits amazings, tels que Realtime Database, Cloud Firestore et Authentication. Et il permet également l'hébergement et offre des API pour des tâches d'apprentissage automatique comme la reconnaissance de texte, l'étiquetage d'images et bien plus encore ! 

Rendez-vous sur leur site lié [ici](https://firebase.google.com/) et salivez devant les options merveilleuses disponibles. 

## Comment configurer une base de données Firebase Realtime

Créez un nouveau projet sur Firebase – appelons-le BookStoreProject. Une fois qu'il est configuré, créez une base de données Realtime en sélectionnant l'option Créer une base de données.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/pic-1.png)
_Création d'une base de données Realtime en utilisant la console Firebase_

Lorsque vous cliquez sur Créer une base de données, vous devez spécifier l'emplacement de la base de données et les règles de sécurité. Deux règles sont disponibles :

* le mode verrouillé, qui refuse toutes les lectures et écritures dans la base de données, et 
* le mode test, qui permet l'accès en lecture et écriture pendant 30 jours par défaut (après quoi toutes les lectures et écritures sont refusées sauf si les règles de sécurité sont mises à jour). 

Puisque nous utiliserons la base de données pour la lecture, l'écriture et l'édition, nous choisissons le mode test. Une fois cela fait, la base de données est prête pour notre utilisation !

## Comment écrire dans la base de données Firebase Realtime en utilisant Python

L'étape immédiate suivante est de découvrir comment nous pouvons nous connecter à notre base de données en utilisant Python. Nous allons utiliser l'API Admin Database. Vous devrez installer la bibliothèque requise. 

Pour plus d'informations sur l'utilisation de `firebase_admin` pour Python, consultez la documentation officielle liée [ici](https://firebase.google.com/docs/database/admin/start).

```python
pip install firebase_admin
```

Pour se connecter à Firebase, nous avons besoin des lignes de code suivantes :

```
import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('....chemin vers le fichier')
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':databaseURL
	})
```

Pour que le code fonctionne, nous avons besoin de quelques prérequis. 

Tout d'abord, nous devons spécifier le chemin vers une clé de compte de service qui sera utilisée pour initialiser le SDK admin. 

Firebase permettra l'accès aux API du serveur Firebase à partir des comptes de service Google. Pour authentifier le compte de service, nous avons besoin d'une clé privée au format JSON. 

Le chemin vers ce fichier JSON doit être fourni pour créer l'objet d'identification. Pour générer la clé, allez dans les paramètres du projet, cliquez sur Générer une nouvelle clé privée, téléchargez le fichier et placez-le dans votre structure de répertoires.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-205.png)
_Paramètres du projet sur la console Firebase_

Pour une explication approfondie de ce processus, consultez la documentation officielle liée [ici](https://firebase.google.com/docs/admin/setup). 

Ensuite, nous avons besoin du databaseURL, qui est simplement l'URL qui donne accès à notre base de données. Il est présent sur la page de la console Firebase de la base de données Realtime elle-même. 

### Comment écrire en utilisant la fonction set()

```
from firebase_admin import db

ref = db.reference("/")
```

Nous définissons la référence à la racine de la base de données (ou nous pourrions également la définir à une valeur de clé ou à une valeur de clé enfant). La question qui se pose naturellement est de savoir quel schéma est autorisé pour stocker des données dans les bases de données Realtime ? 

Toutes les données à stocker doivent être au format JSON, c'est-à-dire une séquence de paires clé-valeur. Si vous avez besoin d'une clé générée par le système, vous pourriez opter pour l'utilisation de la fonction `push()` que nous aborderons bientôt. 

Construisons un JSON approprié qui peut être enregistré dans la base de données. Nous avons des informations concernant quatre livres comme suit :

```json
{
	"Book1":
	{
		"Title": "The Fellowship of the Ring",
		"Author": "J.R.R. Tolkien",
		"Genre": "Epic fantasy",
		"Price": 100
	},
	"Book2":
	{
		"Title": "The Two Towers",
		"Author": "J.R.R. Tolkien",
		"Genre": "Epic fantasy",
		"Price": 100	
	},
	"Book3":
	{
		"Title": "The Return of the King",
		"Author": "J.R.R. Tolkien",
		"Genre": "Epic fantasy",
		"Price": 100
	},
	"Book4":
	{
		"Title": "Brida",
		"Author": "Paulo Coelho",
		"Genre": "Fiction",
		"Price": 100
	}
}
```

Nous chargeons le fichier JSON requis et enregistrons les données dans la base de données comme ceci :

```
import json
with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
```

La base de données ressemble maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-207.png)
_Schéma de la base de données vu depuis la console Firebase_

### Comment écrire en utilisant la fonction push()

Firebase nous fournit la fonction `push()` qui enregistre les données sous une clé unique générée par le système. Cette méthode garantit que si plusieurs écritures sont effectuées sur la même clé, elles ne s'écrasent pas mutuellement. 

Par exemple, si plusieurs sources tentent d'écrire à /Books/Best_Sellers/, alors quelle que soit la source qui effectue la dernière écriture, cette valeur persistera dans la base de données. Cela introduit la possibilité que les données soient écrasées. `push()` résout ce problème en utilisant des clés uniques pour chaque nouvel enfant qui est ajouté. 

```
ref = db.reference("/")
ref.set({
	"Books":
	{
		"Best_Sellers": -1
	}
})

ref = db.reference("/Books/Best_Sellers")
import json
with open("book_info.json", "r") as f:
	file_contents = json.load(f)

for key, value in file_contents.items():
	ref.push().set(value)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-208.png)
_Schéma de la base de données après l'exécution de la méthode push()_

Veuillez noter que `push()` et `set()` ne sont pas atomiques. Cela signifie qu'il n'y a aucune garantie que les deux fonctions s'exécuteront ensemble sans interruption en tant qu'unité indivisible. 

Pendant que la base de données est mise à jour, si nous essayons de récupérer les données, il peut arriver que `push()` soit terminé mais que `set()` ne le soit pas – donc le JSON que nous recevons aura une clé générée par le système sans champ de valeur. 

## Comment mettre à jour votre base de données Firebase en utilisant Python

La mise à jour de la base de données est aussi simple que de définir la référence au point requis et d'utiliser la fonction `update()`. Supposons que le prix des livres de J. R. R. Tolkien est réduit à 80 unités pour offrir une réduction. 

```
ref = db.reference("/Books/Best_Sellers/")
best_sellers = ref.get()
print(best_sellers)
for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		value["Price"] = 90
		ref.child(key).update({"Price":80})
        
        
```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-209.png)
_Schéma de la base de données après l'utilisation de la fonction update()_

## Comment récupérer des données de Firebase en utilisant Python

Nous avons déjà récupéré des données en utilisant la méthode `get()` lorsque nous essayions de mettre à jour une clé particulière. Maintenant, nous allons voir quelques méthodes supplémentaires et les regrouper pour faire des requêtes complexes.

Obtenons tous les livres dans l'ordre trié par prix en utilisant la méthode `order_by_child()`. Pour appliquer cette méthode, nous devons d'abord définir la clé par laquelle nous trions comme champ d'index via la règle `.indexOn` dans les règles de sécurité Firebase. 

Si nous voulons trier par prix, alors le prix doit être listé comme index. Vous pouvez définir la valeur comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-210.png)
_Allez dans l'onglet Règles et tapez la structure du schéma à laquelle vous souhaitez définir l'index_

```
ref = db.reference("/Books/Best_Sellers/")
print(ref.order_by_child("Price").get())
```

La valeur de retour de la méthode est un OrderedDict. Pour trier par clé, utilisez `order_by_key()`. Pour obtenir le livre avec le prix maximum, nous utilisons la méthode `limit_to_last()` comme suit :

```
ref.order_by_child("Price").limit_to_last(1).get()
```

Alternativement, pour obtenir le livre le moins cher, nous écrivons ceci :

```
ref.order_by_child("Price").limit_to_first(1).get()
```

Pour obtenir les livres qui sont exactement au prix de 80 unités, nous utilisons ceci :

```
ref.order_by_child("Price").equal_to(80).get()
```

Pour plus d'exemples et de méthodes pour interroger la base de données selon vos besoins, consultez la documentation officielle [ici](https://firebase.google.com/docs/database/admin/retrieve-data).

## Comment supprimer des données de Firebase en utilisant Python

Supprimer des données est assez simple. Supprimons tous les livres best-sellers avec J.R.R. Tolkien comme auteur.

```
ref = db.reference("/Books/Best_Sellers")

for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		ref.child(key).set({})
        
        
```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-211.png)
_Schéma de la base de données après suppression_

## Conclusion

Dans cet article, nous avons appris comment créer une base de données Firebase Realtime, la remplir avec des données, et supprimer, mettre à jour et interroger les données en utilisant Python. 

J'espère que cela aidera un développeur Python qui vient de découvrir la beauté de Firebase mais qui se sent submergé par tant d'options et de méthodes différentes à choisir. Si vous avez lu jusqu'ici, merci beaucoup ! Prenez soin de vous, et bon codage !
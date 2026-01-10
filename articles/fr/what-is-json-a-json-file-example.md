---
title: JSON pour débutants – Notation d'objets JavaScript expliquée en anglais simple
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-11-29T19:16:16.000Z'
originalURL: https://freecodecamp.org/news/what-is-json-a-json-file-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/freeCodeCamp-Cover-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: json
  slug: json
seo_title: JSON pour débutants – Notation d'objets JavaScript expliquée en anglais
  simple
seo_desc: "Many software applications need to exchange data between a client and server.\
  \ \nFor a long time, XML was the preferred data format when it came to information\
  \ exchange between the two points. Then in early 2000, JSON was introduced as an\
  \ alternate dat..."
---

De nombreuses applications logicielles doivent échanger des données entre un client et un serveur. 

Pendant longtemps, XML était le format de données préféré pour l'échange d'informations entre ces deux points. Ensuite, au début des années 2000, JSON a été introduit comme un format de données alternatif pour l'échange d'informations.

Dans cet article, vous apprendrez tout sur JSON. Vous comprendrez ce que c'est, comment l'utiliser, et nous clarifierons quelques idées reçues. Alors, sans plus tarder, découvrons JSON.

## Qu'est-ce que JSON ?

JSON (**J**ava**S**cript **O**bject **N**otation) est un format d'échange de données `basé sur du texte`. Il s'agit d'une collection de paires clé-valeur où la clé doit être de type chaîne de caractères, et la valeur peut être de l'un des types suivants :

* Nombre
* Chaîne de caractères
* Booléen
* Tableau
* Objet
* null

Quelques règles importantes à noter :

* Dans le format de données JSON, les clés doivent être encadrées par des guillemets doubles.
* La clé et la valeur doivent être séparées par un deux-points (:).
* Il peut y avoir plusieurs paires clé-valeur. Deux paires clé-valeur doivent être séparées par une virgule (,).
* Aucun commentaire (// ou /* */) n'est autorisé dans les données JSON. (Mais vous pouvez [contourner cela](https://www.freecodecamp.org/news/json-comment-example-how-to-comment-in-json-files/), si vous êtes curieux.)

Voici à quoi ressemblent des données JSON simples :

```js
{
    "name": "Alex C",
    "age": 2,
    "city": "Houston"
}
```

Les données JSON valides peuvent être dans deux formats différents :

* Une collection de paires clé-valeur encadrées par une paire d'accolades `{...}`. Vous avez vu cela comme exemple ci-dessus.
* Une collection de liste ordonnée de paires clé-valeur séparées par une virgule (,) et encadrées par une paire de crochets `[...]`. Voir l'exemple ci-dessous :

```js
[
	{
        "name": "Alex C",
        "age": 2,
        "city": "Houston"
	},
    {
        "name": "John G",
        "age": 40,
        "city": "Washington"
	},
    {
        "name": "Bala T",
        "age": 22,
        "city": "Bangalore"
	}
]
```

Supposons que vous veniez d'un milieu de développeur JavaScript. Dans ce cas, vous pourriez penser que le format JSON et les objets JavaScript (et les tableaux d'objets) sont très similaires. Mais ils ne le sont pas. Nous verrons les différences en détail bientôt.

La structure du format JSON a été dérivée de la syntaxe des objets JavaScript. C'est la seule relation entre le format de données JSON et les objets JavaScript.

JSON est un format indépendant du langage de programmation. Nous pouvons utiliser le format de données JSON en Python, Java, PHP, et dans de nombreux autres langages de programmation.

## Exemples de format de données JSON 

Vous pouvez enregistrer des données JSON dans un fichier avec l'extension `.json`. Créons un fichier `employee.json` avec des attributs (représentés par des clés et des valeurs) d'un employé.

```js
{
	"name": "Aleix Melon",
	"id": "E00245",
	"role": ["Dev", "DBA"],
	"age": 23,
	"doj": "11-12-2019",
	"married": false,
	"address": {
		"street": "32, Laham St.",
		"city": "Innsbruck",
		"country": "Austria"
	},
	"referred-by": "E0012"
}
```

Les données JSON ci-dessus montrent les attributs d'un employé. Les attributs sont :

* `name` : le nom de l'employé. La valeur est de type `String`. Elle est donc encadrée par des guillemets doubles.
* `id` : un identifiant unique d'un employé. Il s'agit à nouveau d'un type `String`.
* `role` : les rôles qu'un employé joue dans l'organisation. Il peut y avoir plusieurs rôles joués par un employé. Le type de données préféré est donc `Array`.
* `age` : l'âge actuel de l'employé. Il s'agit d'un `Number`.
* `doj` : la date à laquelle l'employé a rejoint l'entreprise. Comme il s'agit d'une date, elle doit être encadrée par des guillemets doubles et traitée comme une `String`.
* `married` : l'employé est-il marié ? Si oui, vrai ou faux. La valeur est donc de type `Boolean`.
* `address` : l'adresse de l'employé. Une adresse peut avoir plusieurs parties comme la rue, la ville, le pays, le code postal, et bien plus encore. Nous pouvons donc traiter la valeur de l'adresse comme une représentation d'`Object` (avec des paires clé-valeur).
* `referred-by` : l'id d'un employé qui a recommandé cet employé dans l'organisation. Si cet employé a rejoint l'entreprise par le biais d'une recommandation, cet attribut aurait une valeur. Sinon, il aurait `null` comme valeur.

Maintenant, créons une collection d'employés sous forme de données JSON. Pour cela, nous devons conserver plusieurs enregistrements d'employés à l'intérieur des crochets [...].

```js
[
	{
        "name": "Aleix Melon",
        "id": "E00245",
        "role": ["Dev", "DBA"],
        "age": 23,
        "doj": "11-12-2019",
        "married": false,
        "address": {
            "street": "32, Laham St.",
            "city": "Innsbruck",
            "country": "Austria"
            },
        "referred-by": "E0012"
	},
    {
        "name": "Bob Washington",
        "id": "E01245",
        "role": ["HR"],
        "age": 43,
        "doj": "10-06-2010",
        "married": true,
        "address": {
            "street": "45, Abraham Lane.",
            "city": "Washington",
            "country": "USA"
            },
        "referred-by": null
	}
]
```

Avez-vous remarqué la valeur de l'attribut `referred-by` pour le deuxième employé, Bob Washington ? Elle est `null`. Cela signifie qu'il n'a pas été recommandé par l'un des employés.

## Comment utiliser les données JSON comme valeur de chaîne

Nous avons vu comment formater les données JSON à l'intérieur d'un fichier JSON. Alternativement, nous pouvons utiliser les données JSON comme valeur de chaîne et les assigner à une variable. Comme JSON est un format basé sur du texte, il est possible de le manipuler comme une chaîne dans la plupart des langages de programmation. 

Prenons un exemple pour comprendre comment nous pouvons le faire en JavaScript. Vous pouvez encadrer l'ensemble des données JSON comme une chaîne à l'intérieur de guillemets simples `'...'`.

```js
const user = '{"name": "Alex C", "age": 2, "city": "Houston"}';
```

Si vous voulez conserver le formatage JSON intact, vous pouvez créer les données JSON à l'aide de littéraux de gabarit.

```js
const user = `{
    "name": "Alex C",
    "age": 2,
    "city": "Houston"
}`;

```

C'est également utile lorsque vous voulez construire des données JSON en utilisant des valeurs dynamiques.

```js
const age = 2;

const user = `{
    "name": "Alex C",
    "age": ${age},
    "city": "Houston"
}`;

console.log(user);

// Output
{
    "name": "Alex C",
    "age": 2,
    "city": "Houston"
}
```

## Les objets JavaScript et JSON ne sont PAS identiques

Le format de données JSON est dérivé de la structure des objets JavaScript. Mais la similarité s'arrête là. 

Les objets en JavaScript :

* Peuvent avoir des méthodes, et JSON ne peut pas.
* Les clés peuvent être sans guillemets.
* Les commentaires sont autorisés.
* Sont des entités propres à JavaScript.

Voici un fil Twitter qui explique les différences avec quelques exemples.

%[https://twitter.com/tapasadhikary/status/1463493300225204225]

## Comment convertir JSON en objet JavaScript, et vice-versa

JavaScript dispose de deux méthodes intégrées pour convertir les données JSON en objet JavaScript et vice-versa.

### Comment convertir les données JSON en objet JavaScript

Pour convertir les données JSON en objet JavaScript, utilisez la méthode `JSON.parse()`. Elle analyse une chaîne JSON valide en un objet JavaScript.

```js

const userJSONData = `{
    "name": "Alex C",
    "age": 2,
    "city": "Houston"
}`;

const userObj = JSON.parse(userJSONData);
console.log(userObj);
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/first.png)
_La sortie_

### Comment convertir un objet JavaScript en données JSON

Pour convertir un objet JavaScript en données JSON, utilisez la méthode `JSON.stringify()`.

```js
const userObj = {
    name: 'Alex C', 
    age: 2, 
    city: 'Houston'
}

const userJSONData = JSON.stringify(userObj);
console.log(userJSONData);
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/second.png)
_La sortie_

  
Avez-vous remarqué le terme `JSON` que nous avons utilisé pour invoquer les méthodes `parse()` et `stringify()` ci-dessus ? Il s'agit d'un objet JavaScript intégré nommé `JSON` (il aurait pu être nommé JSONUtil également) mais il n'est pas lié au format de données JSON dont nous avons parlé jusqu'à présent. Donc, s'il vous plaît, ne vous laissez pas confondre.

## Comment gérer les erreurs JSON comme "Unexpected token u in JSON at position 1" ?

Lors de la manipulation de JSON, il est très normal de rencontrer une erreur comme celle-ci lors de l'analyse des données JSON en un objet JavaScript :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-127.png)
_Erreur de syntaxe JSON_

Chaque fois que vous rencontrez cette erreur, veuillez vérifier la validité de votre format de données JSON. Vous avez probablement fait une erreur triviale et c'est ce qui la cause. Vous pouvez valider le format de vos données JSON en utilisant un [JSON Linter](https://jsonlint.com/).

## Avant de terminer...

J'espère que vous avez trouvé l'article perspicace et informatif. Mes messages directs sont ouverts sur Twitter si vous souhaitez discuter davantage. 

Récemment, j'ai publié quelques conseils utiles pour les débutants en développement web. Vous pourriez vouloir y jeter un coup d'œil :

%[https://blog.greenroots.info/5-tips-for-beginners-to-web-development]

Restez connectés. Je partage mes apprentissages sur JavaScript, le développement web et le blogging sur ces plateformes également :

* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary)
* [Abonnez-vous à ma chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1)
* [Projets secondaires sur GitHub](https://github.com/atapas)
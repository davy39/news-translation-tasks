---
title: Qu'est-ce qu'un fichier JSON ? Exemple de code JavaScript
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-25T20:04:19.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-json-file-example-javascript-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/json.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: json
  slug: json
seo_title: Qu'est-ce qu'un fichier JSON ? Exemple de code JavaScript
seo_desc: "JSON stands for JavaScript Object Notation. A JSON file has .json as its\
  \ extension and the data inside are represented in a key:value pair, just like a\
  \ traditional JavaScript object. \nJSON and objects aren't exactly the same, though.\
  \ The core differe..."
---

JSON signifie JavaScript Object Notation. Un fichier JSON a l'extension .json et les données à l'intérieur sont représentées sous forme de paires clé:valeur, tout comme un objet JavaScript traditionnel. 

JSON et les objets ne sont pas exactement identiques, cependant. La différence principale est que la clé en JSON doit être entre guillemets doubles, et les valeurs, à l'exception des types nombre et null, doivent également être entre guillemets doubles.

Si vous avez travaillé avec des APIs au cours de votre parcours en programmation, vous savez probablement ce qu'est JSON, car beaucoup de données d'API sont désormais au format JSON. 

Si vous n'avez jamais travaillé avec des APIs auparavant et que vous êtes un débutant absolu, vous n'êtes pas seul. 

Dans cet article, je vais vous expliquer ce qu'est JSON et comment vous pouvez en tirer le meilleur parti.

## Syntaxe de base de JSON

```js
{
  "clé1": "valeur1",
  "clé2": "valeur2",
  "clé3": "valeur3",
  "clé4": 7,
  "clé5": null,
  "amisPréférés": ["Kolade", "Nithya", "Dammy", "Jack"],
  "joueursPréférés": {"un": "Kante", "deux": "Hazard", "trois": "Didier"}
}
```

## Types de données acceptés par JSON

JSON peut être défini dans un objet ou un tableau, qui peut contenir plusieurs objets. Ainsi, les objets et les tableaux sont automatiquement des types de données acceptés par JSON. D'autres types de données qu'il supporte sont les booléens, null et les chaînes de caractères. 

Les types de données tels que undefined, function et date ne sont pas supportés par JSON.

De plus, JSON peut être étendu à d'autres formats de données qui peuvent accepter des types de données supplémentaires que JSON brut n'accepte pas. 

Des exemples de telles extensions sont GeoJSON et BSON. GeoJSON est utilisé pour représenter des données géographiques tandis que BSON est utilisé par le populaire fournisseur de services de base de données MongoDB.

BSON, par exemple, accepte les expressions régulières, les dates et les timestamps comme types de données, que JSON n'accepte pas.

## Règles de syntaxe de JSON

JSON est très strict en ce qui concerne ses types de données supportés. Si vous avez un linter installé dans votre éditeur de code, il vous indique immédiatement qu'il y a une erreur chaque fois que vous entrez un type de données non supporté ou que vous allez à l'encontre des règles de syntaxe.

### Règles de syntaxe de JSON à connaître :

- Toutes les données dans le fichier doivent être entourées d'accolades si vous les représentez sous forme d'objet, et de crochets si c'est un tableau.
- Les guillemets simples ne sont pas autorisés
- La clé dans chaque JSON doit être unique et doit être entre guillemets doubles
- Les nombres ne doivent pas être entourés de guillemets doubles, sinon ils seront traités comme des chaînes de caractères.
- Le type de données null ne doit pas être entouré de guillemets doubles.
- Les valeurs booléennes ne peuvent être que true ou false.
- Chaque paire clé:valeur doit être terminée par une virgule, sauf pour le dernier élément
- Un objet particulier à l'intérieur d'un tableau doit également être terminé par une virgule.

## Comment les données JSON sont envoyées au client (navigateur)

JSON a été créé pour répondre au besoin d'envoyer des données du serveur (une base de données, par exemple) au client (navigateurs) en temps réel. 

Mais les données JSON ne peuvent pas être transmises au navigateur sous leur forme brute de paire clé:valeur, donc les langages de programmation ont des méthodes pour manipuler les données JSON. 

En JavaScript, par exemple, `JSON.parse()` convertit les données JSON en objets et `JSON.stringify()` convertit la paire clé:valeur d'un objet en données JSON. 

Python fournit des méthodes telles que `json.loads()` pour convertir une chaîne existante en JSON, et `json.dumps()` pour convertir un objet en une chaîne JSON.

Vous pouvez envoyer les données dans la syntaxe JSON de base au navigateur en utilisant les deux méthodes fournies par JavaScript. 

### Comment envoyer des données JSON au client (navigateur) avec JavaScript

La méthode `JSON.stringify()` retourne une chaîne JSON qui est exactement la même qu'un objet JavaScript. Vous pouvez l'utiliser en combinaison avec des méthodes de manipulation du DOM pour afficher les données JSON dans le navigateur, comme je l'ai fait dans les extraits de code ci-dessous :

```html
<h2>Voici les données du JSON :</h2> 
<div id="json"></div>
```

```js
 const JSONData = {
    "clé1": "valeur1",
    "clé2": "valeur2",
    "clé3": "valeur3",
    "clé4": 7,
    "clé5": null,
    "amisPréférés": ["Kolade", "Nithya", "Dammy", "Jack"],
    "joueursPréférés": {"un": "Kante", "deux": "Hazard", "trois": "Didier"}
}

const JSONString = JSON.stringify(JSONData)
const JSONDisplay = document.querySelector("#json")
JSONDisplay.innerHTML = JSONString
```

Dans le code JavaScript, nous avons déclaré les données JSON comme un littéral d'objet avec l'identifiant (nom) `JSONData`. Nous avons utilisé la méthode `JSON.stringify()` de JavaScript pour le transformer en une chaîne, et la méthode de sélection querySelector du DOM pour obtenir la div vide dans le HTML. Cela permet de remplir les données JSON avec la méthode de manipulation du DOM `innerHTML`.

![json-stringify-method](https://www.freecodecamp.org/news/content/images/2021/08/json-stringify-method.png)

Nous pouvons utiliser la méthode `JSON.parse()` pour transformer des données JSON en un objet - et voici comment cela fonctionne :

```html
<h2>Voici les données du JSON :</h2>
<div id="json"></div>
```

```js
const JSONData =
     '{"name": "Kolade", "favFriends": ["Kolade", "Nithya", "Rocco", "Jack"], "from": "Africa"}';

   try {
     const JSONString = JSON.parse(JSONData);
     const JSONDisplay = document.querySelector("#json");
     JSONDisplay.innerHTML = JSONString.name + ", [" + JSONString.favFriends + "], " + JSONString.from;
   } catch (error) {
     console.log("Cannot parse the JSON Data");
   }
```

Le résultat dans le navigateur ressemble à ceci : 
![json-parse-method](https://www.freecodecamp.org/news/content/images/2021/08/json-parse-method.png)

## Conclusion

En tant que programmeur, vous ne pouvez pas vous passer de JSON. La plupart des APIs sont désormais écrites en JSON au lieu de XML. 

JSON était initialement destiné à JavaScript, mais de nombreux autres langages de programmation le supportent désormais grâce à sa nature indépendante du langage. Par conséquent, de nombreux langages ont des bibliothèques pour travailler avec lui.

J'espère que ce tutoriel vous a donné les informations nécessaires pour travailler avec JSON afin que vous puissiez l'utiliser correctement chaque fois que vous le rencontrez.

Merci d'avoir lu, et continuez à coder.
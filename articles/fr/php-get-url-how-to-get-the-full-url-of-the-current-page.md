---
title: PHP Obtenir l'URL - Comment obtenir l'URL complète de la page actuelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-22T17:37:32.000Z'
originalURL: https://freecodecamp.org/news/php-get-url-how-to-get-the-full-url-of-the-current-page
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a1c740569d1a4ca239c.jpg
tags:
- name: PHP
  slug: php
- name: url
  slug: url
seo_title: PHP Obtenir l'URL - Comment obtenir l'URL complète de la page actuelle
seo_desc: "By Dan Englishby\nIn this PHP-focused article, we will explore how to get\
  \ the URL of the current page in the PHP programming language. \nYou may want to\
  \ get the current page URL for the following reasons:\n\nBuilding internal links\n\
  Using filters with GET..."
---

Par Dan Englishby

Dans cet article axé sur PHP, nous allons explorer comment obtenir l'URL de la page actuelle dans le langage de programmation PHP. 

Vous pouvez vouloir obtenir l'URL de la page actuelle pour les raisons suivantes :

* Construire des liens internes
* Utiliser des filtres avec des requêtes GET, par exemple, currentURL.com?myFilterParameter=Food

PHP stocke en réalité beaucoup d'informations utiles lorsque les utilisateurs naviguent dans votre application web. L'une de ces informations est, bien sûr, l'URL actuelle.

PHP stocke ces informations utiles dans son tableau de variables super-globales.

### Qu'est-ce que les Superglobals ?

> Les superglobals sont des variables déjà définies par le moteur PHP qui peuvent être utilisées dans n'importe quel type de portée. Elles sont facilement disponibles à tout moment.

Il existe de nombreuses superglobals, mais celle qui nous intéresse est la superglobale $_SERVER.

### La superglobale $_SERVER

La variable superglobale $_SERVER possède de nombreuses propriétés accessibles avec un index de style associatif. 

Parmi les valeurs auxquelles nous pouvons accéder, on trouve :

* HTTP_USER_AGENT
* HTTP_HOST
* HTTP_ACCEPT_ENCODING
* HTTP_ACCEPT

<p> Vous pouvez voir plus de ces indices dans la documentation PHP <a href="https://www.php.net/manual/en/reserved.variables.server.php" rel="nofollow" target="_blank">ici.</a></p>

### Alors, comment obtenir l'URL complète ?

Avec les points ci-dessus sur les superglobals et la superglobale **$_SERVER** à l'esprit, nous pouvons obtenir l'URL de la page actuelle. 

Dans la capture d'écran suivante, j'ai rendu une application PHP dans un environnement local sur une page nommée "home." 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-91.png)

L'URL est **http://localhost/home**.

Dans le code de cette page, je vais utiliser la variable **$_SERVER**.

Avec cette variable, nous devrons utiliser 2 indices séparés pour obtenir chaque partie de l'URL de la page actuelle. La première partie sera l'hôte, localhost, et la deuxième partie sera le nom de la page, home.

Le premier index que nous utiliserons est **HTTP_HOST** - L'hôte de l'adresse web actuelle, par exemple localhost, ou example.com

Le deuxième est **REQUEST_URI** qui nous donnera la partie de l'URL après l'hôte, donc tout ce qui suit localhost ou example.com

Voyons cela en action :

```
$currentPageUrl = 'http://' . $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"];


echo "URL de la page actuelle " . $currentPageUrl;
```

### Sortie

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-102.png)

Et c'est tout - assez simple !

## Résumé

La variable superglobale **$_SERVER** stocke beaucoup d'informations vitales pour les cas d'utilisation modernes. Comme nous l'avons découvert dans cet exemple, obtenir l'URL de la page actuelle est simplifié grâce à la possibilité d'accéder à cette variable spécifique.

Il vaut la peine de consulter la documentation pour voir quels autres indices sont disponibles, car il est bon de garder à l'esprit à quel point cette variable peut être utile.

J'espère que vous avez apprécié cet article ! Si c'est le cas, n'hésitez pas à consulter mon blog, [https://www.codewall.co.uk/](https://www.codewall.co.uk/)
---
title: MVC en informatique – Le modèle MVC
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-21T21:09:46.000Z'
originalURL: https://freecodecamp.org/news/what-does-mvc-mean-in-computer-science
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/mvc-cover.png
tags:
- name: Computer Science
  slug: computer-science
- name: software architecture
  slug: software-architecture
seo_title: MVC en informatique – Le modèle MVC
seo_desc: 'MVC is an abbreviation that stands for Model, View, and Controller. This
  architectural pattern was created in the late 1970s for making desktop apps, but
  it is now widely used in web application development.

  In this article, I will dive deep into wha...'
---

MVC est une abréviation qui signifie Modèle, Vue et Contrôleur. Ce modèle architectural a été créé à la fin des années 1970 pour la création d'applications de bureau, mais il est désormais largement utilisé dans le développement d'applications web.

Dans cet article, je vais plonger profondément dans ce que signifie MVC ainsi que ses 3 composants, afin que vous puissiez le comprendre.

J'ai également préparé une infographie qui peut vous aider à mieux comprendre MVC, mais vous devez d'abord lire l'article. :)

## Ce que nous allons couvrir
- [Qu'est-ce que MVC et pourquoi est-il utilisé](#heading-quest-ce-que-mvc-et-pourquoi-est-il-utilise)
- [Quels langages et frameworks utilisent MVC ?](#heading-quels-langages-et-frameworks-utilisent-mvc)
- [Qu'est-ce que le Modèle dans MVC ?](#heading-quest-ce-que-le-modele-dans-mvc)
- [Qu'est-ce que la Vue dans MVC ?](#heading-quest-ce-que-la-vue-dans-mvc)
- [Qu'est-ce que le Contrôleur dans MVC ?](#heading-quest-ce-que-le-controleur-dans-mvc)
- [Conclusion](#heading-conclusion)


## Qu'est-ce que MVC et pourquoi est-il utilisé ?

En informatique, MVC est un modèle de conception logicielle pour organiser le code d'application en trois parties interconnectées – un modèle, une vue et un contrôleur.

Le modèle est la logique pour interagir avec la base de données, la vue est l'interface utilisateur avec laquelle l'utilisateur interagit, et le contrôleur est l'intermédiaire entre la vue et le modèle.

Dans de nombreux cas, la vue n'interagit jamais directement avec le modèle – le contrôleur remplit cette fonction.

![mvc1](https://www.freecodecamp.org/news/content/images/2022/06/mvc1.png)

Dans certains autres frameworks, le modèle peut interagir directement avec la vue
![Copy-of-mvc2](https://www.freecodecamp.org/news/content/images/2022/06/Copy-of-mvc2.png)

Le modèle de conception MVC vise à diviser le code de l'application en unités distinctes, afin que la maintenance et l'optimisation ne soient pas un casse-tête. Cela est populairement appelé « séparation des préoccupations ».


## Quels langages et frameworks utilisent MVC ?

Par le passé, MVC était utilisé uniquement pour la création d'interfaces graphiques de bureau. Aujourd'hui, de nombreux langages de programmation et frameworks implémentent MVC pour le développement d'applications web.

Certains frameworks vous obligent même à utiliser MVC, donc vous avez peut-être utilisé MVC sans réaliser que vous l'utilisiez.

Dans une application Express full stack, par exemple, les développeurs divisent souvent le code en un dossier modèle, contrôleur et client (vue).
![Annotation-2022-06-20-103520](https://www.freecodecamp.org/news/content/images/2022/06/Annotation-2022-06-20-103520.png)

Voici la structure de dossiers d'un [générateur de blagues](https://blooming-reef-46396.herokuapp.com/) que j'ai construit pour mon footballeur préféré.

Des exemples de langages de programmation qui utilisent MVC sont C, C++, C#, Java, Ruby, Smalltalk, et bien d'autres.

Les frameworks qui utilisent MVC sont Angular, Express, Django, Flask, Laravel, Ruby on Rails, et d'autres.


## Qu'est-ce que le Modèle dans MVC ?

Le composant modèle contient la logique responsable de la récupération des données de la base de données. Pour cela, vous pouvez également utiliser un fichier JSON à la place d'une base de données.

Par exemple, dans la base de données SQL d'une application eCommerce, cela pourrait être quelque chose comme `product-data = db.get(SELECT * FROM products;`).

Dans de nombreux cas, le modèle communique avec le contrôleur pour envoyer des données à la vue (interface utilisateur). Dans d'autres cas, le modèle peut envoyer des données directement à la vue.


## Qu'est-ce que la Vue dans MVC ?

Le composant vue est la partie avec laquelle l'utilisateur interagit directement. Il communique avec le contrôleur pour montrer ce que l'utilisateur a demandé avec des actions de souris et de clavier.

Des langages comme HTML, CSS et JavaScript sont souvent utilisés pour implémenter cette partie. Vous pouvez également utiliser des frameworks comme React, Vue et Svelte.

Certains développeurs utilisent également des moteurs de templates comme Handlebars, ejs et liquidjs pour implémenter la vue.

Dans une application eCommerce, le code pourrait contenir quelque chose comme ceci :
```js
<h1>{{product.name}}</h2>
<ul>
<p>{{product.description}}</p>
<p>{{product.delivery-modes}}</p>
```


## Qu'est-ce que le Contrôleur dans MVC ?

Le composant contrôleur est l'intermédiaire entre le modèle et la vue. Il n'est ni modèle ni vue – c'est la partie qui les relie.

Ce que le contrôleur fait avec la vue, c'est recevoir et traiter les requêtes et actions de l'utilisateur effectuées avec la vue (interface utilisateur). Ainsi, il traite les requêtes comme `GET`, `POST`, `PUT` ou `PATCH`, et `DELETE`.

Lorsque le contrôleur reçoit les requêtes de l'utilisateur, il communique ensuite avec le modèle pour obtenir ce que l'utilisateur veut, puis le renvoie à la vue (interface utilisateur) pour que l'utilisateur puisse le voir.

Un pseudocode pour ce que fait le contrôleur est dans l'extrait ci-dessous :
```
if (success) {
      show products;
} else {
      show error;
}
```


## Conclusion

Le modèle-vue-contrôleur est devenu un modèle d'architecture largement utilisé pour la création d'applications web et d'autres produits logiciels.

Cela peut être déroutant au début, mais un apprentissage et une pratique persistants devraient vous aider à clarifier votre confusion.

Si vous êtes toujours confus quant à ce qu'est MVC, voyez-le de cette manière :
- **vous** appelez un restaurant pour commander une pizza – vous êtes la `vue`
- vous donnez votre commande à un **serveur** – le serveur est le `contrôleur`
- le serveur récupère votre pizza dans le **magasin** et vous la donne – le magasin est le `modèle`

Vous pouvez voir que vous, la `vue`, n'avez jamais à aller au magasin pour votre pizza, tout comme la vue ne récupère jamais directement les données du modèle dans de nombreuses occasions.

Merci d'avoir lu.
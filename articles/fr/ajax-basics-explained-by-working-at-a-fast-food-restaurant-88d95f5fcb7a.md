---
title: Les bases de l'AJAX expliquées en travaillant dans un restaurant de fast-food
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-15T04:22:43.000Z'
originalURL: https://freecodecamp.org/news/ajax-basics-explained-by-working-at-a-fast-food-restaurant-88d95f5fcb7a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5NmA_RD2IAd7_htOB7RKNA.jpeg
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Les bases de l'AJAX expliquées en travaillant dans un restaurant de fast-food
seo_desc: 'By Kevin Kononenko

  AJAX (Asynchronous JavaScript And XML) can be pretty confusing if you do not have
  a firm understanding of server-side code.

  When I started with web development, I first learned HTML, CSS, JavaScript, and
  jQuery before I ventured in...'
---

Par Kevin Kononenko

**AJAX (Asynchronous JavaScript And XML) peut être assez déroutant si vous n'avez pas une compréhension solide du code côté serveur.**

Lorsque j'ai commencé le développement web, j'ai d'abord appris HTML, CSS, JavaScript et jQuery avant de me lancer dans Node.js et Ruby on Rails.

Mais, bien sûr, je voulais comprendre comment construire des applications web dynamiques, alors j'avais besoin d'apprendre à utiliser AJAX pour communiquer avec un serveur. Je ne voulais pas simplement créer des pages statiques comme celles de 2005.

Le front-end est un défi complètement différent du back-end. J'ai eu du mal à comprendre les différentes parties d'une requête GET ou POST.

Alors, j'ai imaginé l'analogie d'un restaurant de fast-food pour l'expliquer. Si vous êtes déjà allé chez McDonald's, Burger King ou Wendy's, alors vous pouvez écrire vos propres requêtes GET et POST.

Pour comprendre cet article, vous aurez besoin d'avoir une compréhension de base de jQuery.

### À quoi ressemble AJAX ?

Avez-vous déjà remarqué que vous pouvez commenter une publication sur Facebook sans recharger toute la page ? C'est AJAX en action. **AJAX** permet aux utilisateurs d'interagir avec votre application web sans recharger complètement la page.

Imaginez si, chaque fois que vous "aimiez" une publication sur Facebook ou que vous ajoutiez un commentaire, la page se rechargeait ? Ce serait terrible ! Au lieu de cela, Facebook ajoute rapidement votre "commentaire" ou "j'aime" à la publication et vous permet de continuer à lire. Ils ajoutent cette interaction à leur base de données sans interrompre votre expérience !

### Pourquoi avons-nous besoin d'AJAX ?

D'accord, ce sont des exemples anecdotiques, alors regardons l'ensemble du système.

Imaginez votre application web entière comme un restaurant de fast-food. Vous êtes le caissier, la personne en première ligne. Vous gérez les **requêtes** des clients.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PBD--x73I4_zG0Kh.)

Si vous regardez ce diagramme, je peux voir trois tâches distinctes qui doivent être accomplies.

1. Le caissier doit traiter les demandes des utilisateurs à un rythme rapide.
2. Vous avez besoin de cuisiniers pour mettre les burgers sur le grill et cuisiner toute la nourriture.
3. Vous avez besoin d'une équipe de préparation des repas pour emballer la nourriture et la mettre dans un sac ou sur un plateau.

Cependant, si vous n'aviez pas AJAX, vous ne seriez autorisé à traiter qu'une commande à la fois, du début à la fin ! Vous devriez prendre la commande... puis facturer le client... puis rester là à ne rien faire pendant que les personnes dans la cuisine cuisinent la nourriture... puis continuer à attendre pendant que l'équipe de préparation des repas l'emballe. Vous ne pourriez prendre la commande suivante qu'après tout cela.

![Image](https://cdn-media-1.freecodecamp.org/images/0*89PNzvIka550TPv2.)

Maintenant, CELA est une mauvaise expérience utilisateur ! Vous ne pourriez plus l'appeler "fast food". Au lieu de cela, vous devriez l'appeler "nourriture médiocre"... ou quelque chose comme ça.

AJAX permet un **modèle de traitement asynchrone**. Cela signifie que vous pouvez demander des données ou envoyer des données sans recharger toute la page. C'est exactement comme le fonctionnement d'un restaurant de fast-food normal. En tant que caissier, vous prenez la commande du client, vous l'envoyez à l'équipe de cuisine et vous vous préparez à prendre la commande du client suivant.

Les clients peuvent continuer à passer des commandes, et vous n'avez pas besoin de rester là pendant que les employés de la cuisine travaillent et font attendre tout le monde.

Cela introduit certainement une certaine complexité. Vous avez maintenant plusieurs spécialisations au sein du restaurant. De plus, les commandes sont traitées à des rythmes différents. Mais cela crée une bien meilleure expérience utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*716D3LoopXh8ILWC.)

Vous avez probablement vu cela en action dans un restaurant vous-même. Une personne s'occupe de la machine à frites. Une personne gère le grill. Lorsqu'une commande arrive, le caissier peut instantanément communiquer avec les deux et revenir à la prise de commandes.

### Comment créer une requête POST

Mettons ces concepts en pratique. En tant que caissier, vous devez envoyer les commandes des clients entrantes à la cuisine afin que le reste de votre équipe puisse préparer le repas. Vous pouvez le faire avec une requête POST.

Dans votre code réel, une requête POST envoie des données à votre serveur. Cela signifie que vous envoyez des données de commande au back-end, dans ce cas.

Elle comporte trois parties principales :

1. **Une URL** : il s'agit de la route que la requête suivra. Plus d'informations dans un instant.
2. **Données** : tous les paramètres supplémentaires que vous devez envoyer au serveur.
3. [**Callback**](https://blog.codeanalogies.com/2016/04/11/javascript-callbacks-explained-using-minions/) : Ce qui se passe après avoir envoyé la requête

Quelles sont les choses courantes que les gens commandent dans un restaurant de fast-food ? Regardons 2 exemples.

1. Des frites
2. Un menu composé d'un burger, de frites et d'une boisson

Ces deux commandes nécessitent des processus différents. Une commande de frites peut nécessiter qu'une seule personne mette des frites dans un sachet. Mais une commande de menu nécessitera le travail de plusieurs membres de l'équipe. Donc, ces deux commandes nécessitent des URLs différentes.

```
$.post('/comboMeal')
```

```
$.post('/fries')
```

L'URL nous permet d'utiliser la même logique sur le back-end pour certains types de requêtes. Cette partie est hors du cadre de ce tutoriel, alors vous pouvez approfondir cela lorsque vous regarderez le back-end.

Ensuite, il y a les **données**. Il s'agit d'un [objet](https://blog.codeanalogies.com/2017/04/29/javascript-arrays-and-objects-are-just-like-books-and-newspapers/) qui nous donne un peu plus d'informations sur la requête. Pour l'URL du menu, nous devons probablement savoir :

1. Le type de plat principal
2. Le type de boisson
3. Le prix
4. Toutes les demandes spéciales

Pour les frites, nous devons peut-être seulement savoir :

1. La taille des frites
2. Le prix

![Image](https://cdn-media-1.freecodecamp.org/images/0*6W8k6X4azQU9Jb3b.)

Regardons un exemple de menu : un cheeseburger avec un Pepsi qui coûte 6,00 $. Voici à quoi cela ressemble en JavaScript.

```
let order = {  mainMeal: 'cheeseburger',  drink: 'Pepsi',  price: 6,   exceptions: '' };
```

```
$.post('/comboMeal', order);
```

La variable _order_ contient le contenu de la commande. Ensuite, nous l'incluons dans la requête POST afin que notre personnel de cuisine sache quoi mettre dans le menu !

Mais nous ne pouvons pas avoir tout ce code qui s'exécute à un moment aléatoire ! Nous avons besoin d'un événement déclencheur qui lancera la requête. Dans ce cas, une commande client dans un restaurant de fast-food est un peu comme une personne qui clique sur un bouton "commande" sur votre site web. Nous pouvons utiliser l'événement [click()](https://api.jquery.com/click/) de jQuery pour exécuter le POST lorsque l'utilisateur clique sur un bouton.

```
$('button').click(function(){   let order = {     mainMeal: 'cheeseburger',    drink: 'Pepsi',     price: 6,     exceptions: ''   };   $.post('/comboMeal', order); });
```

Dernière partie. Nous devons dire quelque chose au client après que sa commande a été envoyée. Les caissiers disent généralement "Client suivant, s'il vous plaît !" puisque c'est un restaurant de fast-food, alors nous pouvons utiliser cela dans le callback pour montrer que la commande a été soumise.

```
$('button').click(function(){    let order = {     mainMeal: 'cheeseburger',     drink: 'Pepsi',     price: 6,     exceptions: ''    };
```

```
$.post('/comboMeal', order, function(){     alert('Client suivant, s'il vous plaît !');   }); })
```

### Comment créer une requête GET

Jusqu'à présent, nous avons la capacité de soumettre une commande. Maintenant, nous avons besoin d'un moyen de livrer cette commande à notre client.

C'est là que les requêtes GET interviennent. GET nous permet de demander des données au serveur (ou à la cuisine, dans cette analogie). Veuillez noter : pour l'instant, notre base de données est remplie de commandes, et non de la nourriture elle-même. C'est une distinction importante car **les requêtes GET ne modifient pas notre base de données**. Elles livrent simplement ces informations au front-end. Les requêtes POST modifient les informations dans la base de données.

Voici quelques questions typiques que l'on pourrait vous poser avant de recevoir votre nourriture.

1. Souhaitez-vous manger ici ou emporter la nourriture ?
2. Avez-vous besoin de condiments (comme du ketchup ou de la moutarde) ?
3. Quel est votre numéro sur le reçu (pour vérifier que c'est bien votre nourriture) ?

Alors, disons que vous avez commandé trois menus pour votre famille. Vous voulez manger la nourriture dans le restaurant. Vous avez besoin de ketchup. Et le numéro sur votre reçu est 191.

Nous pouvons créer une requête GET avec une URL '/comboMeal', qui correspond à la requête POST avec la même URL. Cependant, cette fois, nous avons besoin de données différentes. C'est un type de requête totalement différent. Le même nom d'URL nous permet simplement de mieux organiser notre code.

```
let meal = {  location: 'here',  condiments: 'ketchup',  receiptID: 191 };
```

```
$.get('/comboMeal', meal);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*v3wuuGaPDFsYr-pgR7a6bg.png)

Nous avons également besoin d'un déclencheur pour celui-ci. Cette requête est déclenchée par les réponses des clients à vos questions en tant que caissier avant de leur livrer la nourriture. Il n'y a pas de moyen pratique de représenter des questions et des réponses avec JavaScript. Alors je vais simplement créer un autre événement de clic pour le bouton avec la classe 'answer'.

```
$('.answer').click(function(){  let meal = {     location: 'here',     condiments: 'ketchup',     idNumber: 191,   };
```

```
$.get('/comboMeal', meal); });
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*dbcZP0FyqCa19uYK.)

Celui-ci a également besoin d'une fonction de callback, car nous allons recevoir ce qui était contenu dans les trois menus de la commande 191. Nous pouvons recevoir ces données via un paramètre _data_ dans notre callback.

Cela retournera ce que le back-end stipule pour la commande 191. Je vais utiliser une fonction nommée _eat_ pour signifier que vous finissez par manger la nourriture, mais gardez à l'esprit qu'il n'y a pas de fonction eat en JavaScript !

```
$('.answer').click(function(){   let meal = {     location: 'here',     condiments: 'ketchup',     idNumber: 191,    };   //data contient les données du serveur   $.get('/comboMeal', meal, function(data){      //eat est une fonction inventée mais vous voyez le point      eat(data);   }); });
```

Le produit final, _data_, contiendrait le contenu des trois menus, théoriquement. Cela dépend de la façon dont cela est écrit sur le back-end !

![Image](https://cdn-media-1.freecodecamp.org/images/0*CmjCchSTgQN7L6Bg.)

### Essayez d'autres explications visuelles

Avez-vous aimé ce tutoriel ? Applaudissez-le pour que d'autres puissent le voir ! Ou, **inscrivez-vous à la newsletter** pour être informé des dernières sorties de tutoriels CSS et JavaScript.
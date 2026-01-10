---
title: AJAX Expliqué en Améliorant Votre Personnage de Jeu Vidéo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-20T17:58:53.000Z'
originalURL: https://freecodecamp.org/news/ajax-explained-by-upgrading-your-video-game-character-17d26305163c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qxz_AwMSypWEHpIIwcCmzQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: AJAX Expliqué en Améliorant Votre Personnage de Jeu Vidéo
seo_desc: 'By Kevin Kononenko

  If you’ve played video games, then you can understand the basics of POST and GET.

  AJAX (short for Asynchronous JavaScript and XML) can be pretty tough for new web
  developers to grasp. Without a sense of how the browser interacts wi...'
---

Par Kevin Kononenko

#### Si vous avez joué à des jeux vidéo, alors vous pouvez comprendre les bases de POST et GET.

AJAX (abréviation de Asynchronous JavaScript and XML) peut être assez difficile à comprendre pour les nouveaux développeurs web. Sans une idée de la manière dont le navigateur interagit avec le serveur, AJAX peut sembler être alimenté par de la magie.

Mais ne perdez pas espoir. Pensez à AJAX comme étant similaire à la manière dont vous améliorez votre personnage dans les jeux de rôle comme Pokemon ou Final Fantasy.

Vous pouvez utiliser AJAX pour construire des applications web modernes avec un **nombre minimum de rechargements de page**. Si vous voulez construire un site qui passe facilement entre différents écrans et fonctionnalités, alors vous aurez besoin d'AJAX pour charger du contenu dynamiquement en fonction des requêtes des utilisateurs.

Cet article se concentrera sur les façons dont vous pouvez interagir avec un serveur en utilisant les deux méthodes AJAX les plus courantes : POST et GET.

Je vais supposer que vous connaissez déjà les [bases des callbacks](https://medium.freecodecamp.com/javascript-callbacks-explained-using-minions-da272f4d9bcd). De plus, je supposerai que vous avez déjà défini un endroit dans votre application web où vous devez charger des données dynamiquement.

### Les requêtes POST sont comme ajouter des objets à votre inventaire

Vous pouvez utiliser POST pour ajouter des données à votre base de données. Dans votre jeu vidéo, cela ressemble un peu au processus où vous ouvrez chaque coffre au trésor en vue jusqu'à ce que vous trouviez l'objet dont vous avez besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ae5a20w-_EBjOjMVr3nwIA.png)

Disons que vous avez besoin d'une nouvelle arme pour relever de plus grands défis dans votre jeu. Vous fouillez chaque cache d'objets jusqu'à ce que vous la trouviez enfin — une nouvelle épée ! Cette arme est plus légère, plus rapide et plus forte que la massue avec laquelle vous avez commencé le jeu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OwUtGFxXM2s3pZUuamn-Og.png)

Alors maintenant, vous voulez ramasser cette épée géniale et vous débarrasser de votre vieille massue puante. D'un point de vue code, il y a quelques choses que vous devez stocker :

1. Le type d'équipement que vous ajoutez (épée)
2. Le poids (disons 20)
3. Les dégâts par coup (disons 10)
4. Son type de métal (disons acier)
5. Capacité de défense/blocage (disons 5)

Pour envoyer ces données au serveur et les sauvegarder, vous devrez les POST.

Notez que nous utiliserons jQuery — l'une des bibliothèques JavaScript les plus populaires — pour simplifier le processus de réalisation de ces requêtes.

Votre requête POST aura 4 parties :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BCjBuV9KqEe8UAt6suztmQ.png)

1. si vous faites `$.post` ou `$.get`
2. La **route**. Une route est un motif répétable que votre back-end reconnaîtra. Dans ce cas, l'ajout de presque n'importe quel équipement, comme une épée, un bouclier ou une cuirasse, suivra un motif similaire car ils peuvent tous être équipés sur votre personnage. Vous utiliseriez une route différente si vous collectiez des ressources, comme du minerai de métal, du bois ou des pièces. Bien que celles-ci doivent être stockées, elles ne seraient pas « équipées » sur votre personnage — simplement stockées dans votre inventaire. Ces routes pourraient être « /gatherResource » ou « /collectCoins ».
3. Les données qui seront réellement stockées. Ici, vous stockez les attributs de l'équipement : type d'équipement, dégâts, poids, etc., comme nous l'avons décrit ci-dessus. Nous pouvons utiliser un objet pour cela.
4. Le callback. Cela vous permet de spécifier ce qui doit se passer directement après la fin du POST. Vous pouvez vouloir équiper l'épée et abandonner la massue.

Voici le code final que vous utiliseriez pour stocker l'épée :

```javascript
$.post(
  '/storeEquipment',
  {
    type: 'sword',
    weight: 20,
    damage: 10,
    metal: 'steel',
    defense: 5
  },
  function(response) {
    // Équiper l'épée et abandonner la massue
    equip('sword');
    drop('club');
  }
);
```

La partie la plus difficile est de déterminer ce qui doit aller dans la route et ce qui va dans les paramètres/données. Dans ce cas, vous écrivez une route `storeEquipment` plus généralisée, car vous pouvez suivre une procédure similaire pour ajouter n'importe quel type d'équipement. Les paramètres vous permettent d'offrir des spécificités.

Les bases de données relationnelles sont un peu en dehors du cadre de ce tutoriel, mais si vous vouliez configurer une base de données pour stocker cela, vous pourriez créer une table « equipment » qui stocke tout l'équipement pour chaque utilisateur. Cela ressemblerait à quelque chose comme ceci :

```sql
CREATE TABLE equipment (
  id INT PRIMARY KEY,
  user_id INT,
  type VARCHAR(255),
  weight INT,
  damage INT,
  metal VARCHAR(255),
  defense INT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

Lorsque vous construisez une application web, vous pourriez utiliser une requête POST pour :

1. Créer un nouvel utilisateur
2. Stocker une entrée créée par un utilisateur
3. Stocker un commentaire créé par un utilisateur

### Les requêtes GET sont comme faire apparaître des ennemis

Les requêtes GET vous permettent de récupérer des données déjà stockées dans votre base de données. Vous ne modifiez ni n'ajoutez rien — vous présentez simplement des données qui existent déjà. Cela ressemble un peu à quand vous courez dans Pokemon, et que cela se produit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZtMtaBNANbl6S_K8ajCpSg.jpeg)

Disons que vous écrasez ce pauvre Diglett. Cela ne changerait pas le fait qu'il existe un Pokemon appelé Diglett qui existe sur votre serveur. Vous pourrez toujours affronter des Diglett à l'avenir.

Disons que vous courez dans un donjon, et que vous faites face à l'ennemi le plus terrifiant de tous les temps : le squelette (pas vraiment).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_0pq6O6wWL0wqr4e92s-Ww.png)

Nous devons écrire le code pour que ce squelette aléatoire ait certains traits. Voici à quoi pourraient ressembler certains de ses attributs :

1. Type : squelette
2. Attaque : 10
3. Mobilité : 5
4. Défense : 2
5. Équipement : casque, masse

Vous pourriez structurer votre GET comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2r7GCghEGEMWXZzMMi3s0g.png)

1. `$.get` ou `$.post`
2. La route. Une route GET signifie que vous allez récupérer des données du serveur dans un package spécifique. Similaire à POST, vous voulez que cette route soit généralisée pour capturer tout type d'interaction avec un ennemi.
3. Les paramètres. Les détails sur cet ennemi spécifique.
4. Le callback. Ce qui se passe lorsque vous engagez cet ennemi dans un combat ?

Lorsque vous avez initialement construit le jeu, vous avez déterminé à quoi ressemblerait un squelette, comment il bougerait. Maintenant, vous devez créer dynamiquement un squelette qui affrontera votre personnage. La requête GET vous permettra d'invoquer un squelette avec des traits spécifiques dictés par vos paramètres.

Si votre personnage vainc ce squelette, cela ne supprimera rien de votre serveur. Cela signifie simplement que votre personnage était supérieur à cette combinaison particulière de données que le squelette représentait.

Maintenant, disons que vous construisez un site de commerce électronique où vous vendez des boîtes en carton. L'utilisateur peut vouloir trier ses choix en fonction de :

1. L'épaisseur de la boîte
2. La taille de la boîte
3. La quantité disponible

Vous voudriez permettre à l'utilisateur de trier les choix dynamiquement. Vous utiliseriez donc une requête GET pour récupérer toutes les boîtes avec les traits spécifiques sans faire recharger la page à l'utilisateur chaque fois qu'une boîte est cochée ou décochée.

### En résumé...

![Image](https://cdn-media-1.freecodecamp.org/images/1*m7N44wJHN0FhFuyzwA3BCg.png)

* Votre base de données est remplie de composants qui peuvent être invoqués et présentés à l'utilisateur. Certains ont été initialisés avec l'application, et d'autres sont ajoutés par l'utilisateur.
* Une requête POST vous permet d'ajouter des composants à la base de données.
* Une requête GET vous permet d'invoquer dynamiquement des composants intégrés et précédemment ajoutés. Ils peuvent être combinés de différentes manières en fonction des paramètres de la requête GET.

Si vous avez aimé cet article, vous aimerez peut-être mes [autres explications](https://www.rtfmanual.io/guides/) de sujets CSS et JavaScript difficiles, comme le positionnement, le Modèle-Vue-Contrôleur et les callbacks.

Et si vous pensez que cela pourrait aider d'autres personnes dans la même situation que vous, donnez-lui un « cœur » !
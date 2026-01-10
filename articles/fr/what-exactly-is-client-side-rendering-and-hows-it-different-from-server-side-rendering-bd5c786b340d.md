---
title: 'Rendu côté client vs. rendu côté serveur : pourquoi ce n''est pas tout noir
  ou blanc'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-28T21:34:12.000Z'
originalURL: https://freecodecamp.org/news/what-exactly-is-client-side-rendering-and-hows-it-different-from-server-side-rendering-bd5c786b340d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ezyfYx8OjGnPbxDTlzV9Kg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: 'Rendu côté client vs. rendu côté serveur : pourquoi ce n''est pas tout
  noir ou blanc'
seo_desc: 'By Cristian Vega

  Since the dawn of time, the conventional method for getting your HTML up onto a
  screen was by using server-side rendering. It was the only way. You loaded up your
  .html pages on your server, then your server went and turned them into...'
---

Par Cristian Vega

Depuis l'aube de l'informatique, la méthode conventionnelle pour afficher votre HTML à l'écran était d'utiliser le rendu côté serveur. C'était la seule façon. Vous chargiez vos pages .html sur votre serveur, puis votre serveur les transformait en documents utilisables sur les navigateurs de vos utilisateurs.

Le rendu côté serveur fonctionnait très bien à l'époque, puisque la plupart des pages web étaient principalement destinées à afficher des images statiques et du texte, avec peu d'interactivité.

Aujourd'hui, ce n'est plus le cas. On pourrait dire que les sites web de nos jours ressemblent davantage à des applications qui se font passer pour des sites web. Vous pouvez les utiliser pour envoyer des messages, mettre à jour des informations en ligne, faire des achats, et bien plus encore. Le web est tout simplement beaucoup plus avancé qu'avant.

Il est donc logique que le rendu côté serveur commence lentement à prendre du retard par rapport à la méthode de plus en plus populaire de rendu des pages web côté client.

Alors, quelle méthode est la meilleure option ? Comme pour la plupart des choses en développement, cela dépend vraiment de ce que vous prévoyez de faire avec votre site web. Vous devez comprendre les avantages et les inconvénients, puis décider par vous-même quelle voie est la meilleure pour vous.

### **Comment fonctionne le rendu côté serveur**

Le rendu côté serveur est la méthode la plus courante pour afficher des informations à l'écran. Il fonctionne en convertissant les fichiers HTML sur le serveur en informations utilisables pour le navigateur.

Chaque fois que vous visitez un site web, votre navigateur envoie une requête au serveur qui contient le contenu du site web. La requête prend généralement quelques millisecondes, mais cela dépend finalement de nombreux facteurs :

* Votre vitesse de connexion internet
* L'emplacement du serveur
* Le nombre d'utilisateurs essayant d'accéder au site
* Et l'optimisation du site web, pour n'en nommer que quelques-uns

Une fois la requête traitée, votre navigateur reçoit le HTML entièrement rendu et l'affiche à l'écran. Si vous décidez ensuite de visiter une autre page sur le site web, votre navigateur enverra à nouveau une autre requête pour les nouvelles informations. Cela se produira chaque fois que vous visiterez une page dont votre navigateur n'a pas de version en cache.

Peu importe si la nouvelle page n'a que quelques éléments différents de la page actuelle, le navigateur demandera la nouvelle page entière et tout sera rendu à nouveau à partir de zéro.

Prenons par exemple ce document HTML qui a été placé sur un serveur imaginaire avec une adresse HTTP de `example.testsite.com`.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Example Website</title>
  </head>
  <body>
    <h1>My Website</h1>
    <p>This is an example of my new website</p>
    <a href="http://example.testsite.com/other.html.">Link</a>
  </body>
</html>
```

Si vous deviez taper l'adresse du site web exemple dans l'URL de votre navigateur imaginaire, votre navigateur imaginaire enverrait une requête au serveur utilisé par cette URL et attendrait une réponse de texte à afficher sur le navigateur. Dans ce cas, ce que vous verriez visuellement serait le titre, le contenu du paragraphe et le lien.

Maintenant, supposons que vous souhaitiez cliquer sur le lien de la page rendue qui contient le code suivant.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Example Website</title>
  </head>
  <body>
    <h1>My Website</h1>
    <p>This is an example of my new website</p>
    <p>This is some more content from the other.html</p>
  </body>
</html>
```

La seule différence entre la page précédente et celle-ci est que cette page n'a pas de lien et a plutôt un autre paragraphe. La logique dicterait que seul le nouveau contenu devrait être rendu et le reste devrait être laissé tel quel. Hélas, ce n'est pas ainsi que fonctionne le rendu côté serveur. Ce qui se passerait réellement, c'est que la nouvelle page entière serait rendue, et non seulement le nouveau contenu.

Bien que cela ne semble pas être un gros problème pour ces deux exemples, la plupart des sites web ne sont pas aussi simples. Les sites web modernes ont des centaines de lignes de code et sont beaucoup plus complexes. Imaginez maintenant naviguer sur une page web et devoir attendre que chaque page soit rendue lors de la navigation sur le site. Si vous avez déjà visité un site WordPress, vous avez vu à quel point ils peuvent être lents. C'est l'une des raisons pour lesquelles.

Du bon côté, le rendu côté serveur est excellent pour le SEO. Votre contenu est présent avant de l'obtenir, donc les moteurs de recherche peuvent l'indexer et le parcourir sans problème. Ce qui n'est pas le cas avec le rendu côté client. Du moins, pas simplement.

### **Comment fonctionne le rendu côté client**

Lorsque les développeurs parlent de rendu côté client, ils parlent de rendre le contenu dans le navigateur en utilisant JavaScript. Ainsi, au lieu d'obtenir tout le contenu du document HTML lui-même, vous obtenez un document HTML squelettique avec un fichier JavaScript qui rendra le reste du site en utilisant le navigateur.

C'est une approche relativement nouvelle pour le rendu des sites web, et elle n'est vraiment devenue populaire que lorsque les bibliothèques JavaScript ont commencé à l'incorporer dans leur style de développement. Quelques exemples notables sont Vue.js et React.js, dont j'ai [écrit plus en détail ici](https://medium.freecodecamp.com/reacts-jsx-vs-vue-s-templates-a-showdown-on-the-front-end-b00a70470409#.ycvoyji7a).

En revenant au site web précédent, `example.testsite.com`, supposons que vous avez maintenant un fichier index.html avec les lignes de code suivantes.

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Example Website</title>
</head>
<body>
  <div id="root">
    <app></app>
  </div>
  <script src="https://vuejs.org"type="text/javascript"></script>
  <script src="location/of/app.js"type="text/javascript"></script>
</body>
</html>
```

Vous pouvez voir tout de suite qu'il y a des changements majeurs dans la façon dont le fichier index.html fonctionne lors du rendu en utilisant le client.

Pour commencer, au lieu d'avoir le contenu à l'intérieur du fichier HTML, vous avez un div conteneur avec un id de root. Vous avez également deux éléments de script juste au-dessus de la balise de fermeture du body. L'un qui chargera la bibliothèque JavaScript Vue.js et l'autre qui chargera un fichier appelé app.js.

Cela est radicalement différent de l'utilisation du rendu côté serveur, car le serveur n'est maintenant responsable que du chargement du minimum squelettique du site web. La principale structure de base. Tout le reste est géré par une bibliothèque JavaScript côté client, dans ce cas, Vue.js, et du code JavaScript personnalisé.

Si vous deviez faire une requête à l'URL avec uniquement le code ci-dessus, vous obtiendriez un écran vide. Il n'y a rien à charger puisque le contenu réel doit être rendu en utilisant JavaScript.

Pour corriger cela, vous placeriez les lignes de code suivantes dans le fichier app.js.

```js
var data = {
        title:"My Website",
        message:"This is an example of my new website"
      }
  Vue.component('app', {
    template:
    `
    <div>
    <h1>{{title}}</h1>
    <p id="moreContent">{{message}}</p>
    <a v-on:click='newContent'>Link</a>
    </div>
    `,
    data: function() {
      return data;
    },
    methods:{
      newContent: function(){
        var node = document.createElement('p');
        var textNode = document.createTextNode('This is some more content from the other.html');
        node.appendChild(textNode);
        document.getElementById('moreContent').appendChild(node);
      }
    }
  })
  new Vue({
    el: '#root',
  });
```

Maintenant, si vous visitez l'URL, vous verriez le même contenu que dans l'exemple côté serveur. La différence clé est que si vous cliquiez sur le lien pour charger plus de contenu, le navigateur ne ferait pas une autre requête au serveur. Vous rendez les éléments avec le navigateur, donc il utilisera plutôt JavaScript pour charger le nouveau contenu et Vue.js s'assurera que seul le nouveau contenu est rendu. Tout le reste sera laissé tel quel.

C'est beaucoup plus rapide puisque vous ne chargez qu'une très petite section de la page pour récupérer le nouveau contenu, au lieu de charger la page entière.

Il y a quelques compromis avec l'utilisation du rendu côté client, cependant. Puisque le contenu n'est pas rendu avant que la page ne soit chargée sur le navigateur, le SEO du site web en prendra un coup. Il existe des moyens de contourner cela, mais ce n'est pas aussi facile qu'avec le rendu côté serveur.

Une autre chose à garder à l'esprit est que votre site web/application ne pourra pas se charger avant que TOUT le JavaScript ne soit téléchargé sur le navigateur. Ce qui est logique, puisque cela contient tout le contenu qui sera nécessaire. Si vos utilisateurs utilisent une connexion internet lente, cela pourrait rendre leur temps de chargement initial un peu long.

### Les avantages et les inconvénients de chaque approche

Voilà donc les principales différences entre le rendu côté serveur et le rendu côté client. Seul vous, le développeur, pouvez décider quelle option est la meilleure pour votre site web ou votre application.

Voici un bref résumé des avantages et des inconvénients de chaque approche :

#### Avantages du rendu côté serveur :

1. Les moteurs de recherche peuvent explorer le site pour un meilleur SEO.
2. Le chargement initial de la page est plus rapide.
3. Idéal pour les sites statiques.

#### Inconvénients du rendu côté serveur :

1. Requêtes fréquentes au serveur.
2. Un rendu globalement lent des pages.
3. Rechargements complets de la page.
4. Interactions non riches sur le site.

#### Avantages du rendu côté client :

1. Interactions riches sur le site
2. Rendu rapide du site web après le chargement initial.
3. Idéal pour les applications web.
4. Large sélection de bibliothèques JavaScript.

#### Inconvénients du rendu côté client :

1. SEO faible si non implémenté correctement.
2. Le chargement initial peut nécessiter plus de temps.
3. Dans la plupart des cas, nécessite une bibliothèque externe.

Si vous souhaitez en savoir plus sur Vue.js, consultez mon site web à l'adresse [juanmvega.com](https://juanmvega.com) pour des vidéos et des articles !
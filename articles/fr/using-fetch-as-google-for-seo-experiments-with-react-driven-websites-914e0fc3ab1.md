---
title: Tester le SEO d'un site web piloté par React en utilisant "Fetch as Google"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-04T10:23:04.000Z'
originalURL: https://freecodecamp.org/news/using-fetch-as-google-for-seo-experiments-with-react-driven-websites-914e0fc3ab1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iIwuLuv-yhL-KvqIS6IbuQ.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: SEO
  slug: seo
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Tester le SEO d'un site web piloté par React en utilisant "Fetch as Google"
seo_desc: 'By Patrick Hund

  I recently tested whether client-side rendering would prevent websites from being
  crawled by search engine robots. As my article showed, React doesn’t seem to hurt
  search engine indexing at all.

  Now I’m taking it to the next level. I’...'
---

Par Patrick Hund

J'ai récemment testé si le rendu côté client empêcherait les sites web d'être explorés par les robots des moteurs de recherche. Comme [mon article](https://medium.freecodecamp.com/seo-vs-react-is-it-neccessary-to-render-react-pages-in-the-backend-74ce5015c0c9#.eg3w0nh17) l'a montré, React ne semble pas nuire à l'indexation par les moteurs de recherche.

Maintenant, je passe à l'étape suivante. J'ai mis en place un projet React de type bac à sable pour voir exactement ce que Google peut explorer et indexer.

### Mise en place d'une petite application web

Mon objectif était de créer une application React minimaliste et de minimiser le temps passé à configurer Babel, webpack et autres outils. Je devrais ensuite déployer cette application sur un site web accessible au public le plus rapidement possible.

Je voulais également pouvoir déployer des mises à jour en production en quelques secondes.

Étant donné ces objectifs, les outils idéaux étaient [create-react-app](https://github.com/facebookincubator/create-react-app) et GitHub Pages.

Avec _create-react-app_, j'ai construit une petite application React en 30 minutes. Il suffisait de taper ces commandes :

```
create-react-app seo-sandbox
cd seo-sandbox
npm start
```

J'ai modifié le texte et le logo par défaut, joué avec la mise en forme, et voilà — une page web rendue à 100 % côté client, pour donner quelque chose à mâcher au Googlebot !

Vous pouvez voir mon projet [sur GitHub](https://github.com/pahund/seo-sandbox).

### Déploiement sur GitHub Pages

_create-react-app_ a été très utile. Presque psychique. Après avoir exécuté _npm run build_, il a reconnu que je prévoyais de publier mon projet sur GitHub Pages et m'a indiqué comment faire :

![Image](https://cdn-media-1.freecodecamp.org/images/o3GvoHmTJGknW561KjVEP6fJ5y1ZLu2WLN5V)

Voici mon bac à sable SEO hébergé sur GitHub Pages : [https://pahund.github.io/seo-sandbox/](https://pahund.github.io/seo-sandbox/)

![Image](https://cdn-media-1.freecodecamp.org/images/Ve9ZLv8Jsj1pVhn6PyfxHlsiVxMNZvTODMWI)
_J'ai utilisé « Argelpargel » comme nom pour mon site web car c'est un mot pour lequel Google n'avait aucun résultat de recherche_

### Configuration de la Google Search Console

Google fournit une suite d'outils gratuits appelée [Google Search Console](https://www.google.com/webmasters/tools) pour que les webmasters testent leurs sites web.

Pour la configurer, j'ai ajouté ce qu'ils appellent une « propriété » pour ma page web :

![Image](https://cdn-media-1.freecodecamp.org/images/ZDQJgCsvwCwPAfQDGPgKGM7O-zOt1SE0tnog)

Pour vérifier que j'étais bien le propriétaire du site web, j'ai dû télécharger un fichier spécial pour que Google le trouve sur le site. Grâce au mécanisme pratique _npm run deploy_, j'ai pu le faire en quelques secondes.

### Voir ma page web à travers les yeux de Google

Avec la configuration terminée, j'ai pu utiliser l'outil « Fetch as Google » pour voir ma page de bac à sable SEO comme le Googlebot la voit :

![Image](https://cdn-media-1.freecodecamp.org/images/9ALQTciaiNwYXQxGfIkZwBWOwjqpd20g04Gw)

Lorsque j'ai cliqué sur « Fetch and Render », j'ai pu examiner quelles parties de ma page pilotée par React pouvaient être indexées par Googlebot :

![Image](https://cdn-media-1.freecodecamp.org/images/-4yOQdw-qNDFSxoZKPueC2eyiHrB8uB4Z-HX)

### Ce que j'ai découvert jusqu'à présent

#### Découverte n°1 : Googlebot lit le contenu chargé de manière asynchrone

La première chose que je voulais tester était de savoir si Googlebot n'indexerait pas ou n'explorerait pas les parties de la page qui sont rendues de manière asynchrone.

Après le chargement de la page, mon application React effectue une requête Ajax pour obtenir des données, puis met à jour des parties de la page avec ces données.

Pour simuler cela, j'ai ajouté un constructeur à mon composant App qui définit l'état du composant avec un appel à [window.setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/WindowTimers/setTimeout).

```
constructor(props) {
    super(props);
    this.state = {
        choMessage: null,
        faq1: null,
        faq2: null,
        faq3: null
    };
    window.setTimeout(() => this.setState(Object.assign(this.state, {
        choMessage: 'yada yada'
    })), 10);
    window.setTimeout(() => this.setState(Object.assign(this.state, {
        faq1: 'bla bla'
    })), 100);
    window.setTimeout(() => this.setState(Object.assign(this.state, {
        faq2: 'shoo be doo'
    })), 1000);
    window.setTimeout(() => this.setState(Object.assign(this.state, {
        faq3: 'yacketiyack'
    })), 10000);
}
```

➜ [Voir le code réel sur GitHub](https://github.com/pahund/seo-sandbox/blob/v1.0.0/src/App.js#L14)

J'ai utilisé 4 délais différents de 10 millisecondes, 100 millisecondes, 1 seconde et 10 secondes.

Il s'avère que Googlebot abandonne uniquement le délai de 10 secondes. Les 3 autres blocs de texte apparaissent dans la fenêtre « Fetch as Google » :

![Image](https://cdn-media-1.freecodecamp.org/images/MlZfIJjVa4lURUAZZKRs7fHww3bruTqWw3kD)

#### React Router perturbe Googlebot

J'ai ajouté [React Router](https://react-router.now.sh/) (version 4.0.0-alpha.5) à mon application web pour créer une barre de menu qui charge diverses sous-pages (copiées et collées directement depuis leur documentation) :

![Image](https://cdn-media-1.freecodecamp.org/images/3NIFccb8Oc5fqK9ctECV5RqbPKdMentvwkj9)

Surprise, surprise — lorsque j'ai fait un « Fetch As Google », j'ai obtenu une page verte vide :

![Image](https://cdn-media-1.freecodecamp.org/images/ZvoDPaXtxwd0vOZWjecPiwu1AANIp0PRxqoG)

Il semble que l'utilisation de React Router pour les pages rendues côté client pose problème en termes de compatibilité avec les moteurs de recherche. Il reste à voir si ce problème est spécifique à la version alpha de React Router 4, ou s'il concerne également le React Router 3 stable.

### Expériences futures

Voici quelques autres choses que je souhaite tester avec ma configuration :

* Googlebot suit-il les liens dans les blocs de texte rendus de manière asynchrone ?
* Puis-je définir des balises meta comme _description_ de manière asynchrone avec mon application React et les faire comprendre par Googlebot ?
* Combien de temps faut-il à Googlebot pour explorer un site web rendu par React avec de nombreuses, nombreuses, nombreuses pages ?

Peut-être avez-vous d'autres idées. J'adorerais les lire dans les commentaires !
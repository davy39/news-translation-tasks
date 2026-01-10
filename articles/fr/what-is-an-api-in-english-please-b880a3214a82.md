---
title: Qu'est-ce qu'une API ? En français, s'il vous plaît.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-19T09:02:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F8R-PEI9iVJ-sY3qFZemCg.png
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce qu'une API ? En français, s'il vous plaît.
seo_desc: 'By Petr Gazarov

  Before I learned software development, API sounded like a kind of beer.

  Today I use the term so often that I have in fact recently tried to order an API
  at a bar.

  The bartender’s response was to throw a 404: resource not found.

  I meet...'
---

Par Petr Gazarov

Avant d'apprendre le développement logiciel, API évoquait pour moi un type de bière.

Aujourd'hui, j'utilise ce terme si souvent que j'ai en fait récemment essayé de commander une API dans un bar.

La réponse du barman a été de lancer une 404 : ressource introuvable.

Je rencontre beaucoup de personnes, travaillant dans la tech ou ailleurs, qui ont une idée plutôt vague ou incorrecte de ce que signifie ce terme assez courant.

Techniquement, API signifie **Interface de Programmation d'Application**. À un moment ou à un autre, la plupart des grandes entreprises ont construit des APIs pour leurs clients, ou pour un usage interne.

Mais comment expliquer API en français simple ? Et existe-t-il une signification plus large que celle utilisée en développement et en entreprise ? Commençons par examiner comment le web lui-même fonctionne.

## WWW et serveurs distants

Quand je pense au Web, j'imagine un grand réseau de serveurs connectés.

Chaque page sur internet est stockée quelque part sur un serveur distant. Un serveur distant n'est pas si mystérieux après tout — c'est simplement une partie d'un ordinateur situé à distance qui est optimisé pour traiter les requêtes.

Pour mettre les choses en perspective, vous pouvez lancer un serveur sur votre ordinateur portable capable de servir un site web entier sur le Web (en fait, un serveur local est ce que les ingénieurs utilisent pour développer des sites web avant de les publier).

Lorsque vous tapez [www.facebook.com](https://www.facebook.com/) dans votre navigateur, une requête est envoyée au serveur distant de Facebook. Une fois que votre navigateur reçoit la réponse, il interprète le code et affiche la page.

Pour le navigateur, également connu sous le nom de client, le serveur de Facebook est une API. Cela signifie que chaque fois que vous visitez une page sur le Web, vous interagissez avec l'API d'un serveur distant.

Une API n'est pas la même chose que le serveur distant — plutôt, **c'est la partie du serveur qui reçoit les requêtes et envoie les réponses**.

## Les APIs comme moyen de servir vos clients

Vous avez probablement entendu parler d'entreprises qui proposent des APIs comme produits. Par exemple, Weather Underground vend l'accès à son [API de données météorologiques](https://www.wunderground.com/weather/api).

**Scénario d'exemple :** Le site web de votre petite entreprise dispose d'un formulaire utilisé pour inscrire les clients à des rendez-vous. Vous souhaitez donner à vos clients la possibilité de créer automatiquement un événement Google Calendar avec les détails de ce rendez-vous.

**Utilisation de l'API :** L'idée est de faire en sorte que le serveur de votre site web communique directement avec le serveur de Google avec une requête pour créer un événement avec les détails donnés. Votre serveur recevrait ensuite la réponse de Google, la traiterait et renverrait des informations pertinentes au navigateur, comme un message de confirmation à l'utilisateur.

Alternativement, votre navigateur peut souvent envoyer une requête API directement au serveur de Google en contournant votre serveur.

**En quoi cette API Google Calendar est-elle différente de l'API de n'importe quel autre serveur distant ?**

**En termes techniques**, la différence réside dans le format de la requête et de la réponse.

Pour rendre la page web complète, votre navigateur attend une réponse en HTML, qui contient du code de présentation, tandis qu'un appel à l'API de Google Calendar ne retournerait que les données — probablement dans un format comme JSON.

Si le serveur de votre site web effectue la requête API, alors le serveur de votre site web est le client (similaire à votre navigateur étant le client lorsque vous l'utilisez pour naviguer vers un site web).

**Du point de vue de vos utilisateurs**, les APIs leur permettent de compléter l'action sans quitter votre site web.

La plupart des sites web modernes consomment au moins certaines APIs tierces.

De nombreux problèmes ont déjà une solution tierce, qu'il s'agisse d'une bibliothèque ou d'un service. Il est souvent plus facile et plus fiable d'utiliser une solution existante.

Il n'est pas rare que les équipes de développement divisent leur application en plusieurs serveurs qui communiquent entre eux via des APIs. Les serveurs qui effectuent des fonctions auxiliaires pour le serveur principal de l'application sont communément appelés [_microservices_](http://microservices.io/patterns/microservices.html).

Pour résumer, lorsqu'une entreprise propose une API à ses clients, cela signifie simplement qu'elle a construit un ensemble d'URLs dédiées qui retournent des réponses de données pures — ce qui signifie **que les réponses ne contiendront pas le type de surcharge de présentation que vous attendriez dans une interface utilisateur graphique comme un site web**.

Pouvez-vous effectuer ces requêtes avec votre navigateur ? Souvent, oui. Puisque la transmission HTTP réelle se fait en texte, votre navigateur fera toujours de son mieux pour afficher la réponse.

Par exemple, vous pouvez accéder directement à l'API de GitHub avec votre navigateur sans même avoir besoin d'un jeton d'accès. Voici la réponse JSON que vous obtenez lorsque vous visitez une route API d'utilisateur GitHub dans votre navigateur ([https://api.github.com/users/petrgazarov](https://api.github.com/users/petrgazarov)) :

```
{  "login": "petrgazarov",  "id": 5581195,  "avatar_url": "https://avatars.githubusercontent.com/u/5581195?v=3",  "gravatar_id": "",  "url": "https://api.github.com/users/petrgazarov",  "html_url": "https://github.com/petrgazarov",  "followers_url": "https://api.github.com/users/petrgazarov/followers",  "following_url": "https://api.github.com/users/petrgazarov/following{/other_user}",  "gists_url": "https://api.github.com/users/petrgazarov/gists{/gist_id}",  "starred_url": "https://api.github.com/users/petrgazarov/starred{/owner}{/repo}",  "subscriptions_url": "https://api.github.com/users/petrgazarov/subscriptions",  "organizations_url": "https://api.github.com/users/petrgazarov/orgs",  "repos_url": "https://api.github.com/users/petrgazarov/repos",  "events_url": "https://api.github.com/users/petrgazarov/events{/privacy}",  "received_events_url": "https://api.github.com/users/petrgazarov/received_events",  "type": "User",  "site_admin": false,  "name": "Petr Gazarov",  "company": "PolicyGenius",  "blog": "http://petrgazarov.com/",  "location": "NYC",  "email": "petrgazarov@gmail.com",  "hireable": null,  "bio": null,  "public_repos": 23,  "public_gists": 0,  "followers": 7,  "following": 14,  "created_at": "2013-10-01T00:33:23Z",  "updated_at": "2016-08-02T05:44:01Z"}
```

Le navigateur semble avoir bien affiché une réponse JSON. Une réponse JSON comme celle-ci est prête à être utilisée dans votre code. Il est facile d'extraire des données de ce texte. Ensuite, vous pouvez faire ce que vous voulez avec les données.

## A pour "Application"

Pour conclure, voici quelques exemples supplémentaires d'APIs.

"Application" peut désigner de nombreuses choses. En voici quelques-unes dans le contexte de l'API :

1. Un logiciel avec une fonction distincte.
2. Le serveur entier, l'application entière, ou juste une petite partie d'une application.

En gros, toute partie de logiciel qui peut être distinctement séparée de son environnement peut être un "A" dans API, et aura probablement aussi une sorte d'API.

Supposons que vous utilisez une bibliothèque tierce dans votre code. Une fois incorporée dans votre code, une bibliothèque devient une partie de votre application globale. Étant une partie distincte de logiciel, la bibliothèque aurait probablement une API qui lui permet d'interagir avec le reste de votre code.

Voici un autre exemple : En **Conception Orientée Objet**, le code est organisé en objets. Votre application peut avoir des centaines d'objets définis qui peuvent interagir les uns avec les autres.

Chaque objet a une API — un ensemble de méthodes et de propriétés publiques qu'il utilise pour interagir avec d'autres objets dans votre application.

Un objet peut également avoir une logique interne qui est privée, ce qui signifie qu'elle est cachée de la portée extérieure (et n'est pas une API).

J'espère que vous retiendrez de ce que nous avons couvert la signification plus large de l'API ainsi que les utilisations plus courantes du terme aujourd'hui.

### Ressources intéressantes (des choses que j'ai laissées de côté mais qui sont toujours très cool) :

[Une excellente vidéo YouTube sur le DNS (Domain Name System)](https://www.youtube.com/watch?v=72snZctFFtA&feature=youtu.be)

[Les bases du protocole HTTP](https://simple.wikipedia.org/wiki/Hypertext_Transfer_Protocol)

[Une vidéo géniale de Khan Academy sur les principes de la conception orientée objet](https://www.khanacademy.org/computing/computer-programming/programming/object-oriented/p/object-types#)
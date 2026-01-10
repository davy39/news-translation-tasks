---
title: Comment les pages Web sont rendues sur le navigateur – Différentes méthodes
  expliquées
subtitle: ''
author: Felix Favour Chinemerem
co_authors: []
series: null
date: '2022-10-26T22:00:00.000Z'
originalURL: https://freecodecamp.org/news/web-page-rendering-on-the-browser-different-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/fav-poster.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment les pages Web sont rendues sur le navigateur – Différentes méthodes
  expliquées
seo_desc: 'Today, all over the world, computers and networks are getting faster. This
  is good for web development and user experience in general. And the possibilities
  of what people can achieve have taken a massive leap forward.

  But although growth is evident ...'
---

Aujourd'hui, partout dans le monde, les ordinateurs et les réseaux deviennent plus rapides. C'est une bonne chose pour le développement web et l'expérience utilisateur en général. Et les possibilités de ce que les gens peuvent accomplir ont fait un bond en avant massif.

Mais bien que la croissance soit évidente dans de nombreux domaines, d'autres sont laissés pour compte dans cette course. La grande question est : comment pouvons-nous uniformiser l'expérience web compte tenu de cette fracture numérique et rendre le web plus accessible aux personnes disposant d'ordinateurs et de réseaux moins efficaces ?

Dans de nombreux cas, une réponse à cette question réside dans la compréhension de la manière dont nous rendons les pages web sur le navigateur.

## Termes utilisés dans cet article

Avant de continuer, je veux m'assurer que vous êtes familiarisé avec les termes utilisés dans cet article. Certains d'entre eux peuvent être particulièrement difficiles à comprendre pour les nouveaux développeurs. N'hésitez pas à passer à la section suivante si vous les connaissez déjà.

* **Serveur** : Un serveur est un ordinateur qui réside dans un emplacement distant (principalement sur Internet). Son travail consiste à traiter les requêtes du client et à générer une réponse.
* **Client** : Un client est tout appareil communiquant avec un serveur pour accéder à des ressources. Un client, dans de nombreux cas, est tout appareil capable d'accéder à Internet. Dans cet article, votre navigateur web joue le rôle du client.
* **CDN** : Acronyme de Content Delivery Network. Un CDN est "un réseau de serveurs interconnectés qui accélère le chargement des pages web pour les applications gourmandes en données" (source : [AWS](https://aws.amazon.com/what-is/cdn/) ).
* **Build-time** : Pendant le build-time, le code de votre application est préparé pour un autre environnement. La plupart du temps, un environnement hébergé sur Internet.

Maintenant, apprenons les différentes façons dont les sites web peuvent être rendus.

## Qu'est-ce que le rendu côté client (CSR) ?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/csr.jpg)

Le rendu côté client génère des pages web dans le navigateur, en s'appuyant entièrement sur votre code JavaScript. Le navigateur traite entièrement votre code JS avant que le contenu de votre page web ne soit visible pour l'utilisateur.

Votre code JavaScript aide à définir dynamiquement l'**architecture** du site web dès qu'il est téléchargé. L'architecture dans ce contexte signifie la récupération de données depuis une [API](https://aws.amazon.com/what-is/restful-api/), la navigation sur le site web et la logique métier simple sur votre site web.

### Rendu côté client et frameworks JavaScript

Le rendu côté client a gagné en popularité avec la sortie des frameworks et bibliothèques JavaScript comme React, Vue et Angular. Ces frameworks ne sont fonctionnels qu'en incluant un CDN dans l'en-tête d'une page HTML — et ces CDN contiennent généralement du code JS de grande taille.

Il n'est un secret pour personne que les fichiers volumineux entraînent un temps de téléchargement accru, mais il y a un piège ici : télécharger des fichiers volumineux lors du chargement initial de l'application signifie un temps de chargement considérablement réduit pour accéder à d'autres pages de ce site web.

Le site web récupère principalement des données depuis une API. Ces données sont ensuite utilisées pour remplir les pages rendues sur le client.

Vous pouvez trouver des exemples courants d'une application réelle utilisant le CSR dans de nombreuses applications web progressives (PWA) que nous utilisons aujourd'hui, comme Spotify, Figma et Google Drive.

## Qu'est-ce que le rendu côté serveur (SSR) ?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/ssr.jpg)

Le rendu côté client a été un changement de jeu et l'est encore — dans de nombreux cas. Bien qu'un examen plus approfondi des performances du CSR ait montré que plus un site web avait de fonctionnalités, plus il avait de code JS. Rappelez-vous que plus de code JS signifie plus de temps de téléchargement.

Les téléchargements lourds lors du chargement initial pour garantir un accès plus rapide à toutes les pages web ne semblaient pas être un compromis que certaines personnes étaient prêtes à faire. Cela a donné naissance au rendu côté serveur.

Le SSR ne résout pas tous les problèmes de rendu sur le web. Mais il a résolu de nombreux problèmes rencontrés par le CSR comme des temps de chargement plus rapides lors de la première visite et quelques autres mis en évidence dans la section Avantages et Compromis de cet article.

Le rendu côté serveur aide à générer une page web sur le serveur juste après avoir reçu une requête du navigateur. Avec le SSR, le serveur rend le HTML, CSS et JavaScript complets requis pour la ressource demandée et les renvoie au navigateur.

Cela signifie que vous pouvez toujours être sûr que le contenu du site web contient les informations les plus récentes du serveur. Vous pouvez le considérer comme une intégration d'une [API REST](https://aws.amazon.com/what-is/restful-api/) — le contenu du backend est toujours mis à jour.

Comme toutes les autres méthodes de rendu sur le web, le SSR a sa part de inconvénients. Pour commencer, le fait de devoir faire des requêtes réseau au serveur pour charger une page web pourrait affecter les utilisateurs disposant d'une bande passante internet limitée. Le SSR nécessite également un volume relativement plus élevé de puissance de calcul pour être actif.

## Qu'est-ce que la génération de site statique (SSG) ?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/ssg.jpg)

La génération de site statique est une approche très courante du rendu sur le web. Cela est dû au fait que la plupart des sites web, sinon tous avant les frameworks JavaScript, étaient générés statiquement.

Les sites statiques sont encore très populaires, mais il existe de meilleures façons de les générer. Cela montre à quel point ils sont importants en termes de performance sur le web.

### Mais, qu'est-ce qu'un site statique ?

Un site statique est rendu sur un navigateur exactement comme il a été généré. Le contenu d'un site statique est généralement non affecté par l'utilisateur qui le consulte, contrairement à une application web rendue en CSR ou SSR, où chaque utilisateur peut voir du contenu basé sur l'authentification ou l'autorisation.

Les sites statiques sont idéaux pour afficher du contenu qui ne change jamais ou qui est mis à jour de temps en temps.

### Génération de site statique expliquée

La génération de site statique implique largement l'automatisation du processus de construction de pages web. Les frameworks JavaScript d'aujourd'hui (comme Nuxt.js, Next.js, et ainsi de suite), fournissent des moteurs de template pour construire plusieurs pages web statiques avec un seul template. Comme vous pouvez l'imaginer, cela fait gagner du temps.

La génération de site statique est différente du SSR et du CSR dans le sens où vos pages web HTML sont rendues et générées pendant le build-time — avant que l'utilisateur n'essaie d'accéder à votre page web. C'est pourquoi le SSG est communément appelé pré-rendu. Il fait le travail difficile à l'avance.

Bien que le SSG semble tout bonheur, il y a des compromis. Un inconvénient majeur du rendu avec SSG est qu'une page doit être générée pour chaque URL accessible sur votre site web. Cela pourrait devenir encore plus fastidieux lorsque vous avez des [pages dynamiques](https://nuxtjs.org/docs/directory-structure/pages#dynamic-pages).

Rappelez-vous que les sites statiques sont idéaux pour afficher du contenu qui est rarement mis à jour, donc cette méthode de rendu ne fonctionne pas pour tous les cas d'utilisation.

## Avantages et compromis des différentes méthodes de rendu

Maintenant que vous comprenez comment toutes ces méthodes de rendu génèrent des pages pour le navigateur, nous devrions consolider toutes ces informations et faire quelques comparaisons.

Nous examinerons les trois principaux critères — Performance, SEO et Coût.

### Performance

Pour construire des sites web accessibles indépendamment de la vitesse d'Internet ou de l'ordinateur de l'utilisateur, nous devons considérer la performance. La performance dans ce contexte pourrait être la rapidité avec laquelle un site web se charge ou récupère des données depuis une API.

Les paragraphes suivants montrent comment le CSR, le SSR et le SSG se traduisent en termes de performance.

#### Performance du rendu côté client

Un site web rendu côté client peut être relativement lent à charger. Cela est dû au fait que le code JS est d'abord téléchargé et utilisé pour générer le contenu réel que les utilisateurs voient.

Souvent, les téléchargements de JS sont lourds, surtout avec les frameworks JS. Les pages web rendues côté client peuvent également avoir besoin de faire des appels API pour récupérer des données depuis le backend. Cela augmente le temps de chargement pour l'utilisateur.

#### Performance du rendu côté serveur

Les pages web rendues avec SSR peuvent être très rapides. Cela dépend principalement de la vitesse du serveur et de la vitesse de l'utilisateur. Si les deux conditions sont remplies, le SSR pourrait facilement remporter la victoire en termes de performance.

#### Performance du rendu de site statique

Les pages web générées avec SSG sont relativement rapides car le rendu réel ne se fait pas sur le navigateur.

Le SSG alimente le navigateur avec le contenu dont il a besoin sans travail supplémentaire. Les pages web rendues avec SSG, comme le CSR, peuvent également avoir besoin de faire des appels API pour récupérer des données depuis le backend. Cela augmente également le temps de chargement pour l'utilisateur.

En fin de compte, la quantité de JavaScript utilisée dans une page web peut déterminer sa performance.

### Optimisation pour les moteurs de recherche (SEO)

Tout site web qui a besoin de visibilité devrait valoriser l'optimisation pour les moteurs de recherche. Le SEO détermine à quel point votre contenu est accessible sur les moteurs de recherche comme Google. Il détermine également à quel point vous êtes bien classé dans les pages de résultats des moteurs de recherche (SERPs).

Voyons comment les trois méthodes de rendu se comportent lorsqu'elles sont indexées par les moteurs de recherche.

#### Optimisation pour les moteurs de recherche du CSR

Les pages web rendues avec CSR n'ont généralement aucun contenu significatif et dépendent de JS pour générer du contenu. L'inconvénient est que tous les robots d'indexation ne supportent pas JS, donc votre site web pourrait ne pas être correctement indexé par les moteurs de recherche.

#### Optimisation pour les moteurs de recherche du SSR

Le SSR rend des pages web complètes avec du contenu mis à jour depuis le serveur. Les pages web rendues avec SSR peuvent être explorées et indexées par les moteurs de recherche.

#### Optimisation pour les moteurs de recherche du SSG

Un robot d'indexation explore très facilement les pages web générées avec SSG. Elles ne dépendent pas de JS pour être entièrement rendues.

### Coût

Il est important que les utilisateurs aient la meilleure expérience lorsqu'ils visitent un site web, mais les factures ne se paient pas toutes seules, donc le coût cumulé de cette expérience doit être aussi faible que possible.

Les trois méthodes de rendu n'ont pas les mêmes implications financières. Les paragraphes ci-dessous examinent de plus près le coût de l'utilisation de chacune.

#### Coût du CSR

Le rendu côté client fonctionne à 100 % sur le navigateur. Cela signifie qu'aucun coût supplémentaire n'est engagé.

#### Coût du SSR

Le rendu côté serveur génère une page web entièrement fonctionnelle à distance sur le serveur. Cela signifie des ressources informatiques supplémentaires et des coûts supplémentaires.

#### Coût du SSG

Aucun coût. La génération de site web statique se fait pendant le build-time. Par conséquent, les pages web générées sont hébergées et aucun rendu supplémentaire n'est effectué sur le serveur.

## Conclusion

Lors de la sélection d'une méthode de rendu, considérez votre cas d'utilisation et ce qui fonctionne le mieux pour lui en fonction de ce que vous avez appris dans cet article. Différentes méthodes de rendu conviennent à différents types de sites web.

Un développeur de site web de commerce électronique pourrait choisir de suivre la voie du SSR ou se sentir plus en sécurité en utilisant des sites statiques. Un développeur d'applications web, en revanche, pourrait ne pas se soucier d'un chargement initial long tant que cela signifie une meilleure expérience pour l'utilisateur à long terme.

Quelle que soit la méthode de rendu que vous sélectionnez, assurez-vous que votre site web est aussi accessible que possible — au-delà des conditions que vous ne rencontreriez pas nécessairement. Enfin, n'oubliez jamais de rester dans une alimentation saine en JS.

J'espère que vous avez trouvé cet article utile. Si c'est le cas, n'hésitez pas à me contacter sur LinkedIn et à consulter [favourfelix.com](http://favourfelix.com/) pour voir ce que j'écris et ce que je fais d'autre.
---
title: 'Une introduction à HTTP : les serveurs du système de noms de domaine'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T15:59:23.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-http-domain-name-system-servers-b3e7060eca98
coverImage: https://cdn-media-1.freecodecamp.org/images/0*yC9oY647Pggg817o.png
tags:
- name: dns
  slug: dns
- name: https
  slug: https
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une introduction à HTTP : les serveurs du système de noms de domaine'
seo_desc: 'By Cher Don

  How does the DNS work, and why is it important?

  Overview

  Throughout this series, we will be tackling the basics such as:


  How does DNS work? [You are here!]

  Network Stack, OSI Model

  HTTP Methods and Formats

  Client Identification

  Basic/Dig...'
---

Par Cher Don

#### Comment fonctionne le DNS et pourquoi est-il important ?

### Aperçu

Tout au long de cette série, nous aborderons les bases telles que :

* Comment fonctionne le DNS ? _[Vous êtes ici !]_
* [Pile réseau, modèle OSI](https://medium.freecodecamp.org/an-introduction-to-http-understanding-the-open-systems-interconnection-model-9dd06233d30e)
* Méthodes et formats HTTP
* Identification du client
* Authentification Basic/Digest
* HTTPS fonctionnant avec SSL/TLS

### Qu'est-ce que HTTP ?

Le protocole HyperText Transfer Protocol (HTTP) est un protocole conçu par Sir Tim Berners Lee en 1989. Il constitue la base de la communication des pages web du serveur web vers le navigateur du client.

![Image](https://cdn-media-1.freecodecamp.org/images/oZPkrtifS2pYPY3NqewKvK7HZYvonNKI6gMm)
_Sir Tim Berners Lee, le Père du World Wide Web. Photo gracieuseté de [CNET](https://www.cnet.com/pictures/images-berners-lee-and-the-dawn-of-the-web/" rel="noopener" target="_blank" title=")_

### Serveurs DNS

La connexion à la page web est-elle établie immédiatement après avoir tapé le nom de domaine, comme `medium.com` ? **Absolument pas !**

Les machines, contrairement à nous, reconnaissent l'emplacement des pages web par des _adresses IP_. Ces chaînes de nombres, comme `104.16.121.127`, sont plus adaptées aux machines, surtout puisque il y a des _millions_ de noms de domaine sur le Web.

![Image](https://cdn-media-1.freecodecamp.org/images/83RTQUPnQ-3eLATrOj9ZMlzGyvkVKeM1arxS)

Le système de noms de domaine (DNS) joue un rôle crucial dans le processus de requête HTTP, car il nous permet d'appeler une page web en tapant un simple nom de domaine, `www.medium.com` au lieu de `104.16.121.127` chaque fois que vous voulez accéder au site.

Sans DNS, votre cerveau serait rempli de nombres juste en essayant de mémoriser les adresses IP pour chaque site web que vous utilisez !

![Image](https://cdn-media-1.freecodecamp.org/images/B1llNAZ2wATRPi2bFeF3yc-xWm2trS2f5ltK)
_Flux de résolution DNS, maintenu par un système de base de données distribuée_

Maintenant que nous savons qu'une adresse IP est demandée chaque fois que nous tapons le nom de domaine, découvrons où cette requête recherche l'adresse IP correcte.

#### Cache local

Un cache est un bloc de mémoire pour le stockage temporaire de données qui ont une forte probabilité d'être utilisées à nouveau. La première chose qui se produit est que le résolveur DNS (résidant dans votre ordinateur) vérifie le cache du navigateur, suivi du cache DNS de l'ordinateur. Si vous avez accédé au site web récemment, il aurait l'adresse IP mise en cache dans le système.

Dans ce cas, le navigateur peut immédiatement appeler l'adresse IP pour récupérer la page web !

Une chose à noter ici est que chaque cache a une date d'expiration, appelée le paramètre _"Time to Live"_. Ce paramètre détermine combien de temps le cache peut être stocké lorsque le site web est accédé. Nous aborderons comment cela fonctionne plus tard.

#### Résolveur DNS

Si l'adresse IP ne peut pas être trouvée dans le cache local, elle sera alors demandée au résolveur DNS. Le résolveur DNS est souvent le serveur DNS de votre fournisseur d'accès à Internet (FAI).

Ces serveurs DNS internes ont des caches des sites web que leurs clients ont visités récemment. Encore une fois, si l'adresse IP ne peut pas être trouvée ici, elle sera transmise au serveur de domaine suivant.

#### Serveur de domaine de niveau racine

Le serveur de domaine de niveau racine (RLDS), ou parfois appelé le serveur de noms ".", est simplement un _gardien_ pour les requêtes. Il lit la requête et localise le serveur de domaine approprié pour la redirection.

![Image](https://cdn-media-1.freecodecamp.org/images/UQ2ptMrZwvPMUV57NPN6UfGAR39ijFEP9kaN)

Ainsi, il joue un rôle important dans la redirection vers la couche suivante des serveurs de domaine. Ils sont dispersés dans le monde entier pour prévenir les attaques malveillantes qui pourraient faire tomber le World Wide Web en ciblant le RLDS.

#### Serveur de domaine de niveau supérieur

Le serveur de domaine de niveau supérieur (TLDS) est le serveur de noms pour les domaines qui se terminent par leurs suffixes de domaine spécifiques tels que `.com`, `.org` ou `.io`. Après avoir été transmis par le RLDS, cette couche fonctionne de la même manière que le deuxième gardien. Il prend les requêtes et parcourt son serveur DNS pour rediriger la requête vers la dernière et ultime étape, le serveur de domaine de second niveau.

Le nombre de noms de domaine augmente de manière exponentielle. Il est impossible pour le RLDS de pouvoir stocker ou rediriger une telle quantité d'adresses IP. Ainsi, il est redirigé vers le TLDS pour diversifier la puissance de traitement et la mémoire requise.

#### Serveur de domaine de second niveau

Cette couche est l'endroit où toutes les informations sur le domaine sont stockées et accessibles. Ce serveur DNS est généralement propriété de l'institution responsable de l'hébergement de votre site web.

Ainsi, une requête pour l'enregistrement du domaine est envoyée à ce serveur DNS. Il retourne l'adresse IP, ainsi que d'autres informations importantes telles que le serveur sur lequel il se trouve et l'alias qu'il possède.

#### Succès !

Le navigateur reçoit maintenant l'adresse IP. Il l'utilise pour établir une connexion avec le serveur hôte en utilisant TCP/IP et récupérer la page web via HTTP. Nous discuterons de cela dans [Partie 2](https://medium.freecodecamp.org/an-introduction-to-http-understanding-the-open-systems-interconnection-model-9dd06233d30e).

### Paramètre "Time to Live"

![Image](https://cdn-media-1.freecodecamp.org/images/lNvth7uNEKVE805YmoqD9TQnylJGQ6CIm5eX)

Les enregistrements DNS ont un paramètre Time to Live (TTL). Cela détermine la durée pendant laquelle l'un des serveurs de domaine peut mettre en cache l'enregistrement.

La mise en cache est importante. Elle réduit le temps de chargement de la page, car les informations DNS devront être réacquises chaque fois que le nom de domaine est demandé. Ainsi, un TTL élevé permettrait aux enregistrements DNS de rester actifs pendant une période plus longue. Cela permet aux pages web de se charger plus rapidement.

**Pourquoi tous les enregistrements DNS n'ont-ils pas un TTL élevé alors ?**

En ayant un TTL élevé, cela signifierait que les visiteurs ne verraient pas les changements apportés au DNS immédiatement. Les visiteurs ne voient le changement qu'après l'expiration de l'enregistrement DNS.

Par exemple, si nous devions changer l'hôte de cette page web et avoir un TTL élevé, les changements n'apparaîtraient pas immédiatement dans le navigateur des visiteurs. Cela pourrait entraîner des liens brisés et des utilisateurs ne pouvant pas accéder à la page web.

### Relation Nom d'hôte - Adresse IP

Donc, un seul nom de domaine est attaché à une adresse IP ?

La réponse est oui... et non. Cela peut être, mais ce n'est pas nécessairement une relation un à un.

#### Un seul nom d'hôte, plusieurs adresses IP

![Image](https://cdn-media-1.freecodecamp.org/images/co7rvdbLXLjlFLhZuwVOuNHTa2fcLFoAU7X2)

Un seul nom d'hôte comme `www.google.com` peut correspondre à plusieurs adresses IP, pour équilibrer la charge sur le serveur, car il y a un nombre significatif d'utilisateurs appelant la même page web à un moment donné.

Les serveurs DNS utilisent une méthode "Round Robin", de sorte que toutes les adresses IP sont utilisées de manière égale.

#### Plusieurs noms d'hôte, une seule adresse IP

Le but de cela peut être pour les liens de référence. Par exemple, la recherche de `amazon.com/products/pc` affichera l'écran des produits pour les PC. Bien que `amazon.com/products/pc?user=cherdon` affichera également la même page web, tout achat indiquera à Amazon que j'étais le référent, me permettant de gagner une commission.

Les entreprises achètent souvent plusieurs domaines qui lient à la même page web. Par exemple, `google.com` et `google.net` vous mèneront à la même page web du moteur de recherche.

### Conclusion

Le serveur DNS est très important car il stocke une base de données pour les adresses IP adaptées aux machines sous des noms de domaine conviviaux pour les utilisateurs. Maintenant que nous avons appris comment les serveurs DNS fonctionnent ensemble dans une base de données distribuée, explorons comment la connexion avec le serveur hôte est établie avec l'adresse IP dans [Partie 2](https://medium.freecodecamp.org/an-introduction-to-http-understanding-the-open-systems-interconnection-model-9dd06233d30e) !

Salut ! Je suis [Cher Don](https://www.freecodecamp.org/news/an-introduction-to-http-domain-name-system-servers-b3e7060eca98/undefined), actuellement en train de poursuivre un diplôme en science des données. Je suis le CTO de [Paralegal Bot](https://www.linkedin.com/company/paralegal-bot/), et vous pouvez trouver mon site web ci-dessous. Merci pour la lecture !

[**Piqued ;**](https://www.piqued.co)  
[_Contenu de qualité Nous offrons le meilleur contenu pour les concepts difficiles à saisir. Nous avons été là et ressenti la même chose que vous... www.piqued.co](https://www.piqued.co)
---
title: Qu'est-ce que le Middleware ? Définition et exemples d'utilisation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T17:10:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-middleware-with-example-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/edgar-chaparro-DPo30-zDO5g-unsplash.jpg
tags:
- name: Application Security
  slug: application-security
- name: Middleware
  slug: middleware
seo_title: Qu'est-ce que le Middleware ? Définition et exemples d'utilisation
seo_desc: 'By Yiğit Kemal Erinç

  Middleware is a commonly used term in web development. It can mean many things depending
  on the context, which makes the term a bit confusing.

  In this article, we will start by defining the term and then continue with a discussio...'
---

Par Yiğit Kemal Erinç

Le middleware est un terme couramment utilisé dans le développement web. Il peut signifier beaucoup de choses selon le contexte, ce qui rend le terme un peu confus.

Dans cet article, nous commencerons par définir le terme, puis nous continuerons avec une discussion sur différents cas d'utilisation.

Après avoir lu cet article, vous serez en mesure de participer davantage aux conversations techniques et architecturales avec vos pairs. Vous serez également plus capable de concevoir des API et des flux de données sécurisés et fiables.

## Définition du Middleware

Le middleware est un logiciel qui agit comme un intermédiaire entre deux applications ou services pour faciliter leur communication.

Vous pouvez le considérer comme un proxy qui peut agir comme un accumulateur de données, un traducteur ou simplement un proxy qui transmet les requêtes.

## Cas d'utilisation courants pour le Middleware

### 1) Traducteur

Il existe de nombreux formats d'échange de données, tels que JSON, XML et Protobuf. Même si nous utilisons principalement JSON de nos jours, chacun d'eux a ses propres cas d'utilisation.

Par exemple, les Protobuffers sont connus pour être plus performants que JSON, mais ils ne sont pas lisibles par l'homme. Vous pourriez donc utiliser des Protobuffers pour les services internes et utiliser JSON lorsque le consommateur de l'API est un navigateur.

Vous pouvez également consulter mon [article](https://erinc.io/2020/08/09/what-is-protobuf-and-when-to-use-it/) sur les Protobuffers si vous êtes intéressé à en apprendre davantage à leur sujet.

Maintenant, disons que nous avons besoin que ces deux services, qui parlent différents protocoles, communiquent entre eux.

Nous pouvons créer un middleware qui utilise une bibliothèque de conversion de données et traduit les requêtes dans un format que le service récepteur peut comprendre.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/0.png)

### 2) Accumulation-Duplication de données

L'architecture microservice est un modèle architectural populaire qui est couramment appliqué dans les applications modernes.

Si vous n'êtes pas familier avec l'architecture microservice, cela signifie essentiellement que votre application se compose de nombreuses petites applications ou services qui sont indépendants les uns des autres et fonctionnent ensemble en communiquant via Internet.

Par exemple, dans un projet de commerce électronique, vous pouvez avoir un microservice pour stocker et récupérer des produits, un autre microservice pour la recherche, et un autre pour l'authentification et le stockage des utilisateurs. Et chacun a sa propre base de données.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-10.png)

Maintenant, disons que nous voulons implémenter notre recherche de manière à ce qu'elle recherche à la fois des utilisateurs et des produits.

Si cela était une application monolithique, nous pourrions simplement écrire une requête pour rechercher dans chaque table et joindre les résultats. Mais maintenant, nos bases de données fonctionnent sur différents serveurs.

Ce problème a plusieurs solutions, et nous en examinerons deux.

#### Accumulation de données

Nous pouvons utiliser un middleware pour envoyer des requêtes aux deux serveurs, et leur demander de rechercher dans leurs bases de données des noms d'utilisateurs et des produits qui correspondent au mot recherché.

Ensuite, nous pouvons accumuler les résultats des deux serveurs et les retourner au client. Notez que le nombre de requêtes augmente linéairement à mesure que nous augmentons le nombre de serveurs (et nous devons également fusionner ces données).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/4-3.png)

#### Duplication de données

Nous pouvons stocker des données dupliquées dans notre serveur de recherche afin qu'il puisse les rechercher directement au lieu de les demander aux serveurs de produits et d'utilisateurs. Cela est moins efficace en termes de mémoire mais beaucoup plus rapide – et la vitesse est cruciale pour les services de recherche.

Si les tables dont nous avons besoin sont Product et User, nous pouvons créer ces tables dans notre serveur de recherche également. Ensuite, chaque fois que nous enregistrons un nouvel utilisateur dans notre base de données d'utilisateurs, nous enregistrerons également une copie dans le serveur de recherche.

Nous avons quelques options : premièrement, nous pouvons appeler les méthodes de sauvegarde du serveur de recherche à partir des méthodes de sauvegarde des serveurs User et Product pour dupliquer les données. Ou nous pouvons créer un middleware pour la sauvegarde, qui fera ce qui suit :

* Chaque fois qu'une requête de sauvegarde arrive, appeler la sauvegarde du serveur Product/User et la sauvegarde du serveur de recherche.
* Si la première sauvegarde échoue, ne pas appeler la sauvegarde sur l'autre (cela maintient les bases de données cohérentes).

Regardons les diagrammes de conception sans et avec un middleware. D'abord, voici à quoi cela ressemble sans :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2-7.png)

Cela semble compliqué, n'est-ce pas ? En effet, c'est compliqué et cela rendra votre code plus compliqué et étroitement couplé.

Voici la même solution avec un middleware :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-6.png)

Dans ce scénario, le côté client appelle simplement le middleware pour sauvegarder un produit ou un utilisateur et il gère le reste.

Il n'y a pas de code lié à la duplication des données soit dans les serveurs Product ou User, soit côté client. Le middleware s'occupe de cela.

### 3) Sécurité de l'API

Pour tout code côté client front-end, nous pouvons voir les requêtes sortantes, soit dans la console du navigateur, soit via un proxy.

Nous avons parlé d'un serveur User qui gère la connexion et l'inscription. Si notre code front-end envoie directement les requêtes à ce serveur, l'adresse de notre serveur d'authentification est exposée. Après avoir appris l'adresse IP de notre backend, les attaquants peuvent utiliser des outils pour trouver nos endpoints et scanner notre serveur pour des vulnérabilités.

Nous pouvons utiliser un middleware comme proxy pour dissimuler l'URL de notre serveur d'authentification. Notre front-end communique avec le middleware et il transmettra la requête au serveur d'authentification, puis retournera la réponse.

Cette approche nous permet également de bloquer toutes les requêtes vers notre serveur d'authentification, à l'exception des requêtes provenant de l'URL de notre middleware. Cela rend notre serveur d'authentification beaucoup plus sécurisé.

Cela n'était pas possible auparavant, car notre front-end communiquait avec le serveur d'authentification. Puisque le front-end signifie l'ordinateur du client, nous ne pouvions pas appliquer de filtre IP.

### 4) Exposition des API publiques

Dans la partie précédente, nous avons appris que les middlewares peuvent être utilisés pour restreindre l'accès à notre API.

Maintenant, regardons l'autre côté de l'équation : que faire si nous voulons donner un accès restreint à notre API ? Peut-être sommes-nous un ingénieur logiciel dans une banque et la banque prévoit un hackathon. Nous devrions fournir un accès à notre API, n'est-ce pas ?

Mais puisque nous sommes une banque, bien sûr, nous ne pouvons pas fournir un accès à l'ensemble de l'API et permettre toutes les opérations. Cela signifie que nous devons trouver un moyen de fournir un accès restreint.

À cette fin, nous pouvons implémenter un middleware qui n'expose que certains des endpoints et redirige les requêtes vers notre API réelle. Ensuite, nous fournissons cette API aux développeurs du hackathon.

## Conclusion

Dans cet article, nous avons commencé par définir ce qu'est le middleware et nous avons essayé de catégoriser les cas d'utilisation des middlewares dans le développement web.

Gardez à l'esprit que ce n'est pas une liste complète des cas d'utilisation, mais j'espère qu'elle vous a été utile.

Merci d'avoir lu. Si vous avez aimé l'article, je vous invite à consulter mon [blog](https://erinc.io/). Vous pouvez également vous abonner à ma liste de diffusion pour être informé lorsque je publie un nouvel article :)
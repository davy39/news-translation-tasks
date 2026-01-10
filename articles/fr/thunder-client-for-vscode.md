---
title: Thunder Client – Une alternative pour tester les APIs Restful
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2022-04-04T19:09:46.000Z'
originalURL: https://freecodecamp.org/news/thunder-client-for-vscode
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-greg-2418664.jpg
tags:
- name: REST API
  slug: rest-api
- name: Testing
  slug: testing
- name: Visual Studio Code
  slug: vscode
seo_title: Thunder Client – Une alternative pour tester les APIs Restful
seo_desc: "This article will teach you an alternative approach to testing client APIs\
  \ using Thunder Client, an open-source extension available on VS Code marketplace.\
  \ \nYou will not need to download any tools to do this, since you can get it done\
  \ right within VS..."
---

Cet article vous apprendra une approche alternative pour tester les APIs client en utilisant Thunder Client, une extension open-source disponible sur le [marketplace de VS Code](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client).

Vous n'aurez pas besoin de télécharger d'outils supplémentaires, car tout peut être fait directement dans VS Code.

L'article couvre les points suivants :

1. Introduction à l'IDE VS Code et au marketplace
2. Pourquoi utiliser Thunder Client ?
3. Avantages de Thunder Client
4. Fonctionnement de Thunder Client
5. Comment télécharger et installer Thunder Client
6. Comment lancer Thunder Client
7. Collections et variables d'environnement
8. Comment faire une requête client
9. Aperçu d'une requête et d'une réponse d'exemple

## Introduction à l'IDE VS Code et au Marketplace

VS Code est bien plus qu'un simple éditeur de code ou un IDE pour de nombreux développeurs. Il ne se contente pas de vous permettre d'écrire du code dans votre ou vos langages préférés – il vous permet également d'accélérer l'ensemble du processus de développement.

VS Code propose un marketplace d'extensions qui vous permet de rechercher et de télécharger facilement vos extensions préférées parmi de nombreuses options open-source.

## Pourquoi Thunder Client ?

Thunder Client est une alternative à l'outil Postman, célèbre pour tester les APIs client. L'extension Thunder Client pour VS Code est légère et vous permet de tester des APIs directement dans l'éditeur.

Vous ne souhaitez peut-être pas télécharger un autre outil pour tester les APIs que vous développez. Pourquoi ne pas télécharger une extension dans VS Code qui offre une large gamme de fonctionnalités comme :

* collections,
* variables d'environnement,
* support des verbes HTTP standard,
* onglets de navigation (Query, Headers, Auth, Body, Test), et
* Support des réponses JSON

### Thunder Client vs Postman

Thunder Client est léger et convient aux utilisateurs qui veulent une interface utilisateur simple et une expérience utilisateur fantastique sans complexité. Il fonctionne également parfaitement hors ligne et fournit une documentation avec support Markdown 💡.

Gardez à l'esprit que Postman est plus robuste et dispose d'une gamme de fonctionnalités plus large, conçue selon les normes de l'industrie. Il permet à une communauté de développeurs d'explorer le plus grand réseau d'APIs, d'espaces de travail et de collections dans le monde. Il dispose également de fonctionnalités comme la création d'équipes, la génération de rapports, les moniteurs (vérification périodique des performances et des réponses des APIs) et les serveurs mock (utilise des serveurs mock qui aident à simuler des endpoints et leurs réponses correspondantes sans backend).

Il est facile de créer des APIs car il offre un support pour le versioning, les types de schémas (OpenAPI 3.0-1.0, RAML, GraphQL) et le format de schéma (JSON, YAML).

Comme tout bon outil, Postman dispose d'un centre d'apprentissage à jour où vous pouvez trouver de la documentation pour commencer avec l'outil. Cela semble intéressant aussi, n'est-ce pas ? Eh bien oui 😁, les deux sont uniques et parfaits pour leurs cas d'utilisation.

## Avantages de Thunder Client

Tout d'abord, c'est une extension de client API ultra-rapide. Elle crée des requêtes pour récupérer des réponses rapidement et sans effort. Elle ne nécessite pas non plus d'accès à Internet lors du test d'APIs sur votre machine locale.

Elle dispose également d'une interface utilisateur intuitive et facile à utiliser. L'interface est conviviale et beaucoup plus facile à utiliser car il y a relativement peu de fonctionnalités sur l'extension par rapport à un outil comme Postman.

Thunder Client offre une gestion extensive des requêtes API. Il est efficace pour traiter de grandes requêtes en même temps et ne ralentit pas l'application VS Code.

Il supporte également les thèmes de Visual Studio Code et adopte le thème actuellement configuré dans VS Code.

Enfin, Thunder Client supporte les collections, les variables d'environnement, GraphQL et les scripts de test. Il dispose également de fonctionnalités populaires que des outils robustes comme Postman possèdent.

En général, Thunder Client constitue une excellente alternative pour une petite équipe qui n'a besoin d'accéder qu'à des fonctionnalités de base comme les collections, les variables d'environnement et les tests.

## Fonctionnement de Thunder Client

Si vous souhaitez utiliser Thunder Client, vous devrez vous rendre sur le marketplace de VS Code pour télécharger l'extension, puis la lancer. Une fois que vous avez fait cela, voici quelques choses de base que vous pouvez faire avec l'extension :

**Suivi de l'activité :** Thunder Client garde une trace des requêtes API récentes qu'un utilisateur a faites dans le passé. Vous pouvez également filtrer l'activité pour la réduire à une recherche d'activité préférée. Cela s'appelle également Historique.

**Utilisation des collections :** Vous pouvez organiser les APIs pour qu'il soit plus facile d'y accéder. Les collections sont un groupe d'APIs, vous pouvez donc créer une collection Utilisateur pour inclure des APIs comme créer un utilisateur, modifier un utilisateur, supprimer un utilisateur, et ainsi de suite.

**Variables d'environnement :** Avec les Envs, vous pouvez stocker des informations d'identification comme des tokens, des URLs de base, et des clés publiques et privées, puis utiliser les variables dans le corps de la requête.

**Faire des requêtes :** Vous pouvez spécifier votre verbe HTTP préféré pour accompagner la requête, comme POST, puis l'endpoint. Avec la requête Thunder Client, il y a également un support pour les paramètres de requête, les en-têtes HTTP (bruts ou non), l'authentification (aucune, basique, Bearer, OAuth 2, AWS et authentification NTLM), le corps (charge utile attachée à une requête individuelle) et le test (vous sélectionnez le type de test qui peut être un code de réponse et définissez une valeur à assert).

**Réponses :** Thunder Client offre une section de réponse bien conçue avec le corps de la réponse, le statut de la réponse, la taille et le temps qu'il a fallu pour la requête. Il permet également aux utilisateurs d'ajouter une documentation supportée par Markdown, ce qui la rend encore plus agréable.

## Comment télécharger et installer Thunder Client

Pour télécharger Thunder Client, vous pouvez le trouver sur le marketplace de VS Code. Il suffit de rechercher "Thunder Client" lorsque vous y êtes invité, puis de l'installer.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-20-at-17.19.32.png)
_Rechercher Thunder Client sur le Marketplace_

**NOTE** : Je l'ai déjà installé, donc l'option de désinstallation s'affiche dans l'image.

Installez l'extension Thunder Client en cliquant sur le bouton d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-20-at-17.20.56-1.png)
_Installer Thunder Client_

## Comment lancer Thunder Client

Cliquez sur la nouvelle icône qui a été ajoutée dans VS Code pour lancer Thunder Client.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-20-at-19.09.50.png)
_Lancer Thunder Client_

Ensuite, vous pouvez commencer à utiliser Thunder Client.

## Comment utiliser l'onglet Activité

L'onglet Activité montre l'historique de vos requêtes API récentes. Vous êtes également libre d'effectuer des opérations telles que l'enregistrement dans une collection, le renommage, la duplication, et plus encore comme montré dans l'image.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-03-at-02.31.28.png)

## Comment utiliser les collections et les variables d'environnement

Les collections sont un groupe de requêtes API. Thunder Client vous permet de travailler avec des collections ou de créer une seule requête individuelle comme le bouton "Nouvelle requête".

Pour travailler avec des collections, cliquez sur l'onglet "Collections", puis cliquez sur l'icône indiquée par la flèche dans l'image ci-dessous. Cela affiche un menu déroulant où vous sélectionnez si vous voulez une "Nouvelle collection" ou si vous avez une collection existante à importer.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-20-at-19.06.19.png)
_Créer et importer une collection_

Vous pouvez ajouter des variables d'environnement en cliquant sur l'onglet "Env", puis en cliquant sur l'icône indiquée par la flèche dans l'image ci-dessous. Cela affiche un menu déroulant pour configurer les variables d'environnement pour les requêtes. Vous pouvez également importer des variables existantes.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-20-at-19.06.46.png)

## Comment faire une requête client

Selon le type de requête, Thunder Client offre une liste de verbes HTTP pour les requêtes tels que **GET, POST, PUT, DELETE** et **PATCH**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-20-at-19.36.24.png)
_Verbes HTTP dans Thunder Client_

Il y a également un support pour les paramètres de requête, les en-têtes, l'autorisation, le corps et les tests. Au moment de la rédaction, il n'y a pas encore de support pour les pièces jointes de fichiers pour les requêtes. Vous pouvez consulter les notes de version à venir [ici](https://github.com/rangav/thunder-client-support/issues/282).

**Paramètres de requête** vous permettent d'ajouter des paramètres de requête à la requête.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-03-at-02.34.19.png)
_Paramètres de requête_

**En-têtes** vous permettent de définir des en-têtes HTTP comme l'autorisation, le type de contenu, l'origine, l'agent utilisateur, la langue acceptée, le référent, etc.

Si vous souhaitez que certains en-têtes soient optionnels, assurez-vous simplement de les laisser non cochés pour la requête. Il y a également une suggestion d'autocomplétion activée pour votre type d'en-tête préféré.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-03-at-02.41.55.png)
_En-têtes HTTP_

Pour accéder aux ressources, vous devez avoir des tokens qui les authentifient. Avec Thunder Client, l'onglet Auth vous permet de sélectionner votre type d'authentification préféré et d'ajouter des informations d'identification.

Dans mon cas, je choisis Bearer ; puis, j'ai un token collé dans la zone de texte et un préfixe de token généré automatiquement pour la requête.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-03-at-02.45.46.png)
_Authentification_

Vous pouvez inclure une charge utile lors de la création d'une requête. Pour ajouter la charge utile, sélectionnez l'onglet Body, et vous verrez différents formats de données supportés par l'extension.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-03-at-02.53.24.png)
_Charge utile de la requête_

## Exemple de requête et de réponse

L'image ci-dessous montre une requête exemple avec des paramètres de requête et une réponse JSON exemple.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-20-at-20.20.52.png)
_Requête et réponse exemple_

## Conclusion

Yaaay, ravi de vous avoir accroché jusqu'à la fin. J'espère que vous avez appris à rechercher des extensions sur le marketplace de VS Code et que vous pouvez commencer à faire des requêtes API avec Thunder Client.

Un énorme merci au créateur [@Rangav](https://www.freecodecamp.org/news/p/7b47d7f1-beed-41b6-a792-6cbf0c8abf52/twitter.com/ranga_vadhineni) sur Twitter pour cette superbe extension.

Suivez-moi sur [twitter](https://twitter.com/bigdevlarry) et partagez si vous trouvez cela utile.
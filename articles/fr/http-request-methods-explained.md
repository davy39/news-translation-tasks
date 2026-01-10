---
title: Méthodes de requête HTTP – Get vs Put vs Post expliquées avec des exemples
  de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-26T21:36:54.000Z'
originalURL: https://freecodecamp.org/news/http-request-methods-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/FCC-Cover.png
tags:
- name: api
  slug: api
- name: http
  slug: http
- name: Web Development
  slug: web-development
seo_title: Méthodes de requête HTTP – Get vs Put vs Post expliquées avec des exemples
  de code
seo_desc: "By Camila Ramos Garzon\nIn this article, we'll be discussing the get, put,\
  \ and post HTTP methods. You'll learn what each HTTP method is used for as well\
  \ as why we use them. \nIn order to get a deep understanding of how HTTP methods\
  \ work, I'll also go o..."
---

Par Camila Ramos Garzon

Dans cet article, nous allons discuter des méthodes HTTP get, put et post. Vous apprendrez à quoi sert chaque méthode HTTP ainsi que _pourquoi_ nous les utilisons. 

Afin d'avoir une compréhension approfondie du fonctionnement des méthodes HTTP, je vais également aborder le contexte et les informations de base clés. 

### Sujets que nous allons couvrir dans cet article :

* Protocole HTTP
* Architecture client-serveur
* APIs

À la fin de cet article, vous aurez une bonne compréhension des fonctions de chaque méthode de requête. Vous aurez également de l'expérience dans la réalisation de requêtes et le travail avec une API web.

## Qu'est-ce que HTTP ? 

HTTP est un protocole, ou un ensemble défini de règles, pour accéder aux ressources sur le web. Les ressources peuvent signifier n'importe quoi, des fichiers HTML aux données d'une base de données, des photos, du texte, et ainsi de suite. 

Ces ressources nous sont rendues disponibles via une `API` et nous faisons des requêtes à ces APIs via le protocole HTTP. `API` signifie interface de programmation d'application. C'est le mécanisme qui permet aux développeurs de demander des ressources. 

### Architecture Client-Serveur

Afin de comprendre les méthodes HTTP, il est important de couvrir le concept d'architecture client/serveur. Cette architecture décrit comment toutes les applications web fonctionnent et définit les règles de leur communication. 

Une application cliente est celle avec laquelle un utilisateur interagit réellement, celle qui affiche le contenu. Une application serveur est celle qui envoie le contenu, ou la ressource, à votre application cliente. Une application serveur est un programme qui s'exécute quelque part, écoute et attend une requête. 

La principale raison de cette séparation est de sécuriser les informations sensibles. Votre application cliente entière est téléchargée dans le navigateur, et toutes les données peuvent être accessibles par quiconque accède à votre page web. 

Cette architecture aide à protéger des choses comme vos clés API, vos données personnelles, et plus encore. Maintenant, des outils modernes comme [Next.js](https://nextjs.org/) et [Netlify](https://www.netlify.com/) permettent aux développeurs d'exécuter du code serveur dans la même application que leur application cliente, sans avoir besoin d'une application serveur dédiée.

### Communication Client-Serveur

Les applications client et serveur communiquent en envoyant des messages individuels au besoin, plutôt qu'un flux continu de communication. 

Ces communications sont presque toujours initiées par les clients sous forme de requêtes. Ces requêtes sont satisfaites par l'application serveur qui envoie une réponse contenant la ressource demandée, entre autres.

### Pourquoi avons-nous besoin d'une architecture serveur-client ?

Disons que vous construisez une application web météo, par exemple. L'application météo avec laquelle votre utilisateur va interagir est l'application cliente – elle a des boutons, une barre de recherche et affiche des données comme le nom de la ville, la température actuelle, l'indice de qualité de l'air, etc.

Cette application météo n'aurait pas toutes les villes et leurs informations météo codées directement. Cela rendrait l'application volumineuse et lente, prendrait une éternité à rechercher et à ajouter manuellement à une base de données, et serait un casse-tête à mettre à jour chaque jour. 

Au lieu de cela, l'application peut accéder aux données météo par ville en utilisant l'API web météo. Votre application recueillerait la localisation de votre utilisateur, puis ferait une requête au serveur en disant : « Hé, envoie-moi les informations météo pour cette ville spécifique. »

Selon ce que vous essayez d'accomplir, vous utiliseriez les différentes méthodes de requête disponibles. Le serveur envoie une réponse contenant les informations météo et quelques autres choses, selon la manière dont l'API est écrite. Il peut également envoyer des choses comme un horodatage, la région où se trouve cette ville, et plus encore. 

Votre application cliente a communiqué avec une application serveur qui s'exécute quelque part, dont le seul travail est d'écouter en continu une requête à cette adresse. Lorsqu'elle reçoit une requête, elle travaille pour satisfaire cette requête soit en lisant à partir d'une base de données, d'une autre API, d'un fichier local, ou d'un calcul programmatique basé sur les données que vous passez.

### L'anatomie d'une requête HTTP

Une requête HTTP doit avoir les éléments suivants :

* Une méthode HTTP (comme `GET`)
* Une URL d'hôte (comme `https://api.spotify.com/`)
* Un chemin de point de terminaison (comme `v1/artists/{id}/related-artists`)

Une requête peut également avoir optionnellement :

* Corps
* En-têtes
* Chaînes de requête
* Version HTTP

### L'anatomie d'une réponse HTTP

Une réponse doit avoir les éléments suivants :

* Version du protocole (comme `HTTP/1.1`)
* Code de statut (comme `200`)
* Texte de statut (`OK`)
* En-têtes

Une réponse peut également avoir optionnellement :

* Corps

## Méthodes HTTP expliquées

%[https://twitter.com/ftrain/status/1195350262145306624?s=20]

Maintenant que nous savons ce qu'est HTTP et pourquoi il est utilisé, parlons des différentes méthodes que nous avons à notre disposition. 

Dans l'exemple de l'application météo ci-dessus, nous voulions récupérer des informations météo sur une ville. Mais que faire si nous voulions soumettre des informations météo pour une ville ? 

Dans la vie réelle, vous n'auriez probablement pas les permissions de modifier les données de quelqu'un d'autre, mais imaginons que nous sommes contributeurs à une application météo gérée par la communauté. Et en plus de recevoir les informations météo d'une API, les membres de cette ville pourraient mettre à jour ces informations pour afficher des données plus précises. 

Ou que faire si nous voulions ajouter une nouvelle ville qui, pour une raison quelconque, n'existe pas déjà dans notre base de données de villes ? Ce sont toutes des fonctions différentes – récupérer des données, mettre à jour des données, créer de nouvelles données – et il existe des méthodes HTTP pour toutes ces actions.

### Requête HTTP POST

Nous utilisons `POST` pour créer une nouvelle ressource. Une requête `POST` nécessite un corps dans lequel vous définissez les données de l'entité à créer. 

Une requête POST réussie renverrait un code de réponse 200. Dans notre application météo, nous pourrions utiliser une méthode POST pour ajouter des données météo sur une nouvelle ville.

### Requête HTTP GET

Nous utilisons `GET` pour lire ou récupérer une ressource. Un `GET` réussi renvoie une réponse contenant les informations que vous avez demandées. 

Dans notre application météo, nous pourrions utiliser un GET pour récupérer la météo actuelle pour une ville spécifique.

### Requête HTTP PUT

Nous utilisons `PUT` pour modifier une ressource. `PUT` met à jour l'intégralité de la ressource avec les données transmises dans le corps de la charge utile. Si aucune ressource ne correspond à la requête, elle créera une nouvelle ressource. 

Dans notre application météo, nous pourrions utiliser `PUT` pour mettre à jour toutes les données météo concernant une ville spécifique.

### Requête HTTP PATCH

Nous utilisons `PATCH` pour modifier une partie d'une ressource. Avec `PATCH`, vous n'avez besoin de transmettre que les données que vous souhaitez mettre à jour. 

Dans notre application météo, nous pourrions utiliser `PATCH` pour mettre à jour les précipitations pour un jour spécifié dans une ville spécifiée.

### Requête HTTP DELETE

Nous utilisons `DELETE` pour supprimer une ressource. Dans notre application météo, nous pourrions utiliser `DELETE` pour supprimer une ville que nous ne souhaitons plus suivre pour une raison quelconque.

## FAQ sur les méthodes HTTP

### Quelle est la différence entre PUT et POST ? 

Les requêtes `PUT` sont idempotentes, ce qui signifie que l'exécution de la même requête `PUT` produira toujours le même résultat. 

En revanche, un `POST` produira des résultats différents. Si vous exécutez une requête `POST` plusieurs fois, vous créerez une nouvelle ressource plusieurs fois malgré le fait qu'elles aient les mêmes données transmises. 

En utilisant une analogie de restaurant, `POST`er plusieurs fois créerait plusieurs commandes séparées, alors que plusieurs requêtes `PUT` mettront à jour la même commande existante.

### Quelle est la différence entre PUT et PATCH ?

Les différences clés sont que `PUT` créera une nouvelle ressource s'il ne trouve pas la ressource spécifiée. Et avec `PUT`, vous devez transmettre des données pour mettre à jour l'intégralité de la ressource, même si vous ne souhaitez modifier qu'un seul champ. 

Avec `PATCH`, vous pouvez mettre à jour une partie d'une ressource en transmettant simplement les données du champ à mettre à jour.

### Que faire si je veux simplement mettre à jour une partie de ma ressource ? Puis-je toujours utiliser PUT ?

Si vous souhaitez simplement mettre à jour une partie de votre ressource, vous devez toujours envoyer des données pour l'intégralité de la ressource lorsque vous effectuez une requête `PUT`. L'option la mieux adaptée ici serait `PATCH`.

### Pourquoi un corps est-il optionnel pour une requête et une réponse ?

Un corps est optionnel car pour certaines requêtes, comme les récupérations de ressources utilisant la méthode `GET`, il n'y a rien à spécifier dans le corps de votre requête. Vous demandez toutes les données du point de terminaison spécifié. 

De même, un corps est optionnel pour certaines réponses lorsqu'un code de statut est suffisant ou qu'il n'y a rien à spécifier dans le corps, par exemple avec une opération `DELETE`.

## Exemples de requêtes HTTP

Maintenant que nous avons couvert ce qu'est une requête HTTP et pourquoi nous les utilisons, faisons quelques requêtes ! Nous allons jouer avec l'[API GitHub Gist](https://docs.github.com/en/rest/reference/gists).

> "Gist est un moyen simple de partager des extraits de code et des collages avec d'autres. Tous les Gists sont des dépôts Git, donc ils sont automatiquement versionnés, forkables et utilisables depuis Git." (Source : Github)

Vous aurez besoin d'un compte GitHub pour cela. Si vous n'en avez pas déjà un, c'est une excellente opportunité pour en créer un afin de sauvegarder votre code à l'avenir. 

Chaque utilisateur sur GitHub peut créer des gists, récupérer ses gists, récupérer tous les gists publics, supprimer un gist et mettre à jour un gist, entre autres. Pour garder les choses simples, nous utiliserons [Hoppscotch](https://hoppscotch.io/), une plateforme avec une interface agréable utilisée pour faire rapidement et facilement des requêtes HTTP. 

Un rapide guide de Hoppscotch :

* Il y a un menu déroulant où vous pouvez sélectionner la méthode avec laquelle vous souhaitez créer une requête.
* Il y a une zone de texte où vous devez coller l'URL du point de terminaison de l'API auquel vous souhaitez accéder.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-12.35.33-PM.png)

* Il y a une section En-têtes où nous allons passer des en-têtes comme indiqué par la documentation GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-12.39.38-PM-1.png)

* Il y a une zone de corps où nous allons passer du contenu à notre corps comme indiqué par la documentation GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-12.41.14-PM.png)

* La colonne de droite vous indiquera rapidement si votre requête a réussi. Si elle est verte, vous avez réussi à faire votre requête, et si elle est rouge, il y a eu une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-3.44.56-PM.png)

### Comment faire une requête GET

Pour faire une requête `GET` afin de récupérer tous les gists d'un utilisateur spécifique, nous pouvons utiliser la méthode et le point de terminaison suivants : `GET /users/{username}/gists`. La documentation nous indique les paramètres que nous pouvons passer pour faire cette requête. 

Nous voyons que dans le chemin, nous devons passer une chaîne avec le nom d'utilisateur de l'utilisateur cible. Nous voyons également que nous devons passer un en-tête appelé accept et le définir sur `application/vnd.github.v3+json`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-20-at-2.01.35-PM.png)

Nous avons l'URL pour cette API : 

```shell
https://api.github.com
```

Nous avons le chemin du point de terminaison pour cette opération spécifique : 

```
/users/{username}/gists
```

Pour faire cette requête :

1. Collez l'URL complète + le chemin dans le champ d'entrée de Hoppscotch. Assurez-vous de remplacer `username` par un nom d'utilisateur réel. Si vous n'avez pas de GitHub avec des Gists existants, vous pouvez utiliser le mien : camiinthisthang. 
2. Sélectionnez la méthode de requête `GET`
3. Dans l'onglet En-têtes, définissez accept comme en-tête et définissez la valeur sur `application/vnd.github.v3+json`

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-12.39.38-PM-2.png)

4.  Envoyez !

En bas, vous verrez votre réponse formatée en `JSON`. Pour la lire plus clairement, copiez la réponse et collez-la dans un [formateur JSON en ligne](https://jsonformatter.curiousconcept.com/#). 

Dans le formateur, vous pouvez voir que la réponse est un tableau d'objets. Chaque objet représente un gist, nous montrant des informations comme l'URL, l'ID, etc. 

### Comment faire une requête POST

Maintenant, créons une ressource en utilisant la méthode `POST`. Dans ce contexte, la nouvelle ressource serait un nouveau gist. 

Tout d'abord, nous devrons créer un jeton d'accès personnel. Pour cela, [allez sur votre page de paramètres](https://github.com/settings/tokens) et cliquez sur Générer un jeton.

Nommez votre jeton et sélectionnez la portée « Créer des Gists » :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-20-at-2.59.11-PM.png)

Ensuite, cliquez sur le bouton vert `Générer un jeton` en bas de la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-20-at-3.28.01-PM.png)

Copiez votre code d'accès et collez-le quelque part où vous pourrez facilement le récupérer. 

Maintenant, nous sommes prêts à faire notre requête ! La documentation nous indique que nous devons passer un en-tête et un objet `files` dans le corps. Nous pouvons optionnellement passer quelques autres choses, y compris un booléen qui dicte si ce gist est public ou privé.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-20-at-2.07.23-PM.png)

Nous avons l'URL pour cette API : 

```shell
https://api.github.com
```

Nous avons le chemin du point de terminaison pour cette opération spécifique : 

```
/gists
```

Pour faire cette requête :

1. Collez l'URL complète + le chemin dans le champ d'entrée de Hoppscotch. 
2. Sélectionnez la méthode de requête `POST`
3. Dans l'onglet En-têtes, définissez accept comme en-tête et définissez la valeur sur `application/vnd.github.v3+json`
4. Dans l'onglet Corps, définissez le type de contenu sur `application/json`. Ensuite, commencez par un objet `{}`.   
  
À l'intérieur de cet objet, nous allons définir le booléen `public` sur `true`. Ensuite, nous allons définir la propriété `files`, et la valeur est un autre objet avec une clé du nom de votre nouveau gist. La valeur pour cela devrait être un autre objet dont la clé est `content`. La valeur ici devrait être ce que vous voulez réellement ajouter au gist.   
  
Voici le code à copier/coller :

```javascript
{
  "public": true, 
  "files": {
    "postgist.txt": {
      "content": "Ajout d'un GIST via l'API!!"
    }
  }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-2.35.57-PM.png)

5.  Dans l'onglet Autorisation, définissez le type d'autorisation sur `Basic Auth`. Tapez votre nom d'utilisateur GitHub et passez votre jeton d'accès personnel que nous avons créé dans le champ du mot de passe.

Après avoir exécuté cela, nous obtenons une longue réponse. Un moyen facile de vérifier que votre gist a été créé est d'aller dans vos Gists sur GitHub. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-2.39.27-PM.png)

Nous voyons que nous avons ajouté un Gist avec succès !

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-2.39.58-PM.png)

### Comment faire une requête PATCH

Mettons à jour le titre et la description du Gist que nous venons de créer. Rappelez-vous : `PATCH` vous permet de mettre à jour une partie d'une ressource, et non la ressource entière. Tout ce que nous ne transmettons pas restera inchangé. 

Nous n'avons pas réellement passé de description à notre Gist lorsque nous l'avons créé, donc nous pouvons le patcher et en créer une.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-20-at-3.35.56-PM.png)

Nous avons l'URL pour cette API : 

```shell
https://api.github.com
```

Nous avons le chemin du point de terminaison pour cette opération spécifique : 

```
/gists/{gist_id}
```

Pour faire cette requête :

1. Collez l'URL complète + le chemin dans le champ d'entrée de Hoppscotch. Obtenez l'`ID du Gist` du gist que vous souhaitez mettre à jour. Vous pouvez trouver l'ID en allant dans le Gist sur GitHub et en copiant la chaîne alphanumérique à la fin de l'URL.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-20-at-3.50.13-PM.png)

2.   Sélectionnez la méthode de requête `PATCH`.

3.   Dans l'onglet En-têtes, définissez accept comme en-tête et définissez la valeur sur `application/vnd.github.v3+json`.

4.   Dans l'onglet Autorisation, définissez le type d'autorisation sur `Basic Auth`. Tapez votre nom d'utilisateur GitHub et passez votre jeton d'accès personnel que nous avons créé dans le champ du mot de passe.

5.   Dans l'onglet Corps, nous allons passer la description et le titre mis à jour. Voici le code :

```javascript
{
  "description": "Ajout d'une description via l'API", 
  "files": {
    "postgist.txt": {
      "content": "Ajout d'un GIST via l'API!! -- ajout de cette ligne à la fin pour rendre le contenu légèrement plus long"
    }
  }
}
```

Si nous actualisons notre Gist, nous voyons que nous avons un titre et une description mis à jour ! 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-3.38.35-PM.png)

### Comment faire une requête DELETE

Supprimons le Gist que nous avons créé. Nous devons passer l'en-tête et l'ID du Gist. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-24-at-3.42.30-PM.png)

Nous avons l'URL pour cette API : 

```shell
https://api.github.com
```

Nous avons le chemin du point de terminaison pour cette opération spécifique : 

```
/gists/{gist_id}
```

Pour faire cette requête :

1. Collez l'URL complète + le chemin dans le champ d'entrée de Hoppscotch. Obtenez l'`ID du Gist` du gist que vous souhaitez mettre à jour. Vous pouvez trouver l'ID en allant dans le Gist sur GitHub et en copiant la chaîne alphanumérique à la fin de l'URL.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-20-at-3.50.13-PM.png)

2.   Sélectionnez la méthode de requête `DELETE`

3.   Dans l'onglet En-têtes, définissez accept comme en-tête et définissez la valeur sur `application/vnd.github.v3+json`.

Si nous naviguons vers nos Gists, nous voyons que celui-ci n'existe plus et nous avons supprimé la ressource avec succès. 

### Comment faire des requêtes dans votre application

Nous avons utilisé Hoppscotch car il nous permet de faire rapidement des requêtes sans avoir à démarrer une application complète ou à télécharger quoi que ce soit. 

Si vous souhaitez faire des requêtes dans une application JavaScript/React, vous pourriez utiliser [Javascript fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) ou [Axios](https://axios-http.com/docs/intro). 

Pour un guide pas à pas du code sur la façon de créer une application simple qui utilise des méthodes de requête HTTP et une API, [regardez ma vidéo sur YouTube où nous créons une application web qui affiche des informations sur tous les pays via une API.](https://www.youtube.com/watch?v=7xu7FnKh54M&t=334s)

%[https://www.youtube.com/watch?v=7xu7FnKh54M]

## Vous l'avez fait !

Si vous lisez ceci, allez-y et donnez-vous une tape dans le dos car vous avez appris sur les APIs web, le protocole HTTP, l'architecture client-serveur – et vous avez également fait vos premières requêtes. 

Si vous avez aimé ce style d'enseignement, je crée du contenu spécifiquement pour les débutants et les ingénieurs en début de carrière sur [YouTube](https://www.youtube.com/channel/UCyEnr-lcCUavJzh0uodvG3w), [Tik Tok](https://www.tiktok.com/@camiinthisthang?), [Twitter](https://twitter.com/camiinthisthang), et [Hashnode](https://hashnode.com/@camiinthisthang). Vous pouvez également trouver des extraits de code et un moyen de me contacter via [mon site web personnel](https://camiinthisthang.dev/).
---
title: Comment concevoir une API asynchrone sans serveur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T14:58:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-a-serverless-async-api-6cfd68939459
coverImage: https://cdn-media-1.freecodecamp.org/images/0*nFjU9ji7_pTwjEVC
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment concevoir une API asynchrone sans serveur
seo_desc: 'By Garrett Vargas

  I recently ran a workshop to teach developers how to create an Alexa skill. The
  workshop material centered around a project to return car rental search results.
  Because I wanted to focus the learning on developing the conversational...'
---

Par Garrett Vargas

J'ai récemment animé un atelier pour enseigner aux développeurs comment créer une compétence Alexa. Le matériel de l'atelier était centré sur un projet visant à retourner des résultats de recherche de location de voitures. Comme je voulais me concentrer sur l'apprentissage du développement du flux conversationnel et non sur les mécanismes de la recherche de voitures, j'ai décidé d'encapsuler la logique de recherche derrière une API. De plus, puisque la demande de recherche de voiture peut prendre 10 secondes ou plus pour se compléter, je voulais que l'appel soit asynchrone afin que nous puissions construire une conversation comme :

> « Trouvez une voiture à New York le week-end prochain »  
> « Quelle taille de voiture souhaitez-vous pour votre voyage à New York le week-end prochain ? »  
> « Une petite voiture »  
> « Y a-t-il une entreprise spécifique chez qui vous souhaitez louer ? »  
> « Non »  
> « OK, j'ai trouvé une voiture compacte chez Enterprise pour 100 $... »

La mise en œuvre de l'API asynchrone était un projet assez intéressant en soi, et dans cet article de blog, je vais vous expliquer comment je l'ai fait de manière sans serveur en utilisant API Gateway, des fonctions Lambda et S3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AwXj5L3SHO-IcWob2wcYDA.png)
_Conception pour appeler une recherche sans serveur asynchrone_

#### Bucket S3

Le bucket S3 dans cette architecture sert de cache qui stocke les résultats de recherche à récupérer plus tard. Les appelants de l'API reçoivent un jeton lorsqu'ils démarrent une recherche, et la conception de base est d'utiliser ce jeton comme partie du nom de l'objet S3 pour vous permettre de récupérer le contenu lors d'un appel ultérieur. Pour empêcher le bucket de se remplir de résultats de recherche, vous pouvez définir une politique d'expiration appropriée pour le cycle de vie de vos résultats d'API (c'est-à-dire combien de temps souhaitez-vous que les résultats asynchrones restent actifs ?).

Notez que la politique d'expiration ne peut être définie qu'en incréments de jours, donc même si vous avez des résultats qui devraient être considérés comme obsolètes après 30 minutes, avec cette approche, vous aurez toujours l'objet en stockage pendant au moins une journée.

Vous pouvez associer un horodatage à l'objet et le vérifier dans votre code pour vous assurer que le résultat est ignoré s'il est plus vieux qu'un certain âge, mais l'objet lui-même persistera pendant au moins une journée.

Pour configurer votre bucket, suivez les étapes suivantes dans la console de gestion AWS :

* Cliquez sur **Créer un bucket** depuis S3
* Entrez le nom du bucket et notez dans quelle région vous le créez (vous devrez vous assurer que vos fonctions Lambda et API Gateway sont toutes configurées dans cette même région). Notez que les noms de buckets S3 sont uniques au niveau mondial, ce qui signifie qu'un nom comme « test » sera probablement pris. Vous devrez choisir quelque chose qu'aucun autre utilisateur n'a créé auparavant, donc quelque chose qui incorpore votre nom ou la date actuelle serait un bon point de départ
* Vous pouvez garder le bucket avec les autorisations par défaut et sans versioning — vous accorderez explicitement à votre fonction Lambda l'autorisation pour ce bucket, donc ne l'exposez pas publiquement au monde (en fait, ce serait une mauvaise idée !)
* Une fois le bucket créé, cliquez dessus et allez dans l'onglet **Gestion**
* Entrez un cycle de vie en cliquant sur **Ajouter une règle de cycle de vie**
* Entrez un nom et passez l'écran des transitions pour arriver à l'écran **Expiration**
* Puisque nous n'avons pas ajouté de versioning à notre bucket S3, vous n'avez besoin de configurer une règle d'expiration que pour la **Version actuelle** comme illustré ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/1*el9er6exEDuhvScJWy8ICw.png)
_Entrez une règle de cycle de vie pour expirer les objets après un jour depuis votre bucket S3_

#### Fonctions Lambda

J'avais l'idée de base d'utiliser une fonction Lambda pour effectuer une recherche, retourner un jeton à l'appelant et écrire les résultats dans un bucket S3. Les résultats pourraient ensuite être récupérés par un appel ultérieur, en passant le jeton et toute information de filtrage supplémentaire (par exemple, « petite voiture » dans l'exemple ci-dessus).

Cependant, j'ai rapidement réalisé que ma fonction Lambda retournerait après avoir validé les paramètres d'entrée et rappelé avec un jeton, ce qui signifiait que je ne pouvais pas la garder active pour écrire les résultats de la recherche dans S3.

Ce dont j'avais besoin, c'était d'un moyen de continuer l'exécution du code après avoir obtenu le jeton afin de pouvoir retourner à l'appelant de l'API. Pour ce faire, j'ai créé **deux** fonctions Lambda, une pour valider les paramètres, et l'autre pour effectuer la recherche et récupérer les résultats mis en cache.

La première fonction valide les paramètres, et une fois cela fait, elle invoque la deuxième fonction Lambda de manière asynchrone pour lancer la recherche, puis retourne avec un jeton généré à l'appelant tandis que la deuxième fonction Lambda tourne. Le jeton que ma fonction `generateToken` a utilisé dans mon atelier était simplement un horodatage puisque je n'avais pas de considérations de scalabilité, mais il pourrait également s'agir d'un UUID ou d'un autre ID généré.

Parce que cette fonction Lambda invoque une autre fonction Lambda, vous devrez lui donner les autorisations appropriées pour effectuer cet appel. Vous faites cela en créant le rôle IAM approprié en suivant ces étapes :

* Dans votre fonction Lambda, sous Rôle d'exécution, sélectionnez **Créer un rôle personnalisé** dans la liste déroulante
* Cela lancera IAM dans un nouvel onglet
* Sélectionnez **Créer un nouveau rôle IAM** dans la liste déroulante pour le rôle IAM et donnez-lui un nom
* Dans la liste complète des rôles IAM, sélectionnez ce nouveau rôle et cliquez sur **Attacher des politiques**
* Filtrez pour la politique **AWSLambdaRole** et ajoutez-la à ce rôle. Optionnellement, vous pouvez modifier le JSON pour lui donner accès **uniquement** à la deuxième fonction Lambda après l'avoir créée dans l'étape suivante, en faisant référence à son ARN dans le champ Ressource

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dw_Pf6dy0TSoMJfHb4-hbA.png)
_Définition du rôle IAM approprié pour appeler une deuxième fonction Lambda_

La deuxième fonction Lambda a deux responsabilités — effectuer la recherche et sauvegarder les résultats dans un bucket S3, et récupérer les résultats d'un bucket S3 lorsqu'elle est appelée avec un jeton valide. J'aurais pu séparer cette logique et créer **trois** fonctions Lambda, mais j'ai estimé qu'il était préférable de regrouper la logique qui accède au cache et sait comment encoder/décoder l'objet en un seul endroit.

Parce qu'API Gateway vous permet de mapper les paramètres de requête, vous trouverez facile de différencier les cas où cette fonction est appelée pour effectuer une nouvelle recherche et lorsqu'elle est appelée pour récupérer un résultat de recherche (je démontrerai comment faire cela plus tard). Notez que cette fonction appelle une fonction interne `doSearch` longue qui écrit les résultats dans S3 en fonction du jeton fourni par la fonction précédente.

Parce que cette fonction Lambda effectue un appel pour lire et écrire depuis S3, vous devrez définir les autorisations appropriées pour cette fonction Lambda — qui seront différentes de la première. Suivez le même ensemble d'étapes pour créer un rôle IAM, seulement cette fois, au lieu de la politique AWSLambdaRole, vous voudrez associer la politique **AmazonS3FullAccess** — en fournissant optionnellement l'ARN du bucket S3 spécifique auquel vous souhaitez donner un accès complet.

#### API Gateway

Maintenant que les fonctions Lambda sont en place, l'étape suivante consiste à créer une API Gateway autour de ces fonctions afin qu'un utilisateur dispose d'une API REST à appeler. Rappelez-vous, le flux que je voulais construire du point de vue du client était :

* Appel POST à l'API avec les paramètres de recherche souhaités
* Obtenir un jeton en réponse
* Poser à l'utilisateur quelques questions supplémentaires pour aider à affiner les résultats
* Appel GET à l'API avec le jeton et des critères de filtrage supplémentaires pour obtenir l'ensemble de résultats réel

API Gateway facilite et rend pratique l'accès à vos fonctions Lambda comme souhaité.

La première étape consiste à créer votre nouvelle API. Dans la console de gestion AWS, vous pouvez naviguer vers API Gateway et cliquer sur **Créer une API** pour créer une nouvelle API. Une fois que vous lui avez donné un nom, vous devez créer les méthodes que vous souhaitez utiliser pour accéder à l'API. Dans mon cas, cela signifiait sélectionner POST et GET comme nouvelles méthodes dans le menu déroulant **Actions**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dz1IoNQdGWnbQPYyafXDOQ.png)
_Création de méthodes dans API Gateway_

Commençons par le POST. Une fois que vous avez sélectionné la méthode POST, vous serez invité à indiquer le **Type d'intégration** que vous souhaitez utiliser. Sélectionnez **Fonction Lambda**, puis remplissez les détails avec la première fonction Lambda que vous avez créée pour valider les paramètres et lancer la recherche. Vous n'avez pas besoin de pointer API Gateway vers la deuxième fonction Lambda qui effectue la recherche — cela est fait par la fonction de validation pour vous.

Après avoir défini ces paramètres, vous verrez le flux complet de l'API, ainsi qu'une barre latérale **TEST** qui vous permettra de passer une charge utile de test à votre API pour voir si elle s'exécute correctement.

Pour l'appel GET, faites de même, bien que dans ce cas, vous allez appeler la deuxième fonction Lambda en passant un jeton afin qu'elle sache récupérer les résultats de votre cache S3. De plus, dans ce cas, vous n'aurez pas de charge utile JSON à transmettre — plutôt, l'attente est que le client fournisse des paramètres de requête dans l'URL. API Gateway vous permet de faire cette transformation facilement via un modèle de mappage.

Les étapes de base sont les suivantes :

* Ajoutez une méthode GET dans le menu déroulant **Actions**
* Définissez le **Type d'intégration** sur **Fonction Lambda**
* Entrez les détails de la deuxième fonction Lambda
* Une fois créée, cliquez sur l'étape **Demande d'intégration** de l'exécution de votre méthode GET
* Développez la section **Modèles de mappage** et cliquez sur **Ajouter un modèle de mappage**
* Tapez **application/json** dans la zone d'édition et cliquez sur la coche pour confirmer
* Entrez le mappage des paramètres de requête vers la requête JSON — vous ferez cela avec des clés de la forme `"field": "$input.params('queryparam')"` Cela mappera le paramètre de requête nommé `queryparam` à un champ nommé `field`

Le point positif ici est que vous n'avez pas besoin d'avoir le même nom pour les paramètres de requête exposés à votre client que pour l'utilisation interne dans votre fonction Lambda. Par exemple, dans mon cas, j'attends des paramètres tels que User, CarSize, SupplierRating et UpgradeClass, mais je les mappe à id, size, rating et upgrade respectivement pour une utilisation interne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KzXmvhyIXX6GxeJcvrYwKw.png)
_Mappage des paramètres d'URL vers une charge utile JSON pour le GET_

#### Construction et déploiement

Maintenant que vous avez intégré votre fonction Lambda dans API Gateway, vous êtes prêt à construire et déployer. Dans le menu Actions, sélectionnez **Déployer l'API**. API Gateway vous demandera un stade de déploiement ; choisissez **[Nouveau stade]** pour créer un nouveau stade, et donnez-lui un nom comme Bêta. Après avoir déployé l'API, API Gateway vous indiquera l'URL à utiliser pour invoquer votre API. Vous utilisez la même URL pour les fonctions POST et GET. Plutôt facile, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*hX28gjVTDahpZJzioaahCw.png)
_Prêt à déployer votre API_

#### Conclusion

Ce que j'ai décrit ici est la base d'une API asynchrone sans serveur. Il y a beaucoup de cas limites et de gestion des erreurs que j'ai survolé, ainsi que des techniques au sein d'API Gateway pour renforcer l'API que je n'ai pas abordées, telles que la validation que tous les paramètres requis sont définis avant d'invoquer la fonction Lambda ou l'exigence d'un jeton d'accès plutôt que de créer une API ouverte à tous.

De plus, ce cas d'utilisation était pour un petit environnement d'atelier. Vous devrez examiner votre propre cas d'utilisation pour comprendre l'échelle dont vous avez besoin et si cette approche fonctionnerait pour vous. Vous devrez porter une attention particulière aux paramètres d'exécution simultanée de votre fonction Lambda. Si l'appel sous-jacent que vous essayez de faire prend une minute à s'exécuter par exemple, même avec une limite de 1000 exécutions simultanées, vous ne pourriez faire que 16 appels par seconde, ce qui pourrait ne pas suffire pour une charge de travail de production complète.

Mis à part les réserves, pour les bons cas d'utilisation, cette approche peut être un moyen simple et puissant de créer une API asynchrone sans avoir à mettre en place des serveurs dédiés ou une solution de mise en cache.
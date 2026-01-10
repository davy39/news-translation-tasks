---
title: Bonnes pratiques pour créer des clés API sécurisées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-30T05:09:37.000Z'
originalURL: https://freecodecamp.org/news/best-practices-for-building-api-keys-97c26eabfea9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-QHPiNtOHuhuD2B7SqMLPw.png
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Bonnes pratiques pour créer des clés API sécurisées
seo_desc: 'By Ramesh Lingappa

  We all know how valuable APIs are. They’re the gateway to exploring other services,
  integrating with them, and building great solutions faster.

  You might have built or are thinking of building APIs for other developers to use.
  An A...'
---

Par Ramesh Lingappa

Nous savons tous à quel point les API sont précieuses. Elles constituent la passerelle pour explorer d'autres services, s'intégrer avec eux et construire des solutions plus rapidement.

Vous avez peut-être construit ou envisagez de construire des API pour que d'autres développeurs les utilisent. Une API a besoin d'une forme d'authentification pour fournir un accès autorisé aux données qu'elle retourne.

Il existe plusieurs normes d'authentification disponibles aujourd'hui telles que les clés API, [OAuth](https://oauth.net/2/), [JWT](https://jwt.io/), etc.

Dans cet article, nous examinerons comment gérer correctement les clés API pour accéder aux API.

#### Pourquoi les clés API ?

Les clés API sont simples à utiliser, elles sont courtes, statiques et n'expirent pas sauf si elles sont révoquées. Elles offrent un moyen facile pour que plusieurs services communiquent.

Si vous fournissez une API pour vos clients, il est essentiel de la construire de la bonne manière.

Commençons, et je vous montrerai comment construire des clés API de la bonne manière.

### Génération de clés API

Puisque la clé API elle-même est une identité permettant d'identifier l'application ou l'utilisateur, elle doit être unique, aléatoire et non devinable. Les clés API générées doivent également utiliser des caractères alphanumériques et spéciaux. Un exemple d'une telle clé API est `zaCELgL.0imfnc8mVLWwsAawjYr4Rx-Af50DDqtlx`.

### Stockage sécurisé des clés API

Puisque la clé API fournit un accès direct aux données, c'est un peu comme un mot de passe qu'un utilisateur d'une application web ou mobile fournit pour accéder aux mêmes données.

Réfléchissez-y. La raison pour laquelle nous devons stocker les clés API est de nous assurer que la clé API dans la requête est valide et émise par nous (comme un mot de passe).

Nous n'avons pas besoin de connaître la clé API brute, mais nous devons simplement valider que la clé est correcte. Au lieu de stocker la clé en texte brut (mauvais) ou de la chiffrer, nous devons la stocker sous forme de valeur hachée dans notre base de données.

Une valeur hachée signifie que même si quelqu'un obtient un accès non autorisé à notre base de données, aucune clé API n'est divulguée et tout est sécurisé. L'utilisateur final enverrait la clé API brute dans chaque requête API, et nous pouvons la valider en hachant la clé API dans la requête et en comparant la clé hachée avec le hachage stocké dans notre base de données. Voici une implémentation approximative en Java :

Dans le code ci-dessus, la clé primaire sera une combinaison du préfixe et du hachage de la clé API `{prefix}.{hash_of_whole_api_key}`.

Mais attendez, il y a plus. Le stockage d'une valeur hachée pose des problèmes spécifiques d'utilisabilité. Abordons-les maintenant.

### Présentation de la clé API aux utilisateurs

Puisque nous ne stockons pas la clé API originale, nous pouvons la montrer une seule fois à l'utilisateur, au moment de la création. Assurez-vous donc d'alerter les utilisateurs qu'elle ne peut pas être récupérée à nouveau, et qu'ils doivent générer un nouveau jeton s'ils oublient de copier la clé API et de la stocker en sécurité. Vous pouvez faire quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DutIyYh2hE-YAkirxtoIxg.png)
_Affichage de la clé API générée avec un message d'alerte_

#### Comment les utilisateurs peuvent identifier une clé API générée plus tard

Un autre problème est de savoir comment les utilisateurs identifient la bonne clé API dans votre console s'ils doivent la modifier ou la révoquer. Cela peut être résolu en ajoutant un préfixe à la clé API. Remarquez dans l'image ci-dessus **les 7 premiers caractères (c'est notre préfixe)**, séparés par le point.

Vous pouvez maintenant stocker ce préfixe dans la base de données et l'afficher dans la console afin que les utilisateurs puissent identifier rapidement la bonne entrée de clé API, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WU0mFXXFXW2VlA9BXK3ffA.png)
_Console de gestion des clés API_

### Ne donnez pas tous les pouvoirs à la clé API

Une erreur courante que commettent les fournisseurs de clés API est de fournir **une seule clé pour accéder à tout**, car c'est facile à gérer. Ne faites pas cela. Supposons qu'un utilisateur doit simplement lire un email et génère une clé API. Mais cette clé a maintenant un accès complet à d'autres services, y compris la suppression de enregistrements dans la base de données.

La **bonne** approche est de permettre aux utilisateurs finaux de restreindre correctement l'accès des clés API et de choisir des actions spécifiques qu'une clé API peut effectuer. Cela peut être fait en fournissant des **portées**, où chaque portée représente une permission spécifique.

Par exemple,

* si vous avez besoin d'une clé API pour simplement envoyer des emails, vous pouvez générer une clé API avec la portée **"email.send"**
* si l'utilisateur final a plusieurs serveurs et que chacun effectue une action spécifique, alors une clé API séparée peut être générée avec une portée spécifique.

Ainsi, lors de la création de la clé API, permettez aux utilisateurs de sélectionner à quelles données cette clé API doit avoir accès, comme dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-HHZ-Vfwz9FBPl-FIlS6mg.png)

De cette manière, les utilisateurs peuvent générer plusieurs clés API, chacune avec des règles d'accès spécifiques pour une meilleure sécurité. Et lorsqu'une requête API est reçue, vous pouvez vérifier si la clé API a la bonne portée pour accéder à cette API. Maintenant, la base de données ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*y9SVyRJa3m50tQ0buEU1VA.png)
_Entité de base de données des clés API_

### Limitation de débit des clés API

Oui, vous le savez peut-être déjà, mais il est important de limiter le débit des requêtes faites avec des clés API spécifiques pour vous assurer qu'aucun acteur malveillant ne peut faire tomber vos serveurs API ou causer des problèmes de performance qui affectent vos autres clients. Avoir une solution de limitation de débit et de surveillance appropriée maintient le service API en bonne santé.

### Conclusion

Les clés API, lorsqu'elles sont bien construites, restent un excellent moyen de communiquer avec un autre serveur. Comme nous l'avons passé en revue dans cet article, le suivi de certaines pratiques offre des avantages à la fois aux consommateurs d'API et aux fournisseurs d'API. J'espère que cela vous aide.

Bonne sécurisation de vos API !
---
title: Comment concevoir une API - Bonnes pratiques de l'interface de programmation
  d'applications
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2022-06-29T18:04:39.000Z'
originalURL: https://freecodecamp.org/news/design-an-api-application-program-interface
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Tech-Blog-Cover--2-.png
tags:
- name: api
  slug: api
- name: best practices
  slug: best-practices
seo_title: Comment concevoir une API - Bonnes pratiques de l'interface de programmation
  d'applications
seo_desc: 'API stands for Application Programming Interface. An API communicates with
  two applications using requests and responses. It is exposed to external users.

  How Does an API Work?


  How an API works

  Imagine you are in a store and want to buy a soda. But ...'
---

**API** signifie Interface de Programmation d'Applications. Une API communique avec deux applications en utilisant des requêtes et des réponses. Elle est exposée aux utilisateurs externes.

## Comment fonctionne une API ?

![Image](https://www.freecodecamp.org/news/content/images/2022/06/What-are-APIs-Learn-How-API-Works.jpg)
_Comment fonctionne une API_

Imaginez que vous êtes dans un magasin et que vous voulez acheter un soda. Mais vous ne pouvez pas simplement entrer et en prendre un parce que vous êtes un outsider – un utilisateur externe – donc vous avez besoin d'un lien (parler à quelqu'un et payer pour votre soda) pour obtenir ce que vous voulez.

Vous ne pouvez pas vous lier directement aux étagères – la base de données – parce qu'elles ne peuvent pas bouger ou parler. C'est là que le vendeur – l'API – intervient. Le vendeur sert d'intermédiaire entre vous et l'article – les données (soda) – que vous voulez.

Maintenant, vous avez un lien pour communiquer avec les articles sur les étagères, alors vous demandez le soda. Ensuite, le vendeur cherche la marque de soda et le parfum que vous voulez et vous le donne. Vous payez, le prenez et partez.

### Que vient-il de se passer ?

Le vendeur (agissant comme l'API) a interrogé les étagères (la base de données) pour les données demandées.

Comme vous le savez peut-être, les ensembles de données viennent sous différentes formes. L'API a interrogé la base de données pour une table puis a cherché dans la table des données détaillées. Enfin, l'API vous a envoyé les données dont vous aviez besoin.

Disons que vous demandez un soda Fanta.

**Votre requête :**

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-184.png)

**Votre réponse :**

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-185.png)

La réponse est toujours au format JSON (JavaScript Object Notation). C'est ainsi qu'une API fonctionne.

## Comment concevoir une API

Lors de la conception d'une API, vous devez considérer certaines bonnes pratiques qui peuvent vous aider à optimiser vos API et leurs temps de réponse.

### Nommer correctement l'API

Supposons que vous créez une API qui vous envoie les données d'un utilisateur particulier. Il ne serait pas judicieux de nommer l'API simplement **GetUsers** car cela signifie que vous voulez obtenir tous les utilisateurs de la base de données, et l'utilisateur externe qui appellera cette API s'attendra à une réponse de ce que vous voulez donner.

#### Exemples de bon nom pour une API

* Utilisez un nom clair et concis :

Si vous voulez interroger une base de données de pommes, il ne serait pas logique de nommer l'API **"api/fruits/."**

Bien qu'une pomme soit un fruit, ce n'est pas ce que l'utilisateur final veut. L'utilisateur final veut un fruit particulier, alors nommez-la **"api/apples/".**

* Utilisez des mots qui expliquent la requête :

Utilisez des mots comme des noms qui représentent le contenu des ressources dans l'API, par exemple **"api/stationery/pens"**. Cela explique que l'API interroge tous les stylo dans la base de données de papeterie.

Cela serait au lieu de, par exemple, **"api/stationery/write".**

* Évitez les caractères spéciaux :

Cela peut confondre l'utilisateur final s'il voit une API comme **"api/fruits%20?/apple".** Ils ne comprendront pas ce que fait cette API ou comment elle interroge, ou quelles informations elle obtiendra.

### Définir les paramètres lorsque nécessaire

Essayez autant que possible d'éviter d'utiliser des paramètres supplémentaires sauf si vous en avez besoin. Voici quelques exemples de paramètres requis lors de la création d'une API RestFul :

* **En-têtes de requête et cookies** : Ce paramètre utilise une petite partie de données qu'un serveur envoie au navigateur web de l'utilisateur.
* **Chaîne de requête URL** : Ces éléments de paramètre sont insérés dans vos URL pour vous aider à filtrer et organiser le contenu ou suivre les informations sur votre site web.
* **Chemins URL** : Il s'agit d'un paramètre requis qui donne à l'utilisateur final ou à celui qui appelle l'API un moyen d'obtenir les bonnes informations, telles que : **"/users/"**, **"/users/<user_id>/", "package/<package_id>"**.
* **Chaîne de requête/multipartie du corps** : Ce paramètre définit la méthode HTTP pour la question ou l'API, telle que **POST** – pour envoyer des données, ou **PUT** – pour mettre à jour les données dans une API.

Alors, quand avez-vous besoin de paramètres ? Supposons que des utilisateurs externes effectuent plusieurs requêtes sur un service API, et que l'API interrogera d'autres services pour obtenir les données souhaitées par les utilisateurs.

Cela ralentira le service API, mais des paramètres supplémentaires sont utiles dans ce cas.

### Définir les objets de réponse

En termes profanes, les objets de réponse sont des propriétés d'une réponse lorsqu'une API est déclenchée ou appelée. Voici quelques objets de réponse :

* **Titre** : Il s'agit du titre d'affichage de la réponse, tel que **User** si l'objet retourne des informations sur un utilisateur. Il s'agit d'un objet de réponse requis.
* **Sujet** : Il s'agit du sujet de la réponse, tel que l'utilisateur et toute autre information liée à l'utilisateur que l'API est censée relier.
* **Sender_id** : Il s'agit de l'ID de l'expéditeur ou de l'utilisateur créé. Il s'agit d'un objet de réponse optionnel, ce qui signifie que vous pouvez choisir de ne pas l'ajouter à l'objet de réponse s'il n'est pas nécessaire.
* **Catégories** : Il s'agit de la catégorie de l'objet de réponse. Si l'API retourne des informations sur un utilisateur, la catégorie sera **Users**.

De nombreux développeurs créent un objet de réponse qui contient tout ce qui provient du service API – même des informations inutiles – dans l'espoir de ne pas changer l'objet de réponse lorsque l'utilisateur demande plus de détails (car cela nécessite plus de ressources réseau).

Malheureusement, cela constitue une mauvaise pratique de conception d'API. Lors de la création d'un objet de réponse, il est judicieux de ne retourner que ce dont l'utilisateur externe aura besoin, car la construction d'un grand microservice affectera les performances et plus encore.

### Définir les objets d'erreur

Lorsque vous retournez un message d'erreur lorsqu'un utilisateur externe interroge la base de données, le message doit être clair et concis – pas seulement un message d'erreur générique comme "**Error Found**" ou "**Error occurred.**"

Cela devrait être le titre de la réponse, et la section des données ou du sujet devrait expliquer quel type d'erreur s'est produit.

Voici mon avis personnel lors de la création d'un message d'erreur d'API. Ne retournez pas un message d'erreur inutile. Supposons que certaines données utilisateur ont une longueur maximale de caractères de 5, et qu'un utilisateur externe interroge l'API pour des données utilisateur avec une longueur de caractères de 8.

Au lieu de faire ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-224.png)

Faites ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-225.png)

Cela explique ce que l'utilisateur final a fait de mal et le formatage montre à l'utilisateur final que cette erreur est une erreur client.

### Utiliser les bonnes méthodes de requête HTTPS

Lors de la définition d'une [méthode HTTP](https://doc.oroinc.com/api/http-methods/#:~:text=The%20primary%20or%20most%20commonly,or%20CRUD)%20operations%2C%20respectively.) pour un service API, vous devez utiliser la méthode correcte pour permettre aux utilisateurs d'interroger de la bonne manière. Voici quelques méthodes HTTPS :

* **POST** : Utilisez cette méthode si l'utilisateur final doit envoyer des données à l'API.
* **GET** : Utilisez cette méthode si l'utilisateur final doit récupérer des données après que l'API a interrogé la base de données.
* **PUT** : Utilisez cette méthode si l'utilisateur final met à jour des données existantes dans la base de données.
* **PATCH** : Utilisez cette méthode si l'utilisateur final doit corriger ou remplacer des données existantes dans la base de données.
* **DELETE** : Utilisez cette méthode si l'utilisateur final supprime des informations ou des données de la base de données.

Imaginez qu'un utilisateur externe souhaite interroger la table des utilisateurs en envoyant un ID, et que la méthode API que vous avez conçue utilise la méthode **POST**. Cela limitera les requêtes des utilisateurs car l'utilisateur final n'ajoute pas ou ne crée pas de données, et l'utilisateur ne peut pas interroger de la manière dont il devrait pouvoir le faire.

Au lieu de cela, il serait préférable d'utiliser la méthode **GET** avec un ID comme paramètre, et cela devrait se faire ainsi :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/users-path.png)

Cela donnera aux utilisateurs la possibilité d'interroger en utilisant un ID et d'obtenir des données spécifiques.

Je suggère de connaître toutes les méthodes de requête HTTP avant de définir une méthode et de retourner le bon ID lorsqu'il est demandé.

Assurez-vous que le routage est parfaitement clair afin que les utilisateurs puissent rapidement appeler le service API que j'ai montré précédemment.

### Ne créez pas d'effets secondaires sur l'API

Un effet secondaire est, par exemple, lorsqu'un utilisateur externe interroge une API pour le prénom de l'utilisateur mais qu'elle retourne l'ID et le nom complet.

Lors de la création d'une API, essayez de ne pas définir tout dans une seule fonction autant que possible. Si l'API définit de nombreux drapeaux ou effectue de nombreuses tâches simultanément, elle doit être divisée en plusieurs API. C'est là que l'atomicité entre en jeu.

L'[atomicité](https://docs.oracle.com/cd/E17275_01/html/programmer_reference/transapp_atomicity.html#:~:text=Atomicity%20means%20that%20multiple%20operations,or%20none%20of%20the%20changes.) est lorsque plusieurs opérations sont regroupées en une seule entité logique. L'atomicité est importante lors de la création d'une API. Lorsque vous utilisez l'atomicité, mal nommer une fonction est simplement une mauvaise idée.

#### Quand l'atomicité est-elle nécessaire ?

Imaginez que nous voulons qu'un utilisateur soit créé en tant qu'administrateur sous la table de groupe des administrateurs. Cependant, nous n'avons pas encore créé la table de groupe des administrateurs, donc notre logique est de créer un utilisateur en tant qu'administrateur, créer la table de groupe des administrateurs, puis ajouter l'utilisateur administrateur à la table de groupe des administrateurs.

_Mais que se passe-t-il si cela échoue ?_ Supposons que l'utilisateur n'est pas créé en tant qu'administrateur, mais que la table des administrateurs est créée ou vice versa. C'est là que l'atomicité entre en jeu.

Lorsque vous utilisez l'atomicité pour appeler une action, essayez d'appeler la bonne action au lieu d'une action générique. Sinon, cela crée un énorme désordre dans l'API, et il y aura de la confusion lors de l'utilisation de l'API.

### Implémenter la pagination

Lors de la création d'un grand microservice et que le corps ou l'objet de réponse devient trop volumineux, la pagination facilite le retour d'une petite quantité d'informations par l'API.

La pagination est une méthode de séparation du contenu numérique en différentes pages sur un site web ou un objet de réponse.

Imaginez une base de données avec soixante-dix utilisateurs. L'API appelle **getUsers** au lieu d'envoyer la réponse de tous les utilisateurs en une seule fois et de la rendre lente.

Vous pouvez diviser la réponse, comme retourner les trente premiers utilisateurs, les trente utilisateurs suivants, et les dix utilisateurs suivants. La réponse paginée est plus rapide, cependant.

Mais cela viole la propriété des API sans état, qui est lorsqu'un utilisateur externe gère le stockage des informations liées à la session de leur côté.

### Utiliser la [fragmentation](https://www.ibm.com/docs/SSGU8G_14.1.0/com.ibm.ddi.doc/ids_ddi_084.htm#:~:text=Fragmentation%20is%20a%20database%20server,to%20some%20algorithm%20or%20scheme%20.)

Lorsque qu'une API communique en interne, la réponse est généralement courte. Mais lorsqu'il s'agit d'une grande réponse, c'est une exception, et lorsqu'il s'agit d'une exception, il y a un problème.

Cela se produit lorsque la réponse dépasse sa limite (10 ko ou 15 ko par réponse). La solution ici est de diviser la réponse et de la donner à un autre service bit par bit.

C'est comme diviser le numéro TCP (Transmission Control Protocol) en fragments et le distribuer afin que le service ne soit pas surchargé.

Il saura que plus de détails sont à venir, et il aura également un paquet de fin, comme une commande de rupture, qui indique que le protocole se termine lorsque les fragments sont sur le point de se terminer.

## Conclusion

Voici quelques points majeurs à retenir de cet article :

* Évitez les caractères étranges et utilisez des mots qui représentent le contenu de la réponse de l'API.
* La pagination et la fragmentation sont essentielles lorsque l'objet de réponse est vaste.
* Vous devriez mettre en cache vos requêtes si vous avez beaucoup de charge sur votre base de données.
* Si vous avez beaucoup de charge, réduisez votre temps de réponse au lieu de transmettre toutes les informations à l'utilisateur. Transmettez simplement les données essentielles ou critiques. Cela s'appelle la **dégradation de service**. Cela implique de donner l'essentiel et de répondre sans planter le service API.
* Lors de la conception d'une API et que vous voulez une cohérence parfaite des données, mettez en cache vos réponses.
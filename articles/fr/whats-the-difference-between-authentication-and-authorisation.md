---
title: Authentification vs Autorisation – Quelle est la différence ?
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2022-09-29T17:45:49.000Z'
originalURL: https://freecodecamp.org/news/whats-the-difference-between-authentication-and-authorisation
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Background1.jpg
tags:
- name: Application Security
  slug: application-security
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: information security
  slug: information-security
seo_title: Authentification vs Autorisation – Quelle est la différence ?
seo_desc: 'When you''re starting out in web development, you''ll likely hear the terms
  authentication and authorization all the time. And it doesn''t help that they''re
  both usually abbreviated ''auth'', so it''s very easy to get the two confused.

  In this article, you...'
---

Lorsque vous débutez en développement web, vous entendrez probablement les termes authentification et autorisation tout le temps. Et le fait qu'ils soient tous deux généralement abrégés en 'auth' n'aide pas, il est donc très facile de les confondre.

Dans cet article, vous apprendrez :

* Les différences entre l'authentification et l'autorisation
* Comment chacun de ces processus fonctionne
* Des exemples d'autorisation et d'authentification dans la vie quotidienne.

‌‌‌‌Ok, commençons.

## Qu'est-ce que l'authentification ?

L'authentification est le processus de **vérification** des identifiants fournis par un utilisateur par rapport à ceux stockés dans un système pour **prouver** que l'utilisateur est bien celui qu'il prétend être. Si les identifiants correspondent, vous accordez l'accès. Sinon, vous le refusez.

### Méthodes d'authentification

#### Authentification à facteur unique :

Elle est souvent utilisée comme processus d'authentification pour les systèmes à faible risque. Vous n'avez besoin que d'un seul facteur pour vous authentifier, le plus courant étant un mot de passe, ce qui le rend plus vulnérable aux attaques de phishing et aux enregistreurs de frappe (key loggers).

En plus de cela, un récent [article](https://dataprot.net/statistics/password-statistics/) de DataProt a montré que 78 % des membres de la génération Z utilisent le même mot de passe pour plusieurs services. Cela signifie que si un attaquant accédait à un compte utilisateur, il aurait une forte probabilité d'accéder aux autres en utilisant simplement le même mot de passe.

#### Authentification à 2 facteurs :

Cette méthode est plus sécurisée, car elle comprend deux facteurs d'authentification – généralement quelque chose que vous connaissez, par exemple un nom d'utilisateur et un mot de passe, plus quelque chose que vous avez / possédez, par exemple un SMS sur votre téléphone ou un jeton de sécurité.

Pour l'authentification à 2 facteurs, vous devriez saisir un mot de passe SMS à usage unique envoyé à votre appareil, ou peut-être un code d'application d'authentification liée et fournir un code d'accès en constante évolution.

Comme vous pouvez l'imaginer, c'est beaucoup plus sûr que de simplement saisir un mot de passe ou un seul identifiant d'authentification. Vous auriez besoin de connaître les identifiants de connexion, ainsi que d'avoir accès à l'appareil physique pour la deuxième partie.

L'authentification à 2 facteurs est devenue très courante parmi les services en ligne ces dernières années, et pour de nombreuses grandes entreprises, c'est la méthode d'authentification par défaut. Beaucoup exigent que vous configuriez l'authentification à 2 facteurs pour pouvoir même utiliser le service.

#### Authentification multi-facteurs :

Aller encore plus loin pour rendre votre processus d'authentification encore plus sécurisé consiste à avoir 3 facteurs ou plus. Cette forme d'authentification fonctionne généralement sur le principe de :

* quelque chose que vous connaissez (nom d'utilisateur + mot de passe ou nom d'utilisateur + question et réponse de sécurité)
* quelque chose que vous avez (SMS sur téléphone mobile, application d'authentification, clé USB)
* quelque chose que vous êtes (comme une empreinte digitale / reconnaissance faciale)

Pour ces raisons, l'authentification multi-facteurs offre la protection la plus élevée, car il faudrait compromettre plusieurs facteurs, et ces facteurs sont beaucoup plus difficiles à "pirater" ou à reproduire.

L'inconvénient de cette méthode d'authentification, et la raison pour laquelle elle n'est pas utilisée dans de nombreux systèmes moyens, est qu'elle peut être fastidieuse à mettre en place et à maintenir. Ainsi, les données / le système que vous protégez doivent réellement justifier le besoin d'une telle sécurité.

## Alors, de quelle quantité d'informations avez-vous besoin pour vous authentifier ?

Cette question revient lors de nombreuses réunions d'architecture de sécurité, et la réponse est "_cela dépend_".

Il n'est pas rare que les entreprises combinent diverses méthodes d'authentification pour accroître la sécurité en fonction de la nature de l'application.

Par exemple, prenez une application bancaire. Elle contient des informations très sensibles et pourrait avoir d'énormes impacts financiers et de réputation si elle était obtenue par la mauvaise personne. La banque peut combiner des questions personnelles auxquelles répondre, ainsi qu'un numéro de client et un mot de passe complexe.

D'un autre côté, pour un site de médias sociaux, vous pourriez n'avoir besoin que d'un nom d'utilisateur et d'un mot de passe, qui sont ensuite vérifiés avant d'autoriser l'accès.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Auth_Process-1.png)

Tout est question du niveau de risque impliqué et des informations auxquelles quelqu'un peut accéder une fois qu'il est dans l'application. Cela aide à déterminer le niveau d'authentification dont vous avez besoin.

Si vous ou votre équipe sous-estimez le niveau d'authentification dont votre application a besoin, vous pourriez être poursuivi pour ne pas avoir sécurisé les données de votre système de manière adéquate. C'est pourquoi les entreprises emploient des spécialistes de la sécurité pour conseiller sur les meilleures pratiques et les solutions appropriées.

## Comment fonctionne l'authentification dans le monde réel ?

Prenons l'exemple d'un compte de médias sociaux. Vous choisissez votre site de médias sociaux préféré (qui est hébergé sur un serveur). Le serveur vous demandera de fournir des identifiants pour accéder au site via une page de connexion. Ici, vous taperiez votre nom d'utilisateur et votre mot de passe que vous avez utilisés lors de la création du compte.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/server-process-2.png)
_Image montrant le processus d'authentification_

Ces détails sont ensuite envoyés au serveur, et le processus d'authentification commence. Les détails que vous avez fournis sont vérifiés dans la base de données du serveur, et s'ils correspondent aux détails enregistrés, vous êtes authentifié. Ensuite, on vous fournit une forme de données d'identification, par exemple un cookie ou un Json Web Token (token JWT).

Succès ! Vous avez accédé au site et l'entrée vous est accordée.

Vous pouvez en apprendre davantage sur les tokens JWT dans un autre article de FreeCodeCamp par Beau Carnes [ici](https://www.freecodecamp.org/news/what-are-json-web-tokens-jwt-auth-tutorial/).

Ensuite, regardons l'autorisation.

## Qu'est-ce que l'autorisation ?

L'autorisation est le processus de vérification que vous êtes **autorisé** à accéder à une zone d'une application ou à effectuer des actions spécifiques, sur la base de certains critères et conditions mis en place par l'application. Vous pouvez également l'entendre appeler contrôle d'accès ou contrôle des privilèges.

L'autorisation peut soit accorder, soit refuser la permission d'effectuer des tâches, ou d'accéder à des zones d'une application.

Regardons un exemple :

Nous avons accédé au site de médias sociaux, mais ce que nous sommes autorisés à y faire dépend de ce que nous sommes autorisés à faire.

Si nous essayons d'accéder au profil de quelqu'un avec qui nous ne sommes pas amis (il n'a pas accepté notre demande de connexion), nous ne sommes pas **autorisés** à voir son profil. Cela signifie que la permission de voir ses publications partagées nous est refusée.

![Basic Authorisation Process](https://www.freecodecamp.org/news/content/images/2022/09/auth-process2-1.png)
_Image du flux d'autorisation_

### Comment implémenter l'autorisation

Il existe de nombreuses façons d'implémenter l'autorisation en fonction des frameworks que vous utilisez.

Au sein du Framework .NET, par exemple, vous pourriez utiliser le contrôle d'accès basé sur les rôles (role-based access control) ou le contrôle d'accès basé sur les revendications (claims-based access control).

Le contrôle d'accès basé sur les rôles est centré sur l'idéologie selon laquelle chaque utilisateur au sein de votre système se voit attribuer un rôle. Ces rôles ont des permissions prédéfinies qui leur sont associées. Se voir accorder un rôle signifie que cet utilisateur héritera automatiquement de toutes ces permissions. Les rôles sont attribués au moment de la création et de la configuration de l'utilisateur.

Le point de terminaison (endpoint) ou le site vérifie simplement si l'utilisateur actuellement connecté a le rôle d'Admin lors de la tentative d'accès à la zone d'administration.

L'inconvénient de cette approche est que parfois les utilisateurs se voient accorder trop de permissions dont ils n'ont pas besoin ou qu'ils ne devraient pas avoir.

Par exemple, donner à un utilisateur le rôle d' `Admin` peut signifier qu'il aurait reçu les privilèges d'utilisateur `Advanced Create`, `Edit`, `Delete` et `View`. Alors que vous pourriez vouloir ne lui donner que les permissions `View` et `Basic Create`.

Le contrôle d'accès basé sur les revendications peut permettre un réglage plus fin des permissions d'un utilisateur spécifique. L'application peut soit vérifier que la revendication (claim) existe simplement sur un utilisateur, soit si une valeur particulière est attribuée à la revendication.

À titre d'exemple, une revendication appelée `CreateUser` pourrait être donnée à un utilisateur, et celle-ci est vérifiée lors de la création d'un utilisateur. Ou vous pourriez attribuer une valeur de "Advanced" à la même revendication, puis avoir différentes actions et interfaces utilisateur disponibles selon que la valeur est "Advanced" ou "Basic".

## Quelle est la différence entre l'authentification et l'autorisation ?

Maintenant que nous avons une meilleure compréhension des termes, regardons un scénario qui vous est peut-être familier et qui implique les deux processus.

Lors d'un dîner avec une liste d'invités exclusive, chaque invité reçoit un surnom et un mot de passe secret.

À votre arrivée, un agent de sécurité vous demande votre surnom et votre mot de passe secret. Il **authentifie** ensuite vos identifiants par rapport à la liste qu'il possède. Si vos identifiants correspondent, on vous remet une enveloppe montrant que vous avez été autorisé à entrer.

Une fois à l'intérieur, vous êtes autorisé à accéder à la fête et aux zones publiques du lieu car celles-ci ne nécessitent aucune **autorisation** (tout le monde a la permission de profiter de la fête). Cependant, vous souhaitez ensuite vous rendre dans la zone VIP.

À votre approche, un autre personnel de sécurité demande à ouvrir votre enveloppe (vos permissions et vos rôles). Il y jette un œil mais malheureusement vous n'avez pas le rôle VIP, et n'êtes donc pas **autorisé** à y accéder.
‌‌‌‌Pour faire simple, l'authentification vérifie l'identité d'un utilisateur ou d'un service autorisant l'accès, tandis que l'autorisation détermine ce qu'il peut faire une fois qu'il est entré.

## Pourquoi devriez-vous implémenter à la fois l'authentification et l'autorisation ?

Comme vous pouvez le voir, bien que l'authentification et l'autorisation soient très différentes, chacune joue un rôle intégral dans la sécurité et l'intégrité de l'application ou du système.

Ces processus vont de pair, et sans l'un, l'autre est en quelque sorte dénué de sens. Si vous pouvez accéder à la zone Admin, mais faire tout ce que vous voulez une fois là-bas, cela pourrait mener à de gros problèmes.

D'un autre côté, vous ne pouvez pas autoriser des individus sans savoir qui ils sont ! C'est pourquoi l'authentification vient toujours avant l'autorisation.

## Mot de la fin

J'espère que cela a été instructif et que vous avez maintenant une compréhension plus claire des différences entre l'autorisation et l'authentification, et comment les utiliser.

Rappelez-vous :

* Authentifier = Vérifie l'identité d'un utilisateur ou d'un processus.
* Autoriser = Détermine si l'utilisateur / le système a la permission d'utiliser une ressource ou d'effectuer une action.

N'hésitez pas à me contacter via Twitter si vous souhaitez discuter de cet article plus en détail [@gweaths](http://twitter.com/gweaths).
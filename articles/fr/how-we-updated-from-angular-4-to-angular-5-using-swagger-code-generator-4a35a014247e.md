---
title: Comment nous avons mis à jour d'Angular 4 à Angular 5 en utilisant le générateur
  de code Swagger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T18:05:47.000Z'
originalURL: https://freecodecamp.org/news/how-we-updated-from-angular-4-to-angular-5-using-swagger-code-generator-4a35a014247e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c5MXOqXBhsy0nVXEdP89og.png
tags:
- name: Angular
  slug: angular
- name: coding
  slug: coding
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment nous avons mis à jour d'Angular 4 à Angular 5 en utilisant le générateur
  de code Swagger
seo_desc: 'By Mark Grichanik

  As a full stack developer in an enterprise company, I had the opportunity to update
  our client side to Angular 5. The process itself is not simple and there are many
  things to take into account. In this article, I’ve outlined the ne...'
---

Par Mark Grichanik

En tant que développeur full stack dans une entreprise, j'ai eu l'opportunité de mettre à jour notre côté client vers **Angular 5**. Le processus lui-même n'est pas simple et il y a beaucoup de choses à prendre en compte. Dans cet article, j'ai décrit les étapes nécessaires pour mettre à jour votre version d'Angular avec facilité et simplicité.

> _Selon l'équipe Angular, il est déconseillé de mettre à jour directement de la version 4 à la version 6. C'est pourquoi cet article se concentrera sur la mise à jour vers la version 5._

> Juste pour information, l'équipe Angular promet que la mise à jour à partir d'Angular 6 et au-delà sera plus légère et plus facile à gérer.

### Prérequis

Assurez-vous d'utiliser la dernière version de Swagger. Angular 5 déprécie OpaqueToken et utilise maintenant InjectionToken à la place.

OpaqueToken est une valeur unique et immuable qui permet aux développeurs d'éviter les collisions d'ID de jetons DI. [InjectionToken](https://angular.io/api/core/InjectionToken)<T> est une version paramétrée et sécurisée de 'OpaqueToken'.

> _Nous utilisons swagger-codegen-maven-plugin, version 2.2.2. En raison du problème mentionné précédemment, nous avons dû passer à la version 2.3.1._

> Dans le fichier maven pom.xml, nous avons dû changer l'attribut de langage du fichier swagger yml de 'typescript-angular2' à 'typescript-angular' qui devrait supporter toutes les versions d'Angular à partir de maintenant.

Avec Swagger 2.2.2, le BASE_PATH est généré comme suit :

Contrairement à Swagger 2.3.1, qui est supporté par Angular 5 :

Notez qu'il y a une autre différence majeure entre les versions de Swagger en ce qui concerne le fichier généré. Par exemple, si nous avions un fichier dogResource.java qui contient toutes sortes d'appels REST, **Swagger 2.2.2** générera dogApi.ts. Alors que **Swagger 2.3.1** le générera en tant que service. C'est-à-dire, dog.service.ts.

> _Après la mise à jour vers la dernière version de Swagger, vous devez refactoriser vos imports pour utiliser dog.service.ts au lieu de dogApi.ts._

![Image](https://cdn-media-1.freecodecamp.org/images/0*KHF_L94Z1iOA6jxA)
_by [Unsplash](https://unsplash.com/@bruno_nascimento?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Bruno Nascimento</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Commençons

Notre côté serveur est écrit en Java tandis que notre côté client est écrit en utilisant Angular 4. Nous utilisons [swagger](https://github.com/swagger-api/swagger-codegen) qui crée un fichier yaml utilisant la spécification [OpenApi](https://www.openapis.org/).

_C'est une interface standard pour les API RESTful qui permet de comprendre les capacités du service sans accès au code source. ([https://swagger.io/specification/](https://swagger.io/specification/))._

Ensuite, nous générons des fichiers Typescript (contenant des objets et des API) à partir du fichier yaml original. Vous pouvez essayer leur générateur [ici](https://editor.swagger.io/).

**_ÉTAPE 1 :_** Mettez à jour votre node et npm vers les dernières versions. Nous avons utilisé npm 6.1 avec node 10.0. Vous pouvez les télécharger depuis [ici](https://nodejs.org/en/).

**_ÉTAPE 2_** : Mettez à jour votre fichier package.json en utilisant :

### Mise à jour de NgRx et refactorisation nécessaire

Il n'est pas obligatoire d'utiliser NgRx, mais je le recommande vivement. Si vous n'utilisez pas NgRx, vous pouvez passer à l'étape suivante.

> L'équipe NgRx a créé un guide de migration très utile [ici](https://github.com/ngrx/platform/blob/master/MIGRATION.md). Ils décrivent vraiment étape par étape les modifications nécessaires pour une migration réussie.

Dans la version 5, la propriété 'payload' dans l'interface Action a été supprimée car elle était une source de problèmes de sécurité de type.

L'équipe NgRx suggère de créer une nouvelle classe pour chaque action que vous avez, et de passer le payload en tant qu'entrée au constructeur de cette classe.

Nous avons décidé de faciliter la transition en créant notre propre interface Action appelée **_ActionWithPayload,_** qui étend l'interface Action régulière. ActionWithPayload étend la nouvelle interface, mais conserve l'ancien attribut payload.

Nous avons également remarqué que nous ne pouvons pas utiliser observable$.select et que nous devons l'envelopper avec l'opération 'pipe' :

### Correction des tests unitaires

Pour utiliser le nouveau mécanisme de store, vous devez créer une classe de store mockée :

Pour l'utiliser dans un test, faites ce qui suit :

Store sera une instance mockée de l'état fourni ! Nous pouvons simuler tous types d'états avec cela !

### Mots de la fin

Bien que cela puisse sembler intimidant au premier abord, les étapes que j'ai décrites sont simples et pas très compliquées. Si vous rencontrez des problèmes, n'hésitez pas à me contacter à l'adresse suivante : [_markgrichanik[at]gmail[dot]com_](mailto:markgrichanik@gmail.com).

J'aimerais également entendre vos retours lors de la mise à jour des applications Angular avec Swagger et NgRx.

> Si vous avez aimé cet article, ? pour que d'autres puissent le lire également.
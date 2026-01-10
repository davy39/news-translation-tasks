---
title: Comment tester vos microservices pour vous assurer qu'ils sont prêts pour la
  production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-20T07:54:00.000Z'
originalURL: https://freecodecamp.org/news/testing-microservices-are-they-production-ready-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/UiqRDTTd.png
tags:
- name: Microservices
  slug: microservices
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
- name: unit testing
  slug: unit-testing
seo_title: Comment tester vos microservices pour vous assurer qu'ils sont prêts pour
  la production
seo_desc: 'By Anton Lawrence

  Microservices architecture describes the practice of breaking up an application
  into a series of smaller and more problem-solution oriented components. Then each
  of these components communicates with one another across common protoc...'
---

Par Anton Lawrence

L'architecture des microservices décrit la pratique consistant à diviser une application en une série de composants plus petits et plus orientés vers la résolution de problèmes. Ensuite, chacun de ces composants communique avec les autres via des protocoles courants comme HTTP ou le plus léger TCP.

## **Vous vous demandez peut-être - les tests sont-ils importants pour moi ?**

**En bref - OUI.**  
  
Les tests logiciels sont importants pour un certain nombre de raisons, mais surtout :

* Cela économise de l'argent et beaucoup de temps
* Sécurité
* Qualité du produit (moins de bugs et d'erreurs)
* Satisfaction du client
* Cela vous permet de dormir paisiblement la nuit

Personne n'aime une application qui a des bugs et qui cesse de fonctionner sans raison. Et il n'est pas nécessaire de parler des dangers d'une mauvaise sécurité, qui permet aux pirates de voler des identifiants et même de l'argent.  
  
Tant que vous développez une application qui sera utilisée par des utilisateurs et qui a une certaine complexité, les tests ne devraient pas être une option - ils devraient être obligatoires.

## **Quels tests devrais-je écrire ?**

Il existe divers types de tests logiciels.  
  
**Les types de tests fonctionnels incluent :**

* Tests unitaires
* Tests d'intégration
* Tests de fumée
* Tests de régression
* Tests de sanity
* Tests bêta/acceptation
* Tests de bout en bout (e2e)

**Les types de tests non fonctionnels incluent :**

* Tests de performance
* Tests de charge
* Tests de stress
* Tests de sécurité
* Tests de conformité
* Tests d'utilisabilité

Plus l'application devient complexe, plus vous utiliserez de types de tests.

**Les tests de base que vous devriez toujours utiliser sont les suivants :**

* Tests unitaires
* Tests d'intégration
* Tests E2E combinés avec des tests de régression et des tests de sécurité

Le processus se déroule comme suit : d'abord, vous écrivez des tests pour vérifier si votre application se comporte comme prévu dans presque tous les aspects, y compris les cas particuliers. Ensuite, si votre application est déjà en ligne, vous écrivez des tests pour vérifier si des modifications apportées au code cassent la fonctionnalité actuelle.  
  
_Note de bas de page : en plus de ces tests de base que vous devriez utiliser pour tout type de logiciel, il existe des tests supplémentaires que vous devriez écrire pour les microservices. N'oubliez pas les tests de charge, par exemple, pour vérifier le comportement de votre système dans des conditions de charge normale et de pointe anticipée._

## **Moins de discours, plus de code**

Dans les exemples suivants, nous verrons comment nous pouvons implémenter ces types de base de tests logiciels ci-dessus dans un microservice. Le microservice utilise le protocole TCP pour la communication et est écrit en Node.js en utilisant le [Framework Nest](https://nestjs.com/).  
  
Si NestJS vous semble nouveau, ne vous inquiétez pas - tout ce que vous devez savoir est ce qui suit :

> "**Nest** est un framework pour construire des applications serveurs **Node.js** efficaces et évolutives.  
>   
> Il utilise le JavaScript moderne, est construit avec TypeScript (conserve la compatibilité avec le JavaScript pur) et combine des éléments de la POO (Programmation Orientée Objet), de la PF (Programmation Fonctionnelle) et de la PRF (Programmation Réactive Fonctionnelle).   
>   
> Sous le capot, Nest utilise [Express](https://expressjs.com/), mais offre également la compatibilité avec une large gamme d'autres bibliothèques, comme par exemple   
>   
> [Fastify](https://github.com/fastify/fastify), permettant une utilisation facile des nombreux plugins tiers disponibles." - _Description officielle du dépôt Github_

Pour cet exemple, nous utiliserons un module simple, nommé : **user**, avec une fonction simple **createUser**, qui créera un nouvel utilisateur dans notre base de données.  
  
La structure des dossiers pour le module ressemble à ceci :

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583005463519_folder-structure.PNG)

  
Nous avons un contrôleur qui écoute un message **create_user**. Après avoir effectué la validation avec le ValidationPipe, il appellera une fonction avec le même nom à l'intérieur de son service.

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583162403293_controller.png)

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583162684122_validation.png)

À l'intérieur du service, nous hachons le mot de passe de l'utilisateur. Ensuite, en utilisant TypeORM, nous sauvegardons un nouvel utilisateur dans notre base de données.

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583162552215_service.png)

  
Pour ce module, nous utilisons TypeORM comme ORM lié à la table User, et un autre module nommé **UtilsModule** dans lequel nous avons quelques fonctions d'assistance :

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583162768022_module.png)

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583163527010_entity.png)

## Tests unitaires

Une **unité** est la plus petite partie testable d'une application comme les fonctions, les classes ou les procédures. Les **tests unitaires** sont une méthode de test logiciel par laquelle des unités individuelles de code source sont testées pour déterminer si elles sont bonnes pour nous. 

En gros, les tests unitaires sont écrits pour s'assurer que chaque implémentation simple de différentes formes de code (fonctions, classes, etc.) répond à leur conception et à leurs exigences et se comporte comme prévu.  
  
Le but des [tests unitaires](https://codepad.co/blog/test-driven-development-writing-efficient-code-for-your-unit-tests/) est de séparer chaque partie du programme et de tester que les parties individuelles fonctionnent correctement.   
  
Cela signifie que les autres parties du code qui ne sont pas directement issues de l'unité de test (mais qui sont liées à celle-ci) seront simulées.  
  
Dans notre cas, la fonction que nous voulons tester (**createUser**) est notre unité que nous voulons tester. Cela signifie que nous devons l'isoler des autres composants. Nous devons donc simuler notre classe **user repository** qui représente le lien avec la base de données en utilisant **TypeORM**.  
  
Si nous analysons la fonction (celle du service), nous voyons qu'elle ne fait que hacher un mot de passe et ensuite sauvegarder un objet User dans notre base de données. Étant donné ce fait, nous écrivons la suite de tests suivante :

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583007348914_unit_test.png)

Tout d'abord, nous écrivons une fonction **beforeAll** qui crée notre module de test. Ensuite, nous remplaçons le dépôt original par notre classe simulée, qui ne retournera que l'objet que nous voulons sauvegarder dans la base de données.

Dans notre fonction, nous avions une exigence avec un cas particulier :

* créer un nouvel objet utilisateur avec certaines propriétés données (email, mot de passe), mais avec un mot de passe haché

Nous avons simulé la fonction **save()**, puisque c'est de TypeORM, en dehors de notre unité, et nous l'avons remplacée par une fonction simple qui retourne l'objet que nous avons passé.   
  
Donc, tout ce que nous avions à faire était de vérifier si nous envoyions l'objet avec la bonne propriété email et avec le bon hachage.

## Tests d'intégration

Les **tests d'intégration** sont une méthode de test logiciel par laquelle des unités de code source sont testées pour vérifier la fonctionnalité combinée.   
  
Les tests unitaires sont essentiellement écrits pour s'assurer que le code répond à sa conception et à ses exigences et se comporte comme prévu. Le but des tests d'intégration est de mélanger différents modules et de tester s'ils interagissent correctement.  
  
Donc maintenant, pour notre exemple, nous combinons notre **UserModule** avec le module TypeORM (dépendance) pour vérifier si l'utilisateur est sauvegardé dans la base de données.  
  
Nous avons à nouveau la même fonction que ci-dessus, mais cette fois avec le test suivant :

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583008813487_integration_test.png)

Cette fois, dans notre fonction **beforeAll**, nous ne simulons pas le **userRepository**. Au lieu de cela, nous utilisons l'original, et nous ajoutons notre **databaseModule** qui crée la connexion à notre base de données.  
  
En même temps, parce que nous utilisons une vraie base de données maintenant, nous devons écrire plusieurs fonctions qui prépareront notre base de données pour les tests.   
  
Nous devons vider la base de données avant et après nos tests, juste pour être sûr qu'elle est complètement vide.   
  
En même temps, nous devons fermer manuellement la connexion à celle-ci, afin de ne pas rester avec des gestionnaires ouverts après avoir terminé les tests.  
  
Avec les tests unitaires, nous avons vérifié si notre fonction fonctionnait comme prévu. Donc ici, tout ce que nous avons à faire est de tester si notre fonction se mélange avec la méthode **save()** de TypeORM et si notre utilisateur est stocké dans la base de données.  
  
Nous écrivons une fonction d'assistance nommée **getOneUserFromDb**, qui fait ce qu'elle dit faire. Ensuite, nous vérifions si l'email est correct ainsi que la propriété **accountConfimed**, qui a été définie dans la classe d'entité avec la valeur par défaut **false**.

## Tests de bout en bout

Les **[tests de bout en bout](https://itnext.io/end-to-end-testing-78033fb768a8)** sont une technique de test logiciel utilisée pour tester si le flux d'une application se déroule comme prévu du début à la fin.   
  
Nous effectuons ce type de test pour nous assurer que l'application fonctionnera comme prévu dans une situation réelle.  
  
Jusqu'à présent, nous avons testé si le mot de passe de l'utilisateur était haché correctement et si le mot de passe et l'email étaient sauvegardés dans la base de données.   
  
Maintenant, nous devons tester nos validations au niveau de la requête. Dans notre contrôleur, nous avons un pipe de validation qui teste la charge utile entrante pour vérifier si l'objet correspond à **CreateUserDto**.

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583163595607_validation.png)

Et les tests :

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583155804389_e2e.png)

Ici, nous avons testé pour voir ce qui se passerait si nous essayions de créer un utilisateur mais que nous n'envoyions pas l'objet complet ou que nous envoyions des propriétés dans un format incorrect.  
  
Ce sont quelques exemples des cas particuliers de notre fonction que nous avons testés en utilisant seulement 3 types de tests logiciels.

## Tests manuels vs automatisés

Jusqu'à présent, nous avons écrit nos tests manuellement - et pour ce cas, c'était parfait. Mais plus vous avez de code, plus vos suites de tests deviendront complexes et volumineuses.  
  
Par exemple, si vous allez tester un système d'authentification, vous devrez répliquer l'ensemble du comportement d'un utilisateur réel. Et vous devrez simuler les requêtes et les réponses, y compris les cookies et bien d'autres choses, juste pour construire l'environnement pour vos tests. Une longue suite de tests peut prendre beaucoup de temps à s'exécuter.  
  
Heureusement, vous avez une autre option en matière de tests : les outils automatisés. Ces outils ont des fonctionnalités intégrées pour vous permettre de simuler l'environnement entier pour vos tests, ce qui rend le processus de test beaucoup plus facile.   
  
Vous pouvez aller encore plus loin et utiliser des [outils de test automatisés d'API](https://www.loadmill.io/) pour votre application. Ce sont des outils qui viennent avec des options supplémentaires qui les rendent idéaux pour les tests de charge, les tests de régression et les rapports de données pour des situations réelles.   
  
De plus, ils ont une bonne interface utilisateur qui facilite grandement l'écriture des tests.

## Conclusion

Construire un logiciel prêt pour la production nécessite des tests. Et parfois, selon la complexité de l'application, ces tests peuvent devenir un goulot d'étranglement pour vous ou votre équipe.   
  
Dans ce cas, assurez-vous de séparer vos suites de tests par leur type, comme nous l'avons fait précédemment. Et ne testez que la fonctionnalité qui appartient au type de test actuel.   
  
Si cela ne suffit pas pour votre cas d'utilisation, ou si les tests sont trop difficiles à écrire et prennent trop de temps, alors vous pouvez utiliser des outils et des plateformes automatisés pour faciliter les choses.
---
title: Comment créer un modèle d'application avec Vert.x, VueJS et OAuth2 en cinq
  étapes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-25T21:45:50.000Z'
originalURL: https://freecodecamp.org/news/vert-x-vuejs-oauth2-in-5-steps-c04ee78475b7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bcIzB5Jcrcw25eIITJYsJg.png
tags:
- name: Java
  slug: java
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Comment créer un modèle d'application avec Vert.x, VueJS et OAuth2 en cinq
  étapes
seo_desc: 'By Thomas Reinecke

  In this tutorial you will learn how to setup an application boilerplate based on
  Vert.x (Java) as a backend and VueJs as a frontend with a focus on User Authentication
  against Keycloak through OAuth2. Once a User is logged in, the ...'
---

Par Thomas Reinecke

Dans ce tutoriel, vous apprendrez comment configurer un modèle d'application basé sur Vert.x (Java) comme backend et VueJS comme frontend, avec un focus sur l'authentification des utilisateurs contre Keycloak via OAuth2. Une fois qu'un utilisateur est connecté, l'application [**vertx-vue-keycloak**](https://github.com/vertx-stack/vertx-vue-keycloak) démontre également comment interroger le backend Vert.x, envoyer des données (mutations) et comment fonctionne le modèle Publish/Subscribe entre Vert.x et VueJS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*775YhFPwxnHVON-d1kYtTg.png)

Le code e2e pour cet article est hébergé sur GH [ici](https://github.com/vertx-stack/vertx-vue-keycloak).

### Étape 1 — Préparation

#### Installer KeyCloak

Dans cet exemple, nous allons utiliser Keycloak comme fournisseur de gestion d'authentification et d'autorisation. [Keycloak](https://www.keycloak.org/) est une solution open source d'identité et de gestion des accès offerte par RedHat, qui fournit OAuth2 et bien plus. Keycloak est livré avec une console d'administration Web pour administrer le serveur. Nous pouvons facilement l'exécuter basé sur docker :

```
docker run -d — name keycloak -p 38080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin -e KEYCLOAK_LOGLEVEL=DEBUG jboss/keycloak
```

Après avoir démarré ce conteneur, la console d'administration **Keycloak** sera disponible à l'adresse [http://127.0.0.1:38080](http://127.0.0.1:38080). Soyez conscient de la version de Keycloak — au moment où cet article a été écrit, c'était la **4.5.0.Final**, donc l'interface utilisateur peut sembler un peu différente avec des versions plus récentes ou antérieures.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rkUMZMj2ZcUhwgwrhpXbXw.png)

#### Créer les informations d'identification du client Keycloak

Pour l'application Vert.x que nous allons développer, nous avons besoin d'un client enregistré dans Keycloak. Remplissez le formulaire avec les valeurs mises en évidence :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vJ7I1kdx_pUX2p2Jmwe90A.png)

Enregistrez ceci, ouvrez et inspectez l'objet client **vertx-account** nouvellement créé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cDKLhjCJbC6rjI2MMsBa7A.png)

Nous reviendrons à cette page, en particulier les informations sur l'onglet **Credentials** plus tard lorsque nous intégrerons les détails du client dans le code vertx.

#### Créer des Rôles

Dans l'onglet Rôles de la barre latérale gauche dans Keycloak, créez deux rôles exemplaires **modify-account** et **view-account** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oX6B46F7Y6M_NMm-NvDJkg.png)

#### Créer un Utilisateur

Dans l'onglet Gérer les utilisateurs, créez un nouvel utilisateur, donnez-lui un nom d'utilisateur **testuser** et une adresse email **test@tester.com** et enregistrez-le :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UsN-3sfPvPYCpoISNFoqDA.png)

Toujours sur la page de l'utilisateur nouvellement créé, basculez vers l'onglet Credentials et définissez le mot de passe de cet utilisateur sur **test**. Désélectionnez également le commutateur **Temporary** et cliquez sur le bouton **Reset Password**. Soyez conscient : le comportement de cette interface utilisateur est un peu étrange. Lorsque vous cliquez sur ce bouton, le drapeau **Temporary** revient à vrai, mais ignorez simplement cela. Le mot de passe que vous avez donné devrait être bien défini.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OwG-b2hQHBJFmySnO0_iGg.png)

Basculez vers l'onglet Role Mapping et attribuez les rôles nouvellement créés **modify-account** et **view-account** à cet utilisateur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ln-lwh-TaTZzlTtwtwGStQ.png)

Cela complète la configuration de Keycloak. Félicitations ! Nous sommes maintenant prêts à travailler sur notre backend vert.x et notre frontend VueJS.

Plus de détails sur la configuration de Keycloak et sa configuration pour Vert.x peuvent être trouvés dans [cet excellent article](https://piotrminkowski.wordpress.com/2017/09/15/building-secure-apis-with-vert-x-and-oauth2/), que j'ai également utilisé comme source pour les instructions ci-dessus (merci à Piotr Minkowski).

### Étape 2 — Créer le Backend Vert.x et le Frontend VueJs

J'ai utilisé Eclipse pour créer un projet Maven simple (sans sélection d'archétype) et à partir de là, j'ai ajouté vertx à la liste des dépendances dans _pom.xml_. Au moment où cet article a été écrit, vertx était en version 3.5.4.

Clonez le dépôt suivant (y compris le code source pour cet article) :

[**vertx-stack/vertx-vue-keycloak**](https://github.com/vertx-stack/vertx-vue-keycloak)
[_Contribuez au développement de vertx-stack/vertx-vue-keycloak en créant un compte sur GitHub._github.com](https://github.com/vertx-stack/vertx-vue-keycloak)

```
git clone https://github.com/vertx-stack/vertx-vue-keycloak.git
```

#### Créer un fichier Keystore

Vous pouvez suivre la procédure que vous jugez appropriée pour créer une chaîne de certificats appropriée et la convertir au format jks. L'exemple que je donne ici est basé sur un certificat auto-signé et il fonctionne très bien en local ou pour les environnements de test. Le dépôt que vous venez de cloner contient le fichier, vous pouvez donc sauter cette section. Pour la production, veuillez obtenir un certificat signé par une autorité de certification (un certificat gratuit, par exemple, de [LetsEncrypt](https://letsencrypt.org/)).

Exécutez la commande OpenSSL suivante pour générer votre clé privée et votre certificat public. Utilisez « **testpassword** » comme mot de passe et laissez toutes les valeurs par défaut (appuyez sur entrée jusqu'à ce que vous ayez terminé) :

```
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
```

Examinez le fichier de certificat :

```
openssl x509 -text -noout -in cert.pem
```

Combinez votre clé et votre certificat dans un bundle PKCS#12 (P12), et comme mot de passe d'exportation, utilisez à nouveau « **testpassword** » :

```
openssl pkcs12 -inkey key.pem -in cert.pem -export -out certificate.p12
```

Convertissez-le en un fichier JKS. Utilisez « **testpassword** » comme mot de passe du keystore de destination :

```
keytool -importkeystore -srckeystore certificate.p12 -srcstoretype pkcs12 -destkeystore test.jks -deststoretype jks
```

Nous avons maintenant notre magasin de certificats dans test.jks, prêt à être utilisé par vert.x pour sécuriser une connexion HTTPS. Ce fichier est également inclus dans le dépôt que vous venez de cloner.

#### Comprendre l'application vertx-vue-keycloak

![Image](https://cdn-media-1.freecodecamp.org/images/1*075b-eAX9emp_XlWQvpTKg.png)

L'application contient à la fois les codes source vertx pour le backend et le code frontend basé sur VueJS.

Dans le **Backend** (src/main/java), le **MainVerticle.java** est le point d'entrée principal. C'est un verticle Vertx qui crée le serveur HTTP/HTTPS, configure les différentes routes, expose le point de terminaison /login qui s'intègre avec Keycloak, et fournit enfin les points de terminaison de l'API pour notre frontend.

Le Frontend (placé dans src/main/frontend) est un frontend VueJS régulier qui a été créé avec le CLI VueJS. Il contient les assets, les bibliothèques et les composants.

### Étape 3 — Intégration avec KeyCloak

Ouvrez src/main/java/backend/MainVerticle.java et inspectez la méthode **createHttpServerAndRoutes** :

```
JsonObject keycloakJson = new JsonObject()  .put("realm", "master")   .put("realm-public-key", "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqZeGGDeEHmmUN4/UXh2gQD0yZEZirprsrdYK7GfcE1+QF9yfYfBrIv5cQUssFQKISVpbbLcoqYolsxcOvDyVFSQedHRsumOzqNZK38RHkidPMPrSNof5C3iMIHuXOCv/6exnLZvVoeYmkq42davYEz1tpSWzkZnlUMbRZFs1CfzLMM2rsAJWsO1/5zbDm0JhFl7EFUsTki72ihac1Q5zUUSFyf1jKUEkL7rrkYINjgAaQKktE8pnubc3Y44F5llY4YyU9/bqUWqMYDx868oiDcnoBpGGd4QrUMlbULZZLRqqUKK6iG1kHxDCJQ9gaCiJoELyAqXjnnO28OODQhxMHQIDAQAB")     .put("auth-server-url", "http://127.0.0.1:38080/auth")  .put("ssl-required", "external")  .put("resource", "vertx-account")  .put("credentials", new JsonObject()    . put("secret", "0c22e587-2ccb-4dd3-b017-5ff6a903891b")); 
```

```
OAuth2Auth oauth2 = KeycloakAuth.create(vertx, OAuth2FlowType.PASSWORD, keycloakJson);
```

Obtenez le **realm** et la **real-public-key** depuis la console d'administration Keycloak. Pour obtenir la clé, cliquez sur le bouton « Public Key » dans l'onglet **Keys** du **master** realm :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kV2D7ULMc3mULzT8cknPUg.png)

En tant que ressource, incluez le client **vertx-account** précédemment créé. Pour ses informations d'identification, naviguez vers celui-ci dans le menu Clients > vertx-account > onglet Credentials et copiez le Secret depuis là :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cT1QhkYcbt3L9T_v41bTyg.png)

En tant que OAuth2FlowType, nous allons sélectionner PASSWORD, représentant le **Password Credentials Flow**. Plus de détails sur les OAuthFlows peuvent être trouvés [ici](https://vertx.io/docs/vertx-auth-oauth2/java/).

Nous sommes maintenant en mesure de définir la route **/login** pour gérer la connexion réelle :

Nous pouvons maintenant exécuter notre premier test du backend vertx en démarrant le lanceur vert.x. En utilisant Postman, nous pouvons maintenant exécuter la première authentification utilisateur via un POST contre **127.0.0.1:8080/login** (notre serveur vertx avec la route **/login**). Dans le Body, nous sélectionnons les données brutes et entrons l'objet JSON suivant :

```
{  "username":"testuser",   "password":"test",   "scope":"modify-account view-account"}
```

Appuyez sur **Send** dans Postman et envoyez ceci à notre serveur vertx :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uSCums5-I5HlHEt0d76NBw.png)

Le résultat sur le serveur ressemblera à ceci, indiquant que nous avons trouvé avec succès l'utilisateur « **testuser** » sur Keycloak. Bon travail !

![Image](https://cdn-media-1.freecodecamp.org/images/1*fSNZf5x45PwH0QPs8p5nYw.png)

#### Authentification avec notre Frontend

Maintenant que nous avons l'authentification de base qui fonctionne et que nous l'avons testée avec Postman, il est temps d'intégrer notre application Frontend avec celle-ci. Le Frontend se trouve dans **src/main/frontend**. Pour le démarrer, exécutez une installation rapide des dépendances avec **yarn** et enfin démarrez-le avec **yarn dev**. Plus de détails [ici](https://github.com/vertx-stack/vertx-vue-keycloak).

Le Frontend démarrera maintenant sur **localhost:8081**. Il présentera une page de connexion assez simple (bootstrap a été utilisé pour la styliser) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*sUnQjpRfDUo5YtnERMpTTg.png)

Je ne vais pas entrer dans tous les détails spécifiques de cette application ici. Pour de nombreux détails sur la façon dont cela a été créé, veuillez consulter [cet excellent article](https://paweljw.github.io/2017/09/vue.js-front-end-app-part-3-authentication/) de [Pawe2 J. Wal](https://www.freecodecamp.org/news/vert-x-vuejs-oauth2-in-5-steps-c04ee78475b7/undefined).

La seule chose supplémentaire que nous devons changer est de configurer CORS sur le côté backend Vert.x pour nous assurer que le Frontend peut communiquer avec lui.

Vous êtes maintenant prêt à authentifier un utilisateur depuis l'application Frontend VueJS vers votre backend Vert.x. La connexion avec votre **testuser:test** vous permet d'accéder à l'espace protégé de votre application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gWu5FC3-6UVVwp0_0YaBSA.png)

Félicitations, vous avez maintenant une méthode assez élégante pour vous connecter à une application VueJS, fonctionnant contre une API Vert.x et un serveur d'authentification intégré à Keycloak.

### Étape 4 — Intégrer la logique de requête et de mise à jour des données

Nous allons implémenter un système de gestion de messages très simple ici comme exemple, qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ohG2OZCp5u3-FecF6GKAA.png)

Le frontend et les pièces de l'intégration de l'eventbus dans cet exemple ont été inspirés par le projet [_vertx-examples_](https://github.com/parzonka/vertx-examples) de [Mateusz Parzonka](https://www.freecodecamp.org/news/vert-x-vuejs-oauth2-in-5-steps-c04ee78475b7/undefined) sur GitHub — merci pour cela !

La procédure proposée dans cet exemple est d'utiliser des points de terminaison de messages standard, des producteurs et des consommateurs sur le Vertx EventBus pour un modèle de communication Client/Serveur entièrement sophistiqué incluant des requêtes, des mutations de données et publish/subscribe. L'idée est assez simple :

* sur le backend, nous exposons un certain nombre de consommateurs de messages qui agissent comme des méthodes get, create et delete.
* sur le frontend, nous nous abonnons à des canaux de données spécifiques qui nous permettent d'envoyer n'importe quoi depuis le backend vers le frontend, ce qui aide également grandement à faire passer la communication client à client par le backend.

Du côté Frontend, nous allons créer un service vertx eventbus qui utilise [**vertx3-eventbus-client**](https://www.npmjs.com/package/vertx3-eventbus-client). Les méthodes essentielles ici sont **callApi** et **subscribe** (pour plus de détails sur pubsub, voir l'étape 5) :

Pour obtenir, supprimer et créer un nouveau message, inspectez le composant Home.vue, en particulier l'utilisation du service **eventbus** depuis utils/eventbus :

En résultat, vous êtes maintenant capable d'utiliser cette interface utilisateur pour recevoir le tableau des messages connus depuis le backend, créer de nouveaux messages et les supprimer. Jusque-là, tout va bien, mais attendez une minute : qu'est-ce qui se passe réellement pour les autres clients qui utilisent la même application en parallèle à moi ? Plongeons enfin dans PubSub...

### Étape 5 — Intégrer Publish & Subscribe

Nous avons déjà vu que le backend publie le tableau complet des messages sur le Vertx EventBus chaque fois qu'une mise à jour est effectuée (ce qui est un peu excessif, mais acceptons cela pour cet exemple). Comment le frontend peut-il finalement capturer ces mises à jour ?

Heureusement, le Vertx EventBus (qui est basé sur SockJS) nous permet de souscrire des clients à des canaux qui peuvent être alimentés par n'importe quel autre client (communication c2c) ou également depuis le serveur.

Notre service eventBus fournit une fonction pour **souscrire** à un tel canal (voir le code ci-dessus). Cela est à nouveau utilisé sur le composant Home.vue pour capturer les changements sur le tableau de messages et sur le nombre de connexions que le serveur vertx gère de la manière suivante :

Ici, nous capturons les messages provenant des canaux **:pubsub/connections** et **:pubsub/messages** et nous poussons les données entrantes dans le frontend. Cela permet de garder plusieurs navigateurs qui exécutent la même application parfaitement synchronisés via le Vertx EventBus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rA8whChtm8U_o080Ue1dog.png)

### Limitations

L'une des plus grandes limitations de cet exemple est la configuration du backend vertx. En particulier, la sécurité sur le vertx Eventbus n'est pas encore configurée, puisque nous ne vérifions pas si l'utilisateur qui appelle l'API est réellement authentifié sur le backend. Donc, ne pas utiliser ce code pour des applications de production sans travailler sur cela.

Un autre aspect est que l'EventBus et également le gestionnaire /login sur le Backend fonctionnent toujours sur HTTP. Le code de redirection vers HTTPS qui est en place ne concerne que les ressources statiques, pas encore l'EventBus autant que je l'ai testé avec un temps limité. Je suppose que puisque nous ne servons pas vraiment de contenu HTML statique via vertx, il serait logique de désactiver complètement le serveur HTTP et de ne fonctionner qu'avec HTTPS.

Enfin, le certificat HTTPS était auto-signé et certainement vous ne voulez pas utiliser cela pour une utilisation sérieuse en dehors de localhost. Obtenez un certificat signé par une autorité de certification (par exemple, de LetsEncrypt) et continuez à partir de là.

Autrement dit : bon vertx'ing !

Si vous avez besoin d'OAuth basé sur Google au lieu de Keycloak, consultez
[Google OAuth2 avec VueJS et Vert.x](https://medium.com/@thomas.reinecke/google-oauth2-with-vuejs-and-vert-x-6c9d9e617bf)
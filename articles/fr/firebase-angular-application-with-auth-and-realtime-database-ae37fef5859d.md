---
title: Comment créer une application Firebase Angular avec authentification et une
  base de données en temps réel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-16T13:35:39.000Z'
originalURL: https://freecodecamp.org/news/firebase-angular-application-with-auth-and-realtime-database-ae37fef5859d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8-shYpRp-eIefsxUs0_iKA.jpeg
tags:
- name: Angular
  slug: angular
- name: authentication
  slug: authentication
- name: crypto
  slug: crypto
- name: data
  slug: data
- name: 'tech '
  slug: tech
seo_title: Comment créer une application Firebase Angular avec authentification et
  une base de données en temps réel
seo_desc: 'By Zdravko Kolev

  For a long time, I was looking for a good Portfolio web app that can help me to
  easily track my Cryptocurrency profits/losses until I’ve decided to develop such
  on my own with the help of Firebase and Angular! Yes, it’s that easy, le...'
---

Par Zdravko Kolev

Pendant longtemps, j'ai cherché une bonne application web de Portfolio qui pourrait m'aider à suivre facilement mes profits/pertes en cryptomonnaies jusqu'à ce que je décide de [développer une telle application](https://igniteui.github.io/crypto-portfolio-app/) moi-même avec l'aide de **Firebase et Angular** ! Oui, c'est aussi simple, laissez-moi vous expliquer pourquoi.

**Firebase** offre les outils parfaits pour les applications avec authentification utilisateur et stockage de [base de données en temps réel](https://firebase.google.com/docs/database/). Il fournit une [documentation](https://firebase.google.com/docs/) riche avec une variété d'exemples de développement pour aider chacun à mieux comprendre comment créer des applications exceptionnelles.

J'ai couvert le démarrage de l'application **Angular**, en utilisant [Ignite UI CLI](https://www.infragistics.com/products/ignite-ui-angular/getting-started), dans un autre [article de blog](https://www.infragistics.com/community/blogs/b/infragistics/posts/easily-create-your-first-ignite-ui-for-angular-application).

**Cet article vise à :**

* Passer par l'installation et la configuration de Firebase.
* Configurer l'authentification Firebase.
* Implémenter le stockage et la synchronisation de la [base de données en temps réel](https://firebase.google.com/docs/database/).
* Ajouter des services de données Observable.
* [Visualiser les données dans une application Angular](https://www.infragistics.com/products/ignite-ui-angular).

### Configurer un compte Firebase

Je veux passer par les étapes que nous avons suivies pour configurer le compte Firebase du Portfolio. Les projets sont créés à partir de la [console Firebase](https://console.firebase.google.com/) en choisissant **Ajouter un nouveau projet**. Une fois le formulaire **Créer un projet** soumis, vous verrez l'aperçu suivant du projet.

![Image](https://cdn-media-1.freecodecamp.org/images/NasIpLrw4HFk-0GPRJgygDdFbFUJFCyj3ZlC)
_Aperçu du projet Firebase_

Dans la section Aperçu du projet, vous pouvez trouver tous les outils de développement utilisés pour l'authentification et le stockage des données. C'est également là que se trouve la configuration utilisée dans l'application web Portfolio. Cette configuration est générée en appuyant sur **Ajouter Firebase à votre application web**, et elle est ensuite ajoutée au fichier **app.module.ts** de l'application.

Revenons à la barre latérale de gauche et sélectionnons **Authentification**. À partir de là, nous avons accès aux **méthodes de connexion** dont nous avons besoin dans l'application. Accédez à l'onglet Connexion, où vous pouvez voir les fournisseurs activés et utilisés dans l'application Portfolio — **Google, Facebook et le fournisseur Email/Mot de passe**.

Les fournisseurs de connexion permettent aux utilisateurs de s'authentifier avec Firebase en utilisant leurs comptes Facebook et Google en intégrant leurs connexions dans l'application. Quant au fournisseur Email/mot de passe, il représente un mécanisme d'authentification simple en utilisant uniquement l'email et le mot de passe. **Firebase Auth** fournit des règles de validation intégrées vérifiant les entrées de l'utilisateur, donc nous n'avons pas besoin de configurer quelque chose d'additionnel ici.

![Image](https://cdn-media-1.freecodecamp.org/images/tLYYAMF7mIhAghwLl17dLrIc1pPLXFLtQxbX)

La partie la plus "tricky" ici était la configuration du fournisseur Facebook car nous avions besoin d'une **application Facebook** pour authentifier la connexion. Nous avons créé une application FB à partir de [Facebook Developers](https://developers.facebook.com/) qui nous a fourni l'ID de l'application et le secret de l'application demandés par Firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/BM7Zm2-pKYb1f2W1dpeA9Kxh7qfJVAtRvHEj)

Les **ID d'API** et **Secret** doivent être remplis lors de l'activation du fournisseur Facebook. Quant à l'**URI de redirection Auth** (à partir de la fenêtre du fournisseur), elle doit être collée sous `Facebook/Connexion Facebook/Section Produits/URI de redirection Auth valides`.

Continuons avec la console Firebase. À partir de la page de vue de la base de données, nous avons créé une **base de données en temps réel**.

![Image](https://cdn-media-1.freecodecamp.org/images/7nr-cSrLC1cCSldefkhHzdMjK5MVrp1gjJeF)
_Vue de la base de données Firebase_

Dans cette vue, nous pouvons trouver des informations sur les éléments de données de l'application et les règles de sécurité d'écriture/lecture. Voici les règles utilisées par l'application Portfolio :

```
{  "rules": {    "items": {      "$uid": {        ".read": "$uid === auth.uid",        ".write": "$uid === auth.uid"      }    }  }}
```

> Cette configuration de règle de sécurité permettra uniquement aux utilisateurs authentifiés de pouvoir lire et écrire dans notre base de données. Si vous souhaitez apprendre à définir des règles plus avancées, je vous recommande vivement de consulter la section [Sécurité et règles officielles](https://firebase.google.com/docs/database/security/).

D'accord, où en étions-nous ? Maintenant que nous avons passé par la création du compte **Firebase Portfolio**, voyons comment le **projet de développement Firebase** a été créé.

Si nous n'avions pas déjà un projet créé, j'aurais recommandé de commencer par installer le [CLI Firebase](https://firebase.google.com/docs/cli/), qui fournit une variété d'outils pour gérer et déployer des projets Firebase. MAIS nous avons démarré le [Projet Angular Portfolio](https://www.infragistics.com/community/blogs/b/infragistics/posts/easily-create-your-first-ignite-ui-for-angular-application) avec Ignite UI CLI, donc nous avions juste besoin d'installer **AngularFire** et **Firebase** depuis **npm**. Nous avons besoin des deux packages pour communiquer avec Firebase. **AngularFire** est la bibliothèque officielle pour le développement Firebase et Angular.

```
npm install firebase @angular/fire --save
```

Tous les modules AngularFire utilisés dans l'application sont ajoutés dans le fichier `app.module.ts` :

* **FirestoreModule** est nécessaire pour les fonctionnalités de base de données comme travailler avec des collections, des requêtes et des services pour le streaming et la manipulation de données.
* **FireAuthModule** est nécessaire pour les fonctionnalités d'authentification comme la surveillance de l'état d'authentification, les fournisseurs de connexion et la sécurité.
* **FireDatabaseModule** nous permet de travailler avec des bases de données en temps réel. C'est très efficace pour les applications mobiles et web qui nécessitent des états synchronisés entre les clients en temps réel.

> Le seul module commun qui n'est pas utilisé dans l'application Portfolio est **AngularFireStorageModule**. Vous pouvez utiliser ce module pour stocker et servir rapidement et facilement du contenu généré par les utilisateurs comme des photos et des vidéos ainsi que pour surveiller les téléchargements et les métadonnées associées aux fichiers.

Maintenant que nous savons comment l'application a été configurée initialement, nous pouvons jeter un coup d'œil aux autres **fonctionnalités Firebase** qui sont utilisées.

### Authentification

Nous utilisons le service `AngularFireAuth` pour surveiller l'état d'authentification de l'application. `AngularFireAuth.auth` retourne une instance initialisée de `firebase.auth.Auth`, nous permettant de connecter et déconnecter les utilisateurs. L'application démontre les capacités de connexion en utilisant trois fournisseurs : Facebook, Google et Email.

L'instance utilisateur Firebase est conservée pour chaque fournisseur lié à l'utilisateur, et lorsqu'un utilisateur est enregistré ou se connecte, cet utilisateur devient l'utilisateur actuel de l'instance Auth. L'instance conserve l'état de l'utilisateur afin que le rafraîchissement de la page ou le redémarrage de l'application ne perde pas les informations de l'utilisateur.

Nous utilisons la méthode `signInWithRedirect` pour les fournisseurs Facebook et Google, afin de nous connecter en redirigeant vers la page de connexion. La [création de compte basée sur un mot de passe](https://firebase.google.com/docs/auth/web/password-auth) est utilisée pour le fournisseur de connexion par email, `createUserWithEmailAndPassword` et `signInWithEmailAndPassword` sont les méthodes responsables de la création de compte utilisateur et de la connexion.

![Image](https://cdn-media-1.freecodecamp.org/images/Un3vsdL0fp6UFYRhxs7LJxUamWku00-0zOdc)
_Vue du compte basé sur un mot de passe_

Je recommande la documentation officielle de Firebase pour plus d'informations détaillées sur l'[authentification](https://firebase.google.com/docs/auth/) et le [cycle de vie de l'utilisateur](https://firebase.google.com/docs/auth/users#the_user_lifecycle).

### Actions de la base de données en temps réel

Firebase offre deux solutions de base de données basées sur le cloud et accessibles par le client, et nous utilisons la base de données originale de Firebase — Realtime. Consultez les différences entre **Realtime** et **Cloud Firestore** sur la page de [documentation officielle](https://firebase.google.com/docs/firestore/rtdb-vs-firestore).

Les services `AngularFireDatabase` et `AngularFireList` sont utilisés dans l'application Portfolio pour récupérer, sauvegarder et supprimer des données facilement.

`AngularFireDatabase` peut être injecté via le constructeur d'un composant ou d'un service `@Injectable()`. Dans notre cas, nous utilisons la [deuxième approche](https://github.com/IgniteUI/crypto-portfolio-app/blob/master/src/app/services/block-item.service.ts#L13) :

Les données sont récupérées via le service `AngularFireDatabase`, qui remplit une liste Observable de `BlockItems`. `AngularFire` fournit des méthodes comme `snapshotChanges()` qui retourne un Observable de données sous forme de tableau synchronisé. C'est très pratique si vous souhaitez limiter les actions d'événement, comme _ajouté_, _modifié_, _supprimé_ et _déplacé_. Par défaut, il écoute les quatre, cependant, vous ne pouvez être intéressé que par l'un de ces événements et vous pouvez spécifier celui que vous souhaitez utiliser. Dans notre application, nous sommes abonnés à tous.

L'ajout d'un nouvel élément, la mise à jour d'un élément existant ou sa suppression de la liste est réalisé en utilisant les méthodes `push()`, `update()` et `remove()`.

Chaque méthode d'opération de données retourne une promesse, bien que nous n'ayons pas besoin d'utiliser la promesse de complétion pour indiquer le succès car la base de données en temps réel maintient la liste synchronisée.

### Observables

#### Service CoinItem

Le service API Cryptocompare gère les données asynchrones et émet plusieurs valeurs à la fois avec des `Observables`. Nous utilisons la méthode `[HttpClient get(](https://angular.io/guide/http))` pour demander les données depuis [la ressource](http://min-api.cryptocompare.com/) et nous y abonnons, afin de les transformer en tableau Observable d'objets `CoinItem`, qui seront utilisés plus tard par nos composants `igxGrid`, `igxList` et `igxCard`.

Rx.js nous permet de mettre en cache le résultat de la requête HTTP. Nous récupérons ces données initialement, les mettons en cache et utilisons la version mise en cache pendant la durée de vie de l'application. La combinaison de `publishReply(1, 300000)` et `refCount()` fait ce qui suit.

> **publishReply(1, 300000)** indique à Rx de mettre en cache la dernière valeur émise et de rester valide pendant 5 minutes. Après ce temps, il invalidera le cache.

> **refCount()** indique à Rx de maintenir l'Observable en vie tant qu'il y a des abonnés.

Maintenant, après nous être abonnés à la liste des pièces, le résultat sera mis en cache, et nous n'aurons pas besoin de faire une autre requête HTTP.

#### Service BlockItem

Les données des pièces de cryptomonnaie du Portfolio sont assurées par la méthode `getItemsList()` qui retourne un tableau Observable `BlockItem` auquel le composant `igxGrid` est abonné. Seuls les utilisateurs authentifiés peuvent utiliser ce service en raison de l'`AngularFireList` que nous manipulons, qui est associé à des identifiants utilisateur uniques.

### Visualiser les données

Pour la visualisation, nous utilisons des composants UI de la bibliothèque [Ignite UI pour Angular](https://github.com/IgniteUI/igniteui-angular). Ces composants sont responsables de la gestion des données tout en fournissant l'accès à des modèles personnalisés et à des mises à jour en temps réel, avec une API intuitive, en utilisant une quantité minimale de code.

#### igxGrid

La liaison de propriété `[data]` des [grilles](https://www.infragistics.com/products/ignite-ui-angular/angular/components/grid.html) est utilisée pour passer le tableau `BlockItem` retourné. Chaque `<igx-column>` représente un champ de l'objet et est utilisé pour définir des fonctionnalités comme l'édition et le tri. Les colonnes sont modifiables, et avec l'aide des [pipes Angular](https://angular.io/guide/pipes), nous pouvons déclarer facilement des transformations de valeur d'affichage. Nous utilisons un pipe décimal pour changer le nombre minimum de chiffres entiers avant le point décimal.

Le composant fournit des gestionnaires d'événements et une API simples pour les opérations CRUD. Des gestionnaires comme `updateRow` et `deleteRow` implémentent une logique supplémentaire comme la manipulation de `AngularFireList` et la logique de restauration des éléments de pièce avec le `igxSnackbar`.

#### igxCard

Les [cartes](https://www.infragistics.com/products/ignite-ui-angular/angular/components/card.html) sont utilisées pour fournir des informations générales sur les pièces de cryptomonnaie en utilisant la disposition [Flexbox layout](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). Ces composants de carte peuvent être filtrés avec la directive `igxFilter`, qui peut être utilisée pour filtrer différentes sources de données. `igxFilter` peut être appliqué comme un pipe ou comme une directive.

#### igxFinancialChart

[Le graphique](https://www.infragistics.com/products/ignite-ui-angular/angular/components/financialchart.html) offre plusieurs façons de visualiser et d'interpréter les données, une fois qu'elles sont retournées par le service. Il existe plusieurs modes d'affichage pour le prix et le volume, et dans notre cas, nous utilisons `chartType="candle"`.

Le composant de graphique financier analyse et sélectionne automatiquement les colonnes de données :
- Colonne `Date/Heure` à utiliser pour l'`axe des x`
- Colonnes `Open`, `High`, `Low`, `Close`, `Volume` ou les cinq premières colonnes numériques pour l'`axe des y`

#### Thème

IgniteUI pour Angular base ses conceptions de composants sur les [Principes de conception Material](https://material.io/design/introduction/#principles) et avec seulement quelques lignes de code, nous pouvons facilement changer les couleurs, les tailles, la typographie et l'apparence générale de nos composants.

Maintenant que nous avons fourni toutes les définitions de base nécessaires pour le `igx-theme`, et avons configuré le mixin `igx-dark-theme`, nous devons simplement appliquer les classes CSS `.light-theme` et `.dark-theme` à un niveau racine d'élément DOM et les basculer lors d'un clic sur un bouton.

### Résultat

![Image](https://cdn-media-1.freecodecamp.org/images/ns6nmMPedTwr0gun8UGBjLC9fISpowsz74Ek)

### Conclusion

Tout est possible avec les bons outils. Nous avons créé une application web de Portfolio en utilisant toute la puissance du Framework Angular, les services d'authentification Firebase et le stockage/synchronisation de la base de données Cloud.

Vous pouvez trouver le [dépôt GitHub](https://github.com/IgniteUI/crypto-portfolio-app) et l'application de portfolio [elle-même](https://igniteui.github.io/crypto-portfolio-app/) ici.

N'hésitez pas à partager dans les commentaires ci-dessous toutes les questions que vous avez, suggestions sur ce qui peut être amélioré ou changé dans l'application, ou tout problème que vous avez rencontré lors de la configuration de votre compte Firebase ou de votre application.
---
title: Permettez-moi de vous présenter Swift networking avec Siesta — ma nouvelle
  bibliothèque préférée.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T20:47:47.000Z'
originalURL: https://freecodecamp.org/news/swift-networking-with-siesta-5b5e7089bd8f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YAavX2qseMIP_llujYfguA.png
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Permettez-moi de vous présenter Swift networking avec Siesta — ma nouvelle
  bibliothèque préférée.
seo_desc: 'By Nikolay Derkach

  Today I’d like to tell you about my new favorite iOS networking library called Siesta.
  “What’s so great about it, and why can’t I just use Alamofire?” you might ask. Actually,
  you can use Alamofire with Siesta! Because it’s a netwo...'
---

Par Nikolay Derkach

Aujourd'hui, je voudrais vous parler de ma nouvelle bibliothèque préférée pour le networking iOS appelée [Siesta](https://github.com/bustoutsolutions/siesta). « Qu'est-ce qu'elle a de si génial, et pourquoi ne puis-je pas simplement utiliser Alamofire ? » pourriez-vous demander. En fait, vous pouvez utiliser Alamofire avec Siesta ! Parce que c'est une couche d'abstraction de networking au-dessus des clients HTTP.

Mais contrairement à des bibliothèques comme [Moya](https://github.com/Moya/Moya), celle-ci ne cache pas HTTP. Cela vous offre un excellent compromis, et c'est exactement ainsi que j'aime consommer mes APIs REST.

En adoptant une approche centrée sur les ressources, plutôt que sur les requêtes, Siesta fournit un **modèle observable à l'échelle de l'application de l'état d'une ressource RESTful**.

Que signifie cela ? Cela signifie éviter les requêtes réseau inutiles et la désérialisation redondante des réponses. Cela découple les contrôleurs de vue des cycles de vie des requêtes réseau. Cela fournit une analyse transparente des réponses dès la sortie de la boîte. [Et bien plus encore.](https://github.com/bustoutsolutions/siesta)

Dans ce tutoriel, je voudrais vous montrer comment commencer avec cette merveille et rendre votre networking à nouveau génial, rapidement ?

### Installation

Installez-le depuis Cocoapods :

```
pod 'Siesta', '~> 1.0'
```

Pour les besoins de ce tutoriel, j'ai construit une [application CRUD simple](https://github.com/nderkach/cashman) avec une API REST et une authentification basée sur JWT que j'ai [déployée sur Heroku](https://jwt-api-siesta.herokuapp.com).

Pour commencer, créez une classe séparée pour votre API. Appelons-la `AwesomeAPI.swift`

Définissons une configuration de base pour l'API ici :

Ici, nous définissons un singleton global pour notre API. Nous configurons le service avec l'URL de notre API et `standardTransformers` qui sont des analyseurs par défaut pour les réponses texte et image. Nous activons également la journalisation en mode débogage, ce qui est très utile pour déboguer les requêtes contre votre API. Enfin, nous définissons notre premier _accès de ressource_, une méthode publique de notre classe API retournant une ressource que nous allons maintenant utiliser dans notre contrôleur de vue.

Pour récupérer les données de notre ressource nouvellement définie, nous devons créer un _observateur de ressource_ dans notre contrôleur de vue :

Ici, nous ajoutons un _observateur de ressource_ à notre ressource `ping`, et définissons une méthode de délégué qui est appelée lorsque l'état de la ressource change. Un état peut changer lorsqu'un observateur est ajouté ou lorsqu'il a de nouvelles données, par exemple.

Parce que Siesta vous permet de découpler la configuration de la requête de l'initialisation de la requête, vous pouvez demander une ressource sans vous soucier des détails fastidieux de la manière dont elle serait demandée.

Par exemple, vous n'avez pas besoin de vous soucier trop souvent de `loadIfNeeded`, puisque Siesta vous permet d'éviter les requêtes redondantes. Le temps d'expiration par défaut pour une ressource est de 30 secondes et est configurable.

Maintenant, si vous exécutez votre application, vous devriez voir quelque chose comme ceci :

```
Siesta:network        │ GET https://jwt-api-siesta.herokuapp.com/ping
```

```
Siesta:network        │ Response:  200 ← GET https://jwt-api-siesta.herokuapp.com/ping
```

```
pong
```

### Transformateurs

Faisons quelque chose de plus amusant. Définissons quelques _transformateurs_ qui décoderaient automatiquement notre réponse JSON brute en un modèle de données.

Dans notre API, nous avons un endpoint `/status` qui retourne

```
{  "text": "ok"}
```

Pour décoder le JSON sur le backend, nous allons utiliser [JSONDecoder](https://developer.apple.com/documentation/foundation/jsondecoder), un ajout récent à Swift 4.

Tout d'abord, nous allons ajouter un transformateur comme ceci :

`[String: String]` signifie que nous attendons un dictionnaire de mappage chaîne à chaîne dans notre réponse JSON.

Ensuite, nous devons mettre à jour notre contrôleur de vue avec l'observateur de ressource.

Comme vous l'avez remarqué ici, pour décoder le JSON, nous utilisons `typedContent()` lors du déballage de l'optionnel. Dans ce cas, nous devons fournir explicitement un type de données (`[String: String]`) sinon le type de données ne peut pas être inféré. De même, nous pouvons réécrire l'observateur de ressource précédent pour l'endpoint `/ping` comme ceci :

### Authentification

Dans notre API, nous avons quelques endpoints authentifiés : `/incomes` et `/expenses`. Pour y accéder, nous devons d'abord obtenir un jeton JWT. Définissons une méthode pour authentifier les requêtes. Cette fois, au lieu de créer une fonction qui retourne une _Resource_, nous allons en faire une qui retourne un `Request`. Ce serait une façon de gérer tout ce qui n'est pas des requêtes _GET_ sur votre API.

Tout d'abord, nous allons ajouter une propriété de classe, qui stockera le jeton d'authentification JWT :

Chaque fois que cette propriété est définie, nous voulons invalider notre configuration de service afin que la prochaine fois qu'une ressource est récupérée, les en-têtes de requête soient actualisées. Cela est nécessaire car vous enverrez probablement votre jeton d'authentification soit dans un cookie, soit dans l'en-tête _Authorization_.

Envisagez également de stocker votre jeton d'authentification dans le Keychain, plutôt que dans `NSUserDefaults` ou un autre stockage non sécurisé. Nous utilisons ici la bibliothèque JWTDecode pour décoder un jeton JWT et obtenir sa date d'expiration.

Après cela, nous voulons également actualiser automatiquement le jeton une fois qu'il expire. Dans une implémentation plus sophistiquée de JWT, nous obtiendrions un _refresh token_ en même temps, que nous utiliserions plus tard pour actualiser notre jeton d'authentification. Dans notre cas, nous avons une implémentation simple de JWT, et nous allons simplement renvoyer la réponse de connexion.

Voici comment vous pouvez implémenter la requête de connexion dans votre classe _AwesomeAPI_ pour obtenir un jeton d'authentification :

Ici, nous envoyons un POST à `/login` avec les identifiants de l'utilisateur dans une charge utile JSON. Nous définissons également deux fermetures : `onSuccess` et `OnFailure` et nous stockons un jeton d'authentification lors d'une authentification réussie.

Enfin, nous voulons mettre à jour automatiquement notre jeton d'authentification _avant_ qu'il n'expire. Nous pouvons utiliser un minuteur à déclenchement unique pour cela :

Oui, les identifiants de connexion réels pour notre API de test sont _test_ et _test_. Vous pouvez facilement intégrer l'appel `AwesomeAPI.login()` dans votre flux de connexion en obtenant les identifiants d'un contrôleur de vue responsable de la connexion. Pour décoder avec succès la réponse de la requête de connexion, vous devez également définir un transformateur pour celle-ci :

L'API nous demande de passer le jeton JWT dans l'en-tête _Authorization_. Pour ce faire, nous pouvons ajouter ce qui suit à notre configuration de service (`init()` ) :

Maintenant que notre requête est authentifiée, essayons de faire quelques requêtes vers des ressources authentifiées, comme `/expenses`. Cet endpoint retourne une liste de dictionnaires suivants :

```
{    "amount": -50.0,    "created_at": "2017-12-07T16:00:52.988245",    "description": "pizza",    "type": "TransactionType.EXPENSE"}
```

Notre objectif est de créer un modèle pour stocker la réponse de ce format. Créons une classe appelée _Expense_. Comme nous utilisons _JSONDecoder_ ici, nous devons simplement faire hériter notre classe de _Codable_ :

L'énumération _CodingKeys_ nous permet de mapper les noms de champs dans notre réponse JSON aux noms de propriétés de la struct. Notez que nous décodons également les dates ici (`createdAt`). Puisque notre date a un format personnalisé, nous devons configurer cela via la stratégie `dateDecodingStrategy` de _JSONDecoder_ :

Enfin, créons un transformateur pour cette classe :

Nous utilisons `[Expense]` ici car nous attendons un tableau d'objets _Expense_.

Après avoir défini un accès de ressource `expenses()` de la même manière que précédemment, nous pouvons récupérer notre ressource authentifiée comme ceci :

### Une dernière chose...

Une dernière chose que je veux vous montrer est ce qu'il faut faire lorsque votre jeton d'authentification expire. Ce que nous pourrions faire avec Siesta, par exemple, est de nous authentifier automatiquement et de réessayer une requête échouée.

Tout d'abord, nous devons ajouter ce qui suit à notre configuration :

Ensuite, nous enchaînons notre requête et la répétons avec un nouveau jeton !

Si vous souhaitez consulter le projet final, il est disponible sur [Github](https://github.com/nderkach/AwesomeAPI).

Bon codage !
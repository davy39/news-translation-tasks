---
title: Comment utiliser Firebase pour créer des jeux Android multijoueurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-10T22:16:35.000Z'
originalURL: https://freecodecamp.org/news/match-making-with-firebase-hashnode-de9161e2b6a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cUxtuiNpwNevTBxw3oAY4g.png
tags:
- name: android app development
  slug: android-app-development
- name: Firebase
  slug: firebase
- name: gaming
  slug: gaming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment utiliser Firebase pour créer des jeux Android multijoueurs
seo_desc: 'By Shukant Pal

  Have you just built your board game for Android? Want to get it online? You are
  in the right place — let’s build it together!


  We are going to implement match-making with the Firebase Realtime Database in this
  article. For that, you ne...'
---

Par Shukant Pal

Venez-vous de créer votre jeu de société pour Android ? Vous voulez le mettre en ligne ? Vous êtes au bon endroit — construisons-le ensemble !

![Image](https://cdn-media-1.freecodecamp.org/images/1*cUxtuiNpwNevTBxw3oAY4g.png)

Nous allons implémenter la mise en relation avec la base de données Firebase Realtime Database dans cet article. Pour cela, vous avez besoin de Firebase configuré dans votre projet Android — voyez comment faire [ici](https://firebase.google.com/docs/database/android/start).

### Prérequis

* **Utilisateurs Firebase** — ici, nous supposons que vous avez pu connecter votre utilisateur à Firebase en utilisant n'importe quelle méthode. Cela est nécessaire pour identifier avec qui communiquer après la mise en relation.
* **Dépendances Gradle** — Ajoutez ces dépendances au bloc `dependencies` dans le fichier grade de votre module d'application.

```
implementation 'com.google.firebase:firebase-core:16.0.6' implementation 'com.google.firebase:firebase-auth:16.1.0' implementation 'com.google.firebase:firebase-database:16.0.6'
```

* Vous n'avez pas terminé après avoir implémenté la mise en relation. C'est parce que vous n'avez trouvé que deux joueurs qui vont jouer — mais vous n'avez pas implémenté comment leurs mouvements vont se propager sur le réseau.

### Notre modèle

Nous allons utiliser un nœud dans la base de données Firebase appelé la salle de jeu qui stockera tous les défis actifs que les utilisateurs ont poussés. Chaque utilisateur recherchera les défis existants dans la salle de jeu et acceptera le premier trouvé. Sinon, l'utilisateur téléchargera son propre défi et attendra qu'un autre utilisateur l'accepte.

Vous pourrez ajouter plus de fonctionnalités à votre implémentation de mise en relation, comme la correspondance basée sur des classements de performance similaires, des amis, des biais régionaux, etc.

### Comment allons-nous implémenter cela ?

J'ai divisé notre problème en trois objets :

* **Matcher** : Trouve les correspondances existantes dans la salle de jeu.
* **SelfChallengeManager** : Gère le défi qu'un utilisateur télécharge si Matcher ne trouve rien.
* **SelfChallengeCanceller** : Annule le processus de mise en relation si cet utilisateur ne veut plus jouer.

De plus, nous aurons besoin d'un objet « Challenge » qui a deux propriétés — la référence du nœud de communication et l'ID de l'utilisateur du défi (comprenez maintenant pourquoi nous devons nous connecter à Firebase ?). Cet objet sera téléchargé dans la salle de jeu par `SelfChallengeManager`.

### Écrire nos composants d'abord

Avant d'écrire nos trois composants, nous devons comprendre ce qu'est une [transaction](https://firebase.google.com/docs/database/android/read-and-write#save_data_as_transactions) Firebase. Nous ne voulons pas que deux utilisateurs acceptent le même défi en même temps — ce qui corromprait notre base de données et rendrait nos précieux utilisateurs furieux. Les transactions viennent à la rescousse en empêchant les opérations concurrentes sur un nœud dans la base de données (qui sera la salle de jeu).

Comment cela se rapporte-t-il à nos composants ? — Nos composants seront modélisés comme des transactions en tant que classes internes dans notre classe 'FirebasePlayerMatchMaker'.

[https://gist.github.com/SukantPal/2c1f5daedfaee784bfeb622d4e26736e](https://gist.github.com/SukantPal/2c1f5daedfaee784bfeb622d4e26736e)

Nous utilisons deux interfaces de rappel — `OnMatchMadeCallback` et `OnFailCallback` en interne. La méthode de fabrique prend un `OnMatchMadeCallback` qui est appelé chaque fois qu'une correspondance est établie. Le `OnFailCallback` est invoqué chaque fois que **MatchMaker** ne parvient pas à trouver une correspondance.

Ici, `findMatch` s'exécute sur un thread séparé et crée un `OnFailCallback` si `Matcher` ne trouve pas de correspondance. Dans ce cas, nous devons créer un `SelfChallengeManager` et l'exécuter en tant que transaction.

1. **Matcher**

Ici, la méthode `doTransaction()` parcourt tous les enfants du nœud de la salle de jeu et recherche un `Challenge` compatible pour notre utilisateur. Par défaut, `isChallengeCompat` retourne `true`, mais vous pouvez changer cela en ajoutant des contraintes supplémentaires comme les classements. Le premier défi compatible est ensuite stocké et le nœud de défi est supprimé (en définissant la valeur sur `null`) dans la base de données. Notez qu'en supprimant le nœud, l'autre joueur sera notifié de l'acceptation.

2. **SelfChallengeManager**

Ici, la méthode `doTransaction` ajoute un nœud enfant au nœud `GAME_RECORD` dans notre base de données. C'est là que les mouvements du jeu seront communiqués après la mise en relation. Il télécharge ensuite un `Challenge` dans la salle de jeu et s'ajoute en tant que `ValueEventListener`. Chaque fois qu'un autre utilisateur accepte la demande, ils supprimeront ce nœud et cet utilisateur sera notifié car nous écoutons.

3. **SelfChallengeCanceller**

Notre code supprime simplement le nœud créé par `SelfChallengeManager` en parcourant toute la salle de jeu et en trouvant notre défi. MAIS C'EST INCOMPLET !! Vous devriez (optionnellement) ajouter une fonctionnalité où cet utilisateur abandonne automatiquement le jeu si la correspondance a déjà été acceptée.

Dans le `OnMatchMadeCallback` que vous fournissez à `FirebasePlayerMatchMaker.newInstance`, vous devez initialiser la communication du jeu à effectuer dans le nœud (par chemin) `mGamePath`.

Yo, vous l'avez fait. Merci d'avoir lu !

_Publié à l'origine sur [hashnode.com](https://hashnode.com/post/match-making-with-firebase-cjrzgoi6k0010ads2xqojc7a1)._
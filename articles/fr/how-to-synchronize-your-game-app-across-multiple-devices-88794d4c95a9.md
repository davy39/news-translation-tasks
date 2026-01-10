---
title: Comment synchroniser votre application de jeu sur plusieurs appareils
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T17:16:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-synchronize-your-game-app-across-multiple-devices-88794d4c95a9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*vLBlhBeBsItUgjMR
tags:
- name: android app development
  slug: android-app-development
- name: communication
  slug: communication
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment synchroniser votre application de jeu sur plusieurs appareils
seo_desc: 'By Shukant Pal

  If you’re having problems with online game synchronization, you’re in the right
  place!


  _Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">rawpixel on <a h...'
---

Par Shukant Pal

Si vous avez des problèmes avec la synchronisation de jeux en ligne, vous êtes au bon endroit !

![Image](https://cdn-media-1.freecodecamp.org/images/0*vLBlhBeBsItUgjMR)
_Photo par [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

À leur niveau le plus bas, les jeux typiques peuvent être décomposés en étapes simples effectuées par chaque joueur — elles sont appelées tours, et à chaque tour, un mouvement se produit. Il n'est pas nécessaire que les joueurs aient un tour à la fois, ou fassent un seul mouvement à la fois. Pour synchroniser votre application de jeu sur plusieurs appareils en ligne, vous devez être capable de décomposer votre jeu en ces petites étapes.

### Notre Modèle

Dans cet article, nous prenons un simple jeu de société générique pour deux joueurs. Avant de faire quoi que ce soit, nous avons besoin de deux joueurs, n'est-ce pas ?

Pour configurer cela, vous devez implémenter une fonctionnalité appelée matchmaking, où vous avez un nœud commun dans votre FirebaseDatabase où chaque joueur peut poster son défi. Le défi posté contient l'UID du défieur et une autre référence à un nœud de mouvements où les mouvements seront publiés. Si vous ne l'avez pas fait ou si vous avez des problèmes à l'implémenter, lisez cet article sur le [matchmaking](https://medium.com/@sukantk3.4/match-making-with-firebase-hashnode-de9161e2b6a7).

Une fois que les deux joueurs ont accès au nœud de mouvements, un joueur doit poster son premier mouvement, puis le deuxième, puis le premier et ainsi de suite. Nous utiliserons le `ChildEventListener` de Firebase pour recevoir les mouvements postés par l'adversaire.

### Plongez plus profondément dans le code

En gros, nous avons deux choses à faire : envoyer un mouvement et recevoir un mouvement. Notre composant `FirebaseGameSynchronizer` fera exactement cela, mais **l'interprétation du mouvement sera faite par le `Modulator` que vous implémentez.**

Le **mover** envoie son mouvement en utilisant `sendMoveMsg`. Vous pouvez encoder votre mouvement de diverses manières. Par exemple, si une pièce est déplacée de (a,b) à (c,d), alors encodez le mouvement comme le nombre `abcd`. Je recommanderais définitivement cette méthode si la taille de votre échantillon (ou si c'est un jeu de société, la taille du plateau) est inférieure à 10.

`sendMoveMsg` télécharge essentiellement le mouvement vers le nœud de mouvements `mMovesRecordList` et s'attend à ce que l'autre joueur l'écoute.

Une fois le mouvement publié, les deux joueurs reçoivent le mouvement. Attendez une minute… Vous ne voulez pas que le mover reçoive le mouvement — parce que vous avez peut-être déjà effectué le mouvement de leur côté, et vous ne voulez pas le faire deux fois.

J'ai donc ajouté une fonctionnalité sympa (si vous voulez que les deux joueurs reçoivent le mouvement, supprimez simplement toutes les références à `mSelfMoveSoph`) : le sémaphore des mouvements personnels. Chaque fois que `sendMoveMsg` est appelé, il incrémente `mSelfMoveSoph`. Nous savons combien de mouvements nous avons téléchargés maintenant avec ce sémaphore.

`onChildAdded` est appelé chaque fois qu'un mouvement est ajouté par Firebase. Il ignore le mouvement si le sémaphore a une valeur ; sinon, le `mMessageModulator` est appelé pour interpréter le mouvement et le montrer à votre utilisateur. `Modulator` est une interface fonctionnelle qui est le complément de votre encodeur de mouvement en chaîne. Il prend cette chaîne téléchargée sur Firebase et la convertit en mouvement.

### **Attendez, cela ne fonctionnera pas si l'utilisateur reçoit un appel**

Oui, si l'utilisateur reçoit un appel et que votre application est fermée… comment l'utilisateur pourra-t-il revenir à jouer ?

Encore une fois, faisons un `Modulator` comme ceci :

```
public class GenericGameFragment implements FirebaseGameSynchronizer.Modulator {
```

```
    public void onMoveReceived(boolean isSyncingPast, String encodedMsg) {       // ... faire le mouvement, l'afficher sur l'UI .....
```

```
    }
```

```
}
```

Maintenant, deux mauvaises choses vont se produire :

1. Si l'utilisateur quitte, `FirebaseGameSynchronizer` restera attaché au nœud qui l'écoute. C'est une fuite de mémoire + d'utilisation du CPU.
2. `FirebaseGameSynchronizer` aura une référence à votre fragment — regardez simplement, Modulator doit mettre à jour l'UI et a une référence à `GenericGameFragment`.

### Synchronisation et désynchronisation avec le nœud de mouvements

J'ai utilisé une solution relativement simple pour le problème. C'est une combinaison de deux choses :

1. **Drapeau de synchronisation :** Lorsque vous définissez la propriété de synchronisation, `FirebaseGameSynchronizer` appellera le modulateur, sinon, il stockera le mouvement dans un tampon. En définissant à nouveau le drapeau de synchronisation, il libère d'abord les mouvements dans son tampon.
2. **Attachement :** Le modulateur est supprimé chaque fois que la méthode `onStop` du fragment et défini à nouveau lors du `onStart` du fragment.

Avant d'utiliser ce nouveau synchroniseur, n'oubliez pas d'appeler `startSync()`. Dans `onStop`, appelez `stopSync` et dans `onResume`, appelez à nouveau `startSync`. Maintenant, vous devez appeler `detachModulator` et `flush` dans `onDestroy`.

Consultez ce lien pour l'implémentation complète : [Gist FirebaseGameSynchronization](https://gist.github.com/SukantPal/bf90b4aa7b6859cf54b0133a0abd2594).

Lectures complémentaires :

* [Firebase Match Maker — Comment utiliser Firebase pour créer des jeux multijoueurs Android ?](https://medium.freecodecamp.org/match-making-with-firebase-hashnode-de9161e2b6a7)
* [Disposition personnalisée pour les jeux de société — BoardLayout!!!](https://medium.com/@sukantk3.4/custom-layout-for-board-games-in-android-ab6d1a321ff6)
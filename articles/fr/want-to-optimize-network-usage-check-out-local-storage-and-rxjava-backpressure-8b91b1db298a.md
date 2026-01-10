---
title: Voulez-vous optimiser l'utilisation du réseau ? Découvrez le stockage local
  et la contre-pression RxJava
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-03T14:32:18.000Z'
originalURL: https://freecodecamp.org/news/want-to-optimize-network-usage-check-out-local-storage-and-rxjava-backpressure-8b91b1db298a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*acDn76XOMsf80_bNbtHnAQ.jpeg
tags:
- name: Android
  slug: android
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Voulez-vous optimiser l'utilisation du réseau ? Découvrez le stockage local
  et la contre-pression RxJava
seo_desc: 'By Nikita Kozlov

  Users love fast, responsive apps. They don’t want to hear how API calls take time.
  They want to see updates immediately. Right now. Once you meet that expectation,
  users start interacting with the app more and more. It’s so easy for ...'
---

Par Nikita Kozlov

Les utilisateurs adorent les applications rapides et réactives. Ils ne veulent pas entendre que les appels API prennent du temps. Ils veulent voir les mises à jour immédiatement. Tout de suite. Une fois que vous répondez à cette attente, les utilisateurs commencent à interagir de plus en plus avec l'application. C'est si facile pour eux, puisque l'application répond immédiatement.

Avec tout cet impact positif sur l'entreprise vient une utilisation accrue du réseau et de la batterie. Il est donc dans l'intérêt de tous de minimiser le nombre d'appels réseau.

Dans cet article, je vais partager comment un tel cas a été résolu en utilisant RxJava.

Pour le rendre plus intéressant, j'ai ajouté un défi optionnel ainsi que la solution. [L'une des branches](https://github.com/NikitaKozlov/Switchman/tree/challenge) du dépôt ne contient que quelques classes de base et un ensemble de tests d'acceptation. Avant de lire la solution, vous pouvez essayer de résoudre le problème par vous-même en faisant passer ces tests. Vous trouverez plus d'informations dans la section « Défi » ci-dessous.

### Le Problème

La tâche consiste à développer une fonctionnalité qui permet aux utilisateurs d'ajouter et de supprimer des éléments d'une certaine liste. La liste est stockée sur le back-end. De nombreuses applications sont confrontées à ce problème d'une manière ou d'une autre : marquer un e-mail comme important dans Gmail, ajouter une chanson à vos favoris sur Spotify, ou recommander un article ici, sur Medium (?).

![Image](https://cdn-media-1.freecodecamp.org/images/nzmj9fLTzEF19NGwqGAwgkGM3i8hw77kdeUE)

Le problème semble simple, mais il devient plus délicat lorsque des éléments comme la latence de connexion et les erreurs réseau sont pris en compte.

L'implémentation doit satisfaire les exigences suivantes :

* **L'interface utilisateur réagit immédiatement aux actions de l'utilisateur.** Les utilisateurs veulent voir les résultats de leurs actions immédiatement. Si nous ne pouvons pas synchroniser ces changements, nous devons notifier nos utilisateurs et revenir à l'état précédent.
* **L'interaction depuis plusieurs appareils est supportée.** Cela ne signifie pas que nous devons supporter les changements en temps réel — mais nous devons récupérer la collection entière de temps en temps. De plus, notre back-end nous fournit des points de terminaison API pour les ajouts et les suppressions, que nous devons utiliser pour supporter une meilleure synchronisation.
* **L'intégrité des données est garantie.** Chaque fois qu'un appel de synchronisation échoue, notre application doit récupérer gracieusement de cette erreur.

Les décisions architecturales sont discutées dans un article séparé : « [Comment tirer parti du stockage local pour construire des applications ultra-rapides](https://medium.freecodecamp.com/how-leverage-local-storage-to-build-lightning-fast-apps-4e8218134e0c) ». Cet article est axé sur l'optimisation du nombre d'appels au back-end en utilisant RxJava.

#### Définition formelle

Nous devons développer l'interface suivante :

```
interface ItemRepository {    Single<List<? extends Item<ItemId>>> getItemList();
```

```
    Single<Response> addItem(ItemId id);
```

```
    Single<Response> removeItem(ItemId id);
```

```
    Observable<Integer> getCounter();
```

```
    boolean hasItem(ItemId id);}
```

Les méthodes `addItem()` et `removeItem()` peuvent être appelées dans n'importe quel ordre avec n'importe quels arguments. Pour éviter de passer des informations inutiles, les deux méthodes n'ont besoin que de `ItemId`, tandis que `getItemList()` retourne des éléments complets.

Veuillez prendre en compte que `getCounter()` retourne un `Observable` qui émet un nombre d'éléments dans la collection chaque fois qu'un changement se produit dans le `ItemRepository`. Cela signifie que, par exemple, nous augmentons le compteur chaque fois qu'un nouvel élément est ajouté, même si la synchronisation avec le back-end n'est pas encore terminée.

L'API back-end est la suivante :

```
public interface Api {    Single<List<? extends Item<ItemId>>> getItemList();
```

```
    Single<ApiResponse> addItem(ItemId id);
```

```
    Single<ApiResponse> removeItem(ItemId id);}
```

Nous pouvons ajouter ou supprimer des éléments par leurs ID et récupérer la collection entière.

### Défi

Afin de le rendre plus intéressant, voici le défi promis. Il est, bien sûr, optionnel, donc vous pouvez passer directement à la section « Solution » si vous préférez.

Inspiré par l'article « [Practical Challenges For RxJava Learners](https://medium.com/proandroiddev/practical-challenges-for-rxjava-learners-1821c454de9) » de Sergii Zhuk, j'ai décidé de créer une [branche](https://github.com/NikitaKozlov/Switchman/tree/challenge) séparée avec seulement des classes de base et des tests d'acceptation. Vous pouvez les faire passer par vous-même et ensuite comparer votre solution avec la mienne. Au total, il y a 29 tests. Ils sont divisés en quatre parties selon la fonctionnalité couverte :

1. **Récupération** : Récupération de la liste depuis l'API et vérification de son contenu.
2. **Ajout et suppression** : Vérification que les méthodes API appropriées sont appelées et que l'état du dépôt est modifié en conséquence.
3. **Changements de compteur** : Certains écrans affichent le nombre total d'éléments dans la liste. Cette fonctionnalité est testée dans cette partie.
4. **Optimisation des appels back-end** : Même si l'utilisateur peut ajouter/supprimer un seul élément autant de fois qu'il le souhaite, le réseau ne doit pas être surchargé.

Il existe plus d'une façon d'optimiser les appels back-end. Donc, au cas où vous ne seriez pas sûr des tests, consultez la section « Stratégie d'optimisation ».

### Solution

Pour résoudre ce problème, j'ai décidé de construire le `ItemRepository` de la manière suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/-uP2T9VUACoHWPNnVPPP3DGQWtr6WZgrOLOo)

En plus d'une copie locale de la liste principale, le stockage local a deux listes supplémentaires : une pour les ajouts en cours, et une pour les suppressions en cours. Elles aident à récupérer les cas négatifs. Pour en savoir plus, veuillez consulter l'article suivant : [Comment tirer parti du stockage local pour construire des applications ultra-rapides](https://medium.freecodecamp.com/how-leverage-local-storage-to-build-lightning-fast-apps-4e8218134e0c).

#### Stratégie d'optimisation

Nous ne devons pas lancer toutes les requêtes vers le back-end en même temps. Par exemple, si vous ajoutez et supprimez le même élément simultanément, le résultat est imprévisible. Nous ne savons pas quelle requête serait la première à se terminer. Donc, les opérations sur un seul élément doivent être mises en file d'attente et lancées une par une. Les requêtes qui traitent d'éléments différents peuvent être exécutées en parallèle sans problème.

![Image](https://cdn-media-1.freecodecamp.org/images/iLW7hfvl99VDGLOheLB7TAfVtg4JxVsFWN7v)
_Regroupement des événements en files d'attente par ID. Les événements au sein d'une seule file d'attente doivent être traités consécutivement. Différentes files d'attente peuvent être traitées en parallèle._

Les files d'attente sont exécutées en parallèle. Chaque file d'attente se compose de requêtes pour ajouter et supprimer un élément particulier. Examinons l'une d'entre elles.

![Image](https://cdn-media-1.freecodecamp.org/images/3F1IA6nOPQt6V1RWE7tKUEsX1touY9Kv40tu)
_Les événements au milieu n'affectent pas l'état du résultat, nous pouvons donc les ignorer._

Les requêtes les plus importantes sont les dernières à arriver et la dernière requête qui a été lancée. Si elles sont identiques — par exemple, elles sont toutes les deux « add » — alors nous pouvons ignorer toute la file d'attente et ne rien faire. Si elles sont différentes, alors une fois la requête actuelle terminée, vous pouvez lancer la dernière et ignorer tout ce qui se trouve au milieu.

De plus, `ItemRepository` doit commencer à se synchroniser avec le back-end, sans aucun délai artificiel, dès qu'il a de nouvelles données. La mise en mémoire tampon et le traitement par lots peuvent être utilisés pour améliorer davantage cette solution, mais cela dépasse le cadre de cet article. Je le mentionne ici pour que vous ne soyez pas surpris par le comportement de la solution.

#### Voici RxJava

RxJava fournit des mécanismes puissants pour manipuler les flux de données. Utilisons-les à notre avantage.

Tout d'abord, créons des événements qui représentent l'intention de l'utilisateur : `Add` et `Remove`. Maintenant, en utilisant `Subject` ou `[Relay](https://github.com/JakeWharton/RxRelay)`, nous pouvons créer un flux d'entrée de ces événements.

Deuxièmement, nous allons implémenter des files d'attente en divisant ce flux en plusieurs sous-flux d'événements regroupés par le même `itemId`. Pour ce faire, nous pouvons utiliser l'opérateur `groupBy` qui retourne un `Observable` de `GroupedObservable`. Chaque `GroupedObservable` est une file d'attente de la stratégie d'optimisation.

![Image](https://cdn-media-1.freecodecamp.org/images/I9p5HRdR0tQ-yeXhJvkS7NxKd0RoFi4A6I7-)
_Diagramme de marbres de l'opérateur « groupBy ». « ItemId » est représenté par la forme de chaque marbre._

Nous ne voulons qu'aucun de ces sous-flux ne se termine. Mais si quelque chose d'inattendu se produit, nous voulons être sûrs que les données continueront à circuler quoi qu'il arrive. Et l'opérateur `groupBy` peut nous aider avec cela. Si l'un des `GroupedObservable` est terminé, peut-être à cause d'une erreur, un nouveau est créé lorsqu'un événement avec un `itemId` correspondant est dans le flux.

Après cette étape, nous avons un ensemble de sous-flux que nous allons optimiser indépendamment.

#### Optimisation

La troisième et dernière étape est l'optimisation. Avant de commencer, vérifions une fois de plus la stratégie d'optimisation. Elle dit que nous devons conserver l'événement le plus récent ainsi que le dernier qui a réellement provoqué un appel réseau. Nous pouvons supprimer tous les événements du milieu ! Ils ne comptent tout simplement **pas**.

Malheureusement, nous ne savons pas combien de temps chaque requête back-end prend ou à quelle fréquence un nouvel événement est émis. Cela signifie que nous ne pouvons pas utiliser `window`, `buffer`, `throttle` ou `debounce` pour implémenter le comportement requis. Pour utiliser ceux-ci, nous devons connaître le timing à l'avance.

Nous avons besoin que chaque `GroupedObservable` émette un nouvel événement uniquement lorsqu'un appel en cours est terminé. En d'autres termes, une fois l'appel terminé, nous devons demander à `GroupedObservable` d'émettre un nouvel élément. Cela peut être fait en utilisant la contre-pression réactive. Nous devons donc créer l'opérateur `onBackpressureLatest(Subscriber)`. Il supprime tous les événements sauf le dernier qui est émis uniquement lorsque la méthode `Subscriber.request()` est appelée.

![Image](https://cdn-media-1.freecodecamp.org/images/CpSJaBXcV3Tv151T3egRBu2MMrIfSA8Wx5r6)
_À chaque appel « request(1) », le dernier élément est émis. C'est exactement ce dont nous avons besoin._

Maintenant, faisons l'appel back-end dans le `Subscriber` pour qu'il sache quand appeler `request()`. Il peut également gérer la comparaison entre les événements. S'ils sont identiques, il ignore le dernier. Sinon, il lance un appel au back-end. Le résultat est posté dans le flux de sortie.

Les méthodes `ItemRepository.addItem()` et `ItemRepository.removeItem()` retournent `Single`, nous devons donc filtrer ce flux pour livrer les réponses appropriées à chacun des appelants de notre API.

### Le troisième état de la requête

Indépendamment de l'ignorance des requêtes ou de leur exécution, les consommateurs de `ItemRepository` s'attendent à recevoir des réponses. Cela signifie que même si certaines requêtes sont ignorées, nous devons toujours retourner autant de réponses que d'appels pour `addItem()` et `removeItem()` sont faits. Il y a deux façons de gérer cela.

Tout d'abord, nous pourrions cacher toutes les optimisations au consommateur et agir comme si toutes les requêtes avaient été exécutées. Cela est bon pour l'encapsulation, car après avoir effectué des optimisations, vous n'avez pas besoin de changer le code des consommateurs.

Mais dans certains cas, cela signifie plus de complexité. Par exemple, si nous affichons un snackbar pour chaque réponse, et que l'utilisateur final a cliqué plusieurs fois pour ajouter et supprimer le même élément, nous allons le spammer avec des notifications. Pour résoudre ce problème, nous devons implémenter une logique pour gérer de tels cas.

Ou nous pourrions opter pour la deuxième approche. Nous pourrions être honnêtes avec les consommateurs de notre API et ajouter un troisième état « skipped » à la réponse. D'après mon expérience, je peux dire que cela simplifie les choses. Dans l'exemple ci-dessus, nous n'afficherions tout simplement pas de notifications pour toutes les requêtes ignorées.

### Temps de codage

En pseudo-code, cela semble plus simple que cela ne paraît :

Passons en revue les parties les plus importantes :

* Ligne 1 : Nous avons regroupé `inputStream` par ID et obtenu nos sous-flux.
* Ligne 3 : Nous avons appliqué la contre-pression. Tout sauf le dernier événement est ignoré à cette étape.
* Ligne 6 : Selon l'événement, nous l'ignorons et retournons la réponse ignorée, ou nous lançons un appel réseau et le sauvegardons pour une comparaison future.

Veuillez noter que le code ci-dessus ne compilera pas. Vous pouvez trouver le code réel et une petite application Android pour jouer dans [le dépôt](https://github.com/NikitaKozlov/Switchman).

### Conclusion

Même une tâche de routine comme l'ajout et la suppression d'éléments dans une collection devient un défi lorsqu'il s'agit d'optimisation, de synchronisation et d'une excellente expérience utilisateur. De bons outils, comme RxJava, peuvent nous aider à garder le code concis et expressif.

Vous pouvez trouver ma solution [ici](https://github.com/NikitaKozlov/Switchman) dans le module `switchman`. Avec celle-ci, dans le module `app`, vous pouvez trouver une application exemple pour jouer. Si vous êtes intéressé par un défi, consultez la branche « challenge » — les tests sont dans le module `switchman`. Pour plus d'informations, consultez la section « Show me the code » dans le README.

[**Nikita Kozlov (@Nikita_E_Kozlov) | Twitter**](https://twitter.com/Nikita_E_Kozlov)  
[_The latest Tweets from Nikita Kozlov (@Nikita_E_Kozlov): https://t.co/wmGSJ7snW1"_twitter.com](https://twitter.com/Nikita_E_Kozlov)

_Merci pour le temps que vous avez consacré à la lecture de cet article. Si vous l'aimez, n'oubliez pas de cliquer sur le_ ? _ci-dessous._
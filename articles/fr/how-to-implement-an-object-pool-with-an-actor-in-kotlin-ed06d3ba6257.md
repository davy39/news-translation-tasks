---
title: Comment implémenter un Object-Pool avec un Actor en Kotlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T19:33:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-an-object-pool-with-an-actor-in-kotlin-ed06d3ba6257
coverImage: https://cdn-media-1.freecodecamp.org/images/0*0aDugHie8xlGjhOZ
tags:
- name: actor model
  slug: actor-model
- name: concurrency
  slug: concurrency
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
seo_title: Comment implémenter un Object-Pool avec un Actor en Kotlin
seo_desc: 'By osha1

  We use object pool in jasync-sql to manage connections to the database. In this
  post, I will share how it is done in a performant, lock-free manner using Kotlin
  coroutines with an Actor.

  An object pool has a very simple API to work with. It ...'
---

Par osha1

Nous utilisons un pool d'objets dans [jasync-sql](https://github.com/jasync-sql/jasync-sql) pour gérer les connexions à la base de données. Dans cet article, je vais partager comment cela est fait de manière performante et sans verrouillage en utilisant les coroutines Kotlin avec un Actor.

Un pool d'objets a une API très simple à utiliser. Il s'agit d'un pool d'objets avec deux méthodes : `take()` et `return()`.

À première vue, cela semble être un problème très simple. Le principal défi ici est qu'il doit être à la fois performant et thread-safe, et c'est ce qui le rend intéressant et délicat à implémenter.

### Mais hey ! Pourquoi avons-nous besoin d'un pool d'objets de toute façon ?

[jasync-sql](https://github.com/jasync-sql/jasync-sql) est une bibliothèque pour accéder aux bases de données relationnelles comme MySQL et PostgreSQL. Les connexions à la base de données sont un excellent exemple de la nécessité des pools d'objets. L'accès à la base de données est effectué en obtenant une connexion à partir d'un **Connection-Pool**, en l'utilisant et en la retournant au pool.

Avec un pool de connexions, nous obtenons plusieurs avantages par rapport à la création de connexions pour chaque requête SQL :

* _Réutilisation des connexions_ — puisque le surcoût de l'initiation d'une connexion à la base de données est élevé (handshake, etc.), les pools de connexions permettent de garder les connexions actives, réduisant ainsi ce surcoût.
* _Limitation des ressources_ — créer une connexion DB par demande utilisateur peut submerger la DB. L'utilisation d'un pool ajoute effectivement une barrière, limitant le nombre maximum de connexions simultanées.

> Bien, je suis convaincu, mais...

### Un Connection Pool n'est-il pas un problème résolu dans le monde Java ?

Oui, c'est un problème résolu si vous utilisez [JDBC](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/). Dans ce cas, [HikariCP](https://brettwooldridge.github.io/HikariCP/) est un excellent choix selon mon expérience, mais il en existe beaucoup d'autres. Dans le cas de jasync-sql, il n'est pas possible d'utiliser [HikariCP](https://brettwooldridge.github.io/HikariCP/), car [HikariCP](https://brettwooldridge.github.io/HikariCP/) fonctionne avec l'API JDBC, et le pilote jasync-sql n'implémente pas cette API complète, seulement un sous-ensemble.

> Qu'en est-il des autres pools d'objets dans le monde Java ?

Il existe de nombreuses implémentations, mais il s'avère que vous trouvez généralement une exigence spécifique qui n'était pas implémentée par ce pool que vous utilisez.

Dans notre cas, cette exigence était le non-blocage. Dans notre pool, toutes les opérations doivent être non-bloquantes puisque la bibliothèque est asynchrone. Par exemple, l'opération `take()` dans la plupart des implémentations retourne un objet immédiatement ou bloque jusqu'à ce qu'un objet soit prêt. Notre `take()` retourne un `Future<Connecti`on>, qui sera complété et continué lorsque la connexion sera prête à être utilisée.

Je n'ai pas vu une telle implémentation dans la nature.

J'aime vraiment cette réponse de Stack Exchange :

[**Is object pooling a deprecated technique?**](https://softwareengineering.stackexchange.com/questions/115163/is-object-pooling-a-deprecated-technique)  
[_Software Engineering Stack Exchange is a question and answer site for professionals, academics, and students working...softwareengineering.stackexchange.com](https://softwareengineering.stackexchange.com/questions/115163/is-object-pooling-a-deprecated-technique)

Une autre exigence qui rend difficile la recherche d'une alternative est la nécessité d'essayer de rester compatible autant que possible avec l'implémentation actuelle que nous avons.

Au cas où vous voudriez voir d'autres implémentations, vous pouvez vérifier ici :

[**object pool in java - Google Search**](https://www.google.co.il/search?q=object+pool+in+java)  
[_object pool is a collection of a particular object that an application will create and keep on hand for those...www.google.co.il](https://www.google.co.il/search?q=object+pool+in+java)

### Alors, comment avons-nous implémenté Object Pool ?

Avant de plonger dans les détails, observons d'autres exigences du pool d'objets qui ont été omises ci-dessus pour des raisons de clarté mais qui sont des détails nécessaires.

#### Interfaces

L'interface du pool d'objets ressemble à ceci :

```
interface AsyncObjectPool<T> {  fun take(): CompletableFuture<T>  fun giveBack(item: T): CompletableFuture<AsyncObjectPool<T>>  fun close(): CompletableFuture<AsyncObjectPool<T>>
```

```
}
```

En outre, lorsqu'un pool souhaite créer de nouveaux objets (connexions), il appellera `ObjectFactory`. L'usine a quelques méthodes supplémentaires pour gérer le cycle de vie de l'objet :

* _validate_ — une méthode pour vérifier que l'objet est toujours valide. La méthode doit être rapide et ne vérifier que les constructions en mémoire. Pour les connexions, nous vérifions généralement que la dernière requête n'a pas levé d'exception et n'a pas reçu de message de terminaison de [netty](https://netty.io/).
* _test_ — similaire à validate, mais une vérification plus exhaustive. Nous permettons à la méthode de test d'être lente et d'accéder au réseau, etc. Cette méthode est utilisée pour vérifier que les objets inactifs sont toujours valides. Pour les connexions, cela sera quelque chose de similaire à `select 0`.
* _destroy_ — appelé pour nettoyer l'objet lorsque le pool ne l'utilise plus.

L'interface complète est :

```
interface ObjectFactory<T> {  fun create(): CompletableFuture<out T>  fun destroy(item: T)  fun validate(item: T): Try<T>  fun test(item: T): CompletableFuture<T>
```

```
}
```

Pour la configuration du pool, nous avons les propriétés suivantes :

* `maxObjects` — nombre maximum de connexions que nous permettons.
* `maxIdle` — temps pendant lequel nous laissons la connexion ouverte sans utilisation. Après ce temps, elle sera récupérée.
* `maxQueueSize` — lorsqu'une demande de connexion arrive et qu'aucune connexion n'est disponible, nous mettons la demande en attente dans une file d'attente. Dans le cas où la file d'attente est pleine (sa taille a dépassé `maxQueueSize`), elle n'attendra pas mais retournera plutôt une erreur.
* `createTimeout` — temps maximum d'attente pour la création d'une nouvelle connexion.
* `testTimeout` — temps maximum d'attente pour une requête de test sur une connexion inactive. Si elle dépasse ce temps, nous considérerons la connexion comme erronée.
* `validationInterval` — à cet intervalle, nous testerons si les connexions inactives sont actives et libérerons les connexions qui ont dépassé `maxIdle`. Nous supprimerons également les connexions qui ont dépassé `testTimeout`.

#### Implémentation originale

La première implémentation du pool d'objets était monothread. Toutes les opérations étaient envoyées à un thread worker qui était responsable de leur exécution. Cette méthode est connue sous le nom de [thread-confinement](https://www.javaspecialists.eu/archive/Issue218.html). La création d'objets et les opérations de test étaient bloquantes et l'exécution des requêtes elle-même était non bloquante.

Cette méthode est problématique car les opérations sont effectuées les unes après les autres. En plus de cela, il y a quelques opérations qui sont bloquantes comme mentionné ci-dessus. Il y avait divers cas de latence élevée lors du travail dans certains scénarios et cas d'utilisation (comme [ici](https://github.com/mauricio/postgresql-async/issues/91) par exemple).

En tant que solution de contournement, `PartitionedPool` a été introduit. Il s'agit d'un contournement au problème de _blocage_ avec l'approche monothread ci-dessus. Le pool partitionné crée plusieurs `SingleThreadedObjectPools`, chacun avec son propre worker. Lorsqu'une connexion est demandée, un pool est sélectionné par un modulus sur l'identifiant du thread. Le pool partitionné est en fait un pool de pools ;-)

J'ai mentionné que c'est un contournement puisque cela a ses propres problèmes : vous pouvez encore être bloqué, mais à un taux plus faible — plus il consomme plus de threads et de ressources.

#### Implémentation basée sur les acteurs

Un acteur est une entité qui possède une boîte aux lettres. Il reçoit des messages dans sa boîte aux lettres et les traite les uns après les autres. La boîte aux lettres est une sorte de canal pour transmettre des événements du monde extérieur à l'acteur.

Un acteur de coroutines emploie des algorithmes sans verrouillage pour permettre une exécution rapide et performante des événements sans avoir besoin de verrous et de blocs `synchronized`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*T1B40xs7Fsf-gnfZ)
« wall rack filled with paper document lot » par [Unsplash](https://unsplash.com/@californong?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title="">Nong Vang</a> sur <a href="https://unsplash.com?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title=")

Vous pouvez voir une explication détaillée [ici](https://www.brianstorti.com/the-actor-model/).

Dans notre cas, ces événements seront `take` et `giveBack`. En plus de ceux-ci, nous aurons des messages internes que l'acteur s'envoie à lui-même comme `objectCreated`, etc. Cela permet à l'acteur d'avoir des états qui ne souffrent pas de problèmes de concurrence, car il est toujours confiné à la même exécution séquentielle. En outre, le canal qui transmet ces événements est une file d'attente qui utilise des algorithmes sans verrouillage, donc il est très efficace, évite les contentions et a généralement des performances très élevées.

Il y a une excellente vidéo expliquant comment cela a été implémenté (notez que cela est un contenu algorithmique « lourd ») :

Récapitulons ce que nous avons jusqu'à présent :

* Un acteur reçoit des messages et les traite un par un.
* Habituellement, les messages contiendront un `CompletableFuture` qui doit être complété lorsque l'acteur le traite.

Les messages seront complétés immédiatement ou retardés (comme dans le cas où nous attendons qu'une connexion soit créée). Si c'est retardé, l'acteur mettra le `Future` dans une file d'attente et utilisera un mécanisme de rappel pour se notifier lorsque le futur original peut être complété.

* Le traitement des messages dans l'acteur ne doit pas être bloqué ou retardé. Si cela se produit, cela retardera tous les messages en attente d'être traités dans la file d'attente et ralentira toute l'opération de l'acteur.

**C'est pourquoi, dans le cas où nous avons des opérations de longue durée à l'intérieur de l'acteur, nous utilisons le mécanisme de rappel.**

#### Voyons plus de détails sur les cas d'utilisation

`Take` — quelqu'un veut un objet du pool. Il enverra un message avec un rappel à l'acteur. L'acteur fera l'une des choses suivantes :

* Si l'objet est disponible — l'acteur le retournera simplement.
* Si le pool n'a pas dépassé la limite d'objets créés — l'acteur créera un nouvel objet et le retournera lorsque l'objet sera prêt.

Dans un tel cas, la création d'un objet peut prendre du temps, donc l'acteur connectera le rappel de la création de l'objet au rappel de la demande de prise originale.

* Mettra la demande dans une file d'attente pour un objet disponible (sauf si la file d'attente est pleine et dans ce cas, elle retournera simplement une erreur).

`GiveBack` — quelqu'un veut rendre un objet au pool (le libérer). Cela se fait également par un message à l'acteur. L'acteur fera l'une des choses suivantes :

* Si quelqu'un attend dans la file d'attente — il lui empruntera l'objet.
* Dans les autres cas, il gardera simplement l'objet dans le pool pour les demandes à venir, de sorte que l'objet reste inactif.

`Test` — périodiquement, quelqu'un de l'extérieur notifiera l'acteur de tester les connexions :

* L'acteur libérera la connexion inactive qui n'a pas été utilisée depuis longtemps (c'est configurable).
* L'acteur testera d'autres objets inactifs en utilisant `ObjectFactory`. Il enverra un rappel à l'usine et marquera ces objets comme _In Use_, pour empêcher de les emprunter jusqu'à ce que le test soit terminé.
* L'acteur vérifiera les délais d'attente dans les tests et détruira les objets dont le temps est écoulé.

Ce sont les principaux cas d'utilisation.

#### Fuites

![Image](https://cdn-media-1.freecodecamp.org/images/0*64dZ7F9trDtbSdWq)
« selective focus photography of brown faucet » par [Unsplash](https://unsplash.com/@leipuri?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title="">Jouni Rajala</a> sur <a href="https://unsplash.com?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title=")

Il peut y avoir toutes sortes de fuites dans un pool d'objets. Certaines sont des bugs internes que j'espère plus faciles à repérer et à corriger, et d'autres sont des objets qui ont été pris mais non rendus en raison d'une erreur utilisateur. Dans de tels cas, les objets peuvent rester dans la file d'attente « In Use » pour toujours.

Pour éviter de tels cas, la carte « In Use » utilise [WeakHashMap](https://www.baeldung.com/java-weakhashmap) de Java. Ainsi, si un utilisateur a perdu une connexion, elle sera automatiquement supprimée de la carte lorsqu'elle sera nettoyée par le Garbage-Collector de Java.

En outre, nous avons ajouté un message de journalisation dans de tels cas qui dit : **« LEAK-DETECTED »**.

### C'est tout !

Le code source complet Kotlin du pool d'objets est disponible ici :

[**jasync-sql/jasync-sql**](https://github.com/jasync-sql/jasync-sql/blob/bacdd12243d89a5e2a46501bb5303815a9fd11e7/db-async-common/src/main/java/com/github/jasync/sql/db/pool/ActorBasedObjectPool.kt)  
[_Java async database driver for MySQL and PostgreSQL written in Kotlin - jasync-sql/jasync-sql_github.com](https://github.com/jasync-sql/jasync-sql/blob/bacdd12243d89a5e2a46501bb5303815a9fd11e7/db-async-common/src/main/java/com/github/jasync/sql/db/pool/ActorBasedObjectPool.kt)

Dans un prochain article, je comparerai les métriques de performance des différentes implémentations.

Si vous souhaitez en savoir plus sur Kotlin, il y a une bonne introduction ici :

Et pour les coroutines en général, consultez cette vidéo :

Enfin, si vous souhaitez en savoir plus sur l'implémentation des acteurs en utilisant les coroutines en Kotlin, rendez-vous ici :

[**Kotlin/kotlinx.coroutines**](https://github.com/Kotlin/kotlinx.coroutines/blob/master/docs/shared-mutable-state-and-concurrency.md)  
[_Library support for Kotlin coroutines . Contribute to Kotlin/kotlinx.coroutines development by creating an account on...github.com](https://github.com/Kotlin/kotlinx.coroutines/blob/master/docs/shared-mutable-state-and-concurrency.md)

Merci d'avoir lu ! ❤️

![Image](https://cdn-media-1.freecodecamp.org/images/0*0aDugHie8xlGjhOZ)
« aerial photography of woman on pink swimming floats » par [Unsplash](https://unsplash.com/@tom_grimbert?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title="">Tom Grimbert</a> sur <a href="https://unsplash.com?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title=")
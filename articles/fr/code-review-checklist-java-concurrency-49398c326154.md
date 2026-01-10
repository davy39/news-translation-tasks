---
title: 'Liste de contrôle pour la révision de code : comment aborder les problèmes
  de concurrency en Java'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T12:20:31.000Z'
originalURL: https://freecodecamp.org/news/code-review-checklist-java-concurrency-49398c326154
coverImage: https://cdn-media-1.freecodecamp.org/images/1*R49yRXvFbFb4kQrfH1eSDg.jpeg
tags:
- name: code review
  slug: code-review
- name: concurrency
  slug: concurrency
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Liste de contrôle pour la révision de code : comment aborder les problèmes
  de concurrency en Java'
seo_desc: 'By Roman Leventov

  At the Apache Druid community, we are currently preparing a detailed checklist to
  be used during code reviews. I decided to publish parts of the checklist as posts
  on Medium to gather more ideas for checklist items. Hopefully, someb...'
---

Par Roman Leventov

Au sein de la communauté [Apache Druid](http://druid.apache.org/), nous préparons actuellement une liste de contrôle détaillée à utiliser lors des révisions de code. J'ai décidé de publier des parties de cette liste sous forme d'articles sur Medium afin de recueillir plus d'idées pour les éléments de la liste. Espérons que quelqu'un la trouvera utile en pratique.

D'ailleurs, il me semble que la création de listes de contrôle spécifiques à un projet pour les révisions de code devrait être une idée puissante, pourtant je ne vois aucun exemple existant parmi les grands projets open source.

Cet article contient des éléments de liste de contrôle concernant les problèmes qui surviennent avec le code Java multithread.

Merci à [Marko Topolnik](https://stackoverflow.com/users/1103872/marko-topolnik), [Matko Medenjak](https://github.com/mmedenjak), [Chris Vest](https://github.com/chrisvest), [Simon Willnauer](https://github.com/s1monw), [Ben Manes](https://github.com/ben-manes), [Gleb Smirnov](https://github.com/gvsmirnov), [Andrey Satarin](https://github.com/asatarin), [Benedict Jin](https://github.com/asdf2014), et [Petr Janeček](https://stackoverflow.com/users/1273080/petr-janeček) pour leurs révisions et contributions à cet article. La liste de contrôle n'est pas considérée comme complète, les commentaires et suggestions sont les bienvenus !

Mise à jour : cette liste de contrôle est désormais disponible [sur Github](https://github.com/code-review-checklists/java-concurrency).

#### 1. Conception

1.1. Si le patch introduit un nouveau sous-système avec du code concurrent, **la nécessité de la concurrency est-elle justifiée dans la description du patch** ? Y a-t-il une discussion sur les approches de conception alternatives qui pourraient simplifier le modèle de concurrency du code (voir l'élément suivant) ?

1.2. Est-il possible d'appliquer un ou plusieurs modèles de conception (certains d'entre eux sont listés ci-dessous) pour **simplifier considérablement le modèle de concurrency du code, sans compromettre de manière significative d'autres aspects de qualité**, tels que la simplicité globale, l'efficacité, la testabilité, l'extensibilité, etc. ?

**Immuabilité/Instantané.** Lorsque certains états doivent être mis à jour, un nouvel objet immuable (ou un instantané au sein d'un objet mutable) est créé, publié et utilisé, tandis que certains threads concurrents peuvent encore utiliser des copies ou instantanés plus anciens. Voir [EJ Item 17], [JCIP 3.4], les éléments 4.5 et 9.2 dans cette liste de contrôle, `CopyOnWriteArrayList`, `CopyOnWriteArraySet`, [structures de données persistantes](https://en.wikipedia.org/wiki/Persistent_data_structure).

**Diviser pour régner.** Le travail est divisé en plusieurs parties qui sont traitées indépendamment, chaque partie dans un seul thread. Ensuite, les résultats du traitement sont combinés. Les Streams parallèles (voir section 14) ou `ForkJoinPool` (voir éléments 10.4 et 10.5) peuvent être utilisés pour appliquer ce modèle.

**Producteur-consommateur.** Les morceaux de travail sont transmis entre les threads de travail via des files d'attente. Voir [JCIP 5.3], l'élément 6.1 dans cette liste de contrôle, [CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes), [SEDA](https://en.wikipedia.org/wiki/Staged_event-driven_architecture).

**Confinement d'instance.** Les objets d'un certain type racine encapsulent un certain état hiérarchique enfant complexe. Les objets racines sont seuls responsables de la sécurité des accès et des modifications de l'état enfant à partir de plusieurs threads. En d'autres termes, les objets composés sont synchronisés plutôt que les objets synchronisés soient composés. Voir [JCIP 4.2, 10.1.3, 10.1.4].

**Confinement de thread/tâche/thread série.** Certains états sont rendus locaux à un thread en utilisant des paramètres passés de haut en bas ou `ThreadLocal`. Voir [JCIP 3.3]. Le confinement de tâche est une variation de l'idée de confinement de thread qui est utilisée en conjonction avec le modèle diviser-pour-régner. Il se présente généralement sous la forme de paramètres ou de champs "contexte" capturés par lambda dans les objets de tâche par thread. Le confinement de thread série est une extension de l'idée de confinement de thread pour le modèle producteur-consommateur, voir [JCIP 5.3.2].

#### 2. Documentation

2.1. Pour chaque classe, méthode et champ qui présente des signes d'être thread-safe, tels que le mot-clé `synchronized`, les modificateurs `volatile` sur les champs, l'utilisation de classes de `java.util.concurrent.*`, ou de primitives de concurrency tierces, ou de collections concurrentes : leurs commentaires Javadoc incluent-ils

* **La justification de la thread safety** : est-il expliqué pourquoi une classe, méthode ou champ particulière doit être thread-safe ?
* **Documentation du flux de contrôle concurrent** : est-il énuméré à partir de quelles méthodes et dans quels contextes de threads (exécuteurs, pools de threads) chaque méthode spécifique d'une classe thread-safe est appelée ?

Là où une certaine logique est parallélisée ou l'exécution est déléguée à un autre thread, y a-t-il des commentaires expliquant pourquoi il est pire ou inapproprié d'exécuter la logique de manière séquentielle ou dans le même thread ? Voir aussi l'élément 14.1 dans cette liste de contrôle concernant l'utilisation des `Stream` parallèles.

2.2. Si le patch introduit un nouveau sous-système qui utilise des threads ou des pools de threads, y a-t-il **des descriptions de haut niveau du modèle de threading, du flux de contrôle concurrent (ou du flux de données) du sous-système** quelque part, par exemple, dans le commentaire Javadoc pour le package dans `package-info.java` ou pour la classe principale du sous-système ? Ces descriptions sont-elles maintenues à jour lorsque de nouveaux threads ou pools de threads sont ajoutés ou que certains anciens sont supprimés du système ?

La description du modèle de threading inclut l'énumération des threads et des pools de threads créés et gérés dans le sous-système, et des pools externes utilisés dans le sous-système (tels que `ForkJoinPool.commonPool()`), leurs tailles et autres caractéristiques importantes telles que les priorités des threads, et le cycle de vie des threads et pools de threads gérés.

Une description de haut niveau du flux de contrôle concurrent devrait être un aperçu et relier ensemble la documentation du flux de contrôle concurrent pour les classes individuelles, voir l'élément précédent. Si le modèle producteur-consommateur est utilisé, le flux de contrôle concurrent est trivial et le flux de données devrait être documenté à la place.

Décrire les modèles de threading et les flux de contrôle/données améliore grandement la maintenabilité du système, car en l'absence de descriptions ou de diagrammes, les développeurs passent beaucoup de temps et d'efforts à créer et à rafraîchir ces modèles dans leur esprit. Mettre les modèles par écrit aide également à découvrir les goulots d'étranglement et les moyens de simplifier la conception (voir l'élément 1.2).

2.3. Pour les classes et méthodes qui font partie de l'API publique ou de l'API d'extensions du projet : est-il spécifié dans leurs commentaires Javadoc s'ils sont (ou dans le cas des interfaces et classes abstraites conçues pour être sous-classées dans les extensions, doivent-ils être implémentés comme) **immuables, thread-safe ou non thread-safe** ? Pour les classes et méthodes qui sont (ou doivent être implémentées comme) thread-safe, est-il documenté précisément avec quelles autres méthodes (ou eux-mêmes) ils peuvent être appelés de manière concurrente à partir de plusieurs threads ? Voir aussi [EJ Item 82] et [JCIP 4.5].

Si l'annotation `@com.google.errorprone.annotations.Immutable` est utilisée pour marquer les classes immuables, l'outil d'analyse statique [Error Prone](https://errorprone.info/) est capable de détecter lorsqu'une classe n'est pas réellement immuable (voir le [modèle de bug](https://errorprone.info/bugpattern/Immutable) pertinent).

2.4. Pour les sous-systèmes, classes, méthodes et champs qui utilisent certains modèles de conception de concurrency, soit de haut niveau (tels que ceux mentionnés dans l'élément 1.2 de cette liste de contrôle) soit de bas niveau (tels que le double-checked locking, voir la section 8 dans cette liste de contrôle) : les **modèles de concurrency utilisés sont-ils prononcés dans les commentaires de conception ou d'implémentation** pour les sous-systèmes, classes, méthodes et champs respectifs ? Cela aide les lecteurs à comprendre plus rapidement le code.

2.5. Les objets `ConcurrentHashMap` et `ConcurrentSkipListMap` sont-ils stockés dans des champs et variables de type `ConcurrentHashMap` ou `ConcurrentSkipListMap` ou `ConcurrentMap`, mais pas simplement `Map` ?

Cela est important, car dans un code comme le suivant :

```
ConcurrentMap<String, Entity> entities = getEntities();if (!entities.containsKey(key)) {  entities.put(key, entity);} else {  ...}
```

Il devrait être assez évident qu'il pourrait y avoir une condition de course car une entité peut être mise dans la map par un thread concurrent entre les appels à `containsKey()` et `put()` (voir l'élément 4.1 sur ce type de conditions de course). Alors que si le type de la variable `entities` était simplement `Map<String, Entity>` ce serait moins évident et les lecteurs pourraient penser que ce n'est qu'un code légèrement sous-optimal et passer leur chemin.

Il est possible de transformer ce conseil en [une inspection](https://github.com/apache/incubator-druid/pull/6898/files#diff-3aa5d63fbb1f0748c146f88b6f0efc81R239) dans IntelliJ IDEA.

2.6. Une extension de l'élément précédent : les ConcurrentHashMaps sur lesquels les méthodes `compute()`, `computeIfAbsent()`, `computeIfPresent()`, ou `merge()` sont appelées sont-ils stockés dans des champs et variables de type `ConcurrentHashMap` plutôt que `ConcurrentMap` ? Cela est dû au fait que `ConcurrentHashMap` (contrairement à l'interface générique `ConcurrentMap`) garantit que les lambdas passés dans les méthodes de type `compute()` sont exécutés de manière atomique par clé, et la thread safety de la classe peut dépendre de cette garantie.

Ce conseil peut sembler excessivement pédant, mais s'il est utilisé en conjonction avec une règle d'analyse statique qui interdit d'appeler des méthodes de type `compute()` sur des objets typés `ConcurrentMap` qui ne sont pas des ConcurrentHashMaps (il est possible de créer une telle inspection dans IntelliJ IDEA également), il pourrait prévenir certains bugs : par exemple, **appeler `compute()` sur un `ConcurrentSkipListMap` pourrait être une condition de course** et il est facile de négliger cela pour quelqu'un qui est habitué à se fier à la sémantique forte de `compute()` dans `ConcurrentHashMap`.

2.7. L'annotation **`@GuardedBy` est-elle utilisée** ? Si les accès à certains champs doivent être protégés par un certain verrou, ces champs sont-ils annotés avec `@GuardedBy` ? Les méthodes privées qui sont appelées depuis des sections critiques dans d'autres méthodes sont-elles annotées avec `@GuardedBy` ? Si le projet ne dépend d'aucune bibliothèque contenant cette annotation (elle est fournie par `jcip-annotations`, `error_prone_annotations`, `jsr305` et d'autres bibliothèques) et qu'il est indésirable d'ajouter une telle dépendance pour une raison quelconque, il devrait être mentionné dans les commentaires Javadoc pour les champs et méthodes respectifs que les accès et appels à ceux-ci doivent être protégés par certains verrous spécifiés.

Voir [JCIP 2.4] pour plus d'informations sur `@GuardedBy`.

L'utilisation de `GuardedBy` est particulièrement bénéfique en conjonction avec Error Prone, qui est capable de [vérifier statiquement les accès non protégés aux champs et méthodes avec des annotations `@GuardedBy`](https://errorprone.info/bugpattern/GuardedBy).

2.8. Si dans une classe thread-safe certains **champs sont accédés à la fois depuis des sections critiques et en dehors des sections critiques**, est-il expliqué dans les commentaires pourquoi cela est sûr ? Par exemple, un accès en lecture seule non protégé à une référence à un objet immuable pourrait être bénignement concurrent (voir l'élément 4.5).

2.9. Concernant chaque champ avec un modificateur `volatile` : **a-t-il vraiment besoin d'être `volatile`** ? Le commentaire Javadoc pour le champ explique-t-il pourquoi la sémantique des lectures et écritures de champs `volatile` (telle que définie dans le [Java Memory Model](https://docs.oracle.com/javase/specs/jls/se11/html/jls-17.html#jls-17.4)) est requise pour le champ ?

2.10. Est-il expliqué dans le **commentaire Javadoc pour chaque champ mutable dans une classe thread-safe qui n'est ni `volatile` ni annoté avec `@GuardedBy`**, pourquoi cela est sûr ? Peut-être que le champ n'est accédé et muté que depuis une seule méthode ou un ensemble de méthodes qui sont spécifiées pour être appelées uniquement depuis un seul thread de manière séquentielle (comme décrit dans l'élément 2.1). Cette recommandation s'applique également aux champs `final` qui stockent des objets de classes non thread-safe lorsque ces objets pourraient être mutés depuis les méthodes de la classe thread-safe englobante. Voir les éléments 4.2-4.4 dans cette liste de contrôle sur ce qui pourrait mal se passer avec un tel code.

#### 3. Sécurité de thread excessive

3.1. Un exemple de sécurité de thread excessive est une classe où chaque champ modifiable est `volatile` ou un `AtomicReference` ou autre atomique, et chaque champ de collection stocke une collection concurrente (par exemple, `ConcurrentHashMap`), bien que tous les accès à ces champs soient synchronisés.

**Il ne devrait pas y avoir de sécurité de thread "extra" dans le code, il devrait y en avoir juste assez.** La duplication de la sécurité de thread confond les lecteurs car ils pourraient penser que les précautions de sécurité de thread supplémentaires sont (ou étaient) nécessaires pour quelque chose mais échoueront à trouver le but.

L'exception à ce principe est le modificateur `volatile` sur le champ initialisé de manière paresseuse dans le [modèle de double-checked locking local sûr](http://hg.openjdk.java.net/code-tools/jcstress/file/9270b927e00f/tests-custom/src/main/java/org/openjdk/jcstress/tests/singletons/SafeLocalDCL.java#l71) qui est la manière recommandée d'implémenter le double-checked locking, malgré le fait que `volatile` est [excessif pour la correction](https://shipilev.net/blog/2014/safe-public-construction/#_correctness) lorsque l'objet initialisé de manière paresseuse a tous les champs `final`[*](https://shipilev.net/blog/2014/safe-public-construction/#_safe_initialization). Sans ce modificateur `volatile`, la sécurité de thread du double-checked locking pourrait facilement être rompue par un changement (ajout d'un champ non-`final`) dans la classe des objets initialisés de manière paresseuse, bien que cette classe ne devrait pas être consciente des implications subtiles de concurrency. Si la classe des objets initialisés de manière paresseuse est _spécifiée_ pour être immuable (voir l'élément 2.3), le `volatile` est toujours inutile et le modèle [UnsafeLocalDCL](http://hg.openjdk.java.net/code-tools/jcstress/file/9270b927e00f/tests-custom/src/main/java/org/openjdk/jcstress/tests/singletons/UnsafeLocalDCL.java#l71) pourrait être utilisé en toute sécurité, mais le fait qu'une classe ait tous les champs `final` ne signifie pas nécessairement qu'elle est immuable.

Voir aussi la section 8 dans cet article sur le double-checked locking.

3.2. N'y a-t-il pas de champs `AtomicReference`, `AtomicBoolean`, `AtomicInteger` ou `AtomicLong` sur lesquels seules les méthodes `get()` et `set()` sont appelées ? Des champs simples avec des modificateurs `volatile` peuvent être utilisés à la place, mais `volatile` pourrait ne pas être nécessaire non plus ; voir l'élément 2.9.

#### 4. Conditions de course

4.1. Les `ConcurrentHashMaps` ne sont-ils pas mis à jour avec plusieurs appels séparés `containsKey()`, `get()`, `put()` et `remove()` au lieu d'un seul appel à `compute()`/`computeIfAbsent()`/`computeIfPresent()`/`replace()` ?

4.2. N'y a-t-il pas d'**accès en lecture ponctuelle tels que `Map.get()`, `containsKey()` ou `List.get()` en dehors des sections critiques à une collection non thread-safe telle que `HashMap` ou `ArrayList`**, tandis que de nouvelles entrées peuvent être ajoutées à la collection de manière concurrente, même s'il existe une relation happens-before entre le moment où une entrée est mise dans la collection et le moment où la même entrée est interrogée ponctuellement en dehors d'une section critique ?

Le problème est que lorsque de nouvelles entrées peuvent être ajoutées à une collection, celle-ci grandit et change sa structure interne de temps en temps (`HashMap` rehash la table de hachage, `ArrayList` réalloue le tableau interne). À de tels moments, des courses peuvent se produire et des accès en lecture ponctuelle non protégés peuvent échouer avec `NullPointerException`, `ArrayIndexOutOfBoundsException`, ou retourner `null` ou une entrée aléatoire.

Notez que cette préoccupation s'applique à `ArrayList` même lorsque les éléments sont uniquement ajoutés à la fin de la liste. Cependant, un petit changement dans l'implémentation d'`ArrayList` dans OpenJDK pourrait avoir interdit les courses de données dans de tels cas à très peu de frais. Si vous êtes abonné à la liste de diffusion concurrency-interest, vous pourriez aider à attirer l'attention sur ce problème en relançant [ce fil de discussion](http://cs.oswego.edu/pipermail/concurrency-interest/2018-September/016526.html).

4.3. Une variation de l'élément précédent : une collection non thread-safe telle que `HashMap` ou `ArrayList` n'est-elle pas **itérée en dehors d'une section critique**, alors qu'elle peut être modifiée de manière concurrente ? Cela pourrait se produire par accident lorsqu'un `Iterable`, `Iterator` ou `Stream` sur une collection est retourné par une méthode d'une classe thread-safe, même si l'itérateur ou le stream est créé au sein d'une section critique.

Comme l'élément précédent, celui-ci s'applique également aux ArrayLists en croissance.

4.4. Plus généralement, des **objets non triviaux qui peuvent être mutés de manière concurrente ne sont-ils pas retournés par des getters** sur une classe thread-safe ?

4.5. S'il y a plusieurs variables dans une classe thread-safe qui sont **mises à jour en même temps mais ont des getters individuels**, n'y a-t-il pas une condition de course dans le code qui appelle ces getters ? Si c'est le cas, les variables doivent être rendues des champs `final` dans un POJO dédié, qui sert d'instantané de l'état mis à jour. Le POJO est stocké dans un champ de la classe thread-safe, directement ou comme un `AtomicReference`. Plusieurs getters vers des champs individuels doivent être remplacés par un seul getter qui retourne le POJO. Cela permet d'éviter une condition de course dans le code client en lisant un instantané cohérent de l'état en une seule fois.

Ce modèle est également très utile pour créer un code non bloquant sûr et raisonnablement simple : voir l'élément 9.2 dans cette liste de contrôle et [JCIP 15.3.1].

4.6. Si une certaine logique au sein d'une section critique dépend de certaines données qui font principalement partie de l'état interne mutable de la classe, mais ont été lues en dehors de la section critique ou dans une section critique différente, n'y a-t-il pas une condition de course parce que la **copie locale des données peut devenir désynchronisée avec l'état interne au moment où la section critique est entrée** ? Il s'agit d'une variante typique de la condition de course check-then-act, voir [JCIP 2.2.1].

4.7. N'y a-t-il pas de **conditions de course entre le code (c'est-à-dire les actions d'exécution du programme) et certaines actions dans le monde extérieur** ou des actions effectuées par d'autres programmes s'exécutant sur la machine ? Par exemple, si certaines configurations ou informations d'identification sont rechargées à chaud à partir d'un fichier ou d'un registre externe, la lecture de paramètres de configuration séparés ou d'informations d'identification séparées (telles que le nom d'utilisateur et le mot de passe) dans des transactions séparées avec le fichier ou le registre peut être en concurrence avec un opérateur système mettant à jour ces configurations ou informations d'identification.

Un autre exemple est la vérification qu'un fichier existe (ou n'existe pas) puis sa lecture, sa suppression ou sa création, respectivement, tandis qu'un autre programme ou un utilisateur peut supprimer ou créer le fichier entre la vérification et l'action. Il n'est pas toujours possible de faire face à de telles conditions de course, mais il est utile de garder de telles possibilités à l'esprit. Préférez les méthodes statiques de la classe `[java.nio.file.Files](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/file/Files.html)` plutôt que les méthodes de l'ancien `java.io.File` pour les opérations sur le système de fichiers. Les méthodes de `Files` sont plus sensibles aux conditions de course du système de fichiers et tendent à lever des exceptions dans les cas défavorables, tandis que les méthodes de `File` avalent les erreurs et rendent même difficile la détection des conditions de course.

#### 5. Remplacement des verrous par des utilitaires de concurrency

5.1. Est-il possible d'utiliser des collections concurrentes et/ou des utilitaires de `java.util.concurrent.*` et **éviter d'utiliser des verrous avec `Object.wait()`/`notify()`/`notifyAll()`** ? Le code reconçu autour des collections concurrentes et des utilitaires est souvent à la fois plus clair et moins sujet aux erreurs que le code implémentant la logique équivalente avec des verrous intrinsèques, `Object.wait()` et `notify()` (les objets `Lock` avec `await()` et `signal()` ne sont pas différents à cet égard). Voir [EJ Item 81] pour plus d'informations.

5.2. Est-il possible de **simplifier le code qui utilise des verrous intrinsèques ou des objets `Lock` avec des attentes conditionnelles en utilisant `Monitor` de Guava** ?

#### 6. Éviter les deadlocks

6.1. Si une classe thread-safe est implémentée de sorte qu'il y a des sections critiques imbriquées protégées par différents verrous, **est-il possible de reconcevoir le code pour se débarrasser des sections critiques imbriquées** ? Parfois, une classe pourrait être divisée en plusieurs classes distinctes, ou un certain travail qui est fait dans un seul thread pourrait être divisé entre plusieurs threads ou tâches qui communiquent via des files d'attente concurrentes. Voir [JCIP 5.3] pour plus d'informations sur le modèle producteur-consommateur.

6.2. Si la restructuration d'une classe thread-safe pour éviter les sections critiques imbriquées n'est pas raisonnable, a-t-il été délibérément vérifié que les verrous sont acquis dans le même ordre dans tout le code de la classe ? **L'ordre de verrouillage est-il documenté dans les commentaires Javadoc pour les champs où les objets de verrouillage sont stockés** ?

6.3. S'il y a des sections critiques imbriquées protégées par plusieurs (potentiellement différents) **verrous déterminés dynamiquement (par exemple, associés à certaines entités de logique métier), les verrous sont-ils ordonnés avant l'acquisition** ? Voir [JCIP 10.1.2] pour plus d'informations.

6.4. N'y a-t-il pas d'**appels à certains callbacks (listeners, etc.) qui peuvent être configurés via des appels d'API publique ou d'interface d'extension au sein des sections critiques** d'une classe ? Avec de tels appels, le système pourrait être intrinsèquement sujet aux deadlocks car la logique externe exécutée au sein d'une section critique pourrait ne pas être consciente des considérations de verrouillage et rappeler la logique du projet, où d'autres verrous pourraient être acquis, formant potentiellement un cycle de verrouillage qui pourrait conduire à un deadlock. Sans parler du fait que la logique externe pourrait simplement effectuer une opération chronophage et ainsi nuire à l'efficacité du système (voir l'élément suivant). Voir [JCIP 10.1.3] et [EJ Item 79] pour plus d'informations.

#### 7. Améliorer la scalabilité

7.1. **Les sections critiques sont-elles aussi petites que possible** ? Pour chaque section critique : ne peut-on pas déplacer certaines instructions au début et à la fin de la section en dehors de celle-ci ? Non seulement la minimisation des sections critiques améliore la scalabilité, mais elle facilite également leur révision et la détection des conditions de course et des deadlocks.

Ce conseil s'applique également aux lambdas passés dans les méthodes de type `compute()` de `ConcurrentHashMap`.

Voir aussi [JCIP 11.4.1] et [EJ Item 79].

7.2. Est-il possible d'**augmenter la granularité du verrouillage** ? Si une classe thread-safe encapsule les accès à une map, est-il possible de **transformer les sections critiques en lambdas passés dans `ConcurrentHashMap.compute()`** ou les méthodes `computeIfAbsent()` ou `computeIfPresent()` pour profiter d'une granularité de verrouillage efficace par clé ? Sinon, est-il possible d'utiliser [**`Striped` de Guava**](https://github.com/google/guava/wiki/StripedExplained) ou un équivalent ? Voir [JCIP 11.4.3] pour plus d'informations sur le striping de verrous.

7.3. Est-il possible d'**utiliser des collections non bloquantes au lieu de collections bloquantes** ? Voici quelques remplacements possibles au sein du JDK :

* `Collections.synchronizedMap(HashMap)`, `Hashtable` → `ConcurrentHashMap`
* `Collections.synchronizedSet(HashSet)` → `ConcurrentHashMap.newKeySet()`
* `Collections.synchronizedMap(TreeMap)` → `ConcurrentSkipListMap`. D'ailleurs, `ConcurrentSkipListMap` n'est pas l'implémentation de dictionnaire trié concurrent la plus avancée. `[SnapTree](https://github.com/nbronson/snaptree)` est [plus efficace](https://github.com/apache/incubator-druid/pull/6719) que `ConcurrentSkipListMap` et il y a eu des articles de recherche présentant des algorithmes qui sont censés être plus efficaces que SnapTree.
* `Collections.synchronizedSet(TreeSet)` → `ConcurrentSkipListSet`
* `Collections.synchronizedList(ArrayList)`, `Vector` → `CopyOnWriteArrayList`
* `LinkedBlockingQueue` → `ConcurrentLinkedQueue`
* `LinkedBlockingDeque` → `ConcurrentLinkedDeque`

A-t-il été envisagé d'**utiliser l'une des files d'attente basées sur des tableaux de la [bibliothèque JCTools](https://www.baeldung.com/java-concurrency-jc-tools) au lieu de `ArrayBlockingQueue`** ? Ces files d'attente de JCTools sont classées comme bloquantes, mais elles évitent l'acquisition de verrous dans de nombreux cas et sont généralement beaucoup plus rapides que `ArrayBlockingQueue`.

7.4. Est-il possible d'**utiliser `[ClassValue](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/ClassValue.html)` au lieu de `ConcurrentHashMap<Class, ...>`** ? Notez, cependant, que contrairement à `ConcurrentHashMap` avec sa méthode `computeIfAbsent()`, `ClassValue` ne garantit pas que la valeur par classe est calculée une seule fois, c'est-à-dire que `ClassValue.computeValue()` pourrait être exécuté par plusieurs threads concurrents. Donc, si le calcul à l'intérieur de `computeValue()` n'est pas thread-safe, il devrait être synchronisé séparément. D'un autre côté, `ClassValue` garantit que la même valeur est toujours retournée par `ClassValue.get()` (sauf si `remove()` est appelé).

7.5. A-t-il été envisagé de **remplacer un verrou simple par un `ReadWriteLock`** ? Attention, cependant, qu'il est plus coûteux d'acquérir et de libérer un `ReentrantReadWriteLock` qu'un verrou intrinsèque simple, donc l'augmentation de la scalabilité se fait au détriment du débit. Si les opérations à effectuer sous un verrou sont courtes, ou si un verrou est déjà strié (voir l'élément 7.2) et donc très peu contesté, **remplacer un verrou simple par un `ReadWriteLock` pourrait avoir un effet net négatif** sur les performances de l'application. Voir [ce commentaire](https://medium.com/@leventov/interesting-perspective-thanks-i-didnt-think-about-this-before-e044eec71870) pour plus de détails.

7.6. Est-il possible d'utiliser un `[**StampedLock**](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/locks/StampedLock.html)` **au lieu d'un `ReentrantReadWriteLock`** lorsque la réentrance n'est pas nécessaire ?

7.7. Est-il possible d'utiliser `[**LongAdder**](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/atomic/LongAdder.html)` **pour les "champs chauds"** (voir [JCIP 11.4.4]) au lieu de `AtomicLong` ou `AtomicInteger` sur lesquels seules des méthodes comme `incrementAndGet()`, `decrementAndGet()`, `addAndGet()` et (rarement) `get()` sont appelées, mais pas `set()` et `compareAndSet()` ?

#### 8. Initialisation paresseuse et double-checked locking

8.1. Pour chaque champ initialisé de manière paresseuse : **le code d'initialisation est-il thread-safe et pourrait-il être appelé par plusieurs threads de manière concurrente** ? Si les réponses sont "non" et "oui", soit le double-checked locking doit être utilisé, soit l'initialisation doit être immédiate.

8.2. Si un champ est initialisé de manière paresseuse sous un verrou simple, est-il possible d'utiliser le double-checked locking à la place pour améliorer les performances ?

8.3. Le double-checked locking suit-il le modèle [SafeLocalDCL](http://hg.openjdk.java.net/code-tools/jcstress/file/9270b927e00f/tests-custom/src/main/java/org/openjdk/jcstress/tests/singletons/SafeLocalDCL.java#l71), comme noté dans l'élément 3.1 de cette liste de contrôle ?

Si les objets initialisés sont immuables, un modèle plus efficace [UnsafeLocalDCL](http://hg.openjdk.java.net/code-tools/jcstress/file/9270b927e00f/tests-custom/src/main/java/org/openjdk/jcstress/tests/singletons/UnsafeLocalDCL.java#l71) pourrait également être utilisé. Cependant, si le champ initialisé de manière paresseuse n'est pas `volatile` et qu'il y a des accès au champ qui contournent le chemin d'initialisation, la valeur du **champ doit être soigneusement mise en cache dans une variable locale**. Par exemple, le code suivant est bogué :

```
private MyClass lazilyInitializedField;
```

```
void foo() {  if (lazilyInitializedField != null) { // (1)    // Peut lancer NPE !    lazilyInitializedField.bar();     // (2)  }}
```

Cela pourrait entraîner une `NullPointerException`, car bien qu'une valeur non nulle soit observée lorsque le champ est lu pour la première fois à la ligne 1, la deuxième lecture à la ligne 2 pourrait observer null.

Le code ci-dessus pourrait être corrigé comme suit :

```
void foo() {  MyClass lazilyInitialized = this.lazilyInitializedField;  if (lazilyInitialized != null) {    lazilyInitialized.bar();  }}
```

Voir « [Wishful Thinking: Happens-Before Is The Actual Ordering](https://shipilev.net/blog/2016/close-encounters-of-jmm-kind/#wishful-hb-actual) » pour plus d'informations.

8.4. Dans chaque cas particulier, l'**impact net du double-checked locking et de l'initialisation paresseuse des champs sur les performances et la complexité ne dépasse-t-il pas les avantages de l'initialisation paresseuse** ? N'est-il pas finalement préférable d'initialiser le champ immédiatement ?

8.5. Si un champ est initialisé de manière paresseuse sous un verrou simple ou en utilisant le double-checked locking, a-t-il vraiment besoin de verrouillage ? Si rien de mauvais ne peut se produire si deux threads effectuent l'initialisation en même temps et utilisent différentes copies de l'état initialisé, une course bénigne pourrait être autorisée. Le champ initialisé doit toujours être `volatile` (sauf si les objets initialisés sont immuables) pour garantir qu'il existe une relation happens-before entre les threads effectuant l'initialisation et lisant le champ.

Voir aussi [EJ Item 83] et « [Safe Publication this and Safe Initialization in Java](https://shipilev.net/blog/2014/safe-public-construction/) ».

#### 9. Code non bloquant et partiellement bloquant

9.1. S'il y a un certain code non bloquant ou semi-symétriquement bloquant qui mute l'état d'une classe thread-safe, a-t-il été délibérément vérifié que si un **thread sur un chemin de mutation non bloquant est préempté après chaque instruction, l'objet est toujours dans un état valide** ? Y a-t-il suffisamment de commentaires, peut-être avant presque chaque instruction où l'état est changé, pour rendre relativement facile pour les lecteurs du code de répéter et de vérifier la vérification ?

9.2. Est-il possible de simplifier un certain code non bloquant en **confinant tout l'état mutable dans un POJO immuable et en le mettant à jour via des opérations de comparaison et d'échange** ? Ce modèle est également mentionné dans l'élément 4.5. Au lieu d'un POJO, une seule valeur `long` pourrait être utilisée si toutes les parties de l'état sont des entiers qui peuvent ensemble tenir dans 64 bits. Voir aussi [JCIP 15.3.1].

#### 10. Threads et Executors

10.1. **Les Threads reçoivent-ils des noms** lors de leur création ? Les ExecutorServices sont-ils créés avec des factories de threads qui nomment les threads ?

Il semble que différents projets aient différentes politiques concernant d'autres aspects de la création de `Thread` : s'il faut les rendre daemon avec `setDaemon()`, s'il faut définir des priorités de thread et si un `ThreadGroup` doit être spécifié. De nombreuses règles de ce type peuvent être efficacement appliquées avec [forbidden-apis](https://github.com/policeman-tools/forbidden-apis).

10.2. N'y a-t-il pas de threads créés et démarrés, mais non stockés dans des champs, à la manière de `**new Thread(...).start()**`, dans certaines méthodes qui peuvent être appelées à plusieurs reprises ? Est-il possible de déléguer le travail à un `ExecutorService` mis en cache ou partagé à la place ?

10.3. **Certaines opérations d'E/S réseau ne sont-elles pas effectuées dans un `ExecutorService` créé avec `Executors.newCachedThreadPool()`** ? Si une machine exécutant l'application a des problèmes réseau ou si la bande passante réseau est épuisée en raison d'une charge accrue, les CachedThreadPools qui effectuent des E/S réseau pourraient commencer à créer de nouveaux threads de manière incontrôlable.

10.4. **N'y a-t-il pas d'opérations bloquantes ou d'E/S effectuées dans des tâches planifiées dans un `ForkJoinPool`** (sauf celles effectuées via un appel `[managedBlock()](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/ForkJoinPool.html#managedBlock(java.util.concurrent.ForkJoinPool.ManagedBlocker))`) ? Les opérations `Stream` parallèles sont exécutées dans le `ForkJoinPool` commun implicitement, ainsi que les lambdas passés dans les méthodes de `CompletableFuture` dont les noms se terminent par "Async".

Ce conseil ne doit pas être pris à l'extrême : les E/S transitoires occasionnelles (comme celles qui peuvent se produire lors de la journalisation) et les opérations qui peuvent rarement bloquer (comme les appels `ConcurrentHashMap.put()`) ne devraient généralement pas disqualifier tous leurs appelants de l'exécution dans un `ForkJoinPool` ou dans un `Stream` parallèle. Voir [Parallel Stream Guidance](http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html) pour une discussion plus détaillée de ces compromis.

Voir aussi la section 14 dans cette liste de contrôle sur les Streams parallèles.

10.5. Opposé à l'élément précédent : **les calculs non bloquants peuvent-ils être parallélisés ou exécutés de manière asynchrone en soumettant des tâches à `ForkJoinPool.commonPool()` ou via des Streams parallèles au lieu d'utiliser un pool de threads personnalisé** (par exemple, créé par l'une des méthodes de factory statiques de `ExecutorServices`) ? À moins que le pool de threads personnalisé ne soit configuré avec une `ThreadFactory` qui spécifie une priorité non par défaut pour les threads ou un gestionnaire d'exceptions personnalisé (voir l'élément 10.1), il y a peu de raisons de créer plus de threads dans le système au lieu de réutiliser les threads du `ForkJoinPool` commun.

#### 11. Interruption de thread et annulation de `Future`

11.1. Si un certain code propage `InterruptedException` enveloppée dans une autre exception (par exemple, `RuntimeException`), **le statut d'interruption du thread actuel est-il restauré avant que l'exception d'enveloppement ne soit lancée** ?

Propager `InterruptedException` enveloppée dans une autre exception est une pratique controversée (surtout dans les bibliothèques) et elle peut être interdite dans certains projets complètement, ou dans des sous-systèmes spécifiques.

11.2. Si une certaine méthode **retourne normalement après avoir attrapé une `InterruptedException`**, cela est-il cohérent avec la sémantique (documentée) de la méthode ? Retourner normalement après avoir attrapé une `InterruptedException` a généralement du sens seulement dans deux types de méthodes :

* `Runnable.run()` ou `Callable.call()` eux-mêmes, ou des méthodes qui sont destinées à être soumises comme tâches à certains Executors en tant que références de méthode. `Thread.currentThread().interrupt()` doit encore être appelé avant de retourner de la méthode, en supposant que la politique d'interruption des threads dans l'`Executor` est inconnue.
* Méthodes avec une sémantique "try" ou "best effort". La documentation pour de telles méthodes doit être claire qu'elles arrêtent d'essayer de faire quelque chose lorsque le thread est interrompu, restaurent le statut d'interruption du thread et retournent.

Si une méthode ne tombe dans aucune de ces catégories, elle doit propager `InterruptedException` directement ou enveloppée dans une autre exception (voir l'élément précédent), ou elle ne doit pas retourner normalement après avoir attrapé une `InterruptedException`, mais plutôt continuer l'exécution dans une sorte de boucle de réessai, en sauvegardant le statut d'interruption et en le restaurant avant de retourner (voir un [exemple](http://jcip.net/listings/NoncancelableTask.java) de JCIP). Heureusement, dans la plupart des situations, il n'est pas nécessaire d'écrire un tel code boilerplate : **l'une des méthodes de la classe utilitaire `[Uninterruptibles](https://google.github.io/guava/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/Uninterruptibles.html)` de Guava peut être utilisée.**

11.3. Si une **`InterruptedException`** ou une **`TimeoutException` est attrapée sur un appel `Future.get()`** et que la tâche derrière le future n'a pas d'effets secondaires, c'est-à-dire que `get()` est appelé uniquement pour obtenir et utiliser le résultat dans le contexte du thread actuel plutôt que pour atteindre un effet secondaire, le future est-il [annulé](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/Future.html#cancel(boolean)) ?

Voir [JCIP 7.1] pour plus d'informations sur l'interruption de thread et l'annulation de tâche.

#### 12. Temps

12.1. Les valeurs retournées par **`System.nanoTime()`** sont-elles **comparées de manière à prendre en compte les débordements**, comme décrit dans [la documentation](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/System.html#nanoTime()) pour cette méthode ?

12.2. Le code qui compare les valeurs retournées par **`System.currentTimeMillis()`** a-t-il des **précautions contre le "retour en arrière du temps"** ? Cela peut se produire en raison de la correction de l'heure sur un serveur. Les valeurs qui sont retournées par `currentTimeMillis()` et qui sont inférieures à certaines autres valeurs déjà vues doivent être ignorées. Sinon, il doit y avoir des commentaires expliquant pourquoi ce problème n'est pas pertinent pour le code.

Alternativement, `System.nanoTime()` pourrait être utilisé à la place de `currentTimeMillis()`. Les valeurs retournées par `nanoTime()` n'augmentent jamais (mais peuvent déborder — voir l'élément précédent). Avertissement : `nanoTime()` n'a pas toujours respecté cette garantie dans OpenJDK jusqu'à 8u192 (voir [JDK-8184271](https://bugs.openjdk.java.net/browse/JDK-8184271)). Assurez-vous d'utiliser la distribution la plus récente.

Dans les systèmes distribués, l'ajustement de la [seconde intercalaire](https://en.wikipedia.org/wiki/Leap_second) provoque des problèmes similaires.

12.3. Les **variables qui stockent les limites de temps et les périodes ont-elles des suffixes identifiant leurs unités**, par exemple, "timeoutMillis" (également -Seconds, -Micros, -Nanos) plutôt que simplement "timeout" ? Dans les paramètres de méthode et de constructeur, une alternative est de fournir un paramètre `[TimeUnit](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/TimeUnit.html)` à côté d'un paramètre "timeout". Il s'agit de l'option préférée pour les API publiques.

12.4. **Les méthodes qui ont des paramètres "timeout" et "delay" traitent-elles les arguments négatifs comme des zéros** ? Cela est fait pour respecter le principe de la moindre surprise car toutes les méthodes bloquantes temporisées dans les classes de `java.util.concurrent.*` suivent cette convention.

#### 13. Sécurité des threads des Cleaners et du code natif

13.1. Si une classe gère des ressources natives et emploie `java.lang.ref.Cleaner` (ou `sun.misc.Cleaner` ; ou remplace `Object.finalize()`) pour s'assurer que les ressources sont libérées lorsque les objets de la classe sont collectés par le garbage collector, et que la classe implémente `Closeable` avec la même logique de nettoyage exécutée directement depuis `close()` plutôt que via `Cleanable.clean()` (ou `sun.misc.Cleaner.clean()`) pour pouvoir distinguer entre un `close()` explicite et un nettoyage via un cleaner (par exemple, `clean()` peut logger un avertissement sur l'objet n'étant pas fermé explicitement avant de libérer les ressources), est-il garanti que même si **la logique de nettoyage est appelée de manière concurrente depuis plusieurs threads, le nettoyage réel est effectué une seule fois** ? La logique de nettoyage dans de telles classes doit évidemment être idempotente car elle est généralement censée être appelée deux fois : la première fois depuis la méthode `close()` et la deuxième fois depuis le cleaner ou `finalize()`. Le piège est que le nettoyage _doit être idempotent de manière concurrente, même si `close()` n'est jamais appelé de manière concurrente sur les objets de la classe_. Cela est dû au fait que le garbage collector peut considérer l'objet comme devenant inaccessible avant la fin d'un appel `close()` et initier le nettoyage via le cleaner ou `finalize()` tandis que `close()` est encore en cours d'exécution.

Alternativement, `close()` pourrait simplement déléguer à `Cleanable.clean()` (`sun.misc.Cleaner.clean()`) qui est thread-safe. Mais alors il est impossible de distinguer entre le nettoyage explicite et automatique.

Voir aussi [JLS 12.6.2](https://docs.oracle.com/javase/specs/jls/se11/html/jls-12.html#jls-12.6.2).

13.2. Dans une classe avec un certain état natif qui a un cleaner ou remplace `finalize()`, les **corps de toutes les méthodes qui interagissent avec l'état natif sont-ils enveloppés avec**  
**`try { ... } finally { Reference.reachabilityFence(this); }`**,  
incluant les constructeurs et la méthode `close()`, mais excluant `finalize()` ? Cela est nécessaire car un objet pourrait devenir inaccessible et la mémoire native pourrait être libérée par le cleaner tandis que la méthode qui interagit avec l'état natif est en cours d'exécution, ce qui pourrait conduire à une utilisation après libération ou à une corruption de la mémoire JVM.

`reachabilityFence()` dans `close()` élimine également la course entre `close()` et le nettoyage exécuté via le cleaner ou `finalize()` (voir l'élément précédent), mais il peut être judicieux de conserver les précautions de sécurité des threads dans la procédure de nettoyage, surtout si la classe en question appartient à l'API publique du projet, car sinon si `close()` est appelé de manière accidentelle ou malveillante de manière concurrente depuis plusieurs threads, la JVM pourrait planter en raison d'une double libération de mémoire ou, pire, la mémoire pourrait être silencieusement corrompue, tandis que la promesse de la plateforme Java est que, quelle que soit la bogue du code, tant qu'il passe la vérification du bytecode, les exceptions levées devraient être le pire résultat possible, mais la machine virtuelle ne devrait pas planter. L'élément 13.4 souligne également ce principe.

`Reference.reachabilityFence()` a été ajouté dans JDK 9. Si le projet cible JDK 8 et Hotspot JVM, [toute méthode avec un corps vide est une émulation efficace de `reachabilityFence()`](http://mail.openjdk.java.net/pipermail/core-libs-dev/2018-February/051312.html).

Voir la documentation pour `[Reference.reachabilityFence()](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/ref/Reference.html#reachabilityFence(java.lang.Object))` et [cette discussion](http://cs.oswego.edu/pipermail/concurrency-interest/2015-December/014609.html) dans la liste de diffusion concurrency-interest pour plus d'informations.

13.3. N'y a-t-il pas de classes qui ont **des cleaners ou remplacent `finalize()` non pas pour libérer des ressources natives**, mais simplement pour retourner des objets heap à certains pools, ou simplement pour signaler que certains objets heap ne sont pas retournés à certains pools ? Il s'agit d'un anti-pattern en raison de la complexité énorme d'utilisation correcte des cleaners et de `finalize()` (voir les deux éléments précédents) et de l'impact négatif sur les performances (surtout de `finalize()`), qui pourrait être encore plus grand que l'impact de ne pas retourner les objets à un certain pool et ainsi augmenter légèrement le taux d'allocation de garbage dans l'application. Si ce dernier problème s'avère important, il devrait être mieux diagnostiqué avec [async-profiler](https://github.com/jvm-profiling-tools/async-profiler) en mode profiling d'allocation (`-e alloc`) plutôt qu'en enregistrant des cleaners ou en remplaçant `finalize()`.

Ce conseil s'applique également lorsque les objets poolés sont des ByteBuffers directs ou d'autres wrappers Java de chunks de mémoire native. `[async-profiler -e malloc](https://stackoverflow.com/questions/53576163/interpreting-jemaloc-data-possible-off-heap-leak/53598622#53598622)` pourrait être utilisé dans de tels cas pour détecter les fuites de mémoire directe.

13.4. Si certaines **classes ont un certain état en mémoire native et sont utilisées activement dans du code concurrent, ou appartiennent à l'API publique du projet, a-t-il été envisagé de les rendre thread-safe** ? Comme décrit dans l'élément 13.2, si des objets de telles classes sont accédés par inadvertance depuis plusieurs threads sans synchronisation appropriée, une corruption de mémoire et des plantages de la JVM pourraient en résulter. C'est pourquoi les classes du JDK telles que `[java.util.zip.Deflater](http://hg.openjdk.java.net/jdk/jdk/file/a772e65727c5/src/java.base/share/classes/java/util/zip/Deflater.java)` utilisent la synchronisation en interne malgré le fait que les objets `Deflater` ne sont pas destinés à être utilisés de manière concurrente depuis plusieurs threads.

Notez que rendre les classes avec un certain état en mémoire native thread-safe implique également que **l'état natif doit être publié en toute sécurité dans les constructeurs**. Cela signifie que soit l'état natif doit être stocké exclusivement dans des champs `final`, soit `[VarHandle.storeStoreFence()](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/invoke/VarHandle.html#storeStoreFence())` doit être appelé dans les constructeurs après l'initialisation complète de l'état natif. Si le projet cible JDK 9 et que `VarHandle` n'est pas disponible, le même effet pourrait être obtenu en enveloppant les corps des constructeurs dans `synchronized (this) { ... }`.

#### 14. Streams parallèles

14.1. Pour chaque utilisation de Streams parallèles via `Collection.parallelStream()` ou `Stream.parallel()` : **est-il expliqué pourquoi le `Stream` parallèle est utilisé dans un commentaire précédant l'opération de stream** ? Y a-t-il des calculs approximatifs ou des références à des benchmarks montrant que le coût total en temps CPU de la computation parallélisée dépasse [100 microsecondes](http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html) ?

Y a-t-il une note dans le commentaire indiquant que les opérations parallélisées sont généralement sans E/S et non bloquantes, conformément à l'élément 10.4 ? Ce dernier pourrait être évident momentanément, mais à mesure que la base de code évolue, la logique appelée à partir de l'opération de stream parallèle pourrait devenir bloquante par accident. Sans commentaire, il est plus difficile de remarquer la divergence et le fait que la computation n'est plus adaptée aux Streams parallèles. Cela peut être corrigé en appelant à nouveau la version non bloquante de la logique ou en utilisant un `Stream` séquentiel simple au lieu d'un `Stream` parallèle.

Bonus : [forbidden-apis](https://github.com/policeman-tools/forbidden-apis) est-il configuré pour le projet et `java.util.StringBuffer`, `java.util.Random` et `Math.random()` sont-ils interdits ? `StringBuffer` et `Random` sont thread-safe et toutes leurs méthodes sont `synchronized`, ce qui n'est jamais utile en pratique et inhibe uniquement les performances. Dans OpenJDK, `Math.random()` délègue à une instance statique globale `Random`. `StringBuilder` doit être utilisé à la place de `StringBuffer`, `ThreadLocalRandom` ou `SplittableRandom` doivent être utilisés à la place de `Random`.

### Liste de lecture

* [JLS] Spécification du langage Java, [Modèle de mémoire](https://docs.oracle.com/javase/specs/jls/se11/html/jls-17.html#jls-17.4) et sémantique des champs `[final](https://docs.oracle.com/javase/specs/jls/se11/html/jls-17.html#jls-17.5)`.
* [EJ] « Effective Java » de Joshua Bloch, Chapitre 11. Concurrency.
* [JCIP] « Java Concurrency in Practice » de Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, et Doug Lea.
* Articles d'Aleksey Shipilëv :  
 [Safe Publication and Safe Initialization in Java](https://shipilev.net/blog/2014/safe-public-construction/)  
 [Java Memory Model Pragmatics](https://shipilev.net/blog/2014/jmm-pragmatics/)  
 [Close Encounters of The Java Memory Model Kind](https://shipilev.net/blog/2016/close-encounters-of-jmm-kind/)
* [When to use parallel streams](http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html) écrit par Doug Lea, avec l'aide de Brian Goetz, Paul Sandoz, Aleksey Shipilev, Heinz Kabutz, Joe Bowbeer, …
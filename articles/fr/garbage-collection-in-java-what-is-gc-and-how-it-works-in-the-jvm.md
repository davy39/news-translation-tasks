---
title: Garbage Collection en Java – Qu'est-ce que le GC et comment il fonctionne dans
  la JVM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-22T17:26:46.000Z'
originalURL: https://freecodecamp.org/news/garbage-collection-in-java-what-is-gc-and-how-it-works-in-the-jvm
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/GC.png
tags:
- name: Java
  slug: java
seo_title: Garbage Collection en Java – Qu'est-ce que le GC et comment il fonctionne
  dans la JVM
seo_desc: 'By Siben Nayak

  In my previous article, I wrote about the Java Virtual Machine (JVM) and explained
  its architecture. As part of the Execution Engine component, I also briefly covered
  the Java Garbage Collector (GC).

  In this article, you will learn mor...'
---

Par Siben Nayak

Dans mon [article](https://www.freecodecamp.org/news/jvm-tutorial-java-virtual-machine-architecture-explained-for-beginners/) précédent, j'ai écrit sur la Java Virtual Machine (JVM) et expliqué son architecture. Dans le cadre du composant Execution Engine, j'ai également brièvement abordé le Java Garbage Collector (GC).

Dans cet article, vous en apprendrez davantage sur le Garbage Collector, son fonctionnement et les différents types de GC disponibles en Java ainsi que leurs avantages. Je couvrirai également certains des nouveaux Garbage Collectors expérimentaux disponibles dans les dernières versions de Java.

## Qu'est-ce que le Garbage Collection en Java ?

Le Garbage Collection est le processus de récupération de la mémoire inutilisée à l'exécution en détruisant les objets inutilisés.

Dans des langages comme C et C++, le programmeur est responsable de la création et de la destruction des objets. Parfois, le programmeur peut oublier de détruire les objets inutiles, et la mémoire qui leur est allouée n'est pas libérée. La mémoire utilisée par le système continue de croître et finalement, il n'y a plus de mémoire disponible dans le système pour l'allocation. De telles applications souffrent de "_fuites de mémoire_".

Après un certain point, une mémoire suffisante n'est plus disponible pour la création de nouveaux objets, et le programme entier se termine anormalement en raison d'erreurs OutOfMemoryErrors.

Vous pouvez utiliser des méthodes comme `free()` en C, et `delete()` en C++ pour effectuer le Garbage Collection. En Java, le garbage collection se fait automatiquement pendant la durée de vie d'un programme. Cela élimine le besoin de désallouer la mémoire et évite ainsi les fuites de mémoire.

Le Garbage Collection en Java est le processus par lequel les programmes Java effectuent une gestion automatique de la mémoire. Les programmes Java se compilent en bytecode qui peut être exécuté sur une Java Virtual Machine (JVM).

Lorsque les programmes Java s'exécutent sur la JVM, les objets sont créés sur le tas, qui est une portion de mémoire dédiée au programme.

Au cours de la durée de vie d'une application Java, de nouveaux objets sont créés et libérés. Finalement, certains objets ne sont plus nécessaires. On peut dire qu'à tout moment, la mémoire du tas se compose de deux types d'objets :

* _Vivants_ - ces objets sont utilisés et référencés depuis un autre endroit
* _Morts_ - ces objets ne sont plus utilisés ou référencés depuis un autre endroit

Le garbage collector trouve ces objets inutilisés et les supprime pour libérer de la mémoire.

## Comment Dereferencer un Objet en Java

L'objectif principal du Garbage Collection est de libérer la mémoire du tas en détruisant les objets qui ne contiennent pas de référence. Lorsqu'il n'y a plus de références à un objet, il est considéré comme mort et n'est plus nécessaire. Ainsi, la mémoire occupée par l'objet peut être récupérée.

Il existe diverses façons de libérer les références à un objet pour en faire un candidat pour le Garbage Collection. Certaines d'entre elles sont :

### En rendant une référence nulle

```java
Student student = new Student();
student = null;
```

### En assignant une référence à une autre

```java
Student studentOne = new Student();
Student studentTwo = new Student();
studentOne = studentTwo; // maintenant le premier objet référencé par studentOne est disponible pour le garbage collection
```

### En utilisant un objet anonyme

```java
register(new Student());
```

## Comment fonctionne le Garbage Collection en Java ?

Le garbage collection en Java est un processus automatique. Le programmeur n'a pas besoin de marquer explicitement les objets à supprimer.

L'implémentation du garbage collection réside dans la JVM. Chaque JVM peut implémenter sa propre version de garbage collection. Cependant, elle doit respecter la spécification standard de la JVM qui consiste à travailler avec les objets présents dans la mémoire du tas, à marquer ou à identifier les objets inaccessibles, et à les détruire avec compaction.

## Qu'est-ce que les Garbage Collection Roots en Java ?

Les garbage collectors fonctionnent sur le concept de _Garbage Collection Roots_ (GC Roots) pour identifier les objets vivants et morts.

Des exemples de tels Garbage Collection roots sont :

* Classes chargées par le chargeur de classes système (et non par des chargeurs de classes personnalisés)
* Threads actifs
* Variables locales et paramètres des méthodes actuellement en cours d'exécution
* Variables locales et paramètres des méthodes JNI
* Référence globale JNI
* Objets utilisés comme moniteur pour la synchronisation
* Objets retenus par la JVM pour ses propres besoins

Le garbage collector parcourt tout le graphe d'objets en mémoire, en commençant par ces Garbage Collection Roots et en suivant les références des racines vers d'autres objets.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-76.png)

## Phases du Garbage Collection en Java

Une implémentation standard du Garbage Collection implique trois phases :

### Marquer les objets comme vivants

Dans cette étape, le GC identifie tous les objets _vivants_ en mémoire en parcourant le graphe d'objets.

Lorsque le GC visite un objet, il le marque comme accessible et donc vivant. Chaque objet que le garbage collector visite est marqué comme vivant. Tous les objets qui ne sont pas accessibles depuis les GC Roots sont considérés comme des déchets et sont considérés comme des candidats pour le garbage collection.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-82.png)

### Balayer les objets morts

Après la phase de marquage, nous avons l'espace mémoire qui est occupé par des objets vivants (visités) et morts (non visités). La phase de balayage libère les fragments de mémoire qui contiennent ces objets morts.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-83.png)

### Compacter les objets restants en mémoire

Les objets morts qui ont été supprimés pendant la phase de balayage ne sont pas nécessairement les uns à côté des autres. Ainsi, vous pouvez vous retrouver avec un espace mémoire fragmenté.

La mémoire peut être compactée après que le garbage collector ait supprimé les objets morts, de sorte que les objets restants soient dans un bloc contigu au début du tas.

Le processus de compaction facilite l'allocation de mémoire aux nouveaux objets de manière séquentielle.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-85.png)

## Qu'est-ce que le Generational Garbage Collection en Java ?

Les Garbage Collectors Java implémentent une _stratégie de garbage collection générationnelle_ qui catégorise les objets par âge.

Devoir marquer et compacter tous les objets dans une JVM est inefficace. À mesure que de plus en plus d'objets sont alloués, la liste des objets grandit, ce qui entraîne des temps de garbage collection plus longs. L'analyse empirique des applications a montré que la plupart des objets en Java ont une durée de vie courte.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/ObjectLifetime.gif)
_Source : oracle.com_

Dans l'exemple ci-dessus, l'axe Y montre le nombre d'octets alloués et l'axe X montre le nombre d'octets alloués au fil du temps. Comme vous pouvez le voir, de moins en moins d'objets restent alloués au fil du temps.

En fait, la plupart des objets ont une durée de vie très courte, comme le montrent les valeurs plus élevées sur le côté gauche du graphique. C'est pourquoi Java catégorise les objets en générations et effectue le garbage collection en conséquence.

La zone de mémoire du tas dans la JVM est divisée en trois sections :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-70.png)

## Young Generation

Les objets nouvellement créés commencent dans la Young Generation. La Young Generation est elle-même subdivisée en :

* **Eden space** - tous les nouveaux objets commencent ici, et la mémoire initiale leur est allouée
* **Survivor spaces (FromSpace et ToSpace)** - les objets sont déplacés ici depuis Eden après avoir survécu à un cycle de garbage collection.

Lorsque les objets sont garbage collectés depuis la Young Generation, il s'agit d'un _événement de garbage collection mineur_.

Lorsque l'espace Eden est rempli d'objets, un Minor GC est effectué. Tous les objets morts sont supprimés, et tous les objets vivants sont déplacés vers l'un des espaces survivor. Le Minor GC vérifie également les objets dans un espace survivor, et les déplace vers l'autre espace survivor.

Prenons la séquence suivante comme exemple :

1. Eden contient tous les objets (vivants et morts)
2. Un Minor GC se produit - tous les objets morts sont supprimés d'Eden. Tous les objets vivants sont déplacés vers S1 (FromSpace). Eden et S2 sont maintenant vides.
3. De nouveaux objets sont créés et ajoutés à Eden. Certains objets dans Eden et S1 deviennent morts.
4. Un Minor GC se produit - tous les objets morts sont supprimés d'Eden et S1. Tous les objets vivants sont déplacés vers S2 (ToSpace). Eden et S1 sont maintenant vides.

Ainsi, à tout moment, l'un des espaces survivor est toujours vide. Lorsque les objets survivants atteignent un certain seuil de déplacement entre les espaces survivor, ils sont déplacés vers la Old Generation.

Vous pouvez utiliser le flag `-Xmn` pour définir la taille de la Young Generation.

## Old Generation

Les objets qui ont une longue durée de vie sont finalement déplacés de la Young Generation vers la Old Generation. Cela est également connu sous le nom de Tenured Generation, et contient des objets qui sont restés dans les espaces survivor pendant une longue période.

Il existe un seuil défini pour la durée de vie d'un objet qui décide combien de cycles de garbage collection il peut survivre avant d'être déplacé vers la Old Generation.

Lorsque les objets sont garbage collectés depuis la Old Generation, il s'agit d'un _événement de garbage collection majeur_.

Vous pouvez utiliser les flags `-Xms` et `-Xmx` pour définir la taille initiale et maximale de la mémoire Heap.

Puisque Java utilise le garbage collection générationnel, plus un objet survit à des événements de garbage collection, plus il est promu dans le tas. Il commence dans la young generation et finit par se retrouver dans la tenured generation s'il survit suffisamment longtemps.

Considérez l'exemple suivant pour comprendre la promotion des objets entre les espaces et les générations :

Lorsque qu'un objet est créé, il est d'abord placé dans l'**Eden space** de la **young generation**. Une fois qu'un garbage collection mineur se produit, les objets vivants de l'**Eden** sont promus dans le **FromSpace**. Lorsque le garbage collection mineur suivant se produit, les objets vivants de l'**Eden** et du **FromSpace** sont déplacés vers le **ToSpace**.

Ce cycle continue pendant un nombre spécifique de fois. Si l'objet est toujours utilisé après ce point, le prochain cycle de garbage collection le déplacera vers l'espace **old generation**.

## Permanent Generation

Les métadonnées telles que les classes et les méthodes sont stockées dans la Permanent Generation. Elle est peuplée par la JVM à l'exécution en fonction des classes utilisées par l'application. Les classes qui ne sont plus utilisées peuvent être garbage collectées depuis la Permanent Generation.

Vous pouvez utiliser les flags `-XX:PermGen` et `-XX:MaxPermGen` pour définir la taille initiale et maximale de la Permanent Generation.

## MetaSpace

À partir de Java 8, l'espace mémoire **MetaSpace** remplace l'espace **PermGen**. L'implémentation diffère de celle du PermGen et cet espace du tas est maintenant redimensionné automatiquement.

Cela évite le problème des applications qui manquent de mémoire en raison de la taille limitée de l'espace PermGen du tas. La mémoire Metaspace peut être garbage collectée et les classes qui ne sont plus utilisées peuvent être automatiquement nettoyées lorsque le Metaspace atteint sa taille maximale.

%[https://youtu.be/X1DkoRGVRp4]

## Types de Garbage Collectors dans la Java Virtual Machine

Le garbage collection rend la mémoire Java efficace car il supprime les objets non référencés de la mémoire heap et libère de l'espace pour de nouveaux objets.

La Java Virtual Machine possède huit types de garbage collectors. Examinons chacun d'eux en détail.

## Serial GC

Il s'agit de l'implémentation la plus simple du GC et elle est conçue pour les petites applications s'exécutant dans des environnements monothread. Tous les événements de garbage collection sont effectués en série dans un seul thread. La compaction est exécutée après chaque garbage collection.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-68.png)

Lorsqu'il s'exécute, il entraîne un événement "stop the world" où l'ensemble de l'application est mis en pause. Comme l'ensemble de l'application est gelé pendant le garbage collection, il n'est pas recommandé dans un scénario réel où des latences faibles sont requises.

L'argument JVM pour utiliser le Serial Garbage Collector est `-XX:+UseSerialGC`.

## Parallel GC

Le collecteur parallèle est destiné aux applications avec des ensembles de données de taille moyenne à grande qui s'exécutent sur du matériel multiprocesseur ou multithread. Il s'agit de l'implémentation par défaut du GC dans la JVM et est également connu sous le nom de Throughput Collector.

Plusieurs threads sont utilisés pour le garbage collection mineur dans la Young Generation. Un seul thread est utilisé pour le garbage collection majeur dans la Old Generation.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-66.png)

L'exécution du Parallel GC provoque également un événement "stop the world" et l'application se fige. Comme il est plus adapté à un environnement multithread, il peut être utilisé lorsqu'il y a beaucoup de travail à faire et que des pauses longues sont acceptables, par exemple l'exécution d'un travail par lots.

L'argument JVM pour utiliser le Parallel Garbage Collector est `-XX:+UseParallelGC`.

## Parallel Old GC

Il s'agit de la version par défaut du Parallel GC depuis Java 7u4. Il est identique au Parallel GC sauf qu'il utilise plusieurs threads pour la Young Generation et la Old Generation.

L'argument JVM pour utiliser le Parallel Garbage Collector est `-XX:+UseParallelOldGC`.

## CMS (Concurrent Mark Sweep) GC

Il est également connu sous le nom de collecteur concurrent à faible pause. Plusieurs threads sont utilisés pour le garbage collection mineur en utilisant le même algorithme que Parallel. Le garbage collection majeur est multithread, comme Parallel Old GC, mais CMS s'exécute de manière concurrente avec les processus de l'application pour minimiser les événements "stop the world".

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-67.png)

En raison de cela, le collecteur CMS utilise plus de CPU que les autres GC. Si vous pouvez allouer plus de CPU pour de meilleures performances, alors le collecteur de déchets CMS est un meilleur choix que le collecteur parallèle. Aucune compaction n'est effectuée dans CMS GC.

L'argument JVM pour utiliser le Concurrent Mark Sweep Garbage Collector est `-XX:+UseConcMarkSweepGC`.

## G1 (Garbage First) GC

G1GC était destiné à remplacer CMS et a été conçu pour les applications multithread qui disposent d'une grande taille de tas disponible (plus de 4 Go). Il est parallèle et concurrent comme CMS, mais il fonctionne assez différemment sous le capot par rapport aux anciens garbage collectors.

Bien que G1 soit également générationnel, il n'a pas de régions séparées pour les jeunes et les anciennes générations. Au lieu de cela, chaque génération est un ensemble de régions, ce qui permet un redimensionnement de la jeune génération de manière flexible.

Il partitionne le tas en un ensemble de régions de taille égale (1 Mo à 32 Mo - selon la taille du tas) et utilise plusieurs threads pour les analyser. Une région peut être soit une ancienne région, soit une jeune région à tout moment pendant l'exécution du programme.

Après la phase de marquage, G1 sait quelles régions contiennent le plus d'objets de déchets. Si l'utilisateur est intéressé par des temps de pause minimaux, G1 peut choisir d'évacuer uniquement quelques régions. Si l'utilisateur ne s'inquiète pas des temps de pause ou a indiqué un objectif de temps de pause assez grand, G1 peut choisir d'inclure plus de régions.

Puisque G1GC identifie les régions avec le plus de déchets et effectue le garbage collection sur cette région en premier, il est appelé Garbage First.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-88.png)

Outre les régions de mémoire Eden, Survivor et Old, il existe deux autres types de régions présentes dans le G1GC :

* _Humongous_ - utilisé pour les objets de grande taille (plus de 50 % de la taille du tas)
* _Available_ - l'espace non utilisé ou non alloué

L'argument JVM pour utiliser le G1 Garbage Collector est `-XX:+UseG1GC`.

## Epsilon Garbage Collector

Epsilon est un garbage collector qui ne fait rien (no-op) et qui a été publié dans le cadre de JDK 11. Il gère l'allocation de mémoire mais n'implémente aucun mécanisme réel de récupération de mémoire. Une fois que le tas Java disponible est épuisé, la JVM s'arrête.

Il peut être utilisé pour des applications ultra-sensibles à la latence, où les développeurs connaissent exactement l'empreinte mémoire de l'application, ou même ont des applications (presque) complètement sans garbage. L'utilisation du GC Epsilon dans tout autre scénario est par ailleurs déconseillée.

L'argument JVM pour utiliser le Epsilon Garbage Collector est `-XX:+UnlockExperimentalVMOptions -XX:+UseEpsilonGC`.

## Shenandoah

Shenandoah est un nouveau GC qui a été publié dans le cadre de JDK 12. L'avantage clé de Shenandoah sur G1 est qu'il effectue davantage de son travail de cycle de garbage collection de manière concurrente avec les threads de l'application. G1 ne peut évacuer ses régions de tas que lorsque l'application est en pause, tandis que Shenandoah peut déplacer des objets de manière concurrente avec l'application.

Shenandoah peut compacter les objets vivants, nettoyer les déchets et libérer la RAM presque immédiatement après avoir détecté de la mémoire libre. Comme tout cela se produit de manière concurrente pendant que l'application s'exécute, Shenandoah est plus intensif en CPU.

L'argument JVM pour utiliser le Epsilon Garbage Collector est `-XX:+UnlockExperimentalVMOptions -XX:+UseShenandoahGC`.

## ZGC

ZGC est un autre GC qui a été publié dans le cadre de JDK 11 et qui a été amélioré dans JDK 12. Il est destiné aux applications qui nécessitent une faible latence (pauses inférieures à 10 ms) et/ou utilisent un très grand tas (multi-téraoctets).

Les objectifs principaux de ZGC sont la faible latence, la scalabilité et la facilité d'utilisation. Pour y parvenir, ZGC permet à une application Java de continuer à s'exécuter tout en effectuant toutes les opérations de garbage collection. Par défaut, ZGC désalloue la mémoire inutilisée et la renvoie au système d'exploitation.

Ainsi, ZGC apporte une amélioration significative par rapport aux autres GC traditionnels en fournissant des temps de pause extrêmement faibles (généralement dans les 2 ms).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/figure2_600w.jpg)
_Source : oracle.com_

L'argument JVM pour utiliser le Epsilon Garbage Collector est `-XX:+UnlockExperimentalVMOptions -XX:+UseZGC`.

**Note :** Shenandoah et ZGC sont prévus pour devenir des fonctionnalités de production et sortir du stade expérimental dans JDK 15.

## Comment sélectionner le bon Garbage Collector

Si votre application n'a pas d'exigences strictes en matière de temps de pause, vous pouvez simplement exécuter votre application et permettre à la JVM de sélectionner le bon collecteur.

La plupart du temps, les paramètres par défaut devraient fonctionner parfaitement. Si nécessaire, vous pouvez ajuster la taille du tas pour améliorer les performances. Si les performances ne répondent toujours pas à vos objectifs, vous pouvez modifier le collecteur en fonction des exigences de votre application :

* **Serial** - Si l'application a un petit ensemble de données (jusqu'à environ 100 Mo) et/ou elle sera exécutée sur un seul processeur sans exigences de temps de pause
* **Parallel** - Si la performance maximale de l'application est la priorité et qu'il n'y a pas d'exigences de temps de pause ou que des pauses d'une seconde ou plus sont acceptables
* **CMS/G1** - Si le temps de réponse est plus important que le débit global et que les pauses de garbage collection doivent être maintenues inférieures à environ une seconde
* **ZGC** - Si le temps de réponse est une priorité élevée, et/ou vous utilisez un très grand tas

## Avantages du Garbage Collection

Il existe de multiples avantages au garbage collection en Java.

Tout d'abord, il simplifie votre code. Vous n'avez pas à vous soucier des cycles d'assignation et de libération de la mémoire. Vous arrêtez simplement d'utiliser un objet dans votre code, et la mémoire qu'il utilise sera automatiquement récupérée à un moment donné.

Les programmeurs travaillant dans des langages sans garbage collection (comme C et C++) doivent implémenter une gestion manuelle de la mémoire dans leur code.

Cela rend également Java efficace en mémoire car le garbage collector supprime les objets non référencés de la mémoire heap. Cela libère la mémoire heap pour accueillir de nouveaux objets.

Bien que certains programmeurs argumentent en faveur de la gestion manuelle de la mémoire par rapport au garbage collection, le garbage collection est désormais un composant standard de nombreux langages de programmation populaires.

Pour les scénarios dans lesquels le garbage collector a un impact négatif sur les performances, Java offre de nombreuses options pour ajuster le garbage collector afin d'améliorer son efficacité.

## Bonnes pratiques du Garbage Collection

### Éviter les déclenchements manuels

Outre les mécanismes de base du garbage collection, l'un des points les plus importants à comprendre sur le garbage collection en Java est qu'il est non déterministe. Cela signifie qu'il n'y a aucun moyen de prédire quand le garbage collection se produira à l'exécution.

Il est possible d'inclure un indice dans le code pour exécuter le garbage collector avec les méthodes `System.gc()` ou `Runtime.gc()`, mais elles ne garantissent pas que le garbage collector s'exécutera réellement.

### Utiliser des outils pour l'analyse

Si vous n'avez pas assez de mémoire pour exécuter votre application, vous rencontrerez des ralentissements, des temps de garbage collection longs, des événements "stop the world" et finalement des erreurs de manque de mémoire. Cela peut indiquer que votre tas est trop petit, mais peut également signifier que vous avez une fuite de mémoire dans votre application.

Vous pouvez obtenir de l'aide d'un outil de surveillance comme `jstat` ou _Java Flight Recorder_ pour voir si l'utilisation du tas croît indéfiniment, ce qui pourrait indiquer un bug dans votre code.

### Les paramètres par défaut sont bons

Si vous exécutez une petite application Java autonome, vous n'aurez probablement pas besoin d'ajuster le garbage collection. Les paramètres par défaut devraient fonctionner parfaitement.

### Utiliser les flags JVM pour l'ajustement

La meilleure approche pour ajuster le garbage collection Java consiste à définir des flags sur la JVM. Les flags peuvent ajuster le garbage collector à utiliser (par exemple Serial, G1, etc.), la taille initiale et maximale du tas, la taille des sections du tas (par exemple, Young Generation, Old Generation), et plus encore.

### Sélectionner le bon collecteur

La nature de l'application à ajuster est un bon guide initial pour les paramètres. Par exemple, le garbage collector Parallel est efficace mais provoquera fréquemment des événements "stop the world", ce qui le rend plus adapté au traitement backend où les longues pauses pour le garbage collection sont acceptables.

D'un autre côté, le garbage collector CMS est conçu pour minimiser les pauses, ce qui le rend idéal pour les applications basées sur le web où la réactivité est importante.

%[https://youtu.be/4sBhc-pSILs]

## Conclusion

Dans cet article, nous avons discuté du Garbage Collection en Java, de son fonctionnement et de ses différents types.

Pour de nombreuses applications simples, le Garbage Collection en Java n'est pas quelque chose qu'un programmeur doit considérer consciemment. Cependant, pour les programmeurs qui souhaitent faire progresser leurs compétences en Java, il est important de comprendre comment fonctionne le Garbage Collection en Java.

C'est également une question d'entretien très populaire, tant pour les niveaux junior que senior pour les rôles backend.

Merci de m'avoir suivi jusqu'ici. J'espère que vous avez aimé l'article. Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) où je discute régulièrement de la technologie et de la vie. Jetez également un coup d'œil à certains de [mes autres articles](https://www.freecodecamp.org/news/author/theawesomenayak/) et à ma [chaîne YouTube](https://www.youtube.com/channel/UCmWAaPgfWAkl-Jep5mY-NNg?sub_confirmation=1). Bonne lecture. 👋
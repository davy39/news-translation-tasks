---
title: Comment résoudre le problème de code répétitif du modèle Builder
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-14T16:08:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-builder-patterns-boilerplate-problem-2ea97001dbe6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*pWJ2kCkdoFaXrlK6.
tags:
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment résoudre le problème de code répétitif du modèle Builder
seo_desc: 'By Harshdeep S Jawanda

  There is a widely-held belief that one of Java’s primary shortcomings is that writing
  “good” (idiomatic) Java requires a lot of boilerplate code. Just ask any Java practitioner.
  Nowhere is this more evident than in the Builder ...'
---

Par Harshdeep S Jawanda

Il existe une croyance largement répandue selon laquelle l'un des principaux défauts de Java est que l'écriture de code Java "bon" (idiomatique) nécessite beaucoup de code répétitif. Demandez à n'importe quel praticien Java. Nulle part cela n'est plus évident que dans le [modèle Builder](http://www.informit.com/articles/article.aspx?p=1216151&seqNum=2). Dans cet article, je présente deux solutions à ce problème et discute de leurs avantages et inconvénients.

### Une introduction au modèle Builder

Le modèle Builder est idéal pour les classes qui peuvent avoir une initialisation complexe. Il consiste généralement à définir des valeurs pour plusieurs variables, dont certaines peuvent être requises, les autres étant optionnelles. L'utilisation de [méthodes de fabrique statiques](http://www.informit.com/articles/article.aspx?p=1216151&seqNum=1) ou de constructeurs peut conduire au **modèle de constructeur télescopique**, décrit par [Joshua Bloch](https://twitter.com/joshbloch) ("Auteur d'Effective Java, concepteur d'API, type bien", comme le dit son Twitter) comme suit :

> …dans lequel vous fournissez un constructeur avec uniquement les paramètres requis, un autre avec un seul paramètre optionnel, un troisième avec deux paramètres optionnels, et ainsi de suite, culminant dans un constructeur avec tous les paramètres optionnels.

Même s'il n'y a que cinq paramètres requis, mais qu'ils sont tous du même **type**, un développeur peut facilement faire une erreur avec l'ordre des paramètres passés. Cela peut entraîner des bugs subtils, souvent difficiles à trouver.

Le modèle Builder offre une solution élégante à tous ces problèmes. De plus, ce modèle peut aider le développeur à s'assurer que toutes les pré-conditions de l'objet sont satisfaites **avant** de construire l'objet. Cela garantit que l'objet construit est dans un état cohérent.

Mis à part tous ces avantages, l'écriture réelle d'un Builder peut être une tâche assez fastidieuse et répétitive. "Et alors ?!" dites-vous, "Au moins j'obtiens tous ces avantages !" Bien sûr que vous les obtenez… mais revenez me parler quand vous écrivez votre **dixième** Builder sur le même projet.

Alors, examinons quelques autres options.

### Le faire dynamiquement : Lombok

[Lombok](https://projectlombok.org) est un outil/bibliothèque bien connu de nombreux développeurs Java (bien que pas assez, à mon avis). Selon son site web, il "est une bibliothèque Java qui s'intègre automatiquement dans votre éditeur et vos outils de construction, rehaussant votre Java". [Lombok ajoute tant de fonctionnalités grâce à la génération dynamique de code](https://projectlombok.org/features/all) qu'elles ne peuvent simplement pas être couvertes ici. Nous nous concentrerons sur l'annotation `[@Builder](https://projectlombok.org/features/Builder)`.

L'annotation `@Builder` — comme son nom l'indique — peut être utilisée pour générer un Builder pour n'importe quel POJO. Elle peut être utilisée en la plaçant sur la classe, sur un constructeur, ou sur une méthode statique ([voir la documentation](https://projectlombok.org/features/Builder) pour plus de détails). Il suffit de placer l'annotation sur la classe `Person` :

Et par la magie de Lombok, une classe `PersonBuilder` est automatiquement générée instantanément. Nous pouvons maintenant instancier un objet `Person` en utilisant le modèle Builder :

```
Person.builder().firstName("Adam").lastName("Savage")    .city("San Francisco").jobTitle("TV Personality").build();
```

Placer l'annotation `@Builder` sur la classe `Person`

1. crée une classe `PersonBuilder` avec des [setters fluides](https://en.wikipedia.org/wiki/Fluent_interface) pour toutes les propriétés de la classe `Person` et une méthode `build()` pour construire un objet `Person` en utilisant les valeurs définies, et,
2. ajoute une méthode `public static builder()` à la classe `Person` qui retourne une nouvelle instance de `PersonBuilder`.

Placer l'annotation `@Builder` sur un constructeur ou une méthode statique fait les mêmes choses que ci-dessus, mais génère des setters uniquement pour les paramètres listés dans le constructeur/méthode statique.

Ajouter l'annotation `@NonNull` à un champ de la classe `Person` en fait un paramètre **requis**. Ne pas définir sa valeur en utilisant la méthode setter correspondante de `PersonBuilder` lèvera une `NullPointerException` lorsque la méthode `build()` sera appelée.

La beauté de Lombok est que aucun de ce code généré n'est visible dans le fichier source (bien qu'Eclipse montrera la ou les classes générées, les méthodes et les champs dans la vue Outline), le laissant très propre et ordonné. Le développeur n'a besoin de se concentrer que sur les parties importantes d'un POJO, pas sur les détails fastidieux et souvent banals de son implémentation. Apportez n'importe quelle modification au POJO, et Lombok met immédiatement à jour/génère le code pertinent.

#### Les inconvénients de Lombok

Malgré toute cette magie, Lombok n'est pas parfait.

Le plus grand inconvénient de la génération de Builders via Lombok est que si vous avez besoin d'une validation plus complexe qu'une vérification de non-nullité dans votre Builder, vous n'avez pas de chance. Vous pouvez [delombok](https://projectlombok.org/features/delombok), copier le code et le modifier à la main, mais c'est assez fastidieux et annule tout le confort de l'utilisation de Lombok en premier lieu.

[Attribuer des valeurs par défaut aux champs d'un POJO](https://reinhard.codes/2016/07/13/using-lomboks-builder-annotation-with-default-values/) était autrefois très fastidieux :

1. Écrire le squelette de la classe Builder correctement nommée.
2. Écrire le champ correspondant/correctement nommé et le définir à la valeur par défaut.

Cependant, l'attribution de valeurs par défaut est devenue plus facile depuis la version v1.16.16 de Lombok grâce à l'utilisation de l'annotation `@Builder.Default` :

Un autre inconvénient — bien que tout le monde ne soit pas d'accord avec cela — est que la vérification de nullité (si une valeur **requise** a été définie) et le lancement de NPE sont effectués **dans le constructeur** du POJO, et non **avant** la construction du POJO. Je préfère ne pas construire un POJO du tout si ses pré-conditions ne sont pas satisfaites.

Un problème plus général avec Lombok est qu'il ne s'intègre pas bien avec les outils de refactorisation des IDE. Considérez le code suivant (admettons qu'il soit un peu stupide) :

Si nous devions renommer la classe `Person` en `HumanBeing`, le nom généré du Builder correspondant deviendrait `HumanBeingBuilder`. Mais les outils de refactorisation de l'IDE ne parviendront pas à mettre à jour `PersonBuilder` ci-dessus en `HumanBeingBuilder` (au moins dans Eclipse :-) ).

Il existe cependant une solution simple à ce problème : utilisez simplement l'option `builderClassName` de l'annotation `Builder` pour définir un nom fixe pour la classe Builder : `@Builder(builderClassName = "Builder")`. Ensuite, toutes les références à la classe Builder deviendront `Person.Builder`, ce qui sera correctement modifié par la refactorisation en `HumanBeing.Builder`.

### Le faire statiquement : Plugin Eclipse Spark

Le [plugin Eclipse Spark](https://marketplace.eclipse.org/content/spark-builder-generator) vous permet de générer du code Builder pour un POJO en cliquant sur un seul bouton dans la barre d'outils : c'est aussi simple que cela ! Cliquer sur le bouton affichera (optionnellement) la liste des champs parmi lesquels choisir pour utiliser dans le Builder. Le code est généré sous vos yeux et est lisible dans le fichier.

Générer un Builder avec le plugin Spark fait ressembler la classe `Person` à ceci :

Maintenant que tout le code généré est sous vos yeux, vous pouvez le personnaliser (ou non !) à votre guise. Mais ce n'est même pas la meilleure partie de l'histoire de Spark.

Spark vous permet également de générer des [Builders étagés](http://blog.crisp.se/2013/10/09/perlundholm/another-builder-pattern-for-java) : vos yeux s'illuminent de joie la première fois que vous utilisez un Builder étagé et que votre IDE offre exactement les suggestions de complétion automatique correctes ! Expliquer les Builders étagés dépasse le cadre de cet article, alors lisez l'article lié ci-dessus pour en savoir plus.

Aucun des inconvénients de Lombok mentionnés ci-dessus ne s'applique au plugin Spark.

#### Inconvénients du plugin Spark

Tout bien considéré, l'utilisation du plugin Spark produit beaucoup de code visible. Même si vous n'avez pas eu à l'écrire à la main, cela augmente le **poids visuel** du fichier source et le fait paraître grand et compliqué. De nombreux développeurs peuvent ne pas aimer cela par rapport à Lombok.

Un autre problème est que Spark est un outil à un seul tour : générer des Builders est tout ce qu'il peut faire — comparez cela à [toutes les choses que Lombok peut faire](https://projectlombok.org/features/all).

### Alors, lequel choisir ?

L'outil que vous devriez utiliser dépend de votre situation unique et de vos préférences. Je continuerai à préférer Lombok dans la grande majorité des cas, en passant à Spark chaque fois que j'ai besoin d'un contrôle fin.

Lequel choisiriez-vous ?

### Dernier point mais non des moindres...

Si vous avez trouvé cet article utile, n'oubliez pas d'applaudir ;-) !

Les discussions constructives et les corrections sont les bienvenues.
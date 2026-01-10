---
title: 'Un guide rapide et complet sur ''null'' : ce que c''est et comment l''utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T18:16:41.000Z'
originalURL: https://freecodecamp.org/news/a-quick-and-thorough-guide-to-null-what-it-is-and-how-you-should-use-it-d170cea62840
coverImage: https://cdn-media-1.freecodecamp.org/images/1*v3HizBzueVfLUMux26k7sA.png
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Un guide rapide et complet sur ''null'' : ce que c''est et comment l''utiliser'
seo_desc: 'By Christian Neumanns

  What is the meaning of null? How is null implemented? When should you use null in
  your source code, and when should you not use it?


  Introduction

  null is a fundamental concept in many programming languages. It is ubiquitous in
  a...'
---

Par Christian Neumanns

Quelle est la signification de `null` ? Comment `null` est-il implémenté ? Quand devez-vous utiliser `null` dans votre code source, et quand ne devez-vous pas l'utiliser ?

![Image](https://cdn-media-1.freecodecamp.org/images/SlPlSzIxTpuDJvmK9d1gh7crctKc0PGxjkNT)

### Introduction

`null` est un concept fondamental dans de nombreux langages de programmation. Il est omniprésent dans tous types de code source écrits dans ces langages. Il est donc essentiel de bien comprendre l'idée de `null`. Nous devons comprendre sa sémantique et son implémentation, et nous devons savoir comment utiliser `null` dans notre code source.

Les commentaires dans les forums de programmeurs révèlent parfois un peu de confusion avec `null`. Certains programmeurs essaient même d'éviter complètement `null`. Parce qu'ils le considèrent comme 'l'erreur à un million de dollars', un terme inventé par Tony Hoare, l'inventeur de `null`.

Voici un exemple simple : Supposons que l'`email_address` d'Alice pointe vers `null`. Que signifie cela ? Est-ce que cela signifie qu'Alice n'a pas d'adresse email ? Ou que son adresse email est inconnue ? Ou qu'elle est secrète ? Ou est-ce que cela signifie simplement que `email_address` est 'indéfini' ou 'non initialisé' ? Voyons cela. Après avoir lu cet article, tout le monde devrait être en mesure de répondre à de telles questions sans hésitation.

**Note :** Cet article est neutre en termes de langage de programmation - dans la mesure du possible. Les explications sont générales et ne sont pas liées à un langage spécifique. Veuillez consulter les manuels de votre langage de programmation pour des conseils spécifiques sur `null`. Cependant, cet article contient quelques exemples simples de code source montrés en Java. Mais il n'est pas difficile de les traduire dans votre langage préféré.

### Implémentation à l'exécution

Avant de discuter de la signification de `null`, nous devons comprendre comment `null` est implémenté en mémoire à l'exécution.

**Note :** Nous allons examiner une implémentation _typique_ de `null`. L'implémentation réelle dans un environnement donné dépend du langage de programmation et de l'environnement cible, et peut différer de l'implémentation montrée ici.

Supposons que nous ayons l'instruction de code source suivante :

```
String name = "Bob";
```

Ici, nous déclarons une variable de type `String` et avec l'identifiant `name` qui pointe vers la chaîne `"Bob"`.

Dire « pointe vers » est important dans ce contexte, car nous supposons que nous travaillons avec des **types de référence** (et non avec des **types de valeur**). Plus sur cela plus tard.

Pour garder les choses simples, nous ferons les hypothèses suivantes :

* L'instruction ci-dessus est exécutée sur un CPU 16 bits avec un espace d'adressage 16 bits.
* Les chaînes sont encodées en UTF-16. Elles sont terminées par 0 (comme en C ou C++).

L'image suivante montre un extrait de la mémoire après l'exécution de l'instruction ci-dessus :

![Image](https://cdn-media-1.freecodecamp.org/images/eTdrWFVeUC11ONGB8xHgStH5N55hjuDjemAe)
_**Figure 1 : Variable `name` pointe vers "Bob"**_

Les adresses mémoire dans l'image ci-dessus sont choisies arbitrairement et sont sans importance pour notre discussion.

Comme nous pouvons le voir, la chaîne `"Bob"` est stockée à l'adresse B000 et occupe 4 cellules mémoire.

La variable `name` est située à l'adresse A0A1. Le contenu de A0A1 est B000, qui est l'emplacement mémoire de départ de la chaîne `"Bob"`. C'est pourquoi nous disons : La variable `name` _pointe vers_ `"Bob"`.

Jusqu'à présent, tout va bien.

Maintenant, supposons que, après avoir exécuté l'instruction ci-dessus, vous exécutiez ce qui suit :

```
name = null;
```

Maintenant, `name` pointe vers `null`.

Et voici le nouvel état en mémoire :

![Image](https://cdn-media-1.freecodecamp.org/images/sJgbydICZG7fnaM3o8qYN0jicPPoeZmDzMqR)
_**Figure 2 : Variable `name` pointe vers `null`**_

Nous pouvons voir que rien n'a changé pour la chaîne `"Bob"` qui est toujours stockée en mémoire.

Note : La mémoire nécessaire pour stocker la chaîne `"Bob"` peut être libérée plus tard s'il y a un ramasse-miettes et qu'aucune autre référence ne pointe vers `"Bob"`, mais cela est sans importance dans notre discussion.

Ce qui est important, c'est que le contenu de A0A1 (qui représente la valeur de la variable `name`) est maintenant 0000. Donc, la variable `name` ne pointe plus vers `"Bob"`. La valeur 0 (tous les bits à zéro) est une valeur typique utilisée en mémoire pour désigner `null`. Cela signifie qu'il n'y a _aucune valeur associée à `name`_. Vous pouvez aussi y penser comme _l'absence de données_ ou simplement _aucune donnée_.

Note : La valeur mémoire réelle utilisée pour désigner `null` est spécifique à l'implémentation. Par exemple, la [Spécification de la Machine Virtuelle Java](https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-2.html#jvms-2.4) indique à la fin de la section _2.4. « Types et Valeurs de Référence : »_

> _La spécification de la Machine Virtuelle Java ne mandate pas une valeur concrète encodant `null`._

**À retenir :**

Si une référence pointe vers `null`, cela signifie simplement qu'il n'y a aucune valeur associée à celle-ci.

Techniquement parlant, l'emplacement mémoire assigné à la référence contient la valeur 0 (tous les bits à zéro), ou toute autre valeur qui désigne `null` dans l'environnement donné.

### Performance

Comme nous l'avons appris dans la section précédente, les opérations impliquant `null` sont extrêmement rapides et faciles à effectuer à l'exécution.

Il n'y a que deux types d'opérations :

* Initialiser ou définir une référence à `null` (par exemple, `name = null`) : La seule chose à faire est de changer le contenu d'une cellule mémoire (par exemple, le définir à 0).
* Vérifier si une référence pointe vers `null` (par exemple, `if name == null`) : La seule chose à faire est de vérifier si la cellule mémoire de la référence contient la valeur 0.

**À retenir :**

**Les opérations sur `null` sont extrêmement rapides et peu coûteuses.**

### Référence vs Types de Valeur

Jusqu'à présent, nous avons supposé travailler avec des **types de référence**. La raison en est simple : `null` n'existe pas pour les **types de valeur**.

Pourquoi ?

Comme nous l'avons vu précédemment, une référence est un **pointeur** vers une adresse mémoire qui stocke une valeur (par exemple, une chaîne, une date, un client, etc.). Si une référence pointe vers `null`, alors aucune valeur n'est associée à celle-ci.

D'autre part, une valeur est, par définition, la valeur elle-même. Il n'y a pas de pointeur impliqué. Un type de valeur est stocké comme la valeur elle-même. Par conséquent, le concept de `null` n'existe pas pour les types de valeur.

L'image suivante démontre la différence. Sur le côté gauche, vous pouvez voir à nouveau la mémoire dans le cas où la variable `name` est une référence pointant vers "Bob". Le côté droit montre la mémoire dans le cas où la variable `name` est un type de valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/lp5yoXOXWz72BIqJwzRFOqtIbcvckaixOIQg)

Comme nous pouvons le voir, dans le cas d'un type de valeur, la valeur elle-même est directement stockée à l'adresse A0A1 qui est associée à la variable `name`.

Il y aurait beaucoup plus à dire sur les types de référence versus les types de valeur, mais cela est hors du cadre de cet article. Veuillez noter également que certains langages de programmation ne supportent que les types de référence, d'autres ne supportent que les types de valeur, et certains (par exemple, C# et Java) supportent les deux.

**À retenir :**

Le concept de `null` n'existe que pour les **types de référence**. Il n'existe pas pour les **types de valeur**.

### Signification

Supposons que nous ayons un type `person` avec un champ `emailAddress`. Supposons également que, pour une personne donnée que nous appellerons Alice, `emailAddress` pointe vers `null`.

Que signifie cela ? Est-ce que cela signifie qu'Alice n'a pas d'adresse email ? Pas nécessairement.

Comme nous l'avons déjà vu, ce que nous pouvons affirmer, c'est qu'_aucune valeur n'est associée à emailAddress_.

Mais _pourquoi_ n'y a-t-il pas de valeur ? Quelle est la raison pour laquelle `emailAddress` pointe vers `null` ? Si nous ne connaissons pas le contexte et l'historique, alors nous ne pouvons que spéculer. La raison pour `null` _pourrait_ être :

Alice n'a pas d'adresse email. Ou...

Alice a une adresse email, mais :

* elle n'a pas encore été entrée dans la base de données
* elle est secrète (non révélée pour des raisons de sécurité)
* il y a un bug dans une routine qui crée un objet personne sans définir le champ `emailAddress`
* et ainsi de suite.

En pratique, nous connaissons souvent l'application et le contexte. Nous associons intuitivement une signification précise à `null`. Dans un monde simple et sans faille, `null` signifierait simplement qu'Alice n'a effectivement pas d'adresse email.

Lorsque nous écrivons du code, la raison _pour laquelle_ une référence pointe vers `null` est souvent sans importance. Nous vérifions simplement `null` et prenons des mesures appropriées. Par exemple, supposons que nous devons écrire une boucle qui envoie des emails pour une liste de personnes. Le code (en Java) pourrait ressembler à ceci :

```
for ( Person person: persons ) {    if ( person.getEmailAddress() != null ) {        // code pour envoyer un email    } else {        logger.warning("Pas d'adresse email pour " + person.getName());    }}
```

Dans la boucle ci-dessus, nous ne nous soucions pas de la raison pour laquelle `null` est présent. Nous reconnaissons simplement le fait qu'il n'y a pas d'adresse email, nous enregistrons un avertissement, et nous continuons.

**À retenir :**

Si une référence pointe vers `null`, cela signifie toujours qu'il n'y a aucune valeur associée à celle-ci.

Dans la plupart des cas, `null` a une **signification plus spécifique qui dépend du contexte**.

### Pourquoi est-ce `null` ?

Parfois, il _est_ important de savoir _pourquoi_ une référence pointe vers `null`.

Considérons la signature de fonction suivante dans une application médicale :

```
List<Allergy> getAllergiesOfPatient ( String patientId )
```

Dans ce cas, retourner `null` (ou une liste vide) est ambigu. Est-ce que cela signifie que le patient n'a pas d'allergies, ou est-ce que cela signifie qu'un test d'allergie n'a pas encore été effectué ? Ce sont deux cas sémantiquement très différents qui doivent être traités différemment. Sinon, le résultat pourrait être mortel.

Supposons simplement que le patient a des allergies, mais qu'un test d'allergie n'a pas encore été fait et que le logiciel indique au médecin qu'il n'y a 'aucune allergie'. Par conséquent, nous avons besoin d'informations supplémentaires. Nous devons savoir _pourquoi_ la fonction retourne `null`.

Il serait tentant de dire : Eh bien, pour différencier, nous retournons `null` si un test d'allergie n'a pas encore été effectué, et nous retournons une liste vide s'il n'y a pas d'allergies.

NE FAITES PAS CELA !

C'est une mauvaise conception de données pour plusieurs raisons.

Les différentes sémantiques pour retourner `null` par rapport à retourner une liste vide devraient être bien documentées. Et comme nous le savons tous, les commentaires peuvent être erronés (c'est-à-dire incohérents avec le code), obsolètes, ou ils peuvent même être inaccessibles.

Il n'y a pas de protection contre les mauvaises utilisations dans le code client qui appelle la fonction. Par exemple, le code suivant est incorrect, mais il compile sans erreurs. De plus, l'erreur est difficile à repérer pour un lecteur humain. Nous ne pouvons pas voir l'erreur en regardant simplement le code sans considérer le commentaire de `getAllergiesOfPatient` :

```
List<Allergy> allergies = getAllergiesOfPatient ( "123" );				if ( allergies == null ) {    System.out.println ( "Pas d'allergies" );             // <-- FAUX !} else if ( allergies.isEmpty() ) {    System.out.println ( "Test non encore fait" );        // <-- FAUX !} else {    System.out.println ( "Il y a des allergies" );}
```

Le code suivant serait également incorrect :

```
List<Allergy> allergies = getAllergiesOfPatient ( "123" );if ( allergies == null || allergies.isEmpty() ) {    System.out.println ( "Pas d'allergies" );             // <-- FAUX !} else {    System.out.println ( "Il y a des allergies" );}
```

Si la logique `null`/vide de `getAllergiesOfPatient` change à l'avenir, alors le commentaire doit être mis à jour, ainsi que tout le code client. Et il n'y a pas de protection contre l'oubli de l'une de ces modifications.

Si, plus tard, il y a un autre cas à distinguer (par exemple, un test d'allergie est en attente — les résultats ne sont pas encore disponibles), ou si nous voulons ajouter des données spécifiques pour chaque cas, alors nous sommes bloqués.

Donc, la fonction doit retourner plus d'informations qu'une simple liste.

Il existe différentes façons de faire cela, selon le langage de programmation que nous utilisons. Examinons une _solution possible_ en Java.

Afin de différencier les cas, nous définissons un type parent `AllergyTestResult`, ainsi que trois sous-types qui représentent les trois cas (`NotDone`, `Pending`, et `Done`) :

```
interface AllergyTestResult {}
```

```
interface NotDoneAllergyTestResult extends AllergyTestResult {}
```

```
interface PendingAllergyTestResult extends AllergyTestResult {    public Date getDateStarted();}
```

```
interface DoneAllergyTestResult extends AllergyTestResult {    public Date getDateDone();    public List<Allergy> getAllergies(); // null si pas d'allergies                                         // non-vide s'il y a des                                         // allergies}
```

Comme nous pouvons le voir, pour chaque cas, nous pouvons avoir des données spécifiques associées.

Au lieu de simplement retourner une liste, `getAllergiesOfPatient` retourne maintenant un objet `AllergyTestResult` :

```
AllergyTestResult getAllergiesOfPatient ( String patientId )
```

Le code client est maintenant moins sujet aux erreurs et ressemble à ceci :

```
AllergyTestResult allergyTestResult = getAllergiesOfPatient("123");
```

```
if (allergyTestResult instanceof NotDoneAllergyTestResult) {    System.out.println ( "Test non encore fait" );   } else if (allergyTestResult instanceof PendingAllergyTestResult) {    System.out.println ( "Test en attente" );   } else if (allergyTestResult instanceof DoneAllergyTestResult) {    List<Allergy> list = ((DoneAllergyTestResult)         allergyTestResult).getAllergies();    if (list == null) {        System.out.println ( "Pas d'allergies" );    } else if (list.isEmpty()) {        assert false;    } else {        System.out.println ( "Il y a des allergies" );    }} else {    assert false;}
```

Note : Si vous pensez que le code ci-dessus est assez verbeux et un peu difficile à écrire, alors vous n'êtes pas seul. Certains langages modernes nous permettent d'écrire un code conceptuellement similaire beaucoup plus succinctement. Et les langages null-safe distinguent entre les valeurs nullable et non-nullable de manière fiable au moment de la compilation — il n'est pas nécessaire de commenter la nullabilité d'une référence ou de vérifier si une référence déclarée comme non-null a été accidentellement définie à `null`.

**À retenir :**

Si nous devons savoir pourquoi il n'y a pas de valeur associée à une référence, alors **des données supplémentaires doivent être fournies pour différencier les cas possibles**.

### Initialisation

Considérons les instructions suivantes :

```
String s1 = "foo";String s2 = null;String s3;
```

La première instruction déclare une variable `String` `s1` et lui attribue la valeur `"foo"`.

La deuxième instruction attribue `null` à `s2`.

L'instruction la plus intéressante est la dernière. Aucune valeur n'est explicitement attribuée à `s3`. Par conséquent, il est raisonnable de demander : Quel est l'état de `s3` après sa déclaration ? Que se passera-t-il si nous écrivons `s3` sur le périphérique de sortie du système d'exploitation ?

Il s'avère que l'état d'une variable (ou d'un champ de classe) déclarée sans attribution de valeur dépend du langage de programmation. De plus, chaque langage de programmation peut avoir des règles spécifiques pour différents cas. Par exemple, différentes règles s'appliquent pour les types de référence et les types de valeur, les membres statiques et non statiques d'une classe, les variables globales et locales, etc.

Autant que je sache, les règles suivantes sont des variations typiques rencontrées :

* Il est illégal de déclarer une variable sans également lui attribuer une valeur
* Il y a une valeur arbitraire stockée dans `s3`, dépendant du contenu de la mémoire au moment de l'exécution - il n'y a pas de valeur par défaut
* Une valeur par défaut est automatiquement attribuée à `s3`. Dans le cas d'un type de référence, la valeur par défaut est `null`. Dans le cas d'un type de valeur, la valeur par défaut dépend du type de la variable. Par exemple `0` pour les nombres entiers, `false` pour un booléen, etc.
* l'état de `s3` est 'indéfini'
* l'état de `s3` est 'non initialisé', et toute tentative d'utiliser `s3` entraîne une erreur de compilation.

La meilleure option est la dernière. Toutes les autres options sont sujettes aux erreurs et/ou impraticables — pour des raisons que nous ne discuterons pas ici, car cet article se concentre sur `null`.

Par exemple, Java applique la dernière option pour les variables locales. Par conséquent, le code suivant entraîne une erreur de compilation à la deuxième ligne :

```
String s3;System.out.println ( s3 );
```

Sortie du compilateur :

```
error: variable s3 might not have been initialized
```

**À retenir :**

Si une variable est déclarée, mais qu'aucune valeur explicite ne lui est attribuée, **son état dépend de plusieurs facteurs qui sont différents dans différents langages de programmation**.

Dans certains langages, `null` est la valeur par défaut pour les types de référence.

### Quand utiliser `null` (et quand ne pas l'utiliser)

La règle de base est simple : `null` ne doit être autorisé que lorsqu'il est logique qu'une référence d'objet ait 'aucune valeur associée'. (Note : une référence d'objet peut être une variable, une constante, une propriété (champ de classe), un argument d'entrée/sortie, etc.)

Par exemple, supposons un type `person` avec des champs `name` et `dateOfFirstMarriage` :

```
interface Person {    public String getName();    public Date getDateOfFirstMarriage();}
```

Chaque personne a un nom. Par conséquent, il n'est pas logique que le champ `name` ait 'aucune valeur associée'. Le champ `name` est _non-nullable_. Il est illégal de lui attribuer `null`.

D'autre part, le champ `dateOfFirstMarriage` ne représente pas une valeur requise. Tout le monde n'est pas marié. Par conséquent, il est logique que `dateOfFirstMarriage` ait 'aucune valeur associée'. Par conséquent, `dateOfFirstMarriage` est un champ _nullable_. Si le champ `dateOfFirstMarriage` d'une personne pointe vers `null`, cela signifie simplement que cette personne n'a jamais été mariée.

Note : Malheureusement, la plupart des langages de programmation populaires ne distinguent pas les types nullable et non-nullable. Il n'y a aucun moyen de déclarer de manière fiable que `null` ne peut jamais être attribué à une référence d'objet donnée. Dans certains langages, il est possible d'utiliser des annotations, telles que les annotations non standard @Nullable et @NonNullable en Java. Voici un exemple :

```
interface Person {    public @Nonnull String getName();    public @Nullable Date getDateOfFirstMarriage();}
```

Cependant, de telles annotations ne sont pas utilisées par le compilateur pour garantir la null-safety. Néanmoins, elles sont utiles pour le lecteur humain, et elles peuvent être utilisées par les IDE et les outils tels que les analyseurs de code statique.

Il est important de noter que `null` ne doit pas être utilisé pour désigner des conditions d'erreur.

Considérons une fonction qui lit des données de configuration à partir d'un fichier. Si le fichier n'existe pas ou est vide, alors une configuration par défaut doit être retournée. Voici la signature de la fonction :

```
public Config readConfigFromFile ( File file )
```

Que doit-il se passer en cas d'erreur de lecture de fichier ?

Simplement retourner `null` ?

NON !

Chaque langage a sa propre manière standard de signaler les conditions d'erreur et de fournir des données sur l'erreur, telles qu'une description, un type, une trace de pile, etc. De nombreux langages (C#, Java, etc.) utilisent un mécanisme d'exception, et les exceptions doivent être utilisées dans ces langages pour signaler les erreurs d'exécution. `readConfigFromFile` ne doit pas retourner `null` pour désigner une erreur. Au lieu de cela, la signature de la fonction doit être modifiée afin de rendre clair que la fonction peut échouer :

```
public Config readConfigFromFile ( File file ) throws IOException
```

**À retenir :**

Autorisez `null` uniquement si cela a du sens pour une référence d'objet d'avoir 'aucune valeur associée'.

N'utilisez pas `null` pour signaler des conditions d'erreur.

### Null-safety

Considérons le code suivant :

```
String name = null;int l = name.length();
```

À l'exécution, le code ci-dessus entraîne l'infâme **erreur de pointeur null**, car nous essayons d'exécuter une méthode d'une référence qui pointe vers `null`. En C#, par exemple, une `NullReferenceException` est levée, en Java c'est une `NullPointerException`.

L'erreur de pointeur null est désagréable.

C'est le _bug le plus fréquent_ dans de nombreuses applications logicielles, et a été la cause de nombreux problèmes dans l'histoire du développement logiciel. Tony Hoare, l'inventeur de `null`, l'appelle 'l'erreur à un milliard de dollars'.

Mais Tony Hoare (lauréat du prix Turing en 1980 et inventeur de l'algorithme Quicksort), donne également un indice pour une solution dans son [discours](https://qconlondon.com/london-2009/qconlondon.com/london-2009/speaker/Tony+Hoare.html) :

> Les langages de programmation plus récents ... ont introduit des déclarations pour les références non-null. C'est la solution, que j'ai rejetée en 1965.

Contrairement à certaines croyances courantes, le coupable n'est pas `null` en soi. Le problème est le _manque de support pour la gestion de `null`_ dans de nombreux langages de programmation. Par exemple, au moment de l'écriture (mai 2018), aucun des dix langages les plus populaires dans l'[index Tiobe](https://www.tiobe.com/tiobe-index/) ne différencie nativement les types nullable et non-nullable.

Par conséquent, certains nouveaux langages fournissent une null-safety à la compilation et une syntaxe spécifique pour gérer `null` de manière pratique dans le code source. Dans ces langages, le code ci-dessus entraînerait une erreur de compilation. La qualité et la fiabilité du logiciel augmentent considérablement, car l'erreur de pointeur null disparaît de manière satisfaisante.

La null-safety est un sujet fascinant qui mérite son propre article.

**À retenir :**

Dans la mesure du possible, utilisez un langage qui **supporte la null-safety à la compilation**.

Note : Certains langages de programmation (principalement les langages de programmation fonctionnelle comme Haskell) ne supportent pas le concept de `null`. Au lieu de cela, ils utilisent le **modèle Maybe/Optional** pour représenter 'l'absence de valeur'. Le compilateur garantit que le cas 'aucune valeur' est traité explicitement. Par conséquent, les erreurs de pointeur null ne peuvent pas se produire.

### Résumé

Voici un résumé des points clés à retenir :

* Si une référence pointe vers `null`, cela signifie toujours qu'il n'y a _aucune valeur associée à celle-ci_.
* Dans la plupart des cas, `null` a une signification plus spécifique qui dépend du contexte.
* Si nous devons savoir _pourquoi_ il n'y a pas de valeur associée à une référence, alors des données supplémentaires doivent être fournies pour différencier les cas possibles.
* Autorisez `null` uniquement si cela a du sens pour une référence d'objet d'avoir 'aucune valeur associée'.
* N'utilisez pas `null` pour signaler des conditions d'erreur.
* Le concept de `null` n'existe que pour les types de référence. Il n'existe pas pour les types de valeur.
* Dans certains langages, `null` est la valeur par défaut pour les types de référence.
* Les opérations sur `null` sont extrêmement rapides et peu coûteuses.
* Dans la mesure du possible, utilisez un langage qui supporte la null-safety à la compilation.
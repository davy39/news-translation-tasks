---
title: Un regard sur le type de données Optional en Java et quelques anti-modèles
  lors de son utilisation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T09:04:42.000Z'
originalURL: https://freecodecamp.org/news/optional-in-java-and-anti-patterns-using-it-7d87038362ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UEpbSnAgz65SLvAbvR3nbA.jpeg
tags:
- name: clean code
  slug: clean-code
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Un regard sur le type de données Optional en Java et quelques anti-modèles
  lors de son utilisation
seo_desc: 'By Mervyn McCreight

  by Mervyn McCreight and Mehmet Emin Tok


  Overview

  In this article, we are going to talk about experiences we gathered while working
  with Java’s Optional-datatype, which has been introduced with Java 8. During our
  daily business, w...'
---

Par Mervyn McCreight

_par_ [Mervyn McCreight](https://www.freecodecamp.org/news/optional-in-java-and-anti-patterns-using-it-7d87038362ba/undefined) _et_ [Mehmet Emin Tok](https://www.freecodecamp.org/news/optional-in-java-and-anti-patterns-using-it-7d87038362ba/undefined)

![Image](https://cdn-media-1.freecodecamp.org/images/K2LKxHKECSsGZxGXipMfxYpRKElJA1Lp1Goj)

#### Aperçu

Dans cet article, nous allons parler des expériences que nous avons accumulées en travaillant avec le type de données _Optional_ de Java, qui a été introduit avec Java 8. Au cours de notre travail quotidien, nous avons rencontré certains "anti-modèles" que nous souhaitions partager. Notre expérience a été que si vous évitez strictement d'avoir ces modèles dans votre code, les chances sont grandes que vous aboutissiez à une solution plus propre.

#### Optional — la manière Java d'exprimer explicitement l'absence possible d'une valeur

Le but d'_Optional_ est d'exprimer l'absence potentielle d'une valeur avec un type de données au lieu d'avoir la possibilité implicite d'avoir une valeur absente simplement parce que la _référence null_ existe en Java.

Si vous regardez d'autres langages de programmation, qui n'ont pas de _valeur null_, ils décrivent l'absence potentielle d'une valeur à travers des types de données. En Haskell, par exemple, cela est fait en utilisant [Maybe](https://hackage.haskell.org/package/base-4.11.1.0/docs/Data-Maybe.html), ce qui, à mon avis, s'est avéré être une manière efficace de gérer un possible "pas de valeur".

```
data Maybe a = Just a              | Nothing
```

Le fragment de code ci-dessus montre la définition de [Maybe](https://hackage.haskell.org/package/base-4.11.1.0/docs/Data-Maybe.html) en Haskell. Comme vous pouvez le voir, _Maybe a_ est paramétré par la variable de type _a_, ce qui signifie que vous pouvez l'utiliser avec n'importe quel type que vous voulez. Déclarer la possibilité d'une valeur absente en utilisant un type de données, par exemple dans une fonction, vous oblige en tant qu'utilisateur de la fonction à penser aux deux résultats possibles d'un appel de la fonction — le cas où il y a effectivement quelque chose de significatif présent et le cas où ce n'est pas le cas.

Avant qu'_Optional_ ne soit introduit dans Java, la "manière Java" de procéder si vous vouliez décrire le rien était la _référence null_, qui peut être assignée à n'importe quel type. Parce que tout peut être null, il devient obscurci si quelque chose est censé être null (par exemple, si vous voulez que quelque chose représente soit une valeur soit rien) ou non (par exemple, si quelque chose _peut_ être null, parce que tout peut être null en Java, mais dans le flux de l'application, il ne devrait pas être null à aucun moment).

Si vous voulez spécifier que quelque chose peut explicitement être rien avec une certaine sémantique derrière, la définition ressemble à celle où vous attendez que quelque chose soit présent tout le temps. L'inventeur de la référence null [_Sir Tony Hoare_](https://en.wikipedia.org/wiki/Tony_Hoare) a même présenté des excuses pour l'introduction de la référence null.

> Je l'appelle mon erreur d'un milliard de dollars... À cette époque, je concevais le premier système de types complet pour les références dans un langage orienté objet. Mon objectif était de garantir que toutes les utilisations des références devraient être absolument sûres, avec une vérification effectuée automatiquement par le compilateur. Mais je n'ai pas pu résister à la tentation de mettre une référence null, simplement parce que c'était si facile à implémenter. Cela a conduit à d'innombrables erreurs, vulnérabilités et plantages système, qui ont probablement causé un milliard de dollars de douleur et de dommages au cours des quarante dernières années. (Tony Hoare, 2009 — [QCon London](https://qconlondon.com/))

Pour surmonter cette situation problématique, les développeurs ont inventé de nombreuses méthodes comme les annotations _(Nullable, NotNull),_ les conventions de nommage (par exemple, préfixer une méthode avec _find_ au lieu de _get_) ou simplement utiliser des commentaires de code pour indiquer qu'une méthode peut intentionnellement retourner _null_ et que l'appelant devrait se soucier de ce cas. Un bon exemple de cela est la fonction _get_ de l'interface map de Java.

```
public V get(Object key);
```

La définition ci-dessus visualise le problème. Juste par la possibilité implicite que tout peut être une _référence null_, vous ne pouvez pas communiquer l'option que le résultat de cette fonction peut être _rien_ en utilisant la signature de la méthode. Si un utilisateur de cette fonction regarde sa définition, il n'a aucune chance de savoir que cette méthode pourrait retourner une _référence null_ par intention — parce qu'il pourrait être le cas qu'aucun mappage vers la clé fournie n'existe dans l'instance de la map. Et c'est exactement ce que la documentation de cette méthode vous dit :

> Retourne la valeur à laquelle la clé spécifiée est mappée, ou `null` si cette map ne contient aucun mappage pour la clé.

La seule chance de le savoir est de regarder plus profondément dans la documentation. Et vous devez vous souvenir — tout le code n'est pas bien documenté comme cela. Imaginez que vous avez du code interne à la plateforme dans votre projet, qui n'a aucun commentaire, mais vous surprend en retournant une _référence null_ quelque part profondément dans sa pile d'appels. Et c'est là qu'exprimer l'absence potentielle d'une valeur avec un type de données brille.

```
public Optional<V> get(Object key);
```

Si vous regardez la signature de type ci-dessus, il est clairement communiqué que cette méthode PEUT retourner rien — elle vous force même à traiter ce cas, parce qu'il est exprimé avec un type de données spécial.

Avoir _Optional_ en Java est donc bien, mais nous rencontrons quelques pièges si vous utilisez _Optional_ dans votre code. Sinon, l'utilisation d'_Optional_ pourrait rendre votre code encore moins lisible et intuitif (en bref — moins propre). Les parties suivantes couvriront certains modèles que nous avons trouvés être une sorte d'"anti-modèles" pour _Optional_ de Java.

#### Optional dans les Collections ou Streams

Un modèle que nous avons rencontré dans le code avec lequel nous avons travaillé est d'avoir des optionnels vides stockés dans une collection ou comme état intermédiaire à l'intérieur d'un stream. Typiquement, cela était suivi par le filtrage des optionnels vides et même suivi par l'invocation de _Optional::get_, parce que vous n'avez pas vraiment besoin d'avoir une collection d'optionnels. L'exemple de code suivant montre un cas très simplifié de la situation décrite.

```
private Optional<IdEnum> findValue(String id) {   return EnumSet.allOf(IdEnum.class).stream()      .filter(idEnum -> idEnum.name().equals(id)      .findFirst();};
```

```
(...)
```

```
List<String> identifiers = (...)
```

```
List<IdEnum> mapped = identifiers.stream()   .map(id -> findValue(id))   .filter(Optional::isPresent)   .map(Optional::get)   .collect(Collectors.toList());
```

Comme vous pouvez le voir, même dans ce cas simplifié, il devient difficile de comprendre quelle est l'intention de ce code. Vous devez regarder la méthode findValue pour comprendre l'intention de tout cela. Et maintenant, imaginez que la méthode findValue soit plus complexe que de mapper une représentation de chaîne à sa valeur de type énumération.

Il y a aussi une lecture intéressante sur pourquoi vous devriez éviter d'avoir _null_ dans une collection [[UsingAndAvoidingNullExplained](https://github.com/google/guava/wiki/UsingAndAvoidingNullExplained)]. En général, vous n'avez pas vraiment besoin d'avoir un optional vide dans une collection. Cela est dû au fait qu'un optional vide est la représentation de "rien". Imaginez avoir une Liste avec trois éléments et qu'ils sont tous des optionnels vides. Dans la plupart des scénarios, une liste vide serait sémantiquement équivalente.

Alors, que pouvons-nous faire à ce sujet ? Dans la plupart des cas, le plan de _filtrer d'abord avant de mapper_ conduit à un code plus lisible, car il indique directement ce que vous voulez atteindre, au lieu de le cacher derrière une chaîne de _maybe mapping_, _filtrage et puis mapping_.

```
private boolean isIdEnum(String id) {   return Stream.of(IdEnum.values())      .map(IdEnum::name)      .anyMatch(name -> name.equals(id));};
```

```
(...)
```

```
List<String> identifiers = (...)
```

```
List<IdEnum> mapped = identifiers.stream()   .filter(this::isIdEnum)   .map(IdEnum::valueOf)   .collect(Collectors.toList());
```

Si vous imaginez que la méthode _isEnum_ est possédée par IdEnum lui-même, cela deviendrait encore plus clair. Mais pour avoir un exemple de code lisible, elle n'est pas dans l'exemple. Mais juste en lisant l'exemple ci-dessus, vous pouvez facilement comprendre ce qui se passe, même sans vraiment avoir à sauter dans la méthode _isIdEnum_ référencée.

Donc, en bref — si vous n'avez pas besoin de l'absence d'une valeur exprimée dans une liste, vous n'avez pas besoin d'Optional — vous avez juste besoin de son contenu, donc optional est obsolète à l'intérieur des collections.

#### Optional dans les paramètres de méthode

Un autre modèle que nous avons rencontré, surtout lorsque le code est migré de la manière "à l'ancienne" d'utiliser une _référence null_ à l'utilisation du _type optional_, est d'avoir des paramètres typés optional dans les définitions de fonction. Cela se produit typiquement si vous trouvez une fonction qui fait des vérifications de null sur ses paramètres et applique un comportement différent ensuite — ce qui, à mon avis, était une mauvaise pratique avant de toute façon.

```
void addAndUpdate(Something value) {    if (value != null) {      somethingStore.add(value);   }    updateSomething();}
```

Si vous "naïvement" refactorisez cette méthode pour utiliser le type optional, vous pourriez aboutir à un résultat comme celui-ci, utilisant un paramètre typé optional.

```
void addAndUpdate(Optional<Something> maybeValue) {   if (maybeValue.isPresent()) {      somethingStore.add(maybeValue.get());   }   updateSomething();}
```

À mon avis, avoir un paramètre typé optional dans une fonction montre un défaut de conception dans tous les cas. Vous avez de toute façon une décision à prendre si vous faites quelque chose avec le paramètre s'il est présent, ou vous faites autre chose s'il ne l'est pas — et ce flux est caché à l'intérieur de la fonction. Dans un exemple comme ci-dessus, il est plus clair de diviser la fonction en deux fonctions et de les appeler conditionnellement (ce qui correspondrait également au principe "une intention par fonction").

```
private void addSomething(Something value) {   somethingStore.add(value);}
```

```
(...)
```

```
// quelque part, où la fonction aurait été appeléeOptional.ofNullable(somethingOrNull).ifPresent(this::addSomething);updateSomething();
```

Dans mon expérience, si j'ai déjà rencontré des exemples comme ci-dessus dans du code réel, cela valait toujours la peine de refactoriser "jusqu'au bout", ce qui signifie que je n'ai pas de fonctions ou de méthodes avec des paramètres typés optional. J'ai abouti à un flux de code beaucoup plus propre, qui était beaucoup plus facile à lire et à maintenir.

En parlant de cela — à mon avis, une fonction ou une méthode avec un paramètre optional n'a même pas de sens. Je peux avoir une version avec et une version sans le paramètre, et décider au point d'invocation quoi faire, au lieu de le décider caché dans une fonction complexe. Donc, pour moi, cela était un anti-modèle avant (avoir un paramètre qui peut **intentionnellement** être null, et est traité différemment si c'est le cas) et reste un anti-modèle maintenant (avoir un paramètre **typé optional**).

#### Optional::isPresent suivi de Optional::get

L'ancienne manière de penser en Java pour faire de la programmation sécurisée contre les null est d'appliquer des vérifications de null sur les valeurs où vous n'êtes pas sûr qu'elles contiennent effectivement une valeur ou qu'elles référencent une _référence null_.

```
if (value != null) {   doSomething(value);}
```

Pour avoir une expression explicite de la possibilité que _value_ puisse effectivement être soit quelque chose soit rien, on pourrait vouloir refactoriser ce code pour avoir une version typée optional de value.

```
Optional<Value> maybeValue = Optional.ofNullable(value);
```

```
if (maybeValue.isPresent()) {   doSomething(maybeValue.get());}
```

L'exemple ci-dessus montre la version "naïve" du refactoring, que j'ai rencontrée assez souvent dans plusieurs exemples de code. Ce modèle de _isPresent_ suivi d'un _get_ pourrait être causé par l'ancien modèle de vérification de null menant dans cette direction. Avoir écrit tant de vérifications de null nous a somehow entraînés à penser automatiquement dans ce modèle. Mais _Optional_ est conçu pour être utilisé d'une autre manière pour atteindre un code plus lisible. La même sémantique peut simplement être atteinte en utilisant _ifPresent_ de manière plus lisible.

```
Optional<Value> maybeValue = Optional.ofNullable(value);maybeValue.ifPresent(this::doSomething);
```

"Mais que faire si je veux faire autre chose à la place, si la valeur n'est pas présente" pourrait être quelque chose que vous pensez en ce moment. Depuis Java-9, _Optional_ vient avec une solution pour ce cas populaire.

```
Optional.ofNullable(valueOrNull)    .ifPresentOrElse(        this::doSomethingWithPresentValue,        this::doSomethingElse    );
```

Étant donné les possibilités ci-dessus, pour atteindre les cas d'utilisation typiques d'une vérification de null **sans** utiliser _isPresent_ suivi d'un _get_ rend ce modèle sorte d'anti-modèle. _Optional_ est conçu par API pour être utilisé d'une autre manière qui, à mon avis, est plus lisible.

#### Calculs complexes, instantiation d'objets ou mutation d'état dans orElse

L'API Optional de Java vient avec la capacité d'obtenir une valeur garantie à partir d'un optional. Cela est fait avec _orElse_ qui vous donne l'opportunité de définir une valeur par défaut à laquelle revenir, si l'optional que vous essayez de déballer est effectivement vide. Cela est utile chaque fois que vous voulez spécifier un comportement par défaut pour quelque chose qui _peut_ être là, mais qui n'a pas à être fait.

```
// maybeNumber représente un Optional contenant un int ou non.int numberOr42 = maybeNumber.orElse(42);
```

Cet exemple de base illustre l'utilisation de _orElse_. À ce stade, vous êtes garanti d'obtenir soit le nombre que vous avez mis dans l'optional, soit vous obtenez la valeur par défaut de 42. Simple comme cela.

Mais une valeur par défaut significative n'a pas toujours à être une valeur constante simple. Parfois, une valeur par défaut significative peut avoir besoin d'être calculée de manière complexe et/ou chronophage. Cela vous amènerait à extraire ce calcul complexe dans une fonction et à le passer à orElse comme paramètre comme ceci.

```
int numberOrDefault = maybeNumber.orElse(complexCalculation());
```

Maintenant, vous obtenez soit le nombre, soit la valeur par défaut calculée. Cela semble bien. Ou est-ce le cas ? Maintenant, vous devez vous souvenir que Java passe les paramètres à une fonction par le concept de **passage par valeur**. Une conséquence de cela est que dans l'exemple donné, la fonction _complexCalculation_ sera **toujours** évaluée, même si orElse ne sera pas appelé.

Maintenant, imaginez que ce _complexCalculation_ est vraiment complexe et donc chronophage. Il serait **toujours** évalué. Cela causerait des problèmes de performance. Un autre point est, si vous manipulez des objets plus complexes que des valeurs entières ici, cela serait aussi un **gaspillage de mémoire**, parce que vous créeriez toujours une instance de la valeur par défaut. Nécessaire ou non.

Mais parce que nous sommes dans le contexte de Java, cela ne s'arrête pas là. Imaginez que vous n'avez pas une fonction chronophage mais une fonction changeant l'état et que vous voudriez l'invoquer dans le cas où l'Optional est effectivement vide.

```
int numberOrDefault = maybeNumber.orElse(stateChangingStuff());
```

Cela est en fait un exemple encore plus dangereux. Souvenez-vous — comme cela, la fonction sera **toujours** évaluée, nécessaire ou non. Cela signifierait que vous mutiez toujours l'état, même si vous ne voudriez pas vraiment le faire. Mon opinion personnelle à ce sujet est d'éviter d'avoir une mutation d'état dans des fonctions comme celle-ci à tout prix.

Pour avoir la capacité de traiter des problèmes comme décrits, l'API Optional fournit une manière alternative de définir un fallback en utilisant _orElseGet_. Cette fonction prend en fait un _supplier_ qui sera invoqué pour générer la valeur par défaut.

```
// sans référence de méthodeint numberOrDefault = maybeNumber.orElseGet(() -> complex());
```

```
// avec référence de méthodeint numberOrDefault = maybeNumber.orElseGet(Something::complex);
```

Ainsi, le supplier, qui génère en fait la valeur par défaut en invoquant _complex_, ne sera exécuté que lorsque _orElseGet_ est effectivement appelé — ce qui est le cas si l'optional est vide. Ainsi, _complex_ n'est **pas** invoqué lorsqu'il n'est pas nécessaire. Aucun calcul complexe n'est fait sans utiliser réellement son résultat.

Une règle générale pour savoir quand utiliser _orElse_ et quand utiliser _orElseGet_ peut être :  
Si vous remplissez **tous les trois critères**

1. une valeur par défaut simple qui n'est pas difficile à calculer (comme une constante)
2. une valeur par défaut peu consommatrice de mémoire
3. une fonction de valeur par défaut non mutante d'état

alors utilisez _orElse_.   
Sinon, utilisez _orElseGet_.

#### Conclusion (TL;DR)

* Utilisez Optional pour communiquer une absence possible intentionnelle d'une valeur (par exemple, la valeur de retour d'une fonction).
* Évitez d'avoir des Optionals dans les collections ou les streams. Remplissez-les directement avec les valeurs présentes.
* Évitez d'avoir des Optionals comme paramètres de fonctions.
* Évitez Optional::isPresent suivi de Optional::get.
* Évitez les calculs complexes ou changeant l'état dans orElse. Utilisez orElseGet pour cela.

#### Feedback & Questions

Quelle est votre expérience jusqu'à présent avec l'utilisation de Java Optional ? N'hésitez pas à partager vos expériences et à discuter des points que nous avons soulevés dans la section des commentaires.
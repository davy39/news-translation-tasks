---
title: Une introduction à Q# — le langage de Microsoft pour l'informatique quantique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T09:46:07.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-q-64beaff53a00
coverImage: https://cdn-media-1.freecodecamp.org/images/0*urFjQNWX1O2TNzmM.
tags:
- name: Microsoft
  slug: microsoft
- name: General Programming
  slug: programming
- name: quantum computing
  slug: quantum-computing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction à Q# — le langage de Microsoft pour l'informatique quantique
seo_desc: 'By Ankit Sharma

  In this article, I’ll introduce you to Q# — the new programming language from Microsoft
  for quantum computing. We will cover Q# data types, expressions, and statements
  with the help of code snippets.

  Prerequisites

  For an overview of q...'
---

Par Ankit Sharma

Dans cet article, je vais vous présenter Q# — le nouveau langage de programmation de Microsoft pour l'informatique quantique. Nous allons couvrir les types de données Q#, les expressions et les instructions à l'aide d'extraits de code.

#### Prérequis

Pour un aperçu de l'informatique quantique, veuillez consulter mon article précédent : [Une introduction à l'informatique quantique](http://ankitsharmablogs.com/introduction-quantum-computing/). Là, je décris également comment installer le Quantum Development Kit (QDK) dans Visual Studio 2017.

### Qu'est-ce que Q# ?

Selon Microsoft :

> _Q# est un langage de programmation spécifique au domaine, multi-paradigme et évolutif pour l'informatique quantique._

Alors, que signifient réellement ces termes ? Plongeons dans les détails.

* **Évolutif**  
 Q# nous permet d'écrire du code qui peut être exécuté sur des machines de capacités de calcul variées. Nous pouvons l'utiliser pour simuler quelques Qubits sur notre machine locale, ou même des milliers de Qubits pour une application de niveau entreprise.
* **Multi-paradigme**  
 Q# est un langage de programmation multi-paradigme. Il supporte à la fois les styles de programmation fonctionnelle et impérative. Si vous êtes nouveau dans les paradigmes de programmation, je vous suggère de vous référer [ici](https://en.wikipedia.org/wiki/Programming_paradigm).
* **Spécifique au domaine**  
 Q# est un langage de programmation pour l'informatique quantique. Il est utilisé pour écrire des algorithmes et des extraits de code qui sont exécutés sur des processeurs quantiques.

### Commencer avec le développement Q#

Cet article supposera que vous avez déjà installé QDK pour Visual Studio 2017. Si ce n'est pas le cas, vous pouvez [consulter mon article précédent](http://ankitsharmablogs.com/introduction-quantum-computing/) pour des instructions.

Après avoir installé QDK avec succès, nous devons vérifier si Visual Studio 2017 a toutes les dépendances requises installées pour le développement Q#. Pour cela, nous allons cloner et exécuter les programmes d'exemple quantique de GitHub fournis par Microsoft.

Ouvrez VS 2017 et naviguez vers Team >> Manage Connections.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-24.png)

Sélectionnez Clone sous Local Git Repositories et entrez l'URL : [https://github.com/Microsoft/Quantum.git](https://github.com/Microsoft/Quantum.git) et cliquez sur « Clone ».

![Image](https://cdn-media-1.freecodecamp.org/images/krnmAb5hG5Aor-xiXb8QtQztnovD28z8vzPo)

Le dépôt sera cloné sur votre ordinateur local et Visual Studio passera à l'Explorateur de solutions. Il affichera toutes les bibliothèques et exemples clonés.

![Image](https://cdn-media-1.freecodecamp.org/images/d6Yc06IIXElFdgcFtm9Rbh90KGe51XTk6WYE)

Maintenant, ouvrez la solution _QsharpLibraries.sln_.

Si vous êtes invité avec la boîte de dialogue « Install Missing Features », cliquez sur « Install » pour permettre l'installation des fonctionnalités nécessaires. Cela téléchargera et installera F# et d'autres outils utilisés par certains des exemples. Assurez-vous d'être connecté à Internet.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-25.png)

Pour exécuter un programme d'exemple, faites un clic droit sur le projet _TeleportationSample_ dans le dossier « Samples > 0.Introduction folder » de la solution _QsharpLibraries_, puis cliquez sur « Set as Startup Project » et appuyez sur F5.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-26.png)

Si vous voyez un écran de sortie similaire à celui montré ci-dessous, alors félicitations, votre VS 2017 est prêt pour le développement Q#.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-27.png)

Notez que votre écran de sortie peut varier car les données téléportées sont aléatoires. Mais il devrait envoyer 8 rounds de données, toutes étant téléportées avec succès.

### Modèle de type Q#

Comprenons quels sont les différents modèles de types fournis par Q# :

#### Type primitif

* Int : — Il représente l'entier signé 64 bits. Remarquez le 'I' majuscule. Cela contraste avec _int_ en C# avec un 'i' minuscule.
* Double : — Il représente le nombre à virgule flottante en double précision. Cela a également un 'D' majuscule contrairement à _double_ en C#.
* Bool : — Il représente le type booléen et peut prendre deux valeurs — _true_ ou _false_.
* Qubit : — Cela représente le bit quantique. Le Qubit est l'unité fondamentale de traitement de l'information dans les ordinateurs quantiques, similaire à un _bit_ dans les ordinateurs classiques.
* Pauli : — Ce type est utilisé pour désigner l'opération de base pour les rotations et pour spécifier la base d'une mesure.
* Result : — Cela représente le résultat d'une mesure. Cela peut prendre deux valeurs possibles _Zero_ ou _One_.
* Range : — Cela représente une séquence d'entiers.
* String : — Il représente une séquence de caractères Unicode.

#### Type tableau

Nous pouvons créer un type tableau de n'importe quel type primitif valide Q#. Q# ne supporte pas les tableaux multidimensionnels rectangulaires. Au lieu de cela, il ne supporte que les tableaux irréguliers.

`Int[], Qubit[][]`

Par défaut, toutes les variables en Q# sont immuables. Leurs valeurs ne peuvent pas être changées après avoir été liées. Donc, pour créer un tableau dont les valeurs peuvent être définies, nous utiliserons le mot-clé `mutable` :

`mutable myArr = new Int [5];`

Cela créera un tableau d'entiers `myArr` de taille 5. Les éléments d'un nouveau tableau sont initialisés à une valeur par défaut dépendant du type. Dans ce cas, ce sera 0, la valeur par défaut pour un type entier.

Les tableaux passés en arguments sont immuables. Tous les tableaux en Q# sont basés sur zéro. C'est-à-dire, le premier élément d'un tableau `arr` est toujours `arr[0]`.

#### Type tuple

Le type tuple représente un tuple de valeurs de n'importe quel type primitif donné. Il est représenté comme `(T1, T2, T3,…)` où `T1`, `T2`, `T3` sont des types primitifs. Le tuple Q# est immuable. Nous ne pouvons pas changer le contenu du tuple une fois qu'il a été créé.

Une expression de tuple peut contenir des valeurs de plusieurs types primitifs. Donc, un tuple de type `(Int, Double, Result)` est un tuple valide.

Nous pouvons créer un tuple avec un seul élément, comme `(2)`. Cela est connu comme un tuple singleton, et il est considéré comme égal à la valeur du type enfermé. Cette propriété est appelée équivalence de tuple singleton.

Par exemple, `(2)` est un tuple singleton de type `Int`, mais il est considéré comme équivalent à un entier 2.

Nous pouvons créer un type défini par l'utilisateur de n'importe quel type primitif. Nous pouvons également créer un tableau de types définis par l'utilisateur ou l'inclure dans un tuple. Les types définis par l'utilisateur ne peuvent pas avoir de dépendance cyclique les uns avec les autres. Donc, il n'est pas possible de créer une structure de type récursive.

Un type défini par l'utilisateur est un sous-type du type `base`. Cela signifie qu'il peut être utilisé partout où une valeur du type `base` est attendue.

#### Type opération

Une _opération_ Q# est une routine appelable, qui contient du code Q# pour effectuer une opération quantique. Une opération est l'unité de base de l'exécution quantique en Q#. L'_opération_ ne peut prendre qu'une seule valeur en entrée sous la forme d'un tuple. Elle retourne une seule valeur en sortie, spécifiée après un deux-points, et peut être un tuple.

Une opération a une section de corps qui contient l'implémentation de l'opération. Elle peut également avoir des sections adjoint, contrôlé, et adjoint contrôlé. Celles-ci sont utilisées pour spécifier des variantes spécifiques d'opérations appropriées. Les arguments d'une opération sont spécifiés sous la forme d'un tuple, entre parenthèses. Le type de retour de l'opération est spécifié après le deux-points.

Veuillez vous référer à une opération d'exemple ci-dessous :

```
operation AddInteger(a: Int, b: Int): Int {  
    body {  
        mutable c = 0;  
        set c = a + b;  
        return (c);  
    }  
}
```

Ici, nous avons une opération `AddInteger` qui prend un tuple `(Int, Int)` en entrée. Elle retourne une sortie de type `Int` après avoir effectué des opérations d'addition sur les entiers d'entrée.

#### Type fonction

Une fonction Q# est une sous-routine classique utilisée dans un algorithme quantique et ne peut contenir que du code classique (mais pas d'opérations quantiques). Similaire aux opérations Q#, une fonction prendra également une seule valeur en entrée et retournera une seule valeur en sortie. Les deux peuvent être un tuple. Les fonctions ne peuvent pas allouer de qubits ou appeler des opérations.

Regardons un exemple de fonction.

```
function ProductNumber(a: Double, b: Double): Double {  
    mutable c = 0.0;  
    set c = a * b;  
    return (c);  
}
```

Ici, nous avons défini une fonction `ProductNumber`, qui prend un tuple `(Double, Double)` en entrée et retourne une sortie de type `Double` après avoir effectué le produit des valeurs d'entrée. Remarquez également qu'une _fonction_ n'a pas de section de corps, comme dans le cas d'une _opération_.

### Expressions en Q#

Examinons les différentes expressions fournies en Q#.

#### Expressions numériques

Il existe deux types d'expressions numériques fournies par Q# :

* Nombres entiers : ceux-ci sont représentés par Int
* Nombres à virgule flottante : représentés par Double

Pour représenter un entier hexadécimal, nous utilisons le préfixe « 0x ».

Nous pouvons également effectuer des opérations binaires sur des expressions numériques pour former une nouvelle expression numérique. Le type de la nouvelle expression sera `Double` si les deux expressions d'entrée sont des nombres à virgule flottante, ou sera un `Int` si les deux sont des entiers.

Outre les opérations binaires, les expressions numériques supportent également les opérations de modulus, de puissance, de ET binaire, de OU binaire, de XOR binaire et de complément binaire.

#### Expressions Qubit

Les expressions Qubit sont les symboles qui sont liés aux valeurs de qubit ou aux éléments d'un tableau de qubits. Q# ne fournit aucun support pour les littéraux de qubit.

#### Expressions Pauli

Comme nous l'avons discuté précédemment, le type primitif `Pauli` peut prendre quatre valeurs possibles : `PauliI`, `PauliX`, `PauliY` et `PauliZ`. Ce sont toutes des expressions Pauli valides. Nous pouvons également créer un tableau de types Pauli, et les éléments du tableau sont considérés comme des expressions Pauli valides.

Les deux valeurs de résultat possibles `Zero` et `One` sont des expressions Result valides. Un point important à noter est que `One` n'est pas la même chose que l'entier 1, et `Zero` n'est pas la même chose que l'entier 0. De plus, il n'y a pas de conversion directe entre eux.

Cela contraste avec C# où, le booléen `true` est considéré comme le même que l'entier 1 et le booléen `false` est considéré comme le même que l'entier 0.

#### Expressions de plage

Une expression de plage est représentée comme `start..step..stop` où `start`, `step`, `stop` sont tous des entiers. L'expression de plage peut prendre des valeurs comme `start`, `start+step`, `start+step+step` et ainsi de suite jusqu'à ce que `stop` soit dépassé.

Si seulement `start` et `stop` sont mentionnés dans une expression de plage, alors elle prendra la valeur du pas définie à 1 implicitement.

Comprenons cela à l'aide d'un exemple :

* `1..3` — cela indique la plage `1,2,3`. Cela donne `1`, `1+1`, `1+1+1`
* `1..2..6` indique la plage `1,3,5`, ou `1`, `1+2`,`1+2+2`
* `8..-2..3` indique la plage `8,6,4` ou `8`, `8+(-2)`, `8+(-2)+(-2)`

#### Expressions de tableau

En Q#, un tableau peut être représenté comme un ensemble d'expressions d'éléments séparées par des points-virgules et enfermées dans des crochets. Similaire à C#, tous les éléments d'un tableau en Q# doivent avoir le même type.

Donc, `[1;2;3]` est un tableau valide, mais `[1;2.5;Zero]` est un tableau invalide.

Nous pouvons également utiliser l'opérateur '+' pour concaténer deux tableaux du même type.

Donc, `[2;4;6] + [8;10;12]` donnera `[2;4;6;8;10;12]` comme sortie.

Pour trouver la longueur d'un tableau, nous utilisons la fonction intégrée `Length`.

Par exemple, si `myArr` est un tableau d'entiers ayant 5 éléments, alors `Length(myArr)` retournera `5` comme sortie.

### Instructions Q#

Les symboles en Q# peuvent être mutables ou immuables.

Un symbole immuable ne peut pas être changé après avoir été lié. Nous utilisons le mot-clé let pour définir et lier un symbole immuable.

`let i=8;`

Cela liera le symbole `i` comme un entier avec la valeur 8. Si nous essayons de réinitialiser la valeur d'une expression immuable, nous obtiendrons une erreur de compilation.

Donc `set i=10;` donnera une erreur dans ce cas.

La valeur d'un symbole mutable peut être changée après avoir été liée. Nous utilisons le mot-clé `mutable` pour définir et lier un symbole mutable.

`mutable i=8;`

Cela liera le symbole `i` comme un entier avec la valeur 8.

Pour changer la valeur d'un symbole mutable, nous utilisons le mot-clé `set` :

`set i=10;`

Cela mettra à jour la valeur de la variable `i` à 10.

#### Boucles for

Q# permet une boucle for pour itérer sur une plage d'entiers. L'instruction for se compose du mot-clé `for`, suivi d'un identifiant, du mot-clé `in`, d'une expression de plage et d'un bloc d'instructions.

Une plage est spécifiée par les premier et dernier entiers de la plage, par exemple : `1..5` représente la plage 1, 2, 3, 4 et 5. Si un pas autre que +1 est nécessaire, alors trois entiers avec .. entre eux sont utilisés.

Donc, `1..2..10` est la plage 1, 3, 5, 7 et 9. La plage est inclusive aux deux extrémités.

```
for(num in 1..2..10)  
{  
   //Faire quelque chose  
}
```

Comme le nom l'indique, cette boucle se répétera jusqu'à ce que l'opération réussisse. Cette boucle est basée sur le modèle quantique « repeat until success ». Elle se compose du mot-clé `repeat` et de son bloc d'instructions, du mot-clé `until`, d'une expression booléenne, du mot-clé `fixup`, et de son bloc d'instructions.

L'instruction à l'intérieur du bloc repeat est exécutée, puis la condition booléenne est évaluée. Si la condition booléenne est évaluée à vrai, alors la boucle se termine. Sinon, le bloc fixup est exécuté et la boucle se répète une fois de plus.

Le bloc fixup est toujours requis — même s'il n'y a pas de fixup à faire — auquel cas il sera vide.

```
repeat {  
    //faire quelque chose  
}  
until boolean condition  
fixup {  
    // faire quelque chose  
}
```

Q# supporte les instructions if pour l'exécution conditionnelle, similaire à C#. L'instruction if se compose du mot-clé `if`, suivi d'une expression booléenne et du bloc d'instructions. Un bloc if peut avoir un bloc else optionnel, qui est représenté par le mot-clé `else`.

```
if (num % 2 == 0) {  
    return true;  
} else {  
    return false;  
}
```

Une instruction conditionnelle peut consister en une série de chaînes if-elseif-else. La clause else-if est représentée par le mot-clé `elif`.

```
if (num == 1) {  
    //faire quelque chose  
}  
elif(num == 2) {  
    //faire quelque chose  
}  
else {  
    //faire quelque chose  
}
```

### Conclusion

Dans cet article, nous avons appris les bases du langage de programmation Q#. Nous avons également installé QDK et vérifié l'environnement d'exécution Q# avec Visual Studio 2017. Veuillez poster vos précieux commentaires dans la section des commentaires et restez à l'écoute pour plus d'informations sur l'informatique quantique.

Vous pouvez toujours vous référer à mes articles précédents [ici](http://ankitsharmablogs.com/).

Vous pouvez également trouver cet article sur [C# Corner](http://www.c-sharpcorner.com/article/an-introduction-to-q/)

_Publié à l'origine sur [ankitsharmablogs.com](http://ankitsharmablogs.com/an-introduction-to-q/) le 16 janvier 2018._
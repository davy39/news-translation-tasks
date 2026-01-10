---
title: Quelques fonctionnalités modernes impressionnantes de C++ que chaque développeur
  devrait connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-08T16:21:51.000Z'
originalURL: https://freecodecamp.org/news/some-awesome-modern-c-features-that-every-developer-should-know-5e3bf6f79a3c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*IttEgAi22EwkjY2h
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Quelques fonctionnalités modernes impressionnantes de C++ que chaque développeur
  devrait connaître
seo_desc: 'By M Chowdhury

  As a language, C++ has evolved a lot.

  Of course this did not happen overnight. There was a time when C++ lacked dynamism.
  It was difficult to be fond of the language.

  But things changed when the C++ standard committee decided to spin u...'
---

Par M Chowdhury

En tant que langage, le C++ a beaucoup évolué.

Bien sûr, cela ne s'est pas fait du jour au lendemain. Il fut un temps où le C++ manquait de dynamisme. Il était difficile d'apprécier le langage.

Mais les choses ont changé lorsque le comité de standardisation du C++ a décidé de faire tourner la roue.

Depuis 2011, le C++ est devenu un langage dynamique et en constante évolution, comme beaucoup l'espéraient.

Ne vous méprenez pas en pensant que le langage est devenu plus facile. Il reste l'un des langages de programmation les plus difficiles, sinon le plus difficile, parmi ceux qui sont largement utilisés. Mais le C++ est également devenu beaucoup plus convivial que ses versions précédentes.

Dans mon dernier article, j'ai parlé de la [bibliothèque d'algorithmes C++](https://medium.freecodecamp.org/how-i-discovered-the-c-algorithm-library-and-learned-not-to-reinvent-the-wheel-2398a34e23e3) qui s'est enrichie au cours des dernières années.

Aujourd'hui, nous allons examiner certaines nouvelles fonctionnalités (à partir de C++11, qui a déjà 8 ans, soit dit en passant) que chaque développeur aimerait connaître.

Notez également que j'ai omis certaines fonctionnalités avancées dans cet article, mais je suis prêt à en écrire à leur sujet à l'avenir. ?fe0f

C'est parti !

#### Le mot-clé auto

Lorsque C++11 a introduit pour la première fois `**auto**`, la vie est devenue plus facile.

L'idée de `**auto**` était de faire en sorte que le compilateur C++ déduise le type de vos données lors de la compilation — au lieu de vous faire déclarer le type _à chaque fois_. C'était si pratique lorsque vous avez des types de données comme `**map<string,vector<pair<int,int>>>**` ?

![Image](https://cdn-media-1.freecodecamp.org/images/YwOaX7rBM68C0zmNWaR6gndEN3QGeNJC818u)

Regardez la ligne numéro 5. Vous ne pouvez pas déclarer quelque chose sans un `**initialiseur**`. Cela a en fait du sens. La ligne 5 ne permet pas au compilateur de savoir quel peut être le type de données.

Initialement, `**auto**` était quelque peu limité. Ensuite, dans les versions ultérieures du langage, plus de puissance lui a été ajoutée !

![Image](https://cdn-media-1.freecodecamp.org/images/-T08jZzWKlBmaksJQ07a73Z7OqtEVZ-w0uP5)

Dans les lignes 7 et 8, j'ai utilisé l'initialisation entre accolades. C'était également une nouvelle fonctionnalité ajoutée dans C++11.

Rappelez-vous, dans le cas de l'utilisation de `**auto**`, il doit y avoir un moyen pour le compilateur de déduire votre type.

Maintenant, une très bonne question, _que se passe-t-il si nous écrivons_ `**auto a = {1, 2, 3}**`? Est-ce une erreur de compilation ? Est-ce un vecteur ?

![Image](https://cdn-media-1.freecodecamp.org/images/vqLLzds6Emf3TXGvAE0G7wLljRA5A809IABC)

_smh ?_

En fait, C++11 a introduit `**std::initializer_list<type>**`. La liste initialisée entre accolades sera considérée comme ce conteneur léger si déclarée auto.

Enfin, comme je l'ai mentionné précédemment, la déduction de type par le compilateur peut être vraiment utile lorsque vous avez des structures de données complexes :

![Image](https://cdn-media-1.freecodecamp.org/images/-eqnhRNy7wggdV2kZKrm8Jb075m5iQKBwb76)

N'oubliez pas de vérifier la ligne 25 ! L'expression `**auto [v1,v2] = itr.second**` est littéralement une nouvelle fonctionnalité dans C++17. Cela s'appelle **structured binding**. Dans les versions précédentes du langage, vous deviez extraire chaque variable séparément. Mais le structured binding l'a rendu beaucoup plus pratique.

De plus, si vous vouliez obtenir les données en utilisant une référence, vous ajouteriez simplement un symbole — `**auto &[v1,v2] = itr.second**`.

Propre.

#### L'expression lambda

C++11 a introduit les expressions lambda, quelque chose comme les fonctions anonymes en JavaScript. Ce sont des objets fonctionnels, sans aucun nom, et ils capturent des variables sur divers _scopes_ basés sur une syntaxe concise. Ils sont également assignables à des variables.

Les lambdas sont très utiles si vous avez besoin de faire quelque chose de petit et rapide à l'intérieur de votre code mais que vous n'êtes pas prêt à écrire une fonction séparée pour cela. Une autre utilisation assez courante est de les utiliser comme fonctions de comparaison.

![Image](https://cdn-media-1.freecodecamp.org/images/q06OCThwvuI4tAq9WDMcFYMc45cQuBSMlorB)

L'exemple ci-dessus a beaucoup à dire.

Tout d'abord, remarquez comment l'initialisation entre accolades vous facilite la tâche. Ensuite, viennent les `**begin(), end()**` génériques qui sont également une addition dans C++11. Ensuite, vient la fonction lambda comme comparateur pour vos données. Les paramètres de la fonction lambda sont déclarés `**auto**` qui a été ajouté dans C++14. Avant cela, nous ne pouvions pas utiliser `**auto**` pour les paramètres de fonction.

Remarquez comment nous commençons l'expression lambda avec un crochet `**[]**`. Ils définissent la portée de la lambda — combien d'autorité elle a sur les variables et objets locaux.

Comme défini dans ce [dépôt impressionnant](https://github.com/AnthonyCalandra/modern-cpp-features#lambda-expressions) sur le C++ moderne :

* `[]` — ne capture rien. Vous ne pouvez donc pas utiliser de variable locale de la portée externe à l'intérieur de votre expression lambda. Vous ne pouvez utiliser que les paramètres.
* `[=]` — capture les objets locaux (variables locales, paramètres) dans la portée par valeur. Vous pouvez les utiliser, mais vous ne pouvez pas les modifier.
* `[&]` — capture les objets locaux (variables locales, paramètres) dans la portée par référence. Vous pouvez les modifier. Comme dans l'exemple suivant.
* `[this]` — capture le pointeur `this` par valeur.
* `[a, &b]` — capture les objets `a` par valeur, `b` par référence.

Donc, si à l'intérieur de votre fonction lambda, vous voulez transformer vos données dans un autre format, vous pouvez utiliser lambda en tirant parti de la portée. Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/5Mzg1Eaplh7V3tBwddUibP6e32TASKqNB5Bo)

Dans l'exemple ci-dessus, si vous aviez capturé les variables locales par valeur (`**[factor]**`) dans votre expression lambda, vous n'auriez pas pu changer `**factor**` à la ligne 5. Parce que simplement, vous n'avez pas le droit de le faire. Ne abusez pas de vos droits ! ?

Enfin, remarquez que nous prenons `**val**` comme référence. Cela garantit que tout changement à l'intérieur de la fonction lambda change réellement le `**vector**`.

![Image](https://cdn-media-1.freecodecamp.org/images/bybwfMOcOk0FvwwbyJ3SpNr7PZ4hZbEvZZKo)
_Ils se sentent joyeux après avoir appris le C++ moderne ! (Photo par [Unsplash](https://unsplash.com/@goian?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Ian Schneider</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="))_

#### Instructions d'initialisation à l'intérieur de if & switch

J'ai vraiment aimé cette fonctionnalité de C++17 dès que j'en ai eu connaissance.

![Image](https://cdn-media-1.freecodecamp.org/images/YbAQUY16a5gfoVCDzIxa0VQRI2L62g3YmN51)

Apparemment, maintenant vous pouvez faire l'initialisation des variables et vérifier la condition sur celle-ci — simultanément à l'intérieur du bloc `**if/switch**`. Cela est vraiment utile pour garder votre code concis et propre. La forme générale est :

```c++
if( init-statement(x); condition(x)) {
    // faire quelque chose ici
} else {
    // else a la portée de x
    // faire autre chose
}
```

#### Faites-le à la compilation avec constexpr

`**constexpr**` est cool !

Disons que vous avez une expression à évaluer et que sa valeur ne changera pas une fois initialisée. Vous pouvez pré-calculer la valeur et ensuite l'utiliser comme une macro. Ou comme l'a offert C++11, vous pouvez utiliser `**constexpr**`.

Les programmeurs tendent à réduire le temps d'exécution de leurs programmes autant que possible. Donc, s'il y a des opérations que vous pouvez faire faire au compilateur et ainsi soulager le temps d'exécution, alors le temps d'exécution peut être amélioré.

![Image](https://cdn-media-1.freecodecamp.org/images/oFNs0a4DpggilcCOH4rUe6Lb7Og4g5JpI1PR)

Le code ci-dessus est un exemple très courant de `**constexpr**`.

Puisque nous avons déclaré la fonction de calcul de Fibonacci comme `**constexpr**`, le compilateur peut pré-calculer `**fib(20)**` au moment de la compilation. Donc après la compilation, il peut remplacer la ligne

`**const long long bigval = fib(20);**` par

`**const long long bigval = 2432902008176640000;**`

Notez que l'argument passé est une valeur `**const**`. C'est un point important des fonctions déclarées `**constexpr**` — les arguments passés doivent également être `**constexpr**` ou `**const**`. Sinon, la fonction se comportera comme une fonction normale, ce qui signifie qu'il n'y aura pas de pré-calcul pendant la compilation.

Les variables peuvent également être `**constexpr**`. Dans ce cas, comme vous pouvez le deviner, ces variables doivent être évaluables à la compilation. Sinon, vous obtenez une erreur de compilation.

Intéressamment, plus tard dans C++17, `[**constexpr-if**](https://hackernoon.com/a-tour-of-c-17-if-constexpr-3ea62f62ff65)` et `[**constexpr-lambda**](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-constexpr?view=vs-2019)` ont été introduits.

#### Tuples

Tout comme `**pair**`, `**tuple**` est une collection de valeurs de taille fixe de divers types de données.

![Image](https://cdn-media-1.freecodecamp.org/images/jeeQ66M5YWztfoGaEVNd5vBQgYXZkh6-layn)

Parfois, il est plus pratique d'utiliser `**std::array**` au lieu de `**tuple**`. `array` est similaire au tableau de type C simple avec quelques fonctionnalités de la bibliothèque standard C++. Cette structure de données a été ajoutée dans C++11.

#### Déduction d'argument de modèle de classe

Un nom très verbeux pour une fonctionnalité. L'idée est que, à partir de C++17, la déduction d'argument pour les modèles se fera également pour les modèles de classe standard. Auparavant, elle était supportée uniquement pour les modèles de fonction.

En conséquence,

```c++
std::pair<std::string, int> user = {"M", 25}; // précédent
std::pair user = {"M", 25}; // C++17
```

La déduction de type est faite implicitement. Cela devient encore plus pratique pour `**tuple**`.

```c++
// précédent
std::tuple<std::string, std::string, int> user ("M", "Chy", 25);
// déduction en action ! 
std::tuple user2("M", "Chy", 25);
```

La fonctionnalité ci-dessus n'aura aucun sens si vous n'êtes pas assez familier avec les modèles C++.

#### Pointeurs intelligents

Les pointeurs peuvent être infernaux.

En raison de la liberté que des langages comme le C++ offrent aux programmeurs, il devient parfois très facile de se tirer une balle dans le pied. Et dans de nombreux cas, les pointeurs sont responsables du dommage.

Heureusement, C++11 a introduit les pointeurs intelligents, des pointeurs qui sont beaucoup plus pratiques que les pointeurs bruts. Ils aident les programmeurs à prévenir les fuites de mémoire en la libérant lorsque cela est possible. Ils offrent également une sécurité contre les exceptions.

J'ai pensé écrire sur les pointeurs intelligents en C++ dans cet article. Mais apparemment, il y a beaucoup de détails importants à leur sujet. Ils méritent leur propre article et je suis certainement prêt à en écrire un à leur sujet dans un avenir proche.

C'est tout pour aujourd'hui. Rappelez-vous que le C++ a en fait ajouté beaucoup plus de nouvelles fonctionnalités dans les dernières versions du langage. Vous devriez les vérifier si vous êtes intéressé. Voici un dépôt impressionnant sur le C++ moderne qui s'appelle littéralement [Awesome Modern C++](https://github.com/rigtorp/awesome-modern-cpp) !

Adios !
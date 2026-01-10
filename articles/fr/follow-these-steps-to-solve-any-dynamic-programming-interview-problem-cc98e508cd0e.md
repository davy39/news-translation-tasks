---
title: Suivez ces étapes pour résoudre n'importe quel problème d'entretien sur la
  programmation dynamique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T19:32:36.000Z'
originalURL: https://freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*DpsbrfUM89M_LHKY.jpg
tags:
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: jobs
  slug: jobs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Suivez ces étapes pour résoudre n'importe quel problème d'entretien sur
  la programmation dynamique
seo_desc: 'By Nikola Otasevic

  Despite having significant experience building software products, many engineers
  feel jittery at the thought of going through a coding interview that focuses on
  algorithms. I’ve interviewed hundreds of engineers at Refdash, Google,...'
---

Par Nikola Otasevic

Malgré une expérience significative dans la construction de produits logiciels, de nombreux ingénieurs se sentent nerveux à l'idée de passer un entretien de codage axé sur les algorithmes. J'ai interviewé des centaines d'ingénieurs chez [Refdash](https://refdash.com/?utm_source=dp_blog_f), Google et dans des startups dont j'ai fait partie, et certaines des questions les plus courantes qui mettent les ingénieurs mal à l'aise sont celles qui impliquent la programmation dynamique (DP).

De nombreuses entreprises technologiques aiment poser des questions sur la DP lors de leurs entretiens. Bien que nous puissions débattre de leur efficacité pour évaluer la capacité de quelqu'un à performer dans un rôle d'ingénierie, la DP continue d'être un domaine qui fait trébucher les ingénieurs sur le chemin de trouver un emploi qu'ils aiment.

### Programmation dynamique — Prédictible et préparable

L'une des raisons pour lesquelles je crois personnellement que les questions sur la DP ne sont peut-être pas le meilleur moyen de tester les compétences en ingénierie est qu'elles sont prévisibles et faciles à reconnaître. Elles nous permettent de filtrer beaucoup plus pour la préparation que pour les compétences en ingénierie.

Ces questions semblent généralement assez complexes de l'extérieur et pourraient vous donner l'impression qu'une personne qui les résout est très douée en algorithmes. De même, les personnes qui ne parviennent pas à surmonter certains concepts de la DP pourraient sembler assez faibles dans leur connaissance des algorithmes.

La réalité est différente, et le plus grand facteur de leur performance est la préparation. Alors assurons-nous que tout le monde soit préparé pour cela. Une fois pour toutes.

### 7 étapes pour résoudre un problème de programmation dynamique

Dans le reste de cet article, je vais passer en revue une recette que vous pouvez suivre pour déterminer si un problème est un « problème de DP », ainsi que pour trouver une solution à un tel problème. Plus précisément, je vais passer par les étapes suivantes :

1. Comment reconnaître un problème de DP
2. Identifier les variables du problème
3. Exprimer clairement la relation de récurrence
4. Identifier les cas de base
5. Décider si vous voulez l'implémenter de manière itérative ou récursive
6. Ajouter la mémoisation
7. Déterminer la complexité temporelle

### Exemple de problème de DP

Dans le but d'avoir un exemple pour les abstractions que je vais faire, laissez-moi introduire un problème d'exemple. Dans chacune des sections, je ferai référence au problème, mais vous pourriez également lire les sections indépendamment du problème.

#### Énoncé du problème :

![Image](https://cdn-media-1.freecodecamp.org/images/YIelQx3b0OSZIaNWVkJEmirqOZRZWXm2fbBk)

_Dans ce problème, nous sommes sur une balle qui saute de manière folle, en essayant de nous arrêter, tout en évitant les piques sur le chemin._

#### Voici les règles :

1) Vous avez une piste plate avec une série de piques. La piste est représentée par un tableau booléen qui indique si un endroit particulier (discret) est dégagé de piques. C'est True pour dégagé et False pour non dégagé.

Représentation d'un exemple de tableau :

![Image](https://cdn-media-1.freecodecamp.org/images/c5h0NAmIsaNYEjJfcIZa3uPCiTxO28ew9gPV)

2) Vous avez une vitesse de départ S. S est un entier non négatif à tout moment, et il indique de combien vous allez avancer avec le prochain saut.

3) Chaque fois que vous atterrissez sur un endroit, vous pouvez ajuster votre vitesse jusqu'à 1 unité avant le prochain saut.

![Image](https://cdn-media-1.freecodecamp.org/images/bCnFU8w6zxjnUpypi0ArUOyON6L20E0EPl0p)

4) Vous voulez vous arrêter en toute sécurité n'importe où le long de la piste (ce n'est pas besoin d'être à la fin du tableau). Vous vous arrêtez lorsque votre vitesse devient 0. Cependant, si vous atterrissez sur un pique à tout moment, votre balle qui rebondit de manière folle éclate et c'est la fin du jeu.

**La sortie de votre fonction doit être un booléen indiquant si nous pouvons nous arrêter en toute sécurité n'importe où le long de la piste.**

#### Étape 1 : Comment reconnaître un problème de programmation dynamique

Tout d'abord, clarifions que la DP est essentiellement juste une technique d'optimisation. La DP est une méthode pour résoudre des problèmes en les décomposant en une collection de sous-problèmes plus simples, en résolvant chacun de ces sous-problèmes une seule fois, et en stockant leurs solutions. La prochaine fois que le même sous-problème se présente, au lieu de recalculer sa solution, vous regardez simplement la solution précédemment calculée. Cela économise du temps de calcul au détriment d'un (espérons-le) modeste investissement en espace de stockage.

Reconnaître qu'un problème peut être résolu en utilisant la DP est la première et souvent l'étape la plus difficile pour le résoudre. Ce que vous voulez vous demander, c'est si la solution de votre problème peut être exprimée comme une fonction des solutions à des problèmes similaires plus petits.

Dans le cas de notre problème d'exemple, étant donné un point sur la piste, une vitesse et la piste devant, nous pourrions déterminer les endroits où nous pourrions potentiellement sauter ensuite. De plus, il semble que le fait de pouvoir s'arrêter à partir du point actuel avec la vitesse actuelle dépend uniquement du fait de pouvoir s'arrêter à partir du point que nous choisissons d'aller ensuite.

C'est une excellente chose, car en avançant, nous raccourcissons la piste devant et rendons notre problème plus petit. Nous devrions pouvoir répéter ce processus jusqu'à ce que nous arrivions à un point où il est évident si nous pouvons nous arrêter.

> Reconnaître un problème de programmation dynamique est souvent l'étape la plus difficile pour le résoudre. La solution du problème peut-elle être exprimée comme une fonction des solutions à des problèmes similaires plus petits ?

#### Étape 2 : Identifier les variables du problème

Maintenant, nous avons établi qu'il existe une certaine structure récursive entre nos sous-problèmes. Ensuite, nous devons exprimer le problème en termes de paramètres de fonction et voir lesquels de ces paramètres changent.

Typiquement dans les entretiens, vous aurez un ou deux paramètres changeants, mais techniquement cela pourrait être n'importe quel nombre. Un exemple classique de problème à un paramètre changeant est « déterminer le n-ième nombre de Fibonacci ». Un tel exemple pour un problème à deux paramètres changeants est « Calculer la distance d'édition entre les chaînes ». Si vous n'êtes pas familier avec ces problèmes, ne vous en faites pas.

Une façon de déterminer le nombre de paramètres changeants est de lister des exemples de plusieurs sous-problèmes et de comparer les paramètres. Compter le nombre de paramètres changeants est précieux pour déterminer le nombre de sous-problèmes que nous devons résoudre. C'est aussi important en soi pour nous aider à renforcer la compréhension de la relation de récurrence de l'étape 1.

Dans notre exemple, les deux paramètres qui pourraient changer pour chaque sous-problème sont :

1. **Position du tableau (P)**
2. **Vitesse (S)**

On pourrait dire que la piste devant change également, mais cela serait redondant étant donné que toute la piste non changeante et la position (P) portent déjà cette information.

Maintenant, avec ces 2 paramètres changeants et d'autres paramètres statiques, nous avons la description complète de nos sous-problèmes.

> Identifier les paramètres changeants et déterminer le nombre de sous-problèmes.

#### Étape 3 : Exprimer clairement la relation de récurrence

C'est une étape importante que beaucoup bâclent afin de passer à la programmation. Exprimer la relation de récurrence aussi clairement que possible renforcera votre compréhension du problème et rendra tout le reste significativement plus facile.

Une fois que vous avez compris que la relation de récurrence existe et que vous spécifiez les problèmes en termes de paramètres, cela devrait venir comme une étape naturelle. Comment les problèmes sont-ils liés les uns aux autres ? En d'autres termes, supposons que vous avez calculé les sous-problèmes. Comment calculeriez-vous le problème principal ?

Voici comment nous y pensons dans notre problème d'exemple :

Parce que vous pouvez ajuster votre vitesse jusqu'à 1 avant de sauter à la position suivante, il n'y a que 3 vitesses possibles, et donc 3 endroits où nous pourrions être ensuite.

Plus formellement, si notre vitesse est S, la position P, nous pourrions aller de (S, P) à :

1. **(S, P + S)**; # si nous ne changeons pas la vitesse
2. **(S — 1, P + S — 1)**; # si nous changeons la vitesse de -1
3. **(S + 1, P + S + 1)**; # si nous changeons la vitesse de +1

Si nous pouvons trouver un moyen de nous arrêter dans l'un des sous-problèmes ci-dessus, alors nous pouvons également nous arrêter à partir de (S, P). Cela est dû au fait que nous pouvons passer de (S, P) à l'une des trois options ci-dessus.

C'est généralement un bon niveau de compréhension du problème (explication en anglais simple), mais parfois vous pourriez vouloir exprimer la relation mathématiquement également. Appelons une fonction que nous essayons de calculer canStop. Alors :

**canStop(S, P) = canStop(S, P + S) || canStop(S — 1, P + S — 1) || canStop(S + 1, P + S + 1)**

Hourra, il semble que nous ayons notre relation de récurrence !

> Relation de récurrence : En supposant que vous avez calculé les sous-problèmes, comment calculeriez-vous le problème principal ?

#### Étape 4 : Identifier les cas de base

Un cas de base est un sous-problème qui ne dépend d'aucun autre sous-problème. Pour trouver de tels sous-problèmes, vous voulez généralement essayer quelques exemples, voir comment votre problème se simplifie en sous-problèmes plus petits, et identifier à quel point il ne peut plus être simplifié.

La raison pour laquelle un problème ne peut plus être simplifié est qu'un des paramètres prendrait une valeur qui n'est pas possible étant donné les **contraintes** du problème.

Dans notre problème d'exemple, nous avons deux paramètres changeants, S et P. Réfléchissons aux valeurs possibles de S et P qui pourraient ne pas être légales :

1. **P doit être dans les limites de la piste donnée**
2. **P ne peut pas être tel que runway[P] soit faux car cela signifierait que nous sommes sur un pique**
3. **S ne peut pas être négatif, et un S==0 indique que nous avons terminé**

Parfois, il peut être un peu difficile de convertir les assertions que nous faisons sur les paramètres en cas de base programmables. Cela est dû au fait que, en plus de lister les assertions si vous voulez que votre code paraisse concis et ne vérifie pas les conditions inutiles, vous devez également réfléchir à quelles conditions sont même possibles.

Dans notre exemple :

1. **P < 0 || P >= longueur de** runway semble être la bonne chose à faire. Une alternative pourrait être de considérer **P == fin de** runway comme un cas de base. Cependant, il est possible qu'un problème se divise en un sous-problème qui va au-delà de la fin de la piste, donc nous devons vraiment vérifier l'inégalité.
2. Cela semble assez évident. Nous pouvons simplement vérifier **si runway[P] est faux**.
3. Similaire à #1, nous pourrions simplement vérifier S < 0 et S == 0. Cependant, ici nous pouvons raisonner qu'il est impossible pour S d'être < 0 car S diminue d'au plus 1, donc il devrait passer par le cas S == 0 auparavant. Par conséquent, S == 0 est un cas de base suffisant pour le paramètre S.

#### Étape 5 : Décider si vous voulez l'implémenter de manière itérative ou récursive

La manière dont nous avons parlé des étapes jusqu'à présent pourrait vous amener à penser que nous devrions implémenter le problème de manière récursive. Cependant, tout ce dont nous avons parlé jusqu'à présent est complètement agnostique quant à savoir si vous décidez d'implémenter le problème de manière récursive ou itérative. Dans les deux approches, vous devriez déterminer la relation de récurrence et les cas de base.

**Pour décider si vous voulez procéder de manière itérative ou récursive, vous devez réfléchir attentivement aux compromis.**

![Image](https://cdn-media-1.freecodecamp.org/images/E-2qbrD5g7UtOJIN7ULrdwAdgiL0jAU7uGFH)

**Les problèmes de débordement de pile sont généralement un critère d'exclusion** et une raison pour laquelle vous ne voudriez pas avoir de récursion dans un système de production (backend). Cependant, pour les besoins de l'entretien, tant que vous mentionnez les compromis, vous devriez généralement être en mesure de choisir l'une ou l'autre des implémentations. Vous devriez vous sentir à l'aise pour implémenter les deux.

**Dans notre problème particulier, j'ai implémenté les deux versions. Voici le code Python pour cela :**  
 Une solution récursive : (les extraits de code originaux peuvent être trouvés [ici](http://blog.refdash.com/dynamic-programming-tutorial-example/))

![Image](https://cdn-media-1.freecodecamp.org/images/MmSzAzTeUbtfjiYFSjilQlCBaXRAsOOIesKL)

Une solution itérative : (les extraits de code originaux peuvent être trouvés [ici](http://blog.refdash.com/dynamic-programming-tutorial-example/))

![Image](https://cdn-media-1.freecodecamp.org/images/aZgiyRIJ3SAD0Mx6lywCaohZt1BUJ0ZW-1Hm)

#### Étape 6 : Ajouter la mémoisation

**La mémoisation** est une technique qui est étroitement associée à la DP. Elle est utilisée pour stocker les résultats des appels de fonction coûteux et retourner le résultat mis en cache lorsque les mêmes entrées se produisent à nouveau.

Pourquoi ajoutons-nous la mémoisation à notre récursion ? Nous rencontrons les mêmes sous-problèmes qui, sans mémoisation, sont calculés à plusieurs reprises. Ces répétitions conduisent très souvent à des complexités temporelles exponentielles.

Dans les solutions récursives, l'ajout de la mémoisation devrait sembler simple. Voyons pourquoi. Rappelez-vous que la mémoisation est simplement un cache des résultats de la fonction. Il y a des moments où vous voulez vous écarter de cette définition afin de tirer quelques optimisations mineures, mais traiter la mémoisation comme un cache de résultats de fonction est la manière la plus intuitive de l'implémenter.

Cela signifie que vous devriez :

1. Stocker votre résultat de fonction dans votre mémoire avant chaque instruction _return_
2. Rechercher le résultat de la fonction dans la mémoire avant de commencer à faire d'autres calculs

Voici le code ci-dessus avec la mémoisation ajoutée (les lignes ajoutées sont mises en évidence) : (les extraits de code originaux peuvent être trouvés [ici](http://blog.refdash.com/dynamic-programming-tutorial-example/))

![Image](https://cdn-media-1.freecodecamp.org/images/aAgK5alenVTE0zyCTsknv32r-RTjiFOJmMu6)

Afin d'illustrer l'efficacité de la mémoisation et des différentes approches, faisons quelques tests rapides. Je vais tester les trois méthodes que nous avons vues jusqu'à présent. Voici la configuration :

1. J'ai créé une piste de longueur 1000 avec des piques à des endroits aléatoires (j'ai choisi d'avoir une probabilité de 20 % qu'un pique soit à un endroit donné)
2. initSpeed = 30
3. J'ai exécuté toutes les fonctions 10 fois et mesuré le temps d'exécution moyen

Voici les résultats (en secondes) :

![Image](https://cdn-media-1.freecodecamp.org/images/bOxJ2uGkAzVHEakgeFnPJMMe44oFIhLAqGh5)

Vous pouvez voir que l'approche purement récursive prend environ 500 fois plus de temps que l'approche itérative et environ 1300 fois plus de temps que l'approche récursive avec mémoisation. Notez que cet écart augmenterait rapidement avec la longueur de la piste. Je vous encourage à essayer de l'exécuter vous-même.

#### Étape 7 : Déterminer la complexité temporelle

Il existe des règles simples qui peuvent rendre le calcul de la complexité temporelle d'un problème de programmation dynamique beaucoup plus facile. Voici deux étapes que vous devez faire :

1. Compter le nombre d'états — cela dépendra du nombre de paramètres changeants dans votre problème
2. Réfléchir au travail effectué par chaque état. En d'autres termes, si tout le reste sauf un état a été calculé, combien de travail devez-vous faire pour calculer cet dernier état ?

Dans notre problème d'exemple, le nombre d'états est **|P| * |S|**, où

* P est l'ensemble de toutes les positions (|P| indique le nombre d'éléments dans P)
* S est l'ensemble de toutes les vitesses

Le travail effectué par chaque état est O(1) dans ce problème car, étant donné tous les autres états, nous devons simplement regarder 3 sous-problèmes pour déterminer l'état résultant.

Comme nous l'avons noté dans le code précédent, |S| est limité par la longueur de la piste (|P|), donc nous pourrions dire que le nombre d'états est |P|² et parce que le travail effectué par chaque état est O(1), alors la complexité temporelle totale est O(|P|²).

Cependant, il semble que |S| puisse être encore limité, car si c'était vraiment |P|, il est très clair que l'arrêt ne serait pas possible car vous devriez sauter la longueur de toute la piste au premier mouvement.

Alors voyons comment nous pouvons mettre une limite plus stricte sur |S|. Appelons la vitesse maximale S. Supposons que nous partons de la position 0. À quelle vitesse pourrions-nous nous arrêter si nous essayions de nous arrêter dès que possible et si nous ignorions les piques potentiels ?

![Image](https://cdn-media-1.freecodecamp.org/images/tnzdVcGH4Npix6BcaJu1vGVlOkcvJo89NYgv)

À la première itération, nous devrions arriver au moins au point (S-1), en ajustant notre vitesse à zéro par -1. De là, nous irions au minimum par (S-2) étapes vers l'avant, et ainsi de suite.

Pour une piste de **longueur L**, ce qui suit doit être vrai :

**=> (S-1) + (S-2) + (S-3) + ….+ 1** < L

**=> S*(S-1) / 2** < L

**=> S² — S — 2L** < 0

Si vous trouvez les racines de la fonction ci-dessus, elles seront :

**r1 = 1/2 + sqrt(1/4 + 2L) et r2 = 1/2 — sqrt(1/4 + 2L)**

Nous pouvons écrire notre inégalité comme :

**(S — r1) * (S — r2) <** ; 0

Considérant que S — r2 > 0 pour tout S > 0 et L > 0, nous avons besoin de ce qui suit :

**S — 1/2 — sqrt(1/4 + 2L) <** ; 0

**=> S < 1/2 + sqrt(1/4** + 2L)

C'est la vitesse maximale que nous pourrions avoir sur une piste de longueur L. Si nous avions une vitesse plus élevée, nous ne pourrions pas nous arrêter même théoriquement, indépendamment de la position des piques.

Cela signifie que la complexité temporelle totale dépend uniquement de la longueur de la piste L sous la forme suivante :

O(L * sqrt(L)) qui est meilleur que O(L²)

> _O(L * sqrt(L)) est la limite supérieure de la complexité temporelle_

Super, vous avez réussi ! :)

Les 7 étapes que nous avons suivies devraient vous donner un cadre pour résoudre systématiquement n'importe quel problème de programmation dynamique. Je vous recommande vivement de pratiquer cette approche sur quelques autres problèmes pour parfaire votre méthode.

### **Voici quelques prochaines étapes que vous pouvez suivre**

1. Étendez le problème d'exemple en essayant de trouver un chemin vers un point d'arrêt. Nous avons résolu un problème qui vous dit si vous pouvez vous arrêter, mais que se passe-t-il si vous vouliez aussi connaître les étapes à suivre pour vous arrêter éventuellement le long de la piste ? Comment modifieriez-vous l'implémentation existante pour faire cela ?
2. Si vous voulez solidifier votre compréhension de la mémoisation et comprendre qu'il s'agit simplement d'un cache de résultats de fonction, vous devriez lire sur les décorateurs en Python ou des concepts similaires dans d'autres langages. Réfléchissez à la manière dont ils vous permettraient d'implémenter la mémoisation en général pour toute fonction que vous souhaitez mémoiser.
3. Travaillez sur plus de problèmes de DP en suivant les étapes que nous avons parcourues. Vous pouvez toujours en trouver un tas en ligne (ex. [LeetCode](https://leetcode.com/tag/dynamic-programming/) ou [GeeksForGeeks](http://www.geeksforgeeks.org/dynamic-programming/)). En vous entraînant, gardez à l'esprit une chose : apprenez les idées, n'apprenez pas les problèmes. Le nombre d'idées est significativement plus petit et c'est un espace plus facile à conquérir qui vous servira également beaucoup mieux.

Lorsque vous aurez l'impression d'avoir conquis ces idées, consultez [**Refdash**](https://refdash.com/?utm_source=dp_blog) où vous êtes interviewé par un ingénieur senior et recevez un retour détaillé sur votre codage, vos algorithmes et votre conception de systèmes.

_Publié à l'origine sur [Refdash blog](http://blog.refdash.com/dynamic-programming-tutorial-example/). Refdash est une plateforme d'entretien qui aide les ingénieurs à passer des entretiens de manière anonyme avec des ingénieurs expérimentés de grandes entreprises telles que Google, Facebook ou Palantir et à recevoir un retour détaillé. [Refdash](https://refdash.com/) aide également les ingénieurs à découvrir des opportunités d'emploi incroyables basées sur leurs compétences et intérêts._
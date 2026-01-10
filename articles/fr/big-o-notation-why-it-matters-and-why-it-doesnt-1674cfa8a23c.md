---
title: 'Qu''est-ce que la Notation Big O Expliquée : Complexité Spatiale et Temporelle'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-16T17:24:00.000Z'
originalURL: https://freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/0_NSxbYAwcC7Qzk7PP.jpg
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
- name: Computer Science
  slug: computer-science
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
seo_title: 'Qu''est-ce que la Notation Big O Expliquée : Complexité Spatiale et Temporelle'
seo_desc: 'By Shen Huang

  Do you really understand Big O? If so, then this will refresh your understanding
  before an interview. If not, don’t worry — come and join us for some endeavors in
  computer science.

  If you have taken some algorithm related courses, you’v...'
---

Par Shen Huang

Comprenez-vous vraiment le Big O ? Si oui, cela rafraîchira votre compréhension avant un entretien. Si non, ne vous inquiétez pas — venez nous rejoindre pour quelques efforts en informatique.

Si vous avez suivi des cours liés aux algorithmes, vous avez probablement entendu le terme **notation Big O**. Si ce n'est pas le cas, nous allons le passer en revue ici, puis obtenir une compréhension plus approfondie de ce qu'il est vraiment.

La notation Big O est l'un des outils les plus fondamentaux pour les informaticiens afin d'analyser le coût d'un algorithme. C'est également une bonne pratique pour les ingénieurs logiciels de comprendre en profondeur.

Cet article est écrit en supposant que vous avez déjà abordé un peu de code. De plus, certaines matières approfondies nécessitent également des bases mathématiques de niveau lycée, et peuvent donc être un peu moins confortables pour les débutants complets. Mais si vous êtes prêt, commençons !

Dans cet article, nous aurons une discussion approfondie sur la notation Big O. Nous commencerons par un exemple d'algorithme pour ouvrir notre compréhension. Ensuite, nous entrerons un peu dans les mathématiques pour avoir une compréhension formelle. Après cela, nous passerons en revue quelques variations courantes de la notation Big O. Enfin, nous discuterons de certaines des limitations du Big O dans un scénario pratique. Un tableau des matières peut être trouvé ci-dessous.

### Table des Matières

1. Qu'est-ce que la notation Big O, et pourquoi est-elle importante
2. Définition formelle de la notation Big O
3. Big O, Little O, Omega & Thêta
4. Comparaison de la complexité entre les Big O typiques
5. Complexité temporelle et spatiale
6. Meilleure, moyenne, pire, complexité attendue
7. Pourquoi le Big O n'a pas d'importance
8. En fin de compte...

Alors commençons.

### 1. Qu'est-ce que la notation Big O, et pourquoi est-elle importante

> « La notation Big O est une notation mathématique qui décrit le comportement limite d'une fonction lorsque l'argument tend vers une valeur particulière ou l'infini. C'est un membre d'une famille de notations inventées par Paul Bachmann, Edmund Landau et d'autres, collectivement appelées notation Bachmann-Landau ou notation asymptotique. »
>
> — Définition de la notation Big O selon Wikipédia

En termes simples, la notation Big O décrit la **complexité** de votre code en utilisant des termes algébriques.

Pour comprendre ce qu'est la notation Big O, nous pouvons examiner un exemple typique, **_O(n²)_**, qui se prononce généralement **« Big O carré »**. La lettre **« n »** ici représente la **taille de l'entrée**, et la fonction **« g(n) = n² »** à l'intérieur du **« O() »** nous donne une idée de la complexité de l'algorithme par rapport à la taille de l'entrée.

Un algorithme typique qui a la complexité O(n²) serait l'algorithme de **tri par sélection**. Le tri par sélection est un algorithme de tri qui parcourt la liste pour s'assurer que chaque élément à l'index **_i_** est le **_ième_** plus petit/plus grand élément de la liste. Le **CODEPEN** ci-dessous donne un exemple visuel.

%[https://codepen.io/iMultiThinker/pen/yEpRVr]

L'algorithme peut être décrit par le code suivant. Afin de s'assurer que le _ième_ élément est le _ième_ plus petit élément de la liste, cet algorithme parcourt d'abord la liste avec une boucle for. Ensuite, pour chaque élément, il utilise une autre boucle for pour trouver le plus petit élément dans la partie restante de la liste.

```js
SelectionSort(List) {
  for(i from 0 to List.Length) {
    SmallestElement = List[i]
    for(j from i to List.Length) {
      if(SmallestElement > List[j]) {
        SmallestElement = List[j]
      }
    }
    Swap(List[i], SmallestElement)
  }
}
```

Dans ce scénario, nous considérons la variable **_List_** comme l'entrée, ainsi la taille de l'entrée n est le **_nombre d'éléments à l'intérieur de List_**. Supposons que l'instruction if, et l'affectation de valeur délimitée par l'instruction if, prennent un temps constant. Ensuite, nous pouvons trouver la notation big O pour la fonction SelectionSort en analysant combien de fois les instructions sont exécutées.

Tout d'abord, la boucle for interne exécute les instructions à l'intérieur n fois. Et ensuite, après que **_i_** est incrémenté, la boucle for interne s'exécute pour n-1 fois… jusqu'à ce qu'elle s'exécute une fois, puis les deux boucles for atteignent leurs conditions de terminaison.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_1ajbPJXjt3z7CofVODlaCw.png)
_Boucles de tri par sélection illustrées_

Cela donne en fait une somme géométrique, et avec un peu de [mathématiques de niveau lycée](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF), nous trouverions que la boucle interne se répétera pour 1+2…+n fois, ce qui équivaut à n(n-1)/2 fois. Si nous développons cela, nous obtiendrons n²/2-n/2.

Lorsque nous calculons la notation big O, nous ne nous soucions que des **termes dominants**, et nous ne nous soucions pas des coefficients. Ainsi, nous prenons n² comme notre big O final. Nous l'écrivons comme O(n²), qui se prononce à nouveau **« Big O carré »**.

Maintenant, vous vous demandez peut-être, qu'est-ce que ce **« terme dominant »** ? Et pourquoi ne nous soucions-nous pas des coefficients ? Ne vous inquiétez pas, nous allons les passer en revue un par un. Cela peut être un peu difficile à comprendre au début, mais tout cela aura beaucoup plus de sens à mesure que vous lirez la section suivante.

### 2. Définition formelle de la notation Big O

Il était une fois un roi indien qui voulait récompenser un homme sage pour son excellence. L'homme sage n'a demandé que du blé qui remplirait un échiquier.

Mais voici ses règles : dans la première case, il veut 1 grain de blé, puis 2 sur la deuxième case, puis 4 sur la suivante… chaque case de l'échiquier devait être remplie par le double de la quantité de grains de la précédente. Le roi naïf a accepté sans hésiter, pensant que ce serait une demande triviale à satisfaire, jusqu'à ce qu'il essaie réellement…

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_em0jJ2rgj-ZapCef.jpg)
_Blé et échiquier, Image de [Wikipedia](https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem)_

Alors, combien de grains de blé le roi doit-il à l'homme sage ? Nous savons qu'un échiquier a 8 cases par 8 cases, ce qui fait 64 cases. Donc la dernière case devrait avoir un total de **2⁶³** grains de blé. Si vous faites un calcul en ligne, **pour l'ensemble de l'échiquier**, vous obtiendrez **1,8446744*10¹⁹** — c'est environ 18 suivi de 18 zéros.

En supposant que chaque grain de blé pèse 0,01 gramme, cela nous donne 184 467 440 737 tonnes de blé. Et 184 milliards de tonnes, c'est beaucoup, n'est-ce pas ?

Les nombres croissent assez vite plus tard pour une croissance exponentielle, n'est-ce pas ? La même logique s'applique aux algorithmes informatiques. Si les efforts requis pour accomplir une tâche croissent de manière exponentielle par rapport à la taille de l'entrée, cela peut finir par devenir énormément grand.

Comme nous allons le voir dans un instant, la croissance de 2ⁿ est beaucoup plus rapide que n². Maintenant, avec n = 64, le carré de 64 est 4096. Si vous ajoutez ce nombre à 2⁶⁴, il sera perdu en dehors des chiffres significatifs.

C'est pourquoi, lorsque nous regardons le taux de croissance, nous ne nous soucions que des termes dominants. Et puisque nous voulons analyser la croissance par rapport à la taille de l'entrée, les coefficients qui ne multiplient que le nombre plutôt que de croître avec la taille de l'entrée ne contiennent pas d'informations utiles.

Voici la définition formelle du Big O :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_cyqWw3UxODl-wqJi.jpg)
_[Diapositives CSE 373](https://slideplayer.com/slide/9739625/" rel="noopener) de l'Université de Washington_

La définition formelle est utile lorsque vous devez effectuer une preuve mathématique. Par exemple, la complexité temporelle pour le tri par sélection peut être définie par la fonction f(n) = n²/2-n/2 comme nous l'avons discuté dans la section précédente.

Si nous permettons à notre fonction g(n) d'être n², nous pouvons trouver une constante c = 1, et un N₀ = 0, et tant que N > N₀, N² sera toujours supérieur à N²/2-N/2. Nous pouvons facilement prouver cela en soustrayant N²/2 des deux fonctions, puis nous pouvons facilement voir que N²/2 > -N/2 est vrai lorsque N > 0. Par conséquent, nous pouvons conclure que f(n) = O(n²), dans l'autre sélection _sort est « big O carré »_.

Vous avez peut-être remarqué un petit truc ici. C'est-à-dire, si vous faites croître g(n) super rapidement, bien plus rapidement que tout, O(g(n)) sera toujours suffisamment grand. Par exemple, pour toute fonction polynomiale, vous pouvez toujours avoir raison en disant qu'elles sont O(2ⁿ) parce que 2ⁿ finira par dépasser tout polynôme.

Mathématiquement, vous avez raison, mais généralement lorsque nous parlons de Big O, nous voulons connaître la **borne serrée** de la fonction. Vous comprendrez cela davantage à mesure que vous lirez la section suivante.

Mais avant de continuer, testons votre compréhension avec la question suivante. La réponse sera trouvée dans les sections ultérieures, donc ce ne sera pas un abandon.

> **Question :** Une image est représentée par un tableau 2D de pixels. Si vous utilisez une boucle for imbriquée pour parcourir chaque pixel (c'est-à-dire que vous avez une boucle for parcourant toutes les colonnes, puis une autre boucle for à l'intérieur pour parcourir toutes les lignes), quelle est la complexité temporelle de l'algorithme lorsque l'image est considérée comme l'entrée ?

### 3. Big O, Little O, Omega & Thêta

> Big O : « f(n) est O(g(n)) » si pour certaines constantes c et N₀, f(N) ≤ cg(N) pour tout N > N₀
>
> Omega : « f(n) est Ω(g(n)) » si pour certaines constantes c et N₀, f(N) ≥ cg(N) pour tout N > N₀
>
> Thêta : « f(n) est Θ(g(n)) » si f(n) est O(g(n)) et f(n) est Ω(g(n))
>
> Little O : « f(n) est o(g(n)) » si f(n) est O(g(n)) et f(n) n'est pas Θ(g(n))
>
> — Définition formelle de Big O, Omega, Thêta et Little O

En termes simples :

* **Big O (O())** décrit la **borne supérieure** de la complexité.
* **Omega (Ω())** décrit la **borne inférieure** de la complexité.
* **Thêta (Θ())** décrit la **borne exacte** de la complexité.
* **Little O (o())** décrit la **borne supérieure excluant la borne exacte**.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_O-dcXbYXojkAPEnDuVZMvA.png)
_Relations entre Big O, Little O, Omega & Thêta illustrées_

Par exemple, la fonction g(n) = n² + 3n est O(n³), o(n⁴), Θ(n²) et Ω(n). Mais vous auriez toujours raison si vous dites qu'elle est Ω(n²) ou O(n²).

Généralement, lorsque nous parlons de Big O, ce que nous voulons dire est Thêta. Il est un peu inutile de donner une borne supérieure qui est bien plus grande que la portée de l'analyse. Cela serait similaire à résoudre des inégalités en mettant ∞ du côté le plus grand, ce qui vous donnera presque toujours raison.

Mais comment déterminons-nous quelles fonctions sont plus complexes que d'autres ? Dans la section suivante que vous allez lire, nous allons apprendre cela en détail.

### 4. Comparaison de la complexité entre les Big O typiques

Lorsque nous essayons de déterminer le Big O pour une fonction particulière g(n), nous ne nous soucions que du **terme dominant** de la fonction. Le terme dominant est le terme qui croît le plus rapidement.

Par exemple, n² croît plus rapidement que n, donc si nous avons quelque chose comme g(n) = n² + 5n + 6, ce sera big O(n²). Si vous avez pris un peu de calcul différentiel auparavant, cela est très similaire au raccourci pour trouver les limites des polynômes fractionnaires, où vous ne vous souciez que du terme dominant pour les numérateurs et les dénominateurs à la fin.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_MPwgKd4lgXACfuNt.png)
_Une autre façon de voir le Big O, Image de [Stack Overflow](https://stackoverflow.com/questions/1364444/difference-between-big-o-and-little-o-notation" rel="noopener)_

Mais quelle fonction croît plus rapidement que les autres ? Il y a en fait quelques règles.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_KfZYFUT2OKfjekJlCeYvuQ.jpeg)
_Illustration de la croissance de la complexité de [Big O Cheatsheet](http://bigocheatsheet.com/" rel="noopener)_

#### 1. O(1) a la complexité la plus faible

Souvent appelé **« temps constant »**, si vous pouvez créer un algorithme pour résoudre le problème en O(1), vous êtes probablement au mieux. Dans certains scénarios, la complexité peut dépasser O(1), puis nous pouvons les analyser en trouvant leur contrepartie O(1/g(n)). Par exemple, O(1/n) est plus complexe que O(1/n²).

#### 2. O(log(n)) est plus complexe que O(1), mais moins complexe que les polynômes

Comme la complexité est souvent liée aux algorithmes de type diviser pour régner, O(log(n)) est généralement une bonne complexité que vous pouvez atteindre pour les algorithmes de tri. O(log(n)) est moins complexe que O(√n), car la fonction racine carrée peut être considérée comme un polynôme, où l'exposant est 0,5.

#### 3. La complexité des polynômes augmente à mesure que l'exposant augmente

Par exemple, O(n⁵) est plus complexe que O(n⁴). En raison de sa simplicité, nous avons en fait passé en revue de nombreux exemples de polynômes dans les sections précédentes.

#### 4. Les exponentielles ont une complexité supérieure aux polynômes tant que les coefficients sont des multiples positifs de n

O(2ⁿ) est plus complexe que O(n⁹⁹), mais O(2ⁿ) est en fait moins complexe que O(1). Nous prenons généralement 2 comme base pour les exponentielles et les logarithmes car les choses tendent à être binaires en informatique, mais les exposants peuvent être changés en changeant les coefficients. Si non spécifié, la base pour les logarithmes est supposée être 2.

#### 5. Les factorielles ont une complexité supérieure aux exponentielles

Si vous êtes intéressé par le raisonnement, consultez la [**fonction Gamma**](https://en.wikipedia.org/wiki/Gamma_function), c'est une [**continuation analytique**](https://en.wikipedia.org/wiki/Analytic_continuation) d'une factorielle. Une courte preuve est que les factorielles et les exponentielles ont le même nombre de multiplications, mais les nombres qui sont multipliés croissent pour les factorielles, tandis qu'ils restent constants pour les exponentielles.

#### 6. Multiplier les termes

Lors de la multiplication, la complexité sera supérieure à l'originale, mais pas plus que l'équivalent de multiplier quelque chose qui est plus complexe. Par exemple, O(n * log(n)) est plus complexe que O(n) mais moins complexe que O(n²), car O(n²) = O(n * n) et n est plus complexe que log(n).

Pour tester votre compréhension, essayez de classer les fonctions suivantes de la plus complexe à la moins complexe. Les solutions avec des explications détaillées peuvent être trouvées dans une section ultérieure à mesure que vous lisez. Certaines d'entre elles sont destinées à être trompeuses et peuvent nécessiter une compréhension plus approfondie des mathématiques. À mesure que vous arriverez à la solution, vous les comprendrez mieux.

> **Question :** Classez les fonctions suivantes de la plus complexe à la moins complexe.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_69bzUpQxBwZFLBimaMe7kQ.png)
_Exemples tirés de [Problèmes de manuel](https://www.chegg.com/homework-help/questions-and-answers/problem-ask-refresh-knowledge-asymptotic-notations-rank-following-functions-order-growth-f-q23698273" rel="noopener)_

> **Solution à la question de la section 2 :**
>
> Il s'agissait en fait d'une question piège pour tester votre compréhension. La question essaie de vous faire répondre O(n²) parce qu'il y a une boucle for imbriquée. Cependant, n est censé être la taille de l'entrée. Puisque le tableau d'images est l'entrée, et que chaque pixel n'a été parcouru qu'une seule fois, la réponse est en fait O(n). La section suivante passera en revue d'autres exemples comme celui-ci.

### 5. Complexité temporelle et spatiale

Jusqu'à présent, nous n'avons discuté que de la complexité temporelle des algorithmes. C'est-à-dire que nous ne nous soucions que du temps nécessaire au programme pour accomplir la tâche. Ce qui compte également, c'est l'espace que le programme prend pour accomplir la tâche. La complexité spatiale est liée à la quantité de mémoire que le programme utilisera, et est donc également un facteur important à analyser.

La complexité spatiale fonctionne de manière similaire à la complexité temporelle. Par exemple, le tri par sélection a une complexité spatiale de O(1), car il ne stocke qu'une seule valeur minimale et son index pour la comparaison, l'espace maximum utilisé n'augmente pas avec la taille de l'entrée.

Certains algorithmes, comme le tri par compartiment, ont une complexité spatiale de O(n), mais sont capables de réduire la complexité temporelle à O(1). Le tri par compartiment trie le tableau en créant une liste triée de tous les éléments possibles dans le tableau, puis incrémente le compte chaque fois que l'élément est rencontré. À la fin, le tableau trié sera les éléments de la liste triée répétés selon leurs comptes.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_GfLWx2TXS55unwqZ5-X26w.png)
_Visualisation du tri par compartiment_

### 6. Meilleure, moyenne, pire, complexité attendue

La complexité peut également être analysée comme le meilleur cas, le pire cas, le cas moyen et le cas attendu.

Prenons **le tri par insertion**, par exemple. Le tri par insertion parcourt tous les éléments de la liste. Si l'élément est plus petit que son élément précédent, il insère l'élément en arrière jusqu'à ce qu'il soit plus grand que l'élément précédent.

![Image](https://cdn-media-1.freecodecamp.org/images/0*C9ork5K0ay7_CLBv.gif)
_Tri par insertion illustré, Image de [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort" rel="noopener" target="_blank" title=")_

Si le tableau est initialement trié, aucun échange ne sera fait. L'algorithme parcourra simplement le tableau une fois, ce qui résulte en une complexité temporelle de O(n). Par conséquent, nous dirions que la complexité temporelle **meilleur cas** du tri par insertion est O(n). Une complexité de O(n) est également souvent appelée **complexité linéaire**.

Parfois, un algorithme a simplement de la malchance. Le tri rapide, par exemple, devra parcourir la liste en O(n) temps si les éléments sont triés dans l'ordre inverse, mais en moyenne, il trie le tableau en O(n * log(n)) temps. Généralement, lorsque nous évaluons la complexité temporelle d'un algorithme, nous regardons leurs performances dans le **pire cas**. Plus d'informations sur cela et le tri rapide seront discutées dans la section suivante à mesure que vous lisez.

La complexité moyenne décrit la performance attendue de l'algorithme. Parfois, cela implique de calculer la probabilité de chaque scénario. Cela peut devenir compliqué d'entrer dans les détails et donc n'est pas discuté dans cet article. Ci-dessous se trouve une feuille de triche sur la complexité temporelle et spatiale des algorithmes typiques.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_XZsrnwao98R3dGTB.png)
_[Feuille de triche Big O](http://bigocheatsheet.com/" rel="noopener) pour les algorithmes courants_

> **Solution à la question de la section 4 :**

En inspectant les fonctions, nous devrions pouvoir classer immédiatement les polynômes suivants du plus complexe au moins complexe avec la règle 3. Où la racine carrée de n est simplement n à la puissance 0,5.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_RKlbisO36urUbi237TjyrQ.png)

En appliquant ensuite les règles 2 et 6, nous obtiendrons ce qui suit. Le logarithme en base 3 peut être converti en base 2 avec les **[conversions de base logarithmique](https://www.purplemath.com/modules/logrules5.htm)**. Le logarithme en base 3 croît encore un peu plus lentement que les logarithmes en base 2, et est donc classé après.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_6R1jrWMGXpKxBqtEre9q8Q.png)

Le reste peut sembler un peu trompeur, mais essayons de révéler leurs vrais visages et voyons où nous pouvons les placer.

Tout d'abord, 2 à la puissance de 2 à la puissance de n est supérieur à 2 à la puissance de n, et le +1 le rend encore plus complexe.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_eGLwpHDUJtr6CuALrpcQ2w.png)

Et ensuite, puisque nous savons que 2 à la puissance de log(n) avec une base de 2 est égal à n, nous pouvons convertir ce qui suit. Le logarithme avec 0,001 comme exposant croît un peu plus que les constantes, mais moins que presque tout le reste.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_4yo7najRBY_OaTnDpT3cIg.png)

Celui avec n à la puissance de log(log(n)) est en fait une variation du [**quasi-polynôme**](https://en.wikipedia.org/wiki/Time_complexity#Quasi-polynomial_time), qui est supérieur au polynôme mais inférieur à l'exponentiel. Puisque log(n) croît plus lentement que n, la complexité de celui-ci est un peu moindre. Celui avec le logarithme inverse converge vers une constante, car 1/log(n) diverge vers l'infini.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_ZYUCFuiSbOibqdSfmuwdvA.png)

Les factorielles peuvent être représentées par des multiplications, et peuvent donc être converties en additions en dehors de la fonction logarithmique. Le « n choisir 2 » peut être converti en un polynôme avec un terme cubique étant le plus grand.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_cbrjlMGsWYCs36u831pLTA.png)

Et enfin, nous pouvons classer les fonctions de la plus complexe à la moins complexe.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_NHVggTVMGjGOe7SxtSgIpQ.png)

### Pourquoi le Big O n'a pas d'importance

> **!!! — AVERTISSEMENT — !!!**
>
> Les contenus discutés ici sont généralement **non acceptés** par la plupart des programmeurs dans le monde. Discutez-en **à vos propres risques** lors d'un entretien. Les gens ont même blogué sur la façon dont ils ont **échoué** leurs entretiens chez Google parce qu'ils ont remis en question l'autorité, comme ici.
>
> **!!! — AVERTISSEMENT — !!!**

Puisque nous avons précédemment appris que la complexité temporelle dans le pire cas pour le tri rapide est O(n²), mais O(n * log(n)) pour le tri par fusion, le tri par fusion devrait être plus rapide — n'est-ce pas ? Eh bien, vous avez probablement deviné que la réponse est fausse. Les algorithmes sont simplement conçus de manière à ce que le tri rapide soit le « tri rapide ».

Pour démontrer, consultez ce [trinket.io](https://trinket.io/python/87a3166026) que j'ai créé. Il compare le temps pour le tri rapide et le tri par fusion. Je n'ai réussi à le tester que sur des tableaux d'une longueur allant jusqu'à 10 000, mais comme vous pouvez le voir jusqu'à présent, le temps pour le tri par fusion croît plus rapidement que le tri rapide. Malgré le fait que le tri rapide ait une complexité dans le pire cas de O(n²), la probabilité de cela est vraiment faible. Lorsque l'on en vient à l'augmentation de la vitesse que le tri rapide a sur le tri par fusion, limité par la complexité O(n * log(n)), le tri rapide finit par avoir une meilleure performance en moyenne.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_UvDTlLjNnQurODtnCWjEJg.png)
_Comparaison du temps entre le tri rapide et le tri par fusion_

J'ai également fait le graphique ci-dessous pour comparer le ratio entre le temps qu'ils prennent, car il est difficile de les voir à des valeurs plus basses. Et comme vous pouvez le voir, le pourcentage de temps pris pour le tri rapide est en ordre décroissant.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1_Zdm_8c-uU5941r7zJd4FPQ.png)
_Ratio de temps entre le tri rapide et le tri par fusion_

La morale de l'histoire est que la notation Big O n'est qu'une analyse mathématique pour fournir une référence sur les ressources consommées par l'algorithme. En pratique, les résultats peuvent être différents. Mais c'est généralement une bonne pratique d'essayer de réduire la complexité de nos algorithmes, jusqu'à ce que nous tombions sur un cas où nous savons ce que nous faisons.

### En fin de compte...

J'aime coder, apprendre de nouvelles choses et les partager avec la communauté. Si quelque chose vous intéresse particulièrement, faites-le moi savoir. J'écris généralement sur la conception web, l'architecture logicielle, les mathématiques et la science des données. Vous pouvez trouver d'excellents articles que j'ai écrits auparavant si vous êtes intéressé par l'un des sujets ci-dessus.

J'espère que vous passez un bon moment à apprendre l'informatique !!!
---
title: Un guide définitif de la logique conditionnelle en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-16T22:57:34.000Z'
originalURL: https://freecodecamp.org/news/a-definitive-guide-to-conditional-logic-in-javascript-23fa234d2ca3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uReSWIlSxDQFqdMx
tags:
- name: JavaScript
  slug: javascript
- name: Mathematics
  slug: mathematics
- name: Problem Solving
  slug: problem-solving
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Un guide définitif de la logique conditionnelle en JavaScript
seo_desc: 'By Nick Gard

  I am a front-end engineer and mathematician. I rely on my mathematical training
  daily in writing code. It’s not statistics or calculus that I use but, rather, my
  thorough understanding of Boolean logic. Often I have turned a complex comb...'
---

Par Nick Gard

Je suis ingénieur front-end et mathématicien. Je m'appuie sur ma formation mathématique quotidiennement pour écrire du code. Ce n'est pas la statistique ou le calcul que j'utilise, mais plutôt ma compréhension approfondie de la logique booléenne. Souvent, j'ai transformé une combinaison complexe d'espersands, de pipes, de points d'exclamation et de signes égaux en quelque chose de plus simple et beaucoup plus lisible. J'aimerais partager cette connaissance, alors j'ai écrit cet article. Il est long, mais j'espère qu'il sera aussi bénéfique pour vous qu'il l'a été pour moi. Bonne lecture !

### Valeurs truthy et falsy en JavaScript

Avant d'étudier les expressions logiques, comprenons ce qui est "truthy" en JavaScript. Puisque JavaScript est faiblement typé, il force les valeurs en booléens dans les expressions logiques. Les instructions `if`, `&&`, `||` et les conditions ternaires forcent toutes les valeurs en booléens. **Notez** que cela ne signifie pas qu'elles retournent toujours un booléen à partir de l'opération.

Il n'y a que six valeurs **falsy** en JavaScript — `false`, `null`, `undefined`, `NaN`, `0`, et `""` — et **tout le reste est truthy**. Cela signifie que `[]` et `{}` sont tous deux truthy, ce qui tend à piéger les gens.

### Les opérateurs logiques

En logique formelle, seuls quelques opérateurs existent : la négation, la conjonction, la disjonction, l'implication et la bicondition. Chacun de ces opérateurs a un équivalent en JavaScript : `!`, `&&`, `||`, `if (/* condition */) { /* alors conséquence */}`, et `===`, respectivement. Ces opérateurs créent toutes les autres déclarations logiques.

#### Tables de vérité

Tout d'abord, examinons les **tables de vérité** pour chacun de nos opérateurs de base. Une table de vérité nous indique quelle est la vérité d'une **expression** en fonction de la vérité de ses **parties**. Les tables de vérité sont importantes. **Si deux expressions génèrent la même table de vérité, alors ces expressions sont équivalentes et peuvent se remplacer l'une l'autre.**

La table de **négation** est très simple. La négation est le seul opérateur logique unaire, agissant uniquement sur une seule entrée. Cela signifie que `!A || B` n'est pas la même chose que `!(A || B)`. Les parenthèses agissent comme la notation de regroupement que vous trouveriez en mathématiques.

Par exemple, la première ligne de la table de vérité de la négation (ci-dessous) devrait être lue comme ceci : "si l'énoncé A est Vrai, alors l'expression !A est Faux."

![Image](https://cdn-media-1.freecodecamp.org/images/K-jmGbtTzpUdUPQH8SOuwSGnAVXir-YIAdvj)

Nier une simple déclaration n'est pas difficile. La négation de "il pleut" est "il ne pleut **pas**", et la négation du primitif `true` de JavaScript est, bien sûr, `false`. Cependant, nier des déclarations ou expressions complexes n'est pas si simple. Quelle est la négation de "il pleut **toujours**" ou `isFoo && isBar` ?

La table de **conjonction** montre que l'expression `A && B` est vraie uniquement si **A et B sont tous deux vrais**. Cela devrait être très familier de l'écriture en JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/dDDgyRcBXfG7LmENeZI720phsbo0QTdsNnkZ)

La table de **disjonction** devrait également être très familière. Une disjonction (déclaration logique OU) est vraie si **l'un ou l'autre** ou **les deux** de A et B sont vrais.

![Image](https://cdn-media-1.freecodecamp.org/images/RCuUvGM-KRXDzLFw85aMGmPCYUBUyuFV7wn9)

La table d'**implication** est moins familière. Puisque A **implique** B, A étant vrai implique que B est vrai. Cependant, B peut être vrai pour des raisons autres que A, ce qui explique pourquoi les deux dernières lignes du tableau sont vraies. La seule fois où l'implication est fausse est lorsque A est vrai et B est faux, car alors A n'implique pas B.

![Image](https://cdn-media-1.freecodecamp.org/images/nHexOd2buy2EfAZa83vhf984Pv9KBtP5QpJO)

Bien que les instructions `if` soient utilisées pour les implications en JavaScript, toutes les instructions `if` ne fonctionnent pas de cette manière. Habituellement, nous utilisons `if` comme un contrôle de flux, et non comme une vérification de vérité où la conséquence compte également dans la vérification. Voici l'instruction `if` archétypique d'**implication** :

```
function implication(A, B) {  if (A) {    return B;  } else {    /* si A est faux, l'implication est vraie */    return true;  }}
```

Ne vous inquiétez pas que cela soit quelque peu maladroit. Il existe des moyens plus faciles de coder les implications. En raison de cette maladresse, cependant, je continuerai à utiliser `[2192]` comme symbole pour les implications dans cet article.

L'opérateur **bicondition**, parfois appelé si-et-seulement-si (IFF), évalue à vrai uniquement si les deux opérandes, A et B, partagent la même valeur de vérité. En raison de la manière dont JavaScript gère les comparaisons, l'utilisation de `===` à des fins logiques ne doit être utilisée que sur des opérandes convertis en booléens. C'est-à-dire, au lieu de `A === B`, nous devrions utiliser `!!A === !!B`.

![Image](https://cdn-media-1.freecodecamp.org/images/gzfEIPFIl7rKvIuk6SnN15QjlxYovintRrP7)

![Image](https://cdn-media-1.freecodecamp.org/images/GkvYod28GzsLT4FsVkGKXzfIZHp7VBCJLca2)
_La table de vérité complète_

#### Mises en garde

Il y a deux grandes mises en garde à traiter le code JavaScript comme de la logique propositionnelle : **le court-circuit** et **l'ordre des opérations**.

Le court-circuit est quelque chose que les moteurs JavaScript font pour gagner du temps. Quelque chose qui ne changera pas la sortie de l'expression entière n'est pas évalué. La fonction `doSomething()` dans les exemples suivants n'est jamais appelée car, peu importe ce qu'elle retourne, le résultat de l'expression logique ne changerait pas :

```
// doSomething() n'est jamais appeléfalse && doSomething();true || doSomething();
```

Rappelons que les conjonctions (`&&`) sont vraies **uniquement si** **les deux déclarations sont vraies**, et les disjonctions (`||`) sont fausses **uniquement si les deux déclarations sont fausses**. Dans chacun de ces cas, après avoir lu la première valeur, aucun autre calcul n'a besoin d'être fait pour évaluer le résultat logique des expressions.

En raison de cette fonctionnalité, JavaScript brise parfois la commutativité logique. Logiquement, `A && B` est équivalent à `B && A`, mais vous briseriez votre programme si vous commutiez `window && window.mightNotExist` en `window.mightNotExist && window`. Cela ne veut pas dire que la **véracité** d'une expression commutée est différente, juste que JavaScript **peut** lancer une erreur en essayant de l'analyser.

L'[ordre des opérations en JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence#Table) m'a surpris car on ne m'a pas appris que la logique formelle **avait** un ordre des opérations, autre que par regroupement et de gauche à droite. Il s'avère que de nombreux langages de programmation considèrent `&&` comme ayant une priorité plus élevée que `||`. Cela signifie que `&&` est regroupé (non évalué) en premier, de gauche à droite, puis `||` est regroupé de gauche à droite. Cela signifie que `A || B && C` n'est **pas** évalué de la même manière que `(A || B) && C`, mais plutôt comme `A || (B && C)`.

```
true || false && false; // évalue à true(true || false) && false; // évalue à false
```

Heureusement, le **regroupement**, `()`, a la priorité la plus élevée en JavaScript. Nous pouvons éviter les surprises et les ambiguïtés en associant manuellement les déclarations que nous voulons évaluer ensemble en expressions discrètes. C'est pourquoi de nombreux linters de code interdisent d'avoir à la fois `&&` et `||` dans le même groupe.

#### Calcul des tables de vérité composées

Maintenant que la vérité des déclarations simples est connue, la vérité d'expressions plus complexes peut être calculée.

Pour commencer, comptez le nombre de variables dans l'expression et écrivez une table de vérité qui a 2ⁿ lignes.

Ensuite, créez une colonne pour chacune des variables et remplissez-les avec toutes les combinaisons possibles de valeurs vrai/faux. Je recommande de remplir la première moitié de la première colonne avec `T` et la seconde moitié avec `F`, puis de diviser la colonne suivante en quartiers et ainsi de suite jusqu'à ce que cela ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/NVVIXTUbqt51LffWcIyVfDMZfHbmUsOLnbf0)

Ensuite, écrivez l'expression et résolvez-la en couches, des groupes les plus internes vers l'extérieur pour chaque combinaison de valeurs de vérité :

![Image](https://cdn-media-1.freecodecamp.org/images/V0yaOQNhvwRxzaFldpBD652aU39U92GysKWk)

Comme indiqué ci-dessus, les expressions qui produisent la même table de vérité peuvent être substituées l'une à l'autre.

### Règles de remplacement

Maintenant, je vais couvrir plusieurs exemples de règles de remplacement que j'utilise souvent. Aucune table de vérité n'est incluse ci-dessous, mais vous pouvez les construire vous-même pour prouver que ces règles sont correctes.

#### Double négation

Logiquement, `A` et `!!A` sont équivalents. Vous pouvez toujours supprimer une double négation ou **ajouter** une double négation à une expression sans changer sa vérité. Ajouter une double négation est utile lorsque vous voulez nier une partie d'une expression complexe. La seule mise en garde ici est que dans JavaScript, `!!` agit également pour forcer une valeur en booléen, ce qui peut être un effet secondaire indésirable.

> `A === !!A`

#### Commutation

Toute disjonction (`||`), conjonction (`&&`), ou bicondition (`===`) peut échanger l'ordre de ses parties. Les paires suivantes sont _logiquement_ équivalentes, mais peuvent changer le calcul du programme en raison du court-circuit.

> `(A || B) === (B || A)`  
> `(A && B) === (B && A)`  
> `(A === B) === (B === A)`

#### Association

Les disjonctions et les conjonctions sont des opérations binaires, ce qui signifie qu'elles n'opèrent que sur deux entrées. Bien qu'elles puissent être codées en chaînes plus longues — `A || B || C || D` — elles sont implicitement associées de gauche à droite — `((A || B) || C) || D`. La règle d'association stipule que l'ordre dans lequel ces regroupements se produisent ne fait _aucune différence_ pour le résultat logique.

> `((A || B) || C) === (A || (B || C))`  
> `((A && B) && C) === (A && (B && C))`

#### Distribution

L'association ne fonctionne pas à travers les conjonctions et les disjonctions. C'est-à-dire, `(A && (B || C)) !== ((A && B) || C)`. Afin de dissocier `B` et `C` dans l'exemple précédent, vous devez _distribuer_ la conjonction — `(A && B) || (A && C)`. Ce processus fonctionne également en sens inverse. Si vous trouvez une expression composée avec une disjonction ou une conjonction répétée, vous pouvez la redistribuer, comme factoriser un facteur commun dans une expression algébrique.

> `(A && (B || C)) === ((A && B) || (A && C))`  
> `(A || (B && C)) === ((A || B) && (A || C))`

Une autre occurrence courante de la distribution est la double-distribution (similaire à FOIL en algèbre) :  
1. `((A || B) && (C || D)) === ((A || B) && C) || ((A || B) && D)`  
2. `((A || B) && C) || ((A || B) && D) ===`  
`((A && C) || B && C)) || ((A && D) || (B && D))`

> `(A || B) && (C || D) === (A && C) || (B && C) || (A && D) || (B && D)`  
> `(A && B) ||(C && D) === (A || C) && (B || C) && (A || D) && (B || D)`

#### Implication matérielle

Les expressions d'implication (`A [2192] B`) sont généralement traduites en code sous la forme `if (A) { B }` mais ce n'est pas très utile si une expression composée contient plusieurs implications. Vous vous retrouveriez avec des instructions `if` imbriquées — une mauvaise odeur de code. Au lieu de cela, j'utilise souvent la règle de remplacement de l'implication matérielle, qui dit que `A [2192] B` signifie soit `A` est faux, soit `B` est vrai.

> `(A [2192] B) === (!A || B)`

#### Tautologie et contradiction

Parfois, au cours de la manipulation d'expressions logiques composées, vous vous retrouverez avec une simple conjonction ou disjonction qui n'implique qu'une seule variable et sa négation ou un littéral booléen. Dans ces cas, l'expression est soit toujours vraie (une tautologie), soit toujours fausse (une contradiction) et peut être remplacée par le littéral booléen dans le code.

> `_(A || !A) === true_`  
> `_(A || true) === true_`  
> `_(A && !A) === false_`  
> `_(A && false) === false_`

En relation avec ces équivalences se trouvent la disjonction et la conjonction avec l'autre littéral booléen. Celles-ci peuvent être simplifiées en la vérité de la variable.

> `_(A || false) === A_`  
> `_(A && true) === A_`

#### Transposition

Lors de la manipulation d'une implication (`A [2192] B`), une erreur courante que les gens commettent est de supposer que la négation de la première partie, `A`, implique que la deuxième partie, `B`, est également négative — `!A [2192] !B`. Cela s'appelle la _converse_ de l'implication et elle n'est **pas nécessairement vraie**. C'est-à-dire, avoir l'implication originale ne nous dit pas si la converse est vraie car `A` n'est pas une condition _nécessaire_ de `B`. (Si la converse est également vraie — pour des raisons indépendantes — alors `A` et `B` sont biconditionnels.)

Ce que nous pouvons savoir de l'implication originale, cependant, c'est que la _contraposée_ est vraie. Puisque `B` _est_ une condition nécessaire pour `A` (rappelons de la table de vérité pour l'implication que si `B` est vrai, `A` doit également être vrai), nous pouvons affirmer que `!B [2192] !A`.

> `_(A [2192] B) === (!B [2192] !A)_`

#### Équivalence matérielle

Le nom _biconditionnel_ vient du fait qu'il représente deux déclarations conditionnelles (implications) : `A === B` signifie que `A [2192] B` **et** `B [2192] A`. Les valeurs de vérité de `A` et `B` sont verrouillées l'une dans l'autre. Cela nous donne la première règle d'équivalence matérielle :

> `_(A === B) === ((A [2192] B) && (B [2192] A))_`

En utilisant l'implication matérielle, la double-distribution, la contradiction et la commutation, nous pouvons manipuler cette nouvelle expression en quelque chose de plus facile à coder :  
1. `((A [2192] B) && (B [2192] A)) === ((!A || B) && (!B || A))`  
2. `((!A || B) && (!B || A)) ===`   
`((!A && !B) || (B && !B)) || ((!A && A) || (B && A))`  
3. `((!A && !B) || (B && !B)) || ((!A && A) || (B && A)) ===`   
`((!A && !B) || (B && A))`  
4. `((!A && !B) || (B && A)) === ((A && B) || (!A && !B))`

> `_(A === B) === ((A && B) || (!A && !B))_`

#### Exportation

Les instructions `if` imbriquées, surtout s'il n'y a pas de parties `else`, sont une mauvaise odeur de code. Une simple instruction `if` imbriquée peut être réduite à une seule instruction où la conditionnelle est une conjonction des deux conditions précédentes :

```
if (A) {  if (B) {    C  }}// est équivalent àif (A && B) {  C}
```

> `_(A [2192] (B [2192] C)) === ((A && B) [2192] C)_`

#### Lois de DeMorgan

Les lois de DeMorgan sont essentielles pour travailler avec des déclarations logiques. Elles indiquent comment distribuer une négation à travers une conjonction ou une disjonction. Considérons l'expression `!(A || B)`. Les lois de DeMorgan disent que lors de la négation d'une disjonction ou d'une conjonction, il faut nier chaque déclaration et changer le `&&` en `||` ou vice versa. Ainsi, `!(A || B)` est la même chose que `!A && !B`. De même, `!(A && B)` est équivalent à `!A || !B`.

> `_!(A || B) === !A && !B_`  
> `_!(A && B) === !A || !B_`

#### Ternaire (Si-Alors-Sinon)

Les déclarations ternaires (`A ? B : C`) apparaissent régulièrement en programmation, mais elles ne sont pas tout à fait des implications. La traduction d'un ternaire en logique formelle est en fait une conjonction de deux implications, `A [2192] B` et `!A [2192] C`, que nous pouvons écrire comme : `(!A || B) && (A || C)`, en utilisant l'implication matérielle.

> `_(A ? B : C) === (!A || B) && (A || C)_`

#### XOR (Ou Exclusif)

Le Ou Exclusif, souvent abrégé **xor**, signifie "l'un ou l'autre, mais pas les deux". Cela diffère de l'opérateur _ou_ normal uniquement en ce que les deux valeurs ne peuvent pas être vraies. C'est souvent ce que nous voulons dire lorsque nous utilisons "ou" en anglais simple. JavaScript n'a pas d'opérateur xor natif, alors comment le représenter ?   
1. "A ou B, mais pas les deux A et B"  
2. `(A || B) && !(A && B)` _traduction directe_  
3. `(A || B) && (!A || !B)` _Lois de DeMorgan_  
4. `(!A || !B) && (A || B)` _commutativité_  
5. `A ? !B : B` _définition si-alors-sinon_

> `_A ? !B : B_` est le ou exclusif (xor) en JavaScript

Alternativement,  
1. "A ou B, mais pas les deux A et B"  
2. `(A || B) && !(A && B)` _traduction directe_  
3. `(A || B) && (!A || !B)` _Lois de DeMorgan_  
4. `(A && !A) || (A && !B) || (B && !A) || (B && !B)` _double-distribution_  
5. `(A && !B) || (B && !A)` _remplacement de contradiction_  
6. `A === !B` ou `A !== B` _équivalence matérielle_

> `_A === !B_` _ou `A !== B`_ est xor en JavaScript

### Logique des ensembles

Jusqu'à présent, nous avons examiné des déclarations sur des expressions impliquant deux (ou quelques) valeurs, mais maintenant nous allons tourner notre attention vers des ensembles de valeurs. Tout comme les opérateurs logiques dans les expressions composées préservent la vérité de manière prévisible, les _fonctions prédicats_ sur les ensembles préservent la vérité de manière prévisible.

Une **fonction prédicat** est une fonction dont l'entrée est une valeur d'un ensemble et dont la sortie est un booléen. Pour les exemples de code suivants, j'utiliserai un tableau de nombres pour un ensemble et deux fonctions prédicats : `isOdd = n => n % 2 !==` 0; et `isEven = n => n % 2` === 0;.

#### Déclarations universelles

Une déclaration **universelle** est celle qui s'applique à **tous** les éléments d'un ensemble, ce qui signifie que sa fonction prédicat retourne vrai pour chaque élément. Si le prédicat retourne faux pour un (ou plusieurs) élément(s), alors la déclaration universelle est fausse. `Array.prototype.every` prend une fonction prédicat et retourne `true` uniquement si chaque élément du tableau retourne vrai pour le prédicat. Il se termine également tôt (avec `false`) si le prédicat retourne faux, sans exécuter le prédicat sur d'autres éléments du tableau, donc en pratique _évitez les effets secondaires dans les prédicats_.

Par exemple, considérons le tableau `[2, 4, 6, 8]`, et la déclaration universelle, "chaque élément du tableau est pair". En utilisant `isEven` et la fonction universelle intégrée de JavaScript, nous pouvons exécuter `[2, 4, 6, 8].every(isEven)` et trouver que cela est `true`.

> `_Array.prototype.every_` est la déclaration universelle de JavaScript

#### Déclarations existentielles

Une déclaration **existentielle** fait une affirmation spécifique sur un ensemble : au moins un élément de l'ensemble retourne vrai pour la fonction prédicat. Si le prédicat retourne faux pour chaque élément de l'ensemble, alors la déclaration existentielle est fausse.

JavaScript fournit également une déclaration existentielle intégrée : `Array.prototype.some`. Similaire à `every`, `some` retournera tôt (avec true) si un élément satisfait son prédicat. Par exemple, `[1, 3, 5].some(isOdd)` n'exécutera qu'une seule itération du prédicat `isOdd` (consommant `1` et retournant `true`) et retournera `true`. `[1, 3, 5].some(isEven)` retournera `false`.

> `_Array.prototype.some_` est la déclaration existentielle de JavaScript

#### Implication universelle

Une fois que vous avez vérifié une déclaration universelle par rapport à un ensemble, disons `nums.every(isOdd)`, il est tentant de penser que vous pouvez prendre un élément de l'ensemble qui satisfait le prédicat. Cependant, il y a un piège : en logique booléenne, une déclaration universelle vraie **n'implique pas** que l'ensemble est non vide. Les déclarations universelles sur les ensembles vides sont _toujours vraies_, donc si vous souhaitez prendre un élément d'un ensemble satisfaisant une certaine condition, utilisez une vérification existentielle à la place. Pour prouver cela, exécutez `[].every(() => fal`se). Cela sera vrai.

> Les déclarations universelles sur les ensembles vides sont **toujours vraies**_._

#### Négation des déclarations universelles et existentielles

Nier ces déclarations peut être surprenant. La négation d'une déclaration universelle, disons `nums.every(isOdd)`, n'est pas `nums.every(isEven)`, mais plutôt `nums.some(isEven)`. Il s'agit d'une déclaration existentielle avec le prédicat nié. De même, la négation d'une déclaration existentielle est une déclaration universelle avec le prédicat nié.

> `_!arr.every(el => fn(el)) === arr.some(el => !fn(el))_`  
> `_!arr.some(el => fn(el)) === arr.every(el => !fn(el))_`

#### Intersections d'ensembles

Deux ensembles ne peuvent être liés l'un à l'autre que de quelques manières, en ce qui concerne leurs éléments. Ces relations sont facilement représentées par des diagrammes de Venn et peuvent (pour la plupart) être déterminées en code en utilisant des combinaisons de déclarations universelles et existentielles.

Deux ensembles peuvent partager certains mais pas tous leurs éléments, comme un diagramme de Venn _conjoint_ typique :

![Image](https://cdn-media-1.freecodecamp.org/images/MGx95CkbyLkzZji3SW1ch-kukLO23IIuDYxv)

> `_A.some(el => B.includes(el)) && A.some(el => !B.includes(el)) && B.some(el => !A.includes(el))_ décrit une paire d'ensembles conjoints

Un ensemble peut contenir tous les éléments de l'autre ensemble, mais avoir des éléments non partagés par le deuxième ensemble. Il s'agit d'une relation de **sous-ensemble**, notée `Subset [2286] Superset`.

![Image](https://cdn-media-1.freecodecamp.org/images/za1zDosVZwMxkxXR-WPRHYB3pfGiwG0zJyNL)

> `_B.every(el => A.includes(el))_ décrit la relation de sous-ensemble B [2286] A

Les deux ensembles peuvent ne partager **aucun** élément. Ce sont des ensembles _disjoints_.

![Image](https://cdn-media-1.freecodecamp.org/images/sWWv066Leg7ceuP6TvZj2zIeK2xUy2MwItfn)

> `_A.every(el => !B.includes(el))_ décrit une paire d'ensembles disjoints

Enfin, les deux ensembles peuvent partager chaque élément. C'est-à-dire qu'ils sont des sous-ensembles l'un de l'autre. Ces ensembles sont _égaux_. En logique formelle, nous écririons `A [2286] B && B [2286] A [27f7] A === B`, mais en JavaScript, il y a quelques complications avec cela. En JavaScript, un `Array` est un ensemble _ordonné_ et peut contenir des valeurs en double, donc nous **ne pouvons pas** supposer que le code de sous-ensemble bidirectionnel `B.every(el => A.includes(el)) && A.every(el => B.includes(el))` implique que les tableaux `A` et B sont égaux. Si `A` et B sont des Sets (c'est-à-dire qu'ils ont été créés `avec new` Set()), alors leurs valeurs sont uniques et nous pouvons faire la vérification de sous-ensemble bidirectionnelle pour voir si A` === B.

![Image](https://cdn-media-1.freecodecamp.org/images/LkvQeGAGIZhEpxtaDnOJRv0FTzomcqioyPYJ)

> `_(A === B) === (Array.from(A).every(el => Array.from(B).includes(el)) && Array.from(B).every(el => Array.from(A).includes(el)), étant donné que `_A_` et B sont construits `_en utilisant new_` Set()

### Traduction de la logique en anglais

Cette section est probablement la plus utile de l'article. Maintenant que vous connaissez les opérateurs logiques, leurs tables de vérité et les règles de remplacement, vous pouvez apprendre à traduire une phrase anglaise en code et à la _simplifier_. En apprenant cette compétence de traduction, vous serez également capable de _lire_ le code plus facilement, en stockant une logique complexe dans des phrases simples dans votre esprit.

Ci-dessous se trouve un tableau de code logique (à gauche) et leurs équivalents en anglais (à droite) qui a été largement emprunté au livre excellent, [_Essentials of Logic_](https://www.amazon.com/Essentials-Logic-Irving-Copi/dp/013238034X/ref=sr_1_1?ie=UTF8&qid=1531944915&sr=8-1&keywords=essentials+of+logic&selectObb=rent)_._

![Image](https://cdn-media-1.freecodecamp.org/images/YtimcMWoAB7lsuFgCN7nFdCw7aBdu8Ir15rx)
_Voir une version lisible à l'écran de ce tableau de traduction code-anglais [ici](https://docs.google.com/spreadsheets/d/e/2PACX-1vTei2ttk-psZ1ynH74emvJVIoFu7qPpY6c1LdZHrv5qnTBqQorR-tOXrmRggcn8DvYAbv-Z0z0cNCSc/pubhtml?gid=0&amp;single=true" rel="noopener" target="_blank" title=")._

Ci-dessous, je vais passer en revue quelques exemples concrets de mon propre travail où j'interprète de l'anglais vers le code, et vice-versa, et simplifie le code avec les règles de remplacement.

#### Exemple 1

Récemment, pour satisfaire aux exigences du RGPD de l'UE, j'ai dû créer une modale qui montrait la politique de cookies de mon entreprise et permettait à l'utilisateur de définir ses préférences. Pour rendre cela aussi peu intrusif que possible, nous avions les exigences suivantes (par ordre de priorité) :

1. Si l'utilisateur n'était pas dans l'UE, **ne jamais** montrer la modale des préférences RGPD.
2. Si l'application devait montrer la modale de manière programmatique (si une action de l'utilisateur nécessitait plus de permissions que celles actuellement autorisées), montrer la modale.
3. Si l'utilisateur était autorisé à avoir la bannière RGPD moins intrusive, ne pas montrer la modale.
4. Si l'utilisateur **n'avait pas** déjà défini ses préférences (ironiquement sauvegardées dans un cookie), montrer la modale.

J'ai commencé avec une série d'instructions `if` modélisées directement après ces exigences :

```
const isGdprPreferencesModalOpen = ({  shouldModalBeOpen,  hasCookie,  hasGdprBanner,  needsPermissions}) => {  if (!needsPermissions) {    return false;  }  if (shouldModalBeOpen) {    return true;  }  if (hasGdprBanner) {    return false;  }  if (!hasCookie) {    return true;  }  return false;}
```

Pour être clair, le code ci-dessus fonctionne, mais [retourner des littéraux booléens est une mauvaise odeur de code](https://medium.com/@ntgard/returning-boolean-literals-is-a-code-smell-7a39531d6b60). J'ai donc suivi les étapes suivantes :

```
/* changer pour une structure if-else-if à retour unique */let result;if (!needsPermissions) {  result = false;} else if (shouldBeOpen) {  result = true;} else if (hasBanner) {  result = false;} else if (!hasCookie) {  result = true} else {  result = false;}return result;
```

```
/* utiliser la définition de ternaire pour convertir en un seul retour */return !needsPermissions ? false : (shouldBeOpen ? true : (hasBanner ? false : (!hasCookie ? true : false)))
```

```
/* convertir des ternaires en conjonctions de disjonctions */return (!!needsPermissions || false) && (!needsPermissions || ((!shouldBeOpen || true) && (shouldBeOpen || ((!hasBanner || false) && (hasBanner || !hasCookie))))
```

```
/* simplifier les doubles négations et les conjonctions/disjonctions avec des littéraux booléens */return needsPermissions && (!needsPermissions || ((!shouldBeOpen || true) && (shouldBeOpen || (!hasBanner && (hasBanner || !hasCookie))))
```

```
/* Lois de DeMorgan */return needsPermissions && (!needsPermissions || ((!shouldBeOpen || true) && (shouldBeOpen || ((!hasBanner && hasBanner) || (hasBanner && !hasCookie))))
```

```
/* éliminer les tautologies et les contradictions, simplifier */return needsPermissions && (!needsPermissions || (shouldBeOpen || (hasBanner && !hasCookie)))
```

```
/* Lois de DeMorgan */return (needsPermissions && !needsPermissions) || (needsPermissions && (shouldBeOpen || (hasBanner && !hasCookie)))
```

```
/* éliminer la contradiction, simplifier */return needsPermissions && (shouldBeOpen || (hasBanner && !hasCookie))
```

J'ai fini par obtenir quelque chose que je pense être plus élégant et toujours lisible :

```
const isGdprPreferencesModalOpen = ({  needsPermissions,  shouldBeOpen,  hasBanner,  hasCookie,}) => (  needsPermissions && (shouldBeOpen || (!hasBanner && !hasCookie)));
```

#### Exemple 2

J'ai trouvé le code suivant (écrit par un collègue) en mettant à jour un composant. Encore une fois, j'ai ressenti l'envie d'éliminer les retours de littéraux booléens, alors je l'ai refactorisé.

```
const isButtonDisabled = (isRequestInFlight, state) => {  if (isRequestInFlight) {    return true;  }  if (enabledStates.includes(state)) {    return false;  }  return true;};
```

Parfois, je fais les étapes suivantes dans ma tête ou sur du papier brouillon, mais le plus souvent, j'écris chaque étape suivante dans le code et supprime ensuite l'étape précédente.

```
// convertir en structure if-else-iflet result;if (isRequestInFlight) {  result = true;} else if (enabledStates.includes(state)) {  result = false;} else {  result = true;}return result;
```

```
// convertir en ternairereturn isRequestInFlight  ? true  : enabledStates.includes(state)    ? false    : true;
```

```
/* convertir du ternaire en conjonction de disjonctions */return (!isRequestInFlight || true) && (isRequestInFlight || ((!enabledStates.includes(state) || false) && (enabledStates.includes(state) || true))
```

```
/* supprimer les tautologies et les contradictions, simplifier */return isRequestInFlight || !enabledStates.includes(state)
```

Je finis par obtenir :

```
const isButtonDisabled = (isRequestInFlight, state) => (  isRequestInFlight || !enabledStates.includes(state));
```

Dans cet exemple, je n'ai pas commencé par des phrases en anglais et je n'ai jamais pris la peine d'interpréter le code en anglais pendant les manipulations, mais maintenant, à la fin, je peux facilement traduire cela : "le bouton est désactivé si soit la requête est en cours, soit l'état n'est pas dans l'ensemble des états activés." Cela a du sens. Si vous traduisez votre travail en anglais et que cela _n'a pas_ de sens, revérifiez votre travail. Cela m'arrive souvent.

#### Exemple 3

En écrivant un framework de test A/B pour mon entreprise, nous avions deux listes principales d'expériences activées et désactivées et nous voulions vérifier que _chaque_ expérience (chacune un fichier séparé dans un dossier) était enregistrée dans l'une ou l'autre liste **mais pas les deux**. Cela signifie que les ensembles activés et désactivés sont _disjoints_ et que l'ensemble de toutes les expériences est un sous-ensemble de la conjonction des deux ensembles d'expériences. La raison pour laquelle l'ensemble de toutes les expériences doit être un sous-ensemble de la combinaison des deux listes est qu'il ne devrait pas y avoir une seule expérience qui existe _en dehors_ des deux listes.

```
const isDisjoint = !enabled.some(el => disabled.includes(el)) &&   !disabled.some(el => enabled.includes(el));const isSubset = allExperiments.every(  el => enabled.concat(disabled).includes(el));assert(isDisjoint && isSubset);
```

### Conclusion

J'espère que tout cela a été utile. Non seulement les compétences de traduction entre l'anglais et le code sont utiles, mais avoir la terminologie pour discuter des différentes relations (comme les conjonctions et les implications) et les outils pour les évaluer (tables de vérité) est pratique.
---
title: Comment aborder la recherche de racines en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-02T16:12:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-tackle-root-finding-in-javascript-40d2c34507b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UAE-xb9qHM4PuRbNc-eu3g.jpeg
tags:
- name: calculus
  slug: calculus
- name: JavaScript
  slug: javascript
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment aborder la recherche de racines en JavaScript
seo_desc: 'By Zaid Humayun

  Introduction

  I’ve been wanting to write about this topic for a while now. I recently had the
  opportunity to work on simulating the GoalSeek functionality of Excel for a web
  application. I found the whole purpose of GoalSeek and how it...'
---

Par Zaid Humayun

### Introduction

J'avais envie d'écrire sur ce sujet depuis un certain temps. J'ai récemment eu l'opportunité de travailler sur la simulation de la fonctionnalité GoalSeek d'Excel pour une application web. J'ai trouvé tout le but de GoalSeek et son fonctionnement fascinants.

Le but de GoalSeek dans Excel est de trouver une entrée pour une équation qui fournira la solution souhaitée. Pour comprendre comment cela est censé fonctionner, nous allons considérer quelque chose de vraiment simple.

### Qu'est-ce que GoalSeek ?

Prenons l'exemple de la recherche du montant dû sur la base d'un principal en utilisant la formule des intérêts simples.

L'équation pour la formule des intérêts simples est, eh bien, simple :

```
A = P(1+rt), eqn(1)
```

```
P -> principalr -> taux d'intérêtt -> temps en années
```

Nous allons définir les valeurs suivantes :

```
P -> 10000r -> 7.5t -> 15
```

Cela nous donne le montant dû comme étant :

```
A = 10000(1+7.5*15) = 1135000
```

Maintenant, disons que les exigences pour notre solution ont changé. Au lieu de _trouver le montant dû_ sur la base du principal, du taux d'intérêt et du temps, nous devons plutôt trouver le _taux d'intérêt qui nous donnera le montant dû souhaité_ mais en gardant le principal et le temps identiques.

Modifions l'exemple maintenant :

```
P -> 10000r -> ?t -> 15A -> 1120000
```

Ici, nous essayons de trouver le taux d'intérêt qui nous permettra de payer 1120000 au lieu de 1135000. Nous pouvons résoudre cela en échangeant les variables.

```
A = P(1+rt) => 1120000 = 10000(1+r*15)
```

```
1+15*r = 1120000 / 10000 => r = (112 - 1) / 15
```

```
r = 7.4%
```

Brillant ! Nous avons réussi ! Nous avons fait quelque chose que GoalSeek d'Excel fait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dh3k5_mfbzp0ZjLr3xOvSw.gif)
_Gif capture de la fonctionnalité Excel GoalSeek_

Un problème, cependant. C'était une équation vraiment simple. Que se passe-t-il si l'équation est beaucoup plus complexe et implique des fonctions trigonométriques ainsi que plusieurs solutions possibles ? Je vais vous donner un exemple d'équation que vous pourriez résoudre avec GoalSeek :

```
f(x, y) = 1550 - (4*x/y * sinh(y/2 * 1500 / (2*x))), eqn(2)
```

Oui, cela semble définitivement compliqué. L'un des facteurs intimidants lorsque je regarde quelque chose comme cela est que les choses sont exprimées comme des fonctions avec des variables dépendantes.

N'était-ce pas plus facile de regarder `A = P(1+rt)` ? Certes, cela est aussi dû au fait que l'équation est beaucoup plus petite.

Mais, que se passe-t-il si nous la réécrivions comme ceci :

```
f(P, r, t) = P(1+rt)
```

Vous voyez ? C'est toujours la même chose.

Revenons à l'équation (2). Que se passe-t-il si nous avons l'énoncé de problème suivant :

```
0 = 1550 - (4*x/0.022 * sinh(0.022/2 * 1500 / (2*x))), résoudre pour x
```

Eh bien, encore une fois, tout ce que vous faites vraiment est de résoudre pour une variable, mais regardez simplement à quel point le problème s'est compliqué. Et c'est principalement à cause de ce `sinh` ennuyeux qui se trouve dans l'équation.

D'accord, si vous êtes nouveau dans ce domaine, j'imagine que les choses deviennent un peu écrasantes. Faisons un pas en arrière et réfléchissons à ce que nous avons compris jusqu'à présent.

1. Nous avons compris qu'il n'y a pas de réelle différence entre écrire une fonction avec des notations comme les deux suivantes :

```
f(P, r, t) = P(1+rt)A = P(1+rt)
```

2. Nous avons compris que nous pouvons résoudre pour une variable afin d'obtenir le résultat souhaité. Cependant, plus l'équation est complexe, plus il est compliqué d'obtenir la solution.

Nous avons deux équations de difficultés très opposées à résoudre. Je vais introduire une troisième équation qui aidera à combler l'écart.

```
y = 2x^2+3x-5, eqn(3)
```

L'équation ci-dessus est une fonction parabolique de base. Voici à quoi ressemble l'équation lorsqu'elle est tracée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*v1T8kOf8DVqnD-sH7oc3vQ.png)
_Tracé de 2x²+3x-5_

D'accord, réfléchissons maintenant à la manière de résoudre cette équation. Disons que nous voulons résoudre pour `x` de sorte que `y = 0` :

```
y = 2x^2+3x-5 => 2x^2+3x-5 = 0
```

```
x = [-3 + sqrt(3^2 - 4*2*(-5))] / (2*2),     [-3 - sqrt(3^2 - 4*2*(-5))] / (2*2)]
```

```
x = 1, -2.5
```

Si vous vous demandez d'où vient l'équation pour les solutions, notez qu'il s'agit simplement de la solution classique à une équation quadratique.

```
y = ax^2+bx+c, où y = 0 => ax^2+bx+c = 0
```

```
x = -b+sqrt(b^2-4ac) / 2a, x = -b-sqrt(b^2-4ac) / 2a
```

_Note : Si vous voulez savoir comment cette solution a été dérivée, consultez [ici](https://www.purplemath.com/modules/sqrquad2.htm#formula)._

Eh bien, c'est une façon de résoudre l'équation. Vous pourriez potentiellement écrire un analyseur qui pourrait accepter n'importe quelle équation, vérifier les coefficients, les séparer avec précision et ensuite essayer de résoudre l'équation. Vous pourriez également utiliser la merveilleuse bibliothèque [algebra.js](https://algebra.js.org/#equations) ici, qui fait ce que je viens de décrire.

Cependant, si vous regardez le graphique, vous remarquerez que vous auriez pu résoudre cela graphiquement. Le but était de trouver le point sur la courbe où `y = 0`

Eh bien, regardez attentivement et voyez où la courbe croise l'axe des X. Elle le croise en deux points : `[1, -2.5]` Voici votre solution !

Maintenant, vous pensez probablement que c'est génial, mais je ne peux pas exactement apprendre à un ordinateur à regarder le graphique, trouver les points où il croise l'axe des X et identifier ces points. Eh bien, potentiellement vous pourriez, avec une forme de modèle entraîné pour la reconnaissance d'image, mais c'est un autre article. Alors, comment pouvons-nous trouver notre chemin autour de cela ?

Il existe deux méthodes que nous pouvons utiliser, et ce sont celles que je vais explorer en profondeur dans cet article.

Elles sont appelées la **méthode de Newton-Raphson** et la **méthode de bisection**.

Je vais vous donner un bref aperçu de la manière dont chaque méthode fonctionne.

**Version TL;DR**

La méthode de Newton-Raphson fonctionne en choisissant un point aléatoire et en traçant une ligne tangente à ce point. Elle calcule ensuite une nouvelle valeur `x` qui est plus proche de la racine. Si vous continuez à répéter cela, vous trouverez la racine.

La méthode de bisection fonctionne sur le principe de trouver l'intervalle dans lequel se trouve la racine. Une fois l'intervalle précis trouvé, la solution est obtenue en utilisant un algorithme similaire à celui utilisé pour la recherche binaire.

Examinons chacune d'elles plus en détail.

### Méthode de Newton-Raphson

D'accord, plongeons dans la méthode de Newton-Raphson. La méthode de Newton-Raphson est basée sur trois idées majeures.

1. La tangente à une courbe en un point spécifique est une ligne droite
2. La tangente à une courbe en un point spécifique est également la dérivée de la courbe en ce point
3. L'équation d'une ligne droite, qui est : `y = mx + c`

![Image](https://cdn-media-1.freecodecamp.org/images/1*QDGdH6GRcih-TU189cHX2w.png)
_Tangente à une courbe en un point. Source : [https://brilliant.org/wiki/newton-raphson-method/](https://brilliant.org/wiki/newton-raphson-method/" rel="noopener" target="_blank" title=")_

L'image ci-dessus est celle d'une courbe aléatoire avec une tangente tracée.

Nous avons choisi un point aléatoire `x_n` sur l'axe des X.

`f(x_n)` est l'équivalent du point sur la courbe. c'est-à-dire l'interception y

`f'(x_n)` est la tangente à la courbe au point f(x_n).

`x_(n+1)` est le point où la tangente interceptée l'axe des X.

Rappelez-vous, nous avons dit que nous voulions trouver le point où la courbe croise l'axe des X, car cela nous donnerait notre solution. Remarquez, le point `x_(n+1)` est beaucoup plus proche de la solution que `x_n`, malgré le fait que nous avons choisi `x_n` au hasard.

Eh bien, que se passerait-il si nous répétions le même processus, sauf que cette fois avec `x_(n+1)` comme notre nouveau point initial ? Eh bien, présumément, nous aboutirions à un nouveau `x` qui est encore plus proche de la solution.

Alors, comment trouvons-nous le point `x_(n+1)` étant donné l'équation, la dérivée et le `x_n` original ?

Revenons à l'équation d'une ligne droite : `y = mx+c`

Nous avons dit que la tangente à une courbe en un point est une ligne droite.

Nous avons également dit que l'interception y est égale à `f(x_n)`

Nous savons du calcul que la dérivée est égale à la pente.

Par conséquent, nous obtenons ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7Uoj0Og0M-rM0BFrHMcmRw.png)
_Équation d'une ligne_

Maintenant, nous devons trouver la racine de cette ligne tangente, donc nous définissons `y = 0` et `x = x_(n+1)`, et nous résolvons pour `x_(n+1)`

Cela nous donne ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yoa_cFXA4ywq0yUGg6VJYw.png)
_Source : [https://brilliant.org/wiki/newton-raphson-method/](https://brilliant.org/wiki/newton-raphson-method/" rel="noopener" target="_blank" title=")_

Maintenant, nous avons tout ce dont nous avons besoin pour résoudre `x_(n+1)`.

Cela m'a dépassé la première fois que j'ai vu toutes les équations, alors essayons avec un exemple pour voir comment cela fonctionne.

Nous allons prendre l'équation (2) et la travailler. Choisissons `x_n=3`

```
f(x) = 2x^2+3x-5f'(x) = 4x+3f(3) = 18+9-5 = 22f'(3) = 15x_1 = 3 - 22/15 = 1.53
```

```
f(1.53) = 4.2718f'(1.53) = 9.12x_2 = 1.53 - 4.2718/9.12 = 1.0616
```

Si vous suivez cela jusqu'au bout, vous devriez obtenir une solution où `x=1` et comme nous le savons d'après le graphique précédent, c'est l'une de nos solutions.

Si vous remarquez ce que nous avons fait ci-dessus, c'est simplement suivre une série d'étapes dans un certain ordre de manière répétée, c'est-à-dire la définition même d'un algorithme. Voici à quoi ressemble le code pour la même chose.

L'extrait de code utilise largement la bibliothèque [math.js](http://mathjs.org/). Les principales fonctions que j'utilise sont math.derivative et math.eval. Elles calculent respectivement la dérivée d'une expression et évaluent une expression basée sur un objet de paires clé-valeur.

La partie de l'extrait de code à laquelle je veux attirer votre attention est les lignes 14-16.

```
if (Math.abs(result - guess) < Math.exp(-15)) {              return result        }
```

Ce que nous faisons ici, c'est définir la condition de base pour mettre fin à notre itération. Nous disons que si la différence entre `x_n` et `x_(n+1)` est inférieure à `10^(-15)`, retourner le résultat.

Si vous travaillez sur l'exercice précédent jusqu'au bout, vous arriverez à une situation où chaque valeur successive de `x` est presque identique à la valeur précédente de `x`, et c'est ainsi que nous savons que nous avons trouvé une solution.

J'ai une petite simulation construite avec d3.js dans codepen qui vous montre comment cela fonctionnerait de manière itérative.

Entrez simplement une valeur dans la boîte d'entrée et appuyez sur soumettre et vous pouvez regarder l'algorithme s'exécuter graphiquement.

_Note : Veuillez essayer une plage d'entrées sensées, je n'ai pas exactement construit un système robuste ici._

### Méthode de bisection

D'accord, nous avons compris comment fonctionne la méthode de Newton-Raphson. Abordons ensuite la méthode de bisection.

La méthode de bisection est beaucoup plus facile à comprendre que la méthode de Newton-Raphson. Elle est basée sur une propriété mathématique très simple :

_Si une fonction f(x) est continue sur l'intervalle [a, b] et le signe de f(a) !== f(b), alors il existe une valeur c dans la plage (a, b) où f(c) = 0. En d'autres termes, c est la racine de l'équation._

Si cela n'a pas de sens pour vous, pensez-y purement numériquement et ensuite purement graphiquement.

Disons que vous avez l'intervalle suivant : [-7, 6]. Maintenant, si je vous demande de compter simplement les entiers de -7 à 6, vous compteriez également 0 à un moment donné dans cet intervalle. C'est essentiellement ce que dit la propriété ci-dessus.

Regardons ce que cela signifie graphiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zS0iP-KtUgAuJ0jLroL22A.png)
_Source de l'image : [http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/07/bisection.html](http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/07/bisection.html" rel="noopener" target="_blank" title=")_

La fonction ci-dessus est une ligne continue et elle passe de négative à positive, ce qui implique qu'elle doit croiser 0 à un moment donné. Puisqu'elle doit croiser 0, cela signifie que la racine se trouve dans cet intervalle.

D'accord, cela signifie que l'utilisation de la méthode de bisection est un processus en deux étapes.

1. Trouver l'intervalle dans lequel se trouve la racine, si un tel intervalle existe
2. Trouver la racine réelle dans cet intervalle

Voici le code pour trouver l'intervalle :

Encore une fois, j'utilise mathjs ici, donc vous pouvez consulter la documentation pour cela.

La partie intéressante de cet algorithme se trouve aux lignes 18-26, où je fais une vérification pour voir si l'évaluation de la fonction de l'intervalle de gauche ou de droite a abouti à quelque chose qui est `NaN`. Je vais expliquer pourquoi j'ai inclus ce bloc de code lorsque nous explorerons comment résoudre l'équation (2).

Une fois que nous avons l'intervalle dans lequel se trouve la solution, nous pouvons nous concentrer sur la recherche de la solution elle-même.

Si vous avez déjà essayé d'écrire un algorithme de recherche binaire sur un tableau, l'extrait de code ci-dessus devrait vous sembler très familier. Nous employons plus ou moins la même approche ici. Voici les étapes impliquées.

1. Je commence avec mes intervalles de gauche et de droite et je trouve un point médian
2. Vérifiez si la solution se trouve à gauche du point médian ou à droite du point médian
3. Si elle se trouve à gauche, définissez `right = mid`, sinon définissez `left = mid`

Finalement, le point médian sera la racine elle-même.

Voici une petite simulation qui montre ce qui se passe réellement.

_Note : Je m'excuse pour l'apparence peu esthétique de la simulation, malheureusement le style n'est pas mon fort. Encore une fois, une plage d'entrées sensées, car sinon cela prendra assez longtemps pour que la simulation s'exécute._

Dans le stylo ci-dessus, entrez une valeur, et la simulation essaiera de trouver un intervalle dans lequel une racine potentielle pourrait exister. Une fois qu'elle a trouvé un intervalle, elle commencera à essayer de trouver la racine en utilisant l'algorithme que nous avons discuté immédiatement avant cela.

### **Résolution d'équations complexes**

D'accord, nous avons exploré deux méthodes différentes pour trouver les racines des équations. Maintenant, il est temps d'explorer l'équation plus complexe (2) que nous avions et de voir laquelle de ces méthodes peut résoudre cette équation.

Je vais mettre l'équation ci-dessous pour que ce soit clair

```
f(x, y) = 1550 - (4*x/y * sinh(y/2 * 1500 / (2*x))), eqn(2)
```

```
Résoudre pour f(x, y) = 0, où y = 0.022
```

```
0 = 1550 - (4*x/0.022 * sinh(0.022/2 * 1500 / (2*x)))
```

Tout d'abord, visualisons à quoi ressemble cette équation. Cela nous donnera une bien meilleure intuition de pourquoi quelque chose pourrait mal tourner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*56y9PGq5znTkICE_TfAJOw.png)
_f(x) = 1550 — (4x/0.022 * sinh(0.022/2 * 1500 / (2x)))_

La chose à noter à propos de cette équation est qu'elle tend vers l'infini lorsque x tend vers 0. Cela va poser un problème pour la méthode de Newton-Raphson car la solution de Newton-Raphson tend à suivre le chemin de la tangente, auquel cas elle pourrait rapidement se dissoudre à l'infini comme une solution à moins qu'elle ne parvienne à tomber sur la solution par hasard.

Essayez d'exécuter l'équation ci-dessus avec la méthode de Newton-Raphson et vous verrez ce que je veux dire. Vous obtiendrez probablement un résultat nul.

La méthode de bisection, en revanche, fonctionnera assez bien pour cela. Elle fonctionne bien parce que nous faisons des pas incrémentiels très petits avec une taille de pas que nous contrôlons. Exécutez le codepen ci-dessous et vous devriez voir à quel point la méthode de bisection fonctionne bien pour la plupart des équations.

Le code ci-dessus est presque identique à la version précédente que nous avons configurée pour la méthode de bisection, à quelques différences près. J'ai configuré un codepen séparé pour éviter l'effort de devoir permettre une manière d'entrer des équations, ce qui nécessiterait des vérifications et une gestion des erreurs extensives. De plus, cette équation nécessite des limites spéciales pour définir ses données puisqu'elle tend vers l'infini lorsque x approche 0. Si vous êtes intéressé, vous pouvez voir ce que je veux dire si vous jetez un coup d'œil au code.

Maintenant, dans le code de la méthode de bisection, je vous ai parlé de ce bloc de code ici :

```
if (Number.isNaN(result_left)) {        left -= stepSize        scope_left[variable] = left        result_left = math.eval(eqn, scope_left)    } if (Number.isNaN(result_right)) {        right += stepSize        scope_right[variable] = right        result_right = math.eval(eqn, scope_right)}
```

La raison pour laquelle j'ai cela est de gérer des situations comme celles qui surviennent pour l'équation (2). Parce que l'équation (2) tend vers l'infini lorsque x tend vers 0, il pourrait y avoir une situation où l'évaluation de l'équation retourne soit `NaN` soit `Infinity`. Pour éviter cette situation, je décale simplement l'équation par la taille de pas de manière répétée jusqu'à ce que je puisse revenir au domaine de la fonction qui se trouve dans la plage des nombres réels.

### **Bisection > Newton-Raphson ?**

Cela m'amène à un point important, pourquoi Newton-Raphson a-t-il échoué pour cette équation ? Nous savons que puisque Newton-Raphson suit la tangente de la courbe à différents points, il peut se dissoudre à l'infini si l'équation tend à l'infini à un point particulier. Cela met en évidence l'un des inconvénients de la méthode de Newton-Raphson.

1. La méthode de Newton-Raphson fonctionne bien pour une fonction **continue**. Si la fonction est discontinue comme dans l'équation (2), elle échouera généralement.
2. Newton-Raphson ne peut pas tenir compte de plusieurs maxima et minima dans une fonction.

Prenons l'exemple du graphique suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GmEkZ9CzPRQdwVVLi8lhRw.png)
_Une fonction avec plusieurs maxima et minima. Source : [https://brilliant.org/wiki/newton-raphson-method/](https://brilliant.org/wiki/newton-raphson-method/" rel="noopener" target="_blank" title=")_

Choisissez un point au hasard entre -0,19 et +0,19, et vous devriez voir que vous obtiendrez une pente négative, ce qui signifie que la tangente à la courbe à ce point interceptée l'axe des X à un point plus éloigné de la racine, ce qui va à l'encontre du principe de la méthode de Newton-Raphson. Cela implique que Newton-Raphson échouera généralement pour les équations cubiques et d'ordre supérieur.

La méthode de bisection ne devrait pas avoir le même problème car elle dépend de la recherche d'un intervalle dans lequel la solution doit se trouver, et des courbes comme celle ci-dessus ne seront pas un obstacle à cela tant qu'elle est continue dans ce domaine.

Si vous comparez les deux en termes de notation Big(O), il semble évident que Newton-Raphson s'exécute avec moins d'itérations que la méthode de bisection, simplement parce qu'elle converge beaucoup plus rapidement lorsque vous la visualisez graphiquement. Ironiquement, si vous l'exécutez avec un processus de chronométrage, il s'avère fréquemment que, étant donné le même point de départ, la méthode de bisection s'exécute plus rapidement que la méthode de Newton-Raphson.

Cela est dû au fait que Newton-Raphson implique le calcul d'une dérivée à chaque étape, ce qui s'avère être très coûteux en termes de calcul. Incrémenter et décrémenter un nombre, en revanche, est relativement peu coûteux en termes de calcul.

Si vous souhaitez exécuter le même processus sur votre machine et vérifier les résultats, consultez le dépôt [ici](https://github.com/redixhumayun/root-finding). Vous pouvez cloner ce dépôt, exécuter `npm install` puis `npm run start` sur votre machine, et vous devriez voir les résultats de l'exécution de la méthode de Newton-Raphson et de la méthode de bisection sur une équation identique étant donné la même estimation initiale.

### **Conclusion**

D'accord, nous avons couvert beaucoup de choses ici. Mais honnêtement, ce sujet est si ridiculement vaste que je n'ai à peine effleuré la surface. La convergence des équations est un sujet largement étudié. Considérez l'une des choses les plus basiques que nous n'avons pas couvertes : trouver plusieurs racines.

Vous pouvez bien sûr modifier les algorithmes fournis dans cet article pour atteindre cet objectif.

Prenez l'équation ci-dessous, par exemple. Elle a 3 racines (3 points où elle interceptée l'axe des X, et vous devez trouver toutes ces racines).

![Image](https://cdn-media-1.freecodecamp.org/images/1*QSL-JQG8vggP1OHYw2xMKw.png)
_Les équations cubiques ont plusieurs racines_

Je vais poster toutes mes sources ici, n'hésitez pas à les consulter.

_Note : Si vous avez des questions ou des commentaires sur l'article, n'hésitez pas à me contacter via les commentaires sur cet article ou sur [GitHub](https://github.com/redixhumayun) ou [Twitter](https://twitter.com/zz_humayun)._

1. [https://brilliant.org/wiki/newton-raphson-method/](https://brilliant.org/wiki/newton-raphson-method/)
2. [http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/07/bisection.html](http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/07/bisection.html)
3. [http://www.sosmath.com/calculus/diff/der07/der07.html](http://www.sosmath.com/calculus/diff/der07/der07.html)
4. [https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw)
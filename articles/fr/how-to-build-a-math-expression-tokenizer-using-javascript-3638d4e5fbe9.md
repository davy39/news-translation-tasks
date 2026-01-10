---
title: Comment construire un tokeniseur d'expressions mathématiques en utilisant JavaScript
  (ou tout autre langage)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-12T16:38:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-math-expression-tokenizer-using-javascript-3638d4e5fbe9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cgIB8FPxdoWvQtgm9JazIA.png
tags:
- name: JavaScript
  slug: javascript
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment construire un tokeniseur d'expressions mathématiques en utilisant
  JavaScript (ou tout autre langage)
seo_desc: 'By Shalvah

  Some time ago, I got inspired to build an app for solving specific kinds of math
  problems. I discovered I had to parse the expression into an abstract syntax tree,
  so I decided to build a prototype in Javascript. While working on the parse...'
---

Par Shalvah

Il y a quelque temps, je me suis inspiré pour construire une application pour résoudre des types spécifiques de problèmes mathématiques. J'ai découvert que je devais analyser l'expression en un [arbre de syntaxe abstraite](https://en.wikipedia.org/wiki/Abstract_syntax_tree), alors j'ai décidé de construire un prototype en Javascript. En travaillant sur l'analyseur, j'ai réalisé que le tokeniseur devait être construit en premier. Je vais vous guider à travers comment en faire un vous-même. (Avertissement : c'est plus facile que cela en a l'air au premier abord.)

### Qu'est-ce qu'un Tokeniseur ?

Un [tokeniseur](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization) est un programme qui divise une expression en unités appelées **tokens**. Par exemple, si nous avons une expression comme « Je suis un gros développeur », nous pourrions la tokeniser de différentes manières, telles que :

En utilisant des mots comme tokens,

```
0 => Je1 => suis2 => un3 => gros4 => développeur
```

En utilisant des caractères non blancs comme tokens,

```
0 => J1 => '2 => s3 => u4 => i6 => p17 => e18 => r
```

Nous pourrions également considérer tous les caractères comme des tokens, pour obtenir

```
0 => J1 => '2 => s3 => (espace)4 => u5 => i(espace)6 => g0 => p21 => e22 => r
```

Vous comprenez l'idée, n'est-ce pas ?

Les [tokeniseurs](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization) (également appelés lexers) sont utilisés dans le développement de compilateurs pour les langages de programmation. Ils aident le compilateur à donner un sens structurel à ce que vous essayez de dire. Dans ce cas, cependant, nous en construisons un pour des expressions mathématiques.

### Tokens

Une expression mathématique valide se compose de tokens mathématiquement valides, qui pour les besoins de ce projet pourraient être des **Littéraux**, des **Variables**, des **Opérateurs, Fonctions _ou_ Séparateurs d'arguments de fonction**.  
Quelques notes sur ce qui précède :

* Un Littéral est un nom fantaisiste pour un nombre (dans ce cas). Nous permettrons les nombres sous forme entière ou décimale uniquement.
* Une Variable est celle à laquelle vous êtes habitué en mathématiques : a,b,c,x,y,z. Pour ce projet, toutes les variables sont limitées à des noms d'une seule lettre (donc rien comme _var1_ ou _price_). Cela permet de tokeniser une expression comme _ma_ comme le produit des variables _m_ et _a_, et non comme une seule variable _ma_.
* Les Opérateurs agissent sur les Littéraux et les Variables et les résultats des fonctions. Nous permettrons les opérateurs +, -, *, /, et ^.
* Les Fonctions sont des opérations « plus avancées ». Elles incluent des choses comme sin(), cos(), tan(), min(), max() etc.
* Un Séparateur d'arguments de fonction est simplement un nom fantaisiste pour une virgule, utilisée dans un contexte comme celui-ci : _max(4, 5)_ (le maximum des deux valeurs). Nous l'appelons un Séparateur d'arguments de fonction car il sépare bien les arguments de fonction (pour les fonctions qui prennent deux arguments ou plus, comme _max_ et _min_).

Nous ajouterons également deux tokens qui ne sont généralement pas considérés comme des tokens, mais qui nous aideront à clarifier : **Parenthèse Gauche** et **Parenthèse Droite**. Vous savez ce que sont ces tokens.

### Quelques Considérations

#### Multiplication Implicite

La multiplication implicite signifie simplement permettre à l'utilisateur d'écrire des multiplications « raccourcies », comme _5x_, au lieu de _5*x_. En allant plus loin, cela permet également de le faire avec des fonctions (_5sin(x)_ = _5*sin(x)_).

Encore plus loin, cela permet 5(x) et 5(sin(x)). Nous avons l'option de le permettre ou non. Des compromis ? Ne pas le permettre rendrait en fait la tokenisation plus facile et permettrait des noms de variables à plusieurs lettres (des noms comme `price`). Le permettre rend la plateforme plus intuitive pour l'utilisateur, et bien, fournit un défi supplémentaire à surmonter. J'ai choisi de le permettre.

#### Syntaxe

Bien que nous ne créions pas un langage de programmation, nous devons avoir quelques règles sur ce qui constitue une expression valide, afin que les utilisateurs sachent quoi entrer et que nous sachions quoi prévoir. En termes précis, _les tokens mathématiques doivent être combinés selon ces règles de syntaxe pour que l'expression soit valide._ Voici mes règles :

1. Les tokens peuvent être séparés par 0 ou plusieurs caractères d'espace

```
2+3, 2 +3, 2 + 3, 2 + 3 sont tous OK 5 x - 22, 5x-22, 5x- 22 sont tous OK
```

En d'autres termes, **l'espacement n'a pas d'importance** (sauf dans un token à plusieurs caractères comme le Littéral 22).

2. **Les arguments de fonction doivent être entre parenthèses** (_sin(y)_, _cos(45)_, pas _sin y_, _cos 45_). (Pourquoi ? Nous allons supprimer tous les espaces de la chaîne, donc nous voulons savoir où une fonction commence et se termine sans avoir à faire quelques « gymnastiques ».)

3. La multiplication implicite est autorisée uniquement entre **Littéraux et Variables**, ou **Littéraux et Fonctions**, dans cet ordre (c'est-à-dire que les Littéraux viennent toujours en premier), et peut être avec ou sans parenthèses. Cela signifie :

* _a(4)_ sera traité comme un appel de fonction plutôt que comme _a*4_
* _a4_ n'est pas autorisé
* _4a_ et _4(a)_ sont OK

Maintenant, mettons-nous au travail.

### Modélisation des Données

Il est utile d'avoir une expression d'exemple en tête pour tester cela. Nous commencerons par quelque chose de basique : _2y + 1_

Ce que nous attendons est un tableau qui liste les différents tokens dans l'expression, avec leurs types et leurs valeurs. Donc pour ce cas, nous attendons :

```
0 => Littéral (2)1 => Variable (y)2 => Opérateur (+)3 => Littéral (1)
```

Tout d'abord, nous définirons une classe Token pour faciliter les choses :

```
function Token(type, value) {   this.type = type;   this.value = value}
```

### Algorithme

Ensuite, construisons le squelette de notre fonction de tokenisation.

Notre tokeniseur passera par chaque caractère du tableau `str` et construira des tokens en fonction de la valeur qu'il trouve.

_[Notez que nous supposons que l'utilisateur nous donne une expression valide, donc nous sauterons toute forme de validation tout au long de ce projet.]_

```
function tokenize(str) {  var result=[]; //tableau de tokens    // supprimer les espaces ; souvenez-vous qu'ils n'ont pas d'importance ?  str.replace(/\s+/g, "");
```

```
  // convertir en tableau de caractères  str=str.split("");
```

```
str.forEach(function (char, idx) {    if(isDigit(char)) {      result.push(new Token("Littéral", char));    } else if (isLetter(char)) {      result.push(new Token("Variable", char));    } else if (isOperator(char)) {      result.push(new Token("Opérateur", char));    } else if (isLeftParenthesis(char)) {      result.push(new Token("Parenthèse Gauche", char));    } else if (isRightParenthesis(char)) {      result.push(new Token("Parenthèse Droite", char));    } else if (isComma(char)) {      result.push(new Token("Séparateur d'arguments de fonction", char));    }  });
```

```
  return result;}
```

Le code ci-dessus est assez basique. Pour référence, les helpers `isDigit()`, `isLetter()`, `isOperator()`, `isLeftParenthesis()`, et `isRightParenthesis()` sont définis comme suit (ne soyez pas effrayé par les symboles — c'est ce qu'on appelle [regex](http://www.regular-expressions.info/), et c'est vraiment génial) :

```
function isComma(ch) { return (ch === ",");}
```

```
function isDigit(ch) { return /\d/.test(ch);}
```

```
function isLetter(ch) { return /[a-z]/i.test(ch);}
```

```
function isOperator(ch) { return /\+|-|\*|\/|\^/.test(ch);}
```

```
function isLeftParenthesis(ch) { return (ch === "(");}
```

```
function isRightParenthesis(ch) { return (ch == ")");}
```

_[Notez qu'il n'y a pas de fonctions_ isFunction()_,_ isLiteral() _ou_ isVariable()_, car nous testons les caractères individuellement.]_

Donc maintenant notre analyseur fonctionne réellement. Essayez-le sur ces expressions : 2 + 3, 4a + 1, 5x+ (2y), 11 + sin(20.4).

Tout est bon ?

Pas tout à fait.

Vous observerez que pour la dernière expression, 11 est signalé comme _deux_ tokens Littéraux au lieu d'un. De plus, `sin` est signalé comme _trois_ tokens au lieu d'un. Pourquoi cela ?

Faisons une pause un instant et réfléchissons à cela. Nous avons tokenisé le tableau caractère par caractère, mais en réalité, certains de nos tokens peuvent contenir plusieurs caractères. Par exemple, les Littéraux peuvent être 5, 7.9, .5. Les Fonctions peuvent être sin, cos etc. Les Variables ne sont que des caractères uniques, mais peuvent apparaître ensemble dans une multiplication implicite. Comment résoudre cela ?

#### Buffers

Nous pouvons corriger cela en implémentant un buffer. Deux, en fait. Nous utiliserons un buffer pour contenir les caractères Littéraux (nombres et point décimal), et un pour les lettres (qui couvre à la fois les variables et les fonctions).

Comment fonctionnent les buffers ? Lorsque le tokeniseur rencontre un nombre/point décimal ou une lettre, il le pousse dans le buffer approprié, et continue à le faire jusqu'à ce qu'il entre dans un type d'opérateur différent. Ses actions varieront en fonction de l'opérateur.

Par exemple, dans l'expression _456.7xy + 6sin(7.04x) — min(a, 7)_, cela devrait se dérouler comme suit :

```
lire 4 => numberBuffer lire 5 => numberBuffer lire 6 => numberBuffer lire . => numberBuffer lire 7 => numberBuffer x est une lettre, donc mettre tout le contenu de numberbuffer ensemble comme un Littéral 456.7 => résultat lire x => letterBuffer lire y => letterBuffer + est un Opérateur, donc supprimer tout le contenu de letterbuffer séparément comme Variables x => résultat, y => résultat + => résultat lire 6 => numberBuffer s est une lettre, donc mettre tout le contenu de numberbuffer ensemble comme un Littéral 6 => résultat lire s => letterBuffer lire i => letterBuffer lire n => letterBuffer ( est une Parenthèse Gauche, donc mettre tout le contenu de letterbuffer ensemble comme une fonction sin => résultat lire 7 => numberBuffer lire . => numberBuffer lire 0 => numberBuffer lire 4 => numberBuffer x est une lettre, donc mettre tout le contenu de numberbuffer ensemble comme un Littéral 7.04 => résultat lire x => letterBuffer ) est une Parenthèse Droite, donc supprimer tout le contenu de letterbuffer séparément comme Variables x => résultat - est un Opérateur, mais les deux buffers sont vides, donc il n'y a rien à supprimer lire m => letterBuffer lire i => letterBuffer lire n => letterBuffer ( est une Parenthèse Gauche, donc mettre tout le contenu de letterbuffer ensemble comme une fonction min => résultat lire a=> letterBuffer , est une virgule, donc mettre tout le contenu de letterbuffer ensemble comme une Variable a => résultat, puis pousser , comme un Séparateur d'arguments de fonction => résultat lire 7=> numberBuffer ) est une Parenthèse Droite, donc mettre tout le contenu de numberbuffer ensemble comme un Littéral 7 => résultat
```

Complet. Vous comprenez maintenant, n'est-ce pas ?

Nous y arrivons, il reste juste quelques cas à gérer.

C'est le moment où vous vous asseyez et réfléchissez profondément à votre algorithme et à la modélisation des données. Que se passe-t-il si mon caractère actuel est un opérateur, et que le numberBuffer n'est pas vide ? Les deux buffers peuvent-ils jamais être non vides simultanément ?

En mettant tout cela ensemble, voici ce que nous obtenons (les valeurs à gauche de la flèche décrivent notre type de caractère actuel (ch), NB=numberbuffer, LB=letterbuffer, LP=parenthèse gauche, RP=parenthèse droite

```
boucle à travers le tableau :  quel type est ch ?
```

```
chiffre => pousser ch vers NB  point décimal => pousser ch vers NB  lettre => joindre le contenu de NB comme un Littéral et pousser vers le résultat, puis pousser ch vers LB  opérateur => joindre le contenu de NB comme un Littéral et pousser vers le résultat OU pousser le contenu de LB séparément comme Variables, puis pousser ch vers le résultat  LP => joindre le contenu de LB comme une Fonction et pousser vers le résultat OU (joindre le contenu de NB comme un Littéral et pousser vers le résultat, pousser l'Opérateur * vers le résultat), puis pousser ch vers le résultat  RP => joindre le contenu de NB comme un Littéral et pousser vers le résultat, pousser le contenu de LB séparément comme Variables, puis pousser ch vers le résultat  virgule => joindre le contenu de NB comme un Littéral et pousser vers le résultat, pousser le contenu de LB séparément comme Variables, puis pousser ch vers le résultat
```

```
fin de boucle
```

```
joindre le contenu de NB comme un Littéral et pousser vers le résultat, pousser le contenu de LB séparément comme Variables,
```

Deux choses à noter.

1. Remarquez où j'ai ajouté « pousser l'Opérateur * vers le résultat » ? C'est nous qui convertissons la multiplication implicite en explicite. De plus, lorsque nous vidons le contenu de LB séparément comme Variables, nous devons nous souvenir d'insérer l'Opérateur de multiplication entre elles.
2. À la fin de la boucle de la fonction, nous devons nous souvenir de vider ce qu'il reste dans les buffers.

### Traduction en Code

En mettant tout cela ensemble, votre fonction de tokenisation devrait maintenant ressembler à ceci :

Nous pouvons exécuter une petite démonstration :

```
var tokens = tokenize("89sin(45) + 2.2x/7");tokens.forEach(function(token, index) {  console.log(index + "=> " + token.type + "(" + token.value + ")");});
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*dRLwtjvcAXiO8OekLuxpgg.png)
_Oui ! Notez les * ajoutés pour les multiplications implicites_

### Conclusion

C'est le moment où vous analysez votre fonction et mesurez ce qu'elle fait par rapport à ce que vous voulez qu'elle fasse. Posez-vous des questions comme, « La fonction fonctionne-t-elle comme prévu ? » et « Ai-je couvert tous les cas limites ? »

Les cas limites pour cela pourraient inclure les nombres négatifs et similaires. Vous exécutez également des tests sur la fonction. Si à la fin vous êtes satisfait, vous pouvez alors commencer à chercher comment vous pouvez l'améliorer.

Merci d'avoir lu. Veuillez cliquer sur le petit cœur pour recommander cet article, et partager si vous l'avez apprécié ! Et si vous avez essayé une autre approche pour construire un tokeniseur mathématique, faites-le moi savoir dans les commentaires.
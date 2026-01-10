---
title: Analyse des expressions mathématiques avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-22T19:30:07.000Z'
originalURL: https://freecodecamp.org/news/parsing-math-expressions-with-javascript-7e8f5572276e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zs_bmXKVXHJQuz0pnsDdqQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Analyse des expressions mathématiques avec JavaScript
seo_desc: 'By Shalvah

  A while ago, I wrote about tokenizing a math expression, with Javascript as the
  language of choice. The tokenizer I built in that article was the first component
  of my quest to render and solve math expressions using Javascript, or any oth...'
---

Par Shalvah

Il y a quelque temps, j'ai écrit sur [la tokenization d'une expression mathématique](https://medium.freecodecamp.com/how-to-build-a-math-expression-tokenizer-using-javascript-3638d4e5fbe9), avec JavaScript comme langage de choix. Le tokeniseur que j'ai construit dans cet article était le premier composant de ma quête pour rendre et résoudre des expressions mathématiques en utilisant JavaScript, ou tout autre langage. Dans cet article, je vais expliquer comment construire le composant suivant : le parseur.

Quel est le travail du parseur ? Assez simple. Il analyse l'expression. (Évidemment.) En fait, [Wikipedia](https://en.wikipedia.org/wiki/Parsing#Parser) a une bonne réponse :

> Un parseur est un composant logiciel qui prend des données d'entrée (souvent du texte) et construit une structure de données — souvent une sorte d'arbre d'analyse, d'arbre de syntaxe abstraite ou une autre structure hiérarchique — donnant une représentation structurelle de l'entrée, vérifiant la syntaxe correcte dans le processus. L'analyse peut être précédée ou suivie par d'autres étapes, ou celles-ci peuvent être combinées en une seule étape. Le parseur est souvent précédé par un analyseur lexical séparé, qui crée des tokens à partir de la séquence de caractères d'entrée.

Donc, en essence, voici ce que nous essayons d'atteindre :

```
expression mathématique => [parseur] => une structure de données (nous y viendrons dans un instant)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*jFWR28LjzW4rec1egUDwWg.gif)
_Quelque chose comme ceci (source : [codeproject.com)](https://www.codeproject.com/Articles/50377/Create-Your-Own-Programming-Language" rel="noopener" target="_blank" title=")_

Passons un peu en avant : « ... Le parseur est souvent précédé par un analyseur lexical séparé, qui crée des tokens à partir de la séquence de caractères d'entrée ». Cela parle du tokeniseur que nous avons construit plus tôt. Donc, notre parseur ne recevra pas l'expression mathématique brute, mais plutôt un tableau de tokens. Maintenant, nous avons :

```
expression mathématique => [tokeniseur] => liste de tokens => [parseur] => une structure de données
```

Pour le tokeniseur, nous avons dû inventer l'algorithme manuellement. Pour le parseur, nous allons implémenter un algorithme déjà existant, [l'algorithme Shunting-yard](https://en.wikipedia.org/wiki/Shunting-yard_algorithm). Vous vous souvenez de la « structure de données » mentionnée plus haut ? Avec cet algorithme, notre parseur peut nous donner une structure de données appelée un arbre de syntaxe abstraite (AST) ou une représentation alternative de l'expression, connue sous le nom de notation polonaise inverse (RPN).

### Notation Polonaise Inverse

Je vais commencer par la RPN. Encore une fois, selon [Wikipedia](https://en.wikipedia.org/wiki/Reverse_Polish_notation), la RPN est « une notation mathématique dans laquelle **chaque opérateur suit tous ses opérandes** ». Au lieu d'avoir, par exemple, 3+4, la RPN serait 3 4 +. Bizarre, je sais. Mais la règle est que l'opérateur doit venir **après** tous ses opérandes.

Gardez cette règle à l'esprit alors que nous examinons quelques exemples plus complexes. N'oubliez pas qu'un opérande pour une opération peut être le résultat d'une opération précédente.

```
Algébrique : 3 - 4                        RPN : 3 4 -

Algébrique : 3 - 4 + 5                    RPN : 3 4 - 5 +

Algébrique : 2^3                          RPN : 2 3 ^

Algébrique : 5 + ((1 + 2) × 4) − 3        RPN : 5 1 2 + 4 * + 3 -

Algébrique : sin(45)                      RPN : 45 sin

Algébrique : tan(x^2 + 2*x + 6)           RPN : x 2 ^ 2 x * + 6 + tan
```

Parce que l'opérateur doit venir après ses opérandes, la RPN est également connue sous le nom de _notation postfixée_, et notre notation algébrique « régulière » est appelée _infixée_.

Comment évaluez-vous une expression en RPN ? Il y a un algorithme simple que j'utilise :

> _Lisez tous les tokens de gauche à droite jusqu'à ce que vous obteniez un opérateur ou une fonction. Sachant que l'opérateur/fonction prend n arguments (par exemple, pour +, n = 2 ; pour cos(), n = 1), évaluez les n arguments précédents avec l'opérateur/fonction, et remplacez tous (opérateur/fonction + opérandes) par le résultat. Continuez comme avant, jusqu'à ce qu'il n'y ait plus d'opérateurs/fonctions à lire. Le seul token (littéral ou variable) restant est votre réponse._

(Ceci est un algorithme simplifié, qui suppose que l'expression est valide. Quelques indicateurs que l'expression n'est pas valide sont si vous avez plus d'un token restant à la fin, ou si le dernier token restant est un opérateur/fonction.)

Donc, pour quelque chose comme 5 1 2 + 4 * + 3 −:

```
lire 5
lire 1
lire 2
lire +. + est un opérateur qui prend 2 arguments, donc calculez 1+2 et remplacez par le résultat (3). L'expression est maintenant 5 3 4 * + 3 -
lire 4
lire *. * est un opérateur qui prend deux arguments, donc calculez 3*4 et remplacez par le résultat, 12. L'expression est réduite à 5 12 + 3 -
lire +. + est un opérateur qui prend deux arguments, donc calculez 5+12, remplacez par le résultat, 17. Maintenant, nous avons 17 3 -
lire 3
lire -. - est un opérateur qui prend deux arguments, donc calculez 17-3. Le résultat est 14.
```

J'espère que vous avez eu un A dans mon petit cours accéléré sur la RPN. Vous l'avez eu ? OK, passons à la suite.

### Arbres de Syntaxe Abstraite

La définition de Wikipedia ici pourrait ne pas être très utile pour beaucoup d'entre nous : « une représentation arborescente de la structure syntaxique abstraite du code source écrit dans un langage de programmation. » Pour ce cas d'utilisation, nous pouvons penser à un AST comme une structure de données qui représente la structure mathématique de l'expression. Cela se voit mieux que cela ne se dit, alors dessinons un diagramme approximatif. Je vais commencer par un AST pour l'expression simple 3+4 :

```
  [+]
 /   \
[3] [4]
```

Chaque `[]` représente un nœud dans l'arbre. Donc vous pouvez voir d'un coup d'œil, que les deux tokens sont réunis par l'opérateur +.

Une expression plus complexe, 5 + ((1 + 2) × 4) − 3 :

```
           [-]
          /   \
        [+]    \___[3]   
       /  \
 [5]__/   [*]
         /   \
        [+]  [4]
       /   \  
     [1]  [2]
```

Ah, un bel arbre de syntaxe. Il relie tous les tokens et opérateurs parfaitement. Vous pouvez voir que l'évaluation de cette expression est beaucoup plus facile — il suffit de suivre l'arbre.

Alors, pourquoi un AST est-il utile ? Il vous aide à représenter la logique et la structure de l'expression correctement, ce qui facilite l'évaluation de l'expression. Par exemple, pour évaluer l'expression ci-dessus, sur notre backend, nous pourrions faire quelque chose comme ceci :

```
result = binaryoperation(+, 1, 2)
result = binaryoperation(*, result, 4)
result = binaryoperation(+, 5, result)
result = binaryoperation(-, result, 3)
return result
```

En d'autres termes, pour chaque nœud d'opérateur (ou fonction) que l'évaluateur/compilateur/interprète rencontre, il vérifie combien de branches il y a, puis évalue les résultats de toutes ces branches avec l'opérateur.

D'accord, le cours accéléré est terminé, revenons à notre parseur. Notre parseur convertira l'expression (tokenisée) en RPN, puis en AST. Alors commençons à l'implémenter.

### L'algorithme Shunting-yard

Voici la version RPN de l'algorithme complet ([de notre ami Wikipedia](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)), et modifié pour s'adapter à notre tokeniseur :

> _Tant qu'il y a des tokens à lire :_  
>   
> _1. Lire un token. Appelons-le `t`_  
>   
> _2. Si `t` est un Littéral ou une Variable, poussez-le dans la file de sortie._  
>   
> _3. Si `t` est une Fonction, poussez-le sur la pile._  
>   
> _4. Si `t` est un Séparateur d'Argument de Fonction (une virgule), retirez les opérateurs de la pile vers la file de sortie jusqu'à ce que le token au sommet de la pile soit une Parenthèse Gauche._  
>   
> _5. Si `t` est un Opérateur :_  
>   
> _a. tant qu'il y a un token Opérateur `o` au sommet de la pile d'opérateurs et soit `t` est associatif à gauche et a une precedence inférieure ou égale à celle de `o`, ou `t` est associatif à droite, et a une precedence inférieure à celle de `o`, retirez `o` de la pile d'opérateurs, vers la file de sortie ;_  
>   
> _b. à la fin de l'itération, poussez `t` sur la pile d'opérateurs._  
>   
> _6. Si le token est une Parenthèse Gauche, poussez-le sur la pile._  
>   
> _7. Si le token est une Parenthèse Droite, retirez les opérateurs de la pile vers la file de sortie jusqu'à ce que le token au sommet de la pile soit une parenthèse gauche. Ensuite, retirez la parenthèse gauche de la pile, mais pas vers la file de sortie._  
>   
> _8. Si le token au sommet de la pile est une Fonction, retirez-le vers la file de sortie._  
>   
> _Quand il n'y a plus de tokens à lire, retirez tous les tokens Opérateur de la pile vers la file de sortie._  
>   
> _Quittez._

(Note de côté : au cas où vous auriez lu l'article précédent, j'ai mis à jour la liste des tokens reconnus pour inclure le Séparateur d'Argument de Fonction, alias virgule).

L'algorithme ci-dessus suppose que l'expression est valide. Je l'ai fait ainsi pour qu'il soit facilement compréhensible dans le contexte d'un article. Vous pouvez consulter l'algorithme complet [sur Wikipedia](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).

Vous observerez quelques choses :

* Nous avons besoin de deux structures de données : une **pile** pour contenir les fonctions et les opérateurs, et une **file** pour la sortie. Si vous n'êtes pas familier avec ces deux structures de données, voici un rappel pour vous : si vous voulez récupérer une valeur d'une pile, vous commencez par la dernière que vous avez mise, alors que pour une file, vous commencez par la première que vous avez mise.

```js
// nous utiliserons des tableaux pour représenter les deux
var outQueue=[];
var opStack=[];
```

* Nous devons connaître l'**associativité** des opérateurs. L'[associativité](https://en.wikipedia.org/wiki/Operator_associativity) signifie simplement dans quel ordre une expression contenant plusieurs opérations du même type sont regroupées en l'absence de parenthèses. Par exemple, 2 + 3 + 4 est canoniquement évalué de gauche à droite (2+ 3 =5, puis 5 + 4 =9), donc + a une associativité à gauche. Comparez cela à 2 ^ 3 ^ 4, qui est évalué comme 2 ^81, et non 8 ^4. Ainsi ^ a une associativité à droite. Nous allons regrouper les associativités des opérateurs que nous rencontrerons dans un objet JavaScript :

```js
var assoc = {
  "^" : "right",
  "*" : "left",
  "/" : "left",
  "+" : "left",
  "-" : "left"
 };
```

* Nous devons également connaître la **précédence** des opérateurs. La [précédence](https://en.wikipedia.org/wiki/Order_of_operations) est une sorte de classement attribué aux opérateurs, afin que nous sachions dans quel ordre ils doivent être évalués s'ils apparaissent dans la même expression. Les opérateurs avec une précédence plus élevée sont évalués en premier. Par exemple, * a une précédence plus élevée que +, donc 2 + 3 * 4 est évalué comme 2 + 12, et non 5 * 4, sauf si des parenthèses sont utilisées. + et – ont la même précédence, donc 3 + 5 – 2 peut être évalué comme 8–2 ou 3+3. Encore une fois, nous allons regrouper les précédences des opérateurs dans un objet :

```js
var prec = {
  "^" : 4,
  "*" : 3,
  "/" : 3,
  "+" : 2,
  "-" : 2
 };
```

Maintenant, mettons à jour notre classe `Token` afin que nous puissions facilement accéder à la précédence et à l'associativité via des méthodes :

```
Token.prototype.precedence = function() {
  return prec[this.value];
 };
 
 Token.prototype.associativity = function() {
  return assoc[this.value];
 };
```

* Nous avons besoin d'une méthode qui nous permet de **jeter un coup d'œil** à la pile (pour vérifier l'élément au sommet sans le retirer), et une autre qui nous permet de **retirer** de la pile (récupérer et retirer l'élément au sommet). Heureusement, les tableaux JavaScript ont déjà une méthode `pop()`, donc tout ce que nous avons à faire est d'implémenter une méthode `peek()`. (Rappelez-vous, pour les piles, l'élément au sommet est celui que nous avons ajouté en dernier.)

```js
Array.prototype.peek = function() {
  return this.slice(-1)[0]; //récupérer le dernier élément du tableau
};
```

Donc voici ce que nous avons :

```js
function tokenize(expr) {
  ...   // il suffit de coller le code du tokeniseur ici
}
  
function parse(inp){
 var outQueue=[];
 var opStack=[];
Array.prototype.peek = function() {
  return this.slice(-1)[0];
 };
    
var assoc = {
  "^" : "right",
  "*" : "left",
  "/" : "left",
  "+" : "left",
  "-" : "left"
 };
    
var prec = {
  "^" : 4,
  "*" : 3,
  "/" : 3,
  "+" : 2,
  "-" : 2
 };
    
Token.prototype.precedence = function() {
  return prec[this.value];
 };
 
 Token.prototype.associativity = function() {
  return assoc[this.value];
 };
    
 //tokenize
 var tokens=tokenize(inp);
 tokens.forEach(function(v) {
   ...   //appliquer l'algorithme ici
 });
     
 return outQueue.concat(opStack.reverse());  // liste de tokens en RPN
}
```

Je ne vais pas m'attarder sur l'implémentation de l'algorithme pour ne pas vous ennuyer. C'est une tâche assez simple, pratiquement une traduction mot à mot de l'algorithme en code, donc à la fin de la journée, voici ce que nous avons :

```js
function parse(inp){
	var outQueue=[];
	var opStack=[];

	Array.prototype.peek = function() {
		return this.slice(-1)[0];
	};

	var assoc = {
		"^" : "right",
		"*" : "left",
		"/" : "left",
		"+" : "left",
		"-" : "left"
	};

	var prec = {
		"^" : 4,
		"*" : 3,
		"/" : 3,
		"+" : 2,
		"-" : 2
	};

	Token.prototype.precedence = function() {
		return prec[this.value];
	};
	
	Token.prototype.associativity = function() {
		return assoc[this.value];
	};

	//tokenize
	var tokens=tokenize(inp);

	tokens.forEach(function(v) {
		//Si le token est un nombre, alors poussez-le dans la file de sortie
		if(v.type === "Literal" || v.type === "Variable" ) {
			outQueue.push(v);
		} 
		//Si le token est un token de fonction, alors poussez-le sur la pile.
		else if(v.type === "Function") {
			opStack.push(v);
		} //Si le token est un séparateur d'argument de fonction 
		else if(v.type === "Function Argument Separator") {
			//Jusqu'à ce que le token au sommet de la pile soit une parenthèse gauche
			//retirez les opérateurs de la pile vers la file de sortie.
			while(opStack.peek()
				&& opStack.peek().type !== "Left Parenthesis") {
				outQueue.push(opStack.pop());
		}
			/*if(opStack.length == 0){
				console.log("Mismatched parentheses");
				return;
			}*/
		} 
		//Si le token est un opérateur, o1, alors :
		else if(v.type == "Operator") {
			  //tant qu'il y a un token opérateur o2, au sommet de la pile d'opérateurs et soit
			  while (opStack.peek() && (opStack.peek().type === "Operator") 
				//o1 est associatif à gauche et sa précédence est inférieure ou égale à celle de o2, ou
				&& ((v.associativity() === "left" && v.precedence() <= opStack.peek().precedence())
					//o1 est associatif à droite, et a une précédence inférieure à celle de o2,
					|| (v.associativity() === "right" && v.precedence() < opStack.peek().precedence()))) {
			  	outQueue.push(opStack.pop());
			}
			//à la fin de l'itération, poussez o1 sur la pile d'opérateurs
			opStack.push(v);
		} 
		
		//Si le token est une parenthèse gauche (c'est-à-dire "("), alors poussez-le sur la pile.
		else if(v.type === "Left Parenthesis") {
			opStack.push(v);
		}
		//Si le token est une parenthèse droite (c'est-à-dire ")") :
		else if(v.type === "Right Parenthesis") {
			//Jusqu'à ce que le token au sommet de la pile soit une parenthèse gauche, retirez les opérateurs de la pile vers la file de sortie.
			while(opStack.peek() 
				&& opStack.peek().type !== "Left Parenthesis") {
				outQueue.push(opStack.pop());
		}
			/*if(opStack.length == 0){
				console.log("Unmatched parentheses");
				return;
			}*/
			//Retirez la parenthèse gauche de la pile, mais pas vers la file de sortie.
			opStack.pop();

			//Si le token au sommet de la pile est un token de fonction, retirez-le vers la file de sortie.
			if(opStack.peek() && opStack.peek().type === "Function") {
				outQueue.push(opStack.pop());
			}
		}
	});

	return outQueue.concat(opStack.reverse());
}

function toString(rpn) {
	return rpn.map(token => token.value).join(" ");
}
```

La fonction `toString` formate simplement notre liste de tokens RPN dans un format lisible.

Et nous pouvons tester notre parseur infixe vers postfixe :

```js
var rpn = parse("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3");
console.log(toString(rpn));
```

Sortie :

```
3 4 2 * 1 5 - 2 3 ^ ^ / +
```

RPN!!

### Il est temps de planter un arbre

Maintenant, modifions notre parseur pour qu'il retourne un AST.

Pour générer un AST au lieu de RPN, nous devons apporter quelques modifications :

* Nous allons créer un objet pour représenter un nœud dans notre AST. Chaque nœud a une valeur et deux branches (qui peuvent être `null`) :

```js
function ASTNode(token, leftChildNode, rightChildNode) {
   this.token = token.value;
   this.leftChildNode = leftChildNode;
   this.rightChildNode = rightChildNode;
}
```

* La deuxième chose que nous allons faire est de changer notre structure de données de sortie en une pile. Bien que le code réel pour cela soit simplement de changer la ligne `var outQueue = []` en `var outStack = []` (parce qu'il reste un tableau), le changement clé est dans notre compréhension et notre traitement de ce tableau.

Maintenant, comment notre algorithme infixe vers AST va-t-il fonctionner ? Basiquement, le même algorithme, avec quelques modifications :

1. Au lieu de pousser un token Littéral ou Variable sur notre `outQueue`, nous poussons un nouveau nœud dont la valeur est le token, et dont les branches sont `null` sur notre `outStack`
2. Au lieu de retirer un token Opérateur/Fonction de la `opStack`, nous remplaçons les deux nœuds supérieurs sur la `outStack` par un seul nœud dont la valeur est le token, et qui a ces deux nœuds comme branches. Créons une fonction qui fait cela :

```js
Array.prototype.addNode = function (operatorToken) {
  rightChildNode = this.pop();
  leftChildNode = this.pop();
  this.push(new ASTNode(operatorToken, leftChildNode, rightChildNode));
}
```

3. Notre parseur doit maintenant retourner un seul nœud, le nœud au sommet de notre AST. Ses deux branches contiendront les deux nœuds enfants, dont les branches contiendront leurs enfants, et ainsi de suite, de manière récursive. Par exemple, pour une expression comme 3 + 4 * 2 / ( 1–5 ) ^ 2 ^ 3, nous nous attendons à ce que la structure de notre nœud de sortie soit comme ceci (dans une forme horizontale) :

```
+ => 3 => null
       => null
  => / => * => 4 => null
                 => null
            => 2 => null
                 => null
       => ^ => - => 1 => null
                      => null
                 => 5 => null
                      => null
            => ^ => 2 => null
                      => null
                 => 3 => null
                      => null
```

Dans le diagramme ci-dessus, les => représentent les branches du nœud (le nœud supérieur est la branche gauche, celui du bas est la branche droite). Chaque nœud a deux branches, et les nœuds à la fin de l'arbre ont les leurs pointant vers `null`.

Donc, si nous mettons tout cela ensemble, voici le code que nous obtenons :

```js
function ASTNode(token, leftChildNode, rightChildNode) {
	this.token = token.value;
	this.leftChildNode = leftChildNode;
	this.rightChildNode = rightChildNode;
}


function parse(inp){
	var outStack=[];
	var opStack=[];

	Array.prototype.addNode = function (operatorToken) {
		rightChildNode = this.pop();
		leftChildNode = this.pop();
		this.push(new ASTNode(operatorToken, leftChildNode, rightChildNode));
	}

	Array.prototype.peek = function() {
		return this.slice(-1)[0];
	};

	var assoc = {
		"^" : "right",
		"*" : "left",
		"/" : "left",
		"+" : "left",
		"-" : "left"
	};

	var prec = {
		"^" : 4,
		"*" : 3,
		"/" : 3,
		"+" : 2,
		"-" : 2
	};

	Token.prototype.precedence = function() {
		return prec[this.value];
	};
	
	Token.prototype.associativity = function() {
		return assoc[this.value];
	};

	//tokenize
	var tokens=tokenize(inp);

	tokens.forEach(function(v) {
		//Si le token est un nombre, alors poussez-le sur la pile de sortie
		if(v.type === "Literal" || v.type === "Variable" ) {
			outStack.push(new ASTNode(v, null, null));
		} 
		//Si le token est un token de fonction, alors poussez-le sur la pile.
		else if(v.type === "Function") {
			opStack.push(v);
		} //Si le token est un séparateur d'argument de fonction 
		else if(v.type === "Function Argument Separator") {
			//Jusqu'à ce que le token au sommet de la pile soit une parenthèse gauche
			//retirez les opérateurs de la pile vers la file de sortie.
			while(opStack.peek()
				&& opStack.peek().type !== "Left Parenthesis") {
				outStack.addNode(opStack.pop());
		}
			/*if(opStack.length == 0){
				console.log("Mismatched parentheses");
				return;
			}*/
		} 
		//Si le token est un opérateur, o1, alors :
		else if(v.type == "Operator") {
			  //tant qu'il y a un token opérateur o2, au sommet de la pile d'opérateurs et soit
			  while (opStack.peek() && (opStack.peek().type === "Operator") 
				//o1 est associatif à gauche et sa précédence est inférieure ou égale à celle de o2, ou
				&& ((v.associativity() === "left" && v.precedence() <= opStack.peek().precedence())
					//o1 est associatif à droite, et a une précédence inférieure à celle de o2,
					|| (v.associativity() === "right" && v.precedence() < opStack.peek().precedence()))) {
			  	outStack.addNode(opStack.pop());
			}
			//à la fin de l'itération, poussez o1 sur la pile d'opérateurs
			opStack.push(v);
		} 
		
		//Si le token est une parenthèse gauche (c'est-à-dire "("), alors poussez-le sur la pile.
		else if(v.type === "Left Parenthesis") {
			opStack.push(v);
		}
		//Si le token est une parenthèse droite (c'est-à-dire ")") :
		else if(v.type === "Right Parenthesis") {
			//Jusqu'à ce que le token au sommet de la pile soit une parenthèse gauche, retirez les opérateurs de la pile vers la file de sortie.
			while(opStack.peek() 
				&& opStack.peek().type !== "Left Parenthesis") {
				outStack.addNode(opStack.pop());
		}
			/*if(opStack.length == 0){
				console.log("Unmatched parentheses");
				return;
			}*/
			//Retirez la parenthèse gauche de la pile, mais pas vers la file de sortie.
			opStack.pop();

			//Si le token au sommet de la pile est un token de fonction, retirez-le vers la file de sortie.
			if(opStack.peek() && opStack.peek().type === "Function") {
				outStack.addNode(opStack.pop());
			}
		}
	});

	while(opStack.peek()) {
		outStack.addNode(opStack.pop());
	}

	return outStack.pop();
}
```

Et si nous le démontrons :

```js
//un petit hack que j'ai assemblé pour qu'il s'imprime dans un format lisible
ASTNode.prototype.toString = function(count) {
   if (!this.leftChildNode && !this.rightChildNode)
     return this.token + "\t=>null\n" + Array(count+1).join("\t") + "=>null";
   var count = count || 1;
   count++;
   return this.token + "\t=>" + this.leftChildNode.toString(count) + "\n" + Array(count).join("\t") + "=>" + this.rightChildNode.toString(count);
};

var ast = parse("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3");
console.log("" + ast);
```

Et le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3vdqt8rw-Lbkil3CrIBDNA.png)
_Oh, bel arbre !_

Lentement, mais sûrement, nous nous rapprochons de la compréhension de ce qui fait fonctionner les compilateurs et les interpréteurs ! Admettons-le, le fonctionnement des langages de programmation modernes et de leurs outils est beaucoup plus complexe que ce que nous avons examiné jusqu'à présent, mais j'espère que cela s'avère être une introduction facile à comprendre pour eux. Comme un certain nombre de personnes l'ont souligné, des outils existent pour générer automatiquement des tokeniseurs et des parseurs, mais il est souvent agréable de savoir comment quelque chose fonctionne réellement.

Les concepts que nous avons couverts dans cet article et le précédent sont des sujets très intéressants dans le domaine de l'informatique et de la théorie des langages. J'ai encore beaucoup à apprendre à leur sujet, et je vous encourage à aller de l'avant et à les rechercher si ils vous intéressent. Et [envoyez-moi un message](http://m.me/shalvah.adebayo) pour me faire savoir de vos progrès. Paix !
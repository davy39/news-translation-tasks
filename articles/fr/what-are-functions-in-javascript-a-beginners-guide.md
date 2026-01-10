---
title: Qu'est-ce que les fonctions en JavaScript ? Un guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-30T20:32:18.000Z'
originalURL: https://freecodecamp.org/news/what-are-functions-in-javascript-a-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/banner-image-for-functions-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que les fonctions en JavaScript ? Un guide pour débutants
seo_desc: 'By Chinwendu Enyinna

  Functions are one of the fundamental concepts in programming. They let us write
  concise, modular, reusable, and maintainable code. They also help us obey the DRY
  principle when writing code.

  In this article, you will learn what f...'
---

Par Chinwendu Enyinna

Les fonctions sont l'un des concepts fondamentaux en programmation. Elles nous permettent d'écrire du code concis, modulaire, réutilisable et maintenable. Elles nous aident également à respecter le principe DRY lors de l'écriture de code.

Dans cet article, vous apprendrez ce que sont les fonctions en JavaScript, comment écrire vos propres fonctions personnalisées et comment les implémenter.

En tant que prérequis, vous devriez être familier avec certains concepts fondamentaux de JavaScript tels que les variables, les expressions et les instructions conditionnelles pour suivre cet article.

## Qu'est-ce qu'une fonction en JavaScript ?

Une fonction est un bloc de code réutilisable écrit pour effectuer une tâche spécifique.

Vous pouvez penser à une fonction comme un sous-programme au sein du programme principal. Une fonction se compose d'un ensemble d'instructions mais s'exécute comme une seule unité.

En JavaScript, nous avons certaines fonctions intégrées au navigateur comme alert(), prompt() et confirm(). Vous les avez probablement utilisées dans votre projet auparavant, n'est-ce pas ? Mais vous pouvez toujours créer vos propres fonctions personnalisées.

Il existe plusieurs façons de définir une fonction. Le plus couramment, nous avons la déclaration de fonction et l'expression de fonction.

## Comment définir une fonction en utilisant la déclaration de fonction

Vous écrivez une déclaration de fonction comme ceci :

```javascript
function nomDeLaFonction() {
	//du code ici....
}
```

En gros, elle se compose des éléments suivants : 

* Mot-clé Function
* Le nom de la fonction
* Parentheses (qui peuvent prendre des paramètres, ou être vides)
* Le corps de la fonction (entouré d'accolades).

Voici un exemple :

```javascript
function direBonjour() {
	console.log("Bonjour le monde"); 
}
```

Cette fonction ne fera rien – dans ce cas, afficher _Bonjour le monde_ – à moins que vous ne l'appeliez. Le terme pour cela est _invoquer la fonction_.

Voici comment appeler la fonction :

```javascript
direBonjour();

//sortie : Bonjour le monde
```

Voici un autre exemple :

```javascript
function somme(num1, num2){
	return num1 + num2;
}

```

Pour invoquer cette fonction, nous l'appelons comme ceci :

```javascript
somme(1, 2);

//sortie : 3
```

Vous pouvez voir une légère différence entre notre premier exemple de fonction et le second.

Si vous avez deviné que c'est le contenu à l'intérieur des parenthèses de la deuxième fonction, alors vous avez raison !

La fonction `somme()` a pris deux paramètres lorsque nous l'avons définie – `num1`, et `num2`. Et lorsque nous l'appelons, nous avons passé deux valeurs – les arguments, `1` et `2`. Laissez-moi expliquer ce que signifient ces deux termes (paramètres et arguments).

Un **paramètre** est une variable que vous passez à une fonction lorsque vous la déclarez. 

Supposons que vous voulez que votre fonction soit dynamique, afin qu'elle applique la logique de la fonction à différents ensembles de données à différents moments. C'est là que les paramètres sont utiles. Ainsi, votre fonction ne produit pas simplement le même résultat de manière répétée. Au lieu de cela, son résultat dépend des données que vous passez.

Un **argument**, en revanche, est la valeur équivalente au paramètre que vous passez à la fonction lorsque vous l'appelez.

Donc, la syntaxe pour déclarer une fonction avec des paramètres ressemblera à ceci :

```javascipt
function nomDeLaFonction(paramètres){
	//corps de la fonction.....
}
```

Et pour l'invoquer :

```javascript
nomDeLaFonction(arguments)
```

## Comment définir une fonction en utilisant une expression de fonction

Une expression de fonction est une autre notation pour définir une fonction. En termes de syntaxe, elle est similaire à la déclaration de fonction. Mais les expressions de fonction vous permettent de définir une fonction nommée ou d'omettre le nom de la fonction pour créer une fonction anonyme. 

Voyons à quoi ressemble une expression de fonction :

```javascript
let fonctionNommee = function maFonction(){
	//du code ici...
}
```

Remarquez que dans cet exemple, la fonction a un nom, `maFonction`. Ce n'est pas le cas avec la fonction anonyme. Lorsque vous définissez une fonction anonyme, vous omettez le nom de la fonction comme dans cet exemple ci-dessous :

```javascript
let fonctionAnonyme = function(){
	//du code ici...
}
```

Vous pouvez voir que les deux exemples de fonctions sont assignés à une variable, n'est-ce pas ? 

**Un mot-clé de fonction crée une valeur de fonction qui peut être assignée à une variable lorsqu'il est utilisé comme une expression**.

Donc, pour invoquer cette fonction, nous l'appelons en utilisant le nom de la variable qui sert de nouveau nom de fonction.

Une différence majeure entre la déclaration de fonction et l'expression de fonction est que, avec la déclaration de fonction, vous pouvez invoquer la fonction même avant de la définir. Cela n'est pas possible avec les expressions de fonction.  

Par exemple :

```javascript
console.log(salutation());

function salutation(){
  console.log("J'espère que vous allez bien ?");

}
//sortie : J'espère que vous allez bien ?
```

Cela ne fonctionnera pas si la fonction est définie comme une expression de fonction car l'expression de fonction suit une séquence de flux de contrôle de haut en bas.

## Comment utiliser les fonctions fléchées en JavaScript

Les fonctions fléchées sont une autre notation d'une expression de fonction mais elles ont une syntaxe plus courte. Elles ont été introduites dans ES6 et nous aident à écrire du code plus propre. 

Ici, le mot-clé de fonction est exclu et nous utilisons un symbole de flèche (=>) à la place. La syntaxe ressemble à ceci :

```javascript
let nomDeLaFonction = (paramètres) => {
	//corps de la fonction
}

```

Si le corps de la fonction à l'intérieur des accolades contient seulement une seule instruction, alors les accolades peuvent être omises. Une fonction fléchée avec des accolades doit inclure le mot-clé return.

## **Qu'est-ce que les expressions de fonction immédiatement invoquées (IIFE) ?**

IIFE est une autre notation d'expression de fonction (explicitement une fonction anonyme) qui fonctionne de manière isolée et est indépendante de tout autre code. Elle est invoquée immédiatement là où elle est définie. 

La syntaxe est la suivante :

```javascript
(function (){
	//corps de la fonction
})();
```

Un cas d'utilisation de IIFE serait d'enfermer une variable que vous n'utiliserez probablement plus dans votre code. Ainsi, dès que la fonction est exécutée, la variable cesse d'exister.

## **Comment utiliser le mot-clé return dans une fonction**

Pour créer une fonction qui résoudra une valeur après l'invocation de la fonction, vous utilisez le mot-clé return. Vous écrivez cela dans le corps de la fonction.

**`return`** est une directive qui retourne une valeur à la fonction après que le code à l'intérieur a été exécuté.

Voici un exemple de fonction qui retourne une valeur, dans ce cas, la somme de deux nombres :

```javascript
function somme(a, b){
	return  a + b;
}

somme(10, 20);

//la sortie sera 30

```

L'utilisation de `return` à l'intérieur d'une fonction facilite la manipulation des données que la fonction retourne, soit en les passant comme valeur à, disons, une autre fonction, soit en effectuant des opérations supplémentaires sur elles.

## **Comment fonctionnent la portée des fonctions et les fermetures en JavaScript ?**

Une portée est un espace de noms imbriqué qui localise les noms créés à l'intérieur de celui-ci de sorte que ces noms n'interfèrent pas avec des noms similaires créés en dehors de cette portée. Certaines règles de portée s'appliquent à l'intérieur d'une fonction.

Chaque nouvelle fonction que vous définissez crée une nouvelle portée connue sous le nom de **portée de fonction**. Les variables créées dans la portée de la fonction ne sont pas visibles ou accessibles en dehors de cette portée.

Néanmoins, les variables créées en dehors de la portée de la fonction mais dans la portée dans laquelle la fonction est définie peuvent être accessibles à l'intérieur de la fonction. Par conséquent, si vous définissez une fonction dans la portée globale, elle peut accéder à toutes les variables déclarées dans cette portée globale.

De plus, supposons que vous avez une fonction enfant (c'est-à-dire une fonction interne) imbriquée dans une fonction parente (qui est la fonction externe). La fonction enfant peut accéder à toutes les variables et fonctions déclarées dans sa fonction parente ainsi qu'à toutes les variables et fonctions auxquelles la fonction parente a accès – même lorsque sa fonction parente a fini de s'exécuter et que ses variables ne sont plus accessibles en dehors de cette fonction. Ce concept est connu sous le nom de fermetures en JavaScript.

Cependant, la fonction parente ne peut pas accéder aux variables créées à l'intérieur de la fonction enfant. De cette manière, les variables et fonctions à l'intérieur de la fonction enfant sont confinées à leur propre portée.

Voyons un exemple de code de cela :

```javascript
//variables définies dans la portée globale

let  a = 40;
let b = 20;

//cette fonction est également définie dans la portée globale

function fonctionParente(){
	//accéder aux variables a et b à l'intérieur de cette fonction

	console.log(a + b); 
}

//sortie : 60

```

Supposons que je place une fonction interne à l'intérieur de la fonction parente, comme ceci :

```javascript
//variables définies dans la portée globale

let a = 40;
let b = 20;

//cette fonction est également définie dans la portée globale

function fonctionParente(){
	let  nom = "Doe";
    
    //cette fonction interne est définie à l'intérieur de la portée de la fonction parente
    
	function fonctionEnfant(){
		console.log(`${nom} a ${a - b} ans`); 
      }
    return fonctionEnfant();
}

fonctionParente(); //sortie : Doe a 20 ans

```

Maintenant, si je crée une variable à l'intérieur d'une fonction et que j'essaie d'y accéder depuis la portée globale, nous obtiendrons une erreur de référence. Cela est dû au fait que cette variable est locale à la portée de la fonction et n'est pas visible pour la portée globale.

```javascript
console.log(c);

function fonctionParente(){
	let c = 30
} 

//sortie : erreur de référence - c n'est pas défini
```

Essayons d'accéder à une variable créée à l'intérieur d'une fonction imbriquée dans la fonction parente :

```javascript
function fonctionParente(){
	console.log(age);
	function fonctionEnfant(){
		let  age = 20;
	} 
    return fonctionEnfant();
}

fonctionParente(); //sortie : erreur de référence - age n'est pas défini.

```

## Comment fonctionnent les paramètres par défaut en JavaScript ?

À l'origine, les paramètres de fonction sont assignés _undefined_ lorsqu'aucune valeur n'est explicitement passée. Les paramètres par défaut vous permettent d'assigner une valeur par défaut à un paramètre lorsque vous définissez une fonction. Par exemple :

```javascript
function salutation(nom, message = "Bonjour"){
	console. log(`${message}  ${nom}`)
}

salutation('John'); //sortie : Bonjour John

//vous pouvez également assigner une nouvelle valeur au paramètre par défaut 
//lorsque vous appelez la fonction

salutation('Doe', 'Salut'); //sortie : Salut Doe

```

Il est important de noter que dans la déclaration d'un paramètre par défaut, il doit venir après le paramètre régulier.

## **Comment fonctionnent les paramètres rest en JavaScript ?**

Avec les paramètres rest, vous pouvez définir une fonction pour stocker plusieurs arguments dans un seul tableau. Cela est particulièrement utile lorsque vous invoquez votre fonction avec plusieurs arguments. Voici un exemple :

```javascript
function direBonjour(message, ...noms){
  noms.forEach(nom => console.log(`${message} ${nom}`));
}

direBonjour('Bonjour', "John", "Smith", "Doe");

/*
sortie:

Bonjour John

Bonjour Smith

Bonjour Doe 

*/



```

Le `...` est ce qui fait de `noms` un paramètre rest.

Tout comme les paramètres par défaut, les paramètres rest doivent apparaître après tout paramètre régulier dans votre fonction.

## Conclusion

Dans cet article, vous avez appris ce que sont les fonctions en JavaScript et comment vous pouvez écrire vos propres fonctions. 

Avec les fonctions, vous pouvez organiser votre code en regroupant tout en blocs séparés qui effectuent différentes tâches. 

J'espère que vous avez apprécié la lecture de cet article. Pour en savoir plus sur les fonctions, voici quelques ressources que vous pouvez consulter :

* [Fonctions JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
* [Fermetures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

C'est tout pour cet article. Bon codage :)
---
title: Portée et Fermetures en JavaScript – Expliqué avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-01T23:52:27.000Z'
originalURL: https://freecodecamp.org/news/scope-and-closures-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/karine-avetisyan-ipuiM-36tAg-unsplash.jpg
tags:
- name: closure
  slug: closure
- name: JavaScript
  slug: javascript
- name: Scope
  slug: scope
seo_title: Portée et Fermetures en JavaScript – Expliqué avec des Exemples
seo_desc: "By Zach Snoek\nYou may have come across or written code similar to this\
  \ when writing JavaScript:\nfunction sayWord(word) {\n    return () => console.log(word);\n\
  }\n\nconst sayHello = sayWord(\"hello\");\n\nsayHello(); // \"hello\"\n\nThis code\
  \ is interesting for a..."
---

Par Zach Snoek

Vous avez peut-être rencontré ou écrit du code similaire à ceci en écrivant du JavaScript :

```javascript
function sayWord(word) {
	return () => console.log(word);
}

const sayHello = sayWord("hello");

sayHello(); // "hello"
```

Ce code est intéressant pour plusieurs raisons. Premièrement, nous pouvons accéder à `word` dans la fonction retournée par `sayWord`. Deuxièmement, nous avons accès à la valeur de `word` lorsque nous appelons `sayHello` – même si nous appelons `sayHello` là où nous n'avons pas autrement accès à `word`.

Dans cet article, nous allons apprendre la portée et les fermetures, qui permettent ce comportement.

## Introduction à la Portée en JavaScript

La portée est le premier élément qui nous aidera à comprendre l'exemple précédent. La portée d'une variable est la partie d'un programme où elle est disponible pour être utilisée.

Les variables JavaScript sont à portée lexicale, ce qui signifie que nous pouvons déterminer la portée d'une variable à partir de l'endroit où elle est déclarée dans le code source. (Ceci n'est pas entièrement vrai : les variables `var` ne sont pas à portée lexicale, mais nous en discuterons bientôt.)

Prenons l'exemple suivant :

```javascript
if (true) {
	const foo = "foo";
	console.log(foo); // "foo"
}
```

L'instruction `if` introduit une portée de bloc en utilisant une [déclaration de bloc](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block). Nous disons que `foo` est à portée de bloc dans l'instruction `if`. Cela signifie qu'il ne peut être accessible que depuis ce bloc.

Si nous essayons d'accéder à `foo` en dehors du bloc, nous obtenons une `ReferenceError` car il est hors de portée :

```javascript
if (true) {
	const foo = "foo";
	console.log(foo); // "foo"
}

console.log(foo); // Uncaught ReferenceError: foo is not defined
```

Les déclarations de bloc sous d'autres formes, telles que les boucles `for` et `while`, créeront également une portée pour les variables à portée de bloc. Par exemple, `foo` est à portée dans un corps de fonction ci-dessous :

```javascript
function sayFoo() {
	const foo = "foo";
	console.log(foo);
}

sayFoo(); // "foo"

console.log(foo); // Uncaught ReferenceError: foo is not defined
```

## Portées Imbriquées et Fonctions

JavaScript permet des blocs imbriqués et donc des portées imbriquées. Les portées imbriquées créent un arbre de portée ou une chaîne de portée.

Considérons le code ci-dessous, qui imbrique plusieurs déclarations de bloc :

```javascript
if (true) {
	const foo = "foo";
	console.log(foo); // "foo"

	if (true) {
		const bar = "bar";
		console.log(foo); // "foo"

		if (true) {
			console.log(foo, bar); // "foo bar"
		}
	}
}
```

JavaScript nous permet également d'imbriquer des fonctions :

```javascript
function foo(bar) {
	function baz() {
		console.log(bar);
	}

	baz();
}

foo("bar"); // "bar"
```

Comme prévu, nous pouvons accéder aux variables depuis leur portée directe (la portée où elles sont déclarées). Nous pouvons également accéder aux variables depuis leurs portées internes (les portées qui sont imbriquées dans leur portée directe). C'est-à-dire que nous pouvons accéder aux variables depuis la portée où elles sont déclarées et depuis chaque portée interne.

Avant d'aller plus loin, nous devons clarifier la différence de ce comportement entre les types de déclarations de variables.

## Portée de let, const, et var en JavaScript

Nous pouvons créer des variables avec les déclarations `let`, `const`, et `var`. Pour `let` et `const`, la portée de bloc fonctionne comme expliqué ci-dessus. Cependant, `var` se comporte différemment.

### let et const

`let` et `const` créent des variables à portée de bloc. Lorsqu'elles sont déclarées dans un bloc, elles ne sont accessibles que dans ce bloc. Ce comportement a été démontré dans nos exemples précédents :

```javascript
if (true) {
	const foo = "foo";
	console.log(foo); // "foo"
}

console.log(foo); // Uncaught ReferenceError: foo is not defined
```

### var

Les variables créées avec `var` sont à portée de leur fonction la plus proche ou de la portée globale (que nous discuterons bientôt). Elles ne sont pas à portée de bloc :

```javascript
function foo() {
	if (true) {
		var foo = "foo";
	}
	console.log(foo);
}

foo(); // "foo"
```

`var` peut créer des situations confuses, et cette information est incluse uniquement pour exhaustivité. Il est préférable d'utiliser `let` et `const` lorsque c'est possible. Le reste de cet article ne concernera que les variables `let` et `const`.

Si vous êtes intéressé par le comportement de `var` dans l'exemple ci-dessus, vous devriez consulter [mon article sur le hoisting](https://www.freecodecamp.org/news/what-is-hoisting-in-javascript/).

## Portée Globale et de Module en JavaScript

En plus des portées de bloc, les variables peuvent être à portée globale et de module.

Dans un navigateur web, la portée globale est au niveau supérieur d'un script. C'est la racine de l'arbre de portée que nous avons décrit précédemment, et elle contient toutes les autres portées. Ainsi, créer une variable dans la portée globale la rend accessible dans toutes les portées :

```html
<script>
	const foo = "foo";
</script>
<script>
	console.log(foo); // "foo"
		
	function bar() {
		if (true) {
			console.log(foo);
		}
	}

	bar(); // "foo"
</script>
```

Chaque module a également sa propre portée. Les variables déclarées au niveau du module ne sont disponibles que dans ce module – elles ne sont pas globales :

```html
<script type="module">
	const foo = "foo";
</script>
<script>
	console.log(foo); // Uncaught ReferenceError: foo is not defined
</script>
```

## Fermetures en JavaScript

Maintenant que nous comprenons la portée, revenons à l'exemple que nous avons vu dans l'introduction :

```javascript
function sayWord(word) {
	return () => console.log(word);
}

const sayHello = sayWord("hello");

sayHello(); // "hello"
```

Rappelons qu'il y avait deux points intéressants à propos de cet exemple :

1. La fonction retournée par `sayWord` peut accéder au paramètre `word`
2. La fonction retournée maintient la valeur de `word` lorsque `sayHello` est appelée en dehors de la portée de `word`

Le premier point peut être expliqué par la portée lexicale : la fonction retournée peut accéder à `word` parce qu'il existe dans sa portée externe.

Le deuxième point est dû aux fermetures : Une fermeture est une fonction combinée avec des références aux variables définies en dehors d'elle. Les fermetures maintiennent les références des variables, ce qui permet aux fonctions d'accéder aux variables en dehors de leur portée. Elles « enferment » la fonction et les variables dans son environnement.

## Exemples de Fermetures en JavaScript

Vous avez probablement rencontré et utilisé des fermetures fréquemment sans en être conscient. Explorons d'autres façons d'utiliser les fermetures.

### Callbacks

Il est courant qu'un callback référence une variable déclarée en dehors de lui-même. Par exemple :

```javascript
function getCarsByMake(make) {
	return cars.filter(x => x.make === make);
}
```

`make` est disponible dans le callback grâce à la portée lexicale, et la valeur de `make` est conservée lorsque la fonction anonyme est appelée par `filter` grâce à une fermeture.

### Stocker l'état

Nous pouvons utiliser des fermetures pour retourner des objets depuis des fonctions qui stockent l'état. Considérons la fonction `makePerson` suivante qui retourne un objet pouvant stocker et changer un `name` :

```javascript
function makePerson(name) {
	let _name = name;

	return {
		setName: (newName) => (_name = newName),
		getName: () => _name,
	};
}

const me = makePerson("Zach");
console.log(me.getName()); // "Zach"

me.setName("Zach Snoek");
console.log(me.getName()); // "Zach Snoek"
```

Cet exemple illustre comment les fermetures ne figent pas simplement les valeurs des variables de la portée externe d'une fonction lors de sa création. Au lieu de cela, elles maintiennent les références tout au long de la durée de vie de la fermeture.

### Méthodes privées

Si vous êtes familier avec la programmation orientée objet, vous avez peut-être remarqué que notre exemple précédent ressemble étroitement à une classe qui stocke un état privé et expose des méthodes publiques de getter et de setter. Nous pouvons étendre cette parallèle orientée objet en utilisant des fermetures pour implémenter des méthodes privées :

```javascript
function makePerson(name) {
	let _name = name;

	function privateSetName(newName) {
		_name = newName;
	}

	return {
		setName: (newName) => privateSetName(newName),
		getName: () => _name,
	};
}
```

`privateSetName` n'est pas directement accessible aux consommateurs et peut accéder à la variable d'état privée `_name` grâce à une fermeture.

### Gestionnaires d'événements React

Enfin, les fermetures sont courantes dans les gestionnaires d'événements React. Le composant `Counter` suivant est modifié à partir de la [documentation React](https://reactjs.org/docs/hooks-reference.html#functional-updates) :

```jsx
function Counter({ initialCount }) {
	const [count, setCount] = React.useState(initialCount);

	return (
		<>
			<button onClick={() => setCount(initialCount)}>Reset</button>
			<button onClick={() => setCount((prevCount) => prevCount - 1)}>
				-
			</button>
			<button onClick={() => setCount((prevCount) => prevCount + 1)}>
				+
			</button>
			<button onClick={() => alert(count)}>Show count</button>
		</>
	);
}

function App() {
	return <Counter initialCount={0} />;
}
```

Les fermetures permettent :

* aux gestionnaires de clics des boutons de réinitialisation, de décrémentation et d'incrémentation d'accéder à `setCount`
* au bouton de réinitialisation d'accéder à `initialCount` depuis les props de `Counter`
* et au bouton "Show count" d'afficher l'état `count`.

Les fermetures sont importantes dans d'autres parties de React, telles que les props et les hooks. La discussion sur ces sujets est hors de portée pour cet article. Je recommande de lire [cet article](https://epicreact.dev/how-react-uses-closures-to-avoid-bugs/) de Kent C. Dodds ou [cet article](https://overreacted.io/making-setinterval-declarative-with-react-hooks/) de Dan Abramov pour en apprendre davantage sur le rôle que jouent les fermetures dans React.

## Conclusion

La portée fait référence à la partie d'un programme où nous pouvons accéder à une variable. JavaScript nous permet d'imbriquer des portées, et les variables déclarées dans les portées externes sont accessibles depuis toutes les portées internes. Les variables peuvent être à portée globale, de module ou de bloc.

Une fermeture est une fonction enfermée avec des références aux variables dans sa portée externe. Les fermetures permettent aux fonctions de maintenir des connexions avec les variables externes, même en dehors de la portée des variables.

Il existe de nombreuses utilisations des fermetures, de la création de structures de type classe qui stockent l'état et implémentent des méthodes privées à la transmission de callbacks aux gestionnaires d'événements.

## Restons en contact

Si vous êtes intéressé par plus d'articles comme celui-ci, [abonnez-vous à ma newsletter](https://mailchi.mp/2df4b6d5458f/signup-page) et connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/zach-snoek-5b327b179/) et [Twitter](https://twitter.com/zach_snoek) !

## Remerciements

Merci à [Bryan Smith](https://github.com/bryanrsmith) pour ses commentaires sur les brouillons de cet article.

Photo de couverture par [Karine Avetisyan](https://unsplash.com/@kar111?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/chain?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).
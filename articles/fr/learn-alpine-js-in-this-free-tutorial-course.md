---
title: Apprenez Alpine JS dans ce tutoriel interactif gratuit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-24T14:58:11.000Z'
originalURL: https://freecodecamp.org/news/learn-alpine-js-in-this-free-tutorial-course
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/galpinejs.png
tags:
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
seo_title: Apprenez Alpine JS dans ce tutoriel interactif gratuit
seo_desc: "By Per Harald Borgen\nAlpine.js is a rugged, minimal framework for composing\
  \ Javascript behavior in your markup. That's right, in your markup! \nIt allows\
  \ you to write most of your JS inline in your HTML, making it easier to write declarative\
  \ code (as ..."
---

Par Per Harald Borgen

Alpine.js est un framework minimaliste et robuste pour composer des comportements JavaScript directement dans votre balisage. Oui, dans votre balisage ! 

Il vous permet d'écrire la plupart de votre JS en ligne dans votre HTML, ce qui facilite l'écriture de code déclaratif (par opposition au code procédural). Selon son créateur Caleb Porzio, il vise à combler le vide entre le JS vanilla (ou jQuery) et les grands frameworks v-dom comme Vue/React. 

Nous, chez Scrimba, pensons définitivement qu'il tient sa promesse, c'est pourquoi nous sommes heureux de vous présenter un [cours gratuit d'une heure !](https://scrimba.com/g/galpinejs?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=galpinejs_launch_article) 

%[https://twitter.com/scrimba/status/1231942780492165120]

Dans ce cours, vous trouverez une série de tutoriels interactifs et amusants qui ancrent votre apprentissage et vous donnent la mémoire musculaire nécessaire pour devenir un expert d'Alpine.js.

Maintenant, examinons comment le cours est structuré !

## Pourquoi apprendre Alpine.js ?

Dans la première leçon, l'enseignant Andre Madarang commence par expliquer pourquoi vous devriez apprendre cette bibliothèque. En bref, Alpine.js est efficace lorsque vous avez besoin d'une petite quantité de JS, par exemple, quelques menus déroulants ou onglets. Cela signifie que vous obtenez une grande puissance avec une taille incroyablement petite et sans avoir besoin d'installer NPM.

Andre se présente également. Il est développeur full-stack et YouTuber qui enseigne des concepts de développement web tels que Laravel, Vue et Tailwind CSS. Nous sommes ravis de l'avoir à bord en tant qu'enseignant Scrimba !

## Installation et un composant Alpine de base

L'installation d'Alpine.js est facile - vous pouvez utiliser npm si vous le souhaitez, mais Andre nous montre également comment utiliser un cdn et l'ajouter dans une balise `script` - c'est aussi simple que cela ! :

```html
<head>
	<script
		src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.9.8/dist/alpine.js"
		defer
	></script>
</head>

```

Maintenant, il est temps de créer notre premier composant Alpine.js ! Tout d'abord, nous définissons l'état en utilisant l'attribut `x-data`. L'état est disponible dans le scope de la `<div>` dans laquelle il est défini, donc dans l'exemple ci-dessous, à la fois le `<button>` et le `<h1>` ont accès à l'état.

Pour utiliser cet état, nous utilisons ensuite la directive `x-show` pour afficher ou masquer l'élément et basculer l'élément en utilisant `@`.

```html
<div x-data="{ isOpen: true }">
	<button @click=" isOpen = !isOpen">Basculer</button>
	<h1 x-show="isOpen">index.html</h1>
</div>

```

## Menu déroulant

Maintenant, nous utilisons notre nouvelle connaissance de l'état pour implémenter un menu déroulant.

![UI avec un menu déroulant](https://dev-to-uploads.s3.amazonaws.com/i/emgjs6bayqsolgxpio6i.png)

Nous voyons ensuite comment définir des événements pour fermer le menu déroulant en cliquant à l'extérieur du menu ou en appuyant sur la touche échap, en utilisant `@click.away` sur la `<ul>` ou `@keydown.escape` sur le `<button>`.

## Modales et x-ref

Dans ce cast, Andre nous montre un autre exemple de l'utilisation de l'état pour ouvrir et fermer une modale. Ensuite, il introduit les références, qui nous permettent d'ajouter des méthodes à des éléments particuliers dans le gestionnaire de clics.

Dans ce cas, nous mettons le focus sur le bouton de fermeture une fois la modale ouverte en ajoutant une référence au bouton de fermeture avec une directive `x-ref` puis en ajoutant une méthode au gestionnaire de clics.

```html
<button
	class="bg-blue-700 text-white px-4 py-3 mt-4 text-sm rounded"
	@click="isOpen = false"
	x-ref="modalCloseButton"
></button>

```

```html
<button
	class="bg-blue-700 text-white px-4 py-3 mt-4 text-sm rounded"
	@click="isOpen = true
                    $nextTick(() => $refs.modalCloseButton.focus())
                    "
></button>

```

## Barre latérale

Maintenant, il est temps de faire une révision pour aider notre nouvelle connaissance à s'ancrer. Dans ce court cast, nous ajoutons la fonctionnalité pour basculer la visibilité d'une barre latérale. C'est un excellent moyen d'ancrer notre apprentissage et de nous montrer une autre application de ce que nous avons appris.

![UI avec barre latérale](https://dev-to-uploads.s3.amazonaws.com/i/olbjs8mspkd8zutkkzir.png)

## Onglets

Ensuite, nous construisons un ensemble d'onglets. Cela est plus impliqué que nos exemples précédents car nous devons maintenir l'état pour tous les onglets, et pas seulement un booléen.

Comme d'habitude, l'état est défini en utilisant la directive `x-data` sur un élément HTML qui encapsule tous les éléments requis. Nous définissons ensuite la valeur par défaut sur `tab1` et définissons un écouteur d'événement (qui rend l'onglet actif) pour chacun des onglets.

```html
<li class="-mb-px mr-1">
	<a
		class="inline-block rounded-t py-2 px-4 font-semibold hover:text-blue-800 bg-white text-blue-700 border-l border-t border-r"
		href="#"
		@click.prevent="tab = 'tab1'"
		>Onglet 1</a
	>
</li>

```

Pour changer la section de contenu en fonction de l'onglet qui a été cliqué, nous ajoutons des directives `x-show` aux `<div>` contenant le contenu :

```html
<div x-show="tab === 'tab1'"></div>

```

Enfin, Andre nous montre comment appliquer les styles de l'onglet actif avec un rendu de classe conditionnel.

```css
:class="{ 'bg-white text-blue-700 border-l border-t border-r' : tab === 'tab1'
}" ;

```

## Sélection d'image

Dans ce cast, Andre nous montre comment les compétences que nous avons apprises dans le cast précédent peuvent être appliquées à une expérience UI différente - un sélecteur d'image. Les sélecteurs d'image fonctionnent de la même manière que les onglets, mais avec des images au lieu de texte.

[Sélecteur d'image](https://dev-to-uploads.s3.amazonaws.com/i/58dfy95mhhl1w0rtgfjt.png)

![Sélecteur d'image](https://dev-to-uploads.s3.amazonaws.com/i/58dfy95mhhl1w0rtgfjt.png)

## Détection de défilement

Maintenant, Andre nous montre comment construire un détecteur de défilement qui change la couleur de fond lorsque l'utilisateur fait défiler la page. Pour ce faire, nous définissons un état qui garde une trace de si l'utilisateur a fait défiler la page.

```html
<div x-data="{ atTop: true }"></div>

```

Maintenant, nous ajoutons un écouteur d'événement de défilement sur la fenêtre et un rendu de classe conditionnel sur la `<nav>`.

```html
<nav
	class="p-4 w-full fixed"
	:class="{ 'bg-white shadow-md' : !atTop }"
	@scroll.window="atTop = (window.pageYOffset > 40) ? false : true"
>
	La navigation supérieure va ici
</nav>

```

## Bascule d'accordéon et boucles

Dans cette section, nous construisons une bascule d'accordéon en utilisant des boucles. Dans notre exemple, il y a plusieurs FAQ avec des réponses, et nous voulons basculer la visibilité des réponses.

Une excellente façon de faire cela sans répéter de code est d'utiliser des boucles. Pour ce faire, nous stockons toutes nos questions et réponses dans un tableau, nous les parcourons en boucle, puis nous définissons l'écouteur d'événement sur chaque itération de la boucle.

**Note :** Pour que cela fonctionne, nos éléments doivent être enveloppés dans une balise `template`.

```html
<template x-for="faq in faqs" :key="faq.question">
	<div>
		<button
			class="w-full font-bold border-b border-gray-400 py-3 flex justify-between items-center mt-4"
			@click="faq.isOpen = !faq.isOpen"
		>
			<div x-text="faq.question"></div>
		</button>
		<div
			class="text-gray-700 text-sm mt-2"
			x-text="faq.answer"
			x-show="faq.isOpen"
		></div>
	</div>
</template>

```

## fetch et x-init

Maintenant, nous voyons comment nous pouvons faire des requêtes à une API externe. Cela semble intimidant mais se décompose facilement en quatre étapes.

* Ajouter un état pour contenir les citations :

```js
x - data = "{ quote:'' }";

```

* Donner à l'application une citation à afficher lors de l'initialisation :

```js
x - init = "quote = 'Awesome quote'";

```

* Définir le texte dans la `<div>` qui affiche la citation comme l'état : 

Utiliser `fetch` pour récupérer la citation d'une API externe :

```js
x-init=" fetch('https://api.kanye.rest') .then(response => response.json()) .then(data => quote = data.quote) "
```

Voici le bloc de code complet :

```html
<div
	class="container mx-auto px-4"
	x-data="{ quote:'' }"
	x-init="
                fetch('https://api.kanye.rest')
                    .then(response => response.json())
                    .then(data => quote = data.quote)
            "
>
	<div
		class="flex items-center text-center justify-center h-screen text-2xl italic"
		x-text='`"${quote}"`'
	></div>
</div>

```

L'interface utilisateur ressemble à ceci :

![Générateur de code tel que vu par l'utilisateur final](https://dev-to-uploads.s3.amazonaws.com/i/evbizajs28yldwnx47bg.png)

## Application Todo et x-model

Dans ce cast, nous apprenons à construire une mini application de liste de tâches. Nous avons besoin de trois morceaux d'état pour cela ; un pour garder les tâches dans un tableau (`todos`), un pour garder une trace de ce que l'utilisateur tape comme nouvelle tâche (`todoTitle`) et un pour garder une trace du nouvel ID de tâche (`todoId`).

Comme nous utilisons plusieurs morceaux d'état, nous extrayons notre fonction dans une balise `<script>` pour rendre les choses plus claires. La fonction retourne un objet qui contient notre état et nos fonctions :

```html
<script>
	function todos() {
		return {
			todos: [
				{
					id: 1,
					title: "Terminer le screencast Alpine",
					isComplete: false
				}
			],
			todoTitle: "",
			todoId: 2
		};
	}
</script>

```

Maintenant, nous parcourons nos tâches pour afficher le titre que nous avons stocké dans le tableau et ajoutons conditionnellement une ligne barrée si la tâche est terminée.

```html
<template x-for="todo in todos" :key="todo.id">
	<li class="flex items-center justify-between">
		<div
			class="flex items-center"
			:class="{ 'line-through' : todo.isComplete }"
		>
			<input type="checkbox" />
			<div class="ml-3" x-text="todo.title"></div>
		</div>
		<button class="text-xl ml-2">&times;</button>
	</li>
</template>

```

Nous travaillons maintenant sur l'ajout d'une tâche. Tout d'abord, nous ajoutons une directive `x-model` à notre `<input>` qui synchronise le `todoTitle` avec ce qui est tapé dans le `<input>` :

```html
<input
	type="text"
	class="shadow w-full px-2 py-2"
	x-model="todoTitle"
	@keydown.enter="addTodo()"
/>

```

La fonction que nous voulons exécuter lorsqu'un utilisateur tape une nouvelle tâche est ensuite ajoutée à notre balise `<script>`.

Nous utilisons également un `x-model` sur la case à cocher pour permettre à l'utilisateur de marquer une tâche comme terminée.

```html
<input type="checkbox" x-model="todo.isComplete" />

```

## Transitions : Menu déroulant

Ensuite, Andre nous montre quelques transitions funky qui donnent à notre menu déroulant une finition nette et professionnelle en utilisant les classes utilitaires de Tailwind CSS. Ces transitions vous donnent un contrôle fin sur la manière dont votre menu déroulant passe de masqué à visible, avec des options incluant l'opacité, la durée, l'origine et d'autres.

```html
<ul
	x-show="isOpen"
	@click.away="isOpen = false"
	class="absolute font-normal bg-white shadow overflow-hidden rounded w-48 border mt-2 py-1 right-0 z-20"
	x-transition:enter="transition transform origin-top-right ease-out duration-200"
	x-transition:enter-start="opacity-0 scale-75"
	x-transition:enter-end="opacity-100 scale-100"
	x-transition:leave="transition transform origin-top-right ease-out duration-200"
	x-transition:leave-start="opacity-100 scale-100"
	x-transition:leave-end="opacity-0 scale-75"
></ul>

```

## Transitions : Modale

Maintenant, il est temps de mettre à l'épreuve nos nouvelles connaissances des transitions en les ajoutant à notre modale. Dans l'esprit de Scrimba, Andre nous donne une chance de tester nos nouvelles compétences avant de nous montrer comment il le fait, donc pas de spoilers ici !

## Transitions : Barre latérale

Enfin, nous ajoutons une belle transition fluide pour la barre latérale que nous avons implémentée précédemment. Encore une fois, pas de spoilers, donc vous pouvez essayer par vous-même lorsque vous regarderez le cours.

## Conclusion

Nous avons maintenant examiné quelques cas d'utilisation pour Alpine.js et construit quelques exemples où il pourrait être un meilleur choix que React ou Vue. Espérons que vous avez appris quelque chose de nouveau sur Alpine.js et que vous mettrez vos nouvelles compétences à bon escient très bientôt.

Si vous ne l'avez pas encore fait, n'oubliez pas de consulter le [cours sur Scrimba](https://scrimba.com/g/galpinejs?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=galpinejs_launch_article).

En attendant, bon codage avec Alpine ! :)

%[https://www.youtube.com/watch?v=VerLjLcXsTk]
---
title: Comment créer un menu déroulant avec CSS et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-15T21:50:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-dropdown-menu-with-css-and-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eac740569d1a4ca3e7c.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
seo_title: Comment créer un menu déroulant avec CSS et JavaScript
seo_desc: In this tutorial you will learn how to create a simple dropdown menu with
  vanilla Javascript, HTML and CSS. We will walk through the HTML, CSS and Javascript
  code, but paying more attention to the programming, since this is a JS tutorial.
  We’ll use j...
---

Dans ce tutoriel, vous apprendrez à créer un menu déroulant simple avec JavaScript vanilla, HTML et CSS. Nous passerons en revue le code HTML, CSS et JavaScript, mais en accordant plus d'attention à la programmation, puisque c'est un tutoriel JS. Nous utiliserons simplement du JS et du CSS pur, sans frameworks ni préprocesseurs. La seule (en quelque sorte) exception sera l'importation du fichier CSS de [Font Awesome](https://fontawesome.com/) car nous utiliserons l'une de ses icônes.

Ce tutoriel s'adresse aux développeurs qui ont une compréhension moyenne de HTML, CSS et JS. J'ai essayé de le rendre aussi propre que possible, mais je ne me concentrerai pas trop sur les détails ici. J'espère que vous apprécierez tous.

## **Captures d'écran**

Voici à quoi ressemble le résultat du code :

Écran initial :

![Image](https://i.imgur.com/jrnu6mE.png)

Menu déroulant ouvert :

![Image](https://i.imgur.com/gszPtRa.png)

Menu déroulant avec une option sélectionnée :

![Image](https://i.imgur.com/TKXxZGF.png)

#### **HTML :**

Dans cette section, nous discuterons de la mise en œuvre du code HTML pour la page de démonstration. Commençons par voir le code `<head>`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Exemple de menu déroulant</title>

	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="styles.css">
</head>
```

Il s'agit essentiellement du code standard de l'en-tête HTML, à l'exception des balises `link` qui chargent les deux feuilles de style CSS que nous utiliserons dans ce tutoriel : les styles Font Awesome et le fichier `styles.css`, où nous définirons les styles de cette page.

Ensuite, il y a le reste du fichier HTML, le corps :

```html
<body>
	<div class='dropdown'>
		<div class='title pointerCursor'>Sélectionnez une option <i class="fa fa-angle-right"></i></div>
		
		<div class='menu pointerCursor hide'>
			<div class='option' id='option1'>Option 1</div>
			<div class='option' id='option2'>Option 2</div>
			<div class='option' id='option3'>Option 3</div>
			<div class='option' id='option4'>Option 4</div>
		</div>

	</div>
	<span id='result'>Le résultat est : </span>
	<script>
	  ...
	</script>
</body>
</html>
```

Cette section peut être divisée en 3 parties principales :

* La div `.dropdown`, où la structure de l'élément du menu déroulant sera définie.
* L'élément `#result`, qui contiendra l'option sélectionnée par l'utilisateur, à partir de l'élément du menu déroulant.
* Le script écrit dans la balise `<script>`. Sa mise en œuvre est cachée ici, car ses détails seront expliqués dans la dernière section de ce tutoriel.

L'élément du menu déroulant est une `div` contenant des éléments `title` et `menu`. Le premier définit simplement le texte qui sera présenté sur l'élément avant qu'une option ne soit sélectionnée, et le second définira les options qui pourront être sélectionnées par l'élément.

L'élément `result` est là pour vous montrer quelle option est actuellement sélectionnée.

#### **Styles :**

Vous pouvez consulter le code CSS complet ci-dessous. Comme vous pouvez le voir, il utilise les constructions CSS3 `transition` et `transform`.

Veuillez prêter attention aux définitions des classes `.dropdown`. Celles-ci sont utilisées pour définir la disposition du composant conteneur du menu déroulant ainsi que ses éléments internes, tels que `.title` et ses `.option`.

```css
body{
	font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.hide {
    max-height: 0 !important;
}

.dropdown{
	border: 0.1em solid black;
	width: 10em;
	margin-bottom: 1em;
}

.dropdown .title{
	margin: .3em .3em .3em .3em;	
	width: 100%;
}

.dropdown .title .fa-angle-right{
	float: right;
	margin-right: .7em;
	transition: transform .3s;
}

.dropdown .menu{
	transition: max-height .5s ease-out;
	max-height: 20em;
	overflow: hidden;
}

.dropdown .menu .option{
	margin: .3em .3em .3em .3em;
	margin-top: 0.3em;
}

.dropdown .menu .option:hover{
	background: rgba(0,0,0,0.2);
}

.pointerCursor:hover{
	cursor: pointer;
}

.rotate-90{
	transform: rotate(90deg);
}
```

#### **JavaScript :**

Maintenant, nous allons voir comment la partie JavaScript est implémentée. Nous commencerons par les définitions de fonctions, puis le code qui appelle ces fonctions pour faire fonctionner les actions du menu déroulant.

En gros, il y a 3 actions qui ont lieu en fonction de l'interaction de l'utilisateur, car leurs écouteurs sont ajoutés aux éléments du DOM :

1. Cliquer sur l'élément du menu déroulant
2. Sélectionner l'une des options du menu déroulant
3. Changer l'option actuellement sélectionnée

Je tiens à préciser que nous utilisons des fonctions fléchées (`() => {}`) et le mot-clé `const`, qui sont des fonctionnalités d'ES6. Vous devriez être en mesure de les utiliser si vous utilisez une version récente de votre navigateur, mais gardez cela à l'esprit.

#### **1. Cliquer sur l'élément du menu déroulant**

```javascript
function toggleClass(elem,className){
	if (elem.className.indexOf(className) !== -1){
		elem.className = elem.className.replace(className,'');
	}
	else{
		elem.className = elem.className.replace(/\s+/g,' ') + 	' ' + className;
	}
	
	return elem;
}

function toggleDisplay(elem){
	const curDisplayStyle = elem.style.display;			
				
	if (curDisplayStyle === 'none' || curDisplayStyle === ''){
		elem.style.display = 'block';
	}
	else{
		elem.style.display = 'none';
	}
}


function toggleMenuDisplay(e){
	const dropdown = e.currentTarget.parentNode;
	const menu = dropdown.querySelector('.menu');
	const icon = dropdown.querySelector('.fa-angle-right');

	toggleClass(menu,'hide');
	toggleClass(icon,'rotate-90');
}
```

Lorsque l'élément du menu déroulant est cliqué, il s'ouvre (s'il est fermé) ou se ferme (s'il est ouvert). Cela se produit en liant `toggleMenuDisplay` à l'écouteur d'événement de clic sur l'élément du menu déroulant. Cette fonction bascule l'affichage de son élément `menu` en utilisant les fonctions `toggleDisplay` et `toggleClass`.

#### **2. Sélectionner l'une des options du menu déroulant**

```javascript
function handleOptionSelected(e){
	toggleClass(e.target.parentNode, 'hide');			

	const id = e.target.id;
	const newValue = e.target.textContent + ' ';
	const titleElem = document.querySelector('.dropdown .title');
	const icon = document.querySelector('.dropdown .title .fa');


	titleElem.textContent = newValue;
	titleElem.appendChild(icon);
	
	//déclencher un événement personnalisé
	document.querySelector('.dropdown .title').dispatchEvent(new Event('change'));
	//setTimeout est utilisé pour que la transition soit correctement affichée
	setTimeout(() => toggleClass(icon,'rotate-90',0));
}
```

#### **3. Changer l'option actuellement sélectionnée**

```javascript
function handleTitleChange(e){
	const result = document.getElementById('result');

	result.innerHTML = 'Le résultat est : ' + e.target.textContent;
}
```

La fonction `handleTitleChange` est liée à l'événement personnalisé `change` sur l'élément `.title`, pour changer le contenu de l'élément `#result` chaque fois que l'élément du titre change. Le déclenchement de cet événement est effectué dans la section précédente.

#### **Code principal**

```javascript
//obtenir les éléments
const dropdownTitle = document.querySelector('.dropdown .title');
const dropdownOptions = document.querySelectorAll('.dropdown .option');

//lier les écouteurs à ces éléments
dropdownTitle.addEventListener('click', toggleMenuDisplay);
dropdownOptions.forEach(option => option.addEventListener('click',handleOptionSelected));
document.querySelector('.dropdown .title').addEventListener('change',handleTitleChange);
```

Dans la section principale, il y a juste un peu de code simple pour obtenir le titre et les options du menu déroulant afin de lier à ceux-ci les événements discutés dans la dernière section.

## **Démonstration**

Le code complet de cette application et la démonstration peuvent être trouvés [ici](https://codepen.io/GCrispino/pen/EEXmYd).

## **Plus d'informations**

* [Introduction à ES6](https://guide.freecodecamp.org/javascript/es6)
* [Fonctions fléchées](https://guide.freecodecamp.org/javascript/es6/arrow_functions/)
* [Let et Const](https://guide.freecodecamp.org/javascript/es6/let_and_const/)
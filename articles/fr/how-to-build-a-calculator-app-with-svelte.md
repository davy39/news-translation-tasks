---
title: Comment créer une application de calculatrice avec Svelte
subtitle: ''
author: Adejumo Ridwan Suleiman
co_authors: []
series: null
date: '2023-08-22T15:48:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-calculator-app-with-svelte
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/WHATSAPP-DICTIONARY-CHATBOT--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: Svelte
  slug: svelte
seo_title: Comment créer une application de calculatrice avec Svelte
seo_desc: 'Svelte is an open-source front-end JavaScript framework used for building
  web applications, designed to make developing interactive user interfaces more efficient
  and performant.

  Compared to other front-end frameworks like React, Vue, or Angular, it ...'
---

Svelte est un framework JavaScript open-source pour le développement front-end, utilisé pour construire des applications web, conçu pour rendre le développement d'interfaces utilisateur interactives plus efficace et performant.

Comparé à d'autres frameworks front-end comme React, Vue ou Angular, il se concentre sur une approche différente en compilant les composants.

Dans la plupart des frameworks traditionnels, vous construisez des composants en utilisant une abstraction de DOM virtuel (Document Object Model).

Dans ces frameworks, les modifications de l'interface utilisateur sont d'abord effectuées sur une représentation virtuelle de l'interface utilisateur qui calcule les différences et met à jour le DOM réel en conséquence. Ce processus peut introduire des surcharges et des goulots d'étranglement de performance, surtout pour les applications complexes.

Svelte, en revanche, adopte une approche différente.

Il déplace une grande partie du travail vers le processus de construction, en compilant les composants en code JavaScript hautement optimisé qui manipule directement le DOM pendant l'exécution.

Les applications Svelte ont une empreinte d'exécution plus petite et peuvent souvent atteindre de meilleures performances par rapport aux applications construites avec des frameworks traditionnels.

Dans ce tutoriel, vous apprendrez à construire une calculatrice simple en utilisant Svelte.

Contrairement à la plupart des frameworks, Svelte n'a pas une courbe d'apprentissage abrupte. Une compréhension de base de HTML, CSS et JavaScript est suffisante pour maîtriser Svelte.

Les prérequis pour ce tutoriel sont les suivants :

* Connaissance de base de HTML, CSS et JavaScript
  
* Volonté d'apprendre
  

Vous pouvez expérimenter le fonctionnement de la calculatrice [ici](https://svelte.dev/repl/cdf560babcf148639631872f27ba3275?version=4.2.0).

## Comment planifier le projet

Ceux qui échouent à planifier, planifient d'échouer. Il est bon de planifier ce que vous construisez.

Nous voulons que l'application de calculatrice suive certains critères comme suit :

* La calculatrice doit avoir une interface conviviale avec des boutons pour les chiffres (0-9), le point décimal (.) et les opérations arithmétiques (+, -, \*, /).
  
* Elle doit afficher l'entrée actuelle et le résultat à l'écran.
  
* La calculatrice doit supporter plusieurs opérations arithmétiques en séquence (par exemple : 2 + 3 \* 5).
  
* L'utilisateur doit pouvoir effacer l'entrée et réinitialiser la calculatrice.
  
* La calculatrice doit gérer les cas limites et empêcher les entrées invalides.
  

Ci-dessous se trouve un design de l'apparence de la calculatrice. Vous pouvez utiliser des outils comme [Figma](https://www.figma.com/) ou [Adobe XD](https://helpx.adobe.com/xd/get-started.html) pour dessiner comment vous voulez que votre interface utilisateur apparaisse ou l'esquisser sur papier.

![Image de la calculatrice proposée à construire](https://www.freecodecamp.org/news/content/images/2023/08/image-118.png align="left")

## Comment construire l'interface utilisateur

La calculatrice que vous allez construire est une application simple utilisant [Svelte REPL](https://svelte.dev/repl/hello-world?version=4.2.0). C'est un environnement de codage interactif qui vous permet de jouer avec Svelte sans avoir à le configurer localement sur votre PC.

Mais si vous préférez suivre localement, assurez-vous d'avoir [Node.js](https://nodejs.org/en) installé, et exécutez le code suivant sur votre terminal :

```shell
npm create svelte@latest <nom-de-votre-app>
cd myapp
npm install
npm run dev
```

Vous pouvez lire plus [ici](https://svelte.dev/docs/introduction) sur comment commencer.

Svelte vous permet de construire des applications basées sur des composants écrits dans un fichier `.svelte`. Une application web contient des composants tels que des boutons, des en-têtes, etc.

Svelte simplifie ce processus en vous permettant de le créer une fois et de le réutiliser dans n'importe quelle partie de votre application. La plupart des applications web contiennent un ou plusieurs composants.

L'application principale se trouve dans `App.svelte`, qui contient le code principal pour l'application de calculatrice que vous êtes sur le point de construire.

Lorsque vous ouvrez [Svelte REPL](https://svelte.dev/repl/hello-world?version=4.2.0), vous pouvez voir que l'application par défaut imprime *Hello World* à l'écran :

```html
<script>
	let name = 'world';
</script>

<h1>Hello {name}!</h1>
```

![Image affichant l'application Hello World](https://www.freecodecamp.org/news/content/images/2023/08/image-119.png align="left")

Un fichier `.svelte` contient JavaScript, HTML et CSS.

Le JavaScript est écrit dans la balise `<script>...</script>`, tandis que vous pouvez écrire le code HTML en dessous, et appliquer le style CSS dans la balise `<style>...</style>`.

```html
<script>
	let name = 'world';
</script>

<h1>Hello {name}!</h1>
<style>
	h1{
		background: red;
	}
</style>
```

![Image du résultat du code ci-dessus, Hello World est imprimé avec un fond rouge](https://www.freecodecamp.org/news/content/images/2023/08/image-120.png align="left")

Les variables déclarées dans la balise script sont affichées en utilisant les parenthèses courbées `{}`. Tout comme vous pouvez voir `Hello Word` affiché en utilisant la variable `name`.

Maintenant, commençons à construire l'application, copiez et collez le code suivant dans `App.svelte` :

```html
<script>
</script>

<div class="calculator">
	<div class="display"></div>
	<div class="buttons">
		<button>7</button>
		<button>8</button>
		<button>9</button>
		<button class="operator">+</button>
		<button>4</button>
		<button>5</button>
		<button>6</button>
		<button class="operator">-</button>
		<button>1</button>
		<button>2</button>
		<button>3</button>
		<button class="operator">*</button>
		<button>0</button>
		<button>.</button>
		<button class="clear">C</button>
		<button class="operator">/</button>
		<button class="equals">=</button>
	</div>
</div>

<style>

</style>
```

![Image montrant le résultat du code ci-dessus, les boutons sont tous disposés horizontalement sans aucun style](https://www.freecodecamp.org/news/content/images/2023/08/image-121.png align="left")

Si vous avez fait cela, vous avez créé deux divs – `calculator` et `display`. `calculator` est la div parente qui contient `display` et les boutons de la calculatrice.

Toutes les opérations arithmétiques portent le nom de classe `operator`. Le signe de suppression porte également le nom de classe `clear`, et le signe égal porte le nom de classe `equals`.

Vous ne voyez peut-être pas l'affichage maintenant car nous n'avons pas appliqué de style CSS.

À l'intérieur de la balise `<style></style>`, collez le code ci-dessous :

```javascript
<script>

</script>

...

<style>
.calculator {
	display: inline-block;
	border: 1px solid #ccc;
	padding: 10px;
	border-radius: 5px;
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.display {
	font-size: 24px;
	border: 1px solid #ccc;
	height: 24px;
	padding: 10px;
	margin-bottom: 10px;
	width: 300px;
	text-align: right;
}
</style>
```

![Image montrant le style appliqué sur les deux divs calculator et display](https://www.freecodecamp.org/news/content/images/2023/08/image-122.png align="left")

Maintenant, stylisons les boutons en une grille de quatre colonnes.

Mettez à jour la balise `<style></style>` avec le style `buttons` et `button` ci-dessous :

```html
...

<style>
 ...
.buttons {
	display: grid;
	grid-template-columns: repeat(4, 75px);
	gap: 5px;
}

button {
	padding: 10px;
	font-size: 18px;
	border: none;
	cursor: pointer;
	border-radius: 5px;
	font-family: Arial, sans-serif;
	text-align: center;
}
</style>
```

Notez que `buttons` est le nom de classe pour la div contenant les diverses balises HTML `button`.

![Image affichant la grille de 4 colonnes de la div des boutons](https://www.freecodecamp.org/news/content/images/2023/08/image-123.png align="left")

Ensuite, stylisons les boutons pour améliorer l'expérience utilisateur pour quiconque utilise la calculatrice et faisons en sorte que le bouton égal occupe les espaces vides.

Mettez à jour la balise `<style></style>` comme suit :

```html
...
<style>
 ...
 .operator{
	border: 0px solid #A46D19;
	background: #F90;
}
.clear{
	border: 0px solid #000;
	background: red;
}
.equals{
	border: 0px solid #000;
	background: #245BE9;
	width: 320px
}
</style>
```

![Image montrant l'interface utilisateur de la calculatrice, avec une couleur orange donnée aux boutons arithmétiques, rouge au bouton de suppression et bleu au bouton du signe égal. Le bouton du signe égal est également étendu pour remplir l'espace montré précédemment](https://www.freecodecamp.org/news/content/images/2023/08/image-124.png align="left")

Pas encore terminé, une dernière chose à faire.

Vous devez inclure un effet de survol sur tous les boutons, permettant à un utilisateur de savoir quand la souris est sur un bouton particulier. Cela améliorera l'expérience utilisateur.

Mettez à jour la balise `<style></style>` comme suit :

```html
...
<style>
    ...
.operator:hover{
	background: #FFD700;
}
.clear:hover {
	background: #FFC0CB ;
}
.equals:hover {
	background: #ADD8E6; 
}
</style>
```

![Image montrant l'effet de survol sur le signe égal](https://www.freecodecamp.org/news/content/images/2023/08/image-125.png align="left")

Maintenant, nous avons terminé avec l'interface utilisateur de la calculatrice.

Si vous avez tout fait correctement, votre code devrait ressembler à ceci :

```html
<script>
</script>

<div class="calculator">
	<div class="display"></div>
	<div class="buttons">
		<button>7</button>
		<button>8</button>
		<button>9</button>
		<button class="operator">+</button>
		<button>4</button>
		<button>5</button>
		<button>6</button>
		<button class="operator">-</button>
		<button>1</button>
		<button>2</button>
		<button>3</button>
		<button class="operator">*</button>
		<button>0</button>
		<button>.</button>
		<button class="clear">C</button>
		<button class="operator">/</button>
		<button class="equals">=</button>
	</div>
</div>

<style>
.calculator {
	display: inline-block;
	border: 1px solid #ccc;
	padding: 10px;
	border-radius: 5px;
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.display {
	font-size: 24px;
	border: 1px solid #ccc;
	height: 24px;
	padding: 10px;
	margin-bottom: 10px;
	width: 300px;
	text-align: right;
}
.buttons {
	display: grid;
	grid-template-columns: repeat(4, 75px);
	gap: 5px;
}

button {
	padding: 10px;
	font-size: 18px;
	border: none;
	cursor: pointer;
	border-radius: 5px;
	font-family: Arial, sans-serif;
	text-align: center;
}
.operator{
	border: 0px solid #A46D19;
	background: #F90;
}
.clear{
	border: 0px solid #000;
	background: red;
}
.equals{
	border: 0px solid #000;
	background: #245BE9;
	width: 320px
}
.operator:hover{
	background: #FFD700;
}
.clear:hover {
	background: #FFC0CB ;
}
.equals:hover {
	background: #ADD8E6; 
}
</style>
```

Maintenant, commençons à coder !

## Comment gérer l'interactivité

Maintenant que vous avez terminé avec l'interface utilisateur, rendons la calculatrice interactive en commençant par les boutons numériques.

Copiez et collez le code suivant dans la balise `<script></script>` dans `App.svelte` :

```javascript
<script>
	let display_number = "";
	const select = (num) => () => (display_number += num);
	const clear = () => (display_number = "");
</script>
...
...
```

* `display_number` est le nombre affiché sur l'écran de la calculatrice.
  
* `select` est la fonction qui permet à tout nombre cliqué d'apparaître sur l'écran.
  
* `clear` est la fonction qui efface l'écran, réinitialisant la valeur du nombre affiché à une chaîne vide.
  

Notez que `display_number` est un type de données chaîne. Plus tard, vous apprendrez à le convertir en un type de données numérique et à effectuer des calculs avec.

Ensuite, implémentons les fonctions `select` et `clear` dans le HTML.

Modifiez le HTML comme suit :

```html
...
<div class="calculator">
	<div class="display">{display_number}</div>
		<div class="buttons">
			<button on:click={select(7)}>7</button>
			<button on:click={select(8)}>8</button>
			<button on:click={select(9)}>9</button>
			<button class="operator" >+</button>
			<button on:click={select(4)}>4</button>
			<button on:click={select(5)}>5</button>
			<button on:click={select(6)}>6</button>
			<button class="operator" >-</button>
			<button on:click={select(1)}>1</button>
			<button on:click={select(2)}>2</button>
			<button on:click={select(3)}>3</button>
			<button class="operator">*</button>
			<button on:click={select(0)}>0</button>
			<button on:click={select(".")}>.</button>
			<button on:click={clear} class="clear">C</button>
			<button class="operator">/</button>
			<button class="equals" >=</button>
		</div>
</div>

...
```

La directive `on:click` de Svelte vous permet d'attacher un gestionnaire d'événements à un élément, de sorte que lorsque vous appelez la fonction `select` pour un élément, elle affiche le nombre de cet élément ajouté à la valeur précédente.

Le bouton `clear` a également le gestionnaire d'événements clear, pour effacer l'écran et réinitialiser à `""` à chaque appel.

Si vous avez tout fait correctement, vous devriez voir la valeur des boutons cliqués sur l'écran.

![Image montrant les nombres s'affichant sur l'écran lorsqu'ils sont cliqués.](https://www.freecodecamp.org/news/content/images/2023/08/image-126.png align="left")

Créons un gestionnaire d'événements pour effectuer une fonction d'addition et afficher le résultat. Cela servira de base pour toutes les autres opérations dans la calculatrice.

Mettez à jour la balise `<script></script>` comme suit :

```html
<script>
    ...
    let operand;
    let result;

    function addition() {
        operand = Number(display_number);
        display_number = "";
    }

    function equals() {
        display_number = Number(display_number);
        result = operand + display_number
        display_number = result.toString()
    }
</script>
...
...
```

Lorsque vous effectuez des calculs, vous pouvez avoir deux opérandes ou plus – `operand` est la variable où l'opérande précédent est stocké, tandis que `display_number` contient l'opérande actuel.

`result` est le résultat final après avoir effectué une opération arithmétique.

La fonction `addition` prend la valeur initiale affichée, la convertit en `Number` et la stocke dans la nouvelle variable `operand`, qui réinitialise `display_number` à sa valeur initiale `""`.

La fonction `equals` prend le nouveau nombre actuellement affiché, l'ajoute à `operand` et l'enregistre comme `result` final. `result` est maintenant converti en `string` et enregistré comme `display_number` pour qu'il apparaisse à l'écran.

Notez que la fonction `equals` convertit `result` en une chaîne. Lorsque vous voulez l'utiliser pour un autre calcul, la fonction `addition` gérera la conversion en `Number`.

Essayez d'effectuer une opération d'addition pour voir si vous avez bien compris.

À ce stade, `App.svelte` devrait ressembler à ceci :

```html
<script>
	let display_number = "";
	const select = (num) => () => (display_number += num);
	const clear = () => (display_number = "");

	let operand;
	let result;

	function addition() {
        	operand = Number(display_number);
        	display_number = "";
  	}

	function equals() {
        	display_number = Number(display_number);
        	result = operand + display_number
        	display_number = result.toString()
  	}
</script>

<div class="calculator">
	<div class="display">{display_number}</div>
		<div class="buttons">
			<button on:click={select(7)}>7</button>
			<button on:click={select(8)}>8</button>
			<button on:click={select(9)}>9</button>
			<button on:click={addition} class="operator" >+</button>
			<button on:click={select(4)}>4</button>
			<button on:click={select(5)}>5</button>
			<button on:click={select(6)}>6</button>
			<button class="operator" >-</button>
			<button on:click={select(1)}>1</button>
			<button on:click={select(2)}>2</button>
			<button on:click={select(3)}>3</button>
			<button class="operator">*</button>
			<button on:click={select(0)}>0</button>
			<button on:click={select(".")}>.</button>
			<button on:click={clear} class="clear">C</button>
			<button class="operator">/</button>
			<button on:click={equals} class="equals" >=</button>
		</div>
</div>

<style>
.calculator {
	display: inline-block;
	border: 1px solid #ccc;
	padding: 10px;
	border-radius: 5px;
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.display {
	font-size: 24px;
	border: 1px solid #ccc;
	height: 24px;
	padding: 10px;
	margin-bottom: 10px;
	width: 300px;
	text-align: right;
}
.buttons {
	display: grid;
	grid-template-columns: repeat(4, 75px);
	gap: 5px;
}

button {
	padding: 10px;
	font-size: 18px;
	border: none;
	cursor: pointer;
	border-radius: 5px;
	font-family: Arial, sans-serif;
	text-align: center;
}
.operator{
	border: 0px solid #A46D19;
	background: #F90;
}
.clear{
	border: 0px solid #000;
	background: red;
}
.equals{
	border: 0px solid #000;
	background: #245BE9;
	width: 320px
}
.operator:hover{
	background: #FFD700;
}
.clear:hover {
	background: #FFC0CB ;
}
.equals:hover {
	background: #ADD8E6; 
}
</style>
```

Améliorons le code pour supporter d'autres opérations – soustraction, multiplication et division :

```javascript
<script>
...
let operator;
let operators = ["+", "-", "*", "/"];

function operation(sign) {
    	operand = Number(display_number);
        operator = sign;
    	display_number = "";
  }

function equals() {
    display_number = Number(display_number);
    if (operator === "+") {
      result = operand + display_number;
    } else if (operator === "-") {
      result = operand - display_number;
    } else if (operator === "*") {
      result = operand * display_number;
    } else if (operator === "/") {
      result = operand / display_number;
    }
display_number = result.toString()
</script>
...
...
```

La fonction `addition` change en `operation`, qui supporte l'argument `sign`.

La fonction `equals` effectue des opérations basées sur la valeur de l'argument de signe dans la fonction operation.

Mettez à jour le code HTML pour ajouter des gestionnaires d'événements aux diverses opérations arithmétiques :

```html
<div class="calculator">
	<div class="display">{display_number}</div>
		<div class="buttons">
			<button on:click={select(7)}>7</button>
			<button on:click={select(8)}>8</button>
			<button on:click={select(9)}>9</button>
			<button on:click={() => operation(operators[0])} class="operator" >+</button>
			<button on:click={select(4)}>4</button>
			<button on:click={select(5)}>5</button>
			<button on:click={select(6)}>6</button>
			<button on:click={() => operation(operators[1])} class="operator" >-</button>
			<button on:click={select(1)}>1</button>
			<button on:click={select(2)}>2</button>
			<button on:click={select(3)}>3</button>
			<button on:click={() => operation(operators[2])} class="operator">*</button>
			<button on:click={select(0)}>0</button>
			<button on:click={select(".")}>.</button>
			<button on:click={clear} class="clear">C</button>
			<button on:click={() => operation(operators[3])} class="operator">/</button>
			<button on:click={equals} class="equals" >=</button>
		</div>
</div>
```

Chaque fonction prend sa valeur de signe en accédant au signe respectif dans `operators`.

Nous avons maintenant une calculatrice fonctionnelle.

Maintenant, comment gérons-nous quelque chose comme ceci ?

![L'image montre les nombres dépassant des bordures de l'affichage](https://www.freecodecamp.org/news/content/images/2023/08/image-144.png align="left")

Le problème ci-dessus est un bug où les nombres dépassent les limites de l'affichage.

Pour résoudre cette erreur, mettez à jour la div `display` comme suit :

```html
...
<div class="calculator">
	<div class="display">{display_number.length < 23? display_number: display_number.substring(0,23)}</div>
    ...
</div>
...
```

Si la longueur de `display_number` est supérieure à `22`, qui est le nombre de chiffres que l'écran d'affichage peut contenir, les vingt-deux premiers caractères sont sélectionnés.

Cela corrigera le bug ci-dessus.

## Défi

Vous pouvez étendre davantage la calculatrice en :

* Ajoutant des opérations mathématiques et scientifiques avancées.
  
* Donnant la possibilité aux utilisateurs d'utiliser leur clavier pour saisir des valeurs.
  
* Affichant les opérations arithmétiques à l'écran, avant de calculer.
  

## Conclusion

Dans ce tutoriel, vous avez appris à utiliser Svelte pour créer de l'interactivité dans une application web. Et vous avez également appris sur les gestionnaires d'événements Svelte.

Vous pouvez approfondir vos connaissances actuelles de Svelte en visitant la [documentation officielle](https://svelte.dev/docs/introduction).
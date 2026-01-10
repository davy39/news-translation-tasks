---
title: Comment créer une page de destination animée avec GSAP et TailwindCSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-12T23:56:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-animated-landing-page-with-gsap-and-tailwindcss
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/gsap-gears.jpg
tags:
- name: animation
  slug: animation
- name: JavaScript
  slug: javascript
- name: tailwind
  slug: tailwind
- name: Web Development
  slug: web-development
seo_title: Comment créer une page de destination animée avec GSAP et TailwindCSS
seo_desc: 'By Paul Akinyemi

  Animations are a crucial part of any great website. Why? When done well, animations
  vastly improve the user experience of any site, as they help make sites fun and
  intuitive to use.

  This article will show you how to build an animated...'
---

Par Paul Akinyemi

Les animations sont une partie cruciale de tout site web exceptionnel. Pourquoi ? Lorsque elles sont bien réalisées, les animations améliorent considérablement l'expérience utilisateur de tout site, car elles aident à rendre les sites amusants et intuitifs à utiliser.

Cet article vous montrera comment créer une page de destination animée avec l'aide d'une bibliothèque JavaScript appelée [GSAP](https://greensock.com/docs/v3).

GSAP est un kit d'outils magnifique pour créer des animations. Il a été utilisé dans environ **11 000 000** de sites web jusqu'à présent, offre d'excellentes performances et prend en charge les incohérences des navigateurs pour vous, parmi d'autres [grandes fonctionnalités](https://greensock.com/why-gsap).

La page de destination que vous allez créer a été inspirée par ce [post Twitter](https://twitter.com/Ayoolafelix/status/1479157194029514754?s=20). Voici à quoi elle ressemblera lorsque vous aurez terminé :

%[https://vimeo.com/697946646]

Vous pouvez consulter une démonstration en direct [ici](https://gsap-landing-psi.vercel.app/).

## Public visé

Cet article suppose que vous êtes un développeur web ayant une compréhension de base du HTML, du CSS et du JavaScript, ainsi qu'une certaine familiarité avec [TailwindCSS](https://tailwindcss.com/docs/installation), NPM et l'utilisation du terminal.

L'article suppose également que vous utiliserez un terminal Linux. Si vous utilisez Windows à la place, consultez [cet article](https://www.geeksforgeeks.org/linux-vs-windows-commands/) pour voir l'équivalent des commandes Windows cmd des commandes de terminal utilisées dans l'article.

Connaître GSAP n'est pas un prérequis, car cet article fournit une introduction aux fonctionnalités de la bibliothèque utilisées dans le tutoriel. Gardez simplement à l'esprit que cela n'est pas destiné à être un guide complet de la bibliothèque.

## Aperçu de l'article

Cet article se compose des sections suivantes :

* Comment configurer le projet
* Écrire le balisage
* Une brève introduction à GSAP
* Ajout d'animation à la page
* Conclusion

## Comment configurer le projet

Avant de commencer à créer la page de destination, il y a quelques choses que vous devez mettre en place.

Dans cette section, vous allez :

* Configurer le répertoire où votre projet résidera.
* Configurer GSAP et TailwindCSS.
* Importer une police.
* Configurer un serveur de développement simple.

### Comment configurer le répertoire du projet

Commencez par exécuter les commandes suivantes dans votre terminal :

```sh
mkdir gsap-landing
cd gsap-landing
mkdir build src
mkdir build/assets build/static
```

Ce code devrait créer une arborescence de dossiers qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/gsap-landing-structure.png)
_structure de répertoire pour le projet_

### Comment configurer GSAP

Pour installer GSAP, créez un fichier dans build appelé `index.html`, puis placez le code suivant à l'intérieur :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.10.2/gsap.min.js"></script>
    <title>Orfice</title>
</head>
<body>
    
</body>
</html>
```

Cela crée un document HTML de base et importe GSAP via la balise script dans le head.

### Comment configurer TailwindCSS

Pour installer TailwindCSS, assurez-vous d'être dans le répertoire racine de votre projet, puis exécutez les commandes suivantes dans votre terminal :

```sh
npm install tailwindcss
npx tailwind init
```

Cela devrait créer trois nouveaux fichiers dans la racine de votre projet : `package.json`, `package-lock.json` et `tailwind.config.js`.

Ensuite, créez un fichier dans le dossier `src` appelé `input.css`, et placez le code suivant à l'intérieur :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Retournez à la racine du projet et remplacez le contenu de `tailwind.config.js` par le suivant :

```js
module.exports = {
  content: [
  "./build/**/*.{html,js}"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

```

Après cela, ouvrez votre fichier `package.json` et remplacez son contenu par le suivant :

```json
{
  "scripts": {
    "build-css": "npx tailwindcss -i ./src/input.css -o ./build/static/output.css --watch"
  },
  "dependencies": {
    "tailwindcss": "^3.0.23"
  }
}

```

Maintenant, ouvrez votre terminal et exécutez cette commande :

```sh
npm run build-css
```

Cette commande est responsable de la création et de la mise à jour du fichier : `build/static/output.css`, qui est l'endroit où le style de votre page de destination résidera, vous devez donc le laisser fonctionner dans sa propre fenêtre de terminal jusqu'à ce que vous ayez terminé le tutoriel.

Ensuite, liez le CSS à votre page de destination en ajoutant le code suivant à `build/index.html`, juste au-dessus de la balise script qui importe GSAP :

```html
<link rel="stylesheet" href="static/output.css">
```

Cela conclut la configuration pour TailwindCSS.

### Comment importer la police

Remplacez le head de `build/index.html` par le suivant :

```html
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="static/output.css">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.10.2/gsap.min.js"></script>
	<title>Orfice</title>
</head>
```

Maintenant, appliquez la police à votre CSS.

Ouvrez `src/input.css`, et ajoutez le code suivant à la fin :

```css

@layer base {
    body {
        @apply overflow-hidden h-screen;
        font-family: 'Be Vietnam Pro', sans-serif;
    }
}
```

### Comment configurer le serveur

Pour configurer votre serveur de développement, ouvrez une nouvelle fenêtre de terminal, naviguez jusqu'à la racine de votre projet, puis exécutez le code suivant :

```sh
npm install --save-dev live-server
```

C'est tout ce que vous avez à faire ! Pour démarrer votre serveur, exécutez la commande suivante dans votre terminal :

```sh
live-server build
```

Tant que la commande `live-server` est en cours d'exécution, elle servira `build/index.html` à [localhost:8080](localhost:8080), et rafraîchira automatiquement la page lorsque vous apporterez des modifications au projet.

## Comment écrire le balisage

Jetez un coup d'œil à ce à quoi votre page devrait ressembler à la fin de l'animation :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/gsap-landing-structure-outline-1.jpg)
_contour structurel de la page de destination_

Appelons la section bleue la barre de navigation, la section jaune l'en-tête et l'image le préchargeur.

Votre prochaine étape consiste à construire chacune de ces sections dans l'ordre où elles apparaissent sur la page.

### Comment construire la barre de navigation

Vous aurez besoin d'une image dans votre barre de navigation, alors allez à [ce lien](https://raw.githubusercontent.com/Morgenstern2573/gsap-landing/master/build/assets/logo.jpg) et téléchargez-la. Enregistrez-la dans `build/assets`, avec le nom `logo.jpg`.

Votre barre de navigation sera divisée en trois sections :

* le logo à gauche
* un `div` au milieu
* un bouton à droite

Ouvrez `build/index.html`, et ajoutez le code suivant en haut de la balise body :

```html
<nav>
    <img src="assets/logo.jpg" alt="logo">
    <div class="nav-links">
        <a href="#">Accueil</a>
        <a href="#">Boutique</a>
        <a href="#">Contact</a>
        <a href="#">Témoignages</a>
    </div>
    <button class="cta">Travaillons ensemble</button>
</nav>
```

Ensuite, vous ajouterez de l'espacement et de l'alignement à votre barre de navigation avec un peu de CSS.

Ouvrez `src/input.css`, et ajoutez ce qui suit à la fin de la section `@layer base` :

```css
nav {
        @apply flex p-4 md:py-8 md:px-4 lg:p-12;
        @apply justify-center items-center gap-4;
    }
```

Puis ajoutez ceci à la fin du fichier, _en dehors_ de `@layer base` :

```css
@layer components {
	nav > img {
        width: 120px;
    }

    nav a {
        @apply underline;
    }

    .cta {
        @apply rounded bg-black text-white py-2 px-4;
    }

    nav .cta {
        @apply hidden md:inline-block;
    }

    .nav-links {
        @apply hidden md:flex gap-4 lg:gap-8 lg:mx-16 xl:mx-20;
    }
}
```

Après avoir fait cela, votre page devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-14.png)
_capture d'écran de la barre de navigation_

Maintenant que vous avez construit la barre de navigation, cachez-la pour l'instant afin de pouvoir l'animer en visibilité plus tard.

Retournez à `index.html`, et ajoutez une classe `opacity-0` à la `nav` :

```html
<body>
    <nav class="opacity-0">
		<!-- laissez le reste du code tel quel -->
    </nav>
</body>
```

### Comment construire l'en-tête

Vous allez implémenter l'en-tête en construisant trois rangées.

La première rangée est composée de texte en gras et agrandi, et d'un paragraphe de texte normal que vous allez cacher lorsque l'écran est plus petit que 768px (sur les appareils mobiles).

La deuxième rangée est similaire à la première : du texte en gras et agrandi, décalé vers la droite, et un SVG rotatif à la place du paragraphe. Le SVG sera également caché sur les appareils mobiles.

La troisième rangée ne sera visible que sur les appareils mobiles et contient un paragraphe de texte et un bouton.

Placez le code suivant dans `build/index.html`, après la balise nav :

```html
<header>
		<div class="row first-row">
            <p class="bold-text">
                Les Possibilités
            </p>

            <p class="copy">
                <span>
                    Nous croyons que les espaces de travail
                </span>
                <span>
                    devraient être conviviaux et pratiques.
                </span>
                <span>
                    Voici une invitation à découvrir comment
                </span>
                <span>
                    nous concevons les espaces de travail chez curved.
                </span>
            </p>
		</div>

		<div class="row second-row">
			<p class="bold-text">
				Des Espaces de Travail
			</p>
			
			<p class="round-text" >
				<svg xmlns="http://www.w3.org/2000/svg" width="106" height="106" viewBox="0 0 106 106" fill="none">
					<path d="M0,53a53,53 0 1,0 106,0a53,53 0 1,0 -106,0" id="curve"></path>
					<text width="314.1593">
							<textPath alignment-baseline="top" xlink:href="#curve">
									espace de travail bureau . espace de travail bureau . espace de travail bureau .
							</textPath>
					</text>
					<defs>
					</defs>
				</svg>
			</p>
		</div>

		<div class="row mobile-row">
			<p class="copy">
				<span>
					Nous croyons que les espaces de travail
				</span>
				<span>
					devraient être conviviaux et pratiques.
				</span>
				<span>
					Voici une invitation à découvrir comment
				</span>
				<span>
					nous concevons les espaces de travail chez curved.
				</span>
			</p>

			<button class="cta">Travaillons ensemble</button>
		</div>
	</header>
```

Maintenant que la structure est en place, il est temps pour les effets visuels.

Vous allez définir une classe d'utilitaire personnalisée appelée `animate-spin-slow`, qui applique une animation de rotation lente à l'élément sur lequel elle est utilisée.

Remplacez le contenu de `tailwind.config.js` par le suivant :

```js
module.exports = {
  content: [
    "./build/**/*.{html,js}"
  ],
  theme: {
    extend: {
      animation: {
        'spin-slow': 'spin 10s linear infinite',
      }
    },
  },
  plugins: [],
}

```

Ensuite, vous allez écrire le style pour l'en-tête lui-même.

Placez le code suivant dans `src/input.css`, à l'intérieur de `@layer components` :

```css
    .row {
        @apply flex p-4 justify-center md:justify-start;
        @apply items-center gap-4 md:gap-8;
        @apply lg:gap-12 text-center md:text-left;
    }

    .first-row {
        @apply md:pt-8 lg:pt-16;
    }

    .bold-text {
        @apply font-bold text-5xl lg:text-6xl xl:text-8xl;
    }

    .copy {
        @apply font-medium;
    }

    .second-row .bold-text {
        @apply lg:pl-16 xl:pl-36
    }

    .first-row .copy {
        @apply hidden md:flex md:flex-col;
    }

    .round-text {
        @apply hidden md:block pl-20 lg:pl-40;
    }

    .round-text svg{
        @apply animate-spin-slow;
    }
    
    .round-text textPath {
        @apply text-xs fill-black;
    }

    .mobile-row {
        @apply flex md:hidden flex-col py-4;
    }


```

À ce stade, votre page devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-16.png)
_capture d'écran de l'en-tête_

Votre barre de navigation devrait être présente sur la page, mais invisible, ce qui est la cause de l'espace blanc en haut.

Maintenant, cachez tous les blocs dans chaque rangée, en leur donnant une classe `opacity-0`. Modifiez `index.html` pour qu'il ressemble à ceci :

```html
<header>
		<div class="row first-row">
				<p class="bold-text opacity-0">
					<!-- laissez tel quel -->
				</p>

				<p class="copy opacity-0">
					<!-- laissez tel quel -->
				</p>
		</div>

		<div class="row second-row">
			<p class="bold-text opacity-0">
				<!-- laissez tel quel -->
			</p>
			
			<p class="round-text opacity-0" >
				<!-- laissez tel quel -->
			</p>
		</div>

		<div class="row mobile-row">
			<p class="copy opacity-0">
				<!-- laissez tel quel -->
			</p>

			<button class="cta opacity-0"><!-- laissez tel quel --></button>
		</div>
	</header>
```

Et vous avez terminé avec l'en-tête !

### Comment construire le préchargeur

Tout d'abord, téléchargez l'image depuis [ce lien](https://raw.githubusercontent.com/Morgenstern2573/gsap-landing/master/build/assets/office.jpg). Enregistrez-la dans `build/assets` sous le nom `office.jpg`.

Maintenant que vous avez l'image, vous allez écrire le balisage réel.

Le préchargeur va consister en une div avec l'image à l'intérieur, et une div intérieure pour servir de superposition.

Placez le code suivant dans `index.html`, à l'extérieur de la balise header :

```html
<div class="pre-loader">
    <img src="assets/office.jpg" alt="un bureau">
    <div class="overlay"></div>
</div>
```

Maintenant, vous allez positionner le préchargeur au milieu de la page et ajouter un style à la superposition.

Placez le code suivant dans `src/input.css`, à l'intérieur de `@layer components` :

```css
.pre-loader {
        @apply absolute z-10;
        width: 40vw;
        top: calc(50% - (0.668 * 20vw));
        left: calc(50% - 20vw);
    }

    .pre-loader > .overlay {
        @apply absolute inset-x-0 bottom-0;
        @apply top-full bg-black bg-opacity-10 -z-0;
    }
```

Après cela, votre page web devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-15.png)
_capture d'écran du préchargeur_

## Une brève introduction à GSAP

Dans cette section, nous allons rapidement passer en revue quelques fonctionnalités de GSAP. N'hésitez pas à sauter cette partie si vous avez déjà une certaine expérience avec GSAP.

Selon la documentation de GSAP :

> GSAP est un manipulateur de propriétés
>
> L'animation se résume finalement à changer les valeurs des propriétés plusieurs fois par seconde, faisant apparaître quelque chose en mouvement, en fondu, en rotation, etc. GSAP capture une valeur de départ, une valeur de fin, puis interpolé entre elles 60 fois par seconde.
>
> Par exemple, changer la coordonnée `x` d'un objet de 0 à 1000 sur une durée de 1 seconde le fait se déplacer rapidement vers la droite. Changer progressivement l'`opacity` de 1 à 0 fait disparaître un élément. Votre travail en tant qu'animateur est de décider quelles propriétés changer, à quelle vitesse et le style du mouvement. (Source : [Qu'est-ce que GSAP](https://greensock.com/get-started/#what-is-gsap) ?)

Pour paraphraser : au cœur de GSAP, il s'agit d'une bibliothèque qui vous permet de changer en douceur n'importe quelle propriété d'un objet entre deux points définis sur une certaine période.

GSAP a beaucoup de fonctionnalités, mais nous nous concentrerons sur celles dont vous aurez besoin pour construire votre page de destination. Vous allez utiliser :

* `gsap.to()`
* `gsap.set()`
* `gsap.fromTo()`
* Les timelines

### Méthode gsap.to()

Cette méthode indique à GSAP d'animer une cible de son état actuel à un état final spécifié.

La méthode prend deux arguments :

* La cible de l'animation. Il peut s'agir soit d'un objet brut, d'un tableau d'objets, soit d'une chaîne contenant un sélecteur CSS (pour cibler un élément DOM).
* Un objet qui liste : quelles propriétés vous animez, leurs valeurs finales, et des propriétés spéciales qui affectent l'animation elle-même (comme la définition de la durée ou d'un délai).

Voici un exemple :

```js
gsap.to('#object', {top: '75%', duration: 2})
```

Ce code indique à GSAP de changer la propriété top de l'élément DOM avec un id de object à une valeur de 75%, et de faire durer le changement deux secondes.

### Méthode gsap.set()

Cette méthode fonctionne presque exactement de la même manière que `gsap.to()`. Elle anime également la cible vers un état final donné.

La différence est que `gsap.set()` crée une animation avec une durée de zéro seconde, définissant instantanément les propriétés de la cible à leurs valeurs données.

Voici un exemple :

```js
gsap.set('#object', {top: '75%'})
```

Une fois ce code exécuté, la propriété top de `#object` devient 75%.

### Méthode gsap.fromTo()

La méthode `fromTo()` indique à GSAP d'animer l'objet cible d'un état de départ que nous fournissons à un état final que nous fournissons également. Lorsque la méthode s'exécute, la cible sera instantanément définie à l'état de départ, puis animée vers l'état final.

La méthode `fromTo()` accepte trois arguments :

* L'argument cible.
* Un objet qui contient les propriétés que vous souhaitez que la cible ait au début de l'animation.
* Un objet qui contient les propriétés que vous souhaitez que la cible ait à la fin de l'animation.

Toutes les propriétés spéciales qui contrôlent l'animation elle-même ne peuvent aller que dans le dernier argument, l'objet qui contient l'état final.

Voici un exemple :

```js
gsap.fromTo('#object', {top: '75%'}, {top: '33%', delay: 3})
```

### Timelines

Une timeline GSAP est un objet spécial qui agit comme un conteneur pour plusieurs animations. Son travail est de rendre le séquençage des animations liées beaucoup plus facile.

Voici comment fonctionnent les timelines : vous créez une timeline avec `gsap.timeline()`, puis vous ajoutez des animations avec les mêmes méthodes que nous avons discutées jusqu'à présent.

Les timelines permettent également de spécifier des propriétés spéciales par défaut pour chaque animation dans la timeline, en les passant à `gsap.timeline()` en tant que propriétés d'un objet.

Exemple :

```js
let timeLine = gsap.timeline({defaults: {duration: 1}})

timeLine.set('#object', {top: '75%'})
timeLine.to('#object', {top: '50%', delay: 0.5})
timeLine.fromTo('#object', {top: '60%'}, {top: '25%', delay: 0.5})
```

C'est tout ce que vous devez savoir sur GSAP pour comprendre le reste de ce tutoriel.

## Comment ajouter de l'animation

Maintenant que tout le balisage est en place, il est enfin temps d'ajouter l'animation.

Commencez par créer un nouveau fichier dans `build/static` appelé `script.js`.

C'est ce qui contiendra tout votre JavaScript d'animation. Ensuite, liez `script.js` à votre HTML en ajoutant une balise script à `index.html` juste au-dessus de la balise de fermeture body, comme ceci :

```html
<body>
	<!-- laissez tel quel -->
    <script src="static/script.js"></script>
</body>

```

La première chose que vous allez animer est votre préchargeur. Vous allez écrire du code pour augmenter lentement la hauteur de la superposition, puis pour augmenter sa largeur tout en la déplaçant vers le bas et vers la gauche.

Ajoutez ce qui suit à `static/script.js` :

```js
const timeLine = gsap.timeline({defaults: {duration: 1}})

timeLine.to('.pre-loader > .overlay', {top: '75%'})
timeLine.to('.pre-loader > .overlay', {top: '50%', delay: 0.5})
timeLine.to('.pre-loader > .overlay', {top: '25%', delay: 0.5})
timeLine.to('.pre-loader > .overlay', {top: '0', delay: 0.5})
timeLine.to('.pre-loader', {width: '80vw', left:0, top: '50%'})
timeLine.set('.pre-loader', {'z-index': -20})

```

Prenons un moment pour décomposer ce code. Il fait quelques choses :

* Il crée une timeline pour nos animations, en définissant une durée par défaut de 1 seconde.
* Il utilise `gsap.to()` pour augmenter la hauteur de la superposition en ajustant la propriété `top`.
* Il utilise `gsap.to()` pour augmenter la largeur du préchargeur, l'aligner avec le bord gauche de l'écran et augmenter la largeur.
* Il utilise `gsap.set()` pour définir immédiatement le `z-index` à -20, afin qu'il ne couvre aucun de notre texte.

Ensuite, c'est au tour de la barre de navigation. Vous voulez créer un effet où il semble que la barre de navigation glisse depuis le haut de l'écran et devienne progressivement visible en même temps.

Faites cela en ajoutant le code suivant à la fin de `script.js` :

```js
timeLine.fromTo('nav', {y:-100}, {y:0, opacity:1})
```

Ce code utilise `gsap.fromTo()` pour définir une `transalateY(-100px)` sur l'élément, puis l'anime à sa position normale et à une opacité totale.

Vous allez maintenant animer l'en-tête, pièce par pièce.

La première chose à faire est d'animer le texte en gras de la première rangée. Vous allez implémenter exactement le même type d'animation, mais il va glisser depuis le bas, pas depuis le haut.

Ajoutez ceci à la fin de `script.js` :

```js
timeLine.fromTo('.first-row .bold-text', {y:100}, {y:0, opacity:1}, "<")
```

Le dernier argument, `<`, indique à GSAP de démarrer cette animation en même temps que l'animation précédente dans la timeline. Comme les deux animations ont la même durée, cela a pour effet de les exécuter simultanément.

Ensuite, animez le texte en gras de la deuxième rangée de la même manière, mais omettez l'argument `<`, comme ceci :

```js
timeLine.fromTo('.second-row .bold-text', {y:100}, {y:0, opacity:1, delay:0.5})
```

Les parties restantes de l'en-tête sont intéressantes, car les éléments que vous souhaitez animer ensuite dépendent du fait que le site est consulté sur un appareil mobile ou non.

Si le site est sur mobile, ce que vous voulez animer sont les éléments de la troisième rangée. Mais si ce n'est pas le cas, vous animez les parties restantes des première et deuxième rangées.

Vous allez résoudre ce problème en utilisant la [méthode window.matchMedia()](https://developer.mozilla.org/en-US/docs/web/api/window/matchmedia).

Elle prend une requête média comme argument et vous permet de vérifier si le navigateur correspond à cette requête média ou non.

Ajoutez ce code à la fin de `script.js` :

```js
const isMobile = !(window.matchMedia('(min-width: 768px)').matches)

if (isMobile) {
    timeLine.fromTo('.mobile-row .copy', {y:100}, {y:0, opacity:1, delay:0.5})
    timeLine.fromTo('.mobile-row .cta', {y:100}, {y:0, opacity:1, delay:0.5})
} else {
    timeLine.fromTo('.first-row .copy', {y:100}, {y:0, opacity:1, delay:0.5})
    timeLine.set('.round-text', {opacity:1, delay:0.5})
}
```

Passons en revue cela. Le code que vous venez d'ajouter :

* Détermine si la largeur de la fenêtre est inférieure à 768px.
* Si c'est le cas, le code fait glisser le paragraphe de la rangée mobile vers le haut, suivi du bouton.
* Si ce n'est pas le cas, il fait glisser le paragraphe de la première rangée vers le haut, puis rend le SVG visible.

Et cela complète votre page de destination !

## Conclusion

Dans cet article, vous avez appris à utiliser les bases de GSAP pour créer quelques animations cool. Si vous souhaitez en savoir plus sur GSAP et les choses incroyables que vous pouvez faire avec, visitez [ce lien](https://greensock.com/learning).

Vous pouvez trouver la base de code complète [ici](https://github.com/Morgenstern2573/gsap-landing-article).

Si vous avez aimé cet article, suivez-moi sur [Twitter](https://twitter.com/apexPaul09) pour savoir quand j'écris quelque chose de nouveau !
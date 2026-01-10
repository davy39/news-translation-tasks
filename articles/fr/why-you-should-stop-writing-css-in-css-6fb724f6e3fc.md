---
title: Pourquoi vous devriez arrêter d'écrire du CSS en "CSS"
subtitle: ''
author: Saheed Oladele
co_authors: []
series: null
date: '2019-04-08T16:23:33.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-stop-writing-css-in-css-6fb724f6e3fc
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca37a740569d1a4ca5bd6.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Pourquoi vous devriez arrêter d'écrire du CSS en "CSS"
seo_desc: 'CSS is fun to write, but it can quickly get complicated. A typical example
  is having to scroll upwards to check the hexadecimal values of the colors you are
  using.

  Typing a class or id selector several times within a single CSS file, or having
  to cop...'
---

Le CSS est amusant à écrire, mais cela peut rapidement devenir compliqué. Un exemple typique est de devoir faire défiler vers le haut pour vérifier les valeurs hexadécimales des couleurs que vous utilisez.

Taper un sélecteur de classe ou d'identifiant plusieurs fois dans un seul fichier CSS, ou devoir copier et coller chaque préfixe de support de navigateur dans votre code à chaque fois pour la compatibilité multi-navigateurs peut rendre votre fichier CSS plus difficile à maintenir.

![Image](https://cdn-media-1.freecodecamp.org/images/863sGFar-HXTATzeqGsA3n-jlIMgrFFlNeBS)
_Un exemple de code CSS_

```css
// compatibilité multi-navigateurs

-webkit-transform: $property
-ms-transform: $property
transform: $property

display: -ms-flexbox;
display: flex;

-ms-flex-wrap: wrap;
flex-wrap: wrap;
```

La prochaine fois que vous voulez écrire du CSS, essayez de ne pas "écrire" en CSS du tout.

Au lieu de cela, essayez d'utiliser des préprocesseurs CSS.

### Qu'est-ce que les préprocesseurs ?

Selon [MDN](https://developer.mozilla.org/en-US/docs/Glossary/CSS_preprocessor), un **préprocesseur CSS** est un programme qui vous permet de générer du CSS à partir de la syntaxe unique du préprocesseur. Vous écrivez votre code CSS dans ceux-ci, puis générez un fichier CSS correspondant pour styliser votre HTML.

Certains des préprocesseurs populaires à utiliser incluent [SASS/SCSS](http://sass-lang.com/), [LESS](http://lesscss.org/), [Stylus](http://stylus-lang.com/), et [PostCSS](http://postcss.org/). J'utilise SASS, donc mes illustrations dans cet article sont en SASS.

Bien que les préprocesseurs aient leur propre syntaxe, ils sont assez faciles à maîtriser, avec seulement quelques différences par rapport à l'écriture de CSS vanilla.

### 6 raisons pour lesquelles vous devriez ARRÊTER d'écrire du CSS en "CSS"

La syntaxe des préprocesseurs offre des fonctionnalités supplémentaires qui permettent les éléments suivants :

#### 1. Variables

Les préprocesseurs utilisent des variables pour stocker des valeurs réutilisables. Vous pouvez stocker n'importe quel type de style dans une variable. Cela peut être `color`, `font-family`, ou même des valeurs pour votre `padding`, `margin`, `width`, ou `height`.

Lorsque vous définissez la variable, il n'est pas nécessaire de se souvenir de la valeur. Rappelez la variable chaque fois que vous avez besoin de la valeur stockée.

```css
// variables

$my_font: Helvetica, sans-serif
$my-color: #333

body  
    font: 100% $my-font
    color: $my-color
```

#### **2. Imbrication**

Nous écrivons du HTML en imbriquant des éléments enfants dans des éléments parents comme les éléments `ul`, `li`, et `a` dans un `nav`. Lorsque vous utilisez des préprocesseurs, vous n'avez pas à écrire le sélecteur CSS parent (la balise `nav` dans ce cas) à chaque fois.

Passez à la ligne suivante et tapez l'élément enfant comme montré ci-dessous :

```css
// barre de navigation

nav
  	ul
        margin: 0    
        padding: 0    
        list-style: none  

	li    
		display: inline-block
 
 	a    
		display: block
		padding: 6px 12px
		text-decoration: none
```

Les sélecteurs `ul`, `li`, et `a` sont imbriqués à l'intérieur du sélecteur `nav`.

Certains développeurs pensent que cela arrive dans CSS. Mais hey, ce n'est pas encore là, cela ne fait pas de mal de s'y habituer avant son arrivée dans CSS. :)

#### **3. Import**

Les préprocesseurs améliorent l'`import` existant de CSS.

`import` vous permet de diviser votre CSS en fichiers plus petits pour une meilleure lisibilité et maintenabilité. Il prend le fichier que vous importez et l'ajoute au fichier dans lequel vous importez.

```css
// _reset.sass

html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote    
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
```

Vous pouvez importer le fichier `reset.sass` comme montré ci-dessous :

```css
// main.sass

@import reset
    
body
    font: 100% Helvetica, sans-serif
    background-color: #efefef
```

Cela signifie que vous pouvez avoir le fichier `main.sass`, puis d'autres comme `reset.sass`, `header.sass`, `footer.sass`, ou `variables.sass`. Vous `importez` d'autres fichiers dans le `main.sass` en utilisant la syntaxe `import` du préprocesseur.

Le fichier importé est ensuite ajouté à la fin du fichier `main.sass` (le fichier dans lequel vous avez importé).

#### **4. Extend**

`extend` stocke un style ou une série de styles dans une classe. Cela fonctionne comme une variable. Il utilise une classe de placeholder `(%)` pour indiquer au compilateur de ne pas imprimer la classe sauf si elle est étendue.

Lorsque la classe est étendue dans un élément, alors l'élément hérite de toutes les propriétés de style sauvegardées dans la classe de placeholder. Vous pouvez toujours ajouter un style unique si nécessaire.

```css
// Ce CSS sera imprimé car %message-shared est étendu.
// "%" illustre la classe de placeholder

%message-shared
    border: 1px solid #ccc
    padding: 10px
    color: #333

// Ce CSS ne sera pas imprimé car %equal-heights n'est jamais étendu.

%equal-heights  
    display: flex
    flex-wrap: wrap

// Cela étend sans ajouter d'autre style

.message
	@extend %message-shared
        
// Ceux-ci étendent avec un style supplémentaire (vert, rouge, jaune)

.success
	@extend %message-shared
	border-color: green

.error  
	@extend %message-shared  
	border-color: red

.warning  
	@extend %message-shared
	border-color: yellow
```

Cela permet de gagner du temps et de garder votre CSS propre.

#### **5. Opérations arithmétiques**

Les préprocesseurs vous permettent d'effectuer des opérations arithmétiques dans votre CSS. Ils supportent les opérateurs mathématiques standard comme `+`, `-`, `*`, `/`, et `%`.

```css
// Opérations arithmétiques
.container  
    width: 100%

article[role="main"]  
    float: left
	width: 600px / 960px * 100%
```

#### **6. Minification**

La minification réduit la taille de votre fichier pour accélérer le temps de chargement. Elle supprime les espaces blancs et les caractères inutiles de votre code (CSS dans ce cas).

Les préprocesseurs vous permettent de générer une version compressée de votre CSS. Je sais qu'il existe plusieurs autres façons de générer cela, mais hey, c'est aussi cool. :)

### **Conclusion**

Devoir utiliser le terminal lors de la compilation est le principal inconvénient de l'utilisation des préprocesseurs. Cependant, il existe d'autres façons de compiler, comme l'utilisation de [CodeKit](https://codekitapp.com/), [Compass.app](http://compass-style.org/), et [GhostLab](https://www.vanamco.com/ghostlab/). Il existe maintenant certains plugins dans l'éditeur (comme Live Sass Compiler sur Visual Studio Code) pour aider avec cela également.

Essayez n'importe quel préprocesseur de votre choix. Je parie que vous n'écrirez plus jamais de CSS en "CSS". Si vous avez utilisé des préprocesseurs, partagez votre expérience dans les commentaires.

Peace out et bon codage !
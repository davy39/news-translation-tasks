---
title: Comment utiliser les sélecteurs CSS pour styliser votre page web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-19T23:17:21.000Z'
originalURL: https://freecodecamp.org/news/use-css-selectors-to-style-webpage
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/CSS-Selectors.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les sélecteurs CSS pour styliser votre page web
seo_desc: 'By Peter Lynch

  CSS selectors are one of the most important parts of CSS. They give you the ability
  to target HTML elements on your web page that you want to style.

  Without CSS selectors, you wouldn''t be able to style your page to look how you
  want.

  T...'
---

Par Peter Lynch

Les sélecteurs CSS sont l'une des parties les plus importantes de CSS. Ils vous donnent la possibilité de cibler les éléments HTML de votre page web que vous souhaitez styliser.

Sans les sélecteurs CSS, vous ne pourriez pas styliser votre page pour qu'elle ressemble à ce que vous voulez.

Heureusement, les sélecteurs CSS existent depuis un certain temps, et vous pouvez styliser les éléments de votre page comme vous le souhaitez. 

Mais si vous voulez vraiment libérer la puissance de CSS et créer des éléments incroyables, vous devez comprendre ce que vous pouvez faire avec les sélecteurs CSS. Plus précisément, vous devez comprendre les sélecteurs CSS de base avant de passer aux sélecteurs CSS avancés.

Cet article examinera les deux. À la fin, vous serez sur la bonne voie pour libérer la puissance des sélecteurs CSS afin de créer vos propres éléments incroyables. Commençons donc par examiner ce que sont les sélecteurs CSS.

## Que sont les sélecteurs CSS ?

Si vous avez déjà écrit du CSS, vous avez probablement déjà vu un sélecteur CSS. Ils constituent la première partie d'une règle CSS. Vous utilisez les sélecteurs CSS pour sélectionner les éléments HTML que vous souhaitez styliser.

En CSS, les sélecteurs sont définis par la spécification des sélecteurs CSS. Cela signifie que chaque sélecteur doit être [supporté](https://www.w3.org/TR/selectors-3/#selectors) par le navigateur pour fonctionner réellement.

Les sélecteurs CSS ont tendance à être divisés en cinq catégories différentes. Cet article va les examiner en deux catégories clés : de base et avancés. Voici les cinq catégories :

1. Sélecteurs simples
2. Sélecteurs de combinaison
3. Sélecteurs de pseudo-classes
4. Sélecteurs de pseudo-éléments
5. Sélecteurs d'attributs

Pour devenir bon dans un domaine, il faut en comprendre les bases, alors commençons par là.

# Sélecteurs CSS de base

Vous avez probablement vu de nombreux types de sélecteurs CSS – les sélecteurs CSS fondamentaux qui suffisent pour commencer à construire des pages web élégantes. Examinons chacun des sélecteurs CSS de base pour nous assurer de bien comprendre leur rôle.

## Sélecteur d'élément (type) CSS

Le sélecteur d'élément CSS sélectionne les éléments HTML en fonction du nom de l'élément. En HTML, les noms d'éléments sont des choses comme `h1`, `p`, ou des noms sémantiques comme `article` ou `footer`. Par conséquent, les sélecteurs d'éléments sélectionnent tous les éléments HTML portant le nom que vous sélectionnez.

Regardons un exemple de sélecteur CSS pour les sélecteurs d'éléments :

```css
/* sélection de tous les éléments h3 */
h3 {
	text-align: center;
	color: blue;
}

/* sélection de tous les éléments article */
article {
	font-size: 14px;
	line-height: 1.1px;
}

```

Dans l'exemple ci-dessus, nous avons sélectionné tous les éléments de la page qui sont de type `h3` et `article` et avons appliqué des styles à ces éléments.

Les sélecteurs d'éléments vous aident à garder votre code simple en appliquant le style à tous les éléments d'une page de ce type. Cela signifie que vous n'avez à suivre vos styles pour ces éléments qu'à un seul endroit.

## Sélecteur d'ID CSS

Le sélecteur d'ID sélectionne les éléments HTML qui ont un attribut ID correspondant au sélecteur. Comme vous ne pouvez pas avoir plus d'un élément avec le même ID dans un document HTML, ce sélecteur vous permet de sélectionner un élément individuel. Cela signifie que le style sur l'élément sélectionné sera unique.

Pour sélectionner un élément avec un ID spécifique, vous utilisez un caractère `#` (dièse) suivi de l'ID de l'élément HTML. Dans ce cas, cela ressemblerait à ceci `#id-name`.

Regardons un exemple de sélecteur CSS pour le sélecteur d'ID.

```css
#projects-flex-container {
	width: 90vw;
	display: flex;
}

```

Dans l'exemple ci-dessus, nous avons sélectionné l'élément HTML individuel avec l'ID `#projects-flex-container` et lui avons appliqué un style. Ce style ne s'appliquera qu'à cet élément individuel.

Une chose à noter, cependant, est que vous devriez être prudent lors de l'utilisation des sélecteurs d'ID. Comme les sélecteurs d'ID ne peuvent pas être réutilisés sur d'autres éléments, vous devriez vous demander si vous avez réellement besoin d'utiliser un sélecteur d'ID pour cibler l'élément.

## Sélecteur de classe CSS

Le sélecteur de classe sélectionne les éléments HTML qui ont un attribut de classe correspondant au sélecteur. Le sélecteur de classe est utile pour cibler plusieurs éléments, comme des cartes ou des images auxquelles vous souhaitez appliquer des styles identiques.

Pour sélectionner un élément avec une classe spécifique, vous utilisez un caractère `.` (point) suivi du nom de la classe.

Regardons un exemple de sélecteur CSS pour le sélecteur de classe.

```css
.project-card {
	color: #badA55;
	padding: 5px;
	border-radius: 5px;
}

```

Dans l'exemple ci-dessus, nous avons sélectionné tous les éléments avec le nom de classe `project-card` en utilisant le sélecteur de classe CSS. Tous les éléments avec la classe `project-card` se verront appliquer les styles listés.

## Sélecteur universel

Le sélecteur universel sélectionne tous les éléments HTML. Cela signifie chaque élément de votre page, des titres au pied de page. Vous l'utiliserez souvent pour rendre les marges et le rembourrage de la page cohérents ou pour effectuer ce que l'on appelle une remise à zéro.

La syntaxe pour le sélecteur universel est le caractère `*` (astérisque).

```css
* {
	margin: 0;
	padding: 0;
}

```

Dans l'exemple ci-dessus, il a remis à zéro la marge et le rembourrage pour toute la page en utilisant le sélecteur universel.

# Comment grouper les sélecteurs CSS

Avant d'aborder les sélecteurs CSS avancés, nous devons examiner rapidement le groupement des sélecteurs CSS. C'est une pratique courante que vous verrez souvent et elle aide à rendre votre code propre et lisible.

Le groupement vous permet de sélectionner plusieurs éléments HTML à la fois et de ne déclarer leurs définitions de style qu'une seule fois.

Regardons un exemple de sélecteur de groupement pour expliquer.

```css
h1 {
	text-align: left;
	letter-spacing: 3px;
	color: #111111;
}

h2 {
	text-align: left;
	letter-spacing: 3px;
	color: #111111;
}

h3 {
	text-align: left;
	letter-spacing: 3px;
	color: #111111;
}

```

Dans le code CSS ci-dessus, nous avons trois éléments `h1`, `h2` et `h3` et chacun de ces éléments a les mêmes définitions de style. En conséquence, nous pouvons nettoyer notre code en groupant les sélecteurs.

Pour grouper les sélecteurs, nous séparons chaque sélecteur par un caractère `,` (virgule).

```css
h1, h2, h3 {
	text-align: left;
	letter-spacing: 3px;
	color: #111111;
}

```

Parce que leurs définitions de style sont les mêmes, nous n'avons plus qu'à l'écrire une seule fois.

Notez que le groupement de sélecteurs peut être utilisé pour tous les sélecteurs mentionnés dans cet article, ce qui signifie que les sélecteurs n'ont pas besoin d'être du même type. 

Nous pourrions grouper un sélecteur de classe avec un sélecteur d'ID si nous voulons qu'ils partagent des définitions de style. Et nous pourrions grouper les propriétés de style et les valeurs qui correspondent, puis définir des définitions différentes sur chaque élément. 

Développons notre exemple pour comprendre ce concept.

```css
/* grouper les sélecteurs et déclarer les définitions qui sont les mêmes */

h1, h2, h3 {
	text-align: left;
	letter-spacing: 3px;
	color: #111111;
}

/* appliquer des styles individuels aux sélecteurs */

h1 {
	font-size: 72px;
}

h2 {
	font-size: 48px;
}

h3 {
	font-size: 32px;
}

```

Et voilà, ce sont tous les sélecteurs CSS de base. Si vous voulez devenir bon en CSS, vous devez comprendre ce que chacun d'eux fait. Avec ces connaissances en main, vous devriez maintenant être sur la bonne voie pour y parvenir.

Si vous voulez passer au niveau supérieur en CSS, vous voudrez comprendre les sélecteurs CSS avancés.

# Sélecteurs CSS avancés

Les sélecteurs CSS avancés vous permettent de repousser les limites du CSS. Ils vous aident à être très spécifique sur les éléments que vous souhaitez cibler et sur l'état de cet élément lors du ciblage. 

Entrons directement dans certains sélecteurs CSS avancés en examinant les sélecteurs d'attributs. 

## Sélecteurs d'attributs CSS

Les sélecteurs d'attributs vous permettent de sélectionner des éléments selon qu'un certain attribut est présent ou non. En d'autres termes, ce sélecteur CSS correspondra à n'importe quel élément de votre page s'il possède un certain attribut. 

Un attribut est un contenu ajouté à la balise d'ouverture d'un élément HTML. Il peut s'agir de choses comme `id`, `name` ou `value`.

```html
<a title="Apprenez à coder gratuitement !" href="https://www.freecodecamp.org/">Apprenez à coder</a>
```

Il existe sept sélecteurs d'attributs qui vous permettent chacun de trouver des éléments selon qu'un attribut est présent et ce que la valeur peut contenir. 

1. Sélecteur de présence
2. Sélecteur d'égalité (`=`)
3. Sélecteur de début (`^`)
4. Sélecteur de fin (`$`)
5. Sélecteur de contenu (`*`)
6. Sélecteur d'espace blanc (`~`) 
7. Sélecteur de trait d'union (`|`)

La syntaxe commune pour ces sélecteurs est le sélecteur suivi de `[ ]` (crochets) dans lesquels vous indiquez ce que vous recherchez. Le sélecteur peut être n'importe quoi, comme un sélecteur de classe ou même un sélecteur universel.

```css
selector[attribute] 

```

Aujourd'hui, nous allons examiner les cinq sélecteurs d'attributs les plus courants. Afin de comprendre ces five sélecteurs d'attributs, examinons chacun d'eux avec des exemples.

### Sélecteur d'attribut de présence

Ce sélecteur d'attribut trouve n'importe quel élément selon qu'il inclut un attribut.

Regardons un exemple de sélecteur de présence pour expliquer.

```css
a[title] {
	color: khaki;
	background: grey; 
}

```

Dans l'exemple ci-dessus, notre sélecteur de présence trouvera n'importe quel élément `a` qui possède un attribut `title` et leur appliquera la définition de style. Tous les autres éléments `a` qui n'ont pas d'attribut title ne seront pas stylisés comme ci-dessus.

### Sélecteur d'attribut d'égalité

Ce sélecteur d'attribut trouve un élément avec une correspondance exacte de la valeur de l'attribut. Pour utiliser ce sélecteur, vous indiquez le nom de l'attribut suivi d'un `=` (égal) pour trouver la correspondance exacte de la valeur.

Regardons un exemple de sélecteur d'égalité pour expliquer.

```css
a[href="<https://peterlunch.com/>"] {
	color: purple;
} 

```

Dans l'exemple ci-dessus, le sélecteur d'égalité trouvera n'importe quel élément `a` qui possède un attribut `href` avec la valeur exacte de "[https://peterlunch.com/](https://peterlunch.com/)".

### Sélecteur d'attribut de début

Ce sélecteur d'attribut trouve n'importe quel élément qui commence par une valeur que vous spécifiez. Pour utiliser ce sélecteur, vous indiquez l'attribut que vous recherchez, suivi des caractères `^` et `=`, puis de la valeur que vous cherchez à faire correspondre.

Regardons un exemple de sélecteur de début pour expliquer.

```css
a[href^="https"] {
	color: yellow;
	text-decoration: none;
}

```

Dans l'exemple ci-dessus, le sélecteur de début trouve n'importe quel élément `a` qui possède un attribut `href` et qui commence par "https".

### Sélecteur d'attribut de fin

Tout comme le sélecteur de début, ce sélecteur d'attribut fait le contraire et trouve n'importe quel élément qui se termine par une valeur que vous spécifiez. 

Pour utiliser ce sélecteur, vous indiquez l'attribut que vous recherchez, suivi des caractères `$` et `=`, puis de la valeur que vous cherchez à faire correspondre.

Regardons un exemple de sélecteur de fin pour expliquer.

```css
img[src$="/blog-imgs"] {
	border-radius: 4px;
	box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

```

Dans l'exemple ci-dessus, le sélecteur de fin trouve n'importe quel élément `img` qui possède un `src` se terminant par "/blog-imgs". C'est un sélecteur que j'utilise réellement pour mon site web.

### Sélecteur d'attribut de contenu

Ce sélecteur d'attribut trouve n'importe quel élément qui contient la valeur que vous recherchez quelque part dans la valeur de l'attribut. Cela signifie que la valeur doit contenir au moins une occurrence de la valeur.

Pour utiliser ce sélecteur, vous indiquez l'attribut que vous recherchez, suivi des caractères `*` et `=`, puis de la valeur dont vous recherchez une occurrence.

Regardons un exemple de sélecteur de contenu pour expliquer.

```css
a[href*="peterlunch"] {
	color: green;
}

```

Dans l'exemple ci-dessus, le sélecteur d'attribut de contenu trouve n'importe quel élément `a` qui possède un `href` contenant la valeur "peterlunch".

C'est tout pour les sélecteurs d'attributs, passons au sélecteur CSS avancé suivant.

## Sélecteurs de combinaison

Les prochains sélecteurs CSS avancés sont les sélecteurs de combinaison. Ces sélecteurs peuvent combiner plus d'un sélecteur CSS. Il existe quatre types de sélecteurs de combinaison en CSS :

1. Sélecteurs de descendants
2. Sélecteurs d'enfants
3. Sélecteurs de frères adjacents
4. Sélecteurs de frères généraux

Pour comprendre comment fonctionnent ces sélecteurs, vous devez d'abord comprendre que le HTML suit une hiérarchie d'arbre généalogique. Cela signifie qu'il existe un élément parent qui peut contenir des enfants, et les enfants peuvent avoir des enfants, et ainsi de suite, comme un arbre généalogique.

```html
<div> <!--parent-->
	<p> <!--enfant de div-->
	<article> <!--enfant de div, parent de h1 & p-->	 
		<h1>
			<p></p>
		</h1>
	</article>
	<article>	
		<h1>
			<p></p>
			<p></p>
		</h1>
	</article>
</div>

```

Dans l'exemple ci-dessus, le `div` est le parent, ses enfants sont les éléments `article`, et les articles sont les parents des enfants `h1` et `p`.

Avec cette connaissance à l'esprit, explorons chacun de ces sélecteurs de combinaison un par un avec des exemples pour comprendre comment ils fonctionnent.

### Sélecteur de combinaison de descendants

Le sélecteur de combinaison de descendants correspond à tous les éléments qui sont des descendants d'un élément spécifié.

Regardons un exemple de combinaison de descendants pour expliquer.

```css
div p {
	line-height: 2em;
}

```

L'exemple ci-dessus sélectionne tous les éléments `p` à l'intérieur des éléments `div`.

### Sélecteur de combinaison d'enfants

Le sélecteur de combinaison d'enfants correspond à tous les éléments qui sont des enfants directs d'un élément spécifique. C'est différent du sélecteur de combinaison de descendants, car il ne sélectionne que les enfants directs de l'élément parent.

Les sélecteurs d'enfants sont désignés par un caractère `>`.

Regardons un exemple de sélecteur de combinaison d'enfants pour expliquer.

```css
div > p {
	color: aquamarine;
}

```

En nous référant à notre exemple de hiérarchie HTML ci-dessus, ce sélecteur ne trouvera que la première balise `p` et non les balises `p` à l'intérieur des balises `article`. Il fait cela car elles ne sont pas des enfants directs de l'élément parent `div`.

### Sélecteur de combinaison de frères adjacents

Les sélecteurs de frères adjacents sont désignés à l'aide d'un `+` qui sépare deux sélecteurs et ne correspond au second élément sélecteur que s'il suit immédiatement le premier élément.

Un bon exemple concret de cela est de vouloir que le texte qui suit immédiatement une image soit stylisé comme une légende.

```css
img + p {
	font-size: 10px;
	color: grey;
	font-style: italic;
}

```

Dans l'exemple ci-dessus, tout élément `p` qui suit une image sera stylisé avec la définition ci-dessus.

### Sélecteur de combinaison de frères généraux

Le sélecteur de frères généraux sélectionne tous les éléments qui sont des frères d'un élément. Les sélecteurs de frères généraux sont désignés par un caractère `~`.

Regardons un exemple de sélecteur de frères généraux pour expliquer.

```css
article ~ h1 {
	font-weight: 900;
}

```

Dans l'exemple ci-dessus, il sélectionne tous les éléments `h1` qui sont des frères des éléments `article`.

### Pseudo-sélecteurs

Les pseudo-sélecteurs se divisent en deux catégories. La première concerne les [sélecteurs de pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) et la seconde les [sélecteurs de pseudo-éléments](https://peterlunch.com/css-pseudo-elements/). 

Ces sélecteurs sont complexes et offrent de nombreuses options. Pour les comprendre, il vaut la peine de lire des articles séparés à leur sujet car ce sont des sujets complexes en soi. Mais je vais brièvement aborder les deux ici.

Premièrement, les sélecteurs de pseudo-classes sélectionnent des éléments en fonction d'un certain état. Vous avez peut-être vu des choses comme `:hover` ou `:active`. Ce sont les états des éléments sur votre page. Vous pouvez sélectionner des éléments selon que cet élément se trouve dans l'état spécifié.

Un exemple rapide serait :

```css
button:hover {
	background: red;
}

```

Dans l'exemple ci-dessus, lorsqu'un utilisateur survole un bouton, la couleur d'arrière-plan change en rouge.

Si vous voulez mieux comprendre les sélecteurs de pseudo-classes, je vous encourage à lire [cet article](https://www.freecodecamp.org/news/explained-css-pseudo-classes-cef3c3177361/) de Nash Vail, qui fait un travail fantastique pour les expliquer. 

Viennent ensuite les sélecteurs de pseudo-éléments sur lesquels j'ai écrit [ici](https://peterlunch.com/css-pseudo-elements/). Ces sélecteurs sélectionnent des parties d'un élément. Une partie d'un élément peut être la première lettre de l'élément ou le contenu avant et après l'élément. 

Avec les sélecteurs de pseudo-éléments, il est important de noter qu'ils utilisent `::` (doubles deux-points) par opposition à `:` (deux-points simples) comme les pseudo-classes.

```css
p {
  width: 600px;
  line-height: 1.5;
  font-weight: 500;
}

p::first-letter {
  color: white;
  background-color: rgb(55, 97, 117);
  border-radius: 3px;
  box-shadow: 3px 3px 0 rgb(212, 173, 81);
  font-size: 250%;
  padding: 6px 3px;
  margin-right: 6px;
  float: left;
}
```

%[https://codepen.io/pin0s/pen/BapXWOg]

## Résumé

Vous devriez maintenant avoir une bonne compréhension des sélecteurs CSS et de la manière dont vous pouvez les utiliser pour trouver des éléments HTML sur vos pages web. 

J'espère que vous avez apprécié la lecture de cet article. Si vous avez appris quelque chose grâce à ce post, consultez le reste de mes articles [ici](https://bit.ly/2Re6Vdf) ou [inscrivez-vous à ma newsletter](ttps://mailchi.mp/bfaa8a288d7c/7o1pve3bv9) pour obtenir du contenu pour débutants incroyablement bon et super exclusif.
---
title: Les meilleurs tutoriels HTML et HTML5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-26T00:41:00.000Z'
originalURL: https://freecodecamp.org/news/best-html-html5-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f0a740569d1a4ca4084.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: Tutorial
  slug: tutorial
seo_title: Les meilleurs tutoriels HTML et HTML5
seo_desc: "HyperText Markup Language (HTML) is a markup language used to construct\
  \ online documents and is the foundation of most websites today. A markup language\
  \ like HTML allows us to\n\ncreate links to other documents, \nstructure the content\
  \ in our document, ..."
---

HyperText Markup Language (HTML) est un langage de balisage utilisé pour construire des documents en ligne et est la base de la plupart des sites web aujourd'hui. Un langage de balisage comme HTML nous permet de

* créer des liens vers d'autres documents, 
* structurer le contenu de notre document, et 
* attribuer un contexte et une signification au contenu de notre document.

Un document HTML a deux aspects. Il contient des informations structurées (balisage) et des liens texte (hypertexte) vers d'autres documents. Nous structurons nos pages en utilisant des [éléments HTML](https://guide.freecodecamp.org/html#). Ce sont des constructions du langage fournissant une [structure](https://guide.freecodecamp.org/html#) et une [signification](https://guide.freecodecamp.org/html#) dans notre document pour le navigateur, et les éléments lient à d'autres documents à travers l'internet.

L'internet a été créé à l'origine pour stocker et présenter des documents statiques (inchangés). Les aspects de HTML discutés ci-dessus étaient parfaitement visibles dans ces documents qui manquaient de tout design et style. Ils présentaient des informations structurées contenant des liens vers d'autres documents.

HTML5 est la dernière version, ou spécification, de HTML. Le World Wide Web Consortium (W3C) est l'organisation responsable du développement des standards pour le World Wide Web, y compris ceux pour HTML. À mesure que les pages web et les applications web deviennent plus complexes, le W3C met à jour les standards de HTML.

HTML5 introduit une multitude d'éléments sémantiques. Bien que nous ayons discuté de la manière dont HTML aide à fournir une signification à notre document, ce n'est qu'avec l'introduction des [éléments sémantiques](https://guide.freecodecamp.org/html#) par HTML5 que son potentiel a été réalisé.

## **Un exemple simple de document HTML**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Titre de la Page</title>
</head>
<body>

  <h1>Mon Premier Titre</h1>
  <p>Mon premier paragraphe.</p>

</body>
</html>
```

!DOCTYPE html: Définit ce document comme étant HTML5

html: L'élément racine d'une page HTML

head: L'élément contient des méta-informations sur le document

title: L'élément spécifie un titre pour le document

body: L'élément contient le contenu visible de la page

h1: L'élément définit un grand titre

p: L'élément définit un paragraphe

# Tutoriels pour commencer avec HTML et HTML5

Le meilleur endroit pour commencer à apprendre HTML est avec le [tutoriel d'introduction à HTML de 2 heures de freeCodeCamp](https://www.youtube.com/watch?v=pQN-pnXPaVg).

Ensuite, si vous vous sentez plus aventureux, nous avons un [cours complet de 12 heures qui couvre HTML, HTML5 et CSS en détail](https://www.youtube.com/watch?v=mU6anWqZJcc).

![Image](https://img.youtube.com/vi/mU6anWqZJcc/maxresdefault.jpg)

## **Structure de la Page**

Pour créer vos pages en `HTML`, vous devez savoir comment structurer une page en `HTML`. Basiquement, la structuration d'une page suit l'ordre ci-dessous :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Titre de la Page</title>
  </head>
  <body>
    <!-- Contenu -->
  </body>
</html>
```

1 - La déclaration `<!DOCTYPE html>` doit toujours apparaître en premier sur une page `HTML` et indique au navigateur quelle version du langage est utilisée. Dans ce cas, nous travaillons avec `HTML5`.

2 - Les balises `<html>` et `</html>` indiquent au navigateur web où le code `HTML` commence et se termine.

3 - Les balises `<head>` et `</head>` contiennent des informations sur le site web, par exemple : le style, les méta-balises, les scripts, etc.

4 - Les balises `<title>` et `</title>` indiquent au navigateur quel est le titre de la page. Le titre peut être vu en identifiant l'onglet dans votre navigateur internet. Le texte qui est défini entre ces balises est également le texte qui est utilisé comme titre par les moteurs de recherche lorsqu'ils présentent les pages dans les résultats d'une recherche.

5 - Entre les balises `<body>` et `</body>` est placé le contenu de la page, qui est ce qui est affiché dans le navigateur.

## Changements dans HTML5

#### **Introduction des balises sémantiques**

Au lieu d'utiliser `<div>` pour chaque autre conteneur, il existe plusieurs balises sémantiques (ces balises aident les lecteurs d'écran utilisés par les personnes malvoyantes) telles que `<header>`, `<footer>`. Il est donc conseillé d'utiliser ces balises au lieu du générique `<div>`.

# **Éléments HTML**

Les éléments sont les blocs de construction de HTML qui décrivent la structure et le contenu d'une page web. Ils sont la partie "Markup" de HyperText Markup Language (HTML).

La syntaxe HTML utilise les chevrons ("<" et ">") pour contenir le nom d'un élément HTML. Les éléments ont généralement une balise d'ouverture et une balise de fermeture, et donnent des informations sur le contenu qu'ils contiennent. La différence entre les deux est que la balise de fermeture a une barre oblique.

Voici un exemple utilisant l'[élément p](https://guide.freecodecamp.org/html/elements#) (`<p>`) pour indiquer au navigateur qu'un groupe de texte est un paragraphe :

```html
<p>Ceci est un paragraphe.</p>
```

Les balises d'ouverture et de fermeture doivent correspondre, sinon le navigateur peut afficher le contenu de manière inattendue.

![Bande dessinée XKCD montrant le texte "Q: Comment énerver un développeur ?" entouré d'une balise div ouvrante et d'une balise span fermante](http://imgs.xkcd.com/comics/tags.png)

## **Éléments auto-fermants**

Certains éléments HTML sont auto-fermants, ce qui signifie qu'ils n'ont pas de balise de fermeture séparée. Les éléments auto-fermants insèrent généralement quelque chose dans votre document.

Un exemple est l'[élément br](https://guide.freecodecamp.org/html/elements#) (`<br>`), qui insère un saut de ligne dans le texte. Auparavant, les balises auto-fermantes avaient la barre oblique à l'intérieur (`<br />`), cependant, la spécification HTML5 ne l'exige plus.

## **Fonctionnalité des éléments HTML**

Il existe de nombreux éléments HTML disponibles. Voici une liste de certaines des fonctions qu'ils remplissent :

* donner des informations sur la page web elle-même (les métadonnées)
* structurer le contenu de la page en sections
* intégrer des images, des vidéos, des clips audio ou d'autres médias
* créer des listes, des tableaux et des formulaires
* donner plus d'informations sur un certain contenu textuel
* lier à des feuilles de style qui contiennent des règles sur la manière dont le navigateur doit afficher la page
* ajouter des scripts pour rendre une page plus interactive et dynamique

## **Imbrication des éléments HTML**

Vous pouvez imbriquer des éléments dans d'autres éléments dans un document HTML. Cela aide à définir la structure de la page. Assurez-vous simplement que les balises se ferment à partir de l'élément le plus interne en premier.

Correct : `<p>Ceci est un paragraphe qui contient un <span>élément span.</span></p>`

Incorrect : `<p>Ceci est un paragraphe qui contient un <span>élément span.</p></span>`

## **Éléments de niveau bloc et en ligne**

Les éléments se divisent en deux catégories générales, connues sous le nom de niveau bloc et en ligne. Les éléments de niveau bloc commencent automatiquement sur une nouvelle ligne tandis que les éléments en ligne se trouvent dans le contenu environnant.

Les éléments qui aident à structurer la page en sections, comme une barre de navigation, des titres et des paragraphes, sont généralement des éléments de niveau bloc. Les éléments qui insèrent ou donnent plus d'informations sur le contenu sont généralement en ligne, comme les [liens](https://guide.freecodecamp.org/html/elements#) ou les [images](https://guide.freecodecamp.org/html/elements#).

## **L'élément HTML**

Il existe un élément `<html>` qui est utilisé pour contenir les autres balises d'un document HTML. Il est également connu sous le nom d'élément "racine" car il est le parent des autres éléments HTML et du contenu d'une page.

Voici un exemple de page avec un [élément head](https://guide.freecodecamp.org/html/elements#the-head-element), un [élément body](https://guide.freecodecamp.org/html/elements#the-body-element) et un [paragraphe](https://guide.freecodecamp.org/html/elements#the-p-element) :

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Je suis un paragraphe</p>
  </body>
</html>
```

## **L'élément HEAD**

Ceci est le conteneur pour les informations de traitement et les métadonnées d'un document HTML.

```html
<head>
  <meta charset="utf-8">
</head>
```

## **L'élément BODY**

Ceci est un conteneur pour le contenu affichable d'un document HTML.

```html
<body>...</body>
```

## **L'élément P**

Crée un paragraphe, peut-être l'élément de niveau bloc le plus courant.

```html
<p>...</p>
```

## **L'élément A(Lien)**

Crée un hyperlien pour diriger les visiteurs vers une autre page ou ressource.

```html
<a href="#">...</a>
```

# Images en HTML

Vous pouvez définir des images en utilisant la balise `<img>`. Elle n'a pas de balise de fermeture puisqu'elle ne peut contenir que des attributs. Pour insérer une image, vous définissez la source et un texte alternatif qui est affiché lorsque l'image ne peut pas être rendue.

`src` - Cet attribut fournit l'URL de l'image présente soit sur votre P.C./Ordinateur portable ou à inclure depuis un autre site web. Rappelez-vous que le lien fourni ne doit pas être rompu, sinon l'image ne sera pas produite sur votre page web.

`alt` - Cet attribut est utilisé pour surmonter le problème d'image brisée ou l'incapacité de votre navigateur à produire une image sur la page web. Cet attribut, comme le nom le suggère, fournit une "Alternative" à une image qui est un certain "TEXTE" décrivant l'image.

## **Exemple**

```html
<img src="URL de l'Image" alt="Titre Descriptif" />
```

### **Pour définir la hauteur et la largeur d'une image, vous pouvez utiliser les attributs height et width :**

```html
<img src="URL de l'Image" alt="Titre Descriptif" height="100" width="150"/>
```

### **Vous pouvez également définir l'épaisseur de la bordure (0 signifie pas de bordure) :**

```html
<img src="URL de l'Image" alt="Titre Descriptif" border="2"/>
```

### **Aligner une image :**

```html
<img src="URL de l'Image" alt="Titre Descriptif" align="left"/>
```

### **Vous pouvez également utiliser des styles dans un attribut style :**

```html
<img src="URL de l'Image" alt="Titre Descriptif" style="width: 100px; height: 150px;"/>
```

# Comment utiliser les liens en HTML

En HTML, vous pouvez utiliser la balise `<a>` pour créer un lien. Par exemple, vous pouvez écrire `<a href="https://www.freecodecamp.org/">freeCodeCamp</a>` pour créer un lien vers le site web de freeCodeCamp.

Les liens se trouvent dans presque toutes les pages web. Les liens permettent aux utilisateurs de cliquer pour passer d'une page à l'autre.

Les liens HTML sont des hyperliens. Vous pouvez cliquer sur un lien et sauter vers un autre document.

Lorsque vous déplacez la souris sur un lien, la flèche de la souris se transforme en une petite main.

Note : Un lien n'a pas besoin d'être du texte. Il peut s'agir d'une image ou de tout autre élément HTML.

En HTML, les liens sont définis avec la balise `<a>` :

```html
<a href="url">texte du lien</a>
```

Exemple

```html
<a href="https://www.freecodecamp.org/">Visitez notre site pour des tutoriels</a>
```

L'attribut href spécifie l'adresse de destination (https://www.freecodecamp.org) du lien.

Le texte du lien est la partie visible (Visitez notre site pour des tutoriels).

En cliquant sur le texte du lien, vous serez envoyé à l'adresse spécifiée.

# Comment utiliser les listes en HTML

Les listes sont utilisées pour spécifier un ensemble d'éléments consécutifs ou d'informations connexes de manière bien formée et sémantique, comme une liste d'ingrédients ou une liste d'étapes procédurales.

Le balisage HTML a trois types différents de listes - **ordonnées**, **non ordonnées** et **descriptives**.

### **Listes ordonnées**

Une liste ordonnée est utilisée pour regrouper un ensemble d'éléments connexes, dans un ordre spécifique. Cette liste est créée avec la balise `<ol>`. Chaque élément de la liste est entouré de la balise `<li>`.

##### **Code**

```html
<ol>
    <li>Mélanger les ingrédients</li>
    <li>Cuire au four pendant une heure</li>
    <li>Laisser reposer pendant dix minutes</li>
</ol>
```

##### **Exemple**

1. Mélanger les ingrédients
2. Cuire au four pendant une heure
3. Laisser reposer pendant dix minutes

### **Listes non ordonnées**

Une liste non ordonnée est utilisée pour regrouper un ensemble d'éléments connexes, dans aucun ordre particulier. Cette liste est créée avec la balise `<ul>`. Chaque élément de la liste est entouré de la balise `<li>`.

##### **Code**

```html
<ul>
    <li>Gâteau au chocolat</li>
    <li>Forêt noire</li>
    <li>Gâteau à l'ananas</li>
</ul>
```

#### **Exemple**

* Gâteau au chocolat
* Forêt noire
* Gâteau à l'ananas

### **Listes de description**

Une liste de description est utilisée pour spécifier une liste de termes et leurs descriptions. Cette liste est créée avec la balise `<dl>`. Chaque élément de la liste est entouré de la balise `<dd>`.

##### **Code**

```html
<dl>
    <dt>Pain</dt>
    <dd>Un aliment cuit fait de farine.</dd>
    <dt>Café</dt>
    <dd>Une boisson faite à partir de grains de café torréfiés.</dd>
</dl>
```

##### **Sortie**

**Pain** Un aliment cuit fait de farine. **Café** Une boisson faite à partir de grains de café torréfiés.

#### **Style de liste**

Vous pouvez également contrôler le style de la liste. Vous pouvez utiliser la propriété `list-style` des listes. Votre liste peut être des puces, des carrés, en chiffres romains, ou peut être des images si vous le souhaitez.

La propriété `list-style` est un raccourci pour `list-style-type`, `list-style-position`, `list-style-image`.
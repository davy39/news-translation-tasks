---
title: Les meilleurs exemples HTML et HTML5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-24T18:09:00.000Z'
originalURL: https://freecodecamp.org/news/html-and-html5-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/html-examples.jpeg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: Les meilleurs exemples HTML et HTML5
seo_desc: 'HTML provides the structure of websites. Here are some examples of how
  to use HTML syntax to build websites, including some examples of newer HTML5 features.

  The A Href Attribute Example

  The <a href> attribute refers to a destination provided by a li...'
---

HTML fournit la structure des sites web. Voici quelques exemples de l'utilisation de la syntaxe HTML pour construire des sites web, y compris certains exemples de fonctionnalités plus récentes de HTML5.

## **Exemple de l'attribut A Href**

L'attribut `<a href>` fait référence à une destination fournie par un lien. La balise `a` (ancre) est inutile sans l'attribut `<href>`. Parfois, dans votre flux de travail, vous ne voulez pas d'un lien actif ou vous ne connaîtrez pas encore la destination du lien. Dans ce cas, il est utile de définir l'attribut `href` sur `"#"` pour créer un lien mort. L'attribut `href` peut être utilisé pour lier des fichiers locaux ou des fichiers sur Internet.

Par exemple :

```html
<html>
  <head>
    <title>Exemple d'attribut Href</title>
  </head>
  <body>
    <h1>Exemple d'attribut Href</h1>
    <p>
      <a href="https://www.freecodecamp.org/contribute/">La page de contribution de freeCodeCamp</a> vous montre comment et où vous pouvez contribuer à la communauté et à la croissance de freeCodeCamp.
    </p>
  </body>
</html>
```

L'attribut `<a href>` est supporté par tous les navigateurs.

#### **Plus d'attributs :**

`hreflang` : Spécifie la langue de la ressource liée. `target` : Spécifie le contexte dans lequel la ressource liée s'ouvrira. `title` : Définit le titre d'un lien, qui apparaît à l'utilisateur sous forme d'infobulle.

### **Exemples**

```html
<a href="#">Ceci est un lien mort</a>
<a href="https://www.freecodecamp.org">Ceci est un lien actif vers freeCodeCamp</a>
<a href="https://html.com/attributes/a-href/">plus sur l'attribut a href</a>
```

### **Ancres dans la page**

Il est également possible de définir une ancre à un certain endroit de la page. Pour ce faire, vous devez d'abord placer une ancre à l'emplacement sur la page avec la balise `<a>` et l'attribut "name" avec une description de mot-clé, comme ceci :

```html
<a name="haut"></a>
```

Toute description entre les balises n'est pas requise. Après cela, vous pouvez placer un lien menant à cette ancre à n'importe quel endroit de la même page. Pour ce faire, vous devez utiliser la balise avec l'attribut nécessaire "href" avec le symbole # (dièse) et la description du mot-clé de l'ancre, comme ceci :

```html
<a href="#haut">Aller en haut</a>
```

### **Liens d'images**

L'attribut `<a href="#">` peut également être appliqué aux images et à d'autres éléments HTML.

### **Exemple**

```html
<a href="#">
  <img itemprop="image" style="height: 90px;" src="https://bit.ly/fcc-relaxing-cat" alt="Un mignon chat orange allongé sur le dos.">
</a>
```

### **Exemple**

![Un mignon chat orange allongé sur le dos.](https://www.freecodecamp.org/news/content/images/2021/03/relaxing-cat.jpg)

### Exemple de l'attribut A Target

L'attribut `<a target>` spécifie où ouvrir le document lié dans une balise `a` (ancre).

**Exemples :**

Un attribut target avec la valeur "_blank" ouvre le document lié dans une nouvelle fenêtre ou un nouvel onglet.

```html
<a href="https://www.freecodecamp.org/" target="_blank">freeCodeCamp</a>
```

Un attribut target avec la valeur "_self" ouvre le document lié dans le même cadre où il a été cliqué (c'est le comportement par défaut et il n'est généralement pas nécessaire de le spécifier).

```html
<a href="https://www.freecodecamp.org/" target="_self">freeCodeCamp</a>
```

```html
<a href="https://www.freecodecamp.org/">freeCodeCamp</a>
```

Un attribut target avec la valeur "_parent" ouvre le document lié dans le cadre parent.

```html
<a href="https://www.freecodecamp.org/" target="_parent">freeCodeCamp</a>
```

Un attribut target avec la valeur "_top" ouvre le document lié dans le corps complet de la fenêtre.

```html
<a href="https://www.freecodecamp.org/" target="_top">freeCodeCamp</a>
```

Un attribut target avec la valeur _"nomduframe"_ ouvre le document lié dans un cadre nommé spécifié.

```html
<a href="https://www.freecodecamp.org/" target="nomduframe">freeCodeCamp</a>
```

## **Exemple de l'attribut Body Background**

Si vous souhaitez ajouter une image de fond au lieu d'une couleur, une solution est l'attribut `<body background>`. Il spécifie une image de fond pour un document HTML.

Syntaxe :

`<body background="URL">`

Attribut :

`background - URL pour l'image de fond`

Exemple :

```html
<html>
  <body background="https://assets.digitalocean.com/blog/static/hacktoberfest-is-back/hero.png">
  </body>
</html>
```

## **L'attribut body-background est obsolète**

L'attribut body-background a été déprécié en HTML5. La bonne façon de styliser la balise `<body>` est avec CSS.

Il existe plusieurs propriétés CSS utilisées pour définir l'arrière-plan d'un élément. Celles-ci peuvent être utilisées pour définir l'arrière-plan d'une page entière.

## **Exemple de l'attribut Body Bgcolor**

L'attribut `<body bgcolor>` attribue une couleur de fond à un document HTML.

**Syntaxe :**

`<body bgcolor="couleur">` La valeur de couleur peut être soit un nom de couleur (comme, `violet`) soit une valeur hexadécimale (comme, `#af0000`).

Pour ajouter une couleur de fond à une page web, vous pouvez utiliser l'attribut `<body bgcolor="######">`. Il spécifie une couleur pour le document HTML à afficher.

**Par exemple :**

```html
<html>
  <head>
    <title>Exemple d'attribut Body bgcolor</title>
  </head>
  <body bgcolor="#afafaf">
    <h1>Cette page web a un fond coloré.</h1>
  </body>
</html>
```

Vous pouvez changer la couleur en remplaçant ###### par une valeur hexadécimale. Pour des couleurs simples, vous pouvez également utiliser le mot, comme "rouge" ou "noir".

Tous les principaux navigateurs supportent l'attribut `<body bgcolor>`.

_Note :_

* HTML 5 ne supporte pas l'attribut `<body bgcolor>`. Utilisez CSS à cette fin. Comment ? En utilisant le code suivant : `<body style="background-color: couleur">` Bien sûr, vous pouvez également le faire dans un document séparé au lieu d'une méthode en ligne.
* N'utilisez pas de valeur RGB dans l'attribut `<body bgcolor>` car `rgb()` est uniquement pour CSS, c'est-à-dire qu'il ne fonctionnera pas en HTML.

## **Exemple de l'attribut Div Align**

L'attribut `<div align="">` est utilisé pour aligner le texte dans une balise div à gauche, à droite, au centre ou justifié.

Par exemple :

```html
<html>
  <head>
    <title>Attribut Div Align</title>
  </head>
  <body>
    <div align="left">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
      labore et dolore magna aliqua.
    </div>
    <div align="right">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
      labore et dolore magna aliqua.
    </div>
    <div align="center">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
      labore et dolore magna aliqua.
    </div>
    <div align="justify">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
      labore et dolore magna aliqua.
    </div>
  </body>
</html>

```

## **Important !**

Cet attribut n'est plus supporté en HTML5. CSS est la voie à suivre.

L'attribut Div Align peut être utilisé pour aligner horizontalement le contenu d'une div. Dans l'exemple ci-dessous, le texte sera centré dans la div.

```html
<div align="center">
  Ce texte sera centré
</div>
```

**Cet attribut n'est pas supporté en HTML5 et [CSS Text Align](https://github.com/freeCodeCamp/guides/blob/f50b7370be514b2a03ee707cd0f0febe2bb713ae/src/pages/css/text-align/index.md) doit être utilisé à la place

## **Exemple de l'attribut Font Color**

Cet attribut est utilisé pour définir une couleur au texte enfermé dans une balise `<font>`.

### Important :

Cet attribut n'est pas supporté en HTML5. Au lieu de cela, cet [article de freeCodeCamp](https://guide.freecodecamp.org/css/colors) spécifie une méthode CSS, qui peut être utilisée.

### Note :

Une couleur peut également être spécifiée en utilisant un 'code hexadécimal' ou un 'code rgb', au lieu d'utiliser un nom.

### Exemple :

1. Attribut de nom de couleur

```html
<html>
  <body>
    <font color="green">Exemple de couleur de police utilisant l'attribut color</font>
  </body>
</html>

```

Attribut de code hexadécimal

```html
<html>
  <body>
    <font color="#00FF00">Exemple de couleur de police utilisant l'attribut color</font>
  </body>
</html>

```

Attribut RGB

```html
<html>
  <body>
    <font color="rgb(0,255,0)">Exemple de couleur de police utilisant l'attribut color</font>
  </body>
</html>

```

## **Exemple de l'attribut Font Size**

Cet attribut spécifie la taille de la police comme une valeur numérique ou relative. Les valeurs numériques vont de `1` à `7`, `1` étant la plus petite et `3` la valeur par défaut. Elle peut également être définie en utilisant une valeur relative, comme `+2` ou `-3`, qui la définissent par rapport à la valeur de l'attribut size de l'élément `<basefont>`, ou par rapport à `3`, la valeur par défaut, si aucun n'existe.

Syntaxe :

`<font size="nombre">`

Exemple :

```html
<html>
  <body>
    <font size="6">Ceci est du texte !</font>
  </body>
</html>
```

Note : `L'attribut size de <font> n'est pas supporté en HTML5. Utilisez CSS à la place.`

## **Exemple de l'attribut Img Align**

L'attribut align d'une image spécifie où l'image doit être alignée selon l'élément environnant.

Valeurs de l'attribut :  
droite - Aligner l'image à droite gauche - Aligner l'image à gauche  
haut - Aligner l'image en haut  
bas - Aligner l'image en bas  
milieu - Aligner l'image au milieu

Par exemple :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Attribut Img Align</title>
  </head>
  <body>
    <p>
      Ceci est un exemple. <img src="image.png" alt="Image" align="middle" /> Plus de texte ici
      <img src="image.png" alt="Image" width="100" />
    </p>
  </body>
</html>

```

Nous pouvons également aligner à droite si nous le souhaitons :

```html
<p>Ceci est un autre exemple<img src="image.png" alt="Image" align="right" /></p>

```

**Veuillez noter que l'attribut align n'est pas supporté en HTML5, et vous devriez utiliser CSS à la place. Cependant, il est toujours supporté par tous les principaux navigateurs.**

## **L'attribut Img Width**

L'attribut HTML 'width' fait référence à la largeur d'une image. La valeur entre guillemets est le nombre de pixels.

Par exemple, si vous avez déjà un lien vers une image configuré via l'attribut `src`, vous pouvez ajouter l'attribut width comme suit :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Attribut Img Width</title>
  </head>
  <body>
    <img src="image.png" alt="Image" width="100" />
  </body>
</html>

```

Dans l'extrait de code ci-dessus, il y a une balise image et l'image est définie à une largeur de 100 pixels. `width="100"`

## **Exemple de l'attribut Img Src**

L'attribut `<img src>` fait référence à la source de l'image que vous souhaitez afficher. La balise `img` n'affichera pas d'image sans l'attribut `src`. Cependant, si vous définissez la source sur l'emplacement de l'image, vous pouvez afficher n'importe quelle image.

Il y a une image du logo freeCodeCamp située à `https://avatars0.githubusercontent.com/u/9892522?v=4&s=400`

Vous pouvez la définir comme image en utilisant l'attribut `src`.

```html
<html>
  <head>
    <title>Exemple d'attribut Img Src</title>
  </head>
  <body>
    <img src="https://avatars0.githubusercontent.com/u/9892522?v=4&s=400" />
  </body>
</html>

```

Le code ci-dessus s'affiche comme ceci :

![L'avatar de freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=4&s=400?raw=true)

L'attribut `src` est supporté par tous les navigateurs.

Vous pouvez également avoir un fichier hébergé localement comme image.

Par exemple, `<img src="images/freeCodeCamp.jpeg>` fonctionnerait si vous aviez un dossier appelé `images` qui contient `freeCodeCamp.jpeg`, tant que le dossier 'images' est au même endroit que le fichier `index.html`.

`../files/index.html`

`..files/images/freeCodeCamp.jpeg`

# **Exemple d'entité HTML**

## **Aperçu**

### **Qu'est-ce que les entités HTML ?**

Les entités HTML sont des caractères utilisés pour remplacer les caractères réservés en HTML ou pour des caractères qui n'apparaissent pas sur votre clavier. Certains caractères sont réservés en HTML. Si vous utilisez les signes inférieur à (<) ou supérieur à (>) dans votre texte, le navigateur pourrait les confondre avec des balises.

### **À quoi servent-elles ?**

Comme mentionné, les entités HTML sont utilisées pour remplacer les caractères réservés qui sont réservés par HTML.

### **Comment les utilise-t-on ?**

Une entité de caractère ressemble à ceci :

```html
<!-- format &[nom_entité]; -->
<!-- exemple pour un signe inférieur à (<) -->
&lt;
```

Ou

```html
<!-- &#[numéro_entité]; -->
<!-- exemple pour un signe inférieur à (<) -->
&#60;
```

## **Guide de référence**

Ce n'est en aucun cas une liste exhaustive, mais les liens ci-dessous pourront vous donner plus d'entités si celles ci-dessous ne fonctionnent pas pour vos besoins. Bon codage :bowtie:

```
Caractère	Nom de l'entité	Numéro de l'entité	Description
&#32;	Espace
!		&#33;	Point d'exclamation
2		&#34;	Guillemet
#		&#35;	Signe dièse
$		&#36;	Signe dollar

2	&cent;	&#162;	Signe cent

c	&euro;	&#8364;	Signe euro

3	&pound;	&#163;	Signe GBP

5	&yen;	&#165;	Signe yen
%		&#37;	Signe pourcentage
&	&amp;	&#38;	Esperluette
7		&#39;	Apostrophe
(		&#40;	Parenthèse ouvrante/gauche
)		&#41;	Parenthèse fermante/droite
*		&#42;	Astérisque
+		&#43;	Signe plus
,		&#44;	Virgule
-		&#45;	Trait d'union
.		&#46;	Point
/		&#47;	Barre oblique

9	&copy;	&#169;	Copyright

e	&reg;	&#174;	Marque déposée
2	&quot;	&#34;	Guillemet double
>	&gt;	&#62;	Signe supérieur à
<	&lt;	&#60;	Signe inférieur à
e2	&bull;	&#8226	Puce
```

## **Exemple de formulaire HTML**

En gros, les formulaires sont utilisés pour collecter les données saisies par un utilisateur, qui sont ensuite envoyées au serveur pour un traitement ultérieur. Ils peuvent être utilisés pour différents types de saisies utilisateur, comme le nom, l'email, etc.

Le formulaire contient des éléments de contrôle qui sont enveloppés dans des balises `<form></form>`, comme `input`, qui peut avoir des types comme :

* `text`
* `email`
* `password`
* `checkbox`
* `radio`
* `submit`
* `range`
* `search`
* `date`
* `time`
* `week`
* `color`
* `datalist`

Exemple de code :

```html
<form>
  <label for="username">Nom d'utilisateur :</label>
  <input type="text" name="username" id="username" />
  <label for="password">Mot de passe :</label>
  <input type="password" name="password" id="password" />
  <input type="radio" name="gender" value="male" />Homme<br />
  <input type="radio" name="gender" value="female" />Femme<br />
  <input type="radio" name="gender" value="other" />Autre
  <input list="Options" />
  <datalist id="Options">
    <option value="Option1"></option>
    <option value="Option2"></option>
    <option value="Option3"></option>
  </datalist>

  <input type="submit" value="Soumettre" />
  <input type="color" />
  <input type="checkbox" name="correct" value="correct" />Correct
</form>

```

D'autres éléments que le formulaire peut contenir :

* `textarea` - est une zone multiligne qui est le plus souvent utilisée pour ajouter du texte, par exemple un commentaire. La taille de la zone de texte est définie par le nombre de lignes et de colonnes.
* `select` - avec la balise `<option></option>` crée un menu déroulant de sélection.
* `button` - L'élément bouton peut être utilisé pour définir un bouton cliquable.

PLUS D'INFORMATIONS SUR LES FORMULAIRES HTML.

Les formulaires HTML sont nécessaires lorsque vous souhaitez collecter des données auprès des visiteurs du site. Par exemple, lors de l'inscription d'un utilisateur, vous souhaiteriez collecter des informations telles que le nom, l'adresse e-mail, la carte de crédit, etc.

Un formulaire prendra les données du visiteur du site et les enverra ensuite à une application back-end telle qu'un script CGI, ASP ou PHP, etc. L'application back-end effectuera le traitement requis sur les données transmises en fonction de la logique métier définie dans l'application.

Il existe divers éléments de formulaire disponibles comme des champs de texte, des zones de texte, des menus déroulants, des boutons radio, des cases à cocher, etc.

La balise HTML `<form>` est utilisée pour créer un formulaire HTML et elle a la syntaxe suivante −

```html
<form action="URL du script" method="GET|POST">éléments de formulaire comme input, textarea, etc.</form>

```

Si la méthode du formulaire n'est pas définie, elle sera par défaut "GET".

La balise form peut également avoir un attribut nommé "target" qui spécifie où le lien s'ouvrira. Il peut s'ouvrir dans l'onglet du navigateur, un cadre, ou dans la fenêtre actuelle.

L'attribut action définit l'action à effectuer lorsque le formulaire est soumis. Normalement, les données du formulaire sont envoyées à une page web à l'URL du script lorsque l'utilisateur clique sur le bouton de soumission. Si l'attribut action est omis, l'action est définie sur la page actuelle.

## **Exemple audio HTML5**

Avant HTML5, les fichiers audio devaient être lus dans un navigateur en utilisant un plug-in comme Adobe Flash. Le HTML

L'extrait de code suivant ajoute un fichier audio avec le nom de fichier `tutorial.ogg` ou `tutorial.mp3`. L'élément indique des fichiers audio alternatifs que le navigateur peut choisir. Le navigateur utilisera le premier format reconnu.

#### **Exemple 1**

```html
<audio controls>
  <source src="tutorial.ogg" type="audio/ogg" />
  <source src="tutorial.mp3" type="audio/mpeg" />
  Votre navigateur ne supporte pas l'élément audio.
</audio>

```

#### **Exemple 2**

```html
<audio src="https://s3.amazonaws.com/freecodecamp/simonSound1.mp3" controls loop autoplay></audio>

```

L'attribut `controls` inclut des contrôles audio comme lecture, pause et volume. Si vous n'utilisez pas cet attribut, aucun contrôle ne sera affiché.

L'élément `<source>` vous permet d'indiquer des fichiers audio alternatifs que le navigateur peut choisir. Le navigateur utilisera le premier format reconnu. Le texte entre les balises `<audio>` et `</audio>` peut être affiché dans les navigateurs qui ne supportent pas l'élément HTML5 `<audio>`.

L'attribut autoplay lecture automatiquement votre fichier audio en arrière-plan. Il est considéré comme une meilleure pratique de laisser les visiteurs choisir de lire l'audio.

L'attribut preload indique ce que le navigateur doit faire si le lecteur n'est pas défini sur lecture automatique.

L'attribut loop lecture votre fichier audio en boucle continue si mentionné

Puisque ceci est du HTML5, certains navigateurs ne le supportent pas. Vous pouvez le vérifier sur [https://caniuse.com/#search=audio](https://caniuse.com/#search=audio)

## **Exemple d'éléments sémantiques HTML5**

Les éléments sémantiques HTML décrivent clairement leur signification de manière lisible par l'homme et la machine. Des éléments tels que `<header>`, `<footer>` et `<article>` sont tous considérés comme sémantiques car ils décrivent avec précision le but de l'élément et le type de contenu qui s'y trouve.

### **Un bref historique**

HTML a été créé à l'origine comme un langage de balisage pour décrire des documents sur l'internet naissant. À mesure que l'internet grandissait et était adopté par plus de personnes, ses besoins changeaient. Alors que l'internet était à l'origine destiné au partage de documents scientifiques, les gens voulaient maintenant partager d'autres choses également. Très rapidement, les gens ont commencé à vouloir rendre le web plus beau. Parce que le web n'était pas initialement conçu pour être stylisé, les programmeurs utilisaient différentes astuces pour disposer les éléments de différentes manières. Plutôt que d'utiliser `<table></table>` pour décrire des informations à l'aide d'un tableau, les programmeurs les utilisaient pour positionner d'autres éléments sur une page. À mesure que l'utilisation de mises en page conçues visuellement progressait, les programmeurs ont commencé à utiliser une balise "non sémantique" générique comme `<div>`. Ils donnaient souvent à ces éléments un attribut `class` ou `id` pour décrire leur but. Par exemple, au lieu de `<header>`, cela s'écrivait souvent `<div class="header">`. Comme HTML5 est encore relativement nouveau, cette utilisation d'éléments non sémantiques est encore très courante sur les sites web aujourd'hui.

#### **Liste des nouveaux éléments sémantiques**

Les éléments sémantiques ajoutés dans HTML5 sont :

* `<article>`
* `<aside>`
* `<details>`
* `<figcaption>`
* `<figure>`
* `<footer>`
* `<header>`
* `<main>`
* `<mark>`
* `<nav>`
* `<section>`
* `<summary>`
* `<time>`

Des éléments tels que `<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, et `<footer>` agissent plus ou moins comme des éléments `<div>`. Ils regroupent d'autres éléments en sections de page. Cependant, là où une balise `<div>` pourrait contenir n'importe quel type d'information, il est facile d'identifier quel type d'information irait dans une région sémantique `<header>`.

**Un exemple de mise en page d'éléments sémantiques par w3schools**

![Éléments sémantiques disposant une page par w3schools](https://www.w3schools.com/html/img_sem_elements.gif)

### **Avantages des éléments sémantiques**

Pour examiner les avantages des éléments sémantiques, voici deux morceaux de code HTML. Ce premier bloc de code utilise des éléments sémantiques :

```text
<header></header>
<section>
  <article>
    <figure>
      <img />
      <figcaption></figcaption>
    </figure>
  </article>
</section>
<footer></footer>

```

Alors que ce deuxième bloc de code utilise des éléments non sémantiques :

```text
<div id="header"></div>
<div class="section">
  <div class="article">
    <div class="figure">
      <img />
      <div class="figcaption"></div>
    </div>
  </div>
</div>
<div id="footer"></div>

```

Premièrement, il est beaucoup **plus facile à lire**. C'est probablement la première chose que vous remarquerez en regardant le premier bloc de code utilisant des éléments sémantiques. C'est un petit exemple, mais en tant que programmeur, vous pouvez lire des centaines ou des milliers de lignes de code. Plus il est facile de lire et de comprendre ce code, plus cela facilite votre travail.

Il a une **meilleure accessibilité**. Vous n'êtes pas le seul à trouver les éléments sémantiques plus faciles à comprendre. Les moteurs de recherche et les technologies d'assistance (comme les lecteurs d'écran pour les utilisateurs ayant une déficience visuelle) sont également capables de mieux comprendre le contexte et le contenu de votre site web, ce qui signifie une meilleure expérience pour vos utilisateurs.

Dans l'ensemble, les éléments sémantiques conduisent également à un code plus **cohérent**. Lors de la création d'un en-tête utilisant des éléments non sémantiques, différents programmeurs pourraient écrire cela comme `<div class="header">`, `<div id="header">`, `<div class="head">`, ou simplement `<div>`. Il existe de nombreuses façons de créer un élément d'en-tête, et elles dépendent toutes de la préférence personnelle du programmeur. En créant un élément sémantique standard, cela facilite la tâche de tout le monde.

Depuis octobre 2014, HTML4 a été mis à niveau vers HTML5, avec certains nouveaux éléments "sémantiques". À ce jour, certains d'entre nous peuvent encore être confus quant à la raison pour laquelle tant d'éléments différents qui ne semblent pas montrer de changements majeurs.

#### **`<section>` et `<article>`**

"Quelle est la différence ?", pourriez-vous demander. Ces deux éléments sont utilisés pour sectionner un contenu, et oui, ils peuvent définitivement être utilisés de manière interchangeable. C'est une question de situation. HTML4 n'offrait qu'un seul type d'élément conteneur, qui est `<div>`. Bien que cela soit encore utilisé en HTML5, HTML5 nous a fourni `<section>` et `<article>` pour remplacer `<div>`.

Les éléments `<section>` et `<article>` sont conceptuellement similaires et interchangeables. Pour décider lequel de ceux-ci vous devez choisir, notez ce qui suit :

1. Un article est destiné à être distribuable ou réutilisable de manière indépendante.
2. Une section est un regroupement thématique de contenu.

```html
<section>
  <p>Top Stories</p>
  <section>
    <p>News</p>
    <article>Story 1</article>
    <article>Story 2</article>
    <article>Story 3</article>
  </section>
  <section>
    <p>Sport</p>
    <article>Story 1</article>
    <article>Story 2</article>
    <article>Story 3</article>
  </section>
</section>

```

#### **`<header>` et `<hgroup>`**

L'élément `<header>` se trouve généralement en haut d'un document, d'une section ou d'un article et contient généralement le titre principal et certains outils de navigation et de recherche.

```html
<header>
  <h1>Company A</h1>
  <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact us</a></li>
  </ul>
  <form target="/search">
    <input name="q" type="search" />
    <input type="submit" />
  </form>
</header>

```

L'élément `<hgroup>` doit être utilisé lorsque vous souhaitez un titre principal avec un ou plusieurs sous-titres.

```html
<hgroup>
  <h1>Heading 1</h1>
  <h2>Subheading 1</h2>
  <h2>Subheading 2</h2>
</hgroup>

```

N'OUBLIEZ PAS que l'élément `<header>` peut contenir n'importe quel contenu, mais que l'élément `<hgroup>` ne peut contenir que d'autres en-têtes, c'est-à-dire de `<h1>` à `<h6>` et y compris `<hgroup>`.

#### **`<aside>`**

L'élément `<aside>` est destiné au contenu qui ne fait pas partie du flux du texte dans lequel il apparaît, mais qui y est tout de même lié d'une certaine manière. Considérez `<aside>` comme une barre latérale à votre contenu principal.

```html
<aside>
  <p>
    Ceci est une barre latérale, par exemple une définition de terminologie ou un court arrière-plan d'une figure historique.
  </p>
</aside>

```

Avant HTML5, nos menus étaient créés avec des `<ul>` et des `<li>`. Maintenant, avec ceux-ci, nous pouvons séparer nos éléments de menu avec un `<nav>`, pour la navigation entre vos pages. Vous pouvez avoir n'importe quel nombre d'éléments `<nav>` sur une page, par exemple, il est courant d'avoir une navigation globale en haut (dans le `<header>`) et une navigation locale dans une barre latérale (dans un élément `<aside>`).

```html
<nav>
  <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact us</a></li>
  </ul>
</nav>

```

#### **`<footer>`**

S'il y a un `<header>`, il doit y avoir un `<footer>`. Un `<footer>` se trouve généralement en bas d'un document, d'une section ou d'un article. Tout comme le `<header>`, le contenu est généralement des métainformations, telles que les détails de l'auteur, les informations légales et/ou les liens vers des informations connexes. Il est également valide d'inclure des éléments `<section>` dans un pied de page.

```html
<footer>&copy;Company A</footer>
```

#### **`<small>`**

L'élément `<small>` apparaît souvent dans un élément `<footer>` ou `<aside>` qui contiendrait généralement des informations de copyright ou des mentions légales, et d'autres petits caractères. Cependant, cela n'est pas destiné à rendre le texte plus petit. Il décrit simplement son contenu, sans prescrire la présentation.

```html
<footer><small>&copy;Company A</small> Date</footer>
```

#### **`<time>`**

L'élément `<time>` permet de joindre une date ISO 8601 non ambiguë à une version lisible par l'homme de cette date.

```html
<time datetime="2017-10-31T11:21:00+02:00">Mardi, 31 octobre 2017</time>
```

Pourquoi s'embêter avec `<time>` ? Alors que les humains peuvent lire l'heure qui peut être désambiguïée par le contexte de manière normale, les ordinateurs peuvent lire la date ISO 8601 et voir la date, l'heure et le fuseau horaire.

#### **`<figure>` et `<figcaption>`**

`<figure>` est utilisé pour envelopper votre contenu d'image, et `<figcaption>` est utilisé pour légender votre image.

```html
<figure>
  <img src="https://en.wikipedia.org/wiki/File:Shadow_of_Mordor_cover_art.jpg" alt="Shadow of Mordor" />
  <figcaption>Art de couverture pour Middle-earth: Shadow of Mordor</figcaption>
</figure>
```

## **Exemple vidéo HTML5**

Avant HTML5, pour avoir une vidéo qui joue dans une page web, vous deviez utiliser un plugin, comme Adobe Flash Player. Avec l'introduction de HTML5, vous pouvez maintenant la placer directement dans la page elle-même. Le HTML

Pour intégrer un fichier vidéo dans une page web, ajoutez simplement cet extrait de code et changez la source du fichier audio.

```html
<video controls>
  <source src="tutorial.ogg" type="video /ogg" />
  <source src="tutorial.mp4" type="video /mpeg" />
  Votre navigateur ne supporte pas l'élément vidéo. Veuillez le mettre à jour vers la dernière version.
</video>

```

L'attribut controls inclut des contrôles vidéo, similaires à lecture, pause et volume.

Cette fonctionnalité est supportée par tous les navigateurs modernes/mis à jour. Cependant, tous ne supportent pas le même format de fichier vidéo. Ma recommandation pour une large gamme de compatibilité est MP4, car c'est le format le plus largement accepté. Il existe également deux autres formats (WebM et Ogg) qui sont supportés dans Chrome, Firefox et Opera.

L'élément vous permet d'indiquer des fichiers vidéo alternatifs que le navigateur peut choisir. Le navigateur utilisera le premier format reconnu. En HTML5, il y a 3 formats vidéo supportés : MP4, WebM et Ogg.

Le texte entre les balises ne sera affiché que dans les navigateurs qui ne supportent pas l'élément

Il existe plusieurs éléments différents de la balise vidéo, beaucoup de ces explications sont basées sur les documents web de Mozilla (liés ci-dessous). Il y en a encore plus si vous cliquez sur le lien en bas.

#### **autoplay**

"autoplay" peut être défini sur vrai ou faux. Vous le définissez sur vrai en l'ajoutant dans la balise, s'il n'est pas présent dans la balise, il est défini sur faux. Si défini sur vrai, la vidéo commencera à jouer dès que suffisamment de la vidéo aura été mise en mémoire tampon pour pouvoir être lue. De nombreuses personnes trouvent les vidéos en lecture automatique perturbatrices ou ennuyeuses, utilisez donc cette fonctionnalité avec parcimonie. Notez également que certains navigateurs mobiles, comme Safari pour iOS, ignorent cet attribut.

```html
<video autoplay>
  <source src="video.mp4" type="video/mp4" />
</video>

```

#### **poster**

L'attribut "poster" est l'image qui s'affiche sur la vidéo jusqu'à ce que l'utilisateur clique pour la lire.

```html
<video poster="poster.png">
  <source src="video.mp4" type="video/mp4" />
</video>

```

#### **controls**

L'attribut "controls" peut être défini sur vrai ou faux et gérera si des contrôles tels que le bouton lecture/pause ou le curseur de volume apparaissent. Vous le définissez sur vrai en l'ajoutant dans la balise, s'il n'est pas présent dans la balise, il est défini sur faux.

```html
<video controls>
  <source src="video.mp4" type="video/mp4" />
</video>

```

Il existe de nombreux autres attributs qui peuvent être ajoutés et qui sont facultatifs pour personnaliser le lecteur vidéo dans la page. Pour en savoir plus, cliquez sur les liens ci-dessous.

## **Exemple de stockage Web HTML5**

Le stockage Web permet aux applications Web de stocker jusqu'à 5 Mo d'informations dans le stockage du navigateur par origine (par domaine et protocole).

### **Types de stockage Web**

Il existe deux objets pour stocker des données sur le client :

`window.localStorage` : stocke les données sans date d'expiration et vit jusqu'à ce qu'elles soient supprimées.

```javascript
// Stocker un élément
localStorage.setItem("foo", "bar");

// Obtenir un élément
localStorage.getItem("foo"); // retourne "bar"
```

`window.sessionStorage` : stocke les données pour une session, où les données sont perdues lorsque le navigateur/onglet du navigateur est fermé.

```javascript
// Stocker un élément
sessionStorage.setItem("foo", "bar");

// Obtenir un élément
sessionStorage.getItem("foo"); // retourne "bar"
```

Puisque l'implémentation actuelle ne supporte que les mappages chaîne à chaîne, vous devez sérialiser et désérialiser d'autres structures de données.

Vous pouvez le faire en utilisant JSON.stringify() et JSON.parse().

Par exemple, pour le JSON donné

```text
var jsonObject = { 'one': 1, 'two': 2, 'three': 3 };
```

Nous convertissons d'abord l'objet JSON en chaîne et le sauvegardons dans le stockage local :

```text
localStorage.setItem('jsonObjectString', JSON.stringify(jsonObject));
```

Pour obtenir l'objet JSON à partir de la chaîne stockée dans le stockage local :

```text
var jsonObject = JSON.parse(localStorage.getItem('jsonObjectString'));
```

## **Exemple de liens Mailto**

Un lien mailto est un type de lien hypertexte (`<a href=""></a>`) avec des paramètres spéciaux qui vous permettent de spécifier des destinataires supplémentaires, une ligne d'objet et/ou un texte de corps.

### **La syntaxe de base avec un destinataire est :**

```html
<a href="mailto:friend@something.com">Some text</a>
```

### **Plus de personnalisation !**

#### **Ajouter un sujet à ce mail :**

Si vous souhaitez ajouter un sujet spécifique à ce mail, faites attention à ajouter `%20` ou `+` partout où il y a un espace dans la ligne de sujet. Une façon facile de s'assurer qu'il est correctement formaté est d'utiliser un [décodeur/encodeur d'URL](https://meyerweb.com/eric/tools/dencoder/).

#### **Ajouter un texte de corps :**

De même, vous pouvez ajouter un message spécifique dans la partie corps de l'email : Encore une fois, les espaces doivent être remplacés par `%20` ou `+`. Après le paramètre de sujet, tout paramètre supplémentaire doit être précédé de `&`

Exemple : Supposons que vous souhaitiez que les utilisateurs envoient un email à leurs amis sur leurs progrès chez Free Code Camp :

Adresse : vide

Sujet : Bonne nouvelle

Corps : Je deviens développeur

Votre lien html maintenant :

```html
<a href="mailto:?subject=Great%20news&body=I%20am%20becoming%20a%20developer">Envoyer un mail !</a>
```

Ici, nous avons laissé mailto vide (`mailto:?`). Cela ouvrira le client de messagerie de l'utilisateur et l'utilisateur ajoutera lui-même l'adresse du destinataire.

#### **Ajouter plus de destinataires :**

De la même manière, vous pouvez ajouter des paramètres CC et BCC. Séparez chaque adresse par une virgule !

Les paramètres supplémentaires doivent être précédés de `&`.

```html
<a href="mailto:firstfriend@something.com?subject=Great%20news&cc=secondfriend@something.com,thirdfriend@something.com&bcc=fourthfriend@something.com">Envoyer un mail !</a>
```

## **Merci d'avoir utilisé cette référence HTML. Bon codage !**
---
title: Les attributs HTML expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T18:45:00.000Z'
originalURL: https://freecodecamp.org/news/html-attributes-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d3a740569d1a4ca3699.jpg
tags:
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
seo_title: Les attributs HTML expliqués
seo_desc: 'HTML elements can have attributes, which contain additional information
  about the element.

  HTML attributes generally come in name-value pairs, and always go in the opening
  tag of an element. The attribute name says what type of information you’re pro...'
---

Les éléments HTML peuvent avoir des attributs, qui contiennent des informations supplémentaires sur l'élément.

Les attributs HTML sont généralement sous forme de paires nom-valeur, et vont toujours dans la balise d'ouverture d'un élément. Le nom de l'attribut indique le type d'information que vous fournissez sur l'élément, et la valeur de l'attribut est l'information réelle.

Par exemple, un élément d'ancrage (`<a>`) dans un document HTML crée des liens vers d'autres pages, ou d'autres parties de la page. Vous utilisez l'attribut `href` dans la balise d'ouverture `<a>` pour indiquer au navigateur où le lien envoie un utilisateur.

Voici un exemple de lien qui envoie les utilisateurs vers la page d'accueil de freeCodeCamp :

```html
<a href="www.freecodecamp.org">Cliquez ici pour aller à freeCodeCamp !</a>
```

Remarquez que le nom de l'attribut (`href`) et la valeur ("www.freecodecamp.org") sont séparés par un signe égal, et des guillemets entourent la valeur.

Il existe de nombreux attributs HTML différents, mais la plupart d'entre eux ne fonctionnent que sur certains éléments HTML. Par exemple, l'attribut `href` ne fonctionnera pas s'il est placé dans une balise d'ouverture `<h1>`.

Dans l'exemple ci-dessus, la valeur fournie à l'attribut `href` pourrait être n'importe quel lien valide. Cependant, certains attributs n'ont qu'un ensemble d'options valides que vous pouvez utiliser, ou les valeurs doivent être dans un format spécifique. L'attribut `lang` indique au navigateur la langue par défaut du contenu dans un élément HTML. Les valeurs pour l'attribut `lang` doivent utiliser des codes de langue ou de pays standard, tels que `en` pour l'anglais, ou `it` pour l'italien.

## **Attributs booléens**

Certains attributs HTML n'ont pas besoin de valeur car ils n'ont qu'une seule option. Ce sont des attributs booléens. La présence de l'attribut dans une balise l'appliquera à cet élément HTML. Cependant, il est acceptable d'écrire le nom de l'attribut et de le définir égal à la seule option de la valeur. Dans ce cas, la valeur est généralement la même que le nom de l'attribut.

Par exemple, l'élément `<input>` dans un formulaire peut avoir un attribut `required`. Cela oblige les utilisateurs à remplir cet élément avant de pouvoir soumettre le formulaire.

Voici des exemples qui font la même chose :

```html
<input type="text" required >
<input type="text" required="required" >
```

Vous pouvez en savoir plus sur les attributs <a href>, <a target>, <script> src, et roll ici :

## [Attribut <a href>](https://www.freecodecamp.org/news/the-a-href-attribute-explained/)

## [Attribut <script> src](https://www.freecodecamp.org/news/link-javascript-to-html-with-the-src/)

## [Attribut roll](https://www.freecodecamp.org/news/html-role-attribute/)

## [Attribut <a target>](https://www.freecodecamp.org/news/the-a-target-html-attribute-explained/)



Maintenant, apprenons-en plus sur certains autres attributs HTML :

## **Attribut Align de P**

### **Important**

Cet attribut n'est pas supporté en HTML5. Il est recommandé d'utiliser la propriété CSS [`text-align`](https://guide.freecodecamp.org/css/text-align).

Pour aligner le texte à l'intérieur d'une balise `<p>`, cet attribut sera utile.

### **Syntaxe**

```html
<p align="position">Lorem Ipsum...</p>
```

### **Attributs**

* **left** - Le texte est aligné à gauche
* **right** - Le texte est aligné à droite
* **center** - Le texte est aligné au centre
* **justify** - Toutes les lignes de texte ont une largeur égale

### **Exemple**

```html
<html>
<body>
<p align="center">Exemple d'attribut d'alignement de paragraphe</p>
</body>
</html>
```

## **Attribut Src de Img**

L'attribut `<img src>` fait référence à la source de l'image que vous souhaitez afficher. La balise `img` n'affichera pas d'image sans l'attribut `src`. Cependant, si vous définissez la source à l'emplacement de l'image, vous pouvez afficher n'importe quelle image.

Il y a une image du logo freeCodeCamp située à `https://avatars0.githubusercontent.com/u/9892522?v=4&s=400`

Vous pouvez la définir comme image en utilisant l'attribut `src`.

```html
<html>
  <head>
    <title>Exemple d'attribut Src de Img</title>
  </head>
  <body>
    <img src="https://avatars0.githubusercontent.com/u/9892522?v=4&s=400">
  </body>
</html>
```

Le code ci-dessus s'affiche comme ceci :

![L'avatar de freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=4&s=400?raw=true)

L'attribut `src` est supporté par tous les navigateurs.

Vous pouvez également avoir un fichier hébergé localement comme votre image.

Par exemple, `<img src="images/freeCodeCamp.jpeg>` fonctionnerait si vous aviez un dossier appelé `images` qui contenait `freeCodeCamp.jpeg`, tant que le dossier 'images' était au même endroit que le fichier `index.html`.

`../files/index.html`

`..files/images/freeCodeCamp.jpeg`

## **Attribut Size de Font**

Cet attribut spécifie la taille de la police sous forme de valeur numérique ou relative. Les valeurs numériques vont de `1` à `7`, `1` étant la plus petite et `3` la valeur par défaut. Elle peut également être définie en utilisant une valeur relative, comme `+2` ou `-3`, qui la définissent par rapport à la valeur de l'attribut size de l'élément `<basefont>`, ou par rapport à `3`, la valeur par défaut, si aucun n'existe.

Syntaxe :

`<font size="number">`

Exemple :

```html
<html>
  <body>
    <font size="6">Ceci est un texte !</font>
  </body>
</html>
```

Note : `L'attribut size de <font> n'est pas supporté en HTML5. Utilisez CSS à la place.`

## **Attribut Color de Font**

Cet attribut est utilisé pour définir une couleur au texte enfermé dans une balise `<font>`.

### **Syntaxe :**

html

```text

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

## **Attribut Autofocus** 

L'attribut **autofocus** est un attribut booléen.

Lorsqu'il est présent, il spécifie que l'élément doit automatiquement recevoir le focus d'entrée lorsque la page se charge.

Un seul élément de formulaire dans un document peut avoir l'attribut **autofocus**. Il ne peut pas être appliqué à `<input type="hidden">`.

### **S'applique à**

ElementAttribute`<button>`autofocus`<input>`autofocus`<select>`autofocus`<textarea>`autofocus

### **Exemple**

```html
<form>
    <input type="text" name="fname" autofocus>
    <input type="text" name="lname">
</form>
```

### **Compatibilité**

Il s'agit d'un attribut HTML5.

## **Attribut d'événement Onclick**

Lorsque l'élément est cliqué, un événement est déclenché.

Il fonctionne comme la méthode _onclick_ ou `addEventListener('click')` sur l'élément.

```html
<element onclick="event"></element>
```

`event` peut être une fonction JavaScript ou vous pouvez écrire du JavaScript brut

### **Exemples**

Changer la couleur d'un élément `<p>` lorsqu'il est cliqué

```html
<p id="text" onclick="redify()">Changez ma couleur</p>

<script>
function redify(){
  let text = document.querySelector('#text');
  text.style.color = "red";
}
</script>
```

Utilisation de l'attribut onclick avec du JavaScript brut :

```html
<button onclick="alert('Hello')">Bonjour le monde</button>
```

## **Attribut Align de Img**

L'attribut align d'une image spécifie où l'image doit être alignée selon l'élément environnant.

Valeurs de l'attribut :  
right - Aligner l'image à droite left - Aligner l'image à gauche  
top - Aligner l'image en haut  
bottom - Aligner l'image en bas  
middle - Aligner l'image au milieu

Par exemple :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
   <title>Attribut Align de Img</title>
 </head>
<body>
  <p>Ceci est un exemple. <img src="image.png" alt="Image" align="middle"> Plus de texte ici
  <img src="image.png" alt="Image" width="100"/>
  </body>
</html>
```

Nous pouvons également aligner à droite si nous le souhaitons :

```html
<p>Ceci est un autre exemple<img src="image.png" alt="Image" align="right"></p>
```

**Veuillez noter que l'attribut align n'est pas supporté en HTML5, et vous devriez utiliser CSS à la place. Cependant, il est toujours supporté par tous les principaux navigateurs.**

## **Attribut Type de Input**

L'attribut type de input spécifie le type de l'entrée que l'utilisateur doit mettre dans votre formulaire.

### **text**

Une ligne de texte.

```html
    <form>
      <label for="login">Login :</label>
      <input type="text" name="login">
    </form>
```

### **password**

Une ligne de texte. Le texte est automatiquement affiché comme une série de points ou d'astérisques (dépend du navigateur et du système d'exploitation).

```html
    <form>
      <label for="password">Mot de passe :</label>
      <input type="password" name="password">
    </form>
```

### **email**

Le HTML vérifie si l'entrée correspond au format de l'adresse e-mail (quelquechose@quelquechose).

```html
    <form>
      <label for="email">Adresse e-mail :</label>
      <input type="email" name="email">
    </form>
```

### **number**

Autorise uniquement l'entrée numérique. Vous pouvez également spécifier les valeurs minimale et maximale autorisées. L'exemple ci-dessous vérifie que l'entrée est un nombre compris entre 1 et 120.

```html
    <form>
      <label for="age">Âge :</label>
      <input type="number" name="age" min="1" max="120">
    </form>
```

### **radio**

Une seule option peut être sélectionnée par l'utilisateur. Le groupe de boutons radio doit avoir le même attribut name. Vous pouvez sélectionner automatiquement une option en utilisant la propriété `checked` (dans l'exemple ci-dessous, la valeur Blue est sélectionnée).

```html
    <form>
      <label><input type="radio" name="color" value="red">Rouge</label>
      <label><input type="radio" name="color" value="green">Vert</label>
      <label><input type="radio" name="color" value="blue" checked>Bleu</label>
    </form>
```

### **checkbox**

L'utilisateur peut sélectionner zéro ou plusieurs options parmi le groupe de cases à cocher. Vous pouvez utiliser la propriété `checked` ici aussi pour une ou plusieurs options.

```html
    <form>
      <label><input type="checkbox" name="lang" value="english">anglais</label>
      <label><input type="checkbox" name="lang" value="spanish">espagnol</label>
      <label><input type="checkbox" name="lang" value="french">français</label>
    </form>
```

### **button**

L'entrée est affichée comme un bouton, le texte qui doit être affiché dans le bouton est dans l'attribut value.

```html
    <form>
      <input type="button" value="cliquez ici">
    </form>
```

### **submit**

Affiche le bouton de soumission. Le texte qui doit être affiché dans le bouton est dans l'attribut value. Après avoir cliqué sur le bouton, le HTML effectue la validation et si elle réussit, le formulaire est soumis.

```html
    <form>
      <input type="submit" value="SOUMETTRE">
    </form>
```

### **reset**

Affiche le bouton de réinitialisation. Le texte qui doit être affiché dans le bouton est dans l'attribut value. Après avoir cliqué sur le bouton, toutes les valeurs du formulaire sont supprimées.

```html
    <form>
      <input type="reset" value="ANNULER">
    </form>
```

Il existe d'autres types d'éléments.

## Autres attributs HTML :

### [Attribut <script> src](https://www.freecodecamp.org/news/link-javascript-to-html-with-the-src/)

### [Attribut roll](https://www.freecodecamp.org/news/html-role-attribute/)

### [Attribut <a href>](https://www.freecodecamp.org/news/the-a-href-attribute-explained/)

### [Attribut <a target>](https://www.freecodecamp.org/news/the-a-target-html-attribute-explained/)





##
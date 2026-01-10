---
title: Centrage d'image en CSS – Comment centrer une image dans une div
date: '2022-08-16T19:32:10.000Z'
author: Joel Olawanle
authorURL: https://www.freecodecamp.org/news/author/joel-olawanle/
originalURL: https://freecodecamp.org/news/how-to-center-an-image-in-a-div-css
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template.png
tags:
- name: CSS
  slug: css
- name: css flex
  slug: css-flex
- name: flexbox
  slug: flexbox
- name: Web Development
  slug: web-development
seo_desc: 'When you''re working on the front-end of a web page, you sometimes need
  to center an image within a div (container).

  This can become tricky at times. And based on certain conditions, a particular method
  may not work at some point, leaving you searchin...'
---


Lorsque vous travaillez sur le front-end d'une page web, vous avez parfois besoin de centrer une image à l'intérieur d'une `div` (conteneur).

<!-- more -->

Cela peut parfois s'avérer délicat. Selon certaines conditions, une méthode particulière peut ne pas fonctionner à un moment donné, vous obligeant à chercher des alternatives.

Dans cet article, vous apprendrez comment centrer une image dans une `div` avec CSS.

## Comment centrer une `div` avec CSS

Vous pouvez centrer une image dans une `div` de deux manières : horizontalement et verticalement. En combinant ces deux méthodes, vous obtiendrez une image parfaitement centrée :

![s_E4F69027FF573CB7A65859895F7B6CD8342925344584ACB8BE37F8B299430A72_1660599829888_Untitled](https://paper-attachments.dropbox.com/s_E4F69027FF573CB7A65859895F7B6CD8342925344584ACB8BE37F8B299430A72_1660599829888_Untitled.png)

Par défaut, le contenu web commence toujours dans le coin supérieur gauche de l'écran et s'affiche en `ltr` (de gauche à droite) – sauf pour certaines langues comme l'arabe, qui s'affiche en `rtl` (de droite à gauche).

Commençons par voir comment centrer horizontalement une image dans une `div`. Ensuite, nous verrons comment la centrer verticalement. Enfin, nous verrons comment combiner les deux.

![s_E4F69027FF573CB7A65859895F7B6CD8342925344584ACB8BE37F8B299430A72_1660702367688_image](https://paper-attachments.dropbox.com/s_E4F69027FF573CB7A65859895F7B6CD8342925344584ACB8BE37F8B299430A72_1660702367688_image.png)

### Comment centrer horizontalement une image dans une div avec text-align

Supposons que vous ayez une `div` dans laquelle vous placez votre image de cette façon :

```html
<div class="container">
    <img src="./fcc-logo.png" alt="FCC Logo" />
</div>
```

Et que vous appliquiez un style CSS de base pour que votre image soit visible :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
}
.container img {
    width: 100px;
}
```

La méthode `text-align` ne fonctionnera pas dans tous les cas, car on l'utilise généralement pour centrer du texte. Mais lorsque vos images se trouvent dans un conteneur de type bloc comme une `div`, cette méthode fonctionnera :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    text-align: center;
}

.container img {
    width: 100px;
}
```

Cela fonctionne en ajoutant la propriété `text-align` avec la valeur `center` au conteneur et non à l'image elle-même.

### Comment centrer horizontalement une image dans une div avec margin-auto

Une autre méthode que vous pouvez utiliser pour centrer horizontalement une image dans une `div` (conteneur) est la propriété `margin` avec la valeur `auto`.

L'élément occupera alors la largeur **spécifiée** (`width`), et l'espace restant sera réparti également entre les marges gauche et droite.

Vous devriez normalement appliquer cette méthode à l'image elle-même et non au conteneur. Malheureusement, cette propriété seule ne suffit pas. Vous devez également spécifier d'abord la largeur (`width`) que l'image occupera. Cela permet à la marge de connaître la largeur restante du conteneur afin qu'elle puisse être divisée équitablement.

Deuxièmement, `img` est un élément inline, et la propriété `margin-auto` n'affecte pas les éléments de niveau inline. Cela signifie que vous devez d'abord le convertir en un élément de niveau bloc avec la propriété `display` définie sur `block`.

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
}

.container img {
    width: 100px;
    margin: auto;
    display: block;
}
```

### Comment centrer horizontalement une image dans une div avec les propriétés position et transform

Une autre méthode pour positionner une image horizontalement est la propriété `position` combinée à la propriété `transform`.

Cette méthode peut être très complexe, mais elle fonctionne. Vous devez d'abord définir la `position` du conteneur sur `relative`, puis celle de l'image sur `absolute`.

Une fois cela fait, vous pouvez déplacer l'image vers n'importe quelle position souhaitée en utilisant les propriétés `left`, `top`, `bottom` ou `right` sur l'image.

Dans ce cas, vous voulez seulement déplacer l'image au centre horizontalement. Cela signifie que vous déplaceriez l'image via `left` à 50 % ou `right` à -50 % :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    position: relative;
}

.container img {
    width: 100px;
    height: 100px;
    position: absolute;
    left: 50%;
}
```

Mais en vérifiant votre image, vous remarquerez qu'elle n'est toujours pas parfaitement placée au centre. C'est parce qu'elle a commencé à partir de la marque des 50 %, qui est la position centrale.

Dans ce cas, vous devez utiliser la propriété `transform-translateX` pour l'ajuster et obtenir un centrage horizontal parfait :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    position: relative;
}

.container img {
    width: 100px;
    height: 100px;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
}
```

### Comment centrer horizontalement une image dans une div avec display-flex

Le flexbox CSS facilite la conception de structures de mise en page flexibles et responsives sans utiliser `float` ou le positionnement. Nous pouvons également l'utiliser pour placer une image au centre horizontal d'un conteneur en utilisant la propriété `display` avec `flex` comme valeur.

Mais cela ne suffit pas seul. Vous devez également définir la position où vous voulez votre image. Cela pourrait être `center`, `left` ou peut-être `right` :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    display: flex;
    justify-content: center;
}

.container img {
    width: 100px;
    height: 100px;
}
```

**Note :** La propriété `display: flex` n'est pas supportée par les anciennes versions des navigateurs. Vous pouvez en lire plus [ici][1]. Vous remarquerez également que la largeur et la hauteur de l'image sont définies pour garantir que l'image ne rétrécisse pas.

Apprenons maintenant comment centrer une image verticalement dans une `div`. Plus tard, nous verrons comment centrer une image horizontalement et verticalement ensemble, pour un centrage parfait.

![s_E4F69027FF573CB7A65859895F7B6CD8342925344584ACB8BE37F8B299430A72_1660702330431_image](https://paper-attachments.dropbox.com/s_E4F69027FF573CB7A65859895F7B6CD8342925344584ACB8BE37F8B299430A72_1660702330431_image.png)

### Comment centrer verticalement une image dans une div avec display-flex

Tout comme vous avez pu centrer l'image horizontalement avec la méthode `display-flex`, vous pouvez faire de même verticalement.

Mais cette fois-ci, vous n'aurez pas besoin d'utiliser la propriété `justify-content`. Vous utiliserez plutôt la propriété `align-items` :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    display: flex;
    align-items: center;
}

.container img {
    width: 100px;
    height: 100px;
}
```

Pour que cette méthode fonctionne, le conteneur doit avoir une hauteur (`height`) spécifiée que vous utiliserez pour calculer la hauteur et savoir où se trouve le centre.

### Comment centrer verticalement une image dans une div avec les propriétés position et transform

De la même manière que vous avez utilisé les propriétés `position` et `transform` précédemment pour placer votre image au centre horizontalement, vous pouvez faire de même verticalement.

Mais cette fois, vous n'utiliserez pas `left` ou `right`. À la place, vous utiliserez `top` ou `bottom` avec `translateY` plutôt que `translateX` :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    position: relative;
}

.container img {
    width: 100px;
    height: 100px;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
}
```

Vous avez appris comment centrer une image dans une `div` horizontalement et verticalement en utilisant toutes les méthodes possibles. Apprenons maintenant comment centrer à la fois horizontalement et verticalement.

![s_E4F69027FF573CB7A65859895F7B6CD8342925344584ACB8BE37F8B299430A72_1660702293626_image](https://paper-attachments.dropbox.com/s_E4F69027FF573CB7A65859895F7B6CD8342925344584ACB8BE37F8B299430A72_1660702293626_image.png)

### Comment centrer horizontalement et verticalement une image dans une div avec display-flex

La propriété `display-flex` est une combinaison des méthodes de centrage vertical et horizontal.

Pour la méthode flex, cela signifie que vous utiliserez à la fois les propriétés `justify-content` et `align-items` définies sur `center` :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container img {
    width: 100px;
    height: 100px;
}
```

### Comment centrer horizontalement et verticalement une image dans une div avec les propriétés position et transform

C'est également très similaire, car il suffit de combiner les deux façons de centrer verticalement et horizontalement :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    position: relative;
}

.container img {
    width: 100px;
    height: 100px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%) translateY(-50%);
}
```

Vous pouvez également combiner `translateX` et `translateY` en utilisant `translate(x,y)` :

```css
.container {
    width: 200px;
    height: 200px;
    background-color: #0a0a23;
    position: relative;
}

.container img {
    width: 100px;
    height: 100px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

## Conclusion

Dans cet article, vous avez appris comment centrer une image dans une div verticalement, horizontalement ou les deux.

Vous utiliserez souvent la méthode Flexbox pour centrer une image, car la méthode `position` peut déformer votre page web et s'avère complexe à manipuler.

Vous pouvez en apprendre davantage sur la [méthode de positionnement CSS ici][2] et sur la [méthode flexbox ici.][3]

Bon code !

[1]: https://caniuse.com/#search=display%20flex
[2]: https://www.freecodecamp.org/news/css-position-property-explained/
[3]: https://www.freecodecamp.org/news/css-flexbox-tutorial-with-cheatsheet/
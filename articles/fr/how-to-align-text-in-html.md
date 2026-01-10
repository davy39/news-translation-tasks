---
title: Comment aligner du texte en HTML – Exemples de text-align, centré et justifié
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-22T16:02:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-align-text-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--8-.png
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: Comment aligner du texte en HTML – Exemples de text-align, centré et justifié
seo_desc: 'Text is essential on web pages, as it tells your users what your web page
  is all about.

  When you add text to your web page, it dictates the direction and feel of your web
  page based on your language.

  For example, by default, English moves from left t...'
---

Le texte est essentiel sur les pages web, car il indique à vos utilisateurs le sujet de votre page web.

Lorsque vous ajoutez du texte à votre page web, il dicte la direction et l'aspect de votre page en fonction de votre langue.

Par exemple, par défaut, l'anglais s'écrit de gauche à droite (LTR), tandis que l'arabe s'écrit de droite à gauche (RTL).

Mais la plupart du temps, vous ne voudrez pas que tout votre texte reste dans une seule position de votre écran ou conteneur. Vous voudrez que certains soient au centre, d'autres à gauche et d'autres à droite. Vous pourriez même vouloir que le texte remplisse votre page ou conteneur.

C'est similaire à ce que vous faites lors de l'édition de textes dans Microsoft Word ou Google Docs, en utilisant les boutons d'alignement à gauche, à droite, au centre et justifié.

Vous pouvez également faire de même sur vos pages web en utilisant du code.

## Comment aligner du texte au centre avant l'HTML5

Avant l'introduction de l'HTML5, les développeurs effectuaient des styles spécifiques avec des balises HTML. Par exemple, vous pouviez utiliser la balise center pour aligner votre texte au centre, mais dans l'HTML4, cette balise est devenue obsolète. Bien que cela puisse encore fonctionner avec certains navigateurs majeurs, elle pourrait être supprimée à tout moment.

Voici à quoi cela ressemble :

```html
<center>
  <h1> Welcome to freeCodeCamp </h1>

  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>

  <h3>How we work</h3>

  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>
</center>
```

Cela affichera tout notre texte au centre de la page ou de n'importe quel conteneur auquel il est appliqué :

![](https://paper-attachments.dropbox.com/s_1FCD88D32AEADC1D26B97285FE174892A040B3C1BC2D3128B4E56D61375B2EDB_1663883648627_image.png align="left")

Mais maintenant que nous avons l'HTML5, nous n'utilisons plus cette méthode. Rappelez-vous qu'il est essentiel de toujours gérer tous les styles avec CSS. Vous ne devriez utiliser l'HTML que pour ajouter du balisage à votre page web.

## Comment aligner du texte en HTML5

Avec CSS, vous avez de nombreuses options que vous pouvez utiliser pour aligner votre texte. La principale propriété CSS qui fonctionne bien avec l'alignement du texte est la propriété `text-align`. Vous utilisez cette propriété pour spécifier l'alignement **horizontal** du texte dans un élément.

Supposons que vous ayez du texte sur votre page web, par exemple :

```html
<h1> Welcome to freeCodeCamp </h1>

<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.

  Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>

<h3>How we work</h3>

<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>
```

Vous pouvez utiliser la propriété `text-align` pour déplacer le texte vers la gauche, la droite, le centre, ou même justifier votre contenu, afin qu'il remplisse l'élément ou la page web **horizontalement**.

```css
// Syntaxe

text-align: start;
text-align: end;
text-align: left;
text-align: right;
text-align: center;
text-align: justify;
```

Si vous souhaitez aligner l'ensemble du texte de votre page web, vous pouvez appliquer cette propriété à n'importe quelle balise contenant le texte, telle que la balise div, un titre, un paragraphe ou la balise body.

Avant de voir un exemple, explorons les options/valeurs disponibles pour cette propriété.

* `start` : Ceci est basé sur la direction. Lorsque la direction est de gauche à droite, `start` signifie `left`. Si la direction est de droite à gauche, alors `start` signifie `right`.
    
* `end` : Ceci est également basé sur la direction. Lorsque la direction est de gauche à droite, alors `end` signifie `right`. Si la direction est de droite à gauche, alors `end` signifie `left`.
    
* `left` : Vous utilisez ceci pour aligner les textes sur le bord `gauche` de la page ou du conteneur.
    
* `right` : Vous utilisez ceci pour aligner les textes sur le bord `droit` de la page ou du conteneur.
    
* `center` : Vous utilisez ceci pour aligner les textes au `centre` parfait de la page ou du conteneur.
    
* `justify` : Vous utilisez ceci pour ajuster le contenu du texte afin qu'il touche les bords gauche et droit de votre page ou conteneur.
    

La syntaxe générale serait :

```css
selector {
  text-align: value;
}
```

### Comment aligner du texte à gauche

Vous pourriez avoir besoin de changer l'alignement de votre texte vers la gauche s'il se trouve initialement sur le côté droit. Vous faites cela en ciblant le sélecteur et en utilisant la propriété `text-align` avec `left` comme valeur.

```html
// HTML
<p> Welcome to freeCodeCamp </p>

// CSS
p {
  text-align: left;
}
```

Par exemple, si vous avez votre contenu à partir de la droite de votre écran en utilisant la direction RTL :

```html
<html dir="rtl">
  <body>
    <h1> Welcome to freeCodeCamp </h1>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.
      
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>
      
      <h3>How we work</h3>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>
  </body>
</html>
```

Cela affichera :

![](https://paper-attachments.dropbox.com/s_1FCD88D32AEADC1D26B97285FE174892A040B3C1BC2D3128B4E56D61375B2EDB_1663885469001_image.png align="left")

Vous pouvez styliser la balise body pour aligner le texte de la page vers la `gauche` :

```css
body{
  text-align: left;
}
```

### Comment aligner du texte à droite

Par défaut, votre page web ou le contenu du conteneur et d'autres éléments commencent par la gauche. Vous pourriez vouloir aligner ce contenu vers la droite, ce qui est accessible en utilisant la propriété `text-align` avec la valeur `right`.

```html
// HTML
<p> Welcome to freeCodeCamp </p>

// CSS
p {
  text-align: right;
}
```

### Comment aligner du texte au centre

Au lieu d'utiliser la balise `center` pour déplacer notre contenu textuel au centre, vous pouvez désormais utiliser la propriété `text-align` avec la valeur `center` pour déplacer votre texte au centre.

```html
// HTML
<p> Welcome to freeCodeCamp </p>

// CSS
p {
  text-align: center;
}
```

### Comment justifier du texte

Si vous savez utiliser n'importe quel outil textuel comme Microsoft Word ou Google Docs, ou des outils comme Photoshop, Figma et bien d'autres qui gèrent du contenu, vous saurez comment fonctionne l'icône de texte justifié.

Vous l'utilisez pour aider votre texte à atteindre les bords d'une page/conteneur plutôt que d'avoir des espaces inégaux inutiles à la fin.

Ce n'est pas toujours évident, mais quand on regarde attentivement les bords, on remarque la différence, ce qui est plus logique quand on a beaucoup de texte et des paragraphes plus longs.

![](https://paper-attachments.dropbox.com/s_1FCD88D32AEADC1D26B97285FE174892A040B3C1BC2D3128B4E56D61375B2EDB_1663887493952_Untitled.drawio+12.png align="left")

Vous faites cela en utilisant la propriété `text-align` avec `justify` comme valeur :

```html
// HTML
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>

// CSS
p {
  text-align: center;
}
```

## Conclusion

Dans cet article, vous avez appris comment aligner le texte de votre page web HTML en utilisant la propriété CSS `text-align`.

Vous pouvez en apprendre davantage via d'autres articles similaires qui ont été publiés sur freeCodeCamp :

* [CSS Text Align – Exemple de style de texte centré, justifié et aligné à droite](https://www.freecodecamp.org/news/css-text-align-centered-justified-right-aligned-text-style-example/)
    
* [Text Align en CSS – Comment aligner du texte au centre avec HTML](https://www.freecodecamp.org/news/text-align-in-css-how-to-align-text-in-center-with-html/)
    

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.
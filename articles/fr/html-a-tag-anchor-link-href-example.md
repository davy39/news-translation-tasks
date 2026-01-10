---
title: Balise HTML <a> – Exemple de lien d'ancrage HREF
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-09T15:15:04.000Z'
originalURL: https://freecodecamp.org/news/html-a-tag-anchor-link-href-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/aTag.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Balise HTML <a> – Exemple de lien d'ancrage HREF
seo_desc: "You can use HTML's <a> tag to link to different parts of a website, to\
  \ another web page, or to a separate website entirely. \nBy default, it is underlined\
  \ and given a bluish color, but you can override these style defaults with CSS (which\
  \ a lot of peo..."
---

Vous pouvez utiliser la balise `<a>` de HTML pour lier différentes parties d'un site web, une autre page web, ou même un site web entièrement séparé. 

Par défaut, elle est soulignée et de couleur bleutée, mais vous pouvez remplacer ces styles par défaut avec du CSS (ce que beaucoup de gens font).

Plus important encore, cette balise utilise l'attribut `href`, dans lequel vous spécifiez le site web, la page web ou la partie de la même page web à lier.

En plus de l'attribut href, la balise `<a>` utilise également l'attribut target. Cela permet à la page ou au site web que vous liez de s'ouvrir dans un autre onglet du navigateur. Il vous suffit de définir la valeur de l'attribut target sur blank.

## Syntaxe de base de la balise a href
Voici la syntaxe de base pour la balise `<a>` :

```html
<a href="https://www.freecodecamp.org/">freeCodeCamp</a>
```

Dans ce tutoriel, nous allons examiner comment lier un autre site web, lier une autre page du même site web et lier une partie spécifique de la même page web – tout cela avec la balise `<a>`.

## Comment lier un autre site web (Lien externe)

Nous avons déjà brièvement abordé l'attribut `href`. La valeur de cet attribut indique le site web à lier. La valeur doit être une URL absolue, ce qui signifie que vous devez spécifier l'adresse web complète du site web, par exemple, `https://www.freeCodeCamp.org`. 

```html
<p>
   Apprenez à coder gratuitement sur
   <a href="https://www.freecodecamp.org/">freeCodeCamp</a>
</p>
```

```css
 body {
     display: flex;
     align-items: center;
     justify-content: center;
     height: 100vh;
     font-size: 3rem;
     }
```
    
![lien](https://www.freecodecamp.org/news/content/images/2021/08/link.gif)

Si vous traitez avec des liens externes, il est préférable de les ouvrir dans un onglet séparé afin que l'utilisateur n'ait pas à cliquer en arrière et en avant pour parcourir les liens du site original. Cela aide à fournir une expérience utilisateur plus agréable.

```html
 <p>
      Apprenez à coder gratuitement sur
      <a href="https://www.freecodecamp.org/" target="_blank">freeCodeCamp</a>
 </p>
```

![lienexterne](https://www.freecodecamp.org/news/content/images/2021/08/externallink.gif)
    
## Comment lier une page du même site web 

Lorsque vous liez une page du même site web, la valeur assignée à l'attribut `href` fait la différence. 

Ainsi, au lieu de spécifier une URL absolue, vous utiliserez une URL relative. Par exemple, vous utiliserez `contact.html` au lieu de `https://www.freeCodeCamp.org`. 
  
Vous pouvez voir comment lier des pages du même site web ci-dessous :
    
![memesite](https://www.freecodecamp.org/news/content/images/2021/08/samesite.gif)

Le code qui le fait ressemble à ceci :

Pour lier à la page d'accueil :

```html
<div>
   <p>Ceci est la page d'ACCUEIL !</p>
   <a href="about.html">À propos de moi</a>
   <a href="contact.html">Contactez-moi</a>
</div>
```

```css
body {
     display: flex;
     align-items: center;
     justify-content: center;
     height: 100vh;
     font-size: 3rem;
     }
```


Pour lier à la page de contact :

```html
<div>
  <p>Ceci est la page de CONTACT !</p>
</div>
```

```css
body {
     display: flex;
     align-items: center;
     justify-content: center;
     height: 100vh;
     font-size: 3rem;
     }
```

Pour lier à la page À propos :

```html
<div>
      <p>Ceci est la page À PROPOS !</p>
</div>
```


```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-size: 3rem;
    }
```

## Comment lier une partie spécifique d'une page web

Vous utilisez la balise `<a>`, ainsi que son attribut `href`, pour lier une ou plusieurs parties spécifiques de la même page web en combinaison avec l'attribut `id`.
 
Presque tous les éléments HTML utilisent l'attribut id. Ainsi, lorsque vous identifiez la portion de la page web que vous souhaitez lier, attribuez-lui un id et passez-le à l'attribut `href` comme valeur avec le symbole dièse (#) le précédant.

Les extraits de code ci-dessous démontrent comment lier des parties spécifiques de la même page web :
 
```html
<a href="#intro">Intro</a>
<a href="#apropos">À propos</a>
<a href="#contact">Contact</a>
<p id="intro">
      Intro: Lorem ipsum dolor sit, amet consectetur adipisicing elit. Atque
      nostrum magni dolore laboriosam aspernatur minima officia unde voluptate
      porro nisi animi illo voluptas labore, at harum expedita tenetur vel
      quaerat sit rerum nulla fugit debitis repellat! Rem veniam suscipit at?
</p>

<p id="apropos">
      À propos de moi: Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis
      quos nesciunt nemo dignissimos quisquam quasi harum, vero illum, ducimus
      similique placeat ut rerum hic non aliquid itaque dolores expedita libero
      consequuntur sit rem quod officia? Fugiat explicabo natus optio dolorem?
</p>

<p id="contact">
      Contactez-moi: Lorem ipsum dolor sit amet consectetur adipisicing elit.
      Debitis quos nesciunt nemo dignissimos quisquam quasi harum, vero illum,
      ducimus similique placeat ut rerum hic non aliquid itaque dolores expedita
      libero consequuntur sit rem quod officia? Fugiat explicabo natus optio
      dolorem?
 </p>
```

![memepage](https://www.freecodecamp.org/news/content/images/2021/08/samepage.gif)

## Comment créer des boutons avec la balise `<a>`

Il est assez courant d'utiliser la balise `<a>` pour créer des boutons et ensuite les styliser avec du CSS. 

Vous utilisez généralement le type d'entrée de bouton (`<input type="button">`) et l'élément bouton `<button>...</button>` pour cela. Mais vous devrez peut-être ajouter un peu de JavaScript pour les faire faire ce que vous voulez qu'ils fassent. 

Avec la balise `<a>`, vous pouvez simplement spécifier où vous voulez lier comme valeur `href`.

```html
<a class="btn" href="https://www.freecodecamp.org">freeCodeCamp</a>
```

```css
 body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-size: 3rem;
}

.btn {
    background-color: #2ecc71;
    border: 1px solid white;
    border-radius: 5px;
    text-decoration: none;
    color: white;
    padding: 6px;
}

.btn:hover {
      background-color: #0fa84f;
}
```

Que fait le code ci-dessus ?

Nous avons attaché un attribut de classe `btn` (pour bouton) à la balise `<a>` afin de pouvoir le styliser. En ciblant la balise à travers cette classe assignée, nous avons défini un fond verdâtre, une bordure de 1px de largeur, de style solide et de couleur blanche avec un `border-radius` défini à 5px pour avoir une bordure légèrement arrondie. 

Pour supprimer le soulignement par défaut assigné aux balises `<a>`, nous avons défini un décorateur de texte sur none. Nous avons également défini un remplissage de 6px pour plus d'espacement entre le texte et la bordure. 

Avec la pseudo-classe `:hover` fournie par CSS, nous avons pu spécifier un léger changement de couleur de fond chaque fois qu'un utilisateur survole le bouton avec sa souris.

En fin de compte, nous obtenons le résultat ci-dessous :

![bouton](https://www.freecodecamp.org/news/content/images/2021/08/btn.gif)
    
## Conclusion
    
J'espère que ce tutoriel vous a aidé à comprendre tout ce que vous pouvez faire avec la balise `<a>` afin que vous puissiez commencer à en faire bon usage sur vos sites web.

Merci d'avoir lu, et continuez à coder.
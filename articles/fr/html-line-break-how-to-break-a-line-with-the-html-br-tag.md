---
title: Saut de ligne HTML – Comment sauter une ligne avec la balise HTML <br>
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-20T17:21:23.000Z'
originalURL: https://freecodecamp.org/news/html-line-break-how-to-break-a-line-with-the-html-br-tag
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/linebreak.png
tags:
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Saut de ligne HTML – Comment sauter une ligne avec la balise HTML <br>
seo_desc: 'When you''re writing HTML, you often need to insert line breaks. A line
  break is essential in addresses, poems, or when text exceeds the available browser
  width. If you don''t insert your own line breaks, then the text gets formatted in
  an odd way.

  In ...'
---

Lorsque vous écrivez en HTML, vous devez souvent insérer des sauts de ligne. Un saut de ligne est essentiel dans les adresses, les poèmes ou lorsque le texte dépasse la largeur disponible du navigateur. Si vous n'insérez pas vos propres sauts de ligne, le texte est alors formaté de manière étrange.

Dans ce tutoriel, je vais vous montrer comment insérer des sauts de ligne dans votre code HTML avec des exemples "avec et sans", afin que vous puissiez commencer à l'utiliser correctement et mieux formater votre texte.

## Syntaxe de base du saut de ligne HTML

Vous pouvez insérer des sauts de ligne en HTML avec la balise `<br>`, qui équivaut à un retour chariot sur un clavier.

Sachez que HTML ignorera tout saut de ligne provenant de la touche retour du clavier.

```html
<br />
```

Si vous vous demandez pourquoi il y a une barre oblique dans la balise `<br>` ci-dessus, la barre oblique était importante lorsque HTML4 était encore largement utilisé. Avec HTML5, vous n'avez plus besoin de mettre une barre oblique. Mais les deux feront la même chose.

Si vous utilisez un formateur de code comme Prettier, il insérera toujours la barre oblique lorsque vous enregistrez ou collez, même si vous ne la mettez pas.

## Comment insérer des sauts de ligne dans les adresses

Un saut de ligne est important lorsque vous écrivez une adresse sur une lettre, par exemple, afin de la formater correctement.

### Voici un exemple d'adresse sans sauts de ligne

Une adresse sans sauts de ligne (balises `<br>`) ressemble à ceci :

```html
<p>
     The White House, 1600 Pennsylvania Avenue NW Washington, DC 20500, USA.
</p>
```

J'ai ajouté un peu de code CSS pour centrer tout avec Flexbox et agrandir légèrement le texte :

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-size: 3rem;
    max-width: 1000px;
    margin: 0 auto;
}
```

Voici à quoi cela ressemble dans le navigateur :
![address-without-line-breaks](https://www.freecodecamp.org/news/content/images/2021/08/address-without-line-breaks.png)

### Voici une adresse avec des sauts de ligne

Et voici comment nous pouvons ajouter des sauts de ligne pour formater correctement notre adresse :

```html
<p>
    The White House <br />
    1600 Pennsylvania Avenue <br />
    NW Washington, DC <br />
    20500 <br />
    USA
</p>
```

Voici à quoi cela ressemble dans le navigateur :

![address-with-line-breaks](https://www.freecodecamp.org/news/content/images/2021/08/address-with-line-breaks.png)

## Comment ajouter des sauts de ligne aux poèmes

Les poèmes sont conventionnellement écrits en phrases courtes avec des sauts de ligne afin de créer des hiérarchies visuelles et de les formater joliment.

Ainsi, si vous souhaitez écrire un poème dans votre code HTML, la balise `<br>` facilite le processus de formatage pour vous.

### Un poème sans sauts de ligne

```html
<p>
      I dabbled around a lot when I decided to learn to code 
      I went from A to Z with resources 
      When I decided to make my own things 
      I discovered I've been in the old all while 
      So I remained a novice in coding 
      But then I found freeCodeCamp 
      I got my hands on the platform 
      I went from novice to ninja in coding 
     And now I'm a camper for life
</p>
```

Voici à quoi cela ressemble dans le navigateur :

![poem-without-line-break](https://www.freecodecamp.org/news/content/images/2021/08/poem-without-line-break.png)

Vous pouvez voir que le poème n'a pas de hiérarchie visuelle, il n'est pas formaté correctement et est donc illisible en tant que poème.

### Un poème avec des sauts de ligne

```html
<p>
      I dabbled around a lot when I decided to learn to code <br />
      I went from A to Z with resources <br />
      When I decided to make my own things <br />
      I discovered I've been in the old all while <br />
      So I remained a novice in coding <br />
      But then I found freeCodeCamp <br />
      I got my hands on the platform <br />
      I went from novice to ninja in coding <br />
      And now I'm a camper for life <br />
</p>
```

J'ai également modifié légèrement la taille de la police dans le CSS :

```css
body {
   display: flex;
   align-items: center;
   justify-content: center;
   height: 100vh;
   font-size: 2.5rem;
   max-width: 1000px;
   margin: 0 auto;
}
```

Voici à quoi cela ressemble maintenant dans le navigateur :

![poem-with-line-break](https://www.freecodecamp.org/news/content/images/2021/08/poem-with-line-break.png)

Vous pouvez voir que le poème est maintenant plus lisible et correctement formaté.

**Un conseil précieux :** N'utilisez pas la balise `<br>` pour forcer un espace entre les éléments de niveau bloc (`p`, `h1`, `h2`, `h3`, `div`, etc). Utilisez plutôt la propriété CSS margin.

Vous vous demandez peut-être – puisque la balise `<br>` est un élément, est-il possible de la styliser ?

Eh bien, c'est possible. Mais il n'y a pas de réel besoin pratique de la styliser, car tout ce qu'elle fait est de créer quelques espaces blancs.

## Conclusion

J'espère que ce tutoriel vous a donné les connaissances de base nécessaires pour utiliser la balise `<br>` afin que vous puissiez améliorer l'apparence de votre texte HTML.

Merci d'avoir lu, et continuez à coder.
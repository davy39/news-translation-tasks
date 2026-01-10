---
title: Exemples de code de lien de bouton HTML – Comment créer des hyperliens HTML
  en utilisant l'attribut HREF sur les balises
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-03-15T13:51:15.000Z'
originalURL: https://freecodecamp.org/news/html-button-link-code-examples-how-to-make-html-hyperlinks-using-the-href-attribute-on-tags
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6049c377a7946308b76862f0.jpg
tags:
- name: best practices
  slug: best-practices
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Exemples de code de lien de bouton HTML – Comment créer des hyperliens
  HTML en utilisant l'attribut HREF sur les balises
seo_desc: 'In this article, we are going to explore three different ways you can make
  an HTML button act like a link.

  These are the methods we''ll go over:


  Styling a link to look like a button

  Using the action and formaction attributes in a form

  Using the JavaS...'
---

Dans cet article, nous allons explorer trois façons différentes de faire en sorte qu'un bouton HTML agisse comme un lien.

Voici les méthodes que nous allons aborder :

1. Styliser un lien pour qu'il ressemble à un bouton
2. Utiliser les attributs action et formaction dans un formulaire
3. Utiliser l'événement JavaScript onclick

Mais d'abord, examinons l'approche incorrecte.

## Pourquoi cette approche avec l'élément `a` ne fonctionne-t-elle pas ?

Le snippet de code ci-dessous mène au site web de freeCodeCamp lorsqu'il est cliqué.

```html
  <a href="https://www.freecodecamp.org/">
    <button>freeCodeCamp</button>
  </a> 
```

Cependant, ceci n'est pas du HTML valide. 

> L'élément `[a](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element)` peut être enveloppé autour de paragraphes entiers, de listes, de tableaux, et ainsi de suite, même des sections entières, tant qu'il n'y a pas de contenu interactif à l'intérieur (par exemple, des boutons ou d'autres liens). - (Source : [Web Hypertext Application Technology Working Group](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element))

Cela est considéré comme une mauvaise pratique car cela rend l'intention de l'utilisateur peu claire. 

Les liens sont censés naviguer l'utilisateur vers une autre partie de la page web ou un site externe. Et les boutons sont censés effectuer une action spécifique comme soumettre un formulaire.  

Lorsque vous imbriquez l'un dans l'autre, cela crée une confusion quant à l'action que vous souhaitez effectuer. C'est pourquoi il est préférable de ne pas imbriquer un bouton dans une balise d'ancrage. 

## Comment styliser un lien pour qu'il ressemble à un bouton avec CSS

Cette première approche n'utilise pas du tout le bouton. Nous pouvons styliser une balise d'ancrage pour qu'elle ressemble à un bouton en utilisant CSS.

Voici le style HTML par défaut pour une balise d'ancrage.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/blue-anchor-tag.png)

Nous pouvons ajouter une classe à la balise d'ancrage et utiliser ensuite ce sélecteur de classe pour styliser l'élément.  

```html
  <a class="fcc-btn" href="https://www.freecodecamp.org/">freeCodeCamp</a>  

```

Si vous souhaitez que le lien ouvre une nouvelle page, vous pouvez ajouter l'attribut `target="_blank"` comme ceci : 

```html
  <a target="_blank" class="fcc-btn" href="https://www.freecodecamp.org/">freeCodeCamp</a>  

```

Ensuite, nous pouvons ajouter une couleur de fond et changer la couleur de la police comme ceci :

```css
.fcc-btn {
  background-color: #199319;
  color: white;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/background-and-white-text.png)

L'étape suivante serait d'ajouter un peu de remplissage autour du texte :

```css
.fcc-btn {
  background-color: #199319;
  color: white;
  padding: 15px 25px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/adding-padding-1.png)

Enfin, nous pouvons utiliser la propriété text-decoration pour supprimer le soulignement du texte :

```css
.fcc-btn {
  background-color: #199319;
  color: white;
  padding: 15px 25px;
  text-decoration: none;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/removing-underline.png)

Maintenant, nous avons une balise d'ancrage qui ressemble à un bouton. 

Nous pouvons également rendre ce "bouton" un peu plus interactif en changeant la couleur de fond en fonction de l'état du lien. 

```css
.fcc-btn:hover {
  background-color: #223094;
}
```

%[https://codepen.io/jessica-wilkins/pen/XWNyGBR]

Nous pourrions nous lancer dans un design plus élaboré, mais ceci est juste pour vous montrer les bases de la stylisation d'un lien comme un bouton.

Vous pourriez également choisir d'utiliser une bibliothèque CSS comme [Bootstrap](https://getbootstrap.com/).

```html
  <a class="btn btn-primary" href="https://www.freecodecamp.org/">freeCodeCamp</a>  

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/bootstrap-styles.png)

Si votre projet inclut déjà Bootstrap, alors vous pouvez utiliser les styles de bouton intégrés. Mais je n'importerais pas Bootstrap juste pour styliser un lien. 

### Quels sont les problèmes avec cette approche ?

Il y a un débat sur le fait de savoir si c'est une bonne pratique de styliser les liens comme des boutons. Certains soutiendront que les liens doivent toujours ressembler à des liens et les boutons à des boutons. 

Dans le livre web intitulé [Resilient Web Design](https://resilientwebdesign.com/), Jeremy Keith déclare que 

> un matériau ne doit pas être utilisé comme substitut d'un autre, sinon le résultat final est trompeur. 

Pourquoi ai-je mentionné ce débat ? 

Mon objectif n'est pas de vous faire choisir un côté du débat plutôt qu'un autre. Je veux simplement que vous soyez conscient de cette discussion en cours. 

## Comment utiliser les attributs `action` et `formaction` pour créer un bouton dans un formulaire

### Comment utiliser l'attribut `action`

Une autre alternative serait d'imbriquer le bouton dans un formulaire et d'utiliser l'attribut action. 

Exemple d'entrée :

```html
  <form action="https://www.freecodecamp.org/">
    <input type="submit" value="freeCodeCamp">
  </form>
```

Exemple de bouton :

```html
  <form action="https://www.freecodecamp.org/">
    <button type="submit">freeCodeCamp</button>
  </form>
```

Ce serait le style de bouton par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/default-button-style.png)

Nous pourrions utiliser les mêmes styles que précédemment, mais nous devrions ajouter le curseur pointeur et définir la bordure à none, comme ceci : 

```css
.fcc-btn {
  background-color: #199319;
  color: white;
  padding: 15px 25px;
  text-decoration: none;
  cursor: pointer;
  border: none;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/removing-underline-1.png)

### Comment utiliser l'attribut `formaction`

Similaire à l'approche précédente, nous pouvons créer un formulaire et utiliser l'attribut formaction.

Exemple d'entrée :

```html
  <form>
    <input type="submit" formaction="https://www.freecodecamp.org/" value="freeCodeCamp">
  </form>
```

Exemple de bouton :

```html
  <form>
    <button type="submit" formaction="https://www.freecodecamp.org/">freeCodeCamp</button>
  </form>
```

Vous ne pouvez utiliser l'attribut formaction qu'avec les inputs et les boutons qui ont `type="image"` ou `type="submit"`.  

### Est-ce sémantiquement correct ?

Bien que cela semble être une solution fonctionnelle, il y a une question à savoir si cela est sémantiquement correct. 

Nous utilisons les balises de formulaire mais cela ne fonctionne pas comme un vrai formulaire. Le but d'un formulaire est de collecter et de soumettre des données utilisateur. 

Mais nous utilisons le bouton de soumission pour naviguer l'utilisateur vers une autre page. 

En ce qui concerne la sémantique, ce n'est pas une bonne façon d'utiliser les balises de formulaire. 

### Effets secondaires de l'utilisation des attributs action et formaction

Lorsque vous cliquez sur le bouton, quelque chose d'intéressant se produit avec l'URL. L'URL a maintenant un point d'interrogation à la fin.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/question-mark-at-end.png)

La raison de ce changement est que le formulaire utilise la méthode GET. Vous pourriez passer à la méthode POST, mais il pourrait y avoir des cas où cela n'est pas idéal non plus. 

```html
  <form method="POST" action="https://www.freecodecamp.org/">
    <button type="submit">freeCodeCamp</button>
  </form>
```

Bien que cette approche soit du HTML valide, elle entraîne cet effet secondaire non intentionnel. 

## Comment utiliser l'événement JavaScript onclick pour créer un bouton

Dans les approches précédentes, nous avons examiné des solutions HTML et CSS. Mais nous pouvons également utiliser JavaScript pour obtenir le même résultat. 

Exemple d'entrée :

```html
 <form>
    <input type="button" onclick="window.location.href='https://www.freecodecamp.org/';" value="freeCodeCamp" />
 </form>
```

 Exemple de bouton :

```html
<button onclick="window.location.href='https://www.freecodecamp.org/';">freeCodeCamp</button>  

```

Le `location.href` représente l'emplacement d'une URL spécifique. Dans ce cas, `Window.location.href` retournera [https://www.freecodecamp.org/](https://www.freecodecamp.org/). 

### Inconvénients de cette approche

Bien que cette solution fonctionne, il y a quelques problèmes potentiels à considérer. 

Si l'utilisateur a décidé de désactiver JavaScript dans son navigateur, alors clairement cette solution ne fonctionnerait pas. Malheureusement, cela pourrait conduire à une mauvaise expérience utilisateur. 

## Conclusion

Le but de cet article était de vous montrer trois façons différentes de faire en sorte que les boutons agissent comme des liens.

La première approche consistait à concevoir un lien pour qu'il ressemble à un bouton. Nous avons également examiné le débat sur le fait de savoir s'il est judicieux de changer l'apparence des liens pour qu'ils ressemblent à un autre élément.

La deuxième approche a utilisé les attributs de formulaire et formaction. Mais nous avons également appris que cette approche a certains effets secondaires avec l'URL et n'est pas sémantiquement correcte. 

La troisième approche a utilisé l'événement JavaScript onclick et le Window.location.href. Mais nous avons également appris que cette approche pourrait ne pas fonctionner si l'utilisateur décide de désactiver JavaScript dans son navigateur. 

En tant que développeur, il est vraiment important de regarder les avantages et les inconvénients d'une approche particulière avant de l'incorporer dans votre projet.   

J'espère que vous avez apprécié cet article et appris quelques choses en cours de route. 

Bon codage !
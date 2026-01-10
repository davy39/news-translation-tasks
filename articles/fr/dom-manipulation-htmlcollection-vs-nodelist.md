---
title: HTMLCollection vs NodeList – Quelle est la différence ?
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2023-12-07T22:11:45.000Z'
originalURL: https://freecodecamp.org/news/dom-manipulation-htmlcollection-vs-nodelist
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Benjamin-Semah
seo_title: HTMLCollection vs NodeList – Quelle est la différence ?
---

DevAfterHours.png
étiquettes:
- name: DOM
  slug: dom
- name: Développement Front-end
  slug: front-end-development
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Développement Web
  slug: web-development
seo_title: null
seo_desc: 'Si vous êtes un développeur web ou avez travaillé avec le DOM (Document Object Model), vous avez peut-être déjà rencontré les termes HTMLCollection et NodeList. Mais que signifient-ils et quand devez-vous les utiliser ?

À la fin de cet article, vous aurez appris tout sur HTMLCollection et NodeList. Un...'
---

Si vous êtes un développeur web ou avez travaillé avec le DOM (Document Object Model), vous avez peut-être déjà rencontré les termes `HTMLCollection` et `NodeList`. Mais que signifient-ils et quand devez-vous les utiliser ?

À la fin de cet article, vous aurez appris tout sur `HTMLCollection` et `NodeList`.

## Table des matières

* [Qu'est-ce qu'une `HTMLCollection` ?](#heading-quest-ce-quune-htmlcollection)
    
* [Qu'est-ce qu'une `NodeList` ?](#heading-quest-ce-quune-nodelist)
    
* [Similitudes entre `HTMLCollection` et `NodeList`](#heading-similitudes-entre-htmlcollection-et-nodelist)
    
* [Différences entre `HTMLCollection` et `NodeList`](#heading-differences-entre-htmlcollection-et-nodelist)
    
* [Lequel utiliser ?](#heading-lequel-utiliser)
    
* [Conclusion](#heading-conclusion)
    

Commençons !

## Qu'est-ce qu'une `HTMLCollection` ?

Une `HTMLCollection` est une liste d'éléments DOM qui correspondent à certains critères. Par exemple, ils peuvent avoir le même nom de balise ou de classe. Ou ils peuvent être liés dans un contexte spécifique, comme les enfants d'un élément particulier.

Voici un exemple :

```html
  <button class="btn">Premier bouton</button>
  <button class="btn">Deuxième bouton</button>
  <button class="btn">Troisième bouton</button>
```

Dans cet exemple, nous avons trois éléments bouton. Chacun a une classe `btn`. Maintenant, sélectionnons les boutons en utilisant la méthode `getElementsByClassName`.

```javascript
const buttonElements = document.getElementsByClassName('btn')
console.log(buttonElements)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-04-at-8.10.41-AM.png align="left")

La méthode `getElementsByClassName` retourne une `HTMLCollection` des trois boutons avec la classe `btn`. Cela ressemble à un tableau mais ce n'en est pas un. Plus d'informations à ce sujet plus tard.

## Qu'est-ce qu'une `NodeList` ?

Comme le nom le suggère, une `NodeList` est une liste de nœuds. Mais qu'est-ce qu'un nœud ? Un nœud est tout élément individuel dans l'arbre DOM. Cela peut être des éléments, des attributs, des textes, des commentaires, et ainsi de suite.

Un exemple de méthode DOM qui retournera une `NodeList` est `querySelectorAll`.

Exemple :

```html
  <button class="btn">Premier bouton</button>
  <button class="btn">Deuxième bouton</button>
  <button class="btn">Troisième bouton</button>
```

En utilisant le même exemple, sélectionnons les boutons avec `querySelectorAll` à la place.

```javascript
const buttonElements = document.querySelectorAll('.btn')
console.log(buttonElements)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-04-at-8.33.08-AM.png align="left")

Cette fois, l'instruction `console.log` imprime une `NodeList`. Encore une fois, cela ressemble également à un tableau mais ce n'en est pas tout à fait un.

## Similitudes entre `HTMLCollection` et `NodeList`

Maintenant que vous savez ce que sont `HTMLCollection` et `NodeList`, voyons comment elles se ressemblent. Elles ne sont pas des tableaux même si elles y ressemblent. Mais elles ont des fonctionnalités qui leur donnent certains comportements de tableaux.

Vous pouvez accéder au contenu des deux en utilisant un index basé sur zéro comme vous le feriez avec un tableau. Et vous pouvez également utiliser la propriété length pour trouver la longueur d'une `HTMLCollection` et d'une `NodeList`.

Exemple :

```html
  <div>
    <p class="paragraph">Premier paragraphe</p>
    <p class="paragraph">Deuxième paragraphe</p>
    <p class="paragraph">Troisième paragraphe</p>
  </div>
```

Ceci est une `div` avec trois paragraphes. Voyons des exemples d'accès aux éléments avec un index basé sur zéro et vérifions également la longueur pour `HTMLCollection` et `NodeList`.

### Exemple avec `HTMLCollection` :

```javascript
// getElementsByClassName retournera une HTMLCollection
const paragraphs = document.getElementsByClassName("paragraph")
console.log(paragraphs)

// Utilisez l'index pour obtenir le premier paragraphe
let firstParagraph = paragraphs[0] 
console.log(firstParagraph)

// Utilisez la propriété length
console.log(paragraphs.length)
```

La capture d'écran ci-dessous montre les résultats pour les trois instructions `console.log`.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-04-at-9.38.09-AM.png align="left")

Même si `HTMLCollection` n'est pas un tableau, vous pouvez toujours utiliser l'index pour accéder aux éléments de la collection. Et vous pouvez également obtenir la longueur en utilisant la propriété `length`.

Vous obtiendrez le même résultat pour une `NodeList`. Pour obtenir une `NodeList`, utilisons la méthode `querySelectorAll` à la place.

### Exemple avec `NodeList` :

```javascript
// querySelectorAll retournera une NodeList
const paragraphs = document.querySelectorAll(".paragraph")
console.log(paragraphs)

// Utilisez l'index pour obtenir le premier paragraphe
let firstParagraph = paragraphs[0] 
console.log(firstParagraph)

// Utilisez la propriété length
console.log(paragraphs.length)
```

Tout comme `HTMLCollection`, `NodeList` utilise également un index basé sur zéro. Et vous pouvez également utiliser la propriété length sur celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-04-at-9.55.22-AM.png align="left")

## Différences entre `HTMLCollection` et `NodeList`

Vous avez vu comment une `HTMLCollection` et une `NodeList` se ressemblent. Mais il y a aussi quelques différences dont vous devez être conscient lorsque vous travaillez avec ces deux types de collections dans le DOM.

### Nœuds d'éléments uniquement vs tous les nœuds

Les nœuds d'éléments sont des éléments HTML comme `<p>`, `<div>`, `<img>`, et autres. Mais il existe d'autres types de nœuds également. Par exemple, les nœuds de texte et les nœuds d'attributs.

Une `HTMLCollection` n'inclura que les nœuds d'éléments tandis qu'une `NodeList` inclut d'autres types de nœuds.

Exemple :

```javascript
<div>
  Ceci est un texte
  <p class="paragraph">Premier paragraphe</p>
  <p class="paragraph">Deuxième paragraphe</p>
</div>
```

Voici une `div` avec un nœud de texte et deux nœuds d'éléments (paragraphes). Chaque paragraphe a également un nœud de texte.

En supposant que vous vouliez obtenir uniquement les nœuds d'éléments dans la `div`, vous pouvez utiliser la propriété `children` sur la `div`. Et elle retournera une `HTMLCollection` contenant uniquement les nœuds d'éléments.

Mais si vous vouliez tous les nœuds et pas seulement les nœuds d'éléments, alors vous pouvez utiliser la propriété `childNodes` pour obtenir tous les nœuds.

```javascript
const divElement = document.querySelector('div')

console.log(divElement.children) // retourne une HTMLCollection
console.log(divElement.childNodes) // retourne une NodeList
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-04-at-10.59.18-AM.png align="left")

La `HTMLCollection` a deux éléments : les nœuds d'éléments de paragraphe. Tandis que la `NodeList` inclut le premier texte et les deux paragraphes et leurs contenus textuels également.

### Collections dynamiques vs collections statiques

Les concepts de "dynamique" et "statique" font référence à la manière dont une `HTMLCollection` et une `NodeList` se comportent en réponse aux changements dans la structure du document.

#### Une `HTMLCollection` est toujours dynamique

Que signifie dire qu'une `HTMLCollection` est toujours dynamique ? Cela signifie que lorsqu'il y a un changement dans le document, elle sera automatiquement mise à jour pour refléter le changement.

Exemple :

```html
<p>Premier paragraphe</p>
<p>Deuxième paragraphe</p>
<p>Troisième paragraphe</p>
```

```javascript
// retourne une HTMLCollection
const paragraphs = document.getElementsByTagName('p')

console.log("AVANT MISE À JOUR : ", paragraphs)

const newParagraph = document.createElement('p')
document.body.appendChild(newParagraph)

console.log("APRÈS MISE À JOUR : ", paragraphs)
```

Le code ci-dessus crée une `HTMLCollection` appelée `paragraphs` en utilisant la méthode `getElementsByTagName`. Et il y a deux instructions `console.log`. Une avant qu'un nouveau paragraphe soit créé et ajouté au corps, et une autre après cela.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-06-at-9.04.10-AM.png align="left")

Avant la mise à jour, la `HTMLCollection` avait trois éléments. Mais après la mise à jour, la collection a maintenant quatre éléments, reflétant le changement dans le document.

#### Une `NodeList` est parfois statique

Une `NodeList` n'est pas toujours dynamique. Elle peut être statique ou dynamique selon la manière dont elle est générée. Par exemple, une `NodeList` générée avec la méthode `querySelectorAll` est statique. Un changement dans le document n'est pas reflété dans la `NodeList`.

Exemple :

```html
<p>Premier paragraphe</p>
<p>Deuxième paragraphe</p>
<p>Troisième paragraphe</p>
```

```javascript
// retourne une HTMLCollection
const paragraphs = document.getElementsByTagName('p')

console.log("AVANT MISE À JOUR : ", paragraphs)

const newParagraph = document.createElement('p')
document.body.appendChild(newParagraph)

console.log("APRÈS MISE À JOUR : ", paragraphs)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-06-at-9.09.42-AM.png align="left")

En raison de la nature statique de la `NodeList`, elle reste la même même après une mise à jour dans le document.

Note : dans des cas exceptionnels, comme lorsqu'une `NodeList` est générée avec `getElementsByName`, cette `NodeList` sera dynamique.

### Comment accéder aux éléments de la collection

Lors de l'accès aux éléments dans une `HTMLCollection`, vous pouvez utiliser l'une des méthodes suivantes.

* L'index de l'élément.
    
* Leur attribut `id` avec la propriété `namedItem`.
    
* Leur attribut `name` avec la propriété `namedItem`.
    

Mais avec une `NodeList`, vous ne pouvez accéder aux nœuds de la liste que par leur index.

```javascript
<div id="container">
  <button id="btn1" name="first-name">Premier bouton</button>
  <button id="btn2">Deuxième bouton</button>
  <button id="btn3">Troisième bouton</button>
</div>
```

Voici un conteneur `div` avec trois boutons. Notez que le premier bouton a un attribut id et un attribut name.

#### Exemple avec `HTMLCollection` :

```javascript
const container = document.querySelector('#container')
const buttons = container.children // retourne HTMLCollection

console.log(buttons[0])// en utilisant l'index
console.log(buttons.namedItem("btn1")) // en utilisant l'attribut id
console.log(buttons.namedItem("first-name")) // en utilisant l'attribut name
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-04-at-11.57.33-AM.png align="left")

Les trois instructions `console.log` retournent avec succès le premier bouton.

#### Exemple avec `NodeList` :

```javascript
const container = document.querySelector('#container')
const buttons = container.childNodes // retourne une NodeList

console.log(buttons[1])// en utilisant l'index
console.log(buttons.namedItem("btn1")) // lève une erreur
console.log(buttons.namedItem("first-name")) // lève une erreur
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-06-at-7.19.56-AM.png align="left")

En utilisant le même exemple pour une `NodeList`, la première instruction `console.log` imprime le bouton. Mais les deux autres lèvent une `TypeError`.

### Comment parcourir la collection

Vous ne pouvez pas parcourir une `HTMLCollection` avec l'une des méthodes de tableau. À moins de créer d'abord un tableau à partir de la collection.

Mais avec une `NodeList`, vous pouvez utiliser la méthode `forEach` pour la parcourir. Mais vous ne pouvez pas utiliser d'autres méthodes de tableau comme `map`, `filter`, et autres sans d'abord créer un tableau à partir de celle-ci.

Exemple :

```html
<button class="btn">Premier bouton</button>
<button class="btn">Deuxième bouton</button>
<button class="btn">Troisième bouton</button>
```

Le code ci-dessous tente de parcourir une `HTMLCollection` avec la méthode `forEach` et entraîne une `TypeError`.

```javascript
// retourne une HTMLCollection
const allButtons = document.getElementsByClassName('btn') 

allButtons.forEach(button => console.log(button))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-06-at-8.04.26-AM.png align="left")

Regardons un autre exemple mais avec une `NodeList`.

```javascript
// retourne une NodeList
const allButtons = document.querySelectorAll('.btn') 

allButtons.forEach(button => console.log(button))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-06-at-8.07.27-AM.png align="left")

Dans l'exemple ci-dessus, la méthode `forEach` fonctionne avec succès sur la `NodeList`.

Si pour une raison quelconque, vous souhaitez toujours parcourir une `HTMLCollection` sans d'abord créer un tableau à partir de celle-ci, vous pouvez utiliser l'instruction `for...of`. Utilisons le même exemple de boutons pour montrer comment vous pouvez faire cela.

```javascript
// retourne une HTMLCollection
const allButtons = document.getElementsByClassName('btn')

for (button of allButtons) {
  console.log(button)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-06-at-8.07.27-AM-1.png align="left")

## Lequel utiliser ?

La question de savoir si vous devez utiliser une `HTMLCollection` ou une `NodeList` dépend du cas d'utilisation ou du contexte spécifique.

Si vous voulez une collection dynamique qui se met à jour automatiquement lorsqu'il y a un changement dans le document, alors vous devriez utiliser une `HTMLCollection`. Mais si vous préférez une collection statique qui ne se met pas à jour avec un changement dans le document, alors vous devriez utiliser une `NodeList`.

La plupart des frameworks et bibliothèques JavaScript modernes fournissent des abstractions de haut niveau, simplifiant de nombreuses tâches de manipulation du DOM. Et vous n'avez pas besoin de vous en soucier.

Mais avoir une compréhension solide des collections DOM natives comme `HTMLCollection` et `NodeList` reste précieux, surtout dans les scénarios où un contrôle fin ou une compatibilité avec du code hérité est essentiel.

## Conclusion

Dans cet article, vous avez appris à propos de `HTMLCollection` et `NodeList`. Vous avez appris ce qu'elles sont, leurs similitudes et différences. L'article a également abordé quand vous devriez envisager d'utiliser une `HTMLCollection` ou une `NodeList`.

Merci d'avoir lu. Et bon codage. Pour plus de tutoriels approfondis, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours).
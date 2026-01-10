---
title: Meilleures pratiques de manipulation du DOM en JS – avec exemples
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-01-12T17:41:27.000Z'
originalURL: https://freecodecamp.org/news/dom-manipulation-best-practices
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/freecodecamp-javascript-benjamin-semah.png
tags:
- name: best practices
  slug: best-practices
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: Meilleures pratiques de manipulation du DOM en JS – avec exemples
seo_desc: 'In JavaScript, you can manipulate the content of a web page using the Document
  Object Model (DOM). But how do you write code that is readable, easy to maintain,
  and not prone to performance issues?

  That''s what we''ll cover in this article. I''ll discus...'
---

En JavaScript, vous pouvez manipuler le contenu d'une page web en utilisant le Document Object Model (DOM). Mais comment écrire du code qui est lisible, facile à maintenir et peu sujet aux problèmes de performance ?

C'est ce que nous allons couvrir dans cet article. Je vais discuter de certaines bonnes pratiques importantes afin que vous puissiez manipuler le DOM en toute confiance.

## Table des matières

* [Introduction](#)
    
* [Utiliser l'événement DOMContentLoaded](#utiliser-levenement-domcontentloaded)
    
* [Mettre en cache les éléments sélectionnés](#mettre-en-cache-les-elements-selectionnes)
    
* [Interroger le parent au lieu du document](#interroger-le-parent-au-lieu-du-document)
    
* [Utiliser les classes CSS pour styliser les éléments](#utiliser-les-classes-css-pour-styliser-les-elements)
    
* [Utiliser innerHTML avec prudence](#utiliser-innerhtml-avec-prudence)
    
* [Écrire des écouteurs d'événements lisibles](#ecrire-des-ecouteurs-devenements-lisibles)
    
* [Utiliser la délégation d'événements pour gérer les événements du DOM](#utiliser-la-delegation-devenements-pour-gerer-les-evenements-du-dom)
    
* [Grouper les mises à jour du DOM avec Fragment](#grouper-les-mises-a-jour-du-dom-avec-fragment)
    
* [Utiliser la méthode stopPropagation](#utiliser-la-methode-stoppropagation)
    
* [Tester votre code de manipulation du DOM](#tester-votre-code-de-manipulation-du-dom)
    
* [Conclusion](#conclusion)
    

## Utiliser l'événement `DOMContentLoaded`

L'événement `DOMContentLoaded` est déclenché lorsque le document HTML est entièrement chargé. L'utilisation de cet événement garantit que votre code de manipulation du DOM ne s'exécute qu'après le chargement complet du document.

Pour utiliser `DOMContentLoaded`, ajoutez un écouteur d'événement au document et écoutez l'événement `DOMContentLoaded`. Cela aide à prévenir tout problème qui pourrait survenir lorsque vous essayez de manipuler des éléments qui ne sont pas encore rendus.

Exemple :

```javascript
document.addEventListener('DOMContentLoaded', function() {
  // Votre code de manipulation du DOM va ici...
})
```

## Mettre en cache les éléments sélectionnés

Lorsque vous avez des éléments fréquemment utilisés, interroger le DOM pour le même élément encore et encore est inefficace. Il est préférable d'interroger le DOM une fois et de stocker le résultat dans des variables.

```javascript
const cachedElement = document.getElementById('exampleId')
```

De cette manière, vous pouvez référencer les variables chaque fois que vous souhaitez les utiliser. Cela aide à améliorer les performances en réduisant le travail inutile.

## Interroger le parent au lieu du document

Lorsque vous mettez en cache un élément, vous pouvez également l'interroger pour sélectionner l'un de ses descendants. Cela peut aider à améliorer les performances car cela limite la portée de la requête et réduit le nombre de fois où le document entier est interrogé.

Exemple :

```html
<div id="parent">
    <p id="child">Paragraphe d'exemple</p>
</div>
```

```javascript
const parentElement = document.getElementById('parent')

// Option 1 : Interroger le document entier ❌
const childFromDocument = document.getElementById('child') 

// Option 2 : Interroger l'élément parent ✅
const childFromParent = parentElement.querySelector('#child')
```

Dans l'exemple ci-dessus, il y a un simple balisage contenant un div `#parent` et un paragraphe `.child`. Ensuite, il y a deux options pour sélectionner l'élément enfant.

Techniquement, les deux options sont correctes et sélectionneront le même élément. Mais la différence réside dans la portée de la requête.

L'exemple 1 interroge (ou recherche) le document entier pour trouver et sélectionner l'enfant. Cela est moins performant et même inutile car le parent de l'élément que vous souhaitez sélectionner est déjà mis en cache.

L'exemple 2 réduit la portée de la requête (ou recherche) en interrogeant uniquement l'élément parent et non le document entier. C'est pourquoi il est préféré car il est plus performant – surtout lorsque le document est volumineux.

Notez également que la méthode utilisée pour interroger le parent est `querySelector`. L'utilisation de `getElementById` pour interroger le parent ne fonctionnera pas et entraînera une erreur.

## Utiliser les classes CSS pour styliser les éléments

Il est préférable d'utiliser les classes CSS pour styliser les éléments plutôt que d'utiliser des styles en ligne. Les classes sont faciles à maintenir par rapport aux styles en ligne qui peuvent être difficiles à gérer.

La propriété `classList` dispose de propriétés utiles comme add, remove, toggle, et d'autres qui facilitent la modification des styles.

Exemple :

```css
.styledClass {
  color: red;
}
```

```javascript
element.classList.add('styledClass')
```

Cet exemple utilise la propriété `.add` de `classList` pour ajouter la classe `styledClass` à l'élément. En supposant que vous souhaitiez supprimer la classe de l'élément, vous pouvez facilement le faire en utilisant la propriété `.remove` à la place de add.

## Utiliser `innerHTML` avec prudence

La propriété `innerHTML` lit et analyse le balisage HTML que vous lui passez. Cela signifie qu'elle peut lire et exécuter du code dans une balise de script qui lui est passée. Et cela peut poser un risque de sécurité pour votre application.

Dans la mesure du possible, utilisez la propriété `innerText` ou `textContent` pour rendre des chaînes de caractères. Mais si vous devez utiliser `innerHTML`, assurez-vous de l'utiliser pour insérer du contenu provenant de sources de confiance. Ou nettoyez et validez le contenu fourni avec une bibliothèque comme DOMPurify.

Vous pouvez lire [cet article de freeCodeCamp](https://www.freecodecamp.org/news/innerhtml-vs-innertext-vs-textcontent/#what-is-the-innerhtml-property) pour en savoir plus sur `innerHTML`.

## Écrire des écouteurs d'événements lisibles

Souvent, vous passerez deux arguments aux écouteurs d'événements. Le premier est l'événement que vous écoutez et le second est le gestionnaire d'événement (la fonction qui se déclenche lorsque l'événement se produit).

Pour rendre votre code facile à lire et à maintenir, vous pouvez définir la fonction de gestionnaire d'événement en dehors de l'écouteur d'événement. Ensuite, vous pouvez l'appeler dans l'écouteur d'événement, comme dans l'exemple 1 ci-dessous :

```javascript
Exemple 1 ✅

MyElement.addEventListener('click', handleClick) 

function handleClick() { 
    // votre logique va ici.. 
} 

// Exemple 2 ❌ 

myElement.addEventListener('click', function() { 
    // votre logique va ici... 
})
```

Les deux sont techniquement corrects et feront la même chose. Mais l'exemple 1 est préféré car il est plus facile à lire. De plus, vous pouvez réutiliser la fonction `handleClick` si nécessaire. Cela vous aide à observer le principe DRY (Don't Repeat Yourself).

## Utiliser la délégation d'événements pour gérer les événements du DOM

La délégation d'événements consiste à attacher un écouteur d'événement sur un élément parent pour écouter les événements sur ses descendants. Avec cette technique, vous pouvez réduire le nombre d'écouteurs d'événements à inclure dans votre code.

Par exemple, supposons que vous avez cinq boutons à l'intérieur d'un div parent :

```html
<div id="parent"> 
    <button id="btn-1">1er Bouton</button> 
    <button id="btn-2">2ème Bouton</button> 
    <button id="btn-3">3ème Bouton</button> 
    <button id="btn-4">4ème Bouton</button> 
    <button id="btn-5">5ème Bouton</button> 
</div>
```

Vous pouvez ajouter un écouteur d'événement à chacun des cinq boutons pour écouter un clic. Ou en utilisant la délégation d'événements, vous pouvez ajouter un seul événement sur le div parent uniquement :

```javascript
const parentElement = document.getElementById('parent') 

parentElement.addEventListener('click', handleClick) 

function handleClick(event) { 
  alert(event.target.id) 
}
```

Dans cet exemple, l'événement est délégué à l'élément parent. Et nous utilisons `event.target.id` pour obtenir le bouton réel sur lequel l'utilisateur a cliqué. Si vous êtes curieux, vous pouvez [exécuter le code sur Stackblitz](https://stackblitz.com/edit/js-r3qjyd?file=index.html,index.js) pour voir comment cela fonctionne.

La délégation d'événements aide à gagner du temps et à améliorer les performances. Imaginez comment cette technique peut être utile lorsque vous traitez avec une grande quantité de contenu dynamique.

## Grouper les mises à jour du DOM avec Fragment

Les mises à jour fréquentes du DOM peuvent affecter les performances de votre application. Essayez de réduire le nombre de mises à jour lorsque cela est possible.

Une fonctionnalité utile que vous pouvez utiliser pour regrouper les mises à jour est la propriété `.createDocumentFragment`. Elle vous permet de regrouper plusieurs mises à jour avant de les insérer dans le document. Cela réduit les reflows et rend votre code plus efficace.

Exemple sans Fragment :

```javascript
const container = document.getElementById('container')

for (let i = 0; i < 1000; i++) { 
    const listItem = document.createElement('li')
    listItem.textContent = `Item ${i}`
    container.appendChild(listItem) 
}
```

Ce code met à jour le DOM à chaque itération de la boucle. Cela signifie que le DOM sera mis à jour 1 000 fois. Il existe une méthode plus efficace pour faire cela avec le code ci-dessous qui utilise un fragment.

Exemple avec fragment :

```javascript
const container = document.getElementById('container') 
const fragment = document.createDocumentFragment()

// Ajouter plusieurs éléments de liste au fragment 
for (let i = 0; i < 1000; i++) { 
    const listItem = document.createElement('li') 
    listItem.textContent = `Item ${i}` 
    fragment.appendChild(listItem)
} 

container.appendChild(fragment)
```

Le code ci-dessus ajoute l'élément `listItem` au `fragment` à chaque itération de la boucle. Il n'ajoute l'enfant à l'élément `container` qu'après l'exécution de la boucle. Cela signifie que le DOM est mis à jour une seule fois au lieu de 1 000 fois comme avant.

## Utiliser la méthode `stopPropagation`

La méthode `stopPropagation` contrôle le flux des événements dans le DOM. Par défaut, lorsqu'un événement se produit sur un élément, il remonte (se propage) à travers ses ancêtres.

Ce comportement de propagation des événements peut parfois entraîner des résultats non intentionnels. La méthode `stopPropagation` fournit un moyen d'empêcher l'événement de se propager au parent et aux autres ancêtres.

Prenons une situation où vous avez un bouton à l'intérieur d'un div parent. Et vous voulez gérer un événement de clic sur le bouton sans enregistrer le clic sur le div :

```html
<div id="container">
    <button id="button">Cliquez-moi</button>
</div>
```

```javascript
const containerDiv = document.getElementById('container')
const buttonElement = document.getElementById('button')

containerDiv.addEventListener('click', handleDivClick)
buttonElement.addEventListener('click', handleBtnClick)

function handleDivClick() { 
    console.log('Div cliqué')
} 

function handleBtnClick(event) { 
    event.stopPropagation()
    console.log('Bouton cliqué')
}
```

Sans utiliser la méthode `stopPropagation`, un événement de clic sur le bouton déclenchera également un événement de clic sur le div parent. Cela signifie que les deux gestionnaires d'événements s'exécuteront.

Mais la ligne `event.stopPropagation()` dans le code empêchera la fonction `handleDivClick` de s'exécuter lorsque l'utilisateur clique sur le bouton.

Vous pouvez [exécuter le code sur Stackblitz](https://stackblitz.com/edit/js-wjmnd5?file=index.html,index.js) pour voir comment cela fonctionne. Commentez la ligne avec la méthode `stopPropagation` et voyez la différence.

## Tester votre code de manipulation du DOM

Lorsque vous écrivez des tests, vous créez des scénarios qui imitent les interactions des utilisateurs ou les états de l'application. Vous vérifiez également que votre application vous donne les résultats attendus.

Tester votre code de manipulation du DOM est une bonne pratique car cela rendra votre code fiable et facile à maintenir. Cela vous donne également confiance que votre code se comporte comme prévu, même lorsqu'il évolue au fil du temps lorsque vous apportez des modifications et ajoutez des fonctionnalités.

Vous pouvez utiliser des frameworks et bibliothèques de test disponibles pour JavaScript, tels que Jest, Mocha, Jasmine, et d'autres pour automatiser les tests de vos applications.

L'exemple suivant utilise le framework Jest pour tester le code de manipulation du DOM pour ajouter une classe à un élément.

```javascript
test('Ajouter une classe highlight change la couleur du texte en rouge', () => {
    myElement.classList.add('highlight');
    expect(getComputedStyle(myElement).color).toBe('red');
});
```

L'ajout de la classe `highlight` est censé changer la couleur du texte en rouge. Si le test passe, cela signifie que votre code de manipulation du DOM fonctionne comme prévu. Sinon, vous devrez déterminer ce qui ne va pas et corriger le problème.

## Conclusion

Dans cet article, vous avez appris dix bonnes pratiques à garder à l'esprit lorsque vous travaillez avec le DOM. Certaines d'entre elles sont générales tandis que d'autres sont spécifiques à des situations. En utilisant ces bonnes pratiques dans votre flux de travail, vous construirez vos applications web avec une base de code facile à maintenir.

Si vous souhaitez approfondir la manipulation du DOM, [j'ai écrit un manuel complet](https://www.freecodecamp.org/news/the-javascript-dom-manipulation-handbook/) qui couvre le sujet en profondeur.

Merci d'avoir lu. Et bon codage ! Pour plus de tutoriels approfondis, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours)
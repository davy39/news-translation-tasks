---
title: Comment manipuler le DOM - le guide ultime pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-19T01:06:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-manipulate-the-dom-beginners-guide
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6001cc5998be260817e4a4bd.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: Comment manipuler le DOM - le guide ultime pour débutants
seo_desc: 'By Chibuike Okere

  Okay, so I assume you have heard of the almighty DOM — that’s why you are here,
  right? If you are finding it difficult, I can assure you that after reading this
  article, you will feel comfortable enough with the whole DOM manipulati...'
---

Par Chibuike Okere

D'accord, donc je suppose que vous avez entendu parler du tout-puissant DOM — c'est pourquoi vous êtes ici, n'est-ce pas ? Si vous trouvez cela difficile, je peux vous assurer qu'après avoir lu cet article, vous vous sentirez suffisamment à l'aise avec toute cette histoire de manipulation du DOM. 

Mais s'il vous plaît, avant que je ne commence, permettez-moi de partager avec vous ma petite histoire sur la façon dont j'ai découvert le DOM (c'est une histoire drôle).

## Comment j'ai appris le DOM

Quelques mois après le début de ma carrière en développement web, j'apprenais encore le bon vieux HTML et CSS. J'ai accidentellement tombé sur un cours sur le DOM sur w3schools. Le premier exemple qu'ils avaient était celui avec une ampoule et deux boutons. 

Le onclick de l'un des boutons "allumait" l'ampoule et le onclick du second bouton "éteignait" l'ampoule. J'ai littéralement été soufflé.

Comment un bouton sur un site web pouvait-il allumer une ampoule ? Comment !? 

J'ai même tweeté à ce sujet. Ensuite, j'ai découvert qu'ils changeaient simplement l'attribut source (src) des images. J'ai été déçu, mais malgré cela, cette petite expérience m'a fait tomber amoureux du DOM. Cela m'a donné envie d'en savoir plus. 

Et dans cet article, je vais vous guider à travers tout cela. Je promets que si vous restez avec moi jusqu'à la fin et pratiquez tout ce que j'écris, toute cette histoire de DOM ne sera plus un problème pour vous. Alors, êtes-vous prêt ? Ok Allons-y (c'est parti !).

>Pour rendre cela plus facile à comprendre, j'ai regroupé tout cela dans les sections suivantes.

* Définition du DOM et concepts de base 
* Comment sélectionner des éléments dans le DOM
* Comment parcourir et se déplacer dans le DOM
* Comment manipuler des éléments dans le DOM 
* Styling général 
* Gestion des événements dans le DOM

Alors, prenez un café ou ce que vous voulez et détendez-vous pendant que je vous guide à travers chaque section.

![vvv-1](https://media.giphy.com/media/ceeFbVxiZzMBi/source.gif)

## Définition du DOM et concepts de base
### Qu'est-ce que le DOM ? 

Le DOM signifie Document Object Model. Il peut simplement être compris comme un arbre de nœuds créé par le navigateur. Chacun de ces nœuds a ses propres propriétés et méthodes qui peuvent être manipulées en utilisant JavaScript. 

La capacité à manipuler le DOM est l'une des compétences les plus uniques et utiles de JavaScript. 

L'image ci-dessous donne une représentation visuelle de ce à quoi ressemble l'arbre DOM. 

![images](https://www.freecodecamp.org/news/content/images/2021/01/images.png)

Ici, nous avons l'objet document. C'est le cœur/fondation du DOM. Pour effectuer toute forme de manipulation du DOM, vous devez d'abord accéder à l'objet document. 

Ensuite, nous avons l'élément racine `html` qui est un enfant de l'objet document. 

Ensuite, nous avons les éléments `body` et `head` qui sont frères et sœurs l'un de l'autre et enfants de l'élément `html`.

Sous l'élément head, nous avons l'élément title que vous pouvez considérer comme l'enfant de l'élément head et le parent du nœud texte - "my text".

Directement sous l'élément body, nous avons deux éléments (la balise `a` et la balise `h1`) qui sont frères et sœurs l'un de l'autre et enfants de l'élément body.

Enfin, l'attribut `href` et le nœud texte - "my link" - sont des enfants de la balise `a`. Exactement de la même manière que le nœud texte, "My header", est un enfant de l'élément `h1`.

Cela peut sembler un peu confus si vous êtes un débutant absolu, mais faites-moi confiance - cela s'améliore toujours (avec la pratique, bien sûr).


## Comment sélectionner des éléments dans le DOM

Pour pouvoir manipuler un élément dans le DOM, vous devez sélectionner cet élément particulier. Heureusement pour nous, nous avons 4 principales façons de sélectionner des éléments. 

### Comment sélectionner des éléments DOM avec la méthode getElementById

La manière la plus courante d'accéder à un élément HTML est d'utiliser l'id de l'élément.

Dans l'exemple ci-dessous, la méthode `getElementById()` utilise id="master" pour trouver l'élément

```javascript
<p id="master">j'adore javascript</p>

 <script>
const masterEl = document.getElementById('master')
console.log(masterEl) //<p id="master">j'adore javascript</p> 
 </script>
```


L'id est sensible à la casse. Par exemple, 'master' et 'Master' sont des identifiants totalement différents.

Une fois que vous avez sélectionné un élément, vous pouvez ajouter des styles à l'élément, manipuler ses attributs et parcourir les éléments parent et enfant.


### Comment sélectionner des éléments DOM avec la méthode getElementsByClassName()

Cette méthode retourne une collection de tous les éléments dans le document avec le nom de classe spécifié.

Par exemple, notre page HTML ci-dessous contient trois éléments avec class="master2", et j'ai sélectionné le bouton avec l'id 'btn'. 

Si vous cliquez sur le bouton, il sélectionnera tous les éléments avec un nom de classe "master2" et changera le innerHTML du 3ème élément.


```javascript
        <p class="master2">j'adore javascript</p>
        <p class="master2">j'adore react</p>
        <h1 class="master2">je veux un travail</h1>

        <button id="btn">cliquez-moi</button>
 
 <script>
 
 const btn = document.getElementById('btn')
        
        btn.addEventListener('click', function master(){
            var master = document.getElementsByClassName("master2");
            master[2].innerHTML = 'j'ai besoin d'un travail';
        })

</script>
```

Avant que le bouton ne soit cliqué, voici ce que vous voyez :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/22.png)

Après que le bouton soit cliqué, vous voyez :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/444.png)

>Je sais que j'ai utilisé `addEventListener()` que je n'ai pas encore expliqué, mais restez avec moi. C'est définitivement une partie de ce que je vais vous expliquer ci-dessous :)

### Comment sélectionner des éléments DOM avec la méthode getElementsByTagName()

Cette méthode accepte un nom de balise et retourne tous les éléments du nom de balise spécifié dans l'ordre où ils apparaissent dans le document.

Le code suivant illustre la syntaxe de `getElementsByTagName()` en obtenant tous les éléments `p` sur la page et en changeant le contenu du deuxième élément. 

```javascript
 <p>VsCode</p>
 <p>Atom</p>
 <p>Sublime text</p>
        <button id="btn">cliquez-moi</button>
       

 <script>

const btn = document.getElementById('btn')
        
        btn.addEventListener('click', function master(){
            let master = document.getElementsByTagName('p');
            let masterEl = master[1].innerHTML = 'Éditeurs de code';
            console.log(masterEl) //Éditeurs de code
        })

//<p>Atom</p> devient <p>Éditeurs de code</p>
</script>
```

### Comment sélectionner des éléments DOM avec des sélecteurs CSS

#### .querySelector() 

Cela retourne la première valeur qui correspond au sélecteur donné. Cette méthode peut accepter tous les sélecteurs de style CSS, permettant de sélectionner par balise, classe ou ID.



```javascript
<div id=master>je suis un développeur frontend</div>

<script>
const master = document.querySelector("#master") 
</script>
```

Cette méthode ci-dessus prend un argument, qui est un sélecteur CSS, et retourne le premier élément qui correspond au sélecteur.

#### .querySelectorAll() 

Cela fonctionne de manière similaire à ci-dessus, qui retourne une collection de nœuds de tous les éléments correspondants.

```
     <p class="master">React</p>
     <p class="master">Vue</p>
     <p class="master">Angular</p>

<script>
const master = document.querySelectorAll(".master") 
console.log(master[1])  //<p class="master">Vue</p>
</script>
```

### Résumé de la sélection des éléments DOM

Lorsque vous devez sélectionner un élément DOM, vous avez quatre options différentes parmi lesquelles choisir, quatre façons différentes de faire une chose particulière (sélectionner un ou des éléments).

Donc, si vous ne vous souvenez pas de la première, vous utilisez la deuxième. Et si par hasard vous ne vous souvenez pas des deux, vous avez toujours les options 3 et 4. Est-ce seulement moi ou est-ce que JavaScript facilite notre vie ? :)

Ma recommandation personnelle est de rester avec l'option 1 ou l'option 4a (queryselector avec un Id). Dès vos premiers jours d'apprentissage du HTML, vous avez probablement compris que les éléments ne devraient pas avoir le même id, c'est-à-dire que l'id est un identifiant unique d'un élément dans le document. 

Avec cela en tête, sélectionner un élément avec son id est un "paris sûr" car vous n'appliquerez pas la même "manipulation" à différents éléments (sauf si c'est ce que vous voulez réaliser - alors soyez mon invité, n'hésitez pas à utiliser d'autres options). 

## Comment parcourir le document

À ce stade, vous serez probablement d'accord avec moi pour dire que tout dans un document HTML est un nœud. De plus, le texte à l'intérieur des éléments HTML sont des nœuds de texte.

Avec le DOM HTML, vous pouvez naviguer dans l'arbre de nœuds et accéder aux nœuds dans l'arbre en utilisant les relations de nœuds dont nous avons parlé précédemment (parent, enfant(s), frère(s) et sœur(s), etc).

> De nouveaux nœuds peuvent être créés, et tous les nœuds peuvent être modifiés ou supprimés.

### Une petite révision
* Chaque nœud a exactement un parent, sauf le nœud supérieur (qui n'a pas de parent).
* Un nœud peut avoir plus d'un enfant.
* Les frères et sœurs sont des nœuds avec le même parent.

Dans cette section, nous allons voir comment obtenir l'élément parent, les frères et sœurs d'un élément, et les enfants d'un élément. Je vais utiliser les propriétés de nœuds suivantes pour réaliser ces choses :

* parentNode
* childrenNodes
* firstElementChild
* lastElementChild
* nextElementSibling
* previousElementSibling

De plus, je vais utiliser uniquement cette page HTML ci-dessous pour vous montrer comment nous utilisons chacune de ces propriétés de nœuds. Et à partir de la section 4 ci-dessus, je vais vous montrer comment manipuler le DOM.

C'est l'objectif de cet article - savoir comment manipuler le DOM. Cela n'a pas vraiment d'importance si vous savez comment sélectionner des éléments et parcourir le DOM si vous ne savez pas comment le manipuler. Il est important de savoir comment ajouter un style CSS, créer et ajouter des éléments, définir innerHTML et gérer les événements. 

C'est le cœur de cet article, alors s'il vous plaît restez avec moi. Continuons.

```javascript
 <div id="parent">
        <div id="firstchild">je suis le premier enfant</div>
        <p id="secondchild">je suis le deuxième enfant</p>
        <h4>je suis vivant</h4>
        <h1>bonjour le monde</h1>
        <p>je suis le dernier enfant</p>
    </div>  
    
    const parent = document.getElementById('parent').lastElementChild
    console.log(parent) //<p>je suis le dernier enfant</p>
    
    const parent2 = document.getElementById('parent').children[3]
    console.log(parent2) //<h1>bonjour le monde</h1>
    
    const secondchild = document.getElementById('secondchild')
    console.log(secondchild) //<p id="secondchild">je suis le deuxième enfant</p>
    
    console.log(secondchild.parentNode) //<div id="parent">...</div>

    console.log(secondchild.nextElementSibling) //<h4>je suis vivant</h4>

    console.log(secondchild.previousElementSibling) //<div id="firstchild">je suis le premier enfant</div>
```

## Comment manipuler des éléments dans le DOM
Dans cette section, nous allons voir :

* Comment créer des éléments
* Comment définir le innerHTML/contenu texte d'un élément
* Comment ajouter un élément
* Comment insérer un élément avant un autre
* Comment remplacer un élément enfant
* Comment supprimer un élément enfant

```html

    <div id="parent">
        <div id="firstchild">je suis le premier enfant</div>
        <p id="secondchild">je suis le deuxième enfant</p>
        <h4>je suis vivant</h4>
        <h1>bonjour le monde</h1>
        <p>je suis le dernier enfant</p>
    </div>  

```

### Comment créer des éléments

Le code ci-dessus montre un élément parent avec 5 éléments enfants. Supposons que nous voulons ajouter une autre balise `div` avec JavaScript. Nous devrons définitivement créer un nouvel élément avec la méthode `createElement()`, comme ceci :

```javascript
 const createEl = document.createElement('div')
 console.log(createEl) //<div></div>
```

### Comment définir innerHTML

Nous avons créé avec succès une balise `div`, mais actuellement elle n'a aucun nœud texte. Nous allons utiliser la propriété `.innerHTML()` pour ajouter son nœud texte.

```javascript
 const innerhtml = createEl.innerHTML = 'je suis un développeur frontend'
 console.log(createEl) //<div>i suis un développeur frontend</div>

```

### Comment ajouter un élément

Ce que nous avons réalisé jusqu'à présent est la création d'un élément et l'insertion de son nœud texte. Mais cet élément créé ne fait pas encore partie de l'arbre DOM.

Alors maintenant, je vais vous montrer comment l'ajouter à cette page HTML dans cette section. En construisant sur le code ci-dessus :

```javascript
 const createEl = document.createElement('div')

 const innerhtml = createEl.innerHTML = 'je suis un développeur frontend'

 const parentEl = document.getElementById('parent')

 parentEl.appendChild(createEl)

 console.log(parentEl) 

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Document---Google-Chrome-16_01_2021-11_50_14-PM--2-.png)

### Comment insérer un élément avant un autre

Si vous avez remarqué à partir de l'image du journal de la console ci-dessus, l'enfant ajouté `div` a été ajouté automatiquement en bas.

Et si pour une raison quelconque vous voulez l'ajouter à l'endroit de votre choix ? Peut-être avant le premier élément ou avant le quatrième élément. Je suis ici pour vous dire que c'est tout à fait possible. Dans le code ci-dessous, nous allons l'ajouter avant l'élément actuel.

Nous allons utiliser la méthode JavaScript `insertBefore()` qui accepte deux paramètres, le `newNode` et le `existingNode` dans cet ordre => `document.insertBefore(newNode, existingNode)`.


```javascript
 const parentEl = document.getElementById('parent')
 const firstchildEl = document.getElementById('firstchild')
 
 const createEl = document.createElement('div')

 const innerhtml = createEl.innerHTML = 'je suis un développeur frontend'

 parentEl.insertBefore(createEl, firstchildEl)
   console.log(parentEl)

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/mmm.png)

### Comment remplacer un élément enfant

Nous allons utiliser la méthode JavaScript `replaceChild()` qui accepte deux paramètres pour remplacer notre premier élément par le nouvellement créé. Cela fonctionne dans cet ordre => `document.replaceChild(newNode, existingNode)`.


```javascript
 const firstchildEl = document.getElementById('firstchild')
 const parentEl = document.getElementById('parent')

 const createEl = document.createElement('div')
 const innerhtml = createEl.innerHTML = 'je suis un développeur frontend'

 parentEl.replaceChild(createEl, firstchildEl)

   console.log(parentEl)

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/kkk.png)

### Comment supprimer un élément enfant

Nous allons utiliser la méthode JavaScript `removeChild()` qui accepte un seul paramètre (c'est-à-dire l'élément que vous voulez supprimer, qui dans ce cas est notre premier élément d'origine). Cela fonctionne dans cet ordre => `document.removeChild(element)`


```javascript
const firstchildEl = document.getElementById('firstchild')
 const parentEl = document.getElementById('parent')
 
 parentEl.removeChild(firstchildEl)

 console.log(parentEl)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/vvv.png)

## Comment ajouter du style avec CSS
D'après les exemples précédents, nous avons vu comment créer un élément et l'ajouter à l'élément parent spécifié.

Par conséquent, pour qu'un élément ait un style, nous devons lui ajouter une classe CSS. Dans ce cas, nous allons le faire avec JavaScript.

Je ne vais pas seulement vous montrer comment ajouter une classe. Je vais également vous montrer comment supprimer une classe et comment basculer entre les classes.

Ne vous inquiétez pas, ce n'est pas difficile. Je suis ici pour vous guider à travers tout cela.

### Comment ajouter une classe CSS

Actuellement, nous avons un bouton HTML normal avec un id "master" mais sans aucun style appliqué. Voir l'image ci-dessous :

![ttt](https://www.freecodecamp.org/news/content/images/2021/01/ttt.png)

La première chose que nous allons faire est de créer le style CSS pour le bouton.

Ensuite, dans notre JavaScript, j'ajouterai un écouteur d'événement au bouton afin que, lorsque vous cliquez dessus, JavaScript ajoute automatiquement le style CSS avec une classe "button".

```javascript
 <style>
        body{
            background-color: hotpink;
            display: flex;
            align-items: center;
        }

        .button{
            background-color: blueviolet;
            width: 200px;
            border: none;
            font-size: 2rem;
            padding: 0.5rem;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    

  <button id="master">Cliquez-moi</button>
  
    
const buttonEl = document.getElementById('master')
buttonEl.addEventListener('click', addFunction)

 function addFunction(){
     buttonEl.classList.add('button')
  }
```

Après avoir cliqué sur le bouton, vous verrez ce qui suit. C'est beau, n'est-ce pas ?

![Image](https://www.freecodecamp.org/news/content/images/2021/01/jjj.png)

### Comment supprimer une classe

En utilisant le même exemple ci-dessus, nous allons supprimer le style CSS, cette fois avec `classList.remove()` en JavaScript. Vous avez probablement déjà deviné ce qui allait se passer, n'est-ce pas ?

Exactement, le bouton reviendra à son état par défaut.

```javascript

const buttonEl = document.getElementById('master')
buttonEl.addEventListener('click', addFunction)

function addFunction(){
    buttonEl.classList.remove('button')
 }
 
```

 ### Comment basculer une classe
 
Disons que vous ne voulez pas supprimer complètement le style CSS. Vous voulez un moyen de basculer entre le bouton stylisé et non stylisé.

La méthode JavaScript `classList.toggle()` vous donne cette capacité.

La méthode `classList.toggle()` est typiquement utilisée sur la plupart des plateformes de médias sociaux comme Twitter. Elle vous permet d'aimer une publication avec un bouton et de ne plus l'aimer avec ce même bouton quand vous le souhaitez.

Ainsi, JavaScript vérifie si notre bouton a la classe CSS.

S'il a la classe et que vous cliquez sur le bouton, il la SUPPRIME. S'il n'a pas la classe et que vous cliquez sur le bouton, il l'AJOUTE.

```javascript

const buttonEl = document.getElementById('master')
buttonEl.addEventListener('click', addFunction)


function addFunction(){
    buttonEl.classList.toggle('button')
 }
 
```

# Gestion des événements

### Qu'est-ce que les événements HTML ?

Les événements HTML sont des "choses" qui arrivent aux éléments HTML comme le clic sur un bouton, la saisie dans une zone de texte, etc. Lorsqu'un événement se produit comme ceux ci-dessus, vous pouvez écrire du code JavaScript que nous appelons un gestionnaire d'événements qui sera exécuté.

Ces gestionnaires d'événements sont des fonctions JavaScript. Donc, lorsqu'un événement se produit sur un élément, la fonction de gestion est exécutée.

### Écouteurs d'événements

Jusqu'à présent, nous avons utilisé des écouteurs d'événements dans pratiquement tous les exemples ci-dessus. Cela devrait montrer à quel point les écouteurs d'événements sont importants dans la manipulation du DOM.

Pour ajouter un écouteur d'événements à un élément ou à un objet DOM, nous avons besoin d'une méthode qui est `addEventListener()`. Cette méthode est préférée à l'ancienne où nous incluions l'événement à gérer dans le balisage HTML. 

Avec cela, le JavaScript est séparé du balisage HTML, ce qui le rend plus propre et plus lisible.

J'aime l'idée d'un JS séparé, d'un CSS séparé, etc., donc si vous êtes comme moi, vous aimerez cet écouteur d'événements.

Un écouteur d'événements accepte 3 paramètres. 

* Le premier est le type d'événement, comme "click", etc.
* Le deuxième paramètre est la fonction à exécuter.
* Le troisième paramètre est une valeur booléenne spécifiant si utiliser le bouillonnement d'événements ou la capture d'événements. **Ce paramètre est facultatif.**

>Vous pouvez ajouter de nombreux gestionnaires d'événements à un élément.

>Vous pouvez également ajouter de nombreux gestionnaires d'événements du même type à un élément, comme deux événements "click".

## Conclusion
Savoir comment manipuler le DOM avec JavaScript est très important. Ce n'est pas quelque chose que vous pouvez décider de ne pas savoir.

Si vous comprenez les exemples/illustrations que j'ai donnés ci-dessus, vous pourrez peut-être construire de **petits** projets JS. Je ne peux pas trop insister sur l'importance de construire des projets si vous voulez être un bon développeur.

![kkk-1](https://media.giphy.com/media/mVJ5xyiYkC3Vm/source.gif)
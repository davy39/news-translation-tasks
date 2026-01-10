---
title: Comment créer un élément de sélection personnalisé accessible
subtitle: ''
author: Elizabeth Lola
co_authors: []
series: null
date: '2024-01-04T17:06:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-accessible-custom-dropdown-select-element
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/a11y-select.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment créer un élément de sélection personnalisé accessible
seo_desc: "Sometimes you might want to use a different select element to match your\
  \ style based on the theme of your design. Or perhaps the default design is different\
  \ on separate browsers and you want uniformity. \nBut when designing this new element,\
  \ you might..."
---

Parfois, vous pourriez vouloir utiliser un élément de sélection différent pour correspondre à votre style basé sur le thème de votre design. Ou peut-être que le design par défaut est différent sur des navigateurs séparés et vous voulez de l'uniformité. 

Mais lors de la conception de ce nouvel élément, vous pourriez oublier de considérer l'accessibilité du composant. 

Typiquement, les éléments par défaut sont accessibles – et si vous prévoyez de les remplacer par des designs personnalisés, vous devriez vous assurer qu'ils fonctionnent aussi bien que les éléments par défaut.

Dans ce tutoriel, je vais vous montrer comment construire une liste déroulante personnalisée avec un exemple étape par étape.

## Prérequis

Pour suivre ce tutoriel, vous devriez avoir :

1. **Connaissances de base en HTML** : Comprendre comment les éléments et attributs HTML fonctionnent.
2. **Connaissances de base en JavaScript** : Familiarité avec les concepts de base de JavaScript comme les fonctions, la gestion des événements et la manipulation du DOM est utile.
3. **Compréhension d'ARIA** : Bien que le tutoriel explique les rôles et attributs ARIA, avoir une compréhension de base des concepts d'accessibilité peut être bénéfique.

## Voici ce que nous allons couvrir :

1. [Fonctionnalités de la sélection par défaut](#heading-fonctionnalites-de-la-selection-par-defaut)
2. [Comment déterminer quels attributs ARIA sont requis](#heading-comment-determiner-quels-attributs-aria-sont-requis)
3. [Comment configurer le HTML](#heading-comment-configurer-le-html)
4. [Le CSS](#heading-le-css)
5. [Le JavaScript](#heading-le-javascript)  
– [Basculer la visibilité de la liste déroulante](#heading-basculer-la-visibilite-de-la-liste-deroulante)  
– [Comment fermer la liste déroulante](#heading-fermer-la-liste-deroulante-en-utilisant-la-touche-esc)  
– [Interaction clavier de la liste déroulante](#heading-interaction-clavier-de-la-liste-deroulante)  
– [Comment corriger le problème de visibilité des options](#heading-corriger-le-probleme-de-visibilite-des-options)  
– [Comment mettre en surbrillance les options lors de la pression sur une touche alphanumérique](#heading-mettre-en-surbrillance-les-options-lors-de-la-pression-sur-une-touche-alphanumerique)  
– [Comment améliorer la fonctionnalité du lecteur d'écran](#heading-ameliorer-la-fonctionnalite-du-lecteur-decran)
6. [Conclusion](#heading-conclusion)

## Fonctionnalités de la sélection par défaut

Puisque l'attribut de sélection par défaut est accessible, examinons certaines des fonctionnalités qui le rendent accessible :

* L'élément de sélection indique visiblement lorsqu'il est actif ou sélectionné, généralement par un changement d'apparence.
* L'élément s'ouvre au clic ou à la pression d'une touche (ESPACE, HAUT et BAS)
* Pendant que la liste déroulante est ouverte, les utilisateurs peuvent se déplacer parmi les options disponibles en appuyant sur les touches fléchées HAUT ou BAS.
* La saisie de touches alphanumériques lorsque la liste déroulante est ouverte met en surbrillance l'option qui correspond aux lettres saisies. Si aucune correspondance n'est trouvée, rien ne change.
* Le clic sur une option ou la pression des touches ESPACE ou ENTRÉE lorsqu'une option est mise en surbrillance sélectionne cette option, met à jour la valeur de sélection et ferme la liste déroulante.
* Si la liste déroulante est ouverte, la pression de la touche ÉCHAP ferme la liste déroulante, offrant un moyen rapide d'annuler la sélection ou de fermer la liste déroulante.
* Lorsque l'élément de sélection est focalisé lors de l'utilisation d'un lecteur d'écran, le lecteur d'écran annonce qu'il s'agit d'un élément de sélection et fournit des informations sur la valeur actuellement sélectionnée pour l'accessibilité.

En utilisant ces informations, construisons une liste déroulante personnalisée.

## Comment déterminer quels attributs ARIA sont requis

Bien que les rôles et les noms accessibles de certains éléments soient évidents, il y en a d'autres qui ne le sont pas. Chaque fois que j'ai besoin de trouver le rôle ou l'attribut ARIA approprié pour un composant, je consulte le guide des [noms accessibles W3](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/#accessiblenameguidancebyrole). 

Dans ce cas, je sais que la liste déroulante personnalisée devrait avoir un `role="options"` mais je ne sais pas quel rôle attribuer aux éléments parents. 

Pour commencer, je localise la liste **Accessible Name Guidance by Role**. Vous pouvez voir que l'Option pointe vers un modèle de combobox.

![Liste des options dans le tableau Accessible Name Guidance by Role](https://www.freecodecamp.org/news/content/images/2023/12/image-74.png)
_L'option dans le tableau montre une combobox._

  
La prochaine chose que je dois faire est de lire davantage sur la combobox. Selon [cette page MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/combobox_role#examples), je comprends qu'une combobox est un composant qui combine un élément de type input avec une liste déroulante et permet aux utilisateurs de sélectionner parmi une liste d'options présentées dans la liste déroulante.

Cela ressemble exactement à ce que fait l'élément select. La combobox doit également avoir un attribut `[aria-expanded](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-expanded)` et un élément popup de connexion qui contiendra la liste des options. Selon la page MDN :

> L'élément popup associé à une `combobox` peut être soit un élément [`listbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/listbox_role), [`tree`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/tree_role), [`grid`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/grid_role), ou [`dialog`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/dialog_role).

Dans cet exemple, nous utiliserons un élément `listbox`.

L'élément combobox doit avoir des attributs `aria-contols` et `aria-haspopup`, la valeur de ces attributs sera l'ID de l'élément `listbox`. 

## Comment configurer le HTML

À partir des informations recueillies, nous aurons besoin d'une `combobox`, d'une `listbox` et d'une `option` pour configurer notre HTML.

Dans cet exemple, le HTML ressemblera à ceci :

```html
<form>
  <label for="select">Boîte de sélection personnalisée</label>
  <button
     role="combobox"
     id="select"
     value="Select"
     aria-controls="listbox"
     aria-haspopup="listbox"
     tabindex="0"
     aria-expanded="false">
    Select</button>
  <ul role="listbox" id="listbox">
   <li role="option">Option 1</li>
   <li role="option">Option 2</li>
   <li role="option">Option 3</li>
  </ul>
</form>
```

Dans le code ci-dessus, le bouton a un `role="combobox"` et selon l'article MDN sur la combobox, l'attribut `[aria-expanded](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-expanded)` est requis lors de l'utilisation d'une combobox. L'attribut `aria-controls` pointe vers l'ID de la listbox qui est `listbox`. Cela associe la listbox à la combobox. 

## Le CSS

Vous pouvez styliser la liste déroulante comme vous le souhaitez en fonction de vos exigences. Voici un exemple de style pour mon composant :

```scss
.form {
  margin: 1.2rem 0;
  position: relative;
  #announcement {
    opacity: 0;
  }
  label {
    display: block;
    padding: .7rem .8rem;
    width: 65%;
    margin: 0 auto;
    text-align: left;
    font-size: .75rem;
  }
  button,
  ul{
    display: block;
    padding: .7rem .8rem;
    width: 60%;
    margin: 0 auto;
    text-align: left;
    background: white;
    border: 0;
    font-size: 1rem;
  }
  button{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    
    &::before {
      font-family: "Font Awesome 5 Free";
      content: "\f107";
      vertical-align: middle;
      font-weight: 900;
      position: absolute;
      right: .8rem;
    }

    &:focus-visible {
      outline: 0;
      box-shadow: 0 0 5px 2px rgba(251, 146, 60, 0.7) inset;
    }
  }
  ul {
    color: #3f403b;
    position: absolute;
    left: 0;
    right: 0;
    top: 4.8rem;
    max-height: 10rem;
    overflow-y: auto;
    list-style-type: none;
    padding: 0;
    margin-top: .1rem;
    opacity: 0;
    transform: scale(1,0);
    transform-origin: top left;
    transition: all .3s ease-in;
    pointer-events: none;
    z-index: 2;
    &.active {
      opacity: 1;
      transform: scale(1,1);
      pointer-events: auto;
    }
    li {
      padding: .6rem .5rem;
      border-top: 1px solid #e6e6e6;
      cursor: pointer;
      transition: all .3s ease-in;
      position: relative;
      &::before {
        font-family: "Font Awesome 5 Free";
        content: "\f00c";
        vertical-align: middle;
        font-weight: 900;
        position: absolute;
        right: .8rem;
        opacity: 0;
        transition: opacity .300s ease-out;
      }
      &:hover, &.current {
        background: #e6e6e6;
      }
      &.active {
        box-shadow: 0 0 0 2px rgba(251, 146, 60, 0.7);
      }
      &.active::before {
        opacity: 1;
      }
    }
  }
}

```

Dans le code ci-dessus, j'ai masqué l'élément listbox et ajouté une classe active qui le montre. J'ai également ajouté une classe current qui style l'option mise en surbrillance et une classe active qui style l'option sélectionnée.

Voici à quoi cela ressemble :

![Liste déroulante avec options](https://www.freecodecamp.org/news/content/images/2023/12/image-80.png)
_L'état actuel et l'état actif d'une option_

## Le JavaScript

Il est plus facile de décomposer les fonctionnalités et de travailler sur chacune d'elles une par une, et c'est ce que nous allons faire ici.

### Basculer la visibilité de la liste déroulante

Le fait de cliquer sur la combobox ou d'appuyer sur les touches `Espace` ou `Entrée` du clavier (lorsque le bouton est focalisé) doit basculer la visibilité de la liste déroulante :

```js
const elements = {
  button: document.querySelector('[role="combobox"]'),
  dropdown: document.querySelector('[role="listbox"]'),
}; // J'aime regrouper tous mes éléments dans un seul objet 👍.
let isDropdownOpen = false;

const toggleDropdown = () => {
  elements.dropdown.classList.toggle('active');
  isDropdownOpen = !isDropdownOpen;
  elements.button.setAttribute('aria-expanded', isDropdownOpen.toString()); // met à jour l'état aria-expanded
};

const handleKeyPress = (event) => {
   event.preventDefault();
  const { key } = event;
  const openKeys = ['Enter', ' '];

  if (openKeys.includes(key)) {
    toggleDropdown();
  }
};

elements.button.addEventListener('keydown', handleKeyPress);
elements.button.addEventListener('click', toggleDropdown);
```

Dans le code ci-dessus, nous avons créé un bouton de liste déroulante basculable qui répond aux interactions du clavier et de la souris. La fonction `toggleDropdown` ajoute une classe `active` à la liste déroulante.

### Fermer la liste déroulante : Utiliser la touche Échap

Appuyer sur la touche Échap ou cliquer en dehors de l'élément de la liste déroulante doit fermer la liste déroulante :

```js
// code précédent

// mettre à jour la fonction handleKeyPress 
const handleKeyPress = (event) => {
    event.preventDefault();
  const { key } = event;
  const openKeys = ['Enter', ' '];
    
  if (!isDropdownOpen && openKeys.includes(key) || (isDropdownOpen && key === 'Escape')) {
    toggleDropdown();
    
  }
};

const handleDocumentInteraction = (event) => {
  const isClickInsideButton = elements.button.contains(event.target);
  const isClickInsideDropdown = elements.dropdown.contains(event.target);

  if (isClickInsideButton || (!isClickInsideDropdown && isDropdownOpen)){
    toggleDropdown();
  }
};


elements.button.addEventListener('keydown', handleKeyPress);
// elements.button.addEventListener('click', toggleDropdown);
document.addEventListener('click', handleDocumentInteraction);
```

Bien qu'il puisse sembler que les fonctions `handleKeyPress` et `handleDocumentInteraction` pourraient être combinées pour simplifier, nous allons les garder séparées car ces fonctions géreront plus de tâches plus tard dans l'article.

Dans le code ci-dessus, nous avons mis à jour la fonction `handleKeyPress` pour vérifier `Escape` et avons également introduit une fonction `handleDocumentInteraction` pour fermer la liste déroulante s'il y a un clic en dehors de l'élément de la liste déroulante.

### Interaction clavier de la liste déroulante

Appuyer sur les touches fléchées `HAUT` ou `BAS` doit ouvrir la liste déroulante. Lorsque la liste déroulante est ouverte, ces touches doivent permettre de naviguer parmi les options, en déplaçant la sélection vers le haut ou vers le bas. De plus, cliquer sur une option ou appuyer sur les touches `Espace` ou `Entrée` alors qu'une option est focalisée doit mettre à jour la valeur affichée du bouton. Ce comportement vise à reproduire l'interaction d'un élément de sélection standard.

```js
const elements = {
  button: document.querySelector('[role="combobox"]'),
  dropdown: document.querySelector('[role="listbox"]'),
  options: document.querySelectorAll('[role="option"]'), // ajouter les éléments d'options
};
let isDropdownOpen = false;
let currentOptionIndex = 0;

const toggleDropdown = () => {
  elements.dropdown.classList.toggle('active');
  isDropdownOpen = !isDropdownOpen;
  elements.button.setAttribute('aria-expanded', isDropdownOpen.toString());

  if (isDropdownOpen) {
    focusCurrentOption();
  } else {
    elements.button.focus(); // focaliser le bouton lorsque la liste déroulante est fermée, comme l'élément select
  }
};

const focusCurrentOption = () => {
  const currentOption = elements.options[currentOptionIndex];

  currentOption.classList.add('current');
  currentOption.focus();

  elements.options.forEach((option, index) => {
    if (option !== currentOption) {
      option.classList.remove('current');
    }
  });
};

const handleKeyPress = (event) => {
  event.preventDefault();
  const { key } = event;
  const openKeys = ['ArrowDown', 'ArrowUp', 'Enter', ' '];

  if (!isDropdownOpen && openKeys.includes(key)) {
    toggleDropdown();
    
  } else if (isDropdownOpen) {
    switch (key) {
      case 'Escape':
        toggleDropdown();
        break;
      case 'ArrowDown':
        moveFocusDown();
        break;
      case 'ArrowUp':
        moveFocusUp();
        break;
      case 'Enter':
      case ' ':
        selectCurrentOption();
        break;
      default:
        break;
    }
  }
};

const handleDocumentInteraction = (event) => {
  const isClickInsideButton = elements.button.contains(event.target);
  const isClickInsideDropdown = elements.dropdown.contains(event.target);

  if (isClickInsideButton || (!isClickInsideDropdown && isDropdownOpen)) {
    toggleDropdown();
  }

  // Vérifier si le clic est sur une option
  const clickedOption = event.target.closest('[role="option"]');
  if (clickedOption) {
    selectOptionByElement(clickedOption);
  }
};


const moveFocusDown = () => {
  if (currentOptionIndex < elements.options.length - 1) {
    currentOptionIndex++;
  } else {
    currentOptionIndex = 0;
  }
  focusCurrentOption();
};

const moveFocusUp = () => {
  if (currentOptionIndex > 0) {
    currentOptionIndex--;
  } else {
    currentOptionIndex = elements.options.length - 1;
  }
  focusCurrentOption();
};

const selectCurrentOption = () => {
  const selectedOption = elements.options[currentOptionIndex];
  selectOptionByElement(selectedOption);
};

const selectOptionByElement = (optionElement) => {
  const optionValue = optionElement.textContent;

  elements.button.textContent = optionValue;
  elements.options.forEach(option => {
    option.classList.remove('active');
    option.setAttribute('aria-selected', 'false');
  });

  optionElement.classList.add('active');
  optionElement.setAttribute('aria-selected', 'true');
};

elements.button.addEventListener('keydown', handleKeyPress);
document.addEventListener('click', handleDocumentInteraction);
```

Dans le code mis à jour, nous avons ajouté la navigation au clavier et la sélection des options. Voici le détail :

1. L'objet `elements` inclut maintenant une référence aux éléments d'option avec le rôle "option".
2. La liste déroulante peut également être ouverte avec des touches comme `ArrowDown`, `ArrowUp`, `Space` ou `Enter`
3. Lorsque la liste déroulante est ouverte, `Escape` la ferme, `ArrowDown` déplace le focus vers le bas des options, `ArrowUp` le déplace vers le haut, et `Enter` ou `Space` sélectionne l'option actuelle.
4. Cliquer sur une option ou utiliser l'entrée du clavier sélectionne l'option.
5. L'option sélectionnée est affichée dans le bouton, et l'état aria-selected de l'option est mis à jour.
6. La classe `active` est maintenant ajoutée à l'option sélectionnée

### Corriger le problème de visibilité des options

Cela semble bon jusqu'à présent – mais si vous suivez et testez ce code, vous remarquerez un problème : si une option est hors de vue et que la flèche vers le bas est pressée, l'option n'est pas affichée. 

Pour corriger cela, vous pouvez utiliser la méthode `scrollIntoView` pour vous assurer que l'option actuelle est défilée en vue lorsqu'elle est focalisée. Ajoutez-la à `focusCurrentOption` comme ceci :

```js
const focusCurrentOption = () => {
  const currentOption = elements.options[currentOptionIndex];

  currentOption.classList.add('current');
  currentOption.focus();

  // Faire défiler l'option actuelle en vue
  currentOption.scrollIntoView({
    block: 'nearest',
  });

  elements.options.forEach((option, index) => {
    if (option !== currentOption) {
      option.classList.remove('current');
    }
  });
};

// reste du code
```

De plus, lorsque l'utilisateur sélectionne une option, la liste déroulante doit se fermer, de la même manière que l'élément select fonctionne. Appelez la fonction `toggleDropdown` dans la fonction `selectOptionByElement` comme ceci :

```js
const selectOptionByElement = (optionElement) => {
  const optionValue = optionElement.textContent;

  elements.button.textContent = optionValue;
  elements.options.forEach(option => {
    option.classList.remove('active');
    option.setAttribute('aria-selected', 'false');
  });

  optionElement.classList.add('active');
  optionElement.setAttribute('aria-selected', 'true');

  toggleDropdown(); // fermer la liste déroulante une fois qu'une option est sélectionnée
  
};
```

### Mettre en surbrillance les options lors de la pression sur une touche alphanumérique

Appuyer sur des touches alphanumériques doit mettre en surbrillance l'option qui commence par le caractère saisi. Et si le même caractère est pressé à nouveau, alors l'option suivante doit être mise en surbrillance, et ainsi de suite.

```js
let lastTypedChar = '';
let lastMatchingIndex = 0;

// mettre à jour la fonction handleKeyPress

const handleKeyPress = (event) => {
  event.preventDefault();
  const { key } = event;
  const openKeys = ['ArrowDown', 'ArrowUp', 'Enter', ' '];

  if (!isDropdownOpen && openKeys.includes(key)) {
    toggleDropdown();
    
  } else if (isDropdownOpen) {
    switch (key) {
      case 'Escape':
        toggleDropdown();
        break;
      case 'ArrowDown':
        moveFocusDown();
        break;
      case 'ArrowUp':
        moveFocusUp();
        break;
      case 'Enter':
      case ' ':
        selectCurrentOption();
        break;
      default:
        // Gérer les pressions de touches alphanumériques pour la mini-recherche
        handleAlphanumericKeyPress(key);
        break;
    }
  }
};


// code précédent

const handleAlphanumericKeyPress = (key) => {
  const typedChar = key.toLowerCase();
  
  if (lastTypedChar !== typedChar) {
    lastMatchingIndex = 0;
  }

  const matchingOptions = Array.from(elements.options).filter((option) =>
    option.textContent.toLowerCase().startsWith(typedChar)
  );

  if (matchingOptions.length) {
    if (lastMatchingIndex === matchingOptions.length) {
      lastMatchingIndex = 0;
    }
    let value = matchingOptions[lastMatchingIndex]
    const index = Array.from(elements.options).indexOf(value);
    currentOptionIndex = index;
    focusCurrentOption();
    lastMatchingIndex += 1;
  }
  lastTypedChar = typedChar;
};

// reste du code
```

L'exécution du code et son test avec les entrées de la souris et du clavier doivent donner le comportement attendu. 

### Améliorer la fonctionnalité du lecteur d'écran

La dernière fonctionnalité que j'aborderai dans cet article est la fonctionnalité du lecteur d'écran.

Pour les utilisateurs de lecteurs d'écran, la sélection d'une option doit annoncer l'option sélectionnée, comme le fait l'élément de sélection HTML par défaut. Mettez à jour le HTML pour avoir une div qui contiendra le contenu à annoncer, comme ceci :

```html
<form>
  <label for="select">Boîte de sélection personnalisée</label>
  <button
     role="combobox"
     id="select"
     value="Select"
     aria-controls="listbox"
     aria-haspopup="listbox"
     tabindex="0"
     aria-expanded="false">
    Select</button>
  <div id="announcement" aria-live="assertive" role="alert" style="opacity:0;"></div> <!-- Le lecteur d'écran annoncer le contenu dans cet élément  -->
  <ul role="listbox" id="listbox">
   <li role="option">Option 1</li>
   <li role="option">Option 2</li>
   <li role="option">Option 3</li>
  </ul>
</form>
```

Ensuite, utilisez JavaScript pour mettre à jour la valeur dans l'alerte :

```js
// code précédent
const selectOptionByElement = (optionElement) => {
  const optionValue = optionElement.textContent;

  elements.button.textContent = optionValue;
  elements.options.forEach(option => {
    option.classList.remove('active');
    option.setAttribute('aria-selected', 'false');
  });

  optionElement.classList.add('active');
  optionElement.setAttribute('aria-selected', 'true');

  toggleDropdown();
  announceOption(optionValue); // Annoncer l'option sélectionnée
};

const announceOption = (text) => {
  elements.announcement.textContent = text;
  elements.announcement.setAttribute('aria-live', 'assertive');
  setTimeout(() => {
    elements.announcement.textContent = '';
    elements.announcement.setAttribute('aria-live', 'off');
  }, 1000); // Annoncer et effacer après 1 seconde (ajuster si nécessaire)
};

// reste du code
```

Dans le code ci-dessus, j'ai ajouté une fonction `announceOption`. La fonction est appelée chaque fois qu'un utilisateur sélectionne une option. L'utilisation de la valeur _assertive_ dans l'attribut `aria-live` signale au lecteur d'écran d'interrompre son annonce actuelle et d'annoncer immédiatement la valeur mise à jour.

Maintenant, lorsque vous testez cela avec un lecteur d'écran, le lecteur d'écran annonce l'option sélectionnée comme prévu.

Voici un exemple fonctionnel de la sélection personnalisée sur [Codepen](https://codepen.io/leezee/pen/abXPjvM) :

%[https://codepen.io/leezee/pen/abXPjvM]

## Conclusion

Il y a de la place pour améliorer ces fonctionnalités, comme l'ajout de plusieurs options de sélection, l'autocomplétion et l'amélioration de l'apparence générale. Pourtant, mon intention est que cet article soit un guide utile, vous encourageant à garder l'accessibilité à l'esprit lors de la création d'un composant.

Si vous cherchez un package à utiliser, vous devriez envisager d'utiliser [React-Select](https://react-select.com/home) ou [Vue3-select](https://www.npmjs.com/package/vue3-select).

Merci beaucoup d'avoir lu cet article, si vous l'avez trouvé utile, envisagez de le partager. Bon codage !

Vous pouvez me contacter sur [Linkedin](https://www.linkedin.com/in/elizabeth-meshioye/) ou [Github](https://github.com/Lezette)

### Ressources utilisées dans cet article :

* [Rôles de la combobox MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/combobox_role)
* [Pratiques ARIA W3](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/#accessiblenameguidancebyrole)
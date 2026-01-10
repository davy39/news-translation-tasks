---
title: Virtual DOM vs Shadow DOM – Quelles sont les différences ?
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-03-18T08:22:16.000Z'
originalURL: https://freecodecamp.org/news/virtual-dom-vs-shadow-dom
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--13-.png
tags:
- name: Document Object Model
  slug: document-object-model
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Virtual DOM vs Shadow DOM – Quelles sont les différences ?
seo_desc: 'In web development, understanding the inner workings of the Document Object
  Model (DOM) is crucial. Two concepts that often come up in discussions about DOM
  are Virtual DOM and Shadow DOM.

  While they sound similar, they serve different purposes and h...'
---

Dans le développement web, comprendre le fonctionnement interne du Document Object Model (DOM) est crucial. Deux concepts qui reviennent souvent dans les discussions sur le DOM sont le Virtual DOM et le Shadow DOM.

Bien qu'ils semblent similaires, ils servent des objectifs différents et ont des caractéristiques distinctes.

Dans ce guide complet, nous allons explorer les complexités du Virtual DOM et du Shadow DOM, en mettant en évidence leurs différences avec des explications simples et des extraits de code illustratifs.

### Table des matières

1. **[Introduction au DOM](#heading-introduction-au-dom)**
2. **[Qu'est-ce que le Virtual DOM ?](#heading-quest-ce-que-le-virtual-dom)**
 – [Comment fonctionne le Virtual DOM](#heading-comment-fonctionne-le-virtual-dom)
3. **[Qu'est-ce que le Shadow DOM ?](#quest-ce-que-le-shadow-dom)**
 – [Comprendre le Shadow DOM](#comprendre-le-shadow-dom)
4. **[Différences entre le Virtual DOM et le Shadow DOM](#differences-entre-le-virtual-dom-et-le-shadow-dom)**
5. **[Conclusion](#heading-conclusion)**

## Introduction au DOM

Avant de plonger dans le Virtual DOM et le Shadow DOM, discutons brièvement de ce qu'est le Document Object Model (DOM).

Le DOM représente la structure d'un document HTML sous forme d'une structure arborescente, où chaque nœud représente un élément, un attribut ou un texte dans le document. JavaScript peut manipuler le DOM dynamiquement, permettant aux développeurs de créer des pages web interactives.

## Qu'est-ce que le Virtual DOM ?

Le Virtual DOM est un concept utilisé par des bibliothèques comme React pour améliorer les performances des applications web. Il s'agit essentiellement d'une copie légère du DOM réel, maintenue par le framework.

Lorsque des modifications sont apportées à l'état de l'application, React crée une nouvelle représentation du Virtual DOM et la compare avec la précédente pour identifier les différences (connues sous le nom de "diffing"). Seules les modifications nécessaires sont ensuite appliquées au DOM réel, ce qui entraîne des mises à jour efficaces.

### Comment fonctionne le Virtual DOM

Considérons un exemple simple pour comprendre comment fonctionne le Virtual DOM dans React :

```jsx
// Premier rendu
const element = <div>Bonjour, le monde !</div>;
ReactDOM.render(element, document.getElementById('root'));

// Mise à jour
const updatedElement = <div>Bonjour, le monde ! Mis à jour.</div>;
ReactDOM.render(updatedElement, document.getElementById('root'));
```

Dans cet exemple, React crée une représentation du Virtual DOM de l'`element`. Lorsqu'une mise à jour se produit, il crée une nouvelle représentation du Virtual DOM de l'`updatedElement`.

React compare ensuite les deux représentations du Virtual DOM pour identifier la différence (dans ce cas, le changement de contenu texte). Enfin, React met à jour le DOM réel avec les modifications nécessaires, ce qui entraîne un processus de mise à jour efficace.

## Qu'est-ce que le Shadow DOM ?

Le Shadow DOM est un terme utilisé pour décrire une vue limitée ou restreinte de l'arborescence DOM. Contrairement au Virtual DOM, qui est un concept utilisé pour optimiser les performances, le Shadow DOM fait référence à une structure spécifique au sein de l'arborescence DOM elle-même.

### Comprendre le Shadow DOM

Considérons un scénario où vous avez un composant web personnalisé encapsulé avec le Shadow DOM :

```html
<!DOCTYPE html>
<html>
<head>
  <title>Exemple de Shadow DOM</title>
</head>
<body>
  <my-custom-element></my-custom-element>
  <script>
    class MyCustomElement extends HTMLElement {
      constructor() {
        super();
        const shadow = this.attachShadow({ mode: 'open' });
        const span = document.createElement('span');
        span.textContent = 'Bonjour, Shadow DOM !';
        shadow.appendChild(span);
      }
    }
    customElements.define('my-custom-element', MyCustomElement);
  </script>
</body>
</html>
```

Dans cet exemple, nous définissons un élément personnalisé `my-custom-element` qui encapsule son contenu dans le Shadow DOM en utilisant la méthode `attachShadow`. Le contenu à l'intérieur de la racine de l'ombre est isolé du reste du document, créant une frontière connue sous le nom de Shadow DOM.

## Différences entre le Virtual DOM et le Shadow DOM

Maintenant que vous avez une compréhension de base du Virtual DOM et du Shadow DOM, comparons-les selon différents aspects :

### Objectif

* **Virtual DOM** : Principalement destiné à améliorer les performances en minimisant le nombre de manipulations du DOM nécessaires lors des mises à jour.
* **Shadow DOM** : Se concentre sur l'encapsulation du style et du comportement des composants web, offrant un environnement scopé pour le CSS et JavaScript.

### Implémentation

* **Virtual DOM** : Implémenté par des bibliothèques/frameworks comme React, Vue.js et Angular pour faciliter les mises à jour efficaces du DOM réel.
* **Shadow DOM** : Implémenté nativement par les navigateurs web pour soutenir l'encapsulation des composants web avec le Shadow DOM.

### Performance

* **Virtual DOM** : Offre des avantages de performance en réduisant le nombre de manipulations du DOM, ce qui entraîne des mises à jour et un rendu plus rapides.
* **Shadow DOM** : Bien que le Shadow DOM lui-même n'impacte pas directement les performances, il peut les améliorer en isolant les styles et le comportement des composants.

### Isolation

* **Virtual DOM** : Ne fournit pas d'isolation par lui-même, mais aide à minimiser les effets secondaires non intentionnels des mises à jour du DOM grâce à son algorithme de diffing efficace.
* **Shadow DOM** : Fournit une encapsulation et une isolation pour le contenu des composants web, empêchant les fuites de style et de comportement vers le reste du document.

### Utilisation

* **Virtual DOM** : Communément utilisé dans les frameworks JavaScript modernes comme React, où les composants sont re-rendus efficacement en fonction des changements d'état.
* **Shadow DOM** : Utilisé lors de la création de composants web personnalisés avec des styles et un comportement encapsulés, assurant la modularité et la réutilisabilité.

## Conclusion

En conclusion, le Virtual DOM et le Shadow DOM jouent tous deux des rôles significatifs dans le développement web, bien que dans des contextes différents. Alors que le Virtual DOM se concentre sur l'optimisation des mises à jour du DOM pour la performance, le Shadow DOM fournit une encapsulation et une isolation pour les composants web, améliorant la modularité et la maintenabilité.

Comprendre les différences entre ces concepts est crucial pour construire des applications web efficaces et évolutives.

En tirant parti du Virtual DOM dans des frameworks comme React et en adoptant le Shadow DOM pour encapsuler les composants web, les développeurs peuvent créer des applications web robustes et maintenables qui offrent des performances et une évolutivité optimales.

Alors que les technologies web continuent d'évoluer, avoir une solide compréhension de ces concepts restera inestimable dans le développement web.
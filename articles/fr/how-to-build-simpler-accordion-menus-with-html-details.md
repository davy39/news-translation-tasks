---
title: Comment créer des menus accordéon plus simples avec HTML <details>
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2025-07-21T13:48:33.195Z'
originalURL: https://freecodecamp.org/news/how-to-build-simpler-accordion-menus-with-html-details
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1753119637759/0fb5302d-c21c-4c0d-affb-3f891261aabf.png
tags:
- name: HTML5
  slug: html5
- name: CSS3
  slug: css3
seo_title: Comment créer des menus accordéon plus simples avec HTML <details>
seo_desc: 'Accordion menus are everywhere on the web because users want fast answers
  and smooth navigation.

  They help create clean, organized, and user-friendly interfaces. Many developers
  still reach for JavaScript to build accordions, which adds avoidable com...'
---

Les menus accordéon sont partout sur le web car les utilisateurs veulent des réponses rapides et une navigation fluide.

Ils aident à créer des interfaces propres, organisées et conviviales. De nombreux développeurs utilisent encore JavaScript pour construire des accordéons, ce qui ajoute des complexités évitables à leurs projets.

L'élément HTML `<details>` résout ce problème avec son widget de divulgation intégré qui bascule la visibilité du contenu en utilisant seulement quelques lignes de HTML et de CSS optionnel.

Dans cet article, nous examinerons un accordéon FAQ construit en utilisant `<details>`. Vous pouvez voir le projet final [ici](#heading-notre-projet-exemple).

## Table des matières

* [Qu'est-ce que l'élément HTML `<details>` ?](#heading-quest-ce-que-lelement-html-details)
    
* [Un accordéon FAQ construit avec l'élément `<details>`](#heading-un-accordeon-faq-construit-avec-lelement-details)
    
* [Prise en charge des navigateurs et considérations d'accessibilité](#heading-prise-en-charge-des-navigateurs-et-considerations-daccessibilite)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que l'élément HTML `<details>` ?

L'élément HTML `<details>` est un widget de divulgation qui vous permet de masquer et d'afficher du contenu avec un seul clic. Pensez-y comme un accordéon natif intégré à HTML.

Le cas d'utilisation le plus courant pour les accordéons est la section des questions fréquemment posées (FAQ) sur de nombreux sites. Si vous avez vu ou interagi avec une FAQ, c'est une opportunité d'utiliser `<details>`.

Il comporte deux composants principaux :

* `<details>` est la balise conteneur principale qui s'ouvre et se ferme pour afficher ce qui se trouve dans `<summary>`.
    
* `<summary>` est un conteneur pour le contenu qui est affiché lorsque `<details>` est cliqué.
    

💡 En plus du `summary`, vous pouvez inclure n'importe quel élément de texte HTML dans le conteneur `<details>`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1752662432707/0d6ebbae-d68d-400f-9209-a83feec273b7.png align="center")

L'image ci-dessus montre un cas d'utilisation réel de `<details>` sur le site web d'Apple. Dans une section ultérieure, nous apprendrons quels sont les navigateurs qui le prennent en charge.

### Quand utiliser `<details>` plutôt que des alternatives JavaScript

Contrairement aux accordéons basés sur JavaScript qui alourdissent votre projet, `<details>` offre la même fonctionnalité avec une charge minimale et de meilleures performances. Il offre également une navigation au clavier intégrée et une prise en charge des lecteurs d'écran.

Choisissez `<details>` plutôt que des accordéons créés avec JavaScript lorsque :

* Vous construisez des accordéons simples ou des sections FAQ
    
* L'accessibilité, les performances et le SEO sont une priorité
    
* Vous souhaitez éviter les dépendances JavaScript
    

## Un accordéon FAQ construit avec l'élément `<details>`

Voici à quoi ressemble notre projet d'exemple :

![Projet d'exemple utilisant l'élément details](https://cdn.hashnode.com/res/hashnode/image/upload/v1752662715342/74db7ba5-f7a6-44be-974c-36c0418c4a81.png align="center")

Ce design est de [Frontend Mentor](https://www.frontendmentor.io/?via=ophyboamah) (et vous pouvez consulter le projet sur [Codepen](https://codepen.io/ophyboamah/full/ByaRqaN)).

Pour suivre, vous avez besoin de connaissances de base en HTML et CSS. Puisque l'accent de cet article est sur `<details>`, nous ne mettrons pas l'accent sur le code HTML et CSS de départ (disponible sur le Codepen ci-dessus). Au lieu de cela, nous examinerons une question FAQ avec sa réponse pour apprendre comment `<details>` fonctionne.

### Comment utiliser `<details>`

Pour créer un accordéon avec l'élément `<details>`, vous avez besoin des éléments `<details>` et `<summary>`, comme montré dans le code de démarrage ci-dessous.

```html
<details>
  <summary>Qu'est-ce que Frontend Mentor et comment cela peut-il m'aider ?</summary>
  <p>Frontend Mentor propose des défis de codage réalistes pour aider les développeurs à améliorer leurs compétences en codage frontend avec des projets en HTML, CSS et JavaScript. Il est adapté à tous les niveaux et idéal pour la construction de portefeuilles.</p>
</details>
```

Le GIF ci-dessous sera le résultat après l'exécution du code ci-dessus. Avec moins de cinq lignes de code HTML, nous avons déjà un accordéon.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1752662956079/25c66453-71ba-469c-8dd2-0f1b8e3b9d7f.gif align="center")

### Styliser `<details>`

Maintenant, concentrons-nous sur la transformation de notre accordéon de base en quelque chose de visuellement attrayant (les styles de base peuvent être trouvés sur [Codepen](https://codepen.io/ophyboamah/full/ByaRqaN)). Tout d'abord, nous ajouterons les icônes en tant que SVGs dans `<summary>` avec des classes (closed-icon et open-icon) pour les rendre faciles à styliser.

```html
<details>
  <summary>Qu'est-ce que Frontend Mentor et comment cela peut-il m'aider ?
  <svg class="closed-icon" xmlns="<http://www.w3.org/2000/svg>" class="closed-icon" width="30" height="31" viewBox="0 0 30 31" fill="none">
  <path d="M15 3.3125C12.5895 3.3125 10.2332 4.02728 8.22899 5.36646C6.22477 6.70564 4.66267 8.60907 3.74022 10.836C2.81778 13.063 2.57643 15.5135 3.04668 17.8777C3.51694 20.2418 4.67769 22.4134 6.38214 24.1179C8.08659 25.8223 10.2582 26.9831 12.6223 27.4533C14.9865 27.9236 17.437 27.6822 19.664 26.7598C21.8909 25.8373 23.7944 24.2752 25.1335 22.271C26.4727 20.2668 27.1875 17.9105 27.1875 15.5C27.1835 12.2689 25.8981 9.17131 23.6134 6.88659C21.3287 4.60186 18.2311 3.31653 15 3.3125ZM19.6875 16.4375H15.9375V20.1875C15.9375 20.4361 15.8387 20.6746 15.6629 20.8504C15.4871 21.0262 15.2486 21.125 15 21.125C14.7514 21.125 14.5129 21.0262 14.3371 20.8504C14.1613 20.6746 14.0625 20.4361 14.0625 20.1875V16.4375H10.3125C10.0639 16.4375 9.82541 16.3387 9.64959 16.1629C9.47378 15.9871 9.375 15.7486 9.375 15.5C9.375 15.2514 9.47378 15.0129 9.64959 14.8371C9.82541 14.6613 10.0639 14.5625 10.3125 14.5625H14.0625V10.8125C14.0625 10.5639 14.1613 10.3254 14.3371 10.1496C14.5129 9.97377 14.7514 9.875 15 9.875C15.2486 9.875 15.4871 9.97377 15.6629 10.1496C15.8387 10.3254 15.9375 10.5639 15.9375 10.8125V14.5625H19.6875C19.9361 14.5625 20.1746 14.6613 20.3504 14.8371C20.5262 15.0129 20.625 15.2514 20.625 15.5C20.625 15.7486 20.5262 15.9871 20.3504 16.1629C20.1746 16.3387 19.9361 16.4375 19.6875 16.4375Z" fill="#AD28EB"/>
  </svg> 
  <svg class="open-icon" xmlns="<http://www.w3.org/2000/svg>" class="open-icon" width="30" height="31" viewBox="0 0 30 31" fill="none">
  <path d="M15 3.3125C12.5895 3.3125 10.2332 4.02728 8.22899 5.36646C6.22477 6.70564 4.66267 8.60907 3.74022 10.836C2.81778 13.063 2.57643 15.5135 3.04668 17.8777C3.51694 20.2418 4.67769 22.4134 6.38214 24.1179C8.08659 25.8223 10.2582 26.9831 12.6223 27.4533C14.9865 27.9236 17.437 27.6822 19.664 26.7598C21.8909 25.8373 23.7944 24.2752 25.1335 22.271C26.4727 20.2668 27.1875 17.9105 27.1875 15.5C27.1841 12.2687 25.899 9.17076 23.6141 6.8859C21.3292 4.60104 18.2313 3.31591 15 3.3125ZM19.6875 16.4375H10.3125C10.0639 16.4375 9.82541 16.3387 9.64959 16.1629C9.47378 15.9871 9.37501 15.7486 9.37501 15.5C9.37501 15.2514 9.47378 15.0129 9.64959 14.8371C9.82541 14.6613 10.0639 14.5625 10.3125 14.5625H19.6875C19.9361 14.5625 20.1746 14.6613 20.3504 14.8371C20.5262 15.0129 20.625 15.2514 20.625 15.5C20.625 15.7486 20.5262 15.9871 20.3504 16.1629C20.1746 16.3387 19.9361 16.4375 19.6875 16.4375Z" fill="#301534"/>
  </svg>
  </summary>
  <p>Frontend Mentor propose des défis de codage réalistes pour aider les développeurs à améliorer leurs compétences en codage frontend avec des projets en HTML, CSS et JavaScript. Il est adapté à tous les niveaux et idéal pour la construction de portefeuilles.</p>
</details>
```

Dans le code ci-dessous, nous personnalisons le marqueur de divulgation en masquant la flèche par défaut et en ajoutant une icône personnalisée à droite en utilisant le pseudo-élément `::marker` sur `<summary>`. Nous définissons également son contenu comme vide, ce qui supprime le marqueur complètement.

```css
/* Styles pour l'élément summary cliquable*/
summary {
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: color 0.2s ease;
  margin-bottom: 1em;
  padding: 1.5em;
/* Supprimer le marqueur par défaut */
  &::marker {
    content: '';
  }
  
  &:last-child { 
    margin-bottom: 0; 
  } 
  
  &:hover { 
    color: var(--text-accent);
    outline: none;
  }
}

p {
  padding-top: 1em;
  color: var(--text-light);
}
/* Styles pour le conteneur <details> pliable */
details {
  margin-bottom: 1em;
  
  &:last-child { 
    margin-bottom: 0; 
  }
  
  .open-icon {
    display: none;
  }

  &[open] {
    .open-icon {
      display: inline;
    }
    
    .closed-icon {
      display: none;
    }
  }
  
  .open-icon,
  .closed-icon {
    width: 1.8em; 
    height: 1.8em;
    flex-shrink: 0;
  }
}
```

Le GIF ci-dessous montre le résultat du style de notre accordéon avec le code CSS ci-dessus.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1752663406898/3d033ac2-e9d4-4836-8f3b-816513802353.gif align="center")

Pour avoir une question FAQ développée lorsque la page se charge, ajoutez l'attribut `open` à `<details>`. Cela est particulièrement utile pour mettre en évidence des informations importantes où la FAQ la plus cruciale commence développée.

```html
<details open>
    <summary>Qu'est-ce que Frontend Mentor et comment cela peut-il m'aider ?</summary>
</details>
```

## Prise en charge des navigateurs et considérations d'accessibilité

Selon [MDN](https://developer.mozilla.org/fr/docs/Web/HTML/Element/details), `<details>` est une fonctionnalité bien établie qui fonctionne sur de nombreux appareils et les navigateurs populaires (Chrome, Edge, Firefox et Safari) depuis janvier 2020.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1752663542331/33407311-a4db-47ab-bc9f-16baaed5d060.png align="center")

`<details>` inclut des fonctionnalités d'accessibilité intégrées qui nécessitent du JavaScript supplémentaire dans les solutions personnalisées telles que la navigation au clavier, la prise en charge des lecteurs d'écran et la structure sémantique. Vous pouvez également ajouter des attributs comme role, aria-expanded et aria-labelledby pour garantir encore plus d'accessibilité.

## Conclusion

`<details>` est un élément puissant mais sous-utilisé pour créer des éléments d'interface utilisateur comme des accordéons, des FAQ ou des menus de navigation sans JavaScript. Il est facile à implémenter et léger, et améliore l'expérience utilisateur avec du contenu interactif.

Alors, la prochaine fois que vous devrez créer du contenu pliable, en gardant à l'esprit l'accessibilité et les performances, envisagez d'utiliser `<details>` et cela rendra certainement votre vie de développeur plus facile.

Voici quelques ressources utiles :

* [Documentation MDN pour `<details>`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/details)
    
* [Guide CSS-Tricks pour styliser Details](https://css-tricks.com/quick-reminder-that-details-summary-is-the-easiest-way-ever-to-make-an-accordion/)
    
* [Web.dev Apprendre HTML : Details](https://web.dev/learn/html/details/)
---
title: Comment créer une table des matières interactive et dynamique en JavaScript
subtitle: ''
author: Bhavesh Rawat
co_authors: []
series: null
date: '2023-11-14T15:22:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-dynamic-table-of-contents-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Frame-32-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment créer une table des matières interactive et dynamique en JavaScript
seo_desc: 'While reading some technical articles on various platforms, I kept noticing
  the Table of Contents section in the sidebar. Some were interactive and some were
  just links to those sections.

  A Table of Contents usually ends up being pretty helpful to re...'
---

Lors de la lecture de certains articles techniques sur diverses plateformes, je n'ai pas pu m'empêcher de remarquer la section Table des matières dans la barre latérale. Certaines étaient interactives et d'autres étaient simplement des liens vers ces sections.

Une Table des matières se révèle généralement très utile pour les lecteurs. Elle permet de parcourir facilement ce qu'un article couvrira et de trouver la section qui vous intéresse. Elle vous permet également de savoir si l'article contient les informations que vous recherchez, et c'est un grand avantage pour l'accessibilité.

En m'inspirant de toutes ces diverses plateformes, j'ai essayé de construire ma propre fonctionnalité de Table des matières. Je voulais qu'elle liste dynamiquement tous les titres H2 ainsi que leurs liens de signet. Je voulais également que les titres soient mis en évidence lorsqu'ils sont défilés dans la vue. Je suis excité, commençons.

Note : Je n'ai pas pu utiliser Codepen, car il utilise des iframes pour prévisualiser les résultats - et pour l'instant, [Intersection Observer agit de manière assez capricieuse dans iFrame](https://github.com/w3c/IntersectionObserver/issues/372). Voici le [gist](https://gist.github.com/bhaveshxrawat/7c3b869c74797adfbb10655af2b4cfe2) pour ce code.

%[https://gist.github.com/bhaveshxrawat/7c3b869c74797adfbb10655af2b4cfe2]

## Prérequis

Pour tirer le meilleur parti de ce tutoriel, vous devez être familiarisé avec :

1. HTML5/CSS3/JavaScript

2. Intersection Observer API

Très bien, plongeons maintenant dans le vif du sujet.

## Installation du Projet

Tout d'abord, mettons en place la structure HTML pour notre Table des matières. Ce ne sera rien de sophistiqué - juste une balise `<article>` enveloppant tout le contenu, avec une balise `<aside>` comme frère, le tout étant enveloppé par la balise `<main>`.

Voici à quoi cela ressemblera :

```html
<main>
    <article>
        <h1>Titre Principal</h1>
        <h2>Premier Titre</h2>
        <p>Lorem ipsum dolor sit...</p>
        <h2>Deuxième Titre</h2>
        <p>Lorem ipsum dolor sit...</p>
        <h2>Troisième Titre</h2>
        <p>Lorem ipsum dolor sit...</p>
    </article>
    <aside></aside>
</main>
```

La balise `<aside>` est vide car elle sera remplie en fonction du contenu de la balise `<article>` en utilisant JavaScript.

Nous avons terminé avec la partie structure. Faisons un peu de style, ce qui nous aidera à distinguer entre les liens inactifs et actifs.

## Comment Ajouter le Style

J'ai importé une police Google appelée DM Sans pour ce mini-projet. Dans mon CSS, j'utilise le nesting natif.

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&display=swap');

html {
    scroll-padding: 3.125rem;
    font-family: 'DM Sans', sans-serif;
}
main {
    display: grid;
    gap: 2rem;
    grid-template-columns: 3fr 1fr;
}
aside {
    align-self: start;
    position: sticky;
    top: 0.625rem;
    ul {
      li {
        a {
          transform-origin: left;
          transition: transform 0.1s linear;
          &.active {
            font-weight: 600;
            transform: scale(1.1);
          }
        }
      }
    }
}
@media (max-width: 767px) {
    main {
      grid-template-columns: 1fr;
    }
    aside {
      display: none;
    }
}
```

J'ai utilisé `display: grid;` pour mettre en place une disposition où le contenu occupe les trois quarts de l'espace du conteneur (dans ce cas, la fenêtre d'affichage), et la Table des matières occupe le quart restant de l'espace.

Je garde la balise `<aside>` collante afin qu'elle reste dans la vue pendant que le contenu est défilé. Nous devons expérimenter l'interactivité et le comportement de la 'Table des matières, n'est-ce pas ?

## Comment Construire la Logique

Maintenant, voici la partie amusante - et définitivement la partie la plus importante. Commençons par ce que nous pouvons réaliser facilement et construisons à partir de cela.

### Construire la fonctionnalité de table des matières dynamique

Tout d'abord, nous devons stocker tous les éléments `H2` dans une variable, et c'est ce que nous ferons dans la première ligne. Ensuite, nous sélectionnerons les éléments `aside`, car nous devons les remplir avec quelque chose. Puis, nous créerons un nouvel élément `ul` et le stockerons dans la variable `ul`. Après cela, nous ajouterons le nouvel élément `ul` créé comme enfant de l'élément `aside`.

Voici à quoi cela ressemble :

```js
const headings = Array.from(document.getElementsByTagName("h2"));
const aside = document.querySelector("aside");
const ul = document.createElement("ul");
aside.appendChild(ul);
headings.map((heading) => {
    const id = heading.innerText.toLowerCase().replaceAll(" ", "_");
    heading.setAttribute("id", id);
    const anchorElement = `<a href="#${id}">${heading.textContent}</a>`;
    const keyPointer = `<li>${anchorElement}</li>`;
    ul.insertAdjacentHTML("beforeend", keyPointer);
});
```

Maintenant, nous utilisons la fonction `map` pour itérer et effectuer une fonction pour chaque élément `H2`. Tout d'abord, nous créons un `id` pour chaque élément `h2` en convertissant le contenu textuel en minuscules et en remplaçant les espaces par des traits de soulignement. Cet `id` est utilisé pour lier à la section correspondante.

Ensuite, utilisons l'id que nous venons de créer, et définissons-le comme valeur de l'attribut 'id'. Puis nous créons un élément d'ancrage (`<a>`) avec un attribut `href` pointant vers l'`id` généré. Le texte de l'ancrage est défini sur le contenu textuel de l'élément `h2`.

Maintenant, nous pouvons créer un élément de liste (`<li>`) contenant l'élément d'ancrage précédemment créé et ensuite cet élément de liste est ajouté en tant que HTML à la fin de la liste non ordonnée (`ul`).

### Rendre la ToC interactive

Très bien, nous sommes à mi-chemin ! Actuellement, nous avons une Table des matières dynamique qui liste automatiquement tous les éléments `h2` avec leurs liens de signet.

Maintenant, il nous reste la partie interactive. Nous voulons que notre lien soit mis en évidence lorsque la section correspondante est dans la vue de la page.

Ainsi, maintenant que l'élément `aside` est rempli et contient des balises d'ancrage, nous allons stocker toutes ces ancres et les nommer `tocAnchors`.

```js
const tocAnchors = aside.querySelectorAll("a");
```

Ensuite, nous allons déclarer une fonction fléchée nommée `obFunc` qui sera utilisée plus tard dans Intersection Observer. Intersection Observer est essentiellement une API fournie par le navigateur. Elle nous permet d'observer les changements dans l'intersection des éléments que nous voulons avec la fenêtre d'affichage du document ou l'élément racine de votre choix.

```js
const obFunc = (entries) => {}
```

Maintenant, nous avons défini une fonction `obFunc` qui prend un tableau d'`entries` comme paramètre. La fonction sera exécutée chaque fois que les éléments observés (spécifiés plus tard) intersectent avec la fenêtre d'affichage.

Dans la boucle `forEach` pour `entries`, nous vérifions si un élément observé intersecte avec la fenêtre d'affichage. Si la condition est satisfaite, alors nous trouvons l'index de l'élément intersectant (représenté par `entry.target`) dans le tableau `headings`.

```js
entries.forEach((entry) => {
        if (entry.isIntersecting) {
        	const index = headings.indexOf(entry.target);
        }
}
```

En utilisant une nouvelle boucle `forEach`, nous itérons à travers tous les éléments d'ancrage (`tocAnchors`) et supprimons la classe "active" de chacun d'eux afin que la classe `active` ne persiste pas sur plus d'un élément à la fois.

```js
tocAnchors.forEach((tab) => {
    tab.classList.remove("active");
});
```

Et maintenant, nous ajoutons la classe `active` à l'élément d'ancrage qui intersecte à ce moment-là. En plus de cela, nous utilisons la méthode `scrollIntoView` qui fait défiler la page pour amener l'élément d'ancrage actif dans la vue. L'option `{ block: "nearest" }` garantit qu'il fait défiler jusqu'à la position la plus proche à la fois verticalement et horizontalement.

```js
tocAnchors[index].classList.add("active");
    tocAnchors[index].scrollIntoView({
        block: "nearest"
});
```

Maintenant, nous définissons un objet, `obOption` qui servira de configuration pour Intersection Observer. `rootMargin` spécifie les marges autour de la racine (dans ce cas, la fenêtre d'affichage), et `threshold` définit le seuil auquel la fonction de rappel est déclenchée.

```js
const obOption = {
    rootMargin: "-30px 0% -77%",
    threshold: 1
};
```

L'option `rootMargin` est très importante ici. Vous définissez essentiellement une pseudo-fenêtre d'affichage en créant un décalage par rapport à la fenêtre d'affichage originale. Cela devient la zone de surveillance (en quelque sorte).

Cette option prend des valeurs de la même manière que la marge - sauf que lorsque nous utilisons des valeurs négatives ici, elle en tient compte en se déplaçant vers le centre de l'écran. Vous pouvez certainement utiliser les mêmes valeurs que les miennes et obtenir une zone idéale, ou vous pouvez jouer avec les valeurs jusqu'à obtenir le comportement idéal.

Enfin, tout ce que nous avons à faire est de créer une nouvelle instance Intersection Observer avec la fonction précédemment définie (`obFunc`) comme rappel et les options (`obOption`). Ensuite, nous utiliserons la boucle `forEach` pour itérer sur tous les éléments `H2` et les mettre sous observation en utilisant la méthode `.observe()`.

```js
const observer = new IntersectionObserver(obFunc, obOption);
headings.forEach((hTwo) => observer.observe(hTwo));
```

Lorsque l'un de ces éléments intersecte avec la fenêtre d'affichage, la fonction de rappel `obFunc` sera exécutée.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screen-Recording-2023-11-13-at-3.22.45-PM--online-video-cutter.com-.gif align="left")

*Démonstration du projet montrant la ToC à droite pendant que nous faisons défiler le texte*

## Conclusion

Maintenant, vous avez une Table des matières entièrement interactive et dynamique. J'espère que ce tutoriel vous a été utile. Faites-moi savoir si vous pouvez construire sur cette base ou améliorer davantage ce projet. Santé !
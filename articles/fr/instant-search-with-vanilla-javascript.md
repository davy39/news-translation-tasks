---
title: Recherche Instantanée avec Vanilla JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-25T02:14:28.000Z'
originalURL: https://freecodecamp.org/news/instant-search-with-vanilla-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Week--15_-Instant-Search.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: instant search
  slug: instant-search
- name: JavaScript
  slug: javascript
- name: search
  slug: search
- name: WeeklyCodingChallenge
  slug: weeklycodingchallenge
seo_title: Recherche Instantanée avec Vanilla JavaScript
seo_desc: 'By Florin Pop

  Originally posted on www.florin-pop.com

  The theme for week #15 of the Weekly Coding Challenge is:

  Instant Search

  We live in a fast world and we want everything to be FAST, including search results,
  this is why instant search functionali...'
---

Par Florin Pop

_Originalement publié sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/06/vanilla-javascript-instant-search/)_

Le **thème** pour la semaine #15 du [Weekly Coding Challenge](https://florin-pop.com/blog/2019/03/weekly-coding-challenge/) est :

## Recherche Instantanée

Nous vivons dans un monde rapide et nous voulons que tout soit RAPIDE, y compris les résultats de recherche, c'est pourquoi la fonctionnalité de recherche instantanée est devenue une fonctionnalité "indispensable" plutôt qu'une fonctionnalité "agréable à avoir".

Dans cet article, nous allons construire cette [fonctionnalité](https://codepen.io/FlorinPop17/full/qzNxGa/), mais en utilisant uniquement Vanilla JavaScript :smiley:.

Ci-dessous se trouve l'aperçu en direct de ce que nous allons construire dans cet article. Recherchons parmi les pays du monde pour voir leur population et leur drapeau :

%[https://codepen.io/FlorinPop17/pen/qzNxGa/]

**Note** : vous pouvez utiliser React, Vue, Angular ou tout autre framework/bibliothèque pour créer cette fonctionnalité, bien que la réaliser en Vanilla JavaScript soit beaucoup plus amusant. ?

## Le HTML

Nous aurons besoin de 2 éléments dans notre HTML :

1. Un champ de `recherche`
2. Une div `results` où nous afficherons les résultats de la recherche

```html
<input type="text" id="search" placeholder="Rechercher un pays" />
<div id="results"></div>
```

Habituellement, nous passons à la partie stylisation ensuite, mais dans ce cas, considérant que nous n'avons pas encore tout le balisage (vous verrez dans un instant), nous allons d'abord passer à la partie JS. ?

## Le JavaScript

Faisons un plan avant d'écrire du code. Les choses que nous devons faire sont :

1. Rassembler une liste de tous les pays du monde
2. Afficher la liste des pays
3. Mettre à jour les résultats en fonction de la requête de recherche

Plutôt génial, hein ? ?

### Étape un - obtenir les données

J'ai trouvé une belle API que nous pouvons utiliser pour obtenir la liste des pays dont nous avons besoin. Il s'agit de : [RestCountries.eu](https://restcountries.eu/).

Nous allons utiliser l'API [Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) intégrée afin de récupérer tous les pays, et nous allons les stocker dans une variable : `countries`.

```js
let countries;

const fetchCountries = async () => {
    countries = await fetch(
        'https://restcountries.eu/rest/v2/all?fields=name;population;flag'
    ).then(res => res.json());
};
```

Comme vous pouvez le voir, nous avons créé une fonction asynchrone ; Vous pouvez en lire plus à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

Notez également que nous ne voulons que 3 champs de l'API (nom, population et drapeau), donc c'est ce que nous allons obtenir de l'API en définissant le paramètre de requête `fields`.

### Étape deux - afficher les données

Maintenant, nous devons créer la structure de notre liste afin d'afficher les données et pour cela, nous allons créer tous les éléments dont nous avons besoin (`ul`, `li`, titres, etc.) à l'intérieur d'une fonction et nous les insérerons dans la div `results` que nous avons déclarée dans notre HTML.

Nous allons également appeler notre fonction `fetchCountries` ici car nous voulons parcourir les pays afin de créer les éléments correspondants :

```js
const results = document.getElementById('results');

const showCountries = async () => {
    // obtenir les données
    await fetchCountries();

    const ul = document.createElement('ul');
    ul.classList.add('countries');

    countries.forEach(country => {
        // créer la structure
        const li = document.createElement('li');
        li.classList.add('country-item');

        const country_flag = document.createElement('img');
        // Définir la source de l'image
        country_flag.src = country.flag;
        country_flag.classList.add('country-flag');

        const country_name = document.createElement('h3');
        country_name.innerText = country.name;
        country_name.classList.add('country-name');

        const country_info = document.createElement('div');
        country_info.classList.add('country-info');

        const country_population = document.createElement('h2');
        country_population.innerText = numberWithCommas(country.population);
        country_population.classList.add('country-population');

        const country_popupation_text = document.createElement('h5');
        country_popupation_text.innerText = 'Population';
        country_popupation_text.classList.add('country-population-text');

        country_info.appendChild(country_population);
        country_info.appendChild(country_popupation_text);

        li.appendChild(country_flag);
        li.appendChild(country_name);
        li.appendChild(country_info);

        ul.appendChild(li);
    });

    results.appendChild(ul);
};

// afficher les pays initiaux
showCountries();

// De StackOverflow https://stackoverflow.com/questions/2901102/how-to-print-a-number-with-commas-as-thousands-separators-in-javascript
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}
```

Il y a un "petit" peu de code ci-dessus, alors décomposons-le. ?

Tout d'abord, nous avons notre liste (`ul`) avec les `li` qui sont créés dans la boucle `forEach`.

Tous les `li` ont trois enfants :

1. Le drapeau - `img`
2. Le nom du pays en titre - `h3`
3. Une `div` qui contient : (a) le nombre de `population` - `h2` - et (b) Le texte `'Population'` - `h5`

Nous les avons organisés de cette manière car il sera plus facile dans le CSS d'aligner tout en utilisant **flexbox**. 

Parallèlement à cela, nous avons ajouté une `classe` pour chaque élément car nous voulons les styliser individuellement dans le CSS et ensuite nous avons utilisé `appendChild` pour ajouter ces éléments au DOM à la fin de la fonction `forEach`.

Et enfin, nous avons une fonction `numberWithComma` de StackOverflow qui ajoutera une virgule comme séparateur de milliers pour le nombre de `population`.

### Étape 3 - mettre à jour la vue en fonction de la requête de recherche

Dans cette étape finale, nous allons obtenir la requête de recherche à partir de l'`input` en attachant un `eventListener` dessus, et nous allons modifier notre fonction `showCountries` afin qu'elle `filtre` les valeurs que nous ne voulons pas afficher. Voyons comment nous pouvons faire cela :

```js
const search_input = document.getElementById('search');

let search_term = '';

search_input.addEventListener('input', e => {
    // sauvegarder la valeur de l'input
    search_term = e.target.value;

    // réafficher les pays en fonction du nouveau search_term
    showCountries();
});

const showCountries = async () => {
    // effacer les résultats
    results.innerHTML = '';

    // voir le code ci-dessus à l'étape 2.

    countries
        .filter(country =>
            country.name.toLowerCase().includes(search_term.toLowerCase())
        )
        .forEach(country => {
            // voir le code ci-dessus à l'étape 2.
        });

    // voir le code ci-dessus à l'étape 2.
};
```

Comme vous pouvez le voir, nous avons ajouté deux nouvelles choses dans la fonction `showCountries` :

1. Nous effaçons les `results` précédents en définissant le `innerHTML` sur une chaîne vide
2. Nous filtrons les `countries` en vérifiant si le `search_term` saisi est `inclus` dans le `name` du pays, et nous convertissons également ces deux valeurs en `toLowerCase` car l'utilisateur pourrait taper des lettres en majuscules et nous voulons toujours afficher le pays correspondant

## Le code JS complet

Ci-dessous vous pouvez trouver le code JS complet au cas où vous souhaiteriez le copier :

```js
const search_input = document.getElementById('search');
const results = document.getElementById('results');

let search_term = '';
let countries;

const fetchCountries = async () => {
    countries = await fetch(
        'https://restcountries.eu/rest/v2/all?fields=name;population;flag'
    ).then(res => res.json());
};

const showCountries = async () => {
    results.innerHTML = '';

    await fetchCountries();

    const ul = document.createElement('ul');
    ul.classList.add('countries');

    countries
        .filter(country =>
            country.name.toLowerCase().includes(search_term.toLowerCase())
        )
        .forEach(country => {
            const li = document.createElement('li');
            li.classList.add('country-item');

            const country_flag = document.createElement('img');
            country_flag.src = country.flag;
            country_flag.classList.add('country-flag');

            const country_name = document.createElement('h3');
            country_name.innerText = country.name;
            country_name.classList.add('country-name');

            const country_info = document.createElement('div');
            country_info.classList.add('country-info');

            const country_population = document.createElement('h2');
            country_population.innerText = numberWithCommas(country.population);
            country_population.classList.add('country-population');

            const country_popupation_text = document.createElement('h5');
            country_popupation_text.innerText = 'Population';
            country_popupation_text.classList.add('country-population-text');

            country_info.appendChild(country_population);
            country_info.appendChild(country_popupation_text);

            li.appendChild(country_flag);
            li.appendChild(country_name);
            li.appendChild(country_info);

            ul.appendChild(li);
        });

    results.appendChild(ul);
};

showCountries();

search_input.addEventListener('input', e => {
    search_term = e.target.value;
    showCountries();
});

// De StackOverflow https://stackoverflow.com/questions/2901102/how-to-print-a-number-with-commas-as-thousands-separators-in-javascript
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}
```

## Le CSS

Enfin, ajoutons un peu de style à notre petite application :

```css
@import url('https://fonts.googleapis.com/css?family=Roboto:300,500&display=swap');

* {
    box-sizing: border-box;
}

body {
    background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    font-family: 'Roboto', sans-serif;

    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;

    min-height: 100vh;
}

.countries {
    padding: 0;
    list-style-type: none;
    width: 480px;
}

.country-item {
    background-color: #fff;
    border-radius: 3px;
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 10px;
    margin: 10px 0;
}

.country-item:hover {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
}

.country-flag {
    width: 40px;
}

.country-name {
    flex: 2;
    font-weight: normal;
    letter-spacing: 0.5px;
    margin: 0 5px;
    text-align: center;
}

.country-info {
    border-left: 1px solid #aaa;
    color: #777;
    padding: 0 15px;
    flex: 1;
}

.country-population {
    font-weight: 300;
    line-height: 24px;
    margin: 0;
    margin-bottom: 12px;
}

.country-population-text {
    font-weight: 300;
    letter-spacing: 1px;
    margin: 0;
    text-transform: uppercase;
}

input {
    font-family: 'Roboto', sans-serif;
    border-radius: 3px;
    border: 1px solid #ddd;
    padding: 15px;
    width: 480px;
}
```

Comme ce n'est rien de fantastique, je ne vais pas entrer dans les détails du CSS, mais si vous avez des questions à ce sujet, n'hésitez pas à me contacter et je serai heureux de répondre à vos questions ! ?

## Conclusion

Comme mentionné ci-dessus, cette petite application pourrait probablement être réalisée beaucoup plus simplement avec React, Vue ou Angular, et vous êtes libre de le faire si vous le souhaitez pour votre soumission, mais je voulais m'amuser avec Vanilla JS et ce fut une expérience amusante pour moi ! ?

Comme toujours, assurez-vous de partager ce que vous allez créer !

Bon codage ! ?
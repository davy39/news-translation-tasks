---
title: Comment ajouter une fonctionnalité de recherche à une application Frontend
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-04T16:28:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-search-to-frontend-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pexels-ketut-subiyanto-4126712.jpg
tags:
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: search
  slug: search
seo_title: Comment ajouter une fonctionnalité de recherche à une application Frontend
seo_desc: "By Njoku Samson Ebere\nAs a software developer, part of your job is to\
  \ deliver the best user experience possible to those using your site or product.\
  \ \nAnd building a helpful and efficient search function is one way you can do this.\
  \ So if you are looki..."
---

Par Njoku Samson Ebere

En tant que développeur logiciel, une partie de votre travail consiste à offrir la meilleure expérience utilisateur possible à ceux qui utilisent votre site ou produit. 

Et construire une fonction de recherche utile et efficace est l'une des façons d'y parvenir. Donc, si vous cherchez la bonne façon de construire une fonctionnalité de recherche sur le front end de votre site, vous êtes au bon endroit. 

Il y a quelque temps, je pensais que la fonctionnalité de recherche devait être construite dans le back end et appelée depuis le front end. 

Mais en continuant à construire des applications, j'ai appris que parfois, vous devrez peut-être simplement rechercher parmi les données récupérées depuis un endpoint public où il n'y a pas d'endpoint _search_. D'autres fois, la recherche frontend peut être nécessaire pour améliorer la vitesse d'un site web et l'expérience utilisateur en général.

Ce tutoriel passera d'abord par la "mauvaise façon" de configurer la recherche que beaucoup d'entre nous ont adoptée. Ensuite, nous apprendrons une bien meilleure façon de le faire. Alors, restez avec moi et laissez-moi vous emmener dans ce voyage.

### Prérequis 

Il sera facile de suivre ce tutoriel si vous avez des connaissances de base en :

* [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [React](https://reactjs.org/)

## Projet de démarrage

J'ai préparé une petite application pour vous donner un bon départ si vous voulez coder avec moi. Clonez simplement [ce dépôt](https://github.com/EBEREGIT/search-tutorial/tree/starter-code). La branche qui nous intéresse est la branche **starter-code**. 

Suivez les instructions dans le fichier [ReadMe](https://github.com/EBEREGIT/search-tutorial/blob/starter-code/README.md) pour configurer le projet et vous devriez avoir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-29-at-20.17.12.png)
_Ecran du projet de démarrage_

Dans le projet que vous avez maintenant, nous récupérons les mises à jour du COVID-19 pour chaque pays dans le fichier ``src/context/hatchways.js`` grâce à [coronatracker](https://api.coronatracker.com/). 

Dans notre fichier ``src/App.js``, nous affichons les résultats que nous avons obtenus. Une boîte d'entrée de *recherche* est située au-dessus de la liste des résultats. Pour chacun de ces résultats, le fichier ``src/components/Country.js`` est rendu.

Lorsque l'utilisateur tape dans la boîte d'entrée, la fonction ``filterCountryByName`` est appelée pour rechercher parmi les pays que nous avons collectés précédemment. Cette fonction est construite dans le fichier ``src/Helpers/HatchHelper.js``.

Tous les styles sont dans le fichier ``src/styles/App.scss``.

Vous devriez maintenant pouvoir naviguer dans le projet et vous y retrouver. Commençons par la façon dont vous ne devriez pas construire votre fonctionnalité de recherche.


## Comment NE PAS construire une fonctionnalité de recherche

Nous allons nous concentrer sur le fichier `src/Helpers/HatchHelper.js` pour construire la fonction de recherche.

Nous avons déjà le code suivant :

```javascript
// rechercher des pays par nom
const filterCountryByName = (name, countries, setResults) => {
  // effacer le résultat de la recherche si le champ de recherche est vide
  if (name === "") {
    setResults([]);
  }

  // interrompre si aucune recherche n'a encore été effectuée
  if (name === null || name === "" || countries === []) return;
};
```

Ensuite, nous devons vider le tableau de recherche précédent afin de ne pas ajouter le nouveau résultat de recherche à celui-ci. Cela est juste au cas où nous aurions déjà effectué une recherche et souhaiterions en effectuer une autre.

```javascript
    // vider le tableau de recherche précédent s'il y en a un
    const searchResult = [];
```

Convertir la _chaîne de recherche_ en minuscules pour des raisons de cohérence. Cela rendra la recherche insensible à la casse.

```javascript
const data = name.toLowerCase();
```

Maintenant, parcourez les **pays** comme suit :

```javascript
  // parcourir tous les pays
  for (const country of countries) {

  }
```

Ensuite, collectez chaque nom de pays et mettez-le en minuscules pour vous assurer que la recherche sera insensible à la casse comme suit :

```javascript
    const countryName = country.countryName.toLowerCase();
```

En dessous, vérifiez si la chaîne de recherche correspond à un caractère dans le nom du pays (`[...countryName].includes(data)`), un mot dans le nom du pays (`countryName.split(" ").includes(data)`) ou le nom complet du pays (`countryName === data`) et collectez les détails du pays comme suit :

```javascript
    // vérifier si le mot ou le caractère de recherche correspond
    if (
      [...countryName].includes(data) ||
      countryName === data ||
      countryName.split(" ").includes(data)
    ) {
      searchResult.push(country);
    }
```

Lorsque la boucle est terminée, mettez à jour le résultat de la recherche avec la ligne de code suivante :

```javascript
setResults(searchResult);
```

La fonction `filterCountryByName` ressemble maintenant à ceci :

```javascript
// rechercher des pays par nom
const filterCountryByName = (name, countries, setResults) => {
  // effacer le résultat de la recherche si le champ de recherche est vide
  if (name === "") {
    setResults([]);
  }

  // interrompre si aucune recherche n'a encore été effectuée
  if (name === null || name === "" || countries === []) return;

  // vider le tableau de recherche précédent s'il y en a un
  const searchResult = [];
  const data = name.toLowerCase();

  // parcourir tous les pays
  for (const country of countries) {
    const countryName = country.countryName.toLowerCase();

    // vérifier si le mot ou le caractère de recherche correspond
    if (
      [...countryName].includes(data) ||
      countryName === data ||
      countryName.split(" ").includes(data)
    ) {
      searchResult.push(country);
    }
  }

  setResults(searchResult);
};
```

Remplacez l'élément **main** dans le fichier `src/App.js` par le code suivant pour assurer un retour d'information approprié pendant la recherche :

```html
<main>
    {filterByNameResults && filterByNameResults.length
    ? filterByNameResults.map((country) => (
    <Country country={country} />
    ))
    : filterByName && !filterByNameResults.length
    ? "Aucun résultat trouvé !"
    : hatchLoading === "processing"
    ? "Récupération des données..."
    : hatchLoading === "found" && hatches && hatches.length
    ? hatches.map((country) => <Country country={country} />)
    : "Aucun pays trouvé ! Vérifiez votre connexion Internet !"}
</main>
```

### Comment tester votre fonction de recherche

Faisons maintenant une recherche et voyons ce que nous obtenons :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ezgif.com-gif-maker.gif)
_Test de la façon de faire une recherche Frontend de la mauvaise manière_

Voici le code pour [la mauvaise façon de coder une fonction de recherche](https://github.com/EBEREGIT/search-tutorial/tree/wrong-way).

### Quel est le problème avec la méthode de recherche ci-dessus ?

Vous remarquerez que la chaîne de recherche doit satisfaire au moins l'une des 3 conditions que nous avons spécifiées pour qu'un résultat soit retourné. 

Alors, qu'en est-il d'un utilisateur qui n'est pas sûr de l'orthographe mais connaît quelques caractères contenus dans le nom du pays ? 

Remarquez-vous que l'utilisateur mettra plus de temps à rechercher certains mots car les mots doivent être tapés complètement pour obtenir une correspondance ?

**Réfléchissez à ceci** : ITA- devrait pouvoir retourner ITALY, NIG- devrait pouvoir retourner NIGER et NIGERIA, et ainsi de suite.

Ainsi, bien que notre recherche fonctionne, ces problèmes la rendent difficile à utiliser et impactent négativement l'expérience utilisateur. Cela nous amène maintenant à la bonne façon de faire cette fonctionnalité de recherche.

## Comment construire une fonction de recherche de la bonne manière

Nous devons créer une autre recherche juste en dessous de celle actuelle. 

Commencez par définir 2 états initiaux pour contenir la **chaîne de recherche** et les **résultats de recherche** pour cette nouvelle recherche comme suit :

```javascript
  const [searchString, setSearchString] = useState("");
  const [searchResult, setSearchResult] = useState([]);
```

Ensuite, faites une autre boîte d'entrée juste en dessous de la première comme suit :

```javascript
          {/* rechercher par nom de la bonne manière */}
          <input
            name="searchString"
            value={searchString}
            placeholder="Rechercher par nom (Bonne manière)"
            onChange={(e) => setSearchString(e.target.value)}
            onKeyUp={(e) =>
              searchCountryByName(
                e.target.value,
                hatches,
                setSearchResult
              )
            }
          />
```

Allez dans le fichier `src/Helpers/HatchHelper.js` et créez la fonction **`searchCountryByName`** en dessous de la fonction **`filterCountryByName`** :

```javascript
// rechercher des pays par nom de la bonne manière
const searchCountryByName = (
  searchString,
  countries,
  setSearchResult
) => {

};
```

Incluez-la dans l'export comme ceci :

```javascript
export { filterCountryByName, searchCountryByName };
```

Vous pouvez maintenant l'importer dans le fichier `src/App.js` comme suit :

```javascript
import { filterCountryByName, searchCountryByName } from "./Helpers/HatchHelper";
```

Vous devriez maintenant avoir une deuxième boîte d'entrée qui ne fait encore rien :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-30-at-07.38.27.png)
_Ecran montrant une deuxième boîte d'entrée qui ne fait encore rien_

#### Développer la fonction 

Nous allons maintenant construire la fonction pour qu'elle fonctionne comme nous le souhaitons. 

Commencez par ajouter les lignes de code suivantes :

```javascript
    // effacer le résultat de la recherche si le champ de recherche est vide
    if (searchString === "") {
      setSearchResult([]);
    }
  
    // interrompre si aucune recherche n'a encore été effectuée
    if (searchString === null || searchString === "" || countries === []) return;
```

Ensuite, videz le tableau de recherche précédent s'il y en a un comme ceci :

```javascript
// vider le tableau de recherche précédent s'il y en a un
  setSearchResult([]);
```

Créez ensuite une variable qui contiendra nos résultats de recherche pendant la recherche :

```javascript
let results = [];
```

Créez un motif d'expression régulière pour la chaîne de recherche comme suit :

```javascript
  // créer un motif d'expression régulière pour la chaîne de recherche
  const pattern = new RegExp(searchString, "gi");
```

> Dans le code ci-dessus, nous disons que nous voulons utiliser cette **searchString** pour quelque chose. En l'utilisant, nous voulons qu'elle soit insensible à la casse et nous voulons tous les résultats possibles. Vous pouvez en apprendre plus sur [les expressions régulières ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp).

Maintenant, parcourez les pays et collectez chaque nom de pays comme suit :

```javascript
  // parcourir tous les pays
  for (const country of countries) {
    const countryName = country.countryName;
 
  }
```

Toujours dans la boucle, testez si le motif d'expression régulière correspond au **`countryName`** que nous venons de collecter. Si c'est **vrai**, alors ajoutez les détails du pays au tableau **results** comme suit :

```javascript
// vérifier si le mot ou le caractère de recherche correspond
if (pattern.test(countryName)) {
    results.push(country);
}
```

Terminez en mettant à jour le résultat de la recherche en utilisant le code suivant :

```javascript
setSearchResult(results)
```

La fonction `searchCountryByName` ressemble maintenant à ceci :

```javascript
// rechercher des pays par nom de la bonne manière
const searchCountryByName = (
  searchString,
  countries,
  setSearchResult
) => {
  // effacer le résultat de la recherche si le champ de recherche est vide
  if (searchString === "") {
    setSearchResult([]);
  }

  // interrompre si aucune recherche n'a encore été effectuée
  if (searchString === null || searchString === "" || countries === []) return;

  // vider le tableau de recherche précédent s'il y en a un
  setSearchResult([]);
  let results = [];

  // créer un motif d'expression régulière pour la chaîne de recherche
  const pattern = new RegExp(searchString, "gi");

  // parcourir tous les pays
  for (const country of countries) {
    const countryName = country.countryName;

    // vérifier si le mot ou le caractère de recherche correspond
    if (pattern.test(countryName)) {
      results.push(country);
    }
  }

  setSearchResult(results)
};
```

Retournez dans le fichier `src/App.js` et remplacez l'élément main par le code suivant :

```html
        <main>
          {filterByNameResults && filterByNameResults.length
            ? filterByNameResults.map((country) => (
                <Country country={country} />
              ))
            : filterByName && !filterByNameResults.length
            ? "Aucun résultat trouvé !"
            : searchResult && searchResult.length
            ? searchResult.map((country) => <Country country={country} />)
            : searchString && !searchResult.length
            ? "Aucun résultat trouvé !"
            : hatchLoading === "processing"
            ? "Récupération des données..."
            : hatchLoading === "found" && hatches && hatches.length
            ? hatches.map((country) => <Country country={country} />)
            : "Aucun pays trouvé ! Vérifiez votre connexion Internet !"}
        </main>
```

Maintenant, les résultats pour la deuxième boîte de recherche sont inclus ci-dessus.

### Tester votre fonction de recherche (de la bonne manière)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ezgif.com-gif-maker--1-.gif)
_Test de la façon de faire une recherche Frontend de la bonne manière_

Walah ! Vous venez d'apprendre la bonne façon de créer une recherche sur le front end. 😊

Voici le code pour [la bonne façon de construire une fonction de recherche](https://github.com/EBEREGIT/search-tutorial/tree/right-way).

## Comment optimiser votre fonctionnalité de recherche

Nous avons en fait terminé. Donc vous pouvez sauter cette partie si vous êtes occupé, mais cela ne prendra qu'un moment si vous voulez améliorer votre fonction de recherche.

Vous remarquerez que lorsque vous effectuez une recherche de la mauvaise manière et que vous ne rafraîchissez pas la page, vous resterez bloqué avec les résultats de la mauvaise manière. Il serait préférable d'obtenir des résultats frais lorsque la deuxième boîte de recherche est utilisée pour la bonne manière. 

Pour y parvenir, nous devrons effacer tous les résultats de recherche pour chaque recherche effectuée – qu'il s'agisse de la **mauvaise** ou de la **bonne** manière. Faisons ce qui suit :

Dans le fichier `src/App.js`, remplacez l'événement _onkey_ de la première boîte de recherche par ce qui suit :

```javascript
            onKeyUp={(e) =>
              filterCountryByName(
                e.target.value,
                hatches,
                setFilterByNameResults,
                setSearchString,
                setSearchResult
              )
            }
```

Remplacez l'événement _onkey_ de la deuxième boîte de recherche par ce qui suit :

```javascript
            onKeyUp={(e) =>
              searchCountryByName(
                e.target.value,
                hatches,
                setSearchResult,
                setFilterByName,
                setFilterByNameResults
              )
            }
```

Dans le fichier `src/Helpers/HatchHelper.js`, ajoutez les 2 paramètres que nous venons de passer dans la fonction **`filterCountryByName`** comme suit :

```javascript
// rechercher des pays par nom
const filterCountryByName = (
  name,
  countries,
  setResults,
  setSearchString,
  setSearchResult
) => {...}
```

Ensuite, juste avant de vider les résultats de recherche initiaux, videz l'autre champ de recherche et les résultats comme suit :

```javascript
  // vider l'autre champ de recherche et les résultats s'il y en a
  setSearchString("");
  setSearchResult([]);
```

Faites de même pour la fonction **`searchCountryByName`**.

#### Lorsque vous avez terminé, vous devriez obtenir le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ezgif.com-gif-maker--2--1.gif)
_Notre application après avoir optimisé la fonctionnalité_

Super ! 👍🏾👍🏾👍🏾

Voici le [code d'optimisation](https://github.com/EBEREGIT/search-tutorial/tree/optimization).

## Conclusion 

Ce fut un voyage passionnant avec vous alors que nous avons vu les erreurs que beaucoup d'entre nous ont commises et comment les corriger en créant une fonction de recherche qui offre la meilleure expérience à l'utilisateur.

Je crois que le code peut être encore amélioré. Je vous encourage donc à regarder à nouveau le code et à voir comment vous pouvez le rendre encore meilleur.

Tout le code est [ici](https://github.com/EBEREGIT/search-tutorial). Merci d'avoir lu !
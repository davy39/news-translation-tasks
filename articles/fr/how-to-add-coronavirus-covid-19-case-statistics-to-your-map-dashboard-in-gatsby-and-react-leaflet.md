---
title: Comment ajouter des statistiques de cas de Coronavirus (COVID-19) à votre tableau
  de bord cartographique React avec Gatsby
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-04-22T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-coronavirus-covid-19-case-statistics-to-your-map-dashboard-in-gatsby-and-react-leaflet
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-mapping-app-2600x1000.jpg
tags:
- name: coronavirus
  slug: coronavirus
- name: Covid-19
  slug: covid-19
- name: data analytics
  slug: data-analytics
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: leaflet
  slug: leaflet
- name: Mapping
  slug: mapping
- name: maps
  slug: maps
- name: React
  slug: react
- name: react-leaflet
  slug: react-leaflet
- name: React
  slug: reactjs
seo_title: Comment ajouter des statistiques de cas de Coronavirus (COVID-19) à votre
  tableau de bord cartographique React avec Gatsby
seo_desc: 'Previously, we walked through creating a map that shows an interactive
  look at Coronavirus (COVID-19) cases per country. How can we extend this with some
  case statistics to show recent data about the impacts on our world?

  Author''s note: Similar to be...'
---

Précédemment, nous avons parcouru la création d'une carte qui montre un aperçu interactif des cas de Coronavirus (COVID-19) par pays. Comment pouvons-nous étendre cela avec quelques statistiques de cas pour montrer les données récentes sur les impacts dans notre monde ?

_Note de l'auteur : Comme auparavant, ce tableau de bord est destiné à être une démonstration et une preuve de concept pour l'utilisation de données du monde réel afin de construire un tableau de bord. Bien que ces données devraient être exactes selon l'API NovelCOVID, je recommande d'utiliser des outils comme le [tableau de bord de l'Université Johns Hopkins](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) pour une analyse complète et exacte. Restez chez vous et soyez en sécurité ! ❤️_

* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Que devons-nous avoir avant de commencer ?](#heading-que-devons-nous-avoir-avant-de-commencer)
* [Étape 1 : Mettre à jour la façon dont nous récupérons nos données et récupérer les statistiques](#heading-etape-1-mettre-a-jour-la-facon-dont-nous-recuperons-nos-donnees-et-recuperer-les-statistiques)
* [Étape 2 : Ajout de statistiques à notre tableau de bord](#heading-etape-2-ajout-de-statistiques-a-notre-tableau-de-bord)
* [Étape 3 : Rendre les données plus conviviales](#heading-etape-3-rendre-les-donnees-plus-conviviales)
* [Étape 4 : Ajouter la date de la dernière mise à jour](#heading-etape-4-ajouter-la-date-de-la-derniere-mise-a-jour)
* [Que puis-je faire ensuite ?](#heading-que-puis-je-faire-ensuite)

%[https://www.youtube.com/watch?v=9bfxeod27fU]

## Que allons-nous construire ?

Nous allons étendre notre [démo de carte originale](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet) avec quelques statistiques de base que nous pouvons récupérer depuis l'[API NovelCOVID](https://github.com/NovelCOVID/API). Pour avoir une idée, voici [ma démo](https://coronavirus-map-dashboard.netlify.app/) sur laquelle je base cela.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-covid-19-dashboard-map-stats.jpg)
_Démo de carte Coronavirus (COVID-19) avec statistiques de tableau de bord_

Bien que vous ne soyez pas obligé d'avoir terminé [la Partie 1](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet/) pour appliquer ces concepts, cela aide définitivement et cela vous permet de configurer une carte pour votre tableau de bord. Si vous souhaitez commencer par là, ce que je recommande, consultez [Comment créer une application de tableau de bord et de carte Coronavirus (COVID-19) avec Gatsby et Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet/) d'abord.

## Woah, une application de cartographie ?

Oui. Si vous n'avez jamais joué avec des cartes auparavant, ne vous découragez pas ! Ce n'est pas aussi compliqué que vous le pensez probablement. Si vous préférez commencer par les bases de la cartographie, vous pouvez [en savoir plus sur le fonctionnement de la cartographie](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/) d'abord.

## Que devons-nous avoir avant de commencer ?

Pour ce tutoriel, vous avez besoin d'une application React sous une forme ou une autre. Je vais travailler avec le tableau de bord que nous avons précédemment construit dans mon dernier tutoriel qui inclut une [carte des cas de Coronavirus (COVID-19) par pays](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet/).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-map-tutorial-country-markers.jpg)
_Tableau de bord cartographique Coronavirus (COVID-19)_

Je recommande de commencer par le tutoriel précédent, mais si vous voulez sauter la carte et commencer frais, le moyen le plus facile serait probablement d'utiliser [Create React App](https://github.com/facebook/create-react-app), [Gatsby](https://www.gatsbyjs.org/), ou [Next.js](https://nextjs.org/).

## Étape 1 : Mettre à jour la façon dont nous récupérons nos données et récupérer les statistiques

Pour commencer avec notre tableau de bord de statistiques, nous allons faire un peu de travail préparatoire en changeant la façon dont nous récupérons les données. L'objectif ici est d'encapsuler notre logique de requête de manière réutilisable afin que nous puissions l'utiliser à la fois pour nos données de pays et nos nouvelles données de statistiques.

### Créer un nouveau hook React pour récupérer les données

Pour commencer, la première chose que nous allons faire est de créer un nouveau [hook React](https://reactjs.org/docs/hooks-reference.html) qui servira à récupérer les données. Pour commencer, créez un nouveau fichier dans votre répertoire hooks appelé `useTracker.js` et ajoutez une ligne à l'intérieur de `hooks/index.js` pour l'exporter :

```js
// Nouveau fichier src/hooks/useTracker.js
// Ce fichier sera vide pour l'instant
```

```js
// À l'intérieur de hooks/index.js
export { default as useTracker } from './useTracker';

```

À l'intérieur de notre fichier `useTracker.js`, nous allons configurer notre logique de requête. C'est un long fichier, alors assurez-vous de copier et coller l'ensemble avant que nous parcourions ce qu'il fait :

```js
import { useEffect, useState } from 'react';
import axios from 'axios';

const API_HOST = 'https://corona.lmao.ninja/v2';

const ENDPOINTS = [
  {
    id: 'all',
    path: '/all',
    isDefault: true
  },
  {
    id: 'countries',
    path: '/countries'
  }
]

const defaultState = {
  data: null,
  state: 'ready'
}

const useTracker = ({ api = 'all' }) => {

  const [tracker = {}, updateTracker] = useState(defaultState)

  async function fetchTracker() {
    let route = ENDPOINTS.find(({ id } = {}) => id === api);

    if ( !route ) {
      route = ENDPOINTS.find(({ isDefault } = {}) => !!isDefault);
    }

    let response;

    try {
      updateTracker((prev) => {
        return {
          ...prev,
          state: 'loading'
        }
      });
      response = await axios.get(`${API_HOST}${route.path}`);
    } catch(e) {
      updateTracker((prev) => {
        return {
          ...prev,
          state: 'error',
          error: e
        }
      });
      return;
    }

    const { data } = response;

    updateTracker((prev) => {
      return {
        ...prev,
        state: 'ready',
        data
      }
    });

  }

  useEffect(() => {
    fetchTracker()
  }, [api])

  return {
    fetchTracker,
    ...tracker
  }
};

export default useTracker;


```

En commençant par le haut :

* Nous importons nos dépendances : nous allons utiliser les hooks `useEffect` et `useState` de React pour gérer nos requêtes
* Nous définissons des constantes par défaut : nous avons un point de terminaison d'API de base pour nos données, une liste des points de terminaison disponibles que nous utiliserons, et un objet d'état qui stockera nos données
* Nous définissons notre hook `useTracker` : notre hook inclut un argument `api` qui nous permettra de spécifier quel point de terminaison nous utiliserons pour faire notre requête
* Nous configurons une instance d'état : nous voulons garder une trace de nos données récupérées, donc nous créons une instance d'état `tracker` que nous pourrons mettre à jour
* Nous avons créé une fonction asynchrone `fetchTracker` : nous l'utiliserons pour faire notre requête réelle
* À l'intérieur de notre fonction : nous trouvons d'abord la route de l'API et créons notre URL, mettons à jour notre instance d'état à un état "chargement", essayons de faire notre requête, capturons les erreurs s'il y en a, et enfin si la requête est réussie, nous mettons à jour notre état avec ces données
* Nous déclenchons notre fonction : en utilisant un hook `useEffect`, nous déclenchons notre fonction `fetchTracker` pour faire la requête. Nous n'avons qu'une seule dépendance `api`. Cela signifie que la fonction ne se déclenchera que la première fois et chaque fois que la valeur `api` que nous passons change. Nous ne changerons pas cette valeur, mais cela peut être utile dans d'autres instances si vous changez dynamiquement l'API utilisée
* Nous retournons notre tracker : l'objet retourné inclut à la fois nos données `tracker` ainsi que notre fonction `fetchTracker` que nous pourrions utiliser pour récupérer à nouveau les données si nous le souhaitons

Et avec tout cela, nous avons un tout nouveau hook qui récupérera les données de l'API NovelCOVID.

### Utiliser notre nouveau hook tracker

Pour utiliser ce hook, passons à `src/pages/index.js`, supprimons notre import `axios` s'il est là, et importons plutôt notre hook :

```js
import { useTracker } from 'hooks';

```

Avec notre hook, remplaçons notre requête de données de pays originale. Tout d'abord, ajoutons ce qui suit en haut du composant `IndexPage` :

```js
const { data: countries = [] } = useTracker({
  api: 'countries'
});

const hasCountries = Array.isArray(countries) && countries.length > 0;

```

Cela nous permettra de récupérer nos données de pays et de savoir si nous avons des résultats. Ensuite, remplaçons notre requête originale.

À l'intérieur de notre fonction `mapEffect`, supprimons la requête `axios` ainsi que la réponse, l'objet de données déstructuré et la constante `hasData`.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/code-diff-map-effect-countries-data.jpg)
_Diff de code montrant la mise à jour de l'effet de la carte_

Ensuite, remplaçons `hasData` par `hasCountries` :

```js
if ( !hasCountries ) return;

```

Et remplaçons `data` par `countries` dans l'objet `geoJson` où nous mappons nos caractéristiques :

```js
features: countries.map((country = {}) => {

```

À ce stade, si vous enregistrez et actualisez, vous ne devriez remarquer aucune différence par rapport à ce que vous aviez précédemment.

### Ajouter une requête pour nos statistiques

Maintenant que nous utilisons notre hook `useTracker` pour récupérer nos données de pays, utilisons-le également pour récupérer nos statistiques.

Juste à côté de l'endroit où nous avons configuré notre hook `useTracker` précédemment, ajoutons une autre requête :

```js
const { data: stats = {} } = useTracker({
  api: 'all'
});

```

Et si nous ajoutons une instruction `console.log` en dessous pour voir ce qu'il y a dans `stats` :

```js
console.log('stats', stats);

```

Nous devrions voir notre objet de données `stats` journalisé !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/console-log-coronavirus-stats-1.jpg)
_Utilisation de console.log pour afficher les statistiques Coronavirus (COVID-19)_

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commit/fe9d85e57f7474a86d38213676bf62df4b6168a4)

## Étape 2 : Ajout de statistiques à notre tableau de bord

Maintenant que nous avons nos données disponibles à utiliser, utilisons-les !

Pour commencer à ajouter nos statistiques au tableau de bord, créons une structure de données qui nous permettra de configurer facilement les données que nous voulons utiliser.

Pour ce faire, créons d'abord un nouveau tableau appelé `dashboardStats` sous `hasCountries` en haut du composant de page :

```js
const dashboardStats = [];

```

À l'intérieur de ce tableau, ajoutons quelques nouveaux objets qui spécifient nos données que nous extrayons de l'objet `stats` que nous avons demandé. Pour commencer, essayons d'ajouter :

```js
const dashboardStats = [
  {
    primary: {
      label: 'Total des cas',
      value: stats?.cases
    },
    secondary: {
      label: 'Par million',
      value: stats?.casesPerOneMillion
    }
  },
  {
    primary: {
      label: 'Total des décès',
      value: stats?.deaths
    },
    secondary: {
      label: 'Par million',
      value: stats?.deathsPerOneMillion
    }
  },
  {
    primary: {
      label: 'Total des tests',
      value: stats?.tests
    },
    secondary: {
      label: 'Par million',
      value: stats?.testsPerOneMillion
    }
  }
]

```

La raison pour laquelle nous divisons cela en clés `primary` et `secondary`, c'est que nous allons utiliser cela pour différencier les statistiques logiquement similaires que nous voulons styliser un peu différemment.

_Note : si vous n'êtes pas familier avec la syntaxe `?.`, elle s'appelle [Optional Chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining). Cela nous permet d'enchaîner nos propriétés sans nous soucier de l'existence des objets. Si `stats` est indéfini, il retournera simplement indéfini au lieu de lancer une erreur._

Avec nos données de statistiques, ajoutons le tracker à notre carte. Supprimons notre composant `<Map>` actuel et incluons-le imbriqué à l'intérieur de notre div tracker dans ce qui suit :

```jsx
<div className="tracker">
  <Map {...mapSettings} />
  <div className="tracker-stats">
    <ul>
      { dashboardStats.map(({ primary = {}, secondary = {} }, i) => {
        return (
          <li key={`Stat-${i}`} className="tracker-stat">
            { primary.value && (
              <p className="tracker-stat-primary">
                { primary.value }
                <strong>{ primary.label }</strong>
              </p>
            )}
            { secondary.value && (
              <p className="tracker-stat-secondary">
                { secondary.value }
                <strong>{ secondary.label }</strong>
              </p>
            )}
          </li>
        );
      })}
    </ul>
  </div>
</div>

```

Ce code devrait suivre immédiatement le composant `<Helmet>` si vous suivez.

Pour expliquer ce que nous faisons :

* Nous créons une "div" de tracker qui organisera nos statistiques
* Nous déplaçons notre composant `<Map` à l'intérieur de ce tracker
* Nous créons une section séparée appelée "tracker-stats"
* À l'intérieur de celle-ci, nous créons une liste non ordonnée (`ul`)
* À l'intérieur de notre liste, nous parcourons toutes nos statistiques à l'intérieur de `dashboardStats`
* Pour chaque statistique, nous créons un nouvel élément de liste (`li`) et incluons 2 paragraphes optionnels qui incluent nos données de statistiques principales et nos données de statistiques secondaires

Une fois que nous rechargeons notre page, nous devrions maintenant voir quelques statistiques :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/adding-coronavirus-stats-to-page.jpg)
_Ajout des premières statistiques à la page_

Maintenant que nous avons nos statistiques sur notre page, faisons en sorte qu'elles ressemblent à un tableau de bord.

Créons un nouveau fichier appelé `_tracker.scss` à l'intérieur de notre répertoire `src/assets/stylesheets/components`. Une fois ce fichier créé, ajoutons-le également au fichier `src/assets/stylesheets/components/__components.scss` :

```scss
@import "tracker";

```

Avec notre nouveau fichier de style de composant prêt à l'emploi, ajoutons quelques styles dans `_tracker.scss` :

```scss
.tracker-stats {

  color: white;
  background-color: $blue-grey-900;
  border-top: solid 1px darken($blue-grey-900, 5);

  ul {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    list-style: none;
    padding: 0;
    margin: 0;
  }

}

.tracker-stat {

  font-size: 2em;
  text-align: center;
  padding: .5em;
  border-right: solid 1px darken($blue-grey-900, 5);
  border-bottom: solid 1px darken($blue-grey-900, 5);

  strong {
    font-weight: normal;
    color: $blue-grey-300;
  }

}

.tracker-stat-primary {

  margin: 0;

  strong {
    display: block;
    font-size: .5em;
  }

}

.tracker-stat-secondary {

  font-size: .5em;
  margin: .8em 0 0;

  strong {
    font-size: .8em;
    margin-left: .4em;
  }

}

```

Ci-dessus – nous ajoutons des couleurs et des effets d'organisation, tels que l'utilisation de [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout), pour permettre à nos données d'être organisées de manière facile à lire et à avoir une belle apparence ! Nous utilisons également certaines variables de couleurs préexistantes qui sont utilisées dans le projet pour garder l'utilisation des couleurs cohérente.

Une fois que vous avez enregistré ces styles et rechargé la page, cela devrait avoir une meilleure apparence :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/adding-coronavirus-case-statistics-to-map-dashboard.jpg)
_Ajout de statistiques de cas au tableau de bord_

À partir de là, n'hésitez pas à ajouter plus de statistiques ou à les ajuster à votre convenance. Dans la démo que j'ai créée, j'ai ajouté les statistiques pour les cas actifs, les cas critiques et les cas rétablis. Si vous souhaitez faire de même, vous pouvez [consulter le commit](https://github.com/colbyfayock/my-coronavirus-map/commit/eb8a28c9e46dc2327ada0df21b250422e55d304c).

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commit/eb8a28c9e46dc2327ada0df21b250422e55d304c)

## Étape 3 : Rendre les données plus conviviales

Maintenant, le reste de ce tutoriel pourrait être considéré comme optionnel, mais en fin de compte, nous voulons que les gens puissent lire ces statistiques, n'est-ce pas ? Alors rendons les nombres un peu plus faciles à lire.

Tout d'abord, ouvrons notre fichier `src/lib/util.js` et ajoutons cette fonction :

```js
/**
 * commafy
 * @description Applique des virgules appropriées aux grands nombres
 */

export function commafy(value) {
  let numberString = `${value}`;

  numberString = numberString.split('');

  numberString.reverse();

  numberString = numberString.reduce((prev, current, index) => {
    const shouldComma = (index + 1) % 3 === 0 && index + 1 < numberString.length;
    let updatedValue = `${prev}${current}`;
    if ( shouldComma ) {
      updatedValue = `${updatedValue},`;
    }
    return updatedValue;
  }, '');

  numberString = numberString.split('');
  numberString.reverse()
  numberString = numberString.join('');

  return numberString;
}

```

Cette fonction prendra un nombre et le transformera en une chaîne avec des virgules. Pour parcourir ce qu'elle fait :

* Prend une valeur en argument. Pour notre utilisation, cette valeur sera très probablement un nombre.
* Elle convertit la valeur en une chaîne. Nous utiliserons cela pour travailler avec l'ajout de virgules à notre nombre.
* Nous divisons cette chaîne en un tableau et l'inversons. Nous voulons l'inverser car cela facilite l'ajout de nos virgules en fonction de l'index.
* Nous utilisons la fonction `reduce` de javascript pour recréer notre nombre-chaîne. Après chaque groupe de 3 chiffres, nous voulons ajouter une virgule.
* Une fois que nous avons notre nouvelle valeur avec les virgules, nous voulons la réinverser. Nous la divisons à nouveau, inversons le tableau de caractères et les rejoignons, ce que nous retournons

Et maintenant que nous avons notre fonction `commafy`, utilisons-la. De retour à l'intérieur de `src/pages/index.js`, importons notre fonction en haut de la page :

```js
import { commafy } from 'lib/util';

```

Ensuite, dans notre tableau `dashboardStats`, remplaçons chaque valeur numérique par une expression ternaire et une fonction qui convertira notre nombre s'il est disponible :

```js
value: stats ? commafy(stats?.cases) : '-'

```

Cette ligne vérifie si `stats` existe. Si c'est le cas, nous appliquons `commafy` à la valeur `cases`. Si elle n'existe pas, nous retournons un `-` pour montrer qu'elle est indisponible.

Une fois que nous avons répété ce processus pour tous nos nombres, nous pouvons enregistrer, recharger la page et voir nos nombres conviviaux !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-dashboard-stats-with-readable-stats.jpg)
_Formatage des statistiques pour les rendre lisibles par l'homme_

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commit/90f266c17815239d9d3356d9b9d660915fdc26c2)

## Étape 4 : Ajouter la date de la dernière mise à jour

Enfin, nous voulons nous assurer que les gens restent informés et comprennent la dernière fois où ces données ont été mises à jour. Heureusement, notre API fournit une date de dernière mise à jour pour nous, alors utilisons-la !

Au bas de notre "tracker" `div` sous `tracker-stats`, ajoutons ce qui suit :

```jsx
<div className="tracker-last-updated">
  <p>
    Dernière mise à jour : { stats?.updated }
  </p>
</div>

```

Cela crée une nouvelle section où nous incluons simplement la propriété `updated` de nos statistiques. Et si nous enregistrons et rechargeons la page, nous pouvons voir la date de la dernière mise à jour !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronvirus-dashboard-last-updated.jpg)
_Ajout de la dernière mise à jour au tableau de bord_

Mais comment pourrions-nous même comprendre ce que ce nombre est, à moins que vous ne soyez l'ordinateur qui parcourt cet article de blog ? Alors changeons-le en un format lisible par l'homme comme nous l'avons fait avec nos nombres.

À l'intérieur de notre fichier `src/lib/util.js`, ajoutons une autre fonction :

```js
/**
 * friendlyDate
 * @description Prend une valeur de date et retourne une version conviviale
 */

export function friendlyDate(value) {
  const date = new Date(value);
  return new Intl.DateTimeFormat('en', {
    year: 'numeric',
    month: 'short',
    day: '2-digit',
    hour: 'numeric',
    minute: 'numeric'
  }).format(date);
}

```

Cette fonction crée un nouvel objet `Date`, puis utilise l'API javascript [International DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DateTimeFormat) pour le convertir en un format lisible et convivial !

Une fois cela enregistré, importons-le à côté de notre fonction `commafy` en haut de `src/pages/index.js` :

```js
import { commafy, friendlyDate } from 'lib/util';

```

Ensuite, nous pouvons mettre à jour notre code de manière similaire à la façon dont nous avons mis à jour nos nombres :

```jsx
Dernière mise à jour : { stats ? friendlyDate(stats?.updated) : '-' }

```

Et si nous enregistrons et rechargeons, nous le voyons de manière lisible par l'homme !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronvirus-dashboard-last-updated-formatted-1.jpg)
_Formatage de la date de la dernière mise à jour_

Enfin, pour notre "dernière mise à jour", cela devrait ressembler à ce qu'elle s'intègre avec le reste du tableau de bord, alors ajoutons quelques styles supplémentaires. À l'intérieur de notre fichier `_tracker.scss` avec lequel nous travaillons :

```scss
.tracker-last-updated {

  color: white;
  background-color: $blue-grey-900;
  padding: .8em 0;

  p {
    color: $blue-grey-300;
    font-size: .8em;
    text-align: center;
    margin: 0;
  }

}

```

Et une fois que nous avons enregistré et actualisé le navigateur, nous avons nos statistiques de tableau de bord avec l'heure de la dernière mise à jour ! 🎉

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-dashboard-formatted-styled.jpg)
_Tableau de bord final avec la date de la dernière mise à jour formatée_

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commit/408286aecb32223c8782eb1539f5563135c75dfb)

## Que puis-je faire ensuite ?

### Rendre les données de l'infobulle du marqueur conviviales

Maintenant que nous avons nos fonctions pratiques `commafy` et `friendlyDate`, nous pouvons réutiliser ces fonctions pour nettoyer les données dans nos popups de marqueurs de pays !

### Utiliser la fonction fetchTracker pour interroger les mises à jour

À l'intérieur du hook `useTracker` que nous avons créé, nous avons exporté une fonction appelée `fetchTracker`. Cela nous permet de forcer une requête à l'API pour récupérer de nouvelles données. Pour nous assurer que notre carte reste à jour même lorsque quelqu'un ne rafraîchit pas la page, nous pouvons créer un [timer](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout) en javascript pour invoquer régulièrement cette fonction afin de mettre à jour nos données de tableau de bord.

### Effacer les couches de la carte avant de réajouter les nouvelles

Une chose que nous ne faisons pas actuellement est de nettoyer les anciennes couches avant d'en ajouter une nouvelle. La façon dont la carte est configurée, elle continue simplement à les superposer. Ce que nous pouvons faire, c'est avant d'ajouter toutes nos nouvelles couches, nous pouvons effacer les anciennes. [Consultez ce commit](https://github.com/colbyfayock/my-coronavirus-map/commit/cad3b5a6e31a6ae090549c12e40a08fee4db4aa5) pour commencer !

## Vous voulez en savoir plus sur les cartes ?

Vous pouvez consulter quelques-unes de mes autres ressources pour commencer :

* [Comment créer une application de tableau de bord et de carte Coronavirus (COVID-19) en React avec Gatsby et Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet) (Partie 1 de cet article)
* [Comment configurer un style de carte de base Mapbox personnalisé avec React Leaflet et Leaflet Gatsby Starter](https://www.colbyfayock.com/2020/04/how-to-set-up-a-custom-mapbox-basemap-style-with-react-leaflet-and-leaflet-gatsby-starter/)
* [Tout le monde peut cartographier ! Inspiration et une introduction au monde de la cartographie](https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping)
* [Comment créer une application de cartographie de road trip d'été avec Gatsby et Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet)
* [Comment créer votre propre tracker de Santa avec Gatsby et React Leaflet](https://www.colbyfayock.com/2019/12/create-your-own-santa-tracker-with-gatsby-and-react-leaflet/)
* [Comment construire une application de cartographie en React facilement avec Leaflet](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">🐦 Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">🎥️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>
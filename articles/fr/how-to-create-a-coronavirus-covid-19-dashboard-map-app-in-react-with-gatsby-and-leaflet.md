---
title: Comment créer une application de tableau de bord et de carte du Coronavirus
  (COVID-19) en React avec Gatsby et Leaflet
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-03-31T15:16:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-coronavirus-covid-19-dashboard-map-app-in-react-with-gatsby-and-leaflet
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/coronavirus-mapping-app.jpg
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
seo_title: Comment créer une application de tableau de bord et de carte du Coronavirus
  (COVID-19) en React avec Gatsby et Leaflet
seo_desc: 'The Coronavirus (COVID-19) pandemic has swiftly changed how all of us interact
  day to day. How can we use available APIs to build a mapping app that shows the
  impact it has had on the world?

  Update: The original NovelCOVID API v1 endpoint has been de...'
---

La pandémie de Coronavirus (COVID-19) a rapidement changé la façon dont nous interagissons au quotidien. Comment pouvons-nous utiliser les API disponibles pour créer une application de cartographie qui montre l'impact qu'elle a eu sur le monde ?

**Mise à jour :** Le point de terminaison original de l'API NovelCOVID v1 a été obsolète. Veuillez mettre à jour et utiliser plutôt : [https://corona.lmao.ninja/v2/countries](https://corona.lmao.ninja/v2/countries)

_Note de l'auteur : Ceci est destiné à être une démonstration et une preuve de concept pour mettre ensemble une application de cartographie impactante utilisant des données de la vie réelle. Pour une analyse complète et précise, assurez-vous d'utiliser des outils comme le [tableau de bord de l'Université Johns Hopkins](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6). Restez chez vous et soyez en sécurité ! ❤️_

* [Qu'allons-nous construire ?](#heading-quest-ce-que-nous-allons-construire)
* [Qu'avons-nous besoin avant de commencer ?](#heading-quest-ce-que-nous-avons-besoin-avant-de-commencer)
* [Étape 1 : Nettoyer du code inutile](#heading-etape-1-nettoyer-du-code-inutile)
* [Étape 2 : Récupérer les données du Coronavirus](#heading-etape-2-recuperer-les-donnees-du-coronavirus)
* [Étape 3 : Transformer les données du Coronavirus en un format de données géographiques](#heading-etape-3-transformer-les-donnees-du-coronavirus-en-un-format-de-donnees-geographiques)
* [Étape 4 : Ajouter les données du Coronavirus à la carte](#heading-etape-4-ajouter-les-donnees-du-coronavirus-a-la-carte)
* [Que pouvons-nous faire d'autre ?](#heading-que-pouvons-nous-faire-dautre)
* [Restez en sécurité et informé](#heading-restez-en-securite-et-informe)
* [Vous voulez en savoir plus sur les cartes ?](#heading-vous-voulez-en-savoir-plus-sur-les-cartes)

%[https://www.youtube.com/watch?v=GryBIsfBfro]

## Qu'allons-nous construire ?

Nous allons mettre ensemble une application de cartographie qui utilise une API contenant des statistiques récentes sur le Coronavirus et cartographie les emplacements et l'impact auquel chaque pays est confronté.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/coronavirus-map-dashboard-demo.jpg)
_Démonstration du tableau de bord de la carte du Coronavirus_

Sur la carte, nous allons montrer un marqueur pour chaque pays avec le nombre de cas confirmés. En plus de cela, nous inclurons une petite info-bulle qui montre des informations plus détaillées.

La carte que nous allons construire ressemblera principalement à celle ci-dessus, mais sera un peu plus simple. Nous utiliserons le serveur de tuiles public OpenStreetMap au lieu d'utiliser une [Mapbox](https://www.mapbox.com/) personnalisée.

Pour commencer, nous allons utiliser ce [Leaflet Gatsby Starter](https://github.com/colbyfayock/gatsby-starter-leaflet) que j'ai créé pour rendre le démarrage initial un peu plus fluide. Avec notre application démarrée, nous allons récupérer nos données et ajouter des marqueurs à la carte avec nos données.

## Woah, une application de cartographie ?

Oui. Si vous n'avez pas joué avec des cartes auparavant, ne vous découragez pas ! Ce n'est pas aussi compliqué que vous le pensez probablement. Si vous préférez commencer par les bases de la cartographie, vous pouvez [lire plus sur le fonctionnement de la cartographie](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/) d'abord.

## Qu'avons-nous besoin avant de commencer ?

Si vous avez suivi mes tutoriels précédents pour [construire un suiveur du Père Noël](https://www.freecodecamp.org/news/create-your-own-santa-tracker-with-gatsby-and-react-leaflet/) ou [créer une carte de voyage d'été](https://www.freecodecamp.org/news/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet/), vous pouvez suivre les mêmes étapes pour commencer. Sinon, nous voudrons nous assurer que nous avons les éléments suivants configurés :

* [node](https://nodejs.org/en/) ou [yarn](https://yarnpkg.com/en/) - J'utiliserai yarn, mais vous pouvez substituer avec npm lorsque cela est approprié
* [CLI de Gatsby](https://www.gatsbyjs.org/docs/gatsby-cli/) - `yarn global add gatsby-cli`

Si vous n'êtes pas sûr de l'un des éléments ci-dessus, vous pouvez essayer de consulter le début [de mon tutoriel précédent](https://www.freecodecamp.org/news/create-your-own-santa-tracker-with-gatsby-and-react-leaflet/).

Nous voudrons également mettre en place une base pour notre carte. Nous pouvons le faire en utilisant le Leaflet Gatsby Starter que j'ai mis ensemble et qui nous fournit une configuration de base avec [Leaflet](https://leafletjs.com/) et [React Leaflet](https://react-leaflet.js.org/).

```shell
gatsby new my-coronavirus-map https://github.com/colbyfayock/gatsby-starter-leaflet

```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/terminal-creating-new-coronavirus-map-from-gatsby-starter.jpg)
_Création d'une nouvelle application Leaflet Gatsby dans le terminal_

Une fois que cela a fini de s'exécuter, vous pouvez naviguer vers le répertoire du projet nouvellement créé et démarrer votre serveur de développement local :

```shell
cd my-coronavirus-map
yarn develop

```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/terminal-starting-gatsby-development-server-1.jpg)
_Démarrage de votre application Gatsby dans le terminal_

Si tout se passe comme prévu, votre serveur devrait démarrer et vous devriez maintenant pouvoir voir votre application de cartographie de base dans votre navigateur !

![Image](https://www.freecodecamp.org/news/content/images/2020/03/gatsby-starter-leaflet-in-browser-1.jpg)
_Nouvelle application Leaflet Gatsby dans le navigateur_

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commits/master)

## Étape 1 : Nettoyer du code inutile

Le Gatsby Starter que nous utilisons pour démarrer cette application contient du code de démonstration dont nous n'avons pas besoin ici. Nous voudrons apporter toutes les modifications ci-dessous dans le fichier `src/pages/index.js`, qui est la page d'accueil de notre application.

Tout d'abord, supprimons tout le contenu de la fonction `mapEffect`. Cette fonction est utilisée pour exécuter du code qui se déclenche lorsque la carte est rendue.

```javascript
// Dans src/pages/index.js
async function mapEffect({ leafletElement } = {}) {
  // Supprimez tout ce qui se trouve ici
}

```

Nous allons également changer le nom de la variable de notre `leafletElement` simplement pour pouvoir comprendre plus facilement le code lorsque nous l'écrirons.

```javascript
async function mapEffect({ leafletElement: map } = {}) {
}

```

Ensuite, nous ne voulons pas de marqueur cette fois, alors supprimons le composant `<Marker` de notre composant `<Map` :

```react
<Map {...mapSettings} />

```

Maintenant que nous avons supprimé ces éléments, nous pouvons supprimer toutes les importations et variables suivantes du haut de notre fichier :

* useRef
* Marker
* promiseToFlyTo
* getCurrentLocation
* gatsby_astronaut
* timeToZoom
* timeToOpenPopupAfterZoom
* timeToUpdatePopupAfterZoom
* ZOOM
* popupContentHello
* popupContentGatsby
* markerRef

Après cela, notre carte devrait toujours fonctionner, mais ne rien faire.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/new-empty-mapping-app-1.jpg)
_Nouvelle application de cartographie sans rien faire_

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commit/a3e9cff3949bb7ebb7cc89166c875e97b6dcb5a8)

## Étape 2 : Récupérer les données du Coronavirus

Pour notre application, nous allons utiliser l'[API NovelCOVID](https://github.com/NovelCOVID/API). Plus particulièrement, nous allons utiliser le [point de terminaison des pays](https://corona.lmao.ninja/countries) pour récupérer la liste de nos pays et les statistiques qui leur sont associées.

Pour faire des requêtes, j'aime personnellement utiliser [axios](https://github.com/axios/axios) car il a une API agréable à utiliser. Si vous voulez utiliser [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) ou votre propre bibliothèque de requêtes préférée, substituez-la pour cette étape.

Nous allons commencer par installer axios :

```shell
yarn add axios

```

Une fois que cela est installé, n'oubliez pas de redémarrer votre serveur.

Importez le package axios en haut de notre fichier `pages/index.js` :

```javascript
import axios from 'axios';

```

Ensuite, nous allons effectivement faire notre requête. À l'intérieur de notre fonction `mapEffect`, essayons de faire une requête au point de terminaison de l'API :

```javascript
async function mapEffect({ leafletElement: map } = {}) {
    let response;

    try {
      response = await axios.get('https://corona.lmao.ninja/v2/countries');
    } catch(e) {
      console.log(`Échec de la récupération des pays : ${e.message}`, e);
      return;
    }

    const { data = [] } = response;
}

```

Dans cet extrait, nous faisons ce qui suit :

* Nous configurons une variable `response` qui nous permettra de stocker la réponse
* Nous ajoutons un bloc `try/catch` qui attrapera toute erreur d'API si la requête échoue
* Si la requête est réussie, nous stockons la réponse dans la variable `response`
* Si la requête échoue, nous enregistrons l'erreur dans la console et quittons la fonction pour ne pas continuer à exécuter le code avec une requête échouée
* Une fois que nous avons notre réponse, nous pouvons déstructurer `data` de la réponse et définir la valeur par défaut à un tableau vide, car ce sera le type de données dont nous avons besoin

Après cela, nous pouvons enregistrer l'objet `data` dans la console et nous verrons nos données récupérées avec succès !

![Image](https://www.freecodecamp.org/news/content/images/2020/03/coronavirus-location-data-in-browser.jpg)
_Enregistrement des données de localisation du Coronavirus dans la console du navigateur_

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commit/86bebfee4a34b9bad516879b228921cdaad55126)

**Mise à jour :** Le commit précédent inclut un lien vers le point de terminaison original de l'API NovelCOVID v1 qui est maintenant obsolète. Veuillez utiliser ceci à la place : [https://corona.lmao.ninja/v2/countries](https://corona.lmao.ninja/v2/countries).

[Voir le commit mis à jour](https://github.com/colbyfayock/my-coronavirus-map/commit/e8f63c7ca60ec358b2edc9bc3ed8935be85b5573).

## Étape 3 : Transformer les données du Coronavirus en un format de données géographiques

Maintenant que nous avons nos données, nous pouvons les transformer en un format de données géographiques, en particulier [GeoJSON](https://geojson.org/), qui nous permettra d'interfacer avec Leaflet.

Commençons par ajouter ce bloc de code :

```javascript
const { data = [] } = response;
const hasData = Array.isArray(data) && data.length > 0;

if ( !hasData ) return;

const geoJson = {
  type: 'FeatureCollection',
  features: data.map((country = {}) => {
    const { countryInfo = {} } = country;
    const { lat, long: lng } = countryInfo;
    return {
      type: 'Feature',
      properties: {
       ...country,
      },
      geometry: {
        type: 'Point',
        coordinates: [ lng, lat ]
      }
    }
  })
}


```

Alors, que faisons-nous ici ?

* Nous créons une nouvelle constante appelée `hasData` qui vérifie si notre variable `data` est un tableau et contient des données
* Si nous n'avons pas de données, nous voulons quitter la fonction, car nous ne voulons pas essayer d'ajouter des données que nous n'avons pas
* Nous créons un objet `geoJson` qui sera notre document GeoJSON
* Notre document est de type `FeatureCollection` et en tant que nos `features`, nous parcourons notre ensemble de données
* Pour chaque pays dans nos données, nous obtenons la `lat` et la `lng` pour créer un point pour notre carte
* Nous ajoutons également nos données de pays en tant que propriétés afin de pouvoir y accéder dans nos API de cartographie

Si vous `console.log` cet objet dans votre navigateur et copiez le contenu, vous pouvez coller ceci dans geojson.io et voir les données de localisation s'afficher correctement.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/location-data-geojson-io.jpg)
_Aperçu des données de localisation du Coronavirus sur geojson.io_

Avec ce document GeoJSON, nous pourrons maintenant l'ajouter à notre carte.

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commit/f0da2d05cbc16783322684da7a3efaa61022f5b6)

## Étape 4 : Ajouter les données du Coronavirus à la carte

Nous avons notre document GeoJSON avec nos données de localisation, alors ajoutons-le à la carte.

Commençons par ce bloc de code. Il est long, mais nous allons le décomposer pièce par pièce :

```javascript
const geoJsonLayers = new L.GeoJSON(geoJson, {
  pointToLayer: (feature = {}, latlng) => {
    const { properties = {} } = feature;
    let updatedFormatted;
    let casesString;

    const {
      country,
      updated,
      cases,
      deaths,
      recovered
    } = properties

    casesString = `${cases}`;

    if ( cases > 1000 ) {
      casesString = `${casesString.slice(0, -3)}k+`
    }

    if ( updated ) {
      updatedFormatted = new Date(updated).toLocaleString();
    }

    const html = `
      <span class="icon-marker">
        <span class="icon-marker-tooltip">
          <h2>${country}</h2>
          <ul>
            <li><strong>Confirmés :</strong> ${cases}</li>
            <li><strong>Décès :</strong> ${deaths}</li>
            <li><strong>Rétablis :</strong> ${recovered}</li>
            <li><strong>Dernière mise à jour :</strong> ${updatedFormatted}</li>
          </ul>
        </span>
        ${ casesString }
      </span>
    `;

    return L.marker( latlng, {
      icon: L.divIcon({
        className: 'icon',
        html
      }),
      riseOnHover: true
    });
  }
});

```

Alors, que faisons-nous ici ?

* Nous créons une nouvelle instance de `L.GeoJSON` qui transformera notre document GeoJSON en quelque chose que Leaflet comprendra
* À l'intérieur de cette instance, nous définissons une fonction `pointToLayer` personnalisée. Cela nous permet de personnaliser la couche de carte que Leaflet crée pour notre carte
* Dans notre fonction, nous assignons et créons nos points de données que nous voulons. La plupart est de la déstructuration, mais nous formatons le compte des cas pour afficher `1k+` au lieu de `1000` et une date formatée au lieu du timestamp
* Nous créons un bloc de chaîne HTML qui est utilisé pour définir notre marqueur de carte qui sera ajouté à la carte. Cela inclut également le HTML pour l'info-bulle qui apparaîtra lorsque vous survolez un marqueur
* Nous retournons `L.marker` avec notre configuration personnalisée qui inclut une classe de `icon` pour le conteneur et notre HTML personnalisé.
* De plus, nous ajoutons la propriété `riseOnHover` afin que lorsque vous survolez un marqueur, il se place au-dessus des autres marqueurs sur la carte

Nous voulons également ajouter un peu de CSS ici pour nous assurer que nos marqueurs apparaissent sur la carte et sont utilisables. Ajoutons cet extrait à notre fichier `assets/stylesheets/components/_map.scss` :

```scss
.icon-marker {

  display: flex;
  position: relative;
  justify-content: center;
  align-items: center;
  color: white;
  width: 3.6em;
  height: 3.6em;
  font-size: .7em;
  font-weight: bold;
  background-color: $red-800;
  border-radius: 100%;
  box-shadow: 0 2px 5px rgba(black, .9);

  &:hover {

    .icon-marker-tooltip {
      display: block;
    }

  }

}

.icon-marker-tooltip {

  display: none;
  position: absolute;
  bottom: 100%;
  width: 16em;
  font-size: 1.4em;
  padding: 1em;
  background-color: $blue-grey-900;
  border-radius: .4em;
  margin-bottom: 1em;
  box-shadow: 0 3px 5px rgba(black, .9);

  &:before {
    display: block;
    position: absolute;
    bottom: -.6em;
    left: 50%;
    content: '';
    width: 1.4em;
    height: 1.4em;
    background-color: $blue-grey-900;
    transform: rotate(45deg);
    margin-left: -.7em;
  }

  h2 {
    font-size: 1.5em;
    line-height: 1.2;
    margin-bottom: .1em;
    margin-top: 0;
  }

  h3 {
    font-size: 1.2em;
    margin: .1em 0;
    font-weight: normal;
    color: $blue-grey-100;
  }

  ul,
  p {
    font-weight: normal;
  }

  ul {
    list-style: none;
    padding: 0;
    margin: .6em 0 0;
  }

}

```

Ce que nous faisons :

* Nous créons nos marqueurs ronds en utilisant la classe `.icon-marker` et configurons notre classe `.icon-marker-tooltip` pour qu'elle apparaisse lorsque l'on survole
* Notre classe `.icon-marker-tooltip` est masquée par défaut, car c'est notre info-bulle, mais nous la positionnons de manière absolue pour qu'elle apparaisse au-dessus de notre marqueur et formatée comme nous le voulons

Et enfin, une fois que nous avons créé nos `geoJsonLayers` avec notre style ajouté, nous pouvons l'ajouter à la carte !

```
geoJsonLayers.addTo(map)

```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/map-with-coronavirus-location-data.jpg)
_Carte avec les données de localisation du Coronavirus_

Maintenant, vous vous demandez peut-être pourquoi elle ne semble pas être centrée correctement. Allez-y et changez la variable `LOCATION` en haut du fichier `index.js` en :

```javascript
const LOCATION = {
  lat: 0,
  lng: 0
};

```

Une fois que cela est défini, lorsque la page se recharge, la carte devrait être centrée au milieu du monde !

![Image](https://www.freecodecamp.org/news/content/images/2020/03/map-with-coronavirus-location-data-centered-tooltip.jpg)
_Carte avec les données de localisation du Coronavirus centrées avec une info-bulle_

[Suivez le commit !](https://github.com/colbyfayock/my-coronavirus-map/commit/49c78e4ef3e98c974fab7bca10b6f8f7578b42c2)

## Hourra, nous l'avons fait ! ?

Si vous avez suivi, vous avez maintenant créé votre propre tableau de bord de carte du Coronavirus qui donne quelques statistiques rapides sur les cas dans le monde.

Prenez ce que vous avez appris et courez avec. Vous pouvez appliquer cela à tout autre type de données que vous pouvez imaginer.

## Que pouvons-nous faire d'autre ?

### Ajouter plus de styles et une carte de base personnalisée

Dans ma démonstration originale, j'ai configuré une carte de base personnalisée en utilisant [Mapbox](https://mapbox.com/) qui me permet d'avoir un fond sombre rendant les marqueurs plus faciles à voir.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/mapbox-studio-basemap.jpg)
_Création d'une nouvelle carte de base dans Mapbox Studio_

Mapbox est génial et a un bon niveau gratuit si vous êtes intéressé à commencer.

Une fois que vous avez un compte Mapbox, vous pouvez même [copier le style](https://api.mapbox.com/styles/v1/colbyfayock/ck8c2foj72lqk1jnug0g2haw0.html?fresh=true&title=copy&access_token=pk.eyJ1IjoiY29sYnlmYXlvY2siLCJhIjoiY2swODZzbXYxMGZzdzNjcXczczF6MnlvcCJ9.HCfgUYZUTP7uixjYF7tBSw) que j'ai utilisé et le rendre vôtre.

[Thème Mapbox Dark Basique](https://api.mapbox.com/styles/v1/colbyfayock/ck8c2foj72lqk1jnug0g2haw0.html?fresh=true&title=copy&access_token=pk.eyJ1IjoiY29sYnlmYXlvY2siLCJhIjoiY2swODZzbXYxMGZzdzNjcXczczF6MnlvcCJ9.HCfgUYZUTP7uixjYF7tBSw)

Pour apprendre comment l'intégrer, vous pouvez essayer de consulter le code source de [ma démonstration originale](https://github.com/colbyfayock/coronavirus-map-dashboard) :

[https://github.com/colbyfayock/coronavirus-map-dashboard](https://github.com/colbyfayock/coronavirus-map-dashboard)

### Ajouter des statistiques de tableau de bord général

Les tableaux de bord avec des cartes comme l'[application de l'Université Johns Hopkins](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) nous permettent de voir plus qu'un simple aperçu de la carte, mais un aperçu des statistiques rapides sur les cas dans le monde.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/johns-hopkins-coronavirus-map-march-29.jpg)
_Tableau de bord de la carte du Coronavirus de l'Université Johns Hopkins - 29 mars 2020_

L'[API NovelCOVID](https://github.com/NovelCOVID/API) a plus de points de terminaison comme `/all` qui fournissent quelques statistiques globales.

## Restez en sécurité et informé

Je veux réitérer que vous devez vous assurer de rester à jour en utilisant des sources officielles d'information, comme le tableau de bord de l'Université Johns Hopkins. Bien que les données devraient être fiables, elles devraient également être considérées comme une preuve de concept pour construire une carte et y faire référence, mais ne devraient pas être considérées pour une quelconque analyse statistique.

Veuillez prendre soin de vous pendant ces périodes. Nous sommes tous dans le même bateau ! ❤️

## Vous voulez en savoir plus sur les cartes ?

Vous pouvez consulter quelques-unes de mes autres ressources pour commencer :

* [Tout le monde peut cartographier ! Inspiration et une introduction au monde de la cartographie](https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping)
* [Comment configurer un style de carte de base Mapbox personnalisé avec React Leaflet et Leaflet Gatsby Starter](https://www.colbyfayock.com/2020/04/how-to-set-up-a-custom-mapbox-basemap-style-with-react-leaflet-and-leaflet-gatsby-starter/)
* [Comment créer une application de cartographie de voyage d'été avec Gatsby et Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet)
* [Comment créer votre propre suiveur du Père Noël avec Gatsby et React Leaflet](https://www.colbyfayock.com/2019/12/create-your-own-santa-tracker-with-gatsby-and-react-leaflet/)
* [Comment construire une application de cartographie en React facilement avec Leaflet](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e9f3fb Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>
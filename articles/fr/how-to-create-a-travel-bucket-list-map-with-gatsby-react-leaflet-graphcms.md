---
title: Comment créer une carte de liste de voyages avec Gatsby, React Leaflet et Hygraph
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-23T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-travel-bucket-list-map-with-gatsby-react-leaflet-graphcms
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/travel-bucket-list.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: cms
  slug: cms
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: graphcms
  slug: graphcms
- name: headless cms
  slug: headless-cms
- name: JavaScript
  slug: javascript
- name: leaflet
  slug: leaflet
- name: Mapping
  slug: mapping
- name: maps
  slug: maps
- name: react-leaflet
  slug: react-leaflet
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Travel
  slug: travel
- name: Tutorial
  slug: tutorial
seo_title: Comment créer une carte de liste de voyages avec Gatsby, React Leaflet
  et Hygraph
seo_desc: Traveling is fun and we all have a lot of places we want to visit, but rarely
  do we have time to do it all at once. That’s what bucket lists are for! How can
  we create a custom mapping app that we can show all of our the destinations on our
  bucket li...
---

Voyager est amusant et nous avons tous beaucoup d'endroits que nous voulons visiter, mais nous avons rarement le temps de tout faire en une seule fois. C'est à cela que servent les listes de choses à faire ! Comment pouvons-nous créer une application de cartographie personnalisée qui nous permet d'afficher toutes les destinations de notre liste de choses à faire ?

Note : À partir de juillet 2022, GraphCMS est maintenant [Hygraph](https://hygraph.com/).

* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 1 : Créer une nouvelle application avec Gatsby Starter Leaflet](#heading-etape-1-creer-une-nouvelle-application-avec-gatsby-starter-leaflet)
* [Étape 2 : Créer et gérer une liste de lieux de voyage avec GraphCMS](#heading-etape-2-creer-et-gerer-une-liste-de-lieux-de-voyage-avec-graphcms)
* [Étape 3 : Interroger nos données de localisation GraphCMS avec Gatsby et GraphQL](#heading-etape-3-interroger-nos-donnees-de-localisation-graphcms-avec-gatsby-et-graphql)
* [Étape 4 : Créer une liste de destinations et les ajouter à la carte](#heading-etape-4-creer-une-liste-de-destinations-et-les-ajouter-a-la-carte)
* [Quelles autres fonctionnalités pouvons-nous ajouter à notre application ?](#heading-quelles-autres-fonctionnalités-pouvons-nous-ajouter-a-notre-application)
* [Vous voulez en savoir plus sur les cartes ?](#heading-vous-voulez-en-savoir-plus-sur-les-cartes)

%[https://www.youtube.com/watch?v=isbr52VKjb0]

## Que allons-nous construire ?

Nous allons construire une application de cartographie avec [Gatsby](https://www.gatsbyjs.org/) gérée par un CMS qui affichera à la fois des marqueurs sur une carte et montrera nos lieux dans une liste de destinations simple pour notre liste de choses à faire.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/travel-bucket-list-demo.jpg)
_Démo d'une application de cartographie de liste de voyages_

Nous allons lancer l'application avec un [Gatsby Starter pour Leaflet](https://github.com/colbyfayock/gatsby-starter-leaflet) et ensuite nous utiliserons [GraphCMS](https://graphcms.com/) pour créer et gérer la liste des lieux pour notre carte !

## Woah, une application de cartographie ?

Oui. Si vous n'avez jamais joué avec des cartes auparavant, ne vous découragez pas ! Ce n'est pas aussi compliqué que vous le pensez probablement. Si vous préférez commencer par les bases de la cartographie, vous pouvez [lire plus sur le fonctionnement de la cartographie](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/) d'abord.

## Étape 1 : Créer une nouvelle application avec Gatsby Starter Leaflet

Nous allons commencer avec Gatsby Starter Leaflet. Cela nous donnera une application React de base avec nos outils de cartographie déjà intégrés.

### Créer une nouvelle application Gatsby avec Gatsby Starter Leaflet

Pour commencer, naviguez vers l'endroit où vous souhaitez créer votre nouvelle application et exécutez :

```shell
gatsby new my-travel-bucket-list https://github.com/colbyfayock/gatsby-starter-leaflet

```

_Note : vous pouvez remplacer `my-travel-bucket-list` par ce que vous voulez. Cela sera utilisé pour créer le nouveau dossier pour l'application._

Une fois que vous avez exécuté cela, Gatsby téléchargera le Starter et installera les dépendances. Une fois terminé, naviguez vers ce répertoire et exécutez la commande de développement :

```shell
cd my-travel-bucket-list
yarn develop
# ou
npm run develop

```

Une fois le chargement terminé, votre application devrait être prête à fonctionner !

### Nettoyer un peu de code de démonstration

Parce que nous utilisons un Starter, il contient un peu de code de démonstration. Nettoyons cela pour éviter toute confusion.

Ouvrez le fichier `src/pages/index.js`.

Tout d'abord, supprimez tout ce qui se trouve à l'intérieur de `mapEffect` sauf la première ligne et configurez un alias pour `leafletElement` à `map` :

```js
async function mapEffect({ leafletElement: map } = {}) {
  if ( !map ) return;
}

```

Avec cela supprimé, nous pouvons supprimer la définition `markerRef` en haut du composant `IndexPage`, supprimer la prop `ref={markerRef}` de notre composant `<Marker>`, et l'import `useRef` à côté de React.

Maintenant, nous pouvons supprimer toutes les variables qui commencent par `popup` et `time`, y compris :

* timeToZoom
* timeToOpenPopupAfterZoom
* timeToUpdatePopupAfterZoom
* popupContentHello
* popupContentGatsby

Enfin, vous pouvez supprimer toutes les lignes suivantes :

```js
import L from 'leaflet';
...
import { promiseToFlyTo, getCurrentLocation } from 'lib/map';
...
import gatsby_astronaut from 'assets/images/gatsby-astronaut.jpg';
...
const ZOOM = 10;

```

Une fois terminé, nous devrions être prêts à partir avec une application de base avec une carte !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/new-app-gatsby-starter-leaflet.jpg)
_Nouvelle application avec Gatsby Starter Leaflet_

[Suivez le commit !](https://github.com/colbyfayock/my-travel-bucket-list/commit/63eed5a7a208ede6f8eeec44e0c08b594b407360)

## Étape 2 : Créer et gérer une liste de lieux de voyage avec GraphCMS

### Créer un compte GraphCMS

Pour commencer avec GraphCMS, vous aurez besoin d'un compte. Je ne vais pas vous guider à travers cette partie, mais la bonne nouvelle est qu'ils ont un niveau gratuit généreux qui facilite l'inscription pour que nous puissions l'utiliser pour notre démonstration !

[Inscrivez-vous à GraphCMS](https://app.graphcms.com/signup)

Alternativement, si vous avez déjà un compte, vous pouvez vous assurer que vous êtes connecté.

### Créer un nouveau projet GraphCMS

Une fois connecté, nous voudrons créer un nouveau projet. Nous allons en créer un manuellement, donc une fois sur le [Tableau de bord GraphCMS](https://app.graphcms.com/), sélectionnez **Créer un nouveau projet** :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-create-new-project.jpg)
_Création d'un nouveau projet dans GraphCMS_

Ici, vous pouvez entrer ce que vous voulez pour le **Nom** et la **Description** comme :

* Nom : Ma liste de voyages
* Description : Les lieux que je veux visiter un jour !

En dessous, vous verrez une carte où vous sélectionnerez une **Région**. C'est là que vos données de base de données résideront, donc bien que cela ne compte probablement pas trop pour nos besoins, vous pouvez choisir celle qui est la plus proche de vous.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-new-project.jpg)
_Configuration d'un nouveau projet dans GraphCMS_

Après avoir sélectionné vos options, allez-y et cliquez sur **Créer un projet**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-select-plan.jpg)
_Sélection du plan Personnel dans GraphCMS_

Ensuite, vous serez présenté avec des options de facturation. Puisque nous créons simplement une démonstration, sous **Personnel**, sélectionnez **Continuer**, moment auquel nous serons déposés dans notre nouveau tableau de bord de projet GraphCMS.

### Créer un nouveau schéma de modèle de contenu avec GraphCMS

Dans GraphCMS, un Modèle de Contenu fait référence à un type spécifique de données qui a des propriétés spécifiques associées. Dans notre cas, notre Modèle sera une Destination, qui sera définie par un Nom et un Lieu.

Tout d'abord, naviguez vers la section **Schéma** de GraphCMS dans la barre latérale de gauche et sélectionnez **Créer un Modèle**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-create-new-schema-model.jpg)
_Création d'un nouveau Modèle de Schéma dans GraphCMS_

Une fois sélectionné, vous verrez une fenêtre contextuelle qui demande un peu plus d'informations. Ici, vous pouvez taper "Destination" comme **Nom d'affichage**, ce qui remplira également la plupart des autres champs. Nous les laisserons tels quels.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-new-content-model.jpg)
_Configuration d'un nouveau Modèle dans GraphCMS_

N'hésitez pas à ajouter une description si vous le souhaitez, mais ce n'est pas obligatoire. Ensuite, sélectionnez **Créer un modèle**.

Maintenant que nous avons notre Modèle, nous avons besoin de nos propriétés.

Tout d'abord, sélectionnez **Texte en une seule ligne** dans la liste des champs à droite et ajoutez un **Nom d'affichage** de "Nom". Cela remplira également **ID de l'application** que vous pouvez laisser tel quel. Ensuite, cliquez sur **Créer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-text-field.jpg)
_Ajout et configuration d'un nouveau champ de texte dans GraphCMS_

Ensuite, faites défiler vers le bas dans les options de champ à droite et sous **Lieu**, sélectionnez **Carte**. Ajoutez "Lieu" comme **Nom d'affichage**, ce qui définira l'**ID de l'application** comme "lieu" que vous pouvez laisser tel quel. Ensuite, comme avant, cliquez sur **Créer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-new-map-field.jpg)
_Ajout et configuration d'un nouveau champ de carte dans GraphCMS_

Maintenant, nous avons un Modèle de Contenu que nous utiliserons pour créer nos lieux !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-destination-content-model.jpg)
_Modèle de contenu de destination dans GraphCMS_

### Créer nos lieux

Enfin, créons nos lieux. Naviguez vers **Contenu** dans le tableau de bord GraphCMS, assurez-vous d'avoir sélectionné **Destination** sous **Système** (devrait être le seul), et sélectionnez **Créer un nouveau**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-add-new-content.jpg)
_Créer un nouveau contenu de destination dans GraphCMS_

Maintenant, nous pouvons commencer à ajouter tous nos lieux ! Tout d'abord, ajoutez le nom de votre lieu dans le champ **Nom**, puis vous pouvez utiliser la boîte de **Recherche** sous **Lieu** pour trouver cet endroit sur la carte.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-create-new-destination-content-item.jpg)
_Ajout d'un nouvel élément de contenu de destination dans GraphCMS_

Une fois que vous êtes prêt, cliquez sur **Enregistrer et publier**. Cela créera votre premier lieu !

Suivez ces mêmes étapes et créez autant de lieux que vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-destination-content-items.jpg)
_Liste des éléments de contenu de destination dans GraphCMS_

Nous les utiliserons pour notre carte et notre liste de choses à faire.

## Étape 3 : Interroger nos données de localisation GraphCMS avec Gatsby et GraphQL

Maintenant que nous avons nos lieux, utilisons-les !

### Ajouter un plugin à Gatsby pour interroger nos données GraphQL

Tout d'abord, nous devons [ajouter un nouveau plugin](https://www.gatsbyjs.org/packages/gatsby-source-graphql/) à notre projet Gatsby pour interroger nos données GraphQL. Dans votre terminal, assurez-vous que votre serveur de développement n'est pas en cours d'exécution et exécutez :

```shell
yarn add gatsby-source-graphql
# ou
npm install gatsby-source-graphql

```

Ensuite, ouvrez votre fichier `gatsby-config.js` à la racine de votre projet et ajoutez ce qui suit à vos plugins :

```json
{
  resolve: 'gatsby-source-graphql',
  options: {
    typeName: 'GCMS',
    fieldName: 'gcms',
    url: '[API ENDPOINT]',
  }
}

```

Cela sera ce qui source nos données de GraphCMS, mais nous avons besoin d'un endpoint.

### Trouver notre endpoint API pour GraphCMS

Ouvrez à nouveau votre navigateur et rendez-vous sur votre projet GraphCMS. Après avoir sélectionné **Paramètres** dans la navigation de gauche, sélectionnez **Accès API**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-api-access.jpg)
_Accès API dans GraphCMS_

Avant de copier notre endpoint API, nous devons d'abord mettre à jour nos permissions afin de pouvoir interroger notre API. Sous **Permissions de l'API publique**, cochez la case à côté de **Contenu de l'étape Publié** et cliquez sur **Enregistrer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-api-access.jpg)
_Configuration des permissions de l'API dans GraphCMS_

Ensuite, copiez l'URL sous **Endpoints** :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-copy-api-access-endpoint.jpg)
_Copie de l'Endpoint API dans GraphCMS_

Et collez cela dans votre fichier `gatsby-config.js` que nous avons modifié ci-dessus :

```json
{
  resolve: 'gatsby-source-graphql',
  options: {
    typeName: 'GCMS',
    fieldName: 'gcms',
    url: 'https://[region-id].graphcms.com/v2/[project-id]/master',
  },
},

```

_Note : votre URL aura des valeurs réelles à l'intérieur de `[region-id]` et `[project-id]`._

Enregistrez votre fichier `gatsby-config.js` et redémarrez votre serveur de développement (`yarn develop`) et nous sommes prêts à partir !

### Interroger nos lieux via GraphQL

Enfin, interrogeons réellement nos données afin de pouvoir les utiliser dans notre application.

Nous allons créer un nouveau [React Hook](https://reactjs.org/docs/hooks-reference.html) que nous pourrons utiliser pour récupérer nos lieux n'importe où dans notre application.

Sous `src/hooks/index.js`, ajoutez la ligne suivante à la liste existante :

```js
export { default as useDestinations } from './useDestinations';

```

Cela nous permettra d'importer plus facilement notre hook que nous allons créer ensuite.

Sous `src/hooks`, créez un nouveau fichier `useDestinations.js` et collez ce code :

```js
import { graphql, useStaticQuery } from 'gatsby';

export default function useDestinations() {
  const { gcms = {} } = useStaticQuery( graphql`
    query {
      gcms {
        destinations {
          id
          name
          location {
            latitude
            longitude
          }
        }
      }
    }
  ` );

  let { destinations } = gcms;

  return {
    destinations,
  };
}

```

Ici, nous :

* Importons les utilitaires `graphql` et `useStaticQuery` de Gatsby
* Nous créons une nouvelle fonction (ou hook) qui est exportée par défaut
* Dans cette fonction, nous utilisons `useStaticQuery` pour créer une nouvelle requête GraphQL qui demande à GraphCMS de retourner la structure de données que nous avons définie.
* Cette requête retourne une valeur que nous déstructurons immédiatement pour récupérer l'objet `gmcs`
* Nous déstructurons `destinations` de `gmcs` et le retournons dans le cadre d'un nouvel objet de notre hook

Avec cela, nous pouvons maintenant utiliser notre hook n'importe où dans notre application !

Rendez-vous dans votre fichier `src/pages/index.js`, importez d'abord notre nouveau hook :

```js
import { useDestinations } from 'hooks';

```

Et en haut du composant `IndexPage`, interrogeons nos données :

```js
const { destinations } = useDestinations();

```

Cela place toutes nos destinations dans la variable `destinations`. Nous pouvons tester que cela fonctionne en les enregistrant dans la console :

```js
console.log('destinations', destinations);

```

Et une fois que nous ouvrons notre navigateur et regardons dans la console des outils de développement web, nous pouvons voir nos données de localisation !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/gatsby-starter-leaflet-logging-graphcms-destinations.jpg)
_Enregistrement des données de destinations dans la console web_

## Étape 4 : Créer une liste de destinations et les ajouter à la carte

Nous allons commencer par créer une simple liste de texte de nos destinations. Cela nous permettra de voir toutes nos destinations dans un format facile à lire.

### Créer une liste de texte de nos destinations

À l'intérieur de notre `IndexPage` et au-dessus de "Still Getting Started?", ajoutons le code suivant :

```jsx
<h2>Mes Destinations</h2>
<ul>
  { destinations.map(destination => {
    const { id, name } = destination;
    return <li key={id}>{ name }</li>
  })}
</ul>

```

Ce code :

* Ajoute un nouvel en-tête pour notre liste
* Crée une nouvelle liste non ordonnée
* Parcourt nos `destinations` et crée un nouvel élément de liste pour chaque destination qui inclut le nom du lieu

Une fois que nous avons enregistré et rechargé, nous devrions voir notre liste sous notre carte !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/app-adding-list-of-destinations.jpg)
_Nouvelle liste de base des destinations dans l'application_

La liste semble un peu étrange, n'est-ce pas ? Nous voulons probablement la formater un peu mieux pour qu'elle s'intègre dans la page.

Ouvrez `src/assets/stylesheets/pages/_home.scss` et à l'intérieur de la classe `.home-start`, ajoutez :

```scss
.home-start {

  ...

  ul {
    list-style: none;
    padding: 0;
    margin: 1.2em 0;
  }

```

Modifions également le `h2` pour espacer un peu mieux les choses :

```scss
.home-start {

  ...

  h2 {

    margin-top: 2em;

    &:first-child {
      margin-top: 0;
    }

  }

```

Une fois que vous avez enregistré et rechargé, cela devrait avoir l'air un peu mieux.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/app-fixing-styles-list-of-destinations.jpg)
_Destinations dans l'application avec des styles nettoyés_

N'hésitez pas à apporter des modifications supplémentaires, mais nous allons en rester là pour l'instant.

### Ajouter nos destinations à la carte

Maintenant, nous pouvons enfin ajouter nos destinations à la carte !

À l'intérieur de notre composant `<Map>`, nous avons déjà un `<Marker>`. Cela nous permet d'ajouter facilement un marqueur à la carte étant donné une position. Nous allons prendre ce concept et le combiner avec notre liste de texte pour ajouter nos lieux à la carte.

Mettons à jour notre code `<Map>` pour qu'il corresponde à ce qui suit :

```jsx
<Map {...mapSettings}>
  { destinations.map(destination => {
    const { id, name, location } = destination;
    const position = [location.latitude, location.longitude];
    return <Marker key={id} position={position} />
  })}
</Map>

```

Ici, nous :

* Parcourons nos `destinations` pour créer dynamiquement une nouvelle liste de composants à l'intérieur de notre `<Map>`
* À l'intérieur de chaque instance de boucle, nous déstructurons notre date de `destination`
* Nous créons un nouveau tableau `position` avec la latitude et la longitude
* Créons un nouveau `Marker` où nous utilisons notre position pour l'ajouter à la carte

Cela nous donne nos marqueurs sur la carte !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mapping-app-with-destination-markers.jpg)
_Marqueurs pour chaque destination dans l'application de cartographie_

Mais nous voulons savoir ce que sont chacun de ces lieux, alors ajoutons aussi une popup à chaque marqueur qui affichera le nom.

Tout d'abord, nous devons importer `Popup` de `react-leaflet` :

```js
import { Marker, Popup } from 'react-leaflet';

```

Ensuite, mettons à jour notre composant `<Marker>` pour qu'il retourne :

```jsx
return (
  <Marker key={id} position={position}>
    <Popup>{ name }</Popup>
  </Marker>
);

```

Et une fois que nous avons enregistré et rouvert notre carte, vous pouvez maintenant cliquer sur chaque marqueur et voir le nom de nos destinations !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mapping-app-with-destination-marker-popup.jpg)
_Popup pour chaque marqueur de destination dans l'application de cartographie_

### Avant de terminer, centrer la carte

Auparavant, notre carte de démonstration était centrée sur Washington, DC. Mettons cela à jour au centre du monde puisque notre carte ne se concentre pas sur les États-Unis.

Mettez à jour la variable `LOCATION` à :

```js
const LOCATION = {
  lat: 0,
  lng: 0,
};

```

Et avec cela, nous avons notre carte !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mapping-app-with-travel-bucket-list-markers.jpg)
_Application de cartographie finale avec des marqueurs et des popups pour chaque destination_

[Suivez le commit !](https://github.com/colbyfayock/my-travel-bucket-list/commit/56dbadb74cea2770174eb8ea7c039be27ca18971)

## Quelles autres fonctionnalités pouvons-nous ajouter à notre application ?

### Ajouter un moyen de cocher chaque lieu

Dans GraphCMS, vous pouvez ajouter un nouveau champ à votre modèle de contenu de destination qui vous permet de sélectionner si vous avez visité chaque lieu ou non.

Avec cette valeur, nous pouvons l'ajouter à notre requête et mettre à jour notre carte avec une sorte d'indicateur comme une coche pour montrer que nous l'avons coché de notre liste de choses à faire !

### Personnaliser les styles d'arrière-plan de votre carte

Nous utilisons une version publique de [OpenStreetMap](https://www.openstreetmap.org/#map=5/38.007/-95.844) qui est open source, mais [Mapbox](https://www.mapbox.com/) offre quelques cartes sympas que nous pouvons utiliser pour la rendre un peu plus impressionnante.

Si vous voulez commencer à changer les styles de votre carte, vous pouvez [consulter ce autre tutoriel](https://www.freecodecamp.org/news/how-to-set-up-a-custom-mapbox-basemap-with-gatsby-and-react-leaflet/) pour apprendre comment utiliser Mapbox.

[Consultez l'article de blog](https://www.colbyfayock.com/2020/04/how-to-set-up-a-custom-mapbox-basemap-style-with-react-leaflet-and-leaflet-gatsby-starter) ou [regardez la vidéo](https://www.youtube.com/watch?v=KcPJr1b_rv0) !

### Styliser les marqueurs de la carte avec une image personnalisée

Vous pouvez consulter ma vidéo pour savoir comment changer les marqueurs en une image personnalisée.

Allez plus loin et utilisez la fonctionnalité ci-dessus pour montrer dynamiquement une image de marqueur différente lorsque vous avez coché un lieu.

[Consultez la vidéo sur Egghead.io !](https://egghead.io/lessons/react-customize-geojson-data-markers-with-a-react-leaflet-icon-image?pl=mapping-with-react-leaflet-e0e0&af=atzgap)

## Vous voulez en savoir plus sur les cartes ?

Consultez certains de mes autres tutoriels et vidéos :

* [Cartographie avec React Leaflet](https://egghead.io/playlists/mapping-with-react-leaflet-e0e0?af=atzgap) ([egghead.io](https://egghead.io/?af=atzgap))
* [Applications de cartographie avec React, Gatsby et Leaflet](https://www.youtube.com/playlist?list=PLFsfg2xP7cbJTnTFH3OGXEAt9O1mpoqpR) ([youtube.com](https://www.youtube.com/channel/UC7Wpv0Aft4NPNhHWW_JC4GQ))
* [Comment créer un tableau de bord et une application de carte Coronavirus (COVID-19) avec Gatsby et Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet) (colbyfayock.com)
* [Comment créer une application de cartographie de road trip d'été avec Gatsby et Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet) (colbyfayock.com)
* [Comment construire une application de cartographie en React facilement avec Leaflet](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/) (colbyfayock.com)
* [Tout le monde peut cartographier ! Inspiration et une introduction au monde de la cartographie](https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping) (colbyfayock.com)

## Qu'y a-t-il sur votre liste de voyages ?

[Faites-le moi savoir sur Twitter !](https://twitter.com/colbyfayock)

%[https://twitter.com/colbyfayock/status/1275441134144110595]

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
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709e0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>
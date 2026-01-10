---
title: Comment configurer un style de fond de carte Mapbox personnalisé avec React
  Leaflet et Leaflet Gatsby Starter
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-04-08T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-custom-mapbox-basemap-with-gatsby-and-react-leaflet
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/mapbox-basemap-react-leaflet-1.jpg
tags:
- name: create-react-app
  slug: create-react-app
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
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: leaflet
  slug: leaflet
- name: mapbox
  slug: mapbox
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
seo_title: Comment configurer un style de fond de carte Mapbox personnalisé avec React
  Leaflet et Leaflet Gatsby Starter
seo_desc: 'Building maps can be pretty powerful, but often you’re stuck with open
  source options for the map imagery that might not help the readability of your data.
  How can we leverage Mapbox’s tile APIs to add a custom basemap to our React Leaflet
  app?


  What...'
---

Créer des cartes peut être très puissant, mais souvent vous êtes limité aux options open source pour l'imagerie cartographique qui ne facilitent pas la lisibilité de vos données. Comment pouvons-nous exploiter les API de tuiles de Mapbox pour ajouter un fond de carte personnalisé à notre application React Leaflet ?

* [Qu'allons-nous construire ?](#heading-quest-ce-que-nous-allons-construire)
* [Qu'est-ce que Mapbox ?](#heading-quest-ce-que-mapbox)
* [Partie 1 : Création d'un style Mapbox personnalisé](#heading-partie-1-creation-dun-style-mapbox-personnalise)
* [Partie 2 : Ajout d'une couche de tuiles personnalisée à React Leaflet](#heading-partie-2-ajout-dune-couche-de-tuiles-personnalisee-a-react-leaflet)
* [Partie 3 : Ajout d'un fond de carte personnalisé à Gatsby Starter Leaflet](#heading-partie-3-ajout-dun-fond-de-carte-personnalise-a-gatsby-starter-leaflet)
* [Sécurisation de votre clé Mapbox](#heading-securisation-de-votre-cle-mapbox)
* [Vous voulez en savoir plus sur les cartes ?](#heading-vous-voulez-en-savoir-plus-sur-les-cartes)

%[https://www.youtube.com/watch?v=KcPJr1b_rv0]

## Qu'allons-nous construire ?

Nous allons créer un nouveau style de base [Mapbox](https://www.mapbox.com/mapbox-studio/) dans notre compte [Mapbox](https://www.mapbox.com/). Une fois créé, nous allons utiliser leur [API Map](https://docs.mapbox.com/api/maps/) pour ajouter un fond de carte personnalisé à notre application [React Leaflet](https://react-leaflet.js.org/).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/gatsby-starter-leaflet-with-mapbox-tilelayer.jpg)
_Gatsby Starter Leaflet avec fond de carte Mapbox_

Pour notre carte, nous allons utiliser ce [Leaflet Gatsby Starter](https://github.com/colbyfayock/gatsby-starter-leaflet) que j'ai créé et qui vous permettra de lancer facilement une nouvelle application de cartographie. Avant de le lancer, je vais vous montrer comment l'ajouter en utilisant uniquement des composants React Leaflet.

## Une application de cartographie ?

Oui ! Les cartes sont utilisées dans le monde entier pour étudier des ensembles de données pour des localisations géographiques. Elles sont des outils importants pour les scientifiques et autres personnes qui essaient d'aider le monde.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-map-dashboard-demo.jpg)
_Carte personnalisée du Coronavirus (COVID-19)_

Si vous souhaitez en savoir plus sur la création d'une carte et l'ajout de données, vous pouvez consulter certains de [mes autres articles](https://www.freecodecamp.org/news/author/colbyfayock/) tels que la création d'une [carte du Coronavirus (COVID-19)](https://www.freecodecamp.org/news/how-to-create-a-coronavirus-covid-19-dashboard-map-app-in-react-with-gatsby-and-leaflet/) ou d'une [carte de voyage estival](https://www.freecodecamp.org/news/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet/) ainsi qu'un peu d'inspiration sur pourquoi [Tout le monde peut cartographier](https://www.freecodecamp.org/news/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping/).

## Qu'est-ce que Mapbox ?

Mapbox est une plateforme de cartographie qui permet à ses clients de créer des solutions de cartographie personnalisées. Ils exploitent également une variété d'API qui offrent des capacités puissantes pour construire des fonctionnalités de carte.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-homepage.jpg)
_[mapbox.com](https://www.mapbox.com/)_

Pour nos besoins, nous allons utiliser leur API Map, spécifiquement leur API Static Tiles, pour servir un style de carte personnalisé que nous créons.

## Partie 1 : Création d'un style Mapbox personnalisé

Pour obtenir l'apparence que nous voulons pour notre carte, il est important d'avoir un fond de carte qui aide à présenter nos données sans distractions. De plus, parfois il est amusant d'avoir une carte personnalisée.

### Compte Mapbox

La première chose dont nous avons besoin pour configurer notre style Mapbox personnalisé est d'avoir un compte. Je ne vais pas vous guider à travers ce processus, mais vous pouvez vous rendre sur le site de [Mapbox](https://www.mapbox.com/) où vous pouvez vous inscrire gratuitement : [mapbox.com](https://www.mapbox.com/)

### Création d'un nouveau style personnalisé

Créer un nouveau style dans Mapbox n'est pas aussi difficile que cela en a l'air. Bien que cela puisse devenir très complexe si vous voulez quelque chose d'unique, nous pouvons copier l'un des styles par défaut de Mapbox pour commencer.

Tout d'abord, rendez-vous sur le [tableau de bord Studio](https://studio.mapbox.com/) de Mapbox en cliquant sur le lien de votre compte dans le coin supérieur droit lorsque vous êtes connecté.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-studio.jpg)
_Mapbox Studio_

Une fois sur notre tableau de bord Studio, nous voulons sélectionner le bouton Nouveau Style.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-studio-new-style.jpg)
_Créer un nouveau style dans Mapbox Studio_

Après avoir cliqué sur le bouton, une fenêtre modale s'ouvrira vous permettant de choisir un modèle. Vous pouvez choisir ce que vous voulez ici, mais je vais choisir Monochrome avec une variation de Dark. Et après avoir sélectionné votre modèle, cliquez sur le bouton Personnaliser.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-studio-new-style-choose-template.jpg)
_Sélectionner et personnaliser un modèle pour un nouveau style dans Mapbox Studio_

Et maintenant nous sommes redirigés vers notre interface de personnalisation.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-customize-style.jpg)
_Interface de personnalisation de style Mapbox_

À partir de là, vous pouvez vraiment faire ce que vous voulez. Il y a une tonne d'options pour personnaliser votre carte. C'est un peu complexe d'essayer de creuser ici, mais [Mapbox fournit quelques ressources](https://docs.mapbox.com/studio-manual/overview/) pour essayer de vous aider à être productif.

### Génération d'un jeton Mapbox

Une fois que vous êtes satisfait de votre nouveau style et que tout est publié, nous voulons générer un jeton que nous utiliserons pour fournir l'accès à notre Carte.

Rendez-vous dans la section Compte du tableau de bord Mapbox.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-account.jpg)
_Création d'un nouveau jeton dans Mapbox_

Mapbox vous fournit un jeton "par défaut" que vous pouvez utiliser dans vos applications. Vous êtes libre de l'utiliser, mais je recommande de créer un nouveau jeton que vous pouvez nommer de manière unique, de sorte que si vous dépassez un jour le [niveau gratuit](https://www.mapbox.com/pricing/) de Mapbox, vous pourrez suivre votre utilisation.

De plus, il est préférable de garder un jeton séparé pour chaque application, de sorte que vous pouvez facilement faire tourner une clé individuelle, sans avoir à mettre à jour chaque application l'utilisant.

Une fois que vous cliquez sur Créer un jeton, vous pouvez configurer la clé comme vous le souhaitez, avec les portées et permissions que vous choisissez, mais pour nos besoins, vous pouvez laisser toutes les portées Publiques cochées pour notre carte, ce qu'ils font par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-create-token.jpg)
_Créer un nouveau jeton d'accès dans Mapbox_

### Configuration de notre point de terminaison personnalisé

Pour ce tutoriel, nous allons utiliser le [service Static Tiles de Mapbox](https://docs.mapbox.com/api/maps/#static-tiles).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-static-tiles-map-api.jpg)
_API Maps Static Tiles de Mapbox_

Notre point de terminaison ressemblera à ce qui suit :

```
https://api.mapbox.com/styles/v1/{username}/{style_id}/tiles/256/{z}/{x}/{y}@2x?access_token={access_token}
```

Il y a quelques paramètres ici que nous devons comprendre :

* username : ce sera le nom d'utilisateur de votre compte Mapbox
* style_id : ce sera l'ID du style que vous avez créé précédemment
* z, x, y : ce sont des paramètres que Leaflet échange de manière programmatique, donc nous voulons les laisser tels quels
* access_token : c'est la clé Mapbox que vous avez créée ci-dessus

Pour trouver votre nom d'utilisateur et votre ID de style, nous pouvons utiliser l'URL du style pour notre nouveau style Mapbox pour obtenir ces valeurs.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mapbox-studio-style-url.jpg)
_Trouver l'URL du style dans Mapbox Studio_

Dans mon exemple, mon URL de style ressemble à ceci :

```
mapbox://styles/colbyfayock/ck8lryjfq0jdo1ip9ctmuhc6p
```

`colbyfayock` est mon nom d'utilisateur et `ck8lryjfq0jdo1ip9ctmuhc6p` est mon ID de style.

Et une fois que j'ai mis à jour les paramètres de mon point de terminaison, l'URL finale du point de tuile ressemblera à ceci :

```
https://api.mapbox.com/styles/v1/colbyfayock/ck8lryjfq0jdo1ip9ctmuhc6p/tiles/256/{z}/{x}/{y}@2x?access_token=MYACCESSTOKEN
```

## Partie 2 : Ajout d'une couche de tuiles personnalisée à React Leaflet

Lors de la création d'une carte avec React Leaflet, votre composant principal sera un `<Map>` qui enveloppe l'intégralité de l'application. C'est ce qui configure votre [instance de carte](https://leafletjs.com/reference-1.6.0.html#map-example) pour [Leaflet](https://leafletjs.com/).

Pour nos besoins ici, nous allons utiliser l'exemple sur la [page d'accueil de React Leaflet](https://react-leaflet.js.org/) comme point de départ.

### Composant TileLayer de React Leaflet

À l'intérieur de votre composant `<Map>`, vous incluez un composant `<TileLayer>`, qui définit l'imagerie du monde sur laquelle vous basez votre carte.

L'exemple sur la page d'accueil de React Leaflet utilise une version publique de [OpenStreetMap](https://www.openstreetmap.org/) comme leur TileLayer, qui est un projet de carte open source créé et mis à jour par des personnes du monde entier.

```react
<Map center={position} zoom={13}>
  <TileLayer
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
  />
</Map>
```

Cela vous donne une carte de base, mais nous voulons remplacer par Mapbox afin de pouvoir configurer un look et une sensation personnalisés pour notre carte.

### TileLayer Mapbox personnalisé

Pour ajouter notre style personnalisé, nous allons vouloir mettre à jour les props `url` et `attribution` du composant `TileLayer`.

Pour l'URL, il s'agira simplement du point de terminaison du style personnalisé que nous avons créé précédemment, donc dans mon exemple, cela ressemble à ceci :

```
https://api.mapbox.com/styles/v1/colbyfayock/ck8lryjfq0jdo1ip9ctmuhc6p/tiles/256/{z}/{x}/{y}@2x?access_token=MYACCESSTOKEN
```

Pour l'attribution, nous voulons créditer Mapbox en tant que service, donc nous voulons définir notre attribution comme suit :

```
Map data &copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors, <a href=&quot;https://creativecommons.org/licenses/by-sa/2.0/&quot;>CC-BY-SA</a>, Imagery &copy; <a href=&quot;https://www.mapbox.com/&quot;>Mapbox</a>
```

Une fois intégré à notre `TileLayer`, notre code devrait maintenant ressembler à ceci :

```react
<Map center={position} zoom={13}>
  <TileLayer
    url="https://api.mapbox.com/styles/v1/colbyfayock/ck8lryjfq0jdo1ip9ctmuhc6p/tiles/256/{z}/{x}/{y}@2x?access_token=MYACCESSTOKEN"
    attribution="Map data &copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors, <a href=&quot;https://creativecommons.org/licenses/by-sa/2.0/&quot;>CC-BY-SA</a>, Imagery &copy; <a href=&quot;https://www.mapbox.com/&quot;>Mapbox</a>"
  />
</Map>
```

Et une fois que nous ouvrons notre carte, nous devrions voir notre nouveau fond de carte !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/react-leaflet-mapbox-basemap.jpg)
_React Leaflet avec un fond de carte Mapbox_

### Voir le code !

Si vous voulez voir comment je l'ai fait, [consultez le diff commit par commit](https://github.com/colbyfayock/my-mapbox-react-leaflet/commits/master).

Le seul bémol est que j'ai créé un fichier `.env.development.local` à la racine de mon projet dans lequel j'ai stocké une nouvelle variable d'environnement appelée `REACT_APP_MAPBOX_KEY` pour stocker ma clé Mapbox.

## Partie 3 : Ajout d'un fond de carte personnalisé à Gatsby Starter Leaflet

J'ai écrit [quelques](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet) [autres](https://www.colbyfayock.com/2020/03/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet) [articles](https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping/) sur [comment commencer](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/) avec mon [Leaflet Gatsby Starter](https://github.com/colbyfayock/gatsby-starter-leaflet), mais pour cette partie, nous allons vouloir avoir une application de base lancée que nous pouvons utiliser pour changer notre point de terminaison `TileLayer`.

### Configuration de notre application Gatsby React Leaflet

Pour commencer, consultez les instructions sur le github du Starter :

[https://github.com/colbyfayock/gatsby-starter-leaflet](https://github.com/colbyfayock/gatsby-starter-leaflet)

Une fois que vous êtes prêt, vous devriez avoir une application de cartographie de base prête à l'emploi !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/gatsby-starter-leaflet-in-browser.jpg)
_Nouvelle application Leaflet Gatsby dans le navigateur_

### Configuration de notre service Mapbox

La première chose que nous allons vouloir faire est d'ajouter Mapbox en tant que service dans notre fichier `src/data/map-services.js`.

En prenant notre URL de point de terminaison personnalisé que nous avons créé dans la Partie 1, configurons un nouvel objet avec un nom de Mapbox, et avec une URL et une attribution similaires à ce que nous avons fait dans la Partie 2.

```js
export const mapServices = [
  {
    name: 'OpenStreetMap',
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
  },
  {
    name: 'Mapbox',
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery &copy; <a href="https://www.mapbox.com/">Mapbox</a>',
    url: `https://api.mapbox.com/styles/v1/colbyfayock/ck8c2foj72lqk1jnug0g2haw0/tiles/256/{z}/{x}/{y}@2x?access_token=MY_ACCESS_TOKEN`
  }
];
```

### Utilisation de notre service de carte Mapbox

Une fois que vous avez configuré votre service Mapbox, il ne reste plus qu'à ouvrir le fichier `src/pages/index.js`, trouver la définition de l'objet `mapSettings` et mettre à jour la propriété `defaultBaseMap` en `Mapbox`.

```js
const mapSettings = {
  center: CENTER,
  defaultBaseMap: 'Mapbox',
  zoom: DEFAULT_ZOOM,
  mapEffect
};
```

Enregistrez cette modification, actualisez la carte dans votre navigateur et vous devriez maintenant voir votre style de fond de carte personnalisé !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/gatsby-starter-leaflet-with-mapbox-tilelayer-in-browser.jpg)
_Gatsby Starter Leaflet avec fond de carte Mapbox personnalisé dans le navigateur_

### Voir le code !

Si vous voulez voir comment je l'ai fait, [consultez le diff avec le commit](https://github.com/colbyfayock/my-mapbox-gatsby-starter-leaflet/commit/9baa1b7003504dec5c938328ea9b54477f65ec58).

Le seul bémol est que j'ai créé un fichier `.env.development` à la racine de mon projet dans lequel j'ai stocké une nouvelle variable d'environnement appelée `GATSBY_MAPBOX_KEY` pour stocker ma clé Mapbox.

## Sécurisation de votre clé Mapbox

### Variables d'environnement

Une partie de la plupart des processus de développement qui utilisent des clés individuelles configurera généralement les clés en tant que variables d'environnement. Les variables d'environnement sont des paramètres configurés qui ne vivent pas dans le code lui-même.

Cela est important car cela empêche votre clé d'être enregistrée dans votre code, ce qui est mauvais d'un point de vue sécurité, mais cela vous permet également de fournir une clé différente pour différents environnements.

Lors de la génération de vos clés, essayez de garder cela à l'esprit, car cela peut vous sauver à long terme.

### Verrouillage de votre clé Mapbox

Dans vos paramètres lors de la création d'un jeton ou lors de la modification d'un jeton, Mapbox vous permet de spécifier uniquement les URL auxquelles vous souhaitez que votre clé soit accessible.

Bien que Mapbox ait un niveau gratuit généreux, vous voulez probablement le garder verrouillé uniquement aux URL que vous utilisez. Vous pouvez créer plusieurs clés, où une pourrait être pour un usage public sur votre site web et une autre pour votre développement local.

Cela est utile par exemple, où vous avez une clé qui ne sera jamais utilisée publiquement à des fins de développement, mais ensuite vous avez une clé que vous déployez, qui peut être verrouillée uniquement à cette URL.

Si quelqu'un récupère votre clé, il pourrait la brancher sur son propre site web et utiliser tout votre niveau gratuit, potentiellement en augmentant votre facture !

## Vous voulez en savoir plus sur les cartes ?

Vous pouvez consulter quelques-unes de mes autres ressources pour commencer :

* [Comment créer un tableau de bord et une application de carte Coronavirus (COVID-19) en React avec Gatsby et Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet)
* [Tout le monde peut cartographier ! Inspiration et introduction au monde de la cartographie](https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping)
* [Comment créer une application de cartographie de voyage estival avec Gatsby et Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet)
* [Comment créer votre propre traqueur du Père Noël avec Gatsby et React Leaflet](https://www.colbyfayock.com/2019/12/create-your-own-santa-tracker-with-gatsby-and-react-leaflet/)
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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f3a8 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>
---
title: Comment créer une application de suivi du Père Noël avec Next.js et React Leaflet
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2022-12-21T16:42:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-santa-tracker-app-with-next-js-react-leaflet
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/santa-tracking-map-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment créer une application de suivi du Père Noël avec Next.js et React
  Leaflet
seo_desc: "It's the holiday season and Santa's coming! But just like he watches all\
  \ of us, we can build a map-based tracking app to keep an eye on him and find out\
  \ when he'll come on Christmas night with Next.js and React Leaflet.\n\n  \n   \
  \ How can we track Santa..."
---

C'est la saison des fêtes et le Père Noël arrive ! Mais tout comme il nous observe tous, nous pouvons créer une application de suivi basée sur une carte pour le surveiller et découvrir quand il viendra la nuit de Noël avec Next.js et React Leaflet.

<ul>
  <li>
    <a href="#comment-peut-on-suivre-le-pere-noel">Comment peut-on suivre le Père Noël ?</a>
  </li>
  <li>
    <a href="#comment-creer-une-carte">Comment créer une carte ?</a>
  </li>
  <li>
    <a href="#quest-ce-que-nous-allons-construire">Qu'est-ce que nous allons construire ?</a>
  </li>
  <li>
    <a href="#etape-0-creation-dune-nouvelle-application-nextjs-a-partir-du-starter-nextjs-leaflet">Étape 0 : Création d'une nouvelle application Next.js à partir du Starter Next.js Leaflet</a>
  </li>
  <li>
    <a href="#etape-1-recuperation-des-donnees-du-pere-noel-avec-swr">Étape 1 : Récupération des données du Père Noël avec SWR</a>
  </li>
  <li>
    <a href="#etape-2-affichage-des-etapes-du-pere-noel-sur-une-carte-avec-les-marqueurs-react-leaflet">Étape 2 : Affichage des étapes du Père Noël sur une carte avec les marqueurs React Leaflet</a>
  </li>
  <li>
    <a href="#etape-3-ajustement-des-dates-et-heures-darrivee-et-de-depart-du-pere-noel-pour-lannee-en-cours">Étape 3 : Ajustement des dates et heures d'arrivée et de départ du Père Noël pour l'année en cours</a>
  </li>
  <li>
    <a href="#etape-4-mise-a-jour-des-marqueurs-avec-des-icones-personnalisees">Étape 4 : Mise à jour des marqueurs avec des icônes personnalisées</a>
  </li>
  <li>
    <a href="#etape-5-affichage-de-lendroit-ou-se-trouve-le-pere-noel-et-ou-il-est-passe-en-comparant-les-dates-et-heures">Étape 5 : Affichage de l'endroit où se trouve le Père Noël et où il est passé en comparant les dates et heures</a>
  </li>
</ul>

%[https://www.youtube.com/watch?v=kklt5gDs6Qw]

## Comment peut-on suivre le Père Noël ?

Les personnes qui vous ont apporté le [suivi du Père Noël de Google](https://github.com/google/santa-tracker-web) dans les années passées ont créé un [point de terminaison non officiel](https://firebasestorage.googleapis.com/v0/b/santa-tracker-firebase.appspot.com/o/route%2Fsanta_en.json?alt=media&2018b) qui vous donne une liste de destinations où le Père Noël s'arrête pour distribuer des cadeaux.

Bien qu'il y ait une chance qu'ils le désactivent soudainement, il fonctionne bien depuis 2019. Il y a donc de bonnes chances qu'il reste en ligne (j'ai également [sauvegardé les données dans un Gist](https://gist.github.com/colbyfayock/79bbaf5991dc776fb0db53fddb99db58) 👀).

Mais avec ces données, nous pouvons ajouter des points sur une carte indiquant les lieux où le Père Noël s'arrêtera, ainsi que s'il s'y est déjà arrêté ou non.

## Comment créer une carte ?

Nous allons utiliser [React Leaflet](https://react-leaflet.js.org/), qui est un wrapper autour de la populaire bibliothèque de cartographie [Leaflet](https://leafletjs.com/).

La bibliothèque nous permet de créer une carte et d'ajouter de nombreux types différents de visuels comme des données, des images, ou elle peut même créer des cartes personnalisées de mondes de science-fiction si vous êtes suffisamment avancé.

Mais nous allons utiliser cela pour créer notre carte de suivi du Père Noël.

## Qu'est-ce que nous allons construire ?

Nous allons construire une application de suivi du Père Noël qui nous donne une carte avec toutes les destinations. Elle nous indiquera si le Père Noël s'y est arrêté, s'il s'y trouve actuellement, et s'il est déjà reparti.

Nous allons le faire dans Next.js en utilisant un Starter que j'ai créé appelé Next.js Leaflet Starter. Cela nous donnera notre carte de base que nous pourrons utiliser pour être productifs dans React Leaflet.

## Étape 0 : Création d'une nouvelle application Next.js à partir du Starter Next.js Leaflet

Nous allons commencer par une nouvelle application Next.js en utilisant le [Next.js Leaflet Starter](https://github.com/colbyfayock/next-leaflet-starter). Cela nous permettra de démarrer rapidement avec une carte de base que nous pourrons commencer à utiliser.

Dans votre terminal, exécutez :

```other
yarn create next-app -e https://github.com/colbyfayock/next-leaflet-starter mon-application-de-suivi-du-pere-noel
# ou
npx create-next-app -e https://github.com/colbyfayock/next-leaflet-starter mon-application-de-suivi-du-pere-noel

```

Note : n'hésitez pas à utiliser une valeur différente de `mon-application-de-suivi-du-pere-noel` comme nom de votre projet !

Une fois l'installation terminée, vous pouvez naviguer vers ce répertoire.

```other
cd mon-application-de-suivi-du-pere-noel

```

Ensuite, vous pouvez démarrer votre serveur de développement local avec :

```other
yarn dev
# ou
npm run dev

```

Et une fois que vous le visitez dans votre navigateur à l'adresse [http://localhost:3000](http://localhost:3000), nous devrions voir notre nouvelle application :

![Nouvelle application avec carte du Starter Next.js Leaflet](https://www.freecodecamp.org/news/content/images/2022/12/nextjs-leaflet-starter.jpg)
_Next.js Leaflet Starter_

Si nous prenons un moment pour explorer le projet, nous nous intéressons principalement à la page d'accueil gérée dans `src/pages/index.js` pour ce tutoriel. Là, avec quelques composants d'interface utilisateur de base, nous avons une carte.

La carte est construite en enveloppant la carte React Leaflet avec un [Import Dynamique de Next.js](https://nextjs.org/docs/advanced-features/dynamic-import). Le problème avec Leaflet et React Leaflet est qu'il nécessite l'objet window du navigateur pour fonctionner. Nous utilisons donc l'Import Dynamique pour le charger uniquement lorsqu'il atteint le client.

Mais dans la page d'accueil, nous pouvons voir comment nous utilisons actuellement notre carte, ainsi que quelques composants d'introduction, ce qui nous permettra de commencer à construire notre application de suivi !

## Étape 1 : Récupération des données du Père Noël avec SWR

Pour obtenir nos données sur le Père Noël, nous devons les récupérer depuis notre API.

Bien que nous pourrions techniquement utiliser fetch et les stocker dans l'état, utilisons [SWR](https://swr.vercel.app/) qui nous donne un moyen un peu plus propre de gérer cette requête.

Dans votre terminal, installez d'abord SWR avec :

```other
yarn add swr
# ou
npm install swr

```

Ensuite, importons-le dans notre projet.

En haut de `src/pages/index.js`, ajoutez :

```other
import useSWR from 'swr';

```

Et pour utiliser notre nouveau hook SWR, nous avons deux parties, où d'abord nous définissons notre fonction "fetch", qui est essentiellement la logique de requête abstraite.

Au-dessus du composant de la page d'accueil, ajoutez :

```other
const fetcher = (url) => fetch(url).then((res) => res.json());

```

Et ensuite nous pouvons configurer la requête elle-même à l'intérieur, en haut de notre composant de la page d'accueil :

```other
const { data } = useSWR(
  'https://firebasestorage.googleapis.com/v0/b/santa-tracker-firebase.appspot.com/o/route%2Fsanta_en.json?alt=media&2018b',
  fetcher
);

```

Pour revoir rapidement ce qui se passe, nous utilisons le hook useSWR qui nous donnera quelques fonctionnalités de récupération de données (mise en cache, révalidation). Mais nous devons dire à SWR 2 choses : comment récupérer les données (fetcher) et où (notre endpoint).

Et avec cela, nous devrions avoir nos données, que nous pouvons maintenant tester en ajoutant un journal de console. Là, lorsque nous chargeons notre page et que nous regardons dans la console, nous devrions voir une série de destinations enregistrées :

![Navigateur montrant la page avec la carte et la console de développement avec les données de destination du Père Noël](https://www.freecodecamp.org/news/content/images/2022/12/santa-destination-data.jpg)
_Destinations du Père Noël_

[Suivez le commit !](https://github.com/colbyfayock/my-santa-tracking-app/commit/e9afb6f224744195c6a1118a0aab639770da26b6)

## Étape 2 : Affichage des étapes du Père Noël sur une carte avec les marqueurs React Leaflet

Nous avons les futures étapes du Père Noël ! Maintenant, plaçons-les sur la carte.

Si nous faisons défiler jusqu'à notre composant Map, nous devrions voir que nous imbriquons deux composants :

* Tilelayer : c'est l'arrière-plan, l'imagerie réelle de la carte
* Marker : la épingle qui est placée sur la carte (et un Popup à l'intérieur)

Ce sont des composants abstraits en tant que composants React, donc comme tout autre composant React, nous pouvons parcourir nos données en ajoutant un nouveau Marker pour chaque arrêt.

Remplaçons le composant Marker par :

```other
{data?.destinations?.map(({ id, location, city, region }) => {
  return (
    <Marker key={id} position={[location.lat, location.lng]}>
      <Popup>{ city }, { region }</Popup>
    </Marker>
  )
})}

```

Si nous rechargeons la page, nous verrons... la même chose.

![Carte montrant une épingle sur Washington, DC](https://www.freecodecamp.org/news/content/images/2022/12/map-marker-washington-dc.jpg)
_Toujours montrant Washington, DC_

Mais cela est trompeur. Zoomez sur la carte et nous verrons toutes nos épingles :

![Carte montrant des épingles sur le nord-est des États-Unis](https://www.freecodecamp.org/news/content/images/2022/12/map-markers-santa-locations-united-states.jpg)
_Zoomez pour montrer les épingles_

Nous pouvons même cliquer sur chacune de ces épingles, où nous verrons l'emplacement puisque nous l'avons ajouté dans un Popup.

![Carte montrant un popup ouvert sur Buenos Aires, Argentine](https://www.freecodecamp.org/news/content/images/2022/12/map-marker-popup-buenos-aires-argentina.jpg)
_Gagnant de la Coupe du Monde 2022 avec un popup d'emplacement !_

Tout fonctionne bien jusqu'à présent, mais nous ne voulons pas que les gens doivent zoomer à chaque fois, alors corrigeons cela.

Sur le composant Map, nous pouvons voir une propriété `center` et une propriété `zoom` :

* Center : l'emplacement par défaut pour centrer la carte
* Zoom : le niveau de zoom avec lequel la carte commence

Rendons-les plus appropriés pour notre projet :

```other
<Map ... center={[0, 0]} zoom={1}>

```

Cela le placera au centre du monde avec un niveau de zoom de 1, ce qui nous permet de voir le monde entier.

![Carte avec des épingles sur des villes du monde entier](https://www.freecodecamp.org/news/content/images/2022/12/world-map-markers-santa-locations.jpg)
_Carte montrant des épingles partout dans le monde_

Maintenant, en dernier lieu, au lieu de montrer uniquement le nom de l'emplacement, ajoutons quand le Père Noël arrivera.

Mettez à jour l'instruction de la carte pour les destinations avec :

```other
{data?.destinations?.map(({ id, arrival, departure, location, city, region }) => {
  const arrivalDate = new Date(arrival);
  const arrivalHours = arrivalDate.getHours()
  const arrivalMinutes = arrivalDate.getMinutes()
  const arrivalTime = `${arrivalHours}:${arrivalMinutes}`;

  const departureDate = new Date(departure);
  const departureHours = departureDate.getHours()
  const departureMinutes = departureDate.getMinutes()
  const departureTime = `${departureHours}:${departureMinutes}`;
  
  return (
    <Marker key={id} position={[location.lat, location.lng]}>
      <Popup>
        <strong>Emplacement :</strong> { city }, { region }
        <br />
        <strong>Arrivée :</strong> { arrivalDate.toDateString() } @ { arrivalTime }
        <br />
        <strong>Départ :</strong> { arrivalDate.toDateString() } @ { departureTime }
      </Popup>
    </Marker>
  )
})}

```

Ici nous :

* Utilisons les heures d'arrivée et de départ pour créer de nouvelles dates
* Obtenons des valeurs spécifiques pour la date et l'heure
* Formatons l'heure
* Ajoutons les dates et heures d'arrivée et de départ au Popup

Et lorsque nous rechargeons la page et cliquons sur une épingle, nous devrions voir toutes nos informations !

![Carte montrant un popup ouvert sur l'épingle de l'Ukraine](https://www.freecodecamp.org/news/content/images/2022/12/map-marker-arrival-depature-ukraine-santa.jpg)
_Destination du Père Noël en Ukraine_

[Suivez le commit !](https://github.com/colbyfayock/my-santa-tracking-app/commit/5ef0edea4c8ff3fe01fd40326c5c001dcc06411d)

## Étape 3 : Ajustement des dates et heures d'arrivée et de départ du Père Noël pour l'année en cours

Rebondissement ! L'API que nous utilisons pour charger les destinations du Père Noël montre actuellement 2019 😱.

![Carte mettant en évidence la date de 2019 dans le Popup](https://www.freecodecamp.org/news/content/images/2022/12/map-marker-highlighted-old-date-3.jpg)
_Le Père Noël est dans le passé !_

Il s'avère qu'après 2019, Google a cessé de mettre à jour cette API. Mais ce n'est pas grave, les horaires et les lieux restent les mêmes, nous devons simplement les corriger pour l'année en cours, ce que nous pouvons faire dynamiquement pour également préparer cela pour l'avenir.

En haut du composant de la page d'accueil et sous la requête SWR, obtenons d'abord la date et l'heure actuelles :

```other
const currentDate = new Date(Date.now());
const currentYear = currentDate.getFullYear();

```

Ensuite, nous pouvons créer un nouvel ensemble "corrigé" de destinations :

```other
const destinations = data?.destinations.map((destination) => {
  const { arrival, departure } = destination;

  const arrivalDate = new Date(arrival);
  const departureDate = new Date(departure);

  arrivalDate.setFullYear(currentYear);
  departureDate.setFullYear(currentYear);

  return {
    ...destination,
    arrival: arrivalDate.getTime(),
    departure:  departureDate.getTime(),
  }
});

```

Ici nous :

* Parcourons chaque destination, créant finalement un nouveau tableau de `destinations`
* Obtenons les dates d'arrivée et de départ dans un nouvel objet Date
* Utilisons notre valeur `currentYear` pour ajuster notre arrivée et notre départ
* Retournons toutes les données de destination avec les valeurs mises à jour

Enfin, comme dernière étape, nous devons mettre à jour le code qui crée nos Markers de `data?.destinations?.map` à :

```other
{destinations?.map(({ id, arrival, departure, location, city, region }) => {

```

Et si nous ouvrons notre application.

![Carte montrant un popup ouvert avec l'année en cours](https://www.freecodecamp.org/news/content/images/2022/12/map-marker-popup-2022.jpg)
_Popups avec la date correcte !_

Nous devrions maintenant voir que tous nos popups ont la bonne date.

[Suivez le commit !](https://github.com/colbyfayock/my-santa-tracking-app/commit/e4126ad9e428b18f50d2509c539236bbdfaa8133)

## Étape 4 : Mise à jour des Markers avec des icônes personnalisées

Actuellement, nous utilisons les graphiques par défaut qui viennent avec React Leaflet pour nos Markers, mais nous pouvons faire mieux.

Nous pouvons fournir nos propres images personnalisées qui remplaceront le marqueur, y compris quelque chose de fun comme des sapins de Noël !

Pour vous aider, j'ai créé une image pour cela, que vous pouvez récupérer ici :

![Icône de sapin de Noël @2x](https://www.freecodecamp.org/news/content/images/2022/12/tree-marker-icon-2x.png)
_2x : [https://github.com/colbyfayock/my-santa-tracking-app/blob/main/public/images/tree-marker-icon-2x.png](https://github.com/colbyfayock/my-santa-tracking-app/blob/main/public/images/tree-marker-icon-2x.png)_

![Icône de sapin de Noël @1x](https://www.freecodecamp.org/news/content/images/2022/12/tree-marker-icon.png)
_1x : [https://github.com/colbyfayock/my-santa-tracking-app/blob/main/public/images/tree-marker-icon.png](https://github.com/colbyfayock/my-santa-tracking-app/blob/main/public/images/tree-marker-icon.png)_

Note : vous pouvez utiliser les images que vous voulez, vous devrez simplement vous assurer d'ajuster les tailles et d'utiliser les bons noms de fichiers.

Tout d'abord, placez vos images à l'intérieur du répertoire `public/images` pour les rendre disponibles pour nous.

Ensuite, nous allons dire à notre Marker que nous voulons utiliser notre icône personnalisée.

Pour commencer, nous devons rendre la bibliothèque Leaflet disponible pour l'utiliser dans notre composant Map :

```other
<Map className={styles.homeMap} width="800" height="400" center={[0, 0]} zoom={1}>
  {({ TileLayer, Marker, Popup }, Leaflet) => (

```

Ici, nous ajoutons la variable `Leaflet` comme deuxième argument à notre fonction prop.

Ensuite, nous devons l'utiliser pour créer notre icône en utilisant une instance Leaflet Icon.

À l'intérieur de notre map `destinations`, mettez à jour la balise d'ouverture Marker à :

```other
<Marker
  key={id}
  position={[location.lat, location.lng]}
  icon={Leaflet.icon({
    iconUrl: '/images/tree-marker-icon.png',
    iconRetinaUrl: '/images/tree-marker-icon-2x.png',
    iconSize: [41, 41]
  })}
>

```

Ici, nous ajoutons une nouvelle prop `icon` à notre Marker où nous créons une nouvelle icône Leaflet ainsi que le chemin vers nos icônes.

Nous spécifions également la taille car nous fournissons des images carrées par opposition aux images rectangulaires qui sont là par défaut.

Et juste comme ça, nous avons maintenant des marqueurs de sapins de Noël !

![Carte montrant les emplacements du Père Noël avec des marqueurs de sapins de Noël](https://www.freecodecamp.org/news/content/images/2022/12/map-santa-locations-christmas-trees.jpg)
_Icônes de marqueurs de sapins de Noël !_

Mais nous pouvons aller plus loin et montrer où se trouve le Père Noël avec une icône personnalisée ainsi que là où il est déjà passé avec une autre icône personnalisée, ce que nous ferons à l'étape suivante.

[Suivez le commit !](https://github.com/colbyfayock/my-santa-tracking-app/commit/8e44f8c9bae9e83a0e99d5c4e27575017f7d947a)

## Étape 5 : Affichage de l'endroit où se trouve le Père Noël et où il est passé en comparant les dates et heures

Précédemment, nous avons configuré nos icônes personnalisées pour toutes les étapes du Père Noël.

Nous pouvons aller plus loin et utiliser les heures d'arrivée et de départ du Père Noël pour déterminer s'il se trouve actuellement à un endroit et s'il était à un endroit, puis afficher différentes icônes.

Cela inclura quelques étapes :

* Déterminer si le Père Noël "est ici" et "était ici"
* Ajouter et afficher différentes icônes
* Fausser l'heure actuelle pour tester que cela fonctionne

Pour commencer, déterminons où se trouve actuellement le Père Noël.

Pour chaque destination, nous avons notre heure d'arrivée et de départ, que nous utilisons déjà dans le Popup. Nous pouvons comparer ces valeurs à l'heure actuelle pour déterminer où il se trouve.

À l'intérieur de la map des destinations et juste avant l'instruction return (sous les variables de temps) ajoutez :

```other
const santaWasHere = currentDate.getTime() - departureDate.getTime() > 0;
const santaIsHere = currentDate.getTime() - arrivalDate.getTime() > 0 && !santaWasHere;

```

Ici nous déterminons :

* Si le Père Noël **était** ici – essentiellement si l'heure actuelle est postérieure à l'heure de départ
* Si le Père Noël **est** ici – essentiellement si l'heure actuelle est postérieure à l'heure d'arrivée ET le Père Noël n'est pas encore parti (le ci-dessus est faux)

Ensuite, nous devons définir dynamiquement les URL de nos icônes pour utiliser de nouvelles icônes à différents moments.

Pour ce faire, nous avons besoin de nouvelles images. Heureusement, je vous les fournis à nouveau !

![Icône de cadeau @2x](https://www.freecodecamp.org/news/content/images/2022/12/gift-marker-icon-2x.png)
_Cadeau 2x : https://github.com/colbyfayock/my-santa-tracking-app/blob/main/public/images/gift-marker-icon-2x.png_

![Icône de cadeau @1x](https://www.freecodecamp.org/news/content/images/2022/12/gift-marker-icon.png)
_Cadeau 1x : https://github.com/colbyfayock/my-santa-tracking-app/blob/main/public/images/gift-marker-icon.png_

![Icône du Père Noël @2x](https://www.freecodecamp.org/news/content/images/2022/12/santa-marker-icon-2x.png)
_Père Noël 2x : https://github.com/colbyfayock/my-santa-tracking-app/blob/main/public/images/santa-marker-icon-2x.png_

![Icône du Père Noël @1x](https://www.freecodecamp.org/news/content/images/2022/12/santa-marker-icon.png)
_Père Noël 1x : https://github.com/colbyfayock/my-santa-tracking-app/blob/main/public/images/santa-marker-icon.png_

Comme avant, nous voulons déposer les quatre images dans le répertoire `public/images`.

Note : encore une fois, vous pouvez utiliser différentes images si vous le souhaitez, mais assurez-vous de faire attention à la taille et aux noms de fichiers.

Avec nos images, nous pouvons configurer notre URL d'image dynamique.

Tout d'abord, créons une variable pour stocker ces informations :

```other
let iconUrl = '/images/tree-marker-icon.png';
let iconRetinaUrl = '/images/tree-marker-icon-2x.png';

```

Et mettons à jour notre prop `icon` Marker pour utiliser ces variables :

```other
<Marker
  key={id}
  position={[location.lat, location.lng]}
  icon={Leaflet.icon({
    iconUrl,
    iconRetinaUrl,
    iconSize: [41, 41]
  })}
>

```

En mettant tout cela ensemble, nous pouvons vérifier nos comparaisons de temps et définir l'URL en fonction de cela :

```other
if ( santaIsHere ) {
  iconUrl = '/images/santa-marker-icon.png';
  iconRetinaUrl = '/images/santa-marker-icon-2x.png';
}

if ( santaWasHere ) {
  iconUrl = '/images/gift-marker-icon.png';
  iconRetinaUrl = '/images/gift-marker-icon-2x.png';
}

```

Si nous ouvrons la carte, nous remarquerons que nous avons un problème. Ce n'est pas encore Noël, alors comment savons-nous si cela va fonctionner ?

Nous pouvons fausser l'heure pour vérifier !

En haut du composant Home, commentons notre `currentDate` et définissons-le à une valeur statique :

```other
// const currentDate = new Date(Date.now());
const currentDate = new Date('2022-12-25T02:34:30.115Z');

```

Si nous regardons notre carte :

![Carte montrant des cadeaux là où le Père Noël est déjà passé](https://www.freecodecamp.org/news/content/images/2022/12/map-gifts-trees-santa-locations.jpg)
_Tant de cadeaux !_

Nous devrions maintenant voir que parce que nous avons défini l'heure à 25 déc à 2:34:30 UTC, qui est le 24 déc vers 21h34 EST, nous devrions voir que le Père Noël a commencé à distribuer des cadeaux dans la plupart du monde, mais pas encore sur la côte est des États-Unis.

Maintenant, un petit problème, avez-vous trouvé le Père Noël ?

![Père Noël couvert par une icône d'arbre sur la carte](https://www.freecodecamp.org/news/content/images/2022/12/santa-hiding-behind-tree.jpg)
_Père Noël !_

Le voilà ! Qui se cache derrière un arbre à Buenos Aires.

Ce n'est pas idéal, car le Père Noël est sans doute l'icône la plus importante, n'est-ce pas ?

Nous pouvons donc corriger cela avec un peu de CSS.

Similaire à notre URL d'icône, nous allons créer une nouvelle variable pour ajouter une classe dynamiquement à notre icône.

Tout d'abord, la variable className :

```other
let className = '';

if ( santaIsHere ) {
  className = `${className} ${styles.iconSantaIsHere}`;
}

```

Et ensuite nous appliquons cela à notre prop icon :

```other
<Marker
  key={id}
  position={[location.lat, location.lng]}
  icon={Leaflet.icon({
    iconUrl,
    iconRetinaUrl,
    iconSize: [41, 41],
    className
  })}
>

```

Ensuite, nous pouvons ouvrir `src/styles/Home.scss` et ajouter ce qui suit en bas :

```other
.iconSantaIsHere {
  z-index: 9999!important;
}

```

Et une fois que nous rechargeons la page, nous devrions maintenant voir le Père Noël au-dessus de toutes les icônes :

![Icône du Père Noël au-dessus de toutes les autres icônes sur la carte](https://www.freecodecamp.org/news/content/images/2022/12/santa-map-marker-zindex-fix.jpg)
_Père Noël clair sur la carte_

Avant de continuer...

**Important** : assurez-vous de mettre à jour votre variable `currentDate` à :

```other
const currentDate = new Date(Date.now());

```

Nous ne voulons pas être déçus lorsque le tracker ne... ne suit pas.

[Suivez le commit !](https://github.com/colbyfayock/my-santa-tracking-app/commit/09884333eb965b3130a22affe29e50bcaf8e6d35)

## Que pouvons-nous faire d'autre ?

J'espère que vous vous êtes amusés et que cela vous a mis dans l'esprit des fêtes ! Vous voulez passer à un autre niveau ? Voici quelques autres choses que vous pouvez faire.

### Rafraîchir l'heure pour mettre à jour l'emplacement du Père Noël

Lorsque vous chargez la page pour la première fois, nous obtenons une valeur `currentDate`, mais celle-ci ne sera pas mise à jour tout au long de la nuit.

Si vous souhaitez garder cette application ouverte et voir activement où le Père Noël se déplace, essayez de déplacer l'heure vers l'état React et définissez un intervalle qui la met à jour automatiquement toutes les quelques secondes, par exemple toutes les 30 secondes.

### Afficher l'emplacement du Père Noël s'il n'est pas à un arrêt

L'heure statique que j'ai utilisée pour tester où se trouvait le Père Noël était 2:34:30, ce qui n'était pas une coïncidence. Si je l'avais définie à 2:34:00, il ne se serait pas trouvé à un endroit, plutôt, il aurait été en train de se rendre à un endroit.

En utilisant ces informations, nous pouvons déterminer où se trouve le Père Noël en :

* Trouvant la dernière destination d'où le Père Noël est parti
* Trouvant la prochaine destination où le Père Noël arrivera
* Trouvant le milieu des deux emplacements géographiques (latitude et longitude)
* Ajoutant un Marker à cet endroit

Une façon est d'utiliser la bibliothèque JS Turf, qui, parmi beaucoup d'autres outils, vous permet de trouver le point médian entre deux emplacements :

[https://turfjs.org/docs/#midpoint](https://turfjs.org/docs/#midpoint)

### Personnaliser et styliser la carte

C'est Noël ! Nous ne voulons pas d'une carte et d'une application ennuyeuses.

Nous pouvons utiliser des outils comme Mapbox pour changer l'imagerie de la carte et CSS pour thématiser notre application.

Ce tutoriel est pour utiliser Mapbox avec Gatsby mais les concepts devraient généralement être les mêmes : [https://www.youtube.com/watch?v=KcPJr1b_rv0](https://www.youtube.com/watch?v=KcPJr1b_rv0).

### Ajouter le chemin du Père Noël pour savoir où il va ensuite

Nous voyons un tas d'emplacements, mais nous ne savons pas où le Père Noël va quand.

React Leaflet nous permet d'ajouter d'autres "formes" à la carte, comme un [Polyline](https://react-leaflet.js.org/docs/api-components/#polyline), où nous pouvons passer un tableau de points.

Le seul problème est qu'après avoir essayé cela, parce que notre ligne traverse l'Antiméridien, nous obtenons de grands zigzags sur notre carte.

Celui-ci sera un défi, mais essayez d'utiliser la bibliothèque Leaflet Antimeridian pour corriger ce problème :

[https://github.com/briannaAndCo/Leaflet.Antimeridian](https://github.com/briannaAndCo/Leaflet.Antimeridian)

Conseil : J'ai [implémenté cela dans Gatsby il y a quelques années](https://github.com/colbyfayock/santa-tracker/blob/1b231ed40c43abdeeeeaa57fa16a0fea684d8085/src/lib/santa.js#L70). Peut-être essayez de voir ce que j'ai fait là-bas, encore une fois, les concepts devraient être les mêmes.

## Partagez votre tracker avec moi !

Envoyez un Tweet avec un lien vers votre Santa Tracker déployé et mentionnez-moi [@colbyfayock](https://twitter.com/colbyfayock).

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;width:100%;justify-content:center;align-items:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;text-align:center;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">🐦 Follow On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">📺 Subscribe on Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">📬 Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>
---
title: Comment ajouter une playlist YouTube à une application Next.js React avec l'API
  YouTube
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-08-06T21:11:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-youtube-playlist-to-a-nextjs-react-app-with-the-youtube-api
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/youtube-api.jpg
tags:
- name: api
  slug: api
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment ajouter une playlist YouTube à une application Next.js React avec
  l'API YouTube
seo_desc: "YouTube gives content creators a ton of tools to add their work for everyone\
  \ to see. But those tools only help you manage the experience on YouTube. \nHow\
  \ can we utilize the YouTube API to bring our video content to our own website?\n\
  \nYouTube has an AP..."
---

YouTube offre aux créateurs de contenu une multitude d'outils pour ajouter leur travail afin que tout le monde puisse le voir. Mais ces outils ne vous aident qu'à gérer l'expérience sur YouTube. 

Comment pouvons-nous utiliser l'API YouTube pour intégrer notre contenu vidéo sur notre propre site web ?

* [YouTube a une API ?](#heading-youtube-a-une-api)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Commencer avec Next.js](#heading-etape-0-commencer-avec-nextjs)
* [Étape 1 : Créer un projet Google Developer](#heading-etape-1-creer-un-projet-google-developer)
* [Étape 2 : Demander des éléments de playlist à l'API YouTube](#heading-etape-2-demander-des-elements-de-playlist-a-lapi-youtube)
* [Étape 3 : Afficher les vidéos de la playlist YouTube sur la page](#heading-etape-3-afficher-les-videos-de-la-playlist-youtube-sur-la-page)

%[https://www.youtube.com/watch?v=8YWrmZoUYGs]

## YouTube a une API ?

Oui ! YouTube, ainsi que de nombreux autres services Google, [a une API](https://developers.google.com/youtube) que nous pouvons utiliser pour tirer parti de notre contenu en dehors de YouTube. Et l'API est assez complète.

Avec l'API de YouTube, vous pouvez faire des choses comme gérer vos vidéos, accéder aux analyses et gérer la lecture. Mais nous allons l'utiliser pour récupérer des vidéos d'une playlist afin de pouvoir les ajouter à une page.

## Que allons-nous construire ?

Nous allons créer une application [Next.js](https://nextjs.org/) qui utilise l'API YouTube pour récupérer des vidéos d'une playlist.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/youtube-playlist-app-demo.jpg)
_[Galerie de playlist de démonstration](https://demo-youtube-playlist.vercel.app/)_

Nous allons prendre ces vidéos et afficher leurs miniatures sur une page qui renvoie à la vidéo.

## Étape 0 : Commencer avec Next.js

Pour créer une application, nous allons utiliser Next.js. En utilisant yarn ou npm, nous pouvons facilement créer une nouvelle application qui nous permettra de plonger directement dans le code.

Pour commencer, naviguez vers l'endroit où vous souhaitez créer votre projet et exécutez :

```
yarn create next-app
# ou
npx create-next-app

```

Ce script vous demandera un nom de projet. Je vais utiliser « my-youtube-playlist », et il installera toutes les dépendances nécessaires pour commencer.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/command-line-new-nextjs-project.jpg)
_Création réussie d'une nouvelle application avec Next.js_

Ensuite, naviguez vers ce répertoire et exécutez `yarn dev` pour démarrer votre serveur de développement et nous sommes prêts à partir.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/new-nextjs-app.jpg)
_Page par défaut de Next.js_

[Suivez le commit !](https://github.com/colbyfayock/my-youtube-playlist/commit/f062c01111aa064c43111dad6a23812637ce1f92)

## Étape 1 : Créer un projet Google Developer

Pour utiliser l'API, nous allons avoir besoin d'un nouveau projet dans la console Google Developer qui nous permettra de générer une clé API pour utiliser le service.

Tout d'abord, rendez-vous sur : [https://console.developers.google.com/](https://console.developers.google.com/).

Une fois là-bas et connecté avec votre compte Google, nous allons vouloir créer un nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-developer-console-new-project.jpg)
_Création d'un nouveau projet dans Google Developer Console_

À ce stade, vous pouvez nommer votre projet comme vous le souhaitez. Je vais opter pour « Ma Playlist YouTube ». Ensuite, cliquez sur Créer.

Par défaut, Google ne vous placera pas dans le nouveau projet. Il lance un travail pour créer ce projet, mais une fois terminé, vous pouvez rouvrir le sélecteur de projet et sélectionner votre nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-developer-console-select-project.jpg)
_Sélection de votre projet_

Ensuite, nous voulons créer une clé API. Naviguez vers Credentials, cliquez sur Create Credentials, puis sélectionnez API key.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-create-api-key.jpg)
_Création d'une clé API credential_

Cela créera une nouvelle clé API que vous voudrez copier et sauvegarder pour plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-developer-api-key.jpg)
_Copie de votre nouvelle clé API_

_Note : Cette clé API doit être gardée secrète. Si vous l'exposez ou l'ajoutez quelque part accessible au public comme GitHub, d'autres peuvent en abuser et vous laisser avec une facture à payer._

Enfin, nous devons ajouter l'API YouTube en tant que service. Naviguez vers **Library** dans la barre latérale, recherchez « YouTube », puis sélectionnez **YouTube Data API v3**.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-youtube-data-api.jpg)
_Recherche de l'API YouTube dans la bibliothèque Google API_

Enfin, après le chargement de cette page, cliquez sur Enable, ce qui vous amènera à une nouvelle page de tableau de bord et vous serez prêt à partir.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-enable-youtube-data-api.jpg)
_Activation de YouTube Data API v3_

## Étape 2 : Demander des éléments de playlist à l'API YouTube

Pour demander nos données, nous allons utiliser la fonction [getServerSideProps](https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering).

Tout d'abord, ouvrez le fichier `pages/index.js` et ajoutez ce qui suit au-dessus du composant `Home`.

```js
const YOUTUBE_PLAYLIST_ITEMS_API = 'https://www.googleapis.com/youtube/v3/playlistItems';

export async function getServerSideProps() {
  const res = await fetch(`${YOUTUBE_PLAYLIST_ITEMS_API}`)
  const data = await res.json();
  return {
    props: {
      data
    }
  }
}

```

Voici ce que nous faisons :

* Nous créons une nouvelle constante qui stocke notre point de terminaison API
* Nous créons et exportons une nouvelle fonction `getServerSideProps`
* À l'intérieur de cette fonction, nous récupérons notre point de terminaison
* Nous transformons ensuite cela en JSON
* Enfin, nous retournons les données en tant que props dans notre objet

Maintenant, si nous déstructurons la prop `data` de `Home` et que nous affichons ces données comme suit :

```js
export default function Home({ data }) {
  console.log('data', data);

```

Nous pouvons maintenant voir que nous obtenons une erreur :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-invalid-key.jpg)
_Erreur de requête nécessitant une clé API_

Nous n'utilisons pas notre clé API, alors utilisons-la.

Créez un nouveau fichier à la racine du projet appelé `.env.local` et ajoutez le contenu suivant :

```
YOUTUBE_API_KEY="[API Key]"

```

Assurez-vous de remplacer `[API Key]` par votre clé API de l'Étape 1.

À ce stade, vous voudrez redémarrer votre serveur pour que Next.js puisse voir la nouvelle variable.

Maintenant, mettez à jour la fonction `getServerSideProps` pour ajouter votre clé à la requête API :

```js
export async function getServerSideProps() {
  const res = await fetch(`${YOUTUBE_PLAYLIST_ITEMS_API}?key=${process.env.YOUTUBE_API_KEY}`)

```

Et si nous rechargeons la page, nous obtenons à nouveau une erreur :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-missing-parameters.jpg)
_Erreur de requête nécessitant des paramètres API_

Maintenant, il nous manque l'ID de la playlist et les filtres que nous voulons utiliser pour récupérer nos données.

En utilisant les paramètres de l'[API des éléments de playlist](https://developers.google.com/youtube/v3/docs/playlistItems/list#request), mettons à jour notre point de terminaison API à nouveau :

```js
const res = await fetch(`${YOUTUBE_PLAYLIST_ITEMS_API}?part=snippet&maxResults=50&playlistId=[Playlist ID]&key=${process.env.YOUTUBE_API_KEY}`)

```

Ici, nous ajoutons :

* `part=snippet` : cela indique à l'API que nous voulons le snippet
* `maxResults=50` : cela définit le nombre maximum d'éléments de playlist qui sont retournés à 50
* `playlistId=[Playlist ID]` : cela ajoute le paramètre pour configurer l'ID de la playlist. Ici, vous devez mettre à jour cette valeur avec l'ID de la playlist de votre choix.

Note : vous pouvez trouver l'ID de la playlist dans l'URL de la playlist que vous souhaitez utiliser.

Et enfin, lorsque nous rechargeons la page, nous avons nos données :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-youtube-playlist-data.jpg)
_Requête réussie des éléments de playlist_

[Suivez le commit !](https://github.com/colbyfayock/my-youtube-playlist/commit/7ca0de9005303950fd1aac4442b8fba7b4b179a7)

## Étape 3 : Afficher les vidéos de la playlist YouTube sur la page

Maintenant que nous avons nos données, nous voulons les afficher.

Pour utiliser ce que nous avons déjà de Next.js, nous pouvons transformer la grille existante en une grille de miniatures YouTube.

Remplaçons l'ensemble de la `<div>` avec la classe `styles.grid` par :

```jsx
<ul className={styles.grid}>
  {data.items.map(({ id, snippet = {} }) => {
    const { title, thumbnails = {}, resourceId = {} } = snippet;
    const { medium } = thumbnails;
    return (
      <li key={id} className={styles.card}>
        <a href={`https://www.youtube.com/watch?v=${resourceId.videoId}`}>
          <p>
            <img width={medium.width} height={medium.height} src={medium.url} alt="" />
          </p>
          <h3>{ title }</h3>
        </a>
      </li>
    )
  })}
</ul>

```

Voici ce que nous faisons :

* Nous changeons la `<div>` en `<ul>` pour qu'elle soit plus sémantique
* Nous créons une carte à travers les éléments de notre playlist pour créer dynamiquement de nouveaux éléments
* Nous déstructurons nos données en récupérant l'id, le titre, la miniature et l'ID vidéo
* En utilisant l'ID, nous ajoutons une clé à notre `<li>`
* Nous déplaçons également la `className` de `styles.card` de `<a>` à `<li>`
* Pour notre lien, nous utilisons l'ID vidéo YouTube pour créer l'URL de la vidéo
* Nous ajoutons notre image miniature
* Nous utilisons notre `title` pour le `<h3>`

Et si nous rechargeons la page, nous pouvons voir que nos vidéos sont là, mais les styles sont un peu décalés.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/playlist-videos.jpg)
_Affichage des éléments de playlist sur la page_

Pour corriger cela, nous pouvons commencer par ajouter les styles suivants à `.grid` dans le fichier `Home.module.css` :

```css
list-style: none;
padding: 0;
margin-left: 0;

```

Nous pouvons également changer

```css
align-items: center;

```

en

```css
align-items: flex-start;

```

ce qui aidera à corriger l'alignement de nos vidéos.

Mais nous remarquerons que nous n'avons toujours pas deux colonnes comme dans la disposition originale de Next.js.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/playlist-videos-fixed-list.jpg)
_Suppression des styles de liste HTML par défaut_

Sous notre classe `.grid` que nous venons de mettre à jour, ajoutez ce qui suit :

```css
.grid img {
  max-width: 100%;
}

```

Cela garantit que toutes nos images ne dépassent pas le conteneur. Cela empêchera le débordement et permettra à nos images de s'installer en deux colonnes.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/playlist-videos-fixed-columns.jpg)
_Correction des tailles de colonnes_

Et cela nous donne nos vidéos de playlist.

[Suivez le commit !](https://github.com/colbyfayock/my-youtube-playlist/commit/5bc2d374ea706d3ad920a8568097e3dd6e30f568)

## Que pouvons-nous faire d'autre ?

### Intégrer un lecteur et afficher cette vidéo au clic

YouTube offre également des contrôles pour son propre lecteur. Ainsi, en utilisant un peu de JavaScript, nous pouvons en tirer parti et, lorsqu'une personne clique sur l'une de nos miniatures vidéo, nous pouvons afficher un lecteur intégré et lire cette vidéo.

[YouTube Player API Reference for iframe Embeds](https://developers.google.com/youtube/iframe_api_reference)

### Obtenir des données analytiques

Bien que YouTube fournisse certaines analyses dans son tableau de bord, peut-être voulez-vous quelque chose de plus avancé.

Vous pouvez utiliser les API Analytics et Reporting pour obtenir plus d'informations sur votre chaîne et vos vidéos.

[YouTube Analytics and Reporting APIs](https://developers.google.com/youtube/analytics)

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
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>
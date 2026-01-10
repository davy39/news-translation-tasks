---
title: Comment récupérer des données GraphQL dans Next.js avec Apollo GraphQL
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-12-01T16:22:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-fetch-graphql-data-in-next-js-with-apollo-graphql
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/apollo.jpg
tags:
- name: Apollo GraphQL
  slug: apollo
- name: data
  slug: data
- name: GraphQL
  slug: graphql
- name: Next.js
  slug: nextjs
seo_title: Comment récupérer des données GraphQL dans Next.js avec Apollo GraphQL
seo_desc: 'Next.js has been steadily growing as a must-have tool for developers creating
  React apps. Part of what makes it great is its data fetching APIs that request data
  for each page. But how can we use that API to make GraphQL queries for our app?


  What is...'
---

Next.js s'est progressivement imposé comme un outil indispensable pour les développeurs créant des applications React. Ce qui le rend si puissant, ce sont ses API de récupération de données qui permettent de demander des données pour chaque page. Mais comment pouvons-nous utiliser cette API pour effectuer des requêtes GraphQL pour notre application ?

* [Qu'est-ce que GraphQL ?](#heading-questcequegraphql)
* [Qu'est-ce qu'Apollo GraphQL ?](#heading-questcequapollographql)
* [Récupération de données dans Next.js](#heading-recuperationdedonneesdansnextjs)
* [Que allons-nous construire ?](#heading-queallonsnousconstruire)
* [Étape 0 : Création d'une nouvelle application Next.js](#heading-etape0creationdunenouvelleapplinationnextjs)
* [Étape 1 : Ajout d'Apollo GraphQL à une application Next.js](#heading-etape1ajoutdapollographqlaneapplicationnextjs)
* [Étape 2 : Ajout de données à une page Next.js avec getStaticProps](#heading-etape2ajoutdedonneesanepagenextjsavecgetstaticprops)
* [Étape 3 : Récupération de données avec une requête GraphQL dans Next.js en utilisant Apollo Client](#heading-etape3recuperationdedonneesavecanrequetegraphqlansnextjsenutilisantapolloclient)
* [Étape 4 : Ajout des données de lancement SpaceX à la page](#heading-etape4ajoutdesdonneesdelancementspacexalapage)

%[https://youtu.be/oxUPXhZ1t9I]

## Qu'est-ce que GraphQL ?

[GraphQL](https://graphql.org/) est un langage de requête et un runtime qui offre une manière différente d'interagir avec une API par rapport à ce à quoi on pourrait s'attendre avec une API REST traditionnelle.

Lors de la récupération de données, au lieu de faire une requête [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) à une URL pour obtenir ces données, les endpoints GraphQL prennent une « requête ». Cette requête consiste en les données que vous souhaitez obtenir, qu'il s'agisse d'un ensemble de données complet ou d'une partie limitée de celui-ci.

Si vos données ressemblent à ceci :

```
Movie {
  "title": "Sunshine",
  "releaseYear": "2007",
  "actors": [...],
  "writers": [...]
}

```

Et que vous souhaitez uniquement obtenir le titre et l'année de sortie, vous pourriez envoyer une requête comme celle-ci :

```
Movie {
  title
  releaseYear
} 

```

En ne récupérant que les données dont vous avez besoin.

Le plus intéressant est que vous pouvez également fournir des relations complexes entre les données. Avec une seule requête, vous pourriez également demander des données provenant de différentes parties de la base de données qui nécessiteraient traditionnellement plusieurs requêtes avec une API REST.

## Qu'est-ce qu'Apollo GraphQL ?

[Apollo GraphQL](https://www.apollographql.com/) est, à sa base, une implémentation GraphQL qui aide les gens à rassembler leurs données sous forme de graphe.

Apollo fournit et maintient également un client GraphQL, que nous allons utiliser, qui permet aux gens d'interagir de manière programmatique avec une API GraphQL.

En utilisant le client GraphQL d'Apollo, nous pourrons faire des requêtes à une API GraphQL de manière similaire à ce que nous attendrions avec un client de requête basé sur REST.

## Récupération de données dans Next.js

Lors de la récupération de données avec Next.js, vous avez plusieurs options pour la manière dont vous souhaitez récupérer ces données.

Tout d'abord, vous pourriez opter pour une approche côté client et faire la requête une fois la page chargée. Le problème avec cela est que vous mettez alors la charge sur le client pour prendre le temps de faire ces requêtes.

Les API Next.js comme `getStaticProps` et `getServerSideProps` vous permettent de collecter des données à différents moments du cycle de vie, nous donnant l'opportunité de [créer une application complètement statique](https://www.youtube.com/watch?v=6ElI2ZJ4Uro) ou une qui est rendue côté serveur. Cela servira les données déjà rendues à la page directement au navigateur.

En utilisant l'une de ces méthodes, nous pouvons demander des données avec nos pages et injecter ces données en tant que props directement dans notre application.

## Que allons-nous construire ?

Nous allons créer une application Next.js qui affiche les derniers lancements de SpaceX.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/spacex-launches-demo.jpg)
_Démonstration des lancements SpaceX_

Nous utiliserons l'API maintenue par [SpaceX Land](https://spacex.land/) pour faire une requête GraphQL qui récupère les 10 derniers vols. En utilisant [getStaticProps](https://nextjs.org/docs/basic-features/data-fetching#getstaticprops-static-generation), nous ferons cette requête au moment de la construction, ce qui signifie que notre page sera rendue statiquement avec nos données.

## Étape 0 : Création d'une nouvelle application Next.js

En utilisant Create Next App, nous pouvons rapidement créer une nouvelle application Next.js que nous pouvons utiliser pour commencer à plonger dans le code.

Dans votre terminal, exécutez la commande :

```
npx create-next-app my-spacex-launches

```

_Note : vous n'êtes pas obligé d'utiliser `my-spacex-app`, n'hésitez pas à remplacer cela par le nom que vous souhaitez donner au projet._

Après avoir exécuté ce script, Next.js configurera un nouveau projet et installera les dépendances.

Une fois terminé, vous pouvez démarrer votre serveur de développement :

```
cd my-spacex-launches
npm run dev

```

Cela démarrera un nouveau serveur à l'adresse [http://localhost:3000](http://localhost:3000) où vous pouvez maintenant visiter votre nouvelle application !

![Image](https://www.freecodecamp.org/news/content/images/2020/11/new-nextjs-app-1.jpg)
_Nouvelle application Next.js_

## Étape 1 : Ajout d'Apollo GraphQL à une application Next.js

Pour commencer à faire une requête GraphQL, nous aurons besoin d'un client GraphQL. Nous utiliserons le client Apollo GraphQL pour faire nos requêtes au serveur GraphQL de SpaceX.

De retour dans le terminal, exécutez la commande suivante pour installer nos nouvelles dépendances :

```
npm install @apollo/client graphql

```

Cela ajoutera le client Apollo ainsi que GraphQL, dont nous aurons besoin pour former la requête GraphQL.

Et une fois l'installation terminée, nous serons prêts à commencer à utiliser Apollo Client.

[Suivez avec le commit !](https://github.com/colbyfayock/my-spacex-launches/commit/0fcc3a0141e7bfb795c3c91c355fdfc459a17332)

## Étape 2 : Ajout de données à une page Next.js avec getStaticProps

Avant de récupérer des données avec Apollo, nous allons configurer notre page pour pouvoir demander des données puis passer ces données en tant que prop à notre page au moment de la construction.

Définissons une nouvelle fonction en bas de la page sous notre composant `Home` appelée `getStaticProps` :

```
export async function getStaticProps() {
  // Le code ira ici
}

```

Lorsque Next.js construit notre application, il sait chercher cette fonction. Donc lorsque nous l'exportons, nous informons Next.js que nous voulons exécuter du code dans cette fonction.

À l'intérieur de notre fonction `getStaticProps`, nous allons finalement retourner nos props à la page. Pour tester cela, ajoutons ce qui suit à notre fonction :

```
export async function getStaticProps() {
  return {
    props: {
      launches: []
    }
  }
}

```

Ici, nous passons une nouvelle prop `launches` et la définissons comme un tableau vide.

Maintenant, de retour à l'intérieur de notre composant `Home`, ajoutons un nouvel argument destructuré qui servira de prop ainsi qu'une instruction `console.log` pour tester notre nouvelle prop :

```
export default function Home({ launches }) {
  console.log('launches', launches);

```

Si nous rechargeons la page, nous pouvons voir que nous enregistrons maintenant notre nouvelle prop `launches` qui inclut un tableau vide comme nous l'avons défini.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-console-log-launches-array.jpg)
_Enregistrement de la prop launches_

Le plus intéressant est que, étant donné que la fonction `getStaticProps` que nous créons est asynchrone, nous pouvons faire n'importe quelle requête que nous souhaitons (y compris une requête GraphQL) et la retourner en tant que props à notre page, ce que nous ferons ensuite.

[Suivez avec le commit !](https://github.com/colbyfayock/my-spacex-launches/commit/868a4f6b31200cd2407b4aa2fe37a243fc235932)

## Étape 3 : Récupération de données avec une requête GraphQL dans Next.js en utilisant Apollo Client

Maintenant que notre application est prête à ajouter des props à la page et que nous avons installé Apollo, nous pouvons enfin faire une requête pour récupérer nos données SpaceX.

Ici, nous allons utiliser le client Apollo, qui nous permettra d'interfacer avec le serveur GraphQL de SpaceX. Nous ferons notre requête à l'API en utilisant la méthode getStaticProps de Next.js, ce qui nous permettra de créer dynamiquement des props pour notre page lors de sa construction.

Tout d'abord, importons nos dépendances Apollo dans le projet. En haut de la page, ajoutez :

```
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

```

Cela inclura le client Apollo lui-même, `InMemoryCache` qui permet à Apollo d'optimiser en lisant depuis le cache, et `gql` que nous utiliserons pour former notre requête GraphQL.

Ensuite, pour utiliser le client Apollo, nous devons configurer une nouvelle instance de celui-ci.

À l'intérieur du haut de la fonction `getStaticProps`, ajoutez :

```
const client = new ApolloClient({
  uri: 'https://api.spacex.land/graphql/',
  cache: new InMemoryCache()
});

```

Cela crée une nouvelle instance de client Apollo en utilisant l'endpoint de l'API SpaceX que nous allons utiliser pour interroger.

Avec notre client, nous pouvons enfin faire une requête. Ajoutez le code suivant sous le client :

```
const { data } = await client.query({
  query: gql`
    query GetLaunches {
      launchesPast(limit: 10) {
        id
        mission_name
        launch_date_local
        launch_site {
          site_name_long
        }
        links {
          article_link
          video_link
          mission_patch
        }
        rocket {
          rocket_name
        }
      }
    }
  `
});

```

Cela fait plusieurs choses :

* Crée une nouvelle requête GraphQL à l'intérieur de la balise `gql`
* Crée une nouvelle requête en utilisant `client.query`
* Utilise `await` pour s'assurer qu'il termine la requête avant de continuer
* Et enfin, déstructure `data` à partir des résultats, qui est là où les informations dont nous avons besoin sont stockées

À l'intérieur de la requête GraphQL, nous disons à l'API SpaceX que nous voulons obtenir `launchesPast`, qui sont les lancements précédents de SpaceX, et nous voulons obtenir les 10 derniers (limite). À l'intérieur de cela, nous définissons les données que nous aimerions interroger.

Si nous prenons un moment pour ajouter une nouvelle instruction de journalisation de la console après cela, nous pouvons voir à quoi ressemble `data`.

Une fois que vous avez actualisé la page, vous remarquerez que vous ne voyez rien dans la console du navigateur.

`getStaticProps` s'exécute pendant le processus de construction, ce qui signifie qu'il s'exécute dans Node. Pour cette raison, nous pouvons regarder à l'intérieur de notre terminal et voir nos logs là-bas :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/logging-static-props-terminal.jpg)
_Journalisation des données dans le terminal_

Après avoir vu cela, nous savons qu'à l'intérieur de l'objet `data`, nous avons une propriété appelée `launchesPast`, qui inclut un tableau de détails de lancement.

Maintenant, nous pouvons mettre à jour notre instruction de retour pour utiliser `launchesPast` :

```
return {
  props: {
    launches: data.launchesPast
  }
}

```

Et si nous ajoutons notre instruction `console.log` en haut de la page pour voir à quoi ressemble notre prop `launches`, nous pouvons voir que nos données de lancement sont maintenant disponibles en tant que prop pour notre page :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/logging-static-props-web-console.jpg)
_Journalisation des props dans la console web_

[Suivez avec le commit !](https://github.com/colbyfayock/my-spacex-launches/commit/f273bcde3d2baccd54e4c65930ab499dbe4862ed)

## Étape 4 : Ajout des données de lancement SpaceX à la page

Maintenant, la partie excitante !

Nous avons nos données de lancement que nous avons pu demander avec Apollo Client au serveur GraphQL de SpaceX. Nous avons fait cette requête dans `getStaticProps` afin de rendre nos données disponibles en tant que prop `launches` qui contient nos données de lancement.

En creusant dans la page, nous allons profiter de ce qui existe déjà. Par exemple, nous pouvons commencer par mettre à jour la balise `h1` et le paragraphe en dessous pour quelque chose qui décrit un peu mieux notre page.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/updated-page-title.jpg)
_Titre de la page mis à jour_

Ensuite, nous pouvons utiliser les cartes de liens déjà existantes pour inclure toutes nos informations de lancement.

Pour ce faire, ajoutons d'abord une instruction [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) à l'intérieur de la grille de la page, où le composant que nous retournons est l'une des cartes, avec les détails de lancement remplis :

```
<div className={styles.grid}>
  {launches.map(launch => {
    return (
      <a key={launch.id} href={launch.links.video_link} className={styles.card}>
        <h3>{ launch.mission_name }</h3>
        <p><strong>Date de lancement :</strong> { new Date(launch.launch_date_local).toLocaleDateString("fr-FR") }</p>
      </a>
    );
  })}

```

Nous pouvons également nous débarrasser du reste des cartes Next.js par défaut, y compris Documentation et Learn.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/list-of-spacex-launches.jpg)
_Page avec les lancements SpaceX_

Notre page inclut maintenant les 10 derniers lancements de SpaceX ainsi que la date de chaque lancement !

Nous pouvons même cliquer sur l'une de ces cartes, et comme nous avons lié le lien vidéo, nous pouvons maintenant voir la vidéo du lancement.

[Suivez avec le commit !](https://github.com/colbyfayock/my-spacex-launches/commit/e35ed076253e3648fa5d8cd62e993e4e9e436396)

## Qu'est-ce qui suit ?

À partir de là, nous pouvons inclure des données supplémentaires de notre tableau `launches` sur notre page. L'API inclut même des images de patchs de mission, que nous pouvons utiliser pour afficher de belles graphiques pour chaque lancement.

Vous pouvez même ajouter des données supplémentaires à la requête GraphQL. Chaque lancement a beaucoup d'informations disponibles, y compris l'équipage de lancement et plus de détails sur la fusée.

[https://api.spacex.land/graphql/](https://api.spacex.land/graphql/)



<div id="colbyfayock-author-card">
  <p style="margin: 1em 0;">
    <a href="https://jamstackhandbook.com/" style="display: block;">
      <img src="https://www.freecodecamp.org/news/content/images/size/w1600/2020/11/jamstack-handbook-banner.jpg" alt="Jamstack Handbook" style="width:100%;display: block;margin: 0;border: solid 1px #d2dee9;">
    </a>
  </p>
</div>

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">F426 Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">F4FA Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">F4EB Inscrivez-vous à ma newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">F49D Sponsorisez-moi</a>
    </li>
  </ul>
</div>
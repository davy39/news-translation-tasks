---
title: GraphQL pour les développeurs front-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-19T17:19:00.000Z'
originalURL: https://freecodecamp.org/news/graphql-for-front-end-developers
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/Getting-Started-in-GraphQL-for-front-end-developers--1-.png
tags:
- name: apollo client
  slug: apollo-client
- name: Front-end Development
  slug: front-end-development
- name: GraphQL
  slug: graphql
seo_title: GraphQL pour les développeurs front-end
seo_desc: "By Gaurav Tewari\nIf you are a front end developer who is new to the world\
  \ of GraphQL and you're thinking about getting started with it, this article is\
  \ for you. \nIn this article, we will explore GraphQL basics and kick start our\
  \ journey with it by bu..."
---

Par Gaurav Tewari

Si vous êtes un développeur front-end qui découvre le monde de GraphQL et que vous envisagez de commencer à l'utiliser, cet article est fait pour vous.

Dans cet article, nous allons explorer les bases de GraphQL et démarrer notre voyage avec lui en construisant un projet simple.

## Qu'est-ce que GraphQL ?

GraphQL est un langage de requête qui permet aux applications de récupérer des données à partir des API. Mais ce qu'il fait différemment, c'est qu'il permet aux clients de spécifier comment structurer les données lorsqu'elles sont retournées par le serveur. Cela signifie que le client ne demande que les données dont il a besoin et spécifie même le format dans lequel il a besoin des données.

Mais quel problème résout-il réellement ?

Il résout le problème de la sous-récupération et de la sur-récupération. D'accord, mais qu'est-ce que c'est ? Eh bien, laissez-moi vous expliquer.

Supposons que vous deviez afficher uniquement un nom d'utilisateur, une image d'utilisateur et un nom sur la page de profil de votre site web ou de votre application. Mais lorsque vous demandez les données, vous obtenez beaucoup d'autres informations sur l'utilisateur dont vous n'avez pas besoin.

Cela s'appelle la **sur-récupération** – vous récupérez beaucoup de données, même celles dont vous n'avez pas besoin. D'autre part, la **sous-récupération** se produit lorsque nous obtenons moins de données que nécessaire. Aucune des deux situations n'est idéale.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/sketch1634455883941.png)
_exemple de sous-récupération_

Vous pourriez penser que ce n'est pas un problème du tout. Eh bien, ce n'est pas un gros problème dans les applications à petite échelle. Mais qu'en est-il des applications à grande échelle qui ont des millions d'utilisateurs ? Dans ces cas, la sur-récupération et la sous-récupération gaspillent beaucoup de ressources, c'est là que GraphQL intervient.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/d666aceb-62c2-4482-9c42-cbd12d2d42b6.png)

# Comment commencer avec GraphQL

Ici, nous allons couvrir quelques concepts clés que vous devez connaître avant de commencer avec GraphQL.

### GraphQL PlayGround

GraphQL Playground est un IDE graphique interactif pour GraphQL où vous pouvez explorer visuellement le serveur. Vous pouvez y tester diverses requêtes GraphQL et voir leurs résultats en temps réel.

[Voici un lien vers GraphQL Playground que vous pouvez consulter.](https://graphqlpokemon.favware.tech/)

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-17-at-1.57.04-PM.png)
_GraphQL Playground_

Si vous cliquez sur le bouton de lecture, il exécutera la requête.

### Comment demander, écrire ou publier des données dans GraphQL ?

Vous demandez des données via une requête dans GraphQL. Et pour écrire ou publier des données, vous utilisez des mutations.

Chaque fois que nous effectuons une opération GraphQL, nous spécifions si c'est une mutation ou une requête. Ensuite, nous nommons cette opération, et c'est la manière de base d'effectuer une requête GraphQL.

```

GraphQLOperatoinType Name {
 ....
 ........
 .....
 ...
}

```

Pour faire une simple requête, la syntaxe serait :

```
query getData {
...
}
```

De même, pour ajouter une mutation, nous écririons `mutation` à la place de `query`.

Maintenant que nous connaissons les bases, mettons les mains dans le cambouis. Nous allons utiliser l'[API Anilist](https://studio.apollographql.com/sandbox/explorer?endpoint=https%3A%2F%2Fgraphql.anilist.co&explorerURLState=N4IgJg9gxgrgtgUwHYBcQC4TADpIAR4AKAhgOYJ474F6JgCWxluNNAzvSggKoBOANi1Z4UnfhSrCayUv3psAFkKlJiogG4JlNAL7aCYBGyi96AB1EQk2vdVs6QAGhDrip4gCNxbDFmy9cBx0gA&_gl=1*1sgkza2*_ga*MTg1Mzg5MTM4Ni4xNjM0MjExNTMz*_ga_0BGG5V2W2K*MTYzNDM2NTQxMS43LjEuMTYzNDM2ODk5Ny4w) pour obtenir une liste de séries d'anime.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-17-at-2.25.53-PM.png)
_Apollo Studio_

### Comment utiliser Apollo Studio

Vous avez eu un petit aperçu de GraphQL Playground, mais il y a quelque chose de encore plus génial appelé Apollo Studio. Il facilite la vie en tant que développeur front-end. Dans celui-ci, vous devez simplement sélectionner les champs que vous voulez et il écrit une requête pour vous.

À partir du côté gauche, sélectionnez les champs que vous voulez dans votre requête, et c'est tout. GraphQL créera automatiquement une requête pour vous. Maintenant que vous avez fait la requête, comment l'utiliser dans votre application ?

Eh bien, commençons à construire une simple application Anime avec celle-ci.

Nous utiliserons React dans ce projet, mais vous pouvez choisir n'importe quel framework ou bibliothèque que vous souhaitez.

Tout d'abord, créez un nouveau projet dans React :

```
npx create-react-app graphql-example

```

Une fois le projet créé, allez dans le répertoire du projet et installez le client Apollo.

```
npm install graphql @apollo/client

```

Une fois cela fait, allez dans src/index.js et importez ApolloClient, InMemoryCache et ApolloProvider :

```javascript
import {ApolloClient, InMemoryCache, ApolloProvider} from '@apollo/client';
```

Apollo Client est une classe qui représente le client Apollo lui-même, et nous l'utilisons pour créer une nouvelle instance de client.

Ici, nous devons lui fournir quelques éléments. L'un est l'URI où nous spécifions l'URL de notre serveur GraphQL. De plus, chaque instance de notre client Apollo a besoin d'un cache pour réduire les requêtes réseau et rendre notre application beaucoup plus rapide.

Voici à quoi ressemble notre nouveau client :

```javascript
const client = new ApolloClient({
  uri : 'https://graphql.anilist.co/',
  cache: new InMemoryCache(),
})
```

Maintenant, nous devons rendre ce client disponible dans tout notre arbre de composants, alors nous enveloppons le composant de niveau supérieur de notre application dans ApolloProvider.

Maintenant que nous avons terminé la configuration initiale, il est temps de faire une requête et de demander à notre API les données – mais comment faire cela ?

Nous pouvons le faire en utilisant le hook useQuery. Mais avant cela, nous devons définir une requête, que nous pouvons faire en utilisant GQL (nous devons envelopper notre requête à l'intérieur). Alors maintenant, importez ces deux éléments depuis le client Apollo :

```
import {useQuery, gql} from '@apollo/client';

```

Après les avoir importés, nous envelopperons notre requête à l'intérieur de GQL :

```
 const AnimeList = gql`
 query Query {
  Page {
    media {
      siteUrl
      title {
        english
        native
      }
      description
      coverImage {
        medium
      }
      bannerImage
      volumes
      episodes
    }
  }
}
}



`;


```

À ce stade, vous devez vous demander si la partie requête est terminée, comment obtenons-nous les données maintenant ?

C'est là que le hook useQuery devient pratique. Il retourne les propriétés `loading`, `error` et `data` que nous pouvons utiliser.

```
  const {loading, error, data} = useQuery(AnimeList);

```

Pour l'instant, nous pouvons simplement afficher les données pour vérifier si notre application fonctionne ou non :

```
if(loading) return(<> Loading</>);
  if(error) return(<>{JSON.stringify(error)}</>)
  return (
   <>
   {JSON.stringify(data)}
   </>);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-16-at-5.42.06-PM.png)

Eh bien, cela fonctionne pour l'instant – il est temps de le styliser.

Peut-être pouvons-nous utiliser l'enchaînement d'objets pour l'implémenter proprement :

```
 <div className="container"> 
     <h1> 🐈 Liste d'Anime </h1>
     <hr width="80%" />
   {data?.Page?.media.map(anime => (
     <>
   <div className="card" >
      <img    src={anime.coverImage.medium}/>
      <div> 
         <h1>{anime.title.english} </h1>
           <div className="episodes" >Épisodes  <b>{anime.episodes} </b></div>
          <div  dangerouslySetInnerHTML={{__html: anime.description}} ></div> 
      </div> 
  </div>
  <hr width="75%"/>
 </>
   ))}
   <div className="buttonContainer">
    { page != 1 && <button> Page Précédente</button> } 
     <div className="pageText"> {page}</div>
     <button onClick={NextPage}>  Page Suivante </button> 
   </div>
   </div>);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-17-at-6.02.20-PM.png)
_application stylisée minimaliste_

Vous pouvez consulter ce [dépôt GitHub pour le fichier CSS](https://github.com/tewarig/graphql-Example/blob/7df5c7c199878484e36742287e513d5a249b466b/src/App.css).

Maintenant, nous sommes en mesure d'obtenir une liste de films d'anime à partir de l'API. Alors, que devons-nous faire pour les obtenir à partir de la page suivante de l'application ?

Nous devons passer une variable qui a un nom de page dans la requête. C'est là que les variables dans GraphQL entrent en jeu.

Tout d'abord, allez dans Apollo Studio et cliquez sur les arguments du côté gauche (allez d'abord à root > query > page et vous le verrez) :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-17-at-6.06.58-PM.png)

Cliquez sur page et il ajoutera un argument à votre requête.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-17-at-6.09.46-PM.png)

Remarquez également que dans la variable page dans la section des variables, vous pouvez changer sa valeur et jouer un peu avec. Mais les données ne changeront que selon la page.

Maintenant, nous devons passer cette variable dans la requête – et ensuite nous pourrons afficher les anime de la page suivante dans notre application.

Pour cela, nous utiliserons le hook useState pour suivre la valeur de notre page actuelle. Nous devons également faire une fonction pour incrémenter et décrémenter celle-ci.

```
  const [page, setPage] = useState(1);
  //c'est ainsi que nous passerons la page dans la requête.
  const {loading, error, data} = useQuery(AnimeList , {  variables: { "page" : page } });

const NextPage = () => {
    setPage(page+1);
  }
  const PreviousPage = () => {
    setPage(page - 1);
  }
  
   <div className="buttonContainer">
    { page != 1 && <button onClick={PreviousPage}> Page Précédente</button> } 
     <div className="pageText"> {page}</div>
     <button onClick={NextPage}>  Page Suivante </button> 
   </div>
  
```

Et maintenant, nous avons terminé la construction de notre application simple avec GraphQL. Si vous souhaitez consulter le code source, [voici le lien](https://github.com/tewarig/graphql-Example).

## Conclusion

Dans cet article, nous avons couvert certains des concepts de base pour vous aider à commencer à utiliser GraphQL. Merci d'avoir lu, et bon codage.
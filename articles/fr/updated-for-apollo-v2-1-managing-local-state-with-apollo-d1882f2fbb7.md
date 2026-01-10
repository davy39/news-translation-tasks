---
title: Comment utiliser les nouveaux composants Query d'Apollo pour gérer l'état local
subtitle: ''
author: Andrico Karoulla
co_authors: []
series: null
date: '2018-06-04T07:52:49.000Z'
originalURL: https://freecodecamp.org/news/updated-for-apollo-v2-1-managing-local-state-with-apollo-d1882f2fbb7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CMxI-q0DAMtcF-VGs10G0Q.jpeg
tags:
- name: Apollo GraphQL
  slug: apollo
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment utiliser les nouveaux composants Query d'Apollo pour gérer l'état
  local
seo_desc: 'Note: This article deals with utilizing Apollo’s brand new Query and Mutation
  components, instead of the HOCs. For those that have read the original article here,
  be aware that the two articles are very similar.

  Introduction

  One of Web Development’s ...'
---

Note : Cet article traite de l'utilisation des tout nouveaux composants Query et Mutation d'Apollo, au lieu des HOCs. Pour ceux qui ont lu l'article original [ici](https://itnext.io/managing-local-state-with-apollo-client-3be522258645), sachez que les deux articles sont très similaires.

### Introduction

L'une des plus grandes forces  et faiblesses  du développement Web est son approche de la modularité. Un mantra clé de la programmation est de choisir quelque chose (une fonction, un package) pour faire un seul travail et le faire bien. L'inconvénient de cette approche est qu'un seul projet peut impliquer de jongler avec des dizaines de technologies et de concepts séparés, chacun se concentrant sur quelque chose de spécifique.

Ainsi, choisir Apollo Client pour gérer mon état local ainsi que mes données distantes semble être une évidence. Pourquoi traiter avec le code standard et les idiomes de Redux lorsque j'ai déjà configuré Apollo/GraphQL pour obtenir des données de mon backend ?

Bien que cet article va traiter de la configuration d'Apollo pour gérer l'état local, il ne sera pas une introduction à la technologie. (Ce tutoriel légitime [howtographql](https://www.howtographql.com/) est un bon point de départ pour cela).

Note : Le dépôt finalisé peut être trouvé [ici](https://github.com/andrico1234/apollo-local-state-starter). Vous pouvez parcourir le code si vous êtes bloqué ou si vous vous sentez confus.

### Installation

Nous allons commencer par cloner le dépôt correspondant depuis [ici](https://github.com/andrico1234/apollo-state-blog-repo). Ce dépôt contient un simple site web react, avec une barre latérale, un en-tête et un corps. Il est assez statique par nature, pas de contenu dynamique ( encore). À la fin de ce tutoriel, nous aurons Apollo qui gère l'état du site web. Cliquer sur un élément de la barre latérale changera l'état du site web, ce qui mettra à jour l'en-tête pour afficher les nouvelles données.

Si vous vérifiez `package.json`, vous verrez que nous n'avons que les bases, plus quelques packages supplémentaires concernant notre configuration de parcel.

Après avoir cloné le dépôt, exécutez vos commandes standard dans votre interface de ligne de commande.

```
> yarn
> yarn dev
```

Pour installer tous vos packages et pour créer un serveur local, allez sur localhost:1234 et vous verrez, espérons-le, le site web de démonstration dans toute sa gloire. Il est statique pour le moment, donc cliquer autour ne fera rien.

Ce que nous voulons faire en premier lieu est d'obtenir Apollo dans notre projet, donc installez ces packages. `apollo-client` nous permet de configurer notre instance d'Apollo, et `react-apollo` est le pilote qui nous permet de l'intégrer dans notre application React. En raison d'un problème avec parcel (je pense), nous devrons également installer `graphql`.

```
> yarn add apollo-client react-apollo graphql
```

Créez un nouveau répertoire `src/apollo`, ouvrez un fichier `index.js` et ajoutez ce qui suit :

```js
import ApolloClient from 'apollo-client';
export const client = new ApolloClient({});
```

Cela initialise notre Apollo Client, que nous utiliserons ensuite pour envelopper notre application React en ajoutant ce qui suit à l'intérieur de notre fichier `src/index.js`.

```js
import { ApolloProvider } from 'react-apollo';
import { client } from './apollo';

const WrappedApp = (
  <ApolloProvider client={client} >
    <App />
  </ApolloProvider>
);

ReactDOM.render(WrappedApp, document.getElementById('root'));
// Ne soyez pas un sapin. Enveloppez votre application.
```

Nous avons maintenant Apollo prêt à être utilisé dans notre application. Tout se construit lorsque nous redémarrons notre serveur de développement, mais nous obtenons une erreur lorsque nous essayons d'y accéder dans le navigateur. La console nous dira que nous devons spécifier les propriétés de lien et de cache pour notre client Apollo, alors faisons cela.

```
> yarn add apollo-link apollo-cache-inmemory apollo-link-state
```

La ligne précédente ajoute les nouvelles dépendances Apollo à notre application tandis que le code suivant résout les erreurs de console que nous avions. Donc, retournez à `apollo/index.js` et mettez-le à jour pour que le fichier ressemble à ceci :

```js
import ApolloClient from 'apollo-client';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { ApolloLink } from 'apollo-link';
import { withClientState } from 'apollo-link-state';

const cache = new InMemoryCache();
const stateLink = withClientState({
  cache
});

export const client = new ApolloClient({
  cache,
  link: ApolloLink.from([
    stateLink,
  ]),
})
```

Créons une instance de notre cache. Le cache est le magasin de données normalisé d'Apollo qui stocke les résultats de la requête dans une structure de données aplatie. Nous lirons dans le cache lorsque nous ferons notre requête GraphQL, et nous écrirons dans le cache lorsque nous ferons notre résolveur de mutation.

Vous pouvez voir que nous avons également ajouté `link` à notre objet client. La méthode `ApolloLink.from()` nous permet de configurer de manière modulaire comment nos requêtes sont envoyées via HTTP. Nous pouvons utiliser cela pour gérer les erreurs et l'autorisation, et pour fournir l'accès à notre backend. Nous ne ferons rien de tout cela dans le tutoriel, mais nous configurerons notre état client ici. Donc, nous créons `const stateLink` ci-dessus et passons notre cache. Nous ajouterons notre état par défaut et nos résolveurs ici plus tard.

En revenant au navigateur, vous verrez notre joli site statique s'afficher dans toute sa magnificence. Ajoutons un peu d'état par défaut à notre projet et lançons notre première requête.

À l'intérieur du répertoire Apollo, créez un nouveau répertoire appelé `defaults` et ajoutez un `index.js` à l'intérieur. Le fichier contiendra ce qui suit :

```js
export default {
  apolloClientDemo: {
    __typename: 'ApolloClientDemo',
    currentPageName: 'Apollo Demo',
  }
}
```

Nous créons un objet qui sert d'état par défaut de notre site. apolloClientDemo est le nom de la structure de données que nous voulons accéder lorsque nous faisons nos requêtes. Le `__typename` est l'identifiant obligatoire que notre cache utilise, et currentPageName est l'élément spécifique de données que notre en-tête utilisera pour  vous l'avez deviné  afficher le nom de la page actuelle.

Nous devrons ajouter cela à notre fichier `apollo/index.js` :

```js
import defaults from './defaults';

const stateLink = withClientState({
  cache,
  defaults,
});
```

Éclaircissons un peu cela. `import` et `default` sont tous deux des mots-clés associés à l'importation de modules, mais par coïncidence, le nom de l'objet que nous exportons depuis `./defaults` s'appelle également `defaults` (donc ne pensez pas que j'utilise `import/export` de manière incorrecte). Traitez cette ligne d'importation comme si c'était juste une importation nommée régulière.

Cela étant dit, allons faire une requête !

### Comment faire une requête

Ajoutez le package suivant à votre projet :

```
> yarn add graphql-tag
```

et créez un nouveau répertoire `src/graphql`. À l'intérieur, créez deux nouveaux fichiers : `index.js` et `getPageName.js`. Le répertoire GraphQL abritera toutes les requêtes et mutations. Nous créerons notre requête dans `getPageName.js` en écrivant ce qui suit :

```js
import gql from 'graphql-tag';

export const getPageNameQuery = gql`
  query {
    apolloClientDemo @client {
      currentPageName
    }
  }
`;

export const getPageNameOptions = ({
  props: ({ data: { apolloClientDemo } }) => ({
    apolloClientDemo
  })
});
```

Nous exportons donc deux variables, la requête et les options. Si vous avez déjà utilisé GraphQL, alors la requête vous sera familière. Nous interrogeons la structure de données apolloClientDemo, en récupérant rien de plus que le currentPageName. Vous remarquerez que nous avons ajouté la directive `@client` à notre requête. Cela indique à Apollo d'interroger notre état local au lieu d'envoyer la requête au backend.

Vous verrez ci-dessous que nous exportons quelques options. Cela définit simplement comment nous voulons que les données apparaissent lorsque nous mappons les résultats aux props. Nous déstructurons la réponse GraphQL et l'envoyons à notre vue pour qu'elle ressemble à ceci :

```js
props: {
  currentPageName: 'Apollo Demo',
}
// et pas ceci
props: {
  data: {
    apolloClientDemo: {
      currentPageName: 'Apollo Demo',
    }
  }
}
```

Allez dans le fichier `graphql/index.js` et exportez la requête comme suit :

```js
export { getPageNameQuery, getPageNameOptions } from './getPageName';

```

Encore une fois, bien que cela ne soit pas complètement nécessaire pour une petite démonstration/projet, ce fichier est pratique si votre application grandit. Avoir vos requêtes exportées depuis un emplacement centralisé garde tout organisé et évolutif.

Ajoutez à votre Header.js :

```js
import React from 'react';
import { Query } from 'react-apollo';
import { getPageNameQuery } from '../graphql';

const Header = () => (
    <Query query={getPageNameQuery}>
        {({ loading, error, data }) => {
            if (error) return <h1>Erreur...</h1>;
            if (loading || !data) return <h1>Chargement...</h1>;

            return <h1>{data.apolloClientDemo.currentPageName}</h1>
        }}
    </Query>
);

export default Header;
```

C'est notre première utilisation du nouveau composant Query d'Apollo, qui a été ajouté dans la version 2.1. Nous importons `Query` depuis `react-apollo` et l'utilisons pour envelopper le reste de notre composant. Nous passons ensuite getPageNameQuery comme valeur dans la prop query. Lorsque notre composant se rend, il lance la requête et donne au reste du composant accès aux données, que nous déstructurons pour obtenir l'accès à loading, errors et data.

Le composant Query utilise le modèle de props de rendu pour donner au reste de notre composant accès aux informations retournées par la requête. Si vous avez utilisé l'API de contexte React dans la version 16.3, alors vous avez déjà vu cette syntaxe. Sinon, il vaut la peine de consulter la documentation officielle de React [ici](https://reactjs.org/docs/render-props.html), car le modèle de props de rendu devient de plus en plus populaire.

Dans notre composant, nous effectuons quelques vérifications pour voir s'il y a eu des erreurs lors de l'exécution de la requête ou si nous attendons toujours que les données soient retournées. Si l'un de ces scénarios est vrai, nous retournons le HTML correspondant. Si la requête a été exécutée correctement, le composant affichera dynamiquement le titre de la page actuelle. Comme nous n'avons pas encore ajouté notre mutation, il n'affichera que la valeur par défaut. Mais vous pouvez changer ce qui se trouve dans l'état par défaut et le site web reflétera cela.

Maintenant, tout ce qu'il reste à faire est de muter les données dans le cache Apollo en cliquant sur l'élément de la barre latérale.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OHpQBcsRCsX5Wk_b.)
_Une image rafraîchissante pour casser le texte. [Jeff Sheldon](https://unsplash.com/@ugmonk?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title=")_

### Mutations

Les choses se compliquent un peu lorsque l'on traite avec les mutations. Nous ne récupérons plus simplement les données du magasin Apollo, mais nous les mettons également à jour. L'architecture de la mutation est la suivante :

**> U**tilisateur clique sur l'élément de la barre latérale

**> Se**nds variable à la mutation

**> Fi**res mutation avec variable

**> G**ets envoyé à l'instance d'Apollo

**> Fi**nds le résolveur correspondant

**> Appl**ies la logique au magasin Apollo

**> Se**nds les données à l'en-tête

Si cela est difficile à retenir, alors utilisez ce moyen mnémotechnique pratique créé à l'aide d'un générateur de moyens mnémotechniques : Urban Senile Fauns Groped Faithless Aslan Solemnly. (facile)

Commencez par créer un fichier `graphql/updatePageName.js`.

```js
import gql from 'graphql-tag';

export const updatePageName = gql`
  mutation updatePageName($name: String!) {
    updatePageName(name: $name) @client {
      currentPageName
    }
  }
`;
```

et exportez-le comme nous l'avons fait avec la requête.

```js
export { updatePageNameMutation } from './updatePageName';

```

Vous remarquerez quelques différences concernant la mutation. Tout d'abord, nous avons changé le mot-clé de query à mutation. Cela permet à GraphQL de connaître le type d'action que nous effectuons. Nous définissons également le nom de la requête et ajoutons des types aux variables que nous passons. Ici, nous spécifions le nom du résolveur que nous utiliserons pour effectuer les changements. Nous passons également la variable et ajoutons la directive `@client`.

Contrairement à la requête, nous ne pouvons pas simplement ajouter la mutation à notre vue et nous attendre à ce que quelque chose se passe. Nous devrons revenir à notre répertoire Apollo et ajouter nos résolveurs. Donc, allez-y et créez un nouveau répertoire `apollo/resolvers`, et des fichiers `index.js` et `updatePageName.js`. À l'intérieur de `updatePageName.js`, ajoutez ce qui suit :

```js
import gql from 'graphql-tag';

export default (_, { name }, { cache }) => {
  const query = gql`
    query GetPageName {
      apolloClientDemo @client {
        currentPageName
      }
    }
  `;
  
  const previousState = cache.readQuery({ query });
  
  const data = {
    apolloClientDemo: {
      ...previousState.apolloClientDemo,
      currentPageName: name,
    },
  };
  
  cache.writeQuery({
    query,
    data,
  });
  
  return null;
};
```

Il y a beaucoup de choses intéressantes qui se passent dans ce fichier. Heureusement, tout est très logique et n'ajoute pas beaucoup de nouveaux concepts à ce que nous avons vu auparavant.

Ainsi, par défaut, lorsqu'un résolveur est appelé, Apollo passe toutes les variables et le cache. Le premier argument est un simple '_' car nous n'avons pas besoin de l'utiliser. Le deuxième argument est l'objet des variables, et le dernier argument est le cache.

Avant de pouvoir apporter des modifications au magasin Apollo, nous devrons le récupérer. Nous faisons donc une simple requête pour obtenir le contenu actuel du magasin et l'assignons à previousState. À l'intérieur de la variable data, nous créons un nouvel objet avec les nouvelles informations que nous voulons ajouter au magasin, que nous écrivons ensuite. Vous pouvez voir que nous avons étendu l'état précédent à l'intérieur de cet objet. Cela permet de mettre à jour uniquement les données que nous voulons explicitement changer. Tout le reste reste tel quel. Cela empêche Apollo de mettre à jour inutilement les composants dont les données n'ont pas changé.

Note : bien que cela ne soit pas complètement nécessaire pour cet exemple, c'est super utile lorsque les requêtes et les mutations gèrent de plus grandes quantités de données, donc je l'ai gardé pour le bien de l'évolutivité.

Pendant ce temps, dans le fichier `resolvers/index.js`...

```js
import updatePageName from 'updatePageName';

export default {
  Mutation: {
    updatePageName,
  }
}
```

C'est la forme de l'objet qu'Apollo attend lorsque nous passons nos résolveurs dans stateLink dans `apollo/index.js` :

```js
import resolvers from './resolvers';

const stateLink from = withClientState({
  cache,
  defaults,
  resolvers,
});
```

Il ne reste plus qu'à ajouter la mutation à notre composant de barre latérale.

```js
// previous imports
import { Mutation } from 'react-apollo';
import { updatePageNameMutation } from '../graphql';

class Sidebar extends React.Component {
  render() {
    return (
      <Mutation mutation={updatePageNameMutation}>
        {updatePageName => (
          // outer div elements
          <li className="sidebar-item" onClick={() => updatePageName({ variables: { name: 'React'} })}>React</li>
          // other list items and outer div elements
        )}
      </Mutation>
    );
  }
}

export default Sidebar;
```

Comme notre fichier de résolveur, il y a beaucoup de choses qui se passent dans ce fichier  mais c'est nouveau. Nous importons notre composant `Mutation` depuis `react-apollo`, l'enveloppons autour de notre composant et passons `updatePageNameMutation` à l'intérieur de la prop `mutation`.

Le composant a maintenant accès à la méthode `updatePageName` qui déclenche la mutation chaque fois qu'elle est appelée. Nous faisons cela en ajoutant la méthode comme gestionnaire de la propriété onClick de `<li>`. La méthode s'attend à recevoir un objet contenant les variables en tant que paramètre, donc passez le nom que vous voulez mettre à jour dans l'en-tête. Si tout fonctionne, vous devriez pouvoir exécuter votre serveur de développement et cliquer sur les éléments de la barre latérale, ce qui devrait alors changer notre en-tête.

### Conclusion

Hourra ! Espérons que tout a fonctionné. Si vous êtes bloqué, alors consultez le dépôt [ici](https://github.com/andrico1234/apollo-local-state-starter). Il contient tout le code finalisé. Si vous pensez à utiliser la gestion d'état local dans votre prochaine application React, alors vous pouvez fork ce dépôt et continuer à partir de là. Si vous êtes intéressé à avoir cet article/sujet discuté lors d'une rencontre ou d'une conférence, alors envoyez-moi un message !

Il y a beaucoup plus de choses que je voulais couvrir dans ce tutoriel, comme les résolveurs asynchrones (pensez à Redux thunk), la vérification de type/création d'un schéma, et une mise à jour de mutation. Donc qui sait peut-être que je publierai un autre article bientôt.

J'espère vraiment que ce tutoriel a été utile pour vous. Je tiens à mentionner également le [tutoriel YouTube de Sara Vieira](https://www.youtube.com/watch?v=2RvRcnD8wHY), car il m'a aidé à comprendre Apollo Client. Si je n'ai pas fait mon travail assez bien en vous laissant perplexe, alors suivez le lien. Et enfin, n'hésitez pas à me contacter sur les réseaux sociaux, je suis un grand fan de musique et de technologie, alors parlez-moi geek.

#### Merci d'avoir lu !

Si vous êtes intéressé à m'accueillir lors d'une conférence, d'une rencontre ou en tant qu'invité pour toute intervention, vous pouvez me contacter sur [twitter](https://twitter.com/andricokaroulla?lang=en) !

#### Vous pouvez consulter mes autres articles ci-dessous :

[_Comment utiliser les nouveaux composants Query d'Apollo pour gérer l'état local_](https://medium.com/@andricokaroulla/updated-for-apollo-v2-1-managing-local-state-with-apollo-d1882f2fbb7)

[_Ajoutez une touche de Suspense à votre application web avec React.lazy()_](http://Add a touch of Suspense to your web app with React.lazy())

[_Pas besoin d'attendre les vacances, commencez à Décorer maintenant_](https://codeburst.io/no-need-to-wait-for-the-holidays-start-decorating-now-67b9dabd60d7)

[_Gestion de l'état local avec Apollo et les composants d'ordre supérieur_](https://itnext.io/managing-local-state-with-apollo-client-3be522258645)

[_Le jeu de boisson de la conférence React_](https://medium.com/@andricokaroulla/the-react-conference-drinking-game-7a996bfbef3)

[_Développez et déployez votre propre application React monorepo en moins de 2 heures, en utilisant Lerna, Travis et Now_](https://codeburst.io/develop-and-deploy-your-own-react-monorepo-app-in-under-2-hours-using-lerna-travis-and-now-2b140d647238)
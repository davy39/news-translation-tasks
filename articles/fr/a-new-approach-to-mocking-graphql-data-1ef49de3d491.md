---
title: Une nouvelle approche pour simuler des données GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T17:06:38.000Z'
originalURL: https://freecodecamp.org/news/a-new-approach-to-mocking-graphql-data-1ef49de3d491
coverImage: https://cdn-media-1.freecodecamp.org/images/1*w8fFdZ3gAy7q1x_qOFB-gg.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Une nouvelle approche pour simuler des données GraphQL
seo_desc: 'By Sashko Stubailo

  How we power React component tests and examples at Stripe

  GraphQL’s main benefit for frontend developers has always been excellent tooling
  and developer experience. Chief among those is the ability to easily mock your data.
  API moc...'
---

Par Sashko Stubailo

#### Comment nous alimentons les tests et exemples de composants React chez Stripe

Le principal avantage de GraphQL pour les développeurs frontend a toujours été l'excellente tooling et l'expérience développeur. Parmi ceux-ci, la capacité de simuler facilement vos données est primordiale. La simulation d'API est cruciale car elle permet d'écrire et de tester vos composants sans avoir à exécuter tout le backend de votre application. Vous pouvez même développer des composants UI basés sur un schéma simulé lorsque l'implémentation backend n'est pas encore terminée, accélérant ainsi le développement.

Au cours des derniers mois, l'équipe Dashboard Platform chez [Stripe](https://stripe.com/) a intégré [GraphQL](https://graphql.org/) et [Apollo](https://www.apollographql.com/) pour la récupération de données dans le Stripe Dashboard. Notre objectif est de créer une expérience fluide et productive pour les développeurs de produits à travers toute l'entreprise. L'un des aspects les plus importants est de rendre les tests aussi faciles que possible. Pour atteindre cet objectif, nous avons mis au point de nouveaux modèles qui nous permettent de simuler des données avec une quantité extrêmement réduite de code.

Je vais vous expliquer comment nous :

1. simulons les données GraphQL pour l'ensemble du schéma
2. personnalisons nos simulations sur une base par composant
3. simulons les états de chargement et d'erreur avec une seule ligne de code
4. intégrons ces simulations dans nos tests Jest et notre explorateur de composants

Ensemble, ces nouveaux outils nous permettent de rendre des composants UI qui dépendent des données GraphQL dans les tests et exemples, dans tous les états dont nous avons besoin, sans écrire de code pour gérer des requêtes et réponses spécifiques.

Alors, plongeons directement dans le vif du sujet ! Nous avons inclus tout le code nécessaire pour suivre ce post. Nous accueillons favorablement quelqu'un de la communauté publiant un package `npm` basé sur notre approche.

_Merci tout particulier à mes collègues [Isaac Hellendag](https://twitter.com/hellendag), Oliver Wong et Jason Divock, qui ont contribué à ces outils et à ce post._

![Image](https://cdn-media-1.freecodecamp.org/images/1*DqP8CiEUerOXeYubtxbGRw.png)
_Comment nous avons réduit notre boilerplate de test de composants en éliminant les simulations par requête et en utilisant un schéma simulé._

### Contexte : Simulation de données avec graphql-tools

Il existe une variété d'outils qui rendent super facile la simulation de requêtes basées sur un schéma GraphQL et des queries.

Il y a la bibliothèque originale [graphql-tools](https://www.apollographql.com/docs/graphql-tools/mocking.html), le CLI [graphql-faker](https://github.com/APIs-guru/graphql-faker), et maintenant même [Apollo Server a la simulation intégrée](https://www.apollographql.com/docs/apollo-server/features/mocking.html). J'ai une préférence pour graphql-tools car c'est le plus facile à personnaliser.

Avant de plonger dans les nouvelles fonctionnalités qui m'enthousiasment vraiment avec la personnalisation par composant, je vais vous montrer la configuration de base de la simulation.

Voici comment vous pouvez obtenir un schéma simulé et le faire fonctionner super rapidement avec graphql-tools :

<script src="https://gist.github.com/stubailo/818609c5558ffdf658bdb66088959381.js"></script>

Cette approche vous permet de générer n'importe quelle forme de données fictives, simplement en fournissant une requête. Voici comment nous pouvons connecter notre schéma simulé à nos composants alimentés par Apollo en utilisant [apollo-link-schema](https://www.apollographql.com/docs/link/links/schema.html) et Apollo Client :

<script src="https://gist.github.com/stubailo/ccbb3539d5fab3ebebddb11f584386cd.js"></script>

Maintenant, nous pouvons rendre un composant avec des données simulées n'importe où nous le souhaitons, par exemple dans un test Jest, ou un explorateur de composants comme Storybook. Une chose intéressante est que `graphql-tools` nous permet de passer des simulations personnalisées pour notre schéma sur une base par type.

<script src="https://gist.github.com/stubailo/b5e6a5865c123417a7ee9d780ba36456.js"></script>

Cela nous permet de nous assurer que les données que nous obtenons de nos simulations semblent quelque peu réelles. La bibliothèque `faker` est super utile ici car elle nous permet d'obtenir des données quelque peu réalistes avec peu d'effort.

Malheureusement, avoir un schéma simulé qui retourne des données réalistes n'est pas tout à fait suffisant pour une configuration de simulation complète. Parfois, vous voulez qu'un test ou un exemple de composant affiche une situation très spécifique, plutôt que des données de simulation génériques. Vous devez également vous assurer que votre composant se comporte correctement lorsqu'il reçoit des chaînes vides, ou une liste très longue, ou un état de chargement ou d'erreur. Et c'est là que les choses deviennent vraiment intéressantes.

#### Personnalisation des simulations sur une base par composant avec un fournisseur de simulation

Après avoir essayé de nombreuses approches différentes, nous avons mis au point une API soignée qui nous permet d'utiliser des simulations globales tout en personnalisant uniquement les types et champs dont nous avons besoin pour ce test ou exemple particulier.

Voici à quoi cela ressemble :

<script src="https://gist.github.com/stubailo/51dc130cf5e1e9e684a24a80b158540f.js"></script>

Cela nous permet de nous assurer que le composant reçoit exactement deux éléments `todo`, où le premier est terminé et le second ne l'est pas. Mais voici la meilleure partie — le reste des données provient des simulations globales que nous avons définies pour toute l'application ! **Ainsi, nous n'avons à spécifier que les champs qui nous intéressent pour cet exemple particulier.**

Cela nous permet d'obtenir le meilleur des deux mondes — des simulations globales réalistes et peu coûteuses, **tout en conservant** la capacité d'obtenir des résultats personnalisés pour démontrer des situations spécifiques sur une base par instance. Alors, comment cela fonctionne-t-il ?

Nous avons implémenté cela via un fournisseur de simulation qui fusionne les résolveurs personnalisés passés via ses props avec nos résolveurs de simulation globaux, comme ceci :

<script src="https://gist.github.com/stubailo/c010ba4d947928da769e0f5acf1eb3d5.js"></script>

Il prend les résolveurs personnalisés que vous passez, les fusionne avec vos simulations globales, puis crée une nouvelle instance Apollo Client à utiliser par le composant que vous testez.

La fonction la plus importante ici est `mergeResolvers`, qui nous permet de fusionner nos simulations définies globalement qui remplacent un cas de test spécifique. Elle est un peu trop longue pour tenir dans ce billet de blog, mais elle fait environ 50 lignes de code : [Consultez la fonction mergeResolvers dans le Gist de mon collègue Isaac.](https://gist.github.com/hellendag/2aa9ad1f9b771f38802760c269bb1b76)

### Simulation des états de chargement et d'erreur en une ligne de code

Le système ci-dessus nous donne la plupart de ce dont nous avons besoin, mais il n'a pas de bon moyen de simuler des choses qui ne sont pas des données réelles — spécifiquement, les états de chargement et d'erreur. Heureusement, nous pouvons utiliser une approche similaire avec Apollo Link pour créer des fournisseurs spéciaux pour ces cas. Par exemple, voici un fournisseur simple pour simuler un état de chargement.

<script src="https://gist.github.com/stubailo/0d1ff3491c123d1d4be436c270d93aeb.js"></script>

C'est exact — c'est si petit que cela tient dans un tweet. Et voici comment vous l'utiliseriez :

```jsx
<LoadingProvider>
  <TodoList />
</LoadingProvider>
```

Super simple ! Des choses géniales. Et les états d'erreur sont presque aussi faciles.

<script src="https://gist.github.com/stubailo/610f6319ef551499ffa0883d47df5d9f.js"></script>

Vous pouvez l'utiliser de la même manière, mais vous pouvez également passer une erreur personnalisable :

```jsx
<ErrorProvider graphQLErrors={[{message: 'Mon message d\'erreur'}]}>
  <TodoList />
</ErrorProvider>
```

Armés de ces trois outils — le fournisseur de schéma simulé avec des résolveurs personnalisés, le fournisseur de chargement et le fournisseur d'erreur — vous pouvez atteindre des cas d'utilisation courants de simulation avec une très petite quantité de code.

Pour les cas d'utilisation plus complexes, vous pouvez toujours utiliser le [MockedProvider](https://www.apollographql.com/docs/guides/testing-react-components.html#MockedProvider) intégré de react-apollo, qui vous permet de spécifier des paires de requêtes et réponses totalement personnalisées.

### Intégration dans les tests Jest et votre explorateur de composants

Maintenant que nous avons un moyen facile de simuler des données, des états de chargement et des erreurs, nous pouvons facilement les intégrer dans Jest ou un explorateur de composants. Nous avons notre propre outil interne d'exploration de composants, mais un outil couramment utilisé dans la communauté est React Storybook.

Voici à quoi ressemble un simple test Jest, utilisant `mount` de [Enzyme](https://github.com/airbnb/enzyme) pour rendre un composant React puis vérifier que son contenu est ce à quoi nous nous attendons.

<script src="https://gist.github.com/stubailo/9473f71aeea5040c3e5be98675b92c5e.js"></script>

Et vous pouvez utiliser ces fournisseurs de la même manière lors du rendu d'un exemple de composant dans Storybook ou similaire.

<script src="https://gist.github.com/stubailo/0554b00cdbc84abe10211506c1a2419a.js"></script>

Et c'est ainsi que nous le faisons !

### Conclusion

Nous espérons qu'en apportant la puissance de GraphQL aux développeurs chez Stripe, le développement frontend deviendra beaucoup plus amusant et productif, et ce n'est que le début de l'histoire. Je suis ravi de travailler avec une équipe aussi géniale chez Stripe !

Nous utilisons notre expérience passée en travaillant sur des équipes et technologies frontend pour proposer des approches passionnantes afin d'améliorer la récupération de données et les outils liés aux API. J'ai hâte de partager davantage de ce sur quoi nous travaillons au cours des prochains mois.

N'hésitez pas à me contacter [sur Twitter à @stubailo](https://twitter.com/stubailo) si vous décidez de créer un package basé sur ce post, si vous avez des commentaires ou si vous souhaitez discuter de GraphQL et React !

De plus, **nous recrutons pour de nombreux [rôles d'ingénierie différents](https://stripe.com/jobs#engineering) ici chez Stripe**, alors postulez si vous souhaitez nous aider à construire l'infrastructure économique de l'internet.
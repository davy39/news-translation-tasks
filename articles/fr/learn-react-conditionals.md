---
title: Comment améliorer vos conditionnels React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-06-11T16:04:46.000Z'
originalURL: https://freecodecamp.org/news/learn-react-conditionals
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/5-ways-to-level-up-your-react-conditionals-1.png
tags:
- name: Conditionals
  slug: conditionals
- name: React
  slug: react
seo_title: Comment améliorer vos conditionnels React
seo_desc: "Do you write conditionals correctly within your React applications? \n\
  Good conditionals are an essential part of any React application. We use conditionals\
  \ to show or hide elements or components in our applications. \nIn short – to be\
  \ an effective Reac..."
---

Écrivez-vous correctement les conditionnels dans vos applications React ?

Les bons conditionnels sont une partie essentielle de toute application React. Nous utilisons les conditionnels pour afficher ou masquer des éléments ou des composants dans nos applications.

En bref, pour être un développeur React efficace, vous devez savoir comment écrire de bons conditionnels.

Passons en revue tous les principaux motifs que vous devez connaître pour écrire des conditionnels clairs et concis, ainsi que les anti-motifs à éviter.

### Vous voulez votre propre copie ?📄

**[Téléchargez l'aide-mémoire au format PDF ici](http://bit.ly/react-conditionals-2021)** (cela prend 5 secondes).

Voici quelques gains rapides en téléchargeant la version téléchargeable :

* Guide de référence rapide à consulter comme et quand vous le souhaitez
* Des tonnes d'extraits de code copiables pour une réutilisation facile
* Lisez ce guide complet où cela vous convient le mieux. Dans le train, à votre bureau, en faisant la queue... n'importe où.

Il y a beaucoup de choses intéressantes à couvrir, alors commençons.

## 1. Utilisez principalement les instructions if. Pas besoin de else ou else-if.

Commençons par le type de conditionnel le plus basique dans React. Si nous avons des données, nous voulons les afficher. Sinon, nous voulons ne rien montrer.

Simple ! Comment pourrions-nous écrire cela ?

Supposons que nous récupérons un tableau de données de posts depuis une API. Lorsque nous récupérons les données, `posts` a une valeur de `undefined`.

Nous pouvons vérifier cette valeur avec une simple instruction if.

```js
export default function App() {
  const { posts } = usePosts(); // posts === undefined au début

  if (!posts) return null;

  return (
    <div>
      <PostList posts={posts} />
    </div>
  );
}
```

La raison pour laquelle ce motif fonctionne est que nous retournons tôt. Si la condition est remplie (si `!posts` a une valeur booléenne de `true`), nous n'affichons rien dans notre composant en retournant `null`.

Les instructions if fonctionnent également lorsque vous avez plusieurs conditions que vous souhaitez vérifier.

Par exemple, si vous souhaitez vérifier les états de chargement et d'erreur avant d'afficher vos données :

```js
export default function App() {
  const { isLoading, isError, posts } = usePosts();
  
  if (isLoading) return <div>Chargement...</div>;
  if (isError) return <div>Erreur !</div>;

  return (
    <div>
      <PostList posts={posts} />
    </div>
  );
}
```

Remarquez que nous pouvons réutiliser l'instruction if et n'avons pas à écrire if-else ou if-else-if, ce qui réduit le code que nous devons écrire et reste tout aussi lisible.

## 2. Utilisez l'opérateur ternaire pour écrire des conditionnels dans votre JSX

Les instructions if sont idéales lorsque nous voulons sortir tôt et n'afficher rien ou un composant totalement différent.

Cependant, que faire si nous ne voulons pas écrire un conditionnel séparé de notre JSX retourné, mais directement dans celui-ci ?

Dans React, nous devons inclure des expressions (quelque chose qui se résout en une valeur), et non des instructions dans notre JSX.

C'est pourquoi nous devons écrire des conditionnels dans notre JSX uniquement avec des ternaires et non des instructions if.

Par exemple, si nous voulions afficher un composant imbriqué sur un écran de taille mobile et un autre sur un écran plus grand, un ternaire serait un choix parfait :

```js
function App() {
  const isMobile = useWindowSize()

  return (
    <main>
      <Header />
      <Sidebar />
      {isMobile ? <MobileChat /> : <Chat />}
    </main>
  )
}
```

La plupart des développeurs pensent que c'est le seul motif qu'ils peuvent utiliser lorsqu'il s'agit d'utiliser des ternaires.

En fait, vous n'avez pas à encombrer votre arbre de composants en incluant tous ces ternaires directement dans votre JSX retourné.

Puisque les ternaires se résolvent en une valeur, rappelez-vous que vous pouvez assigner le résultat d'un ternaire à une variable, que vous pouvez ensuite utiliser où vous le souhaitez :

```js
function App() {
  const isMobile = useWindowSize();
  
  const ChatComponent = isMobile ? <MobileChat /> : <Chat />;

  return (
    <main>
      <Header />
      <Sidebar />
      {ChatComponent}
    </main>
  )
}
```

## 3. Pas de condition else ? Utilisez l'opérateur && (et)

Dans de nombreux cas, vous voudrez utiliser un ternaire dans votre JSX, mais vous réaliserez que si cette condition n'est pas remplie, vous ne voulez rien afficher.

Ce ternaire ressemblerait à ceci : `condition ? <Component /> : null`.

Si vous n'avez pas de condition else, utilisez l'opérateur && :

```js
export default function PostFeed() {
  const { posts, hasFinished } = usePosts()

  return (
    <>
      <PostList posts={posts} />
      {hasFinished && (
        <p>Vous avez atteint la fin !</p>
      )}
    </>
  )
}
```

## 4. Instructions switch pour plusieurs conditions

Que faire si nous sommes dans une situation où nous avons de nombreuses conditions différentes, plus d'une ou deux ?

Nous pourrions certainement écrire plusieurs instructions if, mais toutes ces instructions if, comme nous l'avons vu précédemment, vont au-dessus de notre JSX retourné.

Trop d'instructions if peuvent encombrer nos composants. Comment rendre notre code plus propre ?

Nous pouvons souvent extraire plusieurs conditions vers un composant séparé qui contient une instruction switch.

Par exemple, nous avons un composant Menu que nous pouvons basculer et afficher différents onglets.

Nous avons des onglets qui peuvent afficher les données de l'utilisateur, du chat et de la salle comme vous le voyez ci-dessous :

```js
export default function Menu() {
  const [menu, setMenu] = React.useState(1);

  function toggleMenu() {
    setMenu((m) => {
      if (m === 3) return 1;
      return m + 1;
    });
  }

  return (
    <>
      <MenuItem menu={menu} />
      <button onClick={toggleMenu}>Basculer le Menu</button>
    </>
  );
}

function MenuItem({ menu }) {
  switch (menu) {
    case 1:
      return <Users />;
    case 2:
      return <Chats />;
    case 3:
      return <Rooms />;
    default:
      return null;
  }
}
```

Puisque nous utilisons un composant MenuItem dédié avec une instruction switch, notre composant parent Menu n'est pas encombré par la logique conditionnelle et nous pouvons facilement voir quel composant sera affiché en fonction de l'état `menu`.

## 5. Vous voulez des conditionnels en tant que composants ? Essayez les instructions de contrôle JSX

Il est très bénéfique de pouvoir utiliser du JavaScript simple dans nos composants React. Mais si vous voulez des conditionnels encore plus déclaratifs et simples, découvrez la bibliothèque React JSX control statements.

Vous pouvez l'intégrer à vos projets React en exécutant la commande suivante :

```bash
npm install --save-dev babel-plugin-jsx-control-statements
```

De plus, vous pouvez l'ajouter à votre fichier .babelrc comme suit :

```json
{
  "plugins": ["jsx-control-statements"]
}
```

Il s'agit d'un plugin Babel qui vous permet d'utiliser des composants React directement dans votre JSX pour écrire des conditionnels très faciles à comprendre.

La meilleure façon de comprendre l'utilisation d'une telle bibliothèque est de regarder un exemple. Réécrivons l'un de nos exemples précédents avec l'aide des instructions de contrôle JSX :

```js
export default function App() {
  const { isLoading, isError, posts } = usePosts();

  return (
    <Choose>
      <When condition={isLoading}>
        <div>Chargement...</div>
      </When>
      <When condition={isError}>
        <div>Erreur !</div>
      </When>
      <Otherwise>
        <PostList posts={posts} />
      </Otherwise>
    </Choose>
  );
}
```

Vous pouvez voir qu'il n'y a pas d'instruction if ou ternaire en vue et nous avons une structure de composant très lisible.

Essayez les instructions de contrôle JSX dans votre prochain projet React et voyez si une bibliothèque comme celle-ci est faite pour vous.

## **Quoi de neuf**

J'espère que ce guide vous a donné quelques motifs utiles pour écrire de bons conditionnels React.

Si vous voulez une copie de cette aide-mémoire à garder pour des raisons d'apprentissage, vous pouvez [télécharger une version PDF complète de cette aide-mémoire ici.](http://bit.ly/react-conditionals-2021)

Consultez également ces ressources ultimes, conçues pour faire passer vos compétences React au niveau supérieur, notamment :

* [React pour débutants : Le guide complet](https://reactbootcamp.com/react-for-beginners-2021/)
* [Comment récupérer des données dans React de bout en bout](https://reactbootcamp.com/fetch-data-in-react/)
* [Comment construire des applications fullstack dans React avec Node](https://reactbootcamp.com/react-app-node-backend/)

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*
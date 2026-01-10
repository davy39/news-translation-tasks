---
title: Séparation des responsabilités dans React – Comment utiliser les composants
  Container et Presentational
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-12-06T21:43:19.000Z'
originalURL: https://freecodecamp.org/news/separation-of-concerns-react-container-and-presentational-components
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/container-and-presentational-component-pattern-image.jpeg
tags:
- name: components
  slug: components
- name: hooks
  slug: hooks
- name: React
  slug: react
seo_title: Séparation des responsabilités dans React – Comment utiliser les composants
  Container et Presentational
seo_desc: "Many new React developers combine logic and presentation inside the same\
  \ React component. And they may not know why it's important to separate these two\
  \ – they just want to make it work. \nBut later, they'll find that they need to\
  \ make changes to the ..."
---

De nombreux nouveaux développeurs React combinent la logique et la présentation au sein du même composant React. Et ils ne savent peut-être pas pourquoi il est important de séparer ces deux éléments – ils veulent simplement que cela fonctionne.

Mais plus tard, ils constateront qu'ils doivent apporter des modifications au fichier et que cela devient une tâche énorme. Ils devront alors retravailler les choses pour séparer ces deux parties.

Cela vient du fait de ne pas connaître la séparation des responsabilités et le modèle des composants de présentation et de conteneur. C'est pourquoi je vais vous enseigner ces concepts afin que vous puissiez atténuer ce problème tôt dans le cycle de développement de votre projet.

Dans cet article, nous allons plonger dans les composants conteneur et de présentation et aborder brièvement le concept de séparation des responsabilités.

Sans plus attendre, commençons !

## Table des matières

* [Qu'est-ce que la séparation des responsabilités ?](#heading-quest-ce-que-la-separation-des-responsabilites)
* [Quels sont les composants de présentation et les composants conteneur ?](#heading-quels-sont-les-composants-de-presentation-et-les-composants-conteneur)
* [Pourquoi avons-nous besoin de ces composants ?](#heading-pourquoi-avons-nous-besoin-de-ces-composants)
* [Exemple de composant de présentation et de composant conteneur](#heading-exemple-de-composant-de-presentation-et-de-composant-conteneur)
* [Comment remplacer les composants conteneur par des hooks React](#heading-comment-remplacer-les-composants-conteneur-par-des-hooks-react)
* [Résumé](#heading-resume)

## Qu'est-ce que la séparation des responsabilités ?

La séparation des responsabilités est un concept largement utilisé en programmation. Il stipule que la logique qui effectue différentes actions ne doit pas être regroupée ou combinée ensemble.

Par exemple, ce dont nous avons discuté dans la section d'introduction viole la séparation des responsabilités, car nous avons placé la logique de récupération des données et de présentation des données dans le même composant.

Pour résoudre ce problème et adhérer à la séparation des responsabilités, nous devons séparer ces deux parties de la logique – c'est-à-dire la récupération des données et leur présentation sur l'UI – en deux composants différents.

C'est là que le modèle de composant conteneur et de présentation nous aidera à résoudre ce problème. Dans les sections suivantes, nous allons approfondir ce modèle.

## Quels sont les composants conteneur et les composants de présentation ?

Pour atteindre une séparation des responsabilités, nous avons deux types de composants :

- Composants conteneur
- Composants de présentation

### Composants conteneur

Ce sont les composants qui fournissent, créent ou contiennent des données pour les composants enfants.

Le seul travail d'un composant conteneur est de gérer les données. Il ne contient aucune UI propre. Il contient plutôt des composants de présentation comme enfants qui utilisent ces données.

Un exemple simple serait un composant nommé `FetchUserContainer` qui contient une logique pour récupérer tous les utilisateurs.

### Composants de présentation

Ce sont les composants dont la responsabilité principale est de présenter les données sur l'UI. Ils reçoivent les données des composants conteneur.

Ces composants sont sans état, sauf s'ils ont besoin de leur propre état pour rendre l'UI. Ils ne modifient pas les données qu'ils reçoivent.

Un exemple de cela serait un composant `UserList` qui affiche tous les utilisateurs.

## Pourquoi avons-nous besoin de ces composants ?

Pour comprendre cela, prenons un exemple simple. Nous voulons afficher une liste de posts que nous récupérons depuis l'API [JSON placeholder](https://jsonplaceholder.typicode.com/). Voici le code pour cela :

```typescript
import { useEffect, useState } from "react";

interface Post {
  userId: number;
  id: number;
  title: string;
  body: string;
}

/**
 * Un exemple de la manière dont nous ne devrions pas combiner la logique et la présentation des données.
 */
export default function DisplayPosts() {
  const [posts, setPosts] = useState<Post[] | null>(null);
  const [isLoading, setIsLoading] = useState<Boolean>(false);
  const [error, setError] = useState<unknown>();

// Logique
  useEffect(() => {
    (async () => {
      try {
        setIsLoading(true);
        const resp = await fetch("https://jsonplaceholder.typicode.com/posts");
        const data = await resp.json();
        setPosts(data);
        setIsLoading(false);
      } catch (err) {
        setError(err);
        setIsLoading(false);
      }
    })();
  }, []);

// Présentation
  return isLoading ? (
    <span>Chargement... </span>
  ) : posts ? (
    <ul>
      {posts.map((post: Post) => (
        <li key={`item-${post.id}`}>
          <span>{post.title}</span>
        </li>
      ))}
    </ul>
  ) : (
    <span>{JSON.stringify(error)}</span>
  );
}
```

Voici ce que fait ce composant :

- Il a 3 variables d'état : `posts`, `isLoading`, et `error`.
- Nous avons un hook `useEffect` qui contient la logique métier. Ici, nous récupérons les données de l'API : `[https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)` avec l'API [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).
- Nous nous assurons que lorsque les données sont récupérées, nous les stockons dans la variable d'état `posts` en utilisant `setPosts`.
- Nous nous assurons également que nous basculons les valeurs `isLoading` et `error` pendant les scénarios respectifs.
- Nous plaçons toute cette logique à l'intérieur d'une IIFE asynchrone.
- Enfin, nous retournons les posts sous la forme d'une liste non ordonnée et parcourons tous les posts que nous avons récupérés précédemment.

Le problème avec ce qui précède est que la logique de récupération des données et d'affichage des données est codée dans un seul composant. Nous pouvons dire que le composant est maintenant fortement couplé avec la logique. C'est exactement ce que nous ne voulons pas.

Voici quelques raisons pour lesquelles nous avons besoin de composants conteneur et de présentation :

- Ils nous aident à créer des composants qui sont faiblement couplés
- Ils nous aident à maintenir la séparation des responsabilités
- Le refactoring du code devient beaucoup plus facile.
- Le code devient plus organisé et maintenable
- Cela rend les tests beaucoup plus faciles.

## Exemple de composant de présentation et de composant conteneur

D'accord, assez parlé – commençons par un exemple simple. Nous allons utiliser le même exemple que précédemment – récupérer les données depuis une API JSON placeholder.

Comprenons la structure des fichiers ici :

- Notre composant conteneur sera `PostContainer`
- Nous aurons deux composants de présentation :
    - `Posts` : Un composant qui a une liste non ordonnée.
    - `SinglePost` : Un composant qui rend une balise de liste. Cela rendra chaque élément de la liste.

Note : Nous allons stocker tous les composants ci-dessus dans un dossier séparé nommé `components`.

Maintenant que nous savons où vont les choses, commençons par le composant conteneur : `PostContainer`. Copiez-collez le code ci-dessous dans le fichier `components/PostContainer.tsx`

```typescript
import { useEffect, useState } from "react";
import { ISinglePost } from "../Definitions";
import Posts from "./Posts";

export default function PostContainer() {
  const [posts, setPosts] = useState<ISinglePost[] | null>(null);
  const [isLoading, setIsLoading] = useState<Boolean>(false);
  const [error, setError] = useState<unknown>();

  useEffect(() => {
    (async () => {
      try {
        setIsLoading(true);
        const resp = await fetch("https://jsonplaceholder.typicode.com/posts");
        const data = await resp.json();
        setPosts(data.filter((post: ISinglePost) => post.userId === 1));
        setIsLoading(false);
      } catch (err) {
        setError(err);
        setIsLoading(false);
      }
    })();
  }, []);

  return isLoading ? (
    <span>Chargement... </span>
  ) : posts ? (
    <Posts posts={posts} />
  ) : (
    <span>{JSON.stringify(error)}</span>
  );
}
```

D'après l'exemple que nous avons vu dans la section précédente de cet article, le code ci-dessus contient uniquement la logique de récupération des données. Cette logique est présente dans le hook `useEffect`. Ici, ce composant conteneur transmet ces données au composant de présentation `Posts`.

Jetons un coup d'œil au composant de présentation `Posts`. Copiez-collez le code ci-dessous dans le fichier `components/Posts.tsx` :

```typescript
/**
 * Un composant de présentation
 */

import { ISinglePost } from "../Definitions";
import SinglePost from "./SinglePost";

export default function Posts(props: { posts: ISinglePost[] }) {
  return (
    <ul
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center"
      }}
    >
      {props.posts.map((post: ISinglePost) => (
        <SinglePost {...post} />
      ))}
    </ul>
  );
}
```

Comme vous pouvez le voir, il s'agit d'un fichier simple qui contient une balise `ul` – une liste non ordonnée. Ce composant parcourt ensuite les `posts` qui sont passés en tant que props. Nous passons chacun au composant `SinglePost`.

Il y a un autre composant de présentation qui rend la balise de liste, c'est-à-dire la balise `li`. Il affiche le titre et le corps du post. Copiez-collez le code ci-dessous dans le fichier `components/SinglePost.tsx` :

```typescript
import { ISinglePost } from "../Definitions";

export default function SinglePost(props: ISinglePost) {
  const { userId, id, title, body } = props;
  return (
    <li key={`item-${userId}-${id}`} style={{ width: 400 }}>
      <h4>
        <strong>{title}</strong>
      </h4>
      <span>{body}</span>
    </li>
  );
}
```

Ces composants de présentation, comme vous pouvez le voir, affichent simplement les données à l'écran. C'est tout. Ils ne font rien d'autre. Puisqu'ils affichent simplement les données ici, ils auront également leur propre style.

Maintenant que nous avons configuré les composants, revenons sur ce que nous avons accompli ici :

- Le concept de séparation des responsabilités n'est pas violé dans cet exemple.
- L'écriture de tests unitaires pour chaque composant devient plus facile.
- La maintenabilité et la lisibilité du code sont bien meilleures. Ainsi, notre base de code est devenue beaucoup plus organisée.

Nous avons atteint ce que nous voulions ici, mais nous pouvons encore améliorer ce modèle avec l'aide des hooks.

## Comment remplacer les composants conteneur par des hooks React

Depuis **React 16.8.0**, il est devenu beaucoup plus facile de construire et de développer des composants avec l'aide des composants fonctionnels et des hooks.

Nous allons tirer parti de ces capacités ici et remplacer le composant conteneur par un hook.

Copiez-collez le code ci-dessous dans le fichier `hooks/usePosts.ts` :

```typescript
import { useEffect, useState } from "react";
import { ISinglePost } from "../Definitions";

export default function usePosts() {
  const [posts, setPosts] = useState<ISinglePost[] | null>(null);
  const [isLoading, setIsLoading] = useState<Boolean>(false);
  const [error, setError] = useState<unknown>();

  useEffect(() => {
    (async () => {
      try {
        setIsLoading(true);
        const resp = await fetch("https://jsonplaceholder.typicode.com/posts");
        const data = await resp.json();
        setPosts(data.filter((post: ISinglePost) => post.userId === 1));
        setIsLoading(false);
      } catch (err) {
        setError(err);
        setIsLoading(false);
      }
    })();
  }, []);

  return {
    isLoading,
    posts,
    error
  };
}
```

Ici nous avons,

- Extrait la logique qui était présente dans le composant `PostContainer` dans un hook.
- Ce hook retournera un objet qui contient les valeurs `isLoading`, `posts`, et `error`.

Maintenant, nous pouvons simplement supprimer le composant conteneur `PostContainer`. Ensuite, plutôt que de passer les données du conteneur aux composants de présentation en tant que prop, nous pouvons utiliser directement ce hook à l'intérieur du composant de présentation `Posts`.

Apportons les modifications suivantes au composant `Posts` :

```typescript
/**
 * Un composant de présentation
 */

import { ISinglePost } from "../Definitions";
import usePosts from "../hooks/usePosts";
import SinglePost from "./SinglePost";

export default function Posts(props: { posts: ISinglePost[] }) {
  const { isLoading, posts, error } = usePosts();

  return (
    <ul
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center"
      }}
    >
      {isLoading ? (
        <span>Chargement...</span>
      ) : posts ? (
        posts.map((post: ISinglePost) => <SinglePost {...post} />)
      ) : (
        <span>{JSON.stringify(error)}</span>
      )}
    </ul>
  );
}
```

En utilisant des hooks, nous avons éliminé une couche supplémentaire de composant qui était présente au-dessus de ces composants de présentation.

Avec les hooks, nous avons obtenu les mêmes résultats que ceux du modèle des composants conteneur/présentation.

## Résumé

Donc, dans cet article, nous avons appris :

- La séparation des responsabilités
- Les composants conteneur et de présentation
- Pourquoi nous avons besoin de ces composants
- Comment les hooks peuvent remplacer les composants conteneur

Pour aller plus loin, je vous recommande vivement de consulter [react-table](https://tanstack.com/table/v8/). Cette bibliothèque utilise extensivement les hooks et propose de excellents exemples.

Vous pouvez trouver l'intégralité du code de cet article dans ce [codesandbox](https://codesandbox.io/s/container-presentation-pattern-lm1osl?file=/src/components/PostContainer.tsx).

Merci d'avoir lu !

Suivez-moi sur [Twitter](https://twitter.com/keurplkar), [GitHub](https://github.com/keyurparalkar), et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).
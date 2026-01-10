---
title: 10 questions d'entretien React que vous devriez connaître en 2022
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-22T00:21:59.000Z'
originalURL: https://freecodecamp.org/news/react-interview-questions-to-know
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/react-interview-questions-1.png
tags:
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
- name: Job Interview
  slug: job-interview
- name: React
  slug: react
seo_title: 10 questions d'entretien React que vous devriez connaître en 2022
seo_desc: 'Feel confident about your React knowledge? Put it to the test!

  I have selected all of the major questions you should know as a React developer
  in 2022, whether you are interviewing for a hired position or not.

  These questions cover everything from th...'
---

Vous vous sentez confiant concernant vos connaissances en React ? Mettez-les à l'épreuve !

J'ai sélectionné toutes les questions majeures que vous devriez connaître en tant que développeur React en 2022, que vous passiez un entretien pour un poste ou non.

Ces questions couvrent tout, des concepts fondamentaux de React à une compréhension pratique de quand utiliser certaines fonctionnalités.

Pour tirer le meilleur parti de ce guide, assurez-vous d'essayer de répondre à chaque question vous-même avant de regarder les réponses.

C'est parti !

## 1. Qu'est-ce que React ? Pourquoi l'utiliser ?

React est une **bibliothèque** JavaScript, pas un framework.

Nous utilisons React car il nous donne toute la puissance de JavaScript, mais avec des fonctionnalités intégrées qui améliorent la façon dont nous construisons et pensons la construction d'applications.

* Il nous donne un moyen de **créer facilement des interfaces utilisateur** avec des outils comme JSX
* Il nous donne des composants pour **partager facilement des parties de notre interface utilisateur (UI)**, ce que le HTML statique ne peut pas faire
* Il nous permet de **créer un comportement réutilisable** dans tous nos composants avec les hooks React
* React **s'occupe de mettre à jour notre UI** lorsque nos données changent, sans avoir besoin de mettre à jour le DOM manuellement

**Crédit supplémentaire** : Il existe des frameworks dans React qui vous donnent tout ce dont vous avez besoin pour construire une application (avec peu ou pas de bibliothèques tierces), comme Next.js et Gatsby.

React a été créé pour construire des applications monopages en particulier, mais vous pouvez créer tout, des sites statiques aux applications mobiles, avec les mêmes concepts React.

## 2. Qu'est-ce que JSX ?

JSX est une façon de construire des interfaces utilisateur React qui utilise la syntaxe simple de HTML, mais ajoute la fonctionnalité et la nature dynamique de JavaScript.

En bref, c'est **HTML + JavaScript pour structurer nos applications React**.

Bien que JSX ressemble à HTML, sous le capot, ce sont en réalité des **appels de fonctions JavaScript**.

Si vous écrivez un `div` en JSX, c'est en fait l'équivalent d'appeler `React.createElement()`.

Nous pouvons construire nos interfaces utilisateur en appelant manuellement `React.createElement`, mais à mesure que nous ajoutons plus d'éléments, il devient de plus en plus difficile de lire la structure que nous avons construite.

**Le navigateur ne peut pas comprendre JSX lui-même**, nous utilisons donc souvent un compilateur JavaScript appelé **Babel** pour convertir ce qui ressemble à du HTML en appels de fonctions JavaScript que le navigateur peut comprendre.

## 3. Comment passez-vous des données aux composants React ?

Il existe 2 façons principales de passer des données aux composants React :

1. Props
2. Context API

Les props sont des données passées d'un composant parent immédiat. Les props sont déclarées sur le composant enfant, peuvent être nommées n'importe comment et peuvent accepter n'importe quelle valeur valide.

```js
function Blog() {
  const post = { title: "Mon article de blog !" };

  return <BlogPost post={post} />;
}
```

Les props sont consommées dans le composant enfant. Les props sont toujours disponibles dans l'enfant en tant que **propriétés d'un objet**.

```js
function BlogPost(props) {
  return <h1>{props.post.title}</h1>
}
```

Puisque les props sont des propriétés d'objet simples, elles peuvent être déstructurées pour un accès plus immédiat.

```js
function BlogPost({ post }) {
  return <h1>{post.title}</h1>
}
```

Le contexte est une donnée passée d'un fournisseur de contexte à tout composant qui consomme le contexte.

Le contexte nous permet d'accéder aux données n'importe où dans notre application (si le fournisseur est passé autour de tout l'arbre de composants), sans utiliser de props.

Les données de contexte sont passées sur la prop `value` en utilisant le composant `Context.Provider`. Elles peuvent être consommées en utilisant le composant Context.Consumer ou le hook `useContext`.

```js
import { createContext, useContext } from 'react';

const PostContext = createContext()

function App() {
  const post = { title: "Mon article de blog !" };

  return (
    <PostContext.Provider value={post}>
      <Blog />
    </PostContext.Provider>
  );
}

function Blog() {
  return <BlogPost />
}

function BlogPost() {
  const post = useContext(PostContext)

  return <h1>{post.title}</h1>
}
```

## 4. Quelle est la différence entre l'état et les props ?

Les états sont des **valeurs que nous pouvons lire et mettre à jour** dans nos composants React.

Les props sont des **valeurs qui sont passées aux composants React et sont en lecture seule** (elles ne doivent pas être mises à jour).

Vous pouvez penser aux props comme étant similaires aux arguments d'une fonction qui existent en dehors de nos composants, tandis que les états sont des valeurs qui changent au fil du temps, mais existent et sont déclarées à l'intérieur de nos composants.

L'état et les props sont similaires en ce sens que les changements les concernant provoquent le re-rendu des composants dans lesquels ils existent.

## 5. À quoi servent les Fragments React ?

Les fragments React sont une fonctionnalité spéciale dans React qui vous permet de regrouper des éléments ou composants enfants sans créer un nœud réel dans le DOM.

La syntaxe des fragments ressemble à un ensemble de balises vides `<></>` ou à des balises étiquetées `React.Fragment`.

En termes plus simples, parfois nous devons mettre plusieurs éléments React sous un seul parent, mais nous ne voulons pas utiliser un élément HTML générique comme un `div`.

Si vous écrivez un tableau, par exemple, ce serait du HTML invalide :

```js
function Table() {
  return (
    <table>
      <tr>
        <Columns />
      </tr>
    </table>
  );
}

function Columns() {
  return (
    <div>
      <td>Colonne 1</td>
      <td>Colonne 2</td>
    </div>
  );
}

```

Nous pourrions éviter ce problème en utilisant un fragment au lieu d'un élément `div` dans notre composant `Columns`.

```js
function Columns() {
  return (
    <>
      <td>Colonne 1</td>
      <td>Colonne 2</td>
    </>
  );
}
```

Une autre raison de choisir un fragment est que parfois l'ajout d'un élément HTML supplémentaire peut changer la façon dont nos styles CSS sont appliqués.

## 6. Pourquoi avons-nous besoin de clés pour les listes React ?

Les clés sont une valeur unique que nous devons passer à la prop `key` lorsque nous utilisons la fonction `.map()` pour boucler sur un élément ou un composant.

Si nous mappons sur un élément, cela ressemblerait à ceci :

```javascript
posts.map(post => <li key={post.id}>{post.title}</li>)
```

Ou comme ceci si nous mappons sur un composant :

```javascript
posts.map(post => <li key={post.id}>{post.title}</li>)
```

Et dans les deux cas, nous devons ajouter une clé qui est une valeur unique, sinon React nous avertira.

Pourquoi ? Parce que **les clés indiquent à React quel élément ou composant est lequel dans une liste**.

Sinon, si nous devions essayer de changer des éléments dans cette liste en en insérant plus ou en les modifiant d'une certaine manière, React ne saurait pas l'ordre dans lequel les mettre.

C'est parce que React s'occupe de toute la logique de mise à jour du DOM pour nous (en utilisant un DOM virtuel), mais **les clés sont nécessaires pour que React le mette à jour correctement**.

## 7. Qu'est-ce qu'une ref ? Comment l'utiliser ?

Une ref est une **référence à un élément DOM** dans React.

Les refs sont créées à l'aide du hook `useRef` et peuvent être immédiatement placées dans une variable.

Cette variable est ensuite passée à un élément React donné (pas un composant) pour obtenir une référence à l'élément DOM sous-jacent (c'est-à-dire div, span, etc.).

L'élément lui-même et ses propriétés sont maintenant disponibles sur la **.propriété current** de la ref.

```js
import { useRef } from 'react'

function MyComponent() {
  const ref = useRef();

  useEffect(() => {
    console.log(ref.current) // référence à l'élément div
  }, [])

  return <div ref={ref} />
}
```

Les refs sont souvent appelées une "issue de secours" pour pouvoir travailler avec un élément DOM directement. Elles nous permettent d'effectuer certaines opérations qui ne peuvent pas être faites via React autrement, comme effacer ou focaliser une entrée.

## 8. À quoi sert le hook useEffect ?

Le hook `useEffect` est utilisé pour effectuer des effets secondaires dans nos composants React.

Les **effets secondaires** sont des opérations qui sont effectuées avec le "monde extérieur" ou quelque chose qui existe en dehors du contexte de notre application React.

Quelques exemples d'effets secondaires incluent faire une requête GET ou POST à un point de terminaison d'API externe ou travailler avec une API de navigateur comme `window.navigator` ou `document.getElementById()`.

Nous ne pouvons pas effectuer des opérations comme celles-ci directement dans le corps de notre composant React. `useEffect` nous donne une fonction dans laquelle effectuer des effets secondaires et un tableau de dépendances qui liste toutes les valeurs externes dont la fonction dépend.

Si une valeur dans le tableau de dépendances change, la fonction d'effet s'exécute à nouveau.

## 9. Quand utilisez-vous React Context vs Redux ?

> Redux est probablement la bibliothèque d'état global tierce la plus couramment utilisée pour React, mais vous pouvez remplacer le mot "Redux" par n'importe quelle bibliothèque d'état global pour React.

React context est un moyen de fournir et de consommer des données dans toute notre application **sans utiliser de props**.

React context nous aide à prévenir le problème de "**perçage de props**", qui est lorsque vous passez des données avec des props à travers des composants qui n'en ont pas besoin.

Au lieu de cela, avec le contexte, nous pouvons **consommer les données exactement dans le composant qui en a besoin**.

Alors que nous utilisons uniquement le contexte pour obtenir ou "lire" des valeurs globalement dans notre application, Redux et d'autres bibliothèques d'état tierces **nous permettent à la fois de lire et de mettre à jour l'état**.

Le contexte n'est pas un remplacement pour une bibliothèque d'état tierce comme Redux car **il n'est pas conçu pour les mises à jour d'état**. Cela est dû au fait que chaque fois que la valeur fournie sur le contexte change, tous ses enfants seront re-rendus, ce qui peut nuire aux performances.

## 10. À quoi servent les hooks useCallback et useMemo ?

Les hooks `useCallback` et `useMemo` existent pour améliorer les performances de nos composants.

`useCallback` est utilisé pour empêcher les fonctions qui sont déclarées dans le corps des composants fonctionnels d'être recréées à chaque rendu.

Cela peut entraîner des problèmes de performance inutiles, surtout pour les fonctions de rappel qui sont passées aux composants enfants.

`useMemo`, en revanche, mémorise une opération coûteuse que nous lui donnons.

La **mémorisation** est un terme technique pour les fonctions qui sont capables de "se souvenir" des valeurs passées qu'elles ont calculées si leurs arguments n'ont pas changé. Si c'est le cas, la fonction retourne la valeur "souvenue".

En d'autres termes, nous pouvons avoir un calcul qui prend une quantité significative de ressources informatiques et nous voulons qu'il soit effectué aussi rarement que possible.

Dans ce cas, nous utilisons le hook `useMemo`, qui diffère du hook `useCallback` en ce sens qu'il retourne une valeur, et non une fonction.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir quand j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*
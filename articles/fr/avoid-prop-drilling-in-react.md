---
title: Comment éviter le Prop Drilling dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-07T22:58:39.000Z'
originalURL: https://freecodecamp.org/news/avoid-prop-drilling-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Purple-Creative-Livestream-YouTube-Thumbnail.png
tags:
- name: components
  slug: components
- name: React
  slug: react
- name: React context
  slug: react-context
seo_title: Comment éviter le Prop Drilling dans React
seo_desc: 'By Ogundiran Ayobami

  In order to write scalable, reusable, and maintainable applications with React,
  you''ll need to go beyond the surface of using React components, useEffect, useContext,
  useState, and the like. It involves learning in detail how Rea...'
---

Par Ogundiran Ayobami

Pour écrire des applications scalables, réutilisables et maintenables avec React, vous devrez aller au-delà de la surface de l'utilisation des composants React, useEffect, useContext, useState, et autres. Cela implique d'apprendre en détail comment React fonctionne en profondeur. 

Et si vous ne comprenez pas correctement ces concepts clés de React, vous pouvez rencontrer divers problèmes, comme le [prop drilling](https://www.quora.com/What-is-prop-drilling-in-ReactJS).

Dans ce tutoriel, vous apprendrez ce qu'est le prop drilling. Je vous montrerai également comment l'éviter intuitivement sans dépendre du contexte React. À la fin, vous comprendrez comment identifier le prop drilling sans réfléchir et le corriger avec précision.

Si vous préférez un guide visuel, voici une version vidéo de ce tutoriel sur ma [chaîne YouTube ici](https://www.youtube.com/watch?v=ELZZnqHJhlw) (environ 15 minutes).

[![Regarder la vidéo](https://img.youtube.com/vi/ELZZnqHJhlw/hqdefault.jpg)](https://www.youtube.com/embed/ELZZnqHJhlw)


## Qu'est-ce que le Prop Drilling ?

Le prop drilling se produit lorsqu'un composant parent génère son état et le transmet sous forme de `props` à ses composants enfants qui ne consomment pas les props – au lieu de cela, ils les transmettent simplement à un autre composant qui les utilise finalement. 

Voici un exemple de prop drilling dans React :

```js
function App() {
  const [profile, setProfile] = useState({ame: 'John'}); 
  return ( 
    <div> <Header profile={profile} /> 
    </div> 
  ); 
} 
  
function Header({ profile }) { 
  return ( 
    <header> 
      <h1>This is the header</h1> 
      <Content profile={profile} /> 
    </header> 
  ); 
} 

function Content({ profile }) { 
  return ( 
    <main> 
      <h2>Content Component</h2> 
      <p>{profile.name}</p> 
    </main> 
  ); 
} 

export default App;
```

Si vous examinez l'exemple ci-dessus, vous remarquerez que `profile` est passé du composant `App` à travers `Header` jusqu'au composant `Content`, qui l'utilise finalement. Cela est communément appelé prop drilling car le composant `Header` ne consomme pas la `prop` mais la transmet simplement au composant `Content` qui l'utilise finalement.

Maintenant que vous comprenez ce qu'est le prop drilling, le prochain défi est de trouver comment l'éviter car ce n'est pas toujours un processus intuitif. 

Vous devrez commencer à explorer des méthodes pour le résoudre. Bien que vous puissiez utiliser la composition de composants et le contexte React pour le résoudre, le défi réside dans le fait de ne pas toujours reconnaître le problème avant qu'il ne soit trop tard. 

Pour vraiment maîtriser l'art de gérer le prop drilling de manière intuitive, vous devez apprendre à identifier les props allongées et les contextes.

## Qu'est-ce qu'une Prop Allongée ?

![Où est l'amour chanté par The Black Eye Peas recréé dans un passage souterrain.](https://images.unsplash.com/photo-1484069560501-87d72b0c3669?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMTc3M3wwfDF8c2VhcmNofDV8fHF1ZXN0aW9uaW5nfGVufDB8fHx8MTY5OTMyMzQ0MXww&ixlib=rb-4.0.3&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@emilymorter?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Emily Morter</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

Une prop allongée est une `prop` qui n'est pas consommée mais qui est simplement transmise à un autre composant. Lorsqu'un composant reçoit une `prop` de son parent et ne la consomme pas, il la transmet à un autre composant. Cette prop est appelée prop allongée car elle a été étendue.

Chaque fois que vous voyez une `prop` transmise par des composants qui ne la créent ni ne la consomment, vous avez une prop allongée (ainsi que du prop drilling) dans votre code. L'extrait de code suivant en est un exemple :

```js
function Profile({ user }) { 
  return ( 
    <header> 
      <h1>This is the header</h1> 
      <Content user={user} /> 
    </header> 
  ); 
}
```

Dans cet exemple, `user` est une `prop` allongée car elle n'est ni créée ni consommée par le composant `Profile`. Au lieu de cela, elle est simplement transmise au composant `Content`. Et cela signifie que nous avons étendu `user` à travers un composant qui n'en a pas besoin pour qu'il puisse atteindre celui qui en a besoin.

Maintenant, revisitons l'exemple que nous avons utilisé pour illustrer le prop drilling. Attendez, pensez-vous ce que je pense ? La `prop` qui est transmise dans l'exemple de prop drilling est effectivement une prop allongée, n'est-ce pas ? Oui, vous avez compris.

```js
function App() {
  const [profile, setProfile] = useState({ame: 'John'}); 
  return ( 
    <div> 
      <Header profile={profile} /> 
    </div> 
  ); 
} 
  
function Header({ profile }) { 
  return ( 
    <header> 
      <h1>This is the header</h1> 
      <Content profile={profile} /> 
    </header> 
  ); 
} 

function Content({ profile }) { 
  return ( 
    <main> 
      <h2>Content Component</h2> 
      <p>{profile.name}</p> 
    </main> 
  ); 
} 

export default App;
```

Dans le code ci-dessus, vous pouvez observer que la `prop` transmise à `Header` est créée dans le composant `App`. Ensuite, `Header` la transmet à son composant enfant nommé `Content`. Par conséquent, le `profile` transmis peut être considéré comme allongé car il est passé à travers un composant (`Header`) qui ne le crée ni ne le consomme jusqu'à celui qui le fait.

Le composant `Header` transmettant la `prop` qu'il ne crée ni n'a besoin étire inutilement le contexte de la `prop`. 

Maintenant, la question est, comment les props allongées aident-elles à éviter intuitivement le prop drilling dans React ? Elles vous permettent de repérer facilement les `props` utilisées là où elles ne sont ni créées ni consommées.

Plutôt que de se concentrer sur la façon de résoudre le prop drilling, les props allongées vous permettent de l'éviter. Cela est dû au fait qu'il est intuitif de reconnaître lorsqu'un composant ne crée ni ne consomme de `props`, et cela vous aide à savoir que le composant est irrélevant.

Mais avant d'apprendre comment éviter rapidement le prop drilling avec votre compréhension des props allongées, il est important que vous connaissiez les principales causes du prop drilling. Ensuite, vous saurez vraiment comment l'éviter sans y penser.

## Qu'est-ce qui cause le Prop Drilling ?

![Quelle est votre histoire ?](https://images.unsplash.com/photo-1617575521317-d2974f3b56d2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMTc3M3wwfDF8c2VhcmNofDF8fHRyaWdnZXJ8ZW58MHx8fHwxNjk5MzIzNTU2fDA&ixlib=rb-4.0.3&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@etiennegirardet?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Etienne Girardet</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

Le prop drilling ne se produit pas par magie. C'est une conséquence d'une organisation inadéquate des composants, et ce n'est pas un problème de React. C'est un problème de réflexion ou de conception. 

Vous ne rencontrerez pas une instance de prop drilling sans observer une des erreurs de mise en page suivantes :

Tout d'abord, **regrouper des éléments statiques et des composants dépendants** ensemble pour obtenir une conception UI attrayante est la principale cause du prop drilling. Vous ne pouvez pas éviter le prop drilling lorsque votre UI regroupe des éléments statiques et des composants dépendants ensemble dans un parent. Le composant parent n'utilisera clairement pas la `prop`, car tout ce qu'il contient est un élément statique – sauf le composant qui a besoin d'une prop.

Voici un exemple :

```js
function Header({ profile }) { 
  return ( 
    <header> 
      <h1>This is the header</h1> 
      <Content profile={profile} /> 
    </header> 
  ); 
}
```

Dans ce cas, les éléments statiques `<header> et <h1>` sont regroupés avec un composant dépendant `Content` – et c'est pourquoi nous avons du prop drilling.

À condition que le composant `Content` soit indépendant ou ne prenne pas de `props`, il n'aura pas besoin de `profile` et il n'y aura pas de prop drilling en premier lieu. C'est pourquoi forcer un composant qui devrait être indépendant à prendre des `props` de son parent est une recette pour le prop drilling dans React.

Deuxièmement, lorsqu'un **composant accepte des `props` qu'il n'utilise pas mais les transmet simplement à ses enfants**, c'est un signe que vous avez du prop drilling dans votre composant :

```js
function App () { 
  const [profile, setProfile] = useState({name: "Ayobami"})
  return ( 
    <>
      <Parent profile={profile} /> 
    </>
 ); 
}; 

function Parent({ profile }) { 
  return ( 
    <div>
      <Hero profile={profile} /> 
      <Features profile={profile} /> 
    </div>
 ); 
}; 
```

Dans ce cas, il y a du prop drilling car le composant `Parent` prend `profile` et ne l'utilise pas bien qu'il le transmet à ses enfants. 

Troisièmement, lorsqu'un composant représentant une section indépendante d'une page est **forcé à prendre des props de son parent**, le prop drilling est inévitable. Il devrait idéalement être autonome avec son état et ses opérations. 

L'exception serait s'il est intentionnellement lié à son parent pour des raisons spécifiques. Dans de tels cas, le prop drilling devient un compromis nécessaire.  

Si vous revisitez l'exemple de prop drilling cité dans cet article, vous réaliserez qu'il a un problème de prop drilling car le composant `Content`, qui aurait pu être un composant indépendant en ayant un état, est forcé de recevoir des props de son parent.

Et enfin, **la présence de `props` allongées** est un signe certain de prop drilling. Puisqu'une prop allongée est un élément fondamental qui est constamment présent dans chaque cas de prop drilling, comprendre ce concept vous permet d'éviter instinctivement le prop drilling. 

Lorsque vous repérez une prop allongée, vous pouvez être certain qu'une des trois autres erreurs est également en jeu. En bref, une prop allongée est une prop qui n'est pas consommée et qui est également transmise à un autre composant.

Ainsi, regrouper des éléments statiques avec des composants dépendants, forcer des composants à prendre des props, des props allongées, et recevoir une prop sans la consommer sont les signes pour reconnaître le prop drilling dans React.

## Comment corriger le Prop Drilling avec la Composition de Composants

La composition de composants est une bonne approche pour corriger le prop drilling. Si vous vous trouvez dans une situation où un composant transmet une prop qu'il ne crée ni ne consomme, vous pouvez utiliser la composition de composants pour le corriger. 

Mais pour utiliser la composition de composants, vous devez comprendre un contexte de composant.

### Qu'est-ce qu'un contexte de composant ?                           

Le contexte d'un composant englobe tout ce qui est visible à l'intérieur, y compris l'état, les props et les enfants. Le code suivant illustre davantage ce concept :

```js
function App() { 
  const [profile, setProfile] = useState({name: 'Ayobami'}); 
  return ( 
    <div> 
      <Header profile={profile} /> 
    </div> 
  ); 
} 

export default App;
```

Dans ce scénario, le contexte de `App` fait référence à tout ce que nous pouvons voir à l'intérieur du composant `App` – y compris la prop `profile`, le `Header`, et d'autres contenus de `App`. Par conséquent, toute donnée créée dans le composant `App` devrait idéalement être utilisée à l'intérieur du composant `App` lui-même, soit comme ses propres données, soit comme `props` pour ses enfants.

Le prop drilling apparaît toujours lorsque les enfants recevant les `props` ne les consomment pas mais les transmettent simplement à leurs enfants.  

Pour éviter le prop drilling dans ce cas, tout composant petit-enfant nécessitant un accès aux mêmes `props`, surtout lorsque leur parent ne consomme pas les données, devrait être passé en tant qu'enfants en veillant à ce que les données restent dans le contexte de `App`.

```js
export function App() { 
  const [profile, setProfile] = useState({name: 'Ayobami'}); 
  return ( 
    <div> 
      <Header> 
        <Content profile={profile} /> 
      </Header> 
    </div> 
  ); 
}
```

**`Ou`**

```js
export function App() { 
  const [profile, setProfile] = useState({name: 'Ayobami'}); 
  return ( 
    <div> 
      <Header children={<Content profile={profile} />} > 
    </div> 
  ); 
}
```

Comme vous pouvez le voir, nous avons résolu le problème de prop drilling dans l'exemple précédent, même si nous avons toujours un composant redondant, `<Header>`, n'est-ce pas ? Nous avons réussi à résoudre le prop drilling grâce à la composition de composants. 

Ce processus est assez simple car nous nous concentrons sur la reconnaissance des props allongées et leur repositionnement dans des contextes appropriés.

Le concept de prop drilling est axé sur les problèmes, mais l'allongement des props est orienté vers les solutions. Lorsque nous traitons des props allongées, notre objectif principal est d'identifier les props qui ne sont pas consommées mais simplement transmises à d'autres composants.

## Comment corriger le Prop Drilling en déplaçant l'état vers le consommateur

Le prop drilling peut également être corrigé en déplaçant l'état là où il est consommé. L'exemple de prop drilling dans cet article a un composant nommé `Content`. Mais le composant est forcé de recevoir une `prop` de son parent au lieu d'avoir un état et d'être un composant indépendant – et ainsi nous avons du prop drilling. 

Nous pouvons corriger le prop drilling dans ce cas en déplaçant l'état du profil là où il est consommé.

Revisitons l'exemple :

```js
function App() {
  const [profile, setProfile] = useState({ame: 'John'}); 
  return ( 
    <div> 
      <Header profile={profile} />
      <Footer profile={profile />
    </div> 
  ); 
} 
  
function Header({ profile }) { 
  return ( 
    <header> 
      <h1>This is the header</h1> 
      <Content profile={profile} /> 
    </header> 
  ); 
} 

function Content({ profile }) { 
  return ( 
    <main> 
      <h2>Content Component</h2> 
      <p>{profile.name}</p> 
    </main> 
  ); 
} 

export default App;
```

Nous pouvons corriger le prop drilling dans ce cas en déplaçant `profile` là où il est consommé :

```js
function App() { 
  return ( 
    <div> 
      <Header />
      <Footer profile={profile />
    </div> 
  ); 
} 
  
function Header() { 
  return ( 
    <header> 
      <h1>This is the header</h1> 
      <Content /> 
    </header> 
  ); 
} 

function Content({ profile }) { 
  const [profile, setProfile] = useState({ame: 'John'});
  return ( 
    <main> 
      <h2>Content Component</h2> 
      <p>{profile.name}</p> 
    </main> 
  ); 
}
```

Maintenant que nous avons déplacé le profil vers le composant `Content` où il est consommé, le composant `App` n'a pas d'état, tandis que le composant `Header` ne reçoit plus de prop car le composant `Content` a son propre état.

Mais attendez ! Il y a un problème. Le composant `Footer` a besoin de l'état que nous avons déplacé de `App`. Vous voyez ! C'est le problème avec le déplacement ou le déplacement de l'état là où nous pensons qu'il est nécessaire. Dans ce cas, si le composant `Footer` n'en a pas besoin, nous n'aurons aucun problème – mais `Footer` a également besoin de la prop. 

Maintenant que `Footer` a besoin de `profile` comme prop, nous devons résoudre le prop drilling avec une autre méthode.

## Comment corriger le Prop Drilling avec une Stratégie de Remplacement Enfant-Parent

Plus tôt dans cet article, nous avons parlé de la façon d'utiliser la composition de composants et de déplacer l'état vers son consommateur pour résoudre le prop drilling. Mais comme vous l'avez vu, ils ont quelques problèmes – composants ou états dupliqués.

Mais l'utilisation de cette approche de remplacement enfant-parent résout le problème efficacement :

**Fonctionne mais pourrait être mieux :**

```js
export function App() { 
  const [profile, setProfile] = useState({name: 'Ayobami'}); 
  return ( 
    <div> 
      <Header> 
        <Content profile={profile} /> 
      </Header> 
    </div> 
  ); 
}

function Header({ profile }) { 
  return ( 
    <header> 
      <h1>This is the header</h1> 
      <Content profile={profile} /> 
    </header> 
  ); 
}
```

L'exemple ci-dessus montre une solution à l'exemple de prop drilling dans cet article. Mais comme vous pouvez le voir, il a un composant redondant, car `Header` ne fait rien.

**Voici une version meilleure :**

```js
export function App() { 
  const [profile, setProfile] = useState({name: 'Ayobami'}); 
  return ( 
    <header> 
      <h1>This is the header</h1> 
      <Content profile={profile} /> 
    </header> 
  ); 
}
```

Dans le code ci-dessus, nous améliorons la solution de composition de composants que nous avons précédemment mise en œuvre pour l'exemple de prop drilling en remplaçant le composant redondant `Header` par son contenu dans son parent (`App`).

## Ce qu'il faut éviter

![Image](https://images.unsplash.com/photo-1587065915399-8f8c714ab540?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMTc3M3wwfDF8c2VhcmNofDEwfHxkYW5nZXJ8ZW58MHx8fHwxNjk5MzIzMDgxfDA&ixlib=rb-4.0.3&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@edwinhooper?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Edwin Hooper</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

Il est essentiel de souligner ce qu'il faut éviter lors de la gestion du prop drilling pour prévenir des défis inutiles.

* **Évitez le Contexte React, si possible, pour corriger le prop drilling.** Cette approche lie votre composant à un contexte spécifique, restreignant son utilité en dehors de ce contexte et entravant la composition et la réutilisabilité.
* **Évitez les composants redondants en employant une approche de remplacement enfant-parent.** Cette approche incorpore naturellement la [composition de composants](https://www.codementor.io/@dinerismail/the-power-of-component-composition-in-react-21goassg4m) sans introduire de composants ou d'états redondants lors de la résolution du prop drilling.

En évitant les props allongées, vous ouvrez la voie à la création de composants React maintenables, performants, réutilisables et scalables. Cela simplifie le processus de levée des états et des composants en éliminant la lutte pour décider où les placer. 

Avec votre compréhension des props allongées, vous pouvez positionner en toute confiance les props et les composants dans le bon contexte sans stress excessif.

En bref, vous pouvez maintenant découvrir le prop drilling intuitivement en prêtant attention à tout composant qui prend des `props` qu'il ne consomme pas et les transmet simplement à un autre composant. 

Merci d'avoir lu – santé !

Hey attendez ! Je suis [Ayobami Ogundiran](https://twitter.com/codingnninja) et je suis sur le point de commencer à montrer comment construire vos propres sites React, Redux, TypeScript, Zod ou Ecommerce sur ma chaîne YouTube. [Cliquez pour vous abonner](https://youtube.com/youtoocancode) pour rester connecté.
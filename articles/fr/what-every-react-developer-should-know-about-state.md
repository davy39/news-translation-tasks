---
title: Ce que tout développeur React doit savoir sur l'état
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-16T17:31:00.000Z'
originalURL: https://freecodecamp.org/news/what-every-react-developer-should-know-about-state
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/5-things-every-react-developer-should-know-about-state.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'State Management '
  slug: state-management
seo_title: Ce que tout développeur React doit savoir sur l'état
seo_desc: "One of the most important concepts for every React developer to understand\
  \ is state – what it is, how to properly use it, and how to avoid common pitfalls\
  \ as you build your applications. \nLet's cover five of the most essential parts\
  \ of state that you..."
---

L'un des concepts les plus importants pour tout développeur React à comprendre est l'état – ce qu'il est, comment l'utiliser correctement et comment éviter les pièges courants lors de la construction de vos applications. 

Examinons cinq des parties les plus essentielles de l'état que vous devez connaître. Chacune de ces parties s'appuie sur les autres pour aider votre compréhension globale d'un sujet quelque peu complexe.

Pour rendre ces concepts abstraits aussi clairs que possible, j'ai inclus de nombreux exemples pratiques que vous pouvez exécuter dans Code Sandbox ou dans n'importe quel projet React que vous avez configuré.

## 1. Les mises à jour d'état avec useState ne sont pas fusionnées

Un défi auquel de nombreux développeurs React sont confrontés lors du passage des composants basés sur des classes aux composants fonctionnels avec les hooks React est que les mises à jour d'état utilisant des objets ne sont plus automatiquement fusionnées.

Un grand avantage du hook useState est que nous pouvons l'appeler autant de fois que nous le souhaitons pour utiliser autant de variables d'état que nécessaire.

Dans cet exemple, nous avons un formulaire de base avec des champs pour l'email et le mot de passe. Nous gérons l'état de l'email et du mot de passe comme des variables d'état individuelles :

```js
import React from "react";

export default function App() {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");

  return (
    <form>
      <input
        name="email"
        type="email"
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        name="password"
        type="password"
        placeholder="Mot de passe"
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

Modifions notre exemple pour gérer l'état du formulaire dans un seul objet. Cela nous permet d'appeler useState une seule fois, où l'email et le mot de passe ne sont pas gérés par des variables d'état individuelles mais comme des propriétés de cette variable d'état appelée `state`.

_Comment mettons-nous à jour l'état de manière appropriée avec la fonction `setState` lorsqu'il s'agit d'un objet ?_

Si nous devions utiliser un gestionnaire d'événements générique connecté à la prop `onChange` de chaque champ de notre formulaire, cela ressemblerait à ceci :

```js
import React from "react";

export default function App() {
  const [state, setState] = React.useState({
    email: '',
    password: ''
  })

  function handleInputChange(e) {
    setState({
      [e.target.name]: e.target.value
    })
  }

  return (
    <form>
      <input
        name="email"
        type="email"
        onChange={handleInputChange}
      />
      <input
        name="password"
        type="password"
        onChange={handleInputChange}
      />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

Nous mettons maintenant à jour la valeur de chaque champ dans l'état selon le nom du champ que l'utilisateur est en train de taper.

Ce modèle est couramment utilisé pour mettre à jour l'état dans les composants basés sur des classes, mais cela ne fonctionne pas avec le hook useState. Les mises à jour d'état avec la fonction `setState` de useState ne sont pas automatiquement fusionnées.

_Que signifie cela ?_

Cela signifie que chaque fois que nous définissons l'état lorsque l'utilisateur tape, l'état précédent n'est pas inclus dans le nouvel état. Si nous devions journaliser notre nouvel état mis à jour lorsque nous tapons dans notre formulaire, nous verrions ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/5-things-every-react-developer-should-know-about-state-1.gif)

Puisque l'état précédent n'est pas automatiquement fusionné dans le nouvel objet d'état, nous devons fusionner manuellement notre objet d'état avec ses propriétés précédentes en utilisant l'opérateur de propagation d'objet :

```js
import React from "react";

export default function App() {
  const [state, setState] = React.useState({
    email: '',
    password: ''
  })

  function handleInputChange(e) {
    setState({
      // propagation de l'état précédent avec l'opérateur de propagation d'objet
      ...state,
      [e.target.name]: e.target.value
    })
  }

  return (
    <form>
      <input
        name="email"
        type="email"
        onChange={handleInputChange}
      />
      <input
        name="password"
        type="password"
        onChange={handleInputChange}
      />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

Avec le hook useState, nous avons la flexibilité de gérer plusieurs valeurs primitives ou d'utiliser un objet avec plusieurs propriétés.

Si vous utilisez useState avec un objet, cependant, n'oubliez pas de propager l'état précédent lors de la mise à jour pour vous assurer qu'il est mis à jour correctement.

## 2. Les hooks d'état déclenchent un re-rendu, useRef non

L'état React a une relation très importante avec le rendu des composants.

Chaque fois que nous retournons du JSX à partir d'un composant React, lorsque ce composant est utilisé, il sera rendu et donc affiché dans notre application. React s'occupe de ce processus de rendu.

Si notre composant utilise un état, nous devons comprendre qu'il doit être rendu à nouveau – c'est-à-dire, re-rendu – en réponse à toute mise à jour d'état.

_Pourquoi les composants doivent-ils être re-rendus lors des mises à jour d'état ?_

Parce que si nous ne re-rendions pas lors de la mise à jour de l'état, nous ne pourrions pas afficher les nouvelles données. Cela est très simplement exprimé, chaque fois que nous affichons un état contenu dans une variable d'état dans notre JSX.

Si cela ne re-rendait pas chaque fois que nous apportons des modifications à cette variable, les mises à jour ne seraient pas affichées.

Cela semble être un concept plutôt simple, mais vous devez comprendre que **chaque fois que nous mettons à jour l'état, cela provoque non seulement un re-rendu dans le composant qui gère directement l'état – cela provoque également un re-rendu dans tous les composants enfants**.

_Pourquoi cela est-il important ?_ Parce que dans certains cas, nous ne voulons pas qu'un composant enfant soit re-rendu en réponse à un re-rendu d'un composant parent.

_Quel est un exemple de ce cas ?_ Supposons que nous avons une application où un utilisateur peut taper dans un champ dont la valeur est gérée par l'état. Cette application a également un autre composant qui affiche une liste de données.

Chaque fois que l'utilisateur tape dans le champ, notre état est mis à jour, et cela provoque un re-rendu inutile dans cet autre composant enfant.

La façon dont nous pouvons corriger cela est avec l'aide de la fonction `React.memo`, qui aide à empêcher notre composant d'être re-rendu lorsque le composant parent est re-rendu :

```js
export default function App() {
  const [skill, setSkill] = React.useState("");
  const [skills, setSkills] = React.useState(["HTML", "CSS", "JavaScript"]);

  function handleChangeInput(event) {
    setSkill(event.target.value);
  }

  function handleAddSkill() {
    setSkills(skills.concat(skill));
  }

  return (
    <>
      <input onChange={handleChangeInput} />
      <button onClick={handleAddSkill}>Ajouter une compétence</button>
      <SkillList skills={skills} />
    </>
  );
}

/* Mais le problème, si vous exécutez ce code vous-même, est que lorsque nous tapons dans le champ, parce que le composant parent de SkillList (App) est re-rendu, en raison de la mise à jour de l'état à chaque frappe, SkillList est re-rendu constamment (comme indiqué par le console.log) */

/* Cependant, une fois que nous enveloppons le composant SkillList dans React.memo (qui est une fonction d'ordre supérieur, ce qui signifie qu'elle accepte une fonction comme argument), il ne se re-rend plus inutilement lorsque notre composant parent le fait. */
const SkillList = React.memo(({ skills }) => {
  console.log("re-rendu");
  return (
    <ul>
      {skills.map((skill, i) => (
        <li key={i}>{skill}</li>
      ))}
    </ul>
  );
});
```

Une autre chose à noter ici est qu'il existe techniquement un moyen de gérer l'état sans provoquer de re-rendu. Nous pouvons le faire avec un hook que la plupart des gens ne considèrent pas comme un hook React étatique – `useRef`.

useRef peut être utilisé pour stocker n'importe quelle valeur dans sa propriété `.current`. En d'autres termes, si nous voulions faire un simple compteur avec useRef et mettre à jour une valeur de compte que nous y avons stockée, même si nous mettons à jour sa valeur, il n'afficherait pas le compte correct après le rendu initial car cela ne déclenche pas de re-rendu :

```js
import React from "react";

export default function App() {
  const countRef = React.useRef(0);

  function handleAddOne() {
    countRef.current += 1;
  }

  return (
    <>
      <h1>Compte : {countRef.current}</h1>

      {/* cliquer sur ceci ne changera pas l'affichage du compte */}
      <button onClick={handleAddOne}>+ 1</button>
    </>
  );
}
```

## 3. Les mises à jour d'état doivent être immuables

Une partie très importante de l'état dans React est qu'il doit être mis à jour et géré de la bonne manière.

En ce qui concerne la gestion de l'état avec le hook useState, nous devons _uniquement_ utiliser la fonction de définition dédiée fournie comme deuxième élément dans le tableau que nous obtenons de useState pour le mettre à jour. Si nous ne le faisons pas et que nous tentons de le mettre à jour manuellement, avec l'aide de JavaScript simple par exemple, notre application ne fonctionnera pas comme nous l'attendons.

Ce point est très étroitement lié au point précédent que nous avons fait : l'état, lorsqu'il est mis à jour _correctement_, provoque un re-rendu de notre composant.

Que pensez-vous qu'il se passera si nous tentons de mettre à jour l'état à notre manière au lieu de la manière "React" ?

Encore une fois, React est ce qui prend en charge l'affichage et le rendu de notre composant correctement lorsqu'il y a un changement. Si nous n'utilisons pas React, alors nous ne pouvons pas nous attendre à ce que notre application reflète les changements que nous avons apportés à l'état.

En d'autres termes, **si nous mettons à jour l'état avec JavaScript simple et non `setState`, cela ne déclenchera pas de re-rendu et React n'affichera pas ces changements (invalides) dans l'état à notre utilisateur.**

C'est une leçon simple, mais cruciale à retenir.

Nous devons savoir comment mettre à jour l'état en utilisant React et choisir le hook d'état approprié pour nos besoins. Nous pourrions choisir `useReducer`, `useState`, ou une bibliothèque de gestion d'état tierce comme Redux.

Quelle que soit notre choix en matière de gestion d'état, nous devons mettre à jour l'état de manière appropriée et ne pas tenter de le mettre à jour ou de le muter directement.

L'autre raison pour cela, en plus du fait que notre application React ne fonctionnera pas correctement, est que cela viole un principe fondamental de React. Il s'agit du concept d'**immutabilité**.

Les mises à jour d'état doivent toujours être immuables. Cela signifie que nous ne devons pas apporter nos propres modifications ou muter les données stockées dans nos variables d'état. Faire cela rend notre état imprévisible et peut causer des problèmes non intentionnels dans notre application qui sont difficiles à déboguer.

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0);
  
  // Ne pas assigner l'état à de nouvelles variables (non-état)
  const newCount = count;
  // Ne pas muter directement l'état
  const countPlusOne = count + 1;

  return (
    <>
      <h1>Compte : {count}</h1>
    </>
  );
}
```

En plus de ne pas muter directement les variables d'état, assurez-vous de ne jamais assigner les variables d'état à d'autres variables (non-état).

## 4. Les mises à jour d'état sont asynchrones et planifiées

Une leçon cruciale à connaître sur les mises à jour d'état est qu'elles ne sont pas effectuées immédiatement.

Cela peut être vu si nous regardons la documentation React et voyons exactement ce qui se passe lorsque nous appelons la fonction `setState`. Nous l'utilisons pour mettre à jour la variable d'état qui lui est associée, mais on nous dit aussi :

> Elle accepte une nouvelle valeur d'état et met en file d'attente un re-rendu du composant.

_Que signifie ce mot "met en file d'attente" ?_

En d'autres termes, il ne re-rend pas le composant immédiatement. Il n'arrête pas notre code à cette ligne où nous mettons à jour l'état, mais cela se produit à un moment donné dans le futur. Cela est pour des raisons de performance et cela nous donne une meilleure idée de ce que React fait sous le capot.

Sur la base de ces informations, nous devons changer notre modèle mental lorsque nous tentons de mettre à jour l'état : **la fonction `setState` ne met pas à jour l'état immédiatement, elle planifie simplement une mise à jour d'état pour un moment dans le futur.** Après quoi, React s'occupe de déterminer quand cette mise à jour d'état a lieu.

Par conséquent, il n'est pas si facile de simplement regarder notre code et de voir exactement quand la mise à jour d'état s'est produite ou se produira.

Il est important de comparer cela à `useRef`, que nous avons mentionné précédemment comme pouvant conserver les données dans sa propriété current. Toute mise à jour effectuée avec useRef est effectuée de manière synchrone – nous pouvons regarder notre code et voir exactement quand une mise à jour donnée a été effectuée dans `useRef`, mais pas avec useState.

## 5. L'état obsolète peut se produire avec les fermetures

Enfin, un problème important qui peut survenir avec l'état React est le problème de l'état obsolète.

### Qu'est-ce que l'état obsolète dans React ?

L'état obsolète est un problème qui se produit chaque fois que nous essayons de mettre à jour l'état, souvent dans une fermeture.

> Une fermeture est un type de fonction en JavaScript, où nous utilisons une variable d'une portée externe.

Ce problème d'état obsolète est basé sur le fait que la fermeture pourrait ne pas capturer la valeur la plus à jour de la variable d'état. C'est ce que nous entendons par obsolète – nous voulons dire qu'elle est ancienne et non la valeur actuelle que nous voulons.

Ce problème d'état obsolète est étroitement lié au sujet que nous avons discuté précédemment, à savoir que les mises à jour d'état sont asynchrones.

Dans de nombreux cas, ce qui est un problème avec les mises à jour d'état asynchrones est que nous n'obtenons pas toujours la valeur précédente correcte de notre état, surtout si nous essayons de mettre à jour l'état en fonction de cette valeur précédente.

Nous pouvons exprimer le problème d'une fermeture obsolète dans une simple application de compteur qui met à jour le compte après une seconde en utilisant la fonction `setTimeout`.

Parce que setTimeout crée une fermeture, nous accédons à une valeur obsolète de notre variable d'état, `count`, lorsque nous appelons `setCount`.

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0);

  function delayAddOne() {
    setTimeout(() => {
      setCount(count + 1);
    }, 1000);
  }

  return (
    <>
      <h1>Compte : {count}</h1>
      <button onClick={delayAddOne}>+ 1</button>
    </>
  );
}
```

Le problème est apparent lorsque nous exécutons notre application. Malgré le fait de cliquer plusieurs fois sur le bouton, il n'est incrémenté que d'un chaque seconde :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/5-thing-every-react-developer-should-know-about-state-2.gif)

Nous pouvons corriger ce problème d'état obsolète dans notre fermeture en utilisant une méthode plus fiable de mise à jour de l'état. Les mises à jour d'état seront toujours planifiées, mais cela permettra d'obtenir de manière fiable la valeur précédente de l'état.

Nous le faisons avec l'aide de la fourniture d'une fonction interne à la fonction `setState`. Dans le corps de la fonction, nous pouvons obtenir l'état précédent dans les paramètres de cette fonction et ensuite retourner ce que nous voulons que le nouvel état soit.

Dans notre cas, il s'agira de la valeur précédente du compte incrémentée de un :

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0);

  function delayAddOne() {
    setTimeout(() => {
      // le problème d'état obsolète disparaît en utilisant la fonction interne
      setCount(prevCount => prevCount + 1);
    }, 1000);
  }

  return (
    <div>
      <h1>Compte : {count}</h1>
      <button onClick={delayAddOne}>+ 1</button>
    </div>
  );
}
```

> Une autre chose intéressante à noter si vous regardez la documentation React est que si rien n'est retourné par cette fonction, alors aucun re-rendu n'aura lieu.

Une fois que nous fournissons cette fonction interne à `setState` pour obtenir de manière fiable l'état précédent et retourner le nouvel état à partir de notre fonction, notre problème d'état obsolète dû à notre fermeture disparaît.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*
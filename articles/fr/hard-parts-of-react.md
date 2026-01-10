---
title: Comment apprendre les parties difficiles de React – et des conseils pour les
  maîtriser
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-02-26T21:07:53.000Z'
originalURL: https://freecodecamp.org/news/hard-parts-of-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Article-Cover.png
tags:
- name: React
  slug: react
seo_title: Comment apprendre les parties difficiles de React – et des conseils pour
  les maîtriser
seo_desc: "Have you started learning React, only to face bugs that made you contemplate\
  \ a career in goat herding? Don't worry – we've all been there. \nIn this guide,\
  \ you'll join me on a quest through the quirky wonders of React. I'll help you navigate\
  \ the perpl..."
---

Avez-vous commencé à apprendre React, pour faire face à des bugs qui vous ont fait envisager une carrière dans l'élevage de chèvres ? Ne vous inquiétez pas – nous sommes tous passés par là. 

Dans ce guide, vous me rejoindrez dans une quête à travers les merveilles excentriques de React. Je vous aiderai à naviguer dans les moments perplexes, en veillant à ce que vous n'ayez jamais à vous demander : "Qu'est-ce qui se passe avec React ?"

Que vous soyez un aventurier chevronné de React ou que vous découvriez les mystères des DOM virtuels, n'ayez crainte. Je suis là pour partager les récits de mes premières luttes, démystifier les bugs énigmatiques et ouvrir la voie à un voyage plus fluide.

### Prérequis

* Fondamentaux de HTML et CSS
* Fondamentaux de ES6 JavaScript et React

## **Ce que nous allons couvrir :**

1. [Récapitulatif rapide des fondamentaux de React](#heading-ce-que-nous-allons-couvrir)  
– [Composants : Les blocs de construction du Web](#heading-composants-les-blocs-de-construction-du-web)  
– [JSX : Où HTML rencontre JavaScript](#heading-jsx-ou-html-rencontre-javascript)  
– [État et Props : Le duo dynamique](#heading-etat-et-props-le-duo-dynamique)
2. [Les bons, les mauvais et les aspects difficiles de React](#les-bons-les-mauvais-et-les-aspects-difficiles-de-react)  
– [Les bons aspects de React](#heading-les-bons-aspects-de-react)  
– [Les mauvais aspects de React](#heading-les-mauvais-aspects-de-react)  
– [Les aspects difficiles de React](#heading-les-aspects-difficiles-de-react)  
		– [Erreurs de la prop key](#heading-erreurs-de-la-prop-key)  
		– [Mutation directe des états](#heading-mutation-directe-des-etats)  
		– [Bugs mystérieux avec le rendu conditionnel](#heading-bugs-mysterieux-avec-le-rendu-conditionnel)  
		– [Ignorer les tableaux de dépendances dans les Hooks React](#heading-ignorer-les-tableaux-de-dependances-dans-les-hooks-react)  
		– [Négliger le chaînage optionnel pour les données API](#heading-negliger-le-chainage-optionnel-pour-les-donnees-api)  
		– [Ignorer les Fragments React pour regrouper les éléments JSX](#heading-ignorer-les-fragments-react-pour-regrouper-les-elements-jsx)
3. [Approches opinionnées de React](#heading-approches-opinionnees-de-react)
4. [Conclusion du voyage excentrique avec React](#heading-conclusion-du-voyage-excentrique-avec-react)

## Récapitulatif rapide des fondamentaux de React

La bibliothèque React tourne autour de 3 blocs de construction : les Composants, le JSX, et l'État & Props.

### Composants : Les blocs de construction du Web

Imaginez les composants comme les briques LEGO de votre interface utilisateur – une pièce unique et réutilisable qui contribue à la grande structure. Ils encapsulent la fonctionnalité, le style et le comportement, rendant votre UI à la fois modulaire et évolutive. 

D'un simple bouton à une barre latérale élaborée, les composants sont le cœur et l'âme du développement React.

### JSX : Où HTML rencontre JavaScript

JSX, ou JavaScript XML, peut sembler une fusion étrange de HTML et JavaScript au premier abord, mais c'est assez simple. C'est la sauce secrète qui rend la syntaxe de React si expressive et dynamique. 

Avec JSX, vous écrivez vos composants UI en utilisant une syntaxe qui ressemble à HTML, mais en dessous, c'est du JavaScript pur.

### État et Props : Le duo dynamique

Le duo dynamique de l'état et des props donne vie aux pages React en ajoutant de l'interactivité à vos applications web.

#### État : Donner de la mémoire aux composants

L'état donne de la mémoire aux composants, leur permettant de se souvenir des événements passés et de modifier leur comportement au fil du temps. C'est la clé pour rendre votre UI réactive et dynamique. 

Imaginez un formulaire qui se souvient des entrées de l'utilisateur ou un compteur qui s'incrémente à chaque clic. C'est la magie de l'état.

#### Props : Permettre la communication

Les props (abréviation de propriétés) facilitent la communication entre les composants. Elles permettent aux composants parents de transmettre des données à leurs enfants, créant un flux d'informations sans faille. 

Pensez aux props comme des messagers, garantissant que chaque composant connaît son rôle et reçoit les informations nécessaires pour l'accomplir.

## Les bons, les mauvais et les aspects déroutants de React

Avant de plonger dans les aspects déroutants de React, il est essentiel de mettre en lumière les trésors qui font de React un véritable héros dans votre arsenal.

### Les bons aspects de React

#### Virtual DOM et ses avantages

Le Virtual DOM est un concept révolutionnaire qui donne à React sa vitesse et son efficacité. 

Lorsque des changements se produisent dans votre application, React ne met pas immédiatement à jour le DOM réel. Au lieu de cela, il travaille avec une copie légère, le Virtual DOM, en effectuant des ajustements minimaux et ultra-rapides. Cela optimise non seulement les performances, mais offre également une expérience utilisateur plus fluide.

```js
ReactDOM.createRoot(document.getElementById("root")).render(
    <App />
 );
```

Ce processus utilise [l'algorithme de différenciation de React](https://legacy.reactjs.org/docs/reconciliation.html) dans le Virtual DOM. Il identifie l'ensemble minimal de changements nécessaires dans le DOM réel pour refléter l'état mis à jour.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/00--Explaing-how-react-updates-the-UI-using-the-virtual-DOM.png)
_Explication de la manière dont React met à jour l'UI en utilisant le Virtual DOM_

#### Composants réutilisables

Dans React, le principe directeur est la réutilisabilité. Les composants, les blocs de construction fondamentaux dont nous avons discuté ci-dessus, peuvent être conçus et utilisés dans toute votre application. Cela favorise non seulement une structure de code modulaire et organisée, mais vous libère également du fardeau de réinventer la roue.

```js
// Composant Bouton réutilisable
const Button = ({ label, onClick }) => (
  <button onClick={onClick}>{label}</button>
);

// Utilisation
<Button label="Cliquez-moi" onClick={() => console.log("Bouton cliqué")} />
```

#### Liaison de données unidirectionnelle pour un flux prévisible

React impose un flux de données unidirectionnel, garantissant la prévisibilité et la maintenabilité. 

Les composants parents transmettent les données à leurs enfants via les props, et toute modification est supervisée par le composant parent. Cette rue à sens unique évite le chaos de la liaison de données bidirectionnelle observée dans d'autres frameworks.

```js
const ParentComponent = () => {
  const [data, setData] = useState("Bonjour depuis le Parent !");

  return <ChildComponent data={data} />;
};

const ChildComponent = ({ data }) => <div>{data}</div>;
```

### Les mauvais aspects de React

Il y a certaines parties de React qui ne sont pas idéales, cependant. Passons-les brièvement en revue maintenant pour que vous en soyez conscient.

#### Courbe d'apprentissage abrupte pour les débutants

Commencer avec React peut être difficile, surtout si vous êtes nouveau dans le développement web. Des concepts comme JSX, les composants et la gestion d'état peuvent sembler un labyrinthe. Mais ne vous inquiétez pas ! Avec un peu de pratique et de patience, cela devient plus facile, et React devient plus familier.

#### JSX peut vous dérouter au début

JSX, le mélange spécial de HTML et JavaScript, peut être un peu déroutant au début. C'est comme apprendre une nouvelle langue qui fusionne les deux. Mais à mesure que vous vous y habituez, vous verrez comment il rend votre code plus court et plus clair.

#### Défis de la gestion d'état

Utiliser l'état dans React est puissant, mais cela peut aussi être délicat. Gérer l'état à travers de nombreuses pièces différentes, surtout dans de grands projets, peut créer des configurations complexes et des problèmes potentiels. Heureusement, des outils comme [Redux](https://redux.js.org/) existent pour aider à gérer cette complexité.

## Les aspects difficiles de React

### Erreurs de la prop key

Lors de la construction de vos applications, vous pouvez souvent avoir des éléments répétitifs qui affichent des informations similaires ou partagent les mêmes styles. L'étape logique serait de boucler sur eux pour créer une liste d'éléments.

```js
function ListComponent() {
  const people = [{ name: "Mitchelle" }, { name: "July" }, { name: "David" }];
  return (
    <ul>
      {/ Boucle sur le tableau people pour créer des éléments de liste /}
      {people.map((person) => (
        <li>{person.name}</li>
      ))}
    </ul>
  );
}
```

Tout semble bien jusqu'à ce que vous remarquiez un avertissement dans votre console ou, pire, un comportement étrange dans la manière dont votre liste est rendue.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/02--The-console-an-error-due-to-missing-key-prop.png)
_La console affiche une erreur due à l'absence de la prop key_

React utilise des clés pour mettre à jour et réorganiser les éléments dans une liste. Lorsque vous oubliez de fournir une prop key ou si les clés ne sont pas uniques, React se perd un peu. C'est comme essayer de suivre les éléments dans le tableau sans aucun identifiant spécifique – les choses se mélangent, et vous pourriez finir avec des bugs inattendus dans votre UI.

#### Comment résoudre ce problème

Le premier instinct de nombreux développeurs lorsqu'ils sont confrontés à la création de listes dynamiques est d'utiliser la propriété d'index comme clé. Cela semble être une solution pratique, car l'index fournit un identifiant unique pour chaque élément dans le tableau – mais ce n'est pas la meilleure approche pour les raisons suivantes :

* **Non persistant** : Si l'ordre ou le nombre d'éléments change, React peut se confondre. Par exemple, si un élément est ajouté ou supprimé du début de la liste, tous les indices suivants changent, provoquant des problèmes potentiels de re-rendu.
* **Mutations de tableau** : Des opérations comme le tri ou le filtrage peuvent altérer l'ordre des éléments, brisant l'association entre l'index et l'élément réel.
* **Problèmes de performance** : React s'appuie sur les clés pour des mises à jour efficaces. Utiliser l'index comme clé peut affecter les performances lors de la gestion de grandes listes ou de mises à jour fréquentes.

Certaines des meilleures alternatives incluent :

* **Utiliser un ID unique** : Si chaque élément de votre tableau possède un identifiant unique, comme une propriété `id`, utilisez celui-ci comme clé.

```js
{people.map((person) => (
  <li key={person.id}>{person.name}</li>
))}
```

* Générer une clé unique : Dans les cas où les éléments manquent d'un identifiant unique naturel, envisagez d'utiliser une fonction comme `crypto.randomUUID()` pour générer une clé unique.

```js

function ListComponent() {
  const people = [
    { name: "Mitchelle", age: 25, occupation: "Ingénieur" },
    { name: "July", age: 30, occupation: "Médecin" },
    { name: "David", age: 35, occupation: "Artiste" }
  ];

  // Générer des ID uniques pour chaque personne avant le rendu
  const peopleWithIds = people.map(person => ({
    ...person,
    id: crypto.randomUUID(),
  }));

  return (
    <ul>
      {/* Boucle sur le tableau people pour créer des éléments de liste */}
      {peopleWithIds.map((person) => (
        <li key={person.id}>{person.name}</li>
      ))}
    </ul>
  );
}
```

En choisissant l'une de ces alternatives, vous fournissez à React des clés stables et uniques, l'aidant à gérer et mettre à jour vos listes dynamiques.

**Note** : Vous pourriez penser « Si `crypto.randomUUID` génère un ID unique, (`Math.random()` * un grand nombre) fonctionnerait de la même manière, non ? »

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Nope.gif)
_Gif Nope_

`Math.random()` pourrait également suffire comme clé, mais c'est une mauvaise idée car les clés générées ne seront pas stables entre les re-rendus, entraînant des problèmes de performance potentiels et des incohérences de rendu.

### Mutation directe des états

Imaginez que vous travaillez sur un composant qui gère un tableau de noms. Plutôt que d'utiliser la méthode de définition appropriée pour mettre à jour l'état, vous décidez de muter directement l'état.

```js
const MutableStateComponent = () => {
  const [names, setNames] = useState(["David", "John", "Steph", "Anthony"]);

  const removeLastName = () => {
    console.log(names);
    // Mutation directe de l'état en utilisant pop()
    names.pop();
    setNames(names); // Cela ne déclenchera pas de re-rendu
  };

  return (
    <div>
      <p>Noms : {names.join(", ")}</p>
      <button onClick={removeLastName}>Supprimer le dernier nom</button>
    </div>
  );
};
```

À votre grande surprise, l'UI ne se met pas à jour comme prévu, et vous vous retrouvez dans un scénario où la liste des noms semble gelée. Ne vous y trompez pas, le tableau est bien mis à jour comme vu ci-dessous :

![Image](https://lh7-us.googleusercontent.com/yey1I5L7W43d8vcNl7kEUZaRHGZw90xZfviK3rhfFHiqwXv3gsCjHqcs9nhgdWoQlbPEGAj2A_7qHcoeRI9xPtsD0JCiPJdzT4MNRrQ91GfUjdwvW4hmlHGE_LtdG49FzO1buO0yT9tzMRtO95MgvYI)
_Le tableau est muté avec la mise à jour de l'UI_

#### Quel est le problème ?

React repose sur un état immuable pour des mises à jour efficaces, et lorsque vous contournez ce mécanisme, cela perturbe le flux de données unidirectionnel. 

Dans ce cas, l'utilisation de `pop()` mute le tableau original en place, et React perd la trace des changements. Cela conduit à un rendu inexact du composant.

#### Comment résoudre ce problème

Pour vous assurer que votre composant se comporte comme prévu et suit les principes de React, utilisez toujours la fonction de définition (`setNames`) pour mettre à jour l'état.

```js
const MutableStateComponent = () => {
  const [names, setNames] = useState(["David", "John", "Steph", "Anthony"]);

  const removeLastName = () => {
    // Utiliser setNames pour mettre à jour l'état
    setNames((prevNames) => prevNames.slice(0, -1));
    console.log(names);
  };

  return (
    <div>
      <p>Noms : {names.join(", ")}</p>
      <button onClick={removeLastName}>Supprimer le dernier nom</button>
    </div>
  );
};
```

En utilisant `setNames` et en créant un nouveau tableau avec les changements souhaités (dans ce cas, en utilisant `slice` pour supprimer le dernier élément), vous vous assurez que React peut suivre et mettre à jour l'état avec précision, ce qui donne le comportement attendu de l'UI.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/09--Result-of-Mutating-States-with-the-correct-method.gif)
_Résultat de la mutation des états avec la méthode correcte_

### Bugs mystérieux avec le rendu conditionnel

Le rendu conditionnel, bien que puissant, peut introduire des bugs subtils s'il n'est pas géré avec soin. Comprendre les pièges courants, en particulier ceux liés aux évaluations de valeurs vraies et fausses, est crucial pour prévenir les comportements de rendu mystérieux.

Considérez l'exemple suivant :

```js
const IncorrectConditionalComponent = ({ showContent }) => (
  {showContent && <div>Montrez-moi si vrai !</div>}
);
```

#### Le bug : Rendu inattendu avec des valeurs fausses

Dans cet extrait de code, si `showContent` se trouve être une valeur fausse, comme `0`, le composant affichera un résultat inattendu. Au lieu de ne pas rendre le contenu de manière élégante, il affichera `0` à l'écran en raison de l'inclusion directe des accolades.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Gotcha.gif)
_Gif I gotcha_

#### Quel est le problème ?

Le problème réside dans la mauvaise gestion des valeurs vraies et fausses. L'utilisation directe des accolades crée un wrapper d'objet (`[object Object]`), amenant le composant à rendre quelle que soit la valeur présente, même si elle est fausse.

#### Comment résoudre ce problème

Pour détecter les bugs de rendu liés aux valeurs vraies et fausses, utilisez une vérification conditionnelle plus explicite.

```js
const CorrectConditionalComponent = ({ showContent }) => (
  showContent ? <div>Montrez-moi si vrai !</div> : null
);
```

Dans cette version corrigée, l'opérateur ternaire garantit une vérification claire de la véracité, empêchant les problèmes de rendu inattendus. En gérant explicitement les valeurs vraies et fausses, vous construisez des composants robustes qui se comportent de manière prévisible dans divers scénarios.

### Ignorer les tableaux de dépendances dans les Hooks React

Imaginez travailler sur un composant qui dépend d'un effet pour exécuter une logique lorsque l'état change, disons `count`. Mais même si vous incrémentez le compteur, l'effet ne semble pas s'exécuter, et vous vous demandez pourquoi votre logique ne prend pas effet.

```js
const Counter = () => {
  const [count, setCount] = useState(0);

  const handleClick = () => {
   
    setCount((count) => count + 1);
  };

  useEffect(() => {
    console.log("La valeur actuelle du compteur est ", count);
  }, []);

  return (
    <div>
      <p>Compteur : {count}</p>
      <button onClick={handleClick}>Incrémenter</button>
    </div>
  );
};
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/03--testing-the-count-component-without-fixing-the-useEffect-dependency-array.gif)
_Test du composant de compteur sans corriger le tableau de dépendances de useEffect_

#### Quel est le problème ?

Le problème réside dans la négligence du tableau de dépendances dans votre `useEffect`. Lorsque vous omettez les dépendances, React pourrait ne pas reconnaître que l'effet est lié à une pièce spécifique de l'état, conduisant à des données obsolètes et à un comportement inattendu.

#### Comment résoudre ce problème

Pour remettre votre effet sur les rails, incluez les dépendances pertinentes dans le tableau de dépendances. C'est comme mettre en place des déclencheurs – vous dites à React : "Hey, exécute cet effet chaque fois que ces pièces spécifiques de données changent."

```js
useEffect(() => {
    console.log("La valeur actuelle du compteur est ", count);
  }, [count]);
```

Ce qui déclenche maintenant le hook `useEffect` :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/04--testing-the-count-component-after-fixing-the-useEffect-dependency-array.gif)
_Test du composant de compteur après avoir corrigé le tableau de dépendances de useEffect_

### Négliger le chaînage optionnel pour les données API

Vous travaillez sur un composant qui affiche les données utilisateur récupérées depuis une API. Tout semble bien jusqu'à ce que vous rencontriez une erreur d'exécution inattendue. Le coupable ? Un opérateur de chaînage optionnel manquant.

#### Quel est le problème ?

Les réponses API peuvent être imprévisibles, et toutes les structures de données ne correspondent pas à vos attentes. Négliger le chaînage optionnel, surtout lors de l'accès à des propriétés profondément imbriquées (en vous regardant Strapi response data 👀) peut conduire à des erreurs d'exécution si une propriété est indéfinie.

#### Comment résoudre ce problème

Pour protéger votre composant contre les erreurs inattendues, incorporez le chaînage optionnel (`?.`) lors de l'accès aux propriétés imbriquées dans les données API.

Par exemple, disons que vous souhaitez lire une propriété profondément imbriquée (label) à partir de ces données :

```js
const data = {
    id: 1,
    title: "Premier élément",
    content: "Contenu pour le premier élément",
    category: {
      id: 101,
      name: "Catégorie A",
      description: "Description de la catégorie A",
      tags: [
        {
          id: 1001,
          label: "Tag 1",
        },
        {
          id: 1002,
          label: "Tag 2",
        },
      ],
    },
    author: {
      id: 201,
      name: "John Doe",
      email: "john.doe@example.com",
    },
  };
```

La bonne façon serait d'utiliser le chaînage optionnel pour récupérer ces données :

```js
 const firstLabel = data?.category?.tags?.[0]?.label;
```

Plutôt que d'accéder directement à ces propriétés :

```js
const firstLabel = data.category.tags[0].label;
```

Cela vous évite de voir une erreur d'écran blanc et une console inondée si la structure de données change. C'est comme mettre un filet de sécurité – si une propriété est manquante, votre application ne s'écroulera pas comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/05--Error-occuring-when-optional-chaining-isn-t-applied.png)
_Erreur se produisant lorsque le chaînage optionnel n'est pas appliqué_

### Ignorer les Fragments React pour regrouper les éléments JSX

Lorsque vous travaillez avec des composants React, vous pouvez rencontrer un scénario où vous souhaitez retourner plusieurs éléments JSX à partir d'une fonction, pour être accueilli par une erreur de syntaxe.

#### Quel est le problème ?

Cela est dû à une limitation en JavaScript, car il ne permet pas le retour d'éléments adjacents sans un parent commun.

Considérez le code problématique suivant :

```js
function User() {
  return <div> David Jaja</div>
         <div>Twitter: https://twitter.com/JajaDavid8</div>;
}
```

Ce code entraîne une erreur : « Les éléments JSX adjacents doivent être enveloppés dans une balise englobante. »

![Image](https://www.freecodecamp.org/news/content/images/2024/02/06--Error-occuring-when-JSX-returns-2-direct-adjacent-elements.png)
_Erreur se produisant lorsque JSX retourne 2 éléments adjacents directs_

#### Comment résoudre ce problème

Je sais ce que vous pourriez penser — pourquoi ne pas simplement envelopper les éléments dans une div et continuer ?

![Image](https://www.freecodecamp.org/news/content/images/2024/02/sponge-bob-bored.gif)
_Gif SpongeBob ennuyé_

Bien que cela semble être une solution rapide, cela introduit un inconvénient potentiel. En ajoutant une div, vous créez un élément parent inutile dans le DOM. 

Cette balise supplémentaire, bien que résolvant l'erreur immédiate, peut entraîner des conséquences imprévues, telles qu'affecter les styles ou la mise en page, et peut ne pas être conforme aux meilleures pratiques de codage. 

Et je suis sûr que vous ne voulez pas finir avec une « divpocalipse ». 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/07--Divpocalpse.png)
_Une divpocalipse_

Pour surmonter à la fois l'erreur de syntaxe et la balise DOM inutile, React a introduit une solution optimisée : les Fragments React.

Les Fragments React sont utilisés pour répondre au besoin de retourner plusieurs éléments JSX sans introduire d'éléments parents inutiles dans le DOM.

Voici comment vous pouvez utiliser les Fragments React :

```js
import React from "react";
function User() {
  return (
    <React.Fragment>
      <div> David Jaja</div>
      <div>Twitter: https://twitter.com/JajaDavid8</div>
    </React.Fragment>
  );
}
```

Ou en utilisant la syntaxe abrégée :

```js
function User() {
  return (
    <>
      <div> David Jaja</div>
      <div>Twitter: https://twitter.com/JajaDavid8</div>
    </>
  );
}

```

En utilisant les Fragments React, vous maintenez un code JSX propre et concis sans introduire d'éléments inutiles dans le DOM, améliorant la lisibilité du code.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Showing-the-DOM-tree-after-using-fragments-without-any-extra-elements.png)
_Montrant l'arborescence DOM après l'utilisation de fragments sans aucun élément supplémentaire_

## Approches opinionnées de React

J'ai trouvé quelques moyens pratiques pour rendre le travail avec React plus agréable. Au lieu de règles strictes, considérez cela comme mes choix personnels pour rendre le code plus facile à lire, améliorer son fonctionnement et garantir qu'il reste en bon état.

1. **Placer les données en dehors des composants** : Déplacez des éléments comme les listes et les groupes d'informations en dehors de la partie principale d'un composant lorsque cela est possible. Cela aide à éviter les mises à jour supplémentaires et simplifie la gestion des données sans utiliser de fonctions spéciales comme `useCallback`.
2. **Faire attention avec `React.memo`** : Utiliser `React.memo` peut aider vos composants à mieux fonctionner, mais ce n'est pas toujours nécessaire. Si un composant change souvent avec de nouvelles informations, utiliser `React.memo` pourrait ne pas être aussi utile. Utilisez-le judicieusement.
3. **Créer vos propres hooks React personnalisés** : J'aime aussi créer mes propres outils spéciaux avec des hooks React personnalisés. C'est un peu avancé, mais cela aide à garder mon code propre et organisé.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/but-thats-just-my-opinion-just-what-i-think.gif)
_Gif juste mon opinion_

## Conclusion du voyage excentrique avec React

Le voyage de React est un mélange de navigation fluide et de trajets cahoteux. Nous avons vu la force des composants réutilisables et du Virtual DOM, et nous avons abordé des moments déroutants comme les props clés manquantes et les bugs de rendu conditionnel, et ainsi de suite.

Alors que vous continuez votre voyage avec React, que votre code soit propre, vos composants réutilisables, et que vos moments « Qu'est-ce qui se passe avec React ? » se transforment en révélations « Aha ! ». Bon codage ! 🚀

### **Informations de contact**

Vous voulez me contacter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com
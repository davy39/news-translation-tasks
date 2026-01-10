---
title: Comment Créer un Hook React Personnalisé – Un Tutoriel Pratique
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-02-14T17:39:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-custom-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Custom-hooks.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment Créer un Hook React Personnalisé – Un Tutoriel Pratique
seo_desc: "If you have been working with React, I bet you've had the opportunity to\
  \ use hooks. But have you ever tried to create your own hook? \nToday I will help\
  \ you create your first custom hook and explain how they can improve your codebase.\n\
  Why Create Custo..."
---

Si vous avez travaillé avec React, je parie que vous avez eu l'occasion d'utiliser des hooks. Mais avez-vous déjà essayé de créer votre propre hook ?

Aujourd'hui, je vais vous aider à créer votre premier hook personnalisé et expliquer comment ils peuvent améliorer votre base de code.

## Pourquoi Créer des Hooks Personnalisés ?

Vous vous demandez peut-être – pourquoi voudrais-je créer un nouveau hook React ? Après tout, React dispose de tous les hooks essentiels et tout le reste semble légèrement excessif. C'est vrai, React vient avec de nombreux hooks puissants, mais saviez-vous que les hooks personnalisés peuvent améliorer la qualité de votre code ?

Imaginez que vous avez un morceau de code React utilisé dans de nombreux composants. En tant que programmeur, vous ne voulez pas vous répéter, et vous rendez le code répété réutilisable autant que possible. C'est pourquoi il est bon de wrap ces extraits dans des utilitaires, des composants ou des hooks personnalisés.

Créer vos propres hooks simplifiera non seulement vos composants, mais réduira également considérablement la taille de votre base de code. N'oubliez pas, moins de code signifie généralement une meilleure lisibilité et une complexité de code plus faible.

J'espère vous avoir maintenant "accroché" – jeu de mots intentionnel.

## **🛠🏻 Prérequis**

Avant de lire ce guide, vous devez être familier avec React. Ne vous méprenez pas – vous n'avez pas besoin d'être un expert, mais une compréhension des bases est nécessaire.

Si vous ne vous sentez pas assez fort en React, vous pourriez envisager de vous inscrire à [mon cours Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106) où vous apprendrez React 18 en créant un jeu 2048 à partir de zéro. Vous trouverez plus de détails et un code de réduction à la fin de ce tutoriel.

De plus, vous pouvez consulter [ce tutoriel gratuit](https://www.freecodecamp.org/news/learn-react-key-concepts/) où vous apprendrez les concepts clés nécessaires pour commencer avec React.

## 🦝 Votre Premier Hook Personnalisé – `usePreviousProps`

Dans mes articles, j'essaie toujours d'utiliser des exemples concrets – et ce guide ne fera pas exception. Nous allons créer un hook responsable du suivi des valeurs précédentes des props d'un composant. Cela signifie que nous allons construire un hook personnalisé appelé `usePreviousProps` à partir de zéro.

L'un des cas d'utilisation les plus courants pour un hook comme celui-ci est lorsque vous gérez des animations. Par exemple, imaginez que vous devez mettre en surbrillance un élément nouvellement créé. Comment pourriez-vous déterminer s'il est nouveau sans comparer les valeurs actuelles aux précédentes ? C'est là que notre nouveau hook entre en jeu.

Les avantages d'un hook personnalisé comme le nôtre peuvent sembler un peu vagues, mais c'est un outil vraiment puissant. Littéralement, le hook personnalisé `usePreviousProps` que nous allons créer aujourd'hui est utilisé dans certains de mes projets open source, et même dans quelques applications de niveau production que j'ai construites. Vous pouvez donc être sûr que ce hook a un cas d'utilisation réel, et il ne prend que 12 lignes à implémenter.

Maintenant, mettons les mains dans le cambouis !

## 🦚 Comment Créer un Hook Personnalisé

Tout d'abord, nous devons créer un nouveau fichier dans le répertoire `hooks` de votre projet – j'ai décidé de l'appeler `use-previous-props.js`.

Gardez à l'esprit que les hooks React utilisent rarement la syntaxe JSX (HTML), c'est pourquoi nous utilisons l'extension `.js`. Si vous avez besoin d'activer la syntaxe JSX, vous devez changer l'extension en `.jsx`. Mais réfléchissez bien avant de le faire – si vous avez vraiment besoin de JSX, vous devriez probablement créer un composant autonome au lieu d'un hook.

```js
// fichier: hooks/use-previous-props.js

import { useEffect, useRef } from "react";

export default function usePreviousProps(value) {
  const ref = useRef();

  useEffect(() => {
    ref.current = value;
  });

  return ref.current;
}

```

Comme vous pouvez le voir, notre hook est très similaire à un composant fonctionnel régulier. La seule différence est l'instruction `return` – elle retourne une valeur JavaScript au lieu d'un élément HTML.

Les hooks React retournent souvent des valeurs, des fonctions, ou les deux. Par exemple, le hook `useState` retourne un tableau avec deux éléments : la valeur d'état actuelle et une fonction pour mettre à jour cette valeur.

Maintenant, laissez-moi expliquer comment le hook `usePreviousProps` fonctionne réellement :

* `const ref = useRef()` est utilisé pour persister la référence à travers les re-rendus du composant. Dans notre cas, nous l'utiliserons pour stocker la valeur précédente.
* Le hook `useEffect` mettra à jour la valeur `ref.current` chaque fois que le composant se re-rendra. Cela signifie que lorsque `value` change, la valeur `ref.current` sera mise à jour pour stocker la valeur la plus récente de la prop. Importamment, tout cela se produit après que le composant ait terminé le rendu, donc il stocke la valeur précédente pendant le re-rendu.
* `return ref.current` retourne la valeur de la référence `ref`.

Maintenant, notre hook personnalisé `usePreviousProps` est prêt à être utilisé !

## 😎 Comment Utiliser un Hook Personnalisé

La semaine dernière, j'ai publié le tutoriel [Comment Créer des Animations dans React 18](https://www.freecodecamp.org/news/create-animations-in-react/).

Si vous n'avez pas lu mon dernier tutoriel, il inclut le hook personnalisé `usePreviousProps` pour créer des animations de surbrillance :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/hightlight-3.gif)
_Animation de surbrillance_

Voici le code responsable de cette animation :

```jsx
export default function Tile({ value }) {
  const [scale, setScale] = useState(1);

  const previousValue = usePreviousProps(value);
  const hasChanged = previousValue !== value;

  useEffect(() => {
    if (hasChanged) {
      setScale(1.1);
      setTimeout(
          () => setScale(1),
          100 /* 100ms == 0.1s */
      );
    }
  }, [hasChanged, setScale]);

  const style = {
    transform: `scale(${scale})`
  };

  return (
    <div className="tile" style={style}>
      {value}
    </div>
  );
};
```

Concentrons-nous sur cette ligne : `const previousValue = usePreviousProps(value)`.

Ici, `previousValue` contient la valeur précédente pour ce composant. Si c'est un nouveau composant, il retourne `undefined`.

À la ligne suivante, la constante `hasChanged` aide à déterminer si le composant doit être mis en surbrillance. Si c'est nouveau et qu'il a retourné `undefined` plus tôt, il déclenche l'animation de surbrillance.

Quelques lignes plus tard, j'ai déclaré le hook `useEffect` qui vérifiera si un composant a changé sa valeur. Si c'est le cas, React exécutera l'animation de surbrillance.

## **🏁 Résumé**

Aujourd'hui, vous avez appris que les hooks React sont assez similaires aux composants fonctionnels. La seule différence est leur sortie, où ils retournent des valeurs JavaScript, des tableaux ou des fonctions plutôt que des éléments JSX.

Comme vous pouvez le voir, créer des hooks personnalisés n'est pas une science exacte, et j'espère vous avoir inspiré à expérimenter et à créer le vôtre.

Si cet article vous a aidé, veuillez le partager sur vos réseaux sociaux ou me donner un [coup de pouce sur Twitter](https://twitter.com/msokola). Merci !

## **🏫 Voulez-vous Construire Votre Propre Jeu 2048 ?**

Si vous voulez améliorer vos compétences en React, envisagez de rejoindre mon cours en ligne sur Udemy. Je vous aiderai à commencer avec React 18 en construisant un jeu 2048 entièrement fonctionnel. Je crois que créer des jeux rend l'apprentissage plus amusant, et vous aurez quelque chose de cool à montrer à vos amis.

De plus, je donne une réduction de 50 % pour les lecteurs de freeCodeCamp. Il suffit d'utiliser le code **50DISCOUNT** pour vous inscrire.

👏👏👏👏

### **🧑🏻 Rejoignez mon [cours React 18 sur Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106)**

Ce que vous apprendrez :

* Comment construire un jeu 2048 avec React 18 et Next.js.
* Les hooks React essentiels tels que useState, useRef, useCallback, useEffect, et bien plus encore.
* Gérer l'état en utilisant Reducer et React Context.
* Comment créer des applications mobiles réactives qui supportent les événements tactiles (comme le balayage mobile).
* Intégrer TypeScript dans vos projets React.
* Tester les applications React.
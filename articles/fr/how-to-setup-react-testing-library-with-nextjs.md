---
title: Comment configurer React Testing Library avec Next.js – Un guide étape par
  étape
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-03-07T15:58:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-react-testing-library-with-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Testing-next-RTL.png
tags:
- name: React
  slug: react
- name: Testing
  slug: testing
seo_title: Comment configurer React Testing Library avec Next.js – Un guide étape
  par étape
seo_desc: 'In this guide, you will learn how to set up React Testing Library in Next.js.
  We''ll also talk about why you should always test your React applications.

  I''ll discuss the features and benefits of using the React Testing Library to test
  your React appli...'
---

Dans ce guide, vous apprendrez à configurer React Testing Library dans Next.js. Nous parlerons également de l'importance de tester vos applications React.

Je discuterai des fonctionnalités et des avantages de l'utilisation de React Testing Library pour tester vos applications React et comment la configurer avec Next.js. Pour conclure ce tutoriel, je vous montrerai comment j'ai testé le plateau de mon jeu 2048.

Pour comprendre ce guide, vous n'avez pas besoin de connaissances approfondies, mais ce sera plus facile à apprendre si vous connaissez les bases de React. L'objectif ultime est de configurer des tests pour vos applications Next.js, donc comprendre React vous donnera un bon départ avec les tests.

Commençons !

## **Pourquoi les tests sont-ils importants ?**

Pour devenir développeur React et augmenter vos chances de trouver un emploi, vous devez apprendre à tester pour plusieurs raisons :

Tout d'abord, les tests confirment que votre application React fonctionne comme prévu. Cela vous permet de détecter les bugs et les erreurs dès les premières étapes du développement, avant que votre entreprise ne reçoive des appels de clients mécontents.

Les tests vous permettent également de refactoriser votre code en toute confiance en vous assurant que vos modifications ne cassent pas les fonctionnalités existantes. Sans tests en place, après chaque refactorisation, vous devriez cliquer manuellement dans votre application pour double-vérifier. Cela serait si fastidieux et chronophage.

Les développeurs ayant des compétences décents en tests sont toujours plus demandés car ils savent concevoir et construire des applications de qualité qui peuvent être maintenues pendant de nombreuses années.

## **Qu'est-ce que React Testing Library ?**

React Testing Library est un ensemble d'utilitaires de test conçus pour vous aider à garantir la correction de vos projets React et Next.js.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-05-at-10.09.49.png)
_Page d'accueil de React Testing Library_

Peu importe si votre projet est écrit en TypeScript et utilise React ou Next.js – vous pouvez toujours tirer parti de React Testing Library pour tester votre application. Elle est facile à utiliser et réduit la quantité de code dont vous avez besoin pour préparer des cas de test.

React Testing Library a été conçue pour simplifier votre vie en tant que développeur et vous aider à écrire des tests qui ne vous frustrent pas. Vos tests ne casseront que lorsque votre application cassera, et non son implémentation.

Le meilleur, c'est que React Testing Library n'est pas limitée aux tests unitaires. Vous pouvez l'utiliser pour préparer des tests d'intégration, des tests de bout en bout (E2E tests), et bien d'autres. C'est pourquoi c'est un outil si puissant.

## Comment configurer React Testing Library avec Next.js

Utiliser React Testing Library avec Next.js est un processus très simple. Vous n'avez besoin que de quatre choses :

1. Un projet Next.js existant
2. Jest et React Testing Library installés avec npm
3. Jest configuré dans votre projet Next.js
4. Écrire votre premier test

Cela semble simple, n'est-ce pas ?

Le moyen le plus rapide de créer une nouvelle application Next.js est de taper `npx create-next-app@latest` dans votre ligne de commande. Vous devrez répondre à quelques questions et l'application sera automatiquement créée pour vous.

Si vous avez un projet Next.js existant, vous devez simplement installer la suite de test en utilisant npm :

```bash
npm install --save-dev jest jest-environment-jsdom @testing-library/react @testing-library/jest-dom
```

Dans ce guide, nous utiliserons la suite de test Jest pour exécuter les tests, qui est un outil assez courant développé par Facebook. Si vous souhaitez remplacer Jest par autre chose, vous pouvez facilement utiliser Vitest, Playwright ou Cypress – consultez simplement [la documentation de Next.js pour plus de détails](https://nextjs.org/docs/app/building-your-application/testing).

Pour configurer Jest dans Next.js, vous devez créer un fichier `jest.config.js` à la racine de votre projet et y coller le contenu suivant ([c'est un modèle](https://nextjs.org/docs/app/building-your-application/testing/jest)) :

```js
// fichier : jest.config.js
const nextJest = require("next/jest");

const createJestConfig = nextJest({
  dir: "./",
});

const customJestConfig = {
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"], // <= fichier de configuration ici
  testEnvironment: "jest-environment-jsdom",
};

module.exports = createJestConfig(customJestConfig);
```

Comme vous pouvez le voir, le fichier de configuration nous oblige à créer un fichier supplémentaire pour que nos tests fonctionnent. Ce fichier de configuration sera inclus avant chaque test et nous l'utiliserons pour importer React Testing Library dans chaque test afin de ne pas avoir à le faire manuellement.

Créons maintenant le fichier de configuration. Il doit s'appeler `jest.setup.js` et doit contenir la ligne suivante :

```js
// fichier : jest.setup.js
import "@testing-library/jest-dom";
```

La configuration de votre suite de test est presque terminée.

### Comment créer la commande `npm test`

Pour terminer la configuration de notre suite de test, nous devons créer une commande `npm test` et la lier avec Jest et React Testing Library. Nous allons le faire dans `package.json` en ajoutant une commande `test` dans la section `scripts` :

```json
{
  "name": "2048-in-react",
  "version": "0.2.0",
  "homepage": "https://mateuszsokola.github.io/2048-in-react/",
  ...,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest --watch" // <== ICI
  },
  ...
}
```

Maintenant, chaque fois que vous exécuterez la commande `npm test`, vous exécuterez la suite de test :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-05-at-10.49.23.png)
_Résumé des tests vides._

La suite de test fonctionne, mais les tests sont toujours manquants. Cela a du sens car nous n'avons pas encore créé de tests.

### Comment tester les composants en utilisant React Testing Library

Avant d'écrire notre premier test, créons un répertoire où nous les stockerons. Par défaut, les tests sont stockés dans le répertoire appelé `__tests__`. Ce nom semble étrange mais il a une bonne raison d'avoir des doubles underscores en préfixe et suffixe. Grâce à ceux-ci, votre répertoire de test sera toujours en haut de votre arbre de projet.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-05-at-11.09.58.png)
_Arbre du projet Next.js avec le répertoire de test en haut (emplacement 1)_

Maintenant, nous sommes prêts à créer votre premier test.

Nous pourrions faire un test vide aléatoire qui ne teste rien, mais je préférerais utiliser un exemple concret. Prenons un test de mon jeu 2048 ([voici le code source](https://github.com/mateuszsokola/2048-in-react)) – j'en ai choisi un qui garantit que le plateau de jeu est rendu correctement.

Si vous ne connaissez pas le jeu 2048, je vous dirai seulement qu'il se joue sur un plateau de 4 x 4. Cela signifie que le plateau de jeu doit avoir 16 cellules (4 x 4 = 16).

Créons maintenant un nouveau fichier appelé `board.test.jsx` dans le répertoire de test `__tests__` :

```jsx
// __tests__/compontents/board.test.jsx
import { render } from "@testing-library/react";
import Board from "@/components/board";

describe("Board", () => {
  it("should render board with 16 cells", () => {
    const { container } = render(
      <Board />
    );
    const cellElements = container.querySelectorAll(".cell");

    expect(cellElements.length).toEqual(16);
  });
});

```

Comme vous pouvez le voir, ce test rend le plateau et vérifie qu'il y a 16 éléments DOM qui ont une classe `cell`. Rien de plus que cela. Si le nombre de cellules est différent, ce test échouera.

Jetons un bref coup d'œil dans le terminal. Tout est vert et cela signifie que notre test a été implémenté correctement et qu'il passe :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-05-at-10.52.45.png)
_Votre premier test réussi_

## **Quelle est la suite ?**

Félicitations ! Maintenant, vous savez comment configurer l'une des bibliothèques de test les plus populaires pour React. Je pense que cela vous aidera à faire passer votre application Next.js à un tout nouveau niveau en termes de qualité.

Si vous savez comment construire des applications React, vous devriez maintenant vous concentrer sur les tests car cette compétence vous aidera à décrocher votre premier emploi.

J'espère que cet article vous a beaucoup aidé. Cela signifierait beaucoup pour moi si vous le partagez sur vos réseaux sociaux.

[Si vous avez des questions, vous pouvez me contacter sur Twitter](https://twitter.com/msokola).

## Apprendre React & Next.js

Apprendre Next.js peut être intimidant et souvent frustrant. La plupart des cours en ligne se concentrent sur les fonctionnalités de React et Next.js plutôt que sur la construction d'applications. C'est pourquoi j'ai créé un cours qui vous aidera à apprendre React et Next.js tout en construisant un magnifique jeu 2048 à partir de zéro !

Je crois que l'apprentissage doit être amusant et libérer la créativité. Préféreriez-vous construire une autre liste de tâches plutôt qu'un jeu génial ?

Vous pouvez rejoindre mon [cours React et Next.js sur Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?couponCode=FREECODECAMP_) et construire le jeu 2048 avec moi.

C'est le seul cours dont vous avez besoin.

[![Cliquez pour rejoindre le cours React 18 & Next.js](https://www.mateu.sh/udemy-freecodecamp.png)](https://www.udemy.com/course/2048-in-react-and-nextjs/?couponCode=FREECODECAMP_)
_Cliquez pour vous inscrire_
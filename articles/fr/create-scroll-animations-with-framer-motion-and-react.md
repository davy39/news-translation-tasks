---
title: Comment créer des animations de défilement avec React, Tailwind CSS et Framer
  Motion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-27T18:47:58.000Z'
originalURL: https://freecodecamp.org/news/create-scroll-animations-with-framer-motion-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/FreeCodeCamp.png
tags:
- name: animations
  slug: animations
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: tailwind
  slug: tailwind
seo_title: Comment créer des animations de défilement avec React, Tailwind CSS et
  Framer Motion
seo_desc: 'By Manu Arora

  Scroll-based animations are triggered when a user scrolls on a webpage. Recently,
  I built a Scroll Animation with Framer Motion that moves grids in uneven directions.
  This project prompted me to write a tutorial about how I did that her...'
---

Par Manu Arora

Les animations basées sur le défilement sont déclenchées lorsque l'utilisateur fait défiler une page web. Récemment, j'ai créé une [Animation de Défilement avec Framer Motion](https://www.aceternity.com/components/container-scroll-animation) qui déplace des grilles dans des directions inégales. Ce projet m'a incité à écrire un tutoriel sur la façon dont j'ai fait cela ici sur freeCodeCamp.  
  
La bibliothèque Framer Motion rend super facile l'intégration d'animations dans vos applications React. Avec quelques lignes de code, vous pouvez réaliser ce qui peut sembler être une tâche difficile.

Aujourd'hui, nous allons créer une animation déclenchée par le défilement qui fait tourner, translater et mettre à l'échelle une carte (ou un conteneur) lorsque l'utilisateur fait défiler.

## Ce que nous construisons :

%[https://stackblitz.com/edit/stackblitz-starters-2mybwg?embed=1&file=src%2FScroll.tsx&view=preview]

Ici, lorsque l'utilisateur fait défiler, trois choses vont se produire :

1. Le texte `Libérez le pouvoir des Animations de Défilement` se déplace un peu vers le haut.
2. Le cadre (le conteneur noir qui contient les cartes) tourne et s'aligne parfaitement avec la page.
3. Les cartes à l'intérieur du cadre se translatent un peu vers le haut – fournissant un effet de parallaxe.

Toutes ces actions sont réalisées à l'aide de la valeur `scrollYProgress` de la fonction `useScroll()` de Framer Motion. La valeur `scrollYProgress` (nous en parlerons plus tard) vous donne la progression entre `0` et `1`, déterminant où se trouve actuellement l'utilisateur sur la page.

Plongeons dans le code et voyons comment implémenter cette animation à partir de zéro.

## **Prérequis**

Pour cette démonstration, nous allons utiliser :

* Next.js pour écrire notre composant
* Tailwind CSS pour le style et le CSS
* Framer Motion pour les animations

## **Comment configurer le projet**

La configuration du projet est assez simple. Voici les étapes à suivre :

Tout d'abord, vous devrez installer Next.js si vous ne l'avez pas déjà.

Ouvrez votre terminal et tapez la commande suivante :

```
npx create-next-app@latest scroll-animation --typescript --eslint
```

Cela initialisera une application `Next.js` où vous pourrez aller directement dans le dossier `app` pour les routes et le dossier `components` pour créer vos composants.

Nous allons garder cela très simple pour cette démonstration et ajouter le composant dans le dossier `components`.

Ensuite, vous devrez installer Tailwind CSS, que vous pouvez faire comme suit :

```
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Maintenant, ajoutez Tailwind à votre projet en copiant le contenu du fichier suivant dans le fichier `tailwind.config.ts` qui est créé après avoir exécuté l'étape ci-dessus :

```
tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
 
    // Ou si vous utilisez le répertoire `src` :
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Maintenant, ajoutez les styles globaux suivants dans le fichier `globals.css` :

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Avec ces étapes terminées, vous devriez être en mesure d'écrire le composant et de l'ajouter à votre projet de manière transparente.  
  
Maintenant que nous avons terminé la configuration, plongeons dans le code du composant que nous allons construire.

## Comment construire le composant de défilement

Il n'y a essentiellement qu'un seul composant principal avec lequel nous allons travailler. Nous l'appelons `Scroll`, parce que pourquoi pas ? Voici le code :

```tsx
export const Scroll = () => {
  return (
    <div className="flex flex-col bg-white h-screen w-screen">
      <ScrollCore />
    </div>
  );
};
export const ScrollCore = () => {
  return (
    <div className="h-[120vh] p-10 flex items-center justify-center relative ">
      <div
        className="py-40 w-full relative"
      >
        <Header />
        <Card />
      </div>
    </div>
  );
};

export const Header = () => {
  return (
    <div
      className="div max-w-5xl mx-auto text-center"
    >
      <h1 className="text-4xl font-semibold">
        Libérez le pouvoir des <br />{' '}
        <span className="text-5xl lg:text-6xl  font-bold mt-1 leading-none">
          Animations de Défilement
        </span>
      </h1>
    </div>
  );
};

export const Card = () => {
	// À implémenter plus tard dans le blog
};

```

Le composant `Scroll` est le conteneur qui contient un composant `ScrollCore`.

Le composant `ScrollCore` contient les composants `Header` et `Card` :

* Le `Header` est le composant de texte qui se translate vers le haut (comme nous l'avons vu dans l'aperçu
* Le composant `Card` est le `Frame` dont nous avons parlé plus tôt.

Ces deux composants sont stylisés avec Tailwind CSS. Nous donnons une classe de h-screen et w-screen au conteneur, et nous voulons que le conteneur prenne toute la hauteur et la largeur de l'écran.

## Comment construire le composant Card

Le composant `Card` est assez basique (sans l'animation) puisque nous allons rendre plusieurs cartes à l'intérieur d'un conteneur avec des `grids` de Tailwind CSS. Voici le code :

```tsx
import {users} from './users';

export const Card = () => {
  return (
    <div
      style={{
        boxShadow:
          '0 0 #0000004d, 0 9px 20px #0000004a, 0 37px 37px #00000042, 0 84px 50px #00000026, 0 149px 60px #0000000a, 0 233px 65px #00000003',
      }}
      className="max-w-5xl -mt-12 mx-auto h-[30rem] md:h-[40rem] w-full border-4 border-[#6C6C6C] p-6 bg-[#222222] rounded-[30px] shadow-2xl"
    >
      <div className="bg-gray-100 h-full w-full rounded-2xl grid grid-cols-2 md:grid-cols-4 gap-4 overflow-hidden p-4">
        {users.map((user, idx) => (
          <div
            key={`user-${idx}`}
            className="bg-white rounded-md cursor-pointer relative"
          >
            <div className="absolute top-2 right-2 rounded-full text-xs font-bold bg-white px-2 py-1">
              {user.badge}
            </div>
            <img
              src={user.image}
              className="rounded-tr-md rounded-tl-md text-sm "
            />
            <div className="p-4">
              <h1 className="font-semibold text-sm ">{user.name}</h1>
              <h2 className=" text-gray-500 text-xs ">{user.designation}</h2>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

```

Ici, nous donnons une `box shadow` que j'ai prise de [Box shadows for Tailwind CSS](https://manuarora.in/boxshadows). Nous lui donnons également un arrière-plan de `#22222`. Dans Tailwind, nous pouvons utiliser des valeurs arbitraires en utilisant la notation `[]`. Par exemple, nous avons donné la classe `bg-[#22222]` pour l'arrière-plan.

Nous utilisons également un tableau `users` pour rendre une liste d'utilisateurs. Le tableau des utilisateurs ressemble à ceci :

```tsx
export const users = [
  {
    name: 'Manu Arora',
    designation: 'Fondateur, Algochurn',
    image: 'https://picsum.photos/id/10/300/300',
    badge: 'Mentor',
  },
  {
    name: 'Sarah Singh',
    designation: "Fondatrice, Cuisine de Sarah",
    image: 'https://picsum.photos/id/11/300/300',
    badge: 'Mentor',
  },
  // Reste des utilisateurs...
];
```

Ici, nous rendons le nom, la désignation, l'image et le badge de l'utilisateur.

Maintenant que nous avons terminé la conception de base des `cards` et du `header`, nous pouvons passer à l'animation de ceux-ci en utilisant Framer Motion.

## Comment ajouter les fonctions d'animation

Framer Motion fournit des fonctions utiles que vous pouvez utiliser pour animer n'importe quoi sur une page web. Certains des cas d'utilisation de ces animations peuvent être :

* Animer lorsque l'utilisateur fait glisser et dépose
* Animer lorsque l'utilisateur fait défiler
* Animer lorsque l'utilisateur clique ou survole
* Animer au chargement de la page

Dans cette démonstration, nous voulons animer sur le `défilement`. Pour cela, nous pouvons utiliser la fonction `useScroll()` fournie par Framer Motion.

Pour animer en utilisant le défilement, nous allons :

1. Obtenir `scrollYProgress` à partir de la méthode `useScroll()`
2. Utiliser le hook `useTransform` pour transformer les valeurs de `scrollYProgress`
3. Utiliser les valeurs transformées pour animer nos cartes.

Examinons l'extrait de code pour cela :

```tsx
import { useScroll, useTransform, motion } from 'framer-motion';

import { users } from './users';

export const Scroll = () => {
  return (
    <div className="flex flex-col bg-white h-screen w-screen">
      <ScrollCore />
    </div>
  );
};
export const ScrollCore = () => {
  const { scrollYProgress } = useScroll();

  const rotate = useTransform(scrollYProgress, [0, 1], [20, 0]);
  const scale = useTransform(scrollYProgress, [0, 1], [1.05, 1]);
  const translate = useTransform(scrollYProgress, [0, 1], [0, -100]);

  return (
    <div className="h-[120vh] transform scale-[0.8] p-10 flex items-center justify-center relative ">
      <div
        className="py-40 w-full relative"
        style={{
          perspective: '1000px',
        }}
      >
        <Header />
        <Card />
      </div>
    </div>
  );
};
// reste du code
```

Décomposons ce qui se passe dans le code :

Nous utilisons la valeur `scrollYProgress` de la fonction `useScroll()`. Cette `scrollYProgress` est une `valeur de mouvement` que nous pouvons utiliser avec `motion.div` de Framer Motion pour animer diverses propriétés CSS. Les propriétés CSS que nous allons animer sont `rotate`, `scale` et `translate`.

Nous combinons ces valeurs `scrollYProgress` avec un autre hook de framer-motion qui est `useTransform`.  
  
Le hook `useTransform` est responsable de la conversion d'une valeur en une autre. Par exemple, si nous voulons faire tourner la carte de 45 degrés à 90 degrés lorsque l'utilisateur fait défiler du haut de la page vers le bas de la page, nous pourrions utiliser quelque chose comme ceci :

```tsx
 const rotate = useTransform(scrollYProgress, [0, 1], [45, 90]);

```

Cette valeur `rotate` peut maintenant être passée à la balise `style` d'un élément `motion.div`. N'oubliez pas qu'un div régulier ne peut pas être utilisé ici puisque rotate est une VALEUR DE MOUVEMENT et doit être utilisé avec un élément motion.div.

De même, nous allons ajouter toutes les valeurs pour `rotate`, `scale` et `translate` comme ceci :

```tsx
const rotate = useTransform(scrollYProgress, [0, 1], [20, 0]);
const scale = useTransform(scrollYProgress, [0, 1], [1.05, 1]);
const translate = useTransform(scrollYProgress, [0, 1], [0, -100]);

```

Ici :

1. Lorsque l'utilisateur fait défiler de haut en bas (0 est le début, 1 est la fin, ce qui signifie que l'utilisateur a fait défiler de haut en bas), nous voulons faire tourner la carte de 20 degrés à 0 degrés. Mais voici un piège : nous spécifions également la propriété `perspective` et la définissons à `800px` pour qu'elle donne un effet 3D.
2. Nous voulons que l'échelle passe de `1.05` à `1` lorsque l'utilisateur fait défiler.
3. Et enfin, nous voulons translater les cartes de 0 à -100 px dans la direction Y (plus tard sur la façon dont nous allons animer la direction Y).

Maintenant que nous avons toutes les animations configurées, nous devons simplement passer ces valeurs aux balises `style` des composants et faire fonctionner les animations.

## Comment ajouter les animations

Nous avons vu précédemment comment utiliser le hook `useScroll()` pour obtenir la progression du défilement et obtenir les valeurs `rotate`, `scale` et `translate` (ces valeurs sont appelées valeurs de mouvement, car elles ne peuvent être utilisées qu'avec un bloc `motion.div`). Il est maintenant temps d'utiliser réellement ces valeurs dans notre composant.

Nous pouvons faire cela en passant les valeurs `rotate`, `scale` et `translate` aux composants `Header` et `Card` et en les utilisant dans leurs balises de style respectives.  
  
Examinons l'extrait de code pour mieux comprendre :

```tsx
import { useScroll, useTransform, motion } from 'framer-motion';

import { users } from './users';

export const Scroll = () => {
  return (
    <div className="flex flex-col bg-white h-screen w-screen">
      <ScrollCore />
    </div>
  );
};
export const ScrollCore = () => {
  const { scrollYProgress } = useScroll();

  const rotate = useTransform(scrollYProgress, [0, 1], [20, 0]);
  const scale = useTransform(scrollYProgress, [0, 1], [1.05, 1]);
  const translate = useTransform(scrollYProgress, [0, 1], [0, -100]);

  return (
    <div className="h-[120vh] transform scale-[0.8] p-10 flex items-center justify-center relative ">
      <div
        className="py-40 w-full relative"
        style={{
          perspective: '1000px',
        }}
      >
        <Header translate={translate} />
        <Card rotate={rotate} translate={translate} scale={scale} />
      </div>
    </div>
  );
};
// reste du code
```

Ici, nous passons les valeurs translate, rotate et scale à l'intérieur des composants :

```tsx
<Header translate={translate} />
<Card rotate={rotate} translate={translate} scale={scale} />
```

* Pour `Header`, nous voulons simplement translater le texte du bas vers le haut un peu (sortant d'un effet de parallaxe)
* Pour `Card`, nous voulons faire un peu plus avec la rotation et la translation.

Voici le code pour le composant `Header` :

```tsx
export const Header = ({ translate }: any) => {
  return (
    <motion.div
      style={{
        translateY: translate,
      }}
      className="div max-w-5xl mx-auto text-center"
    >
      <h1 className="text-4xl font-semibold">
        Libérez le pouvoir des <br />{' '}
        <span className="text-5xl lg:text-6xl  font-bold mt-1 leading-none">
          Animations de Défilement
        </span>
      </h1>
    </motion.div>
  );
};
```

Ici, nous avons converti le `div` en `motion.div` pour qu'il puisse accepter les valeurs de mouvement.

Nous avons également animé la propriété `translateY` fournie par Framer Motion et ajouté la valeur `translate`. N'oubliez pas que translate va de `0` à `-100`.

Et c'est tout pour animer le texte. Essentiellement pour le composant `Header`, nous avons écrit seulement trois lignes de code pour l'animer. Plutôt cool, non ?

Voici le code pour le composant `Card` :

```tsx
export const Card = ({
  rotate,
  scale,
  translate,
}: {
  rotate: any;
  scale: any;
  translate: any;
}) => {
  return (
    <motion.div
      style={{
        rotateX: rotate, // rotation dans l'axe X
        scale,
        boxShadow:
          '0 0 #0000004d, 0 9px 20px #0000004a, 0 37px 37px #00000042, 0 84px 50px #00000026, 0 149px 60px #0000000a, 0 233px 65px #00000003',
      }}
      className="max-w-5xl -mt-12 mx-auto h-[30rem] md:h-[40rem] w-full border-4 border-[#6C6C6C] p-6 bg-[#222222] rounded-[30px] shadow-2xl"
    >
      <div className="bg-gray-100 h-full w-full rounded-2xl grid grid-cols-2 md:grid-cols-4 gap-4 overflow-hidden p-4">
        {users.map((user, idx) => (
          <motion.div
            key={`user-${idx}`}
            className="bg-white rounded-md cursor-pointer relative"
            style={{ translateY: translate }}
            whileHover={{
              boxShadow:
                '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)',
            }}
          >
            <div className="absolute top-2 right-2 rounded-full text-xs font-bold bg-white px-2 py-1">
              {user.badge}
            </div>
            <img
              src={user.image}
              className="rounded-tr-md rounded-tl-md text-sm "
            />
            <div className="p-4">
              <h1 className="font-semibold text-sm ">{user.name}</h1>
              <h2 className=" text-gray-500 text-xs ">{user.designation}</h2>
            </div>
          </motion.div>
        ))}
      </div>
    </motion.div>
  );
};
```

C'est le même code qu'avant avec une seule différence : le `div` est maintenant converti en `motion.div` pour accepter les valeurs là où c'est nécessaire. Ici, nous voulons que les `cards` à l'intérieur du conteneur se translatent, et que la carte entière tourne.

Dans le code ci-dessus, examinons cette partie de près :

```tsx
<motion.div
      style={{
        rotateX: rotate, // rotation dans l'axe X
        scale,
        boxShadow:
          '0 0 #0000004d, 0 9px 20px #0000004a, 0 37px 37px #00000042, 0 84px 50px #00000026, 0 149px 60px #0000000a, 0 233px 65px #00000003',
      }}
      className="max-w-5xl -mt-12 mx-auto h-[30rem] md:h-[40rem] w-full border-4 border-[#6C6C6C] p-6 bg-[#222222] rounded-[30px] shadow-2xl"
    >
	// reste du code...
</motion.div>
```

Ici, nous voulons : 

1. `rotateX` pour qu'il donne l'illusion de passer de couché à plat sur l'écran à debout droit. (N'oubliez pas, lorsque l'utilisateur fait défiler, la valeur passe de `20deg` à `0deg`.)
2. La `scale` du conteneur (ou du cadre) est également animée pour passer de `1.05` à `1`.

Regardons maintenant les cartes à l'intérieur de ce cadre :

```tsx
{users.map((user, idx) => (
          <motion.div
            key={`user-${idx}`}
            className="bg-white rounded-md cursor-pointer relative"
            style={{ translateY: translate }}
            whileHover={{
              boxShadow:
                '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)',
            }}
          >
            <div className="absolute top-2 right-2 rounded-full text-xs font-bold bg-white px-2 py-1">
              {user.badge}
            </div>
            <img
              src={user.image}
              className="rounded-tr-md rounded-tl-md text-sm "
            />
            <div className="p-4">
              <h1 className="font-semibold text-sm ">{user.name}</h1>
              <h2 className=" text-gray-500 text-xs ">{user.designation}</h2>
            </div>
          </motion.div>
        ))}
```

Ici, la propriété `translateY` est animée et le div est converti en `motion.div`.

Et c'est tout. C'est tout ce qu'il faut pour animer lors du défilement en utilisant Framer Motion.

## Conclusion

Dans ce tutoriel, vous avez appris comment animer en utilisant Framer Motion. Essentiellement, nous avons examiné deux fonctions principales :

* `useScroll()`
* `useTransform()`

Il existe d'autres fonctions que vous pouvez utiliser et qui peuvent vous aider à atteindre vos objectifs d'animation. Mais je crois que Framer Motion est une API d'animation vraiment simple à utiliser, étant donné ses fonctions intuitives et sa facilité d'utilisation.  
  
Voici le [code source complet](https://stackblitz.com/edit/stackblitz-starters-2mybwg?file=src%2FScroll.tsx) pour la démonstration.

J'ai créé diverses autres démonstrations comme celle-ci [Effet Parallaxe en utilisant Tailwind CSS et Framer Motion](https://www.aceternity.com/components/parallax-scroll) qui utilise essentiellement le même modèle que nous avons discuté dans ce guide.  
  
Si vous avez aimé cette démonstration et que vous voulez que je crée plus de ces composants cool [Tailwind CSS et Framer motion](https://aceternity.com/components), faites-le moi savoir sur [Twitter](https://twitter.com/mannupaaji) et je serais plus qu'heureux de travailler dessus. :)

Bon codage 4a0
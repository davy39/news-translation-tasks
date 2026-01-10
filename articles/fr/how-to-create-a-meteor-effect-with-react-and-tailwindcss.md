---
title: Comment créer un effet de météorite avec React et TailwindCSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-08-11T16:14:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-meteor-effect-with-react-and-tailwindcss
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-11-at-9.20.20-PM.png
tags:
- name: animations
  slug: animations
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: tailwind
  slug: tailwind
seo_title: Comment créer un effet de météorite avec React et TailwindCSS
seo_desc: 'By Manu Arora

  A while ago, I saw a post on Twitter that had some fancy beams of light emanating
  out from behind the main image. It looked like a meteor was blazing softly behind
  the card, and I thought it was a really cool UI component to have in a p...'
---

Par Manu Arora

Il y a quelque temps, j'ai vu un post sur Twitter qui avait des faisceaux de lumière fantaisistes émanant de derrière l'image principale. Cela ressemblait à une météorite qui brillait doucement derrière la carte, et j'ai pensé que c'était un composant UI vraiment cool à avoir dans un projet.

En le voyant, j'ai pensé à créer un composant React qui ferait le même travail – c'est-à-dire, ajouter cet effet de lueur de météorite à l'arrière-plan d'une carte. 

Cela ferait ressortir la carte instantanément et serait vraiment utile si vous vouliez mettre en avant une carte spécifique parmi votre ensemble de cartes UI.

C'est donc ce que nous allons construire dans ce tutoriel.

## Prérequis

Pour créer cet effet, nous allons utiliser :

* **Next.js** pour notre framework (parce que nous allons créer un composant)
* **TailwindCSS** pour le style

## Comment configurer le projet

Pour configurer un projet avec Next.js et TailwindCSS, suivez simplement ces étapes :

Tout d'abord, rendez-vous dans le terminal et entrez la commande suivante :

```bash
npx create-next-app@latest meteor-effect --typescript --eslint
```

Une fois que vous avez installé `Next.js`, accédez au projet comme ceci :

```bash
cd meteor-effect
```

Puis installez TailwindCSS comme ceci :

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Configurez le fichier `tailwind.config.js` pour que Tailwind sache où trouver vos styles :

```js
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

Une fois que vous avez configuré le fichier de configuration, ajoutez les styles de base pour Tailwind à la feuille de style globale comme ceci :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Avec ces étapes, vous devriez être prêt à commencer.

## Que construisons-nous ?

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-11-at-9.20.20-PM-1.png)
_les lignes cool à l'arrière-plan sont des météorites_

Une **Météorite** (comme je l'appelle, vous pouvez l'appeler comme vous voulez) est essentiellement un élément UI avec une tête et une queue. C'est une sorte de faisceau qui a un dégradé. 

Sur l'image, les lignes de l'arrière-plan sont ce que j'appelle des météorites. Nous allons animer ces lignes pour qu'elles aillent du côté gauche du conteneur de la carte au côté droit, donnant l'illusion d'une pluie de météorites.

Nous allons construire :

* Un beau composant de carte
* Un composant de météorite à ajouter à la carte

Mais avant de construire le composant principal de la météorite, créons le conteneur qui contient les météorites.

## Comment créer le conteneur de carte

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-11-at-9.21.23-PM.png)
_Le conteneur de carte que nous allons construire ici_

Avant de créer le composant `Meteor`, créons d'abord le conteneur qui contiendra nos météorites.

Le conteneur de carte a quatre parties :

* Une icône SVG
* Un titre
* Une section de contenu
* Un appel à l'action

Nous allons styliser cette carte avec TailwindCSS et lui donner également un dégradé de fond pour qu'elle ait l'air bien.

```tsx
import React from "react";

export const MeteorPreview = () => {
  return (
    <div className=" h-[40rem]">
      <div className=" h-3/4 md:h-1/2 w-3/4  relative max-w-sm">
        <div className="absolute inset-0 h-full w-full bg-gradient-to-r from-blue-500 to-teal-500 transform scale-[0.80] bg-red-500 rounded-full blur-3xl" />
        <div className="relative shadow-xl bg-gray-900 border border-gray-800  px-4 py-8 h-full overflow-hidden rounded-2xl flex flex-col justify-end items-start">
          <div className="h-5 w-5 rounded-full border flex items-center justify-center mb-4 border-gray-500">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              className="h-2 w-2 text-gray-300"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M4.5 4.5l15 15m0 0V8.25m0 11.25H8.25"
              />
            </svg>
          </div>

          <h1 className="font-bold text-xl text-white mb-0 mt-4 relative z-50">
            Des météorites parce que c'est cool
          </h1>

          <p className="font-normal text-base text-slate-500 mb-4 relative z-50">
            Je ne sais pas quoi écrire alors je vais juste coller quelque chose de cool ici.
            Une phrase de plus parce que le lorem ipsum est juste inacceptable.
          </p>

          <button className="border px-4 py-1 rounded-lg !text-sm  border-gray-500 text-gray-300">
            Explorer &rarr;
          </button>

        </div>
      </div>
    </div>
  );
};

```

Tout d'abord, nous avons créé un conteneur qui contient le contenu de la carte. Ce conteneur contient les éléments suivants :

* Une icône SVG en haut du conteneur
* Un titre, qui est une phrase montrant le but de la carte
* Du contenu, qui est contenu dans une balise de paragraphe expliquant le contenu de la carte
* Un CTA, qui est un élément bouton qui emmène l'utilisateur vers une autre partie du site web.

Maintenant que nous avons le composant de carte en place (le conteneur), créons le composant `Meteor`.

## Comment construire le composant Meteor

Comme je l'ai expliqué précédemment, une météorite n'est rien d'autre qu'un élément UI avec une tête et une queue qui a un dégradé. Nous allons construire exactement cela ici.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-11-at-9.04.17-AM.png)
_Météorites autonomes_

Chaque météorite aura :

* Une queue de largeur de `50px`
* Une hauteur de queue de `1px`
* Un dégradé de fond (pour la queue) qui va de `#64748b` à `transparent`
* Une tête de hauteur et de largeur de `2px`

```tsx
import clsx from "clsx";
import React from "react";

export const Meteors = ({ number }: { number?: number }) => {
  const meteors = new Array(number || 20).fill(true);
  return (
    <>
      {meteors.map((el, idx) => (
        <span
          key={"meteor" + idx}
          className={clsx(
            "animate-meteor-effect absolute top-1/2 left-1/2 h-0.5 w-0.5 rounded-[9999px] bg-slate-500 shadow-[0_0_0_1px_#ffffff10] rotate-[215deg]",
            "before:content-[''] before:absolute before:top-1/2 before:transform before:-translate-y-[50%] before:w-[50px] before:h-[1px] before:bg-gradient-to-r before:from-[#64748b] before:to-transparent"
          )}
          style={{
            top: 0,
            left: Math.floor(Math.random() * (400 - -400) + -400) + "px",
            animationDelay: Math.random() * (0.8 - 0.2) + 0.2 + "s",
            animationDuration: Math.floor(Math.random() * (10 - 2) + 2) + "s",
          }}
        ></span>
      ))}
    </>
  );
};

```

Comprenons le composant Meteor.

* Le composant `Meteor` prend une prop `numbers`. Cela est créé de telle sorte que si vous passez les nombres, les météorites augmentent. Le défaut est fixé à 20.
* Nous créons un élément `span` qui sera essentiellement notre météorite qui va de gauche à droite.
* La classe `before:` crée un pseudo-élément avant qui est essentiellement la partie `ligne` de la météorite. Nous lui donnons un dégradé linéaire et une largeur de `50px`.
* La balise `style` décide où se trouve actuellement la météorite dans le DOM. Nous allons utiliser `Math.random()` pour placer aléatoirement les météorites en arrière-plan.
* Pour animer réellement les météorites, nous utilisons la classe `animate-meteor-effect`. Cette classe est en fait ajoutée dans le fichier `tailwind.config.js` pour ajouter une animation de mouvement.

```js
 theme: {
    extend: {
      animation: {
        "meteor-effect": "meteor 5s linear infinite",
      },
      keyframes: {

        meteor: {
          "0%": { transform: "rotate(215deg) translateX(0)", opacity: 1 },
          "70%": { opacity: 1 },
          "100%": {
            transform: "rotate(215deg) translateX(-500px)",
            opacity: 0,
          },
        },
      },
    },
  },
```

Ici, nous déplaçons essentiellement le faisceau à `-500px` en 5 secondes. C'est ce qui fait que la météorite se déplace de gauche à droite. Cela anime également joliment l'opacité de visible à caché (quand nous sommes à 70% du chemin).

## Comment utiliser le composant Meteor

Maintenant que nous avons le composant `Meteor` en place, nous pouvons facilement l'intégrer dans notre composant de carte que nous avons créé précédemment :

```tsx
import React from "react";
import { Meteors } from "./Meteors";

export const MeteorPreview = () => {
  return (
    <div className=" h-[40rem]">
      <div className=" h-3/4 md:h-1/2 w-3/4  relative max-w-sm">
        <div className="absolute inset-0 h-full w-full bg-gradient-to-r from-blue-500 to-teal-500 transform scale-[0.80] bg-red-500 rounded-full blur-3xl" />
        <div className="relative shadow-xl bg-gray-900 border border-gray-800  px-4 py-8 h-full overflow-hidden rounded-2xl flex flex-col justify-end items-start">
          <div className="h-5 w-5 rounded-full border flex items-center justify-center mb-4 border-gray-500">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              className="h-2 w-2 text-gray-300"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M4.5 4.5l15 15m0 0V8.25m0 11.25H8.25"
              />
            </svg>
          </div>

          <h1 className="font-bold text-xl text-white mb-0 mt-4 relative z-50">
            Des météorites parce que c'est cool
          </h1>

          <p className="font-normal text-base text-slate-500 mb-4 relative z-50">
            Je ne sais pas quoi écrire alors je vais juste coller quelque chose de cool ici.
            Une phrase de plus parce que le lorem ipsum est juste inacceptable. 
          </p>

          <button className="border px-4 py-1 rounded-lg !text-sm  border-gray-500 text-gray-300">
            Explorer &rarr;
          </button>

          {/* Partie principale - Effet de météorite */}
          <Meteors number={10} />
        </div>
      </div>
    </div>
  );
};

```

Ici, nous intégrons le composant `<Meteor />` avec une prop `number={10}` pour n'avoir que 10 météorites dans notre composant.

Le composant final ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-11-at-9.20.20-PM-2.png)
_Le composant de carte final avec des météorites_

## Conclusion

Il est vraiment facile de créer de beaux composants qui se démarquent avec TailwindCSS 

J'ai adoré créer ce composant à partir de zéro et j'espère qu'il vous aidera à faire ressortir vos composants. 

Si vous aimeriez voir plus de ces composants cool [TailwindCSS et Framer motion](https://aceternity.com/components), faites-le moi savoir sur [Twitter](https://twitter.com/mannupaaji) et je serais plus qu'heureux de travailler dessus. :)

Bon codage ! ✨
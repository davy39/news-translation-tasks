---
title: Comment créer un menu hamburger animé dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-07T17:15:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-animated-hamburger-menu-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Frame-14.jpg
tags:
- name: animation
  slug: animation
- name: React
  slug: react
seo_title: Comment créer un menu hamburger animé dans React
seo_desc: "By Yazdun Fadali\nIf you're looking to add some polished animations to\
  \ your React apps, Framer Motion is the tool for the job. \nIn this tutorial, I'll\
  \ walk you through creating a fully animated mobile menu using Framer Motion in\
  \ React.\nWhat Are We Goi..."
---

Par Yazdun Fadali

Si vous cherchez à ajouter des animations polies à vos applications React, Framer Motion est l'outil qu'il vous faut. 

Dans ce tutoriel, je vais vous guider à travers la création d'un menu mobile entièrement animé en utilisant Framer Motion dans React.

## **Que allons-nous construire ?**

Dans ce tutoriel, je vais vous guider étape par étape pour implémenter un composant de menu mobile animé et réactif complet dans React en utilisant Framer Motion.

Vous pouvez également consulter ce [tutoriel vidéo](https://youtu.be/FZRzwMjdwxk?si=QX-2tosWy1q3KwRI) détaillé que j'ai créé basé sur cet article.

![Un enregistrement d'écran qui affiche un menu mobile entièrement animé. Sur les grands écrans, les routes seront affichées normalement sous forme de liste non ordonnée, mais sur les petits écrans, vous verrez une icône de hamburger. Une fois que vous cliquez sur l'icône de hamburger, vous pourrez voir les éléments de menu mobile animés](https://www.freecodecamp.org/news/content/images/2023/11/ezgif-5-e28e07a84d.gif)
_Barre de navigation réactive avec un menu mobile entièrement animé_

## Prérequis

Bien que la familiarité préalable avec Framer Motion ne soit pas requise pour commencer ce tutoriel, il est important d'avoir une base en React, car je ne couvrirai pas les concepts de base de React en détail ici.

Tout au long de ce tutoriel, vous utiliserez les outils suivants :

* **React 18.2.0** : React est une bibliothèque JavaScript utilisée pour construire des interfaces utilisateur. Elle permet aux développeurs de créer des composants UI réutilisables et de mettre à jour efficacement l'UI en fonction des changements de données.
* **Framer Motion** : Framer Motion est une bibliothèque d'animation populaire pour React. Elle fournit une interface facile à utiliser pour créer des animations et des transitions fluides et interactives dans les applications web.
* **Vite** : Vite est un serveur de développement rapide et un outil de construction pour les applications web modernes.
* **Tailwind** : Vous utiliserez Tailwind pour appliquer des styles à vos composants React dans ce tutoriel.

## **Commencer**

Pour commencer ce tutoriel, j'ai préparé un projet de base pour vous qui contient toutes les dépendances requises, donc vous n'avez pas besoin de configurer votre projet à partir de zéro.

Il vous suffit de cloner le [modèle de départ](https://github.com/Yazdun/react-burger-menu/tree/starter) depuis le dépôt GitHub et ensuite de suivre le tutoriel.

* Modèle de départ : [Voir sur GitHub](https://github.com/Yazdun/react-animated-sidebar/tree/starter)
* Version finale : [Voir sur GitHub](https://github.com/Yazdun/react-burger-menu/tree/main)

## Comment créer une barre de navigation simple dans React

Avant de commencer à créer le menu mobile animé, il est important d'abord de s'occuper de la barre de navigation de bureau. Vous voulez vous assurer que votre barre de navigation reste non seulement réactive mais aussi esthétique sur les appareils de bureau.

J'ai déjà configuré un répertoire `routes` pour vous, contenant un tableau avec toutes les routes nécessaires pour votre application. Vous pouvez facilement afficher ces routes en important le tableau et en le parcourant chaque fois que nécessaire.

```ts
//📂./src/routes.ts

import { BiHomeAlt2 } from "react-icons/bi";
import { FiSearch } from "react-icons/fi";
import { PiChatCircleBold } from "react-icons/pi";
import { IoPricetagsOutline } from "react-icons/io5";

export const routes = [
  {
    title: "Accueil",
    href: "#",
    Icon: BiHomeAlt2,
  },
  {
    title: "Explorer",
    href: "#",
    Icon: FiSearch,
  },
  {
    title: "Tarifs",
    href: "#",
    Icon: IoPricetagsOutline,
  },
  {
    title: "À propos",
    href: "#",
    Icon: PiChatCircleBold,
  },
];
```

Chaque objet dans le tableau `routes` inclut une icône importée de la bibliothèque [React Icons](https://react-icons.github.io/react-icons/), un titre clair et un `href` qui indique le chemin de la route.

Affichons le tableau `routes` sur la barre de navigation. Ouvrez `./src/components/nav-desktop` et ajoutez le code suivant :

```tsx
//📂./src/components/nav-desktop.tsx

import { routes } from "../routes";

export const NavDesktop = () => {
  return (
    <ul className="hidden lg:flex lg:items-center gap-5 text-sm">
      {routes.map((route) => {
        const { Icon, href, title } = route;
        return (
          <li>
            <a
              href={href}
              className="flex items-center gap-1 hover:text-neutral-400 transition-all"
            >
              <Icon />
              {title}
            </a>
          </li>
        );
      })}
    </ul>
  );
};
```

Le composant `NavDesktop` rend une liste non ordonnée (`ul`) contenant des routes. Il utilise le tableau `routes` importé depuis le fichier `../routes` pour générer dynamiquement des éléments de liste (`li`) avec des liens (`a`) et des icônes.

![Éléments de navigation de bureau](https://www.freecodecamp.org/news/content/images/2023/11/image-7.png)
_Navigation de bureau_

Vous venez de créer une belle barre de navigation de bureau, super ! 🎉

Maintenant que vous avez votre barre de navigation de bureau en place, il est temps de créer le menu mobile animé. 

## Comment créer une icône de hamburger animée dans React

Commençons par créer un bouton avec une icône de hamburger. Ce bouton permettra aux utilisateurs de basculer la visibilité de votre menu mobile.

[Hamburger React](https://hamburger-react.netlify.app/) est une bibliothèque React incroyablement légère qui fournit une large gamme d'icônes de hamburger animées pour une intégration fluide dans vos applications React.

Bien que vous ayez certainement la possibilité de créer vos propres icônes de hamburger animées à partir de zéro, dans ce tutoriel, vous utiliserez [Hamburger React](https://hamburger-react.netlify.app/) pour implémenter l'icône de hamburger animée et passer à la construction du menu mobile animé.

Ouvrez `./src/components/nav-mobile.tsx` et ajoutez le code suivant :

```tsx
//📂./src/components/nav-mobile.tsx

import { useClickAway } from "react-use";
import { useRef } from "react";
import { useState } from "react";
import { Squash as Hamburger } from "hamburger-react";
import { AnimatePresence, motion } from "framer-motion";
import { routes } from "../routes";

export const NavMobile = () => {
  const [isOpen, setOpen] = useState(false);

  return (
    <div className="lg:hidden ">
      <Hamburger toggled={isOpen} size={20} toggle={setOpen} />
    </div>
  );
};
```

Ce composant React crée un bouton qui ouvre et ferme un menu. Le bouton commence fermé (`isOpen` est `false`). Lorsqu'il est cliqué, il bascule la visibilité du menu.

De plus, le composant `NavMobile` restera caché sur les grands écrans, car vous avez déjà implémenté le composant de barre de navigation de bureau.

![Bouton cliquable en haut à droite avec une icône de hamburger. Cliquer bascule entre les états ouvert et fermé et déclenche des transitions fluides.](https://www.freecodecamp.org/news/content/images/2023/11/ezgif-2-a7c01fc67a.gif)
_Icône de hamburger cliquable. Basculer entre les états ouvert et fermé avec des animations fluides._

## Comment créer un menu mobile animé dans React

Améliorons la fonctionnalité de votre menu mobile et affichons les routes de navigation une fois que l'utilisateur clique sur le bouton hamburger.

Ouvrez `./src/components/nav-mobile.tsx` et ajoutez le code suivant :

```tsx
//📂./src/components/nav-mobile.tsx

import { useClickAway } from "react-use";
import { useRef } from "react";
import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Squash as Hamburger } from "hamburger-react";
import { routes } from "../routes";

export const NavMobile = () => {
  const [isOpen, setOpen] = useState(false);
  const ref = useRef(null);

  useClickAway(ref, () => setOpen(false));

  return (
    <div ref={ref} className="lg:hidden ">
      <Hamburger toggled={isOpen} size={20} toggle={setOpen} />
      {isOpen && (
        <div className="fixed left-0 shadow-4xl right-0 top-[3.5rem] p-5 pt-0 bg-neutral-950 border-b border-b-white/20">
          <ul className="grid gap-2">
            {routes.map((route) => {
              const { Icon } = route;

              return (
                <li
                  key={route.title}
                  className="w-full p-[0.08rem] rounded-xl bg-gradient-to-tr from-neutral-800 via-neutral-950 to-neutral-700"
                >
                  <a
                    onClick={() => setOpen((prev) => !prev)}
                    className={
                      "flex items-center justify-between w-full p-5 rounded-xl bg-neutral-950"
                    }
                    href={route.href}
                  >
                    <span className="flex gap-1 text-lg">{route.title}</span>
                    <Icon className="text-xl" />
                  </a>
                </li>
              );
            })}
          </ul>
        </div>
      )}
    </div>
  );
};

```

Voici une explication simplifiée du composant jusqu'à présent :

**Configuration de l'état et des références :**

* Le composant commence par créer deux variables : `isOpen` et `ref`.
* `isOpen` garde une trace de l'état du menu (ouvert ou fermé).
* `ref` est comme une étiquette que nous attachons à un élément dans le HTML. Dans ce cas, il est utilisé pour référencer le conteneur du menu.

**Gestion des clics en dehors du menu :**

* Le composant utilise le hook `useClickAway` de la bibliothèque [React-Use](https://streamich.github.io/react-use/) pour détecter quand un utilisateur clique en dehors du menu. Lorsqu'un clic est détecté, il déclenche une fonction qui ferme le menu en définissant `isOpen` sur `false`.

**Rendu du bouton hamburger :**

* Le composant rend un bouton qui ressemble à une icône de hamburger. Ce bouton sert d'interrupteur pour ouvrir et fermer le menu.
* Lorsque le bouton est cliqué, il bascule la valeur de `isOpen`, ce qui contrôle l'affichage du menu.

**Affichage du menu :**

* Si `isOpen` est `true`, cela signifie que le menu doit être affiché. Dans ce cas, une liste de liens et d'icônes est affichée.
* Chaque lien représente une page ou une section différente. Lorsqu'un lien est cliqué, il met à jour `isOpen` pour fermer le menu.

C'est le flux de base de ce composant React ! Il configure l'état pour suivre l'état ouvert/fermé du menu, gère les clics en dehors du menu, rend un bouton pour basculer le menu et affiche le contenu du menu lorsqu'il doit être ouvert.

![Une fois que vous cliquez sur l'icône de hamburger en haut à droite de l'écran, vous pourrez voir le menu mobile et les éléments de navigation. Cliquer sur le bouton hamburger basculera la visibilité du menu mobile](https://www.freecodecamp.org/news/content/images/2023/11/ezgif-2-24c6a3c200.gif)
_Fonctionnalité de basculement du menu hamburger_

Maintenant, utilisons [Framer Motion](https://www.framer.com/motion/) pour animer le menu mobile. Ouvrez `./src/components/nav-mobile.tsx` et ajoutez le code suivant :

```tsx
//📂./src/components/nav-mobile.tsx

import { useClickAway } from "react-use";
import { useRef } from "react";
import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Squash as Hamburger } from "hamburger-react";
import { routes } from "../routes";

export const NavMobile = () => {
  const [isOpen, setOpen] = useState(false);
  const ref = useRef(null);

  useClickAway(ref, () => setOpen(false));

  return (
    <div ref={ref} className="lg:hidden ">
      <Hamburger toggled={isOpen} size={20} toggle={setOpen} />
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="fixed left-0 shadow-4xl right-0 top-[3.5rem] p-5 pt-0 bg-neutral-950 border-b border-b-white/20"
          >
            <ul className="grid gap-2">
              {routes.map((route, idx) => {
                const { Icon } = route;

                return (
                  <motion.li
                    initial={{ scale: 0, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    transition={{
                      type: "spring",
                      stiffness: 260,
                      damping: 20,
                      delay: 0.1 + idx / 10,
                    }}
                    key={route.title}
                    className="w-full p-[0.08rem] rounded-xl bg-gradient-to-tr from-neutral-800 via-neutral-950 to-neutral-700"
                  >
                    <a
                      onClick={() => setOpen((prev) => !prev)}
                      className={
                        "flex items-center justify-between w-full p-5 rounded-xl bg-neutral-950"
                      }
                      href={route.href}
                    >
                      <span className="flex gap-1 text-lg">{route.title}</span>
                      <Icon className="text-xl" />
                    </a>
                  </motion.li>
                );
              })}
            </ul>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};
```

Décomposons les parties liées à l'animation :

**AnimatePresence :**

Le composant `AnimatePresence` est un conteneur spécial fourni par la bibliothèque `framer-motion`. Il gère le cycle de vie des animations pour les éléments entrant et sortant du DOM. 

Dans ce code, il enveloppe le contenu du menu, indiquant qu'il doit être animé lorsqu'il apparaît ou disparaît.

**Animation du contenu du menu :**

Le contenu du menu (la partie qui apparaît lorsque le menu est ouvert) reçoit des instructions d'animation. Ces instructions incluent :

* `initial` : Cela définit l'état de départ de l'animation. Ici, il est défini pour commencer avec une opacité nulle (complètement invisible).
* `animate` : Cela définit comment l'animation progresse. Il spécifie que l'opacité doit passer à 1 (complètement visible), créant un effet de fondu en entrée.
* `exit` : Cela définit comment l'animation se comporte lorsque le contenu du menu est retiré du DOM. Ici, il définit l'opacité à 0, créant un effet de fondu en sortie.
* `transition` : Cela contrôle comment l'animation se comporte dans le temps. Dans ce cas, il est défini pour avoir une durée de 0,2 seconde, ce qui signifie qu'il faut 0,2 seconde pour que l'animation se termine.

**Animation des éléments de lien :**

Chaque élément de lien individuel dans le menu reçoit des instructions d'animation. Ces instructions incluent :

* `initial` : Cela définit l'état de départ de l'animation. Il commence avec l'élément petit (échelle 0) et complètement invisible (opacité 0).
* `animate` : Cela définit comment l'animation progresse. Il spécifie que l'élément doit grandir à sa taille normale (échelle 1) et devenir complètement visible (opacité 1).
* `transition` : Cela détermine le comportement de l'animation. Il est défini sur une animation "spring", qui donne un effet rebondissant. Les valeurs `stiffness` et `damping` contrôlent le rebond, tandis que `delay` crée un effet décalé, faisant que chaque élément commence son animation légèrement plus tard que le précédent.

Ces animations ajoutent une touche visuelle au menu et aux éléments de menu, les faisant passer en douceur lors de l'ouverture et de la fermeture.

![Un enregistrement d'écran qui affiche un menu mobile entièrement animé. Sur les grands écrans, les routes seront affichées normalement sous forme de liste non ordonnée, mais sur les petits écrans, vous verrez une icône de hamburger. Une fois que vous cliquez sur l'icône de hamburger, vous pourrez voir les éléments de menu mobile animés](https://www.freecodecamp.org/news/content/images/2023/11/ezgif-5-e28e07a84d.gif)
_Éléments de menu animés_

Félicitations, vous avez maintenant un menu Hamburger entièrement animé, excellent travail ! 🎉

## **Conclusion** 

Dans ce tutoriel, nous avons intégré Framer Motion pour créer un menu hamburger animé dynamique dans React. En appliquant les techniques couvertes, vous possédez maintenant les compétences pour améliorer la navigation utilisateur avec des animations fluides et des éléments interactifs.

Vous pouvez me suivre sur [Twitter](https://twitter.com/Yazdun) où je partage plus de conseils utiles sur le développement web. Bon codage !
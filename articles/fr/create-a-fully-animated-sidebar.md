---
title: Comment créer une barre latérale entièrement animée dans React.js en utilisant
  Framer Motion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-16T23:49:46.000Z'
originalURL: https://freecodecamp.org/news/create-a-fully-animated-sidebar
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Frame-11.jpg
tags:
- name: animation
  slug: animation
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer une barre latérale entièrement animée dans React.js en utilisant
  Framer Motion
seo_desc: 'By Yazdun Fadali

  Adding smooth and professional animations to your user interfaces can be a bit tricky.
  In this tutorial, I''ll show you how to use Framer Motion in your React apps to
  create beautiful animations.

  This guide is perfect if you''re new to...'
---

Par Yazdun Fadali

Ajouter des animations fluides et professionnelles à vos interfaces utilisateur peut être un peu délicat. Dans ce tutoriel, je vais vous montrer comment utiliser Framer Motion dans vos applications React pour créer de belles animations.

Ce guide est parfait si vous êtes nouveau dans Framer Motion ou si vous souhaitez simplement faire ressortir vos animations. Nous allons parcourir les étapes ensemble, ce qui vous permettra d'ajouter facilement ces belles touches professionnelles à vos projets. Commençons !

## Que allons-nous construire ?

Au cours de ce tutoriel, je vais vous guider étape par étape pour implémenter un composant de barre latérale animée complet dans React et Framer Motion.

Vous pouvez également consulter ce [tutoriel vidéo](https://youtu.be/5_DTV975MOI?si=StJd9XNDYAl_YN3m) approfondi que j'ai créé basé sur cet article.

![composant de barre latérale animée à thème sombre](https://www.freecodecamp.org/news/content/images/2023/10/ezgif-5-0b78748b45.gif)
_Composant de barre latérale animée_

## Installation

Pour commencer avec ce tutoriel, j'ai préparé un projet de base pour vous qui contient toutes les dépendances requises, vous n'avez donc pas besoin de configurer votre projet à partir de zéro.

Clonez simplement le [modèle de base](https://github.com/Yazdun/react-animated-sidebar/tree/starter) depuis le dépôt GitHub, puis suivez le tutoriel.

* Modèle de base : [Voir sur GitHub](https://github.com/Yazdun/react-animated-sidebar/tree/starter)
* Version finale : [Voir sur GitHub](https://github.com/Yazdun/react-animated-sidebar)

## Qu'est-ce que Framer Motion ?

Framer Motion est une bibliothèque d'animation simple mais puissante pour React. Avec Framer Motion, vous pouvez ajouter sans effort des animations et des interactions fluides et professionnelles à vos projets React.

Framer Motion vous permet de créer des éléments tels que des boutons glissant en douceur, du texte s'estompant, ou même des animations complexes avec seulement quelques lignes de code simples.

Vous pourriez également trouver intéressant de savoir que Framer Motion est ce qui alimente Framer, un outil populaire pour les concepteurs web professionnels. Il est donc approuvé par les experts pour créer ces animations cool que vous voyez souvent sur des sites web très soignés.

## Comment créer une barre de navigation simple dans React

Dans cette section, vous allez créer une barre de navigation simple. Ouvrez simplement le fichier `components/Navigation` et insérez le code suivant :

```jsx
//🗃components/Navigation

import { Sidebar } from './Sidebar'
import { FiGithub } from 'react-icons/fi'

export const Navigation = () => {
  return (
    <nav className="flex items-center justify-between px-5 py-2 border-b-2 border-zinc-800">
      <div className="flex items-center gap-3">
        <Sidebar />
        <p>Animated Sidebar</p>
      </div>
      <a
        className="flex items-center gap-2 px-4 py-2 text-orange-400 bg-orange-700/20 rounded-xl"
        href=""
      >
        <FiGithub className="text-lg" />
        Source Code
      </a>
    </nav>
  )
}

```

Ce composant rend une barre de navigation sur une page web. Dans cette barre de navigation, il y a deux sections principales. La première section inclut le composant `Sidebar`. La deuxième section contient un élément de lien stylisé comme un bouton avec une icône.

Ce code configure essentiellement une interface de navigation de base avec des styles prédéfinis pour une application React.

## Comment créer un composant de barre latérale simple dans React

Dans cette section, vous allez construire un composant de barre latérale simple dans React. Tout d'abord, ouvrez `components/Sidebar` et ajoutez le code suivant :

```jsx
//🗃components/Sidebar

export const Sidebar = () => {
  const [open, setOpen] = useState(false)
  const ref = useRef(null)
  useClickAway(ref, () => setOpen(false))
  const toggleSidebar = () => setOpen(prev => !prev)

  return (
    <>
      <button
        onClick={toggleSidebar}
        className="p-3 border-2 border-zinc-800 rounded-xl"
        aria-label="toggle sidebar"
      >
        <GiHamburgerMenu />
      </button>
      {open && (
        <>
          <div
            aria-hidden="true"
            className="fixed bottom-0 left-0 right-0 top-0 z-40 bg-[rgba(0,0,0,0.1)] backdrop-blur-sm"
          ></div>
          <div
            className="fixed top-0 bottom-0 left-0 z-50 w-full h-screen max-w-xs border-r-2 border-zinc-800 bg-zinc-900"
            ref={ref}
            aria-label="Sidebar"
          >
            <div className="flex items-center justify-between p-5 border-b-2 border-zinc-800">
              <span>Welcome</span>
              <button
                onClick={toggleSidebar}
                className="p-3 border-2 border-zinc-800 rounded-xl"
                aria-label="close sidebar"
              >
                <AiOutlineRollback />
              </button>
            </div>
            <ul>
              {items.map((item, idx) => {
                const { title, href, Icon } = item
                return (
                  <li key={title}>
                    <a
                      onClick={toggleSidebar}
                      href={href}
                      className="flex items-center justify-between gap-5 p-5 transition-all border-b-2 hover:bg-zinc-900 border-zinc-800"
                    >
                      <span>{title}</span>
                      <div>
                        <Icon className="text-2xl" />
                      </div>
                    </a>
                  </li>
                )
              })}
            </ul>
          </div>
        </>
      )}
    </>
  )
}

const items = [
  { title: 'Home', Icon: BiHomeSmile, href: '#' },
  { title: 'About', Icon: BiUser },
  { title: 'Contact', Icon: HiOutlineChatBubbleBottomCenterText, href: '#' },
  { title: 'Settings', Icon: FiSettings, href: '#' },
  { title: 'Shop', Icon: FiShoppingCart, href: '#' },
]

```

Ce composant crée un menu de navigation latéral repliable.

Lorsque le bouton de la barre latérale est cliqué, la barre latérale s'ouvre ou se ferme. À l'intérieur de la barre latérale, il y a des éléments de menu comme `Home`, `About`, `Contact`, et ainsi de suite, représentés par des icônes.

Cliquer sur l'un de ces éléments effectuera une action, comme naviguer vers une page différente.

Le composant gère également diverses interactions, telles que cliquer à l'extérieur de la barre latérale pour la fermer.

Dans l'ensemble, ce composant configure un menu latéral fonctionnel et interactif pour une application web. Voici à quoi ressemble votre barre latérale pour l'instant :

![Aperçu du composant de barre latérale simple](https://www.freecodecamp.org/news/content/images/2023/10/ezgif-3-fc03bdde04.gif)
_Composant de barre latérale_

Bien que cette barre latérale fonctionne parfaitement, vous pouvez remarquer qu'il n'y a pas d'animations présentes. Intégrons maintenant Framer Motion et incorporons quelques animations fluides dans cette barre latérale.

## Comment animer les composants React avec Framer Motion

Maintenant que vous avez une barre latérale fonctionnelle, améliorons-la avec quelques animations pour ajouter un peu de panache. Ouvrez `components/Sidebar` et ajoutez le code suivant :

```jsx
import { useRef, useState } from 'react'
import { GiHamburgerMenu } from 'react-icons/gi'
import { AnimatePresence, motion } from 'framer-motion'
import { useClickAway } from 'react-use'
import { AiOutlineRollback } from 'react-icons/ai'
import { BiHomeSmile, BiUser } from 'react-icons/bi'
import { HiOutlineChatBubbleBottomCenterText } from 'react-icons/hi2'
import { FiSettings, FiShoppingCart } from 'react-icons/fi'

export const Sidebar = () => {
  const [open, setOpen] = useState(false)
  const ref = useRef(null)
  useClickAway(ref, () => setOpen(false))
  const toggleSidebar = () => setOpen(prev => !prev)

  return (
    <>
      <button
        onClick={toggleSidebar}
        className="p-3 border-2 border-zinc-800 rounded-xl"
        aria-label="toggle sidebar"
      >
        <GiHamburgerMenu />
      </button>
      <AnimatePresence mode="wait" initial={false}>
        {open && (
          <>
            <motion.div
              {...framerSidebarBackground}
              aria-hidden="true"
              className="fixed bottom-0 left-0 right-0 top-0 z-40 bg-[rgba(0,0,0,0.1)] backdrop-blur-sm"
            ></motion.div>
            <motion.div
              {...framerSidebarPanel}
              className="fixed top-0 bottom-0 left-0 z-50 w-full h-screen max-w-xs border-r-2 border-zinc-800 bg-zinc-900"
              ref={ref}
              aria-label="Sidebar"
            >
              <div className="flex items-center justify-between p-5 border-b-2 border-zinc-800">
                <span>Welcome</span>
                <button
                  onClick={toggleSidebar}
                  className="p-3 border-2 border-zinc-800 rounded-xl"
                  aria-label="close sidebar"
                >
                  <AiOutlineRollback />
                </button>
              </div>
              <ul>
                {items.map((item, idx) => {
                  const { title, href, Icon } = item
                  return (
                    <li key={title}>
                      <a
                        onClick={toggleSidebar}
                        href={href}
                        className="flex items-center justify-between gap-5 p-5 transition-all border-b-2 hover:bg-zinc-900 border-zinc-800"
                      >
                        <motion.span {...framerText(idx)}>{title}</motion.span>
                        <motion.div {...framerIcon}>
                          <Icon className="text-2xl" />
                        </motion.div>
                      </a>
                    </li>
                  )
                })}
              </ul>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </>
  )
}

const items = [
  { title: 'Home', Icon: BiHomeSmile, href: '#' },
  { title: 'About', Icon: BiUser },
  { title: 'Contact', Icon: HiOutlineChatBubbleBottomCenterText, href: '#' },
  { title: 'Settings', Icon: FiSettings, href: '#' },
  { title: 'Shop', Icon: FiShoppingCart, href: '#' },
]

const framerSidebarBackground = {
  initial: { opacity: 0 },
  animate: { opacity: 1 },
  exit: { opacity: 0, transition: { delay: 0.2 } },
  transition: { duration: 0.3 },
}

const framerSidebarPanel = {
  initial: { x: '-100%' },
  animate: { x: 0 },
  exit: { x: '-100%' },
  transition: { duration: 0.3 },
}

const framerText = delay => {
  return {
    initial: { opacity: 0, x: -50 },
    animate: { opacity: 1, x: 0 },
    transition: {
      delay: 0.5 + delay / 10,
    },
  }
}

const framerIcon = {
  initial: { scale: 0 },
  animate: { scale: 1 },
  transition: {
    type: 'spring',
    stiffness: 260,
    damping: 20,
    delay: 1.5,
  },
}

```

Passons maintenant en revue les modifications que vous venez d'apporter à votre composant de barre latérale :

* **`motion` de Framer Motion** : `motion` est un élément fourni par la bibliothèque Framer Motion. Il est utilisé pour envelopper d'autres composants ou éléments afin d'activer les effets d'animation. Dans ce code, nous l'avons utilisé pour animer différents éléments de la barre latérale, tels que les superpositions d'arrière-plan et les icônes.
* **`AnimatePresence` de Framer Motion** : `AnimatePresence` est un composant de Framer Motion qui nous aide à animer les composants lorsqu'ils sont montés ou démontés. Il est utilisé pour envelopper les éléments qui peuvent apparaître ou disparaître dynamiquement. Dans ce code, nous l'avons utilisé pour gérer l'animation lorsque la barre latérale s'ouvre ou se ferme.
* **Objets d'animation** : `framerSidebarBackground` – Cet objet contient des propriétés qui définissent comment la superposition d'arrière-plan de la barre latérale s'anime. Il a trois états : initial (quand il n'est pas visible), animate (quand il est pleinement visible), et exit (quand il disparaît). `opacity` est utilisé pour contrôler la transparence de la superposition. `transition` définit comment l'animation passe d'un état à l'autre, y compris la durée de l'animation et un délai.
* `framerSidebarPanel` : Cet objet définit l'animation pour le panneau de la barre latérale lui-même, contrôlant comment il glisse en vue.
* `x` est utilisé pour définir la position horizontale de la barre latérale. Similaire à `framerSidebarBackground`, il définit les états initial, animate et exit, ainsi que les propriétés de transition.
* `framerText` et `framerIcon` : Ces objets définissent les animations pour le texte et les icônes dans les éléments de la barre latérale. Ils contrôlent des propriétés comme l'opacité, la position (x) et l'échelle pour créer des transitions et des effets fluides.

Ces objets d'animation fournissent un moyen structuré de définir comment différents éléments dans la barre latérale doivent s'animer lorsqu'ils apparaissent ou disparaissent. Ils utilisent une combinaison de propriétés comme l'opacité, la position et l'échelle pour animer vos composants React.

![composant de barre latérale animée à thème sombre](https://www.freecodecamp.org/news/content/images/2023/10/ezgif-5-0b78748b45.gif)
_Résultat final_

Félicitations ! Vous avez réussi à donner vie à votre barre latérale en utilisant React et Framer Motion. 🎉

## Conclusion

Dans ce tutoriel, vous avez appris comment créer une barre latérale entièrement animée en utilisant Framer Motion.

Avec cette nouvelle compétence, vous êtes maintenant équipé pour ajouter des animations fluides et professionnelles à vos applications React.

Les possibilités de création d'animations impressionnantes et complexes en utilisant Framer Motion sont infinies.

N'hésitez pas à présenter vos projets sur [Twitter avec moi](https://twitter.com/Yazdun) – j'adorerais voir vos idées créatives prendre vie !
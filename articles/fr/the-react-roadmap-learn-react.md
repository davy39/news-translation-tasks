---
title: Le guide React pour 2024 – Comment apprendre React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-01-09T18:57:12.000Z'
originalURL: https://freecodecamp.org/news/the-react-roadmap-learn-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/react-roadmap-2024.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Le guide React pour 2024 – Comment apprendre React
seo_desc: 'In this guide, I''ll break down a complete roadmap that will cover all
  the concepts, libraries, and tools to help you become a React developer in 2024.

  My goal is to show you the happy path in React, navigating you away from pitfalls
  so you can spend ...'
---

Dans ce guide, je vais décomposer une feuille de route complète qui couvrira tous les concepts, bibliothèques et outils pour vous aider à devenir un développeur React en 2024.

Mon objectif est de vous montrer le chemin le plus efficace dans React, en vous évitant les pièges afin que vous puissiez consacrer votre temps à ce qui compte vraiment dans React pour vous aider à atteindre vos objectifs.

Voici la feuille de route que je choisirais pour tout développeur React, que vous soyez un débutant complet ou plus avancé, pour vous aider à construire des applications incroyables, obtenir un emploi et profiter de l'utilisation de React.

Si vous êtes intéressé par un guide étape par étape sur la façon d'apprendre React en 2024, [consultez cet article](https://www.freecodecamp.org/news/how-to-learn-react-step-by-step/) que j'ai écrit. Je recommande de lire les deux ensemble.

## Voici un aperçu :

1. [Apprendre les concepts de base de React](#heading-apprendre-les-concepts-de-base-de-react)
2. [Apprendre les Hooks de base](#heading-apprendre-les-hooks-de-base)
3. [Concepts intermédiaires de React](#heading-concepts-intermediaires-de-react)
4. [Créer des applications React avec Vite](#heading-creer-des-applications-react-avec-vite)
5. [Récupérer des données avec TanStack Query](#heading-recuperer-des-donnees-avec-tanstack-query)
6. [Gérer l'état avec Zustand](#heading-gerer-letat-avec-zustand)
7. [Styliser avec TailwindCSS et Radix](#heading-styliser-avec-tailwindcss-et-radix)
8. [Ajouter le routage avec TanStack Router](#heading-ajouter-le-routage-avec-tanstack-router)
9. [Construire des formulaires avec React Hook Form](#heading-construire-des-formulaires-avec-react-hook-form)
10. [Applications full-stack React avec Next.js](#heading-applications-full-stack-react-avec-nextjs)

## \ud83e\uddf1 Apprendre les concepts de base de React

Il existe un certain nombre de concepts de base de React qui sont nécessaires pour construire presque toutes les applications React, peu importe leur simplicité ou leur complexité.

Le plus grand concept dans React est sans doute les **composants**. En 2024, presque tous les composants que vous créerez seront des **composants de fonction**.

Ces composants sont composés d'**éléments** React et de **JSX**. Comprendre le comportement de JSX est essentiel, ainsi que le passage de données aux composants en utilisant les props et connaître la différence entre **props et state**. Enfin, savoir comment rendre conditionnellement des parties de l'interface utilisateur avec le **rendu conditionnel** est également clé.

\u23f3 Passez moins de temps sur :

* Les composants de classe, que l'on voit presque exclusivement dans les anciens projets. Les composants de classe ne sont plus le type de composant par défaut en raison des React Hooks, qui sont utilisés uniquement dans les composants de fonction.
* Les anciens modèles comme les render props et les composants d'ordre supérieur ne sont pas nécessaires à apprendre car ils étaient largement utilisés avant l'arrivée des React Hooks en 2018.
* Les concepts simples tels que les listes, les clés et les événements, qui sont moins difficiles à comprendre.

## \ud83c\udfa3 Apprendre les Hooks de base

Après les concepts de base de React, vous avez les Hooks React intégrés. Les plus importants et les plus fréquemment utilisés sont **useState**, **useEffect**, **useRef** et **useContext**.

Pour utiliser ces hooks, vous devrez comprendre les bases de l'état React, comment effectuer un effet de bord avec useEffect, et éviter les pièges potentiels de useEffect, tels que les boucles infinies.

Vous devrez également comprendre les refs pour le hook useRef. Et l'API de contexte pour useContext.

Encore une fois, ce sont ceux que vous allez probablement utiliser 90 % du temps. Les 10 % restants pourraient être des hooks personnalisés que vous créez afin d'ajouter des fonctionnalités uniques à votre application.

\u23f3 Passez moins de temps sur :

* Les hooks comme useReducer, qui ne seront pas utilisés aussi fréquemment en comparaison à useContext.
* Les hooks d'optimisation comme useCallback et useMemo. Ceux-ci peuvent être importants à certains moments, mais vous les utiliserez beaucoup moins fréquemment.

## \ud83e\udde0 Concepts intermédiaires de React

Pour vraiment maîtriser React, vous devez avoir une solide compréhension de certains concepts intermédiaires.

Certains de ces concepts intermédiaires incluent :

* Comprendre ce qui provoque le rendu de React
* Comment déplacer la logique métier dans des hooks réutilisables
* Les modèles de base comme "lifting state up"
* Comment utiliser la composition pour éviter le prop drilling et l'utilisation excessive du contexte

Alors que les concepts de base que j'ai mentionnés sont généralement mieux compris en codant activement et en réalisant des projets React, les concepts intermédiaires nécessitent de comprendre comment React fonctionne.

Heureusement, vous pouvez obtenir toute cette compréhension en lisant la toute nouvelle [documentation React](https://react.dev). Il existe un certain nombre de guides très utiles couvrant ces concepts intermédiaires et parfois avancés.

## \ud83d\udee0\ufe0f Créer des applications React avec Vite

Ce qui est à la fois un point positif et négatif de React est son manque d'opinions. React nous aide à créer des applications monopages, mais nous devons souvent recourir à des bibliothèques tierces pour ajouter des fonctionnalités essentielles.

Pour créer une nouvelle application React en 2024, je recommande vivement d'utiliser l'outil CLI/construction, **Vite**.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.42.58-PM.png)
_Créer des applications React avec Vite_

Vous pouvez utiliser un gestionnaire de paquets comme NPM et une seule commande pour créer une application React à partir de zéro avec tous les outils dont vous avez besoin pour l'exécuter en développement et la construire pour la production.

```bash
npm create vite@latest my-react-app -- --template react

```

Create React App n'est plus recommandé. Il n'est plus aussi activement maintenu et est beaucoup plus lent que Vite.

## \ud83d\udc15 Récupérer des données avec TanStack Query

La récupération de données dans les applications React est difficile sans une bibliothèque dédiée. Sans une bibliothèque dédiée, vous devez effectuer des requêtes HTTP dans le hook useEffect.

Cependant, cela nécessite l'ajout de beaucoup de code supplémentaire pour gérer les états de chargement et d'erreur, et cela ne gère pas beaucoup de logique pour éviter de faire des requêtes inutiles.

La bibliothèque que je recommande pour toute application React ou Next.js serait **TanStack Query** (anciennement connu sous le nom de React Query).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.43.53-PM.png)
_Récupérer des données avec TanStack Query_

Il fournit des hooks simples non seulement pour demander mais aussi pour "muter" (mettre à jour) les données d'un point de terminaison API.

Il couvre presque tout ce que vous pourriez vouloir d'une bibliothèque de récupération de données, y compris la mise en cache, la déduplication de plusieurs requêtes, la connaissance de quand les données sont obsolètes. Et peut être personnalisé exactement comme vous le souhaitez.

Si vous cherchez une bonne alternative, vous pouvez essayer SWR. Il n'a pas autant de fonctionnalités que TanStack Query mais est une autre bonne option légère qui facilite la récupération de données avec React.

## \ud83e\udd39\u200d\u2642\ufe0f Gérer l'état avec Zustand

Les bibliothèques de gestion d'état sont un must dans les applications React lorsque vous atteignez une certaine taille de projet. La bibliothèque de gestion d'état par défaut pour les applications React pendant longtemps a été Redux, et a été améliorée avec Redux Toolkit.

Il y a encore des milliers d'entreprises utilisant Redux même en 2024. Cependant, l'écosystème s'est tourné vers des solutions de gestion d'état plus faciles.

Cela vous permet de décrire votre état comme un objet et d'écrire des fonctions pour mettre à jour les propriétés de cet objet d'état. La bibliothèque de gestion d'état que j'ai utilisée au cours des dernières années est **Zustand**.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.44.32-PM.png)
_Gérer l'état avec Zustand_

C'est une excellente petite bibliothèque très utile – non seulement pour gérer l'état dans n'importe quel composant en utilisant des hooks simples, mais elle offre également des fonctionnalités très pratiques telles que la prévention des rerenders inutiles.

Il existe de nombreuses bonnes alternatives à Zustand comme Recoil et Jotai, qui partagent tous deux une API similaire à Zustand.

## \u2728 Styliser avec TailwindCSS et Radix

Il existe de nombreuses options de style pour React sous forme de bibliothèques de composants. Ce sont des ensembles de composants préconçus, qui offrent non seulement un design cohérent, mais aussi une fonctionnalité intégrée.

Les années passées, j'aurais recommandé quelque chose comme Material UI, mais ces bibliothèques de composants peuvent souvent être inflexibles, difficiles à personnaliser et augmenter considérablement la taille de votre bundle.

Une meilleure alternative pour 2024 vers laquelle de nombreux développeurs et entreprises se tournent est l'utilisation d'une solution comme **Tailwind CSS**. Cela vous permet simplement de styliser vos composants avec des classes préconçues et chaînables, en combinaison avec une bibliothèque de composants minimale, telle que **Radix**.

Radix fournit ce que l'on appelle des primitives. Elles vous permettent de créer des composants très fonctionnels dont votre application a besoin, tels que des dialogues, des boutons, des sélecteurs, des infobulles, et à peu près tout ce à quoi vous pouvez penser, qui peuvent être stylisés de la manière que vous souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.45.07-PM.png)
_Styliser vos applications avec ShadCN UI_

**ShadCN UI** est un ensemble de composants qui utilise à la fois TailwindCSS et les composants Radix et fournit un bon point de départ pour toute application. Vous pouvez également le personnaliser plus qu'une bibliothèque de composants traditionnelle.

Je recommande vivement d'utiliser quelque chose comme ShadCN UI pour les projets React que vous utilisez en 2024.

Si vous souhaitez utiliser une bibliothèque de composants à la place, de bons choix sont Mantine, Chakra UI et Material UI.

## \ud83e\udea7 Ajouter le routage avec TanStack Router

**React Router** reste le routeur de choix pour la plupart des applications React que vous construirez.

React Router existe depuis pratiquement le début de React et continue de recevoir des mises à jour significatives avec React Router 6. Il couvre presque tous les cas d'utilisation que vous pouvez imaginer, comme vous pouvez le voir dans leur documentation complète.

Une alternative importante, cependant, est **TanStack Router**. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.45.50-PM.png)
_Ajouter le routage avec TanStack Router_

C'est un tout nouveau routeur pour 2024 avec une pléthore de grandes fonctionnalités. Il dispose d'une navigation sécurisée par type, d'un support TypeScript intégré, d'un routage imbriqué, d'un préchargement automatique des routes et est conçu pour être utilisé avec des bibliothèques de récupération de données côté client comme TanStack Query et SWR.

Si vous utilisez TanStack Query, je vous recommande vivement de consulter TanStack Router pour les futurs projets React.

## \ud83d\udcd1 Construire des formulaires avec React Hook Form

Les bibliothèques de formulaires ne sont pas toujours nécessaires lors de la construction d'applications React. Mais si vous avez besoin de validation de formulaire, un choix hautement personnalisable et simple est **React Hook Form**.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.46.53-PM.png)
_Validation de formulaire avec React Hook Form_

Avec le hook `useForm` intégré, il est très facile de personnaliser la validation des entrées et les messages d'erreur.

Ce qui est génial avec React Hook Form, c'est qu'il y a très peu de code à ajouter à vos composants. La plupart est abstraite dans le hook useForm lui-même.

D'autres alternatives fiables qui pourraient inclure un peu plus de code à configurer sont Formik et Final Form.

## \ud83e\udd5e Applications full-stack React avec Next.js

Peut-être le choix le plus important ici lors du choix d'une manière de construire un projet React est le framework full-stack React.

Ces frameworks vous permettent de construire non seulement le client React avec lequel les utilisateurs interagissent, mais aussi le côté serveur, où vous pouvez créer des API, ajouter une authentification, et ainsi de suite.

Le framework React le plus populaire est **Next.js** et pour de bonnes raisons. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.47.25-PM.png)
_Construire des applications full-stack avec Next.js_

Next.js 13 nous a apporté les composants serveur, qui nous permettent d'exécuter notre code React sur le serveur. Cela réduit la quantité de JavaScript envoyée à notre client, offrant une meilleure et plus rapide expérience utilisateur globale.

Cela nous permet également de récupérer des données sur le serveur et d'inclure ces données dans notre composant React lors de son rendu initial. Cela signifie que nous pouvons éviter beaucoup de spinners de chargement, tout en donnant à nos applications une expérience similaire à celle d'une application monopage.

L'inconvénient de Next.js est qu'il vient avec beaucoup de modèles qui pourraient sembler en conflit avec les concepts de base de React. Mais c'est fait avec l'intention de faciliter votre vie en tant que développeur React et de construire plus rapidement.

Une bonne alternative à Next.js est **Remix**, qui adoptera bientôt les composants serveur.

## \ud83c\udfc6 Devenir un développeur React professionnel

À la recherche de la ressource ultime pour apprendre React de A à Z ?

\u2728 **[Présentation : Le React Bootcamp](https://www.thereactbootcamp.com)**

Le bootcamp propose toutes les ressources pour vous aider à réussir avec React :

* \ud83c\udfac 200+ vidéos approfondies
* \ud83d\udd79\ufe0f 100+ défis pratiques React
* \ud83d\udee0\ufe0f 5+ projets de portfolio impressionnants
* \ud83d\udcc4 10+ fiches de révision React essentielles
* \ud83e\udd7e Un bootcamp complet Next.js
* \ud83d\uddbc\ufe0f Une série complète de vidéos animées

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même.

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)  
_Cliquez pour commencer_
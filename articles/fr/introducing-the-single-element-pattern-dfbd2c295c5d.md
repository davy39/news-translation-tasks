---
title: Présentation du modèle Single Element
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-21T01:01:57.000Z'
originalURL: https://freecodecamp.org/news/introducing-the-single-element-pattern-dfbd2c295c5d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*safLOvm16NWX1Z4mPBHNCQ.png
tags:
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Présentation du modèle Single Element
seo_desc: 'By Diego Haz

  Rules and best practices for creating reliable building blocks with React and other
  component-based libraries.


  Back in 2002 — when I started building stuff for the web — most developers, including
  me, structured their layouts using <tab...'
---

Par Diego Haz

#### Règles et meilleures pratiques pour créer des blocs de construction fiables avec React et d'autres bibliothèques basées sur les composants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*safLOvm16NWX1Z4mPBHNCQ.png)

En 2002, lorsque j'ai commencé à construire des choses pour le web, la plupart des développeurs, y compris moi, structuraient leurs mises en page en utilisant des balises `<table>`.

Ce n'est qu'en 2005 que j'ai commencé à suivre les [standards du web](https://en.wikipedia.org/wiki/Web_standards).

> Lorsqu'un site web ou une page web est décrit comme conforme aux standards du web, cela signifie généralement que le site ou la page a un HTML, CSS et JavaScript valides. Le HTML doit également répondre aux directives d'accessibilité et sémantiques.

J'ai appris la sémantique et l'accessibilité, puis j'ai commencé à utiliser des balises HTML appropriées et du CSS externe. J'ajoutais fièrement ces [badges W3C](https://www.w3.org/QA/Tools/Icons) à chaque site web que je créais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pFL99e3lxpYN-Fp24HfdBw.jpeg)

Le code HTML que nous écrivions était presque le même que le code de sortie qui allait au navigateur. Cela signifie que la validation de notre sortie en utilisant le [validateur W3C](https://validator.w3.org/) et d'autres outils nous apprenait également à écrire un meilleur code.

Le temps a passé. Pour isoler les parties réutilisables du front-end, j'ai utilisé PHP, des systèmes de templates, jQuery, Polymer, Angular et React. Ce dernier, en particulier, je l'utilise depuis les trois dernières années.

Avec le temps, le code que nous écrivions devenait de plus en plus différent de celui servi à l'utilisateur. De nos jours, nous transpilons notre code de nombreuses manières différentes (en utilisant Babel et TypeScript, par exemple). Nous écrivons [ES2015+](https://devhints.io/es6) et [JSX](https://reactjs.org/docs/introducing-jsx.html), mais le code de sortie sera simplement du HTML et du JavaScript.

Actuellement, même si nous pouvons toujours utiliser les outils W3C pour valider nos sites web, ils ne nous aident pas beaucoup avec le code que nous écrivons. Nous cherchons toujours les meilleures pratiques pour rendre notre code plus cohérent et maintenable. Et, si vous lisez cet article, je suppose que vous cherchez également la même chose.

Et j'ai quelque chose pour vous.

### Le modèle Single Element ([Singel](https://github.com/diegohaz/singel))

Je ne sais pas exactement combien de composants j'ai écrits jusqu'à présent. Mais, si je mets ensemble Polymer, Angular et React, je peux dire en toute sécurité que ce nombre est supérieur à mille.

Outre les projets d'entreprise, je maintiens un [modèle React](https://github.com/diegohaz/arc) avec plus de 40 exemples de composants. De plus, je travaille avec [Raphael Thomazella](https://github.com/Thomazella), qui a également contribué à cette idée, sur un [kit d'outils UI](https://github.com/diegohaz/reas) avec des dizaines d'autres.

De nombreux développeurs ont l'idée fausse que, s'ils commencent un projet avec la structure de fichiers parfaite, ils n'auront aucun problème. La réalité, cependant, est que peu importe à quel point votre structure de fichiers est cohérente. Si vos composants ne suivent pas des règles bien définies, cela rendra éventuellement votre projet difficile à maintenir.

Après avoir créé et maintenu tant de composants, je peux identifier certaines caractéristiques qui les ont rendus plus cohérents et fiables et, par conséquent, plus agréables à utiliser. Plus un composant ressemblait à un élément HTML, plus il devenait **fiable**.

> Il n'y a rien de plus fiable qu'un `<div>`.

Lorsque vous utilisez un composant, vous vous poserez une ou plusieurs de ces questions :

* Question #1 : Et si je dois passer des props aux éléments imbriqués ?
* Question #2 : Cela va-t-il casser l'application pour une raison quelconque ?
* Question #3 : Et si je veux passer un `id` ou un autre attribut HTML ?
* Question #4 : Puis-je le styliser en passant des props `className` ou `style` ?
* Question #5 : Qu'en est-il des gestionnaires d'événements ?

**Fiabilité** signifie, dans ce contexte, ne pas avoir besoin d'ouvrir le fichier et de regarder le code pour comprendre comment il fonctionne. Si vous traitez avec un `<div>`, par exemple, vous connaîtrez les réponses immédiatement :

* [Règle #1 : Rendre un seul élément](#heading-installation)
* [Règle #2 : Ne jamais casser l'application](#a129)
* [Règle #3 : Rendre tous les attributs HTML passés en props](#cbaa)
* [Règle #4 : Toujours fusionner les styles passés en props](#f168)
* [Règle #5 : Ajouter tous les gestionnaires d'événements passés en props](#3646)

C'est le groupe de règles que nous appelons [Singel](https://github.com/diegohaz/singel).

### Développement piloté par le refactoring

> Faites en sorte que cela fonctionne, puis améliorez-le.

Bien sûr, il n'est pas possible d'avoir tous vos composants suivant [Singel](https://github.com/diegohaz/singel). À un moment donné — en fait, à de nombreux moments — vous devrez briser au moins la première règle.

Les composants qui doivent suivre ces règles sont la partie la plus importante de votre application : atomes, primitives, blocs de construction, éléments ou peu importe comment vous appelez vos composants de base. Dans cet article, je vais les appeler **éléments simples**.

Certains d'entre eux sont faciles à abstraire immédiatement : `Button`, `Image`, `Input`. C'est-à-dire, ces composants qui ont une relation directe avec les éléments HTML. Dans d'autres cas, vous ne les identifierez que lorsque vous devrez dupliquer du code. Et c'est bien.

Souvent, chaque fois que vous devez changer un composant, ajouter une nouvelle fonctionnalité ou corriger un bug, vous verrez — ou commencerez à écrire — des styles et comportements dupliqués. C'est le signal pour l'abstraire en un nouvel élément simple.

Plus le pourcentage d'éléments simples dans votre application est élevé par rapport aux autres composants, plus elle sera cohérente et facile à maintenir.

Mettez-les dans un dossier séparé — `elements`, `atoms`, `primitives` — afin que, chaque fois que vous importez un composant depuis celui-ci, vous soyez sûr des règles qu'il suit.

### Un exemple pratique

Dans cet article, je me concentre sur React. Les mêmes règles peuvent être appliquées à n'importe quelle bibliothèque basée sur les composants.

Cela dit, considérons que nous avons un composant `Card`. Il est composé de `Card.js` et `Card.css`, où nous avons des styles pour `.card`, `.top-bar`, `.avatar`, et d'autres sélecteurs de classe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sm0TM1LOvrWi0WBVjVRIsA.png)

À un moment donné, nous devons mettre l'avatar dans une autre partie de l'application. Au lieu de dupliquer le HTML et le CSS, nous allons créer un nouvel élément simple `Avatar` afin de pouvoir le réutiliser.

#### Règle #1 : Rendre un seul élément

Il est composé de `Avatar.js` et `Avatar.css`, qui contient le style `.avatar` que nous avons extrait de `Card.css`. Cela rend simplement une balise `<img>` :

Voici comment nous l'utiliserions à l'intérieur de `Card` et d'autres parties de l'application :

```
<Avatar profile={profile} />
```

#### Règle #2 : Ne jamais casser l'application

Une balise `<img>` ne casse pas l'application si vous ne passez pas d'attribut `src`, même si c'est un attribut requis. Notre composant, cependant, cassera toute l'application si nous ne passons pas `profile`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aAB2QAEHkWxMBo-UFaCsUA.png)

React 16 fournit une [nouvelle méthode de cycle de vie](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html) appelée `componentDidCatch`, qui peut être utilisée pour gérer gracieusement les erreurs à l'intérieur des composants. Même si c'est une bonne pratique d'implémenter des limites d'erreur dans votre application, cela peut masquer des bugs à l'intérieur de notre élément simple.

Nous devons nous assurer que `Avatar` est fiable par lui-même, et supposer que même les props requises peuvent ne pas être fournies par un composant parent. Dans ce cas, en plus de vérifier si `profile` existe avant de l'utiliser, nous devrions utiliser `Flow`, `TypeScript`, ou `PropTypes` pour avertir à ce sujet :

Maintenant, nous pouvons rendre `<Avatar />` sans props et voir dans la console ce qu'il attend de recevoir :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5Cjn18Fr2n_O1wHMGff4wQ.png)

Souvent, nous ignorons ces avertissements et laissons notre console en accumuler plusieurs. Cela rend `PropTypes` inutile, puisque nous ne remarquerons probablement jamais les nouveaux avertissements lorsqu'ils apparaissent. Alors, assurez-vous de toujours résoudre les avertissements avant qu'ils ne se multiplient.

#### Règle #3 : Rendre tous les attributs HTML passés en props

Jusqu'à présent, notre élément simple utilisait une prop personnalisée appelée `profile`. Nous devrions éviter d'utiliser des props personnalisées, surtout lorsqu'elles sont mappées directement aux attributs HTML. En savoir plus à ce sujet ci-dessous, dans [Suggestion #1 : Éviter d'ajouter des props personnalisées](#c3e6).

Nous pouvons facilement accepter tous les attributs HTML dans nos éléments simples en passant simplement toutes les `props` à l'élément sous-jacent. Nous pouvons résoudre le problème avec les props personnalisées en attendant les attributs HTML respectifs à la place :

Maintenant, `Avatar` ressemble davantage à un élément HTML :

```
<Avatar src={profile.photoUrl} alt={profile.photoAlt} />
```

Cette règle inclut également le rendu de `children` lorsque, bien sûr, l'élément HTML sous-jacent l'accepte.

#### Règle #4 : Toujours fusionner les styles passés en props

Quelque part dans votre application, vous voudrez que l'élément simple ait un style légèrement différent. Vous devriez pouvoir le personnaliser que ce soit en utilisant les props `className` ou `style`.

Le style interne d'un élément simple est équivalent au style que les navigateurs appliquent aux éléments HTML natifs. Cela dit, notre `Avatar`, lorsqu'il reçoit une prop `className`, ne devrait pas remplacer celle interne — mais l'ajouter.

Si nous appliquions une prop de `style` interne à `Avatar`, cela pourrait être facilement résolu en utilisant [object spread](https://github.com/tc39/proposal-object-rest-spread/blob/master/Spread.md) :

Maintenant, nous pouvons appliquer de nouveaux styles à notre élément simple de manière fiable :

```
<Avatar  className="my-avatar"  style={{ borderWidth: 1 }}/>
```

Si vous vous retrouvez à devoir dupliquer les nouveaux styles, n'hésitez pas à créer un autre élément simple composant `Avatar`. C'est bien — et souvent nécessaire — de créer un élément simple qui rend un autre élément simple.

#### Règle #5 : Ajouter tous les gestionnaires d'événements passés en props

Puisque nous passons toutes les `props`, notre élément simple est déjà préparé à recevoir n'importe quel gestionnaire d'événements. Cependant, si nous avons déjà ce gestionnaire d'événements appliqué en interne, que devrions-nous faire ?

Dans ce cas, nous avons deux options : nous pouvons remplacer le gestionnaire interne par la prop, ou appeler les deux. C'est à vous de choisir. Assurez-vous simplement de **toujours** appliquer le gestionnaire d'événements provenant de la prop.

### **Suggestions**

#### Suggestion #1 : Éviter d'ajouter des props personnalisées

Lors de la création d'éléments simples — surtout lors du développement de nouvelles fonctionnalités dans votre application — vous serez tenté d'ajouter des props personnalisées afin de les configurer de différentes manières.

En utilisant `Avatar` comme exemple, par quelque excentricité du designer, supposons que vous avez certains endroits où l'avatar doit être carré, et d'autres où il doit être rond. Vous pourriez penser que c'est une bonne idée d'ajouter une prop `rounded` à `Avatar`.

Sauf si vous créez une bibliothèque open source bien documentée, **résistez à cela**. En plus d'introduire le besoin de documentation, ce n'est pas scalable et cela conduira à un code difficile à maintenir. Essayez toujours de créer un nouvel élément simple — tel que `AvatarRounded` — qui rend `Avatar` et le modifie, plutôt que d'ajouter une prop personnalisée.

Si vous continuez à utiliser des noms uniques et descriptifs et à construire des composants fiables, vous pouvez en avoir des centaines. Cela restera hautement maintenable. Votre documentation sera les noms des composants.

#### Suggestion #2 : Recevoir l'élément HTML sous-jacent comme une prop

Toutes les props personnalisées ne sont pas mauvaises. Souvent, vous voudrez changer l'élément HTML sous-jacent rendu par un élément simple. Et ajouter une prop personnalisée est le seul moyen d'y parvenir.

Un exemple courant est le rendu d'un `Button` comme un `<a>` :

```
<Button as="a" href="https://google.com">  Aller sur Google</Button>
```

Ou comme un autre composant :

```
<Button as={Link} to="/posts">  Posts</Button>
```

Si vous êtes intéressé par cette fonctionnalité, je vous recommande de jeter un œil à [ReaKit](https://github.com/diegohaz/reakit), un kit d'outils UI React construit avec Singel en tête.

### Valider vos éléments simples en utilisant Singel CLI

Enfin, après avoir lu tout cela, vous vous êtes peut-être demandé s'il existe un outil pour valider automatiquement vos éléments selon ce modèle. J'ai développé un tel outil, [Singel CLI](https://github.com/diegohaz/singel).

Si vous voulez l'utiliser sur un projet en cours, je vous suggère de créer un nouveau dossier et de commencer à y mettre vos éléments simples.

Si vous utilisez React, vous pouvez installer `singel` via **npm** et l'exécuter de cette manière :

```
$ npm install --global singel$ singel components/*.js
```

La sortie sera similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fE7wp8PS2EG7043OYcQhkg.png)

Une autre bonne façon est de l'installer comme une dépendance de développement dans votre projet et d'ajouter un script dans `package.json` :

```
$ npm install --dev singel
```

```
{  "scripts": {    "singel": "singel components/*.js"  }}
```

Ensuite, exécutez simplement le script **npm** :

```
$ npm run singel
```

### Merci d'avoir lu ceci !

Si vous aimez cela et le trouvez utile, voici quelques choses que vous pouvez faire pour montrer votre soutien :

* Cliquez sur le bouton d'applaudissements ? plusieurs fois sur cet article (jusqu'à 50)
* Donnez une étoile ⭐ sur GitHub : [https://github.com/diegohaz/singel](https://github.com/diegohaz/singel)
* Suivez-moi sur GitHub : [https://github.com/diegohaz](https://github.com/diegohaz)
* Suivez-moi sur Twitter : [https://twitter.com/diegohaz](https://twitter.com/diegohaz)
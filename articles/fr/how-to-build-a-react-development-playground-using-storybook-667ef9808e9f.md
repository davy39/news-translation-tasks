---
title: Comment créer un environnement de développement React avec Storybook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T16:53:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-react-development-playground-using-storybook-667ef9808e9f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*7GPOPeGqBSteTFBK
tags:
- name: JavaScript
  slug: javascript
- name: portfolio
  slug: portfolio
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer un environnement de développement React avec Storybook
seo_desc: 'By Sarah Sweat

  Lately, I have been wanting to try new things and test out new technologies or patterns
  in my React components. I needed a place where I could test these things out without
  launching a new app every time.

  I recently started using React...'
---

Par Sarah Sweat

Récemment, j'ai eu envie d'essayer de nouvelles choses et de tester de nouvelles technologies ou modèles dans mes composants React. J'avais besoin d'un endroit où je pourrais tester ces choses sans lancer une nouvelle application à chaque fois.

J'ai récemment commencé à utiliser React Storybook au travail afin d'établir un nouveau système de design pour les futurs projets. Je l'ai également utilisé pour prototyper plusieurs versions d'un nouvel outil d'édition de contenu sur lequel notre équipe travaille. Associer cet outil à mon désir de créer des composants et d'expérimenter de nouvelles choses de manière peu risquée semblait parfait. Quelques exemples de ces nouvelles "choses" sont React Context, SlateJs et React Hooks.

Cela pourrait également être utilisé comme portfolio et comme une excellente façon de présenter votre travail. Puisque Storybook peut être déployé en tant qu'application autonome, vous pouvez héberger une page web où vous avez une variété de projets et de composants que vous pouvez afficher à des employeurs ou clients potentiels. Une fois déployé, il est aussi simple que de leur envoyer un lien vers votre Storybook !

Cet article se concentrera sur la création de l'environnement Storybook pour React et je prévois de publier à l'avenir sur ce que je crée à l'intérieur !

### Donc... Qu'est-ce que Storybook ?

Extrait directement du site web de Storybook car je ne pourrais pas mieux le dire moi-même :

> "Storybook est un environnement de développement d'interface utilisateur et un terrain de jeu pour les composants UI. L'outil permet aux développeurs de créer des composants indépendamment et de présenter des composants de manière interactive dans un environnement de développement isolé.
> 
> Storybook fonctionne en dehors de l'application principale, de sorte que les utilisateurs peuvent développer des composants UI en isolation sans se soucier des dépendances et des exigences spécifiques à l'application."

Cela signifie... que je peux créer et afficher/interagir avec des composants indépendamment de l'exécution réelle de l'application React ! Et puisque ce projet ne sera pas axé sur les performances ou la DRYness d'une seule application, je peux avoir plusieurs prototypes et versions de composants afin de les perfectionner, permettre aux parties prenantes de les approuver, etc. avant de les intégrer dans l'application pour laquelle ils étaient destinés. Je peux également l'utiliser pour simplement pratiquer la création de composants et tester comment utiliser les nouvelles technologies que j'ai mentionnées précédemment.

Commençons à construire maintenant !

### Créer une application React de base

```bash
npx create-react-app my-playground
```

![Image](https://cdn-media-1.freecodecamp.org/images/f6lC8PLFZ8zCo4fXY-xnXViv6swd9QuntJ2T)

Vous pouvez vous assurer que votre application a été créée avec succès en exécutant `yarn start`. Une nouvelle fenêtre devrait apparaître dans votre navigateur à l'adresse `localhost:3000` qui ressemble à l'image ci-dessus. Une fois confirmé, vous pouvez l'arrêter en appuyant sur ⌘ + C.

### Ajouter Storybook

Tout d'abord, depuis la ligne de commande dans votre projet, vous devrez ajouter Storybook avec la commande suivante :

```bash
npx -p @storybook/cli sb init
```

Ensuite, vous pouvez exécuter Storybook en utilisant :

```bash
yarn storybook
```

Maintenant, vous devriez être opérationnel et voir un écran dans votre navigateur comme celui ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/SvZGeZrDFFxQc-S0gaSxdtpHZmfr-fQSCrZo)
_vue du navigateur de Storybook_

Si vous regardez dans votre dossier de projet, vous remarquerez que certains fichiers ont été ajoutés et d'autres mis à jour :

![Image](https://cdn-media-1.freecodecamp.org/images/HgeQxkKp3SmFN8ULagIKpMhgxn7yOFtY2egL)

Le dossier `./storybook` est l'endroit où vous configurerez beaucoup des paramètres de votre Storybook. Il existe toutes sortes d'add-ons que vous pouvez appliquer à votre projet pour ajouter plus de fonctionnalités. Le fichier `config.js` est généralement l'endroit où vous appliquerez des add-ons et où vous indiquerez à Storybook où trouver vos stories. La configuration par défaut est la suivante :

```js
import { configure } from '@storybook/react';

function loadStories() {
  require('../src/stories');
}

configure(loadStories, module);
```

Cela indique à Storybook de rechercher dans le dossier `../src/stories` les stories que vous avez écrites. Pour l'instant, Storybook a ajouté quelques stories par défaut pour vous. Vous pouvez les consulter pour avoir une idée de la façon d'écrire les stories. Vous rendez finalement vos composants dans leurs propres fonctions et vous pouvez leur passer les props que vous souhaitez.

Comme vous pouvez le voir dans l'exemple ci-dessous, vous pouvez créer plusieurs versions du même composant en le rendant simplement avec différentes props.

![Image](https://cdn-media-1.freecodecamp.org/images/-rM7J25dlSzAAhNn-7EB7KDe2kGKjFpKcOIz)

Vous pouvez imaginer cependant, une fois que vous commencez à créer plus de composants, ce fichier pourrait devenir très grand et vous ne voulez pas avoir à épeler dans votre config chaque fichier avec des stories que vous voulez rendre... Au lieu de cela, une façon pratique de faire cela est de nommer n'importe quel fichier dans votre dossier `src` avec `stories.js` et de laisser Storybook trouver dynamiquement tous les fichiers nommés avec `stories.js` à la fin, dans votre dossier `src` vous mettriez ce qui suit dans votre fichier de configuration :

```js
import { configure } from '@storybook/react'

function loadStories() {
  const req = require.context('../src', true, /\.stories\.js$/)
  req.keys().forEach(filename => req(filename))
}

configure(loadStories, module)
```

Cela permet une structure de fichiers beaucoup plus propre et vous pouvez organiser vos stories par projet ou même par composant dans votre dossier src.

### Construisez vos mini-projets

Construisons un petit composant comme exemple pour montrer comment vous pourriez créer un exemple de projet rapide pour commencer à apprendre l'API Context de React. Dans mon dossier `src`, je vais créer un dossier ContextProject où je vais ajouter un fichier où je vais définir mon composant, puis un autre où je vais définir la story :

![Image](https://cdn-media-1.freecodecamp.org/images/VJQfKZeg40GHgMnVO7Dvwqv5Y-xZDhSYIYgy)

Maintenant, lorsque je vérifie mon Storybook, je vois que j'ai une option de menu pour mon projet Context API et en dessous, je peux cliquer pour voir mon composant Home que j'ai créé :

![Image](https://cdn-media-1.freecodecamp.org/images/glN1nJWxPee5BJ1-rNSpgLJZR631NvnCr6FY)

Et maintenant, je peux commencer à construire mon contexte et d'autres composants dans ce dossier dans `src`. Je pourrai jouer et rendre les composants que je construis, ce qui me permettra de voir rapidement mes changements et de ne pas avoir à me soucier de lancer une nouvelle application React chaque fois que je veux simplement tester une fonctionnalité spécifique ou une nouvelle idée.

Cela permet également une grande flexibilité lorsque vous essayez de prototyper rapidement une nouvelle idée. Vous avez déjà un environnement opérationnel et pouvez avoir vos bibliothèques préférées comme les composants stylisés déjà installés ou avoir des thèmes prédéfinis qui peuvent être facilement importés dans de nouveaux projets. Vous pouvez également prédéfinir certains composants de base tels que des en-têtes stylisés, des divs, des boutons, etc. que vous pouvez partager entre les projets pour accélérer encore plus le développement.

J'espère que cela aide et restez à l'écoute pour les futurs articles sur mes add-ons préférés et les détails sur les projets de test que je construis dans mon Storybook.

Bon codage !

Références :

[**Storybook : atelier de composants UI pour les développeurs frontend**](https://storybook.js.org/)
[_Storybook est un outil open source pour développer des composants UI en isolation pour React, Vue et Angular. Il permet..._](https://storybook.js.org/)
[storybook.js.org](https://storybook.js.org/)

Mon dépôt GitHub :

[**sarahsweat/my-playground**](https://github.com/sarahsweat/my-playground)
[_Contribuez au développement de sarahsweat/my-playground en créant un compte sur GitHub._](https://github.com/sarahsweat/my-playground)
[github.com](https://github.com/sarahsweat/my-playground)
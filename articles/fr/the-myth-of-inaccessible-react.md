---
title: Le Mythe de l'Inaccessibilité de React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-28T12:38:50.000Z'
originalURL: https://freecodecamp.org/news/the-myth-of-inaccessible-react
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/storybook-preview.png
tags:
- name: Accessibility
  slug: accessibility
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Le Mythe de l'Inaccessibilité de React
seo_desc: 'By Ben Robertson

  On Twitter, in Slack, on Discord, in IRC, or wherever you  hang out with other developers
  on the internet, you may have heard some  formulation of the following statements:


  React doesn''t support accessibility

  React makes websites in...'
---

Par Ben Robertson

Sur Twitter, dans Slack, sur Discord, sur IRC, ou partout où vous discutez avec d'autres développeurs sur Internet, vous avez peut-être entendu certaines formulations des déclarations suivantes :

* React ne supporte pas l'accessibilité
* React rend les sites web inaccessibles
* Les gens devraient écrire du HTML accessible au lieu de React
* React est en train de ruiner Internet

Il existe une idée fausse quelque peu répandue selon laquelle les frameworks JavaScript et [l'accessibilité web](https://www.mediacurrent.com/videos/common-accessibility-mistakes-and-how-avoid-them/) ne font pas bon ménage. React, étant l'une des plus grandes bibliothèques JavaScript, est souvent la cible.

Dans ma carrière, cependant, j'ai eu l'expérience intéressante d'être initié à l'accessibilité et à ReactJS à peu près au même moment. J'ai trouvé des outils dans React qui m'ont aidé à en apprendre beaucoup sur l'accessibilité que je n'aurais jamais rencontrée autrement.

Et bien que je ne sois pas en désaccord avec le fait qu'il existe de nombreuses bibliothèques, sites web, applications, etc., écrits en React qui sont inaccessibles, je ne suis pas d'accord pour dire qu'il y a quelque chose d'inhérent à ReactJS qui pousse les développeurs à créer des sites inaccessibles. En fait, j'**adore** les outils d'accessibilité disponibles dans l'écosystème React, donc cet article parle vraiment de la manière dont React peut vous aider à créer des sites web _plus accessibles_ que vous n'en avez jamais créés auparavant.

Je vais décrire comment vous pouvez combiner les outils de linting React, l'audit du DOM et Storybook (un outil de bibliothèque de composants) pour fournir un environnement d'accessibilité vraiment supportif pour les développeurs -- qu'ils soient des professionnels de l'accessibilité ou qu'ils commencent tout juste. À la fin de cet article, vous aurez configuré ce qui suit pour votre [projet Gatsby](https://www.mediacurrent.com/videos/webinar-recording-rain-gatsbyjs-fast-tracking-drupal-8/) (ou autre projet React) :

* rapport en éditeur des erreurs d'accessibilité
* un hook de pré-commit pour empêcher les erreurs d'accessibilité d'entrer dans le dépôt
* rapport de la console du navigateur des erreurs d'accessibilité pendant le développement, avec des liens vers des informations sur la manière de résoudre les erreurs
* une bibliothèque de composants avec des tests d'accessibilité intégrés afin que toutes les parties prenantes du projet puissent tenir l'équipe responsable des problèmes d'accessibilité

_Voulez-vous commencer tout de suite ? J'ai créé un starter Gatsby avec tous ces outils d'accessibilité intégrés. Consultez le **[dépôt gatsby-starter-accessibility](https://github.com/benjamingrobertson/gatsby-starter-accessibility)** qui dispose de toutes ces fonctionnalités disponibles dès la sortie de la boîte._

## Outils et Installation

### **[eslint-plugin-jsx-a11y](https://github.com/evcohen/eslint-plugin-jsx-a11y)**

Si vous avez écrit du JavaScript au cours des dernières années, vous avez probablement utilisé ou au moins entendu parler de [ESLint](https://eslint.org/). Si ce n'est pas le cas, c'est le moment idéal pour commencer à l'utiliser !

ESLint est un utilitaire de linting pour JavaScript qui vous aide à attraper les erreurs de formatage et de syntaxe pendant que vous écrivez du code. La plupart des éditeurs ont une sorte de configuration de linting intégrée, ce qui vous permet de voir les erreurs dans votre éditeur pendant que vous codez.

Cela est vraiment utile pour garder le code cohérent, surtout lorsqu'il y a beaucoup de personnes travaillant sur un projet.

ESLint dispose également d'un écosystème de plugins très sain. Vous pouvez inclure des règles spécifiques au framework JavaScript avec lequel vous travaillez (c'est-à-dire, React, Angular, Vue, etc.), parmi d'autres. Pour React, j'utilise généralement `eslint-plugin-react` et le très utile [eslint-plugin-jsx-a11y](https://github.com/evcohen/eslint-plugin-jsx-a11y). Ce plugin vérifie votre code pour les violations d'accessibilité connues, en utilisant [ces règles](https://github.com/evcohen/eslint-plugin-jsx-a11y#supported-rules).

Avoir ces tests automatisés qui s'exécutent pendant que vous écrivez du code peut prévenir _tant d'erreurs_. Même si les tests d'accessibilité automatisés ne détectent qu'environ [20-30% de toutes les erreurs d'accessibilité](https://www.mediacurrent.com/blog/manual-accessibility-testing-why-how/), attraper ces erreurs avant qu'elles ne se retrouvent dans une base de code peut économiser du temps, du budget et de l'énergie pour effectuer des tests plus manuels une fois le code dans le navigateur.

#### Utilisation

Voici comment vous pouvez commencer avec le linting d'accessibilité dans votre projet React.

Tout d'abord, nous devons installer les packages eslint nécessaires :

`npm install eslint eslint-plugin-react eslint-plugin-jsx-a11y --save-dev`

Dans votre package.json, ajoutez la configuration suivante :

```json
"eslintConfig": {
    "parserOptions": {
      "sourceType": "module"
    },
    "env": {
      "node": true,
      "browser": true,
      "es6": true
    },
    "plugins": [
      "react",
      "jsx-a11y"
    ],
    "extends": [
      "eslint:recommended",
      "plugin:react/recommended",
      "plugin:jsx-a11y/recommended"
    ]
}
```

Avec cela ajouté à votre `package.json`, ESLint utilisera les règles recommandées par ESLint, React et le plugin jsx-a11y pendant que vous travaillez.

Vous voudrez vous assurer que votre éditeur est configuré pour afficher les erreurs de linting dans l'éditeur pour que cela soit vraiment utile.

### Ajouter un hook de pré-commit pour empêcher le code inaccessible dans la base de code en utilisant lint-staged

Maintenant que nous avons configuré un linting d'accessibilité, et espérons que tout le monde travaillant sur le projet a activé le linting dans leur éditeur afin qu'ils puissent voir les erreurs pendant qu'ils travaillent.

Mais vous ne pouvez pas être sûr à 100% que tout le monde prêtera attention au linter. Et même s'ils le font, il est facile de faire un changement rapide, de changer de fichier, et les erreurs seront hors de vue, hors de l'esprit.

Ce que nous pouvons faire comme vérification supplémentaire pour empêcher le code inaccessible d'entrer dans la base de code est d'ajouter un _hook de pré-commit_ qui exécute le linting que nous avons configuré ci-dessus chaque fois qu'un développeur essaie de commiter du code. Si une erreur d'accessibilité est trouvée, un message d'erreur s'affichera avec l'erreur de linting pertinente et l'emplacement de l'erreur, et le commit sera empêché jusqu'à ce que le développeur résolve le problème.

![lint-staged exécutera un hook de pré-commit qui attrapera toute erreur d'accessibilité soulevée par eslint-plugin-jsx-a11y](https://publish.mediacurrent.com/sites/default/files/media/lint-staged-example.png)
_lint-staged exécutera un hook de pré-commit qui attrapera toute erreur d'accessibilité soulevée par eslint-plugin-jsx-a11y_

#### Utilisation

La manière la plus simple de configurer les hooks de linting de pré-commit est d'utiliser le [package](https://www.npmjs.com/package/lint-staged) `[lint-staged](https://www.npmjs.com/package/lint-staged)`. Après avoir configuré toute votre configuration eslint (à partir de notre première étape), exécutez la commande suivante dans votre répertoire de projet :

`npx mrm lint-staged`

Cette commande installera le [package](https://www.npmjs.com/package/husky) `[husky](https://www.npmjs.com/package/husky)` pour gérer les hooks de pré-commit et recherchera dans votre package.json pour configurer automatiquement un hook de pré-commit basé sur votre configuration de linting.

Une configuration simple qui vérifie tous les fichiers JS basée sur la configuration eslint existante dans le dépôt ressemblera à ceci (à partir de `package.json`) :

```json
"husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
},
"lint-staged": {
    "*.js": [
      "eslint"
    ]
}
```

Vous pouvez ajuster cela comme vous le souhaitez. Par exemple, parfois vous voulez limiter le linting à certains répertoires. Pour exécuter le hook de pré-commit uniquement sur les fichiers JS dans le répertoire src, vous mettriez à jour la configuration lint-staged comme ceci :

```json
"lint-staged": {
    "src/*.js": [
      "eslint"
    ]
}
```

Le grand avantage de `lint-staged` est qu'il ne vérifie que les fichiers qui font partie du commit actuel. Si pour une raison quelconque il y a des erreurs préexistantes dans une autre partie de la base de code, le commit ne sera pas empêché--il empêche uniquement l'introduction de nouvelles erreurs.

### react-axe

Le grand avantage de la configuration de linting que nous avons maintenant est qu'elle empêchera de nombreuses erreurs d'être introduites dans la base de code. Cependant, elle n'empêchera pas toutes les erreurs. Certaines erreurs n'existent que lorsque plusieurs composants sont utilisés ensemble, ou à partir de certains contenus, et ne peuvent être attrapées que dans le navigateur.

Heureusement, nous avons aussi une solution pour cela. Axe est un moteur open source pour les tests d'accessibilité automatisés, soutenu par [Deque](https://www.deque.com/). J'ai d'abord découvert axe en utilisant leur extension de navigateur vraiment utile pour [tester des pages individuelles dans le navigateur](https://www.mediacurrent.com/blog/5-website-accessibility-checkers/).

Le problème avec les tests d'accessibilité par extension de navigateur est qu'ils sont généralement exécutés uniquement _après_ la fin du développement. En utilisant la bibliothèque `react-axe`, vous pouvez avoir des tests d'accessibilité automatisés exécutés sur chaque page pendant le développement, afin que les développeurs puissent obtenir des commentaires en temps réel sur les problèmes d'accessibilité. Cela aide à s'assurer que les problèmes d'accessibilité n'atteignent jamais la production, et cela éduque également les développeurs qui ne sont peut-être pas des experts en accessibilité sur les pièges potentiels.

La bibliothèque [react-axe](https://github.com/dequelabs/react-axe) est une implémentation facile à utiliser du moteur axe, spécifiquement pour React.

#### Utilisation

Voici comment commencer à utiliser react-axe avec Gatsby ([quelqu'un a fait un plugin Gatsby pour cela !](https://github.com/angeloashmore/gatsby-plugin-react-axe)) :

`npm install --save gatsby-plugin-react-axe`

Ajoutez gatsby-plugin-react-axe à votre tableau de plugins dans gatsby-config.js

```javascript
module.exports = {
 siteMetadata: {
        title: 'Gatsby Default Starter',
    description:
      'Kick off your next, great Gatsby project with this default starter. This barebones starter ships with the main Gatsby configuration files you might need.',
    author: '@gatsbyjs',
  },
  plugins: [
    'gatsby-plugin-react-axe',
    // other plugins go here
  ],
};
```

Maintenant, lorsque la page se rend, le plugin imprimera toute erreur d'accessibilité dans la console du navigateur. Voici un exemple, où j'ai mis un `<h5>` directement sous un `<h1>` :

![React aXe affichera les erreurs d'accessibilité dans la console pendant que vous développez.](https://publish.mediacurrent.com/sites/default/files/media/react-axe-example.png)
_React aXe affichera les erreurs d'accessibilité dans la console pendant que vous développez._



_React aXe affichera les erreurs d'accessibilité dans la console pendant que vous développez._

Vous pouvez voir que dans le message axe dans la console, il a identifié mon problème de titre : "Les problèmes de titre ne doivent augmenter que d'un" comme un problème modéré. Il inclut également un lien pour en savoir plus sur _pourquoi_ c'est un problème et comment le résoudre : [https://dequeuniversity.com/rules/axe/3.2/heading-order](https://dequeuniversity.com/rules/axe/3.2/heading-order). Et enfin, il affiche l'élément spécifique qui cause le problème pour une identification facile.

Ce type de retour instantané est _si_ important, que vous soyez un débutant en accessibilité ou même un professionnel expérimenté. Attraper les problèmes automatisés instantanément peut vous donner plus de bande passante pour vous concentrer sur d'autres tâches plus impliquées.

### Storybook et Accessibilité

La dernière partie de notre flux de travail d'accessibilité concerne notre [flux de travail basé sur les composants](https://www.mediacurrent.com/blog/building-components-breaking-it-down/). Pour les projets React, j'ai vraiment apprécié utiliser [Storybook](https://storybook.js.org/) pour construire et documenter nos composants front-end.

Storybook est un outil open source pour développer des composants UI en isolation pour React, Vue et Angular. Il rend la construction d'interfaces utilisateur magnifiques organisée et efficace.

- [storybook.js.org](https://storybook.js.org/)

En plus d'avoir un flux de travail et une UI agréables, Storybook dispose d'un excellent [module complémentaire d'accessibilité](https://github.com/storybooks/storybook/tree/master/addons/a11y) qui ajoute un panneau à chaque composant dans votre bibliothèque de composants mettant en évidence les problèmes d'accessibilité.

_Notre configuration Storybook dispose de tests axe intégrés pour chaque composant et d'un simulateur de daltonisme, fourni par le module complémentaire d'accessibilité Storybook._

En coulisses, le module complémentaire utilise en fait aXe pour les tests. C'est vraiment bien, car cela signifie que les tests que nous utilisons en développement sont les mêmes que ceux que nous utilisons dans la bibliothèque de composants. Avoir les erreurs mises en évidence dans la bibliothèque de composants aide également tout le monde dans nos équipes de projet à attraper les problèmes d'accessibilité lorsqu'ils parcourent la bibliothèque, que ce soit à des fins de QA ou d'inspiration de design.

#### Configuration

La configuration de Storybook est un peu plus impliquée, donc si vous n'avez jamais utilisé Storybook auparavant, vous pouvez consulter la [documentation Storybook pour React](https://storybook.js.org/docs/guides/guide-react/) pour une configuration React générique.

Si vous voulez faire fonctionner Storybook avec Gatsby, voir [Visual Testing with Storybook](https://www.gatsbyjs.org/docs/visual-testing-with-storybook/) dans la documentation Gatsby.

Une fois que vous avez configuré Storybook, l'ajout du module complémentaire d'accessibilité est assez simple.

Tout d'abord, installez le module complémentaire :

`npm install @storybook/addon-a11y --save-dev`

Ensuite, ajoutez cette ligne à votre fichier addons.js dans votre répertoire de configuration Storybook :

`import '@storybook/addon-a11y/register';`

Et enfin, ajoutez cette ligne dans votre fichier config.js de Storybook pour ajouter automatiquement le panneau d'accessibilité à tous les composants :

`addDecorator(withA11y);`

Lorsque vous exécutez Storybook maintenant, vous devriez voir le panneau d'accessibilité ([voir une version live ici](https://gatsby-starter-accessibility.netlify.com/storybook/?path=/story/header--default)) :

![Notre configuration Storybook dispose de tests axe intégrés pour chaque composant et d'un simulateur de daltonisme, fourni par le module complémentaire d'accessibilité Storybook.](https://publish.mediacurrent.com/sites/default/files/media/storybook-preview.png)
_Notre configuration Storybook dispose de tests axe intégrés pour chaque composant et d'un simulateur de daltonisme, fourni par le module complémentaire d'accessibilité Storybook._

En tant que note à part - vous pouvez contrôler l'ordre des onglets dans votre panneau de modules complémentaires en fonction de l'ordre dans lequel vous importez les modules complémentaires dans votre fichier addons.js, si vous voulez que le panneau d'accessibilité s'affiche par défaut, assurez-vous qu'il est la première ligne de votre addons.js.

## Conclusion

Si vous n'avez pas suivi la configuration ou si vous voulez simplement configurer un nouveau projet rapidement avec ce flux de travail, consultez le [gatsby-starter-accessibility Gatsby starter !](https://github.com/benjamingrobertson/gatsby-starter-accessibility)

Vous pouvez créer un nouveau site Gatsby avec toutes les configurations que j'ai décrites ci-dessus dès la sortie de la boîte avec cette seule ligne dans votre terminal :

`npx gatsby new my-accessible-project https://github.com/benjamingrobertson/gatsby-starter-accessibility`

Ou vous pouvez consulter la configuration spécifique dans le [dépôt](https://github.com/benjamingrobertson/gatsby-starter-accessibility).

Que vous ayez suivi toutes les étapes ci-dessus ou utilisé le [starter](https://github.com/benjamingrobertson/gatsby-starter-accessibility), vous aurez les fonctionnalités suivantes configurées dans votre projet Gatsby / React :

* rapport en éditeur des erreurs d'accessibilité
* un hook de pré-commit pour empêcher les erreurs d'accessibilité d'entrer dans le dépôt
* rapport de la console du navigateur des erreurs d'accessibilité pendant le développement, avec des liens vers des informations sur la manière de résoudre les erreurs
* une bibliothèque de composants avec des tests d'accessibilité intégrés afin que toutes les parties prenantes du projet puissent tenir l'équipe responsable des problèmes d'accessibilité

Sur un projet complexe avec de nombreux membres d'équipe et des pièces mobiles, l'automatisation des tests d'accessibilité aidera à économiser du temps pour s'assurer que vous pouvez prêter plus d'attention aux tâches d'accessibilité qui ne peuvent pas être attrapées par des tests automatisés.

Au-delà de cela, des outils comme celui-ci peuvent vraiment aider les développeurs à améliorer leurs connaissances en accessibilité.

Je sais que cela m'a aidé--j'espère que cela aidera votre équipe aussi !

_Voulez-vous approfondir la création de sites web accessibles ? Rejoignez mon cours gratuit par e-mail :_ ? [_Erreurs courantes d'accessibilité et comment les éviter_](https://benrobertson.io/courses/common-accessibility-mistakes/). 30 jours, 10 leçons, 100% de plaisir !_ ? [_Inscrivez-vous ici_](https://benrobertson.io/courses/common-accessibility-mistakes/)
---
title: Outils d'accessibilité React – Comment construire des applications React plus
  accessibles
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2021-09-27T14:18:59.000Z'
originalURL: https://freecodecamp.org/news/react-accessibility-tools-build-accessible-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/tool-box.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: React
  slug: react
seo_title: Outils d'accessibilité React – Comment construire des applications React
  plus accessibles
seo_desc: 'Making a website or web app accessible improves the user experience for
  people with disabilities and for all users as well.

  Since developers deal with tight deadlines and competing priorities, it is easy
  to accidentally ship unresolved accessibility ...'
---

Rendre un site web ou une application web accessible améliore l'expérience utilisateur pour les personnes handicapées et pour tous les utilisateurs également.

Puisque les développeurs traitent avec des délais serrés et des priorités concurrentes, il est facile d'envoyer accidentellement des problèmes d'accessibilité non résolus en production. Et les choses deviennent encore plus complexes lorsque l'on travaille avec des frameworks JavaScript tels que React qui impliquent l'écriture de JSX.

Mais heureusement, il existe des outils que vous pouvez utiliser pour lint ou évaluer les problèmes d'accessibilité courants dans votre éditeur de texte ou le navigateur.

Cet article mettra en lumière ces outils d'accessibilité existants et comment vous pouvez les utiliser pour construire des applications React plus accessibles.

## Qu'est-ce que l'accessibilité web ?

Un site web ou une application web est dit accessible s'il n'exclut pas les personnes handicapées de l'utiliser en raison de leur handicap.

Avoir un site web accessible élimine les barrières et garantit que les personnes handicapées et non handicapées ont un accès égal au contenu web et à la fonctionnalité.

Les avantages de rendre votre site web accessible aux personnes handicapées s'étendront à tous les utilisateurs, y compris les personnes non handicapées.

## Pourquoi vous devriez prêter attention à l'accessibilité

Je ne peux pas assez insister sur l'importance de l'accessibilité. Si vous n'y prêtez pas attention dès le début de votre projet, vous risquez de transformer l'accessibilité en un fardeau et en un coût élevé à l'avenir si vous commencez à retrofitter.

Rendre votre site accessible devrait faire partie intégrante de votre projet dès le départ. Cela ne devrait pas être une réflexion après coup.

J'ai mis en évidence ci-dessous pourquoi vous devez vous concentrer sur l'accessibilité dès le début :

### Suit les meilleures pratiques SEO

Certaines des exigences d'accessibilité de base telles que l'utilisation d'éléments HTML sémantiques, l'utilisation appropriée des éléments de titre et l'ajout d'attributs `alt` descriptifs aux balises `img` sont également des meilleures pratiques SEO.

### Améliore l'UX pour tous les utilisateurs

Améliorer l'accessibilité pour les personnes handicapées améliorera l'expérience de tous vos utilisateurs.

Par exemple, ajouter un ratio de contraste suffisant n'est pas seulement utile pour les personnes malvoyantes, daltoniennes ou ayant des troubles cognitifs, mais cela est également utile pour les personnes travaillant dans différentes conditions d'éclairage.

De même, ajouter un attribut `alt` avec un texte approprié aidera les personnes utilisant des lecteurs d'écran ainsi que celles ayant des connexions Internet lentes lorsque l'image échoue à se charger ou prend trop de temps à se charger.

### C'est la bonne chose à faire

En rendant votre site web accessible, vous faites la bonne chose. Ils ont également le droit d'accéder au service que vous offrez et certains sont vos clients. De plus, ce ne sera pas bon pour vous ou votre entreprise si vous êtes accusé de discrimination parce que votre site est inaccessible aux personnes handicapées. Cela nuira à votre marque et à votre réputation.

### Évite les problèmes juridiques

Enfin, vous pourriez rencontrer des exigences légales d'accessibilité selon l'endroit où vous vivez et travaillez. Certains pays ont une législation qui exige que les sites web soient accessibles aux personnes handicapées.

## Normes et directives d'accessibilité

Il existe plusieurs normes et directives d'accessibilité différentes. Les normes les plus notables et largement reconnues ont été développées par le [World Wide Web Consortium (W3C)](https://www.w3.org/Consortium/) à travers son [Web Accessibility Initiative (WAI)](https://www.w3.org/WAI/about/).

J'ai mis en évidence certaines de ces normes et directives dans les sous-sections ci-dessous.

### [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/WAI/standards-guidelines/wcag/)

WCAG est l'une des normes internationalement reconnues pour l'accessibilité du contenu web.

Elle a été développée par le W3C à travers un processus participatif avec des contributions de nombreuses parties prenantes individuelles et institutionnelles du monde entier.

Cette norme explique comment rendre le contenu web plus accessible aux personnes handicapées. Elle a également été [approuvée par l'ISO](https://www.iso.org/standard/58625.html).

Selon le W3C, le WCAG a été créé principalement pour servir de norme de référence pour les individus, les organisations et les gouvernements à l'échelle internationale en matière d'accessibilité du contenu web.

### [Authoring Tools Accessibility Guidelines (ATAG) 2.0](https://www.w3.org/WAI/standards-guidelines/atag/)

ATAG est un ensemble de directives d'accessibilité que vous pouvez utiliser pour concevoir des outils de création de contenu web.

Cette directive vous aide à vous assurer que vous produisez des outils de création accessibles aux personnes handicapées. Les outils devraient, à leur tour, aider les auteurs à créer du contenu web accessible.

### [User Agent Accessibility Guidelines (UAAG) 2.0](https://www.w3.org/WAI/standards-guidelines/uaag/)

L'UAAG 2.0 est une sœur du WCAG. Cet ensemble de directives précise comment vous pouvez rendre les navigateurs, les extensions de navigateur, les lecteurs multimédias et autres agents utilisateurs accessibles aux personnes handicapées.

Il est utilisé par les fournisseurs de navigateurs et les créateurs d'extensions de navigateur pour traiter certains problèmes d'accessibilité tels que la personnalisation du texte dans le navigateur.

Dans la section suivante, nous mettrons en évidence quelques outils qui peuvent vous aider à signaler les problèmes d'accessibilité de base dans vos applications React.

## Outils d'accessibilité pour vos applications React

Il est facile d'envoyer accidentellement des problèmes d'accessibilité en production malgré vos meilleurs efforts pour faire autrement. Dans cette section, nous mettrons en lumière certains outils que vous pouvez utiliser pour mettre en évidence les problèmes d'accessibilité courants.

Il peut être tentant d'omettre certaines fonctionnalités d'accessibilité si vous traitez avec des délais serrés. Il est donc utile d'avoir des outils d'accessibilité dans votre configuration qui vous avertissent des défauts d'accessibilité que vous auriez pu manquer.

Ce n'est en aucun cas une liste exhaustive d'outils d'accessibilité. Si vous connaissez d'autres outils que vous pensez utiles mais qui ne sont pas inclus ici, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/mjmawa). Je serai ravi de mettre à jour cet article. Quelqu'un pourrait les trouver utiles également.

Bien que ces outils attraperont certains problèmes d'accessibilité courants que vous pouvez mesurer de manière programmatique, ils ne feront pas le travail à votre place. Il est de votre responsabilité de faire un effort délibéré pour développer des produits numériques plus accessibles et inclusifs dès la conception du projet.

J'ai classé les outils que nous allons couvrir en deux catégories, à savoir :

* Outils d'accessibilité que vous pouvez intégrer dans votre projet React et qui ont été développés en pensant à React.

* Outils d'audit d'accessibilité généraux que vous pouvez utiliser pour auditer des sites construits avec ou sans React.

Dans les sous-sections ci-dessous, je mettrai en évidence les outils que vous pouvez utiliser dans vos projets React. Ils sont spécialement créés pour être utilisés avec React ou JSX.

### Outils d'accessibilité conçus pour React

#### [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y)

Vous pouvez utiliser cet outil pour lint les problèmes d'accessibilité sur les éléments JSX dans vos projets React. Vous pouvez l'utiliser en conjonction avec des outils tels que eslint pour lint votre projet selon les normes d'accessibilité directement dans votre éditeur de texte.

Puisqu'il est distribué via npm, vous pouvez l'installer en exécutant la commande suivante dans votre projet :

```sh
# en utilisant npm comme gestionnaire de paquets

npm install eslint-plugin-jsx-a11y --save-dev

# en utilisant yarn comme gestionnaire de paquets

yarn add eslint-plugin-jsx-a11y --dev
```

Tout projet React que vous avez créé en utilisant `create-react-app` vient avec cet outil déjà configuré – mais il n'a qu'un sous-ensemble des règles d'accessibilité configurables activées par défaut.

Vous pouvez activer des règles supplémentaires en créant un fichier de configuration `.eslintrc` dans votre projet et en y ajoutant le code suivant. Le code ci-dessous active les règles recommandées :

```js

{
  "extends": ["react-app", "plugin:jsx-a11y/recommended"],
  "plugins": ["jsx-a11y"]
}
```

Si vous souhaitez signaler les problèmes d'accessibilité dans un projet React personnalisé, vous devez installer `eslint` et ajouter `"jsx-a11y"` au champ des plugins de votre fichier de configuration `.eslintrc`.

Il signalera ensuite les problèmes d'accessibilité qu'il peut identifier de manière programmatique et vous avertira directement dans votre éditeur de texte en fonction de votre configuration.

```js

{  "plugins": [    "jsx-a11y"  ]}
```

Pour plus d'informations sur la configuration de cet outil de lint dans un projet React personnalisé, consultez le [README](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y#readme) du projet sur GitHub.

#### [axe accessibility linter](https://marketplace.visualstudio.com/items?itemName=deque-systems.vscode-axe-linter)

Axe accessibility linter est une extension Visual Studio Code que vous pouvez utiliser pour lint React, HTML, Vue et Markdown pour certains défauts d'accessibilité courants.

Il vérifie les problèmes d'accessibilité dans les fichiers `.js`, `.jsx`, `.ts`, `.tsx`, `.vue`, `.html`, `.htm`, `.md` et `.markdown`.

Vous n'avez pas besoin de configuration pour commencer à utiliser axe accessibility linter après l'installation. Vous l'installez depuis le marketplace de VS Code et il commence automatiquement à lint les fichiers compatibles pour les défauts d'accessibilité sans avoir besoin de configuration supplémentaire.

Pour une liste complète des règles utilisées par axe accessibility linter, consultez la page de l'extension sur le marketplace de VS Code.

Vous pouvez également configurer l'outil si vous le souhaitez en activant ou désactivant certaines règles en ajoutant le fichier de configuration `axe-linter.yml` à la racine de votre projet.

Vous avez la possibilité de désactiver les règles d'accessibilité individuellement ou en groupe en utilisant la norme WCAG. L'utilisation de cette fonctionnalité dans votre projet garantira que tous les membres de votre équipe adhèrent à la même norme d'accessibilité.

Vous pouvez ajouter ce qui suit à votre fichier `axe-linter.yml` pour activer ou désactiver certaines règles individuellement. Pour une liste complète des règles configurables, consultez la page de l'extension axe accessibility linter sur le marketplace de VS Code.

```yml

# Pour activer/désactiver les règles au niveau individuel
rules:
  accessibility-rule: false # désactiver la règle
  another-accessibility-rule: true # activer la règle
```

Alternativement, vous pouvez ajouter ce qui suit à votre fichier de configuration `axe-linter.yml` pour désactiver les règles en groupe en utilisant des normes WCAG spécifiques.

Pour une liste complète des normes WCAG configurables, consultez la page de l'extension axe accessibility linter sur le marketplace de VS Code.

```yml


# Pour activer/désactiver les règles au niveau du groupe basé sur la norme WCAG

tags: 
  - wcag2a # Désactiver toutes les règles pour WCAG 2.0 niveau A
  - wcag21a # Désactiver toutes les règles pour WCAG 2.1 niveau A
```

#### [axe-core-react](https://www.npmjs.com/package/@axe-core/react)

Cet outil de test d'accessibilité est développé et maintenu par [Deque Labs](https://www.deque.com/), les mêmes personnes derrière axe accessibility linter.

`axe-core-react` était à l'origine appelé `react-axe`. Vous pouvez l'exécuter dans votre projet React en développement et les défauts d'accessibilité sont mis en évidence dans la console Chrome DevTools chaque fois que votre composant est mis à jour.

Il peut vraiment vous aider à attraper certains problèmes d'accessibilité tôt dans le développement. Pour l'instant, `axe-core-react` fonctionne mieux avec Google Chrome. Contrairement aux deux premiers, il teste l'accessibilité du DOM rendu au lieu de l'élément JSX que vous écrivez dans les composants React.

```js

npm install @axe-core/react --save-dev
```

Vous pouvez ensuite exécuter le package en développement après l'installation.

Le code ci-dessous illustre comment vous pouvez exécuter `axe-core-react` dans votre application React en utilisant la configuration la plus basique. Il existe des options de configuration supplémentaires que vous pouvez lire sur le [README](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/react/README.md) du package sur GitHub.

```js

const React = require('react');
const ReactDOM = require('react-dom');

// Assurez-vous d'exécuter @axe-core/react en développement

if (process.env.NODE_ENV !== 'production') {
  const axe = require('@axe-core/react');
  axe(React, ReactDOM, 1000);
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

Vous pouvez utiliser les outils mentionnés ci-dessus directement dans votre application React pour attraper et corriger les problèmes d'accessibilité courants.

Dans la section suivante, nous examinerons quelques autres outils d'accessibilité qui ne sont pas directement liés à React mais qui sont utiles pour identifier les défauts d'accessibilité de base dans une application React.

### Autres outils d'accessibilité

Il existe de nombreux outils que vous pouvez utiliser pour détecter les problèmes d'accessibilité courants dans le navigateur. J'ai mis en évidence quelques-uns de ces outils ci-dessous.

#### [Axe DevTools browser extension](https://www.deque.com/axe/)

Il s'agit d'une extension de navigateur que vous pouvez utiliser pour effectuer un audit simple de votre page web pour les problèmes d'accessibilité courants.

Votre application doit être hébergée quelque part avant d'utiliser cette extension de navigateur pour vérifier les problèmes d'accessibilité. Elle catégorise les défauts d'accessibilité en critiques, sérieux, modérés et mineurs.

#### [WAVE Evaluation Tool browser extension](https://wave.webaim.org/extension/)

Il s'agit d'une autre extension de navigateur Chrome que vous pouvez utiliser pour identifier les problèmes d'accessibilité sur votre site web.

Tout comme l'extension de navigateur Chrome Axe DevTools, cette extension nécessite que vous hébergiez l'application avant de l'utiliser pour auditer votre application web pour les défauts d'accessibilité.

#### [Google's Lighthouse in Chrome DevTools](https://developers.google.com/web/tools/lighthouse)

Vous pouvez utiliser Google's Lighthouse Chrome DevTools pour auditer votre site web pour les problèmes d'accessibilité. Il génère un rapport que vous pouvez utiliser pour corriger les défauts de votre site web.

Il existe une liste sans fin d'outils d'évaluation de l'accessibilité web générale. Vous pouvez choisir celui qui répond à vos besoins.

Pour une liste complète, vous pouvez consulter la [liste des outils d'évaluation de l'accessibilité web par le W3C](https://www.w3.org/WAI/ER/tools/) ou les [outils d'accessibilité par le projet a11y](https://www.a11yproject.com/resources/#tools).

## Conclusion

L'utilisation d'outils tels que eslint-plugin-jsx-a11y, axe accessibility linter et axe-core-react dans votre projet vous aidera grandement à développer des produits plus accessibles et inclusifs en utilisant React.

Bien qu'ils soient pratiques, les outils mentionnés ici ne signaleront qu'un certain pourcentage de défauts d'accessibilité – principalement ceux qui sont possibles à détecter de manière programmatique.

Il est donc vraiment important d'intégrer les tests automatisés, les tests manuels et les tests utilisateurs réels dans votre développement, car les tests automatisés seuls peuvent ne pas être en mesure de détecter même 50 pour cent des problèmes d'accessibilité dans votre projet.
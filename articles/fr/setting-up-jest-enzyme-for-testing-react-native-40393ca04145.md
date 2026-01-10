---
title: Comment configurer Jest et Enzyme pour tester des applications React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-20T07:55:33.000Z'
originalURL: https://freecodecamp.org/news/setting-up-jest-enzyme-for-testing-react-native-40393ca04145
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ro5rChbmw1G4Cf5i2GAZJg.jpeg
tags:
- name: Jest
  slug: jest
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
seo_title: Comment configurer Jest et Enzyme pour tester des applications React Native
seo_desc: 'By Sam Ollason

  This short article shares my experiences setting up my testing environment to unit
  test React Native components with Jest and Enzyme.


  _Photo by [Unsplash](https://unsplash.com/photos/6wdRuK7bVTE?utm_source=unsplash&utm_medium=referral...'
---

Par Sam Ollason

Cet article court partage mes expériences de configuration de mon environnement de test pour tester les composants React Native avec Jest et Enzyme.

![Image](https://cdn-media-1.freecodecamp.org/images/nks4F4Jhip65XWA3f1i0GDn6a2TvXE0qhwfh)
_Photo par [Unsplash](https://unsplash.com/photos/6wdRuK7bVTE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Neil Soni</a> sur <a href="https://unsplash.com/search/photos/mobile-app?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Outils et environnement de test

La première chose que j'ai apprise, c'est que l'approche et l'infrastructure pour écrire des tests unitaires pour une application React Native sont très similaires à celles pour écrire des tests unitaires pour une application React... peut-être sans surprise.

Cependant, bien que les outils et l'utilisation des suites de test soient très similaires, **l'environnement de test et l'infrastructure doivent être configurés de manière légèrement différente**. Cela est essentiellement dû au fait que les applications React sont conçues pour fonctionner avec le DOM à l'intérieur d'un navigateur, tandis que les applications mobiles ne ciblent pas cette structure de données pour le rendu (elles ciblent des modules 'natifs' réels qui se trouvent sur le système mobile à la place).

#### Utilisation de Jest

[Jest](https://jestjs.io/) est une bibliothèque utilisée pour tester les applications JavaScript.

Je voulais utiliser Jest pour plusieurs raisons :

Tout d'abord, il a été créé et est activement maintenu par Facebook pour leurs propres applications React Native.

Ensuite, il est pré-empaqueté avec la version de React Native avec laquelle je travaillais (créée en utilisant [react-native](https://github.com/facebook/react-native)).

Enfin, **Jest est un framework de test 'complet'** et contient toute la suite d'outils de test dont j'avais besoin. Par exemple, Jest est livré avec une bibliothèque pour vérifier les assertions, un exécuteur de test pour exécuter réellement les tests et des outils pour vérifier la couverture de code. Avec d'autres solutions, il faut choisir et assembler les composants individuels d'une suite de test.

#### Utilisation de Jest + Enzyme

Je voulais combiner Jest et Enzyme. Il y a beaucoup de commentaires légèrement confus sur le web qui comparent 'Jest versus Enzyme'. Cela est un peu trompeur. Alors que Jest est un framework de test, vous pouvez considérer Enzyme comme une bibliothèque qui facilite la sélection et l'interrogation des éléments à l'intérieur d'un DOM émulé. Donc **il est souvent utilisé avec Jest** pour rendre l'écriture de la logique des tests plus propre et plus facile à lire.

Toujours confus ? C'est similaire à la façon dont jQuery a introduit une syntaxe concise et claire pour interroger et sélectionner des éléments dans le DOM, alors que la syntaxe utilisant JavaScript vanilla était (au moins au moment où jQuery a été introduit pour la première fois) moins claire et facile à utiliser. Et les gens ne comparent pas souvent 'jQuery versus JavaScript', sauf s'ils comparent une manière particulière dont les deux approches utilisent pour interroger et modifier les éléments du DOM.

_Note :_ vous pouvez utiliser Jest sans Enzyme (je crois que Facebook fait cela) mais Enzyme rend vos tests un peu plus faciles à créer et à lire. De mon point de vue, combiner Enzyme avec Jest est une question de commodité.

### Configuration de Jest + Enzyme

J'ai dû sauter à travers quelques cerceaux pour configurer avec succès Jest et Enzyme dans mon environnement React Native.

Jest est maintenant inclus avec les applications React Native créées en utilisant l'outil 'react-native'. Donc je pouvais utiliser Jest directement. Magnifique !

Mais j'ai rencontré quelques problèmes en essayant de combiner Enzyme avec React Native en utilisant leur [documentation](https://airbnb.io/enzyme/docs/guides/react-native.html). Je n'ai jamais vraiment compris quel était le problème sous-jacent, mais je continuais à obtenir des erreurs de 'modules non trouvés' comme celle-ci [ici](https://github.com/facebook/react-native/issues/23943).

#### Une solution

En fin de compte, j'ai utilisé une solution qui abstrait essentiellement une partie de la configuration dans un environnement pré-empaqueté en utilisant la bibliothèque [jest-enzyme](https://github.com/FormidableLabs/enzyme-matchers/tree/master/packages/jest-enzyme#readme), puis j'ai veillé à ce que les 'presets' de Jest soient définis sur 'react-native' dans mon package.json.

J'ai suivi les instructions pour installer ces bibliothèques :

```
npm install jest-environment-enzyme jest-enzyme enzyme-adapter-react-16 --save-dev
```

Les erreurs lorsque j'ai essayé d'exécuter mes tests m'ont également dirigé à installer explicitement ceux-ci moi-même :

```
npm install --save-dev react-dom enzyme
```

Voici ce que j'ai dû ajouter manuellement à package.json :

```
// package.json avant avec react-native init

{
...
   "jest": {
       "presets": ["react-native"],
     }
...
}

// package.json après mes modifications manuelles :
{
...

"jest": {
       "presets": ["react-native"], // non clair dans la documentation !
       "setupTestFrameworkScriptFile": "jest-enzyme",
       "testEnvironment": "enzyme",
       "testEnvironmentOptions": {
           "enzymeAdapter": "react16"
       }  
   }
...
}
```

Vous pouvez voir le dépôt [ici](https://github.com/SamOllason/jest-enzyme-config-for-react-native/blob/master/README.md).

L'utilisation de la bibliothèque jest-enzyme de cette manière a bien fonctionné pour moi et cela a également signifié que j'avais une configuration légèrement plus propre. Cela est dû au fait que l'autre approche (que je n'ai pas réussi à faire fonctionner, en suivant la documentation d'Enzyme) aurait signifié que je devais également configurer et maintenir un script de 'configuration jest' séparé.

### Résumé

Écrire la logique métier à l'intérieur des tests Jest+Enzyme pour React Native semble être exactement la même chose que d'écrire des tests pour React en utilisant Jest+Enzyme. Cela signifie que les exemples et la documentation en ligne pour les tests unitaires React sont facilement transférables, ce qui est vraiment utile. C'est une grande étape vers la vision des développeurs web pouvant facilement transférer leurs compétences pour créer des applications mobiles multiplateformes.

Cependant, pour la facilité d'utilisation dans la phase d'écriture des tests, j'ai payé le prix lors de la configuration de l'infrastructure et de l'environnement afin que les divers outils soient compatibles avec mon écosystème React Native.

De plus, en tombant sur des problèmes Github dans ce domaine, il semble qu'il y ait beaucoup de petites instabilités entre les versions de React Native qui rendent vraiment difficile la découverte de la cause sous-jacente d'un problème d'infrastructure comme ceux que j'ai décrits ci-dessus. Mais je suppose que nous ne pouvons pas avoir de flexibilité dans un espace en évolution aussi rapide que celui-ci sans quelques défis.

[Ici](https://github.com/SamOllason/jest-enzyme-config-for-react-native/blob/master/README.md) se trouve le dépôt avec ma configuration jest-enzyme avec quelques exemples de tests.

J'espère que vous avez trouvé cela intéressant et utile ! N'hésitez pas à ajouter des questions ou des commentaires ci-dessous.
---
title: La meilleure structure de fichiers pour vos composants React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-23T17:59:13.000Z'
originalURL: https://freecodecamp.org/news/best-file-structure-for-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/reactcomponents-1.png
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: La meilleure structure de fichiers pour vos composants React
seo_desc: "By Iva Kop\nCreating an adequate and scalable file structure for front\
  \ end projects can be challenging. The freedom we have when using un-opinionated\
  \ tools like React comes with a great deal of responsibility. \nUsually, when we\
  \ talk about file structu..."
---

Par Iva Kop

Créer une structure de fichiers adéquate et évolutive pour les projets front-end peut être un défi. La liberté dont nous disposons lorsque nous utilisons des outils non prescriptifs comme React s'accompagne d'une grande responsabilité. 

Habituellement, lorsque nous parlons de structure de fichiers, la discussion se concentre sur le projet dans son ensemble. Mais ce qui est tout aussi important (et souvent négligé) est la question de la meilleure façon de structurer les composants.

Permettez-moi de vous montrer ce que je veux dire.

## Ce qu'il faut inclure dans le répertoire des composants

Les composants sont les éléments de base de chaque application React. À ce titre, ils peuvent être traités comme des mini-projets à part entière. Un composant doit être aussi autonome que possible (mais pas plus).

Un répertoire de composants typique pourrait ressembler à ceci :

```
├── components
│   ├── Component
│   │   ├── SubComponent
│   │   │   ├── SubComponent.test.tsx
│   │   │   ├── index.tsx
│   │   ├── Component.stories.tsx
│   │   ├── Component.test.tsx
│   │   ├── icon.svg
│   │   ├── index.tsx
│   │   ├── utils.ts
│   │   ├── utils.test.ts


```

Décortiquons cela.

### Fichier index principal

L'export par défaut de ce fichier est le composant lui-même.

En outre, l'index peut également inclure des exports nommés. Par exemple, si je construis un composant `Menu`, je voudrais pouvoir l'utiliser comme ceci :

```
import Menu, { MenuItem } from 'components/Menu'

const ComponentWithMenu = () => {
    return (
        <Menu>
            <MenuItem />
            <MenuItem />
        </Menu>
    )
}


```

Ainsi, dans mon fichier index, je dois exporter `Menu` comme export par défaut mais également ré-exporter le sous-composant `MenuItem` comme export nommé. De cette manière, je peux ensuite importer les deux depuis le même endroit. 

La ré-exportation explicite aide également à documenter ce qui est public (et destiné à être utilisé par le reste de l'application) et ce qui est privé au composant.

> Remarque : Il est possible de soutenir que seul l'export par défaut devrait être public et que tout le reste devrait rester privé. Pour découvrir pourquoi je recommande une approche différente, consultez mon article sur la [construction de composants React non triviaux](https://blog.whereisthemouse.com/a-guide-to-building-non-trivial-react-components).

### Tests

Pourquoi placer les tests ici plutôt que dans un répertoire `tests` séparé ? Un seul mot - colocation ! 

Les fichiers qui appartiennent ensemble doivent vivre ensemble. Les avantages de cette approche deviennent très clairs si vous imaginez le processus de modification ou même de suppression de composants. La maintenance est beaucoup plus simple lorsque tout est au même endroit.

De plus, les tests servent souvent de documentation. Les avoir à côté de notre composant a donc tout son sens.

### Story

[Storybook](https://storybook.js.org/) est un outil génial pour développer des composants en isolation. Il nous permet de traiter nos composants comme des mini-projets séparés. La colocation de chaque story avec son composant correspondant est importante pour toutes les mêmes raisons énoncées ci-dessus.

### Styles

Lorsque nous utilisons CSS-in-JS, les composants stylisés peuvent être créés directement dans le fichier du composant. Si nous avons opté pour les modules CSS, les fichiers de style doivent être colocés avec le composant dans son répertoire.

### Assets

Les images, icônes ou autres assets spécifiques au composant doivent être placés directement dans le répertoire du composant. Encore une fois - colocation !

### Utils

Les utils peuvent inclure tout, des fonctions d'assistance aux hooks personnalisés. Nous pourrions les séparer en différentes catégories (hooks, services, etc.), si nous le préférons, mais les mêmes principes de base s'appliquent. 

Nous devons nous assurer que tous les utils sont spécifiques au composant et non quelque chose qui est réutilisé par d'autres parties de l'application. Les tests pour les utils sont placés dans le répertoire du composant.

### Sous-composants

Les sous-composants sont structurés de manière très similaire au composant principal. Ils sont généralement utilisés par le composant principal. 

Si votre intention est de les utiliser dans toute l'application (comme avec notre exemple `MenuItem`), ils doivent être ré-exportés dans le fichier index principal. Il ne devrait pas être possible d'utiliser les sous-composants sans le composant principal. 

Si c'est le cas, alors le sous-composant lui-même devrait devenir un composant principal.

Les sous-composants doivent avoir leurs propres tests unitaires colocés (quand nécessaire), styles et assets. La plupart du temps, les stories sont réservées au composant principal uniquement.

## Ce qu'il faut garder à l'extérieur du répertoire des composants

Voici une bonne règle : si vous êtes jamais tenté d'utiliser autre chose que ce qui a été explicitement exporté depuis l'index du composant, c'est un signal clair que ce morceau de code particulier devrait être placé ailleurs.

Permettez-moi de vous donner un exemple.

Revenons à notre composant `Menu`. Normalement, nous nous attendrions à ce que si un utilisateur clique à l'extérieur d'un menu, il se ferme. Pour ce faire, nous avons créé un hook personnalisé `useClickOutside` et l'avons placé dans utils. 

Après un certain temps, il devient clair que nous avons besoin du même comportement, cette fois pour notre composant `Dialog`. 

Nous voulons réutiliser notre hook mais, en même temps, il n'est plus spécifique au composant. Nous devons le sortir du composant Menu et le placer plus haut, peut-être dans notre dossier utils général.

**Une note de prudence** : Le fait de déplacer du code pour le réutiliser doit être fait avec soin et uniquement lorsque cela est vraiment nécessaire. En tant que développeurs, nous sommes souvent tentés de [créer des abstractions trop tôt](https://www.deconstructconf.com/2019/dan-abramov-the-wet-codebase) et sans contexte complet. Cela peut avoir de graves conséquences pour la maintenabilité du projet à l'avenir. 

La plupart du temps, si un morceau de code fait quelque chose de similaire (mais pas exactement la même chose), il est préférable de répliquer une partie de la fonctionnalité au début, et de ne créer l'abstraction que lorsque les cas d'utilisation sont suffisamment clairs.

## Conclusion

La structure des composants est cruciale pour l'architecture React. Se tromper peut avoir des conséquences durables sur l'évolutivité et la maintenabilité des projets. C'est pourquoi il est important de souligner que ce que je propose ci-dessus n'est qu'un modèle.

Bien que j'aie trouvé cette structure applicable à un large éventail de scénarios, chaque application React est unique ou, à tout le moins, a ses propres idiosyncrasies. Un guide généralisé ne peut pas remplacer une réflexion critique sur les spécificités d'un projet et la prise de décisions en conséquence.

*Si vous avez trouvé cet article utile, [connectons-nous](https://twitter.com/iva_kop). Pour plus d'articles approfondis sur React, consultez [mon blog](https://blog.whereisthemouse.com/).*
---
title: Une Nouvelle Approche de la Conception des Composants React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-10T22:39:24.000Z'
originalURL: https://freecodecamp.org/news/a-new-approach-to-react-component-design-2bf76a87add1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nFP5vJPVTEaimO8n4jPKgA.gif
tags:
- name: Design
  slug: design
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Une Nouvelle Approche de la Conception des Composants React
seo_desc: 'By Austin Malerba

  In 2015, Dan Abramov wrote an article, Presentational and Container Components,
  that some React new-comers misconstrued as commandments. In fact, I myself stumbled
  upon the article and many others echoing its teachings and I thought...'
---

Par Austin Malerba

En 2015, Dan Abramov a écrit un article, [Presentational and Container Components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0), que certains nouveaux venus dans React ont mal interprété comme des commandements. En fait, je suis moi-même tombé sur l'article et beaucoup d'autres échoant à ses enseignements et j'ai pensé, _ce doit être la meilleure façon de séparer les préoccupations parmi les composants_.

Mais Dan Abramov lui-même a plus tard adressé la communauté pour s'accrocher aux modèles de conception qu'il avait décrits.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5TKk6it2JOAomEj-IwKgCg.png)

En travaillant avec React depuis plus d'un an maintenant, je suis tombé sur mes propres modèles de conception et ici je vais essayer de les formaliser. Prenez ces idées avec des pincettes, ce ne sont que mes propres observations que j'ai trouvées constructives.

### Échapper à la Dichotomie

Pendant longtemps, les composants ont été largement classés comme soit intelligents ou stupides, conteneurs ou présentationnels, stateful ou stateless, purs ou impurs. Il y a beaucoup de terminologie, mais ils signifient tous à peu près la même chose. Les composants intelligents savent comment lier ensemble votre application et les composants stupides se contentent de prendre des données à présenter à l'utilisateur final. C'est une distinction utile, mais ce n'est vraiment pas ainsi que je me surprends à penser en concevant des composants.

Le problème avec l'état d'esprit Conteneur vs Présentationnel est qu'il essaie trop fort de définir les responsabilités des composants en termes d'état, de logique et d'autres aspects du fonctionnement interne d'un composant.

La conception des composants est mieux abordée en différant les détails d'implémentation et en pensant en termes d'**interfaces de composants**. Il est particulièrement important de réfléchir au type de **personnalisations** qu'un composant doit permettre et au type de **dépendances implicites et explicites** qu'un composant doit inclure.

### Introduction de la Trichotomie

Trichotomie ? Est-ce même un mot ? Je ne sais pas, mais vous voyez l'idée. J'en suis venu à penser que les composants React tombent dans l'une des trois catégories.

#### Composants Universels

Ce sont des composants qui peuvent être utilisés **plusieurs fois dans n'importe quelle application**.

Ces composants :

* Doivent être **réutilisables**
* Doivent être **hautement personnalisables**
* Ne doivent **pas être conscients du code spécifique à l'application** incluant les modèles, les stores, les services, etc.
* Doivent **minimiser les dépendances** aux bibliothèques tierces
* Doivent rarement être utilisés directement dans votre application
* Doivent être utilisés comme **blocs de construction pour les composants Globaux**
* Peuvent se terminer par le suffixe « Base » (par exemple, ButtonBase, ImageBase)

Ce sont des composants fondamentaux qui sont agnostiques à l'application et ne sont pas nécessairement utilisés directement dans vos composants de Vue car ils sont souvent trop personnalisables. Les utiliser directement dans vos composants de Vue signifierait beaucoup de copie et de collage du même code boilerplate. Vous risqueriez également que les développeurs abusent de la nature hautement personnalisable des composants de manière à créer une expérience incohérente dans votre application.

#### Composants Globaux

Ce sont des composants qui peuvent être utilisés **plusieurs fois dans une application**.

Ces composants :

* Doivent être **réutilisables**
* Doivent être **minimalement personnalisables**
* Peuvent utiliser du **code spécifique à l'application**
* Doivent **implémenter des composants Universels**, restreignant leur personnalisation
* Doivent être utilisés comme **blocs de construction pour les composants de Vue**
* Souvent liés un-à-un avec des instances de modèle (par exemple, DogListItem, CatCard)

Ces composants sont réutilisables dans votre application mais ne sont pas facilement transférables à d'autres applications car ils dépendent de la logique de l'application. Ce sont les blocs de construction pour les composants de Vue et d'autres composants Globaux.

Ils doivent être minimalement personnalisables pour garantir la cohérence dans votre application. Les applications ne devraient pas avoir trente variations différentes de boutons, mais plutôt une poignée de variations différentes de boutons. Cela devrait être imposé en prenant un composant Universal ButtonBase hautement personnalisable et en y intégrant des styles et des fonctionnalités sous la forme d'un composant Global Button. Les composants Globaux prennent souvent une autre forme en tant que représentations de données de modèle de domaine.

#### Composants de Vue

Ce sont des composants qui sont utilisés **une seule fois dans votre application**.

Ces composants :

* Ne doivent **pas** se soucier de la réutilisabilité
* Sont susceptibles de **gérer l'état**
* Reçoivent des **props minimales**
* Doivent lier ensemble des composants Globaux (et éventuellement des composants Universels)
* Résolvent souvent les **routes de l'application**
* Mainiennent souvent un espace dédié de l'immobilier de la fenêtre d'affichage
* Ont souvent un grand nombre de dépendances
* Doivent être des **blocs de construction pour votre application**

Ce sont les composants de plus haut niveau de votre application qui collent ensemble des composants réutilisables et même d'autres Vues. Ce seront souvent les composants qui résolvent les routes et peuvent apparaître sous la forme de composants de niveau page. Ils sont lourds en état et légers en props. Ce sont ce que Dan Abramov considérerait comme des composants conteneurs.

#### Le PromiseButton

Examinons les implémentations Universelles et Globales d'un bouton de promesse et voyons comment elles se comparent. Un bouton de promesse agit comme un bouton ordinaire sauf si le gestionnaire onClick retourne une promesse. Dans le cas d'une promesse retournée, le bouton peut rendre conditionnellement du contenu basé sur l'état de la promesse.

<script src="https://gist.github.com/malerba118/86465f12da532d57f32d607e90f9d72b.js"></script>

<script src="https://gist.github.com/malerba118/ce2eccea26a307ac852bf0f47dd696be.js"></script>

Remarquez comment le PromiseButtonBase nous permet de contrôler ce qu'il faut rendre à tout moment dans le cycle de vie de la promesse, mais le PromiseButton intègre le teal PulseLoader pendant l'état en attente. Maintenant, chaque fois que nous utilisons le PromiseButton, nous sommes assurés d'une animation de chargement teal et nous n'avons pas à nous soucier de dupliquer ce code ou de fournir une expérience de chargement incohérente en incluant plusieurs animations de chargement de plusieurs couleurs dans notre application. Le PromiseButtonBase est personnalisable, mais le PromiseButton est restrictif.

#### Structure du Répertoire

Ce qui suit illustre comment nous pourrions organiser les composants en suivant ce modèle.

```
App/
  App.js
  Views/
    DogListView/
  Global/
    Models/
      Dog/
        DogListItem/
    Image/
    PromiseButton/
Universal/
  ImageBase/
  PromiseButtonBase/
```

#### Dépendances des Composants

Ci-dessous illustre comment les composants ci-dessus dépendent les uns des autres.

```javascript
/* App.js */
import { DogListView } from './Views'

/* DogListView.js */
import { DogListItem } from 'App/Global/Models/Dog'

/* DogListItem.js */
import Image from '../../Image',
import PromiseButton from '../../PromiseButton'

/* Image.js */
import { ImageBase } from 'Universal'

/* PromiseButton.js */
import { PromiseButtonBase } from 'Universal'
```

Notre composant de Vue dépend d'un composant Global et nos composants Globaux dépendent d'autres composants Globaux ainsi que de composants Universels. Ce flux de dépendances sera assez courant. Remarquez également l'utilisation des imports absolus et relatifs. Il est agréable d'utiliser des imports relatifs lorsque vous tirez des dépendances qui résident dans le même module. De plus, il est agréable d'utiliser des imports absolus lorsque vous tirez des dépendances à travers des modules ou lorsque votre structure de répertoire est profondément imbriquée ou fréquemment modifiée.

Le problème avec le modèle Conteneur vs Présentationnel est qu'il essaie trop fort de définir les responsabilités des composants en termes de fonctionnement interne des composants. Le point clé à retenir est de voir la conception des composants en termes d'**interfaces de composants**. Ce qui compte moins, c'est l'implémentation qui permet au composant de satisfaire son contrat. Il est important de réfléchir au type de **personnalisations** qu'un composant doit permettre et au type de **dépendances implicites et explicites** qu'un composant doit inclure.

Si vous avez trouvé ces réflexions utiles et que vous aimeriez voir plus de mes idées, n'hésitez pas à consulter ce [dépôt](https://github.com/malerba118/react-redux-template) que j'utilise pour maintenir mes réflexions et meilleures pratiques pour écrire des applications React/Redux.
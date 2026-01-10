---
title: Comment créer des graphiques React Native avec des infobulles dynamiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T19:00:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-react-native-charts-with-dynamic-tooltips-64aefc550c95
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zjVWOfAZdFWrzyTHJsiobw.gif
tags:
- name: coding
  slug: coding
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: Comment créer des graphiques React Native avec des infobulles dynamiques
seo_desc: 'By Vikrant Negi

  Creating charts, be it on the web or on mobile apps, has always been an interesting
  and challenging task especially in React Native. It’s difficult to find a suitable
  library that can meet your functional and design needs at the same ...'
---

Par Vikrant Negi

Créer des graphiques, que ce soit sur le web ou sur des applications mobiles, a toujours été une tâche intéressante et stimulante, surtout dans React Native. Il est difficile de trouver une bibliothèque appropriée qui puisse répondre à vos besoins fonctionnels et de conception en même temps. Vous pouvez essayer de créer vos propres graphiques, mais cela implique souvent l'apprentissage et la mise en œuvre de choses à partir de zéro.

Si vous êtes un débutant comme moi, vous voulez probablement utiliser une bibliothèque de graphiques existante. Et étant donné la jeunesse de la communauté React Native, vous avez très peu d'options disponibles pour implémenter et personnaliser des graphiques.

#### Énoncé du problème

Avant de commencer notre voyage en profondeur, je voudrais vous présenter notre énoncé du problème.

Dans ce tutoriel, nous allons dessiner un graphique en aire et ajouter un marqueur circulaire à chacun des points de données qui peut être appuyé pour afficher une infobulle contenant les valeurs des coordonnées x et y.

Pour résoudre ce problème, j'ai fait quelques recherches sur certaines bibliothèques React Native existantes et je les ai réduites à deux d'entre elles, [react-native-charts-wrapper](https://github.com/wuxudong/react-native-charts-wrapper), et [react-native-svg-charts](https://github.com/JesperLekland/react-native-svg-charts).

#### React Native Charts Wrapper

Notre premier concurrent, `[react-native-charts-wrapper](https://github.com/wuxudong/react-native-charts-wrapper)` est un wrapper React Native de la bibliothèque de graphiques Native populaire [MPAndroidChart](https://github.com/PhilJay/MPAndroidChart) et [Charts](https://github.com/danielgindi/Charts).

Cette bibliothèque est hautement configurable, et puisque elle utilise les bibliothèques de graphiques natives, elle fournit des transitions fluides et un support tactile. Elle dispose également de nombreux exemples de cas d'utilisation sur son dépôt Github.

Au début, c'était mon choix préféré étant donné ses performances et sa personnalisation. Elle dispose d'un guide d'[installation](https://github.com/wuxudong/react-native-charts-wrapper/blob/master/installation_guide/README.md) très long et spécifique, en suivant lequel j'ai pu l'installer et l'exécuter sur les appareils iOS et Android.

Tout semble fonctionner correctement sur Android. Cependant, lorsque j'ai essayé de créer une build iOS, cela m'a donné une erreur. Après d'innombrables heures de recherche à travers les problèmes GitHub et Google, j'ai décidé de l'abandonner.

#### React Native SVG Charts

Après avoir abandonné `react-native-charts-wrapper`, c'était la prochaine meilleure solution disponible que j'ai pu trouver.

`[react-native-svg-charts](https://github.com/JesperLekland/react-native-svg-charts)` utilise `[react-native-svg](https://github.com/react-native-community/react-native-svg)` sous le capot pour rendre les graphiques. Il dispose également de nombreux [exemples](https://github.com/JesperLekland/react-native-svg-charts-examples) présentant de nombreux cas d'utilisation.

Puisqu'il n'utilise aucun lien natif, l'installation et la mise en œuvre étaient assez simples et directes.

> Si vous voulez simplement voir le code source du projet d'exemple, trouvez le dépôt du projet [ici](https://github.com/vikrantnegi/react-native-tooltip-chart).

Maintenant que c'est fait, commençons.

#### Getting Started

Créez un projet React Native et installez toutes les dépendances requises.

```
~ react-native init ReactNativeTooltip
```

Nous devons également installer et lier la bibliothèque `react-native-svg`.

```
~ npm i react-native-svg
```

```
~ react-native link react-native-svg
```

Si vous rencontrez un problème lors de la liaison automatique de la bibliothèque à l'aide de la commande link, suivez les étapes [manuelles](https://github.com/react-native-community/react-native-svg) mentionnées dans la documentation officielle.

Maintenant, installez enfin `react-native-svg-charts`.

```
~ npm install react-native-svg-charts
```

#### Obtenir les données factices

Avant d'aller plus loin, nous devons avoir des données que nous pouvons utiliser pour rendre notre `AreaChart`. Nous allons utiliser un service tiers appelé [Mockaroo](https://www.mockaroo.com/) pour générer des données factices pour notre graphique en aire.

Idéalement, nous obtiendrons ces données à partir d'une API que nous stockerons dans l'état du composant, puis nous les alimenterons dans notre composant d'aire.

Voici à quoi ressemblent mes données JSON factices. Voir [ici](https://github.com/vikrantnegi/react-native-tooltip-chart/blob/master/src/Data.js) pour le fichier JSON complet.

```
export const DATA = [  {    id: 1,    date: '2019-01-26T22:37:01Z',    score: 3,  },  {    id: 2,    date: '2019-01-06T06:03:09Z',    score: 9,  },  {    id: 3,    date: '2019-01-28T14:10:00Z',    score: 10,  },  {    id: 4,    date: '2019-01-03T02:07:38Z',    score: 7,  },  ...]
```

#### Utilisation de React Native SVG charts

`react-native-svg-charts` dispose de nombreux composants que nous pouvons utiliser pour créer des graphiques. Dans ce tutoriel, nous utiliserons le composant `AreaChart`, mais vous pouvez utiliser l'un des composants de [graphiques disponibles](https://github.com/JesperLekland/react-native-svg-charts#components). Voici à quoi ressemble un composant de graphique `AreaChart`:

```
<AreaChart  style={{ height: '70%' }}  data={data}  yAccessor={({ item }) => item.score}  xAccessor={({ item }) => moment(item.date)}  contentInset={contentInset}  svg={{ fill: '#003F5A' }}  numberOfTicks={10}  yMin={0}  yMax={10}>
```

Passons en revue les props importants que nous utilisons dans le `AreaChart`.

* `data` : Il s'agit d'un champ obligatoire et doit être un tableau.
* `yAccessor`: Une fonction qui prend chaque entrée de `data` (nommée "item") ainsi que l'index et retourne la valeur y de cette entrée.
* `xAccessor`: Même chose que `yAccessor` mais retourne la valeur x de cette entrée.

Vous pouvez lire plus sur les autres props disponibles dans la documentation officielle [documentation](https://github.com/JesperLekland/react-native-svg-charts#common-props).

#### Ajout de décorateurs

React Native SVG charts a été conçu pour être aussi extensible que possible. Tous les graphiques peuvent être étendus avec des "décorateurs", un composant qui style ou améliore d'une certaine manière votre graphique. Il suffit de passer un composant conforme à `react-native-svg` en tant qu'enfant du graphique et il sera appelé avec toutes les informations nécessaires pour disposer votre décorateur.

Pour ce tutoriel, nous aurons besoin de deux décorateurs, l'un pour le marqueur de point de données et un autre pour l'infobulle.

> Assurez-vous de placer les décorateurs à l'intérieur du composant `_AreaChart_`. Sinon, ils ne seront pas rendus.

#### Ajout de marqueurs de points de données

Créons un décorateur à utiliser comme marqueur à chaque point de données dans le graphique.

```
const ChartPoints = ({ x, y, color }) =>  data.map((item, index) => (   <Circle     key={index}     cx={x(moment(item.date))}     cy={y(item.score)}     r={6}     stroke={color}     fill="white"     onPress={() =>       this.setState({         tooltipX: moment(item.date),         tooltipY: item.score,         tooltipIndex: index,       })     }  />));
```

Nous avons besoin d'un marqueur circulaire pour chaque élément du tableau de données. Pour cela, nous allons parcourir chaque élément du tableau de données et retourner le composant SVG `Circle` pour chacun d'eux.

Maintenant, pour les positionner sur le graphique, nous allons utiliser les props `cx` et `cy` pour les positionner horizontalement et verticalement, respectivement. Pour `cx`, nous utiliserons la clé `date` et pour `cy`, nous utiliserons la clé `score`.

En plus de cela, nous allons également passer la prop `onPress` qui définira trois états, `tooltipX`, `tooltipY` et `tooltipIndex` lorsque l'un des points de données est pressé. Nous utiliserons ensuite ces états pour positionner le décorateur `Tooltip`.

![Image](https://cdn-media-1.freecodecamp.org/images/7DDoNAP66bEyXcKvCeyxj8FbCaTMw4-nwtdq)
_Graphiques en aire avec les marqueurs_

#### Ajout d'infobulles

Maintenant que nous avons les informations nécessaires comme l'axe x (tooltipX), l'axe y (tooltipY) et l'index (tooltipIndex) du marqueur pressé, nous pouvons les utiliser pour placer l'`Tooltip` sur le `AreaChart`.

Nous allons créer un nouveau [fichier](https://github.com/vikrantnegi/react-native-tooltip-chart/blob/master/src/Tooltip.js) pour le décorateur `Tooltip`.

```
const Tooltip = ({ x, y, tooltipX, tooltipY, color, index, dataLength,}) => {
```

```
let xAxis = 4;  if (dataLength > 4) {    if (index < 2) {      xAxis = 35;    } else if (index > dataLength - 2) {      xAxis = -20;    } else {     xAxis = 4;    }  }
```

```
return (    <G x={x(tooltipX) - 40} y={y(tooltipY)}>      <G y={tooltipY > 9 ? 20 : -29} x={xAxis}>        <Rect x={-2} y={0} height={22} width={70} stroke={color} fill="white" ry={10} rx={10} />        <Rect x={-2} y={0} height={22} width={18} fill={color} ry={10} rx={10} />        <Rect x={10} y={0} height={22} width={tooltipY > 9 ? 12 : 10} fill={color} />        <Text x={6} y={14} stroke="#fff">          {tooltipY}        </Text>        <Text x={tooltipY > 9 ? 24 : 22} y={14}>          {moment(tooltipX).format('MMM DD')}        </Text>      </G>    </G>  );};
```

Ne vous laissez pas confondre ou intimider par toutes les balises `React`, `G` et `Text` ici, la plupart d'entre elles sont juste pour le style de l'infobulle.

Concentrez-vous simplement sur `tooltipX` et `tooltipY` que nous utilisons pour positionner l'`Tooltip` horizontalement et verticalement sur le graphique. Ces valeurs sont les mêmes que `cx` et `cy` que nous avons utilisées pour le marqueur, sauf que nous ajoutons et soustrayons certaines valeurs pour les ajuster sur le graphique.

En plus de cela, nous utilisons `tooltipIndex` pour décaler la première et la dernière infobulle afin qu'elles ne soient pas coupées sur les côtés.

> [Voici](https://github.com/vikrantnegi/react-native-tooltip-chart) le code source complet d'un exemple fonctionnel.

![Image](https://cdn-media-1.freecodecamp.org/images/Dfhg49lhgH6Q6oFeHteuXmc9jkRlMJaHioLo)
_Graphique en aire avec des infobulles cliquables_

#### Réflexions finales

C'est tout ce que nous devons faire pour créer des graphiques, des marqueurs et des infobulles. Il s'agit d'une implémentation de base de ce qui peut être réalisé en utilisant la bibliothèque `react-native-svg-charts`.

Si vous souhaitez explorer davantage, consultez leur dépôt [exemples](https://github.com/JesperLekland/react-native-svg-charts-examples) où ils présentent de nombreux autres cas d'utilisation.

> Pour des raisons de brièveté, j'ai omis certains codes de base que vous pouvez trouver sur le dépôt Github.

Faites-moi savoir si vous trouvez quelque chose de confus. Si vous avez travaillé sur des graphiques React Native, partagez les bibliothèques et les cas d'utilisation que vous avez rencontrés.
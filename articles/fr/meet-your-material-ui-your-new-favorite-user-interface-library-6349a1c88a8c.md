---
title: Découvrez Material-UI — votre nouvelle bibliothèque d'interface utilisateur
  préférée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-28T17:05:59.000Z'
originalURL: https://freecodecamp.org/news/meet-your-material-ui-your-new-favorite-user-interface-library-6349a1c88a8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FDNeKIUeUnf0XdqHmi7nsw.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Découvrez Material-UI — votre nouvelle bibliothèque d'interface utilisateur
  préférée
seo_desc: 'By Code Realm


  Update (17/05/2018): Material-UI v1.0.0 is out! Check out this post by Olivier.


  Huh? Yet another library? What’s wrong with Bootstrap? And why not v0.20?

  Great questions! Let’s start with a brief introduction. In a nutshell, Material-...'
---

Par Code Realm

> **Mise à jour** (17/05/2018) : Material-UI v1.0.0 est sorti ! Consultez [cet article](https://medium.com/material-ui/material-ui-v1-is-out-e73ce13463eb) d'Olivier.

Quoi ? Encore une autre bibliothèque ? Qu'est-ce qui ne va pas avec Bootstrap ? Et pourquoi pas v0.20 ?

Excellentes questions ! Commençons par une brève introduction. En résumé, Material-UI est un projet open-source qui propose des composants [React](https://reactjs.org/) implémentant le [Material Design de Google](https://material.io/guidelines/material-design/introduction.html).

Il a été lancé en 2014, peu après la sortie publique de React, et sa popularité n'a fait que croître depuis. Avec [plus de 35 000 étoiles sur GitHub](https://github.com/mui-org/material-ui), Material-UI est l'une des principales bibliothèques d'interface utilisateur pour React.

Son succès n'est pas venu sans défis. Conçu avec LESS, Material-UI v0.x était sujet aux pièges courants de CSS, tels que la portée globale, ce qui a conduit le projet sur la trajectoire du [CSS-in-JS](https://speakerdeck.com/vjeux/react-css-in-js). C'est ainsi que `next` est né en 2016.

Le [voyage vers un meilleur style](https://github.com/oliviertassinari/a-journey-toward-better-style), comme le dit Olivier Tassinari, a commencé avec des styles en ligne, mais leurs performances sous-optimales et leur support limité des fonctionnalités (pensez aux sélecteurs pseudo ou aux requêtes média) ont finalement conduit l'équipe à adopter [JSS](http://cssinjs.org). Et ils ont fait un choix judicieux.

#### Pourquoi tant d'engouement pour la version v1 ?

Elle est géniale. Non seulement elle résout les problèmes inhérents à LESS, mais elle déverrouille également une tonne de fonctionnalités fantastiques, notamment :

* des styles dynamiques générés à l'exécution
* des thèmes imbriqués avec des remplacements intuitifs
* un temps de chargement réduit avec le fractionnement de code

Et [beaucoup plus](https://material-ui-next.com/getting-started/comparison/#styling-solution). La bibliothèque est également suffisamment mature pour être utilisée en production. Tellement que l'équipe suggère v1 pour [tous les nouveaux projets](https://github.com/mui-org/material-ui#should-i-start-with-v1-beta) à venir.

#### D'accord, allons-nous construire une application, ou quoi ?

Je suis content que vous ayez demandé ! Pour cette démonstration, nous allons construire une simple application de fitness. Tout le monde en a assez des applications de liste de tâches de toute façon, n'est-ce pas ?

Lire est bien et tout, mais regarder est souvent plus amusant ! Consultez cette playlist que j'ai créée sur YouTube si vous voulez construire une application plus avancée.

#### *D'accord, vous m'avez convaincu. Comment commencer ?*

Nous allons d'abord initialiser notre application avec create-react-app

```
create-react-app mui-fitness
cd mui-fitness
code .
```

#### Et pour Material-UI ?

Si vous avez yarn, l'installation est aussi simple que

```
yarn add @material-ui/core
```

Sinon, avec `npm`

```
npm i @material-ui/core
```

Il n'y a pas si longtemps, nous devions spécifier le tag `@next` pour obtenir la dernière pré-version (par exemple, cela aurait pu ressembler à `v1.0.0-beta.47`). Maintenant que v1 et v0.x sont sous la portée `material-ui`, nous devons référencer le cœur de la bibliothèque avec `/core` pour cibler la dernière version. Ne manquez pas cette dernière partie, sinon vous vous retrouverez avec la dépendance stable `0.20` !

#### Attendez, est-ce vraiment tout ?

Presque ! Une dernière chose : les polices. Nous allons utiliser la police [Roboto Font](https://fonts.google.com/specimen/Roboto) recommandée depuis le CDN de Google :

```
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">
```

Alternativement, vous pouvez l'importer depuis NPM avec

```
yarn add typeface-roboto
# ou npm i typeface-roboto
```

auquel cas, vous devrez avoir une importation à la racine de votre projet

```
// Assurez-vous de ne charger que les poids de police 300, 400 et 500 !
import 'typeface-roboto'
```

#### Terminé ! Que faire ensuite ?

Eh bien, refactorisons notre composant `App.js` avant d'aller plus loin

```
import React, { Component } from 'react'
```

```
export default class App extends Component {  state = {    exercises: [],    title: ''  }
```

```
  render() {    return <h1>Exercices</h1>  }}
```

Et pourquoi ne pas nettoyer `index.js` pendant que nous y sommes ?

```
import React from 'react'
import { render } from 'react-dom'
import App from './App'
```

```
render(<App />, document.getElementById('root'))
```

N'hésitez pas à supprimer les fichiers restants sous `src`, car nous n'en aurons pas besoin.

#### Où intervient Material-UI ?

C'est juste, il est temps de le voir en action. Changeons le `h1` laid en un beau titre `Typography` :

```
import Typography from '@material-ui/core/Typography'
```

```
...
```

```
  render() {    return (      <Typography variant='display1' align='center' gutterBottom>        Exercices      </Typography>    )  }}
```

> Notez que depuis v1.0.0-rc.0, MUI est passé à `@material-ui/core` et le [chemin d'importation a été aplati](https://github.com/mui-org/material-ui/pull/11330). C'était la [dernière modification majeure](https://github.com/mui-org/material-ui/releases/tag/v1.0.0-rc.0) dans la pré-version.

Ensuite, lancez `yarn start` pour voir la magie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3LXrxIWyUdUQUqTyqfd_9w.png)
_Titre de taille « Display 1 » avec une marge inférieure centré horizontalement_

Nous sommes sur une bonne voie ! Le composant `Typography` vient avec un ensemble prédéfini de [tailles de texte](https://material-ui-next.com/style/typography/#component). D'autres `variant`s incluent `body1`, `title`, `display2`, et ainsi de suite. Parmi les autres props intégrées, on trouve `align` que nous utilisons ici pour centrer le texte horizontalement, et `gutterBottom` qui ajoute une marge inférieure.

Pourquoi ne pas étendre cela à un formulaire, afin que nous puissions créer nos propres exercices ? Nous allons commencer par un `TextField` et le lier au `title` de l'état

```
import Typography from '@material-ui/core/Typography'
import TextField from '@material-ui/core/TextField'
```

```
...
```

```
  handleChange = ({ target: { name, value } }) =>    this.setState({      [name]: value    })
```

```
  render() {    const { title } = this.state    return (      ...      <form>        <TextField          name='title'          label='Exercice'          value={title}          onChange={this.handleChange}          margin='normal'        />      </form>    )  }}
```

Bien sûr, nous devons rendre React heureux en enveloppant `Typography` et `form` avec un élément parent. Quelle meilleure opportunité pour un fond de type carte en papier ? Faisons appel à `Paper` alors

```
import Paper from '@material-ui/core/Paper'
```

```
...
```

```
  render() {      const { title } = this.state      return <Paper>        ...      </Paper>    }  }}
```

Il est également temps de commencer à utiliser des imports nommés (en supposant que notre configuration Webpack permet le tree shaking) :

```
import { Paper, Typography, TextField } from '@material-ui/core'
```

Super ! Et à quoi sert un formulaire sans bouton de soumission ? Les `Button`s sont un composant de base dans Material-UI ; vous les verrez partout. Par exemple,

```
import {  Paper,  Typography,  TextField,  Button } from '@material-ui/core'
...
        <Button          type='submit'          color='primary'          variant='raised'        >          Créer        </Button>      </form>    </Paper>  }}
```

Cela devrait être clair. `type` est une prop React régulière, `color` et `variant` sont spécifiques à Material-UI, et forment un bouton de forme rectangulaire. Une autre variante serait `fab` pour un bouton flottant, par exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GWviICnReMU62qHX2V1iKA.png)
_Ce n'est pas le formulaire le plus joli du monde, mais nous allons l'améliorer dans un instant !_

Il ne fait pas grand-chose cependant. Nous devons intercepter l'événement de soumission du formulaire

```
    return <Paper>      ...      <form onSubmit={this.handleCreate}>        ...      </form>    </Paper>  }}
```

et ensuite le gérer avec

```
  handleCreate = e => {    e.preventDefault()
```

```
    if (this.state.title) {      this.setState(({ exercises, title }) => ({        exercises: [          ...exercises,          {            title,            id: Date.now()          }        ],        title: ''      }))    }  }
```

Whoa ! Qu'est-ce que ce code cryptique ? Très rapidement, nous

1. Empêchons le rechargement par défaut de la page
2. Vérifions si le champ `title` n'est pas vide
3. Définissons l'état avec une [fonction de mise à jour](https://reactjs.org/docs/state-and-lifecycle.html#state-updates-may-be-asynchronous) pour atténuer les mises à jour asynchrones
4. Déstructurons `exercises` et `title` de l'objet `prevState`
5. Étalons les `exercises` sur le prochain état avec un nouvel objet d'exercice
6. Réinitialisons le `title` pour vider le champ de saisie

Je devrais avoir mentionné que je suis aussi amoureux d'ES6. N'est-ce pas le cas de nous tous ?

#### Mais comment les lister ?

Maintenant est le bon moment. Y a-t-il un composant de liste ? Bien sûr, vous êtes un peu naïf !

À l'intérieur d'un `List`, nous allons parcourir nos `exercises` et retourner un `ListItem` avec un peu de `ListItemText` pour chacun

```
import { List, ListItem, ListItemText } from '@material-ui/core'
```

```
...
```

```
  render() {    const { title, exercises } = this.state    return <Paper>          ...      <List>        {exercises.map(({ id, title }) =>          <ListItem key={id}>            <ListItemText primary={title} />          </ListItem>        )}      </List>    </Paper>  }}
```

Ajoutons également quelques exercices initiaux en dur pour avoir quelque chose à l'écran. Vous l'avez deviné, la trinité de tous les entraînements de musculation, mesdames et messieurs :

```
  state = {    exercises: [      { id: 1, title: 'Développé couché' },      { id: 2, title: 'Soulevé de terre' },      { id: 3, title: 'Squats' }    ],    title: ''  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*7v9-VMXQ-7grca3AxVBtUw.gif)
_Nous pouvons maintenant créer et lister nos exercices !_

Dernier point mais non des moindres, nos utilisateurs sont susceptibles de faire des fautes de frappe, alors mieux vaut ajouter un bouton de suppression à côté de chaque exercice, afin qu'ils puissent supprimer les entrées qu'ils ne veulent plus dans leur liste.

Nous pouvons utiliser `ListItemSecondaryAction` pour faire exactement cela. Placé à l'extrême droite de l'élément de liste, il peut contenir un élément de contrôle secondaire, tel qu'un `IconButton` avec une action

```
import {  /*...*/,  ListItemSecondaryAction,  IconButton} from '@material-ui/core'
```

```
...
```

```
          <ListItem key={id}>            <ListItemText primary={title} />            <ListItemSecondaryAction>              <IconButton                color='primary'                onClick={() => this.handleDelete(id)}              >                {/* ??? */}              </IconButton>            </ListItemSecondaryAction>          </ListItem>
```

```
...
```

Et n'oublions pas le gestionnaire de suppression également :

```
  handleDelete = id =>    this.setState(({ exercises }) => ({      exercises: exercises.filter(ex => ex.id !== id)    }))
```

qui filtrera simplement nos exercices pour ne garder que ceux qui ne correspondent pas à l'`id` de celui qui doit être supprimé.

#### Peut-on avoir une icône de poubelle dans le bouton ?

Oui, ce serait super ! Bien que vous puissiez utiliser [Material Icons](http://google.github.io/material-design-icons/#icon-font-for-the-web) directement depuis le CDN de Google avec les composants `Icon` ou `SvgIcon`, il est souvent préférable d'utiliser un préréglage prêt à l'emploi.

Heureusement, il existe un [package](https://www.npmjs.com/package/@material-ui/icons) Material-UI pour cela

```
yarn add @material-ui/icons
# ou npm i @material-ui/icons
```

Il exporte plus de 900 icônes matérielles officielles en tant que composants React, et les noms des icônes sont presque identiques, comme vous le verrez ci-dessous.

Supposons que nous voulions ajouter une icône de poubelle. Nous irions d'abord sur [material.io/icons](https://material.io/icons/) pour connaître son nom précis

![Image](https://cdn-media-1.freecodecamp.org/images/1*nGrpog4i4mCEWNXIeGeQiA.png)
_Google propose deux variations de l'icône de poubelle, « delete » et « delete forever »_

Ensuite, nous transformons ce nom en PascalCase dans notre chemin d'importation

```
import Delete from '@material-ui/icons/Delete'
```

Tout comme avec les composants Material-UI, si votre configuration a le tree-shaking activé, vous pourriez raccourcir l'importation à

```
import { Delete } from '@material-ui/icons'
```

ce qui est particulièrement utile lorsque vous importez plusieurs icônes à la fois.

Maintenant que nous avons notre icône de poubelle, affichons-la dans notre bouton de suppression

```
<IconButton color='primary' onClick={() => this.handleDelete(id)}>  <Delete /></IconButton>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*0s5edmQdwwrVQ7qEVN9i-A.gif)
_Et avec cela, notre MVP d'application CRUD peut être considéré comme terminé !_

#### Comment puis-je rendre le formulaire moins laid ?

Ah, le style. Je pensais que vous ne demanderiez jamais ! Une touche de CSS ne ferait pas de mal. Alors, importons-nous une feuille de style externe avec des styles globaux ? Ou peut-être utiliser des [modules CSS](https://github.com/css-modules/css-modules) et assigner des noms de classe à nos éléments ? Pas tout à fait.

Sous le capot, Material-UI utilise une bibliothèque CSS-in-JS connue sous le nom de [react-jss](https://github.com/cssinjs/react-jss).

Il s'agit d'une intégration React de la [bibliothèque JSS](https://github.com/cssinjs/jss) par le même auteur, Oleg Isonen. Vous vous souvenez que nous en avons parlé au début ? Son idée de base est de vous permettre de définir des styles en JavaScript. Ce qui distingue JSS parmi [d'autres bibliothèques](https://github.com/MicheleBertoli/css-in-js#readme), c'est son support pour le SSR, sa petite taille de bundle et son riche support de plugins.

Essayons ! Dans notre composant `App`, créez un objet de styles comme vous le feriez avec des styles en ligne. Ensuite, trouvez un nom de clé, par exemple `root`, faisant référence à l'élément `Paper` racine, et écrivez quelques styles en camelCase

```
const styles = {  root: {    margin: 20,    padding: 20,    maxWidth: 400  }}
```

Ensuite, importez le HOC `withStyles` depuis `material-ui`

```
import { withStyles } from '@material-ui/core/styles'
```

et enveloppez le composant `App` avec celui-ci, en passant l'objet `styles` comme argument

```
export default withStyles(styles)(  class App extends Component {    ...  })
```

> Notez que vous pourriez également utiliser le HOC `withStyles` comme un [décorateur](https://babeljs.io/docs/plugins/transform-decorators/). Gardez à l'esprit que create-react-app [ne supporte pas les décorateurs](https://github.com/facebook/create-react-app/issues/214) hors de la boîte pour l'instant, donc si vous insistez pour les utiliser, vous devrez éjecter ou [forker](https://www.youtube.com/watch?v=I22TW-33dDE) pour ajuster la configuration.

Cela injectera une prop `classes` dans `App` contenant un nom de classe généré dynamiquement pour notre élément `root`

![Image](https://cdn-media-1.freecodecamp.org/images/1*GDot9qSrDic2OH-k6EEKXw.png)
_console.log(this.props) révèle un objet classes_

Le nom de la classe est garanti unique, et il sera souvent raccourci dans une version de production. Nous l'assignons ensuite à `Paper` via l'attribut `className`

```
    render() {      const { title, exercises } = this.state      const { classes } = this.props
```

```
      return <Paper className={classes.root}>        ...      </Paper>    }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*gbPzl0I7P961-YwiyoS92g.png)
_Composant Paper avec un style de base appliqué_

Comment fonctionne cette magie ? Il s'avère que `withStyles` est responsable du travail difficile. En coulisses, il a injecté un tableau de styles dans le DOM sous des balises `<style>`. Vous pourriez les repérer si vous creusez dans le `<head>` avec les outils de développement

![Image](https://cdn-media-1.freecodecamp.org/images/1*3shG1_HG51pbygI2-g0bSA.png)
_Aha ! Voici nos styles pour le composant App._

Vous pourriez également voir d'autres balises `style` liées aux composants natifs, comme `MuiListItem` pour le composant `ListItem` que nous avons importé plus tôt. Celles-ci sont auto-injectées à la demande, pour chaque élément d'interface utilisateur donné que vous importez.

Cela signifie que _Material-UI ne chargera jamais de styles pour les composants que nous n'utilisons pas_. D'où une performance accrue et des temps de chargement plus rapides. Cela est très différent de [Bootstrap](https://getbootstrap.com/), qui nécessite de charger l'ensemble du bundle CSS monolithique, que vous utilisiez ou non son vaste assortiment de classes.

Stylisons également le formulaire pour qu'il ait l'air soigné

```
const styles = {  root: {    ...  },  form: {    display: 'flex',    alignItems: 'baseline',    justifyContent: 'space-evenly'  }}
```

Cela espacera joliment le champ de texte et le bouton. N'hésitez pas à vous référer à [align-items](https://css-tricks.com/almanac/properties/a/align-items/) et [justify-content](https://css-tricks.com/almanac/properties/j/justify-content/) sur CSS-Tricks si vous avez besoin de clarifications supplémentaires sur la disposition Flexbox.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FMK3C9iGnWttA0mtwUQpYg.png)
_Cela devrait apaiser notre faim d'esthétique._

#### Bien sûr, mais qu'en est-il du thème alors ?

Le HOC `withStyles` est conçu pour personnaliser un composant ponctuel, mais il n'est pas adapté pour les remplacements à l'échelle de l'application. Chaque fois que vous devez appliquer des changements globaux à tous les composants dans Material-UI, votre premier instinct serait de vous tourner vers l'objet `theme`.

Les thèmes sont conçus pour contrôler les couleurs, les espacements, les ombres et autres attributs de style de vos éléments d'interface utilisateur. Material-UI est livré avec des types de thèmes _clair_ et _sombre_ intégrés, le thème clair étant celui par défaut.

Si nous transformons nos `styles` en une fonction anonyme, elle recevra l'objet `theme` comme argument, afin que nous puissions l'inspecter

```
const styles = theme => console.log(theme) || ({  root: ...,  form: ...})
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*qtc-xSN8m0QC-jLQfNz3sA.png)
_Objet thème par défaut avec des variables de configuration, tel que vu dans la console_

La manière dont vous personnalisez votre thème est à travers des [variables de configuration](https://material-ui-next.com/customization/themes/#theme-configuration-variables), comme `palette`, `type`, `typography`, etc. Pour avoir un aperçu de toutes les propriétés et options imbriquées, visitez la section [Thème par défaut](https://material-ui-next.com/customization/default-theme/) de la documentation Material-UI.

Supposons que nous voulions changer la couleur primaire de `bleu` à `orange`. Tout d'abord, nous devons créer un thème avec l'aide `createMuiTheme` dans `index.js`

```
import { createMuiTheme } from '@material-ui/core/styles'
```

```
const theme = createMuiTheme({ /* config */ })
```

Dans Material-UI, les couleurs sont définies sous la propriété `palette` de `theme`. La palette de couleurs est subdivisée en intentions qui incluent `primary`, `secondary` et `error`. Pour personnaliser une intention, vous pouvez simplement fournir un objet de couleur

```
import { orange } from '@material-ui/core/colors'
```

```
const theme = createMuiTheme({  palette: {    primary: orange  }})
```

Lorsque cela est appliqué, la couleur sera alors calculée pour les variations `light`, `main`, `dark` et `contrastText`. Pour un contrôle plus granulaire, vous pourriez passer un objet simple avec l'une de ces quatre clés

```
const theme = createMuiTheme({  palette: {    primary: {      light: orange[200] // même que '#FFCC80',      main: '#FB8C00', // même que orange[600]      dark: '#EF6C00',      contrastText: 'rgb(0,0,0)'    }  }})
```

Comme vous pouvez le voir, les couleurs individuelles peuvent être exprimées à la fois sous forme de chaîne hex ou rgba (`#FFCC80`) et de [paire teinte/nuance](https://material-ui-next.com/style/color/) (`orange[200]`).

![Image](https://cdn-media-1.freecodecamp.org/images/1*SLj1X7h5Jx-PuLtS2sbsjw.png)
_Intention principale avec les couleurs bleutées par défaut (à gauche) et l'objet de couleur orange (à droite)_

Créer un thème en soi ne suffira pas. Pour remplacer le thème par défaut, nous devrions positionner `MuiThemeProvider` à la racine de notre application et passer notre `theme` personnalisé comme prop

```
import { /*...*/, MuiThemeProvider } from '@material-ui/core/styles'
```

```
const theme = createMuiTheme({  palette: {    primary: orange  }})
```

```
render(  <MuiThemeProvider theme={theme}>    <App />  </MuiThemeProvider>,  document.getElementById('root'))
```

`MuiThemeProvider` transmettra alors le `theme` à tous ses éléments enfants via le contexte React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6TiadjlFJlCFIZnmXP0yLA.png)
_Les éléments d'interface utilisateur qui héritent de la couleur principale sont maintenant affichés en orange._

Bien que cela puisse sembler beaucoup de travail pour changer une couleur, gardez à l'esprit que cette substitution se propagera à _tous_ les composants imbriqués sous le fournisseur. Et en plus des couleurs, nous pouvons maintenant ajuster les tailles de viewport, les espacements, l'opacité et de nombreux autres paramètres.

L'utilisation de variables de configuration lors du stylage de vos composants aidera à la cohérence et à la symétrie dans l'interface utilisateur de votre application. Par exemple, au lieu de coder en dur des valeurs magiques pour `margin` et `padding` sur notre composant `Paper`, nous pourrions plutôt nous appuyer sur l'unité d'espacement du thème

```
const styles = ({ spacing: { unit } }) => ({  root: {    margin: unit,    padding: unit * 3,    maxWidth: 400  },  form: ...}
```

`theme.spacing.unit` est de `8px` par défaut, mais si elle est utilisée uniformément dans l'application, lorsque nous devons mettre à jour sa valeur, plutôt que de fouiller dans l'ensemble de la base de code, nous n'avons besoin de la changer qu'à un seul endroit, c'est-à-dire, dans notre objet d'options que nous passons à `createMuiTheme`.

Les variables de thème sont nombreuses, et si vous tombez sur un cas d'utilisation qui n'est pas couvert par l'objet thème intégré, vous pouvez toujours définir vos propres [variables personnalisées](https://material-ui-next.com/customization/themes/#custom-variables). Voici une version légèrement modifiée de notre application de fitness qui met en avant la palette de couleurs, le type de thème et les options d'unité d'espacement

![Image](https://cdn-media-1.freecodecamp.org/images/1*KLpF7ayyOr3PCO7vpsAZFg.gif)
_Passer d'une couleur à l'autre, d'un type à l'autre et d'une unité d'espacement à l'autre à la volée_

Notez que l'exemple ci-dessus n'est qu'une démonstration. Il recrée un nouveau thème chaque fois qu'une option change, ce qui conduit à un nouvel objet CSS étant recalculé et réinjecté dans le DOM. La plupart du temps, votre configuration de thème restera statique.

Il existe bien plus de fonctionnalités intéressantes que nous n'avons pas couvertes. Par exemple, Material-UI est livré avec un composant `CssBaseline` opt-in qui applique des normalisations multi-navigateurs, telles que la réinitialisation des marges ou de la famille de polices (très similaire à ce que fait [normalize.css](http://necolas.github.io/normalize.css/)).

En ce qui concerne les composants, nous avons notre `Grid` standard avec une disposition à 12 colonnes et cinq viewports (`xs`, `sm`, `md`, `lg` et `xl`). Nous avons également des composants familiers comme `Dialog`, `Menu` et `Tabs`, ainsi que des éléments tels que `Chip` et `Tooltip`. En effet, il y en a toute une série d'autres, et heureusement, ils sont tous très bien documentés avec du code de démonstration exécutable depuis CodeSandbox

![Image](https://cdn-media-1.freecodecamp.org/images/1*EBrJaL41TOHB_9faNZno8w.png)
_Un exemple de page de documentation pour le composant AppBar [https://material-ui-next.com](https://material-ui-next.com" rel="noopener" target="_blank" title=")_

En outre, Material-UI Next fonctionne également avec le [SSR](https://material-ui-next.com/guides/server-rendering/), si vous êtes intéressé par cela. De plus, bien qu'il soit livré avec JSS par défaut, il peut être adapté pour fonctionner avec presque n'importe quelle [autre bibliothèque](https://material-ui-next.com/guides/interoperability/), comme Styled Components, ou même du CSS brut.

Assurez-vous de consulter la documentation officielle pour plus d'informations.

J'espère que vous avez trouvé cette lecture utile ! Et si vous l'aimez tellement que vous êtes excité à l'idée d'en apprendre plus sur Material-UI ou React, alors consultez peut-être ma [chaîne YouTube](https://www.youtube.com/c/CodeRealm) ?

Merci d'être passé ! Et un grand merci à l'équipe de [Call-Em-All](https://www.call-em-all.com/) et à tous les soutiens qui ont aidé à construire cette bibliothèque géniale ❤️

À votre santé,

Alex
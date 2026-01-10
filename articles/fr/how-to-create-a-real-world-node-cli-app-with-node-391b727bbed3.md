---
title: Comment créer une application CLI Node réelle avec Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T21:43:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-real-world-node-cli-app-with-node-391b727bbed3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2mHsgB-JH_yxlRev.png
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment créer une application CLI Node réelle avec Node
seo_desc: 'By Timber.io

  The command line is a user interface that doesn’t get enough attention in the world
  of JavaScript development. The reality is that most dev tools should have a CLI
  to be utilized by nerds like us, and the user experience should be on par...'
---

Par Timber.io

L'interface en ligne de commande est une interface utilisateur qui ne reçoit pas assez d'attention dans le monde du développement JavaScript. La réalité est que la plupart des outils de développement devraient avoir une CLI pour être utilisés par des passionnés comme nous, et l'expérience utilisateur devrait être à la hauteur de celle de votre application web méticuleusement créée. Cela inclut un design agréable, des menus utiles, des messages d'erreur et des sorties clairs, des indicateurs de chargement et des barres de progression, et ainsi de suite.

Il n'existe pas beaucoup de tutoriels réalistes sur la création d'interfaces en ligne de commande avec Node, donc voici le premier d'une série qui ira au-delà d'une application CLI basique "hello world". Nous allons créer une application appelée `outside-cli`, qui vous donnera la météo actuelle et les prévisions sur 10 jours pour n'importe quel lieu.

![Image](https://cdn-media-1.freecodecamp.org/images/U7W2bAC42fKLJFVZ4YDEcjOfhEGR-68myb0T)

**Note** : Il existe plusieurs bibliothèques qui aident à créer des CLI complexes telles que [oclif](https://github.com/oclif/oclif), [yargs](https://github.com/yargs/yargs) et [commander](https://github.com/tj/commander.js), mais nous garderons nos dépendances minimalistes pour cet exemple afin que vous puissiez mieux comprendre comment les choses fonctionnent sous le capot. Ce tutoriel suppose que vous avez une connaissance de base de JavaScript et Node.

### Installation

Comme pour tous les projets JavaScript, la création d'un package.json et d'un fichier d'entrée est la meilleure façon de commencer. Nous pouvons garder cela simple — aucune dépendance n'est nécessaire pour l'instant.

```json
{
  "name": "outside-cli",
  "version": "1.0.0",
  "license": "MIT",
  "scripts": {},
  "devDependencies": {},
  "dependencies": {}
}
```

```js
module.exports = () => {
  console.log('Bienvenue à l'extérieur !')
}
```

Nous aurons besoin d'un moyen d'invoquer notre nouvelle application et d'afficher le message de bienvenue, ainsi que de l'ajouter au chemin du système afin qu'elle puisse être appelée de n'importe où. Un fichier binaire est la solution.

```
#!/usr/bin/env node
require('../')()
```

Vous n'avez jamais vu `#!/usr/bin/env node` auparavant ? Cela s'appelle un [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)). Il indique essentiellement au système qu'il ne s'agit pas d'un script shell et qu'il doit utiliser un autre interpréteur.

Il est important de garder le fichier binaire minimal, car son seul but est d'invoquer l'application. Tout notre code doit résider en dehors du binaire afin qu'il reste modulaire et testable. Cela aidera également si nous voulons fournir un accès programmatique à notre bibliothèque à l'avenir.

Pour exécuter directement le fichier binaire, nous devons lui donner les permissions correctes du système de fichiers. Si vous êtes sous UNIX, cela est aussi simple que d'exécuter `chmod +x bin/outside`. Si vous êtes sous Windows, faites-vous une faveur et utilisez le sous-système Linux.

Ensuite, nous ajouterons notre binaire au fichier package.json. Cela le placera automatiquement sur le chemin du système de l'utilisateur lorsqu'il installera notre package globalement (`npm install -g outside-cli`).

```json
{
  "name": "outside-cli",
  "version": "1.0.0",
  "license": "MIT",
  "bin": {
    "outside": "bin/outside"
  },
  "scripts": {},
  "devDependencies": {},
  "dependencies": {}
}
```

Nous pouvons maintenant appeler directement notre fichier binaire en exécutant `./bin/outside`. Vous devriez voir le message de bienvenue. L'exécution de `npm link` à la racine de votre projet créera un lien symbolique vers votre fichier binaire dans le chemin du système, le rendant accessible de n'importe où en exécutant `outside`.

Lorsque vous exécutez une application CLI, elle se compose d'arguments et de commandes. Les arguments (ou "flags") sont les valeurs précédées d'un ou deux tirets (comme `-d`, `--debug` ou `--env production`) et sont utiles pour passer des options à notre application. Les commandes sont toutes les autres valeurs qui n'ont pas de flag.

Contrairement aux commandes, les arguments n'ont pas besoin d'être spécifiés dans un ordre particulier. Par exemple, nous pourrions exécuter `outside today Brooklyn` et supposer que la deuxième commande sera toujours le lieu, mais ne serait-il pas préférable d'exécuter `outside today --location Brooklyn` au cas où nous voudrions ajouter plus d'options à l'avenir ?

Pour que notre application soit utile, nous devons analyser ces commandes et arguments et les transformer en un objet. Nous pourrions toujours plonger dans `process.argv` et essayer de le faire nous-mêmes, mais installons notre première dépendance appelée [minimist](https://github.com/substack/minimist) pour nous en occuper.

```
npm install --save minimist
```

```js
const minimist = require('minimist')

module.exports = () => {
  const args = minimist(process.argv.slice(2))
  console.log(args)
}
```

**Note** : La raison pour laquelle nous supprimons les deux premiers arguments avec `.slice(2)` est que le premier argument sera toujours l'interpréteur suivi du nom du fichier interprété. Nous ne nous intéressons qu'aux arguments qui suivent.

Maintenant, l'exécution de `outside today` devrait produire `{ _: ['today'] }`. Si vous exécutez `outside today --location "Brooklyn, NY"`, cela devrait produire `{ _: ['today'], location: 'Brooklyn, NY' }`. Nous approfondirons les arguments plus tard lorsque nous utiliserons réellement le lieu, mais pour l'instant, cela suffit pour configurer notre première commande.

### Syntaxe des arguments

Pour mieux comprendre comment fonctionne la syntaxe des arguments, [vous pouvez lire ceci](https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html). Basiquement, un flag peut être précédé d'un ou deux tirets et prendra la valeur immédiatement suivante dans la commande ou sera vrai lorsqu'il n'y a pas de valeur. Les flags à tiret unique peuvent également être combinés pour des booléens raccourcis (`-a -b -c` ou `-abc` vous donnerait `{ a: true, b: true, c: true }`).

Il est important de se souvenir que **les valeurs doivent être entre guillemets si elles contiennent des caractères spéciaux ou un espace**. L'exécution de `--foo bar baz` vous donnerait `{ : ['baz'], foo: 'bar' }`, mais l'exécution de `--foo "bar baz"` vous donnerait `{ foo: 'bar baz' }`.

Il est bon de diviser le code pour chaque commande et de ne le charger en mémoire que lorsqu'il est appelé. Cela crée des temps de démarrage plus rapides et empêche les modules inutiles de se charger. Facile à faire avec une instruction switch sur la commande principale donnée par minimist. Avec cette configuration, chaque fichier de commande doit exporter une fonction, et dans ce cas, nous passons les arguments à chaque commande afin de pouvoir les utiliser plus tard.

```js
const minimist = require('minimist')

module.exports = () => {
  const args = minimist(process.argv.slice(2))
  const cmd = args._[0]

  switch (cmd) {
    case 'today':
      require('./cmds/today')(args)
      break
    default:
      console.error(`"${cmd}" n'est pas une commande valide !`)
      break
  }
}
```

```js
module.exports = (args) => {
  console.log('aujourdhui il fait ensoleillé')
}
```

Maintenant, si vous exécutez `outside today`, vous verrez le message "aujourdhui il fait ensoleillé", et si vous exécutez `outside foobar`, il vous dira que "foobar" n'est pas une commande valide. Nous devons toujours interroger une API météo pour obtenir des données réelles, mais c'est un bon début.

Il y a quelques commandes et arguments qui sont attendus dans chaque CLI : `help`, `--help` et `-h`, qui doivent afficher les menus d'aide, et `version`, `--version` et `-v` qui doivent afficher la version actuelle de l'application. Nous devons également afficher par défaut un menu d'aide principal si aucune commande n'est spécifiée.

Cela peut être facilement implémenté dans notre configuration actuelle en ajoutant deux cas à notre instruction switch, une valeur par défaut pour la variable `cmd`, et en implémentant quelques instructions if pour les flags d'arguments d'aide et de version. Minimist analyse automatiquement les arguments en clés/valeurs, donc l'exécution de `outside --version` rendra `args.version` égal à vrai.

```js
const minimist = require('minimist')

module.exports = () => {
  const args = minimist(process.argv.slice(2))

  let cmd = args._[0] || 'help'

  if (args.version || args.v) {
    cmd = 'version'
  }

  if (args.help || args.h) {
    cmd = 'help'
  }

  switch (cmd) {
    case 'today':
      require('./cmds/today')(args)
      break

    case 'version':
      require('./cmds/version')(args)
      break

    case 'help':
      require('./cmds/help')(args)
      break

    default:
      console.error(`"${cmd}" n'est pas une commande valide !`)
      break
  }
}
```

Pour implémenter nos nouvelles commandes, suivez le même format que la commande `today`.

```js
const { version } = require('../package.json')

module.exports = (args) => {
  console.log(`v${version}`)
}
```

```js
const menus = {
  main: `
    outside [command] <options>

    today .............. afficher la météo pour aujourd'hui
    version ............ afficher la version du package
    help ............... afficher le menu d'aide pour une commande`,

  today: `
    outside today <options>

    --location, -l ..... le lieu à utiliser`,
}

module.exports = (args) => {
  const subCmd = args._[0] === 'help'
    ? args._[1]
    : args._[0]

  console.log(menus[subCmd] || menus.main)
}
```

Maintenant, si vous exécutez `outside help today` ou `outside today -h`, vous devriez voir le menu d'aide pour la commande `today`. L'exécution de `outside` ou `outside -h` devrait vous montrer le menu d'aide principal.

![Image](https://cdn-media-1.freecodecamp.org/images/G1BNtKcKV5D1dMaVgKfclg7mZ1IYF8WXps9w)

Cette configuration de projet est vraiment géniale car si vous devez ajouter une nouvelle commande, tout ce que vous avez à faire est de créer un nouveau fichier dans le dossier `cmds`, de l'ajouter à l'instruction switch et d'ajouter un menu d'aide s'il en a un.

```js
module.exports = (args) => {
  console.log('demain il pleut')
}
```

```js
// ...
    case 'forecast':
      require('./cmds/forecast')(args)
      break
// ...
```

```js
const menus = {
  main: `
    outside [command] <options>

    today .............. afficher la météo pour aujourd'hui
    forecast ........... afficher les prévisions météo sur 10 jours
    version ............ afficher la version du package
    help ............... afficher le menu d'aide pour une commande`,

  today: `
    outside today <options>

    --location, -l ..... le lieu à utiliser`,

  forecast: `
    outside forecast <options>

    --location, -l ..... le lieu à utiliser`,
}

// ...
```

Parfois, une commande peut prendre beaucoup de temps à s'exécuter. Si vous récupérez des données depuis une API, générez du contenu, écrivez des fichiers sur le disque ou tout autre processus qui prend plus de quelques millisecondes, vous voulez donner un retour à l'utilisateur que votre application n'a pas gelé et travaille simplement dur. Parfois, vous pouvez mesurer la progression de votre opération et il est logique d'afficher une barre de progression, mais d'autres fois, c'est plus variable et il est plus logique d'afficher un indicateur de chargement.

Pour notre application, nous ne pouvons pas mesurer la progression de nos requêtes API, donc nous utiliserons un spinner basique pour montrer que quelque chose se passe. Installez deux autres dépendances pour nos requêtes réseau et notre spinner :

```
npm install --save axios ora
```

### Récupération des données depuis l'API

Créons maintenant un utilitaire qui fera une requête à l'API météo Yahoo pour les conditions actuelles et les prévisions d'un lieu.

**Note** : L'API Yahoo utilise la syntaxe "YQL", et elle est un peu étrange — n'essayez pas de la comprendre, copiez et collez simplement. C'était la seule API météo que j'ai pu trouver qui ne nécessitait pas de clé API.

```js
const axios = require('axios')

module.exports = async (location) => {
  const results = await axios({
    method: 'get',
    url: 'https://query.yahooapis.com/v1/public/yql',
    params: {
      format: 'json',
      q: `select item from weather.forecast where woeid in
        (select woeid from geo.places(1) where text="${location}")`,
    },
  })

  return results.data.query.results.channel.item
}
```

```js
const ora = require('ora')
const getWeather = require('../utils/weather')

module.exports = async (args) => {
  const spinner = ora().start()

  try {
    const location = args.location || args.l
    const weather = await getWeather(location)

    spinner.stop()

    console.log(`Conditions actuelles à ${location} :`)
    console.log(`\t${weather.condition.temp}° ${weather.condition.text}`)
  } catch (err) {
    spinner.stop()

    console.error(err)
  }
}
```

Maintenant, si vous exécutez `outside today --location "Brooklyn, NY"`, vous verrez un spinner rapide pendant la requête, suivi des conditions météo actuelles.

Comme la requête se fait si rapidement, il peut être difficile de voir l'indicateur de chargement. Si vous voulez le ralentir manuellement pour le voir, vous pouvez ajouter cette ligne au début de votre fonction utilitaire météo : `await new Promise(resolve => setTimeout(resolve, 5000)).

![Image](https://cdn-media-1.freecodecamp.org/images/0eoDghnUZOOvNti5wf3puX9oyxvK4RMjYG10)

Super ! Copions maintenant ce code dans notre commande `forecast`, et changeons un peu le formatage.

```js
const ora = require('ora')
const getWeather = require('../utils/weather')

module.exports = async (args) => {
  const spinner = ora().start()

  try {
    const location = args.location || args.l
    const weather = await getWeather(location)

    spinner.stop()

    console.log(`Prévisions pour ${location} :`)
    weather.forecast.forEach(item =>
      console.log(`\t${item.date} - Min : ${item.low}° | Max : ${item.high}° | ${item.text}`))
  } catch (err) {
    spinner.stop()

    console.error(err)
  }
}
```

Vous pouvez maintenant voir les prévisions météo sur 10 jours lorsque vous exécutez `outside forecast --location "Brooklyn, NY"`. Cela a l'air bien ! Ajoutons un autre utilitaire pour obtenir automatiquement notre localisation basée sur notre adresse IP si aucun lieu n'est spécifié dans la commande.

```js
const axios = require('axios')

module.exports = async () => {
  const results = await axios({
    method: 'get',
    url: 'https://api.ipdata.co',
  })

  const { city, region } = results.data
  return `${city}, ${region}`
}
```

```js
// ...
const getLocation = require('../utils/location')

module.exports = async (args) => {
  // ...
    const location = args.location || args.l || await getLocation()
    const weather = await getWeather(location)
  // ...
}
```

Maintenant, si vous exécutez simplement `outside forecast` sans lieu, vous verrez les prévisions pour votre localisation actuelle.

![Image](https://cdn-media-1.freecodecamp.org/images/oXE-zFoeG9LjeDVfp-n7vhSs3KZuC3tue3-m)

### Gestion des erreurs

Je ne suis pas entré dans les détails sur la meilleure façon de gérer les erreurs (cela viendra dans un tutoriel ultérieur), mais la chose la plus importante à retenir est d'utiliser les codes de sortie corrects.

Si votre CLI a une erreur critique, vous devez quitter avec `process.exit(1)`. Cela informe le terminal que le programme ne s'est pas terminé correctement, ce qui vous avertira depuis un service CI, par exemple.

Créons un utilitaire rapide qui fait cela pour nous, afin que nous puissions obtenir le code de sortie correct lorsqu'une commande inexistante est exécutée.

```js
module.exports = (message, exit) => {
  console.error(message)
  exit && process.exit(1)
}
```

```js
// ...
const error = require('./utils/error')

module.exports = () => {
  // ...
    default:
      error(`"${cmd}" n'est pas une commande valide !`, true)
      break
  // ...
}
```

### Finalisation

La dernière étape pour mettre notre bibliothèque à disposition est de la publier sur un gestionnaire de packages. Comme notre application est écrite en JavaScript, il est logique de la publier sur NPM. Complétons un peu plus notre `package.json` :

```json
{
  "name": "outside-cli",
  "version": "1.0.0",
  "description": "Une application CLI qui vous donne les prévisions météo",
  "license": "MIT",
  "homepage": "https://github.com/timberio/outside-cli#readme",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/timberio/outside-cli.git"
  },
  "engines": {
    "node": ">=8"
  },
  "keywords": [
    "weather",
    "forecast",
    "rain"
  ],
  "preferGlobal": true,
  "bin": {
    "outside": "bin/outside"
  },
  "scripts": {},
  "devDependencies": {},
  "dependencies": {
    "axios": "^0.18.0",
    "minimist": "^1.2.0",
    "ora": "^2.0.0"
  }
}
```

* La définition de `engine` garantira que toute personne installant notre application dispose d'une version mise à jour de Node. Comme nous utilisons la syntaxe async/await sans transpilation, nous exigeons Node 8.0 ou supérieur.
* La définition de `preferGlobal` avertira l'utilisateur s'il installe avec `npm install --save` plutôt qu'avec `npm install --global`.

C'est tout ! Vous pouvez maintenant exécuter `npm publish` et votre application sera disponible pour le téléchargement. Si vous voulez aller plus loin et publier sur d'autres gestionnaires de packages (comme Homebrew), vous pouvez consulter [pkg](https://github.com/zeit/pkg) ou [nexe](https://github.com/nexe/nexe), qui vous aident à bundler votre application dans un binaire autonome.

### Résumé

C'est la structure que nous suivons pour toutes nos applications CLI ici chez [Timber](https://timber.io/), et cela aide à garder les choses organisées et modulaires.

Quelques **points clés** de ce tutoriel pour ceux qui l'ont seulement parcouru :

* Les fichiers binaires sont le point d'entrée de toute application CLI et ne doivent invoquer que la fonction principale
* Les fichiers de commande ne doivent pas être requis tant qu'ils ne sont pas nécessaires
* Incluez toujours les commandes `help` et `version`
* Gardez les fichiers de commande minces — leur but principal est d'appeler des fonctions et d'afficher des messages utilisateur
* Montrez toujours une sorte d'indicateur d'activité
* Quittez avec les codes d'erreur corrects

J'espère que vous avez maintenant une meilleure compréhension de la création et de l'organisation des applications CLI dans Node. Il s'agit de la première partie d'une série de tutoriels, alors revenez plus tard pour approfondir l'ajout de design, d'art ASCII et de couleur, l'acceptation des entrées utilisateur, l'écriture de tests d'intégration, et plus encore. Vous pouvez voir tout le code source que nous avons écrit aujourd'hui [sur GitHub](https://github.com/timberio/outside-cli).

_Nous sommes une entreprise de journalisation basée sur le cloud ici @ [Timber](http://timber.io). Nous serions ravis que vous essayiez notre produit (il est vraiment génial ! — vous pouvez créer un compte gratuit [ici](http://timber.io)), mais c'est tout ce que nous allons promouvoir notre produit... vous êtes venus ici pour apprendre à créer une application CLI en Node et nous espérons que ce guide vous a aidé à commencer._

_Publié à l'origine sur [timber.io](https://timber.io/blog/creating-a-real-world-cli-app-with-node).
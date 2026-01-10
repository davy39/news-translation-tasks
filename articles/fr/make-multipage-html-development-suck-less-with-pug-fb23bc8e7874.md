---
title: Rendre le développement multipage HTML moins pénible avec Pug
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T15:01:11.000Z'
originalURL: https://freecodecamp.org/news/make-multipage-html-development-suck-less-with-pug-fb23bc8e7874
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bHG9n86BQWgllXfDw0uXhw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: webpack
  slug: webpack
seo_title: Rendre le développement multipage HTML moins pénible avec Pug
seo_desc: 'By Jared Nutt

  Inspired by a true story

  Let’s take a journey…

  Imagine you are on the call list for a freelance agency in a city of your choosing.
  Now let’s say you get a nice message in your inbox. You open up the message and
  it looks pretty normal.


  ...'
---

Par Jared Nutt

#### Inspiré d'une histoire vraie

### Faisons un voyage…

Imaginez que vous êtes sur la liste d'appel d'une agence freelance dans une ville de votre choix. Supposons que vous recevez un joli message dans votre boîte de réception. Vous ouvrez le message et il semble tout à fait normal.

> Nous avons un besoin immédiat pour un Développeur pour commencer aujourd'hui.

le message et il semble tout à fait normal.

_Nous avons un besoin immédiat pour un Développeur pour commencer aujourd'hui._

En tant que personne qui aime manger pour survivre, vous tapez quelques informations et postulez.

Dans les cinq minutes suivant l'envoi, vous recevez un appel. Dix minutes plus tard, vous obtenez l'accès au serveur.

Il va sans dire que vous êtes sous pression. La date limite est à la fin de la journée.

Vous ouvrez les fichiers HTML et les examinez… avec horreur.

Le code est partout, désordonné et mal organisé. Sans compter que vous devez apporter des modifications à l'en-tête et au pied de page… sur cinq pages différentes.

La première chose que vous faites est de le passer par [Prettify](https://github.com/google/code-prettify) (Merci Dieu pour Prettify). Cela l'a nettoyé, mais il y a encore d'autres problèmes. Il s'agit d'un site HTML statique, ce qui signifie que chaque modification que vous apportez aux éléments globaux (en-tête, pied de page, etc.), vous devrez la copier dans **TOUS** les fichiers. Oh, mon Dieu.

Que allez-vous faire ???

C'est simple, vous allez créer un fichier Webpack pour gérer la partie pénible de l'écriture HTML, et vous allez le faire rapidement.

## Voici ce avec quoi vous devez être familier :

* Javascript ! (à cause de Webpack)
* HTML ! (parce que c'est de ça qu'est fait l'internet)
* CSS ! (parce que qui aime les choses laides ?)
* pug ! (parce que c'est le but de cet article !)
* npm (parce que c'est Dieu)
* Connaissances de base de la ligne de commande (parce que faire des choses via des téléchargements est stupide…)
* Connaître Jim Carrey (parce que les gifs)

Si vous n'êtes pas familier avec pug, vous pouvez toujours vous en sortir. Mais si vous avez le temps, lisez à ce sujet. Je recommande d'apprendre [pug avec des carlins](https://codepen.io/mimoduo/post/learn-pug-js-with-pugs). Ou leurs [docs](https://pugjs.org/api/getting-started.html). Ce sont aussi des ressources correctes, je suppose.

Voici les versions que j'ai utilisées pour cela :

* html-loader : 0.5.5,
* html-webpack-plugin : 3.2.0,
* pug-html-loader : 1.1.5,
* Webpack : 4.12.0
* webpack-cli : 3.0.8
* npm : 6.1.0
* node : 10.4.0

**Mise à jour :** J'ai fait une vidéo ! Regardez-la si vous ne voulez pas lire, mais préférez écouter ma voix pendant 30 minutes.

%[https://youtu.be/vBJwetqiX0g]

# Étape 1. Organisez la structure de votre projet

Voici comment j'aime organiser mon dossier pour ce type de projets.

```
src/
oldHTML/
dist/
images/
css/
webpack.config
```

J'aime mettre tout le HTML original dans un dossier séparé que je ne peux pas supprimer par accident. Webpack est un peu plus gentil que, disons, Gulp, qui m'a déjà supprimé un dossier entier ?. Cette structure est suffisamment bonne pour commencer.

# Étape 2. Démarrez le moteur npm

À part : Je suis récemment revenu à `npm` depuis `yarn` pour quelques raisons. L'une d'entre elles était qu'il a cessé de fonctionner et que j'avais peu de patience pour le faire fonctionner à nouveau. Article intéressant [ici](https://mixmax.com/blog/to-yarn-and-back-again-npm), si vous voulez en lire plus.

**Bref, initialisez ce npm.**

```
npm init -y
```

Note : (le **-y** est si vous ne voulez pas répondre à ses questions)

## **Installez les dépendances de développement.**

Ne vous inquiétez pas, je vais expliquer chacun d'eux au fur et à mesure.

```
npm install -D webpack webpack-cli pug-html-loader html-webpack-plugin html-loader
```

## **Ajoutez quelques scripts au package.json**

Par défaut, package.json a un script, mais nous devons en ajouter quelques-uns.

```
"dev": "webpack --watch --mode development",
"prod": "webpack --mode production"
```

Ce sont les deux que j'aime inclure. Le premier exécutera Webpack en mode développement (note : le flag --mode est nouveau dans Webpack 4) et surveillera les changements de fichiers. Le second est lorsque nous voulons exécuter Webpack en production, cela minifie généralement les fichiers.

Cela devrait ressembler à quelque chose comme ceci :

```
"name": "pugTut",
"version": "1.0.0",
"description": "",
"main": "index.js",
"scripts": {
"test":
  "dev": "webpack --watch --mode development",
  "prod": "webpack --mode production"
},
.....more code
```

## **Créez quelques fichiers de démarrage pour tester notre configuration Webpack**

Webpack a besoin d'un point d'entrée, alors créons-en un. Créez un **app.js** dans le dossier **src/**. Il peut être vide. Peu importe. Il a également besoin d'un fichier pug initial à compiler. Créez un fichier **index.pug** dans le dossier **src/**, également.

## **Créez et configurez webpack.config.js dans le répertoire racine**

D'accord, si vous n'avez jamais utilisé Webpack auparavant, je vais passer en revue chaque partie individuellement pour vous donner (et espérons-le, à moi aussi) une idée de ce qui se passe dans ce fichier de configuration.

Tout d'abord, déclarons nos dépendances.

```
// webpack.config.js
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
```

**path** est une dépendance native de Node, donc vous ne devriez pas avoir à vous soucier de son inclusion dans votre package.json.

**Webpack** est, eh bien Webpack…

**HtmlWebpackPlugin** est ce que nous utilisons pour extraire le HTML. Je ne suis pas un expert du fonctionnement de Webpack. D'après ce que je comprends, puisque Webpack est conçu pour consommer du JavaScript, nous devons avoir des chargeurs dans notre fichier de configuration pour extraire des choses comme le HTML et le CSS. **HtmlWebpackPlugin** est ce que nous utilisons pour faire quelque chose d'utile avec le HTML extrait par les chargeurs.

Cool ? Étape suivante…

```
const pug = {
  test: /\.pug$/,
  use: ['html-loader?attrs=false', 'pug-html-loader']
};
```

Cette méthode est utilisée par [Wes Bos](https://wesbos.com/) et je l'aime vraiment, donc je l'utilise. Nous devons définir des règles sur la façon de gérer certains types de fichiers, par exemple .pug ou .css. Le mettre dans une variable le rend plus lisible, à mon avis. Bref, nous configurons un cas de test avec une regexp, puis définissons les chargeurs que nous voulons utiliser. Pour une raison quelconque, les chargeurs sont listés dans l'ordre inverse de ce à quoi vous pourriez vous attendre. Je suis sûr qu'il y a une explication mais je n'ai pas pu la trouver.

Confus ? Ce que cela signifie, c'est que si nous voulons utiliser pug pour compiler en HTML, nous l'écrivons dans l'ordre ci-dessus : notre **chargeur html** -> **chargeur pug**. Cependant, en réalité, lorsque le code s'exécute, il exécute d'abord le **chargeur pug**… puis le **chargeur HTML**. Oui.

Note : Ne vous inquiétez pas pour `?attrs=false` pour l'instant, je l'expliquerai un peu plus tard.

Cool ? Étape suivante…

```
const config = {
  entry: './src/app.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js'
  },
  module: {
    rules: [pug]
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.pug',
      inject: false
    })
 ]
};
module.exports = config;
```

Bon sang. C'est beaucoup de choses. Décomposons cela.

**entry** est simplement le point d'entrée pour notre fichier JS.

**output** définit où nous voulons que notre fichier JS aille. Ce n'est pas là que nos fichiers HTML iront. Comme mentionné ci-dessus, **path** est un module node. **__dirname** est une variable que nous pouvons obtenir de Node. Le filename est ce que nous voulons appeler notre fichier JS. Le `[name]` est une substitution. Dans ce cas, il utilise le nom de fichier du fichier d'entrée. Vous pouvez également utiliser `[hash]` si vous voulez un identifiant unique.

**module** définit les différents modules. Pour les besoins de ce tutoriel, il n'y a qu'un seul module avec un ensemble de règles. **rules** définit les règles que nous utiliserons pour ce module. Nous y ajoutons la variable **pug** que nous avons créée précédemment. Si propre, si net.

Enfin, plugins est l'endroit où nous pouvons ajouter des éléments tiers. Dans notre cas, nous utilisons **HtmlWebpackPlugin** pour faire quelque chose avec nos fichiers pug.

**filename** est ce que nous voulons appeler notre fichier HTML. **template** est le fichier pug que nous compilons. **inject** est : « injecter tous les actifs dans le modèle donné ». Je l'ai défini sur false parce que… eh bien, honnêtement, je ne m'en souviens pas.

L'une des choses les plus pénibles avec **HtmlWebpackPlugin** est que vous devez créer une entrée pour **CHAQUE** fichier HTML. J'ai essayé de trouver un moyen de contourner cela, mais je n'ai trouvé aucune solution simple.

```js
// webpack.config.js
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const pug = {
  test: /\.pug$/,
  use: ['html-loader?attrs=false', 'pug-html-loader']
};
const config = {
  entry: './src/app.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js'
  },
  module: {
    rules: [pug]
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.pug',
      inject: false
    })
 ]
};
module.exports = config;
```

Avant de continuer, assurons-nous que notre code fonctionne ! Exécutez le script.

```
npm run dev
```

Si tout s'est bien passé, vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_JQLr9uvGeW2P9VQRaWmsMA.png)

Nous avons parcouru un long chemin. Voici un cadeau :



# Étape 3. Divisez les pages en partials

C'est là que la magie commence à opérer. Je sais que cela semble comme si nous avions travaillé pendant un moment avec très peu de gains, mais faites-moi confiance… cela en valait la peine.

L'une des fonctionnalités les plus importantes de pug est les partials. L'idée est d'avoir un fichier qui contient la plupart de votre code global (head, header, footer, nav, etc.) et d'avoir des fichiers individuels pour tout votre contenu.

Créons quelques fichiers. Vous devriez avoir déjà créé le fichier **index.pug**, mais créons-en un autre, **layout.pug**.

```
src/
- index.pug
- layout.pug
```

# Étape 4. Configurez le fichier de layout

Le fichier de layout est essentiellement le modèle principal pour l'ensemble de votre site. Il contiendra toutes les informations globales, par exemple head, header et footer.

```
//- layout.pug
doctype html
html
  head
    title Je suis un titre
  body
    block header
    block content
    block footer
  script(src="somescript.js")
```

Je suppose qu'il y a quelque chose à expliquer : pug est entièrement basé sur l'indentation, similaire à YAML. C'est glorieux, car cela signifie plus de balises de fermeture ! Cependant, cela peut poser problème, surtout pour ceux qui ont une mauvaise indentation dès le départ. Alors commencez lentement et assurez-vous que tout est correctement indenté et vous serez bien.

En regardant notre fichier layout.pug, vous verrez quelques balises HTML familières mélangées à des balises moins familières. Je vous recommande vivement de télécharger la coloration syntaxique pour pug dans votre éditeur de choix. Si vous utilisez VSCode, elle devrait être incluse par défaut. Merci Microsoft.

Je pense que c'est assez facile à comprendre, mais examinons le cœur du document pour nous assurer de savoir ce qui se passe.

```
head
  title Je suis un titre
body
  block header
  block content
  block footer
script(src="somescript.js")
```

**head**, **body**, **title** et **script** sont des balises normales, mais qu'est-ce que **block** ? **block** est la façon dont nous définissons le contenu dynamique. En gros, cela indique à pug que du contenu va aller ici. Espérons que cela aura plus de sens lorsque nous créerons nos fichiers de page individuels.

# Étape 5. Créez plus de partials

Utilisons ce fichier index.pug.

```
//- index.pug
extends layout
block content
  p Woah.
```

En regardant notre fichier index, il semble étrangement petit pour une page HTML complète. C'est à cause de ce petit **extends**. extends indique à pug que vous souhaitez utiliser un autre fichier pug comme modèle, dans notre cas **layout**. Ensuite, en dessous de cela, **block content** fait référence à ce que nous avons mis dans notre fichier **layout.pug**.

Si vous avez toujours Webpack en cours d'exécution en arrière-plan, il devrait recompiler et vous obtiendrez un tout nouveau **index.html** dans votre dossier **dist/**. Sinon, exécutez à nouveau Webpack.

# Étape 6. Récupérez tout l'ancien HTML

Ces fichiers de démarrage sont bien et beaux, mais nous devons faire des progrès réels. Nous devons commencer à récupérer ce HTML et à l'utiliser ! Heureusement, pug reconnaîtra les anciennes balises HTML, donc vous pouvez littéralement copier tout le contenu HTML que vous voulez et le coller là.

Cela pourrait ressembler à ceci :

```
extends layout
block content
  <h1>blerb</h1>
  <p>Woah.</p>
```

**D'accord, ce n'est pas vraiment si simple.**

Comme je l'ai mentionné, pug est basé sur l'indentation. Pour vous faciliter la vie, je vous suggère de supprimer toute l'indentation du fichier HTML avant de le coller dans le fichier pug. Cela fonctionnera principalement, mais vous devrez probablement le bidouiller un peu. Heureusement pour nous, **pug-html-loader** nous indiquera ce qui ne va pas lorsqu'il essaiera de compiler. Il y a quelques exemples de problèmes courants dans l'étape suivante.

# Étape 7. Commencez à optimiser

Je ne vais pas mentir, lorsque vous insérez du HTML pour la première fois, Webpack ne va pas l'aimer. Voici quelques points à surveiller :

## **Images**

1. Assurez-vous que les liens vers les images sont corrects. Pour une raison quelconque, cela échoue souvent si le src = « images/ » au lieu de src = « /images/ »

2. J'ai promis plus tôt de revenir sur ce que `?attrs=false` était, eh bien, nous y voilà !

Voici l'extrait du site [html-loader](https://www.npmjs.com/package/html-loader) expliquant ce que cela fait.

> Pour désactiver complètement le traitement des attributs de balise (par exemple, si vous gérez le chargement des images côté client), vous pouvez passer `attrs=false`.

```
html-loader?attrs=false

```

## **Javascript**

pug ne s'entend pas bien avec le JS dans les balises script. Si vous collez des balises script JS d'ouverture et de fermeture régulières, cela peut fonctionner correctement. Cependant, si vous souhaitez utiliser la balise script pug, assurez-vous simplement d'ajouter un point à la fin, comme ceci :

# Étape 8. Créez plus de pages et commencez à convertir en balises pug

Clairement, c'est inutile si vous ne faites que la page d'index. Pour ce que vous faites, créez simplement un nouveau fichier pour chaque page que vous voulez. De plus, assurez-vous de créer de nouvelles entrées **HtmlWebpackPlugin** dans la section **plugins** dans Webpack.

Cela finira par ressembler à ceci :

```js
//webpack.config.js
...previous code...
plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.pug',
      inject: false
    }),
    new HtmlWebpackPlugin({
      filename: 'contact.html',
      template: 'src/contact.pug',
      inject: false
    })
  ]
...more code...
```

Vous n'avez pas besoin de tout convertir au format pug immédiatement. En fait, si vous avez un site énorme avec une tonne de HTML, vous pouvez le faire au fur et à mesure, mais cela le rend plus facile.

## **Includes**

Ce ne serait pas un très bon tutoriel si nous ne parlions pas des includes. Vous vous souvenez de ces blocs dans le fichier de layout ? Eh bien, si vous ne voulez pas que le fichier de layout soit géant, vous pouvez créer des fichiers séparés qui seront intégrés au moment de la compilation. Par exemple, si vous voulez créer un seul fichier qui contient toutes les informations d'en-tête. Diviser cela de cette manière aide également substantiellement avec l'indentation.

Créez un nouveau fichier « header » dans un nouveau dossier « includes » :

```
src/
-- includes/
   header.pug
```

Dans ce fichier, mettez ce que vous voulez dans l'en-tête.

```
//- header.pug
header
  h1 Je suis un en-tête
```

Maintenant, retournez à layout.pug et incluez-le.

```
//- layout.pug
doctype html
html
  head
    title Je suis un titre
  body
    block header
      include includes/header
    block content
    block footer
  script(src="somescript.js")
```

# Étape 7. Voulez-vous devenir élégant ?

Il y a beaucoup plus de choses que vous pouvez faire avec pug et webpack. Cependant, je pense que nous avons atteint la fin des bases. Toujours, consultez [mixins](https://pugjs.org/language/mixins.html). Ces choses sont incroyables.

# Conclusion

Je vous recommande vivement d'intégrer le HTML lentement, sinon vous finirez par déboguer 1 000 erreurs à la fois.
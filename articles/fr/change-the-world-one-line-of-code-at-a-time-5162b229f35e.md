---
title: Changer le monde, une ligne de code à la fois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T22:22:01.000Z'
originalURL: https://freecodecamp.org/news/change-the-world-one-line-of-code-at-a-time-5162b229f35e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cHz2cUq8zLjjSsB_e9vexw.jpeg
tags:
- name: coding
  slug: coding
- name: Inspiration
  slug: inspiration
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
seo_title: Changer le monde, une ligne de code à la fois
seo_desc: 'By Usheninte Dangana

  People like to look at changing the world as a big task. I believe changing the
  world can be done in little steps.

  The key is identifying a problem and taking a little step.

  My journey began on Friday, September 7th, 2018. That w...'
---

Par Usheninte Dangana

Les gens aiment voir le changement du monde comme une grande tâche. Je crois que changer le monde peut se faire en petites étapes.

La clé est d'identifier un problème et de faire un petit pas.

Mon voyage a commencé le vendredi **7 septembre 2018**. C'était le jour où j'ai décidé de construire un plugin React pour la suite de tests freeCodeCamp. J'ai remarqué un problème et j'ai agi.

Il y a une [version fonctionnelle](https://www.npmjs.com/package/react-fcctest) disponible pour l'installation sur le registre du Node Package Manager. C'est une étape importante pour moi, car le projet est ma première contribution Open Source.

J'ai utilisé certaines technologies clés pour construire le projet, comme Webpack, React, NPM et Node.js. J'ai eu beaucoup de plaisir à le construire, et j'ai aussi beaucoup appris.

J'ai essayé plusieurs fois (en fait, toute une journée) avant de réussir à faire fonctionner le plugin.

Après l'avoir fait fonctionner, l'implémentation dans une application React était un défi. Bien que j'ai été confronté à des difficultés techniques, à la fin, le plugin a fonctionné.

### Le processus

L'idée derrière le projet était simple. Tout ce que je voulais faire était de trouver un moyen simple d'ajouter la suite de tests freeCodeCamp aux applications React.

Mon premier plan était de le construire avec Create-React-App.

Je pensais que puisque je pouvais l'utiliser pour construire des applications React, je pourrais l'utiliser pour construire un plugin. Je me trompais.

Create-React-App était trop lourd pour ce que je devais construire.

J'ai découvert que pour rendre le plugin facile à exporter, j'aurais besoin de certaines configurations supplémentaires.

Je suis allé en ligne et j'ai googlé plusieurs fois, et je suis tombé sur Webpack et react-helmet. Ce que j'ai trouvé était à la fois amazing et confus, au début.

Pourtant, je savais que c'était ce dont j'avais besoin. J'ai continué à chercher un peu plus.

Avant Webpack, j'avais essayé d'exporter et de publier le plugin en tant que module sans configuration supplémentaire. Cela n'a pas fonctionné. Erreur de débutant, je sais.

C'était un grand défi que je devais surmonter.

Heureusement, nous apprenons en grandissant !

Pendant que je développis le plugin, il y avait des coupures de courant constantes. Au Nigeria, la situation électrique n'est pas très stable.

Je devais travailler jusqu'à ce que mon ordinateur portable s'éteigne, puis réfléchir profondément à ce que je devais faire lorsque le courant revenait.

Tout cela s'est passé le deuxième jour (samedi).

### La magie, la beauté

En utilisant Webpack, j'ai commencé à construire le plugin.

J'ai placé le code principal dans un fichier index.js. Voici le code ci-dessous :

```js
import React from 'react';
import { Helmet } from 'react-helmet';
import './styles.css';

const ReactFCCtest = () => {
  return (
    <div>
      <Helmet>
        <script type="text/javascript" 
                src="https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js" >
        </script>
      </Helmet>
      <h5>react-fcctest running</h5>
    </div>
  );
};

export default ReactFCCtest;
```

Le code ci-dessus était tout ce dont j'avais besoin pour ajouter le script à la balise head de n'importe quelle application React que je souhaitais.

Je suis tombé sur un [article sur Medium](https://medium.com/dailyjs/building-a-react-component-with-webpack-publish-to-npm-deploy-to-github-guide-6927f60b3220) qui m'a été d'une grande aide.

Il m'a aidé à comprendre comment utiliser Webpack pour créer un module node que je pourrais publier avec succès sur le registre du Node Package Manager.

J'ai suivi les instructions de cet article. Après avoir fait quelques changements, j'ai construit le fichier **webpack.config.js** suivant :

```js
const path = require('path');
const HtmlWebpackPlugin = require("html-webpack-plugin");
const htmlWebpackPlugin = new HtmlWebpackPlugin({
    template: path.join(__dirname, "demo/src/index.html"),
    filename: "./index.html"
});
module.exports = {
    entry: path.join(__dirname, "demo/src/index.js"),
    output: {
        path: path.join(__dirname, "demo/dist"),
        filename: "bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                use: "babel-loader",
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            }
        ]
    },
    plugins: [htmlWebpackPlugin],
    resolve: {
        extensions: [".js", ".jsx"]
    },
    devServer: {
        port: 3001
    }
};
```

Permettez-moi d'expliquer ce que fait ce fichier :

>> Premièrement, il utilise le HtmlWebpackPlugin pour créer un fichier HTML afin de servir mon bundle webpack.

>> Ensuite, il exporte le plugin que j'ai créé en tant que module node.

>> Il indique que le point d'entrée de mon plugin se trouve à l'emplacement `demo/src/index.js`. Cela signifie que c'est là que le code à exporter sera pris.

>> Ensuite, il indique que le répertoire de sortie de mon plugin est `demo/dist`. Dans ce répertoire, le plugin **react-fcctest** sera exporté dans un fichier nommé `bundle.js`.

>> Ensuite, il introduit un ensemble de règles pour le fichier à exporter.

>> Les règles indiquent au fichier de faire deux choses. Premièrement, utiliser babel-loader lors de la manipulation de fichiers `.js` et `.jsx` et ne pas inclure le dossier `node_modules`. Deuxièmement, utiliser style-loader et css-loader lors de la manipulation de fichiers `.css`.

>> La partie resolve et extensions du fichier m'a permis de laisser de côté les `.js` et `.jsx` à la fin de mes fichiers lors de leur importation.

>> Enfin, mon serveur de développement était sur le port 3001. Ce port aurait pu être un autre de mon choix.

> Je viens de remarquer que la beauté implique du travail acharné…

J'ai ajouté Webpack au projet le dimanche, et ensuite le plugin a fonctionné !

Avec cela, j'ai pu créer un module qui pouvait être facilement exporté. Ce module était **ReactFCCtest**.

Je ne peux pas dire à quel point la méthodologie **read-search-ask** m'a aidé tout au long du projet.

Voici une [démo](https://usheninte.github.io/react-fcctest/) du plugin terminé. Ce fut très amusant à construire.

Je l'ai testé dans un projet freeCodeCamp, et il a fonctionné parfaitement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OL4Q9xvDLtsMcgY21--tOQ.gif)
_Crédit : [https://giphy.com](https://giphy.com/" rel="noopener" target="_blank" title=")_

J'ai créé un [dépôt Github](https://github.com/Usheninte/react-fcctest) qui contient tout le code open source du projet.

### **Comment installer et utiliser `react-fcctest`**

Exécutez `npm i react-fcctest` ou `yarn add react-fcctest` pour installer le plugin React.

Placez `import ReactFCCtest from 'react-fcctest';` dans votre App.js :

```js
import React, { Component } from 'react';
import ReactFCCtest from 'react-fcctest';

class App extends Component {
  render() {
    return (
      <div>
        <ReactFCCtest />
      </div>
    );
  }
};

export default App;
```

C'est tout ce qu'il y a à faire !

#### Notes finales

Mon année 2018 jusqu'à présent a été amazing.

Je suis maintenant le Developer Student Club Lead pour mon université, dans un programme soutenu par **Google Developers** en Afrique subsaharienne.

Je vise la grandeur, dans l'espace extra-atmosphérique — peut-être que je pourrais atterrir sur une lune. [Suivez-moi](https://twitter.com/Usheninte) dans mon voyage.
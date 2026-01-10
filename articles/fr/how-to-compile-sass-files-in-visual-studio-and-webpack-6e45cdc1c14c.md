---
title: Comment compiler des fichiers Sass dans Visual Studio et Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-07T16:38:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-compile-sass-files-in-visual-studio-and-webpack-6e45cdc1c14c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-rQU7AOJC3p-ZbiEQnYYlw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Sass
  slug: sass
- name: 'tech '
  slug: tech
- name: visual studio
  slug: visual-studio
- name: webpack
  slug: webpack
seo_title: Comment compiler des fichiers Sass dans Visual Studio et Webpack
seo_desc: 'By Esau Silva

  Sass is a very popular CSS pre-processor. The intent of this tutorial is to show
  you how to compile Sass files within Visual Studio using Webpack. Our discussion
  will include minification and autoprefixing for production.


  Visual Studio...'
---

Par Esau Silva

Sass est un pré-processeur CSS très populaire. L'objectif de ce tutoriel est de vous montrer comment compiler des fichiers Sass dans Visual Studio en utilisant Webpack. Notre discussion inclura la minification et l'autopréfixage pour la production.

![Image](https://cdn-media-1.freecodecamp.org/images/3k12b5dvlT4iN20sLPdB9W064Z6R7tSYIuX7)
_Visual Studio rencontre Sass_

Bien sûr, il existe des plug-ins dans le Visual Studio Marketplace, et il peut être agréable d'installer un plug-in et d'oublier la configuration. Mais que se passe-t-il si le plug-in n'est plus supporté et cesse de fonctionner avec les nouvelles versions de Visual Studio ? Eh bien, trop tard. C'est le cas de l'un des plug-ins de compilation les plus populaires sur le marché.

En configurant la compilation vous-même, vous aurez un contrôle total sur la sortie. De plus, les préfixes vendeurs seront ajoutés automatiquement à vos règles CSS. N'est-ce pas génial ?

#### Prérequis

Vous devrez avoir Node installé, et vous pouvez le télécharger [ici](https://nodejs.org/en/). C'est tout. Vous aurez également besoin de npm, mais il sera également installé avec Node.

### Création du Projet

**Note :** Nous allons créer une application .NET Core MVC, mais les mêmes principes s'appliquent à toute application ASP.NET MVC. Vous devrez simplement modifier légèrement la configuration Webpack pour sortir le fichier CSS dans le répertoire `Content`.

Ouvrez Visual Studio et créez une nouvelle **application Web ASP.NET Core**, puis sélectionnez **Application Web (Modèle-Vue-Contrôleur)**. Je nomme mon projet _netcore-sass-webpack_.

![Image](https://cdn-media-1.freecodecamp.org/images/aiZk0QmUZvH0pLbYz4NJQDjsubLYGjSu3D7S)
_Création du projet_

Créez un dossier `Styles` à la racine du projet. À l'intérieur, créez un fichier Sass et nommez-le `site.scss`. Ouvrez ce nouveau fichier Sass et copiez ce qui suit :

```css
/* Veuillez consulter la documentation à l'adresse https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification\ 
pour plus de détails sur la configuration de ce projet pour regrouper et minifier les actifs web statiques. */
body {
    padding-top: 50px;
    padding-bottom: 20px;
    background: #D69655 url('../wwwroot/images/pattern.png') repeat;
}

/* Élément d'enveloppement */
/* Définir un padding de base pour éviter que le contenu ne touche les bords */
.body-content {
    padding-left: 15px;
    padding-right: 15px;
}

/* Carousel */
.carousel-caption p {
    font-size: 20px;
    line-height: 1.4;
}

/* Faire en sorte que les fichiers .svg dans le carousel s'affichent correctement dans les anciens navigateurs */
.carousel-inner .item img[src$=".svg"] {
    width: 100%;
}

/* Générateur de code QR */
#qrCode {
    margin: 15px;
}

/* Masquer/réorganiser pour les petits écrans */
@media screen and (max-width: 767px) {
    /* Masquer les légendes */
    .carousel-caption {
        display: none;
    }
}
```

Vous remarquerez que c'est le même CSS fourni par Visual Studio lors de la création du projet, à l'exception de la règle `background` dans la balise `body`. Maintenant, supprimez le CSS fourni sous `wwwroot/css` (les deux fichiers : `site.css` et `site.min.css`). Ne vous inquiétez pas, nous allons les générer automatiquement avec Webpack.

Maintenant, téléchargez [pattern.png](https://github.com/esausilva/netcore-sass-webpack/tree/master/netcore-sass-webpack/wwwroot/images) et placez-le sous `wwwroot/images`.

Créez un fichier JavaScript vide à la racine de l'application et nommez-le `webpack.config.js`. Nous nous en occuperons plus tard. Vous devriez obtenir la structure de projet suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/jLrFCNq5AeHVD47jJDIveoOzJgDw6zkryxt3)
_Structure du projet_

**Note :** Vous n'avez pas besoin de faire les deux étapes suivantes pour chaque projet, seulement une fois (sauf si vous désinstallez et réinstallez Visual Studio).

Vous devrez fournir à Visual Studio le chemin d'installation de Node. Retournez à votre projet et sélectionnez **Outils -> Options** dans le panneau de gauche **Projets et Solutions -> Gestion des packages Web** et ajoutez le chemin d'installation de Node en haut de la liste (C:\Program Files\nodejs ou C:\Program Files (x86)\nodejs, selon que vous avez installé la version x64 ou x86).

![Image](https://cdn-media-1.freecodecamp.org/images/J8sJYylsXyYm2gZ2V3Nma4bvABRfJdefnldJ)
_Chemin de Node_

Enfin, téléchargez [NPM Task Runner](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.NPMTaskRunner) et installez-le — mais vous devrez d'abord fermer Visual Studio.

### Webpack et les dépendances NPM

Ouvrez **l'invite de commandes** et naviguez jusqu'à la racine du projet et installez les dépendances nécessaires :

```
cd netcore-sass-webpack\netcore-sass-webpack
npm init -y
npm i -D webpack webpack-cli node-sass postcss-loader postcss-preset-env sass-loader css-loader cssnano mini-css-extract-plugin cross-env file-loader
```

La première commande `npm` initialise votre `package.json` et la seconde installe vos dépendances.

* **webpack, webpack-cli** — Bundler de modules
* **node-sass** — Liaisons pour Node à LibSass ; fournit un support pour Sass
* **postcss-loader, postcss-preset-env** — Chargeur PostCSS pour Webpack pour traiter l'autopréfixage et la minification
* **sass-loader, css-loader** — Webpack a besoin de chargeurs spécifiques pour supporter Sass et CSS
* **cssnano** — Minificateur CSS
* **mini-css-extract-plugin** — Extrait le CSS dans un fichier séparé
* **cross-env** — Fournit un support aux utilisateurs Windows pour les variables d'environnement. Nous utiliserons la variable d'environnement NODE_ENV
* **file-loader** — Fournit un support pour les fichiers (images) dans nos règles CSS

À ce stade, vous pouvez rouvrir le projet dans Visual Studio. Après que le projet ait fini de charger, ouvrez `package.json` et ajoutez les scripts suivants :

```js
"scripts": {
    "dev": "webpack --watch",
    "build": "cross-env NODE_ENV=production webpack"
  },
```

* **dev** — Nous allons lier ce script chaque fois que le projet s'ouvre, et Webpack surveillera continuellement les changements dans les fichiers Sass sources, les compilera et sortira le fichier CSS séparé
* **build** — Nous allons lier ce script avant chaque build du projet et cela produira le fichier CSS de production, incluant la minification et l'autopréfixage

**Note :** Les scripts NPM s'exécuteront automatiquement en utilisant la fenêtre **Task Runner**. Plus d'informations à ce sujet plus tard.

Il est temps de travailler sur notre configuration Webpack. Ouvrez `webpack.config.js` et copiez ce qui suit :

```js
const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const postcssPresetEnv = require("postcss-preset-env");
// Nous obtenons 'process.env.NODE_ENV' des scripts NPM
// Vous vous souvenez du script 'dev' ?
const devMode = process.env.NODE_ENV !== "production";
module.exports = {
  // Indique à Webpack quelles optimisations intégrées utiliser
  // Si vous omettez cela, Webpack utilisera par défaut 'production'
  mode: devMode ? "development" : "production",
// Webpack doit savoir où commencer le processus de bundling,
  // nous définissons donc le fichier Sass sous le répertoire './Styles'
  entry: ["./Styles/site.scss"],
// C'est ici que nous définissons le chemin où Webpack placera
  // un fichier JS bundlé. Webpack doit produire ce fichier,
  // mais pour nos besoins, vous pouvez l'ignorer
  output: {
    path: path.resolve(__dirname, "wwwroot"),
// Spécifiez le chemin de base pour tous les styles dans votre
    // application. Cela est relatif au chemin de sortie, donc dans
    // notre cas, ce sera './wwwroot/css'
    publicPath: "/css",
// Le nom du bundle de sortie. Le chemin est également relatif
    // au chemin de sortie, donc './wwwroot/js'
    filename: "js/sass.js"
  },
  module: {
    // Tableau de règles qui indique à Webpack comment les modules (sortie)
    // seront créés
    rules: [
      {
        // Recherche les fichiers Sass et les traite selon les
        // règles spécifiées dans les différents chargeurs
        test: /\.(sa|sc)ss$/,
// Utilise les chargeurs suivants de droite à gauche, donc il utilisera
        // sass-loader en premier et se terminera avec MiniCssExtractPlugin
        use: [
          {
            // Extrait le CSS dans un fichier séparé et utilise
            // les configurations définies dans la section 'plugins'
            loader: MiniCssExtractPlugin.loader
          },
          {
            // Interprète le CSS
            loader: "css-loader",
            options: {
              importLoaders: 2
            }
          },
          {
            // Utilise PostCSS pour minifier et autopréfixer avec les règles vendeurs
            // pour la compatibilité avec les anciens navigateurs
            loader: "postcss-loader",
            options: {
              ident: "postcss",
// Nous instruisons PostCSS à autopréfixer et minimiser notre
              // CSS en mode production, sinon ne rien faire.
              plugins: devMode
                ? () => []
                : () => [
                    postcssPresetEnv({
                      // Compile notre code CSS pour supporter les navigateurs
                      // qui sont utilisés dans plus de 1 % de la
                      // part de marché mondiale des navigateurs. Vous pouvez modifier
                      // les navigateurs cibles selon vos besoins
                      // en utilisant des requêtes supportées.
                      // https://github.com/browserslist/browserslist#queries
                      browsers: [">1%"]
                    }),
                    require("cssnano")()
                  ]
            }
          },
          {
            // Ajoute un support pour les fichiers Sass, si vous utilisez Less, alors
            // utilisez le less-loader
            loader: "sass-loader"
          }
        ]
      },
      {
        // Ajoute un support pour charger les images dans vos règles CSS. Il recherche
        // .png, .jpg, .jpeg et .gif
        test: /\.(png|jpe?g|gif)$/,
        use: [
          {
            loader: "file-loader",
            options: {
              // L'image sera nommée avec le nom et l'extension d'origine
              name: "[name].[ext]",
// Indique où les images sont stockées et utilisera
              // ce chemin lors de la génération des fichiers CSS.
              // Par exemple, dans site.scss j'ai
              // url('../wwwroot/images/pattern.png') et lors de la génération
              // du fichier CSS, file-loader sortira
              // url(../images/pattern.png), qui est relatif
              // à '/css/site.css'
              publicPath: "../images",
// Lorsque cette option est 'true', le chargeur émettra l'
              // image vers output.path
              emitFile: false
            }
          }
        ]
      }
    ]
  },
  plugins: [
    // Options de configuration pour MiniCssExtractPlugin. Ici, je n'indique que
    // le nom du fichier de sortie CSS et
    // l'emplacement
    new MiniCssExtractPlugin({
      filename: devMode ? "css/site.css" : "css/site.min.css"
    })
  ]
};
```

Veuillez vous référer aux commentaires dans le code pour comprendre la configuration. (Fichier plus lisible [ici](https://github.com/esausilva/netcore-sass-webpack/blob/master/netcore-sass-webpack/webpack.config.js).)

Maintenant, nous devons créer quelques liaisons dans **Task Runner Explorer**. Naviguez vers **Affichage -> Autres fenêtres -> Task Runner Explorer**. La fenêtre s'affichera en bas et vous verrez les scripts que vous avez créés dans `package.json` listés là **sous** Custom. Vous verrez également certaines tâches **sous Défauts**, mais vous pouvez simplement les ignorer.

Nous avons besoin de deux liaisons :

* Cliquez avec le bouton droit sur **build -> Liaisons -> Avant** la construction — Visual Studio exécutera cette tâche avant chaque construction. Rappelez-vous que ce script npm exécute Webpack pour la production et optimisera le fichier CSS.
* Cliquez avec le bouton droit sur **dev -> Liaisons -> Ouverture** du projet — Visual Studio exécutera cette tâche lorsque vous ouvrirez le projet. Rappelez-vous que ce script npm exécute Webpack en mode surveillance et _surveillera_ tout changement dans vos fichiers Sass et sortira le fichier CSS traité.

**Task Runner Explorer** devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/cEQsi3RjNiBTTQr1tAhSoAARAmhkc79kQRza)
_Task Runner Explorer_

**Note :** Pour une raison quelconque, Visual Studio échoue parfois à démarrer la tâche **dev** lors de l'ouverture du projet. Si cela se produit, ouvrez simplement l'Explorateur de tâches et exécutez la tâche manuellement.

Vous pouvez obtenir le code complet depuis le [dépôt GitHub](https://github.com/esausilva/netcore-sass-webpack).

### Réflexions finales

Et c'est tout. Puisque vous avez déjà Visual Studio ouvert, aucune des tâches n'est en cours d'exécution. Allez-y et _cliquez avec le bouton droit_ sur la tâche **dev** et sélectionnez exécuter. Vous verrez la tâche se charger et, lorsqu'elle sera terminée, vous verrez qu'un fichier `site.css` a été créé dans le répertoire `wwwroot/css`. Ouvrez `site.scss`, faites une modification et enregistrez-la. Maintenant, ouvrez `site.css`, vous verrez votre modification reflétée là. Cool !!

Exécutez votre projet en appuyant sur **Ctrl + F5**, vous verrez un fichier `site.min.css` créé dans le répertoire `wwwroot/css`. Ce fichier a été créé lorsque Task Runner a _exécuté_ le script `build` avant de construire le projet.

Le site final devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/CBTg3rcS670jv5PSQzM35LZ9awQdUfzS2Nb3)
_Site final_

Je sais, je sais, l'arrière-plan est très kitsch… mais j'avais besoin d'une image pour montrer le `file-loader` de Webpack en action.

Avec cette configuration, vous pouvez même ajouter un support pour transpiler le JavaScript moderne (ES6+) en ES5. Regardez ces éléments : `@babel/core`, `babel-loader`, `@babel/preset-env`.

Merci d'avoir lu, et j'espère que vous avez apprécié. Si vous avez des questions, des suggestions ou des corrections, faites-le moi savoir dans les commentaires ci-dessous. N'oubliez pas de partager cet article, et vous pouvez me suivre sur [Twitter](https://twitter.com/_esausilva), [GitHub](https://github.com/esausilva/), [Medium](https://medium.com/@_esausilva), [LinkedIn](https://www.linkedin.com/in/esausilva/).

Vous pouvez également visiter mon site personnel de [blogging](https://esausilva.com).

---

**<ins>Mise à jour 25/08/19 :</ins>** J'ai été en train de construire une application web de prière appelée "**My Quiet Time - A Prayer Journal**". Si vous souhaitez rester informé, veuillez vous inscrire via le lien suivant : [http://b.link/mqt](http://b.link/mqt)  

L'application sera publiée avant la fin de l'année, j'ai de grands projets pour cette application. Pour voir quelques maquettes, suivez le lien suivant : [http://pc.cd/Lpy7](http://pc.cd/Lpy7)

Mes DM sur [Twitter](https://twitter.com/_esausilva) sont ouverts si vous avez des questions concernant l'application ?
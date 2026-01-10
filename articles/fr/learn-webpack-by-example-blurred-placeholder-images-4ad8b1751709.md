---
title: 'Apprendre Webpack par l''exemple : Images de remplacement floues'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-28T15:49:27.000Z'
originalURL: https://freecodecamp.org/news/learn-webpack-by-example-blurred-placeholder-images-4ad8b1751709
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h2X9ckg3FJr4FGSfwh0F2w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Apprendre Webpack par l''exemple : Images de remplacement floues'
seo_desc: 'By Kalalau Cantrell

  The repo that goes along with this post uses webpack 3. If you are interested in
  learning webpack 4, you will find this post useful as the concepts as well as the
  config file format is the same. Webpack 4 did introduce optimizatio...'
---

Par Kalalau Cantrell

***Le dépôt qui accompagne cet article utilise webpack 3. Si vous êtes intéressé par l'apprentissage de webpack 4, vous trouverez cet article utile car les concepts ainsi que le format du fichier de configuration sont les mêmes. Webpack 4 a introduit des optimisations, des capacités de configuration zéro, ainsi que de nouveaux plugins prêts à l'emploi qu'un utilisateur avancé voudrait connaître mais qui dépassent le cadre de cet article.***

Ce guide épisodique vous permettra d'apprendre webpack à travers divers exemples. Les débutants avec webpack sont les bienvenus. Je suis moi-même un débutant et j'essaierai d'expliquer les concepts de webpack de manière à ce qu'ils soient compréhensibles pour quelqu'un qui découvre l'outil.

Toutes les personnes qui maintiennent les packages utilisés dans ce guide méritent d'être reconnues pour avoir mis à disposition de la communauté des outils aussi géniaux. Puisque c'est le sujet de ce guide, un remerciement spécial va à [responsive-loader](https://github.com/herrstucki/responsive-loader/) et à [Jeremy Stucki](https://www.freecodecamp.org/news/learn-webpack-by-example-blurred-placeholder-images-4ad8b1751709/undefined) qui maintient le projet.

Dans cet épisode, nous allons examiner une technique pour charger des images. Cela inclut 1) l'inclusion de versions floues de remplacement de nos images lors du chargement initial de la page. Ensuite, 2) la demande des images complètes depuis le serveur. Enfin, 3) lorsque les images complètes sont enfin chargées, elles s'estompent et les remplacements flous sont supprimés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zxTkKZ-oMGJXO0l-_RQZxQ.gif align="left")

*Images de remplacement floues.*

Cette technique est idéale pour les appareils sur des connexions lentes. Elle donne aux utilisateurs une idée de ce à quoi la page ressemblera pendant les quelques secondes (pensez à un 3G lent) qu'il peut falloir pour que les images de la page se chargent complètement.

### Mise en route

Si vous souhaitez suivre dans votre éditeur de code, vous pouvez soit télécharger [ce dépôt](https://github.com/klcantrell/webpack-through-example-blog/tree/blur-up) ou faire un `git clone` et un `checkout` de la branche `blur-up` du dépôt si vous préférez.

Voici la structure de fichiers que vous devriez trouver lorsque vous ouvrez le dossier du projet.

```bash
/src
    /css
        main.css
    /imgs
        barret-wallace.jpg
        cloud-strife.jpg
        tifa-lockhart.jpg 
    /js
        index.js
        loadImages.js
    index.html
package.json
webpack.config.js
```

Nous allons utiliser webpack et spécifiquement **responsive-loader**. Nous allons redimensionner et générer des remplacements flous pour les trois images dans `src/imgs`. Ce sont, soit dit en passant, des personnages du jeu vidéo préféré de l'auteur de tous les temps.

Examinons maintenant notre code source en commençant par `index.html`. En cours de route, nous verrons ce que webpack fait pour nous et nous nous arrêterons pour en parler. Le code standard a été omis et remplacé par `<-- ... -->` pour plus de concision.

```xml
<!-- index.html -->
 
<!-- ... --> 
 
    <section class="characters">
        <a href="${require('./imgs/cloud-strife.jpg').src}"
            class="hero-pic replace">
            <img src="${require('./imgs/cloud-strife.jpg').placeholder}"
                class="hero-preview"
                alt="cloud strife">
        </a>
        <a href="${require('./imgs/tifa-lockhart.jpg').src}"
            class="hero-pic replace">
            <img src="${require('./imgs/tifa-lockhart.jpg').placeholder}"
                class="hero-preview"
                alt="tifa lockhart">
        </a>
        <a href="${require('./imgs/barret-wallace.jpg').src}"
            class="hero-pic replace">
            <img src="${require('./imgs/barret-wallace.jpg').placeholder}"
                class="hero-preview"
                alt="barret wallace">
        </a>
    </section>
 
<!-- ... -->
```

Vous avez probablement remarqué qu'il y a trois éléments `<a>`, un pour chacune de nos images. Mais qu'en est-il des littéraux de modèle ? Et qu'en est-il de la fonction `require` ? Ce sont les moyens par lesquels nous demandons à webpack de faire son travail.

Lorsque webpack analyse notre `HTML`, il rencontre les littéraux de modèle et sait qu'il doit y mettre quelque chose. La fonction `require` indique à webpack *quoi* y mettre – dans notre cas, nous y mettons des données d'image (il n'est peut-être pas encore clair quelles données nous y mettons, mais restez avec moi, nous y viendrons). Alors, comment webpack sait-il faire cela ? Est-ce automatique ?

Si vous n'avez jamais vu de fichier de configuration webpack auparavant, vous pourriez probablement deviner en jetant un coup d'œil qu'il n'est pas du tout automatique. Il existe de nombreuses options, certaines spécifiques à webpack et d'autres spécifiques à un chargeur ou un plugin particulier. Alors, qu'est-ce qu'un **chargeur** de toute façon ? Qu'est-ce qu'un **plugin** ?

### Définitions rapides

Avant de plonger dans la configuration, je vais fournir des définitions rapides de ces concepts webpack. Je fournirai également des liens vers la documentation qui les explique plus en détail.

* [**Chargeur**](https://webpack.js.org/concepts/#loaders) : Son travail consiste à prendre vos fichiers, à les transformer d'une certaine manière et à vous donner le résultat de cette transformation. Le résultat que vous obtenez dépend du type de fichier avec lequel vous travaillez et des capacités du chargeur. Pour utiliser un exemple de notre projet d'aujourd'hui, vous pouvez utiliser un chargeur pour prendre un fichier image, le transformer en données d'image, puis intégrer ces données dans votre `HTML`.
    
* [**Plugin**](https://webpack.js.org/concepts/#plugins) : Son travail consiste à accomplir des tâches plus générales que les chargeurs. Alors que les chargeurs appliquent des transformations spécifiques à des types de fichiers spécifiques. Les plugins, cependant, peuvent effectuer des tâches telles que la compression de fichiers, la minification de texte, et ainsi de suite. Pour utiliser un exemple de notre projet d'aujourd'hui, vous pouvez utiliser un plugin pour compresser des fichiers image.
    

### Traitement HTML

Examinons maintenant comment nous utilisons les chargeurs et les plugins pour gérer notre `HTML` spécifiquement. Voici les parties de notre `webpack.config.js` qui concernent le `HTML`. Les autres options dont nous parlerons éventuellement sont omises et remplacées par `// ...` :

```javascript

/* 
    webpack.config.js
    Options spécifiques au HTML
*/

// ...
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
// ...
    module: {
        rules: [
          {
            test: /\.html$/,
            use: {
              loader: 'html-loader',
              options: {
                interpolate: true
              }
            }
          }
        // ...
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
          template: 'src/index.html'
        }),
    // ...
    ]
}
```

Tout d'abord, nous importons le **html-webpack-plugin** et l'assignons à une variable nommée `HtmlWebpackPlugin` (créatif, n'est-ce pas ?). Le travail de ce plugin est de générer le fichier `HTML` que nous utiliserons en distribution. Pour initier le plugin, nous utilisons l'opérateur `new` sur notre variable dans la propriété `plugins` de notre objet de configuration. L'objet de configuration auquel je fais référence est celui assigné à `module.exports`, et c'est ce qui "dit" à webpack quoi faire.

**html-webpack-plugin** générerait un `HTML` de base assez générique sans aucune option passée. Mais, remarquez que nous avons défini sa propriété `template` égale à notre fichier source `index.html`. Comme vous pouvez le deviner, cela signifie que nous demandons au plugin d'utiliser notre `index.html` comme modèle lorsqu'il génère un fichier `HTML` pour nous. Super, mais pourquoi passer par tout ce trouble, demandez-vous ?

C'est parce que nous voulons utiliser des chargeurs pour transformer notre source `HTML`. Nous voulons transformer ceci :

```javascript
<!-- ... -->
 
<a href="${require('./imgs/cloud-strife.jpg').src}"
    class="hero-pic replace">
    <img src="${require('./imgs/cloud-strife.jpg').placeholder}"
        class="hero-preview"
        alt="cloud strife">
</a>
 
<!-- ... -->
```

en ceci :

```xml
<!-- ... -->

<!-- données d'image tronquées pour plus de concision -->
<a href="imgs/cloud-strife-300.jpg"
   class="hero-pic replace">
    <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/
            2wCEAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhw
            XExQaFRERGCEYGh0dHx8fExciJCIeJBweHx4BBQUFBwYHDggIDh4U
            ERQeHh4eHh4e..."
        class="hero-preview"
        alt="cloud strife">
</a>
 
<!-- ... -->
```

Remarquez que les littéraux de modèle et les fonctions `require` ont été remplacés. Maintenant, l'attribut `a.href` a une URL vers une version redimensionnée de notre image, de `300px` de large. De plus, l'attribut `img.src` a maintenant des données d'image en ligne. J'ai montré la transformation de notre `HTML` pour un élément `<a>`, mais c'est ce que nous voulons que tous les éléments ressemblent.

Examinons comment nous utilisons les chargeurs pour accomplir cette transformation. Zooms sur le bloc de code de notre `webpack.config.js` qui commence par la paire clé-valeur `test: /\.html$/`.

```bash
{
  test: /\.html$/,
  use: {
    loader: 'html-loader',
    options: {
     interpolate: true
    }
  }
}
```

Ce bloc dit, "Hey webpack, lorsque vous rencontrez des fichiers `HTML`, veuillez utiliser **html-loader** et assurez-vous qu'il est configuré pour permettre l'interpolation".

En d'autres termes, nous `testons` l'extension "html". Nous `utilisons` **html-loader** comme `loader` pour ce type de fichier, puis nous spécifions dans `options` que nous aimerions utiliser la fonction `interpolate` de **html-loader**.

Si vous regardez la [documentation](https://github.com/webpack-contrib/html-loader) de **html-loader**, vous verrez que lorsque `interpolate` est défini sur `true`, vous pouvez intégrer le résultat de quelque JavaScript `(JS)` directement dans notre `HTML`. Dans notre cas, nous en profitons en appelant la fonction `require` pour dire à webpack d'importer des ressources d'image. Mais comment webpack sait-il quoi faire avec les images ?

### Traitement des images

Nous devons lui dire quels chargeurs et plugins utiliser. Voici la partie de notre fichier `webpack.config.js` qui indique à webpack quoi faire avec les images.

```javascript
/* 
    webpack.config.js
    Options spécifiques aux images
*/
 
// ...
const ImageminPlugin = require('imagemin-webpack-plugin').default;
// ...
 
module.exports = {
// ...
    module: {
        rules: [
        // ...
          {
            test: /\.(png|jpg|gif)$/,
            use: {
              loader: 'responsive-loader',
              options: {
                sizes: [300],
                placeholder: true,
                placeholderSize: 50,
                name: 'imgs/[name]-[width].[ext]'
              }
            }
          }
        // ...
        ]
    },
    plugins: [
    // ...
        new ImageminPlugin({test: /\.(png|jpg|gif)$/})
    ]
}
```

Le **imagemin-webpack-plugin** que nous utilisons a un travail assez simple — il compresse simplement nos images. Vous pouvez en lire plus à ce sujet [ici](https://www.npmjs.com/package/imagemin-webpack-plugin), mais ce qui est plus intéressant, c'est le chargeur que nous utilisons pour transformer nos images. Regardez le bloc de code qui commence par la paire clé-valeur `test: /\.(png|jpg|gif)$/`.

Ce bloc dit, "Hey webpack, lorsque vous rencontrez des fichiers image, utilisez **responsive-loader**. Générez une version redimensionnée de l'image à `300px` de large. Et pendant que vous y êtes, créez des données pour une image de remplacement floue qui fait `50px` de large".

[En](https://www.npmjs.com/package/imagemin-webpack-plugin) d'autres termes, nous `testons` les extensions "png" ou "jpg" ou "gif". Nous `utilisons` **responsive-loader** comme `loader` pour ces types de fichiers. Ensuite, nous spécifions dans `options` que nous aimerions utiliser les fonctionnalités `resize`, `placeholder` et `name` de **responsive-loader** pour transformer nos images.

Examinons en détail ce que **responsive-loader** fait pour nous avec ces options. Lorsque nous disons :

```bash
require('./imgs/cloud-strife.jpg');
```

Alors **responsive-loader** nous donne ceci en retour :

```bash
{
    placeholder: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx4BBQUFBwYHDggIDh4UERQeHh4eHh4eHh4eHh4eHh4eHh4e....",
                  /* le reste des données a été omis pour plus de concision */
    src: "imgs/cloud-strife-300.jpg", // chemin vers l'image redimensionnée
    srcSet: "imgs/cloud-strife-300.jpg 300w" // plus d'informations à ce sujet dans un futur épisode
 
    // ... il y a d'autres propriétés mais je laisse cela à la curiosité du lecteur
}
```

C'est juste un objet `JS`. Et c'est pourquoi nous pouvons utiliser `.src` et `.placeholder` pour accéder à ce dont nous avons besoin depuis nos instructions `require` afin que lorsque nous faisons ceci :

```xml
<img src="${require('./imgs/cloud-strife.jpg').placeholder}"
     class="hero-preview" 
     alt="cloud-strife">
```

webpack nous donne ceci :

```xml
<!-- données d'image tronquées pour plus de concision -->
<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/
          2wCEAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhw
          XExQaFRERGCEYGh0dHx8fExciJCIeJBweHx4BBQUFBwYHDggIDh4U
          ERQeHh4eHh4e..."
     class="hero-preview"
     alt="cloud strife">
```

### Récapitulatif rapide

Super, nous avons donc un flux de travail pour traiter notre `HTML` et nos images. Pour récapituler :

Pour le `HTML`, nous utilisons le **html-webpack-plugin** pour générer un fichier `HTML` en utilisant notre `index.html` source comme modèle. Nous utilisons **html-loader** pour traiter notre `HTML` et spécifiquement permettre l'interpolation. L'interpolation nous permet d'utiliser des instructions `require` dans notre `HTML` afin que nous puissions demander à webpack de charger des images d'une certaine manière.

Pour les images, nous utilisons **responsive-loader** pour générer des versions redimensionnées de nos images. Il génère ensuite des données d'image pour des versions floues de remplacement de nos images que nous pouvons utiliser en ligne.

Une fois notre code transformé avec ces chargeurs, les chemins d'image et les données d'image sont intégrés dans notre `HTML`. Bien !

### Feuille de style en cascade (CSS) et JavaScript (JS) source

Examinons le reste de notre code source. Voir les commentaires de code pour les explications sur la façon dont nous utilisons `JS` et `CSS` pour estomper l'image complète une fois qu'elle est chargée, puis supprimer l'image de remplacement.

#### CSS :

```css
/*  main.css  */
 
body {
    background: black;
}
 
/* alignement général */
.characters {
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
}
 
/* élément parent */
.hero-pic {
    display: block;
    flex-shrink: 0;
    width: 300px;
    height: 240px;
    position: relative;
    overflow: hidden;
    margin: 5px;
    border-radius: 10px;
    box-shadow: 0px 0px 139px -5px rgba(138,178,209,0.78);
}
 
/* image de remplacement */
.hero-preview {
    width: 100%;
    position: absolute;
    left: 0;
    right: 0;
}
 
/* supprime le curseur de pointeur sur les éléments <a>
   une fois l'image complète chargée */
.hero-pic:not(.replace) {
    cursor: default;
}
 
/* estompe et positionne l'élément d'image complète
   une fois qu'il est chargé */
.reveal {
    position: absolute;
    left: 0;
    right: 0;
    will-change: opacity;
    animation: reveal 1s ease-out;
}
 
/* animation pour l'estompage */
@keyframes reveal {
    0% { opacity: 0; }
    100% { opacity: 1; }
}
```

#### JS :

```javascript
/*  loadImages.js  */
 
function loadFullImages() {
    let imageEls = [].slice.call(document.querySelectorAll('.hero-pic'));
    imageEls.forEach((imageEl) => {
        loadFullImage(imageEl);
    });
 
    /* crée l'élément image et configure un rappel pour l'ajouter
       à la page une fois qu'il est chargé */
    function loadFullImage(item) {
        const img = new Image();
        img.src = item.href;
        img.className = 'reveal';
        if (img.complete) {
            phaseInImg(item, img);
        } else {
            img.addEventListener('load', function fullImageLoaded() {
                phaseInImg(item, img);
                img.removeEventListener('load', fullImageLoaded);
            })
        }
    }
 
    /* ajoute l'élément image complet à la page, supprime l'élément de remplacement */
    function phaseInImg(item, img) {
        removePreviewFeatures(item);
        item
            .appendChild(img)
            .addEventListener('animationend', function phaseOutPreview(e) {
                let previewImage = item.querySelector('.hero-preview');
                item.removeChild(previewImage);
                e.target.classList.remove('reveal');
                e.target.removeEventListener('animationend', phaseOutPreview);
            })
    }
 
    /* supprime le comportement par défaut d'un élément <a> */
    function removePreviewFeatures(item) {
        item.classList.remove('replace');
        item.addEventListener('click', function(e) {
            e.preventDefault();
        })
    }
}
```

### Chargement du CSS et du JS

Voici à quoi ressemble notre `index.js`. Ce fichier est l'endroit où nous disons à webpack d'importer tous les modules que nous voulons utiliser, puis de les utiliser. Un [**module**](https://webpack.js.org/concepts/modules/) en termes simples est simplement un morceau de code d'un autre fichier que nous voulons importer et utiliser.

[À l'intérieur](https://webpack.js.org/concepts/modules/) d'un fichier `JS`, nous pouvons utiliser la syntaxe `import` ES2015 au lieu de `require` pour importer des modules. Par exemple, notez que `import loadFullImages from './loadImages'` fait la même chose que `const loadFullImages = require('./loadImages')`.

```javascript

/*  index.js  */
     
import mainStyles from '../css/main.css';
import loadFullImages from './loadImages';
 
window.addEventListener('load', function onWindowLoad() {
    loadFullImages();
});
```

Dans notre cas, nous avons simplement deux modules. Remarquez que les modules dans webpack ne sont pas restreints au `JS` — nous pouvons traiter les fichiers `CSS` comme des modules également, si nous utilisons les bons chargeurs. C'est puissant mais peut être déroutant au début. Une fois que je vous aurai expliqué comment webpack charge notre fichier `CSS`, cependant, vous verrez que tout ce que nous faisons est de minifier notre `CSS` source et de générer un fichier `main.css` :

```javascript
/* 
    webpack.config.js
    Options spécifiques au CSS
*/
 
// ...
 
module.exports = {
// ...
    module: {
        rules: [
        // ...
          {
            test: /\.css$/,
            use: [
              {
                loader: 'file-loader',
                options: {
                  name: '[name].[ext]'
                }
              },
              'extract-loader',
              {
                loader: 'css-loader',
                options: {
                  minimize: true
                }
              }
            ]
          }
        // ...
        ]
    }
// ...
}
```

Dans le bloc d'options ci-dessus, notez que nous pouvons spécifier plusieurs chargeurs dans la propriété `use` en passant un tableau d'objets chargeurs. Le fichier est ensuite traité par chacun des chargeurs en commençant par le dernier chargeur du tableau et en terminant par le premier.

Ce bloc dit essentiellement, "Hey webpack, lorsque vous rencontrez des fichiers `CSS`, veuillez utiliser **css-loader** pour importer le `CSS` et le minifier. Ensuite, utilisez **extract-loader** pour le séparer de l'inclusion dans notre `JS` (plus d'informations à ce sujet [ici](https://webpack.js.org/loaders/extract-loader/)). Ensuite, utilisez **file-loader** pour créer un fichier pour nous avec le nom et l'extension du fichier source [original](https://webpack.js.org/loaders/extract-loader/) (dans notre cas, il le nomme "main.css").

Voici comment nous disons à webpack de charger notre JS :

```javascript
/* 
    webpack.config.js
    Options spécifiques au JS
*/
 
// ...
 
module.exports = {
// ...
    module: {
        rules: [
            {
              test: /\.js$/,
              exclude: /node_modules/,
              use: {
                loader: 'babel-loader',
                options: {
                  presets: [
                    ['env', { 
                        modules: false,
                    }]
                  ]
                }
              }
            }
        // ...
        ]
    }
// ...
}
```

Ce que ce bloc dit essentiellement, c'est, "Hey webpack, lorsque vous rencontrez des fichiers [`JS`](https://webpack.js.org/loaders/extract-loader/), veuillez utiliser **babel-loader** et son preset **env** pour compiler notre `JS`. Babel prend notre `JS` source écrit en syntaxe ES2015+ et le compile en ES5 compatible avec les navigateurs. L'option `modules: false` indique à Babel de ne pas se soucier de la transformation de notre syntaxe `import`. Webpack s'en charge déjà.

### La construction

Si vous souhaitez voir webpack générer les fichiers de distribution, allez-y et installez [Node.js](https://nodejs.org/) qui vient avec [npm](https://www.npmjs.com/) si vous ne les avez pas encore installés. Ouvrez une console de ligne de commande et `cd` dans le répertoire du projet. Si vous êtes sous Windows et avez besoin d'un shell compatible *NIX, utilisez Windows Powershell plutôt que l'invite de commande par défaut.

Une fois que vous êtes dans le répertoire du projet, exécutez la commande `npm install` pour installer tous les packages dont nous avons parlé dans ce guide. Ensuite, exécutez la commande `npm start` pour exécuter la construction. Voici la dernière partie de la configuration webpack que nous devons encore passer en revue. C'est ainsi que webpack sait où envoyer les fichiers de distribution :

```javascript
/* 
    webpack.config.js
*/
 
// ...
const path = require('path');
 
module.exports = {
    entry: {
        app: path.join(__dirname, 'src/js/index.js')
    },
    output: {
        path: path.join(__dirname, 'dist'),
        filename: "[name].bundle.js"
    }
// ...
}
```

`path` est un module utilitaire. Il nous permet de construire facilement des chemins de fichiers et de répertoires compatibles avec les plateformes. Ceux-ci fonctionneront que votre système de fichiers de plateforme utilise '/' ou '\' comme séparateurs de chemin. Ici, nous utilisons la fonction `path.join` pour dire à webpack où trouver et envoyer nos fichiers.

`entry` indique à webpack quel module est le module "principal", celui dans lequel nous importons tous les autres modules dont nous dépendons. `app` est le nom que nous avons donné au bundle principal que webpack créera en assemblant tous nos modules.

Enfin, `output.path` indique à webpack où envoyer tous les fichiers qu'il crée pour nous. Le `output.filename` indique à webpack quel schéma de nommage utiliser pour les bundles qu'il crée. Dans notre cas, nous créons simplement un bundle et il sortira nommé "app.bundle.js".

### Conclusion

J'espère que vous avez pu apprendre un peu plus sur la façon dont webpack peut vous aider à construire des choses à travers cet exemple. J'espère également que vous avez retenu quelque chose de la lecture de cet article. Par exemple, une technique de chargement d'images, une façon d'écrire du `JS` modulaire, ou même simplement de la pratique à lire le code de quelqu'un d'autre. Enfin, j'espère que vous avez pu exécuter le code résultant dans un navigateur et le voir en action. Merci d'avoir lu !

**Applaudissez si cela vous a aidé à apprendre quelque chose, commentez ci-dessous avec vos questions, et dites bonjour à [moi](https://twitter.com/kalalaucantrell) et merci à [Jeremy Stucki](https://twitter.com/herrstucki) sur Twitter.**
---
title: Comment maîtriser Webpack 4 et créer une application React géniale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T05:27:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-conquer-webpack-4-and-build-a-sweet-react-app-236d721e6745
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VuWmde9oMOIIIHjaRj1vDA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment maîtriser Webpack 4 et créer une application React géniale
seo_desc: 'By Adeel Imran


  This article has been outdated with the new release for babel, kindly check the
  updated article “How to combine Webpack 4 and Babel 7 to create a fantastic React
  app”, last updated October 13th, 2018


  In this article, I’ll go through ...'
---

Par Adeel Imran

> Cet article est obsolète avec la nouvelle version de Babel, veuillez consulter l'article mis à jour « [Comment combiner Webpack 4 et Babel 7 pour créer une application React fantastique](https://www.freecodecamp.org/news/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff/) », dernière mise à jour le 13 octobre 2018

Dans cet article, je vais expliquer comment configurer une application React en utilisant Webpack 4. À la fin de ce tutoriel, vous saurez comment recharger à chaud votre application chaque fois que vous appuyez sur `**ctrl + s**` dans votre éditeur de choix.

J'utilise [Visual Studio Code](https://code.visualstudio.com/) (VS Code), et je l'adore. Il est léger, flexible, et le meilleur, c'est qu'il est gratuit. J'adore le gratuit. Si vous ne l'avez pas encore essayé, donnez-lui une chance.

### Notre objectif

Notre objectif pour ce tutoriel est de créer une application [React](https://reactjs.org/), avec des fonctionnalités sympas comme async/await. Je n'utiliserai pas [react-router version 4](https://reacttraining.com/react-router/web) dans ce tutoriel, car je veux principalement me concentrer sur comment jouer avec Webpack.

Ainsi, à la fin de cet article, vous serez bon en :

* Configuration d'un environnement de développement, avec rechargement à chaud en utilisant [webpack-dev-server](https://github.com/webpack/webpack-dev-server)
* Ajout de la prise en charge de SCSS et HTML dans votre code avec webpack
* Ajout de la prise en charge des fonctionnalités comme try/catch, async/await et l'opérateur rest
* Création d'une version de production — optimisée et prête pour le déploiement
* Configuration de différents environnements dans votre code comme stage, demo et production

Les gars, je vous dis que si Webpack semble un peu difficile, après ce tutoriel, ce ne sera plus le cas.

### Environnement de développement

#### Créer le dossier

Créez un dossier appelé `tutorial` dans votre répertoire.

#### Créer package.json

Ouvrez votre terminal et allez dans le dossier `tutorial`.

Tapez :

```
npm init -y
```

Cela créera un fichier `**package.json**` dans votre dossier `tutorial`.

Le fichier ressemblera à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wZFOOk5M8Hm-Jal__d_tzA.png)
_C'est à quoi votre fichier package.json ressemblera initialement. J'utilise VS Code pour ce tutoriel_

#### Créer le fichier index.js

Je vais créer un dossier appelé `**src**` dans mon dossier `**tutorial**`.

Dans le dossier `**src**`, je vais créer un fichier appelé `**index.js**`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xf-2jlOilNxVpftvnh8ltg.png)
_et oui, j'utiliserai beaucoup de citations de Star Trek pendant ce tutoriel parce que C'EST GÉNIAL :D_

#### Bundler le code

Je sais que ce n'est pas grand-chose, mais restez avec moi. Les choses vont devenir intéressantes très bientôt.

Maintenant, afin de bundler notre code, nous devons configurer certaines choses pour que Webpack sache où bundler le code. Pour cela, nous devons installer quelques dépendances.

Alors commençons par taper :

```
npm i --save-dev webpack webpack-cli webpack-dev-server @babel/core @babel/preset-env @babel/preset-react @babel/preset-stage-2 babel-loader@^8.0.0-beta
```

WOW ! Je sais que c'était beaucoup de dépendances. Faisons un récapitulatif de pourquoi nous en avions besoin en premier lieu.

[webpack](http://webpack.js.org) : Nous avons besoin de Webpack pour bundler notre code.

[webpack-cli](https://github.com/webpack/webpack-cli) : Nous utiliserons certaines fonctionnalités CLI pour Webpack afin de faciliter l'écriture de scripts.

[webpack-dev-server](https://github.com/webpack/webpack-dev-server) : Je vais créer un serveur en utilisant le package webpack-dev-server. Cela n'est destiné qu'à être utilisé dans l'environnement de développement, et non pour la production. Cela signifie que pendant le développement et le travail sur mon code, je n'ai pas besoin d'un serveur séparé comme Node.js.

[@babel/preset-env](https://github.com/babel/babel/tree/master/packages/babel-preset-env) : Ce package se comporte exactement comme @babel/preset-latest (ou @babel/preset-es2015, @babel/preset-es2016, et @babel/preset-es2017 ensemble). Cool, non ?

[@babel/preset-react](https://github.com/babel/babel/tree/master/packages/babel-preset-react) : Le nom du package est clair — cela ajoutera la prise en charge de React lors du bundling de notre code.

[@babel/preset-stage-2](https://babeljs.io/docs/plugins/preset-stage-2/) : Cela ajoutera les fonctionnalités de stage-2 de la proposition [Ecma TC39](https://github.com/tc39). Vous pouvez en lire plus à ce sujet [ici](https://babeljs.io/docs/plugins/preset-stage-2/).

[@babel/loader](https://github.com/babel/babel-loader) : C'est une dépendance de Webpack. Il permet de transpiler Babel en utilisant Webpack.

[@babel/core](https://github.com/babel/babel/tree/master/packages/babel-core) : C'est une dépendance pour le @babel/loader lui-même.

Maintenant, vous en savez un peu plus sur ce que nous avons installé et pourquoi.

Votre fichier `package.json` devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zABxZp43O89ynHf2Goesgg.png)
_C'est à quoi votre fichier package.json devrait ressembler maintenant._

#### Créer un fichier Babel

Nous devons également ajouter un nouveau fichier appelé `.babelrc`, alors créons-le également.

Dans votre répertoire principal, créez un fichier `.babelrc` et ajoutez le snippet de code suivant. Cela aidera Webpack lors du bundling de votre code et de la conversion de ces codes Sassy que nous allons écrire.

#### Configurer Webpack 4

D'accord, la partie ennuyeuse est terminée. Passons à la partie principale de ce tutoriel : configurer Webpack 4.

Pour citer Star Trek :

> Il me donne du fil à retordre. Il me [_donne du fil à retordre_](http://www.youtube.com/watch?v=s0gk3AXEKUE) ; et je l'aurai. Je le poursuivrai autour des lunes de Nibia et autour du maelström d'Antarès et autour des _flammes_ de Perdition avant de l'abandonner.

Alors créons un nouveau dossier appelé `**config**` et à l'intérieur de ce dossier, créons un fichier appelé `**webpack.base.config.js**`.

La raison pour laquelle j'appelle ce fichier `.base` est qu'il contient toutes les fonctionnalités communes que nous utiliserons dans notre développement et différents environnements de production. Les changements dans ce fichier se refléteront dans tous les environnements. Encore une fois, si cela n'a pas de sens maintenant, les gars, restez avec moi pendant quelques minutes de plus. Cela va commencer à avoir du sens.

Sans plus attendre, dans votre fichier `config/webpack.base.config.js`, écrivez ces lignes de code :

Les `module.rules` définissent l'ensemble des règles que Webpack appliquera à certaines extensions de fichiers.

Dans notre tableau `rules`, nous définissons un `test` qui indique à Webpack quelle extension utiliser. Ici, je dis à Webpack d'appliquer une certaine règle uniquement aux fichiers basés sur `.js`.

Ensuite vient `exclude`. Lors du bundling, je ne veux pas que Webpack transpile tout. Cela deviendra très lent, surtout lorsque j'inclus également mon dossier node_modules.

Je vais donc l'exclure en utilisant la propriété `exclude` dans l'ensemble de règles. La dernière, qui est la plus importante, est la propriété `use.loader`. Ici, je lui donne la valeur `babel-loader`. Ce que fait babel-loader, c'est utiliser nos présélections définies que nous avons définies dans notre fichier `**.babelrc**` pour transpiler tous les fichiers avec une extension `.js`.

**Jusqu'à présent, tout va bien, non ? Nous sommes plus qu'à mi-chemin...**

![Image](https://cdn-media-1.freecodecamp.org/images/1*9BpWHDblN_zsH-9ri_SpHA.gif)
_Même le professeur Snape vous applaudit. Super travail les gars, nous y sommes presque._

Aussi une autre chose : Webpack 4 définit le dossier `**src**` comme point d'entrée par défaut et le dossier `**dist**` comme point de sortie par défaut de votre résultat bundlé. Cool, non ?

Allez dans votre dossier `**tutorial**` et exécutez ce script. Cela bundlera tout votre code et exécutera ce code dans le navigateur :

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

La base de ce script est qu'il combinera tout notre code dans le répertoire `**src**` et l'exécutera dans le navigateur à cette adresse :

```
http://localhost:8080/
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*hw2Qx290aHjl2nOeJob6Hw.png)
_Hmm ! C'est différent. Cela donne une erreur : Cannot GET /_

#### HTML

Donc, lorsque nous avons exécuté le script, il a compilé et ouvert le navigateur. Maintenant, il avait le code que nous avons écrit dans notre fichier `**index.js**`, mais il n'avait pas de fichier .html dans lequel il pouvait l'exécuter.

Nous devons ajouter un html-webpack-plugin à l'intérieur de notre fichier `**webpack.base.config.js**`, et un fichier `**index.html**` dans notre répertoire `**src**`.

Tout d'abord, installez la dépendance pour transpiler HTML avec Webpack :

```
npm i --save-dev html-webpack-plugin
```

Votre fichier `**package.json**` devrait ressembler à ceci :

Maintenant, ajoutons un fichier HTML dans notre répertoire `**src**` et nommons-le `**index.html**` :

Notre répertoire de projet devrait ressembler à ceci maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BjLpopHXvTvhPr77imROIQ.png)
_Notre répertoire de projet devrait ressembler à quelque chose comme ceci_

Pendant que nous y sommes, ajoutons ce `html-webpack-plugin` dans notre fichier `**webpack.base.config.js**`.

Nous avons donc ajouté quelque chose de nouveau à notre fichier de configuration webpack — l'avez-vous remarqué ? Je vous taquine. Je sais que vous l'avez fait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lnDyP4-9zwP7oVJ0DnoLsg.gif)
_Bon travail les gars, nous avons presque terminé._

Maintenant, que fait ce plugin ? Eh bien, c'est très simple. Les plugins, pour faire simple, ajoutent des capacités à votre Webpack. Vous pouvez en lire plus à leur sujet [ici](https://webpack.js.org/plugins/).

J'ai ajouté un seul plugin appelé [html-webpack-plugin](https://webpack.js.org/plugins/html-webpack-plugin/). Le but de ce plugin est très simple : il crée des fichiers HTML pour servir votre ou vos fichiers bundlés.

D'accord, alors exécutons ce script à nouveau (les doigts croisés). « J'espère qu'il n'y aura pas d'erreurs cette fois », a dit chaque développeur une fois.

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

Cela va compiler et ouvrir votre navigateur dans le port par défaut disponible. Le mien est :

```
http://localhost:8080/
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fq9Cg3TFY-fUi1tjJkCtEA.png)
_Je viens de cliquer sur **ctrl + shift + i**, cela a ouvert l'inspecteur d'éléments dans mon navigateur Chrome_

**Partie bleue** : La partie bleue est simplement l'endroit où j'ai mis mes méta-balises et défini un titre pour l'application.

**Partie jaune** : La partie jaune mise en évidence est la partie codée en dur que nous avons écrite dans notre fichier `**index.html**`. C'est là que résidera notre future application React.

**Partie rouge** : La partie que j'ai soulignée en rouge est la plus intéressante. Nous n'avons jamais écrit cela dans notre fichier index.html, alors d'où vient-il ?

Webpack est très intelligent. Il a pris ce fichier dans votre `**index.js**`, l'a bundlé proprement, et l'a ajouté proprement dans le fichier appelé `**main.js**`. Ensuite, il l'a injecté dans notre fichier `**index.html**`. Super cool !

#### Ajouter React

Ajoutons React et commençons la fête. Pour cela, nous devons installer quelques dépendances.

Commençons par :

```
npm i react react-dom --save
```

Maintenant, allez dans votre fichier `**index.js**` et écrivez :

Exécutons ce script à nouveau :

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

Cela va compiler et ouvrir votre navigateur dans le port par défaut. Le mien est :

```
http://localhost:8080/
```

Wow, avez-vous vu ce qui s'est ouvert dans votre navigateur ? Oui ! Vous l'avez fait ! Votre première application React configurée avec Webpack.

Il reste encore beaucoup de choses à faire. Mais bon sang. Bon travail !

![Image](https://cdn-media-1.freecodecamp.org/images/1*ghb2bSQb0lxi_zQY1L7L3A.png)
_C'est notre application React, en cours d'exécution Yayyyy ! :)_

Maintenant, voici la partie amusante. Allez dans votre fichier `**index.js**` et changez le titre en ce que vous voulez. Appuyez sur `**ctrl + s**` et vérifiez votre navigateur. Il a automatiquement mis à jour votre contenu.

Cool, non ?

#### Récapitulons

Nous avons ajouté un environnement de développement. Nous avons ajouté le rechargement à chaud des modules. Nous avons ajouté la prise en charge des fichiers **.js** avec du code React. Dans la prochaine partie, nous ajouterons la prise en charge de SCSS dans notre Webpack.

#### SCSS

Pour la prise en charge de SCSS, nous devons ajouter quelques dépendances supplémentaires dans notre fichier `**package.json**`.

Installez les packages suivants :

```
npm i --save-dev style-loader css-loader sass-loader node-sass extract-text-webpack-plugin@^4.0.0-beta.0
```

[sass-loader](https://github.com/webpack-contrib/sass-loader) : Ce plugin nous aidera à compiler SCSS en CSS.

[node-sass](https://github.com/sass/node-sass) : Le sass-loader nécessite node-sass comme dépendance pair.

[css-loader](https://github.com/webpack-contrib/css-loader) : Le chargeur CSS interprète `@import` et `url()` comme `import/require()` et les résoudra.

[style-loader](https://github.com/webpack-contrib/style-loader) : Ajoute du CSS au DOM en injectant une balise style.

[extract-text-webpack-plugin](https://webpack.js.org/plugins/extract-text-webpack-plugin/) : Il déplace tous les modules `**.css**` requis dans un fichier CSS séparé.

Ainsi, vos styles ne sont plus en ligne dans le bundle JavaScript, mais dans un fichier CSS séparé (`**styles.css**`). Si le volume total de votre feuille de style est important, ce sera plus rapide car le bundle CSS est chargé en parallèle du bundle JavaScript.

Maintenant que nos dépendances ont été installées, apportons quelques modifications à notre fichier de configuration Webpack.

Comprenons d'abord ce que nous avons fait ici. Dans notre `module.rules`, nous avons ajouté une nouvelle règle. Ce que fait cette règle, c'est appliquer un certain bundling à tous les fichiers `**.scss**`. J'espère que cela a du sens. À l'intérieur de notre `use`, nous lui disons d'extraire certaines informations.

Allons un peu plus loin, et j'essaierai de le rendre aussi simple que possible.

```javascript
{ fallback: "style-loader", use: "css-loader!sass-loader" }
```

Essayez de lire ce morceau de code de bas en haut.

Obtenez tout le code SASS — .scss — en utilisant `sass-loader`, puis convertissez-le en code CSS en utilisant `css-loader`. Ensuite, prenez tout ce code CSS et injectez-le dans notre DOM avec la balise <style> en utilisant `style-loader`.

Maintenant, tout cet objet est entouré par :

```
use: ExtractTextPlugin.extract({ ... })
```

Ce `ExtractTextPlugin.extract({ })` prendra tout notre code CSS qui devait être injecté dans notre DOM et combinera tout le code CSS et le bundlera dans un seul fichier appelé `**style.css**`.

L'énorme avantage de cette approche est que si le volume total de notre feuille de style est important lors du chargement depuis le navigateur, il le chargera en parallèle avec notre code JavaScript. Cela rendra notre site plus rapide à télécharger.

Dans la deuxième partie, nous avons dû ajouter une nouvelle entrée dans notre tableau `plugins` qui était :

```
new ExtractTextPlugin('style.css')
```

Cela indique simplement au plugin de combiner tout notre code CSS et de le mettre dans un fichier appelé `**style.css**`.

Créons un nouveau fichier appelé `**styles.scss**` dans notre dossier racine et jouons avec un peu de style.

Maintenant, dans votre fichier `**index.js**`, ajoutez le `**styles.scss**`. Webpack vous permet d'importer du CSS dans JavaScript. C'est génial, je sais.

Dans votre code, ajoutez simplement cette ligne :

```
import './styles.scss';
```

Maintenant, exécutez ce script à nouveau et vérifiez votre navigateur :

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

C'est la dernière fois que nous l'écrivons manuellement. Nous allons faire un script. Et oui, je me souviens — je n'ai toujours pas expliqué ce que fait ce script. Je le ferai. Je promets.

En tout cas, vérifiez votre navigateur... ok cool.

![Image](https://cdn-media-1.freecodecamp.org/images/1*v8yRCnYtcJG63gvRPJXpSA.png)
_Notre application React avec un peu de code .scss. Nous assurons les gars,_

#### Créer le script

Écrivons un peu de script et facilitons-nous la vie. La raison pour laquelle je vous ai demandé d'écrire ce script encore et encore est que vous l'ayez réellement mémorisé et ne le copiez pas simplement depuis Internet.

Sautons dans notre fichier `**package.json**`.

Dans votre section `scripts`, ajoutez le code suivant :

Maintenant, dans votre terminal, tapez :

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ npm run start:dev
```

**Note** : dans le script, nous n'avons plus à écrire ceci :

```
node_modules/.bin/webpack
```

Plus de détails sur l'utilisation de webpack-dev-server dans la documentation [**ici**](https://github.com/webpack/webpack-dev-server#usage).

Le script pour `start:dev` ressemble à quelque chose comme ceci maintenant :

```
webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

Décomposons ce que fait ce script :

`webpack-dev-server --mode development`

Le drapeau `--mode development` définit le build le plus optimisé pour les besoins de développement. Il a une compilation incrémentielle rapide pour le cycle de développement et des messages d'erreur utiles à l'exécution.

Vous pouvez en lire plus sur les modes dans cet article incroyable : [Webpack 4 : Mode et Optimisation](https://medium.com/webpack/webpack-4-mode-and-optimization-5423a6bc597a).

Le drapeau `--config config/webpack.base.config.js` indique à Webpack où se trouve toute notre configuration pour notre bundling Webpack.

Le drapeau `--open` indique à `webpack-dev-server` d'ouvrir le navigateur.

Le drapeau `--hot` indique à `webpack-dev-server` d'activer la fonction de remplacement de module à chaud de Webpack. Cela met à jour le navigateur chaque fois que vous appuyez sur `**ctrl + s**`

Le drapeau `--history-api-fallback` indique à `webpack-dev-server` de revenir à `**index.html**` dans le cas où une ressource demandée ne peut pas être trouvée. Vous pouvez en lire plus sur [history-api-fallback](https://github.com/webpack/webpack-dev-server/tree/master/examples/cli/history-api-fallback) ici.

### Environnement de production

Maintenant que nous avons terminé avec notre environnement de développement, mettons-nous au travail et préparons notre code pour la production.

Créons un nouveau fichier `**webpack.opt.config.js**`. Ce fichier contiendra toutes nos optimisations de production dont nous aurons besoin.

Le plan est de faire quelque chose comme fusionner notre fichier `**webpack.base.config.js**` avec le fichier `**webpack.opt.config.js**` pour créer une configuration de production pour notre application monopage.

Alors commençons. Dans votre répertoire `**config**`, créez un nouveau fichier appelé `**webpack.opt.config.js**`. `opt` est l'abréviation de optimization. Si quelqu'un peut trouver un nom plus cool, faites-le-moi savoir.

Nous devons installer quelques dépendances pour aider avec nos optimisations :

```
$ npm i --save-dev optimize-css-assets-webpack-plugin uglifyjs-webpack-plugin
```

Bien que le `--mode production` vienne avec quelques optimisations assez cool. Vous pouvez en lire plus à ce sujet [ici](https://webpack.js.org/concepts/mode/#mode-production). Mais j'aimerais tout de même en ajouter quelques autres.

Le code est le suivant :

Récapitulons ce que nous avons fait ici. J'ai ajouté deux nouveaux modules en dev-dependency.

[uglifyjs-webpack-plugin](https://github.com/webpack-contrib/uglifyjs-webpack-plugin) : Comme le nom l'indique, cela va uglifier et minimiser tout notre code pour réduire la taille du bundle.

[optimize-css-assets-webpack-plugin](https://github.com/NMFR/optimize-css-assets-webpack-plugin) : Ce plugin va minimiser et optimiser votre code CSS.

**Jusqu'à présent, tout va bien pour tout le monde — nous avons presque terminé.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*H7nnE1npF6MtGTxGBxUPEg.gif)
_Juste un peu plus, et vous avez atteint la ligne d'arrivée._

Vous vous souvenez quand j'ai parlé d'une façon où nous n'aurions pas à répéter notre code encore et encore ? Un pour le développement, l'autre pour la production... et ne me lancez même pas sur la gestion de ces environnements stage, demo et live ! Eh bien, cela se termine aujourd'hui. Plus de répétitions de code.

Je vous présente notre sauveur, le chevalier blanc [Webpack Merge](https://github.com/survivejs/webpack-merge). Ce plugin est incroyable, comme son nom l'indique.

Ce que cela va faire, c'est combiner notre configuration pour les fichiers `**.base**` et `**.opt**` de manière intelligente. Il fournit une fonction `merge` qui concatène les tableaux et fusionne les objets pour créer un nouvel objet.

Alors sans plus attendre, installons également ce plugin incroyable :

```
$ npm i --save-dev webpack-merge
```

Créons notre fichier final `**webpack.prod.config.js**` :

Nous passons un paramètre à notre fonction appelé `productionConfiguration` et utilisons `env`. C'est ainsi que nous passons des informations dans Webpack via notre CLI (je vais expliquer comment nous faisons cela dans une minute).

Je passe quelque chose appelé `NODE_ENV`. C'est la valeur dans laquelle je vais dire à mon webpack quel environnement je vais exécuter — comme demo, test, live ou autre.

Ensuite, tout ce que je reçois dans mon `env.NODE_ENV`, je le définis dans mon `process.env.NODE_ENV` en utilisant le plugin intégré de Webpack appelé `DefinePlugin`. Nous devons simplement nous assurer que toute valeur que nous passons est toujours stringifiée.

Ensuite, dans la dernière ligne, nous faisons ceci :

```
module.exports = merge.smart(baseConfig, optimizationConfig, productionConfiguration);
```

Ce qui se passe ici, c'est que nous utilisons la méthode `smart` de `webpack-merge` pour fusionner intelligemment les trois configurations. Ainsi, nous ne répétons pas le même code partout. C'est la fonctionnalité la plus cool.

Je me souviens d'une époque avant de trouver ce plugin. C'était un vrai bazar de faire la même chose dans tous mes fichiers de configuration Webpack. Maintenant, c'est juste une brise.

En tout cas, en avant, puisque maintenant nos configurations Webpack sont enfin terminées. Créons notre script de build prêt pour la production dans notre fichier `**package.json**`.

Dans votre section scripts, ajoutez les lignes suivantes :

Je vais commencer par la commande `prestart:prod` :

```
"prestart:prod": "webpack --mode production --config config/webpack.prod.config.js --env.NODE_ENV=production --progress",
```

Nous allons décomposer cette commande.

`webpack --mode production`. Comme nous en avons discuté plus tôt, en discutant du `mode développement`, le mode production exécutera quelques processus d'optimisation vraiment cool sur notre ou nos fichiers bundlés pour réduire la taille.

Le drapeau suivant est `--config config/webpack.prod.config.js`. Cela indique à Webpack où se trouve notre configuration de production dans le répertoire.

Le drapeau `env` spécifie la variable d'environnement que nous passons via notre `**webpack-cli**`. Cela se fait comme suit : `--env.NOVE_ENV=production` passe un objet dans notre `**webpack.prod.config.js**` avec la clé `NODE_ENV` qui a la valeur appelée `production`.

Vous pouvez passer autant de variables d'environnement que vous le souhaitez, comme `--env.X=foo --env.Y=bar`. Ensuite, dans votre configuration, vous obtiendrez ces valeurs de la même manière que vous accédez à la valeur `NODE_ENV`.

Le dernier drapeau est `--progess`. Il indique simplement la progression/état du bundle, comme le pourcentage de complétion du bundle lors de la création des fichiers bundlés dans votre dossier `**dist**`.

#### Un rappel rapide

Webpack 4 définit par défaut le dossier `**src**` comme point d'entrée par défaut et le dossier `**dist**` comme point de sortie par défaut de votre résultat bundlé. Cool, non ? Je sais que je me répète — je vous l'ai dit plus tôt — mais c'est pourquoi j'ai dit rappel.

#### Retour à notre tutoriel

Nous avons discuté du script `prestart:prod`, maintenant nous allons parler du script final appelé `start:prod`.

Avec npm, chaque fois que vous voulez exécuter des scripts les uns après les autres, vous les séquenciez avec `preCOMMAND` `COMMAND` `postCOMMAND`.

Comme nous l'avons fait ici :

```
$ prestart:prod
```

```
$ start:prod
```

Nous allons donc toujours exécuter le script `npm run start:prod` avant d'exécuter le script appelé `npm run prestart:prod`.

Discutons de `start:prod`.

```
$ node server => {Cela équivaut à} =&gt; $ node server/index.js
```

Créons un dossier appelé `**server**`. À l'intérieur du dossier, créez un fichier appelé `**index.js**`. Mais avant de faire cela, nous devons ajouter une dernière dépendance.

Ce sera Express, notre framework back-end Node.js :

```
npm i --save express
```

Discutons de ce code avant de continuer.

Nous instancions notre app avec `express()` puis configurons un dossier public statique appelé `**dist**`. C'est le même dossier créé par Webpack lorsque nous exécutons notre commande de production.

Nous incluons notre fichier `**routes**` — nous allons le créer dans une seconde — et définissons le fichier `**routes**` sur le répertoire `/`.

Ensuite, nous configurons un port. Si aucun n'est fourni pour être défini via la CLI de node, nous utilisons le port `3000`. Après cela, nous créons un serveur HTTP et écoutons sur ce serveur via le port. Tout à la fin, nous affichons dans notre terminal que nous exécutons le serveur sur ce port certain.

Créons notre dernier fichier appelé `**routes/index.js` :

Ici, nous vérifions que, quel que soit l'endroit où l'utilisateur arrive, le chemin redirige l'utilisateur vers `**dist/index.html**` où réside notre application React.

Et c'est tout. Nous avons terminé.

Maintenant, allez dans votre terminal et tapez :

```
npm run start:prod
```

Cela prendra un moment. Il vous montrera la progression pendant la transpilation. Après cela, il affiche un message indiquant qu'il `écoute sur le port 3000` si aucun n'est fourni.

Maintenant, allez dans votre navigateur `http:localhost:3000/` et votre application est en vie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zzUTJ889aALPnm_KVmbmeA.gif)
_Félicitations !_

Voir le code sur [GitHub](https://github.com/adeelibr/react-starter).

Un coup de projecteur à mon bon ami [Ahmed Abbasi](https://twitter.com/ehmadabbasi) pour m'avoir aidé à relire cet article.

Vous pouvez me suivre sur [Twitter](http://twitter.com/adeelibr), j'adorerais discuter et vous écouter.
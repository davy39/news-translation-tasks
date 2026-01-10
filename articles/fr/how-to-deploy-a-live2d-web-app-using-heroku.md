---
title: Comment déployer une application Web Live2D en utilisant Heroku
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2020-12-28T17:48:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-live2d-web-app-using-heroku
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/web-2.gif
tags:
- name: animation
  slug: animation
- name: Cloud Computing
  slug: cloud-computing
- name: '#Game Design'
  slug: game-design
- name: Game Development
  slug: game-development
- name: Heroku
  slug: heroku
- name: node
  slug: node
seo_title: Comment déployer une application Web Live2D en utilisant Heroku
seo_desc: 'What is Live2D?

  Live2D is a technology that allows artists to easily transform traditional 2D illustrations
  to create fluid expressions and motions.

  The most popular software for Live2D modeling and animation is Cubism, which also
  provides well-docum...'
---

## Qu'est-ce que Live2D ?

Live2D est une technologie qui permet aux artistes de transformer facilement des illustrations 2D traditionnelles pour créer des expressions et des mouvements fluides.

Le logiciel le plus populaire pour la modélisation et l'animation Live2D est Cubism, qui fournit également un SDK bien documenté pour le web, les applications natives et le moteur de développement de jeux Unity.

Dans ce tutoriel, je vais vous guider à travers la construction sur la base de l'exemple officiel du SDK Web Live2D de Cubism et son déploiement sur Heroku, une plateforme populaire d'hébergement d'applications cloud.

## Comment configurer l'environnement

Pour suivre ce tutoriel, clonez mon dépôt GitHub et basculez sur la branche `start`. Le projet finalisé se trouve sur la branche `develop`.

J'ai également enregistré [un tutoriel vidéo sur YouTube](https://youtu.be/uH1IczzE_t4).

%[https://github.com/RuolinZheng08/heroku-live2d]

```shell
git clone https://github.com/RuolinZheng08/heroku-live2d.git
git checkout start

# mettre à jour le sous-module, le Framework Web Live2D de Cubism
git submodule update --init
```

Installez Node.js et npm en utilisant Homebrew :

```shell
# si vous devez installer homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# homebrew installera node et npm en même temps
brew install node
```

J'utiliserai Visual Studio Code comme mon IDE principal, mais vous pouvez suivre avec n'importe quel éditeur de votre choix.

## Comment exécuter le code de démarrage localement

La structure du répertoire est la suivante. Notre application web sera servie depuis `Samples/TypeScript/Demo`.

```pgsql
.
├─ .vscode          # Paramètres du projet Visual Studio Code
├─ Core             # Code source JavaScript et TypeScript de Live2D Cubism Core
├─ Framework        # Code source pour les fonctionnalités de rendu et d'animation
└─ Samples
   ├─ Resources     # Fichiers de modèle Live2D et actifs d'images web
   └─ TypeScript    # [IMPORTANT] Projet d'exemple TypeScript
```

À l'intérieur du répertoire `heroku-live2d`, exécutez les commandes suivantes :

```shell
cd Samples/TypeScript/Demo/

npm install

npm run-script build

npm run-script serve
```

Accédez à [http://localhost:5000/Samples/TypeScript/Demo/](http://localhost:5000/Samples/TypeScript/Demo/) et vous devriez pouvoir voir un personnage Live2D.

Pour interagir avec le modèle, maintenez le curseur de votre souris enfoncé et la tête et les yeux du personnage suivront votre curseur. Tapotez sur le corps du personnage pour voir une animation spéciale. Tapotez sur l'icône d'engrenage dans le coin supérieur droit pour basculer entre différents modèles.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/web.gif align="left")

*Mark de* `Samples/Resources/Mark`

## Comment déployer sur Heroku

Le code de démarrage utilise npm, TypeScript et webpack.

Pour déployer notre projet sur Heroku, nous devons créer un fichier `package.json` que Heroku peut utiliser pour construire notre projet dans notre répertoire racine du projet. Nous devons également modifier `Samples/TypeScript/Demo/package.json` et la configuration webpack dans `Samples/TypeScript/Demo/webpack.config.js`.

### package.json de niveau supérieur

Le `package.json` de base pour une application Heroku Node.js ressemble à ceci :

```json
{
    "name": "heroku-live2d",
    "description": "Live2D Cubism Heroku Demo",
    "scripts": {
        "start": ...,
        "build": ...
    },
    "dependencies": {
    	...
    }
}
```

Inspectez les attributs `dependencies` et `devDependencies` dans `Samples/TypeScript/Demo/package.json` et ajoutez les deux ensembles de dépendances en tant que `dependencies` à `heroku-live2d/package.json`.

Rappelez-vous que lors de la construction et du service local, nous avons utilisé `npm run-script [build|serve]` depuis le répertoire `Samples/TypeScript/Demo`.

Par conséquent, pour exécuter ces commandes npm depuis la racine du projet, nous devons préfixer `cd Samples/TypeScript/Demo` avant les commandes npm. La commande de construction, par exemple, deviendra :

```shell
cd Samples/TypeScript/Demo && npm run-script build
```

Avec ces changements, le `package.json` de niveau supérieur devrait ressembler à ceci :

```json
{
    "name": "heroku-live2d",
    "description": "Live2D Cubism Heroku Demo",
    "scripts": {
        "start": "cd Samples/TypeScript/Demo && npm run-script start",
        "build": "cd Samples/TypeScript/Demo && npm run-script build"
    },
    "dependencies": {
        "@typescript-eslint/eslint-plugin": "^2.18.0",
        "@typescript-eslint/parser": "^2.18.0",
        "eslint": "^6.8.0",
        "eslint-config-prettier": "^6.10.0",
        "eslint-plugin-prettier": "^3.1.2",
        "prettier": "^1.19.1",
        "rimraf": "^3.0.1",
        "serve": "^11.3.0",
        "ts-loader": "^6.2.1",
        "typescript": "^3.7.5",
        "webpack": "^4.41.5",
        "webpack-cli": "^3.3.10",
        "webpack-dev-server": "^3.10.1",
        "whatwg-fetch": "^3.0.0"
    }
}
```

### Samples/TypeScript/Demo/package.json

En local, nous fonctionnions sur le port 5000. Cependant, Heroku attribuera dynamiquement à notre application web un port stocké dans une variable `$PORT`. Par conséquent, nous devons que la commande `npm run-script start` à l'intérieur de `Samples/TypeScript/Demo/package.json` démarre le serveur webpack sur le port `$PORT`.

Ajoutez à `scripts > start > webpack-dev-server --progress` pour qu'il ressemble à ceci :

```json
"scripts": {
    "start": "webpack-dev-server --progress --port $PORT",
    ...
}
```

### Samples/TypeScript/Demo/webpack.config.js

Ajoutez `disableHostCheck` à la configuration de `devServer` et supprimez `port` puisque nous l'avons configuré dynamiquement ci-dessus.

```javascript
module.exports = {
    ...,
    devServer: {
        contentBase: path.resolve(__dirname, '../../..'),
        watchContentBase: true,
        inline: true,
        hot: true,
        port: 5000, // supprimez cette ligne
        host: '0.0.0.0',
        disableHostCheck: true, // ajoutez cette ligne
        compress: true,
        useLocalIp: true,
        writeToDisk: true
    },
    ...
}
```

Ajoutez `watchOptions` pour que notre `node_modules` ne soit pas surveillé. Si nous ne faisons pas cela, nous rencontrerons une erreur concernant le dépassement du nombre maximum de surveillants lorsque nous déployons sur Heroku.

```javascript
module.exports = {
    ...,
    watchOptions: {
    	ignored: /node_modules/
    },
    ...
}
```

### Déployer sur Heroku

Pour télécharger le client de ligne de commande Heroku, exécutez

```shell
brew tap heroku/brew && brew install heroku
```

Connectez-vous à Heroku depuis la ligne de commande en utilisant `heroku login`.

Créez une application Heroku et ajoutez quelques chiffres (par exemple, 123) au nom de l'application pour garantir l'unicité.

```shell
heroku create heroku-live2d-NUMBERS
```

Configurez Node.js comme le buildpack :

```pgsql
heroku buildpacks:set heroku/nodejs
```

Ajoutez et validez votre projet en utilisant git. Notez que nous n'avons pas nécessairement besoin de `git push` :

```shell
git add .
git commit -m "Prêt à déployer sur heroku"
```

Poussez le projet vers Heroku, en supposant que vous suivez la branche `start`. Vous pouvez toujours vérifier la branche sur laquelle vous vous trouvez et pousser depuis cette branche.

```shell
# vérifier sur quelle branche nous nous trouvons
git branch

# la syntaxe est
# git push heroku GIT_BRANCH_NAME:HEROKU_BRANCH_NAME
git push heroku start:master
```

Vous devrez peut-être attendre quelques minutes pour que le processus de construction se termine.

Après cela, accédez à `YOUR-HEROKU-APP-NAME.herokuapp.com/Samples/TypeScript/Demo`. Dans mon cas, l'URL est [https://heroku-live2d.herokuapp.com/Samples/TypeScript/Demo/](https://heroku-live2d.herokuapp.com/Samples/TypeScript/Demo/). Les personnages Live2D seront là pour vous accueillir :)

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screen-Shot-2020-12-27-at-16.13.19.png align="left")

*Remarquez que l'URL mise en évidence est déjà sur Heroku*

### Comment rediriger index.html vers Samples/TypeScript/Demo

Vous avez peut-être remarqué que `YOUR-HEROKU-APP-NAME.herokuapp.com` affiche une liste de la structure du répertoire au lieu des modèles Live2D. Nous pouvons résoudre ce problème en ajoutant un `index.html` de niveau supérieur factice qui redirige vers `Samples/TypeScript/Demo`.

```html
<!DOCTYPE html>
<html>

<head>
    <title></title>
    <!-- Juste un html factice pour rediriger vers mon sous-répertoire -->
    <meta http-equiv="refresh" content="0; url=Samples/TypeScript/Demo">
</head>

<body>

</body>

</html>
```

Relancez la commande de déploiement `git push heroku start:master`. Maintenant, lorsque vous visitez `YOUR-HEROKU-APP-NAME.herokuapp.com`, vous serez automatiquement redirigé vers la page du modèle Live2D.

Félicitations pour être arrivé à la fin de ce tutoriel ! Vous avez maintenant une application Web Live2D déployée sur Heroku.

J'espère que vous avez apprécié ce tutoriel. Restons en contact ! Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/ruolin-zheng/), [GitHub](https://github.com/RuolinZheng08), [Medium](https://medium.com/@ruolinzheng), ou consultez [mon site web personnel](https://ruolinzheng08.github.io/).

### Ressources et liens

[Mon dépôt GitHub pour ce tutoriel](https://github.com/RuolinZheng08/heroku-live2d/tree/develop)

[Mon application Heroku](https://heroku-live2d.herokuapp.com/)

[Mon tutoriel vidéo YouTube](https://youtu.be/uH1IczzE_t4)

[Documentation officielle du SDK de Cubism](https://docs.live2d.com/cubism-sdk-tutorials/sample-build-web/)
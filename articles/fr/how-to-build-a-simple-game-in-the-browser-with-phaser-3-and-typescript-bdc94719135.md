---
title: Comment créer un jeu simple dans le navigateur avec Phaser 3 et TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T20:01:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-game-in-the-browser-with-phaser-3-and-typescript-bdc94719135
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m16cMnrn60vR49N8Sj1liA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: Game Development
  slug: game-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Comment créer un jeu simple dans le navigateur avec Phaser 3 et TypeScript
seo_desc: 'By Mariya Davydova

  I’m a developer advocate and a backend developer, and my frontend development expertise
  is relatively weak. A while ago I wanted to have some fun and make a game in a browser;
  I chose Phaser 3 as a framework (it looks quite popular...'
---

Par Mariya Davydova

Je suis une développeuse advocate et une développeuse backend, et mon expertise en développement frontend est relativement faible. Il y a quelque temps, je voulais m'amuser et créer un jeu dans un navigateur ; j'ai choisi Phaser 3 comme framework (il semble assez populaire ces jours-ci) et TypeScript comme langage (parce que je préfère le typage statique au typage dynamique). Il s'avère que vous devez faire quelques choses ennuyeuses pour que tout fonctionne, alors j'ai écrit ce tutoriel pour aider les autres personnes comme moi à démarrer plus rapidement.

### Préparation de l'environnement

#### IDE

Choisissez votre environnement de développement. Vous pouvez toujours utiliser le bon vieux Notepad si vous le souhaitez, mais je vous suggérerais d'utiliser quelque chose de plus utile. Pour ma part, je préfère développer des projets personnels dans Emacs, donc j'ai installé [tide](https://github.com/ananthakumaran/tide) et suivi les instructions pour le configurer.

#### Node

Si nous développons en JavaScript, nous pourrions parfaitement bien commencer à coder sans toutes ces étapes de préparation. Cependant, comme nous voulons utiliser TypeScript, nous devons mettre en place l'infrastructure pour rendre le développement futur aussi rapide que possible. Ainsi, nous devons installer node et npm.

Au moment où j'écris ce tutoriel, j'utilise [node 10.13.0](https://nodejs.org/en/) et [npm 6.4.1](https://www.npmjs.com/). Veuillez noter que les versions dans le monde du frontend se mettent à jour extrêmement rapidement, donc vous pouvez simplement prendre les dernières versions stables. Je recommande fortement d'utiliser [nvm](https://github.com/creationix/nvm) au lieu d'installer node et npm manuellement ; cela vous fera gagner beaucoup de temps et de nerfs.

### Configuration du projet

#### Structure du projet

Nous allons utiliser npm pour construire le projet, donc pour démarrer le projet, allez dans un dossier vide et exécutez `npm init`. npm vous posera plusieurs questions sur les propriétés de votre projet et créera ensuite un fichier `package.json`. Il ressemblera à quelque chose comme ceci :

```
{
  "name": "Starfall",
  "version": "0.1.0",
  "description": "Jeu Starfall (Phaser 3 + TypeScript)",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Erreur : aucun test spécifié\" && exit 1"
  },
  "author": "Mariya Davydova",
  "license": "MIT"
}
```

#### Paquets

Installez les paquets dont nous avons besoin avec la commande suivante :

`npm install -D typescript webpack webpack-cli ts-loader phaser live-server`

L'option `-D` (alias `--save-dev`) fait en sorte que npm ajoute ces paquets à la liste des dépendances dans `package.json` automatiquement :

```
"devDependencies": {
   "live-server": "^1.2.1",
   "phaser": "^3.15.1",
   "ts-loader": "^5.3.0",
   "typescript": "^3.1.6",
   "webpack": "^4.26.0",
   "webpack-cli": "^3.1.2"
 }
```

#### Webpack

Webpack exécutera le compilateur TypeScript et collectera le groupe de fichiers JS résultants ainsi que les bibliothèques en un seul JS minifié afin que nous puissions l'inclure dans notre page.

Ajoutez `webpack.config.js` près de votre `project.json` :

```js
const path = require('path');
module.exports = {
  entry: './src/app.ts',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: [ '.ts', '.tsx', '.js' ]
  },
  output: {
    filename: 'app.js',
    path: path.resolve(__dirname, 'dist')
  },
  mode: 'development'
};
```

Ici, nous voyons que webpack doit obtenir les sources à partir de `src/app.ts` (que nous ajouterons très bientôt) et tout collecter dans le fichier `dist/app.js`.

#### TypeScript

Nous avons également besoin d'un petit fichier de configuration pour le compilateur TypeScript (`tsconfig.json`) où nous expliquons quelle version de JS nous voulons que les sources soient compilées et où trouver ces sources :

```
{
  "compilerOptions": {
    "target": "es5"
  },
  "include": [
    "src/*"
  ]
}
```

#### Définitions TypeScript

TypeScript est un langage à typage statique. Par conséquent, il nécessite des définitions de type pour la compilation. Au moment de la rédaction de ce tutoriel, les définitions pour Phaser 3 n'étaient pas encore disponibles en tant que package npm, vous devrez donc peut-être les [télécharger](https://github.com/photonstorm/phaser3-docs/blob/master/typescript/phaser.d.ts) depuis le dépôt officiel et placer le fichier dans le sous-répertoire `src` de votre projet.

#### Scripts

Nous avons presque terminé la configuration du projet. À ce stade, vous devriez avoir créé `package.json`, `webpack.config.js` et `tsconfig.json`, et ajouté `src/phaser.d.ts`. La dernière chose que nous devons faire avant de commencer à écrire du code est d'expliquer ce que npm doit faire exactement avec le projet. Nous mettons à jour la section `scripts` du `package.json` comme suit :

```
"scripts": {
  "build": "webpack",
  "start": "webpack --watch & live-server --port=8085"
}
```

Lorsque vous exécutez `npm build`, le fichier `app.js` sera construit selon la configuration de webpack. Et lorsque vous exécutez `npm start`, vous n'aurez pas à vous soucier du processus de construction : dès que vous sauvegardez une source, webpack reconstruira l'application et le [live-server](https://www.npmjs.com/package/live-server) la rechargera dans votre navigateur par défaut. L'application sera hébergée à l'adresse [http://127.0.0.1:8085/](http://127.0.0.1:8085/).

### Démarrage

Maintenant que nous avons configuré l'infrastructure (la partie que je déteste personnellement lorsque je commence un projet), nous pouvons enfin commencer à coder. Dans cette étape, nous allons faire une chose simple : dessiner un rectangle bleu foncé dans notre fenêtre de navigateur. Utiliser un grand framework de développement de jeux pour cela est un peu... hmmm... excessif. Pourtant, nous en aurons besoin pour les prochaines étapes.

Permettez-moi de vous expliquer brièvement les principaux concepts de Phaser 3. Le jeu est une instance de la classe `Phaser.Game` (ou de son descendant). Chaque jeu contient une ou plusieurs instances de descendants de `Phaser.Scene`. Chaque scène contient plusieurs objets, soit statiques soit dynamiques, et représente une partie logique du jeu. Par exemple, notre jeu trivial aura trois scènes : l'écran de bienvenue, le jeu lui-même et l'écran de score.

Commençons à coder.

Tout d'abord, créez un conteneur HTML minimaliste pour le jeu. Créez un fichier `index.html`, qui contient le code suivant :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Starfall</title>
    <script src="dist/app.js"></script>
  </head>
  <body>
    <div id="game"></div>
  </body>
</html>
```

Il n'y a que deux parties essentielles ici : la première est une entrée `script` qui indique que nous allons utiliser notre fichier construit ici, et la seconde est une entrée `div` qui sera le conteneur du jeu.

Maintenant, créez un fichier `src/app.ts` avec le code suivant :

```js
import "phaser";
const config: GameConfig = {
  title: "Starfall",
  width: 800,
  height: 600,
  parent: "game",
  backgroundColor: "#18216D"
};
export class StarfallGame extends Phaser.Game {
  constructor(config: GameConfig) {
    super(config);
  }
}
window.onload = () => {
  var game = new StarfallGame(config);
};
```

Ce code est auto-explicatif. GameConfig a beaucoup de propriétés variées, vous pouvez les consulter [ici](https://photonstorm.github.io/phaser3-docs/global.html#GameConfig).

Et maintenant, vous pouvez enfin exécuter `npm start`. Si tout a été fait correctement dans cette étape et les étapes précédentes, vous devriez voir quelque chose d'aussi simple que ceci dans votre navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/nzFRXBL717gru5RWhXwaqDtjLVGNHZXnFIlg)
_Oui, c'est un écran bleu._

### Faire tomber les étoiles

Nous avons créé une application élémentaire. Maintenant, il est temps d'ajouter une scène où quelque chose va se passer. Notre jeu sera simple : les étoiles tomberont au sol, et le but sera d'en attraper autant que possible.

Pour atteindre cet objectif, créez un nouveau fichier, `gameScene.ts`, et ajoutez le code suivant :

```js
import "phaser";
export class GameScene extends Phaser.Scene {
  constructor() {
    super({
      key: "GameScene"
    });
  }
  init(params): void {
    // TODO
  }
  preload(): void {
    // TODO
  }
  
  create(): void {
    // TODO
  }
  update(time): void {
    // TODO
  }
};
```

Le constructeur ici contient une clé sous laquelle d'autres scènes peuvent appeler cette scène.

Vous voyez ici des stubs pour quatre méthodes. Permettez-moi de vous expliquer brièvement la différence entre elles :

* `init([params])` est appelé lorsque la scène commence ; cette fonction peut accepter des paramètres, qui sont passés d'autres scènes ou du jeu en appelant `scene.start(key, [params])`
* `preload()` est appelé avant que les objets de la scène ne soient créés, et il contient le chargement des assets ; ces assets sont mis en cache, donc lorsque la scène est redémarrée, ils ne sont pas rechargés
* `create()` est appelé lorsque les assets sont chargés et contient généralement la création des principaux objets du jeu (arrière-plan, joueur, obstacles, ennemis, etc.)
* `update([time])` est appelé à chaque tick et contient la partie dynamique de la scène — tout ce qui bouge, clignote, etc.

Pour être sûr que nous ne l'oublions pas plus tard, ajoutons rapidement les lignes suivantes dans le `game.ts` :

```js
import "phaser";
import { GameScene } from "./gameScene";
const config: GameConfig = {
  title: "Starfall",
  width: 800,
  height: 600,
  parent: "game",
  scene: [GameScene],
  physics: {
    default: "arcade",
    arcade: {
      debug: false
    }
  },
  backgroundColor: "#000033"
};
...
```

Notre jeu connaît maintenant la scène de jeu. Si la configuration du jeu contient une liste de scènes, la première est démarrée lorsque le jeu commence, et toutes les autres sont créées mais pas démarrées jusqu'à ce qu'elles soient explicitement appelées.

Nous avons également ajouté la physique arcade ici. Elle est nécessaire pour faire tomber nos étoiles.

Maintenant, nous pouvons mettre de la chair sur les os de notre scène de jeu.

Tout d'abord, nous déclarons quelques propriétés et objets dont nous allons avoir besoin :

```js
export class GameScene extends Phaser.Scene {
  delta: number;
  lastStarTime: number;
  starsCaught: number;
  starsFallen: number;
  sand: Phaser.Physics.Arcade.StaticGroup;
  info: Phaser.GameObjects.Text;
...
```

Ensuite, nous initialisons les nombres :

```js
init(/*params: any*/): void {
    this.delta = 1000;
    this.lastStarTime = 0;
    this.starsCaught = 0;
    this.starsFallen = 0;
  }
```

Maintenant, nous chargeons quelques images :

```js
preload(): void {
    this.load.setBaseURL(
      "https://raw.githubusercontent.com/mariyadavydova/" +
      "starfall-phaser3-typescript/master/");
    this.load.image("star", "assets/star.png");
    this.load.image("sand", "assets/sand.jpg");
  }
```

Après cela, nous pouvons préparer nos composants statiques. Nous allons créer le sol, où les étoiles tomberont, et le texte nous informant du score actuel :

```js
create(): void {
    this.sand = this.physics.add.staticGroup({
      key: 'sand',
      frameQuantity: 20
    });
    Phaser.Actions.PlaceOnLine(this.sand.getChildren(),
      new Phaser.Geom.Line(20, 580, 820, 580));
    this.sand.refresh();
    this.info = this.add.text(10, 10, '',
      { font: '24px Arial Bold', fill: '#FBFBAC' });
  }
```

Un groupe dans Phaser 3 est un moyen de créer un ensemble d'objets que vous voulez contrôler ensemble. Il existe deux types d'objets : statiques et dynamiques. Comme vous pouvez le deviner, les objets statiques ne bougent pas (sol, murs, divers obstacles), tandis que les objets dynamiques font le travail (Mario, vaisseaux, missiles).

Nous créons un groupe statique de morceaux de sol. Ces morceaux sont placés le long de la ligne. Veuillez noter que la ligne est divisée en 20 sections égales (et non 19 comme vous auriez pu vous y attendre), et les tuiles de sol sont placées sur chaque section à l'extrémité gauche avec le centre de la tuile situé à ce point (j'espère que cela explique ces nombres). Nous devons également appeler `refresh()` pour mettre à jour la boîte de délimitation du groupe (sinon, les collisions seront vérifiées par rapport à l'emplacement par défaut, qui est le coin supérieur gauche de la scène).

Si vous vérifiez votre application dans le navigateur maintenant, vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/wOnfzVfRtvMsSY6n3ftjv5DKOlXpKyh3uRSo)
_Évolution de l'écran bleu_

Nous avons enfin atteint la partie la plus dynamique de cette scène — la fonction `update()`, où les étoiles tombent. Cette fonction est appelée environ une fois toutes les 60 ms. Nous voulons émettre une nouvelle étoile tombante chaque seconde. Nous n'utiliserons pas de groupe dynamique pour cela, car le cycle de vie de chaque étoile sera court : elle sera détruite soit par un clic de l'utilisateur, soit par une collision avec le sol. Par conséquent, à l'intérieur de la fonction `emitStar()`, nous créons une nouvelle étoile et ajoutons le traitement de deux événements : `onClick()` et `onCollision()`.

```js
update(time: number): void {
    var diff: number = time - this.lastStarTime;
    if (diff > this.delta) {
      this.lastStarTime = time;
      if (this.delta > 500) {
        this.delta -= 20;
      }
      this.emitStar();
    }
    this.info.text =
      this.starsCaught + " attrapées - " +
      this.starsFallen + " tombées (max 3)";
  }
private onClick(star: Phaser.Physics.Arcade.Image): () => void {
    return function () {
      star.setTint(0x00ff00);
      star.setVelocity(0, 0);
      this.starsCaught += 1;
      this.time.delayedCall(100, function (star) {
        star.destroy();
      }, [star], this);
    }
  }
private onFall(star: Phaser.Physics.Arcade.Image): () => void {
    return function () {
      star.setTint(0xff0000);
      this.starsFallen += 1;
      this.time.delayedCall(100, function (star) {
        star.destroy();
      }, [star], this);
    }
  }
private emitStar(): void {
    var star: Phaser.Physics.Arcade.Image;
    var x = Phaser.Math.Between(25, 775);
    var y = 26;
    star = this.physics.add.image(x, y, "star");
    star.setDisplaySize(50, 50);
    star.setVelocity(0, 200);
    star.setInteractive();
    star.on('pointerdown', this.onClick(star), this);
    this.physics.add.collider(star, this.sand, 
      this.onFall(star), null, this);
  }
```

Enfin, nous avons un jeu ! Il n'a pas encore de condition de victoire. Nous l'ajouterons dans la dernière partie de notre tutoriel.

![Image](https://cdn-media-1.freecodecamp.org/images/tOFqrM7BADGImoBCe3Z9j3V2W5m06Bw4kRwZ)
_Je suis mauvais pour attraper les étoiles..._

### Conclusion

Habituellement, un jeu se compose de plusieurs scènes. Même si le gameplay est simple, vous avez besoin d'une scène d'ouverture (contenant au moins le bouton 'Jouer !') et d'une scène de fermeture (montrant le résultat de votre session de jeu, comme le score ou le niveau maximum atteint). Ajoutons ces scènes à notre application.

Dans notre cas, elles seront assez similaires, car je ne veux pas accorder trop d'attention à la conception graphique du jeu. Après tout, c'est un tutoriel de programmation.

La scène de bienvenue aura le code suivant dans `welcomeScene.ts`. Notez que lorsque l'utilisateur clique quelque part sur cette scène, une scène de jeu apparaîtra.

```js
import "phaser";
export class WelcomeScene extends Phaser.Scene {
  title: Phaser.GameObjects.Text;
  hint: Phaser.GameObjects.Text;
  constructor() {
    super({
      key: "WelcomeScene"
    });
  }
  create(): void {
    var titleText: string = "Starfall";
    this.title = this.add.text(150, 200, titleText,
      { font: '128px Arial Bold', fill: '#FBFBAC' });
    var hintText: string = "Cliquez pour commencer";
    this.hint = this.add.text(300, 350, hintText,
      { font: '24px Arial Bold', fill: '#FBFBAC' });
    this.input.on('pointerdown', function (/*pointer*/) {
      this.scene.start("GameScene");
    }, this);
  }
};
```

La scène de score ressemblera presque à la même, menant à la scène de bienvenue sur clic (`scoreScene.ts`).

```js
import "phaser";
export class ScoreScene extends Phaser.Scene {
  score: number;
  result: Phaser.GameObjects.Text;
  hint: Phaser.GameObjects.Text;
  constructor() {
    super({
      key: "ScoreScene"
    });
  }
  init(params: any): void {
    this.score = params.starsCaught;
  }
  create(): void {
    var resultText: string = 'Votre score est ' + this.score + ' !';
    this.result = this.add.text(200, 250, resultText,
      { font: '48px Arial Bold', fill: '#FBFBAC' });
    var hintText: string = "Cliquez pour recommencer";
    this.hint = this.add.text(300, 350, hintText,
      { font: '24px Arial Bold', fill: '#FBFBAC' });
    this.input.on('pointerdown', function (/*pointer*/) {
      this.scene.start("WelcomeScene");
    }, this);
  }
};
```

Nous devons mettre à jour notre fichier d'application principal maintenant : ajouter ces scènes et faire en sorte que `WelcomeScene` soit la première dans la liste :

```js
import "phaser";
import { WelcomeScene } from "./welcomeScene";
import { GameScene } from "./gameScene";
import { ScoreScene } from "./scoreScene";
const config: GameConfig = {
  ...
  scene: [WelcomeScene, GameScene, ScoreScene],
  ...
```

Avez-vous remarqué ce qui manque ? Exactement, nous n'appelons pas encore la `ScoreScene` depuis quelque part ! Appelons-la lorsque le joueur a manqué la troisième étoile :

```
private onFall(star: Phaser.Physics.Arcade.Image): () => void {
    return function () {
      star.setTint(0xff0000);
      this.starsFallen += 1;
      this.time.delayedCall(100, function (star) {
        star.destroy();
        if (this.starsFallen > 2) {
          this.scene.start("ScoreScene", 
            { starsCaught: this.starsCaught });
        }
      }, [star], this);
    }
  }
```

Enfin, notre jeu Starfall ressemble à un vrai jeu — il commence, se termine et a même un objectif à atteindre (combien d'étoiles pouvez-vous attraper ?).

J'espère que ce tutoriel est aussi utile pour vous qu'il l'a été pour moi lorsque je l'ai écrit :) Tout retour est grandement apprécié !

Le code source de ce tutoriel peut être trouvé [ici](https://github.com/mariyadavydova/starfall-phaser3-typescript).
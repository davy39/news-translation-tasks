---
title: Comment j'automatise toutes les parties ennuyeuses de mon travail avec Create
  React App DevOps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-07T03:16:18.000Z'
originalURL: https://freecodecamp.org/news/lets-write-create-react-app-devops-together-dc19512c6fbb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LjmVlUg4vIy-MA6BCwkLPw.jpeg
tags:
- name: Devops
  slug: devops
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: UI
  slug: ui
- name: Web Development
  slug: web-development
seo_title: Comment j'automatise toutes les parties ennuyeuses de mon travail avec
  Create React App DevOps
seo_desc: 'By James Y Rauhut

  When you have responsibilities as one of the only designers — and possibly developer
  s— on your team, automation becomes your best friend.

  At work, I have both responsibilities as a designer and sometimes as a lone developer.
  This m...'
---

Par James Y Rauhut

Lorsque vous avez des responsabilités en tant que l'un des seuls designers — et peut-être développeur — de votre équipe, l'automatisation devient votre meilleure amie.

Au travail, j'ai à la fois des responsabilités de designer et parfois de développeur solitaire. Cela signifie qu'il n'y a pas beaucoup de temps pour configurer l'environnement de développement sur lequel je travaille. Du temps est également perdu lorsque je dois manuellement mettre à jour les applications vers leur environnement en ligne.

Heureusement, il existe des outils gratuits qui nous aident à prototyper et à publier en un rien de temps : Create React App, Bluemix, GitHub et Travis CI. Je vais vous partager comment j'utilise tous ces outils pour automatiser toutes les parties ennuyeuses de mon travail avec [Create React App DevOps](https://github.com/seejamescode/create-react-app-devops).

> Mise à jour du 3 mars 2017 : Grâce à l'avertissement d'un commentateur, j'ai été prévenu de ne pas utiliser Babel-Node en production (sur Bluemix). [Create React App DevOps](https://github.com/seejamescode/create-react-app-devops) reflète désormais cela avec la version v1.1.0 !

Il existe trois façons d'adapter ce processus vous-même :

* Suivez ce post pendant que nous écrivons le projet ensemble
* Inspectez la comparaison entre l'utilisation initiale de Create React App et le dernier commit : [Comparaison GitHub entre le premier et le dernier commit](https://github.com/seejamescode/create-react-app-devops/compare/0dbaf64a02f0eeedba2e5a134d472a58b3fc55a5...master)
* Forkez le dépôt et suivez les instructions ci-dessous : [Fork Create React App DevOps](https://github.com/seejamescode/create-react-app-devops#fork-destination-box)

Consultez l'application en direct à l'adresse : [https://create-react-app-devops.mybluemix.net/](http://create-react-app-devops.mybluemix.net/)

Si vous souhaitez connaître les détails du projet, continuez à lire pour le réaliser avec moi ! Il y aura six sections :

1. Utiliser Create React App pour démarrer l'interface utilisateur
2. Configurer votre serveur avec Node, Express et Babel
3. Exécuter l'application sur le Web avec Bluemix
4. Déployer automatiquement depuis GitHub avec Travis CI
5. Récupérer des données API tout en gardant les clés sécurisées
6. Créer une application de staging pour l'expérimentation

### [Utiliser Create React App pour démarrer l'interface utilisateur](https://github.com/seejamescode/create-react-app-devops/commit/0dbaf64a02f0eeedba2e5a134d472a58b3fc55a5)

Lorsque j'ai commencé à utiliser React pour des projets front-end, j'ai perdu beaucoup de temps. Une grande partie de ce temps était consacrée à la configuration de Webpack et de divers plugins. Heureusement, Create React App a été créé pour garder vos projets correctement configurés. Il existe une option pour "éjecter" vos projets Create React App, mais j'évite de le faire. Cela me permet de continuer à recevoir les mises à jour de Facebook pour le projet.

1. [Installez Node](https://docs.npmjs.com/getting-started/installing-node) pour gérer les packages que nous utilisons et le serveur.
2. [Installez Yarn](https://yarnpkg.com/lang/en/docs/install/#mac-tab) (optionnel) pour accélérer l'installation des packages. Si vous choisissez de ne pas le faire, gardez à l'esprit que les commandes terminales comme `yarn run ---` sont généralement `npm run ---`.
3. Il est temps d'ouvrir votre terminal. Installez Create React App globalement : `yarn global add create-react-app`
4. Laissez Create React App créer votre projet et naviguez dedans : `create-react-app <nom-app>`; et cd <`nom-app`>

**Note de côté** : Chaque fois que vous voyez « <nom-app> » dans cet article, vous pouvez le remplacer par un nom unique pour votre projet comme « super-cool-app ».

#### ?????

Vous pouvez maintenant travailler sur tout le code côté client (interface utilisateur) ! Exécutez `yarn start` et Create React App ouvrira un onglet dans votre navigateur pour vous montrer l'interface utilisateur. Chaque fois que vous modifiez le code côté client dans le `<nom-app>`;/src/, le navigateur se rafraîchira avec les changements !  
?????

### [Configurer votre serveur avec Node, Express et Babel](https://github.com/seejamescode/create-react-app-devops/commit/aafd7e34b43906814b7bb49e0a3d33e211e81281)

Maintenant, mettons en place un serveur pour que vous puissiez héberger l'application en ligne. Contrôler votre propre serveur Node sera également important plus tard pour récupérer des données avec une API à partir de services comme GitHub.

1. Ajoutons tous les packages pour un serveur Node. Les packages liés à Babel vous permettront d'utiliser les dernières fonctionnalités de JavaScript : `yarn add babel-cli babel-preset-es2015 babel-preset-stage-2 compression express`
2. Créez maintenant un fichier `index.js` à la racine du dossier du projet pour représenter notre serveur Node :

```
import compression from 'compression';import express from 'express'; const app = express();const port = process.env.PORT || 8080;app.use(compression()); app.use(express.static('./build')); app.listen(port, (err) => { if (err) {   console.log(err);   return; }
```

```
 console.log(`Le serveur est en ligne à l'adresse http://localhost:${port}`);});
```

3. Vous pouvez maintenant voir toutes les dépendances que nous avons installées dans `package.json`. Ajoutons un script appelé « bluemix » pour exécuter le serveur et une section appelée « babel » pour configurer Babel :

```
"scripts": {  "bluemix": "babel-node index.js",  "start": "react-scripts start",  "build": "react-scripts build",  "test": "react-scripts test --env=jsdom",  "eject": "react-scripts eject",},"babel": {  "presets": [    "es2015",    "stage-2"  ]}
```

4. `yarn build && yarn bluemix` construira l'application et exécutera le serveur. Cependant, nous voulons ajouter un mode dev au serveur similaire à notre code côté client. Ainsi, nous voyons les changements simplement en enregistrant `index.js` lorsque nous codons. Ajoutons quelques dépendances qui nous permettront de faire cela : `yarn add babel-watch concurrently --dev`

5. Maintenant, mettez à jour le script « start » dans package.json afin que nous exécutions le mode dev de Create React App et notre serveur. Nous allons également ajouter une ligne « proxy ». Cette ligne indique à Create React App qu'un serveur peut prendre les requêtes qui ne sont pas trouvées dans le code côté client :

```
"proxy": "http://localhost:8081","scripts": {  "bluemix": "babel-node index.js",  "start": "concurrently \"PORT=8080 react-scripts start\" \"PORT=8081 babel-watch index.js\"",  "build": "react-scripts build",  "test": "react-scripts test --env=jsdom",  "eject": "react-scripts eject",},
```

#### ?????

Vous pouvez maintenant travailler sur le code côté serveur dans `index.js` ! Exécutez `yarn start` et à la fois le mode dev de Create React App et notre serveur répondront aux changements enregistrés !  
?????

### [Exécuter l'application sur le Web avec Bluemix](https://github.com/seejamescode/create-react-app-devops/commit/3d61ec57acdbd0988c4aadf402415d290cf9c064)

Puisque je travaille chez IBM, Bluemix est notre plateforme d'hébergement de choix. Non seulement nous hébergeons nos produits finaux sur Bluemix, mais nous hébergeons également tous les prototypes à partager avec les pairs et les tests utilisateurs. J'utilise également Bluemix pour des projets personnels comme celui-ci car il offre un niveau gratuit solide.

1. Créez un compte gratuit sur [Bluemix](https://www.bluemix.net).
2. Installez le [Cloud Foundry CLI](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html). Puisque Bluemix est construit sur un projet open-source appelé Cloud Foundry, vous verrez « cf » dans beaucoup de nos commandes.
3. Similaire aux fichiers `.gitignore`, nous devrions créer un fichier pour empêcher les fichiers inutiles d'être téléchargés sur Bluemix. Créez `.cfignore` dans le dossier racine du projet pour cela :

```
/node_modules .DS_Store npm-debug.log* yarn-debug.log* yarn-error.log*
```

4. Maintenant, nous pouvons indiquer à Bluemix tous les paramètres de notre application pour le déploiement avec un fichier `manifest.yml` à la racine du projet :

```
---applications:- name: <nom-app>  buildpack: https://github.com/cloudfoundry/nodejs-buildpack  command: npm run bluemix  disk_quota: 256MB  memory: 128MB
```

5. Enfin, connectez-vous à Bluemix depuis votre terminal avec `cf login -a https://api.ng.bluemix.net`, construisez votre application avec `yarn build`, puis poussez votre application dans le monde avec `cf push`.

#### ?????

Après environ cinq minutes, votre terminal devrait indiquer que l'application est en ligne à l'adresse <nom-app>.mybluemix.net ! Maintenant, le monde peut la voir. Une erreur courante est que le nom de votre application a déjà été pris sur Bluemix. Choisissez simplement un nom plus unique et cela devrait fonctionner !  
?????

### [Déployer automatiquement depuis GitHub avec Travis CI](http://Automagically Deploy from Github with Travis
0CI)

L'une des parties les plus fastidieuses de la gestion d'une application est de la déployer chaque fois que vous avez des changements prêts. Je devenais même paresseux et je regroupais mes déploiements chaque fois que je me sentais enfin prêt à le faire. Grâce à Travis CI (Intégration Continue), le déploiement peut devenir aussi simple que [la gestion de votre dépôt GitHub](https://guides.github.com/activities/hello-world/).

1. Tout d'abord, vous devez créer un [compte GitHub](https://github.com/join) et configurer [Git sur votre ordinateur](https://help.github.com/articles/set-up-git/).
2. Ensuite, créez un nouveau dépôt sur [GitHub.com](https://github.com/new) puis suivez les instructions du terminal fournies pour pousser votre projet vers GitHub :

```
git initgit add .git commit -m 'Initial commit'git remote add origin https://github.com/<nom-utilisateur-github>/<nom-app>.gitgit push -u origin master
```

3. Maintenant, rendez-vous sur [Travis CI](https://travis-ci.org/) pour vous connecter avec vos identifiants GitHub. Cliquez sur l'icône « + » pour activer votre nouveau dépôt. Si vous ne voyez pas le dépôt que vous venez de créer, cliquez sur « Synchroniser le compte » et il devrait apparaître.

4. Ensuite, cliquez sur les paramètres du projet dans Travis pour choisir les options suivantes :

Construire uniquement si .travis.yml est présent = Activé  
Construire les pushes = Activé  
Limiter les travaux simultanés = Désactivé  
Construire les pull requests = Activé (Cela permettra à GitHub d'exécuter tous les tests automatisés que vous ajoutez à l'avenir pour les PR ouvertes.)  
Variables d'environnement : `BLUEMIX_PASSWORD = <Votre-mot-de-passe-bluemix>`

5. La plus grande étape ici est d'ajouter le plan pour Travis en tant que fichier `.travis.yml` à la racine du projet :

```
sudo: truelanguage: node_jsnode_js:- '5.7'cache:  yarn: true  directories:    - node_modulesenv:  global:  - CF_API=https://api.ng.bluemix.net/  - CF_USERNAME=<Votre-email-bluemix>  - CF_ORG=<Votre-email-bluemix>  - CF_SPACE=devbefore_deploy:  - wget https://s3.amazonaws.com/go-cli/releases/v6.12.4/cf-cli_amd64.deb -qO temp.deb && sudo dpkg -i temp.deb  - rm temp.deb  - cf login -a ${CF_API} -u ${CF_USERNAME} -p ${BLUEMIX_PASSWORD} -o ${CF_ORG} -s ${CF_SPACE}  - cf install-plugin autopilot -r CF-Community  - yarn builddeploy:  - edge: true    provider: script    script: if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then cf zero-downtime-push <Mon-app> -f ./manifest.yml; else echo "PR skip deploy"; fi    skip_cleanup: true    on:      branch: master
```

**Important** : Remarquez qu'il y a deux endroits où vous insérez votre email Bluemix et un endroit où vous insérez le nom de l'application sur Bluemix !

Il se passe beaucoup de choses ici. Je vais donc essayer de le résumer : Dans la section `before_deploy`, Travis construit l'application, se connecte à Bluemix en tant que vous, puis télécharge un plugin Cloud Foundry appelé Autopilot. Ensuite, dans la section deploy, Travis décide si le déploiement est une pull request ouverte ou un commit réel sur la branche master de GitHub. Si c'est un commit réel, exécutez Autopilot pour déployer l'application.

Autopilot pratique le déploiement Blue-Green. Cela signifie que la nouvelle version de votre application sera nommée `<mon-app>-venerable` sur Bluemix. Si la nouvelle version se construit et s'exécute avec succès, l'ancienne version de l'application est supprimée et la nouvelle version se renomme avec le nom d'origine. Si le déploiement échoue, `<mon-app>-venerable` reste en ligne afin que vous puissiez déboguer les logs et l'ancienne version de l'application continue de s'exécuter pour que vos utilisateurs ne voient aucun temps d'arrêt !

#### ?????

Super DevOps, Batman ! Naviguez vers `https://travis-ci.org/<nom-utilisateur-github>/<nom-app>/builds` et vous devriez voir un build Travis sur le point de se produire. Si vous cliquez dessus, vous pouvez le regarder démarrer et suivre son déploiement pour vous !  
?????

### [Récupérer des données API tout en gardant les clés sécurisées](https://github.com/seejamescode/create-react-app-devops/commit/2a4fe33006f46b4f036f1846874ef869243d5743)

La plupart des applications utilisent des données provenant de différentes sources pour composer leur offre. Pour qu'une application obtienne des données externes, elles utilisent une API pour récupérer les données. Pour que l'API s'assure que la bonne application récupère les données, une clé est donnée à l'application pour s'identifier. Nous devons garder cette clé secrète de notre dépôt GitHub !

1. Tout d'abord, demandons une clé à l'[API GitHub](https://github.com/settings/tokens/new). Sous « Sélectionner les étendues », nous allons cocher `public_repo` pour obtenir les informations de votre dépôt. Cliquez sur « Générer un token » et vous obtiendrez une clé à côté d'une coche verte !
2. Il est temps d'ajouter la clé à notre projet localement en tant que `keys.json` à la racine de notre projet :

```
{  "github": "<votre-clé-github>"}
```

Cependant, nous ne voulons pas que votre précieuse clé soit téléchargée sur votre dépôt GitHub. Ajoutez donc ce fichier à votre fichier `.gitignore` :

```
# misc.DS_Store.envnpm-debug.log*yarn-debug.log*yarn-error.log*keys.json
```

3. Maintenant que nous avons votre clé, nous pouvons ajouter une requête serveur. Installez Request dans votre projet avec `yarn add request` puis modifiez le fichier `index.js` de votre serveur :

```
import compression from 'compression';import express from 'express';import fs from 'fs';import request from 'request';
```

```
const app = express();const port = process.env.PORT || 8080;app.use(compression());
```

```
let keys;if (fs.existsSync('./keys.json')) {  keys = require('./keys.json');} else {  keys = JSON.parse(process.env.VCAP_SERVICES)['user-provided'][0].credentials;}
```

```
app.get('/github', (req, res) => {  request({    url: `https://api.github.com/user/repos?affiliation=owner,collaborator&access_token=${keys.github}`,    headers: {      'user-agent': 'node.js',    },  }, (err, response, body) => {    if (!err && response.statusCode === 200) {      res.send(body);    }  });});
```

```
app.use(express.static('./build'));
```

```
app.listen(port, (err) => {  if (err) {    console.log(err);    return;  }  console.log(`Le serveur est en ligne à l'adresse http://localhost:${port}`);});
```

Vous remarquerez d'abord une instruction if vérifiant si nous avons le fichier local `keys.json`. Le « else » dans cette instruction couvrira le cas où l'application est sur Bluemix plus tard. Nous avons ensuite un endpoint où pinguer `[http://localhost:8080/github](http://localhost:8080/github)` retournera les repos de votre profil !

4. Ouvrez `src/App.js` pour récupérer ces données vers votre interface utilisateur depuis votre serveur. Après ces ajouts, `yarn start` devrait montrer tous les repos de votre projet listés :

```
import React, { Component } from 'react';import logo from './logo.svg';import './App.css';
```

```
class App extends Component {
```

```
  state = {    repos: [],  }
```

```
  componentDidMount() {    fetch('/github')    .then(response => response.json())    .then((data) => {      const repos = data.map((repo) =>        <p key={repo.id}>{repo.name}</p>      );
```

```
      this.setState({ repos })    });  }
```

```
render() {    return (      <div className="App">        <div className="App-header">          <img src={logo} className="App-logo" alt="logo" />          <h2>Bienvenue dans React</h2>        </div>        <p className="App-intro">          Pour commencer, modifiez <code>src/App.js</code> et enregistrez pour recharger.        </p>        <h3>Repos du créateur de l'application :</h3>        {this.state.repos}      </div>    );  }}
```

```
export default App;
```

5. Maintenant que nous pouvons utiliser l'API GitHub de manière sécurisée en mode dev, assurons-nous que votre application Bluemix peut également obtenir la clé API. Nous allons créer un service fourni par l'utilisateur sur Bluemix dans le terminal : `cf cups keys -p keys.json`. Ensuite, dites au `manifest.json` que l'application doit toujours se lier à ce service :

```
---applications:- name: <nom-app>  buildpack: https://github.com/cloudfoundry/nodejs-buildpack  command: npm run bluemix  disk_quota: 256MB  memory: 128MB  services:     - keys
```

Note de côté : Si vous devez mettre à jour les clés sur Bluemix, vous pouvez exécuter `cf uups keys -p keys.json` !

#### ?????

Après que Travis ait mis à jour votre application Bluemix, vous devriez voir l'interface utilisateur récupérer tous vos repos en direct sur le web ! Nous avons fait beaucoup d'efforts pour garder les clés hors de github.com. Cela est dû au fait que d'autres développeurs peuvent abuser de vos clés API s'ils en obtiennent beaucoup.  
?????

### [Créer une application de staging pour l'expérimentation](https://github.com/seejamescode/create-react-app-devops/commit/e792b417e6a6b843516fd485668587bc9f513c04)

Maintenant que notre version de production de l'application a DevOps configuré, créons une application de staging. Cela nous aidera à partager les travaux en cours pour les tests utilisateurs et les revues par les pairs !

1. Nous devons créer un fichier manifest pour Bluemix qui spécifie notre nouvelle application de staging maintenant. À la racine de votre projet, créez un fichier `manifest-staging.yml` :

```
---applications:- name: <mon-app>-staging  buildpack: https://github.com/cloudfoundry/nodejs-buildpack  command: npm run bluemix  disk_quota: 256MB  memory: 128MB  services:     - keys
```

2. Allez-y et déployez cette application de staging directement sur Bluemix avec le nouveau fichier manifest : `cf push -f manifest-staging.yml`

3. Ensuite, nous allons modifier les scripts de déploiement dans `.travis.yml`. Nous devons changer le script de déploiement original pour qu'il mette à jour la nouvelle application de staging lorsque nous faisons un commit sur la branche master. Nous devons également ajouter un nouveau script de déploiement pour l'application de production originale :

```
deploy:  - edge: true    provider: script    script: if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then cf zero-downtime-push <mon-app>-staging -f ./manifest-staging.yml; else echo "PR skip deploy"; fi    skip_cleanup: true    on:      branch: master  - edge: true    provider: script    script: if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then cf zero-downtime-push <mon-app> -f ./manifest.yml; else echo "PR skip deploy"; fi    skip_cleanup: true    on:      tags: true
```

Ainsi, maintenant que nous mettons à jour l'application de staging en faisant un commit sur la branche master de GitHub, comment mettons-nous à jour l'application de production ? Vous utiliserez la [fonctionnalité Releases de GitHub](https://help.github.com/articles/creating-releases/) comme si votre application était une vraie offre. ?

4. Allez-y et poussez vos derniers changements vers GitHub ! Ensuite, naviguez vers « Releases » sur le dépôt GitHub et créez une nouvelle release.

#### ?????

Sur la base de la dernière étape, vous devriez voir deux builds en file d'attente sur Travis CI. L'un sera la mise à jour de l'application de staging en raison du dernier commit. L'autre sera la mise à jour de votre application de production en raison de la nouvelle release !  
?????

### La valeur finale et la plus importante de DevOps

Je veux terminer cet article en insistant sur la partie la plus importante de DevOps : **les tests automatisés**. Chaque fois que Travis s'exécute, y compris dans les pull requests ouvertes, il vérifiera que la commande `yarn test` passe avant de prendre des mesures. Create React App a déjà configuré `yarn test` avec [Jest](https://facebook.github.io/jest/). Cependant, vous pouvez ajouter des tests d'accessibilité, de linting et tout autre framework de test avec lequel vous êtes familier !

Pour résumer ce que nous avons fait : Tout d'abord, nous avons rapidement configuré notre projet React grâce à Create React App. Ensuite, nous avons construit un serveur simple. Nous avons poussé l'application dans le monde. Ensuite, nous avons obtenu Travis pour déployer l'application (avec zéro temps d'arrêt) pour tous nos changements. Puis nous avons utilisé l'API GitHub tout en gardant notre clé à l'abri des regards publics. Enfin, nous avons également configuré une application de staging afin que nous puissions tester la pré-release.

J'espère que ce projet a aidé à rendre votre flux de travail plus facile alors que vous créez des applications web épiques ! Un grand ? aux contributeurs de B[abel](https://github.com/babel/babel/graphs/contributors), C[reate React App](https://github.com/facebookincubator/create-react-app/graphs/contributors), E[xpress](https://github.com/expressjs/express/graphs/contributors), N[ode](https://github.com/nodejs/node/graphs/contributors), et tous les autres packages utilisés. De plus, tout l'amour ❤️ va à Bluemix, GitHub et Travis CI pour leurs niveaux gratuits.

Veuillez partager dans les commentaires ou [me tweeter](https://twitter.com/seejamescode) si cela vous a aidé ! J'adorerais également entendre parler de différents flux de travail !

Vous pouvez également me contacter en laissant un commentaire, [en m'envoyant un email](mailto:james@seejamescode.com), ou en tweettant à [@seejamescode](https://twitter.com/seejamescode). Je travaille à ATX pour IBM Design, et j'adore toujours les conversations avec la communauté de design web.

Vous pourriez également aimer...

[**Comment booster le score Google Lighthouse de votre application web progressive jusqu'à 100**](https://medium.freecodecamp.com/how-to-crank-your-progressive-web-apps-google-lighthouse-score-up-to-100-cfc053eb7661)  
[_Si l'équipe de développement de Chrome veut faire passer un message aux développeurs, c'est celui-ci : la performance compte._medium.freecodecamp.com](https://medium.freecodecamp.com/how-to-crank-your-progressive-web-apps-google-lighthouse-score-up-to-100-cfc053eb7661)

#### Consultez [Create React App DevOps sur GitHub](https://github.com/seejamescode/create-react-app-devops)
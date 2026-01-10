---
title: Comment s'assurer que votre Progressive Web App maintient son score d'audit
  Lighthouse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T21:01:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-sure-your-progressive-web-app-keeps-its-lighthouse-audit-score-4c11cf514e1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S5Da5dbVbwPIkDi6nS9uxg.png
tags:
- name: audit
  slug: audit
- name: Continuous Integration
  slug: continuous-integration
- name: JavaScript
  slug: javascript
- name: progressive web app
  slug: progressive-web-app
- name: technology
  slug: technology
seo_title: Comment s'assurer que votre Progressive Web App maintient son score d'audit
  Lighthouse
seo_desc: 'By Ondrej Chrastina

  I bet most of you have implemented a web application before. Some of you may even
  have created a Progressive Web App (PWA) that can act as a native app installed
  in a device. You’ve maybe followed my tips to make your app fully co...'
---

Par Ondrej Chrastina

Je parie que la plupart d'entre vous ont déjà implémenté une application web. Certains d'entre vous ont peut-être même créé une [Progressive Web App](http://bit.ly/create-pwa-with-angular-from-lighthouse) (PWA) qui peut agir comme une application native installée sur un appareil. Vous avez peut-être suivi [mes conseils](http://bit.ly/tune-pwa-score-from-lighthouse-ci) pour rendre votre application entièrement conforme aux règles et conventions PWA prescrites via l'outil d'audit Lighthouse.

Maintenant, ne serait-il pas agréable d'exécuter l'audit chaque fois que l'un de vos collègues met à jour la base de code ? Les accidents arrivent, et même si vous et vos collègues vous efforcez d'avoir une PWA conforme à 100 %, il est toujours bon de recevoir des avertissements précoces, immédiatement après chaque build.

Dans l'article suivant, je vais décrire comment vérifier la conformité automatiquement en intégrant l'audit PWA [Lighthouse](https://github.com/GoogleChrome/lighthouse) dans votre pipeline d'intégration continue.

Je vais commencer exactement là où je m'étais arrêté dans [mon article précédent](http://bit.ly/tune-pwa-score-from-lighthouse-ci) (c'est-à-dire, travailler avec l'application de voyage exemple qui liste des lieux intéressants à visiter). L'application stocke ses données dans le [Kentico Cloud headless CMS](http://bit.ly/kc-home-lighthouse) et elle répond à toutes les [exigences PWA](https://developers.google.com/web/progressive-web-apps/checklist). Après chaque étape d'implémentation, je fournirai un lien GitHub vers l'état du code pour vous permettre d'essayer les changements étape par étape, sans avoir besoin d'écrire le code vous-même.

![Image](https://cdn-media-1.freecodecamp.org/images/ChXsB7q9dIfEsqL0lsbUZndv6QTX7ylGCvC5)
_[État initial](https://github.com/Kentico/cloud-sample-angular-pwa-app/tree/8521c612e273fc91670a408488dc981ad7023895" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/KflsZQz0gDj0VvhSaG-WANi-Ywt7mldUigo1)
_Application exemple_

Je vais utiliser le [package npm Lighthouse](https://www.npmjs.com/package/lighthouse). Bien que Lighthouse puisse être utilisé directement depuis la ligne de commande, sa forme programmatique est meilleure car elle rapporte correctement le succès, l'échec et le score d'audit.

Je vais faire deux choses. D'abord, je vais montrer comment utiliser le package depuis la ligne de commande pour émettre une chaîne JSON avec les résultats de l'audit dans ma fenêtre de console. Ensuite, je vais montrer comment utiliser le package npm dans un pipeline d'intégration continue.

### Comment utiliser le package Lighthouse depuis la ligne de commande

Commençons par installer Lighthouse comme une dépendance de développement du projet.

```
npm install --save-dev lighthouse
```

Pour le déploiement, j'utilise le service [Surge](https://surge.sh/). Vous devez simplement vous inscrire sur son site et installer les outils CLI (dans l'exemple suivant, globalement). Ensuite, vous pouvez déployer le dossier dans un sous-domaine *.surge.sh.

```
npm install -g surge
```

* `surge /dist votre-sous-domaine.surge.sh` par exemple, déploie le dossier "dist" à l'URL spécifiée. Cela nécessite que vous vous connectiez ou [définissiez les variables d'environnement surge](https://docs.travis-ci.com/user/deployment/surge#Environment-variables) avec le login et le token.

Dans votre fichier `package.json`, définissez une URL publique où votre application sera déployée, comme suit :

```
{..."config": {   "deployUrl": "https://votre-sous-domaine.surge.sh"},...}
```

Lighthouse sera configuré pour effectuer l'audit contre cette URL. Mais pour cela, il doit attendre quelques secondes avant que l'application (ou une nouvelle version de celle-ci) ne devienne publiquement accessible.

Surge prend parfois son temps pour publier votre application. Par conséquent, vous devriez utiliser le package [npm-delay](https://www.npmjs.com/package/npm-delay) (ou quelque chose de similaire) pour attendre deux secondes avant d'effectuer l'audit. Passons à cela. Installez le package dans les dépendances de développement.

```
npm install --save-dev npm-delay
```

Une fois l'installation terminée, définissez la commande de script pour le déploiement en utilisant Surge vers votre URL. Ensuite, définissez la commande de script "lighthouse" qui construira l'application en mode production dans le dossier `dist`, utilisera la commande "deploy", attendra deux secondes (pour s'assurer que la dernière version de l'application est publiquement accessible), puis exécutera l'audit PWA contre l'URL de l'application.

```
{..."scripts": {    ...    "deploy": "surge dist %npm_package_config_deployUrl%",    "lighthouse": "npm run build && npm run deploy && npm-delay 2000 && lighthouse --chrome-flags=\"--headless\" --quiet --output=json %npm_package_config_deployUrl%",    ...  }...}
```

**D'accord, exécutons la commande :**

```
npm run lighthouse
```

Dans la console, vous verrez une grande chaîne JSON avec le résultat de l'audit. Ce que vous voulez inspecter est la propriété `reportCategories`, sa partie interne (rapport) nommée "Progressive Web App" avec sa propriété appelée `score`.

```
{  ...  "reportCategories": [    ....    {      "name": "Progressive Web App",      ...      "id": "pwa",      "score": 100    }  ...  ]}
```

![Image](https://cdn-media-1.freecodecamp.org/images/Nm21thuCToMlkcU0XKWVq7S910-BZhMQNvfU)
_[Vérification Lighthouse](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/16da5916da8c14cbe090ce38cef73a93c0d90b31" rel="noopener" target="_blank" title=")_

### Ajouter la vérification Lighthouse au pipeline d'intégration continue

Pour intégrer l'audit PWA dans le pipeline CI, nous pouvons utiliser l'approche [programmatique](https://github.com/GoogleChrome/lighthouse/blob/master/docs/readme.md#using-programmatically) de l'utilisation de Lighthouse. Tout d'abord, vous voudrez définir le script JavaScript qui vérifiera le score de votre PWA.

Le script utilise l'URL définie dans le fichier `package.json`. Dans ce script, il y a une fonction utilisée pour exécuter [Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome) et effectuer l'audit Lighthouse sur celui-ci. Une fois l'audit terminé, le script attendra deux secondes pour être sûr que votre application est déployée et accessible. Enfin, le script sélectionne la valeur de la chaîne JSON du résultat de l'audit et vérifie si elle répond au niveau de score défini — 100 dans ce cas. Sinon, il retourne le code de sortie 1, ce qui provoquera l'échec de la construction [Travis CI](http://travis-ci.org).

```
const lighthouse = require('lighthouse');const chromeLauncher = require('chrome-launcher');const appConfig = require('./package');
```

```
const opts = {    chromeFlags: ['--headless']};
```

```
function launchChromeAndRunLighthouse(url, opts, config = null) {    return chromeLauncher.launch({ chromeFlags: opts.chromeFlags }).then(chrome => {        opts.port = chrome.port;        return lighthouse(url, opts, config).then(results => {            delete results.artifacts;            return chrome.kill().then(() => results);        });    });}
```

```
launchChromeAndRunLighthouse(appConfig.config.deployUrl, opts).then(results => {    setTimeout(() => {      if (results.reportCategories.filter((item) => item.id === "pwa").length) {        const score = results.reportCategories.filter((item) => item.id === "pwa")[0].score        if (score >= 100) {            console.info(`Le score PWA est de 100.`);            process.exit(0);        }        console.error(`Le score est inférieur à 100. Il est de ${score}`);        process.exit(1);    }    console.error(`Aucun score PWA fourni par lighthouse.`);    process.exit(1);    }, 2000);    });
```

Définissons le nouveau script dans le fichier `package.json`.

```
{...    "scripts": {    ...    "check-pwa-score": "node checkLighthouse.js"    ...    }...}
```

Enfin, déclenchez la construction Travis et **publiez une PWA conforme à 100 % !**

J'utilise un fichier yaml pour la configuration Travis. Basiquement, vous vous connectez simplement à [ce service](https://travis-ci.org/) avec votre compte GitHub, activez le CI pour le dépôt dans l'interface utilisateur Travis, puis vous commitez simplement le fichier `.travis.yml` à la racine de votre dépôt.

```
sudo: requireddist: trustylanguage: node_jsnode_js:- "stable"before_script:- npm installbefore_deploy:- npm run builddeploy:  provider: surge  project: ./dist/  domain: https://kentico-cloud-sample-angular-pwa-app.surge.sh   skip_cleanup: trueafter_deploy:- npm run check-pwa-score
```

Comme vous pouvez le voir en bas, il y a une action après le déploiement qui vérifie le score d'audit PWA.

![Image](https://cdn-media-1.freecodecamp.org/images/OBVHa6yT8a1O7xzmQOllT9wfW2c9xTUWI8VU)
_[Ajouter l'audit PWA au pipeline CI](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/5e5a6999cb499345808ea5833f40a293c0b4632c" rel="noopener" target="_blank" title=")_

**Voilà ! Votre pipeline de construction vérifie maintenant automatiquement le score d'audit PWA.**

![Image](https://cdn-media-1.freecodecamp.org/images/RfocjMvvihEm9D-0xbCLr7uURJVZ1aGknXNT)

Désormais, si l'un de vos collègues compromet la conformité de votre application PWA, ils seront immédiatement avertis par Travis.

### Mots de la fin

Bon travail ! Si vous avez suivi les étapes, vous avez ajouté avec succès le package npm Lighthouse pour obtenir la chaîne JSON avec les résultats dans la console.

Vous avez également configuré les choses pour publier automatiquement votre application, attendre deux secondes et utiliser la fonctionnalité Lighthouse dans Headless Chrome pour vérifier votre score dans un pipeline Travis CI.

Maintenant, vous n'avez plus à perdre le sommeil pour votre application précieuse !
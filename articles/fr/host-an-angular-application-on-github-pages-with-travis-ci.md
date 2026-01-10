---
title: Comment héberger une application Angular sur GitHub Pages avec Travis CI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-19T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/host-an-angular-application-on-github-pages-with-travis-ci
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/angular-travisci-cover.png
tags:
- name: Angular
  slug: angular
- name: GitHub
  slug: github
- name: github pages
  slug: github-pages
- name: Travis CI
  slug: travis-ci
seo_title: Comment héberger une application Angular sur GitHub Pages avec Travis CI
seo_desc: 'By Rodrigo Kamada

  In this article, we''ll create an application using the latest version of Angular.
  Then we''ll host it on the GitHub Pages static website service using the continuous
  integration tool Travis CI to deploy the application.

  Prerequisites...'
---

Par Rodrigo Kamada

Dans cet article, nous allons créer une application en utilisant la dernière version d'Angular. Ensuite, nous allons l'héberger sur le service de site web statique GitHub Pages en utilisant l'outil d'intégration continue Travis CI pour déployer l'application.

## Prérequis

Avant de commencer, vous devez installer et configurer les outils ci-dessous pour créer l'application Angular.

* [Git](https://git-scm.com/): Git est un système de contrôle de version distribué que nous utiliserons pour synchroniser le dépôt.
* [Node.js et npm](https://nodejs.org/): Node.js est un logiciel d'exécution de code JavaScript basé sur le moteur V8 de Google. npm est un gestionnaire de paquets pour Node.js (Node Package Manager). Nous les utiliserons pour construire et exécuter l'application Angular et installer les bibliothèques.
* [Angular CLI](https://angular.io/cli): Angular CLI est un outil utilitaire en ligne de commande pour Angular que nous utiliserons pour créer la structure de base de l'application Angular.
* Un IDE (comme [Visual Studio Code](https://code.visualstudio.com/) ou [WebStorm](https://www.jetbrains.com/webstorm/)): un IDE (Environnement de Développement Intégré) est un outil avec une interface graphique qui nous aide à développer des applications. Ici, nous en utiliserons un pour développer l'application Angular.

## Pour commencer

### Créer et configurer votre compte sur GitHub

[GitHub](https://github.com/) est un service de stockage de code source et de fichiers avec contrôle de version utilisant l'outil Git. Et [GitHub Pages](https://pages.github.com/) est un service d'hébergement de fichiers statiques utilisant un dépôt public.

Tout d'abord, vous devrez créer un compte sur GitHub si vous n'en avez pas déjà un. Visitez [https://github.com/](https://github.com/) et cliquez sur le bouton _Sign up_.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step1.png)

Remplissez les champs pour Username, Email address, et Password, cliquez sur le bouton Verify pour résoudre le défi, puis cliquez sur le bouton Create account.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step2.png)

Ensuite, nous allons générer le token qui sera utilisé dans Travis CI. Cliquez sur le menu avec l'avatar et cliquez sur le menu Settings.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step3.png)

Cliquez sur le menu Developer settings.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step4.png)

Cliquez sur le menu Personal access tokens.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step5.png)

Cliquez sur le bouton Generate new token.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step6.png)

Remplissez le champ Note, sélectionnez l'option repo et cliquez sur le bouton Create token.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step7.png)

Copiez le token généré. Dans mon cas, le token `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` a été généré car ce token sera configuré dans Travis CI.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step8.png)

Créons le dépôt. Cliquez sur le menu avec l'avatar et cliquez sur le menu Your repositories.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step9.png)

Cliquez sur le bouton New.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step10.png)

Remplissez le champ Repository name et cliquez sur le bouton Create repository.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step11.png)

Prêt ! Compte créé, token généré, et dépôt [`https://github.com/rodrigokamada/angular-travisci`](https://github.com/rodrigokamada/angular-travisci) créé.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/github-step12.png)

### Créer et configurer votre compte sur Travis CI

[Travis CI](https://www.travis-ci.com/) est un service de déploiement intégré avec GitHub.

Tout d'abord, vous devrez créer un compte Travis CI si vous n'en avez pas déjà un. Visitez [https://travis-ci.com/](https://travis-ci.com/) et cliquez sur le bouton Sign up.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/travisci-step1.png)

Cliquez sur le bouton SIGN IN WITH GITHUB pour vous connecter avec votre compte GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/travisci-step2.png)

Si Travis CI demande la permission de lister les dépôts GitHub, acceptez la demande. Cliquez sur le lien du dépôt angular-travisci.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/travisci-step3.png)

Configurons le token d'accès GitHub. Cliquez sur le menu More options et cliquez sur le menu Settings.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/travisci-step4.png)

Remplissez le champ NAME avec la valeur GITHUB_TOKEN, VALUE avec la valeur de votre token généré sur GitHub, et cliquez sur le bouton Add.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/travisci-step5.png)

Prêt ! Compte créé et dépôt configuré.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/travisci-step6.png)

### Créer votre application Angular

[Angular](https://angular.io/) est une plateforme de développement pour construire des applications Web, mobiles et de bureau en utilisant HTML, CSS et TypeScript (JavaScript). Actuellement, Angular est à la version 13 et Google est le principal mainteneur du projet.

Créons l'application avec la structure de base Angular en utilisant `@angular/cli` avec le fichier de route et le format de style SCSS.

```powershell
? Would you like to add Angular routing? Yes
? Which stylesheet format would you like to use? SCSS   [ https://sass-lang.com/documentation/syntax#scss                ]
CREATE angular-travisci/README.md (1061 bytes)
CREATE angular-travisci/.editorconfig (274 bytes)
CREATE angular-travisci/.gitignore (604 bytes)
CREATE angular-travisci/angular.json (3267 bytes)
CREATE angular-travisci/package.json (1078 bytes)
CREATE angular-travisci/tsconfig.json (783 bytes)
CREATE angular-travisci/.browserslistrc (703 bytes)
CREATE angular-travisci/karma.conf.js (1433 bytes)
CREATE angular-travisci/tsconfig.app.json (287 bytes)
CREATE angular-travisci/tsconfig.spec.json (333 bytes)
CREATE angular-travisci/src/favicon.ico (948 bytes)
CREATE angular-travisci/src/index.html (301 bytes)
CREATE angular-travisci/src/main.ts (372 bytes)
CREATE angular-travisci/src/polyfills.ts (2820 bytes)
CREATE angular-travisci/src/styles.scss (80 bytes)
CREATE angular-travisci/src/test.ts (743 bytes)
CREATE angular-travisci/src/assets/.gitkeep (0 bytes)
CREATE angular-travisci/src/environments/environment.prod.ts (51 bytes)
CREATE angular-travisci/src/environments/environment.ts (658 bytes)
CREATE angular-travisci/src/app/app-routing.module.ts (245 bytes)
CREATE angular-travisci/src/app/app.module.ts (393 bytes)
CREATE angular-travisci/src/app/app.component.scss (0 bytes)
CREATE angular-travisci/src/app/app.component.html (23809 bytes)
CREATE angular-travisci/src/app/app.component.spec.ts (1087 bytes)
CREATE angular-travisci/src/app/app.component.ts (221 bytes)
✔ Packages installed successfully.
    Successfully initialized git.
```

Créez le fichier `.travis.yml`.

```powershell
touch .travis.yml
```

Configurez le fichier `.travis.yml` avec le contenu ci-dessous :

```yaml
notifications:
  email:
    recipients:
      - rodrigo@kamada.com.br

language: node_js

node_js:
  - 16

before_script:
  - npm install

script:
  - npm run test:headless

before_deploy:
  - npm run build:prod

deploy:
  provider: pages
  skip_cleanup: true
  github_token: $GITHUB_TOKEN
  local_dir: dist/angular-travisci
  on:
    branch: main
```

Modifiez le fichier `package.json` et ajoutez les scripts ci-dessous. Remplacez la valeur `rodrigokamada` par votre nom d'utilisateur GitHub.

```json
  "build:prod": "ng build --prod --base-href https://rodrigokamada.github.io/angular-travisci/",
  "test:headless": "ng test --watch=false --browsers=ChromeHeadless"
```

Modifiez le fichier `src/app/app.component.spec.ts` et supprimez les tests `should have as title 'angular-travisci'` et `should render title`.

Exécutez le test avec la commande ci-dessous :

```powershell
npm run test:headless

> angular-travisci@1.0.0 test:headless
> ng test --watch=false --browsers=ChromeHeadless

🔹 Generating browser application bundles (phase: setup)...Compiling @angular/core/testing : es2015 as esm2015
Compiling @angular/compiler/testing : es2015 as esm2015
Compiling @angular/platform-browser/testing : es2015 as esm2015
Compiling @angular/common/testing : es2015 as esm2015
Compiling @angular/platform-browser-dynamic/testing : es2015 as esm2015
Compiling @angular/router/testing : es2015 as esm2015
✨ Generating browser application bundles (phase: building)...05 09 2021 19:40:04.329:INFO [karma-server]: Karma v6.3.4 server started at http://localhost:9876/
05 09 2021 19:40:04.331:INFO [launcher]: Launching browsers ChromeHeadless with concurrency unlimited
05 09 2021 19:40:04.369:INFO [launcher]: Starting browser ChromeHeadless
✔ Browser application bundle generation complete.
05 09 2021 19:40:09.704:INFO [Chrome Headless 92.0.4515.159 (Linux x86_64)]: Connected on socket NUtJhjavb1JvssqOAAAB with id 25989029
Chrome Headless 92.0.4515.159 (Linux x86_64): Executed 1 of 1 SUCCESS (0.068 secs / 0.042 secs)
TOTAL: 1 SUCCESS
```

Exécutez l'application avec la commande ci-dessous. Accédez à l'URL `http://localhost:4200/` et vérifiez si l'application fonctionne.

```powershell
npm start

> angular-travisci@1.0.0 start
> ng serve

✔ Browser application bundle generation complete.

Initial Chunk Files | Names         |      Size
vendor.js           | vendor        |   2.39 MB
polyfills.js        | polyfills     | 128.51 kB
main.js             | main          |   8.89 kB
runtime.js          | runtime       |   6.63 kB
styles.css          | styles        |   1.18 kB

                    | Initial Total |   2.53 MB

Build at: 2021-09-05T22:35:38.010Z - Hash: a4cfc9149589386eca5b - Time: 39997ms

** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **


✔ Compiled successfully.
```

Construisez l'application avec la commande ci-dessous :

```powershell
npm run build:prod

> angular-travisci@1.0.0 build:prod
> ng build --configuration production --base-href https://rodrigokamada.github.io/angular-travisci/

✔ Browser application bundle generation complete.
✔ Copying assets complete.
✔ Index html generation complete.

Initial Chunk Files           | Names         |      Size
main.c678fa8750e7c769.js      | main          | 177.63 kB
polyfills.6d7801353e02e327.js | polyfills     |  36.21 kB
runtime.b136bda8a38c4f2e.js   | runtime       |   1.06 kB
styles.ef46db3751d8e999.css   | styles        |   0 bytes

                              | Initial Total | 214.90 kB

Build at: 2021-09-05T22:42:19.525Z - Hash: 83bfffc079b083727ca4 - Time: 26030ms
```

Synchronisez l'application sur le dépôt GitHub que vous avez créé.

Prêt ! Après avoir synchronisé l'application sur le dépôt GitHub, Travis CI construit l'application et la synchronise sur la branche `gh-pages`.

Accédez à l'URL [`https://rodrigokamada.github.io/angular-travisci/`](https://rodrigokamada.github.io/angular-travisci/) et vérifiez si l'application fonctionne. Remplacez la valeur `rodrigokamada` par votre nom d'utilisateur GitHub.

Et c'est tout ! Le dépôt de l'application est disponible à l'adresse [https://github.com/rodrigokamada/angular-travisci](https://github.com/rodrigokamada/angular-travisci).

## Conclusion

Résumé de ce qui a été couvert dans cet article :

* Nous avons créé un compte sur GitHub.
* Nous avons créé un token d'accès sur GitHub.
* Nous avons créé un dépôt sur GitHub.
* Nous avons créé un compte sur Travis CI.
* Nous avons configuré le token d'accès GitHub sur Travis CI.
* Nous avons créé une application Angular.

Vous pouvez utiliser cet article pour créer votre site web personnel et avoir un portfolio en ligne.

Merci d'avoir lu et j'espère que vous avez apprécié l'article !

Pour rester informé chaque fois que je publie de nouveaux articles, suivez-moi sur [Twitter](https://twitter.com/rodrigokamada).

Ce tutoriel a été publié sur mon [blog](https://rodrigo.kamada.com.br/share/blog/hospedando-uma-aplicacao-angular-no-github-pages-usando-o-travis-ci) en portugais.
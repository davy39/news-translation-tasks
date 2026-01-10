---
title: Qu'est-ce que le Smoke Testing ? Explication des tests de vérification de build
  avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-23T23:02:05.000Z'
originalURL: https://freecodecamp.org/news/smoke-testing
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/What-is-smoke-testing_--5-.png
tags:
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
seo_title: Qu'est-ce que le Smoke Testing ? Explication des tests de vérification
  de build avec des exemples
seo_desc: 'By Laura Cressman

  This may sound familiar: someone pushed code to production and now a critical feature
  is broken. How can you prevent this from happening in the future?

  via GIPHY

  In this tutorial, you''ll learn about smoke testing and how it helps ca...'
---

Par Laura Cressman

Cela peut sembler familier : quelqu'un a poussé du code en production et maintenant une fonctionnalité critique est cassée. Comment pouvez-vous empêcher cela de se reproduire à l'avenir ?

<iframe src="https://giphy.com/embed/143vPc6b08locw" width="480" height="364" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p align="center"><a href="https://giphy.com/gifs/fail-code-boat-143vPc6b08locw">via GIPHY</a></p>

Dans ce tutoriel, vous apprendrez ce qu'est le smoke testing et comment il aide à attraper les bugs. Vous allez ensuite effectuer un smoke test sur une application web selon un calendrier, et envoyer des alertes lorsque les tests échouent. Commençons !

<h1>Table des matières</h1>

1. [Qu'est-ce que le smoke testing ?](#heading-1-questce-que-le-smoke-testing)
2. [Pourquoi devriez-vous vous en soucier ?](#heading-2-pourquoi-devriez-vous-vous-en-soucier)
3. [Configurer votre projet](#heading-3-configurer-votre-projet)
4. [Créer un smoke test](#heading-4-creer-un-smoke-test)
5. [Revoir le code de test](#heading-5-revoir-le-code-de-test)
6. [Exécuter votre test localement](#heading-6-executer-votre-test-localement)
7. [Exécuter les tests dans GitHub Actions](#heading-7-executer-les-tests-dans-github-actions)
8. [Configurer des alertes avec Slack](#heading-8-configurer-des-alertes-avec-slack)
9. [Conclusion](#heading-9-conclusion)

<h1 id="questce-que-le-smoke-testing">1. Qu'est-ce que le smoke testing ?</h1>

Le terme "smoke test" trouve son origine dans la réparation matérielle. Un appareil était allumé, et échouait le smoke test s'il prenait feu. 💨 Le smoke testing est parfois appelé "build verification testing".

Lorsque cela est appliqué aux applications web, les smoke tests vérifient que les fonctionnalités les plus importantes fonctionnent. Par exemple, les smoke tests sur Netflix pourraient inclure la connexion et la lecture d'une vidéo.

Par conception, les smoke tests ne couvrent pas toutes les permutations et cas particuliers. Ils vérifient plutôt que votre application n'est pas si cassée que des tests supplémentaires seraient une perte de temps.

<h1 id="pourquoi-devriez-vous-vous-en-soucier">2. Pourquoi devriez-vous vous en soucier ?</h1>

Les smoke tests offrent beaucoup de valeur par rapport à l'effort nécessaire pour les créer. [Selon Microsoft](https://docs.microsoft.com/en-us/previous-versions/ms182613(v=vs.80)), les smoke tests sont "la méthode la plus rentable pour identifier et corriger les défauts dans les logiciels" après les revues de code.

<iframe src="https://giphy.com/embed/l3V0wpHLf2qOEwegE" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p align="center"><a href="https://giphy.com/gifs/chuber-possum-opossum-awesome-l3V0wpHLf2qOEwegE">via GIPHY</a></p>

Quelques tests de fonctionnalités critiques comme la connexion peuvent améliorer significativement la qualité. Tester ce que les utilisateurs font le plus souvent aide à garantir que les principaux cas d'utilisation de votre application sont supportés. 💡

Les smoke tests donnent également à votre équipe la confiance de livrer un nouveau code. Les changements dans votre base de code ont souvent des conséquences imprévues et inconnues. Les smoke tests offrent une tranquillité d'esprit supplémentaire que votre application ne se cassera pas lorsque vous publierez cette nouvelle fonctionnalité géniale.

Si vous exécutez des smoke tests en production, vous pouvez également attraper des bugs que les tests précédents ont manqués. Même de petites différences entre les environnements comme la pré-production et la production peuvent causer des problèmes. Les smoke tests peuvent identifier ces problèmes avant qu'un client ne le fasse.

En bref, les smoke tests vous offrent une autre couche de protection contre une mauvaise expérience utilisateur. Une application qui fonctionne sans accroc aide votre équipe, votre entreprise et vos clients à être plus performants. **✨**

<h1 id="configurer-votre-projet">3. Configurer votre projet</h1>

Maintenant que nous avons appris ce qu'est le smoke testing, construisons un pipeline de smoke testing !

<iframe src="https://giphy.com/embed/Q6p2n7oHvEjok" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p align="center"><a href="https://giphy.com/gifs/dog-tower-blocks-Q6p2n7oHvEjok">via GIPHY</a></p>

Ce tutoriel suppose que vous [comprenez la ligne de commande](https://guide.freecodecamp.org/linux/the-command-prompt), [avez Node.js et `npm` installés](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm), et [connaissez les bases de JavaScript](https://guide.freecodecamp.org/javascript/additional-javascript-resources) et [Git](https://guide.freecodecamp.org/git).

Vous pouvez configurer vos tests à l'intérieur d'un projet existant, ou en créer un nouveau. Pour créer un nouveau projet, exécutez les commandes suivantes dans la ligne de commande.

```bash
mkdir smoke_tests
cd smoke_tests
```

Si vous ne l'avez pas déjà fait, initialisez votre projet afin de pouvoir installer les packages [Node.js](https://nodejs.org/en).

```bash
npm init -y
```

Maintenant, installons les outils dont nous avons besoin pour créer nos smoke tests. Ce tutoriel créera des tests [Playwright](https://github.com/microsoft/playwright) et [Jest](https://jestjs.io) sur une application web. Playwright est une bibliothèque construite par Microsoft pour automatiser les navigateurs [Chromium](https://www.chromium.org/Home), [Firefox](https://www.mozilla.org/en-US/firefox), et [WebKit](https://webkit.org). Jest est un framework pour créer et exécuter des tests JavaScript.

Pour créer et exécuter rapidement nos tests, nous utiliserons la bibliothèque open source [QA Wolf](https://github.com/qawolf/qawolf) que j'aide à maintenir. QA Wolf convertit vos actions de navigateur en code de test Playwright/Jest. Il exécute également vos tests dans un fournisseur CI comme [GitHub Actions](https://github.com/features/actions).

Si vous préférez utiliser un autre framework de test, vous pouvez toujours suivre ce tutoriel pour exécuter vos tests en CI et configurer des alertes.

Pour configurer votre projet pour les smoke tests, exécutez la commande suivante dans votre répertoire de projet.

```bash
npm init qawolf
```

Vous serez invité à spécifier le répertoire où vos tests seront sauvegardés. Appuyez sur Entrée pour utiliser le répertoire par défaut `.qawolf`, ou tapez un nom différent.

```bash
? rootDir: Répertoire pour créer les tests (.qawolf)
```

Vous verrez ensuite une note dans la ligne de commande indiquant si vos tests utiliseront [TypeScript](https://www.typescriptlang.org/). Notre projet d'exemple n'a pas de fichier "tsconfig.json", donc nos tests n'utiliseront pas TypeScript.

```bash
TypeScript ❌ tsconfig.json non trouvé
```

La dernière étape consiste à choisir votre fournisseur CI. Ce tutoriel utilisera GitHub Actions, mais vous pouvez choisir un autre fournisseur si vous le souhaitez. Sélectionnez votre fournisseur CI dans la ligne de commande et appuyez sur Entrée. 

```bash
? Choisir le fournisseur CI (Utilisez les touches fléchées)
  Azure DevOps 
  Bitbucket Pipelines 
  CircleCI 
✨ GitHub Actions 
  GitLab CI/CD 
  Jenkins 
  Sauter la configuration CI 
```

Les packages nécessaires pour les smoke tests (Playwright, Jest, et QA Wolf) seront alors installés.

Deux fichiers seront également créés dans votre projet. Le premier est un fichier de workflow pour exécuter vos tests en CI. Puisque nous avons sélectionné GitHub Actions, ce fichier est sauvegardé dans ".github/workflows/qawolf.yml". Nous discuterons de ce fichier [plus tard](#heading-7-executer-les-tests-dans-github-actions). 

Il y a également un fichier de configuration créé dans "qawolf.config.js". Nous n'aurons pas besoin de modifier ce fichier, mais vous pouvez [en apprendre plus à ce sujet ici](https://docs.qawolf.com/docs/configure_qa_wolf).

Après que les dépendances aient fini de s'installer, vérifiez que l'installation a réussi.

```
npx qawolf howl
```

<h1 id="creer-un-smoke-test">4. Créer un smoke test</h1>

Maintenant que notre projet est configuré, créons notre premier smoke test. Dans ce tutoriel, nous allons créer un smoke test sur [TodoMVC](http://todomvc.com/examples/react), une application simple de liste de tâches. Plus précisément, nous allons tester que nous pouvons 

1. créer un élément de todo,
2. le compléter, et
3. effacer les todos complétés.

Pour créer notre test, nous allons utiliser la commande [`npx qawolf create`](https://docs.qawolf.com/docs/api/cli#npx-qawolf-create-url-name). Cette commande prend l'URL de votre application et un nom de test optionnel. L'exécution de cette commande ouvrira un navigateur [Chromium](https://www.chromium.org/Home) où vos actions seront converties en code Playwright/Jest. 

Dans la ligne de commande, exécutez ce qui suit. Vous pouvez optionnellement remplacer [`http://todomvc.com/examples/react`](http://todomvc.com/examples/react) par une URL différente, et `myFirstTest` par un nom différent.

```bash
npx qawolf create http://todomvc.com/examples/react myFirstTest
```

Ouvrez votre éditeur de code et trouvez votre fichier de test (".qawolf/myFirstTest.test.js" dans notre exemple). C'est là que votre code de test sera créé lorsque vous utiliserez le navigateur.

Une fois que le navigateur Chromium s'est ouvert sur TodoMVC, effectuez les actions suivantes.

1. Cliquez sur l'entrée de todo pour la focaliser
2. Tapez "créer un test !"
3. Appuyez sur Entrée
4. Cliquez pour compléter le todo
5. Cliquez sur "Effacer les complétés" pour effacer les todos complétés
6. Dans la ligne de commande, surlignez `? Enregistrer et Quitter` et appuyez sur Entrée pour sauvegarder votre test

La vidéo ci-dessous fournit un exemple.

%[https://youtu.be/KP4tpilrOOE]

<h1 id="revoir-le-code-de-test">5. Revoir le code de test</h1>

Maintenant, examinons notre code de test. Dans votre éditeur de code, ouvrez votre fichier de test (".qawolf/myFirstTest.test.js" dans notre exemple). 

Au début de notre test, nous importons `qawolf`. Nous importons également les sélecteurs d'éléments depuis ".qawolf/selectors/myFirstTest.json", que nous discuterons dans un instant.

```js
const qawolf = require("qawolf");
const selectors = require("./selectors/myFirstTest.json");
```

Le test lance ensuite un [navigateur Playwright](https://github.com/microsoft/playwright/blob/master/docs/api.md#class-browser), qui dans notre cas est un navigateur Chromium. Il crée un nouveau [contexte de navigateur Playwright](https://github.com/microsoft/playwright/blob/master/docs/api.md#class-browsercontext), qui est une session de navigateur incognito. QA Wolf est donné accès au `contexte` afin qu'il puisse détecter vos actions. Enfin, une nouvelle [page Playwright](https://github.com/microsoft/playwright/blob/master/docs/api.md#class-page) est créée, ouvrant un nouvel onglet dans le navigateur. 

```js
let browser;
let page;

beforeAll(async () => {
  browser = await qawolf.launch();
  const context = await browser.newContext();
  await qawolf.register(context);
  page = await context.newPage();
});
```

Le test lui-même est contenu dans un bloc [Jest `test`](https://jestjs.io/docs/en/api#testname-fn-timeout) avec le nom que vous avez spécifié. Le test navigue d'abord vers l'URL de TodoMVC. Il passe ensuite par les actions que vous avez effectuées : créer un élément de todo, le compléter et effacer les todos complétés. Chaque action utilise l'une des méthodes `page` de Playwright, comme `click` et `type`.

```js
test('myFirstTest', async () => {
  await page.goto("http://todomvc.com/examples/react");
  await page.click(selectors["0_what_needs_to_b_input"]);
  await page.type(selectors["1_what_needs_to_b_input"], "créer un test !");
  await page.press(selectors["2_what_needs_to_b_input"], "Enter");
  await page.click(selectors["3_input"]);
  await page.click(selectors["4_button"]);
});
```

Le premier argument passé à chaque méthode `page` est un sélecteur [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML). Ce sélecteur indique à Playwright quel élément interagir, comme l'entrée de todo ou le bouton "Effacer les complétés". Ces sélecteurs sont importés depuis le fichier ".qawolf/selectors/myFirstTest.json", qui ressemble à ce qui suit.

```json
{
 "0_what_needs_to_b_input": "html=<div data-reactid=\".0\" qaw_innertext=\"todos\"><header class=\"header\" data-reactid=\".0.0\" qaw_innertext=\"todos\"><input class=\"new-todo\" placeholder=\"What needs to be done?\" value=\"\" data-reactid=\".0.0.1\" /></header></div>",
// ...
}

```

Chaque attribut de l'élément avec lequel vous avez interagi, ainsi que ceux de ses deux [ancêtres](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentElement), est stocké dans ce fichier. Lorsque vous exécutez votre test, il fera de son mieux pour trouver une correspondance suffisamment bonne avec le HTML spécifié. En ne dépendant pas d'un seul attribut, vos tests sont plus robustes face aux changements dans votre code front-end.

Les méthodes Playwright `page` [supportent également](https://github.com/microsoft/playwright/blob/master/docs/api.md#working-with-selectors) d'autres types de sélecteurs, tels que les [sélecteurs CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) ou les sélecteurs de texte. Par exemple, vous pouvez remplacer `selectors["4_button"]` dans la dernière étape par le sélecteur CSS `'.clear-completed'`.

```js
test('myFirstTest', async () => {
  // ...
  // changez ceci
  await page.click(selectors["4_button"]);
  // par ceci (sélecteur CSS)
  await page.click('.clear-completed');
});
```

Vous pouvez optionnellement configurer QA Wolf pour utiliser des attributs de test comme `data-qa` dans le code généré chaque fois que possible. Voir [ce guide](https://docs.qawolf.com/docs/use_custom_selectors) pour en apprendre plus.

Après que le test ait fini de s'exécuter, QA Wolf arrête l'enregistrement de toute vidéo du navigateur si applicable. Le navigateur est également fermé.

```js
afterAll(async () => {
  await qawolf.stopVideos();
  await browser.close();
});
```

En mettant tout ensemble, le code de test complet ressemble à ceci.

```js
const qawolf = require("qawolf");
const selectors = require("./selectors/myFirstTest.json");

let browser;
let page;

beforeAll(async () => {
  browser = await qawolf.launch();
  const context = await browser.newContext();
  await qawolf.register(context);
  page = await context.newPage();
});

afterAll(async () => {
  await qawolf.stopVideos();
  await browser.close();
});

test("myFirstTest", async () => {
  await page.goto("http://todomvc.com/examples/react");
  await page.click(selectors["0_what_needs_to_b_input"]);
  await page.type(selectors["1_what_needs_to_b_input"], "créer un test !");
  await page.press(selectors["2_what_needs_to_b_input"], "Enter");
  await page.click(selectors["3_input"]);
  await page.click(selectors["4_button"]);
});
```

Si le test ne peut pas compléter le workflow, il échouera. Vous êtes libre de modifier votre code de test, par exemple en ajoutant des assertions. Nous n'aborderons pas cela dans ce tutoriel, mais [voici un guide](https://docs.qawolf.com/docs/add_assertions) si vous souhaitez en apprendre plus.

Maintenant que nous comprenons notre code de test, exécutons notre test !

<h1 id="executer-votre-test-localement">6. Exécuter votre test localement</h1>

Exécutons notre test localement pour nous assurer qu'il fonctionne. Dans la ligne de commande, exécutez ce qui suit pour exécuter votre/vos test(s) avec Jest.

```bash
npx qawolf test
```

Vous devriez voir un navigateur Chromium s'ouvrir et exécuter le test. Votre test s'exécutera aussi vite que possible, alors ne soyez pas surpris s'il s'exécute rapidement.

La vidéo ci-dessous fournit un exemple.

%[https://youtu.be/JRcR-d6Yfdw]

<h1 id="executer-les-tests-dans-github-actions">7. Exécuter les tests dans GitHub Actions</h1>

Dans ce tutoriel, nous allons exécuter nos tests selon un calendrier, par exemple toutes les heures. Exécuter des tests selon un calendrier garantit que votre application fonctionne de manière continue. Cela peut également exposer des problèmes périodiques, ou "flakes", qui n'apparaissent que parfois.

Dans ce tutoriel, nous utilisons [GitHub Actions](https://github.com/features/actions) pour exécuter nos tests. GitHub Actions est un outil pour automatiser les workflows logiciels, comme le déploiement d'un service web ou le test d'une application.

<h2>Revoir le fichier de workflow</h2>

Lorsque nous avons [configuré notre projet](#heading-3-configurer-votre-projet), un fichier [YAML](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions) appelé ".github/workflows/qawolf.yml" a été créé. Nous allons d'abord passer brièvement en revue les différentes parties de ce fichier. Nous le mettrons ensuite à jour pour que nos tests s'exécutent selon un calendrier.

La première ligne du fichier de workflow nomme notre workflow. C'est le nom qui apparaîtra dans GitHub Actions, et vous pouvez le changer si vous le souhaitez.

```yaml
name: qawolf
```

La clé [`on`](https://www.freecodecamp.org/news/p/ad7d7d20-5b22-4ae2-84a1-07b00eb0cdb3/La%20première%20partie%20du%20fichier%20de%20workflow%20nomme%20notre%20workflow%20name:%20qawolf.%20C'est%20le%20nom%20qui%20apparaîtra%20dans%20GitHub%20Actions,%20et%20vous%20pouvez%20le%20changer%20si%20vous%20le%20souhaitez.) spécifie ensuite quel événement doit déclencher l'exécution de nos tests. Par défaut, vos tests s'exécuteront chaque fois que quelqu'un poussera vers n'importe quelle branche. Nous allons bientôt modifier cela pour également exécuter nos tests selon un calendrier.

```yaml
on:
  push:
    # tester chaque branche
    # modifier ci-dessous si vous ne voulez tester que certaines branches
    branches: "*"
  # schedule:
  #   # tester selon un calendrier en utilisant la syntaxe cron
  #   - cron: "0 * * * *" # toutes les heures
```

Le reste du fichier définit ce que GitHub Actions doit faire lorsqu'il s'exécute. GitHub Actions exécutera tous les jobs listés sous la clé [`jobs`](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobs). Dans notre cas, nous avons un seul job qui exécute nos tests.

Plus précisément, notre job `test` installe les dépendances, extrait notre code et exécute notre commande de test `npx qawolf test`. Après l'exécution du/des test(s), les artefacts de débogage comme les logs de la console et les vidéos sont sauvegardés.

```yaml
jobs:
  test:
    runs-on: ubuntu-18.04

    steps:
      - name: Installer les dépendances
        run: |
          sudo apt update
          # dépendances chromium
          sudo apt-get install libgbm1
          # dépendances webkit
          sudo apt-get install libwoff1 libopus0 libwebp6 libwebpdemux2 libenchant1c2a libgudev-1.0-0 libsecret-1-0 libhyphen0 libgdk-pixbuf2.0-0 libegl1 libgles2 libevent-2.1-6 libnotify4 libvpx5 libxslt1.1

      - uses: actions/checkout@v2

      - uses: actions/setup-node@v1

      - uses: actions/cache@v1
        with:
          path: ~/.npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-node-

      - run: npm install

      # - name: Démarrer le serveur local
      #   run: npm run start & npx wait-on http://localhost:3000

      - run: npx qawolf test --headless
        env:
          # configurer les tests avec des variables d'environnement
          QAW_ARTIFACT_PATH: ${{ github.workspace }}/artifacts
          # vous pouvez également utiliser les secrets GitHub pour les variables d'environnement
          # https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets
          # LOGIN_PASSWORD: ${{ secrets.PASSWORD }}
      
      - name: Télécharger les artefacts
        if: always()
        uses: actions/upload-artifact@master
        with:
          name: qawolf
          path: ${{ github.workspace }}/artifacts
```

<h2>Exécuter les tests dans GitHub Actions</h2>

Maintenant que nous comprenons un peu mieux notre fichier de workflow, exécutons-le dans GitHub Actions. Si vous ne l'avez pas déjà fait, créez un dépôt Git pour votre projet. Assurez-vous d'ignorer `node_modules/` dans votre fichier "[.gitignore"](https://guide.freecodecamp.org/git/gitignore//).

```bash
git init
git add .
git commit -m "Premier commit"
```

Assurez-vous d'avoir [créé un dépôt](https://help.github.com/en/github/getting-started-with-github/create-a-repo) pour votre projet sur GitHub. Ensuite, poussez votre code vers GitHub.

```bash
git remote add origin VOTRE_URL_DE_DÉPÔT
git push -u origin master
```

Voir [ce dépôt GitHub](https://github.com/qawolf/tutorials-smoke-tests) pour un exemple.

Maintenant, allez dans votre dépôt GitHub et cliquez sur l'onglet "Actions", qui se trouve à côté de l'onglet "Pull Requests".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-22-at-11.04.33-AM.png)
_Onglet GitHub Actions dans le dépôt_

Vous verrez que vos tests sont en cours d'exécution. Cela est dû au fait que notre fichier de workflow a indiqué à GitHub d'exécuter nos tests chaque fois que quelqu'un pousse vers n'importe quelle branche. Cliquez sur l'exécution du workflow pour voir les détails. Notez que le nom variera en fonction de votre message de commit.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/github_actions_workflow.png)
_Workflows GitHub Actions_

Après l'exécution de votre test, vous devriez voir une coche verte indiquant que le workflow a réussi. Vous devriez également voir un lien pour télécharger les artefacts (vidéo et logs) sous "Artifacts". Cliquez sur ce lien pour télécharger les artefacts de test.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/artifacts.png)
_Télécharger les artefacts dans GitHub Actions_

Les artefacts sont organisés avec un dossier par test. Dans notre exemple, nous n'avons qu'un seul test appelé "myFirstTest.test.js". Ouvrez ce dossier pour voir les logs du navigateur dans le fichier "logs_0_${timestamp}.txt" et une vidéo "video_0_${timestamp}.mp4". Le `0` dans les noms de fichiers fait référence à l'index de la page. Si votre test impliquait plus d'une page, il y aurait des logs et des vidéos correspondants pour chaque page supplémentaire.

Maintenant, mettons à jour notre fichier de workflow pour également exécuter nos tests selon un calendrier. Dans le fichier ".github/workflows/qawolf.yml", commentez les lignes 7-9.

```yaml
name: qawolf
on:
  push:
    # tester chaque branche
    # modifier ci-dessous si vous ne voulez tester que certaines branches
    branches: "*"
  schedule:
    # tester selon un calendrier en utilisant la syntaxe cron
    - cron: "0 * * * *" # toutes les heures
```

Ces lignes indiquent à GitHub d'exécuter vos tests selon un calendrier spécifié en utilisant la [syntaxe cron](https://crontab.guru). La valeur par défaut est `"0 * * * *"`, ce qui signifie exécuter toutes les heures. Mettez à jour cette valeur si vous souhaitez utiliser un intervalle de temps différent.

Nous allons changer une autre chose dans notre fichier de workflow. GitHub Actions a une limite de stockage pour les artefacts, donc nous ne voulons pas les télécharger à chaque fois. Au lieu de cela, nous ne téléchargerons les logs et les vidéos que lorsque les tests échouent. Mettez à jour la ligne 51 de `if: always()` à `if: failure()`.

```yaml
# ...
      - name: Télécharger les artefacts
        if: failure()
        uses: actions/upload-artifact@master
        with:
          name: qawolf
          path: ${{ github.workspace }}/artifacts

```

Validez vos modifications et poussez-les vers GitHub.

```bash
git add .
git commit -m "Exécuter les tests selon un calendrier"
git push
```

Maintenant, vos smoke tests s'exécuteront toutes les heures sur GitHub Actions !

<h1 id="configurer-des-alertes-avec-slack">8. Configurer des alertes avec Slack</h1>

La dernière partie de notre pipeline est un système d'alerte qui nous informe lorsque nos tests échouent. Dans ce tutoriel, nous utilisons [Slack](https://slack.com) car il a un plan gratuit. Vous pouvez également utiliser un service comme [PagerDuty](https://www.pagerduty.com), qui aura un processus de configuration similaire.

<iframe src="https://giphy.com/embed/Tdpbuz8KP0EpQfJR3T" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p align="center"><a href="https://giphy.com/gifs/memecandy-Tdpbuz8KP0EpQfJR3T">via GIPHY</a></p>

Si vous n'avez pas déjà un compte Slack et un espace de travail, [créez-les maintenant](https://slack.com/create#email).

<h2>Créer un webhook Slack</h2>

Nous allons maintenant créer un webhook Slack, qui est une URL qui nous permet d'envoyer des messages Slack de manière programmatique. Nous ferons une requête [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) à cette URL lorsque nos tests échouent.

Tout d'abord, nous devons créer une application Slack, qui sera responsable de l'envoi de nos messages d'alerte. Commencez par visiter le [site web de l'API Slack](https://api.slack.com/apps). Dans le coin supérieur droit se trouve un bouton vert pour "Créer une nouvelle application".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/slack_create_app.png)
_Créer une nouvelle application Slack_

Cliquez sur ce bouton et vous serez invité à nommer votre application Slack et à choisir un espace de travail. Dans notre exemple, nous appelons notre application "smoke-tests". Après avoir rempli le formulaire, cliquez sur le bouton vert "Créer une application".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/create_slack_app2.png)
_Nommer l'application Slack et choisir l'espace de travail_

Vous devriez être redirigé vers la page de votre application dans Slack. Assurez-vous d'être sur la page "Informations de base" sous "Paramètres". Sous "Ajouter des fonctionnalités et des fonctionnalités", il y a un lien pour "Incoming Webhooks". Cliquez sur ce lien.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/incoming_webhooks.png)
_Incoming Webhooks pour l'application Slack_

Sur la page Incoming Webhooks, cliquez sur le bouton bascule pour activer les incoming webhooks.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/activate_incoming_webhooks.png)
_Activer les Incoming Webhooks_

Vous pourrez alors voir le bouton "Ajouter un nouveau Webhook à l'espace de travail" en bas de la page. Cliquez sur ce bouton pour ajouter un nouveau webhook. Nous utiliserons ce webhook pour envoyer un message Slack lorsque nos tests échouent.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/add_new_webhook.png)
_Ajouter un nouveau webhook à l'espace de travail Slack_

Vous serez alors invité à choisir le canal où vos messages seront publiés. Dans notre exemple, nous sélectionnons le canal "alertes". Après avoir choisi votre canal, cliquez sur le bouton vert "Autoriser".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/allow_webhook.png)
_Choisir le canal pour les alertes et accorder la permission_

Vous serez redirigé vers la page des webhooks. Sous "URLs de Webhook pour votre espace de travail", vous devriez maintenant voir votre URL de webhook.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/webhook_url.png)
_Voir l'URL du webhook dans Slack_

Pour tester votre webhook, copiez le code sous "Exemple de requête curl pour publier dans un canal". Il ressemblera à quelque chose comme ceci.

```bash
curl -X POST -H 'Content-type: application/json' --data '{"text":"Bonjour, le monde !"}' https://hooks.slack.com/services/SECRET
```

Collez ceci dans la ligne de commande et appuyez sur Entrée. Vous verrez le message "Bonjour, le monde !" publié dans le canal que vous avez spécifié.

<h2>Envoyer une alerte lorsque les tests échouent</h2>

Maintenant que nous avons notre webhook Slack, nous devons mettre à jour notre fichier de workflow GitHub Actions. Nous allons ajouter une étape qui fait une requête `POST` à notre webhook lorsque les tests échouent.

Plutôt que de coller notre URL de webhook directement dans notre fichier de workflow, nous allons l'ajouter à nos [secrets de dépôt](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets). Les secrets sont des variables d'environnement chiffrées qui stockent des informations sensibles. Garder notre URL de webhook secrète empêche les autres de la voir et de l'utiliser potentiellement à des fins malveillantes. **💀**

Ajoutez un nouveau secret sous les paramètres de votre dépôt. Appelez votre secret `SLACK_WEBHOOK_URL`, et définissez sa valeur sur votre URL de webhook Slack. La vidéo ci-dessous fournit un exemple.

%[https://youtu.be/urhpqJgpxGY]

Maintenant, mettons à jour notre fichier de workflow. En bas du fichier ".github/workflows/qawolf.yml", ajoutez les lignes suivantes. Ces lignes indiquent à GitHub de faire une requête `POST` à votre webhook Slack lorsque vos tests échouent. Nous avons changé la valeur passée à `"text"` de "Bonjour, le monde !" à "Les smoke tests ont échoué !", mais vous pouvez utiliser n'importe quel message que vous souhaitez. 

Notez que nous n'utilisons pas la valeur de notre URL de webhook Slack directement, mais la remplaçons par `${{ secrets.SLACK_WEBHOOK_URL }}`.

```yaml
# ...
      - name: Télécharger les artefacts
        if: failure()
        uses: actions/upload-artifact@master
        with:
          name: qawolf
          path: ${{ github.workspace }}/artifacts
          
# ajoutez les lignes suivantes 
      - name: Publier un message Slack
        if: failure()
        run: |
          curl -X POST -H 'Content-type: application/json' --data '{"text":"Les smoke tests ont échoué !"}' ${{ secrets.SLACK_WEBHOOK_URL }}
```

Si vous souhaitez tester que votre webhook fonctionne, lancez une erreur dans votre fichier de test ".qawolf/myFirstTest.test.js". Ensuite, poussez vos modifications vers GitHub.

```js
test("myFirstTest", async () => {
  await page.goto("http://todomvc.com/examples/react");
  await page.click(selectors["0_what_needs_to_b_input"]);
  await page.type(selectors["1_what_needs_to_b_input"], "créer un test !");
  await page.press(selectors["2_what_needs_to_b_input"], "Enter");
  await page.click(selectors["3_input"]);
  await page.click(selectors["4_button"]);
  // ajoutez cette ligne
  throw new Error("demogorgon!");
});
```

Votre test échouera, et un message sera publié dans Slack. Vous pourrez également télécharger les artefacts.

Après avoir terminé de tester votre webhook, assurez-vous de supprimer l'erreur de votre code de test.

<h1 id="conclusion">9. Conclusion</h1>

Si vous êtes arrivé jusqu'ici, félicitations ! **🎉**

<iframe src="https://giphy.com/embed/BMR4cgypuglVu" width="350" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p align="center"><a href="https://giphy.com/gifs/cat-kitten-party-BMR4cgypuglVu">via GIPHY</a></p>

Dans ce tutoriel, nous avons appris ce qu'est le smoke testing et avons construit un pipeline de smoke testing. Maintenant, vous pouvez être le héros du smoke testing de votre équipe ! **🦸‍♀️**

Si votre équipe a besoin d'aide avec l'assurance qualité, ou si vous voulez simplement discuter, n'hésitez pas à m'envoyer un message à [laura@qawolf.com](mailto:laura@qawolf.com). 💌
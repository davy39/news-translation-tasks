---
title: Comment ajouter des tests de capture d'écran avec Cypress à votre projet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-04T16:02:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-screenshot-testing-with-cypress-to-your-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cypress-io-logo-social-share-8fb8a1db3cdc0b289fad927694ecb415.png
tags:
- name: Code Quality
  slug: code-quality
- name: Continuous Integration
  slug: continuous-integration
- name: Testing
  slug: testing
seo_title: Comment ajouter des tests de capture d'écran avec Cypress à votre projet
seo_desc: 'By Leonardo Faria

  Developers are usually concerned with the quality of their code. There are different
  kinds of tests that help us avoid breaking code when a new feature is added in a
  project. But what can we do to ensure that components don''t look d...'
---

Par Leonardo Faria

Les développeurs sont généralement préoccupés par la qualité de leur code. Il existe différents types de tests qui nous aident à éviter de casser le code lorsqu'une nouvelle fonctionnalité est ajoutée à un projet. Mais que pouvons-nous faire pour nous assurer que les composants ne changent pas d'apparence au fil du temps ? 

Dans cet article, vous apprendrez à utiliser Cypress pour capturer des parties de pages d'un site web. Ensuite, vous intégrerez l'outil de test dans CI pour vous assurer que, à l'avenir, personne ne fera de changements indésirables à votre projet.

Ma motivation pour créer cette stratégie de test est venue du travail. Chez [Thinkific](https://www.thinkific.com), nous avons un système de design interne et nous avons ajouté Cypress pour éviter les surprises lors de la manipulation de fichiers CSS/JS.

À la fin de cet article, nous aurons des PRs avec des tests Cypress :

![Cypress bot](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-bot-comment.jpg)

## Avant de commencer

J'ai créé un [site web d'exemple](https://cypress-example.vercel.app/) pour imiter une bibliothèque de composants. Il s'agit d'un site web très simple créé avec TailwindCSS et hébergé sur Vercel. Il documente 2 composants : [badge](https://cypress-example.vercel.app/badge.html) et [button](https://cypress-example.vercel.app/button.html).

Vous pouvez consulter le [code source](https://github.com/leonardofaria/cypress-example) sur GitHub. Le site web est statique et se trouve dans le dossier `public`. Vous pouvez voir le site web localement en exécutant `npm run serve` et en vérifiant dans le navigateur [http://localhost:8000](http://localhost:8000).

![Site web d'exemple](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-sample-website.png)

## Ajout de Cypress et de Cypress Image Snapshot

Commencez par cloner le [dépôt d'exemple](https://github.com/leonardofaria/cypress-example). Ensuite, créez une nouvelle branche et installez [Cypress Image Snapshot](https://www.npmjs.com/package/cypress-image-snapshot), le package responsable de la capture/comparaison des captures d'écran.

```bash
git checkout -b add-cypress
npm install -D cypress cypress-image-snapshot
```

Après avoir ajouté les packages, quelques étapes supplémentaires sont nécessaires pour ajouter Cypress Image Snapshot dans Cypress.

Créez un fichier `cypress/plugins/index.js` avec le contenu suivant :

```js
const { addMatchImageSnapshotPlugin } = require('cypress-image-snapshot/plugin');

module.exports = (on, config) => {
  addMatchImageSnapshotPlugin(on, config);
};

```

Ensuite, créez un fichier `cypress/support/index.js` contenant :

```js
import { addMatchImageSnapshotCommand } from 'cypress-image-snapshot/command';

addMatchImageSnapshotCommand();
```

## Création du test de capture d'écran

Il est temps de créer le test de capture d'écran. Voici le plan :

1. Cypress visitera chaque page (badge et button) du projet.
2. Cypress prendra une capture d'écran de chaque exemple dans la page. La [page Badge](https://cypress-example.vercel.app/badge.html) a 2 exemples (Default et Pill), tandis que la [page Button](https://cypress-example.vercel.app/badge.html) a 3 exemples (Default, Pill et Outline). Tous ces exemples sont à l'intérieur d'un élément `<div>` avec une classe `cypress-wrapper`. Cette classe a été ajoutée dans le seul but d'identifier ce qui doit être testé.

La première étape consiste à créer le fichier de configuration Cypress (`cypress.json`) :

```json
{
  "baseUrl": "http://localhost:8000/",
  "video": false
}
```

L'URL `baseUrl` est le site web en cours d'exécution localement. Comme je l'ai mentionné précédemment, `npm run serve` servira le contenu du dossier `public`. La deuxième option, `video`, désactive l'enregistrement vidéo de Cypress, que nous n'utiliserons pas dans ce projet.

Il est temps de créer le test. Dans `cypress/integration/screenshot.spec.js`, ajoutez :

```js
const routes = ['badge.html', 'button.html'];

describe('Component screenshot', () => {
  routes.forEach((route) => {
    const componentName = route.replace('.html', '');
    const testName = `${componentName} should match previous screenshot`;

    it(testName, () => {
      cy.visit(route);
  
      cy.get('.cypress-wrapper').each((element, index) => {
        const name = `${componentName}-${index}`;
  
        cy.wrap(element).matchImageSnapshot(name);
      });
    });
  });
});
```

Dans le code ci-dessus, je crée dynamiquement des tests basés sur le tableau `routes`. Le test créera une image par élément `.cypress-wrapper` que la page contient.

Enfin, dans le fichier `package.json`, créons la commande pour déclencher les tests :

```json
{
  "test": "cypress"
}  
```

À partir de là, il y a 2 options : exécuter Cypress en mode headless avec `npm run cypress run` ou utiliser le Cypress Test Runner avec `npm run cypress open`.

### Option headless

En utilisant `npm run cypress run`, la sortie devrait être similaire à l'image suivante :

![Sortie du premier test](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-first-test.jpg)

Les tests passeront et 5 images seront créées dans le dossier `/snapshots/screenshot.spec.js`.

### Option Test Runner

En utilisant `npm run cypress open`, le Cypress Test Runner s'ouvrira et vous pourrez suivre les tests étape par étape.

![Capture d'écran du Cypress Test Runner](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-test-runner.jpg)

Notre première étape est terminée, alors fusionnons cette branche avec master. Si vous voulez voir le travail effectué jusqu'à présent, consultez ma [Pull Request](https://github.com/leonardofaria/cypress-example/pull/1). 

## Utilisation de Cypress dans Docker

Si vous exécutez le test ci-dessus en alternant entre le mode headless et le Test Runner, vous remarquerez peut-être que la capture d'écran variera. 

En utilisant le Test Runner avec un ordinateur à écran rétina, vous pouvez obtenir des images rétina (2x), tandis que le mode headless ne vous donne pas de captures d'écran de haute qualité.

De plus, il est important de dire que les captures d'écran peuvent varier selon votre système d'exploitation. 

Linux et Windows, par exemple, ont des applications avec des barres de défilement visibles, tandis que macOS masque la barre de défilement. 

Si le contenu capturé dans la capture d'écran ne correspond pas à un composant, vous pouvez avoir ou non une barre de défilement. Si votre projet repose sur les polices par défaut du système d'exploitation, les captures d'écran seront également différentes selon l'environnement.

Afin d'éviter ces incohérences, les tests s'exécuteront dans Docker afin que l'ordinateur du développeur n'affecte pas les captures d'écran.

Commençons par créer une nouvelle branche :

```bash
git checkout -b add-docker
```

Cypress offre différentes images Docker - vous pouvez consulter les détails dans [leur documentation](https://docs.cypress.io/examples/examples/docker.html) et [leur blog](https://www.cypress.io/blog/2019/05/02/run-cypress-with-a-single-docker-command/). 

Pour cet exemple, j'utiliserai l'image `cypress/included`, qui inclut Electron et est prête à être utilisée.

Nous devons apporter deux modifications : changer l'URL `baseUrl` dans le fichier `cypress.json` :

```json
{
  "baseUrl": "http://host.docker.internal:8000/",
}
```

et la commande `test` dans le fichier `package.json` : 

```json
{
  "test": "docker run -it -e CYPRESS_updateSnapshots=$CYPRESS_updateSnapshots --ipc=host -v $PWD:/e2e -w /e2e cypress/included:4.11.0"
}
```

L'exécution de `npm run test` nous posera un problème :

![Sortie du test](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-docker.jpg)

Les images sont légèrement différentes, mais pourquoi ? Voyons ce qu'il y a dans le dossier `__diff_output__` :

![Différence du bouton](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-button-diff.png)

Comme je l'ai mentionné précédemment, des incohérences typographiques ! Le composant Button utilise la police par défaut du système d'exploitation. Comme Docker s'exécute dans Linux, la police rendue ne sera pas la même que celle que j'ai installée sur macOS. 

Maintenant que nous avons migré vers Docker, ces captures d'écran sont obsolètes. Il est temps de mettre à jour les snapshots :

```bash
CYPRESS_updateSnapshots=true npm run test
```

Veuillez noter que je préfixe la commande de test avec la variable d'environnement `CYPRESS_updateSnapshots`.

La deuxième étape est terminée. Au cas où vous auriez besoin d'aide, consultez ma [pull request](https://github.com/leonardofaria/cypress-example/pull/2).

Fusionnons cette branche et continuons.

## Ajout de CI

Notre prochaine étape consiste à ajouter les tests dans CI. Il existe différentes solutions CI sur le marché, mais pour ce tutoriel, j'utiliserai Semaphore. Je ne suis pas affilié à eux et j'utilise leur produit au travail, donc c'était pour moi un choix naturel. 

La configuration est simple et peut être adaptée à d'autres solutions comme CircleCI ou Github Actions.

Avant de créer notre fichier de configuration Semaphore, préparons notre projet à s'exécuter dans CI.

La première étape consiste à installer [start-server-and-test](https://www.npmjs.com/package/start-server-and-test). Comme le nom du package l'indique, il démarrera un serveur, attendra l'URL, puis exécutera une commande de test :

```bash
npm install -D start-server-and-test
```

Deuxièmement, modifiez le fichier `package.json` :

```json
{
  "test": "docker run -it -e CYPRESS_baseUrl=$CYPRESS_baseUrl -e CYPRESS_updateSnapshots=$CYPRESS_updateSnapshots --ipc=host -v $PWD:/e2e -w /e2e cypress/included:4.11.0",
  "test:ci": "start-server-and-test serve http://localhost:8000 test"
}
```

Dans le script `test`, nous ajoutons la variable d'environnement `CYPRESS_baseUrl`. Cela nous permettra de changer dynamiquement l'URL de base utilisée par Cypress. De plus, nous ajoutons le script `test:ci`, qui exécutera le package que nous venons d'installer.

Nous sommes prêts pour Semaphore. Créez le fichier `.semaphore/semaphore.yml` avec le contenu suivant :

```yml
 1 version: v1.0
 2 name: Cypress example
 3 agent:
 4   machine:
 5     type: e1-standard-2
 6     os_image: ubuntu1804
 7 blocks:
 8   - name: Build Dependencies
 9     dependencies: []
10     task:
11       jobs:
12         - name: NPM
13           commands:
14             - sem-version node 12
15             - checkout
16             - npm install
17   - name: Tests
18     dependencies: ['Build Dependencies']
19     task:
20       prologue:
21         commands:
22           - sem-version node 12
23           - checkout
24       jobs:
25         - name: Cypress
26           commands:
27             - export CYPRESS_baseUrl="http://$(ip route | grep -E '(default|docker0)' | grep -Eo '([0-9]+\.){3}[0-9]+' | tail -1):8000"
28             - npm run test:ci
```

Détail de la configuration :

- Les lignes 1-6 définissent le type d'instance que nous utiliserons dans leur environnement
- Les lignes 8 et 16 créent 2 blocs : le premier bloc, "Build Dependencies", exécutera `npm install`, téléchargeant les dépendances dont nous avons besoin. Le deuxième bloc, "Tests", exécutera Cypress, avec quelques différences.
- À la ligne 27, nous définissons dynamiquement la variable d'environnement `CYPRESS_baseUrl` en fonction de l'IP que Docker utilise à ce moment-là. Cela remplacera `http://host.docker.internal:8000/`, qui peut ne pas fonctionner dans tous les environnements.
- À la ligne 28, nous exécutons enfin le test en utilisant `start-server-and-test` : une fois que le serveur est prêt pour les connexions, Cypress exécutera la suite de tests.

Une autre étape est terminée, il est temps de fusionner notre branche ! Vous pouvez consulter la [Pull request](https://github.com/leonardofaria/cypress-example/pull/6/files) qui contient tous les fichiers de cette section et vérifier le [build dans Semaphore](https://leonardofaria.semaphoreci.com/workflows/061f6c9f-8f2d-4351-8a25-e5bc1568f67e).

## Enregistrement des tests dans cypress.io

Lire la sortie des tests dans CI n'est pas très convivial. Dans cette étape, nous intégrerons notre projet avec [cypress.io](https://www.cypress.io/). 

Les étapes suivantes sont basées sur la [documentation de Cypress](https://docs.cypress.io/guides/dashboard/projects.html#Setup).

Commençons par obtenir un ID de projet et une clé d'enregistrement. Dans le terminal, créez une nouvelle branche et exécutez :

```bash
git checkout -b add-cypress-recording
CYPRESS_baseUrl=http://localhost:8000 ./node_modules/.bin/cypress open
```

Plus tôt, j'ai mentionné que nous utiliserions Cypress dans Docker. Mais ici, nous ouvrons Cypress localement puisque c'est le seul moyen de s'intégrer avec le tableau de bord du site web. 

Dans Cypress, allons dans l'onglet Runs, cliquez sur "Set up project to record", et choisissez un nom et une visibilité. Nous obtiendrons un `projectId` qui est automatiquement ajouté dans le fichier `cypress.json` et une clé d'enregistrement privée. Voici une vidéo des étapes :

<video style="width: 100%; margin: auto;" width="640" height="360" layout="responsive" controls loop autoplay="autoplay">
  <source src="https://leonardofaria.net/wp-content/uploads/2020/08/cypress-adding-integration.mp4" type="video/mp4">
</video>

Dans Semaphore, j'ai ajouté la clé d'enregistrement comme variable d'environnement appelée `CYPRESS_recordKey`. Ensuite, mettons à jour notre script de test pour utiliser la variable :

```json
{
  "test:ci": "start-server-and-test 'serve' 8000 'npm run test -- run --record --key $CYPRESS_recordKey'"
}
```

C'est à peu près tout ce qui doit être fait. Dans la [Pull request](https://github.com/leonardofaria/cypress-example/pull/8), nous pouvons voir l'intégration de cypress.io dans les commentaires. Il y a même un lien profond qui nous mène à leur tableau de bord et montre toutes les captures d'écran. Regardez la vidéo ci-dessous :

<video style="width: 100%; margin: auto;" width="640" height="360" layout="responsive" controls loop autoplay="autoplay">
  <source src="https://leonardofaria.net/wp-content/uploads/2020/08/cypress-io-test-dashboard.mp4" type="video/mp4">
</video>

Il est temps de fusionner notre travail, et c'est la fin de notre intégration.

## Test en situation réelle

Imaginez que nous travaillons sur un changement qui affecte le padding des boutons : il est temps de tester si Cypress capturera la différence. 

Dans le site web d'exemple, doublons le padding horizontal de 16px à 32px. Ce changement est assez simple puisque nous utilisons Tailwind CSS : `px-4` est remplacé par `px-8`. Voici cette [Pull request](https://github.com/leonardofaria/cypress-example/pull/9).

Comme nous pouvons nous y attendre, Cypress a capturé que le bouton ne correspond pas aux captures d'écran. En visitant la page, nous pouvons vérifier la capture d'écran du test échoué :

<video style="width: 100%; margin: auto;" controls loop autoplay="autoplay">
  <source src="https://leonardofaria.net/wp-content/uploads/2020/08/cypress-io-broken-test.mp4" type="video/mp4">
</video>

Le fichier diff montre la capture d'écran originale à gauche, le résultat actuel à droite, et ils sont combinés au milieu. Nous avons également l'option de télécharger l'image pour mieux voir le problème :

<div class="full-width"><img alt="Bouton avant et après" src="https://leonardofaria.net/wp-content/uploads/2020/08/cypress-io-broken-test.png" /></div>

Si ce n'est pas un problème, mettez à jour les captures d'écran :

```bash
CYPRESS_updateSnapshots=true npm run test
```

## La fin

C'est tout pour aujourd'hui. J'espère que vous avez appris comment Cypress peut être utile pour vous assurer que personne n'ajoute de changements inattendus à un projet. 


Également publié sur [mon blog](https://bit.ly/30ncCYj). Si vous aimez ce contenu, suivez-moi sur [Twitter](https://twitter.com/leozera) et [GitHub](https://github.com/leonardofaria).
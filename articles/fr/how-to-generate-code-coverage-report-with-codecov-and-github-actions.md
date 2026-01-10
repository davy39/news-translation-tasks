---
title: Comment générer un rapport de couverture de code avec CodeCov et GitHub Actions
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2021-05-24T19:40:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-code-coverage-report-with-codecov-and-github-actions
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/automation.jpg
tags:
- name: GitHub Actions
  slug: github-actions
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
seo_title: Comment générer un rapport de couverture de code avec CodeCov et GitHub
  Actions
seo_desc: 'Software testing is an important part of the software development process.
  You run tests at different stages of the software development life cycle, and you''ll
  want to make sure that you have good test coverage.

  Here are some key reasons for writing ...'
---

Le test logiciel est une partie importante du processus de développement logiciel. Vous exécutez des tests à différents stades du cycle de vie du développement logiciel, et vous voudrez vous assurer d'avoir une bonne couverture de test.

Voici quelques raisons clés pour écrire des tests logiciels :

* Les tests vous empêchent d'introduire des changements destructeurs (breaking changes) dans votre codebase à l'avenir. En d'autres termes, les tests que vous écrivez maintenant pourraient vous sauver de vous-même plus tard.
    
* Les tests garantissent que le produit que vous construisez répond aux spécifications requises.
    
* Un code bien testé vous donne plus de confiance quant à la qualité de votre code.
    
* Les tests réduisent la probabilité d'avoir du code avec un comportement inconnu dans votre codebase, ce qui pourrait devenir une source d'erreurs.
    
* Les tests facilitent la maintenance de votre code. Vous ne pouvez pas savoir comment la modification d'une petite section de votre codebase pourrait affecter l'ensemble de celle-ci si vous n'avez pas une couverture de code élevée.
    

Dans cet article, vous apprendrez comment générer un rapport de couverture de code en utilisant [codecov](https://about.codecov.io/) et [gitHub actions](https://github.com/features/actions).

## Qu'est-ce que la couverture de code ?

La couverture de code est une métrique qui vous aide à savoir quelle proportion de votre code source a été testée. Il existe un certain nombre d'outils que vous pouvez utiliser pour générer des rapports de couverture de code. Ces outils incluent :

* [codecov](https://about.codecov.io/)
    
* [coveralls](https://coveralls.io/)
    
* [istanbul](https://istanbul.js.org/)
    
* [uberalls](https://github.com/uber/uberalls)
    

La plupart des outils d'analyse de couverture de code utilisent un ensemble de métriques pour rapporter l'analyse. Ces métriques incluent :

* **Couverture de fonctions** : Le nombre de fonctions déclarées qui ont été appelées après l'exécution de vos suites de tests.
    
* **Couverture d'instructions** : Le nombre d'instructions qui ont été exécutées après l'exécution des suites de tests.
    
* **Couverture de branches** : Quelle proportion du code des branches, comme les blocs `if`, a été exécutée.
    
* **Couverture de conditions** : Le nombre de sous-expressions booléennes qui ont été testées pour les valeurs `true` et `false`.
    
* **Couverture de lignes** : Les lignes de code qui ont été testées.
    

Dans cet article, nous nous concentrerons principalement sur l'utilisation de [codecov](https://about.codecov.io/) et [gitHub actions](https://github.com/features/actions) pour générer un rapport de couverture de code pour un projet Node.

## Pourquoi la couverture de code est-elle importante ?

Une bonne couverture de code vous donne confiance dans le code que vous livrez, surtout si vos tests sont robustes et bien pensés.

Lorsque vous écrivez des tests pour augmenter votre couverture de code, il est plus probable que vous détectiez des bugs et que vous les corrigiez avant l'expédition en production.

## Qu'est-ce que Codecov ?

[Codecov](https://about.codecov.io/) est un outil que vous pouvez utiliser pour générer des rapports de couverture pour vos projets. Vous pouvez téléverser les données de couverture de code générées dans votre système de fichiers local vers Codecov et visualiser facilement le rapport de couverture sur différents graphiques.

Dans cet article, cependant, vous allez utiliser GitHub Actions afin que les processus de génération de rapports de couverture et de leur téléversement vers [codecov](https://about.codecov.io/) soient automatisés.

Vous pouvez intégrer Codecov dans votre workflow d'intégration continue. Codecov est capable de publier des commentaires sur les pull requests et bien plus encore. Ces commentaires aideront les autres développeurs à savoir comment la fusion de leur pull request affectera la couverture de code sans quitter l'interface utilisateur de GitHub.

Vous pouvez également afficher un badge montrant le rapport de couverture sur votre dépôt GitHub pour que tous les collaborateurs de votre projet puissent le voir. Il vous suffit d'intégrer Codecov dans votre workflow d'intégration continue.

Vous pouvez en savoir plus sur toutes les autres fonctionnalités offertes par Codecov dans la [documentation](https://docs.codecov.io/docs).

## Comment créer un projet et générer un rapport de couverture

Dans les étapes ci-dessous, vous allez créer un projet Node simple et générer un rapport de couverture Codecov pour celui-ci.

### Prérequis

Vous devez avoir les éléments suivants installés sur votre machine pour pouvoir exécuter les commandes des sous-sections suivantes.

* [Node](https://nodejs.org/en/)
    
* Un éditeur de texte comme [VS code](https://code.visualstudio.com/) ou [atom](https://atom.io/)
    
* [Git](https://git-scm.com/)
    

### Étape 1 : Créer un répertoire et s'y rendre

Dans cette étape, vous allez créer un répertoire appelé `learn-test-coverage` puis vous y rendre. Vous pouvez donner un nom différent au répertoire si vous le souhaitez, à condition qu'il soit explicite.

Exécutez les commandes suivantes dans le terminal :

```js
mkdir learn-test-coverage
cd learn-test-coverage
```

Dans l'étape suivante, vous allez initialiser le projet.

### Étape 2 : Initialiser le projet

Dans cette étape, vous allez initialiser le projet en exécutant la commande ci-dessous dans le terminal :

```js
npm init --yes
```

L'exécution réussie de la commande ci-dessus créera un fichier `package.json` à la racine du répertoire de votre projet.

Dans l'étape suivante, vous allez installer [jest](https://jestjs.io/) en tant que dépendance de développement.

### Étape 3 : Installer Jest en tant que dépendance

Dans cette étape, vous allez installer [jest](https://jestjs.io/) en tant que dépendance de développement. Jest est un Framework de test JavaScript simple qui fonctionne généralement immédiatement dans Node avec une configuration minimale.

Exécutez la commande ci-dessous dans le terminal :

```js
npm install --save-dev jest
```

Après avoir exécuté avec succès la commande ci-dessus, vous devriez voir le répertoire `node_modules` et le fichier `package-lock.json` créés à la racine de votre projet. Vous devriez également voir Jest installé comme dépendance de développement dans le fichier `package.json`.

Dans l'étape suivante, vous initialiserez un dépôt Git dans votre projet.

### Étape 4 : Initialiser un dépôt Git

Dans cette étape, vous allez initialiser un dépôt Git dans votre projet en exécutant la commande ci-dessous :

```shell
git init
```

Créez un fichier `.gitignore` à la racine du répertoire du projet et ajoutez-y le code suivant. Cela ignorera le dossier `node_modules` afin qu'il ne soit pas poussé (Commit) vers le dépôt distant plus tard.

```shell
/node_modules
```

Dans l'étape suivante, nous allons déclarer une fonction simple et écrire un test pour celle-ci.

### Étape 5 : Déclarer une fonction et écrire un test pour celle-ci

Dans cette étape, vous allez déclarer une fonction simple appelée `sum` dans le fichier `sum.js`. Cette fonction prend deux paramètres et retourne leur somme. Vous écrirez également des tests pour votre code dans le fichier `sum.test.js`.

Exécutez la commande ci-dessous dans le terminal :

```js
touch sum.js sum.test.js
```

Vous devriez voir les deux fichiers créés dans votre projet. Copiez et collez le code ci-dessous dans `sum.js` :

```js
function sum(num1, num2) {
  return num1 + num2;
}

module.exports = sum;
```

De même, copiez et collez le code ci-dessous dans `sum.test.js` :

```js
const sum = require("./sum");

test("ajoute 1 + 2 pour égaler 3", () => {
  expect(sum(1, 2)).toBe(3);
});
```

Modifiez la valeur de la propriété `"test"` dans votre `package.json` en `"jest --coverage"` afin que la valeur de la propriété `"scripts"` ressemble à ceci :

```js
{
    "test": "jest --coverage"
}
```

Dans le terminal, exécutez `npm test` pour lancer votre test. Une fois le test terminé, vous devriez voir le résumé de la couverture de code dans le terminal et un répertoire `coverage` généré.

Voici ce que je vois dans mon terminal :

![coverage-terminal-output](https://www.freecodecamp.org/news/content/images/2021/05/coverage-terminal-output.png align="left")

Vous pouvez également consulter le résumé dans le navigateur en ouvrant le fichier `index.html` à l'intérieur du dossier `coverage/lcov-report`. Vous devriez voir ce qui suit :

![codecov-coverage-report-browser](https://www.freecodecamp.org/news/content/images/2021/05/codecov-coverage-report-browser.png align="left")

Vous pouvez générer le rapport de couverture car Jest est livré avec [istanbul](https://istanbul.js.org/). Assurez-vous de supprimer le dossier `coverage`, car vous n'en avez pas besoin puisque nous allons automatiser le processus via GitHub Actions.

Vous devriez être en mesure d'identifier les métriques qu'[istanbul](https://istanbul.js.org/) utilise pour générer le rapport de couverture (les métriques que j'ai mentionnées au début de l'article).

Dans l'étape suivante, nous ajouterons l'intégration continue de GitHub Actions à notre projet.

### Étape 6 : Ajouter un workflow d'intégration continue GitHub Actions

Dans cette étape, vous allez ajouter un workflow d'intégration continue GitHub Actions à votre projet afin que Codecov génère automatiquement un rapport lors de la création d'une pull request.

Créez un dossier `.github` à la racine de votre projet. À l'intérieur du dossier `.github`, créez un dossier `workflows`. Ensuite, dans `workflows`, créez un fichier `codecov.yml`. Le fichier n'a pas besoin d'être nommé `codecov`. Vous pouvez lui donner le nom que vous voulez.

Copiez et collez le code ci-dessous dans votre fichier `codecov.yml`.

C'est le fichier de configuration du workflow. Il exécutera votre test lorsque les deux événements `push` et `pull_request` se produisent. Vous pouvez en savoir plus sur la [syntaxe YAML](https://yaml.org/spec/1.2/spec.html) et [gitHub actions](https://github.com/features/actions) pour comprendre le contenu du fichier ci-dessous.

```yml
name: Running Code Coverage

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [12.x, 13.x, 14.x, 15.x]

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      with:
        fetch-depth: 2

    - name: Set up Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v1
      with:
        node-version: ${{ matrix.node-version }}

    - name: Install dependencies
      run: npm install

    - name: Run tests
      run: npm run test

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v1
```

La dernière étape est responsable du téléversement du rapport de couverture vers Codecov dans le fichier de configuration ci-dessus.

Dans l'étape suivante, vous allez créer un dépôt sur GitHub et y pousser votre projet.

### Étape 7 : Créer un dépôt sur GitHub et y pousser vos modifications

Dans cette étape, vous allez créer un dépôt sur GitHub et y pousser vos modifications.

Allez sur GitHub. Créez un dépôt vide et nommez-le `learn-test-coverage`.

À la racine du répertoire de votre projet sur votre machine, exécutez les commandes suivantes pour initialiser votre dépôt local et valider (Commit) vos modifications.

```shell
git add .
git commit -m "Initial commit"
```

Vous pouvez ensuite ajouter le dépôt distant que vous avez créé ci-dessus à votre dépôt local en utilisant la commande ci-dessous :

```shell
git remote add origin <Remote repository>
```

Enfin, vous pouvez pousser vos modifications vers votre dépôt distant avec la commande suivante :

```shell
git push origin master
```

Dans l'étape suivante, nous allons lier notre dépôt GitHub à Codecov. Cela garantit que nos données de couverture sont automatiquement téléversées chaque fois que nous créons une pull request afin qu'un rapport soit généré.

### Étape 8 : Lier votre dépôt distant à Codecov

Dans cette étape, vous allez lier votre dépôt à Codecov. Mais vous devez d'abord vous inscrire.

Codecov vous permet de vous inscrire avec votre compte GitHub en quelques minutes seulement. Vous pouvez ensuite sélectionner le dépôt GitHub que vous souhaitez lier sur le tableau de bord Codecov.

Après avoir sélectionné le dépôt, vous serez redirigé vers une page avec un jeton (token). Vous n'avez pas besoin de ce jeton pour les dépôts publics.

Pour les dépôts privés, vous devrez l'ajouter à vos secrets GitHub, puis ajouter ce qui suit au bas de votre fichier de configuration de workflow pour qu'il ressemble à ceci :

```yaml
- name: Upload coverage to Codecov
    uses: codecov/codecov-action@v1
    with:
        token: ${{ secrets.YOUR_SECRET_TOKEN }}
```

### Étape 9 : Tester votre workflow d'intégration continue

Dans cette étape, vous allez tester votre workflow d'intégration continue.

Créez un fichier `README.md` à la racine de votre projet. Copiez et collez le badge Codecov qui se trouve sur votre tableau de bord Codecov sous l'onglet paramètres dans votre fichier `README.md`. Voici à quoi ressemblent les badges.

![codecov-badge](https://www.freecodecamp.org/news/content/images/2021/05/codecov-badge.png align="left")

Validez (Commit) et poussez les modifications vers GitHub. Vous devriez pouvoir voir la couverture de code indiquée sur votre badge une fois l'exécution du workflow CI terminée.

![codecov-readme](https://www.freecodecamp.org/news/content/images/2021/05/codecov-readme.png align="left")

Vous pouvez également consulter le rapport de couverture sur votre tableau de bord Codecov. Essayez de créer une pull request pour voir ce qui se passe.

Pour plus d'informations sur ce que vous pouvez faire d'autre, consultez la [documentation de Codecov](https://docs.codecov.io/docs).

Si vous êtes bloqué, vous pouvez également consulter [mon projet](https://github.com/nibble0101/learn-test-coverage) sur GitHub.

## Comment Codecov génère-t-il son rapport de couverture ?

Codecov utilise les termes **hit**, **partial** et **miss** pour décrire la couverture de code dans votre projet. La couverture est le ratio des `hits` sur la somme des `hits`, `partials` et `misses`.

Si le code est décrit comme un **hit**, cela signifie que le code source a été exécuté par la suite de tests.

S'il est décrit comme **partial**, cela indique que le code source n'a pas été entièrement exécuté par la suite de tests. Il reste des branches qui n'ont pas été exécutées.

Un **miss** indique que le code source n'a pas été exécuté par la suite de tests.

> Une base de code qui a 5 lignes exécutées par des tests sur 12 lignes au total recevra un ratio de couverture de 41 % (arrondi à l'inférieur) - [Documentation Codecov](https://docs.codecov.io/docs)

C'est ainsi que vous intégrez Codecov dans votre workflow d'intégration continue. Si vous souhaitez explorer plus de fonctionnalités, vous pouvez consulter la [documentation de Codecov](https://docs.codecov.io/docs).

## Conclusion

Dans cet article, nous avons vu comment intégrer [codecov](https://docs.codecov.io) dans votre workflow d'intégration continue.

Augmenter la couverture de code vous aidera de bien des manières. Mais avoir une couverture de code élevée juste pour la forme peut vous attirer des ennuis si vos tests ne sont pas robustes et bien pensés.

Les outils d'analyse de couverture de code ne sont que des outils destinés à faciliter votre travail. Mais vous ne devriez pas les substituer aux revues de code. Un outil ne vaut que par son utilisateur.

### Références

* [Documentation Codecov](https://docs.codecov.io/docs)
    
* [Documentation Jest](https://jestjs.io/docs/getting-started)
    
* [Documentation Istanbul](https://istanbul.js.org/)
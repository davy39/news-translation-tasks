---
title: Comment écrire de bons messages de commit avec Commitlint
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-12T20:11:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-commitlint-to-write-good-commit-messages
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Thumbnail.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment écrire de bons messages de commit avec Commitlint
seo_desc: "By Anish De\nWe are often in a hurry to commit our changes in Git and so\
  \ we write something random in our commit messages. In fact, I have seen people\
  \ putting the date and time or even something like commit 1, commit 2 in their messages.\
  \ \nThis is not ..."
---

Par Anish De

Nous sommes souvent pressés de valider nos modifications dans Git et nous écrivons donc quelque chose d'aléatoire dans nos messages de commit. En fait, j'ai vu des gens mettre la date et l'heure ou même quelque chose comme `commit 1`, `commit 2` dans leurs messages. 

Ce n'est pas une bonne pratique, car les messages de commit doivent être utiles et avoir du sens afin que les personnes travaillant sur le projet, lisant le code ou contribuant à celui-ci comprennent les modifications à partir du message lui-même. 

Maintenant, voyons une manière simple de résoudre ce problème.

# Qu'est-ce que Commitlint ?

[Commitlint](https://commitlint.js.org/#/) est un outil simple qui vérifie vos messages de commit et s'assure qu'ils suivent un ensemble de règles. 

Il s'exécute en tant que hook pre-commit de husky, c'est-à-dire qu'il s'exécute avant que le code ne soit validé et bloque le commit en cas d'échec des vérifications de linting.

## Comment utiliser Commitlint avec un projet JavaScript simple

Dans cet exemple, nous allons voir comment configurer commitlint dans un projet JavaScript simple. Pour commencer, créons d'abord un projet vide :

```sh
mkdir commitlint_example && cd commitlint_example

npm init
# OU
yarn init
# Acceptez simplement les valeurs par défaut lorsque vous êtes invité à configurer le projet
```

Maintenant, initialisons un dépôt Git vide :

```sh
git init
```

Nous devons également ajouter un fichier `.gitignore` pour empêcher certains fichiers d'être validés :

```gitignore
node_modules/
```

Maintenant, nous allons ajouter un fichier appelé `index.js` et simplement logger quelque chose pour l'instant :

```js
console.log("Hello, World!!!")
```

L'exécution de `node .` devrait afficher le texte sur votre terminal comme ceci :

![Exécution de node . affiche Hello, World!!!](https://www.freecodecamp.org/news/content/images/2021/11/image-33.png)

## Comment configurer commitlint

Nous allons configurer commitlint en suivant [la documentation officielle de configuration locale ici](https://commitlint.js.org/#/guides-local-setup).

Tout d'abord, nous devons installer le CLI de commitlint et ajouter une configuration commitlint (dans ce cas, la configuration par défaut [Conventional Commits Config](https://www.conventionalcommits.org/)).

```sh
npm install @commitlint/cli @commitlint/config-conventional --save-dev
# OU
yarn add -D @commitlint/cli @commitlint/config-conventional
```

Nous devons ajouter une configuration à un fichier nommé `commitlint.config.js` comme ceci :

```js
module.exports = {
    extends: [
        "@commitlint/config-conventional"
    ],
}
```

Maintenant, nous devons installer [husky](https://typicode.github.io/husky/#/) pour exécuter commitlint en tant que hook pre-commit.

```sh
npm install husky --save-dev
# OU
yarn add -D husky
```

Nous devons également activer les hooks de husky :

```sh
npx husky install
# OU
yarn husky install
```

Nous pouvons ajouter une étape de préparation qui active les hooks de husky lors de l'installation :

```sh
npm set-script prepare "husky install"
```

Maintenant que nous avons terminé l'installation de husky, nous devons ajouter un hook pre-commit pour exécuter commitlint avant que le code ne soit validé.

```sh
npx husky add .husky/commit-msg "npx --no -- commitlint --edit $1"
# OU
yarn husky add .husky/commit-msg "yarn commitlint --edit $1"
```

Maintenant, nous avons terminé la configuration de commitlint. Alors testons pour voir si cela fonctionne.

Tout d'abord, nous allons indexer tous les fichiers pour les valider :

```sh
git add -A
```

Maintenant, essayons de valider les modifications, sans suivre la convention par défaut :

```sh
git commit -m "set up a basic js project, added commitlint and husky for liniting commit messages"
```

![Erreur qui devrait se produire en raison du non-respect de la convention par défaut](https://www.freecodecamp.org/news/content/images/2021/11/image-34.png)
_Erreur qui devrait se produire en raison du non-respect de la convention par défaut_

Vous devriez obtenir le résultat ci-dessus (ou quelque chose de similaire) qui génère une erreur. Si le commit est réussi, vous avez probablement fait une erreur quelque part. Assurez-vous d'avoir exécuté toutes les commandes ci-dessus et essayez d'annuler le commit, d'exécuter les scripts et de valider à nouveau jusqu'à ce qu'il échoue.

Maintenant, il est temps de valider correctement. Exécutez cette commande :

```sh
git commit -m "ci: initialised basic js project, added commitlint and husky to lint commit messages"
```

![Le code devrait être validé en raison du respect de la convention par défaut](https://www.freecodecamp.org/news/content/images/2021/11/image-35.png)
_Le code devrait être validé en raison du respect de la convention par défaut_

Et maintenant, tout semble bon.

## Comment fonctionne la convention commitlint par défaut

La convention commitlint par défaut utilise la [Convention des Commits Conventionnels](https://www.conventionalcommits.org/en/v1.0.0/) où il y a un type, éventuellement une portée, un sujet, et éventuellement un corps et un pied de page. 

Par exemple, je peux corriger un bug lié à l'UI et le message de commit peut être `fix(ui): Button was not showing up properly on mobile view`. Ici, le type est `fix`, c'est-à-dire une correction pour un bug, la portée est `ui` car la correction était liée à l'UI, et le sujet fournit plus de contexte sur le problème. 

Notez que je peux fournir plusieurs portées, par exemple, `feat(ui,lang): added an option to save the image as svg and added language support for Spanish`. Ici, nous introduisons 2 fonctionnalités – un nouveau bouton pour enregistrer une image en svg et un support linguistique pour l'espagnol. Cela signifie qu'il y a 2 portées. Les portées peuvent être séparées par les 3 délimiteurs - `,`, `/` et `\`. 

Juste une petite note ici : vous devriez généralement garder les commits petits et spécifiques, et bien qu'il puisse y avoir quelques cas particuliers, ce n'en est pas un. Nous l'utilisons simplement à des fins d'exemple.

Les changements importants sont généralement représentés par un point d'exclamation `!` mais vous pouvez également les écrire en gras dans le pied de page du message de commit. Faire les deux est la meilleure pratique où le pied de page donne plus d'informations. Voici un exemple :

```
refactor(runtime)!: Dropped support for NodeJS v12

BREAKING CHANGE: Support for NodeJS v12 has been dropped due to the latest refactor, please upgrade to the latest LTS version of NodeJS
```

Cela nous amène aux messages de commit multi-lignes. Parfois, nous devons donner plus de contexte sur quelque chose. Dans ce cas, il est préférable d'inclure les informations dans le message de commit pour le rendre clair pour quiconque essaie de comprendre ce qui a changé et pourquoi cela a changé dans un commit. Voici un exemple :

```
docs: Added an aria-label in the IconButton example
aria-label is a required prop by the IconButton component. If it is not present, the build will fail
```

### Avantages de l'utilisation de commitlint

* Journaux de modifications automatiques – Grâce aux commits suivant une convention standard, des outils comme [standard-version](https://github.com/conventional-changelog/standard-version) peuvent générer automatiquement des journaux de modifications
* Meilleure compréhension des commits – Un commit avec un type et une portée spécifiques vous aidera à comprendre quel code le commit modifie
* Respect d'une convention particulière – Lorsque vous avez un grand projet et beaucoup de personnes qui y contribuent, les gens peuvent oublier d'utiliser la convention. commitlint bloque ces commits afin que les commits respectent la convention définie. 

Maintenant, vous connaissez les bases de commitlint. Et dans la prochaine partie de cet article, nous allons approfondir un peu et voir comment écrire des règles commitlint personnalisées et comment exécuter un commitlint CI dans GitHub Actions.

# Comment créer des règles commitlint personnalisées

La [Convention des Commits Conventionnels](https://www.conventionalcommits.org/) fonctionne pour la plupart des projets. Mais parfois, vous pourriez vouloir ajouter des règles supplémentaires spécifiques à votre cas d'utilisation.

> Pour une référence complète, veuillez [consulter la documentation officielle ici](https://commitlint.js.org/#/reference-rules).

Pour notre exemple ici, nous allons utiliser une application qui possède une bibliothèque de boutons créés avec TailwindCSS. Vous pouvez ajouter votre création à cette application via une pull request. 

Maintenant, ces commits peuvent avoir différents types, alors prenons un `button` pour cet exemple. Cela nécessiterait que je remplace la règle `type-enum` dans la convention des commits conventionnels. 

Pour ce faire, je vais créer un objet `rules` dans ma configuration commitlint et ajouter `button` comme type. Voici à quoi devrait ressembler notre `commitlint.config.js` :

```js
module.exports = {
    extends: [
        "@commitlint/config-conventional"
    ],
    rules: {
        "type-enum": [2, "always", ["build", "chore", "ci", "docs", "feat", "fix", "perf", "refactor", "revert", "style", "test", "button"]],
    }
}
```

Ici, j'ai simplement ajouté le type button en plus des types par défaut. Maintenant, validons cela :

```sh
git add -A
git commit -m "ci(commitlint): added button as a type of commit"
```

Maintenant, nous allons tester notre type `button`. Pour cet exemple, je vais simplement ajouter une nouvelle ligne à notre fichier `index.js`. Voici à quoi il devrait ressembler :

```js
console.log("Hello, World!!!")
console.log("New Button")
```

Maintenant, validons-le :

```sh
git add -A
git commit -m "button: added a new console.log to qualify as a button"
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-36.png)

Vous devriez obtenir le résultat ci-dessus.

# Comment utiliser Commitlint avec GitHub Actions

Les messages de commit sont vérifiés localement, mais malheureusement, de telles vérifications peuvent être ignorées localement. Nous pouvons donc ajouter une étape dans notre workflow CI/CD pour double-vérifier. 

Dans cet exemple, nous allons utiliser [GitHub Actions](https://github.com/features/actions) mais il existe des [guides officiels](https://commitlint.js.org/#/guides-ci-setup) pour Travis CI, Circle CI et GitLab CI également.

## Comment pousser notre code vers GitHub

Tout d'abord, nous devons pousser notre code vers GitHub pour utiliser GitHub Actions. Alors faisons cela rapidement. 

Je vais utiliser le [GitHub CLI](https://github.com/cli/cli) pour cela, mais vous pouvez le faire via l'interface graphique – n'oubliez simplement pas d'ajouter l'amont au dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-37.png)

Nous pouvons pousser le code en utilisant `git push origin master`.

## Comment configurer le workflow

Nous allons utiliser une action GitHub pré-construite pour cet exemple, que vous pouvez trouver ici : [https://github.com/wagoid/commitlint-github-action](https://github.com/wagoid/commitlint-github-action).

Nous devons créer un nouveau dossier appelé `.github` et ensuite un nouveau dossier dans celui-ci appelé `workflows`. Ensuite, nous pouvons ajouter un fichier appelé `commitlint.yml` et ajouter la configuration du workflow.

`.github/workflows/commitlint.yml` 

```yml
name: Lint Commit Messages
on: [pull_request, push]

jobs:
  commitlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0
      - uses: wagoid/commitlint-github-action@v4

```

Ce workflow s'exécutera chaque fois que du code sera poussé vers GitHub et chaque fois qu'une pull request sera ouverte. Pour le tester, validons et poussons notre code.

```sh
git add -A
git commit -m "ci(commitlint,workflow): added GitHub action workflow to run commitlint on push and pr"
git push origin master
```

Maintenant, nous pouvons aller dans le dépôt GitHub et ensuite dans l'onglet actions et nous pouvons voir le workflow.

> J'ai fait une faute de frappe dans le nom du dossier `workflows`, donc j'ai dû le corriger et valider et pousser à nouveau, donc le nom du commit est différent.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-38.png)

Lorsque vous regardez les détails, vous pouvez voir que le workflow a réussi car tous les commits jusqu'à présent ont respecté la convention.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-39.png)

Nous pouvons également inspecter les logs :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-40.png)

# Qu'est-ce qui suit ?

J'espère que tout s'est bien passé pour vous jusqu'à présent. Si vous avez eu des problèmes, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/AnishDe12020) et je serai heureux de vous aider 😃. 

Maintenant que vous avez configuré commitlint, c'est une bonne idée d'ajouter des journaux de modifications automatiques. Alors rendez-vous sur le [dépôt standard version](https://github.com/conventional-changelog/standard-version) et essayez de l'implémenter vous-même !

### Liens utiles

* Dépôt de démonstration - [https://github.com/AnishDe12020/commitlint-example](https://github.com/AnishDe12020/commitlint-example)
* Site web et documentation de Commitlint - [https://commitlint.js.org/#/](https://commitlint.js.org/#/)
* Action GitHub de Commitlint - [https://github.com/wagoid/commitlint-github-action](https://github.com/wagoid/commitlint-github-action)
* Dépôt GitHub de Standard Version - [https://github.com/conventional-changelog/standard-version](https://github.com/conventional-changelog/standard-version)
* Site web et documentation de Husky - [https://typicode.github.io/husky/#/](https://typicode.github.io/husky/#/)
* Commits Conventionnels - [https://www.conventionalcommits.org/](https://www.conventionalcommits.org/)
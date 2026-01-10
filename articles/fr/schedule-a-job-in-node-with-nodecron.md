---
title: Comment planifier un travail dans Node en utilisant node-cron
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2021-07-06T14:27:26.000Z'
originalURL: https://freecodecamp.org/news/schedule-a-job-in-node-with-nodecron
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/schedule.jpg
tags:
- name: node
  slug: node
- name: Productivity
  slug: productivity
seo_title: Comment planifier un travail dans Node en utilisant node-cron
seo_desc: 'In this article, you will learn how to schedule a job in Node using node-cron.

  Node-cron is a handy npm package which you can use to schedule jobs to run at specific
  times or intervals. It is most suitable for scheduling repetitive jobs such as email...'
---

Dans cet article, vous apprendrez comment planifier un travail dans Node en utilisant [node-cron](https://www.npmjs.com/package/node-cron).

Node-cron est un package npm pratique que vous pouvez utiliser pour planifier des travaux à exécuter à des heures ou intervalles spécifiques. Il est particulièrement adapté pour planifier des travaux répétitifs tels que les notifications par email, les téléchargements de fichiers et les sauvegardes de bases de données.

Même si vous n'êtes pas intéressé par la planification d'un travail dans Node, vous pourriez tout de même trouver les connaissances acquises dans cet article sur la syntaxe cron très utiles.

Par exemple, GitHub Actions utilise la [syntaxe cron](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#onschedule) lors de la planification d'un workflow pour qu'il s'exécute à une heure spécifique. De même, les plateformes cloud telles que Google Cloud nécessitent une [syntaxe cron](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules) pour décrire les planifications de travaux.

Node-cron est écrit pour [node](https://nodejs.dev/) en JavaScript pur et est basé sur la syntaxe [GNU crontab](https://www.gnu.org/software/mcron/manual/html_node/Crontab-file.html). Bien qu'il soit basé sur crontab, notre focus dans cet article sera sur l'apprentissage de node-cron et de la syntaxe cron.

Pour en savoir plus sur cron, crontab et leur utilisation dans les systèmes d'exploitation de type Unix, vous pouvez consulter [cet article Wikipedia](https://en.wikipedia.org/wiki/Cron) sur le sujet (mais vous n'avez pas besoin de le connaître pour suivre cet article).

## Ce que vous apprendrez dans cet article

À la fin de cet article, vous serez capable de faire ce qui suit :

* Expliquer la syntaxe [cron](https://en.wikipedia.org/wiki/Cron)

* Planifier des travaux en utilisant node-cron

## Prérequis

Avant de continuer, assurez-vous d'avoir complété les prérequis décrits ci-dessous.

* Vous devez avoir l'environnement d'exécution JavaScript [Node](https://nodejs.dev/download) installé sur votre machine.

* Vous devriez avoir au moins une compréhension basique de JavaScript et Node. Si vous êtes un débutant complet avec Node et JavaScript, vous pouvez poser des questions sur le [forum freeCodeCamp](https://forum.freecodecamp.org/) si vous êtes bloqué. Nous serons heureux de vous aider.

## Comment utiliser `node-cron` pour planifier un travail

Comme je l'ai déjà mentionné ci-dessus, [`node-cron`](https://www.npmjs.com/package/node-cron) a été écrit pour Node et est distribué via [npm](https://www.npmjs.com/). Après l'installation en utilisant la commande `npm i node-cron`, il doit être *requis* dans le projet comme tout autre package Node :

```js
const nodeCron = require("node-cron");
```

Pour planifier un travail, vous devez invoquer la méthode `nodeCron.schedule` avec deux arguments. Il y a un troisième argument optionnel que vous pouvez passer à la méthode pour une configuration supplémentaire.

Voici la signature de la fonction pour la méthode `nodeCron.schedule`.

```js
nodeCron.schedule(expression, function, options);
```

L'extrait de code ci-dessous est un exemple de la façon dont vous pouvez invoquer la méthode `schedule`.

```js
const job = nodeCron.schedule("* * * * * *", function jobYouNeedToExecute() {
  // Faites ce que vous voulez ici. Envoyez un email, faites une sauvegarde de la base de données ou téléchargez des données.
  console.log(new Date().toLocaleString());
});
```

Le premier argument que vous devez passer à `nodeCron.schedule` est l'expression cron. Vous utilisez cette expression pour spécifier l'heure (ou les heures) à laquelle le travail doit être exécuté.

Cette expression doit être au format `* * * * * *`. Vous pouvez remplacer chaque champ `*` par un nombre approprié (ou des caractères si possible) afin que l'expression décrive l'heure à laquelle le travail doit être exécuté.

Si vous passez `"* * * * * *"` sans remplacer aucun `*`, comme dans l'exemple ci-dessus, le travail est exécuté chaque seconde. Pour une explication détaillée de la façon de créer une expression cron, lisez la sous-section "Comment comprendre les expressions cron" ci-dessous.

Le deuxième argument est une fonction et c'est le travail qui est exécuté lorsque l'expression du premier argument est atteinte.

Vous pouvez faire ce que vous voulez dans cette fonction. Vous pouvez envoyer un email, faire une sauvegarde de la base de données ou télécharger des données. Cette fonction est exécutée lorsque l'heure système actuelle correspond à l'heure fournie dans le premier argument. Dans l'exemple ci-dessus, je me contente d'imprimer la date actuelle.

Et le troisième argument est un objet de configuration optionnel pour la planification du travail. Je n'ai pas passé le troisième argument dans l'exemple ci-dessus puisqu'il est optionnel.

Voici un exemple de ce à quoi ressemble le troisième argument.

```js
{
   scheduled: false,
   timezone: "America/Sao_Paulo"
}
```

Par défaut, `scheduled` est `true`. Si vous le définissez sur `false`, vous devrez planifier le travail en invoquant la méthode `start` sur l'objet `job`. `job` est l'objet retourné par un appel à la méthode `schedule`.

```js
job.start();
```

Le fuseau horaire par défaut que nous utilisons est celui du système sur lequel le travail est planifié. Vous pouvez passer un fuseau horaire différent si vous le souhaitez.

## Comment comprendre les expressions Cron

L'expression cron, qui est le premier argument de `schedule`, est une chaîne qui prend la forme `"* * * * * *"`. Nous l'utilisons pour décrire l'heure à laquelle le travail doit être exécuté. Chaque `*` dans l'expression est un champ et vous pouvez voir le champ représenté par chaque `*` dans l'illustration ci-dessous.

```shell
"* * * * * *"
 | | | | | |
 | | | | | |
 | | | | | jour de la semaine
 | | | | mois
 | | | jour du mois
 | | heure
 | minute
 seconde(facultatif)
```

Comme vous pouvez le voir dans l'illustration ci-dessus, le premier champ est le champ `seconde`, le deuxième champ est le champ `minute`, et le troisième est le champ `heure`, et ainsi de suite.

Le tableau ci-dessous montre les champs et leurs valeurs autorisées correspondantes :

| Champ | Valeurs autorisées |
| --- | --- |
| seconde | 0 - 59 |
| minute | 0 - 59 |
| heure | 0 - 23 |
| jour du mois | 1 - 31 |
| mois | 1 - 12 ou noms |
| jour de la semaine | 0 - 7 ou noms, 0 et 7 font référence à dimanche |

> Le travail est exécuté lorsque les champs seconde, minute, heure et mois correspondent à l'heure actuelle, **et** lorsque au moins l'un des deux champs jour (jour du mois ou jour de la semaine) correspond à l'heure actuelle. – [documentation crontab](https://www.gnu.org/software/mcron/manual/html_node/Crontab-file.html)

Il existe différentes façons de remplir les champs dans une expression cron. Chaque champ dans une expression Node peut être rempli en utilisant des valeurs entières uniques, une plage de valeurs, plusieurs valeurs séparées par des virgules, des valeurs de pas ou en utilisant des noms (comme expliqué dans les sous-sections ci-dessous).

### Comment utiliser des valeurs entières uniques pour remplir une expression Chron

Vous pouvez remplacer chaque astérisque par une valeur entière unique dans la plage de valeurs autorisées.

Par exemple, passer `"30 20 * * * *"` fera en sorte que node-cron exécute votre travail à la trentième seconde de la vingtième minute de chaque heure. Puisque vous n'avez pas spécifié de valeur pour le champ heure, node-cron interprète `*` pour signifier chaque heure. Il en va de même pour le champ `jour du mois`, et ainsi de suite.

```js
const job = nodeCron.schedule("30 20 * * * *", () => {
  console.log(new Date().toLocaleString());
});
```

De même, passer `"30 5 13 * * *"` exécutera votre tâche à 13:05:30 chaque jour.

```js
const job = nodeCron.schedule("30 5 13 * * *", () => {
  console.log(new Date().toLocaleString());
});
```

### Comment utiliser une plage de valeurs pour remplir les expressions Chron

Vous pouvez également utiliser des plages de nombres pour remplir vos expressions chron. Une plage fait référence à deux nombres séparés par le caractère `-`. Les valeurs de fin font partie de la plage.

Par exemple, si le champ `heure` est défini sur `2-4`, il spécifie l'exécution aux heures 2, 3 et 4.

```js
const job = nodeCron.schedule("* 2-4 3 * *", () => {
  console.log(new Date().toLocaleString());
});
```

Dans l'extrait de code ci-dessus, j'ai exclu le champ `seconde` facultatif. Il exécutera votre travail chaque minute de 2h à 4h le troisième jour (parce que le champ `jour du mois` a une valeur de `3`) de chaque mois.

### Comment utiliser plusieurs valeurs pour remplir les expressions Chron

Vous pouvez également passer plusieurs valeurs séparées par des virgules ou une plage de valeurs séparées par des virgules.

Par exemple, passer `2,3,4` comme valeur du champ `minute` exécutera votre travail aux minutes 2, 3 et 4.

```js
const job = nodeCron.schedule("2,3,4 * * * *", () => {
  console.log(new Date().toLocaleString());
});
```

Dans l'extrait de code ci-dessus, j'ai à nouveau exclu le champ `seconde` facultatif. Il exécutera votre travail aux première, deuxième et troisième minutes de chaque heure.

### Comment utiliser des valeurs de pas pour remplir les expressions Chrone

Vous pouvez utiliser des valeurs de pas avec des plages. Suivre une plage avec `/<nombre>` saute la valeur du nombre à travers la plage.

Par exemple, utiliser `0-8/2` dans le champ `heure` exécutera le code à 0, 2, 4, 6 et 8 heures. Vous pouvez également utiliser des valeurs de pas avec `*`. Par exemple, `*/3` s'exécute toutes les trois heures.

```js
const job = nodeCron.schedule("*/2 * * * *", () => {
  console.log(new Date().toLocaleString());
});
```

Dans l'extrait de code ci-dessus, le travail sera exécuté toutes les deux minutes. Une fois de plus, j'ai omis le champ `seconde` facultatif.

### Comment utiliser des noms pour remplir les expressions Chron

Pour les champs mois et jour de la semaine, vous pouvez utiliser des noms. Ceux-ci peuvent être des noms courts ou longs. Par exemple, `January` ou `Jan`.

```js
const job = nodeCron.schedule("* * * January,September Sunday", () => {
  console.log(new Date().toLocaleString());
});
```

Une fois de plus, j'ai omis le champ `seconde` facultatif. Le travail s'exécutera chaque minute les dimanches en janvier et septembre. Vous pouvez également utiliser des noms courts comme `Jan, Sep`.

C'est tout ce que vous devez savoir sur les bases de la syntaxe cron. Dans la section suivante, vous mettrez en œuvre ce que vous avez appris pour planifier un travail simple.

> Il existe un outil pratique appelé [crontab guru](https://crontab.guru/) qui peut interpréter les expressions crontab pour vous. Si vous entrez une expression, il validera l'expression et vous dira quand le travail sera exécuté. Vous pouvez l'utiliser si vous n'êtes pas sûr de l'expression.

## Comment planifier un travail en utilisant node-cron

Dans cette section, vous appliquerez ce que vous avez appris dans les sections précédentes. Vous allez créer une application simple qui extrait les données de population mondiale du [site worldometers](https://www.worldometers.info/world-population/) et les enregistre dans la console.

Lorsque vous naviguez vers la [page de population mondiale de worldometers](https://www.worldometers.info/world-population/), vous remarquerez que la population mondiale actuelle change rapidement. Vous allez planifier un travail qui extraira les données et les imprimera dans le terminal.

Dans une application réelle, vous les enregistrerez normalement dans une base de données. Suivez les étapes ci-dessous pour créer l'application.

### Étape 1 - Comment créer un répertoire

Dans cette étape, vous allez créer un répertoire pour votre projet et y naviguer. Ouvrez le terminal et exécutez la commande suivante pour créer un répertoire appelé `learn-node-cron`. Le nom du répertoire n'a pas d'importance. Vous pouvez lui donner un nom différent si vous le souhaitez.

```js
mkdir learn-node-cron
```

Vous devriez voir le dossier `learn-node-cron` créé après avoir exécuté la commande ci-dessus avec succès. Vous pouvez ouvrir le dossier dans votre éditeur de texte préféré. Dans l'étape suivante, vous allez initialiser le projet.

### Étape 2 - Comment initialiser le projet

Dans cette étape, vous allez initialiser le projet en exécutant la commande suivante sur le terminal.

```js
npm init -y
```

Après avoir exécuté la commande ci-dessus avec succès, vous devriez voir le fichier `package.json` créé à la racine du répertoire du projet.

### Étape 3 - Comment installer les dépendances

Dans cette étape, vous allez installer les dépendances du projet en exécutant la commande suivante sur le terminal.

```js
npm i node-cron puppeteer ora chalk
```

L'installation ci-dessus prendra un peu de temps, alors soyez patient. Après avoir installé les dépendances ci-dessus avec succès, vous devriez les voir dans le fichier `package.json` sous le champ `dependencies`.

`node-cron` est la dépendance la plus importante ici car c'est le sujet de cet article.

Nous utiliserons `puppeteer` pour extraire des données d'une page web. Selon la [documentation](https://pptr.dev/), `puppeteer` est :

> Une bibliothèque Node qui fournit une API de haut niveau pour contrôler Chrome ou Chromium via le protocole DevTools. Puppeteer s'exécute en mode headless par défaut, mais peut être configuré pour exécuter Chrome ou Chromium complet (non-headless) - [documentation puppeteer](https://pptr.dev/)

Si la déclaration ci-dessus ne vous semble pas claire, il y a un bel article [sur toptal](https://www.toptal.com/puppeteer/headless-browser-puppeteer-tutorial) qui explique puppeteer, les navigateurs headless et pourquoi ils sont nécessaires. Il est toujours possible de ne pas être intéressé par `puppeteer`. Cet article concerne `node-cron` et comment l'utiliser pour planifier un travail.

[ora](https://github.com/sindresorhus/ora) est un simple package npm que nous utiliserons pour afficher des messages et une animation de chargement sur le terminal pendant que nous extrayons les données. Cela fournira une meilleure expérience utilisateur.

[chalk](https://www.npmjs.com/package/chalk) est un autre package npm que nous utiliserons pour afficher des messages colorés sur le terminal.

Dans l'étape suivante, vous allez implémenter le travail cron.

### Étape 4 - Comment implémenter le travail Cron

Dans cette étape, vous allez implémenter un travail cron simple. Créez un nouveau fichier JavaScript en exécutant la commande suivante :

```js
touch app.js
```

L'exécution réussie de la commande ci-dessus créera un fichier `app.js` à la racine du projet. Copiez et collez le code ci-dessous dans le fichier que vous venez de créer :

```js
const nodeCron = require("node-cron");
const puppeteer = require("puppeteer");
const ora = require("ora");
const chalk = require("chalk");

const url = "https://www.worldometers.info/world-population/";

async function scrapeWorldPopulation() {
  // Affiche un message sur le terminal lorsque le travail planifié commence
  // Nous utilisons chalk pour rendre le message sur le terminal coloré
  console.log(chalk.green("Exécution du travail planifié"));
  // Lance une animation de chargement avec un message approprié sur le terminal
  // Cela offre une bonne expérience utilisateur car le processus de scraping prend un peu de temps
  const spinner = ora({
    text: "Lancement de puppeteer",
    color: "blue",
    hideCursor: false,
  }).start();

  try {
    // Cela nous aidera à calculer la durée du travail plus tard
    const date = Date.now();
    // Lance puppeteer
    const browser = await puppeteer.launch();
    // Change le message sur le terminal lorsque nous lançons
    // une nouvelle page de navigateur headless
    spinner.text = "Lancement de la page du navigateur headless";
    // Lance une nouvelle page de navigateur headless
    const newPage = await browser.newPage();
    // Change le message sur le terminal lorsque nous naviguons
    // vers l'URL de la page que nous extrayons
    spinner.text = "Navigation vers l'URL";
    // Navigue vers l'URL de la page que nous extrayons. Cela prend un peu de temps
    // Vous pouvez changer le délai d'attente à une valeur appropriée si vous le souhaitez, sinon
    // nous attendons jusqu'à ce que la page se charge
    await newPage.goto(url, { waitUntil: "load", timeout: 0 });

    // Change le message sur le terminal lorsque nous commençons à extraire la page
    spinner.text = "Extraction de la page";
    // Commence à extraire la page
    // Si la population mondiale est de 7 876 395 914, alors digitGroups sera
    // ["7", "876", "395", "914"]
    const digitGroups = await newPage.evaluate(() => {
      const digitGroupsArr = [];
      // Pour sélectionner les éléments span contenant des groupes de chiffres
      const selector =
        "#maincounter-wrap .maincounter-number .rts-counter span";
      const digitSpans = document.querySelectorAll(selector);
      // Parcourt les spans de chiffres sélectionnés ci-dessus
      digitSpans.forEach((span) => {
        if (!isNaN(parseInt(span.textContent))) {
          digitGroupsArr.push(span.textContent);
        }
      });
      return JSON.stringify(digitGroupsArr);
    });
    // Change le message sur le terminal puisque nous allons
    // fermer le navigateur headless
    spinner.text = "Fermeture du navigateur headless";
    // Ferme le navigateur headless
    await browser.close();
    // Affiche un message de succès avec la durée qu'il a fallu pour extraire les données en ms
    spinner.succeed(`Extraction de la page réussie après ${Date.now() - date}ms`);
    // Supprime l'animation de chargement du terminal
    spinner.clear();
    // Affiche la population mondiale sur le terminal si l'extraction est réussie
    console.log(
      chalk.yellow.bold(`Population mondiale le ${new Date().toISOString()} :`),
      chalk.blue.bold(JSON.parse(digitGroups).join(","))
    );
  } catch (error) {
    // Affiche un message d'échec sur le terminal si l'extraction échoue
    spinner.fail({ text: "Échec de l'extraction" });
    // Supprime l'animation de chargement du terminal
    spinner.clear();
    // Affiche le message d'erreur sur le terminal
    console.log(error);
  }
}
// Planifie un travail pour qu'il s'exécute toutes les deux minutes
const job = nodeCron.schedule("*/2 * * * *", scrapeWorldPopulation);
```

Dans l'extrait de code ci-dessus, nous avons *requis* toutes les dépendances dont nous avions besoin en haut du fichier. Elles incluent `node-cron`, `puppeteer`, `chalk` et `ora`. Nous extrayons les données de `https://www.worldometers.info/world-population/`, donc je l'ai assigné à la variable `url`.

Puisque notre travail consiste à extraire des données d'un site, j'ai nommé la fonction responsable de l'exécution de notre travail `scrapeWorldPopulation`.

J'ai fait de mon mieux pour donner des noms de variables explicites et commenter presque chaque ligne de code. Vous devriez être en mesure de suivre ce qui se passe dans la fonction `scrapeWorldPopulation`.

Puisque cet article concerne la planification de travaux, je ne vais pas approfondir `puppeteer`. Vous pouvez également implémenter un travail différent si vous le souhaitez.

J'ai planifié le travail pour qu'il s'exécute toutes les deux minutes en invoquant la méthode `nodeCron.schedule` en bas.

Vous pouvez exécuter la commande `node app.js` sur le terminal pour planifier le travail. Vous devriez voir le travail s'exécuter toutes les deux minutes. Voici ce que je vois sur mon terminal après avoir exécuté `node app.js`.

![Terminal](https://www.freecodecamp.org/news/content/images/2021/07/006-01-schedule-job.png align="left")

## Conclusion

Dans cet article, vous avez appris la syntaxe crontab et comment implémenter un travail cron dans Node en utilisant `node-cron`.

Il existe plusieurs projets que vous pouvez essayer pour apprendre la syntaxe cron, par exemple :

* planifier un travail pour récupérer la dernière couverture de vaccination COVID-19 pour votre pays et enregistrer la sortie dans la console

* récupérer les hashtags tendance de Twitter (cela pourrait nécessiter une clé API), ou

* obtenir les derniers titres d'actualités à intervalles de temps, etc.

### Références

* [node-cron](https://github.com/merencia/node-cron)

* [crontab guru](https://crontab.guru/)

* [Puppeteer](https://pptr.dev/)
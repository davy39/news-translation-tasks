---
title: Comment automatiser les tâches les plus répétitives de votre projet open source
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-09T03:44:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-productivity-tools-for-an-open-source-javascript-project-c52d403c5087
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4x8Zuht2TaQ87ZhwYcLUqQ.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment automatiser les tâches les plus répétitives de votre projet open
  source JavaScript
seo_desc: 'By Sarah Dayan

  When I started my career, my mentor told me:


  “A good developer is a lazy developer. Don’t waste time on repetitive tasks, instead
  spend it on building automated processes. The computer works for you, and it will
  always be faster than ...'
---

Par Sarah Dayan

Quand j'ai commencé ma carrière, mon mentor m'a dit :

> « Un bon développeur est un développeur paresseux. Ne perdez pas de temps sur des tâches répétitives, mais passez-le à construire des processus automatisés. L'ordinateur travaille pour vous, et il sera toujours plus rapide que vous. »

C'était en 2010, et l'ensemble d'outils dont nous disposions était plus limité qu'aujourd'hui. Pourtant, ce conseil est resté avec moi depuis.

Des scripts exécutables aux configurations Yeoman, en passant par les setups IFTTT et les workflows Automator, sans oublier la multitude d'applications que j'utilise pour assister chacun de mes mouvements sur l'ordinateur. Je vois l'automatisation comme un jeu et j'en tire beaucoup de satisfaction.

![Image](https://cdn-media-1.freecodecamp.org/images/itLJ8msFhVY-dLL8j2FAttAoPEcDrGl7ZroX)

JavaScript a explosé depuis, et a gagné en complexité. Nous avions l'habitude d'ajouter un fichier JavaScript externe à une page HTML et c'était tout. Mais il y a bien plus à construire un projet web maintenant que simplement coder. Nous avons aussi plus d'outils que nous pouvons utiliser pour décharger les tâches répétitives, donc trouver son chemin à travers tout cela peut être écrasant.

Pour y voir plus clair, j'ai décidé de vous montrer la configuration détaillée pour un projet réel - mon dernier projet open source, [Dinero.js](https://github.com/sarahdayan/dinero.js).

**Avertissement** : Ce n'est pas un tutoriel sur la façon de créer une bibliothèque open source, mais plutôt un aperçu de ce que j'utilise, comment et pourquoi. Pour un guide étape par étape complet, je recommande le cours egghead.io [Comment écrire une bibliothèque JavaScript open source](https://egghead.io/courses/how-to-write-an-open-source-javascript-library) par Kent C. Dodds.

### Gestion des dépendances

#### npm et Yarn

Avant les temps modernes, nous avions l'habitude de télécharger les dépendances à la main et de les charger globalement dans les pages. Cela rendait les choses faciles mais conduisait à un certain nombre de problèmes comme des bibliothèques dupliquées, des dépôts lourds, une gestion des versions difficile.

Heureusement, nous avons maintenant un gestionnaire de dépendances front-end robuste et fiable : [npm](http://npmjs.com/). Si vous venez de PHP, vous pouvez voir npm comme Composer et Packagist réunis. Il fournit le dépôt front-end le plus riche qui soit, et une excellente interface en ligne de commande pour gérer les dépendances.

Beaucoup de gens (y compris moi) préfèrent utiliser [Yarn](https://yarnpkg.com/) : un CLI plus rapide qui intègre un système de cache puissant, parallélise les téléchargements et offre un mode hors ligne. Maintenant, Yarn est _uniquement_ une couche au-dessus du dépôt npm : il parcourt les paquets npm, mais vous permet d'utiliser leur outil à la place.

### Style de codage et conventions

#### EditorConfig

Imaginez que vous travaillez sur plusieurs projets, chacun ayant des conventions différentes. Sur cette bibliothèque, vous avez choisi une indentation de deux espaces, mais ce autre projet open source auquel vous contribuez préfère des onglets de quatre espaces. Allez-vous reconfigurer manuellement votre éditeur chaque fois que vous changez ?

[EditorConfig](http://editorconfig.org/) est un fichier de configuration qui réside dans votre projet et définit les paramètres de l'éditeur. Chaque fois que vous travaillez sur un projet qui a un fichier `.editorconfig`, votre éditeur se conformera à ses règles.

La plupart des éditeurs peuvent analyser les fichiers `.editorconfig`, mais si ce n'est pas le cas pour le vôtre, vous pouvez toujours [télécharger un plugin](http://editorconfig.org/#download).

#### Prettier

L'un des outils pour lesquels je suis le plus reconnaissante est [Prettier](https://prettier.io/). Je l'apprécie tellement que je l'ai comme script npm dans mon projet et comme plugin de l'éditeur de code. C'est à quel point mon amour est profond.

Prettier résout le problème des disputes sur le style de codage et du temps perdu en revue de code. Plus de discussions animées autour des guillemets simples vs. doubles. Plus de Pull Requests rejetées parce que vous avez oublié un espace avant une parenthèse `if`.

Et par-dessus tout, plus de temps perdu à formater le code à la main. Prettier est opiniâtre, donc vous aurez peu de place pour personnaliser les règles par défaut. Et **c'est pour le mieux** : ce n'est pas sur cela que vous devriez passer votre temps précieux.

#### ESLint

Comme pour la grammaire et l'orthographe, votre code n'est pas immunisé contre les fautes de frappe. De plus, il n'est pas improbable d'ajouter accidentellement du code qui peut introduire des bugs, comme des globaux ou des coercitions de type non désirées.

C'est ce dont [ESLint](http://eslint.org/) s'occupe. Il ne réécrira pas votre fichier comme le fait Prettier, mais vous obtiendrez des avertissements dans le terminal.

Il _y a_ un [territoire commun entre ESLint et Prettier](https://prettier.io/docs/en/comparison.html), c'est pourquoi je recommande que :

1. Vous exécutiez Prettier en premier, puis ESLint.
2. Vous utilisiez un outil qui garantit qu'ils ne entrent pas en conflit l'un avec l'autre, comme [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier).

#### Commitizen et cz-conventional-changelog

Vous commencez probablement à voir un schéma ici : oui, **je suis très attachée aux conventions**. Je préfère faire confiance à une convention et me concentrer sur mon travail plutôt que de tomber dans le terrier du [bikeshedding](https://en.wiktionary.org/wiki/bikeshedding), et les messages de commit entrent dans cette catégorie. Maintenant, l'idée derrière les messages de commit conventionnels n'est pas _seulement_ de faire de beaux commits, il s'agit d'automatiser une grande partie de votre workflow CI.

Lorsque vous maintenez un logiciel, il y a certaines tâches fastidieuses qui doivent être prises en charge. Parmi elles, **tenir un changelog à jour** et **versionner le projet**.

Maintenir un changelog à la main est une corvée. Vous devez vérifier chaque commit depuis la dernière version, filtrer ce qui ne concerne pas l'utilisateur (changements dans le système de build, refactors non cassants), découvrir quels changements effectifs ont été faits et les écrire de manière lisible par un humain.

Même chose pour la version.

Selon les changements, vous devez déterminer quelle sera la prochaine version. Peu importe à quel point vous pensez connaître [semver](https://frontstuff.io/setup-for-an-open-source-javascript-project#semantic-release), cela peut être fastidieux d'incrémenter la version à la main. L'erreur humaine conduit facilement à des versions incorrectes, et cela peut être un gros problème pour les utilisateurs.

C'est ce que [Commitizen](https://github.com/commitizen/cz-cli) et [cz-conventional-changelog](https://github.com/commitizen/cz-conventional-changelog) enlèvent de votre assiette. Au lieu de commiter de la manière habituelle, vous exécutez un script qui vous pose des questions. Il committera ensuite pour vous avec un message correctement formaté qui suit les [Angular Git Commit Guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines). Plus tard, lorsque vous déployez avec [semantic-release](https://frontstuff.io/setup-for-an-open-source-javascript-project#semantic-release), ces messages de commit seront utilisés pour générer le changelog et résoudre le nouveau numéro de version. Automatiquement. Sympa, non ?

#### lint-staged

Si vous travaillez en équipe, l'une des meilleures façons d'assurer la qualité du code est de faire des **revues de code**. Il est primordial que le code passant en production soit examiné par au moins une deuxième paire d'yeux.

Maintenant, parce qu'elles sont chronophages, il est important que les revues de code observent quelques règles. Parmi celles-ci, **le temps de revue ne doit pas être utilisé pour repérer des erreurs de linting**.

Tout le formatage et le linting doivent se faire avant le commit. Cela ne doit pas distraire le relecteur de son travail, et cela ne doit pas casser le build. C'est pourquoi [lint-staged](https://github.com/okonet/lint-staged) est si utile : chaque fois que vous commitez, il agira comme un hook de pré-commit et exécutera un script de votre choix.

Dans Dinero.js, voici à quoi ressemble ma configuration lint-staged :

```
{  "lint-staged":    { "*.js": ["npm run lint!", "git add"]  }}
```

La commande `npm run lint!` déclenche séquentiellement deux autres scripts : `npm run format` (Prettier), puis `npm run lint` (ESLint). Chaque fois que j'essaie de commiter un fichier JavaScript, Prettier le reformatera. Ensuite, ESLint effectuera une analyse : si elle passe, le commit sera validé. Sinon, ESLint générera une erreur et le commit sera annulé.

### Documentation

#### JSDoc

La documentation doit vivre aussi près que possible du code qu'elle décrit. C'est un bon moyen de la garder à jour et de garantir son exhaustivité. Une excellente implémentation de cette idée est le **doc blocking** : utiliser des commentaires formatés pour documenter le code, qui peut ensuite générer automatiquement un site de documentation. En JavaScript, le générateur de documentation le plus populaire est [JSDoc](http://usejsdoc.org/).

Avec JSDoc, tout ce que vous avez à faire est d'ajouter un commentaire avec des tags et des descriptions spécifiques au-dessus de chaque partie significative du code (une fonction, un module, etc.)

```
{  /**   * Retourne la devise.   *   * @example   * // retourne 'EUR'   * Dinero({ currency: 'EUR' }).getCurrency()   *   * @return {String}   */  getCurrency() {    return currency  }}
```

_Ce bloc de documentation a une description, un exemple et une valeur de retour typée._

Une fois écrits, les blocs de documentation peuvent être transformés en un site de documentation avec une seule commande. Vous pouvez utiliser n'importe quel modèle JSDoc préexistant pour générer votre site ou créer le vôtre.

![Image](https://cdn-media-1.freecodecamp.org/images/rh8AAuIHvLoVLCEvo239DqAfI9sgcMCXhXcQ)
_Voici à quoi ressemble le bloc de documentation pour `Dinero.getCurrency` une fois compilé en un site web._

#### Pourquoi pas ESDoc ?

Le nouveau venu sur le bloc, [ESDoc](https://esdoc.org/), adopte une approche différente de JSDoc. Parmi d'autres choses, ESDoc a été conçu pour bien fonctionner avec les classes ES6, et le code concret en général. L'inconvénient est qu'il [ne supporte pas les fonctions factory](https://github.com/esdoc/esdoc/issues/300).

Les fonctions factory sont des générateurs d'objets dynamiques, un comportement que ESDoc ne couvre pas. Si vous essayez de documenter une factory avec ESDoc, la documentation générée reviendra vide.

Dans mon cas, les factories sont les blocs de construction de Dinero.js, ce qui explique mon choix.

Si votre projet utilise la syntaxe des classes ES6, ESDoc répondra à tous vos besoins. Sinon, optez pour JSDoc : il supporte toutes les fonctionnalités ES6, ainsi que les motifs « plus anciens » comme les fonctions factory et la syntaxe originale pour les constructeurs.

#### Algolia DocSearch

Vous avez peut-être écrit votre documentation avec soin et l'avez présentée dans un joli site web, mais à la fin de la journée, ce qui compte, c'est que les utilisateurs trouvent ce dont ils ont besoin le plus rapidement possible. Personne n'aime interrompre son flux de travail trop longtemps pour aller chercher quelque chose dont il a besoin. Il n'est pas surprenant que StackOverflow soit si populaire : les gens ont besoin de réponses à leurs questions, et ils en ont besoin _rapidement_.

[Algolia](http://algolia.com/) est le meilleur service de recherche qui existe. Leur solution (gratuite) [DocSearch](https://community.algolia.com/docsearch) vous permet de créer une excellente expérience de documentation pour vos utilisateurs. DocSearch est un service à la demande : une fois vos docs prêtes, envoyez-leur une URL et vous recevrez un extrait de code à ajouter à votre site web.

### Tests

#### Mocha et Chai

Les tests unitaires sont cruciaux. Si vous ne pouvez faire **qu'une seule** chose pour la qualité du code, oubliez le linting, oubliez le formatage, oubliez les revues de code et **écrivez des tests unitaires**.

Les tests unitaires vous obligent à construire un code modulaire, à responsabilité unique et garantissent que vous ne cassez pas les choses qui fonctionnaient bien. C'est une partie cruciale de l'intégration continue. Si vous êtes sérieux au sujet de ce que vous construisez, vous devriez le tester unitairement à 100 %.

Maintenant, si vous débutez, les tests unitaires peuvent sembler un peu effrayants. La bonne nouvelle est qu'ils n'ont pas à l'être : grâce à des outils comme [Mocha](http://mochajs.org/) et [Chai](http://chaijs.com/), écrire des tests devient vraiment proche d'être _amusant_.

Voici un extrait de mes tests unitaires pour Dinero.js :

```
import chai from 'chai'import Dinero from '../../src/dinero'
```

```
const expect = chai.expect
```

```
describe('Dinero', () => {  describe('#getAmount()', () => {    it('should return the right amount as a number', () => {      expect(Dinero({ amount: 500 }).getAmount()).to.equal(500)    })    it('should return the default amount as a number when no amount is specified', () => {      expect(Dinero().getAmount()).to.equal(0)    })  })})
```

Ce fichier JavaScript, appelé un « spec », utilise le framework Mocha et la bibliothèque d'assertion Chai. L'API publique est construite pour ressembler à des phrases anglaises réelles : même les personnes non techniques peuvent lire les fichiers spec et comprendre ce qui se passe. Cela facilite la tâche des nouveaux contributeurs, car la courbe d'apprentissage est presque inexistante.

Les tests utilisant Mocha et Chai sont exécutés nativement avec Node.js, ce qui signifie qu'il attend des modules CommonJS pour les fichiers spec et source. Mais grâce à Babel, nous n'avons pas à écrire du CJS si nous ne le voulons pas : nous pouvons toujours utiliser des modules ES et les transpiler à la volée lorsque nous exécutons les tests ! C'est ainsi que je peux inclure des modules avec `import` au lieu de `require` et avoir des tests parfaitement fonctionnels.

#### Istanbul et Coveralls

Écrire des tests unitaires est génial, mais à mesure que votre projet grandit, vous pouvez perdre la trace de ce qui doit être testé. Ce n'est pas de votre faute : vous êtes occupé à construire quelque chose et il y a beaucoup de choses à retenir. C'est pourquoi nous automatisons les tâches, pour nous assister et nous aider à nous souvenir des choses que nous oublions. La couverture de code surveille votre code régulièrement (généralement chaque fois que vous exécutez des tests) et vous donne un rapport sur la quantité de code qui est couverte par des tests unitaires.

[Istanbul](https://istanbul.js.org/) est un outil de couverture de code. Dans Dinero.js, j'utilise [nyc](https://github.com/istanbuljs/nyc), son interface en ligne de commande, pour générer des rapports.

![Image](https://cdn-media-1.freecodecamp.org/images/Z4W6jmCZb744cuSylmvaqFofFtaZrrXX7mdL)
_Un rapport Istanbul une fois les tests unitaires terminés._

Istanbul génère des rapports dans tous les formats : sortie terminal, HTML, mais aussi [LCOV](http://ltp.sourceforge.net/coverage/lcov.php). Celui-ci est particulièrement utile lorsqu'il est utilisé avec des services en ligne comme [Coveralls](https://coveralls.io/). Chaque fois que [Travis CI](https://frontstuff.io/setup-for-an-open-source-javascript-project#travis-ci) exécute un build, il exécute des tests et nyc génère un fichier LCOV. Il est ensuite envoyé à Coveralls qui génère des statistiques détaillées. Cela est particulièrement utile pour les contributions : lorsqu'une personne soumet une pull request, un bot Coveralls répond automatiquement avec la couverture mise à jour. Cela contribue à rendre les revues de code plus faciles et plus rapides.

### Build

#### Babel

ES6+ a apporté des fonctionnalités incroyables à JavaScript, mais elles ne sont toujours [pas supportées partout](https://kangax.github.io/compat-table/es6). Cela ne signifie pas que vous devez attendre avant de pouvoir commencer à l'utiliser : voici [Babel](https://babeljs.io/).

Babel est un _transpiler_. Il traduit le code dans un autre langage ou une autre _version_ du même langage. Votre code source reste le même, mais ce que l'utilisateur obtient est traduit dans une autre syntaxe pour garantir qu'il fonctionne dans son environnement. Vous pouvez utiliser des fonctionnalités de pointe, des syntaxes propres et garder votre code source propre, et vous n'avez pas à vous soucier de son fonctionnement sur les anciens navigateurs.

J'ai écrit l'intégralité du code source de Dinero.js en utilisant des fonctionnalités ES6, telles que les fonctions fléchées et les modules ES. Chaque fois que je publie une version, Babel transpile les fichiers source en code ES5 distribuable.

Babel est également utile pour les tests unitaires. J'utilise Node.js pour cela, qui ne supporte pas nativement les modules ES, donc ne peut pas gérer mes fichiers source. Grâce à Babel, je peux les transpiler à la volée chaque fois que j'exécute ma commande de test.

#### Rollup

Une fois que votre bibliothèque est prête, vous devez la packager pour qu'elle puisse être utilisée par différentes personnes dans différents environnements. Certains l'utiliseront avec Node. D'autres en auront besoin directement dans le navigateur en tant que balise de script. D'autres encore voudront l'utiliser comme un module ES à inclure dans leur propre projet et à bundler avec leurs propres outils.

[Rollup](https://rollupjs.org/) est un bundler de modules comme Webpack ou Parcel, mais il est particulièrement utile pour construire des bibliothèques JavaScript. Il a été conçu pour fonctionner avec les modules ES, et les transformer dans n'importe quel format de module que vous souhaitez.

À l'époque, le code que nous écrivions était exactement le code qui se retrouvait en production. Si vous vouliez que votre code soit aussi omniprésent que possible, vous l'enveloppiez dans un motif [UMD](https://github.com/umdjs/umd) à la main. Aujourd'hui, vous pouvez coder exactement comme vous le souhaitez et livrer différents bundles pour tout le monde, grâce aux bundlers de modules comme Rollup. Besoin d'une version UMD ? La voici. Avec un [AMD](http://requirejs.org/docs/whyamd.html#amd), un [CJS](https://nodejs.org/docs/latest/api/modules.html), un [IIFE](https://developer.mozilla.org/docs/Glossary/IIFE), n'importe quoi.

### CI

#### GitHub

La plateforme collaborative open source la plus populaire ne nécessite pas d'introduction. [GitHub](https://github.com/) est un produit merveilleux qui comble tout ce que les développeurs peuvent espérer et plus encore. Il héberge la plupart de mes projets. Il héberge ce blog. Il se connecte avec les meilleurs outils CI du marché. Si vous voulez contribuer à vos projets open source préférés, vous construire une réputation et créer les meilleurs outils pour d'autres développeurs, ne cherchez pas plus loin.

#### Travis CI

Vous pouvez voir [Travis CI](http://travis-ci.org/) comme le chef d'orchestre du processus de build de votre projet.

Créer un projet de qualité est difficile, et le codage n'en est qu'une petite partie. Il y a des tâches à exécuter dans un certain ordre, au bon moment, dans les bonnes circonstances. Voici une liste de tout ce qui doit être fait une fois que je veux livrer quelque chose pour Dinero.js :

Exécuter les tests unitaires. **Si ils passent** :

* Exécuter la couverture de code
* Construire une version (fichiers dist)
* Recompiler les docs
* Taguer une version et pousser le tag sur GitHub
* Incrémenter la version et pousser le build sur npm
* Écrire une entrée dans le changelog
* Pousser les fichiers docs sur GitHub Pages

**Sinon**, corriger les choses, rincer et répéter.

Avant d'installer mon pipeline CI, j'ai essayé de faire cela à la main. Devinez quoi ? Il n'y a pas eu _une seule fois_ où je l'ai fait correctement. Pourquoi ? Parce qu'en tant qu'humain typique, je suis sujet aux erreurs et aux distractions. D'un autre côté, les machines répondent bien aux ordres. Elles feront exactement ce que vous voulez, comme vous le voulez. Tout ce que vous avez à faire est de le spécifier bien, _une fois_.

Travis CI est gratuit pour les projets open source et s'intègre bien avec les services tiers. Tout ce que vous avez à faire est de vous connecter avec votre compte GitHub et de synchroniser un projet. Par défaut, Travis exécutera les tests chaque fois que vous pousserez vers votre dépôt distant. Ensuite, vous pouvez [dire à Travis quoi faire](https://docs.travis-ci.com/user/customizing-the-build) lorsque les tests passent avec un fichier `.travis.yml` à la racine du projet.

#### semantic-release

Avant de vous lancer dans ce que fait semantic-release, vous devez comprendre le [Versionnage Sémantique](https://semver.org/) (aka « semver »).

En bref, semver est une convention basée sur un format numérique X.Y.Z, respectivement MAJEUR, MINEUR et PATCH :

* Lorsque vous corrigez un bug mais que vos changements sont rétrocompatibles, vous incrémentez le PATCH.
* Lorsque vous ajoutez une fonctionnalité mais que vos changements sont toujours rétrocompatibles, vous incrémentez le MINEUR.
* Lorsque vous faites des changements quelconques incompatibles, vous incrémentez le MAJEUR.

Cela aide les personnes qui dépendent de votre projet à savoir si elles peuvent mettre à jour en toute sécurité, et simplifie la gestion des dépendances en général.

Le Versionnage Sémantique est largement utilisé dans le développement logiciel, mais il peut être difficile à appliquer. Encore une fois, nous, les humains, sommes sujets aux erreurs et aux sentiments. Si vous oubliez de prendre en compte un commit, avez un doute sur la nature d'un changement, ou ne comprenez pas tout à fait semver, vous pouvez mal étiqueter une nouvelle version. Si vous corrigez un petit bug qui a échappé à votre attention juste après avoir publié une nouvelle version, vous pourriez être tenté de le glisser et de faire comme si de rien n'était. C'est là que [semantic-release](https://github.com/semantic-release) entre en jeu.

En bref, semantic-release **s'occupe du versionnage pour vous**. Vous n'avez pas votre mot à dire. Il utilise vos [messages de commit écrits de manière conventionnelle](https://frontstuff.io/setup-for-an-open-source-javascript-project#commitizen--cz-conventional-changelog) pour décider quelle sera la prochaine version. Ajoutez-le à votre pipeline CI (dans votre workflow [Travis CI](https://frontstuff.io/setup-for-an-open-source-javascript-project#travis-ci), par exemple), et vous obtenez un système entièrement automatisé qui lira vos commits, changera la version, la taguera, la poussera sur GitHub, la poussera sur npm, et écrira votre changelog. Ouf.

### N'est-ce pas un peu trop ?

Cela peut sembler beaucoup de choses à configurer. « Ai-je vraiment besoin de tout cela ? » pourriez-vous vous demander. Je répondrai avec quelques questions : combien de tâches gérez-vous actuellement à la main ? Combien de temps vous prend une version ? À quel point êtes-vous confiant lorsque vous le faites ? Quand était la dernière fois que vous avez effectué l'intégralité de votre workflow sans rien oublier ?

Personnellement, je ne peux pas déployer une version à la main sans une feuille de triche. Linting, formatage, tests, couverture de code, docs, build, versionnage sémantique, release, mise à jour du changelog, tout dans cet ordre tout en m'assurant que je suis sur la bonne branche... ouf. J'espère vraiment que je n'ai pas laissé une faute de frappe ! Ce processus est si chronophage, vous pouvez le gâcher de tant de manières, et il vous prend tellement de temps à chaque fois pour le travail réel, que **l'automatiser devrait être une évidence**.

Cela semble compliqué lorsque vous n'êtes pas habitué, mais une fois que vous avez construit votre workflow, tout ce que vous avez à faire est de le maintenir. Mettre à jour les dépendances, garder un œil sur les nouveaux outils innovants, améliorer le processus. Vous pouvez même utiliser un outil de scaffolding pour sauvegarder toute votre configuration et déployer des modèles de projets prêts à l'emploi. Essayez !

Et vous ? Quel est votre workflow pour les projets web ? Qu'est-ce qui a facilité votre vie ? Venez discuter avec moi sur [Twitter](https://twitter.com/frontstuff_io) !

De plus, vous pouvez consulter plus de mes articles sur [mon blog](https://frontstuff.io/setup-for-an-open-source-javascript-project).
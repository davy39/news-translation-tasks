---
title: Améliorons la bonne vieille ligne de commande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T20:02:01.000Z'
originalURL: https://freecodecamp.org/news/lets-fix-the-good-old-command-line-b6eaa1f9c040
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0ClHN36X6976f6SnpcId6w.jpeg
tags:
- name: api
  slug: api
- name: command line
  slug: command-line
- name: Developer Tools
  slug: developer-tools
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Améliorons la bonne vieille ligne de commande
seo_desc: 'By Manuel Vila

  Although we have beautiful graphical user interfaces, it seems that we are using
  more and more command-line tools. And while many of them are really good, I think
  they could be even better if they were based on more modern foundations....'
---

Par Manuel Vila

Bien que nous disposions de belles interfaces utilisateur graphiques, il semble que nous utilisions de plus en plus d'outils en ligne de commande. Et bien que beaucoup d'entre eux soient vraiment bons, je pense qu'ils pourraient être encore meilleurs s'ils étaient basés sur des fondations plus modernes.

Pour illustrer le problème, je vais considérer deux caractéristiques essentielles : la personnalisation et l'utilisabilité. Et, en examinant certains des outils les plus populaires, je vais montrer à quel point il est difficile d'atteindre ces deux caractéristiques en même temps.

Je vais parler principalement des outils JavaScript, car c'est l'environnement avec lequel je suis le plus à l'aise. Mais le problème est similaire, quel que soit l'environnement de développement.

### Create React App

[Create React App](https://github.com/facebook/create-react-app) illustre le cas d'un outil très facile à utiliser mais peu personnalisable. Il rassemble un ensemble d'outils, de techniques et de bonnes pratiques pour démarrer une application web moderne en un rien de temps.

À cet égard, il est extrêmement précieux, mais il est implémenté comme une boîte noire. Il est difficile de changer quelque chose à l'intérieur. Oui, il y a une fonction `eject`, mais je ne pense pas que ce soit une vraie solution. C'est échanger une caractéristique contre une autre. L'outil devient plus personnalisable mais n'est plus facile à utiliser.

### npm scripts et code spécifique

Ici, nous avons le plus haut niveau de personnalisation, mais l'utilisabilité est faible. En écrivant des [npm scripts](https://medium.freecodecamp.org/introduction-to-npm-scripts-1dbb2ae01633) et du code spécifique, il est possible de créer toutes sortes de builders, deployers, etc. Mais ce n'est pas à la portée de tous, et c'est une tâche assez laborieuse. Assembler un ensemble d'outils en utilisant des npm scripts (c'est-à-dire, [Bash](https://www.gnu.org/software/bash/)) n'est pas très convivial, et écrire du code en JavaScript pour configurer et contrôler des outils via des modules npm est quelque peu fastidieux.

### [webpack](https://webpack.js.org/), [gulp](https://gulpjs.com/), [Serverless Framework](https://serverless.com/framework/), etc.

Enfin, voici quelques outils qui sont à la fois assez personnalisables et faciles à utiliser. Mais le prix à payer est élevé. Nous devons gérer leur système de plugins, ou plutôt, le fait qu'il existe un tel système.

Le problème est que chaque fois qu'un outil offre un système de plugins, il crée un nouvel écosystème. Le résultat est que, au lieu d'avoir un écosystème global d'outils, nous finissons avec une prolifération d'écosystèmes qui fonctionnent en silos. Ainsi, de nombreux plugins font la même chose mais pour différents écosystèmes (par exemple, `[awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader)`, `[gulp-typescript](https://github.com/ivogabe/gulp-typescript)`, `[serverless-plugin-typescript](https://github.com/graphcool/serverless-plugin-typescript)`, etc.). Quel gaspillage de temps.

Très souvent, lorsqu'un outil implémente un système de plugins, c'est un indicateur que quelque chose ne va pas. Il essaie de résoudre un problème qui devrait probablement être abordé à un niveau inférieur.

![Image](https://cdn-media-1.freecodecamp.org/images/bknkJrgYXw8sDcmt4QdpnNeRsPTm5Rq078t0)

### *nix, Bash, etc.

Ne vous méprenez pas. Tous les outils que j'ai mentionnés précédemment sont fantastiques. Étant donné les fondations sur lesquelles ils sont basés, ils font du bon travail. Je veux dire qu'ils doivent lutter avec les systèmes de type Unix et les shells tels que [Bash](https://www.gnu.org/software/bash/). Pouvez-vous croire que tous nos outils modernes sont basés sur des fondations qui ont à peine changé en près d'un demi-siècle ?

Typiquement, lorsque nous travaillons sur un projet, nous utilisons plusieurs outils tels que (dans le cas d'un projet web moderne), un gestionnaire de dépendances, un transpileur, un bundler, et ainsi de suite. Nous avons donc besoin d'un moyen d'installer, de configurer et de composer toutes ces choses. Malheureusement, notre bonne vieille ligne de commande n'est pas très bonne pour cela.

Nous utilisons des fichiers de configuration basés sur de nombreux formats différents pour configurer nos outils. Nous communiquons avec eux via un tableau de chaînes de caractères (`argv`). Pour les composer, il y a, eh bien, Bash... Enfin, puisque les shells typiques ne peuvent pas gérer plusieurs versions du même outil, la gestion de notre environnement de développement est douloureuse lorsque nous devons gérer de nombreux projets.

Sérieusement, nous ne pouvons pas dire que c'est convivial. Bien sûr, nous avons de grands langages de programmation et des bibliothèques riches. Les outils sont beaux à l'intérieur, mais à l'extérieur, ils sont laids. Lorsque cela vient à les configurer, les composer et les exécuter, ce n'est pas cool, et à cause de cela, nous finissons avec le dilemme personnalisation-utilisabilité.

### Bonjour, les "ressources"

J'ai travaillé à temps plein pendant un an pour essayer de résoudre ce problème, et j'ai fini par ce que j'appelle une "[ressource](https://run.tools/docs/introduction/what-is-a-resource)". De plus, en tant que preuve de concept, j'ai construit "[Run](https://run.tools/)", un runtime de ressource.

Alors, à quoi sert une ressource ? Basiquement, une ressource ajoute une interface orientée objet aux outils, les rendant plus faciles à utiliser à la fois depuis la ligne de commande et, de manière programmatique, depuis d'autres outils.

Si vous créez un outil, vous pouvez l'envelopper dans une ressource pour améliorer son utilisabilité et économiser beaucoup de temps de développement. Tout d'abord, puisque Run installe les outils automatiquement, le problème d'installation disparaît. Ensuite, étant donné que les utilisateurs configurent les outils en utilisant des ressources, vous n'avez pas besoin de gérer des fichiers de configuration. Enfin, vous n'avez plus besoin d'implémenter une interface en ligne de commande. Run la fournit pour vous.

Si vous êtes un développeur final, et que vous travaillez sur une application, un site web, un backend, etc., vous pouvez utiliser une ressource pour référencer les outils dont votre projet a besoin, et spécifier leur configuration. Ensuite, puisque votre environnement de développement est défini dans un seul fichier, votre projet est super facile à transporter et à partager. Il suffit de prendre la ressource et vous êtes prêt. De plus, puisque votre ressource consomme des outils qui sont eux-mêmes des ressources, tout devient extrêmement facile à configurer, à composer et à utiliser.

### À quoi cela ressemble-t-il ?

Une ressource est un document JSON ou YAML qui vous permet de spécifier ce qui suit :

* Les outils que la ressource consomme (en les héritant ou en les composant)
* Un ensemble d'attributs (pour configurer les outils)
* Un ensemble de méthodes (pour ajouter des comportements personnalisés)

Par exemple, pour construire un site web, vous pouvez commencer avec quelque chose comme ceci :

```
{  "@import": "aws/s3-hosted-website#^0.1.0"}
```

Ensuite, en invoquant Run sans aucun argument :

```
run
```

Vous obtenez une aide auto-générée reflétant le contenu de votre ressource :

![Image](https://cdn-media-1.freecodecamp.org/images/f1pzp0tOzgb4CAuXr60GlBWOg9wo3FJ-uTED)

Parce que la ressource importe `"aws/s3-hosted-website"`, elle hérite d'un certain nombre d'attributs et de méthodes. Spécifions quelques attributs :

```
{  "@import": "aws/s3-hosted-website#^0.1.0",  "domainName": "www.example.com",  "contentDirectory": "./content"}
```

Enfin, invoquons la méthode `deploy` :

```
run deploy
```

Et voilà ! Votre site web est en ligne. Qu'en est-il de cette chose `"aws/s3-hosted-website#^0.1.0"` ? Il s'agit d'une référence à une ressource qui implémente un outil pour gérer des sites web statiques hébergés sur AWS. Et, pour faciliter son utilisation, elle est stockée dans un [répertoire de ressources](https://resdir.com/).

J'ai joué avec les ressources de manière assez intensive pendant des mois, et vraiment, il semble que le dilemme personnalisation-utilisabilité soit résolu. Par exemple, voici une ressource pour un site web plus réaliste incluant des dépendances npm (sans fichier `package.json` !) et une méthode `build` qui exécute un transpileur, un bundler et un copieur de fichiers :

```
{  "@import": ["aws/s3-hosted-website#^0.1.0", "js/resource#^0.1.0"],  "domainName": "www.example.com",  "contentDirectory": "./build",  "dependencies": {    "color": "^3.0.0",    "lodash": "^4.17.4"  },  "build": {    "@type": "method",    "@run": ["transpiler run", "bundler run", "copier run"]  },  "transpiler": {    "@import": "js/transpiler#^0.1.0",    "source": "./src",    "destination": "./dist",    "targets": {"chrome": "41", "safari": "10", "firefox": "50"},    "format": "esm"  },  "bundler": {    "@import": "js/bundler#^0.1.0",    "entry": "./dist/index.js",    "output": "./build/bundle.js",    "target": "browser",    "format": "iife"  },  "copier": {    "@import": "tool/file-copier#^0.1.0",    "sourceDirectory": "./",    "destinationDirectory": "./build",    "files": ["./index.html", "./images"]  }}
```

Assez facile, n'est-ce pas ? Si vous êtes perdu, l'aide auto-générée de Run est votre guide. Par exemple, pour en savoir plus sur le bundler, il suffit d'invoquer :

```
run bundler
```

Vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/LHZGwRocjigwamqLwwv7RiJFLpA618ONAv1v)

### Conclusion

Je ne dis pas que le concept de ressource est le Saint-Graal, mais c'est le meilleur que j'ai trouvé jusqu'à présent, et c'est un travail en cours. Les spécifications ne sont pas encore stables ; tout peut changer, même la dénomination "ressource" peut changer.

Pour en savoir plus sur l'état actuel de Run et des ressources, vous pouvez consulter la [documentation](https://run.tools/docs) et le [dépôt GitHub](https://github.com/runtools/run).

Alors, qu'en pensez-vous ? Est-ce seulement moi qui ai un problème avec la ligne de commande ? Ou est-ce quelque chose qui doit être corrigé ? Et si c'est le cas, croyez-vous que ce concept de ressource est un pas dans la bonne direction ?
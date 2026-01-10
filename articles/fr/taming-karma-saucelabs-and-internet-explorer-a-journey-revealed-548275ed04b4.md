---
title: 'Domptage de Karma, SauceLabs et Internet Explorer : un voyage révélé'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-16T03:49:08.000Z'
originalURL: https://freecodecamp.org/news/taming-karma-saucelabs-and-internet-explorer-a-journey-revealed-548275ed04b4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ex9axm71QoSG-erRQQBWuw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: React
  slug: react
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: 'Domptage de Karma, SauceLabs et Internet Explorer : un voyage révélé'
seo_desc: 'By Gregory Beaver

  It seemed simple enough.

  Just set up karma with TravisCI to run tests on SauceLabs so I can be certain my
  code doesn’t break the internet when Granny wipes off the cobwebs and fires up Internet
  Explorer to browse to a site that uses...'
---

Par Gregory Beaver

Cela semblait assez simple.

Il suffisait de configurer karma avec [TravisCI](http://travis-ci.org) pour exécuter des tests sur [SauceLabs](https://saucelabs.com) afin d'être certain que mon code ne casse pas Internet lorsque Mamie essuie les toiles d'araignée et lance Internet Explorer pour naviguer vers un site qui utilise mon code.

Au début, il semblait que le plus grand défi serait de configurer karma.conf.js. Mon projet, [react-selection-hoc](http://cellog.github.io/react-selection/), est un composant React qui permet à toute liste de choses de devenir sélectionnable en utilisant des [Higher Order Components](https://medium.com/@dan_abramov/mixins-are-dead-long-live-higher-order-components-94a0d2f9e750#.pliuiqo22). En bref, je veux m'assurer qu'il fonctionne sur tous les navigateurs sur lesquels il pourrait fonctionner.

Le projet est écrit en ES6 et JSX, donc pour que karma fonctionne, je devais somehow packager le code de manière à ce que babel puisse le convertir en es5. Cela s'est avéré beaucoup plus difficile que je ne l'avais prévu. Finalement, j'ai trouvé la solution dans la manière dont [react-big-calendar](http://intljusticemission.github.io/react-big-calendar/examples/index.html) le gère, en packgeant les tests avec le plugin karma-webpack. Cela a fonctionné fabuleusement avec le navigateur Chrome local. Terminé !

Étape suivante : configurer SauceLabs. Note : J'ai considéré utiliser [BrowserStack](https://browserstack.com), qui est oh-so-sexy et la meilleure chose pour les tests manuels, mais les tests automatisés ont certaines limitations qui signifiaient que la suite de tests s'exécutait environ 10 à 15 minutes plus lentement que SauceLabs. Une partie de cela était due au compte gratuit limité, une partie à la conception, mais finalement SauceLabs répond mieux à mes besoins. Si j'étais closed source avec des méga-bucks, je choisirais probablement BrowserStack, mais ce n'est ni ici ni là.

Configurer SauceLabs est difficile. Non pas parce que c'est difficile, mais parce que la documentation est dispersée dans tout l'univers. Le configurateur pour SauceLabs est obsolète, mais en triangulant avec la liste des plateformes, il est possible de créer un tableau de navigateurs qui fonctionnera.

De plus, je voulais pouvoir développer rapidement un test localement, en utilisant la fonctionnalité autowatch de karma, une sorte de Hot Module Reload pour les tests. La manière dont j'ai initialement résolu cela était d'utiliser une commande séparée pour les tests locaux, qui passe une variable d'environnement à karma qui lui fait utiliser uniquement le navigateur Chrome local avec singleRun défini sur false. Désactivez la variable d'environnement QUICKTEST, et il se connecte à saucelab. Bien sûr, je dois me souvenir de démarrer le [tunnel de connexion saucelabs](https://wiki.saucelabs.com/display/DOCS/Sauce+Connect+Proxy) et vous ne devriez pas oublier cela lorsque vous exécutez votre propre configuration.

En bref, voici la première configuration fonctionnelle que j'ai utilisée ! Tout semblait bien jusqu'à...

#### Le purgatoire commence

Une partie de mon objectif avec les tests unitaires pour react-selection-hoc est de m'assurer que les particularités des navigateurs sont testées et prises en compte afin que toute contribution ait un cadre de test pour s'assurer qu'elles ne cassent pas l'installation de quelqu'un d'autre. Le code n'utilise que quelques fonctions de mesure spécifiques au DOM pour déterminer si un clic/tap ou un glisser de souris/doigt est sur un élément sélectionnable ou non. Cela devrait être simple à tester, non ?

Pour tester ces choses simples dans tous les navigateurs de manière authentique, pour vraiment vérifier la justesse du code, cela signifie modifier le DOM puis l'interroger. À cause du fonctionnement de Karma, cela signifie que l'environnement de test réel est modifié, ce qui est là où nous entrons dans le purgatoire dans cette histoire.

> À cause du fonctionnement de Karma, cela signifie que l'environnement de test réel est modifié, ce qui est là où nous entrons dans le purgatoire dans cette histoire.

Au début, les choses semblaient cool. J'ai trouvé des cas limites qui ne fonctionnaient pas sous iOS et Internet Explorer, je les ai corrigés et je suis passé à autre chose. Ensuite, j'ai commencé à remarquer des tests qui échouaient aléatoirement alors qu'ils avaient fonctionné auparavant.

Mais le pire, c'est quand j'ai exécuté les tests IE en isolation, c'est-à-dire uniquement sur Internet Explorer et Edge, ils ont tous réussi. Chaque. Seule. Fois.

Alors, pour rectifier cela, j'ai d'abord essayé de mettre le code de manipulation du DOM dans leurs propres blocs describe, avec du code before/after pour configurer la manipulation. Aucune amélioration. Ensuite, j'ai essayé de définir useIframes à false, ce qui indique à Karma d'exécuter les tests dans une fenêtre séparée. Cela a très bien fonctionné pour Internet Explorer, mais a cassé chaque navigateur mobile, et m'a laissé dans un état de désespoir.

#### La solution, ou le nirvana apparaît

Le moment d'illumination est finalement arrivé aujourd'hui. Sur un coup de tête, j'ai décidé de voir ce qui se passerait si j'exécutais 2 exécutions séquentielles de karma avec le même ID de build pour saucelabs. À ma grande joie, SauceLabs a obéissant regroupé tous les tests ensemble. J'ai donc refactorisé tous mes fichiers de configuration karma, me suis débarrassé de la solution basée sur les variables d'environnement, et j'ai abouti à cette solution parfaite et fonctionnelle :

Dans mon package.json, tout ce dont j'ai besoin pour exécuter tous les tests est :

```
"test": "karma start karma.noie.conf.js && karma start karma.ie.conf.js",
```

J'espère que cela résoudra le dilemme de quelqu'un d'autre. Karma + SauceLabs est une manière fantastique de tester à la fois le code de haut niveau et les hypothèses de très bas niveau sur le fonctionnement des navigateurs pour s'assurer que votre suivi des problèmes ne se remplira pas de bugs ennuyeux du type j'aurais-dû-tester-ça.

Bon test !
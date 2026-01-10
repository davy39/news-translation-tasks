---
title: Une introduction au logging pour les programmeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-27T09:30:50.000Z'
originalURL: https://freecodecamp.org/news/you-should-have-better-logging-now-fbab2f667fac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0syxG6pVAgyWwItiegWS8g.jpeg
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Une introduction au logging pour les programmeurs
seo_desc: 'By Stefanos Vardalos

  There is a part of software development that not all developers take very seriously.
  That part is proper logging and everyone who has lost countless hours during debugging
  knows exactly what I mean.

  Useful logs can provide the de...'
---

Par Stefanos Vardalos

Il y a une partie du développement logiciel que tous les développeurs ne prennent pas très au sérieux. Cette partie est le logging approprié et tout le monde qui a perdu d'innombrables heures pendant le débogage sait exactement ce que je veux dire.

Les logs utiles peuvent fournir au développeur (surtout lorsque quelqu'un doit déboguer/maintenir le code de quelqu'un d'autre) une aide considérable lorsqu'il essaie de comprendre ce que le code fait réellement. Certains développeurs disent que la trace de la pile est tout ce dont quelqu'un devrait avoir besoin, mais cela ne pourrait pas être plus éloigné de la vérité. Les traces de pile sont excellentes et peuvent vous dire où et ce qui a mal tourné, mais elles ne peuvent pas vous dire comment vous y êtes arrivé en premier lieu. Bien sûr, vous pouvez suivre l'exécution à travers les points d'arrêt, mais y aller à l'aveugle rendra tout le processus beaucoup plus chronophage qu'il ne devrait l'être.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fyh4F1gDByMdWYn4u8Gjlw.png)
_Pas très utile_

C'est la partie _diagnostic_ du logging, la plus importante et essentiellement celle que les développeurs pourraient comprendre plus facilement, car elle fait plus partie de leur routine de travail quotidienne. Il y a une autre partie appelée _audit_ logging. Alors que le logging de diagnostic s'occupe d'enregistrer les événements qui se produisent pendant l'exécution (appels de méthodes, entrées/sorties, appels HTTP, exécutions SQL), le logging d'audit est responsable de l'enregistrement d'événements plus abstraits, liés à la logique métier. De tels événements peuvent être des actions utilisateur (ajout/modification/suppression de contenu, transactions, accès aux données) ou d'autres choses qui ont soit une valeur managériale, soit, plus important encore, une valeur légale.

Dans le monde du back-end, il y a eu quelques excellents frameworks de logging parmi lesquels choisir, car le besoin pour ceux-ci est apparu beaucoup plus tôt. Par exemple, en Java, vous pouvez choisir entre le propre moteur de logging de Java, java.util.logging, ou quelques excellents frameworks externes comme Logback ou le plus populaire Log4j. 
Dans le monde du front-end, les choses n'ont pas encore évolué aussi loin, mais il existe des options qui peuvent vous aider à faire ce petit effort supplémentaire (et bien sûr à vous débarrasser des messages triviaux console.log). Deux bibliothèques JavaScript pour le front-end sont le minimal mais puissant loglevel et le browser-bunyan, un port du module de logging node.js pour le navigateur. Certaines fonctionnalités sont communes entre ces frameworks, mais il existe des fonctionnalités uniques qui devraient guider le développeur à choisir celui dont il a besoin. L'utilisation de ceux-ci peut être montrée avec quelques exemples.

> Manifeste : Les logs du serveur doivent être structurés. Le format JSON est bon. Faisons cela.

Comme le manifeste original de [Bunyan](https://github.com/trentm/node-bunyan), les logs doivent être structurés et facilement indexés, filtrés, recherchés. Ce framework génial produit des logs au format JSON qui peuvent ensuite être facilement consommés par d'autres services pour un traitement ultérieur.

Outre la capacité d'exportation JSON, [Bunyan](https://github.com/philmander/browser-bunyan) a le concept de loggers enfants, qui peuvent être utilisés pour créer différents loggers pour différents composants de l'application. Cela donne une grande flexibilité quant aux champs et informations supplémentaires que vous souhaitez inclure dans des parties spécifiques de votre application uniquement. Bunyan intègre également des streams, qui sont les paramètres de 'sortie' de ses loggers. Vous pouvez créer plusieurs streams et en assigner un ou plusieurs à chaque logger, et chaque stream peut avoir des paramètres différents comme le niveau minimum de logs à enregistrer (les niveaux acceptables de Bunyan sont fatal/error/warn/info/debug/trace) ou la méthode de sortie (dans le navigateur, il n'y a que des options liées à la console, mais dans un environnement Node, vous pouvez faire d'autres choses comme écrire des logs dans un fichier spécifique).

> Il s'agit d'une bibliothèque de logging fiable et minimaliste pour un usage quotidien. Elle ne fait pas de choses fantaisistes, elle ne vous permet pas de reconfigurer les appenders ou d'ajouter des règles de filtrage de logs complexes ou de faire bouillir du thé (dommage), mais elle dispose de toutes les fonctionnalités de base dont vous avez réellement besoin.

Avec une déclaration assez modeste, [loglevel](http://pimterry.github.io/loglevel/) se présente comme un framework de logging minimal qui ajoute juste le strict minimum dont la plupart des applications ont besoin. Il ajoute un logging basé sur des niveaux appropriés (trace/debug/info/warn/error) et un filtrage quant au niveau minimum à afficher sur la console.

La puissance de ce framework réside dans sa simplicité, car il est extrêmement facile de l'incorporer dans votre projet et de commencer à l'utiliser, en remplaçant le console.log() pour toujours. De plus, loglevel a une autre perle cachée, son extensibilité, car il existe divers plugins écrits pour lui, qui fournissent des fonctionnalités supplémentaires pour ceux qui les souhaitent, comme [l'ajout de préfixes aux messages](https://github.com/kutuluk/loglevel-plugin-prefix).

Quel que soit le framework que vous choisissez finalement pour votre application JavaScript, vous économiserez certainement beaucoup d'heures de travail pendant le débogage et rendrez votre application plus pérenne.
---
title: Quelle est la meilleure façon de prototyper des circuits ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-04T00:07:25.000Z'
originalURL: https://freecodecamp.org/news/whats-the-best-way-to-prototype-circuits
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Copy-of-Dashboard-2.png
tags:
- name: Electronics
  slug: electronics
seo_title: Quelle est la meilleure façon de prototyper des circuits ?
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  There’s something that always goes wrong with a first revision circuit board design.
  No matter how long you spend imagining how a circuit will work, it will bork in
  the most unexpected wa...'
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com](https://www.jaredwolff.com/circuit-boards-versus-breadboarding/)**

Il y a toujours quelque chose qui ne va pas avec une première révision de la conception d'un circuit imprimé. Peu importe le temps que vous passez à imaginer comment un circuit va fonctionner, il va planter de la manière la plus inattendue.

Dans le cas de mon [dernier projet](https://www.jaredwolff.com/dimming-ac-lights-with-a-microcontroller/), j'ai négligé un élément critique du circuit. Ma révélation ? Il s'avère que vous ne pouvez pas dériver de manière fiable 375 mW de puissance dans une résistance de 100 mW. ? Malheureusement, comme vous l'avez deviné, cela nécessiterait une retouche.

Alors, dans ma quête pour trouver la bonne solution de prototypage, je me suis dit : « Pourquoi ne pas partager les choses qui me passent par la tête en ce moment »

Et ainsi, cet article de blog est né. ?

## La plaque d'essai (sans soudure)
Lorsque vous êtes limité par le temps, la plaque d'essai sans soudure est une solution de choix. Ce type de prototypage électronique est indolore, mais il présente quelques inconvénients. Le plus notable est qu'il ne se marie pas bien avec l'optimisation analogique. J'en parlerai un peu plus tard dans cet article.

J'ai récemment assemblé un capteur de qualité de l'air intérieur PM2.5 et l'ai interfacé avec un Particle Argon. Je l'ai assemblé en utilisant du [fil enroulé](https://www.jaredwolff.com/prototype-with-wire-wrap/). mais ce fut un désastre complet. En comparaison, la plaque d'essai sans soudure a gardé les choses organisées et esthétiques.

![Plaque d'essai sans soudure et Particle](https://www.jaredwolff.com/circuit-boards-versus-breadboarding/images//DSC01299.jpeg)

Les ingénieurs en électricité apprennent à aimer (ou à détester) les plaques d'essai tôt dans leurs études. Pour certains, cela peut être un exutoire pour être créatif et faire de belles dispositions. De nombreux étudiants de première année en génie informatique sont fiers de leurs conceptions de plaques d'essai. Tellement que leurs plaques d'essai semblent assemblées par un robot.

Ces jours-ci, cependant, je ne câble plus ensemble de grands circuits logiques numériques comme à l'université. J'utilise néanmoins des plaques d'essai sans soudure pour faire des connexions solides avec des modules de développement. Comme vous pouvez le voir sur la photo ci-dessus, j'ai utilisé 3 plaques séparées qui sont toutes disponibles sur le web. Les connecter ensemble a pris environ 10 minutes au maximum. Il m'a fallu environ 15 minutes pour assembler la version avec fil enroulé.

## La plaque d'essai ?
Parfois, une plaque d'essai sans soudure est géniale, mais elle n'est pas faite pour toutes les situations. Et si vous avez besoin de quelque chose de fiable ? Et si vous travaillez avec des tensions élevées ? Si vous cherchez plus mais ne voulez pas sauter à la création de votre propre PCB, c'est votre prochaine étape.

Créer une plaque d'essai soudable n'est pas si différent d'une version sans soudure. Il m'a fallu environ 20 minutes pour assembler le circuit sur la photo ci-dessous.

![Circuit de passage par zéro sur plaque d'essai](https://www.jaredwolff.com/circuit-boards-versus-breadboarding/images//DSC01301.jpeg)

La plaque d'essai ci-dessus est le circuit de remplacement de passage par zéro mentionné précédemment. Étant donné que je travaillais avec une tension secteur, j'ai été très prudent lors de l'assemblage.

Alors, après avoir vérifié mon travail trois fois, je l'ai branché et vous savez quoi ?

*Ça a marché comme un charme.*

Les plaques d'essai prennent un peu de temps à planifier, mais quand vous les faites bien, elles sont aussi bonnes qu'une carte de circuit normale.

De plus, vous n'avez pas toujours à souder chaque connexion ensemble. J'ai créé cette carte de conversion de niveau JTAG il y a environ un an. Ainsi, je pouvais faire fonctionner mes cartes de circuit dans des plages de 1,8 V à 5 V et les faire fonctionner avec le programmeur standard 3,3 V.

![Plaque d'essai et fil enroulé](https://www.jaredwolff.com/circuit-boards-versus-breadboarding/images//DSC01287.jpeg)

Dans ce cas, j'ai utilisé de la soudure et des connexions de [fil enroulé](https://www.jaredwolff.com/prototype-with-wire-wrap/). Pour les futurs projets, je prévois d'utiliser la carte de conversion de niveau JTAG que j'ai conçue il n'y a pas si longtemps. Elle fait 1/5 de la taille et est aussi fonctionnelle que celle ci-dessus.

## Aller au-delà de la plaque d'essai
Je n'ai définitivement pas peur de [assembler mes propres cartes de circuit](https://www.jaredwolff.com/how-to-self-assemble-circuit-boards/). Il y a un moment et un lieu pour cela. Il y a encore quelques choses que vous pouvez faire avant d'avoir à ouvrir votre programme de capture schématique.

*Envisagez toujours l'utilisation de circuits et de plateformes de développement qui existent déjà !*

Être intelligent dans votre processus de conception rapporte des dividendes à votre futur vous. Cela vous aide à vous concentrer sur les problèmes épineux plutôt que sur les distractions triviales. Si vous avez besoin d'une carte de circuit préconçue, Sparkfun et Adafruit sont d'excellentes ressources. Ils ont déjà créé les cartes de connexion pour les circuits intégrés qui intéressent la plupart des makers.

Pour mettre la cerise sur le gâteau, dans la plupart des cas, ces cartes de circuit sont **très bon marché.**

Des entreprises comme TI fabriquent également des cartes de développement. Les cartes sont raisonnablement prix et généralement en stock sur Digikey et leur boutique en ligne. Certaines de mes cartes de développement de fabricants préférées incluent le NRF52DK et le LT3092EDD. Je les utilise souvent et pour de très bonnes raisons.

![Carte de développement LT3092EDD](https://www.jaredwolff.com/circuit-boards-versus-breadboarding/images//DSC01288.jpeg)

Le LT3092EDD est mon choix pour réguler le courant à partir d'une source de tension variable. Peu importe la tension d'entrée, il dérivera le courant de 0 à 200 mA. Vous pouvez placer plusieurs LT3092 en parallèle pour augmenter la capacité de courant. Je l'utilise pour des tests de décharge statique et de validation qui nécessitent des puits de courant constants.

Quant au NRF52DK, non seulement je peux développer sur cette carte, mais je peux aussi l'utiliser comme programmeur. Avec de nombreuses façons de l'étendre, elle ne quitte pas souvent mon bureau.

![NRF52DK](https://www.jaredwolff.com/circuit-boards-versus-breadboarding/images//DSC01297.jpeg)

*Mais que faire s'il n'y a pas de carte de développement ?*

Parfois, aucun type de plaque d'essai n'est idéal. Cela est particulièrement vrai si votre prototypage dépend de la forme et de la disposition du cuivre sur votre carte. Je m'attendrais à ce que si vous faisiez une plaque d'essai pour une alimentation à découpage, vous pourriez obtenir des opérations très involontaires.

La disposition d'un circuit d'alimentation tend à être un peu plus complexe que, disons, un signal numérique. Oui, cela fonctionnera avec une petite piste reliant deux parties, mais cela fonctionnera bien ? Peu probable.

Ci-dessous se trouve une conception qui permet le transfert de courant vers la couche de puissance intérieure. Comme vous pouvez l'imaginer, une piste fine et une via pourraient fonctionner. En réalité, elles agiraient plus comme une résistance dans des situations de courant élevé.

![Disposition de puissance Eagle](https://www.jaredwolff.com/circuit-boards-versus-breadboarding/images//powercircuit.png)

Bien que vous puissiez obtenir de meilleures connexions, vous courez le risque de coûts plus élevés. De plus, il est beaucoup plus difficile de modifier votre circuit plus tard. Les choses se compliquent lorsque les composants deviennent plus petits et que les signaux sont poussés à l'intérieur. Ce n'est pas impossible cependant...

Lorsque des changements sont nécessaires, mes outils les plus utilisés sont le fil enroulé ou le fil de bobine et mon fidèle couteau X-acto. Vous pouvez utiliser le premier pour faire les connexions et le second pour rompre les connexions. Cela nécessite une main ferme et de la patience, mais c'est possible.

![Retouche de PCB](https://www.jaredwolff.com/circuit-boards-versus-breadboarding/images//DSC01295.jpeg)

Sur la photo ci-dessus, j'ai coupé les pistes thermiques autour des pads et les ai reconnectées à un autre ensemble de pistes. Vous devrez peut-être me croire sur parole concernant celle-ci, car il est difficile de le voir sur la photo ! J'ai fait tout le travail sous un microscope pour éviter les erreurs.

## Vous pouvez le faire ?
Il existe plusieurs façons d'assembler un circuit. Tout dépend de vous pour savoir comment vous voulez le faire. J'ai vu quelques [œuvres d'art de circuits](https://hackaday.com/2018/11/19/flywire-circuits-at-the-next-level/) très cool qui accomplissent la même chose qu'une plaque d'essai.

Si vous ne l'avez pas encore remarqué, j'ai fini par opter pour une conception de plaque d'essai. C'était plus rapide à assembler et à tester par rapport à la commande d'une toute nouvelle carte de circuit. Je vais probablement créer une autre carte à l'avenir. En attendant, cette petite plaque d'essai devrait faire l'affaire.

J'utilise toutes ces techniques lorsque je travaille avec mes clients. Aucune technique n'est exclue et cela bénéficie généralement à tout le monde. En réalité, une plaque d'essai évolue toujours vers une carte de circuit d'une sorte. Il est bon de savoir cependant que le circuit **fonctionnera** avant de le transformer en un prototype coûteux.

Alors, jusqu'à la prochaine fois, lorsque vous vous retrouvez avec le même dilemme, souvenez-vous de vos options.

Amusez-vous bien !

[Jared](https://www.jaredwolff.com/about/)
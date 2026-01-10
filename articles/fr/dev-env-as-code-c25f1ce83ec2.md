---
title: 'Comment rationaliser l''intégration des développeurs : l''environnement de
  développement en tant que code'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T22:44:13.000Z'
originalURL: https://freecodecamp.org/news/dev-env-as-code-c25f1ce83ec2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca7c0740569d1a4ca7950.jpg
tags:
- name: development
  slug: development
- name: Devops
  slug: devops
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: 'Comment rationaliser l''intégration des développeurs : l''environnement
  de développement en tant que code'
seo_desc: 'By Sven Efftinge

  Imagine that only a decade ago system administrators deployed, configured, and maintained
  software systems manually. Doing so burned an endless amount of their precious lifetimes
  and energy.


  _Source: [http://dilbert.com/strip/2017-0...'
---

Par Sven Efftinge

Imaginez qu'il y a seulement une décennie, les administrateurs système déployaient, configuraient et maintenaient les systèmes logiciels manuellement. Cela consumait une quantité infinie de leur temps précieux et de leur énergie.

![Image](https://cdn-media-1.freecodecamp.org/images/s5Awmbn4EjgMdny3zJxQpKmADY2qDy0beEpN)
_Source : [http://dilbert.com/strip/2017-01-02](http://dilbert.com/strip/2017-01-02" rel="noopener" target="_blank" title=")_

Aujourd'hui, à l'ère des architectures microservices, les systèmes sont devenus encore plus compliqués. Essayer de maintenir les opérations et les déploiements manuellement n'est plus une option. De nos jours, nous faisons du "DevOps" ou de "l'Infrastructure as code". Nous avons appris que décrire un système logiciel de manière déclarative et formelle est obligatoire pour déployer des applications automatiquement et en continu.

### **Qu'en est-il de nos environnements de développement ?**

Alors que nous avons automatisé les déploiements de nos applications, la plupart d'entre nous n'appliquent pas encore les mêmes techniques aux environnements de développement. Pourtant, l'intégration d'un nouveau membre de l'équipe sur un projet non trivial est généralement un exercice de plusieurs heures (sinon de plusieurs jours).

Cela se passe souvent comme suit :

1. **Un nouveau développeur est dirigé vers le readme**
2. **Lit une longue procédure de configuration, souvent obsolète**
3. **Installe les exigences sur la machine de développement, met à jour/downgrade les versions, etc.**
4. **Essaie d'exécuter la build… attend 20 minutes**
5. **La build échoue. Essaie de comprendre ce qui s'est mal passé.**
6. **Demande à un collègue. « Oh, oui. Tu dois aussi faire X & Y »**
7. **retour à l'étape 3**

Après de nombreuses itérations, à un moment donné, la build fonctionne somehow. Tu ne sais pas pourquoi, mais cela n'a plus d'importance maintenant. Bien sûr, tu ne mets pas à jour le document, car tu n'es pas sûr et tu ne sais pas comment tu as fini par avoir une configuration fonctionnelle. Cet état actuel est-il même reproductible ? Donc, si tu mets à jour le readme, tu ferais mieux d'ajouter seulement ce que tu as compris. Tu n'oses pas supprimer les parties que tu n'as pas comprises ou que tu as sautées parce qu'elles ne fonctionnaient pas pour toi.

Dommage que la configuration n'ait fonctionné qu'au premier abord. Au cours des semaines suivantes, tu devras résoudre des problèmes mineurs ici et là et ajouter quelques outils qui n'étaient pas listés. Peut-être que le débogage ne fonctionne pas encore, ou tu ne vois pas les sources des dépendances en amont. Finalement, cela s'arrange. Seulement, lorsqu'un collègue change quelque chose dans les exigences, cela prend généralement deux jours avant que toute l'équipe ne l'ait remarqué et ne modifie ses environnements en conséquence.

Malheureusement, la souffrance ne s'arrête pas là.

### **Ça marche sur ma machine**

Tu connais probablement la phrase célèbre « Ça marche sur ma machine » ? La situation où un bug n'apparaît que sur une machine et est difficile à reproduire sur d'autres ? **Ce sentiment quand une mauvaise chose se produit en production, mais que tu ne peux pas la reproduire localement ?** Pas très surprenant, cependant, tant que tu exécutes le code sur une plateforme différente basée sur une configuration différente.

![Image](https://cdn-media-1.freecodecamp.org/images/biCte39sWOOrTeytqtpm7LafwRlbUyiHmOjd)

### **Revenir pour corriger quelque chose sur une ancienne branche**

Un autre point de frustration est lorsque tu dois corriger quelque chose sur une branche de maintenance. Corriger le bug réel aurait pu être si facile, car tu sais comment le faire. Cependant, avant de pouvoir dire que c'est fait, tu dois être en mesure de construire et de tester cette vieille bête. Cela te coûte une quantité infinie de temps.

Bricoler avec une pile technologique vieille de six mois peut être si ennuyeux. Tu dois gérer toutes ces anciennes bibliothèques et leurs versions. Cependant, tu dois toujours faire en sorte que cela fonctionne somehow.

![Image](https://cdn-media-1.freecodecamp.org/images/Xd695rcT3oHBySFL0TOnxNoV-q0atwrgs8bm)
_Photo par [Unsplash](https://unsplash.com/@jeshoots?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">JESHOOTS.COM</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Toute cette souffrance peut prendre fin si nous appliquons l'idée de « l'infrastructure en tant que code » à nos environnements de développement également. Pourquoi ne pas rendre les configurations des environnements de développement automatisées, reproductibles de manière fiable et versionnées en les écrivant dans un format exécutable et en les vérifiant dans le dépôt de code source du projet ?

### **Environnement de développement en tant que code**

Après tout, les environnements de développement sont souvent encore plus compliqués que l'application runtime pour laquelle ils sont utilisés. Tu dois généralement ajouter tous les outils de développement tels que les outils de build, les compilateurs, les linters et un éditeur/IDE décent en plus des exigences runtime.

Si tu veux t'assurer que les changements ne cassent rien en aval, tout le monde doit coder, exécuter et tester sur le même environnement que celui sur lequel les builds CI s'exécutent.

Alors, s'il te plaît, arrêtons de polluer nos fichiers readme et commençons à écrire les instructions de configuration de manière formelle, afin qu'elles puissent être exécutées.

#### Dockerfiles

Les fichiers Docker sont un moyen assez pratique pour décrire un environnement de développement. Imagine que tu veux ajouter quelque chose comme 'asciidoctor' à la chaîne d'outils de ton projet. Tu pourrais simplement ajouter la ligne suivante au Dockerfile de ton environnement de développement :

```
RUN apt-get install -y asciidoctor
```

Une fois que tu pousses le changement vers le dépôt et que l'image Docker est mise à jour (automatiquement), tous les membres de l'équipe ont le nouvel outil dans leur environnement de développement. Nous devons pouvoir coder en un seul clic.

![Image](https://cdn-media-1.freecodecamp.org/images/apInFGXBF9qvVRWyT6duh5T86F0fTOCGNriZ)
_Photo par [Unsplash](https://unsplash.com/@clemhlrdt?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Clément H</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### **Configuration automatisée de l'IDE**

> Avertissement : Je suis affilié à certains des outils mentionnés ci-dessous.

L'approche Docker devient un peu maladroite si tes outils de développement ont une interface utilisateur telle qu'un IDE de bureau. Tu peux les empaqueter dans Docker, mais tu dois exposer l'interface utilisateur de l'IDE via X11. Une autre alternative est d'utiliser un éditeur de terminal comme vim, mais bien sûr, ce n'est pas une option pour la plupart d'entre nous.

Certains IDE de bureau disposent d'outils permettant d'automatiser les configurations. Eclipse, par exemple, dispose d'un outil appelé Oomph. Oomph te permet de décrire de manière déclarative un IDE Eclipse, y compris les plug-ins, la configuration et même la configuration de l'espace de travail (c'est-à-dire les informations git).

De loin, la meilleure option est un IDE qui s'exécute dans les navigateurs, comme le nouvel IDE [Theia](https://theia-ide.org). Theia est open-source sous la Fondation Eclipse. Il peut être vu comme VS Code qui s'exécute sur les navigateurs et les bureaux et est un peu plus personnalisable.

Pour un environnement de développement simple basé sur Docker, tu pourrais ajouter Theia à ton image Docker. Il offre un IDE complet, y compris des terminaux pour ton image de workspace.

L'étape suivante serait de traiter ton environnement de développement comme une fonction serverless que tu ne fais apparaître que lorsque nécessaire et que tu oublies une fois terminé. Le service en ligne [Gitpod](https://www.gitpod.io) fait exactement cela.

Il s'intègre aux plateformes d'hébergement de code telles que GitHub. Il élimine toutes les transitions fastidieuses en les automatisant. Tu vois du code sur un site web et tu veux l'essayer dans un vrai environnement de développement ? Gitpod fait tout ce qu'il peut pour t'y amener en un seul clic. Il te permet de fournir des fichiers Docker ou des images Docker personnalisés et exécute l'IDE Theia.

### **Résumé**

Appliquer les leçons apprises du DevOps à notre configuration de développement peut nous faire économiser tant de temps et d'énergie précieux. [L'enquête auprès des développeurs d'ActiveState en 2018](https://www.activestate.com/developer-survey-2018-open-source-runtime-pains/) souligne cela avec quelques chiffres :

![Image](https://cdn-media-1.freecodecamp.org/images/NnmJcPSnA8h0d2E7anFaSQCIU-Xj88rTEkQF)

Avons-nous vraiment besoin d'accueillir de nouveaux collègues ou contributeurs avec une expérience d'intégration douloureuse ? Sautons la prose dans le _readme_ et écrivons du code pour avoir notre configuration d'environnement de développement **automatisée, reproductible et versionnée.**
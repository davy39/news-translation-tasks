---
title: Comment maintenir un projet open source – Bonnes pratiques et conseils
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-10T14:52:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-maintain-an-open-source-project
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/tezos-BlKBaiFdNgA-unsplash--1-.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: community
  slug: community
- name: open source
  slug: open-source
seo_title: Comment maintenir un projet open source – Bonnes pratiques et conseils
seo_desc: 'By Prajwal Kulkarni

  So, now that you''ve published your first open-source project, what next? If you''re
  new to open source, you might think this is it. But the fun has just begun.

  In fact, most of the work lies in maintaining your project and making i...'
---

Par Prajwal Kulkarni

Alors, maintenant que vous avez publié votre premier projet open source, quoi de neuf ? Si vous êtes nouveau dans l'open source, vous pourriez penser que c'est tout. Mais le plaisir ne fait que commencer.

En fait, la plupart du travail consiste à maintenir votre projet et à le rendre accessible à plus d'utilisateurs. C'est l'une des étapes les plus importantes du processus et c'est ce qui permet à un projet open source d'avoir un succès durable.

Maintenir un [OSS](https://en.wikipedia.org/wiki/Open-source_software) signifie essentiellement garder le projet à jour afin qu'il soit compatible avec la dernière version des diverses bibliothèques tierces, frameworks et logiciels qu'il utilise.

Il est également important de mettre en place de bonnes mesures de sécurité. Les bugs sont une partie inévitable de tout cycle de vie de développement logiciel, donc corriger les bugs qui posent une menace pour la sécurité est tout aussi important.

Il y a quelques jours, j'ai publié mon premier projet open source, un package npm [nextportal](https://www.npmjs.com/package/nextportal). Donc, maintenant, il est important que je suive certaines bonnes pratiques pour le rendre attrayant.

Ici, je vais vous guider à travers certaines des étapes pour vous aider à maintenir un projet open source au fur et à mesure que je les apprends.

Tout au long de cet article, j'utiliserai [GitHub](https://github.com) (en supposant que la plupart des projets y sont hébergés et maintenus).

Mais si vous utilisez un autre site d'hébergement VCS, vous pouvez toujours suivre ces étapes pour assurer le succès de votre projet.

## Rédiger une bonne documentation

La documentation informe les gens sur ce que fait le logiciel ou le code, comment l'installer, comment ils peuvent l'utiliser, et elle fournit un exemple de travail et des guides de contribution.

Notez que même si le code est un projet open source, il doit toujours avoir une licence pour permettre aux autres personnes de l'utiliser, de le modifier ou d'y apporter des ajouts dans le cadre défini. Donc, la documentation est essentiellement un livre de règles ou un guide pour aider les gens à utiliser votre logiciel.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/fcc1.png)

																[Source](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/contribute/documenting-code.html)

Une documentation incomplète rendra difficile pour les gens de saisir l'essence et le but de votre code, les rendant hésitants à l'essayer, peu importe la qualité de votre projet.

Alors, assurez-vous simplement d'avoir une documentation bien rédigée, ainsi que tous les détails sur toutes les dernières modifications que vous avez apportées au projet.

## Automatiser les tâches répétitives

Maintenir un projet open source impliquera généralement de nombreuses tâches répétitives, comme la maintenance planifiée, la mise à jour périodique des dépendances, l'intégration continue, et ainsi de suite.

Étant donné que ces tâches prennent du temps, sont répétitives et ne nécessitent aucune innovation, vous pouvez en automatiser beaucoup.

Prenons la mise à jour des dépendances, par exemple. Il est courant d'utiliser d'autres packages et dépendances dans vos projets. Mais en même temps, vous ne pouvez pas vous permettre de compromettre la sécurité/performance de votre projet en utilisant une dépendance qui est obsolète.

Un outil que je trouve utile pour cela est le gratuit [WhiteSource Renovate](https://www.whitesourcesoftware.com/free-developer-tools/renovate/). Il automatise les mises à jour des dépendances. Donc, utiliser un outil comme Renovate pour garder les dépendances à jour est une tâche cruciale que vous ne devriez pas négliger. Si vous souhaitez apprendre comment intégrer WhiteSource Renovate dans votre projet, continuez à lire la section ci-dessous.

### Mise à jour automatique des dépendances avec Renovate

Tout d'abord, vous devrez [intégrer Renovate](https://github.com/apps/renovate) avec votre compte GitHub. Ensuite, cliquez sur installer et suivez les étapes comme indiqué.

Lors de la configuration, Renovate vous permet de décider s'il doit s'exécuter sur tous les dépôts par défaut ou uniquement sur des dépôts spécifiques. Sélectionnez l'option que vous souhaitez. (Note : Si vous souhaitez que Renovate s'exécute sur des dépôts forkés, cliquer sur Sélectionner tous les dépôts ignorera les dépôts forkés par défaut. Dans de tels cas, vous devrez ajouter manuellement le(s) dépôt(s) forké(s)).

Peu de temps après avoir configuré Renovate avec les dépôts requis, une PR d'intégration sera soumise par le bot Renovate, qui contient des informations telles que le résumé de la configuration et les packages/dépendances qui doivent être mis à jour.

À des fins de démonstration, j'ai forké un dépôt de mon compte GitHub qui est supposément une application mobile construite sur [React Native](https://reactnative.dev/). Elle n'est plus maintenue, donc elle servira de bon exemple pour les tests.

Si vous suivez les étapes ci-dessus correctement, vous devriez voir une PR d'intégration similaire à celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/fcc2-1.png)
_PR initiale_

![Image](https://www.freecodecamp.org/news/content/images/2022/01/fcc3-1.png)
_Fusionner la PR_

  
Une fois que vous avez fusionné la demande de tirage ci-dessus, le bot Renovate commencera à rechercher les dépendances obsolètes ou périmées qui doivent être mises à jour et soumettra une PR pour chaque dépendance qui doit être mise à jour.

Gardez à l'esprit que cet outil ne trace pas les vulnérabilités ou les problèmes, seulement les mises à jour disponibles. Mais les nouvelles dépendances viennent souvent avec des corrections de bugs, des améliorations de sécurité et des fonctionnalités nouvellement ajoutées.

Pourtant, simplement parce qu'une mise à jour est disponible ne signifie pas que vous devez la mettre à jour car il y a des chances qu'elle puisse casser votre système existant en raison d'une incompatibilité ou quelque chose de similaire. Il est donc important de revoir la mise à jour avant de fusionner la PR.

Pour vous aider à prendre des décisions éclairées concernant la mise à jour d'un package ou non, la PR inclut des détails sur le taux d'adoption et le taux de réussite des tests, qui déterminent efficacement le niveau de confiance global.

Il récupère également les dernières notes de version du dépôt de dépendances, ce qui nécessiterait autrement de naviguer manuellement vers le dépôt pour trouver ce qui est nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/fcc4-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/01/fcc5-1.png)

## Toujours traiter les problèmes

Une bonne façon de s'assurer que votre projet s'améliore continuellement est de traiter les problèmes ouverts par vos pairs.

Personne ne montrera d'intérêt à contribuer à un projet open source s'il ne traite pas les bugs potentiels, les problèmes de sécurité ou l'ajout de fonctionnalités.

Vous pouvez configurer un script CI qui attribue une étiquette lorsqu'un problème est ouvert et l'assigner ensuite aux contributeurs qui maintiennent le projet en conséquence. Cela entraînera une révision rapide des problèmes et aidera également les contributeurs à trouver de nouvelles corrections et/ou ajouts de fonctionnalités.

## Faire connaître votre projet

Vous avez publié un excellent projet open source, mais vous ne voyez personne l'utiliser ou y contribuer. La raison principale pourrait être que les gens n'ont pas encore découvert votre projet.

Pour lancer la balle, vous devez vous assurer que votre projet obtient toute l'exposition possible. Une façon efficace de le faire est de partager votre travail sur les réseaux sociaux, partout où les gens sont actifs et pourraient être intéressés.

Vous pouvez également participer à des discussions sur des sujets liés à vos projets sur des plateformes de Q&A, comme Stack Overflow et Reddit. Ensuite, partager votre projet sera une chose naturelle à faire.

## Attirer des contributeurs utiles

Suivre les étapes ci-dessus vous aidera à démarrer. Mais une fois que votre projet commence à croître, il aura besoin de plus de contributeurs prêts à maintenir le projet.

Cela n'est possible que lorsque vous construisez une base solide de contributeurs. Pour augmenter le nombre de personnes vous aidant à maintenir le projet, vous pouvez mettre en place des récompenses pour les contributions, comme distribuer des goodies aux personnes qui satisfont certaines exigences.

Les gens seront également encouragés à contribuer s'ils ressentent un sentiment de fierté et de propriété du projet. Assurez-vous donc que tout le monde reçoit le crédit dû pour ses contributions, grandes ou petites.

Des actions positives comme celle-ci peuvent également permettre aux nouveaux contributeurs de partager leur travail avec leurs amis/collègues, aidant indirectement votre projet à gagner plus d'exposition/utilisateurs/contributeurs.

## Conclusion

À la fin de la journée, la valeur que votre projet apporte est ce qui détermine combien de personnes y contribuent et l'utilisent. Donc, lorsque vous créez un projet open source, gardez l'utilisabilité et l'impact à l'esprit. Comment votre projet facilitera-t-il la vie des autres ? Quels problèmes résout-il ?

Ce sont les étapes que vous devez suivre pour maintenir avec succès un projet open source. Recommandez-vous d'autres pratiques importantes qui peuvent ajouter de la valeur à cette liste ? Si oui, partagez-les avec moi afin que nous puissions tous en apprendre davantage sur la culture open source.

Si vous avez trouvé cet article utile, n'hésitez pas à le partager avec vos amis et collègues, vous pouvez me suivre sur [Twitter](https://twitter.com/mehulmpt) pour plus de contenu :)

Santé !
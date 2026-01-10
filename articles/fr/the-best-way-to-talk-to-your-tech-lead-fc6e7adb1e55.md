---
title: Comment parler à votre tech lead et corriger vos problèmes de communication
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-30T18:06:58.000Z'
originalURL: https://freecodecamp.org/news/the-best-way-to-talk-to-your-tech-lead-fc6e7adb1e55
coverImage: https://cdn-media-1.freecodecamp.org/images/1*By6rwJTTUNUXSsm0iTEZaw.jpeg
tags:
- name: leadership
  slug: leadership
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment parler à votre tech lead et corriger vos problèmes de communication
seo_desc: 'By Greg Sabo

  Here’s where you messed up.

  Your tech lead told you to build out a new API endpoint for an upcoming feature.
  It was supposed to be simple: just return a list of the current user’s email addresses.

  You start with the usual boilerplate. Yo...'
---

Par Greg Sabo

Voici où vous avez fait une erreur.

Votre tech lead vous a demandé de créer un nouveau point de terminaison API pour une fonctionnalité à venir. Cela devait être simple : il suffisait de retourner une liste des adresses e-mail de l'utilisateur actuel.

Vous commencez avec le code standard. Vous enregistrez le nouveau point de terminaison. Vous l'associez à un contrôleur. Vous ajoutez un commentaire explicatif.

Puis vous découvrez que la requête est impossible. Les adresses e-mail de l'utilisateur se trouvent toutes sur différents shards de la base de données.

Les projecteurs s'allument. Le rideau se lève. C'est votre moment de briller en tant que superstar du logiciel ! Vous utiliserez votre travail acharné et votre créativité pour trouver une solution à ce problème unique.

Vous commencez à construire une table dénormalisée pour garder les données locales au shard de l'utilisateur, ainsi qu'une couche d'enveloppement pour garder les copies synchronisées. Votre solution est scalable et performante. Regardez-vous avancer !

Voici le problème. Vous n'avez pas parlé à votre tech lead. De leur point de vue, ils vous ont donné une tâche simple à réaliser, et cela vous prend trois fois plus de temps que prévu. Peu importe si vous créez l'architecture parfaite. Vous avez érodé la confiance dans votre relation avec votre responsable d'équipe.

Les meilleurs ingénieurs peuvent créer des systèmes élégants, mais ils savent aussi parler à leurs tech leads de la bonne manière. Voici ce que je recommande.

### 1. Pendant les réunions, concentrez-vous sur la manière dont vous abordez ce qui ne va pas

C'est l'heure de la réunion quotidienne. Que allez-vous dire à votre équipe et à votre tech lead ?

« J'ai fait quelques progrès sur cette tâche hier. J'ai rencontré quelques échecs de tests, et je les corrige maintenant. J'espère livrer cela aujourd'hui. »

C'était une mise à jour de statut. Et c'était inutile.

Les mises à jour de statut sont des communications qui n'ont pas d'autre réponse que « OK, ça a l'air bien. » Pourquoi perdre du temps à donner ces mises à jour en personne alors ?

Le but des réunions quotidiennes est d'encourager les membres de l'équipe à se débloquer mutuellement. Les trois questions traditionnelles sont :

```
1. Qu'avez-vous terminé hier ?2. Que terminerez-vous aujourd'hui ?3. Qu'est-ce qui vous bloque ?
```

Les gens se concentrent souvent sur les deux premières et omettent complètement la dernière. Pourtant, c'est la plus importante !

Les gens interprètent souvent « Qu'est-ce qui vous bloque ? » comme « Qu'est-ce qui vous empêche complètement de travailler ? » C'est pourquoi je préfère la question « Quel est votre drapeau rouge ? » à la place.

Un drapeau rouge est **n'importe quoi** qui va vous ralentir. Voici quelques exemples de drapeaux rouges :

* « Je ne suis pas sûr de savoir comment commencer le test pour cela. »
* « Je dois comprendre ce dont l'équipe mobile a besoin que je fasse ici. »
* « Je dois refactoriser ce composant pour que cela fonctionne. »

Aucun de ces éléments ne vous empêche complètement de travailler. Mais ils vont prendre une partie considérable de votre temps.

C'est ce que votre tech lead veut entendre. C'est leur meilleure opportunité de faire leur travail, de vous aider à accélérer et de trouver des solutions à vos problèmes les plus épineux.

Une note importante sur les drapeaux rouges : vous devez toujours maintenir une **responsabilité** claire pour votre projet lorsque vous mentionnez un drapeau rouge. Vous ne devez pas avoir l'habitude d'utiliser les drapeaux rouges comme excuse pour ne pas faire votre travail.

La plupart des gens veulent paraître impressionnants pendant leur réunion quotidienne. Ils veulent dire : « Regardez tout ce que j'ai accompli hier ! Regardez comme je suis génial. » Résistez à cette tentation et concentrez-vous plutôt sur la manière dont vous pouvez accélérer le travail à venir.

### 2. Entre les réunions, communiquez de manière proactive

Lorsque vous travaillez en tant que responsable d'équipe ou tech lead, vous avez cette paranoïa constante que votre équipe est complètement bloquée et vous ne le savez pas.

Vous entrez dans l'espace de travail de votre équipe, et tout le monde est à son bureau. Mais que font-ils ? Font-ils de bons progrès ? Passeront-ils leur temps à implémenter quelque chose de complètement faux ? C'est difficile à dire.

Et bien sûr, le tech lead doit absolument avoir une relation de confiance avec son équipe. Ils ne peuvent pas laisser cette paranoïa contrôler leur comportement en tout temps. Alors ils finissent par ne pas demander.

C'est votre opportunité de répondre à l'un des besoins de votre tech lead. Vous devriez communiquer de manière proactive sur ce que vous faites au moins deux fois par jour.

Que veux-je dire par communication proactive ? Je veux dire toute conversation initiée par vous. Les points de contrôle démarrés par votre tech lead et les réunions planifiées ne comptent pas comme proactifs.

Exemples de moyens pour initier une communication proactive :

* Envoyer un message Slack
* Commenter une tâche Asana qu'ils suivent
* Les intercepter à leur retour à leur bureau

La communication proactive peut parfois prendre la forme de [demander de l'aide](https://hackernoon.com/how-awesome-engineers-ask-for-help-93bcb2c7dbb7). « Je n'arrive pas à importer ce module et je ne sais pas ce qui ne va pas. Pouvez-vous m'aider ? » Ce sont des opportunités pour le tech lead de faire son travail, et si vous êtes vraiment bloqué, alors c'est du temps bien dépensé.

L'autre forme que peut prendre la communication proactive est un point de contrôle. Quelque chose comme : « Je travaille sur cette fonctionnalité, et je découvre que je devrais remonter cet état jusqu'au composant racine pour que cela fonctionne. Faites-moi savoir si vous voulez en discuter. » C'est une excellente manière de faire remonter les désaccords architecturaux potentiels. Arrêtez d'attendre la revue de code avant de parler de ces choses, sérieusement.

La communication proactive semble facile. En pratique, tout le monde hésite avant de « déranger » quelqu'un avec ce type de communication. Essayez d'ajouter une tâche quotidienne à votre liste de choses à faire pour communiquer de manière proactive, et vous verrez ce que je veux dire.

Comme pour tous les modèles de communication, il vaut la peine de prendre le temps d'avoir une discussion ouverte avec votre tech lead sur ses préférences. Détestent-ils Slack ? Combien de mises à jour de statut par jour est trop ? Votre communication de la semaine dernière a-t-elle bénéficié à l'équipe ou non ?

### 3. Pendant les discussions techniques, répétez et résumez

Il est important que vous et votre tech lead ayez au moins un certain alignement autour des décisions techniques que vous prenez. Votre opportunité de faire en sorte que cet alignement se produise est les conversations techniques.

Les conversations techniques peuvent ressembler à votre tech lead s'asseyant avec vous pour lancer un nouveau projet. Votre tech lead a quelques idées initiales sur la manière dont il pourrait être implémenté, et ils les partagent avec vous.

Souvent, votre tech lead peut avoir plus de contexte historique que vous sur le système qui change. Ils diront donc probablement au moins une chose qui vous fera dire « hein ? »

Votre tech lead le sait. Mais ils ne savent pas quelles choses qu'ils disent vont vous faire dire « hein ? » à moins que vous ne disiez réellement « hein ? »

Clarifiez toujours à la fois ce que vous **comprenez** et ce que vous **ne comprenez pas**. Plutôt que de dire « Je suis perdu », clarifiez « Je comprends X, mais je ne comprends pas Y. »

En fin de compte, vous voulez que votre tech lead quitte la conversation avec beaucoup de confiance que vous avez entendu et compris ce qu'ils avaient à dire. Beaucoup de gens essaient d'y parvenir en souriant et en hochant la tête. Cela a l'effet inverse.

Au lieu de sourire et de hocher la tête lorsque vous comprenez, **répétez et résumez** ce que vous avez entendu.

Par exemple :

> « Compris. Ce que j'entends, c'est que je devrais calculer cette valeur sur le serveur pour réduire les allers-retours, et l'envoyer au client pendant le chargement de la page. »

Cela prouve à votre tech lead que vous l'écoutiez. Et cela vous force réellement à mieux écouter.

Lorsque vous essayez cela, vous allez résister au début. Cela donne un peu l'impression que vous êtes autoritaire et interruptif. Cela donne aussi un peu l'impression que vous copiez simplement ce qu'ils disent de manière patronnante.

Ne laissez pas cela vous arrêter. Pensez à ce que le tech lead ressentira. Je peux vous dire que c'est un vrai soulagement de voir l'autre personne prendre l'initiative de répéter et de résumer.

Ces résumés sont généralement des éléments d'action. Votre prochaine étape devrait être de les écrire quelque part. Mettez-les quelque part où votre tech lead peut les voir et apporter des corrections si vous avez tort.

### Soyez un super collaborateur

Les tech leads veulent travailler avec des ingénieurs qui prennent leurs responsabilités. Cela peut être difficile à faire sur le plan technique si vous n'êtes pas familier avec les systèmes avec lesquels vous travaillez.

Mais ce que vous **pouvez** prendre en responsabilité, c'est la manière dont vous **communiquez** sur votre travail. Pensez à la manière dont vous pouvez changer vos modèles de communication avec votre tech lead, et vous découvrirez facilement de nouvelles habitudes puissantes à construire.

#### Si vous êtes passionné par l'aide aux équipes pour collaborer efficacement, vous devriez [travailler avec moi chez Asana](https://asana.com/jobs/engineering?utm_source=medium&utm_medium=blog&utm_content=talk-to-tech-lead).
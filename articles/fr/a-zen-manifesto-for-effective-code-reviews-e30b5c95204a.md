---
title: Un manifeste zen pour des revues de code efficaces
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-02T20:30:34.000Z'
originalURL: https://freecodecamp.org/news/a-zen-manifesto-for-effective-code-reviews-e30b5c95204a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Pt73-k3YNsgjnOP8
tags:
- name: code review
  slug: code-review
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: teamwork
  slug: teamwork
- name: 'tech '
  slug: tech
seo_title: Un manifeste zen pour des revues de code efficaces
seo_desc: 'By Jean-Charles Fabre

  When you are coding, interruptions really suck.

  You are in the zone, flying high, killing it. And BAM… meeting, standup, insert
  interruption… Great!

  In that context, code reviews can be perceived as another hurdle to productivit...'
---

Par Jean-Charles Fabre

Lorsque vous codez, les interruptions **vraiment** gênent.

Vous êtes dans la zone, vous volez haut, vous êtes en pleine forme. Et BAM… réunion, standup, *insérez une interruption*… Super !

Dans ce contexte, les revues de code peuvent être perçues comme un autre obstacle à la productivité.

Et franchement, je peux comprendre cela.

#### Les revues de code sont difficiles.

Non seulement vous devez arrêter ce que vous êtes en train de faire, mais vous devez également vous immerger dans le code de quelqu'un d'autre. Cela demande _beaucoup_ d'énergie juste pour changer de focus.

#### Les revues de code prennent du temps.

Selon l'enquête [Slack Overflow de 2019](https://insights.stackoverflow.com/survey/2019#development-practices), 56,4 % des développeurs passent 4 heures ou plus par semaine à effectuer des revues de code. Et cela peut représenter jusqu'à 20 % de la semaine d'un développeur !

#### Les revues de code sont frustrantes.

En tant que soumissionnaire, il peut être frustrant de voir votre pull request rejetée, d'attendre des heures, voire des jours, pour une revue. En tant que relecteur, les revues de code peuvent sembler être un obstacle à une bonne journée productive.

Oui, les revues de code peuvent parfois être difficiles, chronophages et frustrantes.

Mais elles sont aussi un bon moyen de **partager des connaissances, prévenir des bugs et renforcer la culture de votre entreprise**, entre autres.

Ce qui suit est un manifeste pour les soumissionnaires et les relecteurs afin de ramener la paix d'esprit dans les revues de code. ?

### Un manifeste pour les soumissionnaires

En tant que soumissionnaire, voici ce que vous pouvez faire pour augmenter vos chances de voir vos pull requests approuvées en temps opportun.

#### Soumettez lorsque vous avez terminé.

Cela semble évident, je sais. Mais le problème est que — la plupart du temps, si la machine ne fonctionne pas, ce n'est pas parce qu'elle est cassée… c'est parce qu'elle n'est pas branchée !

De très petits détails peuvent faire une grande différence sur la façon dont votre travail est perçu. Et vous ne voulez pas que vos collègues aient l'impression d'investir du temps et des efforts dans la relecture de code en cours de développement.

> Moi : « Il manquait juste un </div> ! »

> Vous : « Oui, je sais, mais tout le truc ne fonctionnait pas et cela m'a pris 20 minutes pour le repérer. »

Voici donc ce que vous pouvez faire :

* **Testez vous-même votre code.** Incluez WIP dans le titre ou l'étiquette si vous n'avez pas encore terminé.
* **Relisez vous-même votre code.** Utilisez le rapport de diff de votre éditeur de code ou de votre outil de versioning pour repérer les erreurs.
* **Assurez-vous que les tests de votre CI sont au vert** avant d'assigner un relecteur, cela lui fera gagner du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/5O1kil0Dxt4qNqUrwFEx6sfPRoyjWHqdD7df)
_Ne soyez pas ce gars, évidemment ? (G[iphy)](https://giphy.com/" rel="noopener" target="_blank" title=")_

#### Faites des pull requests plus petites

Je comprends, c'est une fonctionnalité importante, grande et complexe et vous pourriez être tenté de soumettre une longue pull request. Pourtant, la plupart du temps, il est préférable de soumettre des pull requests plus petites.

Les revues de code demandent de l'énergie. Les grandes revues de code en demandent encore plus. N'imposez pas à votre équipe un défi **développeur contre nourriture** chaque fois qu'ils relisent votre code.

Soyez sympa, coupez-le en petits morceaux. Vous vous rendez aussi service :

* **Vous recevrez des retours plus qualitatifs.** Plus une pull request est longue, moins vous recevrez de retours qualitatifs par ligne de code. Gardez votre pull request petite (mais pas trop petite non plus) et vous augmenterez vos chances d'obtenir de bons retours.
* **Vous les ferez approuver plus rapidement.** C'est un gagnant-gagnant, en décomposant votre travail en pull requests plus petites, vous augmentez vos chances de les faire approuver plus rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/irUe6ZKsZwrWHJwrIqGsymee1oo2cq0mMEBs)
_LGTM ?_

_Pour les passionnés, voici une [étude](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/) menée sur une équipe de programmation de Cisco. Elle montre qu'après 400 lignes de code, la capacité à trouver des défauts diminue de manière assez dramatique._ ?

Le principe suivant aide à garder la taille des pull requests sous contrôle.

#### Réduisez la portée

La portée de votre pull request doit être **simple, unique et bien définie.** Cela peut être une fonctionnalité, une user-story ou une correction de bug.

![Image](https://cdn-media-1.freecodecamp.org/images/hVle2Ce9EvgyfDMvplMuSbg3FpXTF9CN55-j)
_Rendre le monde meilleur, une ligne de code à la fois ?_

Une façon d'y penser est que les relecteurs ont un **nombre limité de "crédits d'attention"** (comme tout le monde). Chaque fois qu'ils se concentrent sur quelque chose, ils utilisent 1 crédit. Que se passe-t-il lorsqu'ils n'en ont plus ?

> LGTM ?

Faites ce que vous pouvez pour réduire le bruit autour de votre travail. Soyez attentif à la durée d'attention du relecteur.

Par exemple, **évitez les changements vides** (comme sauter des lignes). Ils n'ajoutent aucune valeur et compliquent la relecture du code.

De même, si votre pull request change le _comportement_, n'incluez pas de changements de _formatage_. Inversement, si votre pull request change le _formatage_, n'incluez pas de changements qui affectent le _comportement_. Ils pourraient être négligés par le relecteur.

#### Donnez du contexte

Pensez à votre pull request comme à une documentation pour les nouveaux arrivants. Guidez le lecteur avec du contexte.

Commencez par un **titre auto-explicatif.**

![Image](https://cdn-media-1.freecodecamp.org/images/-rZMLs8GynJOJMIB2C1ZTf1sa22RdiccZaw2)
_Bon titre tiré du dépôt xg2xg ?_

Ensuite, **écrivez une description claire** pour expliquer ce que vous faites et pourquoi vous le faites. Quel est le but de cette pull request ? Pourquoi ce changement est-il nécessaire ? Comment avez-vous abordé ce problème ?

![Image](https://cdn-media-1.freecodecamp.org/images/QfB-BL9MLi1SnpFMByRDtEoGcLsnhYqAbtUZ)
_Bon exemple expliquant pourquoi le changement est nécessaire, tiré du dépôt react_

La description est également un excellent endroit pour **souligner les problèmes non résolus et les questions ouvertes.** Les relecteurs pourraient avoir des suggestions pour vous débloquer.

Travailler sur une partie visible du produit ? Les **captures d'écran** peuvent aider à faire passer votre point plus rapidement.

* Montrez les différences avant/après.
* Utilisez des flèches colorées.
* Ajoutez des enregistrements d'écran si vous en avez envie :)

![Image](https://cdn-media-1.freecodecamp.org/images/BMOl9N0I3lUy6RFHW6koF-AHvUaS3zj8ZJzz)
_Du dépôt react_

Enfin, écrivez des **panneaux d'information** tout au long pour guider le relecteur à travers votre raisonnement.

Gardez un historique de commits propre pour faciliter le suivi de vos étapes par le relecteur. Utilisez des commentaires pour indiquer les alternatives que vous avez explorées.

![Image](https://cdn-media-1.freecodecamp.org/images/parB1wMVMrNCIoUjqixRqCHHJ08HMuE2FEb8)
_Bon exemple de commentaire de Lodash_

#### Accueillez les retours ?

Le rejet fait mal.

À vrai dire, **le rejet de code fait encore plus mal.**

![Image](https://cdn-media-1.freecodecamp.org/images/Hw2grLkrNu8rHBcUJxqHt9v71eUAPRVwiBnn)
_Je vois cela souvent !_

C'est bon. Ne le prenez pas personnellement.

Les commentaires et suggestions sont une opportunité d'apprendre et de devenir un meilleur ingénieur logiciel ?

### Un manifeste pour les relecteurs

Félicitations pour être arrivé jusqu'ici ! Maintenant, examinons quelques principes qui pourraient vous aider à devenir un meilleur relecteur ?

#### Adoptez le bon état d'esprit

Il n'existe aucun scénario où une équipe peut bénéficier d'un relecteur méchant ou condescendant. **Soyez** **gentil**. Point.

![Image](https://cdn-media-1.freecodecamp.org/images/xLy0yeaSYmd9HAUIDvcN892VA7ehvPvD4b5p)
_Qu'essaies-tu de dire, mon ami ? ([Giphy](https://giphy.com/" rel="noopener" target="_blank" title="))_

Vous voulez rendre les revues de code plus excitantes ?

Cherchez quelque chose que vous pouvez **apprendre** de cette revue. Une nouvelle bibliothèque, une nouvelle méthode, un nouveau concept, une manière plus simple de faire les choses. Quelle connaissance allez-vous en tirer ?

Si vous êtes le développeur le plus expérimenté, y a-t-il quelque chose que vous pouvez **partager** ? Comment pouvez-vous utiliser cette revue pour transférer des connaissances au soumissionnaire ? Comment pouvez-vous l'aider à devenir un meilleur ingénieur logiciel ?

![Image](https://cdn-media-1.freecodecamp.org/images/CA98J-KCq3p77rFiVmv4W5ojoQnUnBEvgNOn)
_Merci pour le conseil, mon pote ! ?_

### Comment faire une revue de code

#### **Que revoir**

Que suis-je censé chercher ? Sans directives claires sur ce qu'il faut revoir et comment, il est facile de se perdre. Voici ce que vous pouvez faire.

Tout d'abord, **vérifiez le but**. Ce code accomplit-il ce qu'il est censé faire ? Y a-t-il des parties du nouveau code qui ne sont pas claires pour vous ? Posez des questions de clarification. Le code est-il facilement testable ? Testez-le. Il n'est pas nécessaire d'aller plus loin si cette case n'est pas cochée.

D'accord, maintenant que le code fonctionne, il est temps de se concentrer sur **l'implémentation**.

Pensez à la manière dont vous auriez abordé ce problème. L'auriez-vous fait différemment ? Y a-t-il un potentiel de refactorisation ou d'abstraction ? Est-ce que cela réinvente la roue ? Est-ce que cela utilise des motifs de code standard ?

#### **Que ne pas revoir**

Parce qu'un morceau de code a de la marge pour s'améliorer, cela ne signifie pas toujours qu'il doit être amélioré.

À la fin de la journée, les revues de code sont un compromis entre **qualité** et **vitesse** et selon la portée et le stade du projet, il peut être judicieux de laisser certaines choses de côté.

De même, vous ne devriez pas faire des choses qui peuvent être automatisées. Laissez votre linter préféré chasser les points-virgules manquants et les indentations supplémentaires. Pas besoin d'un débat sans fin sur les tabulations contre les espaces.

Enfin, n'augmentez pas la portée de la pull request. Si vous pensez à de nouvelles choses qui doivent être faites, créez une nouvelle pull request/tâche à ce sujet.

#### Relisez en temps opportun

Il y a au moins 3 bonnes raisons de relire les pull requests en **heures plutôt qu'en jours.**

* Le soumissionnaire peut passer à la tâche suivante plus rapidement
* Cela réduit le coût du changement de contexte
* Cela réduit le risque de conflits de fusion entre les branches.

![Image](https://cdn-media-1.freecodecamp.org/images/XVktldbIDiDVoWG2GCGSIo4ppuEMv49qFU5m)
_Ouvert il y a 6 ans. Je reviens tout de suite ?_

**Avis de non-responsabilité :** Je viens de lancer [GitRise](https://www.gitrise.com/), un outil qui aide les équipes utilisant GitHub et Slack à relire les pull requests plus rapidement. Je pense qu'il peut aider avec cela :)

### Comment donner des retours dans une revue de code ?

Lorsqu'on donne un retour, la forme compte autant que le fond.

Saviez-vous qu'en communication écrite, **le contenu neutre semble plus négatif qu'il ne l'est en réalité** ? Méfiez-vous de ce biais et incluez des emojis lorsque nécessaire pour obtenir le bon ton dans vos commentaires.

De plus, la plupart du temps, même si vous êtes assez sûr qu'il existe une meilleure façon de faire quelque chose, il est préférable de **poser une question plutôt que de demander un changement**. De plus, les questions semblent moins agressives.

![Image](https://cdn-media-1.freecodecamp.org/images/YDgB2aLyBwOvo21kVLfvYdlKdlTioV1UUP4a)
_Exemple du dépôt ember.js_

**Enfin, récompensez lorsque les choses sont bien faites.** Les revues de code sont également un excellent endroit pour féliciter les collègues pour un bon travail. Soyez créatif et amusez-vous :)

? Félicitations pour être arrivé à la fin de cet article de blog !

? Merci beaucoup pour la lecture et faites-moi savoir si vous avez des commentaires !

? Je **viens de lancer GitRise**, un outil qui crée des rappels de pull requests pour les équipes utilisant Slack et GitHub. **Essayez-le si vous voulez. J'attends avec impatience vos retours.**
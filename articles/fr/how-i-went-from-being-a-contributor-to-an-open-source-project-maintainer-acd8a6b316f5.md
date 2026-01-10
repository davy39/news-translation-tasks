---
title: Comment je suis passé de contributeur à mainteneur d'un projet Open Source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T17:04:16.000Z'
originalURL: https://freecodecamp.org/news/how-i-went-from-being-a-contributor-to-an-open-source-project-maintainer-acd8a6b316f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DgEQHQ2yavA5ex3FmlxrUQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment je suis passé de contributeur à mainteneur d'un projet Open Source
seo_desc: 'By Dhanraj Acharya

  I was a lone software developer. When I was in college, I attended the KDE conference.
  It was my first encounter with the open source world. At the conference, I thought
  the presenters and the people raising hands were very smart. ...'
---

Par Dhanraj Acharya

J'étais un développeur logiciel solitaire. Lorsque j'étais à l'université, j'ai assisté à la conférence KDE. Ce fut ma première rencontre avec le monde de l'open source. À la conférence, je pensais que les présentateurs et les personnes qui levaient la main étaient très intelligents. Je savais qu'il existait des logiciels libres, créés par la communauté pour la communauté. Mais les développeurs qui les construisaient m'étaient étrangers.

Je pensais que des personnes vraiment cool et intelligentes développaient ces logiciels. Je pensais qu'il fallait être très intelligent et privilégié pour les rejoindre.

J'ai essayé de participer au Google Summer of Code ([GSOC](https://summerofcode.withgoogle.com/)) deux fois pendant mes études, mais sans succès. Ensuite, après l'obtention de mon diplôme, pendant mon travail, j'ai utilisé de nombreux projets open source. Je les utilisais même en freelance. Je dépendais fortement des outils et technologies développés par la communauté. J'étais vraiment fasciné par les histoires des gens sur la façon dont ils avaient commencé à contribuer à l'open source, et comment ils avaient obtenu leurs incroyables emplois à distance !

Maintenant, après avoir procrastiné pendant deux autres mois et n'ayant pas réussi à décrocher un emploi à distance, j'ai décidé de le faire une fois pour toutes et de contribuer moi-même.

J'ai commencé à télécharger mon code sur [GitHub](https://github.com/drex44) — chaque fois que j'écrivais un nouveau code. J'ai créé un module open source [NPM](https://github.com/drex44/awesome-react-links) ainsi que quelques autres projets de démonstration et je les ai téléchargés. Mais ce n'était pas l'essentiel de l'open source. Je ne contribuais pas réellement à d'autres dépôts ou ne travaillais pas avec d'autres développeurs pour créer des logiciels. Je travaillais toujours en isolation.

### Hacktoberfest !

Puis cela est arrivé : je suis tombé sur [Hacktoberfest](https://hacktoberfest.digitalocean.com). Ils (DigitalOcean, GitHub et Twilio) offraient un **t-shirt gratuit** si vous soumettiez 5 Pull Requests à un projet open source sur GitHub en octobre. Même si votre PR n'était pas fusionnée, elle comptait toujours pour votre progression. Et cette fois, ils avaient une tonne de t-shirts, donc il était facile d'en obtenir un. C'était la dernière poussée dont j'avais besoin — apparemment, un t-shirt gratuit vous donne un incroyable coup de pouce !.

Ainsi, j'ai commencé mon voyage dans le MONDE DE L'OPEN SOURCE.

### Traquer les problèmes

J'ai recherché des projets open source à aborder sur GitHub. Je voulais des tâches faciles pour me familiariser rapidement avec le processus de PR. J'ai donc cherché des problèmes qui ne nécessitaient pas de plonger dans tout le code source.

Il y avait de nombreux développeurs qui avaient lancé des projets pour Hacktoberfest et les nouveaux venus. Il était facile de soumettre des PR dans ces dépôts, donc j'en ai soumis trois. J'ai soumis mes deux autres PR à d'autres projets personnels. Il y avait de nombreux autres dépôts où vous deviez simplement ajouter votre nom au fichier et soumettre la PR. Mais j'ai décidé que cela n'était pas productif et n'était pas l'esprit de l'open source.

Ensuite, je suis tombé sur cette développeuse incroyable. Elle avait créé un blog statique en Vue.js et avait listé de nombreux problèmes. Lorsque j'ai vu tous les problèmes, j'ai découvert qu'en fait, elle créait un blog personnel et faisait contribuer les gens en soulevant des problèmes et en les étiquetant avec des tags appropriés. J'étais comme **?.**

Puis j'ai réalisé que l'idée était géniale et j'ai pensé,

![Image](https://cdn-media-1.freecodecamp.org/images/Tr8DG2tcjF2t8FylD51k6TThhcMkT7BCA6C2)
_Hahaha_

J'ai été impressionné par son talent ! Elle construisait son blog statique, et en même temps, cela bénéficiait à d'autres développeurs. Les débutants apprenaient à travailler dans l'open source et obtenaient un t-shirt gratuit. Elle obtenait son blog grâce à un effort de groupe !

Découvrir son blog est ce qui m'a motivé à créer le [Good Food Guide](http://github.com/drex44/good-food-guide).

### L'essor du [Good Food Guide](http://github.com/drex44/good-food-guide)

J'avais déjà décidé quoi faire une fois que j'aurais fini de soumettre mes PR. Donc après deux jours de travail et de soumission de PR, il était temps pour un nouveau départ. J'ai été inspiré par tous les autres développeurs qui avaient créé un dépôt pour soutenir Hacktoberfest. Ils créaient tous un environnement accueillant pour encourager les nouveaux venus à soumettre des PR productives. Je voulais aussi apporter ma contribution à ce mouvement et j'ai décidé de créer mon propre dépôt de projet.

Moi aussi, je veux devenir entrepreneur, et j'ai une liste contenant plusieurs idées. Mais je ne voulais pas passer trop de temps à décider quel projet commencer. J'ai parcouru toutes les idées et j'ai choisi celle que je pensais facile à comprendre et facile à mettre en œuvre.

J'ai choisi de construire le **Good Food Guide**. Ma sœur et moi avions l'habitude de chercher sur Google quels aliments manger pour guérir une maladie particulière. J'ai pensé, et si il existait déjà un site où vous pouvez simplement aller et rechercher vos symptômes ou votre maladie et il vous dira quels aliments manger ? Il devrait être disponible dans toutes les langues afin que plusieurs personnes puissent l'utiliser facilement.

J'ai donc créé une interface utilisateur basique qui transmettait la motivation et l'utilisation du site web. Je voulais le télécharger rapidement, donc j'ai décidé d'avoir toutes les données dans un fichier statique uniquement. Je voulais choisir une technologie facile à apprendre et largement utilisée. Cela permettrait aux nouveaux développeurs d'apprendre ou aux développeurs existants de pratiquer. J'ai donc fini par utiliser React.

En plus de cela, j'ai décidé d'utiliser NextJs pour tirer parti de nombreuses de ses fonctionnalités. Il est également facile à utiliser si vous connaissez déjà React. J'ai téléchargé l'ensemble du projet sur [GitHub](https://github.com/drex44/good-food-guide) et le voyage a commencé. Mais cela ne suffisait pas pour attirer les développeurs.

### L'essor du mainteneur

Après avoir validé le code initial, j'ai ensuite produit une documentation appropriée. J'ai créé des problèmes avec les étiquettes appropriées. J'ai créé le problème comme nous créons des tâches dans un sprint agile. De plus, j'ai divisé les tâches en sous-tâches et les ai listées avec tous les détails.

Lorsque je cherchais des problèmes auxquels contribuer, je cherchais des problèmes avec un problème détaillé et des directives pour la solution. J'ai donc essayé d'inclure les informations que je cherchais initialement dans les problèmes.

Cela a fonctionné comme un charme, et c'était exactement ce qui était nécessaire pour embarquer les contributeurs débutants. Les projets populaires sont utiles pour contribuer. Le manque d'informations dans les problèmes fonctionne comme une démotivation pour eux. En raison de cela, la plupart d'entre eux ne travaillent pas sur des problèmes réels après avoir compilé le code.

#### Exemple de problème

![Image](https://cdn-media-1.freecodecamp.org/images/w4OHKsXyVbbu8ja7ckZRkMqLnwUiyGFAQK1Q)
_exemple de problème_

Une autre chose que j'ai faite a été de publier la branche principale avec Netlify. Netlify a une excellente application d'intégration avec GitHub. Donc, si une PR est fusionnée, le contributeur peut voir le changement passer en direct presque instantanément.

Le résultat ? J'ai obtenu 3 PR et 4 demandes de travail en seulement 2 heures (je vous l'avais dit, le pouvoir du t-shirt gratuit est très fort ?).

Je suis passé avec succès de contributeur à mainteneur de projet !

### Comprendre l'autre côté de la médaille

Le dépôt devenait de plus en plus populaire. Les gens soulevaient des problèmes pour des suggestions, soumettaient des PR et commentaient les problèmes. Mon dépôt attirait l'attention et c'était tout simplement incroyable.

Je recevais des notifications toute la journée. Chaque heure, je recevais au moins une notification de GitHub ! Je jonglais ici et là. Je passais en revue les PR, répondais aux commentaires, fusionnais les PR, soulevais plus de problèmes et contribuais.

Une fonctionnalité incroyable qui s'est avérée utile en intégrant Netlify était qu'il définissait automatiquement la CI (Intégration Continue) pour votre projet. Il effectue diverses vérifications sur la PR soumise et fournit également un déploiement de test où vous pouvez vérifier l'intégration. Je recommande d'utiliser cette fonctionnalité dans tous les projets que vous pouvez !

En conséquence, les gens apprenaient et s'amusaient ! Et obtenaient également un t-shirt gratuit. J'ai appris tellement de choses sur GitHub et git. Astuce pro : si vous voulez apprendre git rapidement, devenez mainteneur d'un projet open source. Cela m'a donné une nouvelle perspective et élargi ma vision. C'était donc une situation gagnant-gagnant pour nous tous.

> « Tout ce qui peut mal tourner tournera mal. » — Loi de Murphy

Pendant un certain temps, je vérifiais les détails des PR, parcourais le code, regardais l'intégration déployée et fusionnais les PR. Parfois, en raison de nombreuses PR en attente, après avoir fusionné la première PR, cela créait un effet de répercussion et il y avait des conflits dans toutes les autres PR. Maintenant, cela semblait mauvais au début, mais c'était une bénédiction déguisée. Grâce à cela, j'ai appris à résoudre les conflits dans git. J'ai résolu de nombreux conflits. L'éditeur en ligne de Github pour la fusion des PR s'est avéré très pratique pour les petits changements.

Bien que les PR n'avaient pas toutes une bonne qualité de code, j'ai tout de même fusionné la plupart d'entre elles. Parce que, venant de contributeurs pour la première fois, je ne voulais pas les décourager de soumettre plus de PR. Je connais le sentiment lorsque vous soumettez une PR et attendez que le mainteneur l'approuve ou la commente. Donc, pour garder l'esprit des contributeurs élevé, j'ai décidé de fusionner la PR et ensuite de faire le nettoyage moi-même (et je pense que cela a résulté en un sentiment positif pour les contributeurs).

À mesure que le nombre de PR augmentait, je ne pouvais pas consacrer beaucoup de temps à contribuer moi-même. La plupart de mon temps alloué passait à répondre aux commentaires, aux e-mails, et à fusionner et résoudre les PR. Après trois jours, je me suis assis pour nettoyer le code. C'était un désordre que j'avais moi-même invité. J'ai réalisé que j'aurais dû informer les contributeurs de suivre au moins quelques directives. Les noms de fichiers, les noms de fonctions et la structure du projet étaient tous incorrects. À mesure que le site web évoluait, ses problèmes aussi.

J'ai dû restructurer toute la base de code. C'était un changement radical, mais c'était beaucoup nécessaire. Si cela continuait, le code deviendrait non maintenable après un certain temps. C'est à ce moment-là que j'ai réalisé pourquoi de nombreuses entreprises insistent sur leurs normes de codage. Je veux dire, je connaissais déjà l'importance, mais l'expérimenter en première main en tant que mainteneur de projet était une autre chose ! Je pouvais voir pourquoi de nombreux projets open source populaires étaient rigides sur leurs normes de codage.

Je peux aussi voir comment mon processus de pensée a évolué au cours des 10 à 11 derniers jours. J'étais un contributeur naïf travaillant sur mon propre dépôt, mais j'ai réussi à devenir un mainteneur de projet travaillant avec tous les autres développeurs.

#### Statistiques GitHub

Voici les étoiles, les forks et les contributeurs des 11 derniers jours !

![Image](https://cdn-media-1.freecodecamp.org/images/Z3mB1v5Vuj0BoSNSc6QmeiJgu3IWjpWhPOtC)
_Statistiques GitHub_

### Le Résultat !

Un site web non réactif créé en 10 minutes !

![Image](https://cdn-media-1.freecodecamp.org/images/sge5u4AyVadJ9fC4UwNdg33Q8ImZG5ma91JZ)
_Accueil_

![Image](https://cdn-media-1.freecodecamp.org/images/gbfiLSsJoTthqzjE4hqtp45A6H-b1cNuLdNR)
_À propos_

#### Après 11 jours,

![Image](https://cdn-media-1.freecodecamp.org/images/Ic76JVetjNJC2SLApBL3k-FyIkLXocoak8HO)
_Accueil_

![Image](https://cdn-media-1.freecodecamp.org/images/1nAIMG-dkvqh68zeU8wTbr7mB2HZ2YktXmQz)
_À propos de nous_

![Image](https://cdn-media-1.freecodecamp.org/images/7JDpAL606fb8Lk1SlLJYzLtNkniILKvKQcdM)
_Contributeurs_

![Image](https://cdn-media-1.freecodecamp.org/images/WWXyT7MCe3aREFRrhmnDg5bclf7iznwhzUZz)
_détails des aliments (en cours de travail)_

![Image](https://cdn-media-1.freecodecamp.org/images/hLnCHASQNOpS68JGSzAgzD93fdx0dOiynqRb)
_conditions_

Vous pouvez également consulter la dernière version du site en direct sur [https://good-food-guide.now.sh](https://good-food-guide.now.sh/).

Chaque jour, le site s'améliore de manière petite ou grande.

#### En conclusion

Ce voyage de 11 jours a été formidable pour moi. J'ai appris beaucoup. Maintenant, je peux voir les deux côtés de la médaille.

Je vois le pouvoir d'une équipe et ce qu'elle peut accomplir. Si une poignée de personnes décident de travailler sur un problème particulier, elles peuvent tout résoudre. Les gens ont besoin d'un environnement accueillant et d'une petite récompense pour rester motivés.

Il peut être difficile pour les nouveaux développeurs de commencer à contribuer. Ils cherchent des problèmes à résoudre, mais ce n'est pas la seule façon de commencer à contribuer. L'idée principale est de s'amuser et de construire quelque chose collectivement, pour améliorer un logiciel. Si vous l'avez utilisé et savez quelque chose que vous pouvez améliorer, alors vous pouvez directement soulever le problème, discuter avec le mainteneur et soumettre une PR. Je pense que c'est l'une des meilleures façons de commencer.

Il est devenu clair pour moi comment un chef de projet utilise les forces de chaque individu pour accomplir une tâche qui aurait été difficile si elle était faite par une seule personne. C'est la même situation dans les projets open source. Le travail du mainteneur est similaire à celui du chef de projet. Ils doivent maintenir l'harmonie entre tous les développeurs et également écouter leurs pensées.

J'ai également réalisé que, auparavant, j'avais cette peur d'une grande base de code chaque fois que je pensais rejoindre un nouveau projet open source. Je compilais le code, l'exécutais et l'oubliais. Maintenant, cette peur a disparu et je pense que je peux faire le grand pas vers la contribution à de grands projets. J'espère continuer à apprendre de nouvelles choses et devenir un bon atout pour la communauté open source.

Merci d'avoir lu ! Et un grand merci à **Jennifer et Abbey** de freeCodeCamp pour la relecture. Elles m'ont aidé à préparer cet article et à en faire un article qui vaut votre temps.

Si vous avez des questions ou des suggestions, laissez-les dans les commentaires ci-dessous.

P.S. Si vous avez trouvé cet article utile, applaudissez ! ??? Cela semble gratifiant et me donne la motivation de continuer à écrire.

[**drex44/good-food-guide**](https://github.com/drex44/good-food-guide)
[_Un guide pour savoir quels aliments sont bons lorsque vous avez certaines maladies ! [Conçu en React/NextJs] - drex44/good-food-guide_github.com](https://github.com/drex44/good-food-guide)[**Good Food Guide**](https://good-food-guide.now.sh/)
[_Un guide pour savoir quels aliments sont bons lorsque vous avez certaines maladies !_ good-food-guide.now.sh](https://good-food-guide.now.sh/)

Édition :

URL du site en direct mise à jour vers [https://good-food-guide.now.sh](https://good-food-guide.now.sh/).
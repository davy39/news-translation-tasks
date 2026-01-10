---
title: Un nouvel outil pour prévenir les suppressions catastrophiques comme celles
  de GitLab
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-26T08:18:20.000Z'
originalURL: https://freecodecamp.org/news/why-and-how-i-created-a-new-wheel-to-prevent-gitlabs-disaster-b8cd5bea6e1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IutJzMkTq_6yyv2HTy2KJw.jpeg
tags:
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Un nouvel outil pour prévenir les suppressions catastrophiques comme celles
  de GitLab
seo_desc: 'By Alan Chen

  Basically: I found most of the existing tools not very helpful and made a new open
  source tool called rm-protection, which you can download from GitHub.

  I was riding a bus back to my dorm and I almost fell asleep. Suddenly one of my
  frie...'
---

Par Alan Chen

En résumé : J'ai trouvé que la plupart des outils existants n'étaient pas très utiles et j'ai créé un nouvel outil open source appelé `rm-protection`, que vous pouvez [télécharger depuis GitHub](https://github.com/alanzchen/rm-protection).

Je prenais le bus pour retourner à ma résidence universitaire et j'étais sur le point de m'endormir. Soudain, un de mes amis m'a envoyé un message sur Telegram : « GitLab a supprimé sa base de données de production et ils diffusent en direct la récupération de la base de données sur YouTube ! »

Ma tête a heurté le siège devant moi. Je n'ai pas senti la douleur, mais j'ai ressenti de la compassion pour les ops et j'ai voulu les soutenir avec #hugops tout en lisant leur journal d'incident.

Ne sommes-nous pas tous humains et sujets aux erreurs ? Mais certaines données sont tout simplement trop importantes pour être perdues. Par exemple, la base de données de production et les photos avec la famille et les amis.

J'ai une peur profondément ancrée de perdre des données. J'ai commencé à jouer avec Linux à l'école primaire, et à cette époque, je n'avais qu'un PC avec un seul disque dur. En tant qu'enfant et novice sous Linux, j'étais plus négligent que la plupart des utilisateurs sophistiqués. Une fois, j'ai accidentellement supprimé une partition entière — non seulement les fichiers système, mais aussi mon répertoire personnel.

Je me souviens encore de l'horreur lorsque tout a planté et que j'ai réalisé que je venais de supprimer toutes mes photos. Puis j'ai versé des larmes de bonheur lorsque `photorec` en a récupéré certaines.

### Un rapide tour d'horizon des outils actuels pour prévenir cela

Je suis descendu du bus, je suis retourné dans ma chambre et j'ai commencé à chercher des méthodes de prévention. J'en avais déjà entendu parler : `rm -i`, `Safe-rm` et `trash-cli`.

#### rm -i

`rm -i` nécessite une confirmation supplémentaire pour _chaque fichier et répertoire individuel_. Il est fastidieux de confirmer tout ce que vous voulez sûrement supprimer. Cela me rappelle l'histoire de _Le Garçon qui criait au loup_.

**Avertir pour _tout_ revient à ne rien avertir.** Ce qui est pire, certains utilisateurs ont développé l'habitude d'utiliser régulièrement `rm -rf`, où l'option `-f` annule la protection `-i`.

Dans le cas de l'incident de GitLab, `rm -i` n'aurait pas aidé : l'op savait quel répertoire il allait supprimer, mais il a oublié sur quelle machine il se trouvait. Il aurait pu taper « yes » et appuyer sur « return ».

#### `[Safe-rm](https://launchpad.net/safe-rm)`

De même, `[Safe-rm](https://launchpad.net/safe-rm)` n'aurait pas aidé non plus. `Safe-rm` dispose d'un fichier de configuration contenant une liste de chemins que vous souhaitez protéger. Il inclut certains chemins par défaut tels que `/usr/lib`. Les utilisateurs peuvent également créer leurs propres listes de chemins. Ce que fait `Safe-rm`, c'est fournir un avertissement supplémentaire au préalable, qui ne donne aucune information supplémentaire sur la raison pour laquelle il vous arrête.

Pensez à la situation de GitLab : l'op aurait simplement pu appuyer sur « y » (il aurait pensé que ce n'était pas une base de données de production, pourquoi ne pas appuyer sur « y » ?). De plus, `Safe-rm` ne fournit pas de protection pour les liens symboliques et la récursion.

Désolé, `Safe-rm`. (Un autre outil s'appelle `[rmfd](https://github.com/d5h/rmfd/wiki)`, un fork de GNU coreutils avec un mécanisme de protection similaire)

#### `trash-cli`

Le seul outil que j'ai trouvé utile pour la situation de GitLab est `trash-cli`. Jusqu'à présent, c'est la meilleure solution que je connaisse. Il apporte la corbeille à la ligne de commande. `trash-cli` peut sûrement prévenir environ 90 % des accidents (y compris celui de GitLab).

Mais que se passe-t-il si vous réalisez qu'il manque quelque chose longtemps après avoir vidé la corbeille.

Ou imaginez que vous manquez d'espace, mais que vous avez des tonnes de données à écrire sur le disque. Vous êtes pressé de libérer de l'espace (comme supprimer la base de données remplie de messages de spam). Vérifieriez-vous toujours soigneusement la corbeille ?

Ainsi, `trash-cli` n'était pas la solution ultime que je recherchais.

### À la recherche d'inspiration

La salle de bain a toujours été un endroit idéal pour les moments d'eureka.

Il était 23 heures. J'ai pris une douche et je n'ai pas arrêté de me parler à moi-même pour trouver une solution afin de prévenir l'incident de GitLab.

> « Qu'est-ce qui cause exactement des accidents comme celui arrivé à GitLab ? »

> « Ne pas savoir ce que l'on fait. »

Nous étions encore en plein milieu des vacances de printemps, et il n'y avait personne autour de mon université. Ainsi, je pouvais me parler à moi-même dans la salle de bain sans que les gens pensent que j'étais fou.

> « Comment faire pour que les utilisateurs sachent clairement ce qu'ils font ? »

> « Hmmm, peut-être en les faisant le dire à voix haute ? »

Je suis sorti en trombe de la salle de bain.

### Invention de l'outil

J'ai immédiatement envoyé un message à mes amis au sujet de mon idée : les utilisateurs « protègent » les fichiers et répertoires importants pendant la période de déploiement. La protection est réalisée en définissant une question de sécurité et une réponse.

Imaginez ceci : lorsque les ops de GitLab déploient des bases de données sur le serveur de production, ils « protègent » également les répertoires des bases de données en configurant une question « Quelle base de données supprimez-vous ? (db1/db2) » et une réponse « db1 ».

Par la suite, lors de toute tentative de suppression de ces répertoires, une version modifiée de `rm` vous posera la question. À moins de connaître la bonne réponse, vous ne pourrez pas continuer.

Les ops de GitLab n'auraient pas pu entrer « db1 » s'ils pensaient que c'était « db2 ». En s'assurant qu'ils savaient ce qu'ils faisaient, la base de données de GitLab aurait pu être sauvée.

J'ai donc écrit un script Python nommé « rm-p.py ». C'est un wrapper pour `rm` qui vérifie s'il existe un fichier `.<nomdufichier>.rm-prot` correspondant (que j'appelle un « fichier de protection »). L'invite pose la question définie dans le fichier de protection lorsqu'il est trouvé.

Si vous donnez la bonne réponse, `rm-p.py` transmettra votre argument à `rm`. Sinon, il ne le fera pas. Bien sûr, il transmettra toujours les fichiers non protégés à `rm`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TEdo7UKvDVyrYBl_iOC-kA.png)
_Démo : Tentative de suppression d'un fichier protégé._

J'ai appelé ce petit script `rm-protection` et j'ai créé un logo pour lui.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9VSw4FTwQG_UsmP5829piA.png)

Le package `rm-protection` est maintenant disponible sur PyPi et le code source est sur [GitHub](https://github.com/alanzchen/rm-protection).

### Qu'est-ce qui vous protège finalement ?

Pour les entreprises et les équipes, les sauvegardes sont sûrement la protection la plus importante contre la perte de données. Elles vous protègent non seulement des erreurs de manipulation, mais aussi des catastrophes naturelles.

Mais pour les particuliers, des sauvegardes complètes ne sont pas toujours économiques ou pratiques.

Mettons de côté le manque de sauvegardes, les mauvaises habitudes sont presque toujours à l'origine de ces erreurs de manipulation.

Nous avons inventé tant d'outils pour gérer ces mauvaises habitudes, mais ils peuvent amener les utilisateurs à adopter de nouvelles mauvaises habitudes.

> « La meilleure et la seule bonne façon de vérifier ce que vous allez supprimer. »

Ou du moins, c'est ce que certains pourraient dire. Mais peu peuvent vivre en ayant à confirmer **chaque** suppression. Ainsi, `rm -rf` devient leur nouvelle mauvaise habitude.

Les outils actuels vous protègent soit avant (comme `rm -i` ou `safe-rm`), soit après (`trash-cli`) les suppressions accidentelles. Les premiers apportent souvent plus de problèmes que prévu dans les opérations quotidiennes.

Les seconds, comme `trash-cli`, ne fournissent pas de protection en amont. Il y a des chances que vous perdiez toujours le fichier important.

Après avoir réfléchi à la question, j'ai réalisé qu'il n'existe pas de _solution ultime_. `rm-protection` est juste une couche de protection supplémentaire. Ce n'est pas la partie la plus vitale de la protection, mais cela peut vous faire gagner beaucoup de temps pour récupérer vos données à partir des sauvegardes.

`rm-protection` **ne vous dérange pas lorsque ce n'est pas nécessaire**, vous gardez donc la flexibilité et l'efficacité pour les opérations quotidiennes. Lorsque c'est vraiment important que vous ne deviez pas supprimer quelque chose, il vous pose une question que vous avez définie.

> Pour être sûr à 99 %, ce dont vous avez besoin est une combinaison de bonnes habitudes, d'un esprit clair et attentif, de sauvegardes fonctionnelles, d'une bonne méthode de protection et de chance.

### Les meilleures pratiques

En résumé, vous devriez faire ce qui suit pour assurer la sécurité de vos données :

1. Faites des **sauvegardes**.
2. **Vérifiez les sauvegardes** régulièrement.
3. **Gardez l'esprit clair. N'utilisez pas** `rm -rf`.
4. Ajoutez une couche de protection supplémentaire : choisissez `rm-protection`, `trash-cli` ou tout autre outil que vous préférez.

Et vous devriez être sûr à 99 %.
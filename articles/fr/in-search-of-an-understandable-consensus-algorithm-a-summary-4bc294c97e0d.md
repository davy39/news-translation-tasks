---
title: 'Comprendre l''algorithme de consensus Raft : un résumé d''article académique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-11T20:01:24.000Z'
originalURL: https://freecodecamp.org/news/in-search-of-an-understandable-consensus-algorithm-a-summary-4bc294c97e0d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*U14WseYPLL8tHj0V.png
tags:
- name: Computer Science
  slug: computer-science
- name: research
  slug: research
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Comprendre l''algorithme de consensus Raft : un résumé d''article académique'
seo_desc: 'By Shubheksha Jalan

  This post summarizes the Raft consensus algorithm presented in the paper In Search
  of An Understandable Consensus Algorithm by Diego Ongaro and John Ousterhout. All
  pull quotes are taken from that paper.


  _[Credit](https://github....'
---

Par Shubheksha Jalan

Cet article résume l'algorithme de consensus Raft présenté dans le document [In Search of An Understandable Consensus Algorithm](https://www.usenix.org/system/files/conference/atc14/atc14-paper-ongaro.pdf) par Diego Ongaro et John Ousterhout. Toutes les citations sont tirées de ce document.

![Image](https://cdn-media-1.freecodecamp.org/images/VeSdEtdSjLC4GMzHVxB3b7tICAH7Zj77lIQJ)
_[Crédit](https://github.com/raft/logo/tree/3d2c4d5ca0d9c4fb8d5c28a82c4a43e576673b06" rel="noopener" target="_blank" title=")_

#### Raft :

Raft est un algorithme de consensus distribué. Il a été conçu pour être facilement compris. Il résout le problème de faire en sorte que plusieurs serveurs s'accordent sur un état partagé, même en cas de défaillances. L'état partagé est généralement une structure de données soutenue par un journal répliqué. Nous avons besoin que le système soit pleinement opérationnel tant qu'une majorité des serveurs est en fonctionnement.

Raft fonctionne en élisant un leader dans le cluster. Le leader est responsable de l'acceptation des requêtes clients et de la gestion de la réplication du journal vers les autres serveurs. Les données circulent uniquement dans un sens : du leader vers les autres serveurs.

Raft décompose le consensus en trois sous-problèmes :

* Élection du leader : Un nouveau leader doit être élu en cas de défaillance d'un leader existant.
* Réplication du journal : Le leader doit maintenir les journaux de tous les serveurs synchronisés avec le sien par réplication.
* Sécurité : Si l'un des serveurs a validé une entrée de journal à un index particulier, aucun autre serveur ne peut appliquer une entrée de journal différente pour cet index.

![Image](https://cdn-media-1.freecodecamp.org/images/1ut8JaHSVAN0gOvJKMwLbDAKNfuWYuMBrYnl)
_Raft garantit que ces propriétés sont vraies à tout moment._

#### Bases :

Chaque serveur existe dans l'un des trois états : leader, follower ou candidat.

![Image](https://cdn-media-1.freecodecamp.org/images/oN6xZLkKQrVnaWWlp7I8w9aep2NNgMz5fR9D)
_Changements d'état des serveurs_

> En fonctionnement normal, il y a exactement un leader et tous les autres serveurs sont des followers. Les followers sont passifs : ils n'émettent aucune requête de leur propre initiative mais répondent simplement aux requêtes des leaders et des candidats. Le leader traite toutes les requêtes clients (si un client contacte un follower, le follower le redirige vers le leader). Le troisième état, candidat, est utilisé pour élire un nouveau leader.

Raft divise le temps en **mandats** de longueur arbitraire, chacun commençant par une élection. Si un candidat remporte l'élection, il reste leader pour le reste du mandat. Si le vote est partagé, alors ce mandat se termine sans leader.

Le **numéro de mandat** augmente de manière monotone. Chaque serveur stocke le **numéro de mandat actuel** qui est également échangé dans chaque communication.

> ... si le mandat actuel d'un serveur est inférieur à celui d'un autre, il met à jour son mandat actuel avec la valeur la plus grande. Si un candidat ou un leader découvre que son mandat est obsolète, il redevient immédiatement follower. Si un serveur reçoit une requête avec un numéro de mandat obsolète, il rejette la requête.

Raft utilise deux appels de procédure à distance (RPC) pour effectuer son opération de base.

* RequestVotes est utilisé par les candidats pendant les élections
* AppendEntries est utilisé par les leaders pour répliquer les entrées de journal et également comme un heartbeat (un signal pour vérifier si un serveur est en fonctionnement ou non — il ne contient aucune entrée de journal)

#### Élection du leader

Le leader envoie périodiquement un heartbeat à ses followers pour maintenir son autorité. Une élection de leader est déclenchée lorsqu'un follower dépasse le temps d'attente pour un heartbeat du leader. Ce follower passe à l'état candidat et incrémente son **numéro de mandat**. Après avoir voté pour lui-même, il envoie des RPC RequestVotes en parallèle aux autres dans le cluster. Trois résultats sont possibles :

1. Le candidat reçoit des votes de la majorité des serveurs et devient leader. Il envoie ensuite un message heartbeat aux autres dans le cluster pour établir son autorité.
2. Si d'autres candidats reçoivent des RPC AppendEntries, ils vérifient le numéro de mandat. Si le numéro de mandat est supérieur au leur, ils acceptent le serveur comme leader et reviennent à l'état follower. Si le numéro de mandat est inférieur, ils rejettent le RPC et restent candidats.
3. Le candidat ne perd ni ne gagne. Si plus d'un serveur devient candidat en même temps, le vote peut être partagé sans majorité claire. Dans ce cas, une nouvelle élection commence après qu'un des candidats dépasse le temps d'attente.

> Raft utilise des délais d'élection aléatoires pour s'assurer que les votes partagés sont rares et qu'ils sont résolus rapidement. Pour éviter les votes partagés dès le départ, les délais d'élection sont choisis aléatoirement dans un intervalle fixe (par exemple, 150–300 ms). Cela répartit les serveurs de sorte que, dans la plupart des cas, un seul serveur dépassera le temps d'attente ; il remporte l'élection et envoie des heartbeats avant que d'autres serveurs ne dépassent le temps d'attente. Le même mécanisme est utilisé pour gérer les votes partagés. Chaque candidat redémarre son délai d'élection aléatoire au début d'une élection, et il attend que ce délai expire avant de commencer la prochaine élection ; cela réduit la probabilité d'un autre vote partagé dans la nouvelle élection.

#### Réplication du journal :

Les requêtes clients sont supposées être en écriture seule pour l'instant. Chaque requête consiste en une commande à exécuter idéalement par les machines à états répliquées de tous les serveurs. Lorsqu'un leader reçoit une requête client, il l'ajoute à son propre journal en tant que nouvelle entrée. Chaque entrée dans un journal :

* Contient la commande spécifiée par le client
* A un index pour identifier la position de l'entrée dans le journal (l'index commence à 1)
* A un **numéro de mandat** pour identifier logiquement quand l'entrée a été écrite

Il doit répliquer l'entrée à tous les nœuds followers afin de maintenir les journaux cohérents. Le leader envoie des RPC AppendEntries à tous les autres serveurs en parallèle. Le leader réessaie jusqu'à ce que tous les followers répliquent la nouvelle entrée en toute sécurité.

Lorsque l'entrée est répliquée à une majorité de serveurs par le leader qui l'a créée, elle est considérée comme validée. Toutes les entrées précédentes, y compris celles créées par des leaders antérieurs, sont également considérées comme validées. Le leader exécute l'entrée une fois qu'elle est validée et retourne le résultat au client.

Le leader maintient l'index le plus élevé qu'il sait être validé dans son journal et l'envoie avec les RPC AppendEntries à ses followers. Une fois que les followers découvrent que l'entrée a été validée, ils appliquent l'entrée à leur machine à états dans l'ordre.

> Raft maintient les propriétés suivantes, qui constituent ensemble la Propriété de Correspondance des Journaux

> • Si deux entrées dans différents journaux ont le même index et le même mandat, alors elles stockent la même commande.

> • Si deux entrées dans différents journaux ont le même index et le même mandat, alors les journaux sont identiques dans toutes les entrées précédentes.

Lors de l'envoi d'un RPC AppendEntries, le leader inclut le **numéro de mandat** et l'index de l'entrée qui précède immédiatement la nouvelle entrée. Si le follower ne trouve pas de correspondance pour cette entrée dans son propre journal, il rejette la requête pour ajouter la nouvelle entrée.

Cette vérification de cohérence permet au leader de conclure que chaque fois qu'AppendEntries retourne avec succès d'un follower, ils ont des journaux identiques jusqu'à l'index inclus dans le RPC.

Mais les journaux des leaders et des followers peuvent devenir incohérents en cas de crash du leader.

> Dans Raft, le leader gère les incohérences en forçant les journaux des followers à dupliquer le sien. Cela signifie que les entrées conflictuelles dans les journaux des followers seront écrasées par les entrées du journal du leader.

Le leader essaie de trouver le dernier index où son journal correspond à celui du follower, supprime les entrées supplémentaires si nécessaire, et ajoute les nouvelles.

> Le leader maintient un nextIndex pour chaque follower, qui est l'index de la prochaine entrée de journal que le leader enverra à ce follower. Lorsqu'un leader prend le pouvoir pour la première fois, il initialise toutes les valeurs nextIndex à l'index juste après le dernier dans son journal.

Chaque fois qu'AppendRPC retourne avec un échec pour un follower, le leader décrémente le **nextIndex** et envoie un autre RPC AppendEntries. Finalement, nextIndex atteindra une valeur où les journaux convergent. AppendEntries réussira lorsque cela se produira et il pourra supprimer les entrées superflues (le cas échéant) et ajouter de nouvelles entrées du journal du leader (le cas échéant). Ainsi, un AppendEntries réussi d'un follower garantit que le journal du leader est cohérent avec lui.

> Avec ce mécanisme, un leader n'a pas besoin de prendre des actions spéciales pour restaurer la cohérence du journal lorsqu'il prend le pouvoir. Il commence simplement le fonctionnement normal, et les journaux convergent automatiquement en réponse aux échecs de la vérification de cohérence Append-Entries. Un leader ne remplace ni ne supprime jamais les entrées dans son propre journal.

#### Sécurité :

Raft s'assure que le leader pour un mandat a validé les entrées de tous les mandats précédents dans son journal. Cela est nécessaire pour garantir que tous les journaux sont cohérents et que les machines à états exécutent le même ensemble de commandes.

Lors d'une élection de leader, le RPC RequestVote inclut des informations sur le journal du candidat. Si l'électeur constate que son journal est plus à jour que celui du candidat, il ne vote pas pour lui.

> Raft détermine quel journal est le plus à jour en comparant l'index et le mandat des dernières entrées dans les journaux. Si les journaux ont des dernières entrées avec des mandats différents, alors le journal avec le mandat le plus récent est le plus à jour. Si les journaux se terminent avec le même mandat, alors le journal le plus long est le plus à jour.

#### Adhésion au cluster :

> Pour que le mécanisme de changement de configuration soit sûr, il ne doit y avoir aucun moment pendant la transition où il est possible que deux leaders soient élus pour le même mandat. Malheureusement, toute approche où les serveurs passent directement de l'ancienne configuration à la nouvelle configuration est dangereuse.

Raft utilise une approche en deux phases pour modifier l'adhésion au cluster. D'abord, il passe à une configuration intermédiaire appelée **consensus joint**. Ensuite, une fois que cela est validé, il passe à la nouvelle configuration.

> Le consensus joint permet aux serveurs individuels de passer d'une configuration à l'autre à différents moments sans compromettre la sécurité. De plus, le consensus joint permet au cluster de continuer à servir les requêtes clients tout au long du changement de configuration.

Le consensus joint combine les nouvelles et anciennes configurations comme suit :

* Les entrées de journal sont répliquées sur tous les serveurs des deux configurations
* Tout serveur de l'ancienne ou de la nouvelle configuration peut devenir leader
* L'accord nécessite des majorités séparées des anciennes et nouvelles configurations

Lorsque le leader reçoit un message de changement de configuration, il stocke et réplique l'entrée pour le consensus joint _C<ancien, nouveau>_. Un serveur utilise toujours la configuration la plus récente dans son journal pour prendre des décisions, même si elle n'est pas validée. Lorsque le consensus joint est validé, seuls les serveurs _avec C<ancien, nouveau>_ dans leurs journaux peuvent devenir leaders.

> Il est maintenant sûr pour le leader de créer une entrée de journal décrivant C<nouveau> et de la répliquer dans le cluster. Encore une fois, cette configuration prendra effet sur chaque serveur dès qu'elle sera vue. Lorsque la nouvelle configuration a été validée selon les règles de C<nouveau>, l'ancienne configuration est irrelevante et les serveurs non présents dans la nouvelle configuration peuvent être arrêtés.

Une visualisation fantastique de comment Raft fonctionne peut être trouvée [ici](http://thesecretlivesofdata.com/raft/).

Plus de matériel tel que des discussions, des présentations, des articles connexes et des implémentations open-source peuvent être trouvés [ici](https://raft.github.io/).

Je n'ai creusé que dans les détails de l'algorithme de base qui compose Raft et les garanties de sécurité qu'il fournit. Le document contient beaucoup plus de détails et il est très accessible car le but principal des auteurs était la compréhensibilité. Je vous recommande définitivement de le lire même si vous n'avez jamais lu d'autre document auparavant.

Si vous avez aimé cet article, veuillez cliquer sur le bouton d'applaudissement ci-dessous pour que plus de gens le voient. Merci.

P.S. — Si vous êtes arrivé jusqu'ici et que vous souhaitez recevoir un mail chaque fois que je publie un de ces articles, inscrivez-vous [ici](http://eepurl.com/dcHGFP).
---
title: 'Certaines Contraintes & Compromis Dans La Conception des Communications Réseau
  : Un Résumé'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-25T18:44:11.000Z'
originalURL: https://freecodecamp.org/news/some-constraints-trade-offs-in-the-design-of-network-communications-a-summary-19589efd55d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1xL5XULHeYCPNkGwBSA3jQ.png
tags:
- name: Computer Science
  slug: computer-science
- name: distributed systems
  slug: distributed-systems
- name: General Programming
  slug: programming
- name: research
  slug: research
- name: summary
  slug: summary
seo_title: 'Certaines Contraintes & Compromis Dans La Conception des Communications
  Réseau : Un Résumé'
seo_desc: 'By Shubheksha Jalan

  This article distills the content presented in the paper “Some Constraints and Trade-offs
  In The Design of Network Communications” published in 1975 by E. A. Akkoyunlu et
  al.

  The paper focuses on the inclusion of Interprocess Comm...'
---

Par Shubheksha Jalan

Cet article résume le contenu présenté dans le document [Certaines Contraintes et Compromis Dans La Conception des Communications Réseau](http://dsg.tuwien.ac.at/linksites/teaching/courses/AdvancedDistributedSystems/download/1975_Akkoyunlu,%20Ekanadham,%20Huber_Some%20constraints%20and%20tradeoffs%20in%20the%20design%20of%20network%20communications.pdf) publié en 1975 par E. A. Akkoyunlu et al.

Le document se concentre sur l'inclusion de primitives de Communication Interprocessus (IPC) et les conséquences de le faire. Il explore, en particulier, le délai d'attente et la fonctionnalité de propriété d'insertion décrite en détail ci-dessous en ce qui concerne les systèmes distribués de processus séquentiels sans tampon système et interruptions.

Il aborde également le problème des deux généraux qui stipule qu'il est impossible pour deux processus de se mettre d'accord sur une décision sur un réseau non fiable.

### Introduction :

La conception d'un Mécanisme de Communication Interprocessus (IPCM) peut être décrite en énonçant le comportement du système et les services requis. Les fonctionnalités à inclure dans l'IPCM sont très critiques car elles peuvent être interdépendantes, d'où le processus de conception doit commencer par une spécification détaillée. Cela implique une compréhension approfondie des conséquences de chaque décision.

> L'objectif principal du document est de souligner l'interdépendance des fonctionnalités à incorporer dans le système.

Le document indique que parfois l'incompatibilité entre les fonctionnalités est visible dès le départ. Pourtant, parfois deux fonctionnalités qui semblent complètement sans rapport finissent par s'affecter mutuellement de manière significative. Si les compromis impliqués ne sont pas explorés dès le début, il pourrait ne pas être possible d'inclure des fonctionnalités souhaitables. Essayer d'accommoder des fonctionnalités conflictuelles entraîne un code désordonné au détriment de l'élégance.

#### Processus Intermédiaires :

Supposons qu'un système n'autorise pas la communication indirecte entre des processus qui ne peuvent pas établir de connexion. Les utilisateurs se soucient uniquement de l'expéditeur et du destinataire logiques des messages : ils ne se soucient pas du chemin que les messages empruntent ou du nombre de processus qu'ils traversent pour atteindre leur destination finale. Dans une telle situation, les processus intermédiaires viennent à notre secours. Ils ne font pas partie de l'IPCM mais sont insérés entre deux processus qui ne peuvent pas communiquer directement via un processus de répertoire ou de courtier lorsque la connexion est établie. Ils sont les seuls à connaître la nature indirecte de la communication entre les processus.

### Systèmes Centralisés vs. Distribués :

#### Installation de Communication Centralisée

1. Dispose d'un seul agent capable de maintenir toutes les informations d'état liées à la communication se produisant dans le système
2. L'agent peut également modifier l'état du système de manière bien définie

Par exemple, si nous considérons l'IPCM comme l'agent centralisé, il sera responsable de la correspondance des demandes SEND et RECEIVE de deux processus, du transfert de données entre leurs tampons et de la transmission du statut approprié aux deux.

#### Installation de Communication Distribuée

1. Aucun agent unique ne possède toutes les informations d'état à tout moment
2. L'IPCM est composé de plusieurs composants individuels qui coordonnent, échangent et travaillent avec des parties des informations d'état qu'ils possèdent.
3. Un changement global peut prendre un temps considérable
4. Si l'un des composants tombe en panne, l'activité des autres composants nous intéresse toujours

![Image](https://cdn-media-1.freecodecamp.org/images/gKAM3khbKCC4hxqH3GK04lKgz0u7iWIYS3uO)

**Cas 1 :**

Dans la Figure 1, P1 et P2 sont les deux processus de communication sur différentes machines via un réseau avec leurs propres IPCM et P est l'interface qui permet cela, avec des parties qui se trouvent sur les deux machines. P gère les détails des lignes de réseau.

> Si une machine ou un lien de communication tombe en panne, nous voulons que les IPCM survivants continuent leur opération. Au moins un composant devrait détecter une défaillance et être capable de communiquer. (En cas de défaillance d'un lien de communication, les deux extrémités doivent le savoir.)

**Cas 2 :**

La communication distribuée peut également se produire sur la même machine à condition qu'il y ait un ou plusieurs processus intermédiaires participant au système. Dans ce cas, P, P1 et P2 seront des processus sur le même système avec des IPCM identiques. P est un processus intermédiaire qui facilite la communication entre P1 et P2.

Les transactions entre P1 et P2 consistent en deux étapes : P1 à P et P à P2. Normalement, le statut renvoyé à P1 refléterait le résultat du transfert de P1 à P, mais P1 s'intéresse au statut de la transaction globale de P1 à P2.

Une façon de gérer cela est un **retour de statut différé**. Le statut n'est pas envoyé à l'expéditeur immédiatement après la transaction mais seulement lorsque l'expéditeur émet une primitive SEND STATUS. Dans l'exemple ci-dessus, après avoir reçu le message de P1, P l'envoie à P2, n'envoie aucun statut à P1 et attend de recevoir un statut de P2. Lorsqu'il reçoit le statut approprié de P2, il le transmet à P1 en utilisant la primitive SEND STATUS.

#### Cas Particuliers de l'Installation Distribuée

Cette section commence par énoncer certains faits et raisonnements autour d'eux.

> FAIT 0 : Un système distribué parfaitement fiable peut être amené à se comporter comme un système centralisé.

Théoriquement, cela est possible si :

1. L'état des différents composants du système est connu à tout moment
2. Après chaque transaction, le statut est correctement transmis entre les processus via leurs IPCM en utilisant une communication fiable.

Cependant, cela n'est pas possible en pratique car nous n'avons pas de réseau parfaitement fiable. Par conséquent, la version plus réaliste du fait ci-dessus est :

> FAIT I : Un IPCM distribué peut être amené à simuler un système centralisé à condition que :

> 1. Le système global reste connecté à tout moment, et

> 2. Lorsqu'un lien de communication tombe en panne, les IPCM des composants qui y sont connectés le savent, et

> 3. Le temps moyen entre deux pannes consécutives est grand par rapport au temps moyen de transaction à travers le réseau.

Le document indique que si les conditions ci-dessus sont remplies, nous pouvons établir des liens de communication suffisamment fiables pour simuler des systèmes centralisés car :

1. Il y a toujours un chemin de l'expéditeur au destinataire
2. Une seule copie d'un message non livré sera conservée par le système en cas de panne due à la détection de panne de lien. Par conséquent, un message ne peut pas être perdu s'il n'est pas livré et sera supprimé du système lorsqu'il sera livré.
3. Une stratégie de routage et une limite du taux de panne garantissent qu'un message se déplaçant dans un sous-ensemble de nœuds finira par sortir en un temps fini si le nœud cible n'est pas présent dans le sous-ensemble.

Les cas décrits ci-dessus sont des cas particuliers car ils font beaucoup d'hypothèses, utilisent des algorithmes inefficaces et ne tiennent pas compte des partitions de réseau conduisant à des composants déconnectés.

### Statut dans les Systèmes Distribués

#### Statut Complet

Un statut complet est celui qui transmet le résultat final du message, comme s'il a atteint sa destination.

> FAIT 2 : Dans une installation distribuée arbitraire, il est impossible de fournir un statut complet.

![Image](https://cdn-media-1.freecodecamp.org/images/XJzsqHDXwVzw4k-tW2Zzch6crkuXxPEtbpNy)

**Cas 1 :**

Supposons qu'un système est partitionné en deux réseaux disjoints, laissant les IPCM déconnectés. Maintenant, si IPCM1 attendait un statut de IPCM2, il n'y a aucun moyen de l'obtenir et de transmettre le résultat à P1.

**Cas 2 :**

Considérons la figure 2, s'il n'y a pas de mécanisme de détection de panne fiable présent dans le système et que IPCM2 envoie un message de statut à IPCM1, alors il ne peut jamais être sûr qu'il a atteint ou non sans un accusé de réception. Cela conduit à un échange infini de messages.

#### **Délais d'Attente**

Les délais d'attente sont nécessaires car le système dispose de ressources finies et ne peut pas se permettre d'être bloqué indéfiniment. Le document indique que :

> FAIT 3 : Dans un système distribué avec des délais d'attente, il est impossible de fournir un statut complet (même si le système est absolument fiable).

![Image](https://cdn-media-1.freecodecamp.org/images/QjeuiCyIRP-6DdAzBYgD666NJAWxLhgJ0zPH)

Dans la figure 3, P1 essaie d'envoyer un message à P2 via une chaîne d'IPCM.

Supposons que I1 prenne des données de P1 mais avant qu'il n'entende parler du statut de la transaction, la demande de P1 expire. IPCM1 n'a maintenant aucune connaissance sur le résultat final, que les données aient été reçues avec succès par P2 ou non. Quel que soit le statut qu'il renvoie à P1, il peut s'avérer incorrect. Par conséquent, il est impossible de fournir un statut complet dans une installation distribuée avec des délais d'attente.

#### Propriété d'Insertion

Un IPCM possède la propriété d'insertion si nous insérons un processus intermédiaire P entre deux processus P1 et P2 qui souhaitent communiquer de telle sorte que :

1. P est invisible pour P1 et P2
2. Le statut transmis à P1 et P2 est le même que celui qu'ils obtiendraient s'ils étaient directement connectés

> FAIT 4 : Dans un système distribué avec des délais d'attente, la propriété d'insertion ne peut être possédée que si l'IPCM retient certaines informations de statut qui lui sont connues.

Un statut différé est nécessaire pour remplir la propriété d'insertion. Considérons que le message est envoyé de P1 à P2. Que se passe-t-il si P reçoit le message de P1, il passe en état `attente-statut` mais le délai expire avant que P ne puisse connaître le statut ?

Nous ne pouvons pas dire à P1 le résultat final de l'échange car il n'est pas encore disponible. Nous ne pouvons pas non plus laisser P savoir qu'il est en état `attente-statut` car cela signifierait que le message a été reçu par quelqu'un. Il n'est pas non plus possible que P2 n'ait jamais reçu les données car une telle situation ne peut pas survenir si P1 et P2 sont directement connectés et viole donc la propriété d'insertion.

La solution à cela est de fournir un statut ambigu à P1, un statut qui est aussi susceptible d'être possible si les deux processus étaient connectés directement.

> Ainsi, une suppression délibérée de ce qui s'est passé est introduite en fournissant le même statut pour couvrir un délai d'attente qui se produit lors de l'attente du statut et, par exemple, une erreur de transmission.

### Messages Logiques et Physiques

La fonction de base d'un IPCM est le transfert et la synchronisation de données entre deux processus. Cela peut se produire en divisant les messages physiques initialement envoyés par le processus expéditeur dans le cadre d'une seule opération en messages plus petits, également connus sous le nom de messages logiques pour faciliter le transfert.

#### Considérations sur la Taille du Tampon

![Image](https://cdn-media-1.freecodecamp.org/images/emD1vUav17PwafIrLIxbg4ch3fpRdJjL8Mr1)

Comme illustré dans la figure 5, si une incompatibilité de tampon survient, nous pouvons adopter les approches suivantes pour la résoudre :

1. Définir une taille de tampon système. Cela est extrêmement restrictif, surtout dans un réseau de systèmes hétérogènes.
2. Satisfaire la demande avec la petite taille de tampon et informer les deux processus impliqués de ce qui s'est passé. Cette approche nécessite que les processus soient conscients des détails de bas niveau de la communication.
3. Autoriser les transferts partiels. Dans cette approche, seul le processus qui a émis la demande la plus petite (50 mots) est réveillé. Tous les autres processus restent endormis en attendant d'autres transferts. Si le tampon du destinataire n'est pas plein, un indicateur EOM (End Of Message) est nécessaire pour le réveiller.

#### Transferts Partiels et Ports Bien Connus

![Image](https://cdn-media-1.freecodecamp.org/images/E-5x03qgbd0Ks6OoNjr2WKZVa1BPtg5kAchU)

Dans la figure 6, un processus de service utilisant un port bien connu accepte les demandes de plusieurs processus utilisateurs, P1...Pn. Si P1 envoie un message au processus de service qui n'est pas complet et ne remplit pas son tampon, nous devons considérer les situations suivantes :

1. Le port bien connu est réservé pour P1. Aucun autre processus ne peut communiquer avec le processus de service en l'utilisant tant que P1 n'a pas terminé.
2. Lorsque le processus de service expire pendant que P1 se prépare à envoyer la deuxième et dernière partie du message, nous devons le gérer sans informer P1 que la première partie a été ignorée. P1 n'écoute pas les messages entrants du processus de service.

Puisque aucun de ces problèmes ne survient sans transferts partiels, une solution consiste à les interdire complètement. Par exemple :

> C'est l'approche adoptée dans ARPANET où la communication vers les ports bien connus est restreinte à des messages courts et complets qui sont utilisés pour établir une connexion séparée pour la communication ultérieure.

#### Processus Tampon

![Image](https://cdn-media-1.freecodecamp.org/images/mVbGqJg3Eawc9Zq9oOukZj4RcWRkQ-Ji6b2N)
_Cette solution est modélisée autour de la création de processus dynamiques._

Chaque fois que P1 souhaite transférer des données au processus de service, un nouveau processus S1 est créé et reçoit des messages de P1 jusqu'à ce que le message logique soit complété, dormant selon les besoins. Ensuite, il envoie le message physique complet au processus de service avec le drapeau EOM activé. Ainsi, aucun transfert partiel ne se produit entre S1 et le processus de service, ils sont tous filtrés avant cela.

Cependant, ce type de solution n'est pas possible avec les ports bien connus. S1 est inséré entre P1 et le processus de service lorsque la connexion est initialisée. Dans le cas des ports bien connus, aucune initialisation n'a lieu.

> En discutant du statut renvoyé aux utilisateurs, nous avons indiqué comment la présence de certaines autres fonctionnalités limite les informations qui peuvent être fournies.

> En fait, nous avons montré des situations dans lesquelles un statut incertain devait être renvoyé, fournissant presque aucune information sur le résultat de la transaction.

Bien que l'inclusion de la propriété d'insertion complique les choses, il est bénéfique d'utiliser la version plus faible de celle-ci.

> Enfin, nous listons un ensemble de fonctionnalités qui peuvent être combinées dans un IPCM fonctionnel :

> (1) Délais d'attente

> (2) Propriété d'insertion faible et transfert partiel

> (3) Processus tampon pour permettre

> (4) Ports bien connus — avec des méthodes appropriées pour traiter les transferts partiels vers eux.
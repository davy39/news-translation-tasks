---
title: Vous voulez apprendre comment fonctionne la réplication Viewstamped ? Lisez
  ce résumé.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-02T18:29:54.000Z'
originalURL: https://freecodecamp.org/news/viewstamped-replication-revisited-a-summary-144ac94bd16f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*88uNSrwWtrYWlRKqBJXBJg.png
tags:
- name: business
  slug: business
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Vous voulez apprendre comment fonctionne la réplication Viewstamped ? Lisez
  ce résumé.
seo_desc: 'By Shubheksha Jalan

  This article will distill the contents of the academic paper Viewstamped Replication
  Revisited by Barbara Liskov and James Cowling. All quotations are taken from that
  paper.

  It presents an updated explanation of Viewstamped Replic...'
---

Par Shubheksha Jalan

Cet article résumera le contenu du document académique [Viewstamped Replication Revisited](http://pmg.csail.mit.edu/papers/vr-revisited.pdf) de Barbara Liskov et James Cowling. Toutes les citations sont tirées de ce document.

Il présente une explication mise à jour de la réplication Viewstamped, une technique de réplication qui gère les pannes où les nœuds tombent en panne. Il décrit comment les requêtes des clients sont traitées, comment le groupe se réorganise lorsqu'une réplique tombe en panne, et comment une réplique défaillante peut rejoindre à nouveau le groupe.

#### Introduction

Le protocole de réplication Viewstamped, appelé VR, est utilisé pour les services répliqués qui s'exécutent sur de nombreux nœuds appelés répliques. VR utilise la réplication de machines d'état : il maintient l'état et le rend accessible aux clients qui consomment ce service.

Quelques caractéristiques de VR :

* VR est principalement un protocole de réplication, mais il fournit également un consensus.
* VR n'utilise aucune E/S disque — il utilise l'état répliqué pour la persistance.
* VR ne traite que les pannes par crash : un nœud fonctionne ou s'arrête complètement.
* VR fonctionne dans un réseau asynchrone comme Internet où rien ne peut être conclu sur un message qui n'arrive pas. Il peut être perdu, livré dans le désordre ou livré plusieurs fois.

#### Groupes de répliques

> VR assure la fiabilité et la disponibilité lorsque pas plus qu'un seuil de f répliques sont défaillantes. Il le fait en utilisant des groupes de répliques de taille 2f + 1 ; c'est le nombre minimal de répliques dans un réseau asynchrone sous le modèle de panne par crash.

Nous pouvons fournir une preuve simple pour l'énoncé ci-dessus : dans un système avec f nœuds en panne, nous avons besoin d'au moins la majorité de f+1 nœuds qui peuvent s'accorder mutuellement pour maintenir le système en fonctionnement.

Un groupe de f+1 répliques est souvent appelé un **quorum**. Le protocole a besoin que la propriété d'intersection de quorum soit vraie pour fonctionner correctement. Cette propriété stipule que :

> Le quorum de répliques qui traite une étape particulière du protocole doit avoir une intersection non vide avec le groupe de répliques disponibles pour traiter l'étape suivante, car de cette manière nous pouvons garantir qu'à chaque étape suivante, au moins un participant sait ce qui s'est passé à l'étape précédente.

#### Architecture :

![Image](https://cdn-media-1.freecodecamp.org/images/GR7HoMCke6z0hrNxDrQzsZIhg-L37RmU8yQW)
_Architecture VR_

L'architecture de VR est la suivante :

1. Le code utilisateur est exécuté sur les machines clientes au-dessus d'un proxy VR.
2. Le proxy communique avec les répliques pour effectuer les opérations demandées par le client. Il renvoie les résultats calculés des répliques au client.
3. Le code VR du côté des répliques accepte les requêtes des clients du proxy, exécute le protocole et exécute la requête en faisant un appel vers le haut au code de service.
4. Le code de service renvoie le résultat au code VR qui envoie à son tour un message au proxy client qui a demandé l'opération.

#### **Aperçu**

> Le défi pour le protocole de réplication est de garantir que les opérations s'exécutent dans le même ordre sur toutes les répliques malgré les requêtes concurrentes des clients et malgré les pannes.

Si toutes les répliques doivent se terminer dans le même état, il est important que la condition ci-dessus soit remplie.

VR traite les répliques comme suit :

**Primaire** : Décide l'ordre dans lequel les opérations seront exécutées

**Secondaire** : Exécute les opérations dans le même ordre que celui sélectionné par le primaire

**Que se passe-t-il si le primaire tombe en panne ?**

* VR permet à différentes répliques d'assumer le rôle de primaire si celui-ci tombe en panne au fil du temps.
* Le système passe par une série de **vues**. Dans chaque vue, une réplique assume le rôle de primaire.
* Les autres répliques surveillent le primaire. Si celui-ci semble défaillant, elles effectuent un **changement de vue** pour sélectionner un nouveau primaire.

Nous considérons les trois scénarios suivants du protocole VR :

* Traitement normal des requêtes utilisateur
* Changements de vue pour sélectionner un nouveau primaire
* Récupération d'une réplique défaillante afin qu'elle puisse rejoindre le groupe

#### Protocole VR

![Image](https://cdn-media-1.freecodecamp.org/images/rOLWLBb1gjHUCsMpDC7N2GW3T4aqJ6agWBFN)
_État de VR sur une réplique_

L'état maintenu par chaque réplique est présenté dans la figure ci-dessus. Quelques points à noter :

* L'identité du primaire n'est pas stockée mais calculée à l'aide du numéro de vue et de la configuration.
* La réplique avec la plus petite adresse IP est la réplique 1, et ainsi de suite.

Le proxy côté client maintient également un certain état :

* Il enregistre la configuration.
* Il enregistre le numéro de vue actuel pour suivre le primaire.
* Il possède un identifiant client et un numéro de requête client incrémentiel.

#### Fonctionnement normal

* Les répliques participent au traitement des requêtes clients uniquement lorsque leur statut est normal.
* Chaque message envoyé contient le numéro de vue de l'expéditeur. Les répliques ne traitent que les requêtes dont le numéro de vue correspond à ce qu'elles connaissent. Si la réplique expéditrice est en avance, elle abandonne le message. Si elle est en retard, elle effectue un transfert d'état.

![Image](https://cdn-media-1.freecodecamp.org/images/VM8lGwj4Qge04W1nK9TpDk2SImIcQ2k6V77P)
_Fonctionnement en mode normal_

Le fonctionnement normal de VR peut être décomposé en les étapes suivantes :

1. Le client envoie un message REQUEST au primaire lui demandant d'effectuer une **opération**, en lui passant le **client-id** et le **numéro de requête**.
2. Le primaire vérifie les informations présentes dans la table client. Si le numéro de requête est inférieur à celui présent dans la table, il le rejette. Il renvoie la réponse si la requête était celle exécutée le plus récemment.
3. Le primaire incrémente le **op-number**, ajoute la requête à son journal, et met à jour la table client avec le nouveau numéro de requête. Il envoie un message PREPARE aux répliques avec le numéro de vue actuel, le numéro d'opération, le message du client, et le **commit-number** (le numéro d'opération de l'opération la plus récemment validée).
4. Les répliques n'accepteront pas un message avec un **op-number** tant qu'elles n'ont pas toutes les opérations qui le précèdent. Elles utilisent le transfert d'état pour se mettre à jour si nécessaire. Ensuite, elles ajoutent l'opération à leur journal, mettent à jour la table client, et envoient un message PREPAREOK au primaire. Ce message indique que l'opération, y compris toutes celles qui la précèdent, a été préparée avec succès.
5. Le primaire attend une réponse de _f_ répliques avant de valider l'opération. Il incrémente le **commit-number**. Après s'être assuré que toutes les opérations précédant celle en cours ont été exécutées, il fait un appel vers le haut au code de service pour exécuter l'opération en cours. Un message REPLY est envoyé au client contenant le numéro de vue, le numéro de requête, et le résultat de l'appel vers le haut.

Habituellement, le message PREPARE est utilisé pour informer les répliques de secours des opérations validées. Il peut également le faire en envoyant un message COMMIT.

Pour exécuter une requête, une réplique de secours doit s'assurer que l'opération est présente dans son journal et que toutes les opérations précédentes ont été exécutées. Ensuite, elle exécute ladite opération, incrémente son **commit-number**, et met à jour l'entrée du client dans la table client. Mais elle n'envoie pas de réponse au client, car le primaire l'a déjà fait.

> Si un client ne reçoit pas de réponse en temps opportun à une requête, il renvoie la requête à toutes les répliques. De cette manière, si le groupe est passé à une vue ultérieure, son message atteindra le nouveau primaire. Les répliques de secours ignorent les requêtes des clients ; seul le primaire les traite.

#### Opération de changement de vue

> Les répliques de secours surveillent le primaire : elles s'attendent à recevoir régulièrement des nouvelles de celui-ci. Normalement, le primaire envoie des messages PREPARE, mais s'il est inactif (en raison de l'absence de requêtes), il envoie des messages COMMIT à la place. Si un délai d'attente expire sans communication du primaire, les répliques effectuent un changement de vue pour passer à un nouveau primaire.

Il n'y a pas d'élection de leader dans ce protocole. Le primaire est sélectionné de manière cyclique. Chaque membre possède une adresse IP unique. Le prochain primaire est la réplique de secours avec la plus petite adresse IP qui fonctionne. Chaque numéro dans le groupe sait déjà qui est censé être le prochain primaire.

Chaque opération exécutée sur les répliques doit survivre au changement de vue dans l'ordre spécifié lors de son exécution. L'appel vers le haut est effectué sur le primaire uniquement après qu'il a reçu _f_ messages PREPAREOK. Ainsi, l'opération a été enregistrée dans les journaux d'au moins f+1 répliques (l'ancien primaire et f répliques).

> Par conséquent, le protocole de changement de vue obtient des informations à partir des journaux d'au moins f + 1 répliques. Cela est suffisant pour garantir que toutes les opérations validées seront connues, puisque chacune doit être enregistrée dans au moins l'un de ces journaux ; ici, nous nous appuyons sur la propriété d'intersection de quorum. Les opérations qui n'avaient pas été validées pourraient également survivre, mais ce n'est pas un problème : il est bénéfique d'avoir autant d'opérations survivre que possible.

1. Une réplique qui remarque le besoin d'un changement de vue avance son **view-number**, définit son statut sur **view-change**, et envoie un message START-VIEW-CHANGE. Une réplique identifie le besoin d'un changement de vue en fonction de son propre temporisateur, ou parce qu'elle reçoit un START-VIEW-CHANGE ou un DO-VIEW-CHANGE d'autres répliques avec un **view-number** plus élevé que le sien.
2. Lorsqu'une réplique reçoit _f_ messages START-VIEW-CHANGE pour son view-number, elle envoie un DO-VIEW-CHANGE au nœud censé être le primaire. Les messages contiennent l'état de la réplique : le journal, le numéro d'opération le plus récent et le commit-number, et le numéro de la dernière vue dans laquelle son statut était normal.
3. Le nouveau primaire attend de recevoir f+1 messages DO-VIEW-CHANGE des répliques (y compris lui-même). Ensuite, il met à jour son état avec le plus récent en fonction des informations des répliques (voir le document pour toutes les règles). Il définit son numéro comme le **view-number** dans les messages, et change son **status** en normal. Il informe toutes les autres répliques en envoyant un message STARTVIEW avec l'état le plus récent, y compris le nouveau journal, le **commit-number** et le **op-number**.
4. Le primaire peut maintenant accepter les requêtes des clients. Il exécute toutes les opérations validées et envoie les réponses aux clients.
5. Lorsque les répliques reçoivent un message STARTVIEW, elles mettent à jour leur état en fonction du message. Elles envoient des messages PREPAREOK pour toutes les opérations non validées présentes dans leur journal après la mise à jour. Elles exécutent ces opérations pour être synchronisées avec le primaire.

Pour rendre l'opération de changement de vue plus efficace, le document décrit l'approche suivante :

> Le protocole décrit a un petit nombre d'étapes, mais de grands messages. Nous pouvons rendre ces messages plus petits, mais si nous le faisons, il y a toujours une chance que plus de messages soient nécessaires. Une manière raisonnable d'obtenir un bon comportement la plupart du temps est que les répliques incluent un suffixe de leur journal dans leurs messages DO-VIEW-CHANGE. La quantité envoyée peut être petite puisque le cas le plus probable est que le nouveau primaire est à jour. Par conséquent, l'envoi de la dernière entrée du journal, ou peut-être des deux dernières entrées, devrait être suffisant. Occasionnellement, ces informations ne seront pas suffisantes ; dans ce cas, le primaire peut demander plus d'informations, et il pourrait même avoir besoin d'utiliser d'abord l'état de l'application pour se mettre à jour.

#### Récupération

> Lorsqu'une réplique se rétablit après une panne, elle ne peut pas participer au traitement des requêtes et aux changements de vue tant qu'elle n'a pas un état au moins aussi récent que lorsqu'elle est tombée en panne. Si elle pouvait participer plus tôt, le système peut échouer.

La réplique ne doit pas « oublier » ce qu'elle a déjà fait. Une façon de garantir cela est de persister l'état sur disque — mais cela ralentira tout le système. Cela n'est pas nécessaire dans VR car l'état est persistant sur d'autres répliques. Il peut être obtenu en utilisant un protocole de récupération à condition que les répliques soient indépendantes des pannes.

> Lorsqu'un nœud redémarre après une panne, il définit son statut sur récupération et exécute le protocole de récupération. Tant que le statut d'une réplique est en récupération, elle ne participe ni au protocole de traitement des requêtes ni au protocole de changement de vue.

Le protocole de récupération est le suivant :

1. La réplique en récupération envoie un message RECOVERY à toutes les autres répliques avec un nonce.
2. Seule si le statut de la réplique est normal, elle répond à la réplique en récupération avec un message RECOVERY-RESPONSE. Ce message contient son numéro de vue et le nonce qu'elle a reçu. Si c'est le primaire, il envoie également son journal, son op-number et son commit-number.
3. Lorsque la réplique a reçu f+1 messages RECOVERY-RESPONSE, y compris un du primaire, elle met à jour son état et change son statut en normal.

> Le protocole utilise le nonce pour garantir que la réplique en récupération n'accepte que les messages RECOVERY-RESPONSE qui sont pour cette récupération et non pour une précédente.

#### Reconfiguration

La reconfiguration traite des époques. L'époque représente le groupe de répliques traitant les requêtes des clients. Si le seuil de pannes, f, est ajusté, le système peut soit ajouter soit supprimer des répliques et passer à une nouvelle époque. Il suit les époques à travers le **epoch-number**.

Un autre statut, à savoir transitioning, est utilisé pour signifier qu'un système passe d'une époque à une autre.

> L'approche pour gérer la reconfiguration est la suivante. Une reconfiguration est déclenchée par une requête client spéciale. Cette requête est exécutée via le protocole de cas normal par l'ancien groupe. Lorsque la requête est validée, le système passe à une nouvelle époque, dans laquelle la responsabilité du traitement des requêtes des clients passe au nouveau groupe. Cependant, le nouveau groupe ne peut pas traiter les requêtes des clients tant que ses répliques ne sont pas à jour : les nouvelles répliques doivent connaître toutes les opérations validées dans l'époque précédente. Pour se mettre à jour, elles transfèrent l'état des anciennes répliques, qui ne s'arrêtent pas tant que le transfert d'état n'est pas terminé.

Les sous-protocoles VR doivent être modifiés pour gérer les époques. Une réplique n'accepte pas les messages d'une époque plus ancienne par rapport à ce qu'elle connaît, comme ceux avec un **epoch-number** plus ancien. Elle informe l'expéditeur de la nouvelle époque.

Lors d'un changement de vue, le primaire ne peut pas accepter les requêtes des clients lorsque le système est en transition entre les époques. Il le fait en vérifiant si la requête la plus haute dans son journal est une requête de RECONFIGURATION. Une réplique en récupération dans une époque plus ancienne est informée de l'époque si elle fait partie de la nouvelle époque ou si elle s'arrête.

Le problème qui vient à l'esprit est que les requêtes des clients ne peuvent pas être servies pendant que le système passe à une nouvelle époque.

> L'ancien groupe cesse d'accepter les requêtes des clients dès que le primaire de l'ancien groupe reçoit la requête de RECONFIGURATION ; le nouveau groupe ne peut commencer à traiter les requêtes des clients que lorsque au moins f + 1 nouvelles répliques ont terminé le transfert d'état.

Cela peut être traité en « préchauffant » les nœuds avant que la reconfiguration ne se produise. Les nœuds peuvent être mis à jour en utilisant le transfert d'état pendant que l'ancien groupe continue à répondre aux requêtes des clients. Cela réduit le délai causé pendant la reconfiguration.

Ce document a présenté une version améliorée de la réplication Viewstamped, un protocole utilisé pour construire des systèmes répliqués capables de tolérer les pannes par crash. Le protocole ne nécessite aucune écriture sur disque lors du traitement des requêtes des clients ou même lors des changements de vue, tout en permettant aux nœuds de se rétablir après des pannes et de rejoindre le groupe.

Le document présente également un protocole permettant des reconfigurations qui modifient les membres du groupe de répliques, et même le seuil de panne. Une technique de reconfiguration est nécessaire pour que le protocole soit déployé en pratique, car les systèmes concernés sont généralement de longue durée.

Si vous avez aimé cet essai, veuillez appuyer sur le bouton d'applaudissements pour que plus de personnes le voient. Merci !

P.S. — Si vous êtes arrivé jusqu'ici et que vous souhaitez recevoir un courrier chaque fois que je publie l'un de ces articles, inscrivez-vous [ici](http://eepurl.com/dcHGFP).
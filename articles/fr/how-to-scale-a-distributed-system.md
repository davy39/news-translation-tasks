---
title: Comment mettre à l'échelle un système distribué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-13T23:37:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-scale-a-distributed-system
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/photo-1515378960530-7c0da6231fb1-1.png
tags:
- name: database
  slug: database
- name: distributed systems
  slug: distributed-systems
- name: scalability
  slug: scalability
- name: scaling
  slug: scaling
seo_title: Comment mettre à l'échelle un système distribué
seo_desc: "By Apoorv Tyagi\nDesigning a distributed system that supports millions\
  \ of users is a complex task, and one that requires continuous improvement and refinement.\
  \ \nRecently I read a book by Alex Xu called \"System Design Interview – An Insider's\
  \ Guide\". T..."
---

Par Apoorv Tyagi

Concevoir un système distribué qui supporte des millions d'utilisateurs est une tâche complexe, et qui nécessite une amélioration et un affinage continus. 

Récemment, j'ai lu un livre d'Alex Xu intitulé "_System Design Interview – An Insider's Guide_" (en anglais). Cet article, inspiré de la première partie du livre, partage quelques techniques populaires utilisées par de nombreuses grandes entreprises technologiques pour mettre à l'échelle leur architecture afin de supporter jusqu'à un million d'utilisateurs.

Ce n'est pas une liste exhaustive, mais si vous êtes un développeur débutant qui commence tout juste, cela peut vous aider à construire une base plus solide pour votre carrière.

## **Utiliser un **Équilibreur** de **Charge****

Un équilibreur de charge est un dispositif qui répartit uniformément le trafic réseau sur plusieurs serveurs web. Dans cette architecture, les clients ne se connectent pas directement aux serveurs – ils se connectent plutôt à l'adresse IP publique de l'équilibreur de charge. 

L'utilisation d'un équilibreur de charge protège également votre site en cas de défaillance d'un serveur web – et cela améliore ainsi la disponibilité. Par exemple,

* Si un serveur tombe en panne, tout le trafic peut être redirigé vers le deuxième serveur. Cela empêche le système global de tomber hors ligne.
* Si, à l'avenir, le trafic augmente et que ces deux serveurs ne suffisent plus à gérer toutes les requêtes correctement, il vous suffit d'ajouter plus de serveurs à votre groupe de serveurs web et l'équilibreur de charge commence automatiquement à distribuer les requêtes vers eux.

### Algorithmes d'équilibrage de charge

Examinons quelques-uns des algorithmes qu'un équilibreur de charge peut utiliser pour choisir un serveur web dans un groupe pour une requête entrante :

* **Round Robin** – Vous commencez par le premier serveur du groupe, passez au serveur suivant, et lorsque vous avez terminé avec le dernier serveur, vous revenez au premier et recommencez à parcourir le groupe.
* **Serveur basé sur la charge** – Vous attribuez un serveur en fonction de celui qui a la charge la plus faible actuellement, augmentant ainsi le débit.
* **Hachage IP** – Vous attribuez un serveur en hachant l'adresse IP des requêtes entrantes et en utilisant la valeur de hachage pour effectuer l'opération modulo avec le nombre de serveurs disponibles dans le groupe de serveurs.

## **Utiliser la **Mise en **Cache**

Un cache stocke le résultat des réponses précédentes afin que toute requête ultérieure pour les mêmes données puisse être servie plus rapidement. Vous pouvez donc utiliser la mise en cache pour minimiser la latence réseau d'un système.

Vous pouvez améliorer considérablement les performances d'une application en réduisant les appels réseau à la base de données. Cela est dû au fait que les appels répétés à la base de données sont coûteux et prennent du temps. 

Par exemple, chaque fois qu'un nouvel utilisateur charge la page d'accueil d'un site web, un ou plusieurs appels à la base de données sont effectués pour récupérer les données. Cela augmente le temps de réponse. La mise en cache peut atténuer ce problème en stockant les résultats que vous savez être souvent appelés et ceux dont les résultats sont modifiés rarement.

Voici quelques considérations à garder à l'esprit avant d'utiliser un cache :

* **Définir une politique d'expiration** : Vous devez toujours avoir une politique d'expiration pour votre cache. Si vous n'en avez pas, les données seront stockées dans le cache de manière permanente et deviendront obsolètes.
* **Synchroniser le cache et la base de données** : Vous devez construire un mécanisme pour maintenir la synchronisation entre la base de données et le cache. Si des opérations de modification de données se produisent dans les bases de données et que le même changement ne se reflète pas dans le cache, cela introduira des incohérences dans votre système. 
* **Définir une politique d'éviction** : Vous devez avoir un algorithme qui peut décider quels éléments existants seront supprimés une fois le cache plein et que vous recevez une demande pour ajouter d'autres éléments au cache. Least-recently-used (LRU) est l'une des politiques d'éviction de cache les plus populaires utilisées aujourd'hui.

## **Utiliser un **Réseau** de **Livraison** de **Contenu (CDN)****

Un CDN ou Content Delivery Network est un réseau de serveurs géographiquement distribués qui aident à améliorer la livraison de contenu statique d'un point de vue performance. Les serveurs CDN sont généralement utilisés pour mettre en cache du contenu comme des images, des fichiers CSS et JavaScript.

Voici comment fonctionne un CDN :

* Lorsqu'un client envoie une requête, un serveur CDN envoie au client tout le contenu statique lié à la requête.
* Si le serveur CDN ne dispose pas du fichier requis, il envoie alors une requête au serveur web d'origine.
* Le CDN met en cache le fichier et le retourne au client.
* Supposons qu'un autre client envoie la même requête, alors le fichier est retourné depuis le CDN.

Voici quelques considérations à garder à l'esprit avant d'utiliser un CDN :

* **Coût** : Les CDN sont généralement gérés par des fournisseurs tiers et ils vous facturent pour les transferts de données entrants et sortants du CDN. Ainsi, la mise en cache d'actifs rarement utilisés ne doit pas être stockée dans le CDN.
* **Mécanisme de secours** : Si un CDN tombe en panne, vous devez être en mesure de le détecter et de commencer à envoyer des requêtes pour des ressources depuis le serveur web d'origine. Vous devez donc construire un mécanisme pour que votre application fasse face à une défaillance du CDN.

## **Configurer une **File** d'**Attente** de **Messages****

Une file d'attente de messages permet une forme de communication asynchrone. Elle agit comme un tampon pour les messages qui sont stockés dans la file d'attente jusqu'à ce qu'ils soient traités.

L'architecture d'une file d'attente de messages comprend un service d'entrée, appelé éditeurs, qui crée des messages, les publie dans une file d'attente de messages et envoie un événement. Un autre service appelé abonnés reçoit ces événements et effectue des actions définies par les messages.

Les éditeurs et les abonnés sont découplés les uns des autres et c'est ce qui fait de la file d'attente de messages une architecture privilégiée pour construire des applications scalables.

### Exemple de file d'attente de messages

Considérons le cas d'utilisation suivant :

Vous construisez une application pour la réservation de billets. Dès qu'un utilisateur termine sa réservation, un message confirmant son paiement et son billet doit être déclenché. Cette tâche peut prendre un certain temps à compléter et ne doit pas faire attendre notre système pour le traitement de la prochaine requête.

Ici, nous pouvons pousser les détails du message ainsi que d'autres métadonnées comme le numéro de téléphone de l'utilisateur vers la file d'attente de messages. Un autre service worker récupère les tâches de la file d'attente de messages et effectue de manière asynchrone les tâches de création et d'envoi du message.

Les éditeurs et les abonnés peuvent être mis à l'échelle indépendamment. Lorsque la taille de la file d'attente augmente, vous pouvez ajouter plus de consommateurs pour réduire le temps de traitement.

## **Choisir sa **Base** de **Données** avec soin**

Selon [Wikipedia](https://en.wikipedia.org/wiki/Database) :

> Une base de données est une collection organisée de données stockées et accessibles via un système informatique. 

Les bases de données sont utilisées pour le stockage persistant des données. Nous avons généralement deux types de bases de données, relationnelles et non relationnelles.

###  2794 Base de données relationnelle

Une base de données relationnelle a des relations strictes entre les entrées stockées dans la base de données et elles sont hautement structurées. Cela est fait pour assurer l'intégrité des données. Par exemple, l'ajout d'un nouveau champ à la table lorsque son schéma ne le permet pas générera une erreur.

Une autre caractéristique importante des bases de données relationnelles est les transactions ACID.

#### Transactions ACID

Ce sont un ensemble de caractéristiques qui décrivent toute transaction donnée (un ensemble d'opérations de lecture ou d'écriture) qu'une bonne base de données relationnelle devrait supporter.

**Atomicité** signifie que lorsqu'une transaction qui comprend plus d'une opération a lieu, la base de données doit garantir que si une opération échoue, l'ensemble de la transaction échoue. Soit elle se produit complètement, soit elle ne se produit pas du tout.

**Cohérence** signifie que chaque transaction dans une base de données ne viole pas les contraintes d'intégrité des données chaque fois que la base de données change d'état et ne corrompt pas les données. En termes simples, la cohérence signifie que pour chaque opération de "lecture", vous recevrez les résultats de l'opération d'"écriture" la plus récente.

**Isolation** signifie que vous pouvez exécuter plusieurs transactions concurrentes sur une base de données, sans entraîner aucun type d'incohérence. Toutes ces transactions multiples se produiront indépendamment les unes des autres.

**Durabilité** signifie que une fois la transaction exécutée, les données mises à jour restent stockées dans la base de données. Elles seront sauvegardées sur un disque et seront persistantes même en cas de défaillance du système.

###  2794 Bases de données non relationnelles

Une base de données non relationnelle a une structure moins rigide et peut ou non avoir des relations strictes entre les entrées stockées dans la base de données. Les données sont généralement stockées sous forme de paires clé-valeur. Par exemple :

```
[
    { 
        firstName: "Apoorv",
        lastName: "Tyagi",
        gender: "M"
    },
    { 
        name: "Judit",
        rank: "Polgar",
        gender: "F"
    },
    {
      //...
    },
]

```

Similaire aux propriétés ACID des bases de données relationnelles, la base de données non relationnelle offre des propriétés BASE :

**Disponibilité de base (BA)** qui stipule que le système garantit la disponibilité même en présence de plusieurs défaillances. 

**État souple (S)** signifie que l'état du système peut changer au fil du temps, même sans interaction de l'application en raison de la cohérence éventuelle. Dans NoSQL, contrairement aux SGBDR, on pense que la cohérence des données est de la responsabilité du développeur et ne doit pas être gérée par la base de données.

**Cohérence éventuelle (E)** signifie que le système deviendra cohérent "éventuellement". Cependant, il n'y a aucune garantie quant au moment où cela se produira.

### NoSQL vs SQL

Les bases de données non relationnelles (souvent appelées bases de données NoSQL) peuvent être un meilleur choix si :

* Votre application nécessite une faible latence. Puisqu'il n'y a pas de requêtes JOIN complexes.
* Vous avez une grande quantité de données non structurées, ou vous n'avez aucune relation entre vos données.

## Comment mettre à l'échelle une base de données 

Examinons maintenant les différentes façons de mettre à l'échelle votre base de données :

### Mise à l'échelle verticale vs horizontale de la base de données

Dans la mise à l'échelle verticale, vous mettez à l'échelle en ajoutant plus de puissance (CPU, RAM) à un seul serveur.

Dans la mise à l'échelle horizontale, vous mettez à l'échelle simplement en ajoutant plus de serveurs à votre groupe de serveurs.

Pour les applications à faible échelle, la mise à l'échelle verticale est une excellente option en raison de sa simplicité. Mais la mise à l'échelle verticale a une limite stricte. Il n'est pratiquement pas possible d'ajouter une RAM, un CPU et une mémoire illimités à un seul serveur. 

Pour cette raison, il est recommandé d'opter pour la mise à l'échelle horizontale (également connue sous le nom de sharding) pour les applications à grande échelle.

### Réplication de la base de données

Il s'agit du processus de copie de données de votre base de données centrale vers une ou plusieurs bases de données.

Vous effectuez la réplication de la base de données en utilisant l'architecture primaire-réplica (anciennement connue sous le nom de maître-esclave). La base de données primaire prend généralement en charge uniquement les opérations d'écriture. Toutes les opérations de modification de données comme l'insertion ou la mise à jour seront envoyées à la base de données primaire.

D'autre part, les bases de données réplicas obtiennent des copies des données de la base de données primaire et ne prennent en charge que les opérations de lecture. Toutes les opérations de requête de données comme la lecture, la récupération seront servies par les bases de données réplicas.

Avantages de la réplication de la base de données :

* **Améliorations des performances** : La réplication de la base de données améliore considérablement les performances, car toutes les écritures et mises à jour se produisent dans le nœud principal et toutes les opérations de lecture sont distribuées aux nœuds réplicas, permettant ainsi à plus de requêtes de s'exécuter en parallèle.
* **Haute disponibilité** : Puisque nous créons des réplicas de données sur différents nœuds disponibles dans différentes parties du monde, l'application reste fonctionnelle même si un nœud de base de données tombe hors ligne, car vous pouvez accéder aux données depuis d'autres nœuds. En cas de défaillance du nœud principal, l'un des nœuds réplicas sera promu nœud principal et servira les opérations d'écriture/mise à jour jusqu'à ce que le nœud principal d'origine revienne en ligne.

## Conclusion

C'est tout. Merci d'être passé par ici. J'espère que vous avez trouvé cet article intéressant et informatif !

Mes messages directs sont toujours ouverts si vous souhaitez discuter davantage de tout sujet technique ou si vous avez des questions, des suggestions ou des commentaires en général :

* [Twitter](https://twitter.com/apoorv__tyagi)
* [LinkedIn](https://www.linkedin.com/in/apoorvtyagi/)
* [GitHub](https://github.com/apoorvtyagi)
* [Blog](https://apoorvtyagi.tech/)

Bonne apprentissage ! 📛 😄
---
title: Apprendre Kubernetes – Guide complet pour les développeurs, les startups et
  les entreprises
subtitle: ''
author: Prince Onukwili
co_authors: []
series: null
date: '2025-05-02T17:34:12.079Z'
originalURL: https://freecodecamp.org/news/learn-kubernetes-handbook-devs-startups-businesses
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746205417767/d9d6b0d3-f2a5-44eb-83b5-d1a614bead9f.png
tags:
- name: Kubernetes
  slug: kubernetes
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Devops
  slug: devops
- name: Cloud
  slug: cloud
- name: Cloud Computing
  slug: cloud-computing
seo_title: Apprendre Kubernetes – Guide complet pour les développeurs, les startups
  et les entreprises
seo_desc: You’ve probably heard the word Kubernetes floating around, or it’s cooler
  nickname k8s (pronounced “kates“). Maybe in a job post, a tech podcast, or from
  that one DevOps friend who always brings it up like it’s the secret sauce to everything
  😅. It s...
---

Vous avez probablement entendu le mot Kubernetes circuler, ou son surnom plus cool k8s (prononcé "kates"). Peut-être dans une offre d'emploi, un podcast tech, ou de la part de cet ami DevOps qui en parle toujours comme si c'était la solution secrète à tout 😅. Cela semble important, mais aussi... un peu mystérieux.

Alors, qu'est-ce que Kubernetes, vraiment ? Pourquoi est-il partout ? Et devriez-vous vous en soucier ?

Dans ce guide, nous allons décomposer Kubernetes de manière à ce que cela ait réellement du sens. Pas de jargon. Pas de discours technique écrasant. Juste des explications claires. Vous apprendrez ce qu'est Kubernetes, comment il est apparu, et pourquoi il est devenu si important – surtout pour les équipes qui construisent et exécutent des applications massives avec des millions d'utilisateurs.

Nous allons revenir un peu en arrière pour voir comment les choses étaient faites avant l'arrivée de Kubernetes (spoiler : ce n'était pas joli), et nous allons passer en revue les vrais problèmes qu'il a été conçu pour résoudre.

À la fin, vous comprendrez non seulement le but de Kubernetes, mais vous saurez également comment déployer une application simple sur un cluster Kubernetes – même si vous débutez.

Oui, d'ici la fin, vous passerez de *« J'entends toujours parler de Kubernetes »* à *« Hé, je commence à comprendre maintenant ! »* 😄

## 📜 Table des matières

1. [Qu'est-ce que Kubernetes ?](#heading-quest-ce-que-kubernetes)

2. [Comment les applications étaient déployées avant Kubernetes](#heading-comment-les-applications-etaient-deployees-avant-kubernetes)

3. [Le problème que Kubernetes résout 🦸](#heading-le-probleme-que-kubernetes-resout)

4. [Comment Kubernetes fonctionne – Composants d'un environnement Kubernetes 👨‍💻](#heading-comment-kubernetes-fonctionne-composants-dun-environnement-kubernetes)

5. [Charges de travail Kubernetes 🏢 – Pods, Déploiements, Services, & Plus](#heading-charges-de-travail-kubernetes-pods-deploiements-services-amp-plus)

6. [Comment créer un cluster Kubernetes dans un environnement de démonstration avec play-with-k8s](#heading-comment-creer-un-cluster-kubernetes-dans-un-environnement-de-demonstration-avec-play-with-k8s)

   * [Se connecter à Play with Kubernetes](#heading-se-connecter-a-play-with-kubernetes)

   * [Créer votre cluster Kubernetes](#heading-creer-votre-cluster-kubernetes)

7. [Comment déployer une application sur votre cluster Kubernetes](#heading-comment-deployer-votre-application-sur-un-cluster-kubernetes)

8. [✅ Avantages de l'utilisation de Kubernetes en entreprise](#heading-avantages-de-lutilisation-de-kubernetes-en-entreprise)

9. [😬 Inconvénients de l'utilisation de Kubernetes](#heading-inconvenients-de-lutilisation-de-kubernetes)

10. [Cas d'utilisation : Quand (et quand ne pas) utiliser Kubernetes](#heading-cas-dutilisation-quand-et-quand-ne-pas-utiliser-kubernetes)

11. [Conclusion](#heading-conclusion)

12. [Étudier plus loin 📚](#heading-etudier-plus-loin)

13. [À propos de l'auteur 👨‍💻](#heading-a-propos-de-lauteur)

## **Qu'est-ce que Kubernetes ?**

Imaginez que vous construisez une énorme plateforme logicielle, comme une application bancaire. Cette application a besoin de nombreuses fonctionnalités, comme l'inscription des utilisateurs, les dépôts d'argent, les retraits, les paiements, et ainsi de suite. Ces fonctionnalités sont si grandes et complexes qu'il est plus facile de les diviser en applications séparées. Ces applications individuelles sont appelées microservices.

**Alors, que sont les Microservices** ? Pensez à eux comme à de petits blocs de construction qui travaillent ensemble pour créer une plateforme plus grande. Ainsi, vous pourriez avoir :

* Un microservice pour l'inscription des utilisateurs

* Un autre pour le traitement des dépôts

* Un autre pour la gestion des paiements

* Et bien d'autres encore !

Pour l'utilisateur, cela ressemble toujours à une application bancaire fluide et unifiée. Mais en coulisses, c'est comme un ensemble de petites applications qui travaillent ensemble pour que tout fonctionne.

### Mais voici où les choses se compliquent...

Lorsque vous avez des dizaines (voire des centaines) de ces microservices, les gérer devient un cauchemar. Vous pourriez avoir besoin de :

* **Déployer** chacun séparément

* **Les surveiller** individuellement (pour vous assurer qu'ils ne plantent pas/ne deviennent pas lents en raison d'une charge trop importante)

* **Les mettre à l'échelle** (les rendre plus grands pour gérer plus d'utilisateurs) lorsque le trafic augmente, un par un

Ainsi, si votre application bancaire reçoit soudainement des millions d'utilisateurs, vous devriez ajuster et mettre à jour manuellement chaque microservice pour qu'il continue à fonctionner sans problème. 😖 C'est beaucoup de travail, et si quelque chose ne va pas, vous êtes dans de beaux draps.

### C'est là que Kubernetes vient à la rescousse ! 🚀

Kubernetes est comme un manager super-efficace pour tous ces microservices. C'est une plateforme qui vous aide à :

* **Automatiser** le déploiement (mettre les applications en route)

* **Mettre à l'échelle** les microservices (les rendre plus grands ou plus petits selon les besoins en fonction de l'afflux de trafic – vos clients)

* **Les surveiller** (garder un œil sur leur santé)

* **Assurer la fiabilité** (ainsi, si un microservice tombe en panne/échoue, k8s le remplace immédiatement)

En termes simples, Kubernetes prend tous vos petits microservices et les organise, en s'assurant qu'ils fonctionnent bien ensemble, peu importe la quantité de trafic que votre application reçoit. Il gère tout en coulisses, comme un chef d'orchestre dirigeant un orchestre, afin que vos microservices travaillent ensemble sans chaos.

## **Comment les applications étaient déployées avant Kubernetes**

Avant l'arrivée de Kubernetes, les équipes logicielles avaient un véritable numéro d'équilibriste lorsqu'il s'agissait de déployer des applications – surtout lorsqu'elles étaient composées de nombreux microservices.

Une méthode populaire consistait à utiliser une configuration de **système distribué**. Voici à quoi cela ressemblait :

Imaginez que chaque microservice (comme votre inscription d'utilisateurs, vos paiements, vos dépôts, etc.) est installé sur des serveurs séparés (ordinateurs physiques ou machines virtuelles). Chacun de ces serveurs devait être soigneusement préparé :

* Le microservice lui-même devait être installé.

* Les dépendances logicielles dont il avait besoin (comme les langages de programmation, les bibliothèques, les outils) devaient également être installées.

* Tout devait être configuré manuellement SUR CHAQUE serveur.

Et tous ces serveurs devaient communiquer entre eux – parfois via l'internet public, ou via des réseaux privés comme les VPN.

Cela semble être beaucoup de travail, n'est-ce pas ? 😮 C'était le cas ! Gérer les mises à jour, corriger les bugs, mettre à l'échelle pendant les pics de trafic et éviter les plantages pouvait devenir un casse-tête à temps plein pour les développeurs et les administrateurs système. 😖

### Puis vinrent les conteneurs 🚂

Une solution plus moderne qui a atténué la douleur (un peu) était l'utilisation de conteneurs.

**Alors, que sont les conteneurs ?**

Pensez à un conteneur comme à une boîte à lunch pour votre microservice. Au lieu d'installer le microservice et ses outils de support directement sur un serveur, vous emballez tout ce dont il a besoin – code, paramètres, bibliothèques logicielles – dans ce seul et même conteneur bien rangé. Où que le conteneur aille, le microservice s'exécute exactement de la même manière. Pas de surprises !

Des outils comme [Docker](https://www.docker.com/) ont rendu cela super facile. Une fois votre microservice emballé dans un conteneur, vous pouviez le déployer sur :

* Un seul serveur

* Plusieurs serveurs

* Ou des plateformes cloud comme AWS Elastic Beanstalk, Azure App Service, ou Google Cloud Run.

## **Le problème que Kubernetes résout** 🦸

Au début, lorsque les conteneurs sont arrivés sur le marché, cela semblait comme si les développeurs avaient trouvé l'or.

Vous pouviez emballer un microservice dans un petit conteneur bien rangé et l'exécuter n'importe où – plus besoin d'installer le même logiciel sur chaque serveur encore et encore. Des outils comme Docker et Docker Compose ont rendu cela fluide pour les petits projets.

Mais le monde réel ? C'est là que cela devient compliqué.

### La gestion croissante des conteneurs devient un casse-tête 🤒

Lorsque vous n'avez que quelques microservices, vous pouvez déployer et gérer manuellement leurs conteneurs sans trop de stress. Mais lorsque votre application grandit – et que vous avez soudainement des dizaines ou même des centaines de microservices – les gérer devient une bataille difficile :

* Vous deviez déployer chaque conteneur manuellement.

* Vous deviez les redémarrer si l'un d'eux plantait.

* Vous deviez les mettre à l'échelle un par un lorsque plus d'utilisateurs commençaient à affluer.

Docker et Docker Compose étaient excellents pour un petit terrain de jeu ou des startups, mais pas pour une application d'entreprise avec un trafic élevé.

### Les services cloud gérés ont aidé... mais seulement jusqu'à un certain point 👨‍💻

Les services cloud comme AWS Elastic Beanstalk, Azure App Service et Google Code Engine offraient un raccourci. Ils vous permettaient de déployer des conteneurs sans vous soucier de la configuration des serveurs.

Vous pouviez :

* Déployer chaque conteneur sur sa propre instance cloud gérée.

* Les mettre à l'échelle automatiquement en fonction du trafic.

MAIS il y avait encore quelques gros casse-têtes :

#### 📧 Regrouper les microservices était maladroit et coûteux

Bien sûr, vous pouviez organiser les conteneurs par environnement (comme "test" ou "production") ou même par équipe (comme "Finance" ou "RH"). Mais chaque nouveau microservice avait généralement besoin de sa propre instance cloud – par exemple, un service Azure App Service ou un environnement Elastic Beanstalk séparé POUR CHAQUE CONTENAIR.

Imaginez ceci :

* Chaque instance App Service coûte ~50 $ par mois.

* Vous avez 10 microservices.

* Cela fait 500 $/mois... même s'ils sont à peine utilisés. 💸 Yikes !

### Kubernetes : Plus intelligent, plus léger et plus flexible 🚀

Avec Kubernetes, vous n'avez pas besoin de lancer un serveur séparé pour chaque microservice. Vous pouvez commencer avec seulement un ou deux serveurs (VM) – et Kubernetes décidera automatiquement quel conteneur va où en fonction de l'espace et des ressources disponibles.

Pas de stress, pas de gaspillage ! 🤒

### 👨‍🍳 **Kubernetes vous permet de tout personnaliser**

1. Vous pouvez attribuer des ressources à chaque conteneur de microservice. 
   
   👉 Exemple : Si vous avez un microservice "Paiement" léger, vous pourriez lui donner 0,5 vCPU et 512 Mo de mémoire. Si vous avez un microservice "Analyse de données" gourmand en ressources, vous pourriez lui donner 2 vCPU et 4 Go de mémoire.
   
2. Vous pouvez définir un nombre minimum d'instances pour chaque microservice. 
   
   👉 Exemple : Si vous voulez au moins 2 copies de votre service "Connexion" toujours en cours d'exécution (pour que votre application ne tombe pas en panne si l'une échoue), Kubernetes s'assure que vous avez toujours 2 copies en direct à tout moment.
   
3. Vous pouvez regrouper vos conteneurs comme vous le souhaitez : 
   
   👉 Par équipes (Finance, RH, DevOps) ou par environnements (Test, Staging, Production). Kubernetes rend ce regroupement super propre et logique.
   
4. Vous pouvez mettre à l'échelle automatiquement des conteneurs individuels. 
   
   👉 Lorsque plus d'utilisateurs inondent votre application, Kubernetes peut créer des copies supplémentaires (appelées "réplicas") uniquement des conteneurs qui sont sous pression. Plus de gaspillage de ressources sur des conteneurs qui n'en ont pas besoin.
   
5. Vous pouvez même mettre à l'échelle vos serveurs ! 
   
   👉 Kubernetes peut automatiquement augmenter le nombre de serveurs (VM) dans votre environnement – appelé un **Cluster** – lorsque le trafic augmente. Vous pourriez commencer avec 2 VM à 30 $ chacune (60 $/mois) et laisser Kubernetes ajouter plus de serveurs uniquement lorsque nécessaire, plutôt que de vous engager dans des coûts fixes élevés comme 500 $/mois pour des services cloud gérés.
   

De plus, Kubernetes fonctionne **de la même manière partout**. Que vous déployiez vos conteneurs sur AWS, Google Cloud, Azure, ou même votre propre ordinateur portable – Kubernetes s'en moque. Votre configuration reste la même.

Comparez cela aux services gérés comme Elastic Beanstalk ou Azure App Service – qui vous lient à leur plateforme, rendant très difficile le changement plus tard.

✅ **En bref** : Kubernetes vous fait économiser de l'argent, du temps et beaucoup de maux de tête. Il vous permet d'exécuter, de mettre à l'échelle et d'organiser vos microservices sans être enchaîné à un seul fournisseur cloud – et sans vous noyer dans le travail manuel.

## **Comment Kubernetes fonctionne – Composants d'un environnement Kubernetes** 👨‍💻

À ce stade, vous avez vu le problème : exécuter des dizaines (ou des centaines !) de microservices manuellement, c'est comme jongler avec trop de balles – vous êtes sûr d'en laisser tomber certaines.

C'est pourquoi Kubernetes a été créé. Mais... comment fait-il toute cette magie ? Commençons par le définir techniquement (simple mais précis – parfait pour les entretiens) puis par une analogie pour les non-initiés (pour que cela reste dans votre tête !).

### 1️⃣ **Cluster 🌍**

Un cluster Kubernetes est l'ensemble complet des machines (physiques ou basées sur le cloud) où Kubernetes s'exécute. Il est composé d'un ou plusieurs nœuds maîtres et nœuds travailleurs, travaillant ensemble pour déployer et gérer des applications conteneurisées.

Pensez à un cluster Kubernetes comme votre terrain de jeu entier. C'est l'environnement où vivent, grandissent et jouent ensemble tous vos microservices.

Un cluster est composé de deux types d'ordinateurs (appelés nœuds) :

* Nœud maître (de nos jours souvent appelé le plan de contrôle)

* Nœuds travailleurs

### 2️⃣ **Nœud maître (Plan de contrôle) 👑**

Le nœud maître est comme le cerveau de Kubernetes. Il gère et coordonne l'ensemble du cluster – en décidant quelles applications s'exécutent où, en surveillant la santé et en mettant à l'échelle les choses selon les besoins.

C'est comme le patron de l'ensemble du cluster. Il n'exécute pas vos applications directement. Au lieu de cela, il :

* Surveille les nœuds travailleurs

* Décide quel microservice (conteneur) va où

* S'assure que tout fonctionne en douceur et équitablement

Pensez à cela comme à un gestionnaire d'usine qui dit aux machines quoi faire, quand commencer, quand s'arrêter et où envoyer le prochain paquet.

À l'intérieur du nœud maître se trouvent quelques mini-composants intelligents qui gèrent le vrai travail.

### 3️⃣ **Serveur API 💬**

Le serveur API est la porte d'entrée de Kubernetes. Il gère la communication entre les utilisateurs et le système, en prenant des commandes et en les alimentant dans le cluster.

C'est ici que vous (ou votre équipe) donnez des instructions à Kubernetes. Que vous déployiez une nouvelle application ou que vous mettiez à l'échelle une application existante, vous "parlez" d'abord au serveur API. C'est comme soumettre une demande à la réception – le serveur API la transmet aux bonnes personnes (ou machines).

### 4️⃣ **Planificateur 📅**

Le planificateur attribue des Pods (applications) aux nœuds travailleurs en fonction des ressources disponibles et des besoins.

Imaginez que vous avez demandé à Kubernetes de lancer un nouveau microservice. Le planificateur vérifie :

* Quel nœud travailleur a assez d'espace ?

* Quel nœud a assez de mémoire et de CPU ?

* Où ce service fonctionnerait-il le mieux ?

Il prend la décision et attribue le microservice à l'endroit parfait. Intelligent, non ?

### 5️⃣ **Gestionnaire de contrôleurs 🎨**

Le gestionnaire de contrôleurs exécute des contrôleurs qui surveillent le cluster et s'assurent que l'état réel du système correspond à l'état souhaité.

Ce composant surveille le système comme un faucon. Supposons que vous ayez dit à Kubernetes : 
*"Hey, je veux 3 copies de mon microservice de paiement en cours d'exécution à tout moment."*

Si l'une d'elles plante, le gestionnaire de contrôleurs le voit et en lance une nouvelle pour la remplacer automatiquement. Il s'assure que la réalité correspond toujours au plan.

### 6️⃣ **etcd 📚**

etcd est la mémoire de Kubernetes – un magasin de valeurs-clés distribué où les données du cluster sont sauvegardées : fichiers de configuration, état et métadonnées.

Imaginez un cahier où toutes les règles, enregistrements et plans sont écrits. Sans etcd, Kubernetes oublierait tout.

### 7️⃣ **Nœuds travailleurs 🚀**

Les nœuds travailleurs sont les serveurs qui exécutent les conteneurs d'applications réels, faisant le gros du travail dans le cluster.

Ce sont les machines où vos microservices vivent et s'exécutent réellement. Le nœud maître donne des ordres, mais les nœuds travailleurs font le gros du travail – ils exécutent vos conteneurs !

Chaque nœud travailleur a quelques assistants pour gérer ses microservices :

* Le Kubelet

* Le Kube Proxy

### 8️⃣ **Kubelet 📧**

Le Kubelet est l'agent qui vit sur chaque nœud travailleur et qui s'assure que les conteneurs sont sains et fonctionnent comme prévu.

Il écoute les instructions du nœud maître. Si le nœud maître dit : *"Hey, exécute ce conteneur !"*, le Kubelet le fait et le maintient en cours d'exécution. Si quelque chose ne va pas, le Kubelet rapporte au nœud maître.

### 9️⃣ **Kube Proxy 🚦**

Kube Proxy gère le trafic réseau, en s'assurant que les Pods peuvent communiquer entre eux et avec le monde extérieur.

Imaginez que le service de connexion de votre application bancaire doit communiquer avec le service de paiements. Le Kube Proxy gère le routage afin que la demande atteigne le bon endroit. Il gère également l'équilibrage de charge, afin qu'aucun microservice ne soit surchargé.

Donc, pour résumer :

* Le nœud maître est le patron – il planifie, surveille et attribue des tâches.

* Les nœuds travailleurs font le vrai travail – exécuter vos microservices.

* Des composants comme etcd, Kubelet, Planificateur, Gestionnaire de contrôleurs et Kube Proxy travaillent tous ensemble comme des parties d'une machine bien huilée.

Kubernetes est conçu pour gérer vos microservices automatiquement – les garder en vie, les mettre à l'échelle, les déplacer et les redémarrer s'ils plantent – afin que vous n'ayez pas à les surveiller vous-même.

## Charges de travail Kubernetes 🏢 – Pods, Déploiements, Services, & Plus

Les charges de travail Kubernetes sont les objets que vous utilisez pour gérer et exécuter vos applications. Pensez à eux comme des plans 📜 qui disent à Kubernetes **quoi** exécuter et **comment** l'exécuter – qu'il s'agisse d'un conteneur d'application unique, d'un groupe de conteneurs, d'une base de données ou d'un travail par lots. Voici quelques-unes des charges de travail dans Kubernetes :

### 1️⃣ **Pods**

Un **Pod** est la plus petite et la plus simple unité dans le modèle d'objet Kubernetes. Il représente une seule instance d'un processus en cours d'exécution dans votre cluster et peut contenir un ou plusieurs conteneurs qui partagent des ressources de stockage et de réseau. 

Pensez à un Pod comme une enveloppe autour d'un ou plusieurs conteneurs qui doivent travailler ensemble. Ils partagent la même adresse IP réseau et le même stockage, ce qui leur permet de communiquer facilement et de partager des données. Les Pods sont éphémères (ils vivent pendant une courte durée, ils peuvent être remplacés très facilement). Si un Pod meurt, Kubernetes peut en créer un nouveau pour le remplacer presque instantanément.

Supposons que vous avez une application qui est divisée en 2 monolithes distribués – un frontend et un backend. Le frontend s'exécutera dans un conteneur dans le Pod A, tandis que l'application backend s'exécutera dans un conteneur dans un autre Pod B.

### 2️⃣ **Déploiements**

Un **Déploiement** fournit des mises à jour déclaratives pour les Pods et les ReplicaSets. Vous décrivez un état souhaité dans un Déploiement, et le Contrôleur de Déploiement modifie l'état réel pour qu'il corresponde à l'état souhaité à un rythme contrôlé.

Les Déploiements gèrent le cycle de vie de vos Pods d'application. Ils garantissent que le nombre spécifié de Pods sont en cours d'exécution et peuvent gérer les mises à jour, les retours en arrière et la mise à l'échelle. Si un Pod échoue, le Déploiement le remplace automatiquement pour maintenir l'état souhaité.

Imaginez que vous gérez un magasin. Un Déploiement est comme le gérant du magasin – vous lui dites combien de travailleurs (Pods) vous voulez, et il s'assure qu'ils sont toujours présents. Si l'un d'eux ne se présente pas au travail, le gérant trouve un remplaçant automatiquement. Vous pouvez également lui dire d'embaucher plus de travailleurs ou d'en licencier lorsque cela est nécessaire.

### 3️⃣ **Services**

Un **Service** dans Kubernetes définit une manière d'accéder/communiquer avec les Pods. Les Services permettent la communication entre différents Pods (par exemple, votre Pod frontend A peut communiquer avec votre Pod backend B via un service) et peuvent exposer votre application au trafic externe (par exemple, l'internet public). 

Les Services agissent comme un point de terminaison stable pour accéder à un ensemble de Pods. Même si les Pods sous-jacents changent, l'IP et le nom DNS du Service restent constants, garantissant la communication entre les Pods au sein du cluster ou avec l'internet.

Un Service est comme la porte d'entrée de votre application. Peu importe quel travailleur (Pod) se trouve derrière, les gens utilisent toujours la même entrée pour y accéder. Il cache les choses compliquées qui se passent en coulisses et donne aux utilisateurs un moyen simple de se connecter à votre application.

### 4️⃣ **ReplicaSets**

Un **ReplicaSet** garantit qu'un nombre spécifié de Pods identiques sont en cours d'exécution à tout moment. Il est souvent utilisé pour garantir la disponibilité d'un nombre spécifié de Pods (mise à l'échelle horizontale). 

Les ReplicaSets maintiennent un ensemble stable de Pods en cours d'exécution. Si un Pod plante ou est supprimé, le ReplicaSet crée automatiquement un nouveau pour le remplacer, garantissant que votre application reste disponible.

Pensez à un ReplicaSet comme à un robot qui compte combien de copies de votre application sont en cours d'exécution. Si l'une d'elles disparaît, il en crée automatiquement une nouvelle. Il maintient le nombre stable, exactement comme vous le lui avez dit.

### 5️⃣ **DaemonSets**

Un **DaemonSet** garantit que tous (ou certains) Nœuds exécutent une instance (une copie) d'un Pod spécifique. Lorsque des nœuds sont ajoutés au cluster, des Pods sont ajoutés à eux. Lorsque des nœuds sont retirés du cluster, ces Pods sont également retirés. 

Les DaemonSets sont utilisés pour déployer un Pod sur chaque nœud du cluster. Cela est utile pour exécuter des tâches en arrière-plan comme la collecte de logs ou des agents de surveillance sur tous les nœuds (par exemple pour obtenir l'utilisation du CPU, de la mémoire et du disque de chaque nœud).

Un DaemonSet est comme dire : « Je veux que cette application d'assistance s'exécute sur **chaque ordinateur** que nous avons. » Comme mentionné précédemment, c'est idéal pour des choses comme les collecteurs de logs ou les vérificateurs de sécurité – de petits assistants que chaque machine devrait avoir.

### 6️⃣ **StatefulSets**

Un **StatefulSet** est l'objet API de charge de travail utilisé pour gérer les applications stateful (applications qui stockent des données, par exemple dans leur système de fichiers – bases de données). Il gère le déploiement et la mise à l'échelle d'un ensemble de Pods et fournit des garanties concernant l'ordre et l'unicité de ces Pods.

Les StatefulSets sont conçus pour les applications qui nécessitent un stockage persistant et des identités réseau stables, comme les bases de données.

Disons que vous exécutez une base de données ou tout ce qui doit sauvegarder des informations. Un StatefulSet est comme donner à chaque application une étiquette de nom et un tiroir personnel pour stocker leurs affaires. Même si vous les redémarrez, ils reviennent avec le même nom et le même tiroir.

### 7️⃣ **Jobs**

Un **Job** crée un ou plusieurs Pods et garantit qu'un nombre spécifié d'entre eux se termine avec succès. À mesure que les Pods se terminent avec succès, le Job suit les terminaisons réussies. Lorsqu'un nombre spécifié de terminaisons réussies est atteint, le Job est terminé. 

Un Job est comme une tâche ponctuelle. Imaginez envoyer un lot d'e-mails ou traiter un rapport. Vous voulez que la tâche s'exécute, se termine, puis s'arrête. C'est exactement ce qu'un Job fait.

### 8️⃣ **CronJobs**

Un **CronJob** crée des Jobs selon un calendrier basé sur le temps. Il exécute un Job périodiquement selon un calendrier donné, écrit au format Cron.

Un CronJob est comme définir un rappel ou une alarme. Il indique à votre application (dans ce cas, le Job) de faire quelque chose tous les soirs à 2 heures, tous les lundis matins, ou une fois par mois – quel que soit le calendrier que vous lui donnez.

## 🏢 Comment créer un cluster Kubernetes dans un environnement de démonstration avec `play-with-k8s`

Comme nous l'avons discuté précédemment, un cluster Kubernetes est un ensemble de machines (appelées nœuds) qui exécutent des applications conteneurisées.

Configurer un cluster Kubernetes localement ou dans le cloud peut être complexe et coûteux. Pour simplifier le processus d'apprentissage, Docker fournit une plateforme gratuite basée sur un navigateur appelée [Play with Kubernetes](https://labs.play-with-k8s.com/). Cet environnement vous permet de créer et d'interagir avec un cluster Kubernetes sans installer quoi que ce soit sur votre machine locale. C'est un excellent outil pour les débutants afin d'acquérir une expérience pratique avec Kubernetes.

### 🔑 Se connecter à Play with Kubernetes

1. **Visitez la plateforme** à l'adresse [https://labs.play-with-k8s.com/](https://labs.play-with-k8s.com/).
   
2. **Authentifiez-vous** :
   
   * Cliquez sur le bouton "Login".
   
   * Vous pouvez vous connecter en utilisant votre compte Docker Hub ou GitHub.
   
   * Si vous n'avez pas de compte, vous pouvez en créer un gratuitement sur [Docker Hub](https://hub.docker.com/) ou [GitHub](https://github.com/).

![Se connecter à Play with k8s](https://cdn.hashnode.com/res/hashnode/image/upload/v1746083007442/a038ee6c-b471-4880-ba17-2e8927678780.png align="center")

### 🚀 Créer votre cluster Kubernetes

Une fois connecté, suivez ces étapes pour configurer votre cluster :

#### Étape 1 : Démarrer une nouvelle session :

Cliquez sur le bouton **"Start"** pour initier une nouvelle session. Cela créera une nouvelle session vous donnant environ 4 heures de temps de jeu, après quoi le cluster et ses ressources seront automatiquement terminés.

![Session chronométrée Play with k8s](https://cdn.hashnode.com/res/hashnode/image/upload/v1746083204331/8410e18b-4ed4-4374-8d4f-44f0fefa1623.png align="center")

#### Étape 2 : Ajouter des instances :

Ensuite, cliquez sur **"+ Add New Instance"** pour créer un nouveau nœud (machine virtuelle).  

![Créer un nouveau nœud maître (VM)](https://cdn.hashnode.com/res/hashnode/image/upload/v1746083280594/740d963a-c70f-43c6-8354-e6ea0c3d7f41.png align="center")

Cela ouvrira une fenêtre de terminal où vous pourrez exécuter des commandes.  

![Terminal du nœud nouvellement créé](https://cdn.hashnode.com/res/hashnode/image/upload/v1746083304493/ffd34d73-e5cd-41d0-908a-2240924e7ad0.png align="center")

#### Étape 3 : Initialiser le nœud maître :

Dans le terminal, exécutez la commande suivante pour initialiser le nœud maître :

```bash
kubeadm init --apiserver-advertise-address $(hostname -i) --pod-network-cidr <SPECIFIED_IP_ADDRESS>
```

Vous pouvez trouver la commande dans le terminal. Dans mon cas, l'adresse IP est `10.5.0.0/16`. Remplacez le `<SPECIFIED_IP_ADDRESS>` par l'adresse IP spécifiée dans votre terminal.

![Initialiser le nœud maître et le plan de contrôle](https://cdn.hashnode.com/res/hashnode/image/upload/v1746083865451/fdf18710-c987-4221-bc02-369cd709a849.png align="center")

Ce processus configurera le plan de contrôle de votre cluster Kubernetes.

#### Étape 4 : Ajouter des nœuds travailleurs :

Si vous souhaitez ajouter des nœuds travailleurs, dans le terminal du nœud maître, vous trouverez une commande `kubeadm join...` après avoir exécuté la commande `kubeadm init --apiserver-advertise-address $(hostname -i) --pod-network-cidr <SPECIFIED_IP_ADDRESS>`.

![Commande pour ajouter un nœud travailleur au plan de contrôle](https://cdn.hashnode.com/res/hashnode/image/upload/v1746084559142/6e539ef6-0219-40da-95e7-42abc9f1af8c.png align="center")

Cliquez sur **"+ Add New Instance"** pour créer un autre nœud comme vous l'avez fait précédemment.

Exécutez cette commande dans le terminal du nouveau nœud pour le joindre au cluster :

![Ajouter un nœud travailleur au plan de contrôle](https://cdn.hashnode.com/res/hashnode/image/upload/v1746084666411/78f07ba1-7f1f-402e-9ed8-c4d6054bdcab.png align="center")

#### Étape 5 : Configurer la mise en réseau du cluster :

Accédez au nœud maître et exécutez la commande ci-dessous pour configurer la mise en réseau du cluster.

```bash
kubectl apply -f https://raw.githubusercontent.com/cloudnativelabs/kube-router/master/daemonset/kubeadm-kuberouter.yaml
```

![Configurer la mise en réseau dans le cluster](https://cdn.hashnode.com/res/hashnode/image/upload/v1746085296963/ba35966c-5dd1-4e17-b4b5-85639cb3a80d.png align="center")

#### Étape 6 : Vérifier le cluster :

Dans le terminal du nœud maître (le premier nœud avec le profil utilisateur mis en évidence), exécutez :

```bash
kubectl get nodes
```

Vous devriez voir une liste de nœuds dans votre cluster, y compris le maître et tous les nœuds travailleurs que vous avez ajoutés.

![Nœuds dans le cluster](https://cdn.hashnode.com/res/hashnode/image/upload/v1746085583418/45e55418-4b0f-461f-98d8-3b0c8f19b839.png align="center")

Félicitations ! Vous venez de créer votre tout premier cluster Kubernetes avec 2 VM : le nœud maître (où réside le plan de contrôle), et les nœuds travailleurs (où les charges de travail Kubernetes, par exemple les Pods, seront déployés).

## 🚀 Comment déployer une application sur votre cluster Kubernetes

Maintenant que nous avons configuré notre cluster Kubernetes en utilisant Play with Kubernetes, il est temps de déployer l'application et de la rendre accessible sur Internet.

### 🦸 Comprendre les approches impérative et déclarative dans Kubernetes

Avant de continuer, il est essentiel de comprendre les deux méthodes principales pour gérer les ressources dans Kubernetes : **Impérative** et **Déclarative**.

### 🔮 Approche impérative

Dans l'approche impérative, vous émettez directement des commandes à l'API Kubernetes pour créer ou modifier des ressources. Chaque commande spécifie l'action souhaitée, et Kubernetes l'exécute immédiatement.

Imaginez dire à quelqu'un : "Allume la lumière." Vous donnez un ordre direct, et l'action se produit immédiatement. De même, avec les commandes impératives, vous instruisez Kubernetes étape par étape sur ce qu'il doit faire.

**Exemple :**  
Pour créer un pod exécutant un conteneur NGINX, exécutez la commande ci-dessous dans le terminal du nœud maître :

```bash
kubectl run nginx-pod --image=nginx
```

Attendez quelques secondes et exécutez la commande ci-dessous pour vérifier l'état du pod :

```bash
kubectl get pods
```

Vous devriez obtenir une réponse similaire à celle-ci

![Obtenir les pods en cours d'exécution dans le cluster](https://cdn.hashnode.com/res/hashnode/image/upload/v1746087463204/52ef26e5-96df-4d91-8a2d-7527a38786d2.png align="center")

Maintenant, exposons notre Pod à Internet en créant un **Service**. Exécutez la commande ci-dessous pour exposer le Pod :

```bash
kubectl expose pod nginx-pod --type=NodePort --port=80
```

Pour obtenir l'adresse IP du Cluster afin que nous puissions accéder à notre Pod, exécutez la commande ci-dessous :

```bash
kubectl get svc
```

La commande affiche l'adresse IP à partir de laquelle nous pouvons accéder à notre service. Vous devriez obtenir une sortie similaire à celle-ci :

![Obtenir l'adresse IP du service](https://cdn.hashnode.com/res/hashnode/image/upload/v1746088678881/a4f3bdbc-c7eb-4696-ba6e-587637be5792.png align="center")

Maintenant, copiez l'adresse IP pour le service `nginx-pod` et exécutez la commande ci-dessous pour faire une requête à votre Pod :

```bash
curl <YOUR-SERVICE-IP-ADDRESS>
```

Remplacez le `<YOUR-SERVICE-IP-ADDRESS>` par l'adresse IP de votre service `nginx-pod`. Dans mon cas, c'est `10.98.108.173`.

Vous devriez obtenir une réponse de votre Pod `nginx-pod` :

![Faire une requête au Pod Nginx en cours d'exécution dans le Cluster](https://cdn.hashnode.com/res/hashnode/image/upload/v1746088937046/8b86cd63-21f0-45d3-9ab5-59bd630fb37c.png align="center")

Nous n'avons pas pu accéder au Pod depuis Internet, c'est-à-dire notre navigateur, car notre Cluster n'est pas connecté à un service cloud comme AWS ou Google Cloud qui peut nous fournir un équilibreur de charge externe.

Maintenant, essayons de faire la même chose mais en utilisant la méthode déclarative.

### 🚀 Approche déclarative

Jusqu'à présent, nous avons utilisé l'approche impérative, où nous avons tapé des commandes comme `kubectl run` ou `kubectl expose` directement dans le terminal pour faire faire quelque chose à Kubernetes immédiatement.

Mais Kubernetes a une autre (et souvent meilleure) façon de faire les choses : l'approche déclarative.

#### 🧑‍🍳 Qu'est-ce que l'approche déclarative ?

Au lieu de donner des instructions à Kubernetes étape par étape comme un chef dans une cuisine, vous lui donnez une recette complète – un fichier qui décrit exactement ce que vous voulez (par exemple, quelle application exécuter, combien de copies, comment l'exposer, etc.).

Cette recette est écrite dans un fichier appelé un **manifest**.

#### 📄 Qu'est-ce qu'un manifest ?

Un manifest est un fichier (généralement écrit au format YAML) qui décrit un objet Kubernetes – comme un Pod, un Déploiement ou un Service.

C'est comme écrire ce que vous voulez, le remettre à Kubernetes et dire : "Hey, s'il te plaît, fais en sorte que cela existe exactement comme je l'ai décrit."

Nous utiliserons deux manifests :

1. Un pour déployer notre application

2. Un autre pour l'exposer à Internet


Passons en revue cela !

#### 📁 Étape 1 : Cloner le dépôt GitHub

Nous avons déjà un dépôt GitHub qui contient les deux fichiers manifest dont nous avons besoin. Clonons-le dans notre environnement Kubernetes.

Exécutez ceci dans le terminal (sur votre nœud maître) :

```bash
git clone https://github.com/onukwilip/simple-kubernetes-app
```

Maintenant, entrons dans le dossier :

```bash
cd simple-kubernetes-app
```

Vous devriez voir deux fichiers :

* `deployment.yaml`

* `service.yaml`

#### 📧 Étape 2 : Comprendre le manifest de déploiement (`deployment.yaml`)

Ce manifest indiquera à Kubernetes de déployer notre application et de s'assurer qu'elle est toujours en cours d'exécution.

Voici ce qu'il contient :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
```

Maintenant, décomposons cela :

* `apiVersion: apps/v1` : Cela indique à Kubernetes quelle version de l'API nous utilisons pour définir cet objet.

* `kind: Deployment` : Cela signifie que nous créons un Déploiement (un contrôleur qui gère les Pods).

* `metadata.name` : Nous donnons à notre Déploiement un nom : `nginx-deployment`.

* `spec.replicas: 3` : Nous disons à Kubernetes : "S'il vous plaît, exécutez 3 copies (réplicas) de cette application."

* `selector.matchLabels` : Kubernetes utilisera cette étiquette pour trouver quels Pods ce Déploiement gère.

* `template.metadata.labels` & `spec.containers` : Cette section décrit les Pods que le Déploiement doit créer – chaque Pod exécutera un conteneur utilisant l'image officielle `nginx`.

✅ En termes simples : Nous demandons à Kubernetes de créer et de maintenir 3 copies d'une application qui exécute NGINX, et de les redémarrer automatiquement si l'une d'elles échoue.

#### 🌐 Étape 3 : Comprendre le manifest de service (`service.yaml`)

Ce fichier indique à Kubernetes d'exposer notre application NGINX au monde extérieur en utilisant un Service.

Voici le fichier – décomposons-le également :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

* `apiVersion: v1` : Nous utilisons la version 1 de l'API Kubernetes.

* `kind: Service` : Nous créons un objet Service.

* `metadata.name: nginx-service` : Nous lui donnons un nom.

* `spec.type: NodePort` : Nous l'exposons via un port sur le nœud (pour que nous puissions y accéder via l'adresse IP du nœud).

* `selector.app: nginx` : Cela indique à Kubernetes de connecter ce Service aux Pods avec l'étiquette `app: nginx`.

* `ports.port` et `targetPort` : Le Service écoutera sur le port 80 et redirigera le trafic vers le port 80 sur le Pod.

✅ En termes simples : Ce fichier dit : "Exposez notre application NGINX via le réseau du cluster pour que nous puissions y accéder depuis le monde extérieur."

#### 🧹 Étape 4 : Nettoyer les ressources précédentes

Si vous exécutez toujours le Pod et le Service que nous avons créés en utilisant l'approche impérative, supprimons-les pour éviter les conflits :

```bash
kubectl delete pod nginx-pod
kubectl delete service nginx-pod
```

#### 📤 Étape 5 : Appliquer les manifests

Maintenant, déployons l'application NGINX et exposons-la – cette fois en utilisant la méthode **déclarative**.

Depuis le dossier `simple-kubernetes-app`, exécutez :

```bash
kubectl apply -f deployment.yaml
```

Puis :

```bash
kubectl apply -f service.yaml
```

Cela créera le Déploiement et le Service décrits dans les fichiers. 🎉

#### 🔍 Étape 6 : Vérifier qu'il est en cours d'exécution

Vérifions si les Pods ont été créés :

```bash
kubectl get pods
```

Vous devriez voir 3 Pods en cours d'exécution !

Et vérifions le service :

```bash
kubectl get svc
```

Recherchez le `nginx-service`. Vous verrez quelque chose comme :

![Accéder au NodePort du service](https://cdn.hashnode.com/res/hashnode/image/upload/v1746092825896/617084f1-3a71-4cfd-a287-9f7a9ac08810.png align="center")

Notez le **NodePort** (par exemple, `30001`) car nous l'utiliserons pour accéder à l'application.

#### 🌍 Étape 7 : Accéder à l'application

Vous pouvez maintenant envoyer une requête à votre application comme ceci :

```bash
curl http://<YOUR-NODE-IP>:<NODE-PORT>
```

> Remplacez `<YOUR-NODE-IP>` par l'IP de votre nœud maître (vous trouverez généralement cela dans Play With Kubernetes en haut de votre terminal), et `<NODE-PORT>` par le NodePort affiché dans la commande `kubectl get svc`.

![Obtenir l'adresse IP du nœud maître](https://cdn.hashnode.com/res/hashnode/image/upload/v1746092570586/b33cabc0-ea1e-4a70-ab55-9f3a0761bec0.png align="center")

Vous devriez voir le contenu HTML de la page de bienvenue NGINX imprimé.

Maintenant, terminez l'environnement du cluster en cliquant sur le bouton **CLOSE SESSION** :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746093081895/79139f75-5e6b-4991-be74-38ecbbf2ef66.png align="center")

### 🎊 Pourquoi l'approche déclarative est meilleure (dans la plupart des cas)

* 🔁 **Réutilisable** : Vous pouvez utiliser les mêmes fichiers encore et encore.

* 📧 **Versionné** : Vous pouvez pousser ces fichiers sur GitHub et suivre les changements au fil du temps.

* 🏢 **Corrige facilement les erreurs** : Vous voulez changer 3 réplicas en 5 ? Il suffit de mettre à jour le fichier et de le réappliquer !

* 🦸 **Plus facile à maintenir** : Surtout lorsque vous avez de nombreuses ressources à gérer.

## 📜 Avantages de l'utilisation de Kubernetes en entreprise

Kubernetes n'est pas seulement un outil pour les développeurs—c'est aussi un facilitateur pour les entreprises. Il aide les entreprises à livrer des produits plus rapidement, de manière plus fiable et avec une réduction des coûts opérationnels.

Décomposons comment Kubernetes se traduit par des avantages commerciaux concrets :

### 1️⃣ **Meilleure utilisation des ressources cloud = économies de coûts**

Avant Kubernetes, le déploiement de nombreux microservices pour une seule application signifiait souvent la création de ressources cloud séparées (comme un service Azure App Service par microservice), ce qui pouvait rapidement engendrer des coûts élevés. Imaginez 50 $/mois par service × 10 services = 500 $/mois 😬.

**Avec Kubernetes :**  
Vous pouvez exécuter plusieurs microservices sur moins de machines virtuelles (VM) tandis que Kubernetes décide automatiquement de la manière la plus efficace d'utiliser les serveurs disponibles. Cela signifie que vous payez pour moins de serveurs et en tirez plus parti 💰.

### 2️⃣ **Haute disponibilité et temps de fonctionnement = clients satisfaits**

Kubernetes surveille vos applications comme un faucon 👀. Si l'une d'elles plante ou échoue, Kubernetes la redémarre ou la remplace *immédiatement* – automatiquement.

**Pour votre entreprise :**  
Cela signifie moins de temps d'arrêt, moins de tickets de support et des clients plus heureux qui ne remarquent même pas lorsque les choses vont mal en arrière-plan.

### 3️⃣ **Mise à l'échelle facile pendant une forte demande**

Mettre à l'échelle manuellement les applications pendant un trafic élevé (comme le Black Friday) peut être un cauchemar 😰. Et si vous n'agissez pas rapidement, les clients subissent des lenteurs ou des plantages.

**Avec Kubernetes :**  
Vous pouvez configurer chaque microservice pour qu'il se mette à l'échelle automatiquement – ce qui signifie qu'il ajoute plus d'instances de ce service *uniquement lorsque nécessaire* (trop d'utilisateurs sur votre site essayant d'acheter différents produits) et réduit l'échelle lorsque le trafic diminue. Cela garantit que votre application est toujours réactive et que vous ne payez que pour ce que vous utilisez.

### 4️⃣ **Déploiement plus rapide = temps de mise sur le marché plus rapide**

Kubernetes prend en charge l'automatisation et la répétabilité. Les équipes peuvent déployer de nouvelles fonctionnalités ou microservices plus rapidement sans se soucier de la configuration de l'infrastructure à chaque fois.

**Pour les entreprises :**  
Cela signifie des mises à jour de produits plus rapides, une réponse plus rapide aux demandes du marché et un avantage concurrentiel 🚀.

### 5️⃣ **Environnements cohérents = moins de bugs**

Chaque microservice dans Kubernetes est conteneurisé, ce qui signifie qu'il s'exécute avec toutes ses dépendances dans un package autonome. Vous pouvez exécuter la même configuration d'application exacte dans :

* Développement

* Test

* Production

Cela réduit les bugs causés par les problèmes "ça marche sur ma machine" 🧑‍💻 et aide les équipes à construire en toute confiance.

### 6️⃣ **Indépendance vis-à-vis des fournisseurs (Adieu au verrouillage des fournisseurs)**

Lorsque vous utilisez des services cloud gérés (comme AWS Elastic Beanstalk ou Azure App Service), il est souvent difficile de passer à un autre fournisseur car tout est adapté à cette plateforme spécifique.

**Avec Kubernetes :**  
Il fonctionne de la même manière sur AWS, Azure, GCP, ou même votre propre centre de données. Cela signifie que vous pouvez changer de fournisseur cloud facilement et éviter d'être verrouillé à un seul fournisseur – alias la liberté du cloud ! ☁️🔓

### 7️⃣ **Clarté organisationnelle**

Kubernetes vous permet d'organiser vos applications clairement. Vous pouvez regrouper les charges de travail par :

* Équipe (par exemple, Finance, RH)

* Environnement (par exemple, test, staging, production)

Cette structure aide les grandes équipes à mieux collaborer, à rester organisées et à gérer les ressources efficacement.

## 😬 Inconvénients de l'utilisation de Kubernetes

Comme tout dans la tech, Kubernetes n'est pas tout en arc-en-ciel et en fusées 🚀. Tout comme tout autre outil, il a ses avantages et ses inconvénients. Et il est super important pour les fondateurs de startups, les chefs de produit, ou même les PDG de savoir quand Kubernetes est le bon choix – et quand il est simplement excessif.

Décomposons les principaux inconvénients de manière simple et honnête :

### 👨‍💻 1. Vous aurez probablement besoin d'un ingénieur DevOps ou d'une équipe

Kubernetes est puissant, oui. Mais cette puissance s'accompagne d'une grande responsabilité 😅.

En termes simples :

* Vous ne cliquez pas simplement sur un bouton et votre application est magiquement en cours d'exécution.

* Kubernetes a besoin de quelqu'un qui comprend comment le configurer, le maintenir en fonctionnement et résoudre les problèmes lorsqu'ils surviennent. Cette personne (ou équipe) est généralement appelée ingénieur DevOps, ingénieur de fiabilité de site ou ingénieur cloud.

Voici ce qu'ils géreront typiquement :

* Créer le cluster (l'environnement où vos applications s'exécuteront)

* Définir comment vos conteneurs d'applications doivent se comporter (combien doivent s'exécuter, combien de mémoire ils ont besoin, quand ils doivent redémarrer, etc.)

* Surveiller les applications et s'assurer qu'elles sont en bonne santé

* Veiller à ce que les règles de sécurité soient respectées

* Gérer la mise à l'échelle automatique, les déploiements, les sauvegardes, etc.

🤒 **En bref :** Vous aurez besoin de quelqu'un de compétent pour gérer cet outil. Si vous êtes un fondateur solo ou une petite équipe sans expérience DevOps, Kubernetes pourrait être trop pour vous au début.

### 💰 2. Kubernetes peut être coûteux (s'il est adopté prématurément)

Kubernetes permet d'économiser de l'argent à grande échelle – mais peut coûter plus cher si vous l'adoptez trop tôt ou pour le mauvais cas d'utilisation.

Voici pourquoi :

* Kubernetes est conçu pour gérer plusieurs applications ou microservices. Si votre entreprise n'a qu'une seule petite application, vous utilisez une fusée pour livrer une pizza 🍕 – ce n'est tout simplement pas nécessaire.

* Kubernetes est également idéal lorsque vous avez un trafic élevé ou imprévisible. Il peut automatiquement mettre à l'échelle vos services lorsque le trafic augmente... mais si votre trafic est stable et faible, vous ne bénéficierez pas beaucoup de cette puissance.

Disons que :

* Vous avez une application avec un trafic modéré.

* Vous la déployez sur Kubernetes (ce qui nécessite au moins 1-2 VM + configuration).

* Vous embauchez un ingénieur DevOps pour la gérer.

* Vous payez pour le calcul cloud + le stockage + la surveillance.

Vous pourriez finir par dépenser 300-800 $/mois ou plus... pour quelque chose qui aurait pu être hébergé sur un service simple comme [Render](https://render.com), [Heroku](https://www.heroku.com), ou une VM de base pour une fraction du coût.

Alors, quand **devriez-vous** envisager Kubernetes ?

* Lorsque votre plateforme est composée de plusieurs services (par exemple, des services séparés pour l'authentification des utilisateurs, les paiements, l'analyse, les notifications, etc.)

* Lorsque vous prévoyez des pics de trafic (par exemple, lancement dans de nouveaux pays, devenir viral, demande saisonnière comme le Black Friday)

* Lorsque vous voulez de la flexibilité dans la gestion de votre infrastructure à travers les fournisseurs cloud (AWS, GCP, Azure) ou même sur site

## 🤖 Cas d'utilisation : Quand (et quand ne pas) utiliser Kubernetes

Kubernetes est un outil incroyablement puissant 🚀 – mais ce n'est pas toujours la bonne solution dès le premier jour.

Décomposons quand il est judicieux d'utiliser Kubernetes et quand cela peut être excessif 👋

### ✅ Quand vous devriez utiliser Kubernetes

Kubernetes devient essentiel dans ces scénarios :

#### 1. Votre application est composée de nombreux microservices

Si votre application est divisée en plusieurs microservices – comme l'authentification des utilisateurs, les paiements, les commandes, les notifications, et plus encore – c'est un bon signe que Kubernetes pourrait éventuellement aider.

Kubernetes peut :

* Aider à gérer chaque microservice indépendamment

* Mettre à l'échelle automatiquement chacun en fonction de la demande

* Redémarrer les services défaillants automatiquement

* Faciliter le déploiement des mises à jour pour des parties spécifiques de l'application

#### 2. Vous recevez un trafic *constant et élevé*

Ce n'est pas seulement une question de complexité – c'est une question de demande.

Si votre application reçoit un volume constant et élevé d'utilisateurs (comme des centaines ou des milliers chaque jour), et que vous commencez à voir des signes que vos serveurs sont surchargés, Kubernetes excelle ici. Il peut :

* Augmenter automatiquement les ressources lorsque le trafic augmente

* Équilibrer la charge sur plusieurs serveurs

* Empêcher les temps d'arrêt dus aux pics de trafic

#### 3. Vous voulez la portabilité et l'indépendance du cloud

Si votre entreprise ne veut pas être verrouillée à un seul fournisseur de cloud (par exemple, uniquement AWS), Kubernetes vous offre de la flexibilité. Vous pouvez déplacer votre application entre AWS, GCP, Azure – ou même vers votre propre centre de données – avec moins de changements.

#### 4. Votre équipe DevOps est en croissance

Lorsque vous avez plusieurs développeurs ou équipes travaillant sur différentes parties de l'application, Kubernetes aide :

* Organiser et isoler les charges de travail par équipe

* Améliorer la collaboration et la cohérence

* Fournir un contrôle d'accès et une surveillance faciles

### ❌ Quand vous ne devriez pas utiliser Kubernetes

Soyons honnêtes : Kubernetes n'est pas pour tout le monde, surtout pas au début.

#### 1. Vous venez de lancer votre application

Dans les premiers jours de votre produit, lorsque vous venez de le lancer et que le trafic est encore faible, Kubernetes est *excessif*. Vous n'avez pas besoin de sa complexité (pour l'instant).

👉 Au lieu de cela, déployez votre application ou chaque microservice sur une machine virtuelle simple (VM). C'est moins cher et plus rapide pour commencer.

#### 2. Vous n'avez pas besoin de mise à l'échelle automatique (pour l'instant)

Si le trafic vers votre application est encore faible et gérable, un seul serveur (ou quelques-uns) peut facilement gérer la charge. Dans ce cas, il est préférable de :

* Déployer vos microservices manuellement ou avec Docker Compose

* Surveiller et mettre à l'échelle manuellement lorsque nécessaire

* Garder les choses simples jusqu'à ce que le besoin d'automatisation devienne évident

#### 3. Vous n'avez pas d'équipe DevOps

Kubernetes est puissant 🚀 – mais il nécessite une expertise pour le configurer et le maintenir. Si vous n'avez pas d'ingénieur DevOps ou quelqu'un qui comprend Kubernetes, cela peut causer plus de problèmes que cela n'en résout.

Embaucher une équipe DevOps peut être coûteux, et configurer Kubernetes incorrectement peut entraîner des pannes, des risques de sécurité ou un gaspillage de ressources 💰

### 📅 Quand passer à Kubernetes

Alors, quel est le meilleur chemin à suivre ?

Voici une feuille de route simple :

1. **Commencez petit** : Déployez votre application (ou microservices) sur une ou quelques VM

2. **Surveillez le trafic** : À mesure que la demande des utilisateurs augmente, augmentez la taille de la VM ou répliquez l'application manuellement

3. **Suivez les points de douleur** : Si la mise à l'échelle devient trop manuelle, ou si les services plantent sous la charge...

4. **Alors adoptez Kubernetes** 🦸

Ce n'est pas une question de complexité de votre application – c'est une question de quand le trafic et la croissance exigent une mise à niveau dans la façon dont vous gérez les choses.

### 🏁 TL;DR pour les fondateurs et les équipes DevOps

* Ne sautez pas sur Kubernetes juste parce que c'est à la mode

* Utilisez-le uniquement lorsque le trafic augmente régulièrement et que la mise à l'échelle automatique devient nécessaire

* Kubernetes est le plus précieux lorsque vous voulez mettre à l'échelle de manière fiable et efficace

* Avant ce point, restez sur des déploiements simples – cela vous fera économiser du temps, de l'argent et du stress

## 🎉 Conclusion

Wow ! Quel voyage nous avons fait 😄

Nous avons commencé par répondre à la grande question 🚀 – **Qu'est-ce que Kubernetes ?** Nous avons découvert que ce n'est pas une bête mythique, mais un outil d'orchestration puissant qui nous aide à gérer, déployer, mettre à l'échelle et maintenir des applications conteneurisées de manière plus intelligente.

Ensuite, nous avons fait un pas en arrière dans le temps pour voir comment les applications étaient déployées avant Kubernetes 🚀 – les maux de tête de l'installation manuelle de logiciels sur les serveurs, la création de séparées instances cloud pour chaque microservice, et l'accumulation de factures cloud énormes juste pour rester à flot. Nous avons également vu comment les conteneurs ont simplifié les choses, mais même eux avaient leurs propres limitations lorsqu'ils étaient gérés à grande échelle.

C'est là que Kubernetes est venu à la rescousse 🦸

Nous avons exploré :

* **Les problèmes que Kubernetes résout** 🚀 – comme la mise à l'échelle automatique, la gestion efficace des ressources, les économies de coûts et le regroupement transparent des conteneurs.

* **L'architecture et les composants de Kubernetes** 🚀 – en décomposant des termes complexes comme le cluster, le nœud maître, les nœuds travailleurs, les Pods, les Services, le Kubelet, et plus encore, en idées simples et faciles à digérer.

* **Les charges de travail Kubernetes** comme les Déploiements, les Pods, les Services, les DaemonSets, et les StatefulSets, et ce qu'ils font en coulisses pour garder nos applications en cours d'exécution de manière fiable.

De la théorie à la pratique, nous avons même mis les mains dans le cambouis :

* Nous avons créé un cluster Kubernetes gratuit en utilisant Play with Kubernetes 🦸

* Déployé une application réelle en utilisant à la fois les approches impérative (commande directe) et déclarative (fichier manifest)

* Compris pourquoi la méthode déclarative rend notre infrastructure plus facile à gérer, surtout lorsque nos systèmes grandissent.

Ensuite, nous avons pris une perspective commerciale 🔍 et regardé :

* Les avantages de Kubernetes 🚀 – de la mise à l'échelle automatique pendant les pics de trafic, à l'efficacité des coûts, et au déploiement agnostique du cloud.

* Et aussi les inconvénients 😬 – comme le besoin d'ingénieurs DevOps expérimentés et le fait de ne pas être idéal pour chaque étape du cycle de vie d'un produit.

Enfin, nous avons conclu avec des cas d'utilisation réels, en mettant en évidence quand Kubernetes est un must-have, et quand il est préférable d'attendre 🚀 – surtout pour les startups en phase de démarrage qui cherchent encore leur public.

Ainsi, que vous soyez un débutant en DevOps, un fondateur de startup, ou simplement quelqu'un de curieux sur la façon dont la technologie moderne maintient vos applications préférées en ligne 🚀 – vous avez maintenant une compréhension fondamentale solide de Kubernetes 🚀

Kubernetes est puissant, mais il n'a pas besoin d'être écrasant. Avec une bonne compréhension des bases (que vous avez maintenant 🚀), vous êtes bien parti pour gérer des applications scalables comme un pro.

Commencez simplement. Grandissez intelligemment. Et lorsque le moment sera venu 🚀 – Kubernetes sera votre meilleur ami.

## **Étudier plus loin 📚**

Si vous souhaitez en apprendre davantage sur Kubernetes, vous pouvez consulter les cours ci-dessous :

* [Docker & Kubernetes : Le Guide Pratique (Academind - Udemy)](https://www.udemy.com/course/docker-kubernetes-the-practical-guide/)

* [Certified Kubernetes Application Developer (CKAD) Specialization (Coursera)](https://www.coursera.org/specializations/certified-kubernetes-application-developer-ckad-course)

## **À propos de l'auteur 👨‍💻**

Bonjour, je m'appelle Prince ! Je suis un ingénieur DevOps et architecte cloud passionné par la construction, le déploiement et la gestion d'applications scalables et le partage de connaissances avec la communauté tech[.](https://www.udemy.com/course/github-actions-the-complete-guide/?couponCode=CMCPSALE24)

Si vous avez apprécié cet article, vous pouvez en apprendre davantage sur moi en explorant plus de mes blogs et projets sur mon [profil LinkedIn.](https://www.linkedin.com/in/prince-onukwili-a82143233/) Vous pouvez trouver mes [articles LinkedIn ici](https://www.linkedin.com/in/prince-onukwili-a82143233/details/publications/). Vous pouvez également [visiter mon site web](https://prince-onuk.vercel.app/achievements#articles) pour lire plus de mes articles. Restons en contact et grandissons ensemble ! 😊
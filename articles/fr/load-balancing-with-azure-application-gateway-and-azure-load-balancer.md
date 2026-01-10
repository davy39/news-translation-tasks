---
title: Équilibrage de charge avec Azure Application Gateway et Azure Load Balancer
  – Quand utiliser chacun
subtitle: ''
author: Prince Onukwili
co_authors: []
series: null
date: '2025-05-14T19:37:46.320Z'
originalURL: https://freecodecamp.org/news/load-balancing-with-azure-application-gateway-and-azure-load-balancer
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747235455030/cb82bfb4-8d7b-47e5-ab31-126906f60b40.png
tags:
- name: Load Balancing
  slug: load-balancing
- name: Azure
  slug: azure
- name: Azure Application Gateway
  slug: azure-application-gateway
- name: virtual machine
  slug: virtual-machine
- name: Cloud
  slug: cloud
- name: '#virtual machine scale set'
  slug: virtual-machine-scale-set
- name: Load Balancer
  slug: load-balancer
seo_title: Équilibrage de charge avec Azure Application Gateway et Azure Load Balancer
  – Quand utiliser chacun
seo_desc: 'You’ve probably heard someone mention load balancing when talking about
  cloud apps. Maybe even names like Azure Load Balancer, Azure Application Gateway,
  or something about Virtual Machines and Scale Sets. 😵‍💫

  It all sounds important...but also a l...'
---

Vous avez probablement entendu quelqu'un mentionner l'équilibrage de charge en parlant des applications cloud. Peut-être même des noms comme Azure Load Balancer, Azure Application Gateway, ou quelque chose sur les machines virtuelles et les groupes identiques. 😵‍💫

Tout cela semble important... mais aussi un peu confus. Comme, pourquoi y a-t-il tant de pièces mobiles ? Et que font-elles réellement ?

Dans ce guide, nous allons tout décomposer – étape par étape – en utilisant des exemples réels et un langage simple.

Vous apprendrez :

* Ce que sont les équilibreurs de charge (et pourquoi les applications en ont même besoin)

* Comment les applications étaient déployées avant l'existence des équilibreurs de charge (indice : tout vivait sur un seul serveur solitaire)

* Comment fonctionnent les machines virtuelles Azure – et comment elles vous permettent de monter en puissance vos applications

* Ce que sont les groupes identiques de machines virtuelles, et comment ils aident à gérer les pics de trafic soudains

* Les différences entre Azure Load Balancer et Azure Application Gateway, et quand utiliser chacun

À la fin, vous ne comprendrez pas seulement ce que font ces outils – vous saurez *quand* et *pourquoi* les utiliser dans des scénarios réels.

Que vous soyez un débutant curieux, un constructeur pratique, ou quelqu'un qui essaie simplement de comprendre l'écosystème d'Azure, ce guide est pour vous.

Prêt à démêler les spaghettis du cloud ? C'est parti ! 🍝🚀

## 📜 Table des matières

1. [🧑‍💻 Qu'est-ce que les équilibreurs de charge ?](#heading-quest-ce-que-les-equilibreurs-de-charge)

2. [🏢 Comment les applications étaient déployées avant les équilibreurs de charge](#heading-comment-les-applications-etaient-deployees-avant-les-equilibreurs-de-charge)

3. [⚙️ Machines virtuelles Azure (VM) – Les blocs de construction](#heading-machines-virtuelles-azure-vm-les-blocs-de-construction)

4. [📈 Le besoin de mise à l'échelle – Vertical vs Horizontal](#heading-le-besoin-de-mise-a-lechelle-vertical-vs-horizontal)

5. [🔄 Groupes identiques de machines virtuelles Azure (VMSS) – Mise à l'échelle simplifiée](#heading-groupes-identiques-de-machines-virtuelles-azure-vmss-mise-a-lechelle-simplifiee)

6. [📧 Azure Load Balancer – Répartition du trafic](#heading-azure-load-balancer-repartition-du-trafic)

7. [🍴 Azure Application Gateway – Routage intelligent pour les applications modernes](#heading-azure-application-gateway-routage-intelligent-pour-les-applications-modernes)

8. [🔍 Azure Load Balancer vs Azure Application Gateway](#heading-azure-load-balancer-vs-azure-application-gateway)

9. [🧑‍🍳](#heading-cas-dusage-quand-utiliser-quoi) [Cas d'usage : Quand utiliser chacun](#heading-cas-dusage-quand-utiliser-chacun)

10. [✅ Conclusion](#heading-conclusion)

11. [Étudier plus loin 📜](#heading-etudier-plus-loin)

12. [À propos de l'auteur 👨‍💻](#heading-a-propos-de-lauteur)

## 🧑‍💻 Qu'est-ce que les équilibreurs de charge ?

Imaginez que vous gérez un petit restaurant avec un seul chef en cuisine. Tout se passe bien lorsque vous avez quelques clients – chaque commande est préparée l'une après l'autre, et tout le monde repart satisfait.

Mais que se passe-t-il lorsque 50 personnes entrent toutes en même temps ?

🍝 Un chef ne peut pas gérer autant de commandes en même temps.  
⏳ Les gens commencent à attendre plus longtemps.  
😭 Certains clients partent.  
💥 Le chef est submergé – et finit par s'épuiser.

C'est ce qui peut arriver à un serveur (l'ordinateur qui exécute votre application) lorsque trop d'utilisateurs essaient d'y accéder en même temps.

### Alors, que fait un équilibreur de charge ?

Un **équilibreur de charge** est comme un gestionnaire de restaurant intelligent. Mais au lieu de commandes de nourriture, il gère les requêtes des utilisateurs – les choses que les gens font lorsqu'ils ouvrent votre application, cliquent sur des boutons, ou chargent des données.

Disons que vous avez maintenant trois chefs (serveurs) au lieu d'un. Le travail de l'équilibreur de charge est de :

* 👀 Surveiller les commandes entrantes (requêtes des utilisateurs)

* 🧑‍🍳 Décider quel chef (serveur) est disponible ou le moins occupé

* 🍝 Envoyer cette requête au bon

* 🔄 Répéter cela encore et encore, en s'assurant que tout reste rapide et fluide

Donc en termes simples, un équilibreur de charge prend tout le trafic entrant vers votre application et le distribue sur plusieurs serveurs afin qu'aucun serveur ne soit surchargé – cool, non ? 😊

### Pourquoi les équilibreurs de charge ont-ils été introduits ?

À l'époque, de nombreuses applications étaient hébergées sur une seule machine – appelée Déploiement sur un seul serveur.

C'était bien lorsque vous aviez un petit nombre d'utilisateurs. Mais une fois que les choses ont commencé à croître – plus d'utilisateurs, plus d'actions, plus de données – les serveurs uniques sont devenus un goulot d'étranglement :

* Ils ne pouvaient gérer qu'un nombre limité de requêtes.

* S'ils tombaient en panne, toute votre application cessait de fonctionner.

* La mise à l'échelle (ajout de plus de puissance) était coûteuse et manuelle.

💡 Entrent en scène les **équilibreurs de charge** – conçus pour résoudre ce problème en rendant possible :

* Répartir le trafic sur plusieurs serveurs (afin qu'aucun serveur ne s'écrase sous la pression),

* Remplacer ou redémarrer des serveurs sans temps d'arrêt,

* Ajouter ou supprimer des serveurs selon les besoins, en fonction de la fréquentation de votre application (c'est ce qu'on appelle la **mise à l'échelle**).

### Un scénario simple de cas d'usage

Disons que vous construisez une boutique en ligne – votre propre mini Amazon. Au début, vous hébergez votre application sur une seule machine virtuelle Azure. Tout va bien. Mais un jour, vous lancez une énorme promo et soudain... des milliers de personnes affluent pour naviguer, faire des achats et passer à la caisse.

Votre seule machine virtuelle commence à ralentir.

Les commandes échouent. Les gens se plaignent. Votre application de rêve ? Elle s'écrase rapidement. 💥

Alors, que faites-vous ?

Vous lancez deux autres machines virtuelles pour aider – mais maintenant vous avez un autre problème : *Comment diviser le trafic entre les trois ?*

C'est là que l'équilibreur de charge intervient. Il :

* Regarde chaque requête utilisateur entrante

* Détermine quelle machine virtuelle est disponible et la moins occupée

* Envoie la requête là

* Continue à faire tourner les requêtes en temps réel

Et le résultat ?  
✅ Aucune machine virtuelle n'est submergée  
✅ Votre application reste rapide et réactive  
✅ Les utilisateurs sont heureux (et achètent à nouveau !)

![Illustration d'équilibreur de charge](https://cdn.hashnode.com/res/hashnode/image/upload/v1746980088916/41be330b-8d5b-4709-b07d-3f1a19d641e7.png align="center")

## 🏢 Comment les applications étaient déployées avant les équilibreurs de charge

Avant les outils cloud comme les équilibreurs de charge, la manière typique de faire fonctionner une application était assez simple : vous déployiez toute l'application sur un seul serveur, comme gérer une petite entreprise à partir d'une seule petite boutique.

### D'abord : Qu'est-ce qu'un serveur ?

Pensez à un serveur comme un ordinateur spécial qui est toujours connecté à Internet. Son travail est de "servir" votre application aux gens lorsqu'ils visitent votre site web, ouvrent votre application ou utilisent votre service.

Dans les plateformes cloud comme Azure, nous appelons généralement ceux-ci des machines virtuelles (VM) – essentiellement, des serveurs alimentés par logiciel que vous pouvez lancer avec quelques clics.

### Monolithes vs Microservices

Maintenant, les applications viennent sous différentes "formes". Les deux plus courantes sont :

* **Monolithes** : Tout est regroupé dans une seule grande application. Tout le code – de la connexion de l'utilisateur au panier d'achat jusqu'à la caisse – vit dans une seule unité.

* **Microservices** : L'application est divisée en petites applications indépendantes (services). Chaque service fait un travail – comme la connexion, les paiements, les commandes – et fonctionne séparément.

#### Comment ces applications étaient-elles déployées ?

Qu'il s'agisse d'un monolithe ou d'un ensemble de microservices, ils étaient généralement déployés sur un seul serveur (VM).

Pour les monolithes, vous exécutiez simplement toute l'application directement sur le serveur. Pour les microservices : vous exécutiez chaque service dans un espace séparé sur ce même serveur, en utilisant des **conteneurs**.

#### Attendez — Qu'est-ce qu'un conteneur ?

Un conteneur est comme un mini-ordinateur *à l'intérieur* d'un ordinateur. Il contient tout ce dont une application a besoin pour fonctionner – code, outils, paramètres – et il garde chaque application isolée des autres.

Pourquoi utiliser des conteneurs ?

* Vous pouvez exécuter plusieurs services sur le même serveur sans que leur logiciel sous-jacent (logiciel nécessaire pour que chaque application fonctionne) n'interfère les uns avec les autres.

* C'est plus rapide et plus efficace que d'installer tout directement sur le serveur.

* Ils rendent le déplacement des applications entre les environnements (par exemple, test → production) super fluide (plus de "Mais, ça marche sur ma machine…").

Des outils populaires comme Docker rendent le travail avec les conteneurs facile.

#### Relier le tout ensemble : Domaines, sous-domaines et proxys inverses

Lorsque votre application vit sur un serveur, vous voulez que les gens puissent y accéder. C'est là que les **noms de domaine** entrent en jeu.

* Votre serveur a une adresse IP publique – un ensemble de chiffres comme `102.80.1.23`, qui lui donne un identifiant unique sur l'internet public

* Mais au lieu de demander aux utilisateurs de taper des chiffres, vous liez cette IP à un nom de domaine, comme `monapplicationcool.com`

Si votre application a des microservices, vous pouvez même attribuer des **sous-domaines** comme :

* `api.monapplicationcool.com` pour le backend

* `tableaubord.monapplicationcool.com` pour l'interface utilisateur

* `paiements.monapplicationcool.com` pour les paiements

Pour gérer tout cela, vous utiliseriez un **proxy inverse** (comme Nginx ou Apache). Il écoute sur le domaine principal et les sous-domaines, et redirige le trafic vers la bonne application ou service.

Exemple :

* Quelqu'un visite `tableaubord.monapplicationcool.com`

* Le proxy inverse vérifie le domaine et redirige la requête vers le bon conteneur exécutant le service de tableau de bord

Et pour aider à toute cette configuration – du déploiement des conteneurs à la configuration des proxys inverses – il existe des outils conviviaux pour les développeurs comme [Coolify](https://coolify.io). Coolify est une plateforme open-source qui facilite grandement le travail des développeurs et des équipes DevOps pour :

* Déployer des applications dans des conteneurs

* Configurer des domaines et sous-domaines

* Configurer des proxys inverses – le tout à partir d'un tableau de bord propre, sans commandes terminales complexes nécessaires

![Exemple de tableau de bord Coolify](https://cdn.hashnode.com/res/hashnode/image/upload/v1746979943646/a6525a09-f44a-4e00-a945-7bded3483b0d.jpeg align="center")

Tout cela était configuré sur UN SEUL SERVEUR/VM. Mais voici le problème : lorsque ce serveur était surchargé ou tombait en panne…💥 tout s'arrêtait.

C'est pourquoi nous avions besoin d'une meilleure façon. Et c'est là que la **mise à l'échelle** et l'**équilibrage de charge** sont entrés en jeu – pour garder les applications en marche sans problème, quel que soit le trafic.

## ⚙️ Machines virtuelles Azure (VM) – Les blocs de construction

![Illustration de machine virtuelle](https://cdn.hashnode.com/res/hashnode/image/upload/v1746980948928/eb6a7fb2-7432-42ed-8cbd-bff6c8250d4e.jpeg align="center")

En ce qui concerne l'exécution d'applications dans le cloud, les **machines virtuelles (VM)** sont les blocs de construction de base – un peu comme louer un appartement dans un gratte-ciel numérique géant.

Vous n'avez pas besoin d'acheter tout le bâtiment (c'est-à-dire des serveurs physiques), vous louez simplement l'espace dont vous avez besoin, quand vous en avez besoin.

### Qu'est-ce qu'une machine virtuelle exactement ?

Une machine virtuelle est un ordinateur basé sur un logiciel qui s'exécute à l'intérieur d'un ordinateur réel et physique (un serveur) – hébergé dans un centre de données, comme ceux gérés par Microsoft Azure.

Elle ressemble et se comporte comme un ordinateur normal :

* Elle a un système d'exploitation (Windows, Linux)

* Vous pouvez installer des applications

* Elle a de la mémoire (RAM), du stockage (disques) et un CPU

Mais le meilleur ? Vous n'avez pas à vous soucier du matériel. Azure s'en occupe en coulisses – tout ce que vous avez à faire, c'est dire :

> « Hé Azure, donne-moi une VM Linux avec 4 Go de RAM et 2 CPU. »

Et boom 💥 – elle se lance en quelques minutes.

### Pourquoi utiliser une VM ?

Disons que vous avez construit une application web – c'est juste un simple blog. Vous voulez la déployer et la rendre accessible au monde.

Voici ce que vous pouvez faire avec une VM :

* La configurer avec votre OS préféré (par exemple, Ubuntu)

* Installer des serveurs web comme Nginx ou Apache

* Déployer votre application

* L'associer à votre nom de domaine

* Laisser le monde visiter votre blog sur [`monbloggenial.com`](http://monbloggenial.com)

C'est votre propre environnement personnel – pas de partage, contrôle total.

## 📈 Le besoin de mise à l'échelle – Vertical vs Horizontal

Imaginez que votre application grandit. Au début, ce ne sont que quelques utilisateurs. Puis quelques centaines. Puis des milliers se connectent, passent des commandes, discutent, téléchargent des photos – tout en même temps 😮

Soudain, votre serveur (VM) est sous pression. C'est comme essayer de verser une inondation à travers une paille.

### Alors, que faites-vous lorsqu'un seul serveur ne suffit pas ?

C'est là que la mise à l'échelle intervient – l'art de mettre à niveau l'infrastructure de votre application pour suivre le trafic.

Il existe deux façons principales de mettre à l'échelle :

#### 🧑‍🍳 Option 1 : Mise à l'échelle verticale (alias Scaling Up)

Vous prenez votre VM existante et lui donnez plus de puissance :

* Ajoutez plus de CPU 🧑‍🍳

* Augmentez la RAM 🧑‍🍳

* Ajoutez des disques plus rapides ⚡

Pensez-y comme passer d'une voiture normale à une voiture de sport. C'est le même véhicule, juste plus rapide et plus puissant.

**Avantages :**

* Simple à faire

* Aucun changement majeur dans la configuration de votre application

**Inconvénients :**

* Il y a une limite à la quantité de mise à niveau possible

* Toujours un point de défaillance unique : si la VM tombe en panne, tout s'arrête 😬

#### 🧑‍🍳 Option 2 : Mise à l'échelle horizontale (alias Scaling Out)

Au lieu de booster un seul serveur, vous ajoutez plus de serveurs – plusieurs VM exécutant des copies de votre application.

Maintenant :

* Les utilisateurs peuvent être distribués sur toutes ces VM

* Si l'une tombe en panne, les autres continuent de servir le trafic

* Vous pouvez *dynamiquement* ajouter ou supprimer des VM en fonction du trafic

C'est comme ouvrir plus de caisses dans un supermarché bondé 🛒

**Avantages :**

* La charge est uniformément distribuée. Par exemple, si un serveur gérait auparavant 100 % du trafic, l'ajout de deux serveurs supplémentaires entraînerait une répartition du trafic d'environ 33 % à 34 % pour chaque serveur.

* Améliore à la fois les performances et la fiabilité

* Vous pouvez mettre à l'échelle en fonction de la demande en temps réel, c'est-à-dire l'afflux de trafic

**Inconvénients :**

* Nécessite quelque chose pour répartir le trafic entre les VM – Équilibreurs de charge

* Plus coûteux. Vous finissez par payer le montant initial pour 1 VM (par exemple 30 $) pour le nombre de VM que vous fournissez – si vous fournissez 3 VM à 30 $ chacune, vous finissez par payer 90 $ à la fin du mois

### Exemple rapide dans la vie réelle

Disons que vous avez lancé un site de commerce électronique pour des baskets 👟 Le trafic explose pendant une grande vente ? Votre mise à l'échelle verticale (VM plus grande) pourrait s'étouffer.

Mais avec la mise à l'échelle horizontale :

* Vous lancez 5 VM dans différentes régions

* Le trafic est partagé entre elles

* Si une VM ralentit, les autres gèrent la charge

#### Alors, rappelez-vous 👋

| Type de mise à l'échelle | Description | Avantages | Inconvénients |
| --- | --- | --- | --- |
| 🧑‍🍳 Mise à l'échelle verticale | Rendre 1 VM plus puissante (ajout de plus de puissance CPU, SSD, RAM, bande passante, etc.) | Configuration facile, moins de changements | Limites matérielles, 1 point de défaillance - Si ce 1 serveur/VM tombe en panne, votre application aussi :( |
| 🧑‍🍳 Mise à l'échelle horizontale | Ajouter plus de VM pour gérer le trafic | Flexible, fiable | Nécessite une logique de distribution de trafic (Équilibreur de charge). Généralement plus coûteux (le prix de 1 VM multiplié par le nombre de VM) |

## 🔄 Groupes identiques de machines virtuelles Azure (VMSS) – Mise à l'échelle simplifiée

D'accord – nous avons donc parlé de la **mise à l'échelle horizontale** : ajouter plusieurs VM pour gérer le trafic croissant. Cela semble génial, non ?

Mais voici le problème : créer et configurer manuellement 5, 10 ou 100 VM... chaque fois que votre application est occupée ? Oui, ce n'est pas amusant 😳

### Entrée : Groupes identiques de machines virtuelles (VMSS)

VMSS est la manière d'Azure d'automatiser la mise à l'échelle horizontale. Au lieu de créer chaque VM une par une, vous définissez un modèle, et Azure s'occupe du reste :

* Combien de VM démarrer

* Comment les configurer (OS, applications, paramètres) ⚙️

* Quand ajouter ou supprimer des VM en fonction du trafic 📈📉

### Une analogie simple 🧃

Pensez à VMSS comme à un distributeur de jus lors d'une fête :

* Au début, il verse dans 2 verres (VM)

* Si 10 invités arrivent ? Il commence à remplir 5 verres

* La fête ralentit ? Retour à 2 verres

Vous n'avez jamais à remplir manuellement – le distributeur s'ajuste tout seul. 🎉

### Comment cela fonctionne (sans le jargon 😌)

1. **Vous définissez les règles :** « Si l'utilisation du CPU dépasse 70 %, ajoutez 2 VM supplémentaires. »

2. **Azure surveille le trafic et ajuste le nombre de VM** automatiquement.

3. **Toutes les VM sont identiques** – comme des clones, toutes exécutant la même configuration d'application.

4. **Il fonctionne avec Azure Load Balancer** pour répartir le trafic sur toutes ces VM en douceur.

### Exemple concret : Application de livraison de nourriture 🍔📱

Vous avez construit une application où les utilisateurs commandent de la nourriture. Pendant le déjeuner et le dîner, le trafic explose.

💡 Avec VMSS :

* Vous commencez avec 3 VM le matin

* À 12h, Azure voit une utilisation élevée du CPU, donc il lance 5 VM supplémentaires

* À 15h, le trafic baisse, donc Azure supprime les VM supplémentaires

Vous ne payez que pour ce que vous utilisez. Et les utilisateurs ont une expérience fluide – pas de retards, pas de plantages 👍

![Illustration de mise à l'échelle automatique](https://cdn.hashnode.com/res/hashnode/image/upload/v1746982520998/7fe3c997-fc8f-418a-861b-e999905ca43c.png align="center")

## 📧 Azure Load Balancer – Répartition du trafic

À ce stade, vous savez que votre application peut vivre sur plusieurs machines virtuelles (VM), et que vous pouvez les mettre à l'échelle facilement en utilisant des groupes identiques de machines virtuelles (VMSS).

Mais voici la grande question : lorsque les utilisateurs commencent à accéder à votre application – des centaines, voire des milliers à la fois – comment vous assurez-vous que tout ce trafic est réparti équitablement et efficacement entre ces VM ?

Vous ne voulez pas qu'une VM soit submergée tandis que d'autres se la coulent douce. Vous avez besoin d'un intermédiaire – quelque chose d'assez intelligent pour équilibrer la charge.

C'est là qu'intervient **Azure Load Balancer**. C'est la manière d'Azure de dire : « Ne vous inquiétez pas, je m'en occupe » lorsque le trafic commence à affluer.

### 🏟️ Alors, qu'est-ce qu'Azure Load Balancer ?

Azure Load Balancer est un **directeur de trafic**. Il prend le trafic entrant depuis Internet (ou même des sources internes au sein de votre réseau) et le répartit intelligemment sur plusieurs machines backend – généralement des VM.

C'est comme avoir une réceptionniste bien formée qui achemine chaque client vers le prochain agent disponible, afin que personne n'attende trop longtemps et que personne ne soit submergé 😃.

Et le meilleur ? Tout ce processus se déroule en arrière-plan – rapide, silencieux et transparent. Les utilisateurs visitant votre application ne savent pas qu'un gestionnaire de trafic travaille en coulisses. Ils voient simplement une expérience rapide et réactive.

### 🌐 L'IP Frontend – La face publique de votre application

Chaque Azure Load Balancer est lié à une **IP Frontend**, qui est essentiellement l'adresse IP publique de votre application – celle à laquelle les utilisateurs se connectent lorsqu'ils ouvrent `www.votreapp.com`.

Cette IP agit comme le point d'entrée. Tout le trafic utilisateur passe d'abord par elle. Mais le Load Balancer n'exécute pas réellement votre application. Au lieu de cela, il accepte le trafic et le transfère à l'une des VM du pool backend (nous y viendrons bientôt).

Vous pouvez configurer cette IP Frontend pour qu'elle soit soit publique (accessible via Internet) soit privée (utilisée pour le trafic interne au sein de votre réseau cloud – par exemple, entre microservices ou outils internes).

![Illustration de l'adresse IP Frontend](https://cdn.hashnode.com/res/hashnode/image/upload/v1747055268951/5afbb738-d00d-4f49-9709-2fa1fe7cffdd.png align="center")

### 🖥️‍💻 Backend Pool – Où la magie opère

Derrière chaque Azure Load Balancer se trouve un **backend pool** – un groupe de VM (ou d'instances de VM Scale Set) où votre application réelle est en cours d'exécution. Ce sont les vrais travailleurs, faisant tout le travail lourd.

Lorsque le trafic atteint l'IP Frontend, le Load Balancer prend cette requête et la transfère à l'une des VM du backend pool.

Mais il ne choisit pas simplement au hasard. Il vérifie d'abord quelques choses – comme si la VM est saine, si elle est déjà occupée, et quelles règles vous avez définies.

Chaque VM du pool exécute généralement la même application ou service. Cela signifie que n'importe laquelle d'entre elles peut gérer n'importe quelle requête entrante, ce qui est ce qui rend l'équilibrage de charge possible en premier lieu.

![Illustration du backend pool](https://cdn.hashnode.com/res/hashnode/image/upload/v1747055337014/e831056d-7c0c-49d9-b05a-6d3dbe3edc76.png align="center")

### 🧑‍⚕️ Health Probes – Garder un œil sur les VM

Maintenant, comment le Load Balancer sait-il quelle VM est saine ou non ? C'est là que les **health probes** entrent en jeu. Pensez à eux comme des vérifications régulières.

Vous configurez le Load Balancer pour qu'il "ping" périodiquement chaque VM – peut-être en atteignant une URL spécifique (comme `/health`) ou un certain port (comme 80 pour HTTP). Si une VM ne répond pas correctement, Azure la marque comme non saine et la retire temporairement de la rotation.

Cela garantit que les utilisateurs ne sont jamais dirigés vers une instance cassée ou non réactive de votre application. Et une fois que la VM redevient saine, elle est automatiquement réajoutée au pool.

### ⚙️ Load Balancing Rules – Qui obtient quoi ?

Ensuite, nous avons les **Load Balancing Rules**. Ce sont les instructions qui disent à Azure Load Balancer exactement comment se comporter.

Vous pouvez définir des règles comme :

* « Transférer tout le trafic HTTP (port 80) vers les VM du backend pool sur le port 80 »

* « Transférer le trafic HTTPS (port 443) vers les VM sur le port 443 »

* « Ne router le trafic que vers les VM saines »

Ces règles rendent Azure Load Balancer hautement personnalisable. Vous décidez comment le trafic circule, quels protocoles prendre en charge, et comment gérer les ports backend. C'est comme personnaliser les règles d'une course de relais – qui obtient le témoin et quand.

### 👟 Exemple concret : Rush de vente de baskets

Imaginez que vous gérez une boutique de baskets en ligne sur `www.sneakerblast.com`. Vous lancez une vente flash, et des milliers d'utilisateurs se ruent sur votre site web en même temps.

Grâce à votre Azure Load Balancer, voici ce qui se passe :

1. Tous ces utilisateurs arrivent sur votre IP Frontend, la face publique de votre site.

2. Le Load Balancer accepte le trafic et vérifie les health probes de toutes les VM dans le backend pool.

3. En fonction de ses règles, il transfère chaque utilisateur vers une VM saine et disponible.

4. Une VM peut servir un utilisateur à Lagos, une autre à Nairobi, une autre à Accra – tout cela de manière transparente.

Si une VM tombe en panne ou ralentit ? Le Load Balancer le détecte instantanément et arrête de router le trafic vers elle jusqu'à ce qu'elle soit de nouveau en ligne.

C'est une gestion fluide du trafic sans aucun effort manuel.

## 🍴 Azure Application Gateway – Routage intelligent pour les applications modernes

Jusqu'à présent, nous avons vu comment Azure Load Balancer vous aide à répartir le trafic sur plusieurs VM exécutant un seul service – comme une application monolithique ou un frontend web.

Disons que vous avez une application web déployée sur une VM. Elle écoute sur le port 80, et vous l'avez mise à l'échelle en 3 instances. L'Azure Load Balancer prend les requêtes d'Internet et les répartit sur les 3 instances du même service. Facile, non ?

Vous pouvez même lier l'adresse IP publique du Load Balancer à votre domaine – comme `mondomaine.com` – afin que les utilisateurs puissent visiter votre site normalement.

### 🧑‍🍳 Mais que se passe-t-il si vous avez *plusieurs* services ?

Maintenant, imaginez que vous êtes passé au-delà d'une seule application. Vous construisez quelque chose de plus moderne, comme un ensemble de microservices.

Vous avez maintenant :

* Un service de paiement écoutant sur le port 5000

* Un service d'authentification sur le port 6000

* Un service d'achat sur le port 7000

Tous déployés sur les mêmes VM (ou Virtual Machine Scale Set), juste sur différents ports.

Voici le problème : un Azure Load Balancer est conçu pour router le trafic vers *un* backend pool – essentiellement un service – sur un port. Si vous le liez à `mondomaine.com`, il ne peut envoyer le trafic que vers l'un de vos microservices. 😬

Alors… que faites-vous ?

Vous pourriez penser : « Laissez-moi simplement créer un Load Balancer séparé pour chaque service ! » 🤔

Mais cela signifie :

* Vous devrez payer pour plusieurs load balancers

* Vous finirez par gérer 3-5 adresses IP publiques

* Vous devrez peut-être même acheter plusieurs domaines comme `monpaiement.com`, `monauth.com`, etc. pour router correctement les utilisateurs

Aïe. C'est impratique, désordonné, *et* coûteux 😖💰

### 🎉 Entrée : Azure Application Gateway

**Azure Application Gateway** résout ce problème magnifiquement. Il est conçu pour router le trafic intelligemment – non pas vers un seul service, mais vers plusieurs services en utilisant une seule passerelle.

Voici comment cela fonctionne :

1. Vous créez une seule IP frontend publique (comme `52.160.100.5`)

2. Vous liez cette adresse IP à votre domaine principal, par exemple `mondomaine.com`

3. Ensuite, vous définissez plusieurs backend pools – un pour chaque service :

   * Service de paiement (port 5000)

   * Service d'auth (port 6000)

   * Service d'achat (port 7000)

4. Ensuite, vous configurez des règles de routage qui décident comment transférer chaque requête.

### ✨ Deux façons de router avec Application Gateway

Vous pouvez configurer un **routage intelligent** basé sur :

* **Chemins d'URL** :

   * `mondomaine.com/paiement` → Service de paiement

   * `mondomaine.com/auth` → Service d'auth

* **Sous-domaines** (en-têtes d'hôte) :

   * `paiement.mondomaine.com` → Service de paiement

   * `auth.mondomaine.com` → Service d'auth

De cette façon, tous vos services partagent une seule IP publique et un seul domaine – super propre, super efficace 👍

### 🧑‍🍳 Scénario réel (Décortiquons-le)

Disons que vous construisez une plateforme de startup qui a trois microservices clés :

* **Service de paiement** qui gère les transactions

* **Service d'authentification** qui gère la connexion et l'identité de l'utilisateur

* **Service d'achat** qui gère la commande de produits

Chaque service est conteneurisé et déployé sur la même VM (ou sur plusieurs VM à l'aide d'un groupe identique de machines virtuelles). Mais – et c'est la clé – ils écoutent tous sur des **ports différents** à l'intérieur des VM :

* Paiement → port 3000

* Auth → port 6000

* Achat → port 7000

Maintenant, sans une solution de routage intelligente, vous seriez coincé en essayant d'exposer seulement l'un de ces services en utilisant un Azure Load Balancer standard. Mais vous avez besoin que les trois soient accessibles depuis Internet – et vous ne voulez pas payer pour ou gérer 3 Load Balancers différents 😅

Alors, que faites-vous ?

### 🧑‍🍳 Utilisation d'Azure Application Gateway pour router le trafic intelligemment

Voici comment vous pouvez résoudre ce problème en utilisant **un** Application Gateway :

1. Déployez vos microservices à l'intérieur de chaque VM :

   * Chaque service s'exécute sur un port spécifique

   * Toutes les VM de votre groupe identique sont identiques (elles contiennent les trois services)

2. Créez des pools backend dans Application Gateway :

   * Un pool backend pour le service de paiement (pointant vers le port 3000 sur toutes les VM)

   * Un pour le service d'auth (port 6000)

   * Un autre pour le service d'achat (port 7000)

3. Créez des règles de routage :

   * Option A (Routage basé sur le chemin) :

      * Les requêtes vers `mondomaine.com/paiement` → vont au pool backend de paiement

      * Les requêtes vers `mondomaine.com/auth` → vont au pool backend d'auth

      * Les requêtes vers `mondomaine.com/achat` → vont au pool backend d'achat

   * Option B (Routage basé sur le sous-domaine) :

      * `paiement.mondomaine.com` → service de paiement

      * `auth.mondomaine.com` → service d'auth

      * `achat.mondomaine.com` → service d'achat

Vous dites simplement à l'Application Gateway : « Hé, si une requête arrive pour cette URL ou ce sous-domaine, envoie-la à ce port sur ces VM. » Et il fait exactement cela – de manière cohérente et intelligente 🔍

### 📧 Alors, que se passe-t-il réellement ?

Imaginez qu'un utilisateur visite `mondomaine.com/auth`. Voici ce qui se passe en coulisses :

1. Le DNS traduit `mondomaine.com` en l'IP publique de votre Application Gateway

2. La passerelle reçoit la requête

3. Elle vérifie vos règles de routage

4. Elle voit que `/auth` doit aller au pool backend pour le port 6000

5. Elle transfère la requête à l'une des VM exécutant le service d'auth

6. La réponse revient à l'utilisateur – rapide et transparente ✨

Cela se produit en millisecondes, pour chaque requête. Et parce que l'Application Gateway est conscient de plusieurs ports et services, il peut gérer la logique de routage qu'un Load Balancer ordinaire ne peut tout simplement pas faire.

![Illustration de l'Application Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1747056436345/7ea97231-d2ee-4f63-aff1-50595e7c06e0.png align="center")

## 🔍 Azure Load Balancer vs Azure Application Gateway

À ce stade, vous avez vu comment les deux outils aident à router le trafic dans Azure – mais ils résolvent des problèmes différents.

Décortiquons comment ils se comparent, et quand vous devriez utiliser l'un plutôt que l'autre 👋

### 🏢 1. **Logique de routage**

**Azure Load Balancer**  
Il distribue simplement le trafic entrant de manière égale sur un pool de VM. Il ne se soucie pas *de ce qu'est* la requête – il équilibre simplement la charge.  
  
Imaginez un livreur qui ne pose pas de questions – il dépose simplement chaque colis à la prochaine maison disponible.  
  
C'est ce que fait Azure Load Balancer : il envoie le trafic à l'un de vos serveurs sans regarder à l'intérieur de la requête.

**Azure Application Gateway**  
C'est le plus intelligent. Il regarde *ce qu'il y a à l'intérieur* de chaque requête (comme le chemin de l'URL ou le domaine) et prend des décisions intelligentes.

Comme un livreur plus intelligent qui regarde l'adresse et décide où aller : "Oh ! Celui-ci est pour le bureau des paiements, pas pour le bureau principal."  
  
C'est ce que fait Application Gateway : il lit la requête (comme l'URL ou le nom de domaine) et l'envoie au bon endroit selon les règles de routage.

### 🌐 2. **Protocoles gérés**

**Load Balancer**  
Fonctionne au niveau de la couche transport (couche 4 dans le modèle OSI). Il gère le trafic TCP/UDP – le trafic réseau brut, comme HTTP, le streaming vidéo, les jeux, etc.

**Application Gateway**  
Fonctionne au niveau de la couche application (couche 7). Il gère uniquement le trafic web – comme les sites web et les applications (HTTP/HTTPS) – et il peut effectivement lire ce qui est demandé, comme :

* "Allez à /login"

* "Allez à [payment.mydomain.com](http://payment.mydomain.com)".

TL;DR : Load Balancer pousse simplement des paquets. App Gateway *lit* réellement vos requêtes web.

### 🔧 3. **Scénarios de cas d'usage**

| Situation | Meilleur choix |
| --- | --- |
| Vous avez une grande application et vous voulez simplement répartir les utilisateurs sur les serveurs | ✅ Load Balancer |
| Vous avez plusieurs services (comme login, paiement, etc.) et vous devez envoyer les utilisateurs au bon | ✅ Application Gateway |
| Vous voulez utiliser des sous-domaines (comme [login.mysite.com](http://login.mysite.com)) | ✅ Application Gateway |
| Vous voulez sécuriser votre site web avec HTTPS et un pare-feu d'application web (WAF) | ✅ Application Gateway |
| Vous voulez la configuration la plus simple et le coût le plus bas | ✅ Load Balancer |

### 🔒 4. **Terminaison SSL et fonctionnalités de sécurité**

**Load Balancer** ne gère pas les trucs de sécurité. Vous devrez sécuriser chaque serveur vous-même (par exemple, configurer HTTPS sur chacun).

**Application Gateway** peut tout sécuriser en un seul endroit – vous téléchargez votre certificat SSL une fois et il gère HTTPS pour tous les services.

Il peut également vous protéger des pirates et du mauvais trafic avec quelque chose appelé **WAF (Web Application Firewall)**, qui protège votre application contre les menaces comme l'injection SQL, XSS, etc. (vous devez configurer cela manuellement).

### 💰 5. **Tarification et complexité**

**Load Balancer** est moins cher et plus facile à configurer. Idéal lorsque vous n'avez pas besoin de fonctionnalités sophistiquées.

**Application Gateway** coûte plus cher, mais vous donne plus de contrôle et moins de maux de tête lorsque vous travaillez avec des applications complexes et des microservices.

Essayer d'utiliser Load Balancer pour plusieurs services ? Vous devrez créer un Load Balancer par service, ce qui devient coûteux et impratique.

### 🧑‍🍳 Tableau récapitulatif

| Fonctionnalité | Load Balancer | Application Gateway |
| --- | --- | --- |
| Peut-il comprendre la requête ? | ❌ Non | ✅ Oui |
| Peut-il router en fonction de l'URL ou du sous-domaine ? | ❌ Non | ✅ Oui |
| Peut-il gérer le trafic HTTPS sécurisé ? | ❌ Non | ✅ Oui |
| Est-il bon pour les applications simples ? | ✅ Oui | ✅ Oui |
| Est-il bon pour les applications complexes avec de nombreux services ? | ❌ Non | ✅ Oui |
| Coût | 💲 Plus bas | 💰 Plus élevé |

## 🧑‍🍳 Cas d'usage : Quand utiliser chacun

Il n'y a pas de solution universelle lorsqu'il s'agit d'héberger des applications dans le cloud. La bonne configuration dépend de ce que vous construisez, de la quantité de trafic que vous attendez et de la complexité de votre application.

Passons en revue 4 scénarios de cas d'usage différents, en commençant par la configuration la plus basique jusqu'à une architecture entièrement auto-scalée et routée intelligemment.

### 1️⃣ **Instance unique de VM – Pour les petits projets ou outils internes**

**Utilisez ceci lorsque :**  
Vous commencez tout juste. Vous avez construit une petite application – peut-être un portfolio, un blog ou un projet secondaire – et vous voulez la rendre accessible, OU Vous êtes une startup qui vient de lancer.

**Comment cela fonctionne :**  
Vous lancez une seule VM Azure, installez votre application dessus et ouvrez le port sur lequel elle écoute (par exemple, le port 80 pour un serveur web). Vous pouvez ensuite attacher une IP publique à la VM et la lier à un domaine personnalisé comme `monapplicationgeniale.com`.

**Exemples concrets :**

* Un développeur hébergeant un site web de portfolio ou un blog

* Une startup testant un nouveau produit avec seulement quelques utilisateurs

* Un outil interne d'entreprise pour une petite équipe

**Avantages :**

* Configuration super simple

* Coût faible

* Contrôle total de votre environnement

**Inconvénients :**

* Si la VM tombe en panne, votre application tombe en panne

* Pas de mise à l'échelle automatique – les performances peuvent baisser avec les pics de trafic (la seule façon de s'adapter à l'augmentation de l'utilisation du CPU/mémoire due à l'afflux de trafic est via la mise à l'échelle verticale manuelle de la VM)

* Vous maintenez et surveillez tout manuellement

### 2️⃣ **Mise à l'échelle horizontale manuelle – Pour les applications avec un trafic moyen et prévisible**

**Utilisez ceci lorsque :**  
Votre application grandit – peut-être avez-vous quelques milliers d'utilisateurs maintenant, et les performances comptent. Vous voulez plus d'un serveur pour que votre application ne plante pas pendant les heures de pointe.

**Comment cela fonctionne :**  
Vous créez manuellement 2 ou 3 VM Azure avec la même configuration d'application. Vous ajoutez ensuite un Load Balancer devant pour répartir le trafic équitablement entre elles.

**Exemples concrets :**

* Une entreprise avec un portail client

* Un site web scolaire qui gère des connexions régulières, la diffusion de vidéos de cours, etc. pendant les heures de classe

* Une application qui reçoit du trafic principalement pendant la journée (charge prévisible)

**Avantages :**

* Meilleure performance et disponibilité

* La charge est partagée entre plusieurs VM

* Vous pouvez mettre à l'échelle manuellement si nécessaire

**Inconvénients :**

* Vous devez ajouter ou supprimer manuellement des VM – ce qui demande des efforts

* Vous devez toujours surveiller les performances manuellement

* Pas d'automatisation ou d'auto-réparation intégrée

### 3️⃣ **Auto-scaling avec VM Scale Sets + Azure Load Balancer – Pour les applications avec un trafic irrégulier ou imprévisible**

**Utilisez ceci lorsque :**  
Vous construisez quelque chose de plus sérieux – le trafic arrive par vagues (par exemple, une application de réservation de coachs/fitness), et vous ne voulez pas passer votre temps à mettre à l'échelle des VM toute la journée. Vous voulez qu'Azure mette automatiquement à l'échelle votre infrastructure pour vous.

**Comment cela fonctionne :**  
Vous configurez un groupe identique de machines virtuelles (VMSS) qui peut automatiquement créer plus de VM lorsque c'est nécessaire (comme pendant un trafic élevé), et les supprimer lorsque les choses se calment 💰. Un Load Balancer distribue le trafic sur toutes ces VM.

**Exemples concrets :**

* Une plateforme de médias où les gens téléchargent des vidéos ou des photos

* Un site de shopping qui connaît des pics pendant les promotions, par exemple les Black Fridays

* Une plateforme de réservation avec un trafic de pointe en soirée/week-end

**Avantages :**

* Mise à l'échelle automatique – économise du temps et de l'argent

* Haute disponibilité : les VM peuvent être remplacées si l'une tombe en panne

* Facile à développer à mesure que votre base d'utilisateurs grandit

**Inconvénients :**

* Fonctionne mieux si votre application est monolithique (un seul grand service)

* Pas de support pour le routage du trafic vers des services spécifiques – répartit simplement le trafic sur les VM

* Le Load Balancer ne peut pas regarder les chemins d'URL ou les sous-domaines

### 4️⃣ **VM Scale Set + Azure Application Gateway – Pour les microservices ou les applications web complexes**

**Utilisez ceci lorsque :**  
Vous avez une application moderne multi-services – peut-être construite avec des microservices. Chaque service (comme les paiements, l'authentification, la recherche, etc.) vit sur un port différent ou même dans un conteneur.

Vous voulez router le trafic intelligemment – comme `/login` va au service d'auth, `/pay` aux paiements, et `/search` au service de recherche – tout cela sur le même domaine.

**Comment cela fonctionne :**  
Vous utilisez toujours un groupe identique de machines virtuelles pour l'auto-scaling, mais au lieu d'un Load Balancer basique, vous ajoutez une Application Gateway. Elle peut inspecter chaque requête et l'envoyer au bon service en fonction de choses comme :

* Chemin d'URL (par exemple, `/payments`, `/orders`)

* Sous-domaine (par exemple, `payments.mydomain.com`, `auth.mydomain.com`)

**Exemples concrets :**

* Un produit SaaS complet avec plusieurs services

* Un site de commerce électronique avec caisse, compte, commandes et tableaux de bord d'administration

* Une entreprise migrant d'un monolithe vers une configuration de microservices

**Avantages :**

* Routage intelligent basé sur le chemin ou le sous-domaine

* Tout fonctionne sous une seule IP publique et un seul domaine

* Gestion sécurisée HTTPS + pare-feu d'application web (WAF) optionnel

* Auto-scaling et haute disponibilité

**Inconvénients :**

* Configuration plus complexe

* Coût légèrement plus élevé en raison de l'Application Gateway

* Nécessite une planification autour des numéros de port et des pools backend

### 🧑‍🍳 Tableau récapitulatif rapide

| Configuration | Meilleur pour | Mise à l'échelle | Logique de routage | Coût | Facilité |
| --- | --- | --- | --- | --- | --- |
| ☀️ VM unique | Petits sites, applications personnelles | ❌ (Manuelle) | ❌ Une seule application | 💲 (Le plus bas) | ⭐⭐⭐⭐ |
| 🧑‍🍳 Mise à l'échelle horizontale manuelle + Load Balancer | Applications de taille moyenne, trafic prévisible | ✅ (Manuelle) | ❌ Une seule application | 💲💲💲 (en raison de plusieurs VM fonctionnant simultanément sans réduction – même sans trafic) | ⭐⭐ (en raison de la mise à l'échelle manuelle) |
| 🔄 VMSS + Load Balancer | Applications occupées, trafic irrégulier | ✅ (Auto) | ❌ Une seule application | 💲💲 | ⭐⭐⭐ |
| 🍴 VMSS + App Gateway | Microservices, applications modernes | ✅ (Auto) | ✅ Routage intelligent (impliquant plusieurs microservices) | 💲💲💲💲(Le plus élevé) | ⭐⭐ |

## ✅ Conclusion

À ce stade, vous êtes passé de simplement entendre les mots « équilibreur de charge » ou « groupe identique » à comprendre exactement comment ils fonctionnent, quand les utiliser et quels problèmes ils résolvent. Que vous lanciez une petite application ou que vous mettiez à l'échelle un service à fort trafic, Azure vous offre des outils flexibles et puissants pour grandir en toute confiance.

Nous avons commencé par le tout début – une seule machine virtuelle. C'est simple et idéal pour les petites applications, mais cela devient rapidement un goulot d'étranglement à mesure que le trafic augmente.

C'est là que la mise à l'échelle intervient. Nous avons exploré :

* 🧑‍🍳 **La mise à l'échelle verticale** – Mettre à niveau la même VM (solution rapide, mais limitée)

* 🧑‍🍳 **La mise à l'échelle horizontale** – Ajouter plus de VM pour mieux gérer le trafic

Ensuite, nous avons introduit les groupes identiques de machines virtuelles Azure (VMSS) – qui donnent vie à la mise à l'échelle automatique. Plus d'intervention manuelle – Azure peut mettre à l'échelle vos serveurs en fonction de la demande.

Mais là où les choses deviennent vraiment intelligentes, c'est avec les équilibreurs de charge :

* 📧 **Azure Load Balancer** aide à répartir le trafic sur vos VM – idéal pour les applications à service unique

* 🍴 **Azure Application Gateway** va plus loin en routant les requêtes en fonction des chemins d'URL ou des sous-domaines – parfait pour les applications multi-services ou microservices

### 🌱 TL;DR – Que devriez-vous utiliser ?

* **VM unique** : Pour les projets secondaires, les portfolios ou les outils internes

* **Mise à l'échelle manuelle + Load Balancer** : Pour les applications de taille moyenne avec une charge prévisible

* **VMSS + Load Balancer** : Pour les applications monolithiques avec des besoins de mise à l'échelle automatique

* **VMSS + Application Gateway** : Inclut également la mise à l'échelle automatique mais pour les microservices ou les besoins de routage intelligent

### 💡 Réflexions finales

Les applications cloud grandissent – vite. Et avec la croissance vient la complexité. Mais avec la bonne configuration Azure, vous pouvez rester une longueur d'avance sur votre trafic, servir les utilisateurs mieux, et garder les coûts sous contrôle.

Rappelez-vous : vous n'avez pas besoin de commencer grand. Commencez petit, comprenez les schémas de trafic de votre application, et mettez à l'échelle seulement lorsque vous en avez besoin. Des outils comme Azure VM Scale Sets, Load Balancer, et Application Gateway vous donnent le contrôle et la puissance de construire des applications modernes et évolutives sans sur-ingénierie.

Merci d'avoir suivi ce guide approfondi. J'espère que cela a rendu les choses plus claires, plus simples, et peut-être même un peu amusantes 😊

## **Étudier plus loin 📜**

Si vous souhaitez en savoir plus sur les machines virtuelles Azure, les groupes identiques, le Load Balancer et l'Application Gateway, vous pouvez consulter les cours ci-dessous :

* [Préparation à l'examen Microsoft Azure Fundamentals AZ-900](https://www.coursera.org/specializations/microsoft-azure-fundamentals-az900-exam-prep) – Microsoft, Coursera

* [Tutoriel Azure Virtual Machine | Création d'une machine virtuelle dans Azure | Formation Azure | Simplilearn](https://youtu.be/QOv_-xBXkpo?si=kSijmQdev5cQbRKl) – YouTube

* [Groupes identiques de machines virtuelles](https://youtu.be/wN4lRWHUHA0?si=kWBGXhXZTnVgzuEj) – YouTube

* [Azure Load Balancer | Tutoriel Azure Load Balancer | Tout sur le Load Balancer | Edureka](https://youtu.be/VqBGjddK5VY?si=diLGQfuW5i0lxbse) – YouTube

* [Plongée approfondie dans Azure Application Gateway | Expliqué étape par étape](https://youtu.be/V9EP4jAg4QM?si=t7EqQjw1eNHqOtjK) – YouTube

## **À propos de l'auteur 👨‍💻**

Salut, je suis Prince ! Je suis un ingénieur DevOps et architecte cloud passionné par la construction, le déploiement et la gestion d'applications évolutives et le partage de connaissances avec la communauté technologique.

Si vous avez aimé cet article, vous pouvez en apprendre plus sur moi en explorant plus de mes blogs et projets sur mon [profil LinkedIn](https://www.linkedin.com/in/prince-onukwili-a82143233/). Vous pouvez trouver mes [articles LinkedIn ici](https://www.linkedin.com/in/prince-onukwili-a82143233/details/publications/). Vous pouvez également [visiter mon site web](https://prince-onuk.vercel.app/achievements#articles) pour lire plus de mes articles. Restons en contact et grandissons ensemble ! 😊
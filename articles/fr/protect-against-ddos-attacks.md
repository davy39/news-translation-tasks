---
title: Comment se protéger contre les attaques DDoS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-10T17:36:54.000Z'
originalURL: https://freecodecamp.org/news/protect-against-ddos-attacks
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-sora-shimazaki-5935794.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: Comment se protéger contre les attaques DDoS
seo_desc: "By Megan Kaczanowski\nDistributed Denial of Service (DDoS) attacks aim\
  \ to take an organization or service offline and originate from multiple, distributed\
  \ hosts. \nThe difficult part of defending against DDoS attacks is that the hosts\
  \ are distributed –..."
---

Par Megan Kaczanowski

Les attaques par déni de service distribué (DDoS) visent à mettre hors ligne une organisation ou un service et proviennent de plusieurs hôtes _distribués_.

La partie difficile de la défense contre les attaques DDoS est que les hôtes sont distribués – s'il s'agissait d'un seul hôte ou d'un petit groupe, vous pourriez facilement bloquer le trafic avec une règle de pare-feu.

Il existe de nombreux types différents d'attaques DDoS, mais nous pouvons les regrouper en trois catégories – volumétriques, protocoles et attaques d'applications. Examinons chacune d'elles en détail.

## Qu'est-ce que les attaques DDoS volumétriques ?

Les attaques DDoS volumétriques visent à saturer la bande passante d'une victime (comme les attaques par réflexion UDP).

Une attaque par réflexion UDP envoie des paquets avec l'adresse IP de la cible falsifiée comme source. Ensuite, les réponses au paquet falsifié seront envoyées à la cible, plutôt qu'à l'attaquant.

L'avantage de passer par un serveur intermédiaire plutôt que d'attaquer directement la cible est que les paquets de réponse sont généralement beaucoup plus grands que le paquet envoyé. Par exemple, la réponse à une requête DNS peut être entre 28 à 54 fois plus grande que la [requête](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.pdf) originale.

De cette manière, un attaquant peut envoyer de nombreux paquets plus petits et les paquets de réponse utiliseront les ressources de la cible.

## Qu'est-ce que les attaques DDoS par protocole ?

Les attaques DDoS par protocole trouvent une faiblesse dans le fonctionnement d'un protocole (comme une attaque SYN flood). Une attaque SYN flood exploite le fonctionnement d'une poignée de main en trois étapes.

Lorsque qu'un attaquant envoie un grand nombre de paquets SYN à une machine, le serveur allouera des ressources à cette requête et enverra un paquet SYN ACK en retour – en supposant qu'il s'agit du début d'une demande de connexion.

Normalement, l'autre serveur répondrait avec ACK, démarrant la connexion. En cas d'attaque, l'attaquant continue d'envoyer des requêtes SYN sans compléter la connexion, jusqu'à ce que le serveur soit à court de ressources et incapable d'accepter un trafic supplémentaire.

## Qu'est-ce que les attaques DDoS d'application ?

Les attaques DDoS d'application ciblent les faiblesses dans le fonctionnement d'une application (comme une attaque Slowloris).

Une attaque Slowloris est très similaire à une attaque SYN flood, mais cible les serveurs web. Elle se produit lorsqu'un attaquant envoie des requêtes HTTP sans les compléter, continuant (lentement) à envoyer des en-têtes supplémentaires pour maintenir la connexion ouverte.

Comme les connexions ne sont jamais complétées, elles absorbent toutes les ressources disponibles du serveur, l'empêchant de traiter les connexions légitimes.

## Autres types d'attaques DDoS

Alternativement, les attaques DDoS peuvent être regroupées en fonction de la couche du modèle OSI qu'elles impactent. Celles-ci sont généralement divisées en attaques d'infrastructure (comme les réflexions UDP et les inondations SYN) ou en attaques d'application (comme les inondations HTTP et le cache-busting).

Les inondations HTTP se produisent lorsqu'un attaquant envoie un « déluge » de requêtes HTTP qui semblent légitimes à un serveur ou une application, épuisant ses ressources.

Les attaques de cache-busting sont un sous-ensemble des inondations HTTP conçues pour éviter la mise en cache CDN en variant la chaîne de requête, de sorte que le CDN doit contacter le serveur d'origine pour chaque requête, le surchargeant ainsi.

## Mesures d'atténuation pour les attaques DDoS

La partie la plus importante de la protection contre une attaque DDoS est la préparation elle-même. Il est beaucoup plus difficile de gérer une tentative de DDoS après qu'elle ait commencé.

### Augmenter la bande passante

Une façon de gérer les attaques volumétriques est d'augmenter la bande passante en réponse. Malheureusement, cela peut être extrêmement difficile en fonction de la taille de l'attaque et de la capacité de l'attaquant à augmenter la taille de son attaque en réponse.

Sauf si l'organisation attaquée est un fournisseur de services ou une organisation extrêmement grande, il est peu probable que cela soit réaliste.

### Externaliser les réponses

Les petites organisations peuvent externaliser leurs réponses à d'autres entreprises spécialisées, ou à leur FAI (ou les deux).

Ces types de relations doivent être en place avant qu'une attaque ne se produise, afin que lorsque cela se produit, l'atténuation soit aussi simple que de contacter le FAI ou le fournisseur de services pour activer la protection (ou avoir une protection constamment activée).

Souvent, ce que le fournisseur de protection DDoS fera, c'est rediriger le trafic vers leur environnement (s'il ne passe pas déjà par leur environnement). Cela peut se faire via DNS, en mettant à jour l'enregistrement A pour pointer vers une IP que le fournisseur DDoS a allouée (bien que vous ayez besoin d'un TTL bas pour que cela prenne effet rapidement), ou BGP, en annonçant une route plus spécifique que celle actuellement annoncée.

### Avoir un plan de réponse aux incidents spécifique aux DDoS

Même si l'organisation a externalisé sa protection DDoS, avoir un plan de réponse aux incidents spécifique aux DDoS est essentiel.

Une fois qu'il a été écrit et approuvé par diverses parties prenantes, il est important de le réviser au moins annuellement (idéalement via un exercice de table) pour s'assurer que tout le monde comprend son rôle dans le plan.

Un plan de réponse spécifique aux DDoS doit inclure les éléments suivants :

#### Avant l'événement :

* **Schéma de circuit :** Créez des schémas de circuit aussi précis que possible, y compris les contacts de télécommunications.

Créez également une carte de votre propre réseau et de tous les contacts appropriés (y compris ceux qui sont capables et habilités à apporter des modifications locales, ainsi que ceux qui peuvent contacter la société de télécommunications pour apporter des mises à jour).
* **Escalade :** Déterminez quand (et comment) impliquer votre FAI ou une organisation d'atténuation DDoS (avec des contacts à jour et une copie du contrat).
* **Communication :** Développez une liste des personnes à notifier et quand (informations de contact pour l'équipe de sécurité, les contacts appropriés de l'équipe réseau, etc.).

Cela doit être divisé en deux groupes - les personnes de réponse technique (qui peuvent/doivent mettre en œuvre des changements techniques pour traiter l'attaque) et les autres (communications, juridique, etc.). Le deuxième groupe doit inclure toute personne qui pourrait devoir être impliquée, mais qui doit être sur un appel séparé des personnes techniques apportant des modifications, afin d'avoir une réponse aussi efficace que possible.

Idéalement, cela doit être imprimé et distribué, afin que les personnes aient accès même si les systèmes sont indisponibles.

Assurez-vous que votre équipe de communication a un plan pour savoir comment et quoi communiquer en cas d'incident qui met hors ligne des actifs orientés client.
* **Révision :** Ces documents et listes de contacts doivent être révisés régulièrement (au moins trimestriellement).

#### Pendant l'événement :

* **Classer un événement comme une attaque DDoS :** Il faut confirmer qu'il s'agit d'une attaque DDoS, et non d'une simple augmentation de trafic ou d'une erreur commise par quelqu'un dans le réseau. Idéalement, cela inclut également la détermination du type d'attaque en cours et de son volume.
* **Escalade :** Impliquez le responsable de l'incident afin qu'il puisse commencer à notifier les personnes nécessaires.
* **Prendre des mesures initiales :** Si possible, [sinkhole](https://www.wired.com/story/what-is-sinkholing/) le trafic. Si le trafic est supérieur à la bande passante du lien, contactez votre opérateur (qui sinkholera probablement le trafic de son côté). Simultanément, si vous avez un service d'atténuation DDoS, contactez-les également.
* **Communiquer :** Mettez en place un lien pour que les personnes techniques communiquent et que les personnes non techniques restent informées de l'incident.

Cela est particulièrement important si les services publics sont hors ligne pendant une période prolongée, car votre équipe de communication devra être à jour afin de communiquer avec les actionnaires/médias/clients.

#### Après l'événement :

* **Retour à la normale :** Quand allez-vous supprimer les mesures d'atténuation ? Qui va les approuver ?
* **Source de l'attaque :** Quelles informations pouvez-vous recueillir sur l'attaque pour l'expliquer et les attaquants derrière elle ? Était-ce une attaque ciblée ?
* **Leçons apprises :** Quelles étaient-elles ? Comment peuvent-elles être utilisées pour améliorer le plan de réponse aux incidents ?

### Construire une architecture résiliente

Concevoir des systèmes résilients nécessite un plan complet de continuité d'activité, avec les DDoS comme composante de ce plan.

Essentiellement, les mêmes principes s'appliquent aux centres de données et aux réseaux lors de la conception pour les DDoS que lors de la conception pour la continuité d'activité. Vous voulez éviter tout point de défaillance unique ou goulot d'étranglement et avoir des réseaux géographiquement diversifiés et une diversité de fournisseurs.

Les réseaux de distribution de contenu (CDN) sont un moyen d'améliorer votre réponse aux DDoS, car ils fournissent un réseau géographiquement distribué de serveurs proxy qui peuvent augmenter considérablement la résilience.

L'architecture cloud offre une amélioration significative par rapport aux anciens modèles. Elle permet aux organisations de toute taille de créer des systèmes entièrement redondants qui peuvent être activés et désactivés en un clic. Elle dispose également d'une infrastructure géographiquement diversifiée pour un coût très bas, et d'un moyen bon marché et facile de faire évoluer la capacité de charge à la hausse ou à la baisse selon les besoins.

Concevoir spécifiquement pour le cloud peut permettre aux organisations de tirer parti de ces nouveaux modèles et d'améliorer considérablement votre réponse aux DDoS.

### Mettre à niveau votre matériel

Certains types d'attaques DDoS sont très anciens et peuvent être atténués par du matériel plus récent. Par exemple, vous pouvez vous défendre contre de nombreuses attaques de protocole (comme les inondations SYN) et attaques d'application (comme Slowloris) avec des pare-feu réseau et des équilibreurs de charge appropriés.

Ces pare-feu peuvent souvent surveiller les signes de ces types d'attaques et fermer les connexions une fois qu'elles atteignent des niveaux insoutenables. L'installation du matériel correct peut atténuer les dommages qu'une attaque pourrait causer.

### Autres ressources :

* [Guide rapide sur les DDoS US CERT](https://us-cert.cisa.gov/sites/default/files/publications/DDoS%20Quick%20Guide.pdf)
* [Meilleures pratiques AWS pour la résilience aux DDoS](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.pdf)
* [Réponse aux incidents cybernétiques DDoS NCC](https://www.gov.scot/binaries/content/documents/govscot/publications/advice-and-guidance/2019/10/cyber-resilience-incident-management/documents/cyber-incident-response-denial-of-service-playbook/cyber-incident-response-denial-of-service-playbook/govscot%3Adocument/Cyber%2BCapability%2BToolkit%2B-%2BCyber%2BIncident%2BResponse%2B-%2BDenial%2Bof%2BService%2BPlaybook%2Bv2.3.pdf)
* [Playbook de réponse aux DDoS d'Imperva](https://www.cbronline.com/wp-content/uploads/dlm_uploads/2018/04/Playbook-DDoS-Response-Playbook-new-V2.pdf)
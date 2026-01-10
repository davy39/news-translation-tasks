---
title: Les plus grandes violations de données de 2020 – et ce que les développeurs
  devraient en retenir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-02T17:15:11.000Z'
originalURL: https://freecodecamp.org/news/biggest-data-breaches-lessons-learned
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/photo-1550607326-2df38662b7dc.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Web Security
  slug: web-security
seo_title: Les plus grandes violations de données de 2020 – et ce que les développeurs
  devraient en retenir
seo_desc: "By Andrej Kovacevic\n2020 was not a good year for hacks, data breaches,\
  \ and other cyber-attacks. As far as those things go, it was among the worst years\
  \ on record. \nBusinesses far and wide experienced some of the most damaging and\
  \ embarrassing hacks i..."
---

Par Andrej Kovacevic

2020 n'a pas été une bonne année pour les piratages, les violations de données et autres cyberattaques. À cet égard, ce fut l'une des pires années jamais enregistrées.

Des entreprises de tous horizons ont subi certains des piratages les plus dommageables et embarrassants imaginables l'année dernière. Et certains de ces incidents ont conduit à des échecs de sécurité graves qui pourraient avoir des implications internationales graves.

Mais malgré tous ces problèmes, certains des piratages de 2020 peuvent fournir des leçons précieuses pour les programmeurs et les ingénieurs logiciels afin de les aider à renforcer leurs produits contre les attaques futures.

Pour les aider dans cette tâche, voici un récapitulatif des plus grands piratages de 2020 et ce que les programmeurs peuvent – et doivent – en apprendre.

## Violation de la base de données d'MGM Resorts

Le premier piratage de cette liste est un peu une tricherie – car techniquement, il s'est produit en 2019. Mais je l'ai inclus ici parce que la cible de l'attaque a attendu jusqu'en février 2020 pour divulguer que quelque chose s'était même produit.

À cette époque, MGM Resorts a confirmé qu'une base de données contenant les informations personnelles de 10,6 millions de clients avait été volée dans le stockage cloud à un moment donné en 2019.

Le problème, c'est que ce n'était pas la fin de l'histoire. Plus tard dans l'année, une autre base de données a été mise en vente sur le dark web contenant un [nombre impressionnant de 142 millions d'enregistrements de clients](https://www.forbes.com/sites/leemathews/2020/07/14/mgm-142-million-guests-hacked/?sh=640b8b325294), apparemment issus de la même attaque initiale.

À cette époque, les pirates ont affirmé avoir accédé aux données en compromettant un service de cybersécurité tiers sur lequel MGM Resorts s'appuyait pour protéger leurs systèmes.

La violation était extrêmement dangereuse car le type de données divulguées devient généralement la matière première pour des attaques d'ingénierie sociale à grande échelle qui peuvent multiplier les dommages bien au-delà de la portée de l'incident initial. Et les enseignements de cette attaque sont nombreux.

Premièrement, il est essentiel que les programmeurs et les ingénieurs logiciels commencent à [faire de l'utilisation du chiffrement une priorité](https://www.wired.com/story/field-level-encryption-databases-mongobd/) chaque fois que nous stockons des données sensibles dans une base de données.

Deuxièmement, nous devons limiter la capacité des services tiers à examiner le fonctionnement interne de notre logiciel.

Et troisièmement, nous devons toujours concevoir des logiciels pour stocker le moins de données privilégiées possible. Juste ce qui est nécessaire pour fonctionner, et rien de plus.

## Piratage du NNID de Nintendo

Tout au long de cette année, la console de jeu Nintendo Switch a connu une résurgence des ventes, alimentée par les restrictions de quarantaine obligeant des millions de personnes à trouver des options de divertissement en solo.

Mais l'année a également apporté de mauvaises nouvelles pour la société de jeux bien-aimée. En avril, leur réseau de jeux en ligne a subi un piratage qui a permis aux attaquants d'[accéder à jusqu'à 300 000 comptes d'utilisateurs](https://www.theverge.com/2020/6/9/21285084/nintendo-nnid-switch-hack-accounts-affected-exposed) – options de paiement et tout.

La violation provenait de la décision de Nintendo d'autoriser les propriétaires de ses anciennes consoles, la Wii U et la Nintendo DS, à continuer à accéder à leurs comptes en ligne en utilisant une méthode de connexion obsolète.

Aggravant le problème, les propriétaires de la Switch avaient la possibilité de lier leurs anciennes connexions à leur nouveau système et de continuer à utiliser leur ancienne méthode de connexion.

La leçon ici est que les méthodes d'authentification obsolètes sont obsolètes pour une raison. Chaque fois qu'il existe une méthode de connexion plus récente et plus sécurisée, nous devons mettre à jour notre logiciel pour l'utiliser et en faire une exigence pour tous les utilisateurs.

C'est un principe fondamental des [pratiques modernes de codage sécurisé](https://vpnoverview.com/internet-safety/business/what-is-secure-coding/), et aucune quantité de grognements d'utilisateurs ne devrait être suffisante pour empêcher la marche constante du progrès de la sécurité logicielle.

## Piratage de SolarWinds Orion

Dans ce qui a été décrit par des experts comme la plus grande violation de sécurité de l'histoire, la plateforme d'administration informatique SolarWinds a [subi une violation de sécurité dévastatrice](https://www.businessinsider.com/solarwinds-hack-explained-government-agencies-cyber-security-2020-12) à la fin de cette année.

Mais le piratage en lui-même n'était pas la partie notable. C'est que les pirates ont réussi à infecter les mises à jour logicielles Orion de SolarWinds avec un malware sur mesure qui a créé un accès par porte dérobée dans tout système que ces mises à jour ont atteint.

Et ils ont atteint des cibles de grande valeur – 18 000 au total. Parmi eux se trouvaient presque toutes les agences gouvernementales américaines, Cisco Systems, Microsoft et d'innombrables autres organisations bien connues.

L'attaque, qui a été exécutée par le Service de renseignement extérieur de la Russie, est à la fois de grande portée et massivement dommageable. Et elle sonne également un avertissement clair pour les programmeurs et les développeurs de logiciels.

Cet avertissement est simple. Ce n'est pas chaque tentative d'accès aux systèmes protégés qui viendra d'une attaque frontale sur un logiciel individuel. Les pirates cibleront presque toujours le fruit le plus facile à atteindre pour obtenir un accès privilégié aux réseaux, qu'ils peuvent ensuite utiliser pour contourner la sécurité et les contrôles d'accès.

Ainsi, à l'avenir, les développeurs de logiciels devront commencer à [appliquer les principes de confiance zéro](https://searchsecurity.techtarget.com/tip/Zero-trust-framework-creates-challenges-for-app-dev) à leur code pour s'assurer que les échecs de sécurité de quelqu'un d'autre ne deviennent pas leurs vols massifs de données.

## Vol des outils Red Team de FireEye

Le dernier piratage de la liste est important car il pourrait devenir le carburant des défis de cybersécurité de 2021.

En décembre 2020, la société de cybersécurité FireEye a annoncé qu'elle avait été la cible d'une autre opération de piratage parrainée par la Russie. Cette fois, les attaquants ont pénétré et [volé les outils mêmes que FireEye utilise](https://www.nytimes.com/2020/12/08/technology/fireeye-hacked-russians.html) pour tester les réseaux clients pour les vulnérabilités.

Les outils Red Team, comme on les appelle, sont composés de certains des extraits de malware les plus méchants et les plus dangereux jamais publiés dans la nature. Ils testent essentiellement si les systèmes ciblés sont toujours vulnérables à des failles de sécurité connues et à d'autres techniques d'attaque.

Mais maintenant qu'ils sont entre les mains d'un groupe qui n'hésitera pas à les utiliser dans des tentatives de piratage réelles, le paysage mondial des menaces numériques est devenu beaucoup plus sombre.

Ce n'est pas parce que les outils représentent des menaces inconnues, mais qu'ils rendront possible pour les attaquants de déguiser leurs traces, rendant la détection et l'analyse médico-légale plus difficiles.

Mais il y a aussi une leçon à tirer de cela. C'est que ces menaces n'ont pas à rester un problème. Et c'est à nous, en tant que programmeurs et développeurs de logiciels, de nous assurer qu'ils ne sont plus un danger en restant à jour et en corrigeant toutes ces vulnérabilités connues dans notre code. De cette façon, les mauvais hackers devront trouver de nouvelles tactiques plutôt que de recycler les anciennes.

## Nouvelle année, défis plus grands

Même si 2020 a été une année aussi difficile pour la cybersécurité que n'importe quelle autre année enregistrée, 2021 s'annonce encore plus difficile.

Avec des outils de piratage haut de gamme dans la nature, des États-nations escaladant leurs attaques numériques et des cybercriminels encore plus déterminés à prendre ce qui ne leur appartient pas, il y a de fortes chances que nous soyons en pour une autre année longue et difficile.

Mais si les programmeurs et les développeurs de logiciels tirent les leçons de cette année et les appliquent à leur travail à l'avenir, il y a de fortes chances que la situation de sécurité s'améliore considérablement.

Et même s'il n'existe pas de sécurité à toute épreuve, nous pouvons tous faire notre part pour rendre le travail des hackers black hat beaucoup plus difficile – et cela vaut bien la peine de faire un effort pour y parvenir.
---
title: Types de Hackers – Et Comment s'en Défendre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T02:44:00.000Z'
originalURL: https://freecodecamp.org/news/types-of-hackers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9694740569d1a4ca11c6.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Types de Hackers – Et Comment s'en Défendre
seo_desc: "By Megan Kaczanowski\nIf you want to protect systems, you need to understand\
  \ whom you’re defending them from. \nMany of the attackers you’ll face will fall\
  \ into several different groups. These different groups often use very different\
  \ tactics, techniqu..."
---

Par Megan Kaczanowski

Si vous souhaitez protéger des systèmes, vous devez comprendre contre qui vous les défendez.

De nombreux attaquants auxquels vous serez confrontés appartiendront à plusieurs groupes différents. Ces différents groupes utilisent souvent des tactiques, techniques et procédures (TTP) très différentes pour attaquer les systèmes.

Identifier quels acteurs ou groupes d'acteurs peuvent cibler vos systèmes peut aider à prioriser les mesures d'atténuation les plus importantes.

## Script Kiddies :

Les script kiddies sont des hackers techniquement inexpérimentés. Souvent, ils sont jeunes, voire adolescents. Ils ne savent pas écrire leur propre code ou exploits, mais peuvent utiliser des outils développés par d'autres. Ils sont souvent motivés par le plaisir.

Ils utilisent couramment des attaques de phishing, des outils achetés à d'autres sur des marchés du dark web, ou des outils gratuits. Ils ont été associés à des piratages de sociétés de jeux vidéo, [comme celui-ci](https://www.wired.com/story/xbox-underground-videogame-hackers/).

## Cybercriminels :

Les cybercriminels varient en sophistication technique, allant des script kiddies aux gangs organisés, où chaque membre joue un rôle différent dans le cercle de cybercriminalité. Ils sont responsables de la [majorité](https://enterprise.verizon.com/resources/reports/dbir/) des violations de données et sont principalement motivés par l'argent. Ils sont connus pour la fraude aux distributeurs automatiques de billets (« jackpotting »), le vol de cartes de crédit et de cartes-cadeaux, les ransomwares et le vol de données (entre autres attaques).

L'attaque la plus courante des cybercriminels est les campagnes de phishing de masse, car celles-ci peuvent être utilisées pour distribuer des ransomwares ou permettre le vol de données. Lorsqu'un utilisateur imprudent clique sur le lien ou ouvre la pièce jointe, un ransomware (logiciel malveillant qui bloquera ses fichiers jusqu'à ce qu'il paie une rançon (généralement en monnaie numérique)) infectera sa machine.

Alternativement, le lien de phishing peut demander les identifiants d'un utilisateur (nom d'utilisateur et mot de passe) et utiliser ces informations pour voler des informations ou faire chanter l'utilisateur.

Les campagnes de phishing à grande échelle comme celle-ci sont très faciles à exécuter sur le plan technique et sont [extrêmement](https://www.businessinsider.com/scammers-squeezed-330000-people-webcam-porn-2019-2) [rentables](https://thenextweb.com/hardfork/2019/02/22/bitcoin-sex-scam-blackmailers/).

Se protéger contre les cybercriminels consiste généralement à être plus sécurisé que ses « voisins », car les cybercriminels recherchent la cible la plus facile.

Le filtrage automatique des spams, l'analyse des pièces jointes et des liens dans les e-mails, ainsi que des mesures telles que DMARC, SPF et DKIM peuvent aider à réduire le nombre d'e-mails de phishing livrés à vos utilisateurs. Les programmes de sensibilisation à la sécurité peuvent également aider les utilisateurs à identifier les e-mails de phishing manqués par les filtres et à les signaler à votre équipe de sécurité.

Au cours des dernières années, cela a quelque peu changé, car la [chasse aux gros gibiers](https://arstechnica.com/information-technology/2019/10/fbi-warns-of-major-ransomware-attacks-as-criminals-go-big-game-hunting/) est devenue plus populaire.

Essentiellement, cela se produit lorsque des cybercriminels choisissent une grande entité (souvent une qui a une faible tolérance aux temps d'arrêt) à cibler et passent des semaines ou des mois à travailler pour pénétrer dans le réseau de la cible, en recherchant spécifiquement des actifs de grande valeur.

Ils déploient ensuite un ransomware et utilisent l'incapacité de l'entreprise à gérer les temps d'arrêt pour négocier une rançon (en plus d'exfiltrer des données et d'utiliser la menace de fuite de ces données pour inciter une entreprise à payer la rançon).

Les criminels tendent à être relativement sophistiqués, privilégiant la discrétion. Se protéger contre ces groupes est beaucoup plus difficile et dépend d'une défense en couches (mécanismes de protection et d'alerte multiples afin de protéger les systèmes, détecter les intrusions et atténuer les vulnérabilités).

## Hacktivistes :

Les hacktivistes sont motivés par des causes (politiques, économiques, religieuses, etc.). Certains de ces acteurs agissent seuls, et d'autres font partie de groupes tels que [Anonymous](https://www.wired.com/2011/11/anonymous-101/) (connu pour une série d'attaques contre l'Église de Scientologie).

Ces groupes utilisent souvent des attaques DDoS (déni de service distribué) et des défacements de sites web. Une attaque DDoS se produit lorsqu'un attaquant submerge un serveur avec tant de requêtes qu'il est incapable de gérer le trafic et plante (souvent en utilisant un botnet). Les défacements de sites web se produisent lorsqu'un groupe supprime le message ou les images actuellement affichés sur un site web et les remplace par les siens.

Les hacktivistes ne sont généralement pas motivés par l'argent ou le vol de données (sauf s'ils pensent que la divulgation des données incriminera ou embarrassera la cible), mais veulent plutôt diffuser leur message ou publiciser leur cause.

Se protéger contre ces attaques consiste à analyser les sites web publics pour détecter les vulnérabilités, à avoir une équipe de réponse aux incidents (et un plan de réponse aux incidents !) et à mettre en place des protections pour atténuer les pics de trafic (par exemple, Amazon Shield pour AWS).

## Menace interne :

La menace interne peut être divisée en deux groupes : les initiés malveillants et les initiés accidentels.

* Les initiés malveillants sont ceux qui ont été compromis par un tiers, ou qui ont décidé de voler à l'organisation pour un gain personnel. Les personnes en colère d'avoir été licenciées ou d'avoir manqué une promotion et qui veulent se venger, ou qui tentent de voler des informations pour du délit d'initié sont des initiés malveillants.
* Les initiés accidentels incluent ceux qui ont cliqué sur un lien de phishing (et ont vu leur compte compromis), qui ont mal configuré une base de données, ou qui ont accidentellement envoyé des informations sensibles à la mauvaise personne.

Quelles que soient les motivations d'un initié, ils représentent l'une des [plus](https://www.sentinelone.com/blog/top-7-most-disturbing-data-breaches-in-2018/) [dangereuses](https://www.venafi.com/blog/deciphering-how-edward-snowden-breached-the-nsa) [menaces](https://www.observeit.com/blog/5-examples-of-insider-threat-caused-breaches/) pour toute [organisation](https://www.csoonline.com/article/3263799/insider-threat-examples-7-insiders-who-breached-security.html). La principale préoccupation concernant les menaces internes devrait être le vol de données, car l'information est généralement la cible de ce type d'attaques.

Se défendre contre les menaces internes devrait être largement motivé par la sensibilisation à la sécurité. Les gens veulent être utiles, ce qui est un trait que les hackers exploiteront par le biais d'attaques d'ingénierie sociale pour obtenir des informations.

Les programmes de sécurité utilisent généralement des formations en sécurité, des programmes de Security Champions et des initiatives de sensibilisation pour éduquer leurs employés sur cette menace. De plus, une surveillance complète des réseaux internes pour détecter les comportements inhabituels (souvent en utilisant l'analyse du comportement des utilisateurs) peut vous aider à identifier et à atténuer les menaces internes.

## Attaquants étatiques :

En 2018, les attaquants étatiques n'étaient responsables que de 12 % de toutes les violations de données ([Rapport sur les violations de données de Verizon](https://enterprise.verizon.com/resources/reports/dbir/)). Cependant, ils sont généralement bien formés, bien financés et extrêmement motivés.

Contrairement aux initiés (qui sont souvent mal formés) ou aux cybercriminels (qui ne sont généralement pas motivés pour attaquer des cibles spécifiques), une fois que les attaquants étatiques (également connus sous le nom d'APT, ou Advanced Persistent Threats) ont ciblé votre organisation, il est peu probable qu'ils s'arrêtent avant d'avoir pénétré l'organisation.

Ces types d'attaquants sont souvent des employés salariés, employés par des agences de renseignement du monde entier. Les objectifs des États-nations varient selon les pays, mais sont généralement conçus pour faire avancer les objectifs politiques et économiques du pays.

Ces attaquants sont connus pour une gamme de tactiques (tout ce qui peut les aider à compromettre votre organisation), mais ont été connus pour utiliser des attaques de phishing ciblées, des logiciels malveillants personnalisés et des attaques zero-day.

Contrairement aux cybercriminels qui veulent monétiser rapidement les actifs, les attaquants étatiques chercheront souvent un accès à long terme à votre infrastructure. Ils feront de leur mieux pour obtenir un accès initial discrètement (et par plusieurs points d'entrée), puis se déplaceront discrètement à travers vos réseaux, en cartographiant autant que possible. Ainsi, ils sont moins susceptibles d'être attrapés, plus susceptibles de trouver leur cible et d'exfiltrer des données sans être attrapés.

Se protéger contre ces organisations dépend de solides fondamentaux de sécurité dans toute votre organisation (tels que des programmes de gestion des correctifs et des vulnérabilités, des programmes de sensibilisation à la sécurité, de surveillance et de détection, et une réponse efficace aux incidents, entre autres), et des protections plus avancées (telles que le renseignement sur les menaces, qui peut vous aider à identifier les acteurs de menace qui peuvent cibler votre organisation).

## Pourquoi est-il important de savoir quel type d'attaquants cible mon organisation ?

Étant donné que les ressources ne sont pas infinies, chaque programme de sécurité doit prioriser certaines protections par rapport à d'autres et ne peut pas se protéger efficacement contre toutes les attaques. Ils peuvent également avoir une capacité limitée à mettre en œuvre des contrôles en fonction des besoins de l'entreprise.

Une équipe de sécurité efficace doit choisir comment dépenser son influence judicieusement lors de la recommandation d'un outil de sécurité.

Étant donné cela, une philosophie pour choisir quels contrôles prioriser est de réaliser une « modélisation des menaces ».

À un niveau très élevé, la modélisation des menaces est conçue pour déterminer les actifs les plus précieux de l'organisation (ou « joyaux de la couronne ») et identifier les acteurs de menace (à la fois par type de haut niveau, et même des groupes spécifiques) qui sont les plus susceptibles d'attaquer l'organisation. Cela peut également impliquer de déterminer quelles attaques, ou types d'attaques, l'organisation est susceptible de rencontrer.

Ces informations peuvent aider l'équipe de sécurité à déterminer quels contrôles seront les plus efficaces pour leur environnement et fourniront la plus grande protection pour le coût. Ensuite, l'équipe peut prioriser les mesures de sécurité les plus importantes pour leur environnement, et utiliser au mieux les ressources limitées et l'influence limitée pour protéger leur environnement contre les menaces les plus probables.
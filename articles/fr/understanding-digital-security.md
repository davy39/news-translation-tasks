---
title: Guide du débutant pour la sécurité numérique – Comment se protéger en ligne
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-01-06T18:09:40.000Z'
originalURL: https://freecodecamp.org/news/understanding-digital-security
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-207580--2-.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
- name: Security
  slug: security
seo_title: Guide du débutant pour la sécurité numérique – Comment se protéger en ligne
seo_desc: "Whatever your connection to technology, security should play a prominent\
  \ role in the way you think and act. \nTechnology, after all, amplifies the impact\
  \ of everything we do with it. The things we say and write using communication technologies\
  \ can be ..."
---

Quelle que soit votre relation avec la technologie, la sécurité devrait jouer un rôle prépondérant dans votre façon de penser et d'agir. 

La technologie, après tout, amplifie l'impact de tout ce que nous faisons avec elle. Les choses que nous disons et écrivons en utilisant les technologies de communication peuvent être lues et entendues par beaucoup plus de personnes que ce ne serait possible sans elles. 

La capacité à se connecter facilement avec les gens et à collaborer sur des projets de toutes sortes est bien plus grande. 

Les tâches que nous pouvons accomplir, grâce à la magie de l'automatisation, sont presque illimitées. La quantité d'informations auxquelles nous pouvons accéder instantanément via les appareils les plus simples et les moins chers dépasse de loin tout ce que les plus grands érudits auraient pu espérer voir de leur vivant il y a quelques décennies.

Tout cela signifie que les criminels et autres individus non contraints par une conscience morale auront des outils encore plus puissants pour compromettre les données que vous créez et consommez, et voler ou endommager les biens que vous acquérez. 

Vous avez donc un fort intérêt à apprendre comment vous protéger, vous, vos biens, et ceux des personnes et organisations qui vous entourent.

Ce tutoriel (tiré de mon livre, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb)) présentera un bref aperçu de ce qui est en jeu dans le domaine de la sécurité technologique. 

Nous définirons les types de menaces auxquelles nous sommes confrontés et discuterons des outils clés à notre disposition pour repousser ces menaces.

Si vous êtes intéressé à approfondir le sujet, mon livre LPI Security Essentials est entièrement consacré à vous donner une vue d'ensemble complète.

Si vous préférez regarder ce chapitre sous forme de vidéo, n'hésitez pas à suivre ici :

%[https://www.youtube.com/watch?v=OJf27vq_PTo]

# Piratage ? Qu'est-ce que le piratage ?

Définir le piratage informatique de manière à ne pas mécontenter quelqu'un, quelque part, c'est comme parler de politique au travail. Préparez-vous à de longs silences gênants et éventuellement à de la violence. 

Vous voyez, les puristes pourraient insister sur le fait que le terme piratage devrait s'appliquer exclusivement aux individus qui se concentrent sur la réutilisation forcée du matériel informatique à des fins non standard. 

D'autres réservent ce titre aux personnes qui contournent les contrôles d'authentification pour s'introduire dans les réseaux à des fins criminelles ou politiques. 

Et que dire de ceux qui portent ce titre comme signe de leur expertise pratique en toutes choses informatiques ? (Et puis, bien sûr, il y a les crackers.)

Mais c'est mon livre, donc je vais utiliser le terme comme je veux. Je décrète donc que le piratage concerne tous les plans que les méchants ont pour vos appareils numériques. Plus précisément, leurs plans pour entrer sans autorisation, sortir sans être remarqués, et (parfois) prendre vos affaires avec eux lorsqu'ils partent. 

Utiliser le terme de cette manière nous donne un moyen utile d'organiser une discussion sur certaines menaces courantes et particulièrement effrayantes.

## Comment les pirates entrent dans votre système

Le truc est de trouver un moyen de passer à travers vos défenses (comme les mots de passe, les pare-feu et les barrières physiques). Dans la plupart des cas, les mots de passe fournissent probablement la protection la plus faible :

* Les mots de passe sont souvent courts, utilisent une gamme limitée de caractères et sont faciles à deviner.
* Si un appareil est livré avec un mot de passe par défaut simple (comme "admin" ou "1234") destiné uniquement à vous permettre de vous connecter pour la première fois, alors les chances sont assez bonnes que de nombreux utilisateurs ne prendront jamais la peine de le remplacer par quelque chose de mieux.
* Même les mots de passe forts peuvent être volés par des escroqueries par e-mail de phishing trompeuses ("Cliquez ici pour vous connecter à votre compte bancaire..."), de l'ingénierie sociale ("Bonjour, c'est Ed de l'IT. Nous avons un problème avec votre compte d'entreprise. Pourriez-vous me donner votre mot de passe par téléphone pour que je puisse le réparer rapidement ?"), et des logiciels de suivi de clavier.

Nous parlerons plus des pare-feu plus tard dans ce tutoriel. Et les barrières physiques ? Je pense que vous savez déjà à quoi ressemble une porte verrouillée. Mais il vaut probablement la peine de passer quelques instants à réfléchir à d'autres types d'attaques numériques.

Le gros lot est généralement d'accéder à vos données et de s'enfuir avec des copies. Mais pour certains, détruire simplement les originaux peut être tout aussi satisfaisant.

Évidemment, se connecter à vos appareils en utilisant des mots de passe volés est l'approche la plus directe. Mais l'accès peut également être obtenu en interceptant vos données lorsqu'elles voyagent sur un réseau non sécurisé. 

Une approche couramment utilisée ici est connue sous le nom d'attaque de l'homme du milieu. C'est là où les paquets de données peuvent être interceptés en transit et altérés sans que les utilisateurs autorisés à chaque extrémité ne sachent qu'il y a un problème. 

Le chiffrement correct de vos connexions réseau (et l'évitement des réseaux publics non sécurisés) est une protection efficace contre ce type de menace. Nous parlerons plus du chiffrement un peu plus tard.

Si le matériel que vous utilisez a une "porte dérobée" non documentée intégrée, alors vous êtes pratiquement perdu quoi que vous fassiez. Nous parlerons plus des portes dérobées plus tard dans le livre, mais pour l'instant, je noterai simplement qu'il n'a pas manqué d'ordinateurs portables, de serveurs en rack et même d'équipements de réseau haut de gamme fournis par les fabricants qui ont été intentionnellement conçus pour inclure des vulnérabilités d'accès sérieuses. Soyez très prudent quant à l'endroit où vous achetez vos appareils informatiques.

Si les attaquants trouvent un moyen d'entrer dans votre bâtiment physique (parfois en se faisant passer pour des employés d'une société de livraison), ils pourraient discrètement brancher un minuscule dispositif d'écoute dans une prise Ethernet inutilisée de votre réseau. Cela leur donnera une belle plateforme pour observer et même influencer toutes vos activités de l'intérieur. 

Protéger votre infrastructure physique et surveiller attentivement l'activité du réseau est votre meilleur espoir contre ce type d'intrusion.

Même si votre domicile ou votre bureau est entièrement fortifié, il n'y a aucune garantie que les données circulant sur les appareils mobiles (comme les smartphones ou les ordinateurs portables) ne tomberont pas entre de mauvaises mains. 

Et même si vous avez été prudent en utilisant uniquement les meilleurs mots de passe pour ces appareils, les disques de données eux-mêmes peuvent encore être facilement montés comme des partitions externes sur la machine d'un voleur. Une fois montés, vos fichiers et informations de compte seront désormais largement ouverts. 

La seule façon de protéger vos appareils mobiles contre ce type de menace est de chiffrer l'ensemble du disque à l'aide d'une phrase de passe forte.

## Ce que les pirates recherchent

Maintenant que des économies entières sont gérées par des ordinateurs directement connectés à des réseaux publics, il y a de l'argent et de la valeur à gagner grâce à des efforts bien planifiés d'espionnage corporatif, académique ou politique... et grâce au vol traditionnel à l'ancienne. 

Que l'objectif soit de construire un avantage militaire ou commercial concurrentiel, de détruire complètement la concurrence, ou simplement de mettre la main sur de l'argent "gratuit", l'accès illégal aux données d'autres personnes n'a jamais été aussi facile.

Alors, que recherchent probablement les pirates ? Toutes les informations financières importantes et autres informations sensibles que vous préféreriez qu'ils n'aient pas. Y compris, il faut le noter, le type d'informations que vous utilisez pour vous identifier auprès des banques, des sociétés de cartes de crédit et des agences gouvernementales. 

Une fois que les méchants ont obtenu des points de données importants comme votre date de naissance, votre adresse domicile, les numéros d'identification émis par le gouvernement, et quelques détails bancaires de base, il est généralement facile de se présenter comme si c'était vous, prenant complètement le contrôle de votre identité dans le processus.

Les attaques numériques peuvent également être utilisées comme chantage pour forcer les victimes à payer pour annuler les dommages qu'elles ont causés. 

C'est l'objectif de la plupart des attaques de ransomware, où les pirates chiffrent toutes les données sur les ordinateurs d'une victime et refusent d'envoyer les clés de déchiffrement nécessaires pour restaurer votre accès légitime, sauf si vous leur envoyez beaucoup d'argent. 

De telles attaques ont déjà effectivement mis hors service des infrastructures critiques comme les systèmes informatiques alimentant les hôpitaux et les villes.

La meilleure défense contre les ransomware est d'avoir des sauvegardes complètes et testées de vos données critiques et un système fiable pour les restaurer rapidement sur votre matériel. Ainsi, si vous êtes un jour victime d'une attaque de ransomware, vous pouvez simplement effacer votre logiciel existant et le remplacer par des copies fraîches, peuplées de vos données sauvegardées. 

Mais vous devriez également renforcer vos paramètres de sécurité généraux pour rendre plus difficile l'accès des pirates de ransomware à votre système en premier lieu.

Lorsque leur objectif principal est de vous empêcher, vous ou votre organisation, de vaquer à vos occupations, les pirates peuvent rester à une distance sûre et lancer une attaque par déni de service distribué (DDoS) contre votre infrastructure web. 

Les attaques DDoS historiques ont utilisé des essaims massifs de milliers d'appareils connectés au réseau, piratés illégalement, pour transmettre des nombres paralysants de requêtes contre un seul service cible. Lorsqu'elles sont suffisamment importantes, les attaques DDoS ont réussi à mettre hors service même de grandes entreprises à l'échelle de l'entreprise utilisant des défenses sophistiquées pendant des heures à la fois. 

Le site hébergeant l'une de mes collections open source en ligne préférées a été durement touché il y a plus d'un an et ne s'en est toujours pas complètement remis.

# Qu'est-ce que le chiffrement ?

Si vos données sont illisibles, il y a beaucoup moins de mauvaises choses que les individus non autorisés pourront faire avec elles. Mais si elles sont illisibles, il y a probablement beaucoup de choses que vous ne pourrez pas faire avec elles non plus. 

Ne serait-il pas agréable s'il y avait un moyen de présenter vos données comme illisibles dans tous les scénarios sauf lorsqu'il y a une raison légitime ? Eh bien, devinez quoi ? Il y en a un, et il s'appelle le chiffrement des données.

## Comment chiffrer les données en transit

Les algorithmes de chiffrement encodent les informations de manière à ce qu'elles soient difficiles, voire impossibles, à lire. 

Un exemple simple (et ancien) est le remplacement de symboles, où chaque lettre "a" dans un message serait remplacée par, disons, la lettre trois positions plus loin dans l'alphabet (ce qui serait "d"). Chaque "b" deviendrait "e" et ainsi de suite. "Hello world" deviendrait "khoor zruog". Les personnes rencontrant ensuite le message seraient incapables de le comprendre.

Bien sûr, il ne faudrait pas longtemps à un ordinateur moderne (ou même à un enfant de 8 ans intelligent) pour décoder celui-ci. Mais certains cryptologues très intelligents ont travaillé dur pendant la majeure partie du siècle dernier pour produire des algorithmes beaucoup plus efficaces. 

Il existe certaines variations significatives de la cryptographie moderne. Mais l'idée générale est que les personnes peuvent appliquer un algorithme de chiffrement à leurs données, puis transmettre en toute sécurité la copie chiffrée sur des réseaux non sécurisés. Ensuite, le destinataire peut appliquer une clé de déchiffrement de quelque sorte aux données, restaurant la version originale.

Le chiffrement est désormais largement disponible pour de nombreuses activités courantes, y compris l'envoi et la réception d'e-mails. Vous pouvez également vous assurer que les données que vous demandez à un site web sont les mêmes données qui sont finalement affichées dans votre navigateur en vérifiant l'icône de cadenas dans la barre d'adresse de votre navigateur. L'icône confirme que le serveur du site web utilise le chiffrement Transport Layer Security (TLS).

Au cours des dernières années, le projet Let's Encrypt (letsencrypt.org) a encouragé des millions de nouveaux sites web à utiliser le chiffrement en fournissant des certificats de chiffrement gratuits et des outils simples à utiliser pour aider les administrateurs de serveurs à les installer.

## Comment chiffrer les données au repos

Le TLS protégera vos données lorsqu'elles sont en déplacement, mais qu'est-ce qui les gardera en sécurité même lorsqu'elles se reposent sur leur disque de stockage confortable ? Le chiffrement de fichiers et de disques, c'est ça. 

Tous les systèmes d'exploitation offrent désormais un logiciel intégré pour chiffrer tout ou partie d'un disque de stockage, soit au moment de l'installation, soit plus tard. Chaque fois que vous allumez un disque chiffré, vous serez invité à entrer la phrase de passe que vous avez créée lorsque vous avez activé le chiffrement.

Le problème est que si vous oubliez votre phrase de passe, vous êtes pratiquement verrouillé en permanence hors de votre système et les données sont aussi bonnes que perdues pour toujours. 

Mais l'autre problème est que si vous ne chiffrez pas votre système, alors, comme nous l'avons noté précédemment, toute personne qui vole le matériel aura un accès facile et instantané à vos informations privées. C'est un monde difficile, n'est-ce pas ?

# Que fait un pare-feu ?

Vous pouvez penser à un pare-feu comme à un filtre. Tout comme, par exemple, un filtre à eau est capable de bloquer certaines impuretés, ne laissant passer que l'eau propre, un pare-feu peut inspecter chaque paquet de données entrant ou sortant de votre infrastructure, bloquant l'accès lorsque cela est approprié. 

Outre le fait de ne pas devoir être remplacé toutes les quelques semaines, le grand avantage d'un pare-feu par rapport à un filtre à eau est qu'il peut être configuré de près pour permettre et refuser l'entrée de manière à correspondre exactement à vos besoins de sécurité et fonctionnels. Ensuite, vous pouvez le mettre à jour plus tard si vos besoins changent.

## Pare-feu matériels

Un pare-feu matériel est un appareil de réseau physique conçu à cet effet, couramment utilisé dans les environnements d'entreprise. De tels pare-feu sont installés à la périphérie d'un réseau privé et configurés pour bloquer le trafic entrant potentiellement dangereux, rediriger d'autres trafics vers des destinations distantes, ou permettre au trafic d'accéder aux hôtes au sein du réseau local.

Les pare-feu matériels sont vendus par des entreprises comme Cisco et Juniper, et des fabricants d'équipements généraux comme HP et Dell. Ils peuvent être utilisés pour gérer le trafic de réseaux composés de milliers d'hôtes. 

Les appareils de pare-feu ont tendance à être très coûteux, coûtant souvent plusieurs milliers de dollars. Ils ne sont normalement déployés que pour gérer l'infrastructure d'entreprise.

## Pare-feu logiciels

Un pare-feu logiciel est une application qui s'exécute sur un PC ordinaire et peut effectuer presque toutes les fonctions que vous attendriez d'un pare-feu matériel. Il y a deux différences importantes :

* Le logiciel de pare-feu (comme l'utilitaire iptables de Linux) est souvent gratuit et, bien que compliqué, bénéficie de vastes ressources de documentation. Le logiciel peut également être installé sur n'importe quel vieux PC qui traîne, réduisant le coût global à presque rien.
* Vous ne voudrez pas utiliser un tel pare-feu dans un environnement professionnel occupé, car un tel PC n'aura probablement pas la puissance de calcul pour gérer de grands volumes de trafic réseau. De plus, dans la plupart de ces cas, il ne sera pas assez fiable pour fournir des services critiques 24h/24 et 7j/7.

Il existe une autre variante de pare-feu logiciel qui est utilisée dans le cadre des systèmes d'exploitation grand public. De tels pare-feu vous permettent de mieux sécuriser votre système d'exploitation en définissant des règles pour les types d'activités que vous souhaitez autoriser. Ceux-ci peuvent être particulièrement utiles pour les appareils mobiles qui passent fréquemment d'un réseau à l'autre.

Les plateformes de cloud computing – comme Amazon Web Services (AWS) et Microsoft's Azure – fournissent une technologie de type pare-feu pour une utilisation avec les ressources que vous pourriez déployer dans leurs systèmes. Les politiques de pare-feu peuvent exister dans des objets avec des noms comme "groupe de sécurité" ou "liste de contrôle d'accès" qui peuvent être appliqués à toute ressource nécessitant ces politiques.

# Qui fait le mieux la sécurité ?

Dans un passé pas trop lointain, on entendait souvent des professionnels de l'informatique jurer qu'ils ne feraient jamais fonctionner leurs opérations informatiques sur une infrastructure qu'ils ne contrôlaient pas physiquement. Cela était courant lorsqu'il s'agissait de sous-traiter à des entreprises tierces, hors site, ou à des plateformes de cloud computing. 

Que ce soit parce que ces administrateurs ne faisaient pas confiance à la fiabilité et à la sécurité de l'infrastructure informatique gérée par des inconnus, ou parce que des restrictions réglementaires exigeaient que les charges de travail sensibles restent locales, ce sentiment était largement partagé. Et cela avait du sens.

Mais le passé est un pays étranger. Aujourd'hui, il peut être affirmé avec force que les environnements les plus sécurisés et fiables peuvent être trouvés chez les plus grands fournisseurs de cloud public. 

Pourquoi ? Ils ont l'argent et l'incitation à embaucher les meilleurs ingénieurs, et l'argent et l'incitation à construire la meilleure infrastructure. 

Au-delà de cela, les fournisseurs de cloud maintiennent des centres de données dans des juridictions politiques à travers le monde, et font de grands efforts pour garantir que leurs déploiements respectent les normes de l'industrie et du gouvernement.

Permettez-moi d'illustrer. Vous vous souvenez de la menace DDoS dont nous avons discuté un peu plus tôt dans le chapitre ? Eh bien, [à l'été 2020](https://www.zdnet.com/article/aws-said-it-mitigated-a-2-3-tbps-ddos-attack-the-largest-ever), une organisation non nommée déployant des ressources sur AWS a été frappée par une attaque DDoS culminant à 2,3 Tbps. C'est-à-dire que chaque seconde, des requêtes frappaient le service public de cette organisation avec 2,3 téraoctets de données.

Que signifie réellement "2,3 téraoctets" ? Eh bien, un mégaoctet est (environ) un million d'octets d'informations (une version PDF de ce livre prendrait probablement six mégaoctets ou plus). Un gigaoctet est mille millions d'octets d'informations. Un téraoctet est mille mille millions d'octets d'informations. Cela équivaudrait à environ 165 000 livres PDF. 2,3 téraoctets équivaudraient à environ 380 000 livres PDF.

Maintenant, essayez d'imaginer tous les caractères de texte utilisés pour remplir 380 000 livres PDF étant lancés sur un service web chaque seconde.

Vous avez cette image en tête ? Maintenant, voici ce qui est arrivé à ce service web : Rien. Il a simplement continué à fonctionner comme si de rien n'était. Comment est-ce même possible ? Le service AWS Shield d'Amazon a simplement atténué l'attaque. Le client n'a rien eu à faire.

Voilà pourquoi le déplacement de vos charges de travail vers le cloud public n'implique pas nécessairement de compromettre vos normes.

## Merci d'avoir lu !

Des vidéos YouTube de tous les dix chapitres de ce livre sont [disponibles ici](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Beaucoup plus de bonnes choses technologiques – sous forme de livres, de cours et d'articles – [peuvent être trouvées ici](https://bootstrap-it.com). Et envisagez de profiter de [mes ressources LPI Essentials ici](https://bootstrap-it.com/lpi-essentials/).
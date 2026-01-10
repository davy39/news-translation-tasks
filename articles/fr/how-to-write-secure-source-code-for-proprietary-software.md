---
title: Comment écrire un code source sécurisé pour les logiciels propriétaires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-05T14:53:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-secure-source-code-for-proprietary-software
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/software-development-code-security.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Comment écrire un code source sécurisé pour les logiciels propriétaires
seo_desc: 'By Andrej Kovacevic

  As software developers working on proprietary software, it''s our job to create
  programs that provide the functionality our clients need. And it''s also our job
  to create those programs in a way that makes them easy to use, maintain...'
---

Par Andrej Kovacevic

En tant que développeurs de logiciels travaillant sur des logiciels propriétaires, notre travail consiste à créer des programmes qui offrent les fonctionnalités dont nos clients ont besoin. Et c'est aussi notre travail de créer ces programmes de manière à les rendre faciles à utiliser, à maintenir et à mettre à niveau.

Mais les développeurs de logiciels propriétaires ont une autre responsabilité, bien plus conséquente. Nous devons créer des logiciels qui sont sécurisés et qui ne mettent pas en danger les données des utilisateurs ou les systèmes de nos clients.

Et la clé pour y parvenir est de renforcer notre code source et de resserrer nos processus de développement pour empêcher les acteurs malveillants d'injecter quoi que ce soit de nuisible pendant que nous travaillons.

Ces types d'efforts sont cruciaux car le code source est le composant de base d'un programme informatique, nous devons donc le protéger contre toute altération non autorisée.

Cet article expliquera pourquoi la sécurisation du code source est si importante pour les projets de logiciels propriétaires. Il donnera également aux programmeurs quelques conseils sur la sécurisation de leur code source, ainsi que quelques orientations sur la protection contre les altérations extérieures pendant le processus de développement.

## Pourquoi est-il important de sécuriser votre code source ?

L'utilisation de code open source dans le développement de logiciels propriétaires est en plein essor. Selon les dernières estimations, jusqu'à [96 % des logiciels propriétaires](https://www.perforce.com/blog/vcs/using-open-source-code-in-proprietary-software) contiennent du code open source. Les développeurs utilisent ces morceaux de code pour accélérer le processus de développement et éviter un travail inutile. Et d'un point de vue sécurité, c'est une bonne chose.

Selon la plupart des experts en sécurité, le code open source est plus susceptible d'être sécurisé et de le rester en raison du [nombre impressionnant de personnes qui le révisent](https://www.itprotoday.com/linux/why-you-should-trust-open-source-software-security) au fil du temps.

Mais une fois qu'un développeur commence à assembler du code open source et à ajouter ses propres personnalisations pour créer quelque chose de propriétaire, tout est possible. À partir de ce moment, c'est à lui de veiller à ne pas ajouter de vulnérabilités qui pourraient conduire à une violation de données ou à un piratage.

Et selon la nature du logiciel en question, il existe une variété de données qui pourraient être en danger dans votre logiciel final, notamment :

* Mots de passe
* Clés de chiffrement
* Adresses IP
* Jetons d'authentification, et bien plus encore.

Cela fait de la menace d'une fuite de code source une menace majeure pour tout développeur de logiciels propriétaires. Et cette menace n'est pas seulement théorique. Il y a eu plusieurs cas de [fuites de code propriétaire](https://www.wired.com/story/source-code-leak-dangers/) ces dernières années. Et dans beaucoup de ces cas, les conséquences ultimes sont encore loin d'être claires.

Mais dans un cas — la fuite de l'ensemble du dépôt de code source de Twitch — les conséquences ont été graves. Selon une revue des données, les pirates ont eu accès à [presque 7 000 secrets](https://blog.gitguardian.com/security-threats-from-the-twitch-leak/). Ces secrets, constitués des types de données listés ci-dessus, pourraient donner aux attaquants un accès catastrophique à la plateforme.

## Les principales menaces pour la sécurité du code source

Il existe deux principales catégories de menaces pour la sécurité du code source :

### Menaces internes

Le code source est à la merci des développeurs et de toute autre personne qui y a accès. Cela signifie que limiter l'accès à votre code source et établir des directives de sécurité pour ceux qui y ont accès est vital pour augmenter la sécurité.

Il est également important de réaliser que les acteurs de menaces internes ne sont pas toujours malveillants. Souvent, les menaces internes proviennent d'erreurs ou d'actions négligentes commises par des employés.

Par exemple, un programmeur pourrait partager des parties du code source sur un forum en ligne pour obtenir des commentaires ou résoudre un problème — ce qui pourrait conduire à ce que ce code tombe entre de mauvaises mains.

### Menaces externes

Les menaces externes proviennent de l'extérieur de votre équipe de développement. Elles peuvent provenir de concurrents qui veulent utiliser le code pour améliorer le leur. Ou elles peuvent provenir de pirates qui tenteront de vendre votre code source ou de le disséquer à la recherche de vulnérabilités.

Le point est que, qu'une fuite provienne de menaces internes ou externes, elle peut avoir des conséquences terribles. Les fuites de code source peuvent conduire à des attaques supplémentaires, exposant de grandes quantités de données sensibles.

Les fuites de code source peuvent également entraîner des pertes financières en donnant un avantage aux concurrents. Et vos clients y réfléchiront à deux fois avant de traiter avec un développeur qui a exposé des données client précieuses dans le passé.

Les réglementations en matière de sécurité deviennent également plus strictes. Vos clients peuvent faire face à des amendes importantes s'ils ne protègent pas leurs données — et ils vous en tiendront responsable.

## Comment sécuriser votre code source

Maintenant que vous connaissez l'importance de sécuriser le code source, examinons quelques moyens de renforcer la sécurité de votre code source :

### Mettre en œuvre des pratiques de développement sécurisées

La sécurité de votre code source commence au début du cycle de développement. Plus vous détectez tôt les failles de sécurité dans le code, mieux c'est.

Vous devez définir un ensemble clair de pratiques, de règles et de procédures de codage dès le début de chaque processus. Cela inclut la formation de votre équipe de développement aux meilleures pratiques de sécurité et la fourniture de documentation sur les normes de sécurité qu'ils doivent respecter pendant le projet.

Le projet Open Web Application Security Project (OWASP) offre [un cadre complet](https://owasp.org/www-pdf-archive/OWASP_SCP_Quick_Reference_Guide_v2.pdf) qui constitue un excellent point de départ. Bien qu'il soit adapté aux applications web, ses concepts sont largement applicables à tous les types de travaux de développement logiciel.

Ses points les plus importants incluent :

* Effectuer toute validation et encodage des données sur un système de confiance unique
* Exiger une authentification standardisée et testée pour l'accès aux ressources du projet
* Prendre des mesures pour réduire la complexité du code autant que possible pour faciliter l'audit de sécurité
* Protéger et chiffrer les dépôts de code liés au projet
* Sécuriser et protéger votre pipeline de développement de build

En gardant votre code et votre processus de développement en ligne avec les meilleures pratiques de sécurité établies comme celles ci-dessus, vous pouvez réduire considérablement les risques que votre code soit compromis, que ce soit pendant le développement ou après sa publication. Comme on dit, mieux vaut prévenir que guérir.

Et une fois le code écrit, vous devriez également utiliser [des outils d'analyse de sécurité](https://www.nist.gov/itl/ssd/software-quality-group/source-code-security-analyzers) pour identifier les failles de sécurité et autres risques. Les analyseurs de code scanneront également pour garantir la conformité avec les meilleures pratiques de sécurité et les normes de codage. Les outils vous aideront à identifier les risques et à corriger les problèmes sous-jacents avant qu'il ne soit trop tard.

Certains des outils les plus couramment utilisés pour cela incluent :

* [Appsonar](https://www.appsonar.com/) – automatise les tests des meilleures pratiques dans plus de 15 langues et scanne les vulnérabilités de code connues
* [Codiga](https://www.codiga.io/) – vérifie les meilleures pratiques, la sécurité, la sûreté et les problèmes de conception dans 18 langues et frameworks
* [Mend SAST](https://www.mend.io/sast/) – fournit une analyse automatisée des vulnérabilités et une remédiation automatique des vulnérabilités connues

### Chiffrer et surveiller les données en transit

Le chiffrement des données est crucial pour sécuriser votre code source. Et les données en transit sont particulièrement vulnérables. Il est donc judicieux de trouver des moyens de garder votre code sécurisé lorsqu'il passe entre les membres de l'équipe de développement.

Un bon point de départ est d'utiliser une plateforme de partage ou de collaboration de code qui inclut un chiffrement de bout en bout.

Il existe une variété de solutions destinées aux développeurs de logiciels qui incluent le chiffrement. Certaines des options les plus utilisées incluent [CryptPad](https://cryptpad.fr/), [CodeTogether](https://www.codetogether.com/pro/), et [Visual Studio Live Share](https://visualstudio.microsoft.com/services/live-share/). Selon la nature de votre projet particulier, l'une d'entre elles est sûre de faire une ajout précieux à la boîte à outils de votre équipe.

Si une plateforme de partage de code est excessive pour ce sur quoi vous travaillez, vous pouvez utiliser une [plateforme de partage de fichiers chiffrés](https://geekflare.com/secure-file-sharing/) à la place et l'utiliser pour échanger des extraits de code. Et si vous travaillez avec une équipe qui n'est pas toute dans un seul bureau, il est judicieux d'investir dans un VPN. Le VPN masquera votre adresse IP et chiffrera tous les transferts de données entre vos réseaux.

Mais soyez conscient que les VPN ralentissent souvent vos vitesses internet, vous devriez donc faire vos recherches avant d'en acheter un pour vous et votre équipe. Certains VPN sont [beaucoup plus rapides](https://nordvpn.com/features/fastest-vpn/) que d'autres et ne ralentissent votre vitesse que de manière incrémentale, alors choisissez judicieusement ou vous pourriez nuire à la productivité de votre équipe.

### Contrôler l'accès

Les seules personnes qui devraient avoir accès aux dépôts de code source sont les développeurs et le personnel de contrôle qualité. Il n'y a aucune raison de donner accès à quiconque n'est pas directement impliqué dans le codage.

En limitant le nombre de personnes ayant accès, vous pouvez réduire considérablement le risque de menaces internes. Protégez votre code avec un contrôle d'accès d'authentification et d'autorisation.

### Effectuer des revues de code sécurisées

Les revues de code sécurisées sont une partie critique du [SDLC (Software Development Lifecycle)](https://www.freecodecamp.org/news/get-a-basic-understanding-of-the-life-cycles-of-software-development/). Les revues sont particulièrement importantes pour la sécurité. Elles permettent aux membres de l'équipe d'identifier et de résoudre toute vulnérabilité de sécurité potentielle avant que le code ne soit mis en ligne. Dans de nombreuses industries où vous pourriez travailler, les revues sont obligatoires pour la conformité réglementaire.

Mais il est important de faire la différence entre une revue de code et une revue de code sécurisée. Cette dernière doit se concentrer strictement sur le "renforcement" de la sécurité du code. Les revues régulières se concentrent principalement sur la correction des bugs ou des problèmes potentiels. Ceux-ci se produisent plus fréquemment lorsque votre base de code est en développement intensif. Les revues de code sécurisées doivent avoir lieu principalement lorsque votre code est proche d'une version.

À ce stade, il est judicieux d'appliquer quelques techniques de renforcement complètes pour rendre plus difficile l'accès des pirates au logiciel par analyse ou à l'exécution.

Certaines techniques de renforcement incluent :

* [L'obfuscation de code](https://www.freecodecamp.org/news/make-your-code-secure-with-obfuscation/)
* [Le chiffrement de chaînes](https://www.pelock.com/products/string-encrypt)
* [La détection et la réponse aux altérations à l'exécution](https://books.nowsecure.com/secure-mobile-development/en/coding-practices/anti-tamper-techniques.html)
* [Les mesures anti-débogage](https://resources.infosecinstitute.com/topic/anti-debugging/)

Selon la sensibilité des données que votre logiciel traite, vous devrez peut-être aller beaucoup plus loin que les techniques que j'ai partagées ci-dessus. Vous devez toujours tenir compte des besoins de sécurité du client avant tout — même s'ils vous demandent de renforcer votre code au-delà de ce que vous jugez nécessaire.

## Réflexions finales

Les développeurs de logiciels propriétaires doivent porter une attention particulière à la sécurité du code source. Ceux qui ne le font pas risquent de s'exposer, eux et leurs clients, à des risques massifs qui sont largement évitables.

Ainsi, tout au long du processus de développement, vous devez vous protéger contre les menaces internes et externes. Ne pas le faire peut mettre des données sensibles en danger, entraînant potentiellement des dommages financiers et réputationnels importants — pour toutes les parties impliquées.

_Image sous licence Gorodenkoff via Adobe Stock Photos_
---
title: 'DevRel au cœur de la pile : Conteneurs, Kubernetes et les ingénieurs DevOps'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-18T10:30:00.000Z'
originalURL: https://freecodecamp.org/news/devrel-down-the-stack-containers-kubernetes-and-devops-engineers
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/marek-devrel-banner.jpg
tags:
- name: containers
  slug: containers
- name: developer-advocacy
  slug: developer-advocacy
- name: developer relations
  slug: developer-relations
- name: Kubernetes
  slug: kubernetes
- name: Swift
  slug: swift
- name: Swift Programming
  slug: swift-programming
seo_title: 'DevRel au cœur de la pile : Conteneurs, Kubernetes et les ingénieurs DevOps'
seo_desc: 'By David Nugent

  IBM’s $34B acquisition of Red Hat closed last week, underscoring the huge and growing
  importance of  hybrid cloud infrastructure. My colleague Marek Sadowski has become
  a  subject matter expert in containers, Kubernetes and server-sid...'
---

Par David Nugent

L'acquisition de Red Hat par IBM pour [$34 milliards](https://newsroom.ibm.com/2019-07-09-IBM-Closes-Landmark-Acquisition-of-Red-Hat-for-34-Billion-Defines-Open-Hybrid-Cloud-Future) a été finalisée la semaine dernière, soulignant l'importance énorme et croissante de l'infrastructure cloud hybride. Mon collègue Marek Sadowski est devenu un expert en conteneurs, Kubernetes et Swift côté serveur, bien qu'il ait commencé comme développeur full stack, fondateur d'une startup en robotique et entrepreneur.

![Marek donnant une conférence](https://res.cloudinary.com/practicaldev/image/fetch/s--LGWhCAWn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/gr6qrvfie9qrbx21gy4o.jpg)

Marek a 20 ans d'expérience en conseil d'entreprise aux États-Unis, en Europe, au Japon, au Moyen-Orient et en Afrique, et il a été pionnier dans la recherche sur les casques de réalité virtuelle pour le système de réalité virtuelle permettant de contrôler des robots sur Mars pendant son temps à la NASA. Après avoir fondé une startup en robotique, Marek est venu travailler chez IBM. Je lui ai parlé de son expérience en matière de plaidoyer DevOps.

## Table des matières

* En quoi le plaidoyer DevOps diffère-t-il du plaidoyer API/application ?
* Comment vous concentrez-vous sur la communauté DevRel ?
* Qu'avez-vous changé en passant à DevRel DevOps ?
* Comment faire pour que les développeurs voient Swift comme un langage côté serveur ?
* Comment êtes-vous entré dans le DevRel ?

![Marek donnant une conférence](https://res.cloudinary.com/practicaldev/image/fetch/s--OCVtuwPo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/x0ccbjsy1k941giianl7.jpg)

### Q : L'un de vos domaines de concentration dans DevRel est les conteneurs. En quoi le plaidoyer pour une technologie DevOps diffère-t-il du plaidoyer pour une API ou une application ?

Bonne question. Lorsque l'on travaille avec des conteneurs, les ingénieurs pensent davantage en termes de "plomberie" et d'idées DevOps, ainsi que de la facilité d'expansion de l'empreinte de l'infrastructure. En revanche, lorsque l'on parle d'API, on essaie de faire de la développement d'applications le centre de gravité de la discussion.

Lorsque l'on discute des API avec les développeurs, on parle de la manière dont on pourrait, de manière robuste, consommer l'API. Prenons l'exemple de l'[API IBM Watson](https://ibm.biz/BdzKG5) : notre équipe parlera de la manière dont vous pouvez créer et exécuter des SDK pour que les développeurs consomment des API dans leur propre langage, par exemple, Swift (pour mobile) ou Java (pour entreprise). Vous examineriez le consommateur de votre API et discuteriez de la manière dont vous pouvez produire l'API, vous protéger et effectuer la facturation.

Revenons aux conteneurs : lorsque l'on discute de la technologie des conteneurs, on parle davantage de la "plomberie" du cloud. Comment gérez-vous les conteneurs ? Les étendez-vous ? Gérez-vous leurs charges de travail ? Livrez-vous et testez-vous de nouvelles versions ?

Il devient rapidement apparent que ce sont deux concepts séparés. La conteneurisation traite de la manière dont votre backend fonctionne et de la maintenance appropriée de votre application, ce qui attire les personnes issues d'un milieu DevOps. Lorsque vous parlez d'API, c'est une histoire complètement différente. Votre paradigme de pensée change pour adopter le point de vue du consommateur : Comment le consommateur trouve-t-il l'API ? Comment les développeurs peuvent-ils consommer l'API ?

Je parle lors de conférences sur ces deux sujets. J'ai constaté que les personnes qui développent des applications sont plus intéressées par l'apparence, la convivialité et l'expérience du développeur de l'application, alors qu'avec les conteneurs, il s'agit davantage de backend, d'équilibrage de charge et de voir les problèmes du point de vue d'un administrateur système.

### Q : Beaucoup de gens sont familiers avec le DevRel axé sur les ingénieurs logiciels, mais DevOps est une communauté entièrement différente. Comment vous concentrez-vous sur cette communauté ?

Il y a une division — tout le monde est intéressé par les nouvelles technologies comme Kubernetes et Docker, mais peu seront prêts à perfectionner leurs compétences au point que ce soit leur travail quotidien. Beaucoup de développeurs veulent savoir comment lancer un conteneur et un service à l'intérieur du conteneur, le mettre dans leur CV et en avoir fini. Les développeurs peuvent être intéressés parce que c'est à la mode ou que c'est un mot à la mode. Cependant, vous pouvez trouver beaucoup de personnes qui exécutent des services dans des conteneurs et ont des questions spécifiques : les administrateurs système qui veulent surveiller les conteneurs et assurer la sécurité, l'équilibrage de charge et d'autres aspects de l'administration. C'est un public complètement différent des développeurs qui consomment des API et créent une application web cool. Ce sont deux communautés différentes, et vous devez donner à chaque communauté un contenu différent.

Par exemple, lors d'un hackathon, il est très difficile de créer de grands déploiements dans des conteneurs. C'est une optimisation du développement et des opérations plus que du codage d'applications.

![L'équipe IBM SF City tenant un stand](https://res.cloudinary.com/practicaldev/image/fetch/s--eA1r0etR--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/9sh0o5no0f09pjbj31qk.jpg)

### Q : Comment avez-vous dû changer votre approche du DevRel en passant à la défense de DevOps ?

Auparavant, lorsque j'animais des ateliers axés sur les développeurs d'applications, ils avaient généralement quelques objectifs : comprendre notre API, consommer des données à partir des points de terminaison de l'API et créer des applications simples de type "Hello World". Les développeurs de ces ateliers posaient des questions sur les façons de haut niveau d'architecturer des applications, par exemple avec Watson, dans des applications mobiles ou web, ou une chaîne de processus.

En revanche, lorsque je parle de DevOps et de conteneurs, les développeurs dans le public veulent lancer les services, voir comment ils montent et descendent en échelle, enquêter sur la manière dont les services se comportent lorsqu'il y a une défaillance et comment améliorer les problèmes de sécurité. C'est une approche complètement différente. Ils ne sont pas intéressés par la construction de quelque chose de nouveau, ils veulent perfectionner leur approche de déploiement.

Une analogie que je peux donner aux personnes nouvelles dans ce domaine : c'est comme inviter un peintre et un plombier à une fête. Ils font tous les deux des choses similaires, pourtant le peintre veut créer une peinture que vous pouvez accrocher au mur, et le plombier parlera rarement du type de tuyauterie qu'il utilise à l'intérieur de vos murs. Tous deux font quelque chose dans votre maison, mais le peintre pense aux personnes qu'ils attireront et à la peinture (nos API) pour assurer une expérience de visualisation agréable, tandis que le plombier veut simplement faire le travail et ne plus y toucher. Les plombiers veulent apporter des changements aussi rarement que possible et se concentrer sur la stabilité, le peintre veut créer plus de nouvelles peintures. Ils ont des approches différentes basées sur leurs objectifs différents.

### Q : Vous donnez également des conférences sur Swift, spécifiquement sur le côté serveur. La plupart des gens connaissent Swift du côté du développement iOS, mais pourquoi est-il utile sur le serveur ? Comment faire pour que les développeurs le considèrent comme un langage serveur ?

Swift côté serveur est un développement relativement nouveau. Je compare l'état actuel de Swift côté serveur à celui de Java il y a vingt-quatre ans. En 1996, j'ai commencé à écrire une application côté serveur en utilisant Java — c'était un concept nouveau à l'époque ! La même chose se produit maintenant avec Swift, alors que les développeurs déplacent le langage Swift vers le serveur. Il y a beaucoup de raisons pour cela ; l'une des plus simples est que vous écrivez dans le même langage sur le serveur que pour votre application mobile, et de cette manière, vous pouvez utiliser les mêmes structures de données, processus de pensée et ressources de personnel sur les deux systèmes. Vous n'avez pas besoin de systèmes ou de frameworks différents pour parler à la base de données ou au cloud.

De nos jours, chaque application mobile vous demande de vous connecter à Internet pour l'IA, la messagerie et les réseaux sociaux. Même les jeux simples vous permettent d'échanger des informations ou d'avoir une conversation avec des personnes du monde entier. Si votre application et votre backend sont écrits dans un seul langage comme Swift, cela rend ces échanges de données simples et transparents.

Certaines personnes disent que _Swift est un langage à la mode à apprendre_. Puisque vous avez la possibilité d'écrire des applications en Java ou JavaScript, vous pouvez également les écrire en Swift. Swift a maintenant été open-sourcé par Apple, de la même manière que Sun a ouvert Java. Vous pouvez maintenant écrire des applications dans le cloud ou sur n'importe quelle plateforme. Par exemple, OpenWhisk vous permet d'écrire des fonctions Swift basées sur des événements dans le cloud sans aucun code DevOps.

Avec Swift, les développeurs sont attirés par la beauté du langage et la capacité d'écrire un langage unique du mobile au cloud pour rendre votre application meilleure et plus facile à maintenir. Vous pouvez profiter de l'écriture dans votre langage de choix et étendre les capacités de l'environnement que vous aimez. Si vous êtes un développeur iOS, peut-être pouvez-vous devenir un développeur full-stack, et les développeurs aiment l'histoire selon laquelle ils peuvent devenir quelque chose de plus et participer au processus de développement full stack.

![Marek](https://res.cloudinary.com/practicaldev/image/fetch/s--SlcpOzfS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/chlb5mirpmyo4jher7bp.jpg)

### Q : Comment êtes-vous entré dans les relations avec les développeurs ?

Je venais d'arriver aux États-Unis depuis la Pologne en tant que fondateur d'une startup, et le but du déménagement était d'étendre mon entreprise. On dit que 99 % des startups ne réussissent pas immédiatement, et les fondateurs doivent souvent démarrer tout en ayant un emploi existant. On m'a dit que travailler dans le cloud était le facteur clé dans de nombreuses industries, mais j'avais peu d'exposition à ces technologies. D'autre part, j'avais acquis des compétences en parlant aux investisseurs, et en tant qu'entrepreneur, j'étais capable de comprendre ce qui était important pour les startups. J'avais également une solide expérience en développement Java et différentes technologies IT — j'avais une carrière d'architecte soutenant les banques et autres entreprises EMEA en tant que professionnel Java, démontrant des systèmes aux clients.

Il y avait une ouverture pour un développeur advocate mobile-first, et malgré mon manque d'expérience en mobile ou en cloud, j'ai convaincu l'interviewer que j'étais le candidat parfait en raison de ma facilité à parler avec les développeurs et à présenter des sujets techniques de manière accessible. J'aime expliquer des sujets complexes de manière simple à travers des démonstrations et des projets exemples.

Mon responsable d'embauche m'a demandé de construire une petite application mobile comme test d'emploi, qui se connectait à [IBM Cloud](https://ibm.biz/BdzKGU) pour échanger des informations entre l'utilisateur et un backend. J'ai apprécié la tâche et j'ai trouvé que j'étais bon dans ce domaine ! Après deux ans, j'ai migré vers plus de technologies cloud et de plus en plus d'API IBM. Finalement, j'ai commencé à m'intéresser à Kubernetes et aux conteneurs, et j'ai réalisé que les conteneurs sont un domaine avec un potentiel de croissance incroyable.

Je dois dire que ce qui m'a le plus attiré vers DevRel était l'opportunité d'apprendre et de transmettre de nouvelles technologies aux développeurs, et d'utiliser mon talent pour expliquer des choses complexes de manière simple.

![Marek faisant du snowboard](https://res.cloudinary.com/practicaldev/image/fetch/s--q3yO1Vrc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/eccad3abeiluyjgz8i8b.jpg)

### [](https://dev.to/drnugent/devrel-down-the-stack-containers-kubernetes-and-talking-to-devops-engineers-hm7#next-steps) Prochaines étapes :

* [Suivez Marek sur Twitter](https://twitter.com/blumareks)
* Voir Marek parler lors d'un prochain [IBM Developer SF Meetup](https://www.meetup.com/IBM-Developer-SF-Bay-Area-Meetup)
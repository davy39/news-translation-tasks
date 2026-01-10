---
title: Comment exploiter la puissance de Kubernetes pour optimiser vos coûts d'hébergement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T17:48:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-leverage-the-power-of-kubernetes-to-optimise-your-hosting-costs-c2e168a232a2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*IfEjMq-JLKawzXvz.png
tags:
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment exploiter la puissance de Kubernetes pour optimiser vos coûts d'hébergement
seo_desc: 'By Daniele Polencic

  During the last few years, the industry has experienced a shift towards developing
  smaller and more focused applications.

  It doesn’t come as a surprise that more and more companies are breaking their massive
  and static monoliths i...'
---

Par Daniele Polencic

Au cours des dernières années, l'industrie a connu un changement vers le développement d'applications plus petites et plus ciblées.

Il n'est pas surprenant que de plus en plus d'entreprises décomposent leurs monolithes massifs et statiques en un ensemble de composants découplés et indépendants.

Et à juste titre.

Les services qui sont minuscules en taille sont :

* **plus rapides à déployer** — car vous les créez et les publiez en plus petits morceaux
* **plus faciles à itérer** — puisque l'ajout de fonctionnalités se fait indépendamment
* **résilients** — le service global peut toujours fonctionner malgré l'indisponibilité de l'un des composants

Les petits services sont excellents d'un point de vue produit et développement.

_Mais comment ce changement culturel impacte-t-il l'infrastructure ?_

### Gérer l'infrastructure à grande échelle

Il s'avère que les choses sont plutôt simples lorsque vous traitez avec quelques applications éparses.

Vous pouvez les compter avec vos mains, et vous avez beaucoup de temps à consacrer au support et à la publication.

Dans une grande organisation, gérer des centaines d'applications est exigeant, mais toujours faisable. Vous avez plusieurs équipes dédiées au développement, à l'emballage et à la publication des applications.

**Développer des services à partir de composants plus petits, en revanche, introduit un défi différent.**

Lorsque pour chaque application, vous pouvez refactoriser les mêmes applications en une collection de quatre composants, vous avez au moins quatre fois plus d'applications à développer, à emballer et à publier.

![Image](https://cdn-media-1.freecodecamp.org/images/S2zCL-xIULOF5TM-sWVz9hIW7fMhEmnFBAVC)

Il n'est pas rare qu'un petit service soit composé d'une douzaine de composants tels qu'une application front-end, une API backend, un serveur d'autorisation, une application d'administration, etc.

En effet, lorsque vous développez des services qui interagissent les uns avec les autres, vous voyez une explosion de composants déployés sur votre infrastructure.

![Image](https://cdn-media-1.freecodecamp.org/images/9SOv8OOpC6oBEIai1dDJyaa-k5Moay7ChQLT)

Cela devient plus difficile, cependant.

### Vous gaspillez probablement votre argent sur les ressources de calcul

La plupart des services sont déployés sur des machines virtuelles telles qu'Amazon EC2, Digital Ocean Droplets ou Azure Virtual Machines.

Chaque machine virtuelle est livrée avec un système d'exploitation qui consomme une partie de la mémoire et des ressources CPU qui lui sont allouées.

Lorsque vous créez une droplet de 1 Go de mémoire et 1 vCPU sur Digital Ocean, vous finissez par utiliser 700 Mo de mémoire et 0,8 vCPU après avoir retiré le surcoût du système d'exploitation.

![Image](https://cdn-media-1.freecodecamp.org/images/5M5g07ClzsjgVS9bkqAo61vhuudKjKhQ2crK)

Ou en d'autres termes, pour chaque cinquième machine virtuelle, le surcoût s'ajoute à une machine virtuelle complète.

**Vous payez pour cinq mais ne pouvez en utiliser que quatre.**

Vous ne pouvez pas y échapper, même si vous êtes sur du bare metal.

Vous devez toujours exécuter vos services à partir d'un système d'exploitation de base.

_C'est bon, tout le monde a besoin d'exécuter un système d'exploitation_ — dites-vous.

Et vous avez raison.

Cependant, l'argent gaspillé sur les systèmes d'exploitation n'est que la partie émergée de l'iceberg.

### Vous gaspillez aussi BEAUCOUP d'argent sur l'utilisation des ressources

Vous avez probablement réalisé que lorsque vous divisez vos services en composants plus petits, chacun d'eux vient avec des exigences de ressources différentes.

Certains composants tels que les applications de traitement de données et d'extraction de données sont intensifs en CPU. D'autres, comme les serveurs pour les applications en temps réel, peuvent utiliser plus de mémoire que de CPU.

![Image](https://cdn-media-1.freecodecamp.org/images/LvpPlLSR1iY5qPRPO9rU1mYUOjVwxTwITDxc)

Amazon Web Services et les autres fournisseurs de cloud ont effectivement une longue liste de ressources de calcul qui répondent à tous les besoins : usage général, optimisé pour le CPU, optimisé pour la mémoire, optimisé pour le stockage et calcul GPU.

Vous devriez vous efforcer d'utiliser la bonne machine virtuelle pour votre composant. Idéalement, elle devrait correspondre à la consommation de mémoire et à l'utilisation du CPU.

_Travaillez-vous sur un composant web critique écrit en Java ?_

Peut-être devriez-vous utiliser un c5.4xlarge optimisé pour les charges de travail intensives en calcul.

Plus vous vous rapprochez des exigences, mieux vous utilisez vos ressources.

En pratique, cela est cependant assez rare.

_Devriez-vous utiliser un c5.2xlarge ou un c5.4xlarge ?_

_Le niveau suivant (8 vCPU et 16 Go de mémoire) fait-il une différence ?_

Il est beaucoup plus facile de sélectionner quelques profils de calcul qui sont suffisamment bons dans 80 % des cas et de les utiliser pour tous les composants.

_En fait, qu'y a-t-il de mal à utiliser principalement la même machine virtuelle pour chaque charge de travail ?_

Rien du tout, si vous êtes heureux d'emballer chaque composant dans une capacité de calcul de 2 Go de mémoire et de vCPU.

Même si votre composant peut fonctionner avec seulement 1 Go de mémoire.

_Oui, vous pourriez optimiser dans le futur._

Mais soyons honnêtes : **c'est comme changer les pneus en conduisant**.

Vous mettez beaucoup d'efforts à ajuster le système pour réaliser que l'application a changé à nouveau et que vous devez recommencer depuis le début.

Vous finissez donc par faire le seul choix sensé : sélectionner un petit, moyen et grand profil pour les machines virtuelles et les utiliser pour toutes les charges de travail.

Vous savez que vous devez vivre avec le gaspillage de centaines de mégaoctets de RAM et de nombreux cycles CPU.

![Image](https://cdn-media-1.freecodecamp.org/images/tZCYzQhraZ2c0MI9eAmUUTyAuqXEmbSVq8hx)

Si cela peut vous réconforter, il y a beaucoup d'entreprises souffrant d'inefficacités similaires.

Certaines n'utilisent que 10 % des ressources allouées.

**Vous payez 1000 $ pour des instances EC2 sur Amazon, mais vous n'utilisez en réalité que 100 $.**

Cela ne semble pas être la meilleure façon de dépenser votre budget.

_Vous devriez récupérer votre argent sur les ressources que vous n'utilisez pas._

_Mais pourquoi ces exigences sont-elles si différentes de toute façon ?!_

### Quand choisir le bon outil fait plus de mal que de bien

Lorsque les développeurs ont la liberté d'utiliser le bon outil pour le travail, ils ont tendance à se lâcher.

Node.js pour le front-end, Spring Boot pour l'API backend, Flask et Celery pour les travaux de traitement en arrière-plan, React.js pour le côté client, vous l'appelez.

L'infrastructure devient un parc d'attractions, des centaines d'applications fonctionnant sur des environnements d'exécution entièrement différents.

Avoir la bonne technologie pour le travail permet une plus grande vitesse d'itération, mais cela vient généralement avec le fardeau supplémentaire de gérer un langage de programmation de plus.

Bien que vous puissiez atténuer la prolifération des outils et des langages, en pratique, c'est plus compliqué que cela.

Deux applications partageant le même environnement d'exécution JVM peuvent dépendre d'un ensemble différent de dépendances et de bibliothèques.

Peut-être qu'une dépend de ImageMagick pour redimensionner les images.

L'autre dépend d'un binaire tel que PhantomJS ou ZeroMQ pour être disponible dans son chemin.

Vous devriez emballer ces dépendances avec son application.

Et ainsi, vous finissez par traiter des dizaines de configurations qui sont les mêmes, mais différentes à leur manière unique.

Vous ne devriez pas traiter l'infrastructure comme une réflexion après coup. Vous devriez prendre soin de vos dépendances et les emballer au fur et à mesure que vous développez l'application, dès le début.

Idéalement, vous devriez archiver toutes les parties nécessaires à l'exécution de votre composant en un seul bundle.

Plus de perte de temps à chercher les dépendances juste avant une publication.

_Oui, plus facile à dire qu'à faire._

Ou peut-être pas.

### Emprunter des conteneurs à l'industrie du transport

La technologie de l'information n'est pas la seule industrie avec le même problème.

Transporter des marchandises en cargo autour du globe est difficile lorsque vous devez stocker des articles individuellement.

Imaginez avoir des milliers de boîtes de toutes formes et tailles à stocker dans la cale. Vous devriez porter une attention particulière à la manière dont vous emballez les articles car vous ne voulez pas en manquer un lorsqu'il est temps de décharger.

L'industrie du cargo a trouvé une solution : les conteneurs.

La compagnie de cargo ne transporte pas de marchandises ; elle expédie des conteneurs.

_Voulez-vous expédier toutes vos marchandises en toute sécurité ?_ Placez-les dans un conteneur. Lorsque le conteneur est déchargé, vous êtes assuré d'avoir tout là.

Vous pouvez appliquer le même principe à vos applications.

_Voulez-vous déployer votre application et toutes ses dépendances en toute sécurité ?_

Emballez-les dans un conteneur Linux.

Un conteneur Linux est comme un conteneur de cargo, mais il encapsule tous les fichiers, binaires et bibliothèques nécessaires à l'exécution de votre processus.

_Cela ne ressemble-t-il pas beaucoup aux machines virtuelles ?_

### Machines virtuelles au régime

En effet, si vous plissez les yeux et regardez de loin les machines virtuelles, elles ressemblent à des conteneurs.

Elles encapsulent l'application et ses dépendances comme des conteneurs.

Cependant, les machines virtuelles sont lentes à démarrer, généralement plus grandes et — comme vous l'avez appris — un gaspillage de ressources.

En fait, vous devez allouer un nombre fixe de CPU et de mémoire pour exécuter votre application.

Elles doivent également émuler du matériel et viennent avec le bagage supplémentaire d'un système d'exploitation.

Les conteneurs Linux, en revanche, ne sont que des processus s'exécutant sur votre hôte.

![Image](https://cdn-media-1.freecodecamp.org/images/sehLADQlF0sl1so4f9BOWW4lPsBvozqs42DG)

En effet, pour le même système d'exploitation et serveur, vous pourriez avoir des dizaines de conteneurs s'exécutant sur cet hôte.

Et malgré le fait de vivre sur le même ordinateur, les processus s'exécutant dans des conteneurs ne peuvent pas se voir les uns les autres.

Les applications s'exécutant à l'intérieur des conteneurs sont entièrement isolées et ne peuvent pas faire la différence entre une machine virtuelle et un conteneur.

C'est une excellente nouvelle !

Les conteneurs Linux sont comme des machines virtuelles, mais plus efficaces.

_Mais de quoi sont faits ces conteneurs Linux, de toute façon ?_

### Les conteneurs Linux sont des processus isolés avec des avantages

La magie des conteneurs vient de deux fonctionnalités du noyau Linux : les groupes de contrôle et les espaces de noms.

Les groupes de contrôle sont un moyen pratique de limiter le CPU ou la mémoire qu'un processus particulier peut utiliser.

Par exemple, vous pourriez dire que votre composant ne devrait utiliser que 2 Go de mémoire et un de vos quatre cœurs CPU.

Les espaces de noms, en revanche, sont responsables de l'isolement du processus et de la limitation de ce qu'il peut voir.

Le composant ne peut voir que les paquets réseau qui lui sont directement liés. Il ne pourra pas voir tous les paquets réseau circulant à travers l'adaptateur réseau. Les groupes de contrôle et les espaces de noms sont des primitives de bas niveau.

Avec le temps, les développeurs ont créé de plus en plus de couches d'abstractions pour faciliter le contrôle de ces fonctionnalités du noyau.

L'une des premières abstractions était LXC, mais la vraie affaire était Docker qui a été publié en 2013.

Docker n'abstrait pas seulement les fonctionnalités du noyau ci-dessus, mais il est agréable de travailler avec.

Exécuter un conteneur Docker est aussi simple que :

```
docker run <my-container>
```

Et puisque tous les conteneurs implémentent une interface standard, vous pouvez exécuter n'importe quel autre conteneur avec la même commande :

```
docker run mysql
```

Et vous avez une base de données MySQL.

La portabilité de l'application et une interface standard pour créer et exécuter des processus est ce qui rend les conteneurs si populaires.

Les conteneurs sont géniaux !

* Vous avez économisé de l'argent en exécutant des dizaines de systèmes d'exploitation ✅
* Vous avez emballé des applications en unités portables ✅
* Vous avez une prolifération de conteneurs ❌

Il semble que les conteneurs n'aient pas résolu tous les problèmes après tout.

Vous avez besoin d'un moyen de gérer les conteneurs.

### Gérer les conteneurs à grande échelle

Lorsque vous avez des centaines, voire des milliers de conteneurs, vous devez trouver un moyen d'exécuter plusieurs conteneurs sur le même serveur. Et vous devez prévoir que les conteneurs soient répartis sur plusieurs serveurs également.

Ainsi, vous pouvez distribuer la charge sur plusieurs nœuds et empêcher qu'une seule défaillance ne fasse tomber l'ensemble du service.

Garder une trace de l'endroit où chaque conteneur est déployé dans votre infrastructure ne semble pas être la meilleure utilisation de votre temps.

_Peut-être y a-t-il un moyen de l'automatiser ?_

Et si vous pouviez avoir un algorithme décidant où placer ces conteneurs également ?

Peut-être pourrait-il être assez intelligent pour emballer les conteneurs de manière efficace afin de maximiser la densité du serveur. Peut-être même garder une liste des conteneurs déployés et de leur hôte.

Il s'avère que quelqu'un a eu précisément cette idée et a trouvé une solution.

### Kubernetes, le puissant orchestrateur de conteneurs

Kubernetes était initialement une création de Google.

Google exécutait une technologie similaire aux conteneurs et devait trouver un moyen efficace de planifier les charges de travail.

Ils ne voulaient pas garder et mettre à jour manuellement une longue liste de conteneurs et de serveurs. Ils ont donc décidé d'écrire une plateforme qui pouvait analyser automatiquement l'utilisation des ressources, planifier et déployer des conteneurs.

Mais c'était du code source fermé.

Quelques Googlers ont décidé de réécrire la plateforme en tant qu'effort open source. Et le reste est de l'histoire.

_Alors, qu'est-ce que Kubernetes ?_

Vous pouvez penser à Kubernetes comme un planificateur.

Kubernetes inspecte votre infrastructure (bare metal ou cloud, public ou privé) et mesure le CPU et la mémoire pour chaque ordinateur.

Lorsque vous demandez à déployer un conteneur, Kubernetes identifie les exigences de mémoire pour votre conteneur et trouve le meilleur serveur qui satisfait votre demande.

Vous ne décidez pas où l'application est déployée. Le centre de données est abstrait pour vous.

En d'autres termes, Kubernetes jouera à Tetris avec votre infrastructure.

Les conteneurs Docker sont les blocs, les serveurs sont les planches, et Kubernetes est le joueur.

![Image](https://cdn-media-1.freecodecamp.org/images/qrq7mTOhhECRV0BMmiHZ-xQ6TGQslqdYEzF9)

Avoir Kubernetes qui emballe efficacement votre infrastructure signifie que vous obtenez plus de calcul pour votre argent. Vous pouvez faire beaucoup plus avec beaucoup moins.

Et votre facture globale devrait diminuer en conséquence.

Vous souvenez-vous des entreprises n'utilisant que 10 % de leurs ressources allouées ?

Eh bien, Kubernetes vient de sauver votre journée.

Mais il y a plus.

Kubernetes a une fonctionnalité redoutable qui est généralement oubliée ou ignorée.

### Kubernetes comme couche API sur votre centre de données

Tout ce que vous faites dans Kubernetes est à un appel API de vous.

_Voulez-vous déployer un conteneur ?_ Il y a un point de terminaison REST pour cela.

_Peut-être souhaitez-vous provisionner un équilibreur de charge ?_ Pas de problème. Il suffit d'appeler cette API.

_Voulez-vous provisionner du stockage ?_ Veuillez envoyer une requête POST à cette URL.

Tout ce que vous faites dans Kubernetes consiste à appeler des API.

Et il y a beaucoup de bonnes raisons d'être excité par cela :

* Vous pouvez créer des scripts et des démons qui interagissent avec l'API de manière programmatique
* L'API est versionnée ; lorsque vous mettez à niveau votre cluster, vous pouvez continuer à utiliser l'ancienne API et migrer progressivement
* Vous pouvez installer Kubernetes dans n'importe quel fournisseur de cloud ou centre de données, et vous pouvez exploiter la même API

Vous pouvez penser à Kubernetes comme une couche au-dessus de votre infrastructure.

Et puisque cette couche est générique et peut être installée n'importe où, vous pouvez toujours l'emporter avec vous.

Amazon Web Services est trop cher ?

**Pas de problème.**

Vous pouvez installer Kubernetes sur Google Cloud Platform et y déplacer vos charges de travail.

Ou peut-être pouvez-vous garder les deux car avoir une stratégie de haute disponibilité est toujours utile.

Mais peut-être que vous ne me croyez pas.

C'est trop beau pour être vrai, et je vends de la fumée et des miroirs.

Permettez-moi de vous montrer.

### Économiser sur votre facture cloud avec Kubernetes

Netlify est une plateforme pour construire, déployer et gérer des sites web statiques.

Elle a son propre pipeline CI, donc chaque fois que vous poussez un changement dans un dépôt, votre site web est reconstruit.

Netlify a réussi à migrer vers Kubernetes, à doubler sa base d'utilisateurs, mais a tout de même maintenu les coûts inchangés.

C'est une excellente nouvelle !

Imaginez économiser 50 % de votre facture Google Cloud Platform !

Mais Netlify n'est pas la seule.

Qbox — une entreprise qui se concentre sur Elastic Search hébergé — a réussi à économiser à nouveau 50 % par mois sur les factures AWS !

Dans le processus, ils ont également [open sourcé leurs efforts en opérations multi-cloud](https://github.com/supergiant/supergiant).

Si vous n'êtes toujours pas impressionné, vous devriez consulter la presse faite par OpenAI.

OpenAI est une entreprise de recherche à but non lucratif qui se concentre sur l'intelligence artificielle et l'apprentissage automatique. Ils ont écrit un algorithme pour jouer au jeu en ligne multijoueur Dota comme le ferait n'importe quel joueur humain.

Mais ils sont allés plus loin et ont entraîné une équipe de machines à jouer ensemble.

Et ils ont utilisé Kubernetes pour mettre à l'échelle leur modèle d'apprentissage automatique dans le cloud.

Vous vous demandez les détails de leur cluster ?

_128000 vCPU_

C'est environ 16000 MacBook Pros.

_256 Nvidia Tesla P100_

C'est 2100 Teraflops de performance en virgule flottante 16 bits.

La même chose que vous obtiendriez en exécutant 525 PlayStation 4.

_Pouvez-vous deviner le coût par heure ?_

_Non ?_

Seulement 1280 $/h pour 128000 vCPU et 400 $ pour les 256 Nvidia P100.

Ce n'est pas beaucoup considérant que gagner des tournois Dota pourrait vous rapporter des prix de l'ordre de millions de dollars.

Alors, qu'attendez-vous ?

Préparez-vous à adopter Kubernetes et à économiser sur votre facture cloud !

### Notes finales

Kubernetes et les conteneurs sont là pour rester.

Avec le soutien d'entreprises telles que Google, Microsoft, Red Hat, Pivotal, Oracle, IBM, et bien d'autres, il est difficile de croire qu'il ne s'imposera pas.

De nombreuses entreprises prennent une longueur d'avance sur Kubernetes et rejoignent la révolution.

Non seulement les startups et les PME, mais aussi les grandes entreprises comme les banques, les institutions financières et les compagnies d'assurance parient sur les conteneurs et Kubernetes pour l'avenir.

Même les entreprises investies dans l'Internet des objets et les systèmes embarqués.

C'est encore les débuts et la communauté a le temps de mûrir, mais vous devriez garder un œil attentif sur l'innovation dans ce domaine.

### C'est tout pour aujourd'hui !

Un grand merci à [Andy Griffiths](https://andrewgriffithsonline.com/), [John Topley](http://johntopley.com/) et [Walter Miani](https://www.linkedin.com/in/waltermiani/) pour avoir lu une ébauche de cet article et offert des suggestions inestimables.

Si vous avez apprécié cet article, vous pourriez trouver intéressant de lire :

* [Commencer avec Docker et Kubernetes sur Windows 10](https://learnk8s.io/blog/installing-docker-and-kubernetes-on-windows) où vous mettrez les mains dans le cambouis et installerez Docker et Kubernetes dans votre environnement Windows.
* [3 astuces simples pour des images Docker plus petites](https://learnk8s.io/blog/smaller-docker-images). Les images Docker n'ont pas besoin d'être grandes. Apprenez à mettre vos images Docker au régime !

### Devenez un expert dans le déploiement et la mise à l'échelle des applications dans Kubernetes

Prenez une longueur d'avance avec nos cours pratiques et apprenez à maîtriser la scalabilité dans le cloud.

Apprenez à :

* Gérer le trafic des sites web les plus fréquentés sans transpirer
* Mettre à l'échelle vos travaux sur des milliers de serveurs et réduire le temps d'attente de jours à minutes
* Avoir l'esprit tranquille en sachant que vos applications sont hautement disponibles avec une configuration multi-cloud
* Économiser beaucoup d'argent sur votre facture cloud en utilisant uniquement les ressources dont vous avez besoin
* Supercharger votre pipeline de livraison et déployer des applications 24h/24 et 7j/7

[Devenez un expert en Kubernetes](https://learnk8s.io/training) →

_L'article a été publié à l'origine sur [learnk8s.io](https://learnk8s.io/blog/what-is-kubernetes)_
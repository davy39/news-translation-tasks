---
title: Qu'est-ce que le Cloud Computing ? Expliqué pour les débutants
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-01-16T19:03:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-cloud-computing-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-210158--1-.jpg
tags:
- name: Cloud
  slug: cloud
- name: Cloud Computing
  slug: cloud-computing
seo_title: Qu'est-ce que le Cloud Computing ? Expliqué pour les débutants
seo_desc: "You may not always be aware of it, but you're enjoying the many fruits\
  \ of the cloud just about every hour of every day. Many of the joys (and horrors)\
  \ of modern life would be impossible without it. \nBefore we talk about what it\
  \ does and where it's ta..."
---

Vous n'en êtes peut-être pas toujours conscient, mais vous profitez des nombreux fruits du cloud presque toutes les heures de chaque jour. Beaucoup des joies (et des horreurs) de la vie moderne seraient impossibles sans lui. 

Avant de parler de ce qu'il fait et de là où il nous mène, nous devrions expliquer exactement ce que c'est.

## Qu'est-ce que le Cloud ?

Le "cloud" consiste à utiliser les ordinateurs d'autres personnes plutôt que le vôtre. C'est tout. Non, vraiment.

Les fournisseurs de cloud exécutent de nombreux serveurs de calcul (qui ne sont que des ordinateurs conçus pour "servir" des applications et des données en réponse à des demandes externes), des dispositifs de stockage et du matériel de mise en réseau. Chaque fois que l'envie vous en prend, vous pouvez provisionner des unités de ces serveurs, dispositifs et capacité de mise en réseau pour vos propres charges de travail. 

Lorsque vous ajoutez des millions d'autres utilisateurs pris par des impulsions similaires, vous obtenez le cloud moderne.

Pour de nombreuses applications - bien que pas toutes - il existe d'énormes avantages en termes de coût et de performance à déployer dans un cloud. Et d'innombrables applications - qu'elles soient petites, grandes ou colossales - ont trouvé des foyers productifs sur une plateforme cloud ou une autre. 

Alors voyons comment tout cela fonctionne et ce que vous pourriez être en mesure de faire avec.

Cet article a été tiré du livre, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). Si vous préférez regarder ce chapitre sous forme de vidéo, n'hésitez pas à suivre ici :

%[https://www.youtube.com/watch?v=eufNv-vpLZE]

# Modèles de déploiement de serveurs d'application

Au fil des décennies, nous avons connu plusieurs modèles pour exécuter des charges de travail de serveur. D'une certaine manière, tous ces changements ont été le produit de seulement deux technologies :

* Les protocoles de mise en réseau qui permettent la communication entre les nœuds connectés
* La virtualisation qui permet une utilisation rapide, efficace et rentable des ressources matérielles pour des utilisations multiples et parallèles

La mise en réseau, largement parce qu'elle est maintenant une technologie si stable et bien établie, n'est pas quelque chose sur lequel nous allons nous concentrer ici. Mais nous reviendrons à la virtualisation un peu plus tard.

## Comment fonctionnent les centres de données locaux

Dans le temps, si vous vouliez lancer un nouveau serveur pour effectuer une tâche de calcul, c'était tout un processus.

Vous passiez une semaine ou deux à calculer la puissance de calcul dont vous auriez besoin pour votre travail, vous contactiez les représentants commerciaux de quelques vendeurs de matériel, vous attendiez qu'ils vous reviennent avec des offres, puis vous compariez les offres. Ensuite, lorsque vous en aviez sélectionné une, vous attendiez encore quelques semaines pour que votre nouveau matériel soit livré. Ensuite, vous assembliez toutes les pièces, vous branchiez le tout et vous commenciez à charger le logiciel.

La salle où vos serveurs fonctionnaient avait besoin d'une alimentation électrique fiable et robuste et d'un système de refroidissement : comme les enfants en colère, les serveurs génèrent beaucoup de chaleur mais n'aiment pas être chauds. Vous ne voudriez probablement pas faire d'autre travail dans cette salle, car le bruit des ventilateurs de refroidissement internes puissants de vos serveurs serait difficile à ignorer.

Bien que les serveurs déployés localement vous donnaient tout le contrôle direct et manuel sur votre matériel dont vous pourriez avoir besoin, cela avait un coût. 

Pour une chose, les opportunités de redondance de l'infrastructure (et la fiabilité qui en découle) étaient limitées. Après tout, même si vous sauvegardiez régulièrement vos données (et en supposant que vos sauvegardes étaient fiables), elles ne vous protégeraient toujours pas d'un incident à l'échelle de l'installation comme un incendie catastrophique. 

Vous devriez également gérer votre propre mise en réseau, ce qui pourrait être particulièrement délicat - et risqué - lorsque des clients distants nécessitaient un accès depuis l'extérieur de votre bâtiment.

Au fait, ne vous laissez pas tromper par mon utilisation trompeuse du passé ici ("étaient limitées", "sauvegardées"). Il y a encore beaucoup de charges de travail de toutes tailles qui tournent joyeusement dans des centres de données sur site. Mais la tendance est, sans aucun doute, dirigée dans l'autre sens.

## Qu'est-ce que la virtualisation ?

Comme je l'ai suggéré plus tôt, la virtualisation est la technologie qui, plus que toute autre, définit l'internet moderne et les nombreux services qu'il permet. 

À sa base, la virtualisation est un tour de logiciel astucieux qui vous permet de convaincre un système d'exploitation qu'il est seul sur un ordinateur bare metal alors qu'il est, en fait, l'un des nombreux systèmes d'exploitation partageant un seul ensemble de ressources physiques. 

Un système d'exploitation virtuel se verra attribuer de l'espace sur un disque de stockage virtuel, de la bande passante via une interface réseau virtuelle et de la mémoire à partir d'un module RAM virtuel.

Voici pourquoi c'est une si grande affaire. Supposons que les disques de stockage sur votre serveur hôte aient une capacité totale de deux téraoctets et que vous ayez 64 Go de RAM. Vous pourriez avoir besoin de 10 Go de stockage et de 10 Go de mémoire pour le système d'exploitation hôte (ou, _hyperviseur_ comme certains hôtes de virtualisation sont appelés). 

Cela vous laisse beaucoup de place pour vos instances de système d'exploitation virtuel. Vous pourriez facilement lancer plusieurs instances virtuelles, chacune allouée avec suffisamment de ressources pour accomplir leurs tâches individuelles. 

Lorsque une instance particulière n'est plus nécessaire, vous pouvez l'éteindre, libérant ses ressources pour qu'elles soient instantanément disponibles pour d'autres instances effectuant d'autres tâches.

Mais les vrais avantages viennent de la manière dont la virtualisation peut être si efficace avec vos ressources. Une instance pourrait, par exemple, se voir attribuer de la RAM et du stockage qui, plus tard, s'avèrent insuffisants. Vous pouvez facilement allouer plus de chaque depuis le pool - souvent sans même éteindre votre instance. De même, vous pouvez réduire l'allocation pour une instance lorsque ses besoins diminuent.

Cela élimine toutes les conjectures de la planification des serveurs. Vous n'avez besoin d'acheter (ou de louer) que des ressources matérielles génériques et de les attribuer en unités incrémentielles selon les besoins. Il n'est plus nécessaire de regarder dans un futur lointain en essayant d'anticiper ce que vous ferez dans cinq ans. Cinq _minutes_ sont plus que suffisantes pour la planification.

Maintenant, imaginez que tout cela se passe à une échelle beaucoup plus grande : supposons que vous avez des milliers de serveurs fonctionnant dans un entrepôt quelque part qui hébergent des charges de travail pour des milliers de clients. Peut-être qu'un client demande soudainement un autre téraoctet d'espace de stockage. 

Même si le disque que le client utilise actuellement est saturé, vous pouvez facilement ajouter un autre téraoctet depuis un autre disque, peut-être un branché à quelques centaines de mètres de l'autre côté de l'entrepôt. Le client ne remarquera jamais la différence, mais le changement peut être pratiquement instantané.

### Bétail vs animaux de compagnie

La virtualisation des serveurs a changé la façon dont nous voyons l'informatique et même le développement de logiciels. 

Il n'est plus aussi important de construire des interfaces de configuration dans vos applications qui vous permettront de régler et de corriger les choses à la volée. Il est souvent plus efficace pour vos développeurs et administrateurs système de construire une image de système d'exploitation personnalisée (presque toujours basée sur Linux) avec tous les logiciels préconfigurés. Vous pouvez ensuite lancer de nouvelles instances virtuelles basées sur votre image chaque fois qu'une mise à jour est nécessaire.

Si quelque chose ne va pas ou si vous devez appliquer un changement, vous créez simplement une nouvelle image, éteignez votre instance, puis la remplacez par une instance exécutant votre nouvelle image. 

En effet, vous traitez vos serveurs virtuels de la manière dont un agriculteur traite les vaches : lorsque le moment est venu (comme il le sera inévitablement), vous retirez une vieille ou malade vache, puis en amenez une autre (plus jeune) pour la remplacer.

Quiconque a déjà été impliqué dans l'administration de salles de serveurs héritées serait horrifié par une telle pensée ! Nos anciennes machines physiques étaient traitées comme des animaux de compagnie bien-aimés. Au moindre signe de détresse, nous serions là, préoccupés, à ses côtés, essayant de diagnostiquer quel était le problème et comment il pouvait être résolu. 

Si tout le reste échouait, nous serions forcés de redémarrer le serveur, espérant contre tout espoir qu'il redémarre. Si même _cela_ n'était pas suffisant, nous cédions et remplacions le matériel.

Mais la modularité que nous obtenons de la virtualisation nous donne toutes sortes de nouvelles flexibilités. Maintenant que les considérations matérielles ont été largement abstraites, notre principal objectif est le logiciel (qu'il s'agisse de systèmes d'exploitation entiers ou d'applications individuelles). Et le logiciel, grâce aux langages de script, peut être automatisé. 

Ainsi, en utilisant des outils d'orchestration comme Ansible, Terraform et Puppet, vous pouvez automatiser la création, le provisionnement et la gestion complète du cycle de vie des instances de service d'application. Même la gestion des erreurs peut être intégrée dans votre orchestration, de sorte que vos applications pourraient être conçues pour corriger magiquement leurs propres problèmes.

### Machines virtuelles vs conteneurs

Les instances virtuelles se présentent sous deux formes. Les machines virtuelles (ou VM) sont des systèmes d'exploitation complets qui s'exécutent sur - mais dans une certaine mesure indépendamment de - la machine hôte. 

C'est le type de virtualisation qui utilise un hyperviseur pour administrer l'accès de chaque VM aux ressources matérielles sous-jacentes, mais de telles VM sont généralement laissées à vivre comme elles l'entendent. 

Des exemples d'environnements d'hyperviseur incluent le projet open source Xen, VMware ESXi, Oracle's VirtualBox et Microsoft Hyper-V.

Les conteneurs, en revanche, partageront non seulement le matériel, mais aussi le noyau logiciel du système d'exploitation hôte. Cela rend les instances de conteneurs beaucoup plus rapides et plus légères (puisque leurs images n'ont pas besoin d'inclure un noyau). 

Non seulement cela signifie que les conteneurs peuvent se lancer presque instantanément, mais que leurs systèmes de fichiers peuvent être transportés entre les hôtes et partagés. La portabilité signifie que les environnements d'instance peuvent être reproduits de manière fiable n'importe où, rendant la collaboration et le déploiement automatisé non seulement possibles, mais faciles.

Des exemples de technologies de conteneurs incluent LXD et Docker. Et les implémentations de conteneurs d'entreprise incluent le système d'orchestration open source Kubernetes de Google.

## Comment fonctionnent les clouds publics

Les plateformes de cloud public ont élevé l'abstraction et l'allocation dynamique des ressources de calcul au rang d'art. Les grands fournisseurs de cloud exploitent de vastes réseaux de centaines de milliers de serveurs et des nombres inimaginables de dispositifs de stockage répartis dans des centres de données à travers le monde.

N'importe qui, n'importe où, peut créer un compte utilisateur avec un fournisseur, demander une instance en utilisant une capacité définie sur mesure, et avoir un serveur web entièrement fonctionnel et accessible au public en quelques minutes. Et comme vous ne payez que pour ce que vous utilisez, vos frais refléteront de près vos besoins réels.

Un serveur web que je fais fonctionner sur Amazon Web Services (AWS) pour héberger deux ou trois de mes sites web modérément fréquentés ne me coûte que 50 $ par an environ. Et il a assez de puissance pour gérer beaucoup plus de trafic. 

Les ressources AWS utilisées par la société de streaming vidéo Netflix coûteront probablement un peu plus - sans aucun doute des millions de dollars par an. Mais ils pensent clairement qu'ils obtiennent une bonne affaire et préfèrent utiliser AWS plutôt que d'héberger leur infrastructure eux-mêmes.

Juste qui sont tous ces fournisseurs de cloud public, je suis sûr que vous vous demandez ? Eh bien, cette conversation doit commencer (et, souvent, se terminer) avec AWS. Ils sont l'éléphant dans chaque pièce. Les millions de charges de travail s'exécutant dans les énormes et omniprésents centres de données d'Amazon, ainsi que leur rythme frénétique d'innovation, en font le joueur à battre dans cette course. Et cela ne tient même pas compte des milliards de dollars de bénéfices nets qu'ils empochent chaque trimestre.

À ce stade, la seule concurrence sérieuse à AWS est Microsoft's Azure qui fait un assez bon travail pour suivre les catégories de services et, à tous égards, réalise de bons bénéfices dans le processus. Il y a aussi Alibaba Cloud qui est principalement axé sur le marché asiatique à ce stade. Google Cloud est dans la partie, mais semble se concentrer sur un ensemble plus restreint de services où ils peuvent réalistement rivaliser.

Comme la barrière à l'entrée sur le marché est redoutable, il n'y a que quelques autres qui se font remarquer, notamment Oracle Cloud, IBM Cloud et, avec une convention de nommage bienvenue, Digital Ocean.

## Comment fonctionnent les clouds privés

La bonté du cloud peut également être obtenue plus près de chez vous, si c'est ce que vous recherchez. Rien ne vous empêche de construire vos propres environnements cloud sur une infrastructure située dans votre propre centre de données. 

En fait, il existe de nombreux logiciels matures qui géreront le processus pour vous. Parmi ceux-ci, les environnements open source OpenStack (openstack.org) et VMware's vSphere (vmware.com/products/vsphere.html) sont particulièrement notables.

La construction et l'exécution d'un cloud est un processus très compliqué et ne convient pas aux amateurs ou aux timides. Et je n'essaierais pas de télécharger et de tester OpenStack - même juste pour expérimenter - à moins que vous n'ayez une station de travail rapide et puissante pour servir d'hôtes cloud et au moins quelques machines pour les nœuds.

Vous pouvez également avoir les deux en maintenant certaines opérations proches de chez vous tout en externalisant d'autres opérations dans le cloud. Cela s'appelle un déploiement de cloud hybride. 

Peut-être, par exemple, des restrictions réglementaires vous obligent à garder une base de données backend d'informations sensibles sur la santé des clients dans les quatre murs de votre propre opération, mais vous aimeriez que vos serveurs web accessibles au public s'exécutent dans un cloud public. Il est possible de connecter des ressources d'un domaine (par exemple, AWS) à un autre (votre centre de données) pour créer un tel arrangement.

En fait, il existe des moyens d'intégrer étroitement vos ressources locales et cloud. Le service _VMware Cloud on AWS_ facilite (relativement) l'utilisation de l'infrastructure VMware déployée localement pour gérer de manière transparente les ressources AWS (aws.amazon.com/vmware).

# La valeur de l'externalisation de vos opérations informatiques

Pourquoi pourriez-vous vouloir migrer des charges de travail vers le cloud ? Vous pourriez finir par économiser beaucoup d'argent. Donc, il y a cela. Bien sûr, cela ne fonctionnera pas de cette manière pour tous les déploiements, mais il semble y avoir beaucoup de cas d'utilisation où c'est le cas. 

Pour vous aider à prendre des décisions éclairées, les plateformes cloud fournissent souvent des calculateurs sophistiqués pour comparer les coûts d'exécution d'une application localement par rapport à ce que cela coûterait dans le cloud. La version AWS de cela est ici : aws.amazon.com/tco-calculator

Une partie du calcul des prix est la _manière_ dont vous payez. Le modèle traditionnel sur site impliquait des investissements initiaux importants pour du matériel de serveur coûteux que vous espériez livrer suffisamment de valeur au cours des cinq à dix prochaines années pour justifier l'achat. Ces investissements sont connus sous le nom de _dépenses en capital_ ("Capex").

Les services cloud, en revanche, sont facturés de manière incrémentielle (à l'heure, ou même à la minute) en fonction du nombre d'unités de service que vous consommez réellement. Cela est normalement classé comme _dépenses d'exploitation_ (Opex). 

En utilisant le modèle Opex, si vous devez exécuter une charge de travail de serveur seulement une fois tous les quelques jours pendant cinq minutes à la fois en réponse à un événement de déclenchement externe, vous pouvez automatiser l'utilisation d'une charge de travail "sans serveur" (en utilisant un service comme Lambda d'Amazon) pour ne fonctionner que lorsque nécessaire. Coûts totaux : peut-être seulement quelques centimes par mois pour couvrir ces minutes où le service est réellement en cours d'exécution.

Outre les considérations de coût, il se passe beaucoup plus de choses dans le monde du cloud qui devraient attirer votre attention. Vous avez déjà vu comment le temps de latence entre la décision de déployer un nouveau serveur sur site et son déploiement réel (semaines ou mois) se compare à un processus de décision/déploiement similaire dans un cloud public (quelques minutes). Mais les grands fournisseurs de cloud sont également positionnés pour fournir des environnements significativement plus sécurisés et fiables.

Par exemple, vous vous souvenez peut-être de notre histoire sur l'attaque DDoS de mon article sur [Comprendre la sécurité numérique](https://www.freecodecamp.org/news/understanding-digital-security/). C'était l'incident où l'équivalent de 380 000 livres PDF de données étaient utilisés pour bombarder un service web hébergé par AWS chaque seconde... et le service a survécu. Êtes-vous confiant de pouvoir faire cela vous-même ?

Et qu'en est-il de la fiabilité par la redondance ? Votre infrastructure sur site survivrait-elle à une perte catastrophique de vos locaux ? Même si vous avez fait ce qu'il fallait et maintenu des sauvegardes hors site, combien de temps vous faudrait-il pour les appliquer à du matériel reconstruit, connecté au réseau et fonctionnel ?

Les grandes plateformes cloud exécutent des centres de données à travers des emplacements physiquement distants dans le monde entier. Elles rendent facile (et dans certains cas inévitable) la réplication de vos données et applications dans plusieurs emplacements afin que, même si un centre de données tombe en panne, les autres seront intacts. Pouvez-vous reproduire cela ?

Les fournisseurs de cloud gèrent également des réseaux de distribution de contenu (CDN) vous permettant d'exposer des copies en cache de données fréquemment consultées à des emplacements de périphérie proches de l'endroit où vos clients vivent sur terre. Cela réduit considérablement la latence, améliorant l'expérience utilisateur que vos clients obtiendront. Est-ce quelque chose que vous pouvez faire vous-même ?

Une dernière pensée. La plupart des grands investissements dans les nouvelles technologies de l'information ces jours-ci sont injectés dans les écosystèmes cloud. C'est en partie parce que les grands fournisseurs de cloud génèrent de l'argent beaucoup plus rapidement qu'ils ne peuvent espérer le dépenser. Mais c'est aussi parce qu'ils sont impliqués dans une course à la vie ou à la mort pour capturer de nouveaux segments du marché de l'infrastructure avant que la concurrence ne les revendique.

Le résultat est que le taux d'innovation dans le cloud est stupéfiant. Je gagne ma vie en gardant un œil attentif sur AWS, et même moi, je manque régulièrement des annonces de nouveaux produits. 

L'une des raisons pour lesquelles j'évite d'inclure des captures d'écran de la console de gestion AWS dans mes livres et cours vidéo est que leur console est mise à jour si souvent que les images seront souvent obsolètes avant que le livre ne soit publié.

Dans certains cas, cela pourrait signifier que les déploiements locaux fonctionneront avec un désavantage intégré simplement parce qu'ils n'auront pas accès aux technologies de pointe équivalentes.

# Les risques de l'externalisation de vos opérations informatiques

Ayant dit tout cela, comme pour la plupart des choses dans la vie, choisir entre le cloud et le local ne sera pas toujours aussi facile que je l'ai peut-être fait paraître. 

Il peut encore y avoir, par exemple, des lois et des règles vous obligeant à garder vos données locales. Il y aura également des cas où les mathématiques ne fonctionnent tout simplement pas : parfois, il est vraiment moins cher de faire les choses dans votre propre centre de données.

Vous devriez également vous soucier de l'enfermement dans une plateforme. La courbe d'apprentissage nécessaire avant que vous ne soyez prêt à lancer des déploiements cloud complexes et multi-niveaux n'est pas triviale. Et vous pouvez être sûr que la manière dont cela fonctionne sur AWS ne sera probablement pas tout à fait la même que ce qui se passe sur MS Azure. L'investissement en connaissances que vous devrez faire une fois que vous aurez fait votre choix sera probablement coûteux.

Mais que se passe-t-il si les politiques du fournisseur changent soudainement d'une manière qui vous force à quitter la plateforme ? Ou s'ils font réellement faillite (cela pourrait arriver : Kodak, Blockbuster Video et Palm étaient autrefois grands, eux aussi) ? 

Et qu'en est-il d'être bloqué hors de votre compte pour une raison quelconque ? Combien de temps vous faudrait-il pour tout réoutiller et recharger ailleurs ?

Réfléchissez simplement à l'avance et assurez-vous de faire un choix rationnel.

Merci d'avoir lu !

_Les vidéos YouTube de tous les dix chapitres de ce livre [sont disponibles ici](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Beaucoup plus de bonté technologique - sous forme de livres, de cours et d'articles - [peut être obtenue ici](https://bootstrap-it.com). Et envisagez de suivre mes [cours sur AWS, la sécurité et la technologie des conteneurs ici](https://www.udemy.com/user/david-clinton-12/)._
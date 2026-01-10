---
title: 'Comprendre les Microservices : De l''Idée à la Ligne de Départ'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T04:04:05.000Z'
originalURL: https://freecodecamp.org/news/microservices-from-idea-to-starting-line-ae5317a6ff02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SlOGiH26JSP3h6uijnAi3A.jpeg
tags:
- name: learning
  slug: learning
- name: Microservices
  slug: microservices
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: 'Comprendre les Microservices : De l''Idée à la Ligne de Départ'
seo_desc: 'By Michael Douglass

  Over the last two months, I have invested most of my free time learning the complete
  ins-and-outs of what the microservices architecture really entails. After much reading,
  note taking, white-boarding, and many hours writing, I fe...'
---

Par Michael Douglass

Au cours des deux derniers mois, j'ai investi la plupart de mon temps libre à apprendre les tenants et aboutissants de l'architecture des microservices. Après de nombreuses lectures, prises de notes, sessions de brainstorming et heures d'écriture, je sens que j'ai atteint un niveau de compréhension tel que je suis prêt à faire le premier pas. Permettez-moi de partager ce que j'ai appris de A à Z.

![Image](https://cdn-media-1.freecodecamp.org/images/2rznJAMhE-qZgITEtIMEB-FIJOASann1LjP1)
_J'ai lu et appris. Maintenant, il est temps de faire ces premiers pas dans le monde des Microservices. D'abord, pour vous, je documente ce que j'ai appris et découvert jusqu'à présent. — Image courtesy of [Pexels.com](https://www.pexels.com/photo/bridge-feet-railings-shoes-244371/" rel="noopener" target="_blank" title=")_

### Microservices : Niveau Élevé, Qu'est-ce que c'est ?

Les microservices sont une architecture dans laquelle différentes parties composantes d'une conception logicielle sont créées et hébergées en tant que services individuels et isolés. Chacun est déployé séparément et ils communiquent via des interfaces réseau bien définies. Les microservices sont censés être « petits » (définition large) et limités à un contexte unique.

Il y a de nombreux avantages aux microservices. Grâce à leur isolation et à l'obligation stricte de communiquer via des interfaces bien définies, les microservices empêchent les solutions rapides et sales souvent trouvées dans les monolithes. Ces hacks à l'intérieur d'un monolithe entraînent une perte de cohésion et une augmentation du couplage — deux causes principales de complexité.

Beaucoup soutiendront que vous pouvez maintenir ce comportement dans un monolithe. En réalité, parce que c'est facile et parce qu'il y a trop peu d'architectes travaillant dans nos bases de code, les monolithes finissent souvent par échouer à cause de cette même défaillance.

> La complexité vient d'une faible cohésion et d'un couplage élevé. Les microservices fournissent la structure pour garder cela sous contrôle.

Cet avantage ne peut être surestimé. Parce que nous gardons le monstre de la complexité sous contrôle, le développement sur des systèmes vieux de dix ans peut continuer à avancer à la vitesse du développement lorsque le système était tout neuf.

Encore et encore, la complexité causée par une faible cohésion et un couplage serré a été la cause d'un développement lent sur des projets plus anciens. La cohésion et le couplage sont traditionnellement la dette technique qui nous retient, nous ralentissant. Accumulez-en suffisamment au fil des ans, et vous vous retrouverez à avancer péniblement.

Lorsque les services sont écrits en les gardant à l'esprit, et que l'infrastructure le permet, d'autres avantages peuvent inclure la scalabilité horizontale, la testabilité, la fiabilité, l'observabilité, la remplaçabilité et l'indépendance du langage.

L'inconvénient des microservices est que pour obtenir ces avantages, vous devez fournir une infrastructure sous-jacente qui les supporte. Sans ce support, vous pouvez facilement vous retrouver avec un système peu fiable et opaque — ou vous vous retrouvez à réinventer la roue de la fiabilité dans chaque service. Cela nous amène parfaitement à la section suivante...

### Microservices : Exigences de Haut Niveau (Le Macro)

Un environnement qui supporte les microservices a fondamentalement besoin d'un ensemble d'exigences de base pour assurer un certain niveau de cohérence. Si vous allez exécuter des microservices, votre organisation doit être prête à supporter le surcoût de leur démarrage et de leur support. Le surcoût ne sera pas insignifiant. Cela prendra du temps et de l'argent pour bien faire des microservices.

Une architecture de microservices réussie doit avoir un comité ou un groupe interne responsable de la définition de l'**architecture macro** — cela définira quelle infrastructure sera fournie pour le développement et l'exploitation des microservices ainsi que les politiques auxquelles tous les microservices doivent adhérer. Ce comité doit être composé des meilleurs éléments de votre personnel de développement, et il peut même s'agir d'une ou plusieurs personnes qui ne travaillent pas encore pour vous.

> L'architecture macro est à la fois une infrastructure fournie et des exigences politiques pour tous les microservices.

L'architecture macro de chaque organisation sera unique. Chaque domaine listé ci-dessous est complètement ouvert à la négociation sur la manière de tracer la ligne pour votre groupe : vous pouvez fournir aux équipes un service ou une bibliothèque de code fixe pour fournir la fonctionnalité requise. Vous pouvez soit imposer son utilisation, soit en faire une utilisation optionnelle. Vous pourriez simplement fournir des critères d'acceptation auxquels un microservice doit adhérer, mais ne fournir aucune bibliothèque ou service implémenté pour aider à satisfaire l'exigence. Enfin, vous pourriez choisir de ne rien faire et de ne rien exiger pour une catégorie donnée.

> Choisissez judicieusement ce que vous laissez de côté dans votre architecture macro. Pour chaque choix que vous permettez aux équipes de développement individuelles de faire, vous devez être prêt à vivre avec des décisions, des implémentations et des comportements opérationnels différents.

Vous êtes le comité, et il est toujours préférable que les personnes de l'organisation prennent ces décisions — par conséquent, je ne peux pas vous fournir un manifeste tout prêt.

Lorsque vous commencez, il est également important de garder cette documentation d'architecture macro ouverte au changement et réceptive aux besoins des équipes et de l'entreprise. Maintenant, tournons-nous vers l'examen des différentes catégories pour lesquelles des décisions d'architecture macro doivent être prises.

#### Intégration Continue/Livraison Continue

Au cœur du concept de microservices se trouve la capacité à construire et exécuter des tests de manière très rapide. Chaque commit dans le microservice doit aboutir à une build testée. Une fois les tests passés et le système de build satisfait, un déploiement en production par bouton-poussoir ou automatique est l'aspect important suivant. Réduire le temps de déploiement permet une itération rapide et active toute une série de bonnes pratiques de codage.

C'est facile à réaliser de nos jours. Il existe de nombreux systèmes de build qui fournissent un accès aux builds de pipeline. [Team City](https://www.jetbrains.com/teamcity/). [Bamboo](https://www.atlassian.com/software/bamboo). [Jenkins avec Blue Ocean](https://jenkins.io/). Essayez-les et choisissez-en un. Pour la plupart, les ensembles de fonctionnalités sont assez standard parmi les leaders du secteur.

Une organisation devrait s'efforcer d'avoir une cohérence dans la manière dont les services sont construits et déployés. Par conséquent, l'architecture macro devrait définir l'outil de build et les processus de pipeline. Les équipes devraient avoir une voix dans la conversation menant au choix, mais elles ne devraient pas être autorisées à faire cavalier seul sur ce point.

#### Machines Virtuelles/Conteneurs

Main dans la main avec CI/CD se trouve la capacité à lancer un certain nombre d'instances d'une version spécifique de votre service. L'architecture macro doit considérer comment les équipes géreront cela pour les environnements de développement, de test, de staging et de production.

Pour le staging et la production, vous êtes souvent confronté au désir de faire des déploiements en canari avec un retour en arrière trivial en cas d'échec. Avoir une infrastructure commune, des politiques et des procédures autour de la manière dont vous emballez et déployez un service rendra cela plus facile pour le développement et les opérations.

La surveillance de charge et la gestion du contrôle des instances doivent également être considérées et facilitées par cette partie de l'architecture macro. Savoir quand plus d'instances d'un service donné sont nécessaires, et avoir une manière cohérente de les mettre en production sera crucial pour le succès à long terme.

#### Journalisation

Il est vital de surveiller vos microservices en production. Pour le faire efficacement, vous devez permettre une localisation rapide des informations disparates. Cela implique que l'architecture macro devrait fortement considérer l'inclusion des éléments suivants :

1. Un service de journalisation pour la journalisation centralisée. Cela peut être la [Elastic Stack](https://www.elastic.co/products), [Slack](https://slack.com/), [Graylog](https://www.graylog.org/), et autres de leur espèce. Vous voulez une stack de journalisation qui inclut un parseur/visualiseur puissant car vous allez traiter beaucoup de données. Une partie de votre infrastructure peut être l'un de ces services, et une garantie que chaque hôte dans l'environnement sera configuré pour transférer les fichiers de journalisation au nom de chaque service.
2. Définition des identifiants de trace pour permettre la localisation de tous les journaux à travers tous les microservices traitant une seule requête externe. Le concept ici est que, pour chaque requête externe entrant dans vos microservices, vous générez un identifiant unique, et cet identifiant est passé à tous les appels internes de microservices utilisés pour traiter cette requête. Ainsi, à travers une recherche pour un seul identifiant de trace, vous pouvez trouver tous les appels de microservices résultant d'un seul accès externe.
3. Exigences de formatage de base pour le serveur, le service, l'instance, l'horodatage et les identifiants de trace.

#### Surveillance

C'est un autre « doit fournir » pour l'architecture macro. Les microservices devront chacun décider des meilleures métriques à mesurer et à surveiller pour assurer le succès individuel, mais l'architecture macro aura besoin d'une instrumentation spécifique de chaque service afin de fournir une supervision de la santé globale du système. Certains points de données macro incluent :

* Le volume de messages, d'échecs, de succès, de nouvelles tentatives et d'abandons.
* La latence des requêtes.
* Le ratio de messages reçus par rapport aux messages envoyés.
* L'état des disjoncteurs.
* Et plus. Beaucoup, beaucoup plus.

L'instrumentation est un domaine où [The Tao of Microservices](https://amzn.to/2G3g3Ly) brille vraiment, et je le recommande vivement pour une bonne compréhension de l'ampleur et de la profondeur de la surveillance dans les microservices.

#### Enregistrement et Localisation des Services

Cela est souvent négligé lorsqu'une architecture de microservices est petite car quelques microservices peuvent toujours se trouver relativement facilement. Cependant, avec le temps et l'augmentation du nombre de microservices, la configuration nécessaire pour connecter tout le monde de manière statique devient trop contraignante et éventuellement sujette aux erreurs. De nombreuses solutions peuvent être trouvées, y compris DNS et les services de configuration (etc, etc.)

L'architecture macro de votre environnement de microservices doit définir comment cela est fait — même si la première itération est `/etc/services.yaml` déployée et synchronisée sur tous les hôtes.

Ce n'est pas quelque chose que les équipes de développement sur des services individuels devraient mettre en place — cela devrait être ubiquitaire et géré au niveau de l'architecture macro.

Il existe de nombreux projets open source existants tentant de résoudre ce problème, y compris certains des logiciels de service mesh listés à la fin de cet article.

#### Mécanismes de Communication

Les microservices devraient avoir un certain niveau de contrôle sur la manière dont ils implémentent leurs interfaces. Le protocole au niveau réseau et le protocole au niveau application devraient fournir un certain niveau de flexibilité. L'utilisation de Google Protocol Buffers sur TCP brut pourrait être aussi disponible que l'utilisation de JSON RPC sur HTTPS. Cela dit, l'architecture macro devrait fournir quelques orientations, quelques restrictions, et peut-être même une certaine infrastructure pour aider à faciliter la communication.

Si une infrastructure de microservices va fonctionner ensemble dans un espace de noms de domaine commun sous des URI HTTPS, alors vous voudrez une standardisation autour de la dénomination et du routage. Les requêtes devraient avoir une méthode commune et cohérente par laquelle les requêtes utilisateur d'ingress ainsi que les requêtes de service à service sont authentifiées, autorisées et routées.

Une infrastructure de microservices qui souhaite permettre l'utilisation de la messagerie comme dispositif de communication devrait envisager de fournir un bus de messagerie géré par les opérations. Cela permet un développement et un déploiement rapides des services sans que les équipes aient besoin de se concentrer d'abord sur le démarrage puis sur la gestion à long terme d'un service de messagerie. Cela favorise également le découplage des services qui souhaitent communiquer via le service de messagerie — si je dois savoir quel service de mise en file d'attente de messagerie chaque service utilise, je deviens plus couplé.

Fournir l'infrastructure pour votre couche de messagerie vous permet également de fournir un routage de messages à vos services — quelque chose qui peut grandement améliorer la flexibilité de votre architecture macro. La capacité à router les requêtes à travers différentes versions d'un service en fonction de divers critères offre beaucoup de flexibilité et aide à maintenir davantage le découplage.

#### Équilibrage de Charge et Résilience

Les microservices sont souvent utilisés dans des environnements où la scalabilité et la disponibilité sont attendues. Traditionnellement, les dispositifs réseau fournissent des fonctionnalités d'équilibrage de charge. Mais dans un environnement de microservices, il est plus typique de voir cela déplacé dans la couche logicielle de l'infrastructure de l'architecture macro.

Le code à travers lequel les services communiquent peut utiliser la localisation de service pour découvrir tous les emplacements réseau d'un service donné, et il peut ensuite effectuer directement la logique d'équilibrage de charge à la périphérie distribuée.

La résilience signifie rester stable même face aux erreurs. Les nouvelles tentatives, les délais, les comportements par défaut, les comportements de mise en cache et la mise en file d'attente sont quelques-unes des façons dont les microservices fournissent la résilience.

Tout comme l'équilibrage de charge, une partie de la résilience est un match parfait pour l'infrastructure à gérer à la périphérie — comme les nouvelles tentatives et la rupture de circuit (réponses d'erreur automatiques pour les services dépassant un seuil d'échec dans le passé récent).

Cependant, le service individuel devrait considérer quel rôle de résilience il devrait jouer en interne. Par exemple, un système d'inscription de compte, où perdre une inscription équivaut à perdre de l'argent, devrait prendre en charge la garantie que chaque inscription passe — même si cela signifie une création différée qui entraîne un email au propriétaire du compte une fois réussie. La mise en file d'attente interne et la gestion des inscriptions en attente peuvent être mieux gérées directement par ce service critique.

#### Persistance : Base de Données, NoSQL, etc.

Une architecture de microservices isole complètement chaque microservice des autres. En fin de compte, ils comprennent mieux leurs propres besoins de stockage de données et devraient donc être encouragés individuellement à contrôler leur propre destin en ce qui concerne la persistance des données. Cependant, vous n'avez toujours pas besoin de permettre à l'Ouest sauvage de régner, et ainsi l'architecture macro devrait fournir des orientations (parfois lourdes).

Voici quelques options que vous pouvez envisager d'inclure dans l'architecture macro :

1. Un ou plusieurs services de stockage de données incluant une base de données relationnelle basée sur SQL et un système de stockage NoSQL. Ces services de stockage de données fournis devraient inclure des sauvegardes intégrées. Un microservice devrait utiliser des identifiants uniques avec un accès limité à un schéma restreint aux seules données de ce microservice. Dans ce schéma, l'équipe des opérations fournissant le service de stockage est responsable de son fonctionnement.
2. Si vous permettez aux microservices d'apporter leur propre persistance, vous devriez avoir des exigences politiques strictes pour les sauvegardes et la récupération après sinistre. Pensez aux sauvegardes hors site, au temps de récupération, au temps de basculement, etc. Dans ce modèle, l'équipe de développement est responsable du fonctionnement du service de stockage.

Vous devez absolument, sans aucun doute, refuser de permettre la mentalité traditionnelle « accès ouvert, une base de données pour les régner toutes » qui imprègne le monde du développement monolithique. Si vos services disparates sont capables de communiquer via la base de données, un couplage inattendu se produira. Les services ne doivent avoir accès qu'à leurs propres magasins de données, et la communication inter-services doit être maintenue via leurs interfaces réseau bien définies.

Je suis récemment tombé sur un couplage extrêmement désagréable de type base de données dans un ancien monolithe. La complexité était immédiatement évidente et ma tristesse a augmenté de manière exponentielle.

#### Sécurité

Vos services doivent savoir à qui ils parlent (authentification) et quelles données et opérations sont autorisées (autorisation) pour ladite identité. Il y a plusieurs concepts potentiels ici :

* Laissez le réseau IP protéger les services — si vous exécutez tous vos microservices sur un réseau protégé, et que vous souhaitez transférer la confiance à votre personnel de développement pour ne pas abuser de l'accès, alors cela pourrait fonctionner pour vous. Gardez à l'esprit qu'une brèche dans un seul service implique un accès complet à tous les autres services.
* Authentification au niveau du service — les clés partagées ou l'authentification basée sur des certificats permettent à un service appelé de valider un service appelant. Vous aurez besoin d'un moyen sécurisé de distribuer et de mettre à jour les clés et les certificats pour garder cela sécurisé. Utilisez un Service de Gestion des Clés.
* Authentification au niveau de l'utilisateur — non seulement les services parlent aux services, mais ils parlent souvent au nom d'un utilisateur ou même directement à un utilisateur. Il doit y avoir un moyen d'authentifier et d'autoriser l'identifiant au niveau de l'utilisateur pour la ressource en question.

Commencez simplement — c'est un domaine qui peut briser une organisation dès le départ, et il est probablement préférable de commencer simplement. Vous avez probablement déjà quelques services différents qui se parlent, et vous utilisez probablement des listes de contrôle d'accès IP pour les protéger. Commencez simplement, ajoutez de la complexité comme une évolution naturelle du système.

#### Amendement X — Pouvoirs Réservés

> Les pouvoirs non délégués à l'infrastructure par l'architecture macro sont réservés aux services individuels respectivement, ou aux développeurs de ceux-ci.

Ne sous-estimez pas le pouvoir de cette déclaration. Si l'architecture macro ne couvre pas un aspect de l'environnement, les développeurs sont libres de choisir et ils choisiront. Plus vous avez d'équipes, plus vous vous retrouverez à maintenir de solutions. Par conséquent, faites deux choses avec votre architecture macro :

1. Considérez très soigneusement ce que vous laissez de côté. Si vous suivez le principe « commencez petit », vous ne fournirez probablement pas beaucoup d'infrastructures prêtes à l'emploi pour couvrir les détails de l'architecture macro. Cela est parfaitement acceptable. Cependant, vous pouvez toujours fournir des orientations et des exigences autour de ces domaines afin de minimiser le chaos.
2. Itérez rapidement. Au fur et à mesure que les premiers services se mettent en ligne, rencontrez-vous et discutez de l'ensemble de l'architecture macro. Qu'est-ce qui fonctionne ? Qu'est-ce qui ne fonctionne pas ? Que devez-vous changer maintenant ? (Comme c'est agile de ma part !) Faites cela régulièrement. Vous entendrez cela à nouveau dans quelques instants.

### Qui Devrait Utiliser les Microservices ?

> Tout le monde devrait utiliser les Microservices.

Voilà, je l'ai dit, et je le défendrai sans relâche. Oui, je réalise qu'il y a beaucoup de gens, probablement bien plus intelligents et plus érudits que moi, qui déclarent, philosophiquement : « Si vous n'êtes pas Netflix et que vous n'êtes pas Amazon, alors le surcoût de l'utilisation d'une architecture de microservices va vous submerger. »

> L'idée que je dois être Netflix ou Amazon pour faire un usage productif d'une architecture de microservices me vient à l'esprit, et j'espère que vous me citerez sur ce point, un seul mot : des balivernes.

#### Tout est une Question de Taille...

La réalité ici est que plus votre organisation est petite, moins vos besoins pour une architecture de microservices entièrement développée sont importants. Cependant, il n'y a aucune raison d'abandonner tout le mouvement et de laisser derrière les avantages que ces personnes très intelligentes ont réalisés, même lorsque vous êtes une petite entreprise avec de petits services.

Vos premières conversations sur l'architecture macro des microservices doivent se concentrer précisément sur ce dont vous avez **besoin** pour commencer, puis déterminer comment mettre cela en place. Construisez quelques services, observez leurs comportements et apprenez de ce qui fonctionne et ne fonctionne pas pour vous.

Reconvenez votre comité d'architecture macro des microservices et utilisez votre nouvelle expérience ainsi que votre lecture saine et votre compréhension croissante de l'écosystème mondial de l'industrie pour déterminer quelle doit être la prochaine évolution de votre architecture macro. Rincez et répétez. Itérez.

> Votre architecture macro de microservices devrait évoluer en continu en parallèle avec le développement itératif quotidien que vous faites déjà.

Nous vivons et respirons ce monde « agile » de conception et de développement itératifs. Il y a très peu de raisons pour que cela ne s'applique pas à l'infrastructure entourant nos services. Même si vous ne réalisez jamais une architecture de microservices entièrement idéalisée, mais que vous avez ces conversations d'architecture et ajoutez continuellement de petites itérations d'infrastructure et d'architecture macro — vous aurez récolté de nombreux avantages au fil du temps.

Plus important encore, parce que vous concentrez chaque itération de l'architecture macro des microservices à partir d'une position de ce dont vous avez besoin à ce moment-là, vous aurez passé votre temps sur les composants les plus précieux de votre organisation.

Peut-être avez-vous commencé avec un pipeline CI/CD sain qui a pris en charge plus de 85 % de vos travaux de développement monolithique existants. Des dividendes ! Ensuite, vous standardisez vos déploiements dans des images Docker et fournissez des outils autour du lancement, de la migration et du retour en arrière des nouvelles versions. Des dividendes ! Ensuite, ajoutez une journalisation et une surveillance cohérentes, et vous commencez à visualiser et à rapporter sur les flux de messagerie à travers vos systèmes. Des dividendes ! Maintenant, alors que vous ajoutez de nouveaux services, vous réalisez que le couplage des services qui se parlent directement vous retient, et vous ajoutez un service de messagerie à votre infrastructure et commencez à déplacer certaines fonctionnalités vers des déclencheurs basés sur des événements. Des dividendes !

Je ne crois pas que vous deviez être Amazon ou Netflix pour récolter les avantages d'une architecture de microservices. Dans certains cas, vous pouvez utiliser les connaissances de comment ces architectures fonctionnent **à l'intérieur** d'un seul monolithe, et les dividendes peuvent être assez riches en effet.

Dès le départ, ou des années après que le monolithe commence à échouer sous son propre poids, vous pouvez utiliser les connaissances de comment séparer les services pour le renforcer et le rendre plus stable. Un monolithe qui est conçu en interne avec une bonne séparation entre les services fait une cible facile pour les microservices lorsque le succès exige plus de lui. (Sachez simplement qu'il faut des architectes pour maintenir l'intégrité d'un monolithe, et au-delà du début d'un système, il sera difficile d'atteindre une réussite à long terme.)

### L'Infrastructure de l'Architecture Macro

L'une de mes questions clés, lorsque j'ai commencé ce voyage, était de savoir comment je fournirais une infrastructure de base souhaitée aux développeurs de services au sein de mon organisation. Mes lectures m'ont conduit à comprendre trois méthodes principales :

1. Exécuter des systèmes qui fournissent les services ainsi que la documentation sur l'utilisation appropriée de ceux-ci. Un exemple ici est de fournir un système CI/CD et des directives sur la manière de configurer le pipeline de votre service. C'est peut-être le plus simple des deux, car nous sommes tous très habitués à avoir ce type d'infrastructure préparée gérée par une équipe d'exploitation.
2. Fournir du code que les développeurs peuvent intégrer dans leurs systèmes pour effectuer la fonctionnalité souhaitée. Un exemple ici serait une bibliothèque partagée qui peut être utilisée pour effectuer la localisation de service et l'équilibrage de charge. Cela restreint la capacité des équipes à choisir leur propre langage, mais l'avantage de ne pas créer cette infrastructure plusieurs fois peut compenser ce coût.
3. Si l'indépendance du langage est vraiment souhaitée pour vos services, les composants d'infrastructure peuvent être placés dans une implémentation sidecar qui s'exécute en tant que processus secondaire aux côtés de chaque service. Le sidecar représente alors le service et fournit l'accès à d'autres services dans l'infrastructure. Les sidecars semblent être plus répandus dans l'industrie que je ne l'avais d'abord pensé possible.

### Infrastructure Prête à l'Emploi Open Source

Il existe une pléthore d'options disponibles pour vous lancer avec une architecture macro de microservices. Vous seriez extrêmement négligent de ne pas considérer les options dans le cadre de vos premières conversations sur l'architecture macro. Certaines de ces pièces d'infrastructure existantes rendent le démarrage assez facile — soutenant davantage ma position selon laquelle tout le monde peut en bénéficier.

Certains des projets d'infrastructure prêts à l'emploi les plus cohérents sont appelés service meshes. Les service meshes fournissent un plan de contrôle (gestion en cluster des proxys de service mesh et autres macro services) et un plan de données (les services proxy à travers lesquels vos services communiquent). Ils fonctionnent généralement sous la forme d'un proxy sidecar qui fournit les fonctionnalités de mise en réseau des microservices dès la sortie de la boîte. L'utilisation de l'un de ceux-ci peut vous donner une longueur d'avance sur la majorité des fonctionnalités — et pour beaucoup de gens, ils peuvent être plus que ce dont vous aurez jamais besoin.

Ces projets sont tous relativement jeunes, et ils vont imposer des limitations à votre environnement que vous n'auriez peut-être pas choisies autrement. Cependant, ils sont conçus et développés par des personnes qui connaissent très bien les microservices, et vous pouvez à la fois utiliser leurs connaissances sur ce qui fonctionne et économiser beaucoup de temps en ne recréant pas les technologies vous-même.

En voici quelques-uns que j'ai trouvés et pour lesquels j'ai fait au moins une quantité modérée de recherche (ces descriptions sont basées sur une lecture de surface uniquement — voir les sites respectifs pour plus d'informations !).

#### [Netflix](https://netflix.github.io/)

Netflix est très présent sur la scène de l'architecture des microservices, et ils ont [open sourcé](https://netflix.github.io/) une grande partie de leurs services et bibliothèques de base d'exécution. Ils fonctionnent dans la JVM, et incluent [Eureka](https://github.com/Netflix/eureka) pour la découverte de services, [Archaius](https://github.com/Netflix/archaius) pour la configuration distribuée, [Ribbon](https://github.com/Netflix/ribbon) pour la communication inter-processus et inter-services résiliente et intelligente, [Hystrix](https://github.com/Netflix/hystrix) pour la tolérance de latence et de défauts à l'exécution, et [Prana](https://github.com/Netflix/prana) en tant que sidecar pour les services non basés sur la JVM.

Les pièces d'infrastructure fournies par Netflix peuvent être trop grandes pour une petite entreprise. Mais si vous travaillez déjà dans la JRE, ajouter le support pour Eureka, Ribbon et Hystrix peut rapidement vous apporter de nombreux avantages avec potentiellement de petits investissements.

#### [Spring Cloud](http://projects.spring.io/spring-cloud/)

Spring est depuis longtemps un endroit central pour les frameworks permettant un développement logiciel rapide et facile basé sur la JVM. Leur section spécialisée Spring Cloud inclut des intégrations avec de nombreuses infrastructures cloud, y compris les bibliothèques Netflix mentionnées ci-dessus parmi beaucoup d'autres. Si vous allez suivre la route JVM, il vaudra la peine de vous familiariser avec Spring Cloud.

#### [**Linkerd**](https://linkerd.io/) **(Service Mesh)**

Ce service mesh, écrit par Buoyant, a été publié dans le monde open source début 2016. Il s'exécute en tant que sidecar et agit comme un proxy entre vos services. Il vous fournit : l'équilibrage de charge, la rupture de circuit, la découverte de services, le routage dynamique des requêtes, l'intégration du proxy HTTP, les nouvelles tentatives et les délais, TLS, le proxy transparent, le traçage distribué et l'instrumentation. La prise en charge des protocoles inclut HTTP/1.x, HTTP/2, gRPC et tout ce qui est basé sur TCP.

Linkerd essaie de ne pas vous lier à une seule technologie — il prend en charge l'exécution locale, dans Docker, dans Kubernetes, dans DC/OS, dans Amazon ECS, et plus.

En tant qu'application sidecar, elle peut être exécutée une fois par service ou une fois par hôte — donc si vous exécutez plusieurs services par hôte, vous pouvez économiser sur la surcharge de processus avec Linkerd. Ils se vantent de quelques noms très connus sur leur liste d'utilisateurs.

Intéressamment, vous pouvez intégrer Linkerd avec Istio (couvert ci-dessous). Je ne suis pas clair sur les avantages de cela, mais une lecture de surface dit qu'il peut y avoir quelque chose là.

#### [**Conduit**](https://conduit.io/) (Service Mesh)

En décembre 2017, presque deux ans après Linkerd, Buoyant a publié un autre service mesh spécifiquement pour les clusters Kubernetes. Ils ont pris les leçons apprises et créent Conduit avec l'intention d'être un service mesh extrêmement léger.

L'outil Conduit fonctionne en tandem avec l'outil Kubernetes pour s'injecter dans votre cluster. Une fois injecté, la plupart du travail se fait en coulisses via le proxy et l'utilisation des schémas de nommage de services Kubernetes standard. Il revendique une bonne visibilité de bout en bout, mais je ne vois pas de bonnes captures d'écran de cela, et ne l'ai pas encore testé moi-même.

Une grande prudence ici est le statut Alpha et la création _extêmement_ nouvelle — février 2018. Ils ont publié une [Feuille de route vers la Production](http://v) avec un aperçu de là où ils vont. Pour l'instant, je le testerais et le garderais sur la liste « à surveiller ».

#### [**Istio**](https://istio.io) **(Service Mesh)**

Istio est un service mesh qui nous est parvenu en mai 2017. En interne, ils utilisent Envoy (couvert ensuite). Ils ont des instructions pour le déploiement sur Kubernetes, Nomad, Consul et Eureka.

En tant que sidecar, il fournit un équilibrage de charge automatique, une injection de fautes, un façonnage du trafic, des délais d'attente, une rupture de circuit, un miroir, et des contrôles d'accès pour le trafic HTTP, gRPC, WebSocket et TCP. Le trafic d'ingress et d'egress bénéficie du même ensemble de fonctionnalités. Des métriques, des journaux et des traces automatiques sont rapidement disponibles via des outils de visualisation inclus. Ils permettent également un routage de messages au niveau de l'infrastructure, à l'exécution, basé sur le contenu et les méta-informations de la requête.

L'inconvénient est qu'il est très jeune et restreint à des environnements de déploiement spécifiques — bien qu'il y ait une certaine documentation qui peut vous aider à déployer dans d'autres environnements en utilisant des méthodes manuelles.

Istio utilise iptables pour proxyfier de manière transparente les connexions réseau via le sidecar — dans le monde Kubernetes, cela est vraiment transparent pour vous, mais dans d'autres environnements, vous êtes impliqué dans la mise en place de cela. (Cela ressemble honnêtement à la plupart de ces services mesh utilisant les mécanismes de proxy transparent d'iptables pour accrocher leurs sidecars à vos applications.)

Du côté positif, l'ensemble des fonctionnalités de sécurité semble mature et bien pensé. Toutes les connexions egress sont, par défaut, refusées jusqu'à ce qu'elles soient explicitement autorisées — et c'est rafraîchissant ! Vous protégez vos services au sein de votre mesh de la même manière que vous les protégez à l'ingress et à l'egress — bien !

La visualisation hors de la boîte de vos services sous forme de diagramme de réseau et diverses métriques par service vous offre une observabilité immédiate de votre environnement. Les déploiements à grande échelle devront probablement s'approprier le déplacement de cela dans des déploiements plus importants, mais en tant qu'environnement de démarrage, c'est très bien.

#### [**Envoy**](https://www.envoyproxy.io/) **(Data Plane)**

À l'origine construit par Lyft, mais publié après Linkerd en 2016, celui-ci a l'air d'être le plus mature. Il se vante de _très grandes_ entreprises sur sa liste « Utilisé Par ». Il est écrit en C++ et est destiné à être exécuté en tant que sidecar comme les autres. Il a été construit pour prendre en charge l'exécution d'un seul service ou d'une seule application ainsi que pour prendre en charge une architecture de service mesh.

Cela dit, Envoy n'est pas un service mesh complet car il ne fournit que le plan de données et vous devez gérer les processus Envoy vous-même ou utiliser Istio (qui, par défaut, utilise le proxy Envoy).

Un rapide coup d'œil à la documentation montre une liste saine de fonctionnalités, y compris des filtres, la découverte de services, la vérification de l'état, l'équilibrage de charge, la rupture de circuit, la limitation du débit, TLS, les statistiques, le traçage, la journalisation, et bien plus encore. Les types de connexion pris en charge incluent HTTPS, TCP et Websockets.

Je suis impressionné par Envoy à première vue, et étant donné l'utilisation d'Envoy par Istio, je l'expérimenterai probablement via un essai d'Istio en premier (et ne regarderai Envoy seul que si je sens qu'Istio cache ou m'empêche d'utiliser pleinement quelque chose).

### Démarrage Rapide — L'Excitation est à son Comble !

Je suis extrêmement excité à l'idée de m'asseoir avec chacune de ces technologies existantes et de les essayer à fond. Avec la quantité de fonctionnalités qu'elles fournissent déjà, je serais gravement négligent de ne pas les comprendre et de les inclure comme base pour toute architecture macro de microservices que je supporte dans mon organisation.

Construire toutes ces fonctionnalités à partir de zéro, et ne pas tirer parti du excellent travail déjà accompli par tant d'individus brillants, serait un crime. Je préférerais que mon organisation passe son temps sur les services et fonctionnalités qui lui rapportent de l'argent — ou, si nous devons étendre davantage les fonctionnalités de l'infrastructure macro, passer ce temps à contribuer à l'un de ces projets.

L'utilisation de l'un de ces service meshes nous obligera à le comprendre extrêmement bien. Nous devons être capables de discerner les implications qu'il a sur notre architecture macro, et nous devons documenter celles-ci très soigneusement dans notre architecture macro. Oh oui, même si vous choisissez un service mesh, vous devez toujours écrire une architecture macro pour votre infrastructure de microservices. Ces service meshes ne vous fournissent qu'un immense coup de pouce, et, dans certains cas, répondent à certaines des questions pour vous.

### En Conclusion

Cela a été une période excitante pour moi de revenir à mes racines très techniques et de creuser plus profondément dans les concepts d'architecture moderne à travers les microservices. Je me réjouis de continuer ce voyage, et j'espère avoir des nouvelles de ceux d'entre vous qui l'ont fait et qui pourraient avoir des conseils pour moi que je n'avais pas pensé à inclure ici. Merci à tous pour votre attention, et j'espère que vous avez tiré quelque chose de cet article.

Je voudrais conclure par une liste des livres que j'ai récemment lus dans ma quête de connaissances, un que je suis en train de lire, et deux que je prévois de lire sur la base de recommandations dans d'autres livres et par de multiples experts en architecture logicielle.

#### [The Tao of Microservices](http://amzn.to/2pmifTF) par Richard Rodger

Une excellente introduction au monde des microservices avec un fort accent sur le large spectre des exigences nécessaires pour entrer dans ce monde.

Richard commence par des définitions pratiques et des orientations sur la manière de construire des microservices suivies d'un aperçu de ce qu'il faut pour exécuter des microservices.

Ce livre fournit une bonne compréhension des messages en tant que transport, de la correspondance de motifs pour le routage, et du grand effort que la surveillance et la mesure de votre environnement seront.

_Avertissement : L'auteur passe le premier tiers du livre à être plutôt dérogatoire envers toute approche de développement non-microservices. Lisez au-delà de cela et il a un bon livre._

#### [Microservices: Flexible Software Architecture](http://amzn.to/2HJGeTz) par Eberhard Wolff

Ce livre est divisé en sections logiques. Les deux premières donnent beaucoup d'informations de fond répétitives sur les microservices présentant ce qu'ils sont, ne sont pas, et quand vous devriez et ne devriez pas les utiliser.

Il y a un manque sévère de virgules dans le livre, ce qui parfois vous fait trébucher, mais le matériel est très bon. La partie 3 a transformé ce livre en un gagnant complet pour moi lorsqu'il a commencé à couvrir des morceaux d'informations très spécifiques.

#### Liste de Lecture et à Lire

Les livres suivants sont actuellement dans ma file d'attente de lecture sur la base de recommandations dans les livres précédents et également par des experts en architecture logicielle.

[Martin Fowler](https://martinfowler.com/articles/microservices.html) est l'un de ces experts qui a rapidement émergé dans mes recherches et lectures. Son site web est également une ressource inestimable.

* [Domain Driven Design](https://amzn.to/2pJgU9P) par Eric Evans — Je suis actuellement en train de lire celui-ci, car littéralement tout le monde (même [Object Thinking](https://amzn.to/2GelWBo)) le référence. La déférence qu'il reçoit dans la communauté des développeurs est semblable à celle de la Bible, et il partage une étiquette de prix similaire. Je suis à un tiers de sa lecture, et il solidifie définitivement et met des noms sur des pratiques que j'ai utilisées depuis un certain temps. Je me réjouis de passer plus de temps avec lui.
* [Building Microservices: Designing Fine-Grained Systems](https://amzn.to/2IU6Qmm) par Sam Newman. Martin Fowler en parle très hautement. Il prétend « fournir de nombreux exemples et conseils pratiques ». Je comprends beaucoup des principes, et maintenant je veux voir plus d'exemples pratiques pour affiner et ancrer davantage ceux-ci.
* [Production Ready Microservices](https://amzn.to/2IXBICD) par Susan J. Fowler. Je crois que Susan va approfondir ce concept d'une architecture macro pour les microservices. Dans cet article, j'ai tenté de faire brièvement ce que j'espère qu'elle fera en beaucoup plus de détails.

#### Comment je suis arrivé ici

Comme je l'ai dit en introduction, je suis en mission depuis quelques mois. Si vous êtes intéressé à voir la progression de mon voyage et peut-être obtenir plus d'informations sur certains de ces sujets, veuillez parcourir mes précédents articles d'investigation :

* [Microservices: A Journey of Understanding](https://codeburst.io/microservices-architecture-e6907b97a42a)
* [Microservices: Early Thoughts Before That First Step](https://codeburst.io/microservices-architecture-early-thoughts-before-that-first-step-fecc2ef9d64)
* [Microservices Architecture: It Takes A Platform — Eureka!](https://codeburst.io/microservices-architecture-it-takes-a-platform-eureka-97f61af90d5c)
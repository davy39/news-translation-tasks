---
title: Comment fonctionnent les plateformes de calcul modernes
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-02-07T20:22:32.000Z'
originalURL: https://freecodecamp.org/news/modern-compute-platforms
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-panumas-nikhomkhai-1148820--1-.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
- name: servers
  slug: servers
seo_title: Comment fonctionnent les plateformes de calcul modernes
seo_desc: "The way things sit now, if you were somehow allergic to computers, you'd\
  \ be hard pressed to really banish them from your life, no matter where you found\
  \ yourself. \nTaking a quiet walk in the woods? What about the smartphone in your\
  \ pocket. Left the p..."
---

À l'heure actuelle, si vous étiez d'une manière ou d'une autre allergique aux ordinateurs, vous auriez du mal à les bannir complètement de votre vie, peu importe où vous vous trouvez. 

Faire une promenade tranquille dans les bois ? Et ce smartphone dans votre poche ? Laissé le téléphone dans la voiture ? Voyez-vous cette tour de téléphone cellulaire juste derrière ces arbres ? Les chances sont bonnes que la tour soit plus qu'une simple antenne. Elle pourrait également héberger un serveur de calcul en périphérie. Et ne pensez pas qu'il n'y avait pas d'ordinateurs intégrés dans les mécanismes sous le capot de la voiture (ou du bus) qui vous a conduit ici.

Allergies mises à part, si vous voulez vraiment comprendre l'état actuel du monde du calcul, il sera utile de comprendre tous les endroits où les ordinateurs peuvent apparaître et à quoi ils pourraient ressembler. 

Dans cet article, nous allons énumérer les classes dans lesquelles les dispositifs de calcul modernes peuvent être classés, et décrire leurs forces, faiblesses et potentiel.

Ce chapitre est tiré du livre, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). Si vous préférez regarder ce chapitre sous forme de vidéo, n'hésitez pas à suivre ici :

%[https://www.youtube.com/watch?v=0IW2GCTkCjI]

# Qu'est-ce qu'un serveur ?

Honêtement, j'avais travaillé comme administrateur système professionnel depuis un certain temps avant de pouvoir répondre correctement à cette question. 

La vérité est que chaque serveur est un ordinateur, et tout ordinateur peut être un serveur. Le terme _serveur_ implique simplement que le dispositif fournit un certain _service_ à au moins un dispositif externe (connu sous le nom de _client_).

Si l'imprimante qui est branchée à votre ordinateur de bureau peut être partagée par les autres ordinateurs de votre réseau local, alors votre ordinateur de bureau est un serveur (un _serveur d'impression_, pour être précis). 

Le routeur WiFi fourni par votre fournisseur de services Internet est, par toutes les définitions, un _serveur réseau_ - car il _fournit_ l'accès au réseau à ses clients. 

Et le petit dispositif Raspberry Pi Zero à 5 $, qui alimente votre caméra de surveillance maison, est un _serveur vidéo_ - bien que cela ne fonctionnera pas sans attacher un module de caméra à 7 $.

Mais ce n'est pas ce que la plupart des gens ont en tête lorsqu'ils utilisent ce terme. La première fois que je suis entré dans la salle des serveurs d'une entreprise de taille moyenne, j'ai été frappé par le son de dizaines de ventilateurs de châssis puissants et la chaleur des CPU travaillant dur et des disques durs tournant rapidement. Instantanément, j'ai su comment les gens utilisent normalement ce mot. 

J'ai également découvert que la chaleur était un problème : les administrateurs avaient du mal à maintenir leur salle des serveurs correctement refroidie et, avec le temps, ils finiraient par devoir amortir du matériel coûteux en raison de pannes liées à la chaleur.

Donc, par "serveur", nous entendons généralement des ordinateurs installés dans ces boîtiers empilables montés en rack, conçus pour loger et protéger efficacement des composants hautement performants, coûteux et délicats. 

Les racks de serveurs vivent généralement dans des pièces bien ventilées et refroidies avec un accès facile à une alimentation électrique abondante. Vous devrez peut-être les chercher, mais ces pièces contiendront également des faisceaux de câbles colorés, reliant les serveurs aux réseaux.

En règle générale, les serveurs n'auront généralement pas d'écrans ni même de claviers branchés, car ils sont susceptibles d'être gérés à distance ou, encore plus probablement, entièrement automatisés et ne nécessitant aucune administration du tout. 

Les fermes de serveurs appartenant à des fournisseurs de cloud géants comme Amazon Web Services auront des milliers d'ordinateurs de commodité fonctionnant dans des allées de vastes entrepôts. Lorsqu'un serveur tombe en panne, un panneau de surveillance quelque part s'allume et un technicien est finalement envoyé pour retirer le serveur, le jeter et glisser un remplacement dans le rack nouvellement disponible.

Aucune larme n'est versée lorsque nous disons au revoir au matériel ancien, dévoué et travailleur dans ces endroits.

# Qu'est-ce que Linux ?

En parlant de serveurs, ai-je mentionné qu'ils ont tous besoin d'un système d'exploitation installé ? 

Et ai-je mentionné en outre que la grande majorité des serveurs alimentant la grande majorité des opérations qui rendent Internet et toutes ses fonctionnalités possibles fonctionnent sous le système d'exploitation Linux ? Oh, et saviez-vous que le système d'exploitation open source Linux est disponible gratuitement ?

Je n'ai pas mentionné tout cela ? Mon erreur.

Eh bien, les serveurs ont besoin de systèmes d'exploitation. La plupart des serveurs (bien plus de 90 pour cent des instances de machines virtuelles fonctionnant sur Amazon AWS EC2, par exemple) fonctionnent sous Linux. Et Linux est, en effet, librement disponible pour toute utilisation sur tout serveur, ordinateur portable, ordinateur de bureau, routeur, système embarqué ou supercalculateur. 

En fait, chacun des 100 premiers supercalculateurs du monde utilise Linux. Et le système d'exploitation Android pour smartphones ? Oui. C'est aussi Linux.

Strictement parlant, "Linux" est le noyau logiciel qui permet à un utilisateur d'ordinateur de prendre le contrôle des éléments matériels physiques d'un ordinateur. Le noyau traduit vos frappes de clavier dans un format qui sera compris par les pilotes contrôlant vos disques de stockage, mémoire, interfaces réseau, écrans et - en fait - clavier et souris. 

De nombreux milliers de programmes logiciels supplémentaires sont étroitement associés à Linux, mais ils font en réalité partie de l'espace utilisateur qui "survole" le noyau Linux.

Cela dit, Linux, y compris son écosystème logiciel plus large, domine actuellement le marché du calcul serveur. Le fait que vous puissiez installer et lancer gratuitement autant d'instances physiques ou virtuelles que vous le souhaitez rend Linux très attractif, surtout dans le monde de l'orchestration de charges de travail scriptées. 

Les instances Linux virtualisées seront souvent mises en vie et, après avoir terminé une tâche qui prend même quelques secondes, éteintes à nouveau. 

La polyvalence et la flexibilité que Linux apporte au calcul ont été l'étincelle de certaines innovations et créativités profondément impressionnantes.

Une partie de la polyvalence de Linux est le fait que vous pouvez choisir parmi des centaines de variations (connues sous le nom de _distributions_). 

Cherchez-vous à exécuter des serveurs pris en charge par l'entreprise ? Des dispositifs de l'Internet des objets (IoT) ? Des machines de test de sécurité ? De la gestion multimédia ? De la production vidéo ou audio ? Tout ce qui précède ? Aucun de ce qui précède ? Il y a certainement une distribution qui vous correspond bien. 

Et si les spécifications exactes dont vous avez besoin ne peuvent pas être trouvées, n'hésitez pas à réécrire le noyau lui-même et à créer votre propre distribution.

Divulgation complète : Je connais une ou deux choses sur Linux, étant l'auteur de Linux in Action (Manning), coauteur de Ubuntu Bible (Wiley), et l'auteur du parcours d'apprentissage Linux Fundamentals chez Pluralsight.

Divulgation plus complète : J'écris ceci sur une station de travail Ubuntu Linux à la maison, où tous nos nombreux dispositifs sont alimentés par Linux depuis plus d'une décennie.

# Qu'est-ce que la virtualisation ?

Nous avons déjà discuté de la virtualisation en profondeur dans le cadre du chapitre 3 (Comprendre le Cloud), nous allons donc simplement couvrir ici quelques bases conceptuelles globales.

Dans le temps, vous aviez une idée pour un nouveau projet de calcul et vous soumettiez une proposition avec vos gestionnaires demandant de l'argent. Lorsque le projet était approuvé, vous estimiez vos besoins, sollicitiez des offres de fournisseurs de matériel, commandiez un nouveau serveur et, lorsqu'il arrivait enfin, vous le chargiez avec votre logiciel d'application. Ensuite, vous le lanciez et laissiez le monde voir ce que vous aviez fait. 

C'est ainsi que les choses fonctionnaient généralement : Un projet. Un serveur. Beaucoup de temps d'attente.

Mais que se passe-t-il si vous avez surestimé vos besoins de calcul de 50 pour cent ? Cela représenterait quelques milliers de dollars perdus. Et si un projet important mais léger n'avait pas vraiment besoin d'un serveur autonome complet, vous deviez souvent l'acheter quand même. 

Et si le projet devait fonctionner pendant seulement quelques mois ? Dépensez l'argent et espérez trouver une nouvelle utilisation pour la chose une fois votre projet initial terminé.

Gênant. Des montagnes de gêne.

La virtualisation est un (principalement) tour de logiciel qui vous permet de tromper plusieurs systèmes d'exploitation installés en leur faisant croire qu'ils sont seuls sur un ordinateur physique alors qu'ils le partagent en réalité avec d'autres systèmes d'exploitation. Vous pouvez provisionner et exécuter un seul hôte de virtualisation d'un type ou d'un autre et le remplir avec un ou une centaine de serveurs virtuels.

L'un de ces serveurs pourrait avoir besoin de beaucoup de mémoire système mais seulement d'un Go ou deux d'espace de stockage. Un autre pourrait être lourd en tâches de conversion vidéo et de stockage mais n'est nécessaire que pendant une demi-heure par jour. Un troisième pourrait être un système de surveillance 24/7 qui a juste besoin d'un endroit calme pour faire son travail sans que personne ne le dérange. 

Tant que vous ne poussez pas l'hôte physique au-delà de ses limites de ressources globales, les machines virtuelles peuvent toutes coexister heureusement ensemble. Et lorsqu'un service n'est plus nécessaire, vous pouvez réaffecter ses ressources libérées à autre chose.

Les montées en puissance et les réductions d'un cycle de vie typique d'un serveur virtuel sont rapides. Pour toutes les intentions et tous les buts, ils se lanceront et s'éteindront généralement instantanément. 

Cela est possible parce que le matériel sous-jacent fonctionne toujours - et parce que l'image du système d'exploitation est petite et, généralement, optimisée pour les environnements virtuels.

Comme [nous l'avons vu dans le chapitre 3](https://www.freecodecamp.org/news/what-is-cloud-computing-beginners-guide/), les services hébergés dans le cloud sont tous virtualisés. À mesure que de plus en plus d'infrastructures informatiques migrent vers le cloud, de plus en plus de vos activités en ligne seront alimentées par des machines virtuelles. 

Vous ne remarquerez pas la différence, mais chaque fois que vous recherchez sur Internet ou vous authentifiez à un compte en ligne, il y a de fortes chances que ce soit un conteneur ou une machine virtuelle à laquelle vous vous connectez, et non directement à une machine physique.

# Terminologie du Cloud Computing

Comme la virtualisation, nous avons également parlé du cloud dans le chapitre 3. Nous avons mentionné comment le marché du cloud public était dominé par AWS et, dans une moindre mesure, par Azure de Microsoft. 

Je vais juste prendre une minute ou deux ici pour ajouter un guide rapide à travers certains des pires jargons de l'industrie du cloud.

Les environnements **Infrastructure as a Service (IaaS)** vous donnent un accès complet aux instances de serveurs virtuels. Le fournisseur s'assurera que le matériel sous-jacent, les éléments de réseau et de sécurité sont en place et fonctionnent, tandis qu'il est de votre responsabilité de gérer le système d'exploitation et les autres logiciels fonctionnant sur votre instance. 

Les principaux acteurs de l'IaaS incluent Amazon Elastic Compute Cloud (EC2) et Azure Compute.

Les environnements **Platform as a Service (PaaS)** masquent la plupart ou la totalité des tâches d'administration de l'infrastructure, vous laissant avec une interface où vous pouvez exécuter vos propres données ou code. 

Un bon exemple est AWS Elastic Beanstalk, qui vous permet de télécharger votre code d'application à partir duquel il sera automatiquement déployé sur le cloud d'Amazon. D'autres fournisseurs dans cet espace incluent Heroku et Salesforce Lightning Platform.

Les environnements **Software as a Service (SaaS)** n'exposent qu'une interface utilisateur finale, gérant toutes les couches de l'infrastructure d'administration de manière invisible. 

Microsoft Office 365 et Google G Suite sont des outils de productivité bureautique SaaS largement utilisés. 

Mais il existe un marché croissant d'outils SaaS fournissant des équivalents logiciels en ligne à de nombreuses applications qui, dans les années passées, ne pouvaient être utilisées que sur des postes de travail autonomes. Ces applications incluent la comptabilité, la conception assistée par ordinateur (CAO) et les solutions de conception graphique.

La **tarification basée sur la consommation** ou, comme on l'appelle parfois, la facturation à l'usage, est un pilier du concept de cloud. L'idée est que vous n'avez pas à parier en investissant à l'avance dans l'infrastructure, mais vous pouvez payer des montants incrémentiels pour des unités de services de calcul à mesure que vous les utilisez. 

Cela ne revient pas toujours moins cher à long terme. Mais le paiement à l'usage facilite définitivement le test des piles d'applications et l'expérimentation de plusieurs configurations alternatives avant de se lancer dans un déploiement complet. 

Cela signifie également que - en supposant que vous ne fassiez pas d'erreurs de configuration stupides - il est presque impossible de sur-provisionner gravement.

**À la demande** est également parfois appelé auto-service. La capacité de demander une livraison instantanée de ressources de calcul à tout moment de la journée/semaine/année vous donne un contrôle complet sur les cycles de vie des applications de votre organisation. Vous n'êtes jamais à la merci des horaires et des limitations des autres.

Les **Accords de Niveau de Service (SLA)** sont des divulgations légales publiées par les entreprises dans le domaine de la fourniture de services. 

Même si le standard de fiabilité des ressources fourni par les principales plateformes de cloud public est généralement excellent, des accidents se produisent. Lorsque vous payez des frais horaires ou mensuels pour des services cloud, le SLA de l'entreprise vous indique que vous devez anticiper un temps d'arrêt d'un certain nombre de minutes ou d'heures chaque mois. 

Par exemple, le SLA d'Amazon fixe son taux de disponibilité EC2 à 99,99 % chaque mois. Si, dans un mois particulier, vous rencontrez un temps d'arrêt plus important, vous pourriez être éligible à des crédits de service ou à des remboursements.

Le **multilocataire** est le placement d'instances virtuelles appartenant à plusieurs comptes clients cloud sur une seule ressource matérielle. 

Une configuration multilocataire pour une instance de serveur sera probablement significativement moins chère qu'une instance dédiée. Choisir une instance dédiée, cependant, garantirait que votre instance ne sera jamais hébergée sur un serveur physique aux côtés d'une instance d'un second compte. Des considérations de sécurité ou réglementaires pourraient vous obliger à éviter le multilocataire.

La **migration** décrit le processus impliqué dans le déplacement des charges de travail existantes des applications et bases de données commerciales des déploiements locaux (sur site) vers un fournisseur de cloud. Les fournisseurs mettent souvent à disposition des outils spécialisés et un support technique gratuit pour les migrations.

L'**élasticité** décrit les moyens par lesquels les ressources cloud virtualisées peuvent être rapidement ajoutées pour répondre à une demande croissante ou, tout aussi rapidement, réduites en réponse à une baisse de la demande. 

Les ressources élastiques sont particulièrement bien adaptées au maintien de la disponibilité et de la santé des applications sans encourir de coûts inutiles. L'élasticité peut généralement être automatisée, de sorte que les applications répondront instantanément aux environnements changeants sans nécessiter d'intervention manuelle.

# Qu'est-ce que le calcul "sans serveur" ?

Le calcul sans serveur n'est pas différent du calcul serveur. C'est juste que, même si vous plissez les yeux très fort, vous ne voyez pas le serveur. 

Ou, pour le dire autrement, le calcul sans serveur est comme l'exécution d'une instance de serveur virtuel, mais sans avoir à configurer ses paramètres d'instance ou à se connecter pour tout configurer.

En d'autres termes, vous ne pouvez pas exécuter de code logiciel de quelque nature que ce soit sans qu'un ordinateur quelque part ne traite vos commandes. Disons donc que le sans serveur est une forme de virtualisation où tout, sauf votre code d'application, est abstrait. 

En ce sens, les plateformes sans serveur comme Lambda d'Amazon et Functions d'Azure ressemblent beaucoup au modèle utilisé par Amazon Elastic Beanstalk. Mais elles sont si simples à utiliser qu'elles peuvent facilement être incorporées dans une charge de travail multi-niveaux plus large et hautement automatisée.

# Qu'est-ce que l'informatique en périphérie ?

La latence est le terme que nous utilisons pour décrire le temps qu'il faut pour que les données voyagent d'un serveur distant à travers un réseau jusqu'à votre ordinateur - ou dans l'autre sens. En supposant que vous préférez un service rapide à un service lent (ce qui semble une supposition sûre), des chiffres de latence élevés sont une mauvaise chose.

Les ingénieurs réseau peuvent invoquer divers sorts magiques - Oups ! Je veux dire des efficacités de configuration astucieuses - pour réduire les retards dus à la latence. 

Mais peu importe le nombre de tours qu'ils cachent dans leurs mystérieux sacs noirs, ils ne peuvent pas ignorer les lois de la physique. Même en utilisant les meilleures connexions et profils de configuration, les données doivent encore se déplacer physiquement sur les distances entre les emplacements distants.

La seule façon de réduire ce type de latence est de raccourcir la distance. Je suppose qu'une façon serait que les fournisseurs de services en ligne demandent très poliment à leurs clients de vendre leurs maisons et de déménager quelque part plus près des serveurs fonctionnant dans le bureau (comme si les prix de l'immobilier n'étaient pas déjà assez élevés dans la Silicon Valley). 

Alternativement, que diriez-vous de rapprocher le serveur du client ?

Ah. Vous avez découvert l'informatique en périphérie : l'art de installer de grands réseaux distribués de serveurs plus petits où des copies miroir des données du serveur peuvent être stockées et, lorsque nécessaire, fournies à tout client de la région qui initie des demandes. 

Si vous avez suffisamment de ces serveurs répartis uniformément dans les régions géographiques où vivent vos clients, alors vous pouvez réduire significativement la latence qu'ils subissent.

Un type d'informatique en périphérie qui remplit cette fonction est connu sous le nom de réseau de distribution de contenu (CDN). Cloudflare et CloudFront d'Amazon sont parmi les plus grands CDN actuellement en opération.

Les ressources d'informatique en périphérie comme celles utilisées par les CDN ont également été de plus en plus utilisées pour gérer de grands flux de données vers et depuis des dispositifs IoT comme les ordinateurs intégrés dans les voitures. Placer des dispositifs de calcul capables aux extrémités de grands réseaux permet de consommer et de transformer de tels ensembles de données plus rapidement qu'en déplaçant les données jusqu'au cloud plus distant.

# Quels sont les principaux facteurs de forme des ordinateurs ?

Les ordinateurs, comme les egos, viennent dans toutes les formes et tailles. Souhaitez-vous transporter un rack rempli de serveurs bare metal dans votre poche pour payer vos achats ? Vous feriez probablement mieux d'utiliser une sorte d'application de paiement mobile sur votre smartphone.

La taille compte. Beaucoup. Le facteur de forme d'un dispositif déterminera les dimensions et la capacité de ses composants internes. Cela signifie que la carte mère particulière, les modules de mémoire, les disques de stockage, les ports périphériques et l'alimentation que vous sélectionnez pour un dispositif seront limités par votre facteur de forme global.

Le facteur de forme que vous choisissez - pour un nouveau projet ou simplement pour votre usage personnel - sera généralement évident (les racks de serveurs peuvent être lourds et ne supportent pas bien les voyages). Mais savoir ce qui est disponible peut faciliter la planification.

## Dispositifs utilisant des écrans vidéo

Le terme _ordinateur personnel_ (PC), de nos jours, est utilisé pour décrire les ordinateurs de bureau ou portables. 

Les ordinateurs portables, conçus pour être mobiles, sont largement autonomes. Les ordinateurs de bureau, en revanche, viennent généralement avec les éléments de calcul de base dans une boîte qui inclut des ports externes pour connecter des périphériques comme les claviers et les moniteurs. 

Bien que vous puissiez trouver des ordinateurs avec une puissance et une fonctionnalité comparables à celles des PC dans des boîtiers très petits (de la taille d'une carte de crédit), les boîtiers plus grands utilisés par les ordinateurs de bureau permettent une personnalisation et des mises à niveau plus faciles.

Les consoles de jeu - comme la PlayStation de Sony, la Xbox de Microsoft et la Nintendo Switch - sont effectivement l'équivalent des ordinateurs de bureau, sauf que leur logiciel est construit sur des systèmes fermés. 

Elles sont "fermées" dans le sens où leur interface logicielle n'expose que la fonctionnalité que le fabricant veut que vous voyiez. Modifier ou personnaliser le système d'exploitation ou les mécanismes internes d'une console de jeu est normalement impossible.

Un dispositif à écran tactile utilise les gestes et les tapotements qu'il détecte des utilisateurs comme dispositifs d'entrée à la place de la souris ou du clavier traditionnel. Les technologies d'écran tactile sont la principale inspiration derrière les facteurs de forme plus petits pour les consommateurs, puisqu'il n'y a pas besoin de dispositifs d'entrée externes. 

Cela, plus que toute autre chose, a alimenté la croissance énorme du marché des tablettes et des smartphones. (Cela explique également les pouces agiles de manière presque surnaturelle de toute une génération de jeunes.)

## Dispositifs sans écran vidéo

Le routeur qui connecte les dispositifs à un réseau via WiFi ou des câbles Ethernet contient à peu près la même carte mère interne et les mêmes interfaces réseau que vous trouveriez dans tout autre dispositif de calcul. 

La grande différence est qu'il n'y a pas de port vidéo HDMI, DVI ou VGA. Les routeurs sont conçus pour fonctionner de manière autonome et, lorsque l'administration est nécessaire, elle se fera généralement via une interface de navigateur à travers un réseau.

Vous lancez une session d'administration avec votre routeur en entrant son adresse IP dans votre navigateur et en vous authentifiant lorsque vous y êtes invité. Dans certains cas, vous pouvez également lancer des sessions de terminal via le protocole Secure Shell (SSH).

Ce modèle d'administration à distance est partagé par de nombreux types de dispositifs sans écran. Ceux-ci incluront les implants médicaux (et non médicaux) ou les _wearables_ qui sont équipés de minuscules ordinateurs conçus pour surveiller, rapporter ou même interagir avec leurs environnements hôtes. 

(Dans le contexte des wearables, je devrais au moins brièvement discuter des montres intelligentes ici, mais, pour la vie de moi, je ne comprends pas pourquoi quelqu'un en voudrait une.)

Les ordinateurs sans écran sont également intégrés dans les dispositifs médicaux, les appareils électroménagers, les voitures, les flottes logistiques et les machines industrielles. Tous ces ordinateurs intégrés sont des composants de l'Internet des objets en croissance.

Merci d'avoir lu !

_Les vidéos YouTube des dix chapitres de ce livre [sont disponibles ici](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Beaucoup plus de bonnes choses technologiques - sous forme de livres, de cours et d'articles - [peuvent être trouvées ici](https://bootstrap-it.com). Et envisagez de suivre mes [cours sur AWS, la sécurité et la technologie des conteneurs ici](https://www.udemy.com/user/david-clinton-12/).
---
title: Connectivité numérique – Comment nous nous connectons à Internet et explication
  de l'IoT
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-01-24T17:08:41.000Z'
originalURL: https://freecodecamp.org/news/digital-connectivity-internet-and-iot-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-andrea-piacquadio-935743.jpg
tags:
- name: internet
  slug: internet
- name: Internet of Things
  slug: internet-of-things
seo_title: Connectivité numérique – Comment nous nous connectons à Internet et explication
  de l'IoT
seo_desc: "Telephones changed the way we all talked to each other and went about our\
  \ work (well, the way our great-grandparents did, at any rate). Information could\
  \ now be communicated instantly, rather than being sent over slow, overland routes.\
  \ \nBut that's ha..."
---

Les téléphones ont changé la façon dont nous parlions tous et dont nous travaillions (enfin, la façon dont nos arrière-grands-parents le faisaient, en tout cas). Les informations pouvaient désormais être communiquées instantanément, plutôt que d'être envoyées par des routes terrestres lentes. 

Mais cela n'est guère une nouvelle pour qui que ce soit de nos jours. Le réseau moderne – mieux connu à travers son itération internet – a de même stimulé la communication, bien que cette fois-ci, c'était le mouvement des données plutôt que la voix qui a été boosté.

Dans les cinquante années ou plus depuis la naissance de l'internet, il a été chargé du mouvement, du stockage et de la gestion de plus en plus de nos données. 

Ces changements ont apporté des opportunités, des risques et des pressions considérables. Se connecter est désormais une nécessité de base. La gestion de tous nos nombreux appareils connectés et l'utilisation des moyens d'authentification pour étendre nos identités présentent également des défis. Nous discuterons de tout cela ici.

Cet article a été tiré du livre, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). Si vous préférez regarder ce chapitre sous forme de vidéo, n'hésitez pas à suivre ici :

%[https://www.youtube.com/watch?v=FnTCMZFe2ww]

# Comment nous nous connectons à Internet

De nos jours, après la nourriture et le logement, la ressource la plus basique de toutes est probablement la connectivité internet. Si vous ne pouvez pas accéder à internet, vous aurez du mal à faire vos opérations bancaires, à vous éduquer, à réserver des arrangements de voyage, ou même à déterminer exactement où vous vous trouvez. 

Ce n'est pas pour rien que l'accès à internet, généralisé, fiable et relativement rapide, est crucial pour le développement économique général d'une région.

Bien que l'internet ait été initialement conçu comme un réseau décentralisé et distribué de ressources, vous devez toujours établir une sorte de connexion pour y accéder. 

Les meilleures connexions sont gérées par des opérateurs de réseau, connus sous le nom de réseaux de niveau 1. Ces réseaux peuvent atteindre tous les autres réseaux grâce à un accord de peering qui ne nécessite pas de paiement pour le transit IP. Vous pouvez considérer ces réseaux comme l'épine dorsale de l'internet, et leur infrastructure réseau en est la structure.

Des exemples d'entreprises gérant des réseaux de niveau 1 incluent AT&T et Verizon aux États-Unis, Tata Communications (Inde) et Deutsche Telekom (Allemagne). Ces opérateurs revendront de la bande passante à des fournisseurs de services internet (FAI) plus petits qui, à leur tour, vendront l'accès à des utilisateurs finaux comme vous et moi.

## Options de haut débit

Les particuliers recherchant un accès haut débit dans leurs foyers ou petites entreprises peuvent généralement choisir entre l'un des quatre modèles d'accès suivants :

* **Câble**. Puisqu'ils sont déjà dans le secteur de la fourniture de données à des millions de foyers via des connexions physiques existantes, les fournisseurs de télévision par câble peuvent facilement transmettre internet via les mêmes fils.
* **Ligne d'abonné numérique (DSL)**. Une famille de technologies qui permettent des données numériques sur des lignes téléphoniques en cuivre, le DSL peut fournir un niveau de service similaire à celui du câble, mais sans nécessiter un abonnement câble sous-jacent. En fait, en utilisant une connexion "cuivre sec", vous n'avez même pas besoin d'un compte de ligne téléphonique fixe.
* **Fibre optique**. En raison de certains détails techniques arcanes (y compris les lois de la physique), la transmission de signaux numériques sous forme de lumière infrarouge peut se faire plus rapidement et nécessiter moins de répéteurs que les câbles électriques comparables. Une connexion internet par fibre optique pourrait typiquement offrir des vitesses de transfert de 10-40 Gbit/s – mille fois plus rapides que les taux actuellement standard utilisant le câble ou le DSL.
* **Satellite**. Poser de nouveaux câbles dans des villes densément peuplées est coûteux, mais les entreprises peuvent rapidement rentabiliser leur investissement grâce aux nombreux contrats d'accès qu'elles signeront. Mais les régions rurales peu peuplées sont beaucoup plus difficiles à desservir. En partie pour combler le fossé de connectivité rurale, un certain nombre d'entreprises travaillent ambitieusement à lancer des constellations de milliers de satellites en orbite pour fournir une couverture internet universelle. À l'heure où nous écrivons ces lignes, SpaceX est la plus avancée avec son projet, ayant déjà lancé avec succès plus de 500 satellites dans le cadre du système Starlink.

Outre ces technologies dominantes, il y a eu plus d'une tentative de solutions de connectivité alternatives. Certaines sont expérimentales mais prometteuses, et d'autres sont un peu plus spéculatives. 

L'Internet par ballon de Google (officiellement connu sous le nom de Loon LLC) est une tentative de faire flotter des flottes de ballons à haute altitude fournissant un signal de 1 Mbps à toute personne à portée sur le sol. 

Loon est conçu pour fournir un haut débit bas de gamme dans des régions difficiles d'accès où un service fiable a été difficile ou même impossible. En 2020, le projet semble être en phase expérimentale avancée.

Le haut débit sur ligne électrique (BPL) peut tirer parti de tout le réseau électrique qui relie les autorités électriques aux foyers et aux entreprises pour fournir des données internet. En fin de compte, la technologie offre une bande passante limitée car le bruit de ligne provoque une perte significative du signal de données. 

Les lignes électriques transportant des données peuvent également causer des interférences avec les communications radio à haute fréquence. En fin de compte, la qualité relativement faible du signal et la forte concurrence d'autres technologies signifient que le BPL ne sera probablement jamais largement adopté.

Les réseaux utilisant des formes de fournisseur de services internet sans fil (WISP) peuvent desservir des foyers et des bureaux sur de plus grandes zones géographiques sans avoir besoin de câbler physiquement chaque bâtiment. Des connexions filaires sont installées au centre d'une zone et, si nécessaire, des backhauls connectés sont installés dans des zones surélevées pour renforcer les signaux sans fil destinés aux consommateurs. 

Les tours radio existantes ou d'autres structures hautes peuvent être utilisées pour les répéteurs de backhaul, rendant un système WISP relativement peu coûteux à installer.

Des coopératives de réseaux sans fil à plus petite échelle peuvent être partagées localement en utilisant un fournisseur de services internet de quartier (NISP) (utilisant des antennes sur les toits) ou un réseau maillé sans fil (où les appareils connectés au réseau agissent comme des nœuds pairs) pour partager efficacement une seule connexion physique.

Ces systèmes sont principalement conçus pour nous servir là où nous vivons et travaillons. Mais l'accès aux données mobiles est définitivement aussi une réalité. Je suis sûr que vous êtes déjà familiarisé avec les forfaits de données que les compagnies de téléphonie mobile peuvent fournir en plus de leurs services d'appel et de messagerie.

## Accès aux données mobiles

La connectivité cellulaire est distribuée à travers des zones géographiques (appelées "cellules") à partir de transmetteurs radio individuels répartis dans la cellule. 

Puisque les transmetteurs dans chaque cellule utiliseront des fréquences radio différentes de celles des cellules environnantes, les technologies sans fil modernes permettent un "transfert" automatique et transparent lorsque l'utilisateur se déplace entre les cellules.

Les technologies utilisées pour la téléphonie sans fil ont changé depuis les années 80, lorsque ce qui est maintenant connu sous le nom de 1G ("Première Génération") des téléphones cellulaires a été introduit. Pour décrire l'évolution des téléphones cellulaires en termes très généraux, nous pourrions dire que :

* Les téléphones **1G** ne transportaient que des communications vocales et avaient une vitesse de transfert maximale de 2,4 Kbps.
* Les téléphones **2G** pouvaient transporter des messages de service de messages courts (SMS) et de service de messagerie multimédia (MMS), qui pouvaient inclure des vidéos courtes et des images.
* Les téléphones **3G** avaient des taux de transfert beaucoup plus élevés (jusqu'à 2 Mbps) que toute variante de 2G et étaient donc appelés "haut débit mobile".
* Les téléphones **4G** pouvaient atteindre des vitesses allant jusqu'à 100 Mbps, ce qui permettait la télévision mobile HD, les jeux en ligne et la vidéoconférence.
* Les téléphones **5G** – lorsqu'ils sont utilisés sur des réseaux compatibles – devraient atteindre des vitesses de transfert allant jusqu'à 20 Gbps avec une très faible latence, permettant des environnements virtuels entièrement immersifs. Si le déploiement de la 5G est réussi (et, au moment de l'écriture, cela n'est pas encore clair), la portée et les limites des nouvelles catégories de services qui pourraient être déployées ne sont pas encore connues.

En ce qui concerne la planification d'une nouvelle entreprise, il est depuis longtemps admis que rien ne remplace une solide recherche de marché. Sans savoir qui seront vos clients, où ils vivent et ce qu'ils aiment, comment pouvez-vous les servir correctement ? 

Eh bien, vous pouvez maintenant ajouter à cette liste "à quel point leur connectivité internet est-elle fiable et robuste", car sans accès numérique, ils ne vous trouveront peut-être jamais ou ne pourront pas consommer votre service.

# Parler à l'Internet des Objets

Deux changements récents sont, plus que tout autre chose, responsables de l'écosystème de l'Internet des Objets (IoT) : la disponibilité de ordinateurs embarqués bon marché et à carte unique (comme le Raspberry Pi) et une connectivité internet bon marché et toujours active.

Ces minuscules cartes uniques – souvent plus petites qu'une carte de crédit – sont faciles à incorporer dans à peu près tout ce que vous prévoyez de fabriquer. 

De tels appareils coûtent très peu – parfois seulement quelques dollars pièce – et ils sont généralement conçus pour exécuter des distributions Linux complètes et gratuites. Et la disponibilité du réseau signifie que les vastes flux de données générés par toutes ces caméras, capteurs et autres périphériques embarqués peuvent être automatiquement envoyés "à la maison" pour traitement et analyse.

## Le Rêve de l'IoT

Voici quelques façons dont les applications IoT changent déjà activement les pratiques commerciales et consommateurs :

### Contrôle des stocks

Le tout premier appareil IoT était – du moins, on peut le dire – un distributeur automatique de Coca-Cola à l'Université Carnegie Mellon. Dans les années 80, la machine a été modifiée pour signaler numériquement son inventaire en cours. 

L'idée simple que les appareils physiques peuvent se surveiller eux-mêmes et leur environnement, fournissant des rapports de statut précis et à la minute aux serveurs distants, est au cœur de nombreuses solutions industrielles modernes. 

Les opérations modernes de vente au détail, de gros, de logistique et de fabrication ont désormais un accès constant à leurs stocks, leur permettant de comprendre les tendances et d'anticiper les problèmes.

### Agriculture

De plus en plus, l'agriculture moderne intègre des technologies robotisées d'irrigation, de fertilisation, de plantation et même de récolte. 

Tous ces robots qui circulent sur votre propriété génèrent des données et, de temps en temps, se mettent dans des situations difficiles. 

Le transfert de ces données "en arrière" vers les serveurs d'administration est crucial pour suivre ce qui se passe, ce qui pourrait avoir besoin d'être réparé et comment votre ferme réelle se comporte. Vous pouvez donc vous attendre à ce que chacun de ces appareils fasse partie de l'IoT de quelqu'un.

### Militaire

La communication est essentielle pour les opérations militaires. Mais si même les armes, les véhicules et autres équipements peuvent communiquer de manière autonome, et s'il existe des serveurs dédiés à l'interprétation et à l'action sur cette communication, alors vous êtes déjà bien en avance dans le jeu. 

Des capteurs connectés à chacun des centaines de composants d'un avion de chasse, par exemple, peuvent contribuer à donner aux planificateurs une vue sans précédent de ce qui se passe réellement.

### Villes intelligentes

Lorsque des capteurs intégrés dans des bâtiments, des routes, l'éclairage public, des smartphones et des systèmes électriques sont combinés avec des données provenant de caméras de circulation et de départements publics, le potentiel d'informations basées sur les données est énorme. 

Des données bien comprises peuvent aider les villes à gérer leurs ressources, leurs services publics et même leur circulation plus efficacement, et à mieux maintenir leur infrastructure physique.

### Maisons intelligentes

À une échelle beaucoup plus petite que les villes intelligentes, les appareils domestiques peuvent être connectés et surveillés et contrôlés via des applications pour smartphones ou des serveurs distants. 

Les appareils domestiques intelligents incluent déjà des systèmes de chauffage et de climatisation, des ampoules, des aspirateurs robotisés, des portes de garage et des systèmes de sécurité. Les appareils domestiques intelligents peuvent être contrôlés via des applications téléphoniques mais, dans de nombreux cas, également via des appareils contrôlés par la voix comme Amazon Echo (Alexa).

Les conversations sur l'IoT sont toujours à un pas du buzzwordisme – où les mots perdent leur sens et l'exagération devient un choix de style de vie acceptable. 

Tous les trucs IoT ne sont pas réellement de l'IoT. Ou, pour le dire autrement, tout l'IoT ne vaut pas la peine d'en parler. Mais voici une bonne façon de catégoriser une technologie particulière : si, heure après heure, quelque chose génère plus de données que ce qu'un être humain pourrait absorber, alors c'est probablement un appareil IoT.

Traiter efficacement toutes ces données peut être un problème. Et ce n'est pas le seul potentiel de problèmes dans le monde de l'IoT.

## Le Cauchemar de l'IoT

Dans le monde de la technologie de l'information, en règle générale, plus vous avez de connexions réseau actives dans votre infrastructure, plus votre risque d'être attaqué avec succès est grand. 

C'est parce que les intrusions réussies des pirates proviennent généralement de dispositifs mal configurés ou non corrigés. Plus vous exposez de dispositifs publics, plus la chance qu'un d'eux ait une vulnérabilité sérieuse est grande.

De quelles vulnérabilités parlons-nous ? Eh bien, la base de données des vulnérabilités et expositions courantes du gouvernement américain contient près de 140 000 entrées individuelles, chacune représentant une faiblesse logicielle unique qui pourrait permettre un accès non autorisé et la destruction d'un système informatique. 

Il existe des menaces affectant tous les systèmes d'exploitation (Windows, Linux, macOS), tous les formats (serveur, PC, smartphone) et tous les âges (il existe des menaces actives remontant aux années 1990). Et des centaines de nouvelles entrées sont ajoutées chaque mois.

À cet égard, les appareils IoT ne sont pas différents des autres types d'ordinateurs. Mais il y a une façon dont ils sont bien pires. Parce que vous n'interagissez normalement pas directement avec les appareils IoT au niveau du système d'exploitation, et parce qu'ils sont souvent des articles de commodité achetés et déployés par dizaines ou milliers, vous ne les traitez pas instinctivement comme des ordinateurs.

La plupart d'entre nous, par exemple, savent que nous devrions créer des mots de passe complexes et uniques pour nos ordinateurs portables et nos routeurs WiFi. Mais votre réfrigérateur ? Il suffit de le brancher et tout ira bien ! Le problème est que de nombreux appareils IoT – comme les réfrigérateurs "intelligents" – ont leurs propres systèmes d'exploitation embarqués et, généralement, leurs propres interfaces réseau.

Il y a de bonnes chances que quiconque roulant dans votre rue résidentielle tranquille puisse scanner les réseaux disponibles, identifier rapidement la marque de l'appareil IoT que vous utilisez, supposer que vous n'avez pas changé les informations d'authentification de leurs paramètres d'usine, et se connecter à votre réseau privé. 

Ce qui aggrave considérablement les choses, c'est que de nombreux fabricants d'appareils expédient encore leurs produits avec des informations d'authentification utilisant une variation de admin/admin.

C'est un gros problème.

# Tirer parti des identités fédérées

Toute cette discussion sur les dangers présentés par l'authentification et les informations d'identification devrait vous rendre curieux de savoir comment elles peuvent être utilisées pour générer de bonnes choses en matière de connectivité. 

En un seul mot, ce serait la fédération. La fédération d'identités est une technologie permettant de lier l'identité d'une seule personne à travers plusieurs services réseau. La fédération est ce qui vous permet de vous connecter à des sites de jeux en ligne ou d'applications web en utilisant, par exemple, vos informations d'identification de compte Google.

L'avantage de la fédération est qu'une seule connexion peut être tout ce dont vous aurez besoin lorsque vous passerez d'un service en ligne à l'autre que vous utilisez régulièrement. Cela vous permet de réduire le risque d'exposer votre mot de passe via un site web vulnérable. 

Bien sûr, cela augmente également les dommages qui peuvent résulter d'une violation grave des données des serveurs utilisés par votre fournisseur de fédération.

La fédération peut être utilisée pour s'intégrer avec des systèmes d'authentification tiers de connexion unique (SSO), comme Kerberos, le Lightweight Directory Access Protocol (LDAP) et Active Directory (AD) de Microsoft. Lorsqu'ils sont utilisés avec des services cloud, les systèmes SSO peuvent permettre un accès automatisé et sécurisé aux ressources de compte privé pour les consommateurs ou les processus.

Outre la commodité, toute cette bonté d'authentification crée des opportunités pour une collaboration à distance sécurisée sur des projets grands et complexes – une tendance en pleine croissance.

_Les vidéos YouTube des dix chapitres de ce livre [sont disponibles ici](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Beaucoup plus de bonté technologique – sous forme de livres, de cours et d'articles – [peut être obtenue ici](https://bootstrap-it.com). Et envisagez de suivre mes [cours sur AWS, la sécurité et la technologie des conteneurs ici](https://www.udemy.com/user/david-clinton-12/)._
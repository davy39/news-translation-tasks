---
title: Qu'est-ce que le Cloud Computing ? Guide du débutant au Cloud Computing avec
  AWS
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-10-18T13:18:21.896Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-cloud-computing-with-aws
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729159103929/5b4c74fe-3bf5-4ac5-9739-4313d46a8dd1.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
seo_title: Qu'est-ce que le Cloud Computing ? Guide du débutant au Cloud Computing
  avec AWS
seo_desc: 'Ever wondered what people mean when they say, “It’s stored in the cloud”?
  If you’re imagining fluffy white clouds up in the sky storing your pictures, documents,
  or your Netflix favorites, then you’re in for a surprise!

  Spoiler alert: the cloud is mu...'
---

Vous êtes-vous déjà demandé ce que les gens veulent dire lorsqu'ils disent : « C'est stocké dans le cloud » ? Si vous imaginez des nuages blancs et duveteux dans le ciel stockant vos photos, documents ou vos favoris Netflix, alors vous allez être surpris !

Alerte spoiler : le cloud est bien plus que cela, et c'est une partie cruciale de ce qui alimente notre monde numérique aujourd'hui. Alors, prenez un café (ou un thé), installez-vous confortablement, et plongeons ensemble dans le royaume nuageux du cloud computing.

## Table des matières

* [Table des matières](#heading-table-des-matieres)
    
* [Alors, qu'est-ce que le Cloud exactement ?](#heading-alors-quest-ce-que-le-cloud-exactement)
    
    * [Une métaphore amusante](#heading-une-metaphore-amusante)
        
* [Types de Clouds](#heading-types-de-clouds)
    
* [Modèles de services Cloud (IAAS, PAAS, SAAS)](#heading-modeles-de-services-cloud-iaas-paas-saas)
    
* [Qu'est-ce qu'AWS ?](#heading-quest-ce-quaws)
    
    * [Pourquoi les gens adorent AWS ?](#heading-pourquoi-les-gens-adorent-aws)
        
    * [Architecture Cloud AWS](#heading-architecture-cloud-aws)
        
    * [Composants clés de l'architecture Cloud AWS](#heading-composants-cles-de-larchitecture-cloud-aws)
        
    * [Modèle de responsabilité partagée](#heading-modele-de-responsabilite-partagee)
        
* [Régions AWS, Zones de disponibilité, Emplacements Edge et Zones locales](#heading-regions-aws-zones-de-disponibilite-emplacements-edge-et-zones-locales)
    
    * [Latence](#heading-latence)
        
    * [Façons d'accéder aux services AWS](#heading-facons-dacceder-aux-services-aws)
        
* [Calculatrice AWS](#heading-calculatrice-aws)
    
* [Conclusion](#heading-conclusion)
    

## Alors, qu'est-ce que le Cloud exactement ?

En termes simples, le cloud est un réseau de serveurs distants à travers le monde qui stockent des données, exécutent des applications et alimentent des services, afin que vous n'ayez pas à le faire. Imaginez cela comme la location d'une unité de stockage, sauf qu'elle est en ligne, plus flexible et peut faire bien plus que simplement stocker des choses.

Le cloud computing consiste à accéder à ces ressources via Internet (au lieu d'un ordinateur physique ou d'un serveur que vous devez maintenir vous-même).

Par exemple, lorsque vous téléchargez une photo sur Instagram ou diffusez une émission sur Netflix, vous accédez à des fichiers qui sont stockés dans le cloud*.* Instagram et Netflix ne stockent pas toutes ces données sur votre téléphone ou ordinateur portable – ils s'appuient sur des serveurs cloud massifs et sécurisés pour tout contenir. Pratique, n'est-ce pas ?

### Une métaphore amusante

Imaginez que vous ouvrez une boulangerie. Vous auriez besoin d'un emplacement physique, de fours, d'ingrédients et d'employés. C'est un investissement énorme ! Maintenant, imaginons qu'il existe un service de boulangerie qui fournit tous ces éléments essentiels sans que vous ayez à en posséder aucun. Vous payez simplement « à mesure que vous cuisez ». C'est le cloud en un mot.

Au lieu d'investir dans et de maintenir une flotte de serveurs (qui, soit dit en passant, prennent beaucoup de place, d'énergie et d'attention), vous louez ce dont vous avez besoin, vous l'utilisez et laissez la maintenance au fournisseur de cloud. Cette approche signifie que vous pouvez « dimensionner » (faire ou servir plus) sans investissements supplémentaires, rendant votre vie beaucoup plus facile et votre travail bien plus flexible.

## Types de Clouds

Allons un peu plus loin avec trois types de configurations cloud. Connaître celles-ci vous aidera à comprendre les différentes saveurs des services cloud :

1. **Cloud Public** : Imaginez louer des espaces partagés dans un immense « bâtiment » en ligne, comme AWS (Amazon Web Services), Microsoft Azure ou Google Cloud. Ici, n'importe qui peut louer de l'espace ou des ressources, et c'est idéal pour la flexibilité et l'efficacité des coûts.
    
2. **Cloud Privé** : Imaginez votre propre configuration de boulangerie où seule votre équipe a accès. Les entreprises mettent en place des clouds privés pour un contrôle et une confidentialité maximaux. Pensez aux banques ou aux agences gouvernementales, elles utilisent souvent des clouds privés pour des raisons de sécurité.
    
3. **Cloud Hybride** : Celui-ci est un mélange ! C'est comme avoir une pièce privée dans un plus grand bâtiment partagé, où vous pouvez accéder aux ressources à la fois de manière privée et publique, selon vos besoins. Cette flexibilité est un favori pour les entreprises cherchant le meilleur des deux mondes.
    

## Modèles de services Cloud (IAAS, PAAS, SAAS)

* Les modèles de services cloud sont les moyens par lesquels les services cloud sont livrés aux utilisateurs, chaque modèle offrant différents niveaux de contrôle, de flexibilité et de gestion. Les trois principaux modèles de services cloud sont **IaaS (Infrastructure as a Service)**, **PaaS (Platform as a Service)** et **SaaS (Software as a Service)**. Chacun répond à différents besoins en fonction du niveau d'infrastructure, de plateforme ou de services d'application qu'une organisation nécessite.
    

#### Sur site

* Imaginez que vous organisez une soirée pizza et que vous voulez un contrôle total. Vous achetez les ingrédients, faites la pâte, préparez les garnitures et faites cuire la pizza dans votre four à la maison. C'est sur site (ou « sur site » en abrégé). Vous êtes responsable de tout : ingrédients, cuisson, nettoyage et gestion de l'équipement. C'est la même chose dans le monde de la technologie. Avec l'informatique sur site, les entreprises gèrent et maintiennent leurs propres serveurs, réseaux et systèmes de stockage, généralement dans leurs propres centres de données.
    
* Cette approche traditionnelle donne aux entreprises un contrôle total, mais elle s'accompagne également de la responsabilité de tout gérer : maintenance du matériel, mises à jour logicielles, sauvegardes de données et sécurité. Pour certaines entreprises, cela en vaut la peine pour la tranquillité d'esprit de garder tout en interne. Mais pour d'autres, tout ce contrôle peut être épuisant et coûteux.
    

#### Infrastructure as a Service (IaaS)

* Si sur site est une pizza à partir de zéro, IaaS (Infrastructure as a Service) est comme louer une cuisine à pizza déjà équipée de fours, de comptoirs et d'outils. Tout ce que vous avez à faire est d'apporter vos ingrédients et de commencer à cuisiner. En termes de cloud, cela signifie qu'un fournisseur comme AWS loue des machines virtuelles, du stockage et des réseaux afin que vous puissiez installer vos systèmes d'exploitation, bases de données et applications.
    
* **Comment cela fonctionne** : Dans un modèle IaaS, AWS ou un autre fournisseur propose la puissance de calcul, le stockage et les ressources réseau dont vous avez besoin, mais vous contrôlez toujours les logiciels et applications qui s'exécutent sur eux. Cela vous donne de la flexibilité sans le tracas de la gestion du matériel physique.
    
* **Pourquoi choisir IaaS ?**
    
    * **Évolutivité** : Vous pouvez augmenter ou diminuer les ressources en fonction de vos besoins, comme ajouter plus de « fours » lorsque la demande est élevée.
        
    * **Économies de coûts** : Vous évitez les dépenses d'achat et de maintenance de matériel.
        
    * **Flexibilité** : Vous obtenez la base, mais vous contrôlez toujours ce que vous construisez par-dessus, vous donnant beaucoup de liberté pour personnaliser.
        

#### Platform as a Service (PaaS)

* Disons que vous voulez vous rapprocher du bonheur de la pizza sans vous soucier de la gestion de la cuisine. Avec PaaS (Platform as a Service), vous recevez une station de cuisson prête à l'emploi, entièrement approvisionnée en pâte, sauce et garnitures. Vous n'avez qu'à choisir vos garnitures et faire la pizza à votre manière.
    
* En termes techniques, un fournisseur PaaS gère l'infrastructure sous-jacente, y compris le système d'exploitation, les serveurs, le stockage et les réseaux. Tout ce que vous avez à faire est de vous concentrer sur le code de votre application et de laisser le fournisseur gérer le reste. AWS Elastic Beanstalk, par exemple, vous permet de déployer et de gérer des applications sans vous enliser dans les configurations de serveur.
    
* **Pourquoi choisir PaaS ?**
    
    * **Vitesse** : Vous sautez la configuration et passez directement à la partie cuisson, parfait pour les développeurs qui se concentrent sur la construction et le déploiement d'applications.
        
    * **Environnement géré** : Le fournisseur gère le système d'exploitation, les mises à jour, les correctifs de sécurité et la mise à l'échelle, afin que vous n'ayez pas à vous en soucier.
        
    * **Concentration sur le code** : C'est idéal si vous voulez vous concentrer sur la création de votre application, et non sur la gestion de l'infrastructure.
        

#### Software as a Service (SaaS)

* Maintenant, si vous êtes d'humeur pour un confort ultime, pourquoi ne pas simplement commander une livraison de pizza ? Avec SaaS (Software as a Service), vous n'avez pas à vous soucier de la cuisine, des ingrédients, ni même de la cuisson. Au lieu de cela, votre pizza arrive chaude et prête à être mangée.
    
* En termes de cloud, SaaS est une application logicielle entièrement gérée, hébergée par le fournisseur et accessible via Internet. Des exemples incluent des applications comme Gmail, Dropbox ou Microsoft 365. Vous vous connectez simplement et commencez à utiliser le service—aucune installation, mises à jour ou maintenance nécessaires.
    
* **Pourquoi choisir SaaS ?**
    
    * **Confort** : Comme la livraison de pizza, il est prêt à être consommé immédiatement, vous faisant économiser du temps de configuration et de maintenance.
        
    * **Accessibilité** : Puisqu'il est basé sur Internet, vous pouvez y accéder de n'importe où.
        
    * **Mises à jour automatiques** : Le fournisseur gère les mises à jour, afin que vous ayez toujours les dernières fonctionnalités.
        

![Modèles de services Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1729157009842/088adbfa-1766-4c57-8150-b6856316ba62.jpeg align="center")

## Qu'est-ce qu'AWS ?

* Amazon Web Services, ou AWS, est une plateforme cloud d'Amazon qui fournit une large gamme de ressources informatiques, du stockage aux bases de données, en passant par les machines virtuelles et les services d'IA. Imaginez pouvoir louer un énorme centre de données virtuel sans avoir à acheter, installer ou maintenir du matériel physique. Cela semble génial, n'est-ce pas ? C'est la beauté d'AWS. Vous pouvez lancer des ressources en quelques minutes et ne payer que ce que vous utilisez, ce qui le rend incroyablement rentable.
    

### Pourquoi les gens adorent AWS ?

* AWS offre une variété de services, en faisant un buffet à volonté d'outils technologiques. Si vous construisez une nouvelle application, exécutez un site web ou stockez des données, AWS peut tout gérer. De plus, il est fiable, sécurisé et évolutif, ce qui signifie que vous pouvez commencer petit et grandir sans avoir à faire des changements drastiques.
    

### Architecture Cloud AWS

* Pensez à l'architecture Cloud AWS comme au cadre ou au « plan » qui définit comment une application est construite et comment elle interagit avec différents services sur la plateforme AWS. Tout comme l'infrastructure d'une ville a besoin de routes, de bâtiments, de services publics et d'un moyen de gérer le trafic, une architecture cloud AWS se compose de divers composants qui maintiennent tout en marche sans problème. Ces composants incluent la mise en réseau, la puissance de calcul, le stockage, les bases de données et les services de sécurité.
    
* Au cœur de l'architecture Cloud AWS, elle est conçue pour aider les entreprises à créer des applications fiables, évolutives et sécurisées sans avoir à tout construire à partir de zéro. AWS offre une large gamme d'outils et de services qui s'emboîtent comme des pièces de puzzle, rendant facile la création d'un environnement cloud personnalisé et efficace.
    

### Composants clés de l'architecture Cloud AWS

* Pour vraiment comprendre l'architecture Cloud AWS, examinons certains de ses composants essentiels. Chaque pièce a un rôle spécifique, et ensemble, elles constituent un environnement cloud solide et performant.
    

##### 1\. **Calcul**

Toute application basée sur le cloud a besoin de puissance de traitement pour exécuter son code, gérer les requêtes des utilisateurs et traiter les données. C'est là que les **services de calcul** interviennent.

* **Amazon EC2 (Elastic Compute Cloud)** : Pensez à EC2 comme la centrale électrique derrière votre application. Les instances EC2 sont des serveurs virtuels qui peuvent être personnalisés pour répondre aux besoins de votre application—un peu comme choisir entre un ordinateur portable, un ordinateur de bureau ou un supercalculateur en fonction de vos exigences de travail.
    
* **AWS Lambda** : AWS Lambda est la star de l'informatique sans serveur, vous permettant d'exécuter du code sans gérer de serveurs. C'est parfait pour les petites tâches qui ne nécessitent pas de ressources constantes. Par exemple, si vous voulez redimensionner automatiquement les photos chaque fois qu'elles sont téléchargées, Lambda peut gérer cela avec facilité !
    

##### 2\. **Stockage**

Toutes les applications ont besoin d'un endroit pour stocker leurs données—pensez aux fichiers, aux profils utilisateurs ou aux enregistrements de transactions. AWS propose plusieurs options de stockage pour répondre à une large gamme de besoins.

* **Amazon S3 (Simple Storage Service)** : S3 est comme une armoire de classement basée sur le cloud et extensible où vous pouvez stocker et récupérer des quantités virtuellement illimitées de données. Il est hautement sécurisé et accessible, ce qui en fait un choix populaire pour le stockage de données.
    
* **Amazon EBS (Elastic Block Store)** : EBS fonctionne comme un disque dur attaché à une instance EC2, ce qui le rend idéal pour les applications nécessitant un stockage haute performance.
    

##### 3\. **Bases de données**

Pour de nombreuses applications, les données doivent être stockées de manière structurée, donc AWS propose plusieurs options de bases de données pour différents types de données.

* **Amazon RDS (Relational Database Service)** : RDS gère les données structurées comme les enregistrements clients ou les informations de commande. Vous pouvez configurer des bases de données comme MySQL ou PostgreSQL, et AWS s'occupe de la maintenance et des sauvegardes.
    
* **Amazon DynamoDB** : Pour les applications à fort trafic qui nécessitent un accès rapide aux données, DynamoDB offre un stockage NoSQL rapide et flexible qui s'adapte automatiquement.
    

##### 4\. **Mise en réseau**

Pour garder tout connecté et garantir que les données circulent de manière sécurisée, AWS propose des services de mise en réseau qui agissent comme les « autoroutes » de votre architecture cloud.

* **Amazon VPC (Virtual Private Cloud)** : VPC crée un réseau virtuel sécurisé où vous pouvez contrôler qui accède à vos ressources. C'est comme avoir votre propre espace privé dans le gigantesque centre de données d'AWS.
    
* **AWS CloudFront** : CloudFront est un réseau de diffusion de contenu (CDN) qui accélère la diffusion de contenu en le mettant en cache plus près des utilisateurs. Ainsi, si votre application a des utilisateurs dans le monde entier, CloudFront garantit qu'ils obtiennent la meilleure expérience possible en réduisant les temps de chargement.
    

##### 5\. **Sécurité et identité**

AWS prend la sécurité au sérieux, et avec des outils comme **AWS Identity and Access Management (IAM)** et **AWS Shield**, vous pouvez gérer l'accès aux ressources et protéger votre architecture contre les menaces de sécurité.

* **IAM (Identity and Access Management)** : IAM vous permet de créer et de gérer les permissions pour chaque utilisateur et service, afin que vous puissiez contrôler qui peut faire quoi. Cela garantit que vos données restent en sécurité et que seules les bonnes personnes y ont accès.
    
* **AWS Shield** : Pour ceux qui s'inquiètent des attaques DDoS, Shield offre une protection en filtrant automatiquement le trafic malveillant.
    

##### **Mettre tout ensemble : Comment fonctionne l'architecture Cloud AWS**

Alors, comment toutes ces pièces fonctionnent-elles ensemble ? Imaginez construire une boutique en ligne sur AWS :

1. **Calcul (EC2/Lambda)** : Le backend de votre boutique s'exécute sur des instances EC2, gérant les requêtes et traitant les commandes. Une fonction Lambda pourrait gérer des tâches plus petites, comme l'envoi d'e-mails de confirmation.
    
2. **Stockage (S3)** : Les photos des produits et les fichiers téléchargés par les utilisateurs sont stockés dans S3, les gardant sécurisés et accessibles.
    
3. **Base de données (RDS)** : Les détails des clients, les informations de commande et les listes de produits sont stockés dans une base de données RDS, afin que vous puissiez facilement suivre les commandes et gérer l'inventaire.
    
4. **Mise en réseau (VPC & CloudFront)** : VPC garde votre réseau sécurisé, et CloudFront accélère la diffusion de votre site aux clients du monde entier.
    
5. **Sécurité (IAM & Shield)** : IAM contrôle l'accès des utilisateurs, garantissant que seul le personnel autorisé peut accéder aux données sensibles. Shield protège contre les attaques DDoS, gardant votre site en ligne et opérationnel même dans des situations de trafic élevé.
    

### Modèle de responsabilité partagée

* Imaginez louer une maison, et AWS possède la maison et s'assure que la structure est sûre et sécurisée. Le toit est solide, les portes se verrouillent et la plomberie fonctionne. Mais en ce qui concerne ce qui se passe *à l'intérieur*—les meubles, qui a les clés et comment vous le gardez propre—c'est votre travail en tant que locataire.
    
* En termes de cloud, AWS s'occupe de l'infrastructure, s'assurant que les serveurs sont protégés et que leurs centres de données sont sécurisés. Mais les données que vous mettez sur AWS, les applications que vous exécutez et les paramètres de sécurité que vous choisissez sont de votre responsabilité. C'est un effort d'équipe où AWS garde le cloud en sécurité, et vous gardez ce qui s'y trouve sécurisé.
    

![Responsabilité partagée AWS](https://cdn.hashnode.com/res/hashnode/image/upload/v1729157534482/562b3616-5339-4ec8-8ca3-540fdc48d9a4.png align="center")

#### Décomposition du modèle de responsabilité partagée

Le modèle de responsabilité partagée est divisé en deux parties principales : **Sécurité du Cloud** (c'est le travail d'AWS) et **Sécurité dans le Cloud** (c'est à vous).

##### 1\. Sécurité **du** Cloud

AWS est comme le gardien de sécurité pour tout l'environnement cloud. Voici ce dont AWS est responsable :

* **Sécurité des centres de données** : AWS est responsable de la sécurité physique de ses centres de données. Ils ont des contrôles d'accès stricts, des caméras de sécurité et même une analyse biométrique pour s'assurer que seul le personnel autorisé peut entrer. Pas besoin de s'inquiéter que quiconque accède physiquement à vos données !
    
* **Maintenance du matériel et des logiciels** : AWS s'occupe de la maintenance, des correctifs et des mises à jour du matériel et des logiciels sous-jacents. Cela inclut la gestion des serveurs physiques, des dispositifs de stockage et des équipements de mise en réseau qui alimentent les services AWS.
    
* **Sécurité du réseau** : AWS s'assure que l'infrastructure de mise en réseau est protégée contre les menaces. Ils déploient des pare-feu, une protection DDoS et d'autres mesures pour tenir les acteurs malveillants à l'écart.
    

Pensez à la responsabilité d'AWS comme la création et la maintenance d'une plateforme cloud hautement sécurisée. Cela signifie que vous pouvez compter sur AWS pour maintenir les centres de données en marche sans problème, fournir des serveurs fiables et gérer les menaces au niveau de l'infrastructure.

##### 2\. Sécurité dans le Cloud

Maintenant, voici où vous intervenez. Bien qu'AWS fournisse une infrastructure sécurisée, vous êtes responsable de ce que vous en faites. Vos responsabilités incluent :

* **Protection des données** : Vous décidez comment vos données sont chiffrées et qui peut y accéder. Par exemple, AWS propose des options pour chiffrer vos données au repos et en transit, mais c'est à vous d'activer le chiffrement et de gérer vos clés de chiffrement.
    
* **Gestion des identités et des accès (IAM)** : Le service IAM d'AWS vous permet de contrôler qui a accès à vos ressources AWS. C'est comme avoir des clés pour différentes pièces dans une maison—certaines personnes peuvent n'avoir besoin d'accès qu'à la cuisine, tandis que d'autres ont besoin d'accès à toutes les pièces. En définissant des rôles et des permissions, vous décidez qui peut faire quoi.
    
* **Configuration des groupes de sécurité** : Les groupes de sécurité sont comme des pare-feu pour vos ressources AWS, contrôlant ce qui peut entrer et sortir. Vous décidez quel trafic est autorisé et où il est autorisé à aller. Pensez à cela comme à la création de règles de sécurité pour votre environnement cloud.
    
* **Sécurité des applications** : Si vous exécutez une application web sur AWS, vous êtes responsable de la sécurisation du code et de la protection contre les vulnérabilités, comme l'injection SQL ou le cross-site scripting. AWS ne peut pas savoir ce qu'il y a dans votre code, donc ils laissent la sécurité des applications entre vos mains.
    
* **Audits réguliers et conformité** : AWS offre des outils pour aider à l'audit, mais c'est à vous de surveiller et de garantir la conformité avec les normes de l'industrie. Des audits réguliers peuvent vous aider à vérifier que tout fonctionne bien et selon vos besoins de sécurité.
    

## Régions AWS, Zones de disponibilité, Emplacements Edge et Zones locales

Si vous avez mis les pieds dans AWS, vous avez probablement rencontré des termes comme « Régions », « Zones de disponibilité », « Emplacements Edge » et « Zones locales ». Et soyons honnêtes, ils peuvent sembler un peu intimidants au début. Mais comprendre ces termes est la clé pour construire une application réussie sur AWS. C'est comme obtenir une carte avant de vous aventurer dans un parc à thème—connaître la disposition rend toute l'expérience plus fluide et plus agréable.

Alors, faisons un tour amusant du « parc cloud » AWS et voyons comment ces zones s'emboîtent !

#### 1\. **Régions AWS**

Imaginez AWS comme un parc à thème avec des entrées partout dans le monde. Les **Régions** sont comme les différentes entrées principales de ce parc massif. Chaque Région est une zone entièrement équipée de l'infrastructure AWS située dans une partie spécifique du monde. Il y a plus de 34 Régions dans le monde, chacune fournissant un ensemble complet de services et d'installations.

Choisir une Région, c'est comme choisir par quelle entrée commencer votre voyage. Si la plupart de vos clients sont en Europe, vous pourriez choisir une Région plus proche d'eux, comme Francfort ou Londres. Cela aide à réduire la latence, ce qui signifie que les utilisateurs bénéficient de temps de chargement plus rapides et d'interactions plus fluides.

#### 2\. **Zones de disponibilité (AZ)**

Une fois que vous êtes à l'intérieur d'une Région (entrée), vous trouverez des **Zones de disponibilité**, ou AZ, qui sont comme les différentes sections du parc à thème. Chaque AZ est un centre de données séparé et indépendant, proche des autres au sein de la même Région, mais avec ses propres sources d'alimentation, de refroidissement et de réseau uniques. Cette configuration offre une redondance, un facteur critique pour une haute disponibilité et une grande fiabilité.

Voici pourquoi c'est important : Imaginez exécuter une application qui doit être en ligne 24h/24 et 7j/7. Si vous l'hébergez dans une seule AZ, et que cette AZ a un problème d'alimentation, votre application pourrait tomber en panne. Mais en configurant votre application sur plusieurs AZ (disons, sur les étages « Adventure Land » et « Fantasy Land »), si une zone rencontre un problème, les autres garderont votre application en marche, créant une expérience fluide pour les utilisateurs.

#### 3\. **Emplacements Edge**

Ensuite, passons aux **Emplacements Edge**, qui sont comme les stands pop-up que vous voyez dans le parc, servant tout, des cartes aux snacks rapides. Les Emplacements Edge sont des « mini-stations AWS » stratégiquement placées qui livrent des données mises en cache près de vos utilisateurs, où qu'ils se trouvent.

Le réseau de diffusion de contenu d'AWS, **Amazon CloudFront**, fonctionne à travers ces Emplacements Edge. Donc, si vous avez une vidéo ou une image de site web que les gens au Japon et en Afrique du Sud doivent accéder, CloudFront la livre depuis l'Emplacement Edge le plus proche au lieu du serveur central. Cela réduit les temps de chargement et offre une expérience plus rapide et plus réactive. Les Emplacements Edge sont parfaits pour les applications avec des besoins médias lourds, car ils garantissent que le contenu se charge rapidement et efficacement.

#### 4\. **Zones locales**

Enfin, nous avons les **Zones locales**. Ce sont comme les zones VIP du parc, donnant aux visiteurs un accès quasi instantané à certaines attractions. Les Zones locales sont de petits groupes d'infrastructure AWS, mis en place plus près de villes spécifiques pour fournir une latence ultra-faible pour les applications nécessitant des temps de réponse rapides.

Disons que vous exécutez une application de jeu, et vous voulez que les joueurs de Los Angeles ressentent un minimum de latence. L'utilisation d'une Zone locale à Los Angeles donne à ces utilisateurs un accès immédiat à votre application, gardant l'expérience rapide et fluide. Les Zones locales sont idéales pour les services nécessitant un traitement haute vitesse dans les zones métropolitaines comme les jeux en ligne, la production de médias et la réalité virtuelle.

#### Mettre tout ensemble : Planifier votre aventure AWS

Pour concevoir l'architecture de votre application, réfléchissez à l'endroit où se trouvent vos utilisateurs et au type d'expérience que vous souhaitez leur offrir. Voici un guide rapide pour vous aider à planifier :

* **Régions** : Choisissez une Région proche de votre base d'utilisateurs principale pour minimiser la latence. Cela aide à offrir une expérience plus rapide et plus réactive aux utilisateurs.
    
* **Zones de disponibilité (AZ)** : Utilisez plusieurs AZ au sein d'une Région pour construire une application résiliente et hautement disponible. Ainsi, si une zone tombe en panne, les autres garderont votre application en marche.
    
* **Emplacements Edge** : Pour les applications gourmandes en contenu, comme les services de streaming ou les sites de commerce électronique, utilisez les Emplacements Edge de CloudFront pour mettre en cache et livrer du contenu rapidement, où que se trouvent les utilisateurs.
    
* **Zones locales** : Pour les applications nécessitant une latence ultra-faible dans des villes spécifiques, les Zones locales rapprochent l'infrastructure AWS des utilisateurs, créant une expérience quasi instantanée pour les applications à forte demande.
    

Vous pouvez trouver les derniers chiffres concernant les régions, les AZ, les emplacements Edge et les zones locales [ici](https://aws.amazon.com/about-aws/global-infrastructure/?p=ngi&loc=1)

### Latence

* En termes simples, la latence est le délai entre l'action d'un utilisateur et la réponse d'une application web à cette action. Imaginez cela comme un écho numérique—dites quelque chose, et il y a une petite pause avant de l'entendre en retour. La latence est mesurée en millisecondes (ms), et plus la latence est faible, plus votre connexion semble rapide.
    
* **Exemple** : Disons que vous naviguez sur un site web depuis votre domicile à New York, mais le serveur hébergeant le site web est situé à Sydney. Votre requête doit parcourir tout le chemin jusqu'à Sydney, et la réponse du serveur doit parcourir tout le chemin jusqu'à vous. Même si les données voyagent vite (vraiment vite !), la distance crée toujours un délai. Et ce délai ? C'est la latence.
    

#### Pourquoi la latence est-elle importante ?

* Un peu de latence peut ne pas sembler un gros problème, mais lorsqu'elle s'accumule, elle peut rendre l'expérience utilisateur frustrante. Avez-vous déjà essayé de jouer à un jeu vidéo multijoueur pour obtenir ce redoutable « lag » juste au moment où vous êtes sur le point de gagner ? Ou peut-être avez-vous attendu quelques secondes de plus pour qu'une vidéo se charge ? Une latence élevée est souvent la coupable ici.
    
* **Faible latence = Expérience rapide et réactive**
    
* **Latence élevée = Retards et frustration**
    
* Lorsque la latence est élevée, chaque interaction avec une application semble retardée, ce qui peut éloigner les utilisateurs. C'est pourquoi des entreprises comme AWS investissent dans la minimisation de la latence en construisant une infrastructure proche des utilisateurs du monde entier.
    

#### AWS et la latence : Comment AWS minimise-t-il la latence ?

* AWS prend la latence au sérieux, et son infrastructure est conçue pour garder la latence aussi faible que possible pour les utilisateurs du monde entier. Voici comment AWS s'attaque à la latence de front :
    

* **Régions et Zones de disponibilité (AZ)** : AWS dispose de centres de données appelés Régions et AZ répartis dans le monde entier. En choisissant une Région proche de votre base d'utilisateurs principale, vous pouvez réduire la latence en minimisant la distance que les données doivent parcourir.
    
* **Emplacements Edge et Amazon CloudFront** : AWS dispose d'Emplacements Edge dans le monde entier qui fonctionnent avec Amazon CloudFront, son réseau de diffusion de contenu (CDN). Pensez aux Emplacements Edge comme des points chauds de données dans des zones populaires—en mettant en cache le contenu dans ces emplacements, AWS s'assure que les utilisateurs obtiennent les temps de chargement les plus rapides possibles, où qu'ils se trouvent.
    
* **Zones locales** : Pour les applications nécessitant une latence ultra-faible dans des villes spécifiques, les Zones locales rapprochent l'infrastructure des zones métropolitaines, offrant un accès ultra-rapide pour les applications qui ne peuvent pas se permettre de lag.
    

#### Une analogie de latence : Commander une pizza

* Décomposons cela avec une analogie de pizza. Imaginez commander une pizza dans un restaurant :
    

* **Faible latence** : Le restaurant de pizza est à quelques rues de là, donc vous obtenez votre pizza fumante en un rien de temps.
    
* **Latence élevée** : Maintenant, imaginez que le restaurant de pizza est de l'autre côté de la ville. Votre pizza arrive en retard et tiède à cause du long trajet. C'est de la latence élevée !
    

En termes AWS, avoir une Région ou un Emplacement Edge proche des utilisateurs, c'est comme commander une pizza dans une boutique à proximité plutôt que dans une boutique à l'autre bout de la ville. Plus la distance est courte, moins vous passez de temps à attendre votre « pizza » (ou, dans ce cas, vos données) à arriver.

### Façons d'accéder aux services AWS

Lorsque vous plongez dans AWS, vous réaliserez rapidement qu'il se passe beaucoup de choses en coulisses. Mais se lancer dans AWS et accéder à sa suite de services cloud n'est pas compliqué—c'est en fait assez convivial. AWS propose plusieurs façons d'interagir avec ses services, que vous préfériez cliquer sur des boutons, taper des commandes ou même écrire du code. C'est comme une grande maison virtuelle avec plusieurs portes d'entrée—choisissez celle qui vous convient le mieux !

#### 1\. **Console de gestion AWS : L'option point-et-clic**

Si vous êtes une personne visuelle, la Console de gestion AWS va vous sembler familière. La console est une interface basée sur le web qui vous permet de gérer vos ressources AWS à travers une série de tableaux de bord conviviaux et cliquables. Imaginez-la comme la « salle de contrôle » AWS, où vous pouvez lancer et gérer des services en quelques clics.

La Console AWS est idéale pour les débutants et ceux qui veulent une manière claire et intuitive d'explorer les services. Elle est également parfaite pour quiconque configure une infrastructure sans avoir besoin de connaissances techniques approfondies—aucune compétence en ligne de commande requise !

**Ce que vous pouvez faire avec la Console AWS** :

* Lancer et gérer des instances EC2 (serveurs virtuels)
    
* Configurer des buckets de stockage S3
    
* Configurer des rôles IAM (Identity and Access Management) pour la sécurité
    
* Accéder aux outils de facturation et de gestion des coûts pour surveiller votre budget
    

**Idéal pour** : Les apprenants visuels, les débutants et quiconque préfère une approche simple et sans code pour gérer AWS.

#### 2\. **Interface de ligne de commande AWS (CLI) : Pour les amateurs de commandes**

Si vous êtes à l'aise avec la saisie de commandes, l'AWS CLI est votre meilleur ami. L'AWS CLI est un outil en ligne de commande qui vous permet de gérer les services AWS via des commandes tapées dans votre terminal ou invite de commande. C'est une option puissante pour ceux qui préfèrent la vitesse et l'efficacité ou qui veulent automatiser des tâches sans dépendre d'une interface graphique.

Avec le CLI, vous pouvez scripter des flux de travail entiers, automatiser des processus et gérer des ressources depuis n'importe quel appareil avec un terminal. De plus, il est souvent plus rapide de taper une seule commande que de cliquer à travers plusieurs pages dans la console !

**Exemple de commande** :

```bash
aws ec2 describe-instances
```

Cette commande liste toutes vos instances EC2 en cours d'exécution. Avec quelques lignes de code, vous pouvez vérifier vos ressources, mettre à l'échelle des services ou même gérer des configurations complexes sans jamais ouvrir un navigateur.

**Idéal pour** : Les utilisateurs avancés, les développeurs, les administrateurs système et quiconque aime l'efficacité et l'automatisation.

#### 3\. **SDK AWS : Pour les codeurs et développeurs**

Si vous êtes un développeur qui souhaite intégrer les services AWS directement dans votre code, les SDK AWS (Software Development Kits) sont là pour vous aider. AWS propose des SDK pour plusieurs langages de programmation, comme Python, JavaScript, Java et Ruby, vous permettant d'interagir avec AWS depuis vos applications.

Les SDK sont comme des « plug-ins » AWS que vous ajoutez à votre code, vous permettant d'accéder aux services, d'automatiser des processus et de construire des applications qui communiquent directement avec les ressources AWS. Par exemple, avec le SDK AWS pour Python (Boto3), vous pouvez écrire du code pour télécharger des fichiers vers S3, exécuter des requêtes sur DynamoDB ou déclencher des fonctions Lambda.

**Exemple avec Boto3 en Python** :

```python
import boto3

s3 = boto3.client('s3')
s3.upload_file('file.txt', 'mybucket', 'file.txt')
```

En quelques lignes seulement, ce code télécharge un fichier vers un bucket S3. Plutôt cool, n'est-ce pas ?

**Idéal pour** : Les développeurs qui veulent intégrer la fonctionnalité AWS directement dans leurs applications.

#### **4\. AWS CloudFormation : Le constructeur de plans**

Si vous êtes intéressé par l'automatisation de la configuration et de la mise en place de l'infrastructure, AWS CloudFormation est l'outil qu'il vous faut. CloudFormation vous permet de créer un « plan » (un fichier JSON ou YAML) qui définit les ressources et configurations AWS que vous souhaitez. AWS utilise ensuite ce plan pour tout configurer pour vous, vous faisant économiser le temps et l'effort de le faire manuellement.

Avec CloudFormation, vous pouvez créer et gérer des « piles » de ressources—pensez aux instances EC2, aux buckets S3, aux bases de données, et plus encore—en écrivant un seul modèle. Cette configuration est idéale pour déployer des applications de manière cohérente et reproductible.

**Exemple de snippet CloudFormation** :

```yaml
Resources:
  MyBucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: 'my-example-bucket'
```

Ce code simple crée un bucket S3 nommé « my-example-bucket ». Une fois que vous avez configuré un modèle, vous pouvez le déployer encore et encore, ce qui facilite la réplication de l'infrastructure dans différents environnements.

**Idéal pour** : Les ingénieurs DevOps, les architectes et les équipes qui ont besoin d'une configuration d'infrastructure automatisée et reproductible.

#### **5\. API AWS : Accès direct pour une flexibilité ultime**

Si vous cherchez un contrôle total et un accès direct aux services AWS, les API AWS sont la solution. AWS propose des API pour presque tous les services, ce qui signifie que vous pouvez interagir avec AWS directement en effectuant des requêtes HTTP, sans avoir besoin de vous appuyer sur la Console AWS, le CLI ou les SDK.

Les API permettent aux développeurs d'appeler les services AWS de manière programmatique—envoyer des requêtes, récupérer des réponses et effectuer des opérations depuis n'importe quel environnement capable d'effectuer des requêtes HTTP. Elles sont parfaites pour construire des solutions personnalisées, automatiser des flux de travail et intégrer des services AWS dans des systèmes existants ou des applications tierces.

**Exemple d'appel API AWS** : En utilisant une requête HTTP, vous pouvez récupérer des informations sur un bucket S3 ou initier une fonction Lambda. Voici un exemple rapide de ce à quoi une requête API pourrait ressembler pour lister des objets dans un bucket S3 :

```plaintext
GET /mybucket?list-type=2 HTTP/1.1
Host: s3.amazonaws.com
Authorization: AWS4-HMAC-SHA256 ...
```

Avec les bonnes permissions et authentification, cet appel API vous permet de récupérer des données sur les objets dans un bucket S3 directement.

#### Avantages de l'utilisation des API AWS

* **Intégration directe** : Les API permettent d'accéder aux services AWS depuis n'importe quel système, langage ou plateforme prenant en charge les requêtes HTTP.
    
* **Léger et flexible** : Puisque les API ne nécessitent pas de SDK ou d'outils supplémentaires, elles constituent une option efficace et minimaliste.
    
* **Idéal pour l'automatisation** : Les API sont idéales pour créer des flux de travail personnalisés et automatiser les interactions avec les services AWS, en particulier pour les équipes DevOps ou les développeurs gérant des systèmes complexes.
    

**Idéal pour** : Les développeurs avancés, les intégrateurs de systèmes et les équipes ayant besoin de moyens personnalisés ou indépendants de la plateforme pour interagir avec AWS.

#### Tableau de comparaison

Voici un tableau mis à jour incluant les API AWS pour une référence plus facile :

| **Méthode d'accès** | **Idéal pour** | **Niveau de compétence** |
| --- | --- | --- |
| **Console AWS** | Apprenants visuels, débutants | Débutant à intermédiaire |
| **CLI AWS** | Utilisateurs avancés, administrateurs système, passionnés d'automatisation | Intermédiaire à avancé |
| **SDK AWS** | Développeurs intégrant AWS dans le code | Intermédiaire à avancé |
| **AWS CloudFormation** | DevOps, déploiements automatisés | Avancé |
| **API AWS** | Intégrations personnalisées, automatisation légère | Avancé |

## Calculatrice AWS

La calculatrice de tarification AWS [Calculatrice](https://calculator.aws/#/addService) n'est pas seulement un outil de budgétisation, c'est votre copilote cloud, vous aidant à explorer le potentiel d'AWS sans les surprises financières. Que vous expérimentiez avec une seule instance EC2 ou planifiiez une configuration multi-services à l'échelle de l'entreprise, cette calculatrice peut décomposer les coûts, projeter vos économies et vous donner l'esprit tranquille avec une vue d'ensemble de vos dépenses.

Alors, la prochaine fois que vous vous demandez : « Combien coûtera vraiment ce projet cloud ? », essayez la calculatrice AWS. Vous pourriez découvrir un moyen de réaliser de grandes choses dans le cloud sans étirer votre budget !

## Conclusion

Et voilà, un tour d'horizon du monde d'AWS et de ce qu'il peut signifier pour vous ou vos projets. Que vous vous lanciez à peine dans les eaux du cloud ou que vous planifiiez un empire multi-cloud, AWS offre des outils et une flexibilité pour soutenir votre parcours.

Alors, allez-y, prenez ce que vous avez appris ici, explorez, expérimentez et, surtout, amusez-vous avec ! Jusqu'à la prochaine fois, bon cloud computing ! 🌤🌏

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
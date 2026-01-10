---
title: Comment déployer une application React en production sur AWS avec Express,
  Postgres, PM2 et nginx
date: '2019-09-11T20:42:00.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/iqbal125/
originalURL: https://freecodecamp.org/news/production-fullstack-react-express
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca067740569d1a4ca4878.jpg
tags:
- name: AWS
  slug: aws
- name: React
  slug: react
seo_desc: "By Mohammad Iqbal\nIn this tutorial I will walk you through a fairly complex\
  \ production-level AWS deployment setup from scratch. I will assume very little\
  \ prior knowledge about AWS and assume you are a beginner. \nWe will setup a React\
  \ Express full sta..."
---


Dans ce tutoriel, je vais vous guider à travers une configuration de déploiement AWS de niveau production assez complexe en partant de zéro. Je partirai du principe que vous avez très peu de connaissances préalables sur AWS et que vous êtes débutant.

<!-- more -->

Nous allons mettre en place une application full stack React Express avec une base de données PSQL. Nous déploierons l'application sur une instance AWS EC2 exécutant une Amazon Linux AMI 2. La configuration utilisera NGINX comme reverse proxy et PM2 comme gestionnaire de cluster. La base de données PSQL sera déployée sur AWS RDS.

Nous resterons dans l'offre gratuite (free tier), donc suivre ce tutoriel ne vous coûtera rien.

**Pourquoi apprendre AWS ?**  
AWS est actuellement la plus grande plateforme de cloud computing. WordPress propulse davantage de petits sites web, mais AWS est utilisé par la grande majorité des sites commerciaux à fort trafic. Cela signifie que les personnes possédant des compétences AWS sont très demandées.

Vous pouvez regarder une version vidéo de ce tutoriel ici :  
[https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5][1]

**Commandes de terminal utiles :**  
[https://github.com/iqbal125/terminal\_commands\_fullstack][2]

**Exemple de projet React/Express :**  
[https://github.com/iqbal125/react-express-sample][3]

## Théorie

-   **Fonctionnement du réseau dans le cloud computing AWS**
-   **Instance AWS EC2**
-   **Adresses IP publiques vs privées**
-   **Adresses IPv4**
-   **Connexion à l'internet public depuis un réseau privé**
-   **Aperçu conceptuel d'AWS VPC**
-   **Fonctionnement du subnetting dans AWS**
-   **ssh**

## Pratique

-   **Déploiement EBS simple**
-   **Configuration du VPC et des sous-réseaux**
-   **Passerelles Internet (Internet Gateways) et tables de routage**
-   **Configuration des groupes de sécurité (Security Groups)**
-   **Lancement d'un ordinateur cloud avec AWS EC2**
-   **Configuration de la base de données sur AWS**
-   **Configuration du build React pour la production**
-   **Configuration de PM2**
-   **Configuration de Nginx**

## Théorie

Le Cloud Computing a considérablement simplifié le déploiement d'une application web. Des sites comme Digital Ocean et Heroku facilitent encore plus les choses en masquant toute la complexité et en vous permettant de déployer votre application en quelques étapes simples.

Ces outils sont bons, mais ce que nous voulons, c'est une configuration de cloud computing robuste, hautement sécurisée et performante, ce qui signifie que nous allons tout faire de zéro.

La configuration AWS impliquera principalement du réseau, c'est pourquoi la majeure partie de ce tutoriel se concentrera sur les concepts et les configurations réseau.

Tout le reste, comme le provisionnement des bases de données et des instances EC2, est facile à faire sur AWS ; le réseau sera le plus grand défi.

Mais ne vous inquiétez pas si vous n'avez aucune expérience en réseau. Je vous donnerai toutes les informations nécessaires.

### Fonctionnement du réseau dans le cloud computing

Cela fonctionne fondamentalement de la même manière que le réseau avec du matériel physique, sauf que tout ce qui est matériel (routeurs, commutateurs, passerelles internet) est virtualisé dans le cloud computing.

Le réseau dans le cloud computing détermine essentiellement comment vos ressources virtuelles communiquent entre elles et avec l'internet mondial.

Les VPC, les adresses IP et les sous-réseaux sont les concepts les plus importants à comprendre concernant le réseau dans AWS.

C'est essentiellement ce que nous allons construire.

![image-1](https://www.freecodecamp.org/news/content/images/2019/09/image-1.png)

Nous aurons un sous-réseau public et un privé dans notre VPC. Le sous-réseau public contiendra notre serveur web et sera accessible via internet. Notre sous-réseau privé contiendra notre base de données mais ne sera pas accessible via internet.

Notre serveur web et notre base de données pourront communiquer entre eux via une table de routage.

Nous verrons des exemples de ces deux éléments lors de la configuration de notre projet sur la console AWS.

### Adresses IP publiques vs privées

Une adresse IP publique est l'emplacement de votre ordinateur dans l'internet mondial. Cependant, ce que nous appelons internet n'est qu'un réseau parmi tant d'autres.

De la même manière que vous pouvez avoir une adresse IP sur internet, vous pouvez également avoir une adresse IP dans un autre réseau qui n'est pas internet.

Une adresse IP est simplement un moyen d'identifier un seul ordinateur sur un réseau, que ce réseau soit internet ou non.

Ainsi, les adresses IP privées sont simplement un moyen d'identifier les ordinateurs sur notre propre réseau et les adresses IP publiques sont un moyen d'identifier les ordinateurs sur le réseau "internet".

### IPv4

IPv4 est le format dans lequel les adresses IP sont écrites.

Exemple d'adresse IPv4 : 10.12.15.22

Appelé IPv4 car il y a 4 octets qui peuvent représenter l'adresse. Chaque octet contient 8 bits et est donc appelé un **octet**.

Puisque chaque octet contient 8 bits et que chaque bit peut être un 0 ou un 1, il y a 2 ^ 8 = 256 combinaisons différentes. Mais nous commençons à 0, donc un octet peut être un nombre entre 0 et 255. Comme nous avons 4 octets, nous avons 256 ^ 4 = 4,3 milliards de combinaisons différentes et donc d'adresses IP !

Une adresse IPv4 est résolue en un format lisible par l'homme : "[https://google.com][4]" via un DNS.

Il existe également l'IPv6, mais pour rester concis, nous ferons l'impasse dessus ; nous n'aurons besoin de connaître que l'IPv4 pour les besoins de ce tutoriel.

Plus d'infos sur l'IPv6 ici :  
[https://searchnetworking.techtarget.com/definition/IPv6-Internet-Protocol-Version-6][5]

### Connexion à un réseau public depuis un réseau privé

Cela se fait via une passerelle internet (internet gateway).

Lorsqu'une requête est faite par un ordinateur dans un réseau privé, une table de routage vérifie si la destination est pour un ordinateur local ou non.

Si ce n'est pas le cas, la requête est transmise à la passerelle internet qui l'envoie hors du réseau privé vers un fournisseur d'accès internet, d'où elle est ensuite envoyée à la destination prévue.

La passerelle internet reçoit également des requêtes provenant d'internet.

La passerelle internet possède sa propre adresse IP publique, ainsi un réseau peut avoir une seule adresse IP publique même s'il possède des milliers d'adresses IP privées.

Le protocole utilisé pour envoyer et recevoir des données est appelé TCP. C'est un modèle qui garantit l'intégrité et la fiabilité des données.

### VPC et Subnetting

Le VPC et le subnetting sont de loin les choses les plus difficiles à comprendre et à saisir dans AWS, c'est pourquoi je vais y consacrer une section plus longue.

**Virtual Private Cloud (VPC)** : Un emplacement virtuel dans lequel vous pouvez déployer des ressources AWS. Vous pouvez déployer des serveurs web, des bases de données, des serveurs de fichiers et des services de messagerie dans un VPC et avoir toutes vos ressources contenues dans un seul endroit virtuel.

Chaque ressource possède sa propre adresse IP privée.

Un **sous-réseau (subnet)** est l'abréviation de sous-réseau ou une petite partie de votre VPC complet. Le subnetting est essentiellement un moyen de diviser votre VPC pour des raisons de performance et de sécurité.

**Exemple :** Déployer une base de données dans un sous-réseau inaccessible par internet, tandis qu'un autre sous-réseau contenant les serveurs web devra être accessible par internet. Même si ces deux sous-réseaux sont séparés, ils font toujours partie du même VPC.

Le subnetting dans AWS se fait avec la notation CIDR.

**Exemple de notation CIDR de sous-réseau :** 10.11.12.0/24

**Masque de sous-réseau**  
Le masque de sous-réseau détermine le nombre d'adresses IP disponibles pour le sous-réseau. Le /24 est le masque de sous-réseau.

Un masque de sous-réseau est utilisé comme moyen de diviser votre sous-réseau en un nombre approximatif d'adresses IP.

**Préfixe réseau** : Les octets de début immuables qui identifient un sous-réseau ou un VPC unique.

**Adresse hôte** : Les adresses IP disponibles pour être utilisées par les différentes ressources d'un sous-réseau.

/24 signifie que les 24 premiers bits doivent être utilisés comme préfixe réseau et sont donc inutilisables pour les hôtes. Puisqu'une adresse IPv4 possède 32 bits au total, il nous reste 8 bits, connus sous le nom d'adresse hôte. Ce sont les adresses IP utilisables. Comme 8 bits offrent 256 combinaisons, notre sous-réseau peut avoir n'importe quelle adresse comprise entre 10.11.12.0 et 10.11.12.255.

Les 1 représentent le préfixe réseau et les 0 représentent l'adresse hôte.

/24 = 255.255.255.0 = 11111111.11111111.11111111.00000000

**Identique :**

10.11.12.0/24

10.11.12.0/255.255.255.0

10.11.12.0/11111111.11111111.11111111.00000000

Un sous-réseau ne doit pas nécessairement se diviser uniformément en octets.

10.11.12.0 /19 signifie un masque de sous-réseau de 11111111.11111111.11100000.00000000.

Si nous utilisons un calculateur de sous-réseau, nous pouvons voir comment cela fonctionne. Un calculateur de sous-réseau vous donne le nombre d'adresses IP disponibles dans un sous-réseau, ainsi que l'adresse IP minimale et maximale.

![image-71](https://www.freecodecamp.org/news/content/images/2019/09/image-71.png)

Comme vous pouvez le voir, ce sous-réseau nous donne 8190 adresses IP utilisables au total.

Les 2 premiers octets sont tous des 1, donc les deux octets sont utilisés comme préfixe réseau, et ils peuvent être n'importe quel nombre entre 0 et 255.

Mais notre troisième octet n'a qu'un préfixe réseau partiel et nous n'avons que 5 bits à utiliser comme adresse hôte. Cela signifie que le troisième octet ne peut être qu'un nombre entre 0 et 31 puisque 2 ^ 5 = 32.

Notre dernier octet est tout à 0, donc comme d'habitude, il peut être n'importe quel nombre entre 0 et 255.

Tout cela signifie que notre sous-réseau peut être n'importe quelle adresse comprise entre :

10.11.0.0 - 10.11.31.255

\*\*Note : La première et la dernière adresse IP sont utilisées comme adresses de réseau et de diffusion (broadcast), qui sont des adresses IP spéciales avec des fonctions spécifiques. C'est pourquoi l'hôte min est la deuxième adresse IP et l'hôte max est l'avant-dernière adresse IP.

Vous pouvez en apprendre plus sur les adresses réseau et de diffusion ici :

[https://www.computernetworkingnotes.com/ccna-study-guide/network-address-basic-concepts-explained-with-examples.html][6]

Pour éviter toute la complexité mentionnée ci-dessus, il est préférable de s'en tenir aux masques de sous-réseau de /8, /16 ou /24. Cela garantira qu'il n'y a pas d'octets partiels.

10.11.12.0/8 aura les 3 derniers octets entiers disponibles comme adresses IP.

10.11.12.0/16 aura les 2 derniers octets entiers disponibles comme adresses IP.

10.11.12.0/24 aura le dernier octet entier disponible comme adresses IP.

Exemple réel  
**VPC :** 10.11.0.0/16

**Sous-réseau public 1 :** 10.11.1.0/24, toute adresse IP entre 10.11.1.0 et 10.11.1.255  
**Sous-réseau public 2 :** 10.11.2.0/24, toute adresse IP entre 10.11.2.0 et 10.11.2.255

**Sous-réseau privé 1 :** 10.11.3.0/24, toute adresse IP entre 10.11.3.0 et 10.11.3.255  
**Sous-réseau privé 2 :** 10.11.4.0/24, toute adresse IP entre 10.11.4.0 et 10.11.4.255

\*\*Note : Toutes les adresses IP ne seront pas disponibles pour votre sous-réseau. Quelques adresses comme les adresses réseau et de diffusion, ainsi que quelques adresses utilitaires supplémentaires, seront réservées par AWS.

### AWS EC2

C'est le "computing" dans le cloud computing. C'est essentiellement un ordinateur virtuel. Il possède tout ce que votre ordinateur à la maison possède : CPU, RAM, disque dur, etc.

Ce sera essentiellement notre serveur web et nous utiliserons l'Amazon Linux AMI 2 comme système d'exploitation.

Il existe également d'autres systèmes d'exploitation Linux disponibles tels qu'Ubuntu et Red Hat.

Il existe également des systèmes d'exploitation basés sur Windows tels que Windows Server. Les systèmes Windows vous permettent d'utiliser une interface graphique si vous préférez ne pas travailler avec la ligne de commande.

Un seul ordinateur EC2 est appelé une instance.

### SSH

**Secure Shell :** utilisé pour se connecter à notre serveur Linux EC2 depuis notre ordinateur personnel.

Vous pouvez utiliser Putty pour le SSH si vous préférez une interface utilisateur graphique.

J'utiliserai Git Bash. C'est plus simple à utiliser mais n'a pas d'interface graphique.

Nous utiliserons le SSH avec des clés privées et publiques. Ces deux clés sont générées par AWS.

La clé privée sera stockée sur votre propre ordinateur et sera utilisée pendant le processus de connexion.

La clé publique sera stockée sur Amazon et permettra les connexions. La clé publique n'a pas besoin d'être gardée secrète. La clé privée doit être conservée dans un endroit sûr sur votre ordinateur ; vous seriez en difficulté si vous la supprimiez accidentellement, car il n'y a aucun moyen d'en obtenir une autre.

## Pratique

**Déploiement EBS simple**

Avant de passer à notre déploiement complexe, nous pouvons effectuer un déploiement EBS simple pour nous mettre dans le bain.

AWS Elastic Beanstalk est un moyen de lancer une application dans le Cloud sans avoir à configurer manuellement les ressources sous-jacentes telles que le VPC, le serveur web et la base de données. Il est très facile et rapide d'obtenir une application fonctionnelle sur AWS ELB et c'est un bon moyen de se familiariser avec AWS.

![image-5](https://www.freecodecamp.org/news/content/images/2019/09/image-5.png)

Allez sur la page d'accueil d'AWS et créez un nouveau compte si vous n'en avez pas déjà un.

![image-6](https://www.freecodecamp.org/news/content/images/2019/09/image-6.png)

Allez ensuite dans Services puis ElasticBeanstalk sous Calcul (Compute).

![image-7](https://www.freecodecamp.org/news/content/images/2019/09/image-7.png)

Ce qui vous amènera à la page d'accueil d'EBS. Après cela, cliquez sur Create New Application, puis donnez-lui un nom et une description.

![image-8](https://www.freecodecamp.org/news/content/images/2019/09/image-8.png)

Vous pouvez ensuite cliquer sur Create New Environment et sélectionner Web Server Environment.

![image-9](https://www.freecodecamp.org/news/content/images/2019/09/image-9.png)

Sur cette page, sélectionnez Node.js comme plateforme et utilisez le code Sample Application, tout le reste peut être laissé par défaut.

Je n'ai pas eu de chance en déployant l'application directement d'ici, alors cliquons sur Configure more options pour configurer un peu plus le projet.

![image-10](https://www.freecodecamp.org/news/content/images/2019/09/image-10.png)

Cliquez sur la carte Network en bas de la page et assurez-vous que le VPC par défaut est utilisé et que la case du sous-réseau par défaut est cochée.

Cliquez ensuite sur la carte Instances et assurez-vous que la case des groupes de sécurité par défaut est cochée.

![image-11](https://www.freecodecamp.org/news/content/images/2019/09/image-11.png)

Et c'est tout, nous pouvons maintenant cliquer sur create environment pour lancer notre application.

Si cela a fonctionné, vous devriez voir "successfully launched environment" sur votre écran.

![image-12](https://www.freecodecamp.org/news/content/images/2019/09/image-12.png)

Et si vous cliquez sur l'URL, vous pouvez voir votre application déployée.

![image-13](https://www.freecodecamp.org/news/content/images/2019/09/image-13.png)

Félicitations pour le déploiement d'une application sur le Cloud AWS !

\*\*Important : Assurez-vous de nettoyer vos ressources pour ne pas être facturé par AWS.

Pour nettoyer, cliquez simplement sur Terminate Environment sous actions, ce qui supprimera l'application ainsi que toutes les ressources sous-jacentes.

![image-14](https://www.freecodecamp.org/news/content/images/2019/09/image-14.png)

Nous pouvons maintenant passer à la configuration complexe.

### Configuration du VPC

Tout d'abord, nous pouvons aller sur le tableau de bord VPC qui se trouve dans la section Network & Content Delivery.

![image-15](https://www.freecodecamp.org/news/content/images/2019/09/image-15.png)

Vous devriez maintenant être sur le tableau de bord VPC. Vous pouvez créer un VPC avec le bouton Launch VPC Wizard, ce qui est un peu plus facile, mais je vais vous montrer comment le configurer de zéro, ce qui est un peu plus difficile mais vous donnera une meilleure compréhension du fonctionnement d'un VPC.

Cliquez d'abord sur l'onglet VPCs et cliquez sur le bouton Create VPC, ce qui vous amènera à une page ressemblant à ceci.

![image-16](https://www.freecodecamp.org/news/content/images/2019/09/image-16.png)

Nous pouvons nommer le VPC : VPC 3.

Nous pouvons définir le bloc CIDR à 10.11.0.0/16. Si vous vous souvenez des sections théoriques sur le VPC et les sous-réseaux, cela signifie que les 2 premiers octets sont le préfixe réseau et les 2 derniers octets sont l'adresse hôte, et sont disponibles pour notre usage.

Tenancy signifie si le VPC sera sur son propre matériel dédié ou non. On pense parfois que le Dedicated Tenancy est plus sécurisé ou offre de meilleures performances, mais aucune donnée ne le suggère.

Default tenancy signifie que votre VPC partagera le matériel sous-jacent avec d'autres utilisateurs AWS mais sera isolé d'eux par logiciel.

Après cela, nous pouvons cliquer sur create VPC, ce qui terminera notre configuration VPC.

### Configuration des sous-réseaux

Ensuite, nous allons configurer les sous-réseaux. Nous pouvons commencer par cliquer sur l'onglet Subnets et cliquer sur create subnet.

Nous allons d'abord créer notre sous-réseau public comme ceci :

![image-17](https://www.freecodecamp.org/news/content/images/2019/09/image-17.png)

La chose principale à noter est le bloc CIDR IPv4, qui est 10.11.1.0/24.

10.11 est notre préfixe réseau immuable provenant de notre VPC. Ce qui fait que .1 fait également partie du préfixe réseau puisque le masque de sous-réseau est /24 et .1 est également l'identifiant de ce sous-réseau.

Le dernier octet sert alors d'adresse hôte, ce qui signifie que ce sous-réseau peut avoir n'importe quelle adresse entre 10.11.1.0 et 10.11.1.255.

Après cela, nous pouvons cliquer sur create, ce qui créera le sous-réseau et l'affichera dans la liste des sous-réseaux.

Maintenant pour notre sous-réseau privé :

![image-18](https://www.freecodecamp.org/news/content/images/2019/09/image-18.png)

Il est configuré de manière similaire au sous-réseau public, la différence principale étant qu'il a un .2 au lieu d'un .1 dans le 3ème octet. De plus, nous devons spécifier une zone de disponibilité (availability zone) pour que ce sous-réseau fonctionne avec notre base de données.

En gros, 10.11 est le préfixe réseau que nous avons obtenu du VPC. .2 est le 3ème octet et l'identifiant unique de ce sous-réseau, et le dernier octet .0 représente les adresses IP disponibles entre 0 et 255.

Cela signifie donc que ce sous-réseau peut avoir n'importe quelle adresse IP de 10.11.2.0 à 10.11.2.255.

Si vous comparez cela à notre sous-réseau public qui a une plage d'adresses IP de 10.11.1.0 à 10.11.1.255, le modèle de configuration du sous-réseau devrait être beaucoup plus clair.

Le déploiement d'une base de données sur AWS nécessite 2 sous-réseaux dans des zones de disponibilité différentes, vous pouvez donc configurer le second comme ceci.

![image-19](https://www.freecodecamp.org/news/content/images/2019/09/image-19.png)

### Passerelles Internet et tables de routage

Les **tables de routage (route tables)** sont essentiellement des routeurs et déterminent comment et où le trafic est dirigé.

Nous pouvons maintenant créer une passerelle internet (internet gateway) que nous attacherons à notre sous-réseau public.

![image-20](https://www.freecodecamp.org/news/content/images/2019/09/image-20.png)

Comme toutes les passerelles internet fonctionnent de la même manière, nous n'avons qu'à définir le nom. Avant de pouvoir attacher cette passerelle internet à notre sous-réseau, nous devons d'abord configurer la table de routage.

Nous pouvons aller dans l'onglet route tables et cliquer sur create route table.

Nous n'avons qu'à définir le nom et l'associer au VPC. Nous pouvons l'associer au VPC 3 et cliquer sur create.

![image-21](https://www.freecodecamp.org/news/content/images/2019/09/image-21.png)

Une fois cela fait, nous pouvons maintenant attacher notre passerelle internet à ce VPC. Retournons dans l'onglet internet gateway, cliquons sur le bouton actions, puis sur attach to VPC.

Pour l'option d'attachement, sélectionnez simplement VPC 3.

Ensuite, nous pouvons retourner à notre table de routage que nous avons configurée et ajouter une route. Nous pouvons ajouter la route comme ceci :

![image-22](https://www.freecodecamp.org/news/content/images/2019/09/image-22.png)

Cela signifie que si une requête est faite, la table de routage vérifie d'abord si la route est pour une route locale 10.11.0.0/16, sinon nous transmettons cette requête à la passerelle internet pour toutes les autres routes, ce qui est représenté par 0.0.0.0/0.

Ensuite, nous pouvons cliquer sur l'onglet subnet associations puis sur le bouton edit subnet associations.

![image-23](https://www.freecodecamp.org/news/content/images/2019/09/image-23.png)

Nous voulons seulement que le sous-réseau public soit associé à cette table de routage, donc nous ne cochons que celui-ci, puis nous pouvons cliquer sur save.

Et nous ne pouvons pas oublier nos sous-réseaux privés. Créez simplement une autre table de routage et associez-y les sous-réseaux privés de la même manière que nous l'avons fait pour le sous-réseau public. N'ajoutez pas de passerelle internet, laissez simplement la table de routage pour les cibles locales.

### Groupes de sécurité

Les **groupes de sécurité (security groups)** sont essentiellement des pare-feu qui filtrent le trafic entrant et sortant.

Nous devons maintenant configurer les groupes de sécurité pour qu'ils fonctionnent avec cette installation. Cliquez sur l'onglet security groups et cliquez sur create security group.

La création du groupe de sécurité est très facile, nous pouvons simplement définir le nom et la description, puis l'associer à notre VPC 3.

Après avoir créé les groupes de sécurité, cliquez sur edit inbound rules.

![image-24](https://www.freecodecamp.org/news/content/images/2019/09/image-24.png)

Ensuite, nous pouvons configurer les règles de sécurité comme ceci :

![image-25](https://www.freecodecamp.org/news/content/images/2019/09/image-25.png)

Tout d'abord, nous avons SSH, qui est la façon dont nous nous connectons à notre instance EC2 depuis notre ordinateur personnel. J'ai laissé la source à 0.0.0.0/0 parce que je ne veux pas mettre mon adresse IP personnelle, mais dans une application réelle, vous voudrez mettre votre propre adresse IP ici.

Après cela, nous avons les ports normaux 80 et 443 qui permettent le trafic normal via internet. ::/0 permet tout le trafic IPv6 ainsi que l'IPv4.

### Lancement d'une instance EC2

Tout d'abord, allons sur le tableau de bord EC2 et cliquons sur launch instance. Ensuite, nous pouvons sélectionner l'Amazon Linux AMI comme système d'exploitation.

![image-26](https://www.freecodecamp.org/news/content/images/2019/09/image-26.png)

Ensuite, pour rester dans l'offre gratuite, sélectionnez l'option t.2 micro pour le type d'instance (Instance type).

Puis, pour la 3ème étape, nous devons configurer les détails de l'instance, ce que nous pouvons faire comme ceci :

![image-27](https://www.freecodecamp.org/news/content/images/2019/09/image-27.png)

Pour le réseau (network), nous pouvons sélectionner notre VPC 3 et pour notre sous-réseau, nous pouvons sélectionner notre sous-réseau public. Puisqu'il s'agit de notre serveur web, nous voulons qu'il soit dans notre sous-réseau public attaché à une passerelle internet.

L'ajout de tags et l'ajout de stockage peuvent être laissés par défaut.

Pour la sécurité, assurez-vous d'ajouter le groupe de sécurité du serveur web que nous avons configuré dans la section précédente.

Enfin, à la dernière étape, nous pouvons simplement cliquer sur launch.

Cela affichera une fenêtre contextuelle nous proposant une paire de clés (keypair). Nous pouvons sélectionner create new key pair puis télécharger la paire de clés.

![image-28](https://www.freecodecamp.org/news/content/images/2019/09/image-28.png)

Si cela est fait correctement, vous devriez voir ceci sur votre écran.

![image-29](https://www.freecodecamp.org/news/content/images/2019/09/image-29.png)

Après cela, notre instance est lancée et disponible pour que nous puissions nous y connecter en SSH. Nous pouvons nous connecter à notre instance avec la commande :

`ssh i- “keypair.pem” ec2-user@public-ip-address`

### Configuration de la base de données

Configurons maintenant la base de données. Nous pouvons commencer par aller dans l'onglet RDS sous la section database, dans les services. Cela nous amènera au tableau de bord de la base de données RDS.

![image-30](https://www.freecodecamp.org/news/content/images/2019/09/image-30.png)

Mais avant de pouvoir créer une base de données, nous devons d'abord créer un groupe de sous-réseaux (subnet group). Pour commencer, nous pouvons aller dans l'onglet subnet groups et cliquer sur create db subnet group.

Un groupe de sous-réseaux de base de données est là pour protéger contre tout type de défaillance complète du serveur ou de suppression accidentelle, c'est pourquoi il s'étend sur 2 zones de disponibilité. Dans le cas peu probable où un serveur échouerait complètement dans une zone de disponibilité, votre base de données serait toujours en sécurité. Il est extrêmement improbable que les deux serveurs échouent complètement dans 2 zones de disponibilité différentes en même temps.

Nous définissons d'abord le nom et la description. Ensuite, nous associons notre VPC 3 au groupe de sous-réseaux. Après cela, nous pouvons ajouter nos sous-réseaux.

![image-31](https://www.freecodecamp.org/news/content/images/2019/09/image-31.png)

Les sous-réseaux seront listés sous la zone de disponibilité dans laquelle nous les avons configurés dans la section précédente. Ensuite, nous pouvons simplement cliquer sur create.

Après avoir créé le groupe de sous-réseaux, nous sommes prêts à créer notre base de données réelle.

Nous pouvons d'abord sélectionner "free tier eligible" en bas.

![image-32](https://www.freecodecamp.org/news/content/images/2019/09/image-32.png)

Nous pouvons ensuite cliquer sur next. Nous pouvons laisser tout le reste sur la page suivante aux paramètres par défaut. Assurez-vous de vous souvenir du nom d'utilisateur et du mot de passe que vous avez définis ici.

Sur la page suivante, nous pouvons définir le VPC sur notre VPC 3, le groupe de sous-réseaux sur celui que nous venons de configurer.

Assurez-vous également de laisser "publicly accessible" sur no. Pour des raisons de sécurité évidentes, nous ne voulons pas que notre application soit disponible via internet.

Tout le reste peut être laissé par défaut. Nous configurerons nos groupes de sécurité de base de données dans un instant.

![image-33](https://www.freecodecamp.org/news/content/images/2019/09/image-33.png)

Maintenant, nous pouvons cliquer sur create database et nous pouvons créer les groupes de sécurité de la base de données pendant que la base de données est en cours de création.

Nous pouvons aller dans l'onglet security groups du tableau de bord VPC et créer un nouveau groupe de sécurité comme nous l'avons vu précédemment. Pour les règles entrantes, nous pouvons les limiter à la plage CIDR de notre serveur web, avec le port défini sur le port par défaut 5432 de PSQL.

![image-34](https://www.freecodecamp.org/news/content/images/2019/09/image-34.png)

Cliquez sur create et nous sommes prêts à ajouter ceci à notre base de données.

Pour ajouter ce nouveau groupe de sécurité, nous pouvons aller à la base de données depuis le tableau de bord de la base de données. Cliquez ensuite sur le bouton modify.

Après cela, nous pouvons simplement sélectionner le groupe de sécurité que nous venons de configurer sous la section Networking and Security.

Une question que vous pourriez vous poser maintenant est comment nous nous connectons à notre base de données si elle n'est pas accessible publiquement via internet.

La façon dont nous procédons est que nous nous connectons d'abord en SSH à notre instance Linux, puis nous nous connectons à notre base de données depuis cette instance via le port TCP PSQL que nous avons configuré sur notre table de routage.

![image-35](https://www.freecodecamp.org/news/content/images/2019/09/image-35.png)

Pour tester cela, nous pouvons nous connecter en SSH à notre instance EC2 de la même manière que nous l'avons vu ci-dessus. Ensuite, nous pouvons installer psql avec la commande :

`sudo amazon-linux-extras install postgresql9.6`

Après cela, nous pouvons nous connecter à la base de données psql avec la commande suivante :

`psql -d name-of-db -h host-name -p port -U username`

Si vous vous êtes connecté avec succès, vous verrez le nom de votre base de données suivi d'une flèche.

![image-36](https://www.freecodecamp.org/news/content/images/2019/09/image-36.png)

### Configuration du projet React et Node

Ici, je vais passer en revue une configuration d'exemple avec React et Node/Express. La toute première chose à faire est d'exécuter la commande `npm run build` qui générera un build de production de votre application dans un répertoire appelé **build.**

\*\*Note : Assurez-vous que toutes les routes qui sont localhost dans votre version de build sont changées pour l'IP publique. Ce sera probablement le cas pour l'authentification. Tout le reste peut être laissé tel quel.

Coupez et collez tout ce répertoire build dans un serveur Node/Express. Ensuite, définissez un chemin vers celui-ci comme indiqué ci-dessous.

```javascript
....
//serveur express

app.use(express.static(path.join(__dirname, 'build')));

if(process.env.NODE_ENV === 'production') {
  app.get('/*', function (req, res) {
   	res.sendFile(path.join(__dirname, 'build', 'index.html'));
  });
}

....
```

La première fonction est la façon dont nous servons les fichiers statiques de notre application React (les fichiers JS, CSS, PWA).

La deuxième fonction vérifie d'abord si l'environnement est en production, puis sert le fichier HTML principal de React.

Cette approche maintient intact notre routage côté client. Par exemple, dans notre build de développement, nous pouvons simplement utiliser des routes telles que /post/22 et elles seront correctement routées vers http://localhost:3000/post/22.

Mais parce que notre application React est maintenant en production, servie par un serveur Express, la route /post/22 pointerait vers http://publicip/build/post/22. Afin de ne pas réécrire tout notre routage, nous utilisons path.join() et le code ci-dessus pour corriger cela.

Après cela, déployez simplement le projet React Express sur un dépôt GitHub.

Et c'est tout, nous pouvons ensuite déployer cette application React Express sur un serveur Linux.

### Déploiement du projet sur une instance AWS EC2

Nous sommes maintenant prêts à déployer notre projet. Connectez-vous d'abord en SSH à votre instance EC2 avec Gitbash en utilisant la commande suivante :

`ssh i- “keypair.pem” ec2-user@public-ip-address`

La prochaine chose que nous devons faire est d'installer git avec la commande :

`sudo yum install git`

Ensuite, nous pouvons cloner le projet sur le serveur avec la commande :

`sudo git clone link-to-repo`

Après avoir fait cela, vous devriez pouvoir voir vos fichiers de projet en faisant un cd dans le répertoire.

![image-62](https://www.freecodecamp.org/news/content/images/2019/09/image-62.png)

Nous n'avons pas encore fini, nous devons encore installer node et npm, car nous voudrons installer les dépendances de notre projet. Nous devons d'abord installer le gestionnaire de versions node (nvm) qui nous permettra ensuite d'installer node et npm. Nous pouvons installer nvm comme ceci :

`sudo curl https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash`

Cela installera nvm que nous pourrons ensuite utiliser pour installer node et npm. Pour ce faire, listez simplement les versions de node disponibles au téléchargement et installez la dernière version stable.

Commande pour lister les versions de node :  
`nvm ls remote`

Commande d'installation :  
`nvm install version-of-node`

Mais après avoir installé npm et node, si vous essayez d'exécuter npm install dans le répertoire du projet, vous obtiendrez une erreur de permission refusée.

![image-63](https://www.freecodecamp.org/news/content/images/2019/09/image-63.png)

Vous pouvez alors exécuter la commande ci-dessous pour donner la permission d'écriture sur le répertoire. La commande ci-dessous donne bien plus que de simples permissions d'écriture, mais la configuration des permissions Linux dépasse largement le cadre de ce tutoriel.

`sudo chmod 777` sur le répertoire

Voici un lien vers un tutoriel si vous souhaitez en savoir plus sur chmod :  
[https://www.computerhope.com/unix/uchmod.htm][7]

Après cela, vos modules npm devraient s'installer normalement avec la commande npm install habituelle.

Ensuite, vous pouvez simplement lancer votre application avec la commande npm start qui démarrera votre serveur node et servira votre projet React en tant que fichiers statiques.

Mais le problème est que le projet ne s'exécutera que sur des ports non traditionnels comme 5000 ou 3000, ou n'importe quel port que vous utilisiez sur localhost. Si vous essayez l'approche naïve et changez simplement le port pour le port 80 sur le serveur, vous obtiendrez une erreur de permission refusée.

![image-64](https://www.freecodecamp.org/news/content/images/2019/09/image-64.png)

Pour corriger cela, nous utiliserons nginx.

### nginx

Vous vous demandez peut-être pourquoi nous utilisons nginx si nous avons déjà node. Il est possible d'utiliser nginx comme serveur HTTP, mais nous utiliserons nginx comme reverse proxy à la place, ce qui maintiendra node comme le véritable serveur HTTP.

La configuration ressemblera à ceci :

![image-68](https://www.freecodecamp.org/news/content/images/2019/09/image-68.png)

Les avantages de procéder ainsi sont :

-   nginx agit comme un équilibreur de charge (load balancer) au niveau de l'application
-   Aide node pour la performance et la fiabilité
-   Améliore la sécurité
-   Prévient les attaques DoS

Et voici un schéma qui montre un proxy classique par rapport à un reverse proxy.

![image-69](https://www.freecodecamp.org/news/content/images/2019/09/image-69.png)

Dans un proxy classique, un client web peut envoyer et recevoir des données de plusieurs serveurs web. Dans un reverse proxy, un seul serveur web peut envoyer et recevoir des données de plusieurs clients web.

Passons maintenant à notre instance EC2 et connectons-nous y en SSH.

La toute première chose que nous devrons faire est d'installer nginx. L'Amazon Linux AMI 2 est déjà livrée avec nginx, vous pouvez donc l'installer comme ceci :

`sudo amazon-linux-extras install nginx1.12`

Ensuite, nous pouvons faire un cd dans le répertoire nginx avec :

`cd /etc/nginx`

Ensuite, nous pouvons éditer le fichier de configuration nginx avec la commande :

`sudo nano nginx.conf`

Ce qui ouvrira le fichier nginx.conf dans l'éditeur sudo nano.

![image-65](https://www.freecodecamp.org/news/content/images/2019/09/image-65.png)

Ensuite, nous pouvons ajouter ce code à la route de l'emplacement racine (home location route) :

![image-66](https://www.freecodecamp.org/news/content/images/2019/09/image-66.png)

En gros, nous disons de définir le build React comme la route racine. Ensuite, définissez le fichier index.html comme index principal, et enfin, sur chaque requête suivante, servez le même fichier index.html.

C'est parce que React est une application monopage (SPA) et littéralement un seul fichier HTML. Donc, pour rendre possible la navigation au sein de l'application React, nous devons servir ce même fichier HTML à nouveau en cas d'erreurs.

Ensuite, nous pouvons également configurer nginx pour gérer nos routes API.

![image-67](https://www.freecodecamp.org/news/content/images/2019/09/image-67.png)

C'est principalement du code générique (boilerplate), mais la propriété à noter est le proxy\_pass qui est notre IP publique et le port non standard.

Cette adresse IP va ensuite être proxifiée vers le port 80 normal, ce qui nous permettra d'accéder au site web normalement.

Version copiable du code :

```
    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  localhost;


        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
                root /react-prod5/build;
                index index.html;                
                try_files $uri /index.html;

        }

        location /api/ {
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
                proxy_set_header X-NginX-Proxy true;
                proxy_pass http://10.0.1.187:3000;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection 'upgrade';
                proxy_set_header Host $host;
                proxy_cache_bypass $http_upgrade;

        }
```

Après cela, nous pouvons simplement sauvegarder et quitter l'éditeur.

Maintenant, nous devons également redémarrer nginx pour que les changements soient pris en compte.

`sudo systemctl restart nginx`

C'est tout ce que vous avez à faire pour avoir nginx comme reverse proxy. Votre application pourra désormais s'exécuter sur le port 80 normal.

### PM2

PM2 est un gestionnaire de cluster et nous permet d'exécuter notre application automatiquement et aussi de la redémarrer automatiquement si elle plante.

Connectons-nous donc à nouveau en SSH à notre instance et installons PM2 :

`npm install pm2 -g`

Le drapeau -g est important car il installe PM2 globalement. Et c'est crucial car c'est ce qui permet à PM2 de faire son travail.

Si vous y réfléchissez, si PM2 était installé localement, il planterait quand notre application planterait, donc cela ne fonctionnerait pas. Nous l'installons globalement pour qu'il soit en dehors de notre projet et puisse redémarrer notre projet s'il plante.

Ensuite, vous pouvez lancer PM2 sur votre projet avec :

`pm2 start app.js -i max`

Cela démarrera le projet avec le nombre maximum de cœurs. C'est important car node est monothreadé et l'utilisation de tous les cœurs maximisera les performances.

Si cela est fait avec succès, vous devriez voir une page qui ressemble à ceci :

![image-70](https://www.freecodecamp.org/news/content/images/2019/09/image-70.png)

Voici quelques autres commandes utiles pour PM2 :

`pm2 list` : liste tous les processus en cours d'exécution

`pm2 stop app 0` : arrête l'application avec l'id 0

`pm2 delete app 0` : supprime l'application avec l'id 0

`pm2 restart app 0` : redémarre l'application avec l'id 0

`pm2 start app.js -i max` : démarre app.js avec le nombre maximum de threads disponibles

Et voilà ! Merci d'avoir lu et félicitations si vous êtes arrivé au bout de ce tutoriel — ce n'est pas chose facile.

> Connectez-vous avec moi sur Twitter pour plus de mises à jour sur les futurs tutoriels : [https://twitter.com/iqbal125sf][8]

[1]: https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5
[2]: https://github.com/iqbal125/terminal_commands_fullstack
[3]: https://github.com/iqbal125/react-express-sample
[4]: https://google.com
[5]: https://searchnetworking.techtarget.com/definition/IPv6-Internet-Protocol-Version-6
[6]: https://www.computernetworkingnotes.com/ccna-study-guide/network-address-basic-concepts-explained-with-examples.html
[7]: https://www.computerhope.com/unix/uchmod.htm
[8]: https://twitter.com/iqbal125sf
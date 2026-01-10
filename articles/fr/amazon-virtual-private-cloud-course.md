---
title: Cours Amazon Virtual Private Cloud
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-13T21:00:37.000Z'
originalURL: https://freecodecamp.org/news/amazon-virtual-private-cloud-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/vpc2.png
tags:
- name: AWS
  slug: aws
- name: youtube
  slug: youtube
seo_title: Cours Amazon Virtual Private Cloud
seo_desc: Amazon Virtual Private Cloud is a service that lets you launch AWS resources
  in a logically isolated virtual network that you define. You get complete control
  over the networking environment including IP address ranges, subnets, routing, firewalls
  an...
---

Amazon Virtual Private Cloud est un service qui vous permet de lancer des ressources AWS dans un réseau virtuel logiquement isolé que vous définissez. Vous obtenez un contrôle complet sur l'environnement réseau, y compris les plages d'adresses IP, les sous-réseaux, le routage, les pare-feu et plus encore.

Nous venons de publier un cours complet sur Amazon Virtual Private Cloud sur la chaîne YouTube de freeCodeCamp.org.

Neal Davis a développé le cours. Il est le fondateur de Digital Cloud Training et possède une grande expérience avec AWS.

Dans ce tutoriel AWS, vous apprendrez AWS Virtual Private Cloud (Amazon VPC) depuis le niveau débutant jusqu'aux concepts avancés. Vous serez un guru AWS VPC en un rien de temps !

Après avoir étudié la théorie en utilisant des diagrammes animés pour aider à expliquer les concepts, vous pourrez apprendre en pratiquant avec de nombreuses leçons pratiques.

Voici toutes les sections de ce cours :

* Primer sur l'adressage IPv4
* Vue d'ensemble d'Amazon VPC
* Définition des blocs CIDR VPC
* Assistant VPC
* Créer un VPC personnalisé avec des sous-réseaux
* Lancer des instances et tester le VPC
* Groupes de sécurité et ACL réseau
* Configurer les groupes de sécurité et les NACL
* Appairage Amazon VPC
* Configurer l'appairage VPC
* Points de terminaison VPC
* Créer un point de terminaison VPC
* VPN client AWS
* VPN site à site AWS
* AWS VPN CloudHub
* AWS Direct Connect (DX)
* Passerelle AWS Direct Connect
* AWS Transit Gateway
* Utilisation d'IPv6 dans un VPC
* Créer des journaux de flux VPC

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube de freeCodeCamp.org](https://youtu.be/g2JOHLHh4rI) (2 heures de visionnage).

%[https://youtu.be/g2JOHLHh4rI]

## Transcription

(généré automatiquement)

Amazon Virtual Private Cloud est un service qui vous permet de lancer des ressources AWS dans un réseau virtuel logiquement isolé que vous définissez.

Neil Davis enseigne ce cours.

Il a créé de nombreux cours populaires sur AWS et c'est un excellent enseignant.

Je suis Neil Davis de Digital Cloud Training.

Et dans cette vidéo pratique, vous allez apprendre Amazon Virtual Private Cloud VPC.

Dans AWS, un VPC est une portion logiquement isolée du cloud dans laquelle vous pouvez déployer vos propres ressources telles que des instances Amazon EC2. Le VPC est un sujet assez complexe.

Dans cette vidéo, je vais commencer au niveau débutant et vous emmener jusqu'à un niveau intermédiaire ou même expert. Vous apprendrez à définir vos propres plages d'adresses IP pour un VPC, à créer un VPC et à lancer des ressources dedans.

Vous apprendrez le routage et les groupes de sécurité VPC, les listes de contrôle d'accès réseau, et nous couvrirons également les connexions VPN, les connexions directes et bien plus encore.

Cette vidéo provient de mon tout nouveau cours AWS Certified Solutions Architect Associate.

Donc, si vous prévoyez de passer un examen de certification AWS, cette vidéo sera très, très utile pour vous.

Mais c'est bien pour toute personne qui veut apprendre Amazon VPC et le pratiquer.

Pour ceux qui veulent en apprendre encore plus.

Il y a quelques vidéos supplémentaires sur la chaîne YouTube Digital Cloud Training, y compris pour créer un VPN client et un VPN site à site, toutes deux des vidéos pratiques. Vous pouvez trouver les liens vers ces vidéos dans la description de cette vidéo.

Et vous trouverez également le téléchargement du cours, dont vous aurez besoin pour compléter les exercices pratiques de ce cours.

Maintenant, j'espère vraiment que vous apprécierez cette vidéo.

Et commençons tout de suite.

Salut les gars, dans cette leçon, je vais couvrir une introduction de base sur l'adressage IP.

Et nous parlons spécifiquement de la version quatre de l'IP, pas de la version six.

Je couvrirai la version six un peu plus tard dans cette section.

Maintenant, ce que je veux faire ici, c'est supposer que vous n'avez pas beaucoup de connaissances en adressage IP, voire aucune.

Et nous allons commencer par les bases.

Maintenant, c'est un sujet vraiment complexe.

Donc je ne vais aller que jusqu'à ce que vous devez savoir pour être compétent en travaillant avec Amazon VPC.

Et avec l'adressage IP en général avec AWS.

Maintenant, il y aura certaines parties du sujet où vous voudrez peut-être aller plus loin.

Et il y a beaucoup de ressources sur Internet pour le faire si vous le souhaitez.

Pour commencer la leçon, commençons par ce qu'est une adresse IP.

Maintenant, disons que nous avons un serveur web sur Internet, et vous voulez communiquer avec ce serveur web.

Maintenant, le serveur web est susceptible d'avoir une sorte d'interface réseau et attachée à cette interface réseau sera une adresse IP.

Et ce sera une adresse IP publique.

Dans ce cas, parce que le serveur web est disponible via Internet, les adresses IP sont les adresses que les ordinateurs utilisent pour communiquer entre eux.

Donc vous avez votre ordinateur à la maison, et vous avez un navigateur web ouvert.

Et vous tapez exemple.com, l'adresse de notre serveur web.

Maintenant, que se passe-t-il maintenant parce que vous avez mis exemple.com, mais comme je l'ai dit, les ordinateurs communiquent en utilisant des adresses IP.

Donc c'est là qu'un système de noms de domaine ou un serveur DNS intervient.

Votre ordinateur parlera à un serveur DNS.

Et il va demander à ce serveur DNS quelle est l'adresse IP pour exemple.com.

Une fois que votre ordinateur a le résultat, il est alors capable de se connecter au serveur web en utilisant l'adresse IP.

Donc c'est la résolution de noms principale, où vous résolvez un nom, un nom convivial que vous pouvez facilement retenir en une adresse IP, qui est moins facile à retenir.

Mais c'est la façon dont les ordinateurs communiquent réellement entre eux.

Passons à la structure d'une adresse IP.

Maintenant, vous avez très probablement vu des adresses IP, nous avons déjà travaillé avec elles dans ce cours.

Donc une adresse IP pourrait ressembler à ceci : 192 point 168 point 0 point 1.

Ceci est connu sous le nom de notation décimale pointée.

Et c'est une manière simple de représenter une adresse IP.

Maintenant, chacune de ces parties entre les points est en fait un octet binaire.

Donc c'est là que les choses deviennent un peu plus complexes.

Mais vous devez savoir cela.

Donc qu'est-ce qu'un octet binaire ? Eh bien, octet signifie que vous avez huit valeurs, et ces valeurs peuvent être soit un, soit zéro.

Ce sont les deux seules options.

C'est binaire.

Dans ce petit tableau ici, vous pouvez voir que dans ce cas, nous avons huit uns, tous en ligne.

Maintenant, du côté gauche, nous avons ce qu'on appelle le bit le plus significatif, ce qui signifie que si un est à cette place la plus à gauche, il aura une valeur de 128.

Si vous avez un, du côté droit, c'est le bit le moins significatif, et sa valeur est seulement un.

Si vous avez un zéro quelque part, cela signifie simplement zéro.

Par exemple, dans cette adresse, le troisième octet est un zéro.

Donc cela signifie que tous les huit bits sont des zéros.

Le un signifie que tous les sept bits ici sont des zéros.

Et nous avons un sur le côté droit, et cela est égal à ce bit le moins significatif ici.

Tout à gauche, nous avons 192.

Eh bien, 192 est 128 plus 64.

Donc nous avons un et un, et les valeurs restantes sont des zéros.

Et puis pour 168, nous avons un, donc c'est 128.

Ensuite, nous avons un dans la troisième place ici, qui est 32.

Et puis nous avons un dans la cinquième place ici, qui est huit.

Donc nous avons 128 plus 32 plus huit égale 168.

La raison pour laquelle il est important de comprendre ce binaire est lorsque nous arrivons au sous-réseautage, avec des masques de sous-réseau de longueur variable qui arrivent bientôt.

Donc d'abord, comprenons que les portions réseau et hôte d'une adresse IP.

Chaque adresse IP a un identifiant de réseau et un identifiant d'hôte, les boîtes bleues libres à gauche représentent l'identifiant de réseau, cette valeur sera la même pour chaque ordinateur sur ce réseau.

L'identifiant d'hôte sera unique pour chaque ordinateur sur ce réseau.

Comme je l'ai dit avant, chaque adresse IP aura un identifiant de réseau et d'hôte.

Mais comment cela est configuré varie.

Maintenant, comment savons-nous quelle partie est l'identifiant de réseau et quelle est l'identifiant d'hôte ? Eh bien, c'est là que le masque de sous-réseau entre en jeu.

Là où nous avons 255.

Dans ce cas, essentiellement là où nous avons un bit qui est un, cela représente l'identifiant de réseau.

Donc ici, nous avons huit bits qui sont un, huit bits qui sont un et huit bits qui sont un, donc ces trois premiers octets représentent tous l'identifiant de réseau.

Maintenant, le dernier octet dans la boîte orange ici sera l'identifiant d'hôte.

C'est pourquoi il est zéro.

Donc chaque bit dans le masque de sous-réseau qui est zéro signifie que c'est là que nous avons des valeurs qui peuvent être assignées à un hôte.

Et chaque bit qui est un, ce sont des valeurs qui vont être exactement les mêmes pour chaque ordinateur sur le réseau.

Donc un masque de sous-réseau est un moyen facile de voir quel bit est le réseau et quelle portion est l'identifiant d'hôte.

Donc regardons un exemple.

Nous avons notre réseau 19216800 avec un masque de sous-réseau qui ressemble à ceci.

Maintenant, c'est 24 bits, un masque de sous-réseau de 24 bits parce que nous avons huit uns dans ces trois premiers octets.

Et cela signifie que c'est un réseau slash 24.

C'est une autre façon de représenter le masque de sous-réseau.

Et c'est le format que vous utiliserez souvent dans AWS.

Donc sur ce réseau, nous pourrions avoir plusieurs ordinateurs.

Et nous pouvons voir qu'ils ont chacun des identifiants d'hôte différents.

Mais le même identifiant de réseau.

Dans ce cas, les identifiants d'hôte sont 123456 et l'identifiant de réseau est 1921680.

Pour tous les hôtes sur le réseau.

Nous avons également quelque chose appelé des classes avec les adresses IP.

La classe A ressemble à ceci : 10 000 et 255000.

Essentiellement, vous avez un masque de sous-réseau de huit bits.

Et cela signifie que la première adresse assignable sera un, vous ne pouvez jamais assigner zéro comme adresse pour un ordinateur sur le réseau.

Et la dernière adresse assignable sera 254 car vous ne pouvez pas utiliser 255, qui est ce qu'on appelle l'adresse de diffusion.

Maintenant, dans AWS, il y a aussi quelques autres adresses qui sont réservées avec un masque de sous-réseau de classe A, vous pouvez avoir jusqu'à 126 réseaux.

Et chacun de ces réseaux peut avoir un grand nombre d'hôtes : 16 777 214.

Et c'est parce que nous avons tous ces bits ici à utiliser pour l'identifiant d'hôte.

Nous avons ensuite la classe B, qui a un masque de sous-réseau de 16 bits.

La première adresse assignable est 172 16 01 pour cet exemple, et la dernière adresse serait 254.

Ici, nous avons 16 382 réseaux, donc beaucoup plus de réseaux et les adresses utilisables par réseau sont réduites à 65 544.

Enfin, nous avons une classe C.

Celle-ci a un masque de sous-réseau de 24 bits.

Et comme vous pouvez le voir, le nombre de réseaux a maintenant vraiment augmenté, mais nous n'avons pas autant d'adresses disponibles par réseau.

Ce sont donc les classes standard.

Maintenant, il y a aussi quelque chose appelé une plage d'adresses IP privées, il y en a quelques-unes qui sont réservées pour un usage privé.

Cela signifie pas sur Internet, en interne, au sein de votre entreprise, nous avons 10, triple zéro à 10 2552 552-551-7216 00217 230-225-5255.

Et puis 19216800321921680255.

Ces adresses sont réservées pour une utilisation dans les réseaux privés.

Donc pas orientées Internet, vous ne pouvez pas utiliser celles-ci sur l'Internet public, les choses deviennent maintenant un peu plus compliquées.

Parfois, nous voulons varier la longueur de nos masques de sous-réseau.

Et nous ne voulons pas nous en tenir à ces classes standard.

Donc nous utilisons quelque chose appelé le routage interdomaine sans classe.

Et cela nous aide à optimiser l'espace IP.

Examinons quelques exemples.

Disons que nous avons ce réseau ici, nous avons un masque de sous-réseau de 24 bits, nous avons huit bits d'hôte, et 254 adresses possibles.

La première adresse est point un.

La dernière est point 254.

Assez standard jusqu'à présent, nous avons ensuite un masque de sous-réseau de 16 bits.

Donc avec le même réseau, nous utilisons un masque de sous-réseau martyr différent, un non standard dans ce cas, car 192168 est typiquement un réseau de classe C.

Avec un masque de sous-réseau de 16 bits, nous avons 16 bits d'hôte, et jusqu'à 65 534 adresses.

Et cela ressemble à ceci.

Mais qu'en est-il d'un masque de sous-réseau slash 20 ? Eh bien, ici, comme vous pouvez le voir, nous avons une boîte bleue slash orange.

Et c'est parce que nous avons emprunté certains bits à l'identifiant de réseau pour les partager et les utiliser pour l'identifiant d'hôte.

Cela signifie que nous avons maintenant 12 bits d'hôte et 4094 adresses.

Parfois, c'est une meilleure configuration pour le nombre d'ordinateurs que vous devez avoir sur le réseau et le nombre de réseaux dont vous avez réellement besoin.

Et les adresses pour ce réseau commenceraient à 01 et iraient jusqu'à 15.254.

Donc c'est le routage interdomaine sans classe ou cidre.

Et il utilise des masques de sous-réseau de longueur variable.

En d'autres termes, en s'éloignant du standard et en optimisant le nombre de réseaux et d'hôtes que nous avons.

Maintenant, je sais que c'est assez complexe, et espérons que cela aura plus de sens au fur et à mesure que nous avancerons dans la section.

Donc c'est tout pour cette leçon particulière.

J'espère que vous en avez tiré beaucoup de valeur et je vous verrai dans la prochaine leçon.

Au revoir les gars.

Dans cette leçon, je vais vous enseigner le cloud privé virtuel Amazon ou VPC.

VPC incorpore plusieurs concepts différents.

Et ce que nous allons faire dans cette section est d'entrer dans les détails.

Donc d'abord, nous allons commencer par les connaissances de base autour du VPC lui-même.

Donc dans une région, nous avons nos VPC et ils sont toujours dans une région, ils ne peuvent pas s'étendre sur plusieurs régions.

Un VPC est essentiellement une portion logiquement isolée du cloud AWS que vous pouvez ensuite utiliser pour déployer vos ressources à l'intérieur.

Et c'est différent de l'espace public en dehors du VPC où des services comme Amazon S3 sont définis, c'est un espace privé et vous avez un contrôle total sur la façon dont vous configurez votre VPC.

Maintenant, comme vous le savez, dans une région, nous avons des zones de disponibilité, et vous pouvez les utiliser dans votre VPC en créant des sous-réseaux et en attribuant ces sous-réseaux à une zone de disponibilité.

Un sous-réseau est toujours attribué à une zone de disponibilité, il ne peut pas s'étendre sur plusieurs AZ.

Mais vous pouvez bien sûr avoir plusieurs sous-réseaux dans la même AZ, nous déployons ensuite nos ressources telles que des instances EC2 dans nos sous-réseaux.

Maintenant, il y a une chose appelée le routeur VPC.

Vous ne voyez pas vraiment le routeur VPC, mais il existe, et nous interagissons avec lui en configurant des tables de routage.

Maintenant, le routeur VPC gère tout le routage pour les connexions qui sortent d'un sous-réseau.

Si vous envoyez des données hors d'un sous-réseau, elles doivent aller ailleurs, peut-être vers un autre sous-réseau, ou peut-être vers Internet ou un autre réseau.

Donc le routeur s'occupe de s'assurer que la connexion de données est envoyée au bon endroit.

Maintenant, comme je l'ai dit, vous ne voyez pas le routeur VPC.

Tout ce que vous faites, c'est voir les tables de routage et elles configurent le routeur VPC pour vous.

Donc nous devons spécifier les destinations et les cibles pour certains réseaux et c'est ainsi qu'il sait ensuite où envoyer ces tentatives de connexion.

Si nous voulons accéder à Internet, nous avons également besoin d'une passerelle Internet, la passerelle Internet est attachée à votre VPC, vous n'en avez qu'une seule par VPC, la passerelle Internet est utilisée pour envoyer des données vers Internet.

C'est le trafic sortant.

Et depuis Internet, c'est le trafic entrant.

Et nous configurons notre table de routage avec une route vers l'ID de la passerelle Internet, ce qui lui indique d'envoyer tout le trafic qui ne correspond pas à l'un des réseaux de la table de routage avant celui-ci vers la passerelle Internet.

Maintenant, vous pouvez créer plusieurs VPC dans une région, vous avez une limite de cinq par défaut, mais vous pouvez demander une augmentation de ce nombre.

Chaque VPC a un bloc CIDR.

C'est le bloc global d'adresses à partir duquel vous créez ensuite les adresses que vous attribuez à vos sous-réseaux.

Donc c'est un peu comme un bloc maître d'adresses.

Chaque VPC a un bloc différent.

Donc dans ce cas, nous avons deux VPC.

Et ils ont des blocs CIDR différents.

Comme vous l'avez appris dans la dernière leçon, CIDR signifie Classless Inter-Domain Routing, à partir du bloc CIDR global, nous pouvons ensuite créer les ID de réseau pour nos sous-réseaux.

Et ils s'intègrent dans ce bloc CIDR global.

Mais ils ont un masque de sous-réseau différent, donc essentiellement un sous-ensemble des adresses disponibles globalement et c'est pourquoi il est vraiment important de s'assurer que nous spécifions correctement nos blocs CIDR afin d'avoir suffisamment de réseaux et suffisamment d'hôtes par réseau.

Nous couvrirons cela dans une autre leçon.

Donc ici, nous avons deux VPC, chacun avec des blocs CIDR différents, puis chacun avec des sous-réseaux différents qui proviennent de ces blocs CIDR.

Maintenant, nous allons couvrir beaucoup de ces composants dans cette section, mais je veux juste les couvrir à un niveau élevé maintenant.

Donc vous savez ce qu'est un VPC et ce que sont les sous-réseaux, vous savez ce qu'est une passerelle Internet.

Maintenant, une passerelle Internet uniquement en sortie est lorsque vous utilisez le protocole IP v six.

Et il permet le trafic uniquement en sortie, alors qu'une passerelle Internet est pour IPv4, et elle permet à la fois le trafic en sortie et en entrée.

Comme vous le savez, le routeur, le routeur VPC gère le routage des connexions vers les bons endroits.

Maintenant, une connexion d'appairage est quelque chose où vous pouvez connecter plusieurs VPC et avoir un routage privé entre eux.

Nous couvrirons cela en détail plus tard dans la section.

Les points de terminaison VPC vous permettent de vous connecter en utilisant des adresses IP privées à des services publics sur AWS.

Encore une fois, nous couvrirons cela en détail plus tard.

Maintenant, les instances et passerelles NAT, nous les avons couvertes plus tôt dans le cours, ce sont deux moyens qui vous permettent d'activer la connectivité Internet uniquement en sortie pour vos instances dans des sous-réseaux privés.

Les deux composants suivants, la passerelle privée virtuelle et la passerelle client sont tous deux liés à la création de connexions VPN (réseau privé virtuel) à nos bureaux d'entreprise ou à nos centres de données d'entreprise.

Donc c'est un réseau virtuellement privé et un tunnel crypté sur Internet.

Nous avons ensuite Direct Connect, qui évite Internet en utilisant des connexions privées jusqu'à votre centre de données ou bureau, et les groupes de sécurité et les ACL réseau sont deux types différents de pare-feu.

Nous les couvrirons un peu plus en détail dans cette section.

Nous avons utilisé les groupes de sécurité assez souvent jusqu'à présent.

Ils sont ce que nous appelons un pare-feu au niveau de l'instance, car ils opèrent au niveau de l'interface réseau attachée à nos instances EC2.

Ensuite, nous avons l'ACL réseau, qui est un pare-feu au niveau du sous-réseau.

Donc il ne voit que le trafic entrant et sortant du sous-réseau.

Donc pour résumer, cette connaissance de base du VPC est un réseau virtuel dédié à votre compte AWS.

C'est similaire à avoir votre propre centre de données à l'intérieur d'AWS, car vous êtes capable d'avoir un contrôle total sur ce que vous faites avec la définition de vos blocs CIDR, la création de vos propres sous-réseaux, la configuration de votre sécurité, votre routage et ainsi de suite.

Vous avez beaucoup, beaucoup de contrôle.

Il est logiquement isolé des autres réseaux virtuels dans le cloud AWS.

Et comme je l'ai mentionné auparavant, vous obtenez un contrôle total sur de nombreux éléments de configuration dans votre VPC.

Et un VPC est un endroit où vous lancez ensuite vos ressources telles que les instances Amazon EC2.

Lorsque vous créez un VPC, vous devez spécifier votre bloc CIDR.

Donc c'est le bloc global d'adresses.

Maintenant, nous verrons comment sélectionner le meilleur bloc CIDR pour notre cas d'utilisation.

Et une autre leçon, un VPC s'étend sur toutes les AZ dans une région.

Cela signifie essentiellement que s'il y a trois ou six ou un autre nombre d'AZ dans une région, vous pouvez créer des sous-réseaux dans votre VPC sur toutes ces AZ.

Mais rappelez-vous, chaque sous-réseau est toujours dans une AZ, il ne peut pas s'étendre sur plusieurs AZ, mais vous pouvez créer plusieurs sous-réseaux si vous le souhaitez.

Dans une zone de disponibilité, vous obtenez un contrôle total sur l'accès à vos ressources à l'intérieur d'un VPC.

Par défaut, vous pouvez en créer cinq par région.

Mais vous pouvez étendre cela si vous soumettez une demande.

Un VPC par défaut est créé dans chaque région avec un sous-réseau dans chaque zone de disponibilité.

Et c'est toujours un sous-réseau public.

Donc, quelle que soit la région que vous avez changée, il y a déjà un VPC par défaut et il a déjà un certain nombre de sous-réseaux publics.

Maintenant, c'est tout pour cette leçon.

Dans la prochaine leçon, nous allons voir comment nous pouvons déterminer un bloc CIDR adapté à notre cas d'utilisation.

Dans cette leçon, nous allons voir ce que nous devons faire pour définir les blocs CIDR, nous allons utiliser quelques règles et directives ainsi que les meilleures pratiques.

Donc d'abord avec les règles et directives.

Et celles-ci proviennent d'AWS, la taille du bloc CIDR peut être comprise entre un masque de sous-réseau /16 et /28, il ne peut pas chevaucher un bloc CIDR existant associé au VPC.

Et vous ne pouvez pas augmenter ou diminuer la taille d'un bloc CIDR existant.

Donc vous devez le faire correctement dès le début, les quatre premières et dernières adresses IP ne sont pas disponibles pour une utilisation.

Donc vous devez en tenir compte lorsque vous définissez la taille de vos sous-réseaux.

Parce que vous voulez vous assurer d'avoir suffisamment d'adresses pour vos instances que vous déployez.

AWS recommande d'utiliser des blocs CIDR provenant des plages RFC 1918.

Rappelez-vous, ce sont les plages d'IP privées.

Et ce sont ces adresses.

Et bien sûr, elles vous donnent beaucoup de possibilités.

Donc cela ne devrait pas poser de problème.

Maintenant, regardons un exemple.

Donc disons que j'ai un bloc CIDR VPC qui ressemble à ceci.

C'est 10 000 avec un masque de sous-réseau de 16 bits.

Donc cela signifie qu'il ressemble à ceci 10 000 slash 16.

Donc c'est le bloc global d'adresses.

Mais maintenant, nous voulons créer nos sous-réseaux.

Donc ce que nous devons faire, c'est que nous allons prendre certains des bits de la portion hôte ici et les assigner à la portion réseau.

Donc peut-être que nous allons avoir 10 010 slash 24.

Et cela signifie que nous avons emprunté tous les huit bits de ce troisième octet pour l'identifiant de réseau.

Donc vos sous-réseaux VPC auront un masque de sous-réseau plus long que le bloc CIDR dont ils proviennent.

Maintenant, dans ce cas, c'est un masque de sous-réseau de 24 bits.

Maintenant, quel est le réseau suivant, le réseau suivant est 10 020 slash 24.

Et puis le suivant est 10, zéro trois, zéro slash 24.

Donc chacun de ces sous-réseaux va avoir jusqu'à 254 hôtes potentiels.

Mais bien sûr, vous devez enlever quelques-uns de ce nombre.

Donc enlevez cinq de ce nombre.

Et c'est le nombre d'adresses qui vous reste pour vos instances EC2.

Donc tant que vous êtes satisfait de ce nombre d'instances par réseau, ce qui est encore un nombre assez grand, alors c'est une bonne plage et très simple à utiliser.

Maintenant, passons en revue quelques considérations supplémentaires.

Vous devez vous assurer d'avoir suffisamment de réseaux et d'hôtes, vous ne voulez vraiment pas vous tromper.

Vous ne pouvez définir le bloc CIDR qu'une seule fois et ensuite vous êtes bloqué avec.

Donc assurez-vous de bien planifier.

Les blocs CIDR plus grands sont généralement meilleurs, cela vous donne plus de flexibilité à l'avenir.

Les sous-réseaux plus petits sont acceptables pour la plupart des cas d'utilisation, vous n'avez pas besoin de milliers d'instances par sous-réseau.

Envisagez de déployer des niveaux d'application par sous-réseau.

Donc si vous avez une application à trois niveaux, vous pourriez avoir différents sous-réseaux pour chaque niveau.

Et vous pourriez l'avoir comme hautement disponible sur plusieurs zones de disponibilité avec un sous-réseau dans chaque AZ.

Donc c'est une bonne façon d'obtenir cette haute disponibilité et cette résilience dans votre charge de travail.

Maintenant, l'appairage VPC, que nous allons couvrir un peu plus tard, est là où vous connectez vos VPC afin de pouvoir router directement entre eux en utilisant des adresses IP privées, donc vous ne sortez pas sur l'Internet public.

Maintenant, il est vraiment essentiel que vous n'ayez pas de blocs CIDR qui se chevauchent.

En d'autres termes, vous ne pouvez pas avoir le même bloc CIDR dans deux VPC et les connecter avec l'appairage VPC.

Donc même si vous ne faites pas d'appairage maintenant, rappelez-vous simplement cela car vous pourriez en avoir besoin à l'avenir.

Vous voulez vous assurer que vos blocs CIDR ne se chevauchent pas.

Et cela concerne tous les VPC et toutes les régions et tous les comptes, alors assurez-vous de le faire correctement.

Donc en général, évitez simplement les blocs CIDR qui se chevauchent autant que possible.

Assurez-vous de prendre cela en considération lorsque vous concevez vos plages d'adresses IP.

Donc revenons à un exemple.

Disons que nous avons 10 000 slash 16.

Donc c'est notre bloc CIDR.

Et nous créons une série de sous-réseaux.

Maintenant, chacun de ces sous-réseaux a un masque de sous-réseau de 24 bits et comme vous pouvez le voir, nous les séparons en sous-réseaux publics et privés dans différentes zones de disponibilité, les sous-réseaux privés ont une table de routage privée, et les publics ont une table de routage différente, bien sûr, la table de routage principale pour les sous-réseaux publics ici aura une passerelle Internet.

Et ces sous-réseaux attribueront également des adresses IP publiques aux instances qui y sont lancées.

Donc c'est un peu de théorie derrière cela et quelques exemples pratiques.

Je veux aussi vous montrer un outil très utile qui vous aide à planifier vos blocs CIDR et vos sous-réseaux.

Je vais joindre un lien vers cet outil à la leçon.

Maintenant, ce que nous pouvons faire avec cet outil est de spécifier notre bloc CIDR et de voir les sous-réseaux.

Et nous pouvons en fait, l'outil nous aidera à déterminer quels sous-réseaux utiliser en fonction du nombre de réseaux dont nous avons besoin de sous-réseaux ou du nombre d'hôtes par réseau.

Donc restons avec l'exemple et mettons 10.0 point 0.0.

Et puis le masque de sous-réseau, nous allons faire défiler jusqu'à slash 16.

Maintenant, je veux avoir des sous-réseaux avec au moins 254 hôtes.

Donc ce serait un réseau de classe C standard.

Maintenant, voyons ce que nous obtenons.

Donc cliquons sur Créer.

Et il nous donne tous les sous-réseaux avec un masque de sous-réseau de 24 bits qui s'intègrent dans le bloc CIDR.

Donc nous avons le sous-réseau zéro ici.

Et puis tout en bas, nous arrivons au tout dernier sous-réseau, qui est 255.

Donc c'est 255 sous-réseaux que nous pouvons avoir.

Et chacun de ces sous-réseaux peut supporter jusqu'à 254 hôtes.

Bien sûr, le VPC va en fait réserver quelques adresses, donc vous n'aurez pas autant, mais vous en aurez encore près de 250.

Donc c'est un outil vraiment utile pour vous aider à déterminer quels seront vos sous-réseaux dans votre bloc CIDR.

Et cela vous aidera également à déterminer le meilleur bloc CIDR.

Salut les gars, dans cette leçon, je vais vous montrer comment utiliser l'assistant VPC.

L'assistant vous aide à créer très facilement un VPC sans avoir à faire beaucoup de travail manuel.

Dans ma console de gestion.

Allons dans le réseau et VPC.

Sur le tableau de bord VPC ici, je peux choisir lancer l'assistant VPC, et nous obtenons ensuite quatre options préconfigurées différentes.

Et ce que je veux faire, c'est simplement passer en revue ce que vous obtenez avec chacune de ces options.

Donc la première est un VPC avec un seul sous-réseau public.

Très simple.

Vous obtenez un bloc CIDR slash 16 et un slash 24.

sous-réseau.

Et c'est un sous-réseau public.

Donc si vous sélectionnez cette option, vous pouvez spécifier votre bloc CIDR et il vous est donné par défaut, vous pouvez spécifier un nom, il a déjà entré le bloc CIDR du sous-réseau.

Vous pourriez choisir une AZ si vous voulez, ou sinon, après avoir entré le nom, vous pourriez littéralement simplement créer le VPC et il va faire toutes les tâches pour vous.

Et cela inclurait l'attachement d'une passerelle Internet afin que vous ayez une connectivité Internet pour votre sous-réseau public.

Maintenant, sortons de cela, revenons en arrière, allons dans VPC avec des sous-réseaux publics et privés.

Donc maintenant, vous obtenez simplement des sous-réseaux publics et privés.

Et vous obtenez un dispositif de traduction d'adresse réseau, donc vous obtenez une passerelle NAT, donc vos instances privées peuvent accéder à Internet.

Donc encore une fois, avec cette option, il n'y a pas trop de choses à configurer, autre que les différents sous-réseaux publics et privés.

La différence clé ici est que votre passerelle Nat a besoin d'une IP élastique, donc vous avez besoin d'un ID d'allocation d'IP élastique.

Maintenant, revenons en arrière.

Et cette fois, nous allons aller dans VPC avec des sous-réseaux publics et privés et un accès VPN matériel.

Ici, vous avez des sous-réseaux publics, des sous-réseaux privés.

Et un tunnel VPN est également créé.

Maintenant, vous devez avoir un appareil VPN dans votre centre de données d'entreprise.

Si nous sélectionnons cette option, et donnons simplement un nom à cela, mon VBC.

Et laissons les valeurs par défaut sur cette page, cliquons sur Suivant.

Et il va demander l'IP de la passerelle client et c'est l'adresse IP de votre appareil VPN de votre côté du réseau dans votre centre de données d'entreprise.

Donc si vous spécifiez ces détails, lorsque vous créez ce VPC, il va établir cette connexion.

Revenons simplement en arrière.

Et la dernière option en bas est VPC avec un sous-réseau privé uniquement et un accès VPN matériel, identique à la précédente, sauf que vous n'avez qu'un sous-réseau privé.

Donc vous avez une connexion VPN depuis votre centre de données d'entreprise vers un sous-réseau privé sur AWS, sans routage sortant via Internet depuis ce sous-réseau dans AWS.

Donc ce sont les quatre options.

Je voulais simplement vous les montrer rapidement.

Et dans la prochaine leçon, nous créerons notre propre VPC personnalisé.

Dans cette leçon, nous allons créer un VPC personnalisé avec des sous-réseaux publics et privés.

Maintenant, voyons ce que nous allons créer. Nous allons utiliser le même exemple de bloc CIDR que nous avons vu dans la section, ce sera un réseau 10 000 avec un masque de sous-réseau de 16 bits, c'est le bloc global d'adresses, puis nous allons créer ces quatre sous-réseaux.

Nous avons privé un a dans privé un, B, et public un a public un, B, et le un a et le un B signifient qu'ils sont associés à une zone de disponibilité spécifique.

Maintenant, pour les sous-réseaux privés, nous aurons une table de routage privée pour les sous-réseaux publics, nous aurons cette table de routage principale qui est créée, par défaut, nous attacherons une passerelle Internet à notre VPC.

Et la table de routage principale aura une route via la passerelle Internet vers Internet pour ces sous-réseaux publics.

Nous devons également spécifier que nous voulons que nos instances obtiennent automatiquement une adresse IP publique.

Donc c'est la configuration, dirigeons-nous vers la console et construisons cela.

Dans le tableau de bord VPC.

Je vais aller dans vos VPC, et nous avons un seul VPC par défaut.

Donc créons-en un nouveau.

Dans votre téléchargement de cours dans le répertoire de code, Amazon VPC, vous aurez ce fichier un VPC personnalisé bash, nous pouvons simplement copier les valeurs.

Donc j'ai le nom, qui va sous l'étiquette de nom, copions le bloc CIDR et mettons-le sous le bloc CIDR ipv4.

Nous ne allons pas faire ipv6 à ce stade.

Dans ce cours, nous laisserons la tenure par défaut.

Si vous changez pour dédié, cela va mettre vos instances sur du matériel qui vous est dédié, et cela va vous coûter plus d'argent.

Donc laissez définitivement cela par défaut.

Et c'est tout ce que nous devons faire pour créer le VPC.

Donc le VPC est en cours de création.

Une chose que j'aime faire est d'aller dans actions, modifier les noms d'hôtes DNS, et activer, cela signifie que nous obtiendrons des noms d'hôtes DNS pour nos instances EC2.

La tâche suivante est de créer nos sous-réseaux, nous avons des sous-réseaux publics et des sous-réseaux privés.

Donc je vais simplement copier ces valeurs dans mon presse-papiers, nous reviendrons, descendrons dans les sous-réseaux.

Créer des sous-réseaux, nous devons spécifier notre VPC.

Donc mon VPC et ensuite nous pouvons mettre le nom et le nom du sous-réseau, choisir la zone de disponibilité comme un a US East one a.

Et puis les IP B pour le bloc CIDR, nous reviendrons, nous copierons ce bloc CIDR.

Et nous le collerons.

Maintenant, nous pourrions créer le sous-réseau là ou nous pouvons en ajouter un nouveau.

Et nous allons faire la même chose pour les trois sous-réseaux suivants.

Donc parcourez simplement ce fichier et copiez les paramètres pour vos trois sous-réseaux supplémentaires.

Lorsque vous avez terminé, votre page devrait ressembler à ceci, vous avez public un a dans US East one a, nous avons un bloc cyber 10 01, et puis vous avez le sous-réseau à public un, B, et cela devrait être dans US East one, B, alors modifions cela.

Et 10 zéro deux privé un a devrait également être dans US East one, a 10, zéro trois, et puis privé un B dans US East one, b 10 04.

Donc tout cela a l'air bien.

Créons les quatre sous-réseaux.

Et voici les quatre sous-réseaux créés.

Maintenant, pour nos sous-réseaux publics.

Nous voulons aller dans actions ici, modifier les paramètres d'assignation automatique d'IP, et activer l'assignation automatique des adresses ipv4 publiques.

Donc je l'ai fait pour public un, B, faisons-le pour public un, a.

Et ceux-ci sont mis à jour maintenant.

Donc la prochaine chose que je veux faire, c'est que je dois créer une table de routage pour mes sous-réseaux privés.

Donc ils ne sont pas attachés à la table de routage principale, qui est là où les sous-réseaux publics seront.

Donc allons dans les tables de routage.

Créer une table de routage, nous allons spécifier un nom, je l'ai dans mon presse-papiers depuis le fichier private RT.

Pour VPC, je vais sélectionner mon VPC.

Et puis nous créerons la table de routage.

Une fois qu'elle est créée, allez dans les associations de sous-réseaux, modifiez les associations de sous-réseaux, et vous voulez sélectionner private one B et private one a et sauvegarder.

Donc maintenant que nous avons fait cela, si nous allons dans les associations de sous-réseaux, nous devrions voir une association explicite pour private one A et B.

Si nous revenons aux tables de routage, nous verrons l'autre table de routage ici.

Donc c'est la table de routage principale ou la table de routage publique si vous voulez.

Et sous les associations de sous-réseaux, il n'y a pas d'associations de sous-réseaux explicites, mais one a et one B public sont associés implicitement.

La prochaine chose que je dois faire est d'aller et de créer une passerelle Internet.

Donc sous les passerelles Internet, ici, créons une passerelle Internet.

Nous allons lui donner un nom.

Et collons simplement cette valeur depuis le fichier et créons la passerelle Internet.

Une fois qu'elle est créée, elle doit être attachée et les actions que vous pouvez attacher au VPC, sélectionnez le VPC et attachez la passerelle Internet.

Maintenant, la dernière chose que nous devons faire maintenant que nous avons une passerelle Internet.

Nous ne faisons pas de route depuis notre table de routage principale.

Donc allons dans la table de routage principale ici.

Allons dans les routes, modifions les routes, ajoutons une route, et nous mettrons le 0000 slash zéro, choisissons notre passerelle Internet.

Et la voilà dans la liste.

Donc maintenant, tout ce qui est dans le bloc CIDR sera routé localement par le routeur VPC.

Et tout ce qui n'est pas dans ce bloc CIDR VPC ira sur Internet via la passerelle Internet.

Donc sauvegardons simplement ces changements.

Donc c'est tout, nous avons créé notre VPC personnalisé avec des sous-réseaux publics, des sous-réseaux privés, deux tables de routage et une passerelle Internet.

Maintenant, c'est tout ce que je dois faire pour cette leçon particulière.

Dans la prochaine leçon, ce que j'aimerais faire, c'est lancer quelques instances et simplement tester notre configuration et nous assurer que nous avons la communication que nous attendons.

Donc nous avons créé notre VPC personnalisé et je voudrais simplement le tester maintenant.

Donc nous allons lancer quelques instances EC2, deux instances dans deux sous-réseaux publics différents et une dans un sous-réseau privé.

Et nous allons en fait le faire via la ligne de commande, c'est vraiment utile de connaître la ligne de commande.

Maintenant, tous les examens ne nécessitent pas de connaître la ligne de commande.

Donc pour l'associé architecte de solutions, cela n'a pas vraiment d'importance.

Pour le développeur, cela compte un peu plus pour certains services, et définitivement pour l'examen sysops.

Maintenant, quel que soit l'examen que vous passez, ou quel que soit le parcours de carrière que vous suivez dans AWS, c'est encore une compétence vraiment utile à avoir.

Donc cela vaut définitivement la peine d'apprendre la ligne de commande.

Donc nous allons lancer quelques instances en utilisant la ligne de commande.

Et puis nous utiliserons ces instances juste pour tester la connectivité entre elles.

Il y a quelques choses que je veux faire avant de commencer.

Tout d'abord, je veux créer une passerelle NAT.

Donc je suis dans la console de gestion VPC.

Sous les passerelles NAT, créons une passerelle NAT, je vais simplement l'appeler ma passerelle NAT, et je dois sélectionner un sous-réseau.

Maintenant, rappelez-vous, avec les passerelles NAT, elles vont toujours dans les sous-réseaux publics.

Donc ici, je vais choisir public one a, et je sais qu'il est dans le bon VPC.

Donc la connectivité est publique, nous attribuons une IP élastique, et créons simplement la passerelle NAT.

Maintenant, bien sûr, elle ne fonctionnera pas jusqu'à ce que nous mettons à jour la table de routage pour nos sous-réseaux privés.

Donc sous les tables de routage, choisissons la RT privée.

Allons dans les routes, modifions les routes, ajoutons une route, et nous allons spécifier 000 slash zéro.

Et cette fois, ce sera une passerelle NAT.

Et nous choisirons cet ID de passerelle NAT.

Maintenant, nos sous-réseaux privés auront accès à Internet.

Et c'est important car lorsque notre instance se lance, nous allons exécuter des données utilisateur.

Et cela va se connecter à Internet pour télécharger certains binaires pour httpd.

La prochaine chose est sous les groupes de sécurité, nous avons besoin d'un groupe de sécurité.

Créons un groupe de sécurité.

Je vais l'appeler public web, lui donner une description, et m'assurer de sélectionner mon VPC.

Pour les règles sortantes.

Par défaut, il permet tout le trafic vers n'importe quelle destination.

Pour les règles entrantes, pour l'instant, nous allons ajouter tout le trafic depuis n'importe quelle destination.

Donc c'est très ouvert, ne vous inquiétez pas, nous allons le verrouiller dans une leçon ultérieure et pratiquer avec quelques configurations de groupe de sécurité différentes.

Mais pour l'instant, ouvrons tout.

Je vais créer mon groupe de sécurité, et il est prêt à être utilisé.

Il y a un fichier dans votre téléchargement de cours.

Et il se trouve dans le répertoire de code Amazon VPC, et c'est AWS COI run instances, nous devons ajouter certaines valeurs dans ce fichier.

La première chose que nous devons faire pour cette commande est de spécifier un ID d'image.

Donc la commande est AWS easy to run dash instances.

Et ce sont les valeurs que nous devons spécifier.

Donc d'abord, trouvons l'ID AMI que nous voulons utiliser.

Les ID AMI sont spécifiques à la région.

Donc nous devons nous assurer que tout ce que nous faisons dans cette leçon est dans la même région.

C'est aussi là où vous avez créé votre VPC personnalisé.

Donc pour moi, c'est la Virginie du Nord, espérons que ce soit la même chose pour vous.

Lançons une instance.

À côté de l'AMI Amazon Linux deux.

Prenons cet ID AMI, ne prenez rien entre parenthèses, copiez-le dans le presse-papiers.

Revenez et collez-le dans le type d'instance, nous pouvons simplement taper cela, ce sera T deux point micro pour les ID de groupe de sécurité.

Revenons et trouvons l'ID de notre groupe de sécurité.

Je peux voir mon groupe de sécurité d'accès web public.

Copions simplement l'ID du groupe de sécurité, revenons et collons celui-ci.

Ensuite, nous avons besoin de l'ID du sous-réseau.

Cette fois, je suis de retour dans la console de gestion VPC.

Allons dans les sous-réseaux.

Tout d'abord, je veux l'ID du sous-réseau public one a.

Donc je vais simplement le copier dans mon presse-papiers.

Le nom de la clé est la paire de clés que vous utilisez dans cette région spécifique.

De retour dans EC2, vous pouvez aller dans les paires de clés si vous ne vous souvenez pas de ce que c'est, et simplement copier ce nom.

Et nous pouvons le coller.

Enfin, il y a des données utilisateur que nous allons spécifier.

Maintenant, c'est le fichier de données utilisateur.

Ce qu'il fait, c'est exécuter un serveur web.

Et puis il crée quelques variables à partir des métadonnées, nous récupérons en fait l'ID du sous-réseau, et il le met essentiellement dans une simple page web.

Donc nous pouvons voir où l'instance est en cours d'exécution.

Dans notre commande ici, nous devons simplement spécifier le nom de ce fichier.

Maintenant, ce que vous voulez faire, c'est changer pour votre répertoire Amazon VPC, où nous avons toutes ces informations.

Et c'est là que se trouve le fichier.

Donc copiez cela dans votre presse-papiers, assurez-vous d'avoir le fichier : slash slash, et puis le nom de votre fichier.

Copions cela et assurons-nous que cela fonctionne.

Avant de remplir les deux autres, vous devrez avoir exécuté AWS configure, avant de faire cet exercice, vous devrez avoir spécifié un ID de clé d'accès, une clé d'accès secrète.

Et votre région doit être la même que la région où nous essayons de déployer nos instances maintenant.

Donc tout est bon pour moi.

Collons cette commande et exécutons la commande.

Et cela semble réussi.

Et nous pouvons voir que nous avons une instance en cours d'exécution dans US East one a.

Et il y a beaucoup d'informations si vous faites simplement défiler et descendez la page ici.

Donc allons dans EC2 et vérifions qu'il se lance, dans EC2, je peux voir que j'ai cette instance en cours d'exécution ici en bas.

Maintenant, je vais simplement étiqueter celle-ci comme public one a pour savoir laquelle c'est.

Maintenant, la prochaine chose que nous devons faire est de revenir à la console de gestion VPC, prendre l'ID de sous-réseau de public one, B et revenir à notre fichier.

Et nous allons utiliser celui-ci.

Donc ce que nous pouvons faire est de copier tout cela, le mettre dans un be ici.

Et puis je vais prendre cet ID de sous-réseau, et simplement remplacer celui-ci ici.

Donc nous devrions maintenant être en mesure de lancer dans public one B, copions cela dans notre presse-papiers, revenons et collons-le.

Cela a l'air bien.

Si je rafraîchis la page ici, et nous avons cette instance en attente, c'est le public one be.

Donc je vais simplement lui donner une étiquette pour savoir laquelle c'est.

Et enfin, nous allons lancer l'instance dans notre sous-réseau privé.

Donc encore une fois, j'ai juste besoin d'obtenir l'ID de sous-réseau pour private one v.

Donc je l'ai copié dans mon presse-papiers, je reviens, je le colle.

Et maintenant nous avons la commande.

Et ces données utilisateur devraient s'exécuter correctement dans le sous-réseau privé, car nous sommes en mesure de nous connecter à Internet via la passerelle NAT.

Donc je colle cela, j'appuie sur Entrée.

Et voilà, nous devrions avoir une autre instance, dans EC2, je peux voir mon instance en attente ici.

Donc appelons celle-ci private, one be super.

Donc j'ai ces instances, faisons simplement un rafraîchissement et voyons où nous en sommes.

Donc quelques-unes sont en cours d'exécution, trions par nom, cela pourrait rendre les choses un peu plus faciles.

Je vais simplement copier dans mon presse-papiers, l'IP publique pour public one a, et la coller dans une fenêtre de navigateur.

Et j'obtiens cette page web.

Et elle me donne l'ID du sous-réseau.

Donc cela devrait correspondre au sous-réseau pour public one A.

Donc c'est super, nous avons prouvé que nous pouvons nous connecter depuis Internet à notre instance EC2.

Maintenant, l'autre chose que je veux faire est de me connecter entre mes instances EC2, dans la console ici, ce que je vais faire est de me connecter à public one, j'utilise EC2 instance Connect.

Et pendant que cela se connecte, revenons.

Ensuite, je veux obtenir l'adresse IP privée de mon instance public one B.

Et c'est 10, zéro deux 25.

Et revenons simplement à EC2 instance Connect.

Et je vais faire un ping à 10 point 0 point 2 point 25.

Et voyons si cela répond.

Donc cela prouve que nous avons la connectivité à notre instance, dans l'autre sous-réseau public, le sous-réseau public one B.

Donc nous avons une connectivité bidirectionnelle, les réponses reviennent également.

Donc c'est super.

Enfin, vérifions que nous pouvons nous connecter à notre sous-réseau privé.

Donc voyons quelle est l'adresse IP privée.

C'est 10 04148.

Donc faisons un ping à 10.0 point 4.148.

Et voyons si cela fonctionne.

Et c'est le cas, nous obtenons une réponse ICMP.

Donc c'est super, cela montre que nous avons cette connectivité qui fonctionne.

Une autre chose que nous pourrions faire à partir d'ici est de voir si nous pouvons nous connecter à cette page web.

Donc nous allons utiliser la commande curl et spécifier 10.0 point 4.148 et appuyer sur Entrée.

Et nous obtenons une réponse ici qui dit que cette instance est dans le sous-réseau avec l'ID et elle nous donne l'ID du sous-réseau.

Donc c'est l'en-tête h1 pour la page web HTML que nous avons sur ce site web.

Donc nous pouvons voir que nous avons le port 80.

Ouvrir également, nous avons pu nous connecter à l'instance dans le sous-réseau privé.

Et nous pouvons également en déduire que l'instance peut se connecter à Internet car elle a pu installer ce service web.

Donc c'est tout pour nos tests de connectivité pour l'instant.

Maintenant, je vais laisser toutes ces instances et la passerelle NAT en cours d'exécution, car nous allons revenir et continuer lorsque nous ferons quelques tests avec des groupes de sécurité et des ACL réseau.

Les gars, les groupes de sécurité et les listes de contrôle d'accès réseau.

Les ACL sont deux types différents de pare-feu que nous pouvons appliquer dans notre environnement AWS.

Donc regardons comment ils fonctionnent.

Donc ici nous avons un VPC avec deux zones de disponibilité.

Et nous avons quelques sous-réseaux publics et privés.

Et nous avons quelques instances EC2 qui ont été lancées dans différents sous-réseaux publics et privés.

Donc voyons comment nous pouvons contrôler le trafic.

Tout d'abord, nous pouvons appliquer quelque chose appelé une liste de contrôle d'accès réseau ou ACL réseau.

Maintenant, celles-ci sont appliquées au niveau du sous-réseau.

Donc vous pouvez voir qu'elles sont assises ici au bord du sous-réseau.

Maintenant, tout le trafic qui entre et sort d'un sous-réseau passera par une ACL réseau.

Donc vous filtrez essentiellement le trafic lorsqu'il entre ou sort du sous-réseau.

Donc le trafic entrant et sortant, un groupe de sécurité est différent.

Un groupe de sécurité s'applique en fait au niveau de l'instance d'une instance EC2, en fait au niveau de l'interface réseau de l'instance EC2.

Donc cela signifie que nous pouvons avoir un groupe de sécurité qui est appliqué aux instances EC2 dans différents sous-réseaux.

Donc c'est le même groupe de sécurité, le groupe de sécurité A, et il a été appliqué aux instances dans plusieurs sous-réseaux différents.

Donc rappelez-vous que c'est au niveau de l'instance, cela signifie qu'il va filtrer le trafic allant entre les instances dans le même sous-réseau, ou à travers différents sous-réseaux, nous pourrions ensuite avoir un groupe de sécurité B, qui est attaché à différentes instances.

Donc les groupes de sécurité peuvent être appliqués aux instances dans n'importe quel sous-réseau.

Maintenant, ce qui se passe ici avec ces groupes de sécurité, c'est la même chose de base qu'une ACL réseau.

Ils recherchent le trafic qui entre et sort du groupe de sécurité.

Donc si vous envoyez du trafic depuis une instance, dans le groupe de sécurité A, vers une instance, dans le groupe de sécurité B, il va vérifier qu'il y a une règle pour permettre le trafic sortant, et ensuite il va vérifier ici, le groupe de sécurité B va vérifier si je vais permettre le trafic depuis le groupe de sécurité A, et vous pouvez le faire par adresse IP, ou vous pouvez le faire par l'ID du groupe de sécurité lui-même, nous verrons tout cela en détail dans le pratique également.

Maintenant, je veux vous parler des pare-feu avec état et sans état, car le groupe de sécurité est un pare-feu avec état.

Et une ACL réseau est un pare-feu sans état.

Et il est vraiment important de comprendre la différence.

Donc regardons un exemple.

Nous avons un client ici.

Donc c'est un ordinateur qui veut accéder à un service sur un serveur web, et nous avons un pare-feu au milieu.

Donc ce qui se passe, c'est que le client va se connecter au serveur, le serveur est un serveur web, il écoute sur le port 80.

Le port source est le port qui est assigné à la connexion par l'ordinateur.

Et c'est ce qu'on appelle un port à numéro élevé, c'est un port au-dessus de 1024.

Et il est assigné dynamiquement pour chaque connexion.

Donc nous avons un port source et un port de destination.

Et nous avons une source et une destination IP également.

Maintenant, le trafic de retour a un port source de Port 80, car c'est là que le port de service web fonctionne, et le port de destination de 65188.

Et bien sûr, les IP sont également échangées.

Donc l'IP de destination sera le client, l'IP source sera le serveur web.

Maintenant, qu'avons-nous besoin dans la table de règles du pare-feu pour que cela fonctionne ? Eh bien, ce dont nous avons besoin ici, c'est d'une règle pour HTTP qui permet à l'IP source 10.1.1.1 de parler à l'IP de destination 10.2.1.10.

Et il doit avoir le port source et le port de destination spécifiés.

Maintenant, bien sûr, c'est un port assigné dynamiquement.

Donc nous ne savons pas ce que c'est à l'avance.

Donc ce que vous auriez probablement ici, c'est n'importe quel port source, plutôt que d'avoir le port source spécifié, nous aurions n'importe quel port source acceptable.

Et plutôt qu'une IP source spécifique, nous pourrions avoir n'importe quelle IP car c'est une connexion basée sur Internet.

Donc ce sont des choses que nous pouvons manipuler dans nos tables de règles.

Mais le port de destination sera toujours 80 car c'est là que le serveur web fonctionne.

Donc nous voulons nous assurer que nous n'autorisons pas les connexions à n'importe quel port sur le serveur web.

Maintenant, c'est le trafic entrant vers le serveur web.

Qu'en est-il du trafic de retour ? Eh bien, dans ce cas, les choses sont inversées.

Donc nous avons le même protocole, l'IP source du serveur web, l'IP de destination du client, et le port source de 80, et le port de destination du port dynamique du client.

Maintenant, vous auriez probablement le port de destination, et l'IP de destination est n'importe quelle IP, car vous voulez autoriser le trafic provenant de n'importe quel client sur Internet si vous exécutez un service web public, mais vous pourriez encore avoir besoin d'un ensemble de règles pour le trafic sortant.

Et c'est là que la différence entre les pare-feu avec état et sans état intervient.

Donc un pare-feu avec état permettra automatiquement le trafic de retour.

Maintenant, c'est ce qu'est un groupe de sécurité, ce que cela signifie, c'est qu'avec un groupe de sécurité, vous n'avez besoin que de cette règle en haut ici, vous avez besoin d'une règle qui dit que vous allez autoriser le trafic de n'importe quel client sur n'importe quel port, mais vous allez autoriser l'entrée vers le port 80 sur votre serveur web.

Et ensuite le trafic de retour est automatiquement autorisé.

Donc vous n'avez pas à vous soucier du trafic de retour, il va simplement sortir automatiquement, il va être autorisé parce que le pare-feu est assez intelligent pour savoir que cela fait partie de la connexion.

Et donc il autorise simplement ce trafic de retour.

Maintenant, un pare-feu sans état vérifie une règle d'autorisation pour les deux connexions.

Maintenant, c'est ce qu'une ACL réseau fait.

Donc nous avons une ACL réseau, vous avez besoin à la fois de la règle entrante et de la règle sortante.

Donc vous devez vous assurer que vous avez la règle entrante pour le trafic entrant, et la règle sortante pour le trafic sortant.

Même si c'est la même connexion, il ne comprend pas que cela fait partie de la même connexion, il les traite séparément.

Donc il est vraiment important de comprendre ces différences lorsque vous configurez vos ACL réseau.

Maintenant, regardons un groupe de sécurité.

Voici à quoi ressemble un ensemble de règles de groupe de sécurité.

Donc ici, nous avons des règles séparées définies pour le trafic entrant et sortant, ce que nous regardons ici, c'est le trafic entrant.

Maintenant, encore une fois, parce qu'il est avec état, nous n'avons pas à avoir une règle pour le trafic de retour.

Mais nous avons peut-être encore besoin d'une règle sortante pour le trafic sortant de nos instances.

Donc lorsque nos instances qui sont attachées au groupe de sécurité initient des connexions sortantes.

Donc ici, nous pouvons voir que nous avons plusieurs règles utilisant différents protocoles.

Et nous avons le protocole spécifié, la plage de ports, et puis la source.

Et la source dans de nombreux cas peut être soit une adresse IP ou une plage d'adresses IP.

Ou cela peut être un ID de groupe de sécurité également.

Les groupes de sécurité ne prennent en charge que les règles d'autorisation.

Donc il n'y a pas de règle de refus dans un groupe de sécurité.

Essentiellement, il y a une règle de refus implicite à la fin de l'ensemble de règles.

Et il va vérifier une autorisation, et s'il n'y a pas d'autorisation, alors par défaut, il va simplement refuser le trafic.

Comme je l'ai mentionné, un groupe de sécurité peut utiliser une source d'adresse IP, une plage d'adresses IP, ou l'ID de groupe de sécurité de lui-même ou d'un autre groupe de sécurité.

Maintenant, regardons une configuration de meilleure pratique lors de l'utilisation de groupes de sécurité.

Ce que nous avons ici, c'est un sous-réseau public et un sous-réseau privé.

Et nous avons un équilibreur de charge orienté Internet.

Donc celui-ci va distribuer le trafic à nos serveurs web.

Donc nous avons un équilibreur de charge, nous avons un front-end de serveur web.

Donc c'est celui auquel les utilisateurs se connectent depuis Internet.

Et puis il y a une couche d'application qui va traiter les données.

Et cela peut avoir plusieurs serveurs.

Donc nous avons un équilibreur de charge.

Et nous avons besoin que les connexions puissent venir de nos clients sur Internet jusqu'à la couche d'application, elle pourrait alors écrire dans une base de données.

Je ne l'ai pas montré dans ce diagramme.

Donc voyons comment nous configurons cela.

Tout d'abord, nous créons un groupe de sécurité pour le public iob.

Il permet le trafic sur le port 80 pour le service web à partir de n'importe quelle source sur Internet.

Maintenant, en sortie, il a, car il va maintenant créer une connexion au front-end web.

Il a une règle qui permet l'accès sortant au port 80.

Et nous avons spécifié l'ID de groupe de sécurité réel public easy to.

Donc c'est le nom de ce groupe de sécurité.

Donc il ne va permettre le trafic sortant qu'au front-end web, le front-end web permet le trafic uniquement depuis le public lb sur le port 80.

Et puis il a une destination pour le trafic sortant d'un autre groupe de sécurité appelé private lb, et un port de 8080.

Donc c'est ce que cette application particulière écoute.

Le groupe de sécurité private lb permettra à son tour uniquement le trafic entrant depuis le groupe de sécurité public EC to.

Et il ne permettra le trafic sortant qu'au groupe de sécurité private easy to.

Et c'est celui qui contient la couche d'application.

Donc c'est une façon de verrouiller l'accès aux différentes couches de notre application, et de s'assurer que l'application peut parler à d'autres composants mais que rien d'autre ne peut le faire.

Donc c'est la configuration de groupe de sécurité de meilleure pratique.

Maintenant, regardons les ACL réseau.

L'une des premières choses que vous remarquerez est que nous avons des règles entrantes et sortantes.

Encore une fois, et nous avons des règles d'autorisation et de refus.

Donc avec NaCl, vous pouvez avoir un refus explicite, c'est différent des groupes de sécurité.

Rappelez-vous, les groupes de sécurité ne prennent en charge que les règles d'autorisation.

Les règles sont traitées dans l'ordre.

Donc vous pouvez voir qu'elles sont numérotées.

Donc nous numérotons généralement nos règles.

Et vous pourriez vouloir dire que les règles suivantes que vous ajoutez sont 202 101.

Et puis 303 101, vous pourriez élaborer votre propre processus pour la façon dont vous attribuez ces numéros, mais rappelez-vous simplement qu'ils seront traités dans l'ordre.

Maintenant, les faits importants à ce sujet signifient que une fois que vous atteignez effectivement une règle qui autorise ou refuse le trafic, le traitement s'arrête là.

Donc si nous avons une règle d'autorisation à 100, qui autorise le trafic, alors même si vous aviez une règle de refus plus tard dans l'ensemble de règles pour ce trafic spécifique, il n'ira pas là, il va l'autoriser parce qu'il atteint DLL et le traitement se termine.

Donc vous devez être très prudent avec la façon dont vous configurez vos règles, l'ordre dans lequel vous les créez, et rappelez-vous simplement qu'elles seront traitées dans l'ordre, et ensuite lorsqu'une autorisation ou un refus est atteint, c'est la fin du traitement, il autorisera ou refusera la connexion.

Donc c'est tout pour la théorie.

Dans la prochaine leçon, nous allons faire un peu de pratique et configurer nos groupes de sécurité et nos ACL réseau.

Salut les gars, dans cette leçon, nous allons utiliser des groupes de sécurité et des ACL réseau.

Et nous devrions déjà avoir quelques instances en cours d'exécution depuis le début de cette section.

Donc vous devriez avoir trois instances en cours d'exécution, deux dans un sous-réseau public, et une dans un sous-réseau privé.

Et ce que nous allons faire, c'est tester diverses configurations de groupes de sécurité et d'ACL réseau.

Maintenant, la première chose que je dois faire dans EC2 est d'aller dans les groupes de sécurité.

Et je vais créer un nouveau groupe de sécurité.

Donc nous avons le web public.

Maintenant, nous allons créer le privé app.

Donc ce groupe de sécurité va s'appeler private dash app.

Je lui ai donné une description.

Et choisissons mon VPC pour le VPC.

Maintenant, quelle sera la règle ici ? Eh bien, je vais en fait supprimer les règles sortantes que nous avons déjà configurées, nous avons donné un accès Internet à cette instance particulière auparavant.

Donc nous avons pu télécharger httpd lorsque nous avons installé le service web.

Mais pour l'instant, je vais supprimer les règles sortantes, ce qui signifie qu'à partir de maintenant, il ne pourra plus se connecter à Internet. Pour les règles entrantes, ce que je veux faire est d'utiliser HTTP.

Donc faisons simplement défiler, trouvons HTTP, c'est le protocole pour le serveur web.

Et pour la source, ce que je vais faire ici est de taper s, G.

Et je peux voir mon accès web public.

Donc je fais la meilleure pratique ici, ce que je veux faire est de m'assurer que le serveur web dans notre application ici ne va permettre que les connexions qui proviennent des serveurs web en front-end, les serveurs web publics dans ce groupe de sécurité.

Donc créons ce groupe de sécurité.

Maintenant, nous devons l'assigner à notre instance.

Donc choisissons private one, B, allons dans actions, sécurité, changer les groupes de sécurité.

Et nous allons supprimer public web.

Et nous allons choisir private app, cliquer sur Ajouter un groupe de sécurité, et puis cliquer sur Sauvegarder.

Super, donc cela devrait être configuré correctement.

Maintenant, la première chose que je veux faire, cependant, est de tester l'accès au groupe de sécurité sur notre front-end.

Donc ce que je vais faire est d'aller dans les groupes de sécurité, de choisir le groupe de sécurité public web.

Et sous les règles entrantes, je vais modifier les règles entrantes.

Et ce que je veux faire ici est de changer de tout le trafic.

Et encore une fois, nous allons choisir uniquement HTTP.

Nous allons supprimer la source quelconque, et nous allons spécifier mon IP.

Donc ce que cela fera, c'est qu'il récupérera mon adresse IP.

Et cela signifie que je pourrai me connecter via Internet à ce service web particulier.

Maintenant, j'utilise en fait un VPN et nous allons le changer dans un moment.

Donc si vous avez accès à un VPN, vous pourrez le faire également.

Sinon, cela peut être un peu difficile à moins d'avoir plusieurs IP publiques.

Mais je veux simplement vous montrer le concept de toute façon.

Donc sauvegardons simplement cette règle, revenons aux instances, prenons l'adresse IP publique.

Et dans un navigateur, appuyons simplement sur Entrée.

Et cela a l'air super.

Donc j'ai accès à cette instance.

Maintenant, ce que je vais faire, c'est simplement entrer et changer mon VPN ici.

Donc je me connecte à un service différent.

Et cela signifie que j'ai une IP différente maintenant.

Donc rafraîchissons simplement la page.

Maintenant, vous ne voyez rien se passer.

Mais si vous regardez en haut dans la barre du navigateur ici, nous pouvons voir que nous essayons de nous connecter et c'est ce qui se passe avec les groupes de sécurité.

Lorsque vous ne pouvez pas vous connecter, cela reste en suspens pendant un certain temps et finit par expirer.

Donc cela fonctionne définitivement.

Nous ne sommes pas en mesure d'accéder à l'instance maintenant.

Si je reviens aux groupes de sécurité, et ce que je préfère faire est de choisir mon groupe de sécurité public web, de modifier les règles entrantes.

Et au lieu de cela, je vais changer cela en n'importe quelle ipv4, car c'est un service web.

Donc nous voulons que n'importe qui sur Internet puisse se connecter.

Donc sauvegardons simplement cette règle.

Et ici, la connexion a échoué, rafraîchissons.

Et maintenant nous sommes de retour.

Donc c'est une bonne configuration.

Maintenant, notre service web permet uniquement HTTP depuis Internet.

Et ensuite, il devrait pouvoir transférer vers le service d'application, grâce aux règles de groupe de sécurité que nous avons configurées auparavant.

Donc testons cette couche.

Maintenant, dans EC2, allons dans les instances.

Et ce que je veux faire ici, c'est me connecter à mon instance public one, via instance connect.

Et je vais vérifier l'adresse IP privée de mon instance dans mon sous-réseau privé.

Et c'est 10 04148.

Maintenant, je viens de remarquer une des choses que nous avons faites ici, nous avons sécurisé, donc nous nous sommes verrouillés.

Maintenant, si vous cliquez simplement sur cette note ici, cela vous amène à un article.

Et nous pouvons voir que nous avons en fait besoin du port 22 depuis notre adresse IP pour pouvoir accéder à l'instance.

Donc revenons et configurons cela comme une configuration sécurisée.

Donc en revenant dans les groupes de sécurité, ce que nous devons faire est d'aller dans public web, de modifier les règles entrantes, d'ajouter une règle.

Et celle-ci peut être SSH.

Et ce que nous allons faire ici, c'est simplement ajouter n'importe quelle adresse Internet car je pourrais changer mon adresse Internet quelques fois.

Donc sinon, bien sûr, vous pourriez utiliser mon IP, ou avoir une plage d'adresses que vous faites confiance, ce qui serait une configuration plus sécurisée.

Mais pour l'instant, nous allons changer les IP.

Donc je suis content d'avoir cela ouvert.

Donc sauvegardons ces règles.

Maintenant, essayons de relancer cette connexion Instance Connect, et nous sommes connectés.

Donc la façon dont je veux essayer de tester que nous pouvons nous connecter à notre couche AP est d'utiliser curl dash s et puis de mettre l'IP 10 04 dash 148.

Appuyons sur Entrée, et nous obtenons une réponse.

Donc c'est super.

Maintenant, rappelez-vous, nous n'avions pas de règle sortante depuis ce groupe de sécurité.

Donc le trafic de réponse revient purement parce que c'est un pare-feu avec état.

Donc c'est tout pour les groupes de sécurité.

Passons à la configuration d'une ACL réseau dans la console de gestion VPC.

Allons dans les ACL réseau.

Et ce que nous verrons, c'est qu'il y a déjà des ACL réseau.

Donc nous en avons une ici pour notre VPC personnalisé.

Maintenant, allons-y et regardons la configuration.

Donc nous avons des règles entrantes, nous avons une règle numéro 100, permettant tout le trafic entrant.

Et puis à la fin, nous avons une règle de refus.

Donc rappelez-vous, celles-ci sont traitées dans l'ordre.

Donc dans ce cas, tout est autorisé à cause de la règle d'autorisation.

Donc la règle de refus n'est pas traitée.

En sortie, nous avons exactement la même chose.

Donc essayons quelque chose, ce que je vais faire est de modifier les règles entrantes.

Et je vais ajouter une règle.

Et je vais en faire une sur un.

Et ce que je vais faire est de spécifier HTTP, la source sera mon adresse IP.

Donc je sais que mon adresse IP est celle-ci pour l'instant.

Donc je mets slash 32 pour une correspondance exacte.

Et je vais cliquer sur refus.

Donc je vais refuser l'accès depuis cette adresse IP particulière à http.

Maintenant, pensez-vous que cela va fonctionner ? Espérons que vous réalisez qu'il y a une erreur ici, mais modifions simplement les changements.

Et nous allons vérifier cela.

De retour dans EC2.

Je vais simplement copier l'IP publique de mon instance, aller à une nouvelle page web, appuyer sur Entrée, et j'ai accès.

Donc bien sûr, cela n'a pas fonctionné.

Maintenant, allons voir pourquoi.

De retour dans la console de gestion VPC, modifions ces règles pour l'ACL réseau.

Maintenant, comme vous le savez, les règles sont traitées dans l'ordre.

Donc nous avons une règle de refus ici qui est après une règle d'autorisation, l'autorisation autorise tout.

Donc en fait, cela ne va pas fonctionner.

Changeons cela en 99, trions par ordre de règle.

Et maintenant nous avons un refus spécifique avant une autorisation.

Donc essentiellement, il va parcourir l'ensemble de règles, il va voir que le trafic arrive sur le port 80 depuis cette IP particulière, et il va le refuser.

Donc nous n'atteignons jamais la règle d'alarme pour ce trafic particulier.

Donc sauvegardons les changements.

Donc nous allons tester cela maintenant.

Mais il y a une chose que vous devez comprendre avec les règles de groupe de sécurité, lorsqu'elles sont appliquées, elles entrent effectivement en vigueur presque immédiatement, il peut y avoir un peu plus de retard avec une ACL réseau.

Donc si vous trouvez que vous avez toujours accès à votre instance, c'est probablement juste parce que vous êtes un peu trop rapide.

Donc donnez-lui quelques minutes et réessayez.

Et nous devrions constater que nous sommes refusés dans une fenêtre de navigateur ici.

Collons notre adresse IP.

Et effectivement, il semble qu'elle soit en suspens.

Donc clairement, cela ne fonctionne pas.

Maintenant, que se passe-t-il si je change mon IP ? Cette fois, je peux changer pour un endroit différent et très rapidement, cette fois, la connexion a effectivement changé, et elle m'a permis d'entrer.

Donc parfois les règles de l'ACL réseau s'appliquent super vite.

Et parfois il y a un peu de retard.

Donc cela peut vraiment varier.

Donc cela vous montre comment utiliser une règle de refus avec une ACL réseau.

Maintenant, je vais simplement revenir et nettoyer cette règle.

Donc je ne veux pas avoir de règles de refus dans mon ACL réseau.

Donc supprimons simplement celle-ci des règles entrantes, et sauvegardons les changements.

Maintenant, il y a quelques choses que nous pouvons nettoyer maintenant pour nous assurer que nous n'avons pas de factures.

Tout d'abord, allons à notre passerelle NAT, celles-ci peuvent coûter de l'argent.

Donc supprimons simplement cette passerelle NAT.

Et elle est partie.

Et n'oubliez pas, vous devrez également vous assurer que l'IP élastique a également été supprimée de votre compte dans EC2. Maintenant, je veux garder une instance publique et une instance privée.

Mais je peux terminer l'autre instance publique.

Maintenant, nous utiliserons en fait la ligne de commande pour cela, je veux simplement vous montrer une autre commande ci.

De retour dans notre fichier ici, nous pouvons spécifier les valeurs pour nos instances DC2.

Donc j'en ai juste une ici.

Donc je vais la mettre entre guillemets.

Copiez cette commande, et dans ma ligne de commande, essayons simplement de terminer cette instance.

Et lorsque vous faites cela, vous voyez que l'état actuel est en cours d'arrêt, et l'état précédent était en cours d'exécution.

Donc nous savons maintenant que notre instance EC2 est en cours de terminaison.

Donc c'est tout pour l'instant, mais laissez ces deux autres instances en cours d'exécution car nous les utiliserons dans les leçons suivantes.

Bonjour et bienvenue à cette leçon.

Il y a plusieurs circonstances où nous pourrions vouloir connecter des machines qui fonctionnent dans différents VPC ensemble en utilisant IPv4 ou IPv6.

Par exemple, nous pourrions avoir deux VPC, qui pourraient être dans la même région.

Cela pourrait être dans une région différente ou même un compte différent.

Et nous voulons que les instances EC2 dans ces deux VPC puissent communiquer en utilisant des adresses IPv4 privées ou peut-être des adresses IPv6.

Maintenant, une façon de faire cela est d'utiliser l'appairage VPC.

L'appairage VPC permet le routage de ces adresses en interne entre ces VPC.

Et lorsque je dis en interne, ce que je veux dire, c'est qu'il ne sort pas sur Internet.

Il utilise le réseau global AWS pour router le trafic entre le VPC, donc il ne touche jamais Internet.

Il est crypté lorsqu'il se déplace entre les régions, et il utilise des adresses IPv4 privées ainsi que des adresses IPv6.

Donc c'est une technologie géniale pour de nombreux cas d'utilisation.

Regardons comment nous pouvons utiliser l'appairage VPC.

Donc disons que nous avons un VPC, c'est le VPC A, et puis nous avons un autre VPC, le VPC B, et nous voulons pouvoir router les connexions entre ces deux.

Donc nous avons des instances EC2, peut-être des bases de données RDS, même des fonctions lambda, tout ce qui communique à l'intérieur d'un VPC et nous voulons pouvoir connecter ces ressources ensemble en utilisant des adresses IPv4 privées.

Donc ce que nous pouvons faire, c'est établir une connexion d'appairage VPC entre ces deux VPC.

Cela permettra le routage en utilisant des adresses IPv4 privées, ou des adresses IPv6.

Maintenant, les blocs CIDR de nos VPC ne doivent pas se chevaucher.

Donc c'est une considération très importante lorsque vous choisissez les blocs CIDR à utiliser pour vos VPC.

Parce que même s'ils sont dans des comptes différents, vous pourriez un jour vouloir connecter vos VPC ensemble.

Et s'ils ont les mêmes blocs CIDR ou des blocs CIDR qui se chevauchent, alors cela ne fonctionnera pas.

Donc vous devez avoir des blocs CIDR qui ne se chevauchent pas.

Maintenant, que se passe-t-il si nous avons un autre VPC, le VPC C et le VPC D, un quatrième ? Donc ils ont tous leur propre bloc CIDR, donc cela a l'air bien.

Nous pouvons définitivement configurer l'appairage VPC entre ceux-ci.

Donc ce que faisons-nous, nous établissons une connexion d'appairage VPC entre le VPC A et le VPC C, entre le VPC B et le VPC D, et puis avec le VPC C et le VPC D.

Donc nous avons maintenant quatre ensembles de connexions d'appairage configurés.

Mais le problème avec l'appairage VPC est qu'il ne supporte pas l'appairage transitif.

Maintenant, ce que cela signifie, c'est, disons que nous avons des ressources dans le VPC A, et il a une connexion d'appairage avec le VPC B.

Le VPC B a ensuite une connexion d'appairage avec le VPC D.

Donc cela signifie-t-il que le VPC A peut communiquer avec les ressources dans le VPC D en passant par le VPC B ? Eh bien, non, cela ne fonctionne pas.

Le routage transitif ne fonctionne pas.

Donc ce que nous devons faire, c'est configurer deux autres connexions d'appairage.

Nous avons maintenant une connexion d'appairage entre A et D, et entre B et C.

Donc nous avons une topologie en maillage complet.

Parce que l'appairage VPC ne supporte pas les relations transitives.

Nous avons besoin de ce maillage complet.

Donc cela devient assez complexe.

Maintenant, avec ces quatre VPC, ce n'est pas trop grave.

Mais vous pouvez imaginer que si vous étendez cela à beaucoup plus de VPC, bientôt cette topologie en maillage complet signifie que vous avez un grand nombre de connexions à configurer et à gérer.

Donc cela devient un peu ingérable.

Et il existe d'autres solutions, que nous allons examiner plus tard dans la section et dans les sections à venir.

Maintenant, comme je l'ai mentionné auparavant, les VPC peuvent être dans des comptes différents, et ils peuvent également être dans des régions différentes.

Maintenant, regardons un peu plus en détail comment nous configurons cela.

Donc nous avons la région un, et nous avons la région deux.

Donc dans cet exemple, nous avons deux VPC dans différentes régions, cela peut être dans le même compte ou dans des comptes différents, et nous voulons les apparier ensemble.

Maintenant, ils ont chacun leur propre bloc CIDR, qui sont uniques, ils ne se chevauchent pas, donc c'est bien.

Et puis nous avons quelques sous-réseaux.

Maintenant, ceux-ci peuvent être des sous-réseaux privés ou publics.

Parce que rappelez-vous, ce sont les adresses privées des instances qui seront utilisées pour la communication VPC à VPC.

Et nous avons quelques instances en cours d'exécution dans ces sous-réseaux.

Maintenant, je montre public parce que nous allons configurer un labo très similaire à celui-ci, cela nous facilite la connexion à nos instances EC2 si elles sont dans des sous-réseaux publics.

Donc nous créons une connexion d'appairage VPC.

Et je vais vous montrer comment faire cela dans la console.

Maintenant, la prochaine chose que nous devons faire est de configurer nos groupes de sécurité.

Donc disons que nous voulons utiliser le protocole ICMP pour envoyer une requête ping d'une instance à une autre, et l'autre instance en retour.

Eh bien, dans ce cas, nous devons également configurer des règles de groupe de sécurité.

Et nous pouvons utiliser le CIDR de l'autre région.

Donc nous pouvons utiliser le bloc CIDR comme source et dire que tout ce qui provient de ce bloc CIDR sera autorisé en fonction de cette règle.

Maintenant, une autre chose que nous devons configurer pour que cela fonctionne est les tables de routage.

Et ce que nous faisons, c'est que nous avons une route de destination, qui va au bloc CIDR du VPC distant.

Et nous spécifions les ID d'appairage, lorsque nous configurons la connexion d'appairage, nous aurons un ID d'appairage, et nous allons spécifier cela comme cible.

Et puis nous faisons l'inverse de l'autre côté, donc la table de routage enverra tout trafic destiné à ce bloc CIDR à la connexion d'appairage, et puis il est routé vers le VPC correct.

Salut les gars, dans cette leçon, nous allons créer une connexion d'appairage VPC entre deux VPC dans deux comptes différents.

Donc la configuration va être à peu près ce que nous voyons à l'écran ici, nous avons notre compte de gestion dans notre organisation AWS et notre compte de production.

Et nous allons avoir un VPC dans chacun utilisant ces blocs CIDR.

Et puis nous allons créer des groupes de sécurité.

Et nous allons spécifier ces règles particulières.

Maintenant, tout d'abord, voyons comment nous établissons la connexion, nous devons établir une connexion d'appairage entre les VPC, et nous pouvons le faire dans la console.

Ensuite, nous devons mettre à jour la table de routage, il est vraiment important que vous ayez une route vers votre cible.

Donc la table de routage de ce VPC doit spécifier comme destination le bloc CIDR de l'autre VPC et la cible d'appairage, et ensuite l'inverse est vrai.

Sur le côté droit.

Nos règles de groupe de sécurité permettront d'utiliser SSH et ICMP pour se connecter et la façon dont nous testerons la connectivité est de faire un ping d'une instance à l'autre en utilisant l'adresse IP privée et cela nous montrera que nous utilisons la connexion d'appairage VPC et non Internet.

Maintenant, il y a un peu de travail de fond que vous devez faire avant de commencer.

Donc, à moins que vous ne souhaitiez utiliser le VPC par défaut dans votre compte de production, vous devez créer un nouveau VPC en utilisant les mêmes plages que je viens de vous montrer.

Donc, à partir de la console de gestion VPC, vous allez vouloir changer pour DCT production, aller dans vos VPC et puis créer un VPC.

J'ai déjà créé le mien, et j'ai les valeurs pour vous dans un fichier.

Donc, ouvrez simplement le code Amazon VPC, le fichier custom VPC dash prod, et voici les informations dont vous avez besoin.

Vous savez comment faire cela, vous l'avez fait plus tôt dans cette section.

Donc, créez simplement ce VPC et ajoutez les sous-réseaux.

Ajoutez votre passerelle Internet, votre table de routage privée, et ensuite nous sommes prêts à partir.

Maintenant, nous n'avons pas besoin de tout cela pour cet exercice particulier, mais créons-le standard comme le VPC dans notre compte de gestion, et ensuite nous pourrions utiliser certains de ces sous-réseaux plus tard.

Donc, commençons.

Maintenant, j'ai besoin de quelques informations.

Avec mon VPC sélectionné dans mon compte de production.

Je vais copier cet ID de propriétaire, c'est l'ID du compte et je vais le mettre dans mon fichier.

Ensuite, j'ai besoin de l'ID du VPC et mettons cela dans le fichier.

Maintenant, nous allons revenir au compte de gestion.

Allons dans les connexions d'appairage, créons une connexion d'appairage.

Nous devons lui donner un nom.

Appelons-le simplement mon pair.

Sélectionnez le VPC local, qui est mon VPC, nous pouvons choisir un autre compte plutôt que mon compte et copier cet ID de compte.

Nous allons le coller.

Nous allons rester dans la même région, mais nous avons besoin de l'ID du VPC de l'autre côté également.

Donc c'est celui que nous avons copié ici.

Donc copions cela dans notre presse-papiers, collons-le et créons la connexion d'appairage.

Donc il est dit ici qu'une connexion d'appairage VPC, PC x, puis il va numéroter mon pair a été demandée, le propriétaire du VPC distant doit accepter la connexion d'appairage.

Donc revenons et faisons cela.

Allons à DCC production, allons dans les connexions d'appairage, et nous pouvons voir la demande en attente d'acceptation.

Donc sélectionnez-la à gauche, puis allez dans actions, accepter la demande.

Et nous pouvons accepter celle-ci.

Et c'est fait.

Maintenant, l'une des choses dont nous allons avoir besoin pour tester est une instance EC2.

Donc lançons une instance EC2.

Mais avant de lancer celle-ci, je vais créer le groupe de sécurité, le groupe de sécurité va s'appeler VPC pair dash prod.

Et ce sont les règles que nous allons configurer.

Donc créons un groupe de sécurité.

Donnons-lui un nom.

Je viens de mettre cela dans la description également.

Choisissez le VPC correct et la règle sortante est correcte.

Pour l'instant.

Tout ce dont nous avons besoin, c'est que les règles entrantes soient configurées.

La première règle que je vais configurer est ICMP ipv4.

Donc tout ICMP qui va permettre les requêtes ping, et cela va venir de 10.0.0.0/16.

La ligne suivante est SSH, vous pouvez soit faire un TCP personnalisé et mettre la plage de ports, soit choisir SSH, et il le fera pour vous.

Et comme celui du dessus, nous voulons simplement lui donner les mêmes adresses.

Donc cela devrait permettre les connexions entrantes depuis le VPC dans l'autre compte dans le compte de gestion en utilisant n'importe quelle adresse IP dans le bloc CIDR entier.

Donc nous pouvons sauvegarder le groupe de sécurité.

Maintenant, lançons une instance qui utilise ce groupe de sécurité.

Donc je vais lancer une instance, ce sera l'AMI Linux 2, T2 micro, assurez-vous de sélectionner votre VPC, je vais la mettre dans mon sous-réseau public public one a.

Cliquons sur Suivant, allons dans le groupe de sécurité.

Et nous allons sélectionner un groupe de sécurité.

Et ce sera VPC peer prod, cliquons sur Examiner et lancer et lançons.

Si vous n'avez pas de paire de clés pour cette région, ce que je n'ai pas à ce stade, alors je vais en créer une nouvelle.

Je l'ai appelée prod dash et V ou téléchargez cette paire de clés et puis lancez mon instance.

Donc maintenant, revenons dans la console de gestion de la ville au compte de gestion.

Dans le compte de gestion, nous devons configurer ce groupe de sécurité et nous allons l'assigner à l'une de nos instances dans un sous-réseau public.

Donc dans ce compte, nous avons deux instances en cours d'exécution, allons dans les groupes de sécurité, créons un groupe de sécurité.

Il s'appelle VPC, pair dash MGMT.

Je vais mettre la même chose dans la description, sélectionner le VPC correct.

Et puis ajoutons les mêmes règles que précédemment.

Cette fois, le bloc sera 10.1.0.0/16.

Donc maintenant nous avons le même protocole spécifié, donc nous devrions pouvoir nous connecter depuis le VPC prod vers le VPC de gestion en utilisant ces protocoles également.

Donc créons ce groupe de sécurité.

Retour aux instances public one a actions sécurité, changer les groupes de sécurité.

Et nous allons ajouter VPC pair dash MGMT.

Et la raison pour laquelle je ne vais pas supprimer public web est parce que nous avons une règle qui permet l'accès depuis Internet au port 22, dont nous avons besoin pour instance connect.

Donc avec ces deux ajoutés, sauvegardons la configuration du groupe de sécurité.

Et la toute dernière chose que nous ne voulons pas oublier, ce sont nos tables de routage.

Donc allons faire cela.

Maintenant.

De retour dans la console VPC pour mon compte de gestion, je vais aller dans ma table de routage principale, choisir les routes, modifier, ajouter, celle-ci sera 10.1.0.0/16.

Et elle ira via une connexion d'appairage.

Nous n'en avons qu'une seule, et elle s'appelle mon pair.

Donc sauvegardons cela, basculons vers le compte DCT production.

Nous devons choisir la table de routage principale.

Je n'ai pas étiqueté celle-ci.

Faisons-le maintenant.

Mais je peux voir qu'elle est attachée à mon VPC.

Donc allons dans les routes, modifions les routes, ajoutons.

Et celle-ci devrait être pour 10.0.0.0/16.

Et encore une fois, nous allons spécifier la connexion d'appairage, elle va voir la même connexion d'appairage, et nous pouvons sauvegarder les changements.

Donc c'est tout, espérons que tout est configuré.

Maintenant que nous avons mis à jour nos tables de routage.

Nous avons ces deux groupes de sécurité avec des règles pour que nous devrions pouvoir utiliser ces protocoles basés sur nos adresses IP privées.

Donc c'est le vrai test, utiliser des adresses IP privées pour voir si nous pouvons nous connecter, nous pouvons définitivement faire un ping via les IP publiques si nous avons correctement configuré nos règles de groupe de sécurité, mais nous voulons le faire via des IP privées car cela montre que plutôt que de sortir vers une passerelle Internet, nous restons dans l'espace privé à travers la connexion d'appairage, de retour dans EC2, sélectionnons l'ID de l'instance, et nous voulons copier l'adresse IP privée, je vais simplement la mettre dans mon fichier ici.

Et en revenant ici, basculons vers le compte de gestion.

Choisissons l'instance public one a, connectons-nous via instance Connect.

Et essayons simplement de nous souvenir de cette IP 10 11221.

Donc faisons un ping à 10.1.1.2 to one et appuyons sur Entrée.

Et voilà, nous obtenons une réponse.

C'est à travers les comptes.

Et c'est aussi à travers les régions.

Et cela montre que nous avons ce trafic bidirectionnel entre ces deux VPC.

L'autre protocole que nous avons activé était SSH.

Donc assurons-nous simplement que nous pouvons créer une connexion SSH 10.1.1.2 to one.

Et nous pouvons maintenant, je ne vais pas vraiment me connecter, car j'ai besoin de ma paire de clés.

Et je devrais spécifier plus de détails également.

Mais je veux juste voir que le port est ouvert.

Et cela montre que les groupes de sécurité sont configurés correctement, ainsi que le réseau sous-jacent pour permettre ce trafic via des adresses IP privées.

Donc c'est vraiment tout pour cette leçon.

La seule autre chose que vous pourriez vouloir faire est que vous pouvez pratiquer en faisant la même chose et en étendant cette configuration jusqu'à votre instance dans votre sous-réseau privé.

Utilisez votre instance de sous-réseau public comme hôte bastion, vous devrez peut-être utiliser le transfert d'agent, puis assurez-vous de pouvoir vous connecter bidirectionnellement depuis là également.

Donc c'est juste un peu de plaisir supplémentaire que vous pourriez avoir si vous voulez pratiquer un peu plus.

Maintenant que nous avons terminé avec ce labo, nous pouvons en fait terminer notre instance, dans le sous-réseau privé.

Nous ne l'avons pas utilisée dans ce labo, sauf si vous avez continué avec la configuration.

Mais nous allons laisser l'instance publique en cours d'exécution pour l'instant.

Donc terminons cette instance.

Et puis vous devriez aller dans votre environnement de production et terminer votre instance EC2 là-bas, et ensuite nous sommes tous nettoyés.

Vous vous souviendrez que plus tôt dans le cours, j'ai parlé de la façon dont certains services AWS sont privés en ce sens qu'ils s'exécutent dans un VPC comme EC2, tandis que d'autres services sont publics car ils ont un point de terminaison public comme Amazon S3, par exemple.

Donc cela signifie que lorsque vous vous connectez à Amazon S3, vous utilisez un nom DNS public, donc vous vous connectez à celui-ci en tant que point de terminaison public.

Maintenant, que se passe-t-il si vous voulez connecter une instance à Amazon S3, mais que vous ne voulez pas utiliser l'Internet public, cela pourrait être une instance dans un sous-réseau privé.

Eh bien, c'est là que les points de terminaison VPC entrent en jeu.

Et il y a quelques cas d'utilisation pour les points de terminaison VPC, la connexion privée à S3 en étant un.

Et il y a deux types différents.

Il y a un point de terminaison d'interface VPC et un point de terminaison de passerelle VPC, le point de terminaison de passerelle est celui que nous pouvons utiliser pour S3.

Et le point de terminaison d'interface est légèrement différent, il est utilisé pour d'autres services.

Donc commençons par là.

Tout d'abord, regardons un exemple utilisant un point de terminaison d'interface VPC.

Donc nous avons une instance EC2 en cours d'exécution dans un sous-réseau privé.

Et nous ne voulons pas que cette instance ait une IP publique.

Et nous ne voulons pas qu'elle soit routée vers Internet via une passerelle NAT.

Donc nous provisionnons un point de terminaison d'interface, qui crée une AMI dans le sous-réseau.

Et ensuite l'instance peut se connecter via cette AMI à des services publics, mais elle utilise des adresses IP privées pour se connecter à eux.

Maintenant, chaque point de terminaison d'interface peut se connecter à l'un des nombreux services AWS.

Et vous pouvez vous connecter à un service alimenté par AWS Private Link.

Nous allons examiner cela brièvement pour voir ce que cela signifie.

Donc c'est une façon dont nous pouvons connecter nos instances EC2 à ces services en utilisant des adresses IP privées.

Maintenant, regardons la différence entre cela et un point de terminaison de passerelle.

Donc dans ce cas, je veux me connecter à Amazon S3 pour stocker des données dans un bucket S3.

Et encore une fois, je ne veux pas avoir d'adresse IP publique.

Donc une instance dans un sous-réseau public, dans ce cas, elle est dans un sous-réseau privé.

Et je ne veux pas provisionner une passerelle NAT, ou du moins je ne veux pas que ce trafic aille sur Internet.

Donc je pourrais provisionner un point de terminaison de passerelle S3.

Cela est légèrement différent.

Il utilise une entrée de table de routage.

Donc nous devons maintenant mettre une entrée de table de routage pour pointer notre trafic vers les points de terminaison de la passerelle S3.

Et cela utilise la liste de préfixes pour S3 et l'ID de la passerelle.

L'instance se connecte à nouveau en utilisant une adresse IP privée à la passerelle de terminaison.

Et de là, elle se connecte à Amazon S3.

Maintenant, vous pouvez sécuriser cela avec des politiques Im, donc vous pouvez appliquer une politique au point de terminaison.

Et vous pouvez également appliquer des politiques de bucket.

Par exemple, vous pouvez avoir une politique de bucket qui limite l'accès à tout trafic provenant du point de terminaison de la passerelle.

Donc vous avez maintenant un bucket qui n'acceptera le trafic que des instances utilisant le point de terminaison de la passerelle S3.

Donc faisons simplement un récapitulatif des différences avec le point de terminaison d'interface.

Vous avez une interface réseau élastique avec une IP privée avec un point de terminaison de passerelle, vous avez une cible dans votre table de routage pour la passerelle.

Donc les points de terminaison d'interface, nous utilisons des entrées DNS pour rediriger le trafic, tandis que les points de terminaison de passerelle utilisent la liste de préfixes dans la table de routage pour rediriger le trafic.

Maintenant, quels services ? Eh bien, il y en a quelques-uns avec un point de terminaison d'interface, API Gateway, CloudFormation.

Et CloudWatch ne sont que quelques exemples.

Beaucoup de services publics peuvent être accessibles via un point de terminaison d'interface.

Mais un point de terminaison de passerelle est restreint à Amazon S3 et DynamoDB.

Seulement avec un point de terminaison d'interface, vous utilisez des groupes de sécurité pour contrôler le trafic, tandis qu'avec un point de terminaison de passerelle, vous pouvez utiliser des politiques de point de terminaison VPC.

Maintenant, enfin, regardons comment nous pouvons utiliser cela dans un modèle de fournisseur de services.

Donc ce que je veux dire, c'est que nous avons un VPC consommateur et un VPC fournisseur de services.

Donc nous avons quelques sous-réseaux dans chaque VPC.

Et ce qui se passe, c'est que le fournisseur de services crée un service.

Et ce service est derrière un équilibreur de charge réseau.

Et ils veulent fournir ce service aux consommateurs.

Donc ce qui se passe en tant que consommateur, c'est que vous provisionnez un point de terminaison, et ensuite vous utilisez ce point de terminaison pour accéder au service.

Donc nous publions en fait un service d'un côté, et ensuite nous le consommons dans le VPC de gauche, et nous utilisons un point de terminaison d'interface pour consommer ce service.

Donc c'est comme ça que ça marche.

Et dans la prochaine leçon, nous allons configurer un point de terminaison de passerelle.

Bienvenue dans une autre session pratique. Dans cette leçon, nous allons créer un point de terminaison VPC, ce sera un point de terminaison de passerelle.

Et nous allons utiliser certaines politiques pour voir comment nous pouvons contrôler l'accès à un bucket Amazon S3.

Donc voici la configuration que nous avons déjà un VPC et un sous-réseau public, et nous avons une instance en cours d'exécution.

Maintenant, nous allons créer un bucket Amazon S3.

Je m'avance un peu ici, car nous couvrons S3 en détail dans la prochaine section.

Si vous n'êtes pas du tout familier avec cela, et que vous voulez une introduction, vous pourriez avancer, mais nous ne ferons pas trop ici, ce sera assez simple.

Maintenant, lorsque nous créons notre point de terminaison, une route sera ajoutée à notre table de routage.

Et cela pointera vers une destination qui se résoudra aux adresses IP d'Amazon S3.

Maintenant, ce qui se passe, c'est que c'est une route plus spécifique que toute autre route, comme la route allant vers Internet.

Donc elle devrait suivre ce chemin, ce qui signifie que toute connexion allant vers les points de terminaison AWS S3 devrait être routée via le point de terminaison de la passerelle, et nous serons en mesure de prouver que cela se produit, et que nous n'utilisons pas l'Internet public.

Donc nous modifierons la politique ici pour faire cela, vous verrez ce que je veux dire bientôt.

Et sur le bucket S3, nous ajouterons une politique.

Maintenant, les politiques de bucket sont essentiellement des politiques basées sur les ressources.

Cela utilise le langage JSON, tout comme nous le faisons avec les politiques IAM, mais nous les utilisons simplement pour contrôler l'accès à nos buckets.

Donc nous les appliquons directement au bucket, plutôt qu'à un principe comme une politique basée sur l'identité.

La première chose à faire est de se rendre et de créer le point de terminaison VPC.

Je suis dans mon compte de gestion en Virginie du Nord.

Ici, à gauche, sous les points de terminaison, nous pouvons créer un point de terminaison.

Cliquons sur ce bouton Créer un point de terminaison.

Et sous les services, si nous mettons s3 et recherchons, nous obtenons ces options, nous allons choisir la passerelle pour Amazon S3.

Maintenant, nous devons spécifier quelle table de routage nous allons réellement mettre à jour.

Maintenant, comme vous pouvez le voir, la table de routage pour notre VPC, celle personnalisée n'est pas là.

C'est parce que nous devons nous assurer que nous spécifions notre VPC personnalisé.

Maintenant, nous pouvons voir nos tables de routage.

Et je vais choisir celle qui est la table de routage principale.

Donc c'est celle associée à mes sous-réseaux publics.

Maintenant, la politique par défaut est l'accès complet.

Donc nous avons une déclaration ici, qui est l'action, n'importe quelle action star effets autoriser, et puis n'importe quelle ressource et n'importe quel principal.

Donc c'est très ouvert, mais vous pouvez le personnaliser.

Donc créons simplement le point de terminaison, et il est créé pour nous.

Donc voici notre point de terminaison.

Maintenant, ce que nous voulons faire est d'aller dans les tables de routage et de nous assurer que la table de routage a été mise à jour.

Donc c'est celle-ci ici, la table de routage principale pour notre VPC personnalisé.

Sous les routes, nous pouvons maintenant voir que nous avons la destination, et celle-ci va virale et les points de terminaison VPC.

Donc c'est la route vers Amazon S3 passant par le point de terminaison.

Donc c'est configuré correctement.

Une autre chose que nous devons faire, nous allons exécuter des commandes contre Amazon S3 depuis notre instance EC2.

Donc je dois lui donner quelques privilèges, je vais créer un rôle.

Donc choisissons Créer un rôle ici dans le service IAM.

Les cas d'utilisation courants seront EC2, donc nous allons permettre à EC2 d'appeler un service AWS pour les permissions, tapez simplement s3 et recherchez.

Et nous allons donner un accès complet.

Je vais copier le nom de cette politique.

Et nous allons utiliser ce nom pour le nom du rôle également.

Donc collons cela, créons le rôle.

Et maintenant nous avons un rôle que nous pouvons assigner à notre instance EC2.

Donc dans EC2, choisissons notre instance, allons dans actions, sécurité, modifier le rôle IAM, et nous allons choisir un rôle et nous devrions le voir ici.

Et le voilà, Amazon S3, accès complet.

Donc sauvegardons une instance maintenant a les privilèges dont elle a besoin.

Dans la console Amazon S3 que vous pouvez trouver sous services et stockage, nous allons créer un bucket S3.

Donc un bucket est simplement un conteneur dans lequel nous ajoutons des objets, des objets ou des fichiers et des vidéos ou ce que vous voulez ajouter.

Je vais l'appeler DCT VPC test, et il sera en Virginie du Nord, je peux faire défiler vers le bas, je n'ai pas besoin de changer autre chose à ce stade et créer ce bucket.

Donc maintenant que nous avons un bucket, nous pouvons ajouter quelques objets, des objets, comme je le dis, sont simplement des fichiers.

C'est un système de stockage basé sur des objets.

Donc nous pouvons entrer et ajouter des fichiers, je vais simplement ajouter quelques images JPEG et télécharger.

Donc aussi simple que cela, nous avons quelques fichiers sur Amazon S3.

Maintenant, revenons à EC2, choisissons notre instance public one a, allons à instance connect et connectons-nous.

Maintenant, nous n'avons pas spécifié de politiques pour l'instant, mais vérifions simplement que nous pouvons nous connecter à Amazon S3.

Maintenant, nous devrions être en mesure d'exécuter des commandes contre S3.

Essayons d'exécuter AWS s3 Ls et appuyons sur Entrée.

Et nous pouvons voir nos buckets, nous devrions être en mesure d'exécuter AWS s3 Ls et puis s3 colon slash slash et le nom de notre bucket aussi.

Et si nous appuyons sur entrer ici, nous devrions voir le contenu du bucket.

Donc pour l'instant, tout fonctionne bien.

Maintenant, comment savons-nous que cela passe par le point de terminaison plutôt que par Internet, car nous sommes dans un sous-réseau public ? Eh bien, revenons à notre point de terminaison.

Avec mes points de terminaison sélectionnés, je vais choisir la politique.

Je vais copier ce code ici dans la politique du point de terminaison, choisir Personnalisé, le coller.

Et changeons simplement la politique pour refuser.

Cela devrait refuser tout.

Maintenant, si nous passons par Internet, cela ne devrait pas faire de différence.

Mais si nous passons par le point de terminaison, alors cela devrait bloquer l'accès.

Donc dans notre instance, essayons de réexécuter cette commande et nous obtenons un accès refusé.

Essayons d'exécuter la commande ls.

Encore une fois, nous obtenons un accès refusé.

Donc cela ne fonctionne définitivement pas, dans mon point de terminaison.

Je vais simplement changer cela à nouveau, car je ne veux pas vraiment que cela me refuse l'accès à ce stade.

Donc revenons à l'accès complet, cliquons sur Enregistrer.

La prochaine chose que nous allons faire est de configurer notre politique de bucket.

Et la politique de bucket va empêcher tout accès sauf depuis le point de terminaison VPC.

Et c'est quelque chose qui revient dans de nombreux scénarios d'examen.

Donc allons dans notre bucket ici.

Allons dans les permissions.

Descendons à la politique de bucket, cliquons sur Modifier, et je vais copier le bucket AR n.

Maintenant, c'est la politique de bucket.

Donc elle se trouve dans votre répertoire de code Amazon VPC, bucket policy VPC, ce que vous devez faire, c'est prendre tout cet AR n ici et simplement coller votre AR n correct par-dessus pour votre bucket.

Et il y a deux options ici.

L'une est sans la barre oblique étoile, et l'autre est avec.

Donc celle avec une barre oblique étoile signifie que vous pouvez également regarder les objets à l'intérieur du bucket.

Maintenant, la dernière chose dont nous avons besoin ici est l'ID du VPC.

Donc de retour à mon point de terminaison ici, je vais copier l'ID du point de terminaison et puis revenir et le coller dans ma politique.

Donc c'est tout, cette politique devrait maintenant s'appliquer.

Maintenant, que fait-elle ? Regardons.

La politique est un refus.

Donc elle va refuser à tout principe toute action S3 sur ces ressources spécifiquement, si la condition n'est pas égale à cet ID de point de terminaison VPC, en d'autres termes, si vous ne venez pas de cet ID de point de terminaison VPC, vous allez être refusé.

Si vous venez de cet ID de point de terminaison VPC, cela ne s'applique pas.

Donc copions tout ce code dans notre presse-papiers.

Et dans l'éditeur de politique de bucket ici, je vais tout coller et simplement sauvegarder ces changements.

Donc revenons et assurons-nous de ne pas avoir cassé l'accès.

Dans notre instance, essayons de réexécuter la commande AWS s3 ls, et nous voyons nos buckets, vérifions que nous pouvons voir à l'intérieur de notre bucket et que cela fonctionne correctement.

C'est bien car cette instance vient du point de terminaison VPC.

Donc encore une fois, nous avons prouvé que nous venons via le point de terminaison.

Mais l'autre chose que nous pouvons faire est de vérifier depuis nos propres ordinateurs.

Et nous ne devrions pas avoir accès.

Donc dans un terminal ici, je vais exécuter AWS s3 Ls.

Et je vois les buckets.

Mais qu'en est-il si j'essaie de voir à l'intérieur du bucket, donc la commande complète est AWS s3 lS s3 colon, slash slash, et puis le nom de votre bucket et appuyez sur entrer.

Donc j'ai un accès refusé.

Donc cela prouve que je ne suis pas en mesure d'accéder au bucket depuis mon ordinateur car je ne viens pas via le point de terminaison.

Maintenant, revenons simplement à la console et regardons le bucket dans le bucket ici, vous pouvez voir que nous n'avons plus de permissions pour ce bucket, nous nous sommes en fait verrouillés car je viens en fait par la console ici, et la console ne vient pas par le point de terminaison.

Donc ce que nous devons faire est de revenir à notre instance EC2.

Maintenant, c'est tout pour cette leçon, nous avons terminé avec l'instance EC2, et le point de terminaison VPC avec le point de terminaison, vous pouvez simplement sélectionner le point de terminaison, aller dans actions, et puis supprimer le point de terminaison.

Et cela devrait nettoyer l'entrée dans votre table de routage également.

Mais vous pouvez toujours simplement aller et vérifier, vous pourriez avoir besoin de rafraîchir la page.

Et puis il est parti.

Une fois que vous avez fait cela, terminez votre instance.

Et nous avons terminé pour cette leçon.

Salut les gars, bienvenue à cette leçon.

Cette leçon concerne le VPN client AWS.

Donc c'est exactement ce à quoi cela ressemble.

C'est une façon dont vous pouvez connecter votre ordinateur client au centre de données AWS, à un VPC via une connexion VPN.

Donc une connexion de réseau privé virtuel.

Donc disons que vous avez un ordinateur qui est Windows ou Mac ou Linux, vous êtes en mesure d'établir une connexion client à partir de là dans un VPC.

Et cela signifie que vous êtes alors en mesure de communiquer avec les ressources dans ce VPC.

Donc vous pourriez être en mesure de vous connecter à une instance EC2, directement en utilisant des adresses IP privées.

Maintenant, bien sûr, c'est un réseau privé virtuel.

Donc cela signifie également qu'il est crypté de bout en bout.

Donc regardons comment vous les configurez.

Donc ici nous avons une région.

Dans cette région, nous avons un VPC, nous avons quelques sous-réseaux.

Maintenant, nous créons un point de terminaison VPN.

Et le point de terminaison VPN est associé à des sous-réseaux.

Donc les interfaces réseau du client VPN sont créées dans le sous-réseau.

Et c'est la méthode par laquelle la connexion VPN est alors en mesure de communiquer avec les ressources dans les sous-réseaux.

Parce qu'il y a une association entre cet adaptateur réseau qui est provisionné dans le sous-réseau, et le point de terminaison VPN, nous avons ensuite l'ordinateur client, et celui-ci va exécuter un logiciel VPN.

Le logiciel VPN n'est pas un logiciel AWS.

Donc vous devez choisir l'une des options disponibles.

Il y a beaucoup d'options gratuites dans le pratique dans la prochaine leçon, nous allons utiliser open VPN, le logiciel client établira une connexion avec le point de terminaison VPN via SSL TLS.

Donc le port 443, et cela va être via Internet, le point de terminaison VPN effectuera en fait une traduction d'adresse réseau source du bloc CIDR qui est associé au client VPN au bloc CIDR qui est associé au VPC.

Et du côté client, si vous regardez dans votre table de routage, vous pouvez exécuter une commande sur Windows, qui est route print, et vous pourrez alors voir votre table de routage et vous pourrez voir que vous avez une destination pour le bloc CIDR du VPC et une passerelle, qui pointe vers le point de terminaison VPN.

Donc c'est la théorie derrière le fonctionnement de notre VPN client.

Encore une fois, il s'agit d'une connexion cryptée sur Internet depuis votre ordinateur.

Donc votre ordinateur est alors en mesure de communiquer en utilisant des adresses IP privées vers vos instances dans vos sous-réseaux au sein de votre VPC.

Donc c'est comme ça que tout fonctionne.

Et dans la prochaine leçon, nous allons configurer cela en utilisant un client Windows sur Amazon Workspaces et un point de terminaison VPN.

Les gars, l'autre type de VPN que nous pouvons établir dans AWS est un VPN site à site.

Donc un VPN site à site est là où vous pourriez connecter, par exemple, un centre de données client ou un emplacement de bureau à AWS et avoir un réseau privé établi sur Internet.

Donc une connexion cryptée, que vous pouvez ensuite tunneliser votre trafic, et encore une fois, utiliser des adresses IP privées.

Donc la configuration ressemble à ceci.

Nous avons un VPC AWS à gauche.

Et puis du côté droit, nous avons un centre de données d'entreprise, cela pourrait être un centre de données ou un bureau, et vous voulez connecter cela à AWS.

Donc AWS VPN est un VPN IPsec géré.

Et ce que nous faisons, c'est que nous créons quelque chose appelé une passerelle privée virtuelle, qui est également connue sous le nom de VGW.

Du côté AWS, le VGW est déployé sur AWS et ensuite une passerelle client est déployée.

Du côté client, lorsque vous avez ces deux composants, vous pouvez alors établir une connexion VPN cryptée sur Internet.

La connexion VPN prend en charge soit des routes statiques, soit le peering et le routage BGP.

Donc dans nos tables de routage, nous pouvons en fait spécifier une destination pour le bloc CIDR du centre de données d'entreprise, et puis le pointer vers un ID de passerelle virtuelle.

Donc c'est cet appareil ici.

Donc cela signifie que tout trafic allant à cette plage d'IP sera envoyé via la connexion VPN.

Donc c'est assez simple.

Et le cas d'utilisation le plus courant pour cela est ce que nous voyons ici, c'est la connexion de centres de données ou d'emplacements de bureaux à AWS, afin que vous puissiez ensuite tunneliser votre trafic via une connexion cryptée en utilisant Internet.

Il peut également être utilisé parfois comme une connexion de sauvegarde pour Direct Connect.

Et nous allons examiner cela plus tard dans cette section.

C'est toute la théorie que je voulais couvrir pour l'instant.

Et ce que nous allons faire dans la prochaine leçon, c'est que ce sera pratique, nous allons faire un labo pratique où nous allons configurer une connexion VPN.

AWS VPN CloudHub n'est pas en fait un service que vous pouvez trouver dans la console AWS.

Ce que cela est vraiment, c'est un modèle et un modèle architectural que vous pouvez utiliser lorsque vous utilisez la technologie AWS site à site VPN.

Donc regardons l'architecture dans laquelle vous pouvez implémenter CloudHub.

Donc nous avons un VPC.

Et nous avons implémenté une passerelle privée virtuelle, une VGW.

Et celle-ci est évidemment déployée du côté AWS.

Nous avons ensuite plusieurs bureaux clients, ou ceux-ci pourraient être des centres de données clients.

Mais ce sont différents environnements sur site que nous voulons connecter en utilisant un réseau privé virtuel à AWS.

Maintenant, la façon dont nous les connectons dans une topologie CloudHub, c'est en utilisant un modèle hub and spoke.

Donc en d'autres termes, AWS est le hub, le VPC.

Et puis les spokes vont vers chacun de ces bureaux.

Donc ce que nous faisons, c'est que nous déployons une passerelle client dans chacun de ces bureaux.

Chacune de ces passerelles clients a un numéro de système autonome BGP unique, c'est un numéro de système autonome de protocole de passerelle frontalière.

Donc BGP est un protocole que vous pouvez utiliser pour annoncer des routes vers différentes parties de votre réseau.

Et chaque environnement a son propre ASN.

Et cela correspond aux routes qui seraient annoncées dans le réseau, donc les préfixes IP, donc vous devez avoir un ASN BGP unique pour chaque bureau.

Et puis nous pouvons établir une connexion VPN entre chacune de ces passerelles clients et la même passerelle virtuelle du côté AWS.

Maintenant, le trafic réseau peut provenir d'un bureau et aller vers le VPC ou le VPC vers un bureau.

Mais aussi, il peut aller entre les bureaux clients ou les environnements sur site des clients, qu'ils soient des bureaux ou des centres de données.

Donc le bureau client ici peut communiquer via la VGW.

Donc ce bureau client ici.

Donc nous utilisons le VPN site à site AWS pour établir une topologie de routage, qui connecte plusieurs bureaux clients, ainsi que le VPC lui-même.

Maintenant, cela utilise le VPN IPsec, le même VPN, que nous venons de voir dans les leçons précédentes.

Donc c'est tout.

C'est le CloudHub VPN.

Comme je l'ai mentionné, si vous cherchez en ligne, vous ne trouverez pas CloudHub.

Mais si vous faites une recherche en ligne, vous trouverez quelques articles sur cette architecture, qui peuvent vous donner un peu plus d'informations sur la façon dont elle est configurée.

Mais essentiellement, nous connectons simplement plusieurs passerelles clients à une seule passerelle privée virtuelle.

Et ensuite, c'est à vous de configurer votre protocole BGP en conséquence pour annoncer les routes que vous voulez annoncer dans le réseau.

Donc c'est tout pour un aperçu rapide de CloudHub.

Je vous verrai dans la prochaine leçon.

Nous avons déjà parlé des connexions de réseau privé virtuel, VPN.

Maintenant, le VPN est généralement exécuté sur l'Internet public, ce qui signifie que nous sommes soumis aux contraintes de bande passante et aux problèmes de latence potentiels sur Internet, nous ne pouvons pas contrôler Internet, nous ne savons pas de minute en minute, d'heure en heure, ce qui va se passer, nous pouvons obtenir un bon fournisseur de services.

Mais même ainsi, parfois il y a un long chemin entre nous et nos services sur AWS.

Et cela signifie que quelque part le long de ce chemin, nous pourrions avoir de la congestion ou de la latence.

Donc l'une des solutions à cela est d'utiliser Direct Connect ou DX. DX signifie que vous avez une connexion privée à AWS, cela signifie qu'elle n'est pas partagée, elle n'est pas publique, elle est dédiée à vous, c'est une connexion tout le long jusqu'à votre centre de données AWS et jusqu'à votre Amazon VPC.

Donc regardons comment nous configurons cela.

Donc disons que nous avons un VPC, nous avons quelques sous-réseaux.

Et puis nous avons notre centre de données d'entreprise, ou cela pourrait être votre bureau.

Maintenant, au milieu ici, il y a quelque chose appelé un emplacement Direct Connect.

Ce sont différents des régions AWS.

Et il y en a beaucoup dans le monde.

Donc il pourrait bien y avoir des emplacements Direct Connect dans le centre de données où se trouve votre équipement, ou quelque part à proximité dans votre ville.

Dans l'emplacement Direct Connect, AWS a une cage, donc ils ont un rack plein de leur propre équipement.

Et puis il y a la cage du client ou du partenaire.

Donc soit vous avez un rack avec un équipement dans ce centre de données, soit vous utilisez un partenaire AWS.

Maintenant, ces deux cages auront un routeur.

Donc nous avons le point de terminaison Direct Connect sur la cage AWS.

Et puis dans la cage du client ou du partenaire, nous avons le routeur du client ou du partenaire, et vous devez utiliser certains types de connecteurs, un port DX est en fait alloué pour vous.

Et puis ce que vous faites, ce sont des interconnexions entre le routeur du client ou du partenaire, et AWS, nous avons ensuite un routeur client, en fait dans votre centre de données, et Direct Connects dans AWS.

Et nous pouvons former la connexion Direct Connect.

Donc maintenant, depuis votre routeur client, vous devez avoir une connexion physique dans la cage du client ou du partenaire.

Donc cela pourrait être quelque chose dont vous devez parler à votre FAI local pour obtenir cette connexion de ce point à votre centre de données, sauf si vous avez tout votre équipement dans un emplacement Direct Connect, ce qui peut souvent être le cas.

Ensuite, de là, nous avons les interconnexions dans AWS et ensuite une connexion physique tout le long jusqu'à une région AWS où se trouve votre VPC, c'est une connexion fibre physique, fonctionnant à un ou dix gigabits par seconde.

Maintenant, 100 gigas vient d'être publié récemment pour certains emplacements.

Si vous voulez des vitesses plus lentes, vous pouvez parler à un partenaire, et ils peuvent vous donner des vitesses à partir de 50 mégabits par seconde.

Donc regardons quelques-uns des avantages.

Vous avez une connectivité privée entre AWS et votre centre de données ou bureau, vous obtenez une expérience réseau constante, vous pouvez contrôler le chemin réseau, ce n'est pas comme sur Internet où vous ne savez tout simplement pas ce qui se passe.

Cela signifie que vous pouvez augmenter la vitesse, améliorer la latence, obtenir une meilleure bande passante et un meilleur débit pour votre connexion.

DX peut être assez coûteux pour de nombreux clients.

Mais pour ceux qui transfèrent beaucoup de données de leur centre de données vers AWS, cela peut être rentable.

Maintenant, allons un niveau plus profond.

Donc nous avons la même configuration ici.

Et vous pouvez voir certains des services AWS qui sont dans l'espace public en bas de cette boîte.

Donc comment provisionnons-nous la connectivité à travers cette ligne privée ? Eh bien, nous devons créer quelque chose appelé un viff privé.

Un Vf est une interface virtuelle.

Un viff privé est la façon dont vous vous connectez à votre VPC dans la même région en utilisant une passerelle virtuelle.

Donc il y a une passerelle privée virtuelle attachée à votre VPC et le viff privé enverra des données à travers la connexion DX dans votre VPC, c'est une interface virtuelle qui utilise 802 point un Q, les réseaux locaux virtuels VLAN et une session BGP également.

Maintenant, qu'en est-il de la connexion à l'espace public, vous ne vous connectez pas aux services AWS publics via un viff privé.

Au lieu de cela, vous avez besoin d'un cinquième public, notre public, cela vous permettra de vous connecter aux services AWS dans l'espace public qui sont dans n'importe quelle région AWS.

Mais vous ne pouvez pas vous connecter à Internet via le cinquième public.

Maintenant, que se passe-t-il si vous voulez vous connecter à plusieurs VPC dans la même région, lorsque dans ce cas, vous avez plusieurs passerelles privées virtuelles et plusieurs cinquièmes privés pour vous connecter à chaque VPC, vous pouvez également créer quelque chose appelé un vf hébergé, ce qui signifie que vous pouvez partager un vf avec un autre compte AWS également.

Comme je l'ai mentionné un peu plus tôt, vous pouvez obtenir des vitesses plus lentes auprès des partenaires APN.

Donc ce sont des partenaires dans le réseau de partenaires AWS.

Et ces vitesses peuvent alors être de 50 à 500 mégabits par seconde, 100 gigas est également disponible dans certains emplacements sélectionnés, ce sont les emplacements AWS Direct Connect.

Donc cela pourrait être là où vous êtes, probablement ne sera pas à l'examen, c'est très, très nouveau.

Quelque chose qui est vraiment important pour l'examen est de se souvenir que les connexions DX ne sont pas cryptées, vous ne pouvez pas crypter une connexion DX.

Donc il n'y a aucun moyen de sélectionner une case à cocher et d'activer le cryptage en transit.

Ce n'est tout simplement pas une fonctionnalité.

Donc que faites-vous si vous voulez crypter votre trafic ? Eh bien, vous pouvez alors créer un VPN IPsec site à site par-dessus la connexion.

Donc vous avez votre connexion DX, et vous exécutez essentiellement un VPN par-dessus cette connexion.

Donc maintenant votre trafic est privé, il est sur votre connexion DNS privée, vous avez les fonctionnalités de latence et de bande passante.

Et vous cryptez également votre trafic en utilisant un tunnel VPN.

Donc c'est vraiment important de s'en souvenir, cela revient souvent dans les questions d'examen.

Maintenant, c'est tout pour la théorie de base autour de Direct Connect.

Et dans la prochaine leçon, nous allons examiner une autre fonctionnalité appelée Direct Connect Gateway.

Bienvenue dans cette leçon.

Dans cette leçon, je vais couvrir la passerelle AWS Direct Connect.

Maintenant, la meilleure façon de comprendre les avantages de la passerelle direct connect est de regarder une architecture où nous n'utilisons pas et à quel point cela peut devenir complexe.

Et ensuite nous allons regarder quand nous utilisons la passerelle direct connect et comment elle peut résoudre certains problèmes.

Donc voici une architecture d'exemple où nous n'utilisons pas la passerelle direct connect.

Maintenant, nous avons plusieurs régions, et nous avons un bureau.

Et nous avons plusieurs emplacements dx dans différentes parties du monde.

Et ce que nous faisons, c'est que nous connectons chacune de ces régions à un emplacement dx qui est proche de cette région et ensuite dans un bureau d'entreprise.

Et nous faisons la même chose dans la région EU central one en bas ici, comme nous le faisons dans US West one.

Donc cette entreprise a maintenant plusieurs emplacements, où ils ont ensuite des connexions à AWS en utilisant dx, ils doivent établir un viff privé.

Et cela se connecte à un seul VPC dans la même région en utilisant une passerelle virtuelle, nous faisons la même chose dans la deuxième région.

Maintenant, dx est un service régional.

Donc évidemment, plusieurs emplacements DNS doivent être utilisés pour cette topologie, et cela nécessite également des bureaux régionaux, ou des liens longue distance coûteux.

Donc en d'autres termes, ces routeurs clients ici doivent soit être dans un seul emplacement physique, une seule zone géographique, et vous avez un lien longue distance venant d'Europe, ou des États-Unis, ou ce sont plusieurs bureaux dans différentes zones géographiques.

Donc lorsque nous voulons commencer à connecter nos bureaux à plusieurs régions, en utilisant des connexions directes, cela peut devenir assez coûteux, et assez complexe.

Donc maintenant, regardons une architecture où nous utilisons la passerelle direct connect.

Donc dans ce cas, nous avons les mêmes deux régions, nous avons un seul bureau d'entreprise et un seul emplacement dx.

Et donc nous n'avons maintenant que cette connexion dans notre bureau depuis un seul emplacement.

Et nous avons une passerelle DX.

Et ensuite la passerelle DX est en fait connectée à plusieurs régions, un viff privé est associé à la passerelle DX.

Et ensuite la passerelle DX est associée à une passerelle virtuelle.

Dans chacune des régions, BGP annonce autour des VPC via la passerelle DX.

Et le trafic qui va de la passerelle DX à ces différentes régions passe par le backbone AWS, donc il utilise cette expérience réseau constante du réseau global AWS.

Maintenant, le trafic réseau peut aller du bureau à n'importe quelle région, donc n'importe lequel des VPC connectés.

Et bien sûr, je n'en montre que deux ici.

Mais vous pouvez avoir de nombreuses, nombreuses régions qui sont connectées à une passerelle dx.

Maintenant, ce que vous ne pouvez pas faire, c'est en fait router le trafic régional d'une région à une autre via la passerelle DX, elle ne supporte pas cela.

Mais vous pouvez l'utiliser pour vous connecter depuis votre bureau d'entreprise en utilisant une seule connexion dx dans plusieurs régions autour du monde.

Donc c'est la passerelle dx.

C'est une technologie vraiment utile si vous êtes une entreprise mondiale, mais vous n'avez pas de bureaux mondiaux ou vous voulez qu'un seul emplacement de bureau ait cette expérience réseau constante dans plusieurs régions autour du monde et cette technologie est géniale à utiliser. AWS Transit Gateway est un service vraiment génial.

Il est décrit par AWS comme étant un routeur cloud, et il connecte des VPC et des emplacements sur site ensemble en utilisant un hub central.

Donc regardons ce que cela signifie.

Maintenant, encore une fois, ce que je veux faire est de vous montrer une architecture en maillage complet sans AWS Transit Gateway pour vous aider à comprendre le problème que nous essayons de résoudre, car lorsque nous avons beaucoup de VPC et d'emplacements sur site, cela peut devenir vraiment complexe, les connexions d'appairage que nous avons établies si nous utilisons l'appairage VPC peuvent devenir extrêmement complexes.

Donc disons que nous avons les VPC A, B, C et D encore, et nous avons établi nos liens d'appairage VPC.

Et comme vous le savez, il y aura assez de liens d'appairage ici, nous avons six liens d'appairage que nous devons établir pour quatre VPC.

Et à mesure que vous augmentez le nombre de VPC, cela devient très complexe.

Donc ici nous avons six connexions d'appairage VPC, nous avons ensuite un bureau d'entreprise connecté via une passerelle client.

Donc comment connectons-nous le bureau d'entreprise en utilisant un VPN site à site à chacun de ces VPC ? Eh bien, nous avons besoin d'une passerelle virtuelle dans chaque VPC, puis nous devons établir une connexion à la passerelle client depuis chaque VPC.

Et chacune de celles-ci est son propre VPN IPsec crypté.

Donc il y a quatre connexions VPN site à site.

Et cela n'inclut même pas la redondance.

Si vous vouliez ajouter de la redondance, vous auriez besoin d'une autre passerelle client, et doubler le nombre de connexions VPN STS.

Donc cela commence à devenir super complexe.

Regardons maintenant la même architecture.

Mais avec Transit Gateway.

Dans ce cas, les mêmes quatre VPC et un bureau d'entreprise, nous plaçons Transit Gateway au milieu, et il devient le hub de transit réseau qui interconnecte les VPC et les réseaux sur site.

Donc maintenant nous avons des connexions dans chacun de ces VPC, les VPC deviennent attachés à la passerelle de transit.

Et vous spécifiez un sous-réseau de chaque zone de disponibilité, et cela permet le routage dans cette zone de disponibilité pour tous les autres sous-réseaux.

Nous avons ensuite le centre de données client, nous avons le bureau d'entreprise ici avec une passerelle client, et la passerelle client se connecte.

Et c'est tout.

C'est maintenant un service, qui nous permet de nous connecter à travers ce routeur cloud, le hub central à l'un de ces VPC, les TGW.

W peuvent être attachés à des VPN, des passerelles Direct Connect, des appliances tierces, et aussi des passerelles de transit dans d'autres régions et aussi d'autres comptes.

Donc regardons comment cela fonctionne avec la passerelle x.

Donc dans ce cas, au lieu d'utiliser un VPN site à site, notre bureau d'entreprise a un routeur client, et nous nous connectons à un emplacement dx, et nous utilisons une passerelle dx.

Donc maintenant la passerelle DX a une connexion à la passerelle de transit.

Et cela s'appelle une association.

Nous avons ensuite la connexion physique retour au bureau d'entreprise depuis direct connect, et nous créons quelque chose appelé un transit van.

Donc c'est un autre type d'interface virtuelle spécifiquement utilisée pour les passerelles Direct Connect, lorsqu'elles sont associées à une passerelle de transit.

Donc transit Vf est uniquement utilisé lorsque vous attachez une passerelle dx à une passerelle de transit.

Maintenant, cette architecture supporte alors le routage transitif entre les locaux, la passerelle de transit et tous ces VPC connectés.

Comme vous pouvez l'imaginer, lorsque votre entreprise grandit et commence à utiliser plus de VPC dans plus de régions, et que vous voulez avoir ce routage transitif entre eux, cela peut devenir si complexe que la passerelle de transit résoudra vraiment beaucoup de défis.

Donc c'est tout pour cette leçon.

Je vous verrai dans la prochaine leçon.

Bonjour et bienvenue à cette leçon.

Je vais maintenant parler de l'utilisation du protocole IPv6 dans un Amazon VPC.

Donc rappelez-vous, j'ai mentionné plus tôt dans le cours qu'il y a deux versions d'IP qui sont largement utilisées.

L'une d'entre elles est IPv4, c'est de loin la plus couramment utilisée, elle existe depuis assez longtemps.

Et puis il y a IPv6.

Maintenant, IPv6 existe également depuis quelques années, mais il n'est pas utilisé aussi largement.

Mais cela doit changer avec le temps car nous manquons d'adresses IPv4.

Donc nous allons voir comment vous pouvez utiliser IPv6 dans un VPC.

Donc commençons par regarder la structure de l'adresse IPv4.

Donc rappelez-vous, elle est composée de quatre nombres séparés par des points.

Et ces nombres proviennent d'un octet.

Donc c'est huit bits binaires, qui sont soit un soit zéro.

Donc une adresse IPv4 fait 32 bits de long.

Maintenant, regardons combien d'adresses vous obtenez pour cela, vous obtenez 4,3 milliards d'adresses, ce qui semble être un grand nombre.

Et c'est un grand nombre de dollars sur votre compte bancaire.

Mais quand il s'agit d'adresses qui doivent être attribuées à toutes sortes d'appareils différents dans le monde entier, dans un monde rempli de 7 milliards de personnes, ce n'est tout simplement pas assez.

Et cela aurait pu sembler plus que suffisant il y a quelques années, mais il est devenu évident, même dans les années 90, que cela ne suffirait pas, et ce n'est pas le cas.

Donc nous sommes proches d'épuiser ces adresses.

Et le NAT doit être utilisé de manière extensive.

Donc si vous êtes dans une entreprise, et que votre entreprise a des milliers d'ordinateurs en interne, alors ces ordinateurs utiliseront probablement des adresses IPv4.

Et celles-ci seront des adresses privées.

Et lorsqu'ils accèdent à Internet, ils passent par un appareil NAT ou autre.

Et cela signifie qu'une adresse IP publique est utilisée pour représenter de nombreux, nombreux PC.

Donc c'est un contournement que nous devons mettre en place avec IPv4.

Avec IPv6, nous n'avons pas à nous en soucier.

Donc regardons la structure d'une adresse IPv6.

Donc voici la structure d'IPv6.

Il a également une partie réseau et une partie nœud.

Mais il fait 128 bits de long.

Donc c'est un nombre beaucoup, beaucoup plus grand.

Mais il utilise aussi l'hexadécimal.

Alors qu'IPv4 utilise le décimal pointé.

Donc cela signifie qu'il y a beaucoup plus de valeurs potentielles que vous pouvez utiliser en hexadécimal par rapport au décimal.

Donc cela signifie que la quantité d'adresses est beaucoup, beaucoup plus grande.

Et voici le nombre, c'est le nombre d'adresses que vous pouvez obtenir avec IPv6.

Et c'est absolument énorme.

Donc pour le mettre en perspective.

Et d'ailleurs, si vous cherchez sur Google des analogies pour la taille de la base d'adresses IPv6, il y a toutes sortes d'analogies fantastiques, car elle est vraiment massive.

Donc celle que j'aime est que vous pouvez obtenir 100 adresses IPv6 pour chaque atome sur Terre.

Donc c'est un nombre énorme, énorme, ce qui signifie que nous n'aurons jamais, jamais à nous soucier de manquer d'adresses IPv6.

Donc regardons comment nous devons configurer notre VPC.

Donc nous avons un VPC avec quelques sous-réseaux, nous devons avoir un bloc CIDR IPv4.

Et puis nous avons besoin des plages de sous-réseaux individuelles pour nos sous-réseaux.

Maintenant, nous avons aussi besoin d'un bloc CIDR IPv6 maintenant, donc nous en avons alloué un à ce compte.

Maintenant, AWS attribuera une plage d'adresses IPv6 slash 56 au VPC, puis vous pouvez créer vos plages de sous-réseaux dans cet espace d'adressage.

Et ceux-ci deviennent des sous-réseaux slash 64.

Maintenant, un sous-réseau slash 64 permettra 18 millions de billions d'adresses.

Donc encore une fois, c'est un exemple de pourquoi vous n'avez vraiment pas à vous soucier du nombre d'adresses que vous allez avoir pour vos ordinateurs, car c'est juste énorme.

Maintenant, vous remarquerez que deux nombres sont mis en évidence en rouge à la fin de l'adresse IP.

Il s'agit d'une paire hexadécimale, qui a des valeurs de 00 à FF.

Et cela désigne le sous-réseau individuel.

Donc il doit être unique pour chaque sous-réseau.

Et cela signifie que vous allez avoir un possible 256 sous-réseaux, avec des blocs IPv6 dedans.

Et chacun de ceux-ci est un slash 64.

Donc chacun de ceux-ci supportera 18 millions de billions d'adresses.

Donc beaucoup de flexibilité pour votre VPC.

Maintenant, regardons la table de routage une fois que nous avons activé IPv6, donc nous avons maintenant une route locale pour le bloc CIDR IPv6.

Et nous avons besoin d'une route vers la passerelle Internet pour tout ce qui est en dehors de cette plage, tout comme nous l'avons fait pour IPv4, nous avons le colon colon slash zéro pour IPv6, pointant vers l'ID de la passerelle Internet.

Et cela signifie que toute adresse IPv6 qui n'est pas dans cette plage ira vers la passerelle Internet.

Donc nous nous assurerons de l'avoir spécifié dans notre table de routage lorsque nous activerons IPv6.

Maintenant, toutes les adresses IPv6 sont routables publiquement.

Cela signifie qu'il n'y a pas de traduction d'adresse réseau.

Maintenant, si vous le souhaitez, vous pouvez utiliser quelque chose appelé une passerelle Internet uniquement en sortie.

Maintenant, le but de cela est lorsque vous voulez permettre l'accès en sortie uniquement en utilisant IPv6.

Donc c'est un peu comme avoir une instance EC2 dans un sous-réseau privé avec IPv4 et ensuite ajouter une passerelle NAT dans un sous-réseau public.

Cela signifie que cette instance est protégée d'Internet, personne ne peut y accéder directement depuis Internet, mais elle a un accès Internet en sortie.

Donc c'est ce que fait une passerelle Internet uniquement en sortie.

Donc c'est tout pour la théorie sur ce sujet, et dans la prochaine leçon, nous allons activer IPv6 pour notre VPC.

Salut les gars, dans cette leçon, vous allez apprendre à connaître les journaux de flux VPC. Ensuite, nous allons également configurer un journal de flux pour voir comment il fonctionne et quelles données il capture réellement.

Donc les journaux de flux VPC capturent des informations sur le trafic IP allant et venant des interfaces réseau.

Dans un VPC, les données sont stockées en utilisant CloudWatch ou Amazon S3.

Et vous pouvez créer le journal de flux à différents niveaux.

Donc au niveau du VPC, au niveau du sous-réseau, ou au niveau de l'interface, le service au niveau de l'interface est associé à l'ENI, qui est attaché à une instance EC2, vous pouvez capturer beaucoup de trafic, ce qui est vraiment utile pour le dépannage et la sécurité également.

Donc allons-y et créons un journal de flux dans EC2, j'ai toujours une instance en cours d'exécution, si vous n'avez pas d'instance en cours d'exécution, lancez simplement une instance, comme nous l'avons fait auparavant, et mettez-la dans votre sous-réseau public one, a, et elle devrait avoir une adresse IP publique.

Ensuite, nous allons envoyer nos données à CloudWatch Logs.

Donc dans le service CloudWatch, je vais aller dans les groupes de logs, créer un groupe de logs, et me créer un groupe de logs, je vais l'appeler mes logs de sous-réseau, je peux définir un paramètre de rétention.

Pour moi, mettons cinq jours, donc après cinq jours, je n'ai plus besoin de ces données.

Et créons le groupe de logs.

Ensuite, nous devons créer un rôle.

Donc le service de journal de flux a les permissions dont il a besoin dans le service d'identité et de gestion des accès, nous allons créer un rôle.

Donc créons un rôle.

Choisissons Créer un rôle, nous allons choisir EC2 pour l'instant, nous allons le modifier bientôt, car ce n'est pas en fait le service qui va assumer ce rôle, nous allons passer directement les politiques, car nous allons ajouter une politique en ligne.

Et je vais appeler mon rôle flow logs cloud watch, je vais supprimer la description et créer ce rôle.

Maintenant, trouvons le rôle.

Et sous permissions, nous allons ajouter une politique en ligne, nous allons aller en JSON.

Et nous avons ce code JSON ici dans votre répertoire de code Amazon VPC.

Et c'est VPC flow logs dot JSON.

Donc tout ce que nous devons faire est de copier tout cela.

Comme vous pouvez le voir, le service va être fourni avec les permissions de créer un groupe de logs, créer un flux de logs, mais des événements de logs, décrire des groupes de logs et décrire des flux de logs.

Donc avec cela copié, revenons, remplaçons tout ce code, cliquons sur réviser, donnons-lui un nom, je vais simplement l'appeler cloud watch permissions et créer la politique.

Maintenant, nous devons modifier la relation de confiance, ce n'est pas en fait EC2 qui va assumer ce rôle.

Donc en revenant ici, la politique de confiance peut être remplacée, nous pouvons littéralement copier ce morceau de texte ici.

Et nous allons le coller par-dessus là où il est écrit EC2 dot Amazon aws.com.

Donc maintenant le service qui est capable d'assumer ce rôle est VPC flow logs.

Mettons à jour cette politique de confiance.

C'est tout, nous sommes maintenant prêts à aller et créer notre journal de flux.

De retour dans EC2, je n'ai qu'une seule instance en cours d'exécution.

Donc ce sera facile d'identifier l'interface réseau, nous allons créer le journal de flux ici au niveau de l'interface réseau.

Donc basculons vers les journaux de flux, créons un journal de flux, je vais simplement l'appeler mon journal de flux.

Mettons-le pour tout le trafic, et une agrégation d'une minute.

Donc nous obtenons des données assez rapidement.

Nous le supprimerons ensuite lorsque nous terminerons notre instance de toute façon.

Et nous allons l'envoyer à CloudWatch Logs.

Donc nous avons notre groupe de logs.

Et trouvons notre rôle, qui commence par flow.

Donc c'est flow logs cloud watch.

Et nous allons laisser le format par défaut, et puis simplement créer ce journal de flux.

Donc maintenant, essayons quelques choses.

Nous voulons envoyer quelques connexions réussies.

Donc copions notre IP publique, allons dans une nouvelle fenêtre ici et mettons cela.

Et nous avons maintenant généré un peu de trafic HTTP.

Je pourrais rafraîchir cela quelques fois.

Et qu'en est-il de l'envoi de trafic, que nous allons nous faire refuser, c'est une autre chose que nous pourrions faire.

Donc revenons aux instances, vérifions dans quel groupe de sécurité se trouve cette instance.

Et elle en a en fait deux.

Donc allons dans le public web un, car je pense que c'est celui qui a quelques règles qui permettent certains protocoles depuis Internet.

Et oui, nous pouvons voir les règles SSH et HTTP sont dedans.

Donc allons modifier les règles entrantes.

Et je vais temporairement supprimer ma règle SSH et sauvegarder.

Maintenant, depuis une ligne de commande, je vais simplement essayer sans aucun argument de me connecter en SSH à cette instance.

Et cela ne devrait pas fonctionner, cela devrait simplement continuer à échouer car nous n'avons pas les règles de sécurité pour permettre cela.

Donc c'est essentiellement juste générer un peu de trafic.

Donc ce que nous pouvons faire maintenant est d'aller dans les logs CloudWatch, et de voir si des données commencent à être envoyées là-bas.

De retour dans les logs CloudWatch, je vais sélectionner mon groupe de logs.

Et voyons si nous avons un flux.

Et j'en ai un qui est assez rapide.

Maintenant, ne vous inquiétez pas si ce n'est pas encore là, vous devrez peut-être attendre quelques minutes, et il apparaîtra.

Donc sélectionnons mon flux de logs et voyons quelles données nous avons ici.

Et vous pouvez voir qu'il y a quelques entrées ici, nous pouvons voir quelques rejets.

Et associés à ceux-ci, diverses informations, y compris l'interface réseau élastique, les adresses IP source et de destination, nous avons des numéros de port, nous avons des numéros de protocole, nous avons diverses informations qui pourraient être utiles dans l'analyse que vous faites.

Si vous voulez rafraîchir, vous pouvez cliquer sur reprendre, et ensuite vous devriez voir plus de données arriver au fil du temps.

Donc voilà, nous avons quelques rejets supplémentaires qui arrivent également.

Et juste quelques minutes plus tard, j'ai rafraîchi mon écran.

Et nous pouvons voir quelques acceptations également.

Donc il y en a quelques-unes, nous pouvons voir le numéro de port ici, le port 80.

Donc ce sont des connexions réussies à notre serveur web.

Donc c'est tout.

Il y a beaucoup de données là que vous pouvez utiliser pour diverses analyses.

Et c'est vraiment utile de comprendre les différents types de logs, nous avons un AWS, quelles données sont incluses afin que vous sachiez lesquels utiliser pour votre dépannage ou votre analyse.

Donc c'est tout pour cette leçon.

Et nous avons terminé avec notre instance EC2 maintenant, donc nous pouvons aller de l'avant et la supprimer.

Une fois que vous avez terminé votre instance, vous êtes tous nettoyés.
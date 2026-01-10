---
title: Comment utiliser OpenVPN pour accéder en toute sécurité aux ressources privées
  d'AWS
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2018-06-12T22:49:42.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-use-openvpn-to-safely-access-private-aws-resources-f904cd24f890
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MgRSD6yOMt1f4JpfGBrfOg.jpeg
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: vpn
  slug: vpn
seo_title: Comment utiliser OpenVPN pour accéder en toute sécurité aux ressources
  privées d'AWS
seo_desc: 'This article was adapted from part of my new Pluralsight course, “Connecting
  On-prem Resources to your AWS Infrastructure.”

  Do you sometimes need to connect to resources you’ve got running on Amazon Web Services?
  Accessing your public EC2 instances u...'
---

_Cet article a été adapté d'une partie de mon nouveau cours Pluralsight, « [Connecter les ressources sur site à votre infrastructure AWS](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) »._

Avez-vous parfois besoin de vous connecter à des ressources que vous avez en cours d'exécution sur Amazon Web Services ? L'accès à vos instances EC2 publiques à l'aide de SSH et le chiffrement de vos données S3 sont, à toutes fins utiles, suffisamment sécurisés. Mais qu'en est-il de l'accès à une instance de base de données RDS back-end ou du travail avec des données basées sur AWS qui ne sont pas publiques ? Il existe toutes sortes de raisons pour lesquelles les administrateurs gardent de telles ressources hors de portée du grand public. Mais si vous ne pouvez pas y accéder lorsque vous en avez besoin, à quoi peuvent-elles bien vous servir ?

Vous devrez donc trouver un moyen sûr et fiable de contourner les ACL et les groupes de sécurité protégeant vos ressources. Une solution que je couvre dans [mon cours « Connecter les ressources sur site à votre infrastructure AWS » sur Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) est Direct Connect. Mais si le prix de Direct Connect est un budget-buster pour votre entreprise, alors un type de tunnel VPN pourrait faire l'affaire.

### Qu'est-ce qu'un réseau privé virtuel ?

Les réseaux privés virtuels (VPN) sont souvent utilisés pour permettre une activité réseau autrement restreinte ou une navigation anonyme. Mais ce n'est pas de cela que parle cet article.

Un VPN est une connexion point à point qui vous permet de déplacer des données de manière sécurisée entre deux sites sur un réseau public. Effectivement, un tunnel peut être conçu pour combiner deux sites privés géographiquement séparés en un seul réseau privé. Dans notre contexte, cela signifierait connecter votre réseau de bureau local avec le VPC AWS qui héberge vos ressources privées.

Il existe deux façons de faire cela :

* Une connexion VPN gérée construite sur une passerelle privée virtuelle AWS
* Utiliser votre propre VPN.

Cet article se concentrera sur la méthode DIY (Do It Yourself).

#### Le serveur d'accès OpenVPN

Comme son nom l'indique, [OpenVPN](https://openvpn.net/) est un projet open source, et vous pouvez toujours télécharger l'édition communautaire gratuite et configurer les choses sur votre propre serveur VPN. Mais la société OpenVPN fournit également un [serveur d'accès OpenVPN spécialement conçu en tant qu'AMI EC2](https://openvpn.net/index.php/access-server/on-amazon-cloud.html) qui sort de la boîte avec une intégration compatible AWS et des outils de configuration automatisés.

D'après ce que je peux voir, lancer l'AMI dans votre VPC AWS et l'ouvrir pour des connexions à distance contrôlées est devenu la méthode « correcte » pour accomplir cette tâche.

Quel est le coût ? Si vous testez simplement les choses et ne prévoyez pas d'accéder au VPN en utilisant plus de deux connexions à la fois, alors l'AMI lui-même est gratuit. Vous serez toujours responsable des coûts réguliers d'une instance EC2, mais si votre compte est toujours éligible pour le niveau gratuit, alors vous pouvez l'obtenir gratuitement également.

Une fois que vous mettez votre VPN en production active, la licence que vous achetez dépendra du nombre de connexions simultanées dont vous aurez besoin. [Cette page](https://docs.openvpn.net/getting-started/software-license-pricing/) contient les détails dont vous aurez besoin.

Voici ce que nous allons faire dans ce guide :

* Sélectionner, provisionner et lancer une AMI Ubuntu avec OpenVPN Access Server préinstallé dans mon VPC
* Accéder au serveur en utilisant SSH et configurer le VPN
* Configurer un utilisateur administrateur
* Configurer une machine locale en tant que client OpenVPN et se connecter à une instance privée dans mon VPC AWS

Prêt ?

### Lancement d'un serveur d'accès OpenVPN

Depuis le tableau de bord EC2 — et en s'assurant que nous sommes dans la bonne région AWS — lancer une instance pour servir de serveur VPN. Plutôt que d'utiliser l'une des AMI Quick Start, je cliquerai sur l'onglet AWS Marketplace et rechercherai « openvpn access server ». OpenVPN fournit un certain nombre d'images officielles qui sont liées à des licences offrant un nombre croissant de clients connectés.

Je vais opter pour cette image Ubuntu qui fonctionne avec un arrangement « Bring Your Own License ». Comme je l'ai écrit précédemment, nous n'aurons pas réellement besoin d'une licence pour ce que nous allons faire.

![Image](https://cdn-media-1.freecodecamp.org/images/XTboqBVguN8FTVoSwQrnrGZuCkC97Y0vtyUu)
_AMI OpenVPN Access Server disponibles sur l'AWS Marketplace_

La sélection de l'AMI ouvre une fenêtre contextuelle nous indiquant combien cette image nous coûtera par heure en utilisant divers types d'instances et choix de stockage EBS. Ce sont cependant uniquement les coûts réguliers d'infrastructure AWS et n'incluent pas les frais de licence.

![Image](https://cdn-media-1.freecodecamp.org/images/HRL623PHVls25j6yVZW80nurh7rWJIDv3mSq)
_Coûts de l'AMI OpenVPN Access Server — facturés directement par AWS_

En ce qui concerne le type d'instance, je vais rétrograder vers un t2.micro pour rester dans le niveau gratuit. Un serveur de production occupé pourrait nécessiter un peu plus de puissance.

Parce que je vais vouloir démarrer une deuxième instance dans le même sous-réseau dans quelques minutes, je vais sélectionner, disons, « us-east-1b » depuis la page Configurer les détails de l'instance, et prendre note pour plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/6R-q7kO9yezjWvSf99cER4Xh4bA3zs5azISg)
_Choisissez un sous-réseau et prenez note pour plus tard_

Maintenant, la page Groupe de sécurité est là où les paramètres de l'AMI OpenVPN brillent vraiment. Nous sommes présentés avec un groupe de sécurité qui ouvre tout ce dont nous aurons besoin. Le port 22 est pour le trafic SSH vers le serveur, 943 est le port que nous utiliserons pour accéder à l'interface graphique d'administration, 443 est le trafic HTTP chiffré TLS, et OpenVPN écoutera les connexions clients entrantes sur le port 1194.

![Image](https://cdn-media-1.freecodecamp.org/images/-h1D6QojwaZIVezNitxZDgaZqiLCbwFJ3FjS)
_Le groupe de sécurité qui accompagne l'AMI OpenVPN_

**Note** : Si possible, il serait normalement judicieux de resserrer ces règles afin que seules les requêtes provenant de plages d'adresses IP valides de l'entreprise soient acceptées, mais cela conviendra pour des tests à court terme.

À partir de là, je vais passer en revue mes paramètres, confirmer que j'ai la clé de chiffrement SSH listée, et lancer l'instance.

Une fois l'instance lancée, je verrai des informations de connexion importantes — y compris le fait que le compte utilisateur que nous utiliserons pour nous connecter en SSH au serveur s'appelle openvpnas — et un guide de démarrage rapide. Je recevrai également un e-mail contenant des liens vers les mêmes informations.

De retour dans la console des instances EC2, pendant que la nouvelle machine termine son démarrage, nous voyons notre adresse IP publique. Si nous devions jamais redémarrer l'instance, il n'y a aucune garantie que nous obtiendrions à nouveau cette même IP, ce qui pourrait causer un certain chaos. Il est donc judicieux d'assigner à l'instance une IP élastique.

Pour ce faire, je cliquerai sur Elastic IPs puis sur Allouer une nouvelle adresse. Notez la nouvelle adresse et fermez la page. Maintenant, avec cette adresse sélectionnée, cliquez sur Actions, puis sur « Associer l'adresse ». Je cliquerai une fois dans la boîte Instance et mon instance OpenVPN — avec son tag utile — est listée. Je n'ai qu'à la sélectionner, cliquer sur « Associer » et j'ai terminé. À partir de maintenant, ce sera l'IP publique permanente pour accéder à notre serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/rQJ5leTI2CTmKdeHxJ8dacPyBz4ueo19IiFe)
_Associez votre nouvelle adresse IP élastique à votre instance_

### Accéder au serveur

Je vais coller l'adresse IP publique dans le terminal dans le cadre de ma commande SSH qui appelle la paire de clés que j'ai définie pour cette instance.

```
ssh -i KeyPairName.pem openvpnas@<PublicIPAddress>
```

Si vous accédez depuis une machine Windows ou macOS, les choses peuvent fonctionner un peu différemment, mais la documentation vous donnera toute l'aide dont vous aurez besoin.

Avant de quitter la console des instances, cependant, je vais effectuer une autre fonction importante. Avec l'instance OpenVPN sélectionnée, je cliquerai sur Actions puis sur Networking et ensuite sur « Change Source/Dest checking ». Je m'assurerai que cette vérification est désactivée. Rien de beaucoup ne sera possible à moins que je ne fasse cela.

Maintenant, je passe à ma session SSH. Dès qu'elle commence, je suis confronté à l'accord de licence EULA d'OpenVPN, puis à l'assistant de configuration. Si vous devez modifier un paramètre plus tard, vous pouvez toujours exécuter à nouveau l'assistant en utilisant cette commande :

```
sudo ovpn-init --ec2
```

La plupart des valeurs par défaut de l'assistant fonctionneront bien, mais il vaut la peine d'expliquer rapidement ce qui se passe. Voici les questions et quelques commentaires où nécessaire :

```
Nœud principal du serveur d'accès ? oui [Vous répondriez non si vous configuriez un nœud de sauvegarde ou de basculement.]
Spécifiez l'interface réseau et l'adresse IP à utiliser par l'interface utilisateur Web Admin [1 — Pour toutes les interfaces ; peut être modifié en statique plus tard.]
Spécifiez le numéro de port pour l'interface utilisateur Web Admin [par défaut]
Spécifiez le numéro de port TCP pour le démon OpenVPN [par défaut]
Le trafic client doit-il être routé par défaut via le VPN ? [non — Ce n'est pas le type de VPN que nous construisons ici. Ce que nous faisons est uniquement de permettre aux clients distants d'accéder en toute sécurité à notre VPC. Il en va de même pour le trafic DNS des clients.]
Le trafic DNS des clients doit-il être routé par défaut via le VPN ? [non]
Utiliser l'authentification locale via la base de données interne ? [non — peut être utile, mais nous utiliserons l'authentification Linux/AWS pour simplifier.]
Les sous-réseaux privés doivent-ils être accessibles aux clients par défaut ? [oui — c'est tout l'intérêt du VPN, après tout.]
Se connecter à l'interface utilisateur Admin en tant que « openvpn » ? [oui]
Fournir la clé de licence du serveur d'accès OpenVPN [Inutile pour les tests.]
```

Lorsque l'assistant est terminé, je vois certaines informations de connexion et je suis invité à installer le démon de temps réseau NTP. Cela ne sera pas nécessaire sur cette boîte Ubuntu, car il est déjà installé et en cours d'exécution par défaut.

Comme je l'ai mentionné précédemment, je devrai donner un mot de passe à l'utilisateur openvpn afin de pouvoir l'utiliser pour me connecter à l'interface Web. Je le fais en tant que sudo avec la commande passwd.

```
sudo passwd openvpn
```

C'est tout ce dont nous aurons besoin côté serveur. Maintenant, je vais utiliser un navigateur pour me connecter à l'interface Web. J'utilise l'adresse IP publique de notre serveur avec le préfixe sécurisé https, suivi d'une barre oblique et admin.

```
https://<PublicIPAddress>/admin
```

Vous obtiendrez un avertissement « Votre connexion n'est pas privée » car nous utilisons un certificat auto-signé plutôt qu'un certificat fourni par une autorité de certification.

![Image](https://cdn-media-1.freecodecamp.org/images/s-fDsz3rKP9Pf7JqKYbPfyAlhUl4YHfSBz1m)
_Ceci est normal lors de l'utilisation de certificats auto-signés_

Ce n'est pas un problème pour nous, puisque nous n'exposons notre VPN qu'à des utilisateurs sélectionnés au sein de notre entreprise, et ils devraient pouvoir faire confiance à notre certificat. Je vais donc cliquer sur l'avertissement, me connecter et accepter l'EULA.

N'hésitez pas à passer du temps à explorer les fonctionnalités fournies par la console d'administration OpenVPN par vous-même.

![Image](https://cdn-media-1.freecodecamp.org/images/VtQgAuVOfhbLTYII1HOdxO5cJiyQo44JSomR)
_La console d'administration OpenVPN_

### Configuration d'un client VPN

Maintenant, je vais ouvrir la page de l'interface utilisateur client en utilisant l'adresse d'accès Web qui nous a été montrée précédemment, mais cette fois sans la barre oblique admin. Ce n'est rien de plus qu'un écran de connexion où vous pouvez vous authentifier en utilisant le même utilisateur openvpn qu'auparavant. (Vous pouvez toujours créer de nouveaux utilisateurs dans la console d'administration.)

Derrière l'écran de connexion, il y a simplement cet ensemble de liens avec des instructions pour installer l'application cliente OpenVPN sur l'une de ces plateformes. Le dernier lien, cependant, s'appelle « Yourself ».

![Image](https://cdn-media-1.freecodecamp.org/images/GFJB-8yTJ0xVtQ1AXnsD1W0DApG3I6JVVXgz)
_La page du client OpenVPN_

En cliquant dessus, vous serez invité à télécharger et à enregistrer un fichier appelé client.ovpn. Ce fichier contient les paramètres de configuration pour correspondre au serveur et les clés réelles que nous utiliserons pour l'authentification. Vous devez absolument traiter ce fichier avec soin pour qu'il ne tombe pas entre de mauvaises mains. Cela inclut de ne pas l'envoyer par e-mail simple sur des connexions non chiffrées.

Je vais ouvrir le fichier localement et copier le contenu. Ensuite, dans un shell au sein d'une machine virtuelle Linux s'exécutant dans mon réseau local, je vais créer un nouveau fichier appelé client.ovpn et coller le contenu. Si vous aviez cliqué sur le lien « OpenVPN pour Linux » dans l'interface utilisateur client plus tôt, vous auriez vu que la seule étape supplémentaire nécessaire était d'installer OpenVPN en utilisant le gestionnaire de paquets Apt — ou Yum si vous êtes sur une machine CentOS ou Red Hat. Eh bien, cela ne prendra qu'une seule commande. Une fois qu'elle aura fait son travail, nous serons prêts.

```
nano client.ovpnsudo apt updatesudo apt install openvpn
```

Ensuite, nous allons ouvrir la connexion VPN. En tant que root — en utilisant sudo — je vais taper openvpn avec le drapeau config pointant vers le fichier de configuration client.ovpn que je viens de créer.

```
sudo openvpn --config client.ovpn
```

Lorsque vous êtes invité à vous authentifier, utilisez le compte openvpn ainsi que le mot de passe que vous avez créé pour lui sur le serveur.

Maintenant, je vais ouvrir une deuxième session shell sur mon client local afin d'essayer de me connecter en SSH au serveur OpenVPN en utilisant son adresse IP _locale_ — quelque chose qui serait impossible sans une connexion VPN fonctionnelle.

Tout d'abord, exécutez ip a pour lister toutes les interfaces réseau actives sur cette machine.

```
ip a
```

En plus de votre réseau local, vous devriez également voir une interface appelée tun0. Cette interface a été créée par OpenVPN et se situera généralement dans la plage 172.16.x.x.

Je vais me connecter en SSH au serveur distant en utilisant ma clé privée — qui, bien sûr, doit exister localement — et l'adresse IP _privée_ du serveur. Si cela fonctionne, vous aurez un VPN !

```
ssh -i KeyPairName.pem openvpnas@<PrivateIPAddress>
```

Enfin, je vais démontrer que le VPN, tel qu'il est actuellement configuré, nous permettra d'accéder à d'autres ressources privées au sein de notre VPC Amazon. Cela pourrait être utile si, par exemple, vous avez une instance de base de données en cours d'exécution dans le VPC que vous ne pouvez pas exposer au réseau public.

Je vais lancer une instance EC2 Ubuntu standard mais je _ne lui_ donnerai _pas_ d'IP publique. Je vais spécifier le même sous-réseau us-east-1b que nous avons utilisé pour le serveur OpenVPN pour simplifier les choses. Le groupe de sécurité que je vais utiliser permettra l'accès SSH via le port 22 mais rien d'autre.

Une fois que cela fonctionne, je noterai son adresse IP privée et retournerai à mon client local. Une fois que je suis sûr que l'instance est complètement lancée, je me connecterai en utilisant la même clé privée, le nom d'utilisateur « ubuntu » — puisque c'est le défaut pour les instances EC2 Ubuntu normales — et l'adresse privée que je viens de copier.

Encore une fois, si cela fonctionne, vous aurez une connexion VPN entièrement configurée vers vos ressources privées AWS. Savourez le moment.

N'oubliez pas d'éteindre tous vos serveurs et de libérer votre adresse IP élastique lorsque vous avez terminé de les utiliser. Vous ne voulez pas encourir de coûts inutilement.

_Cet article a été adapté d'une partie de mon nouveau cours Pluralsight, « [Connecter les ressources sur site à votre infrastructure AWS](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) ». Il y a beaucoup plus d'informations sur mon site [Bootstrap IT](https://bootstrap-it.com), y compris des liens vers mon livre, Linux in Action, et un cours hybride appelé [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) qui est composé de plus de deux heures de vidéo et d'environ 40 % du texte de Linux in Action._
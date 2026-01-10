---
title: Comment sécuriser vos connexions réseau avec OpenVPN
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-08T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/securing-your-network-connections-using-openvpn
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/openvpn.png
tags:
- name: Linux
  slug: linux
- name: OpenVPN
  slug: openvpn
- name: Security
  slug: security
seo_title: Comment sécuriser vos connexions réseau avec OpenVPN
seo_desc: 'They tell us we live in a hyper-mobile world. Not that I’d know: I rarely
  leave my home office. But of course I only get to enjoy the comforts of my home
  office because all the server resources I could possibly need are available remotely.

  Apparently...'
---

On nous dit que nous vivons dans un monde hyper-mobile. Pas que je sache : je quitte rarement mon bureau à domicile. Mais bien sûr, je ne peux profiter des commodités de mon bureau à domicile que parce que toutes les ressources serveur dont je pourrais avoir besoin sont disponibles à distance.

Apparemment, je ne suis pas seul. Presque tout le monde dont le travail touche à l'informatique accédera à ses outils professionnels depuis des lieux distants de temps en temps. Et étant donné que les réseaux publics par lesquels vous accédez à ces lieux distants sont par nature non sécurisés, vous allez vouloir contrôler soigneusement ces connexions.

Le chiffrement des sites web consiste à s'assurer que les données consommées par vos clients distants sont transférées de manière fiable et invisibles pour quiconque pourrait rôder sur le réseau de connexion. Les VPN, en revanche, se concentrent sur le fait de s'assurer que les données consommées par vos clients distants sont transférées de manière fiable et invisibles pour quiconque pourrait rôder sur le réseau de connexion. Voyez-vous la différence ? Moi non plus.

En fait, il existe toutes sortes de technologies dédiées à la sécurisation des communications réseau, et le principe de la _défense en profondeur_ nous enseigne que vous ne devez jamais vous fier à une seule. Voici donc où vous apprendrez à _ajouter de nouvelles_ couches de protection pour vos activités à distance. Plus précisément, en utilisant le chiffrement pour construire un tunnel de réseau privé virtuel (VPN) afin de permettre des connexions distantes sécurisées et invisibles.

## Construire un tunnel OpenVPN

Mon livre [Linux in Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9) - dont cet article est extrait - parle beaucoup du chiffrement. SSH et SCP peuvent protéger les données transférées via des connexions distantes (chapitre 3), le chiffrement de fichiers peut protéger les données au repos (chapitre 8), et les certificats TLS/SSL peuvent protéger les données en transit entre les sites web et les navigateurs clients (chapitre 9). Mais parfois vos exigences demandent une protection sur une gamme plus large de connexions, car parfois vous avez différents types de travail à faire.

Par exemple ? Certains membres de votre équipe doivent travailler en déplacement en utilisant des points d'accès WiFi publics. Il n'est certainement pas intelligent de supposer que les points d'accès WiFi aléatoires sont sécurisés, mais vos collaborateurs ont besoin d'un moyen de se connecter aux ressources de l'entreprise. Les VPN à la rescousse.

Un tunnel VPN correctement conçu fournit une connexion directe entre les clients distants et un serveur de manière à masquer les données lorsqu'elles sont transférées sur un réseau non sécurisé. Mais alors ? Vous avez déjà vu beaucoup d'outils qui peuvent faire cela en utilisant le chiffrement. La vraie valeur d'un VPN est que, une fois que vous avez ouvert un tunnel, il est possible de connecter des réseaux distants comme s'ils étaient tous ensemble localement. D'une certaine manière, vous contournez ce point d'accès WiFi douteux du café.

En utilisant un tel réseau étendu, les administrateurs peuvent faire leur travail sur leurs serveurs peu importe où ils se trouvent. Mais plus important encore, comme vous pouvez le voir sur la figure, une entreprise avec des ressources réparties dans plusieurs bureaux peut les rendre toutes visibles et accessibles à toutes les équipes qui en ont besoin... où qu'elles soient.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-19.png)
_Tunnel connectant des connexions privées distantes à travers un réseau public_

La simple existence d'un tunnel ne garantit pas la sécurité. Mais l'un des nombreux standards de chiffrement peut être incorporé dans la conception, rendant les choses bien meilleures. Les tunnels construits avec le package open source OpenVPN utilisent le même chiffrement TLS/SSL que vous avez déjà vu utilisé ailleurs. OpenVPN n'est pas le seul choix disponible pour le tunneling, mais il est parmi les plus connus, et il est largement considéré comme un peu plus rapide et probablement plus sécurisé que le protocole alternatif Layer 2 Tunnel Protocol utilisant le chiffrement IPsec.

Pour que votre équipe puisse se connecter en toute sécurité les uns avec les autres depuis la route ou entre plusieurs campus, vous allez construire un serveur OpenVPN pour permettre le partage à la fois des applications et l'accès à l'environnement réseau local du serveur. Pour que cela fonctionne, il devrait suffire de lancer deux VM ou conteneurs. L'un pour jouer le rôle de serveur/hôte et l'autre de client.

La construction d'un VPN implique plusieurs étapes, donc prendre quelques instants pour réfléchir à la vue d'ensemble de la manière dont cela va fonctionner sera probablement utile.

## Configurer un serveur OpenVPN

Avant de commencer, voici un conseil utile. Si vous allez suivre ce processus par vous-même - et je vous recommande fortement de le faire - vous allez probablement vous retrouver à travailler avec plusieurs fenêtres de terminal ouvertes sur votre bureau, chacune connectée à une machine différente. Croyez-moi : à un moment donné, vous allez entrer une commande dans la mauvaise fenêtre et tout gâcher dans votre environnement.

Vous pouvez utiliser la commande hostname pour changer le nom de la machine affiché sur la ligne de commande en quelque chose qui vous rappellera visuellement où vous êtes. Une fois que c'est fait, vous devrez quitter le serveur et vous reconnecter pour que le nouveau paramètre prenne effet.

```
ubuntu@ubuntu:~# hostname OpenVPN-Server
ubuntu@ubuntu:~$ exit 
<Host Workstation>$ ssh ubuntu@10.0.3.134
ubuntu@OpenVPN-Server:~# 
```

Suivre cette approche pour attribuer des noms appropriés à chacune des machines avec lesquelles vous travaillez devrait vous aider à garder une trace de l'endroit où vous vous trouvez.

## Préparer votre serveur pour OpenVPN

L'installation d'OpenVPN sur votre serveur nécessite deux packages : openvpn et, pour gérer le processus de génération des clés de chiffrement, easy-rsa. Les utilisateurs de CentOS doivent, si nécessaire, d'abord installer le dépôt epel-release de la manière dont vous l'avez fait au chapitre 2. Pour vous donner un moyen facile de tester l'accès à une application serveur, vous pourriez également installer le serveur web Apache (apache2 pour Ubuntu et httpd sur CentOS).

Pendant que vous configurez votre serveur, vous pourriez aussi bien le faire correctement et activer un pare-feu qui bloque tous les ports sauf 22 (SSH) et 1194 (le port par défaut d'OpenVPN). Cet exemple illustre la manière dont cela fonctionnera sur ufw d'Ubuntu, mais je suis sûr que vous vous souvenez encore de firewalld de CentOS du chapitre 9.

```
ufw enable
ufw allow 22
ufw allow 1194
```

Pour permettre le routage interne entre les interfaces réseau sur le serveur, vous devrez décommenter une seule ligne (net.ipv4.ip_forward=1) dans le fichier /etc/sysctl.conf. Cela permettra de rediriger les clients distants selon les besoins une fois qu'ils sont connectés. Pour charger le nouveau paramètre, exécutez sysctl -p.

```
nano /etc/sysctl.conf
sysctl -p
```

L'environnement serveur est maintenant entièrement configuré, mais il reste encore du chemin à parcourir avant d'être prêt à activer le serveur.

## Générer des clés de chiffrement

Lorsque vous avez installé OpenVPN, un répertoire /etc/openvpn/ a été automatiquement créé, mais il n'y a pas grand-chose dedans pour l'instant. Cependant, les packages openvpn et easy-rsa sont livrés avec des fichiers modèles d'exemple que vous pouvez utiliser comme base pour votre configuration. Pour démarrer le processus de certification, copiez le répertoire modèle easy-rsa de /usr/share/ vers /etc/openvpn/ puis changez pour le nouveau répertoire easy-rsa/.

```
cp -r /usr/share/easy-rsa/ /etc/openvpn
cd /etc/openvpn/easy-rsa
```

Le premier fichier avec lequel vous allez travailler s'appelle simplement vars, et contient des variables d'environnement que easy-rsa utilisera lorsqu'il générera ses clés. Vous voudrez éditer le fichier pour substituer vos propres valeurs aux valeurs par défaut de l'exemple qui s'y trouvent déjà. Voici à quoi ressemblerait mon fichier :

```
export KEY_COUNTRY="CA"
export KEY_PROVINCE="ON"
export KEY_CITY="Toronto"
export KEY_ORG="Bootstrap IT"
export KEY_EMAIL="info@bootstrap-it.com"
export KEY_OU="IT"
```

L'exécution du fichier vars transmettra ses valeurs à l'environnement shell d'où elles seront incorporées dans le contenu de vos nouvelles clés. Une fois cela fait, le script vous encouragera à exécuter le script clean-all pour supprimer tout contenu existant dans le répertoire /etc/openvpn/easy-rsa/keys/.

```
cd /etc/openvpn/easy-rsa/
. ./vars 
NOTE: If you run ./clean-all, I will be doing a rm -rf on /etc/openvpn/easy-rsa/keys
```

Naturellement, votre prochaine étape sera d'exécuter ce script clean-all... suivi de build-ca qui utilisera le script pkitool pour créer votre certificat racine. Vous serez invité à confirmer les paramètres d'identification fournis par vars.

```
./clean-all
./build-ca
Generating a 2048 bit RSA private key
```

Ensuite, le script build-key-server, puisqu'il utilise le même script pkitool ainsi que le nouveau certificat racine, vous posera les mêmes questions de confirmation pour générer une paire de clés. Les clés seront nommées en fonction de l'argument que vous passez — ce qui, sauf si vous exécutez plusieurs VPN sur cette machine, serait normalement server, comme dans cet exemple.

```
./build-key-server server
[]
Certificate is to be certified until Aug 15 23:52:34 2027 GMT (3650 days)
Sign the certificate? [y/n]:y
1 out of 1 certificate requests certified, commit? [y/n]y
Write out database with 1 new entries
Data Base Updated
```

OpenVPN utilisera des paramètres générés à l'aide de l'algorithme Diffie-Hellman (en exécutant build-dh) pour négocier l'authentification des nouvelles connexions. Le fichier qui sera créé ici n'a pas besoin de rester secret, mais doit avoir été généré à l'aide du script build-dh contre les clés RSA actuellement actives. Si vous créez de nouvelles clés RSA à un moment donné dans le futur, vous devrez également mettre à jour le fichier Diffie-Hellman.

```
build-dh
```

Vos clés côté serveur auront maintenant été écrites dans le répertoire /etc/openvpn/easy-rsa/keys/, mais OpenVPN ne le sait pas. Par défaut, OpenVPN les cherchera dans /etc/openvpn/, alors copiez-les.

```
cp /etc/openvpn/easy-rsa/keys/server* /etc/openvpn
cp /etc/openvpn/easy-rsa/keys/dh2048.pem /etc/openvpn
cp /etc/openvpn/easy-rsa/keys/ca.crt /etc/openvpn
```

## Préparer les clés de chiffrement du client

Comme vous l'avez déjà vu, le chiffrement TLS utilise des paires de clés correspondantes, une installée sur le serveur et l'autre sur un client distant. Cela signifie que vous allez avoir besoin de clés client, et notre vieux copain pkitool est juste ce qu'il faut pour en générer. Cet exemple, exécuté alors que vous êtes toujours dans le répertoire /etc/openvpn/easy-rsa/, passe client comme argument pour générer des fichiers appelés client.crt et client.key.

```
./pkitool client
```

Les deux fichiers client, ainsi que le fichier ca.crt original qui se trouve toujours dans le répertoire keys/, devront maintenant être transférés de manière sécurisée vers votre client. En raison de leur propriété et de leurs permissions, cela pourrait être un peu compliqué. L'approche la plus simple est de copier manuellement le contenu du fichier source (et rien d'autre que ce contenu) dans un terminal exécuté sur le bureau de votre PC (en surlignant le texte, en cliquant dessus avec le bouton droit de la souris et en sélectionnant copier dans le menu) puis en le collant dans un nouveau fichier du même nom que vous créez dans un second terminal connecté à votre client.

Mais n'importe qui peut couper et coller. Au lieu de cela, pensez comme un administrateur — surtout puisque vous n'aurez pas toujours accès à une interface graphique où couper et coller est possible. Au lieu de cela, copiez les fichiers dans le répertoire personnel de votre utilisateur (afin qu'une opération scp distante puisse y accéder) puis utilisez chown pour changer le propriétaire des fichiers de root à votre utilisateur régulier, non-root, afin que l'action scp distante puisse fonctionner. Assurez-vous que vos fichiers sont tous installés et confortables pour l'instant... vous les déplacerez vers le client un peu plus tard.

```
cp /etc/openvpn/easy-rsa/keys/client.key /home/ubuntu/
cp /etc/openvpn/easy-rsa/keys/ca.crt /home/ubuntu/
cp /etc/openvpn/easy-rsa/keys/client.crt /home/ubuntu/
chown ubuntu:ubuntu /home/ubuntu/client.key
chown ubuntu:ubuntu /home/ubuntu/client.crt
chown ubuntu:ubuntu /home/ubuntu/ca.crt
```

Avec un ensemble complet de clés de chiffrement prêt à l'action, vous devrez dire à votre serveur comment vous voulez construire votre VPN. Cela se fait en utilisant le fichier server.conf.

## Configurer le fichier server.conf

Comment êtes-vous censé savoir à quoi doit ressembler le fichier server.conf ? Eh bien, souvenez-vous du répertoire modèle easy-rsa que vous avez copié depuis /usr/share/ ? Eh bien, il y a plus de bonnes choses là où cela vient. L'installation d'OpenVPN a laissé un fichier de configuration modèle compressé que vous pouvez copier dans /etc/openvpn/.

Je vais utiliser le fait que le modèle est compressé pour vous présenter un outil utile : zcat. Vous savez déjà imprimer le contenu texte d'un fichier à l'écran avec cat, mais que faire si le fichier est compressé avec gzip ? Bien sûr, vous pourriez toujours décompresser le fichier et cat sera alors heureux de l'imprimer, mais c'est une ou deux étapes de trop. Au lieu de cela, comme vous l'avez probablement déjà deviné, vous pouvez utiliser zcat pour charger le texte décompressé en mémoire en une seule étape. Dans notre cas, au lieu de l'imprimer à l'écran, vous redirigerez le texte vers un nouveau fichier appelé server.conf.

```
zcat \
 /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz
 > /etc/openvpn/server.conf
cd /etc/openvpn
```

En laissant de côté la documentation extensive et utile qui accompagne le fichier, voici à quoi il pourrait ressembler une fois que vous avez terminé l'édition. Notez qu'un point-virgule (;) indique à OpenVPN de _ne pas_ lire et exécuter la ligne qui suit.

```
port 1194
# TCP ou UDP server?
proto tcp
;proto udp
;dev tap
dev tun
ca ca.crt
cert server.crt
key server.key # Ce fichier doit être gardé secret
dh dh2048.pem
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt
push "route 10.0.3.0 255.255.255.0"
keepalive 10 120
comp-lzo
port-share localhost 80 
user nobody 
group nogroup
persist-key
persist-tun
status openvpn-status.log
log openvpn.log 
;log-append openvpn.log
verb 3 
```

Travaillons sur certains de ces éléments un par un.

* Par défaut, OpenVPN fonctionne sur le port 1194. Vous pouvez changer cela — peut-être pour obscurcir davantage vos activités, ou éviter les conflits avec d'autres tunnels actifs. Mais, parce que cela nécessitera le moins de coordination entre les clients, 1194 est normalement votre meilleur choix.
* OpenVPN peut utiliser soit le protocole de contrôle de transmission (TCP) soit le protocole de datagramme utilisateur (UDP) pour les transmissions de données. TCP peut être un peu plus lent, mais il est plus fiable et plus susceptible de s'entendre avec les applications fonctionnant à chaque extrémité du tunnel.
* Vous spécifiez dev tun lorsque vous voulez créer un tunnel IP plus simple et plus efficace qui transfère le contenu des données et rien de plus. Si, en revanche, vous devrez connecter plusieurs interfaces réseau (et les réseaux qu'elles représentent) en créant un _pont ethernet_, alors vous devrez sélectionner dev tap. Si vous n'avez aucune idée de ce que tout cela signifie, optez pour tun.
* Les quatre lignes suivantes passent à OpenVPN les noms des trois fichiers d'authentification du serveur et le fichier de paramètres dh2048 que vous avez créé précédemment.
* La ligne server définit la plage de sous-réseau et le masque de réseau qui seront utilisés pour attribuer des adresses IP aux clients lorsqu'ils se connectent.
* Le paramètre optionnel push "route 10.0.3.0 255.255.255.0" permettra aux clients distants d'accéder aux sous-réseaux privés "derrière" le serveur. Pour que cela fonctionne, il faudra également configurer le réseau sur le serveur lui-même pour s'assurer que le sous-réseau privé est conscient du sous-réseau OpenVPN (10.8.0.0).
* port-share localhost 80 permet au trafic client entrant sur le port 1194 d'être redirigé vers un serveur web local écoutant sur le port 80. Cela sera utile dans notre cas puisque nous allons utiliser un serveur web pour tester notre VPN. Cela ne fonctionnera que lorsque proto est défini sur tcp.
* Les lignes user nobody et group nogroup doivent être activées en supprimant les points-virgules. Forcer les clients distants à travailler en tant que nobody et nogroup garantit que leurs sessions sur le serveur seront non privilégiées.
* log définit les entrées de journal actuelles pour écraser les anciennes entrées à chaque fois qu'OpenVPN démarre, tandis que log-append ajoute de nouvelles entrées au fichier journal existant. Le fichier openvpn.log lui-même sera écrit dans le répertoire /etc/openvpn/.

En outre, il est également très courant d'ajouter client-to-client au fichier de configuration afin que plusieurs clients puissent se voir les uns les autres en plus du serveur OpenVPN.

Une fois que vous êtes satisfait de votre configuration, vous êtes prêt à lancer le serveur OpenVPN.

```
systemctl start openvpn
```

L'exécution de ip addr pour lister les interfaces réseau de votre serveur devrait maintenant inclure une référence à une nouvelle interface appelée tun0. Celle-ci aura été créée par OpenVPN pour l'usage des clients entrants.

```
ip addr
[]
4: tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc []
 link/none 
 inet 10.8.0.1 peer 10.8.0.2/32 scope global tun0
 valid_lft forever preferred_lft forever
```

Il est _possible_ que vous deviez redémarrer le serveur avant que tout ne fonctionne pleinement. Prochaine étape : l'ordinateur client.

## Configurer un client OpenVPN

Traditionnellement, les tunnels sont construits avec au moins deux extrémités (sinon nous préférons les appeler des grottes). Avoir OpenVPN correctement configuré sur le serveur dirige le trafic dans et hors du tunnel à cette extrémité. Mais vous aurez également besoin d'un certain type de logiciel fonctionnant côté client.

> _Dans cette section, je vais me concentrer sur la configuration manuelle d'un ordinateur Linux d'un type ou d'un autre pour qu'il agisse comme un client OpenVPN. Mais ce n'est pas la seule façon dont vous pourriez vouloir consommer le service. OpenVPN lui-même maintient des applications client qui peuvent être installées et utilisées sur des ordinateurs de bureau/laptops Windows ou Mac, ou des smartphones et tablettes Android et iOS. Voir le site web [https://openvpn.net](https://openvpn.net/) pour plus de détails._

Le package OpenVPN devra être installé sur la machine cliente, comme il l'a été sur le serveur — bien qu'il n'y ait pas besoin d'easy-rsa ici, car les clés que vous allez utiliser existent déjà. Vous devrez copier le fichier modèle client.conf dans le répertoire /etc/openvpn/ que l'installation vient de créer. Cette fois, pour une raison quelconque, le fichier ne sera pas compressé, donc une simple commande cp fera très bien le travail.

```
apt install openvpn
cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf \
 /etc/openvpn/
```

La plupart des paramètres dans votre fichier client.conf seront assez évidents : ils devront correspondre aux valeurs utilisées par le serveur. Comme vous pouvez le voir dans le fichier exemple ci-dessous, celui qui est unique est remote 192.168.1.23 1194 — qui pointe le client vers l'adresse IP du serveur. Encore une fois, assurez-vous d'utiliser l'adresse réelle de votre serveur. Vous devriez également forcer votre client à vérifier l'authenticité du certificat du serveur pour prévenir une possible attaque de type man-in-the-middle. Une façon de faire cela est d'ajouter la ligne remote-cert-tls server.

```
client 
;dev tap
dev tun
proto tcp
remote 192.168.1.23 1194 
resolv-retry infinite
nobind
user nobody
group nogroup
persist-key
persist-tun
ca ca.crt
cert client.crt
key client.key
comp-lzo
verb 3
remote-cert-tls server 
```

Vous pouvez maintenant vous déplacer vers le répertoire /etc/openvpn/ et récupérer ces clés de certification depuis le serveur. Vous substituerez évidemment l'adresse IP ou le nom de domaine réel de votre serveur à celui de l'exemple.

```
cd /etc/openvpn
scp ubuntu@192.168.1.23:/home/ubuntu/ca.crt . 
scp ubuntu@192.168.1.23:/home/ubuntu/client.crt .
scp ubuntu@192.168.1.23:/home/ubuntu/client.key .
```

Rien d'excitant ne se produira probablement jusqu'à ce que vous lanciez OpenVPN sur le client. Parce que vous devrez passer un couple d'arguments, vous déclencherez depuis la ligne de commande. — tls-client indique à OpenVPN que vous agirez en tant que client et que vous vous connecterez via le chiffrement TLS tandis que — config pointe vers votre fichier de configuration.

```
openvpn  tls-client  config /etc/openvpn/client.conf
```

Lisez attentivement la sortie de la commande pour vous assurer que vous êtes correctement connecté. Si quelque chose ne va pas la première fois, c'est probablement dû à une incompatibilité de paramètre entre les fichiers de configuration du serveur et du client ou peut-être à un problème de connectivité réseau/pare-feu. Voici quelques étapes de dépannage :

* Lisez attentivement la sortie de l'opération OpenVPN sur le client — elle contient souvent des indices précieux sur ce qu'elle n'a pas pu faire et pourquoi.
* Vérifiez les messages liés aux erreurs dans les fichiers openvpn.log et openvpn-status.log dans le répertoire /etc/openvpn/ sur le serveur.
* Vérifiez les messages OpenVPN pertinents et récents dans les journaux système sur le serveur et le client (journalctl -ce imprimera un écran rempli des entrées les plus récentes).
* Confirmez que vous avez une connexion réseau active entre le serveur et le client (voir le chapitre 14 pour plus de détails).

_Cet article est extrait de mon livre_ [_Manning « Linux in Action »_](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9)_. Il y a beaucoup plus de plaisir_ [_d'où cela vient_](https://bootstrap-it.com/index.php/books/)_,_ incluant un cours hybride appelé [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) qui est composé de plus de deux heures de vidéo et d'environ 40% du texte de Linux in Action. _Qui sait... vous pourriez aussi apprécier mon_ [_Learn Amazon Web Services in a Month of Lunches_](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27)_._
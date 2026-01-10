---
title: Comment exécuter des conteneurs Docker compatibles IPv6 sur AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T16:39:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-ipv6-enabled-docker-containers-on-aws-87e090ab0397
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E3u4QZGhjH8VH_X3fzMWfQ.png
tags:
- name: AWS
  slug: aws
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment exécuter des conteneurs Docker compatibles IPv6 sur AWS
seo_desc: 'By Nicolas Leiva

  Do you want to forget about NAT and run containers without having to translate IP
  addresses? Then you need public IP addresses, lots of them. Unfortunately, the price
  of each IPv4 address is exceeding $20, so you won’t get one for ea...'
---

Par Nicolas Leiva

Voulez-vous oublier le NAT et exécuter des conteneurs sans avoir à traduire les adresses IP ? Alors vous avez besoin d'adresses IP publiques, et en grande quantité. Malheureusement, le prix de chaque adresse IPv4 [dépasse 20 $](http://www.circleid.com/posts/20181024_the_2018_ipv4_market_third_quarter_report/), donc vous n'en aurez pas une pour chacun de vos conteneurs. En revanche, il n'y a pas de pénurie d'adresses IPv6, donc vous pourriez en théorie assigner une adresse unique à autant de conteneurs que vous le souhaitez.

Lorsque le protocole Internet (**IP**) qui aide à livrer cet article de blog à votre appareil a été défini [en 1981](https://tools.ietf.org/html/rfc791), les adresses internet qui identifient les sources et les destinations ont été spécifiées comme ayant une longueur fixe de quatre octets (**32 bits**). Il s'agit en fait de la quatrième version du protocole, donc nous faisons référence à ces adresses comme étant des adresses IP version 4 (**IPv4**).

Approximativement une décennie plus tard, [en 1992](https://tools.ietf.org/html/rfc1338), il est devenu évident que nous finirions par manquer d'adresses IPv4 32 bits, donc en [mars 1994](https://tools.ietf.org/html/rfc1597), des adresses **IP privées** réutilisables ont été définies dans une tentative de préserver l'espace d'adressage IP. Vous utilisez celles-ci pour identifier les hôtes privés d'une entreprise. Si l'un de ces hôtes doit se connecter à un hôte externe, son adresse doit être traduite en une adresse **IP publique** globalement unique. Ce processus est connu sous le nom de traduction d'adresse réseau (**NAT**) et a été défini [quelques mois plus tard](https://tools.ietf.org/html/rfc1631).

Environ [un an plus tard (1995)](https://www.rfc-editor.org/rfc/rfc1883.txt), une nouvelle version du protocole Internet est sortie pour fournir, [entre autres choses](https://tools.ietf.org/html/rfc2460#page-2), des capacités d'adressage étendues. Nous connaissons cela sous le nom d'**IPv6**, qui augmente la taille de l'adresse IP de 32 bits à **128 bits**.

> Le problème ? IPv6 n'est pas rétrocompatible avec IPv4, donc la transition a été vraiment, vraiment lente... Plus de 20 ans maintenant avec une adoption actuelle d'environ ~22 % [adoption de ~22 %](https://www.google.com/intl/en/ipv6/statistics.html).

Quoi qu'il en soit, le but de cet article est de démontrer comment exécuter des conteneurs sur un fournisseur de cloud (AWS) en utilisant IPv6. C'est quelque chose qui était en attente de mon précédent article : [Kubernetes multi-cluster networking made simple](https://medium.com/@nleiva/kubernetes-multi-cluster-networking-made-simple-c8f26827813). La topologie cible est la suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/MxC6Wfw0JBNLbelksIgWkgtnukt8PrBUN7qY)

Bien que nous ne puissions pas actuellement diviser un bloc IPv6 alloué à un `VPC` (`/56`), pour assigner des sous-réseaux plus petits (`/64`) aux instances dans AWS, nous pouvons utiliser des interfaces réseau élastiques ([ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)) pour associer un bloc contigu d'adresses IPv6 à une instance. Cela générera une longueur de préfixe IPv6 supérieure à `/64`—dans cet exemple `/126`—ce qui n'est pas une meilleure pratique dans un LAN, donc prenez cela avec des pincettes.

En résumé, voici ce que nous allons faire :

1. Créer des instances [EC2](https://aws.amazon.com/ec2/) avec une [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) attachée.
2. Reconfigurer l'adressage IPv6 sur l'instance et installer Docker.
3. Exécuter quelques conteneurs en utilisant uniquement IPv6.

### Créer des instances EC2 avec une ENI attachée

Nous allons utiliser l'AWS [CLI](https://aws.amazon.com/cli/) [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html) pour créer une [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) avec une adresse IPv6 principale et également un bloc contigu d'adresses IPv6 pour chacune de nos instances. Ces adresses proviendront d'un `Subnet` connu. Nous appliquerons également un `Security Group` à notre [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html).

#### Subnet, Security Group et ENI

Si vous n'avez pas de `VPC` avec support IPv6 déjà, veuillez consulter [Getting Started with IPv6 for Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/get-started-ipv6.html), afin que vous puissiez stocker l'ID du `Subnet` et du `Security Group` dans les variables `subnetId` et `sgId`.

```
subnetId=subnet-09a931730fa9exxxxsgId=sg-0eaf439572982yyyy
```

Pour `instance-1`, nous allons réserver les adresses `::1:1`, `::8`, `::9`, `::a` et `::b`. J'ai supprimé le préfixe de sous-réseau pour faciliter la lecture. La première adresse sera pour l'instance, et les quatre autres formeront le `/126` dont nous avons besoin pour le pont Linux auquel les conteneurs seront connectés.

```
2600:1f18:47b:ca03::1:12600:1f18:47b:ca03::82600:1f18:47b:ca03::92600:1f18:47b:ca03::a2600:1f18:47b:ca03::b
```

Pour notre `instance-2`, nous allons réserver les adresses `::2:2`, `::c`, `::d`, `::e` et `::f`.

```
2600:1f18:47b:ca03::2:22600:1f18:47b:ca03::c2600:1f18:47b:ca03::d2600:1f18:47b:ca03::e2600:1f18:47b:ca03::f
```

Avec toutes ces informations, nous exécutons la commande [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html). Cependant, nous devons également stocker l'ID de [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) pour les opérations suivantes, donc nous `query` `NetworkInterface.NetworkInterfaceId` et stockons la valeur retournée dans `eni1` pour `instance-1`.

```
eni1=`aws ec2 create-network-interface \  --subnet-id $subnetId \  --description "My IPv6 ENI 1" \  --groups $sgId \  --ipv6-addresses \  Ipv6Address=2600:1f18:47b:ca03::1:1 \  Ipv6Address=2600:1f18:47b:ca03::8 \  Ipv6Address=2600:1f18:47b:ca03::9 \  Ipv6Address=2600:1f18:47b:ca03::a \  Ipv6Address=2600:1f18:47b:ca03::b \  --query 'NetworkInterface.NetworkInterfaceId' \  --output text`
```

Vous pouvez vérifier la valeur retournée comme suit.

```
$ echo $eni1eni-08ba7c2f50a22a160
```

Répétez pour la deuxième [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html).

```
eni2=`aws ec2 create-network-interface \  --subnet-id $subnetId \  --description "My IPv6 ENI 2" \  --groups $sgId \  --ipv6-addresses \  Ipv6Address=2600:1f18:47b:ca03::2:2 \  Ipv6Address=2600:1f18:47b:ca03::c \  Ipv6Address=2600:1f18:47b:ca03::d \  Ipv6Address=2600:1f18:47b:ca03::e \  Ipv6Address=2600:1f18:47b:ca03::f \  --query 'NetworkInterface.NetworkInterfaceId' \  --output text`
```

#### Lancement des instances avec ENI attachée

Amazon EC2 utilise la cryptographie à clé publique pour chiffrer et déchiffrer les informations de connexion [[Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)], donc vous avez besoin d'une clé publique et privée pour vous connecter aux instances.

Vous pouvez utiliser une clé existante ou en créer une nouvelle comme suit, où `~/.ssh/id_rsa.pub` est l'emplacement de votre fichier de clé publique.

```
aws ec2 import-key-pair \  --key-name <name> \  --public-key-material file://~/.ssh/id_rsa.pub
```

Nous allons stocker le nom de la paire de clés dans une variable nommée `AWS_SSH_KEY`. Vous pouvez soit assigner le nom manuellement, comme vous venez de le choisir, soit le récupérer depuis AWS avec `describe-key-pairs`.

```
AWS_SSH_KEY=$(aws ec2 describe-key-pairs --query KeyPairs[0].KeyName --output text)
```

Il est maintenant temps de créer les instances. Nous allons utiliser l'ID d'AMI `ami-0ac019f4fcb7cb7e6`, qui est `Ubuntu Server 18.04 LTS`, et le type d'instance `r5d.large`.

Le nombre d'adresses IP que vous pouvez assigner à une instance est limité par son type, donc pour `r5d.large`, par exemple, nous pouvons aller jusqu'à 10 adresses IPv6, ce qui est suffisant pour cette petite preuve de concept. Voir les détails pour le type d'instance dans [IP Addresses Per Network Interface Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI).

Nous voulons également attacher l'[ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) que nous avons créée précédemment, dont l'ID était stocké dans `eni1`. Nous conservons l'ID de l'instance que nous recevons d'AWS dans `vm1` (nous interrogeons `Instances[0].InstanceId`).

```
vm1=`aws ec2 run-instances \  --key-name $AWS_SSH_KEY \  --image-id ami-0ac019f4fcb7cb7e6 \  --instance-type r5d.large \  --network-interfaces DeviceIndex=0,NetworkInterfaceId=$eni1 \  --query 'Instances[0].InstanceId' \  --output text`
```

De même pour `instance-2`.

```
vm2=`aws ec2 run-instances \  --key-name $AWS_SSH_KEY \  --image-id ami-0ac019f4fcb7cb7e6 \  --instance-type r5d.large \  --network-interfaces DeviceIndex=0,NetworkInterfaceId=$eni2 \  --query 'Instances[0].InstanceId' \  --output text`
```

Ensuite, obtenons la première adresse IPv6 publique de `instance-1` et stockons-la dans `ip1`.

```
ip1=`aws ec2 describe-instances \  --filter Name=instance-id,Values=$vm1 \  --output text \  --query 'Reservations[].Instances[].NetworkInterfaces[].\Ipv6Addresses[0].Ipv6Address'`
```

Vous pouvez maintenant accéder à `instance-1` avec `ssh -i <private key file> ubuntu@`${ip1}. De même, pour `instance-2`, vous pouvez récupérer la première adresse IPv6 publique avec :

```
ip2=`aws ec2 describe-instances \  --filter Name=instance-id,Values=$vm2 \  --output text \  --query 'Reservations[].Instances[].NetworkInterfaces[].\Ipv6Addresses[0].Ipv6Address'`
```

Ainsi, vous pouvez y accéder avec `ssh -i <private key file> ubuntu@`${ip2}.

#### Rendre les instances compatibles IPv6

Nous devrons installer des logiciels dans nos instances. Malheureusement, cela ne sera pas possible immédiatement car notre fichier `sources.list` contient des liens vers `[us-east-1.ec2.archive.ubuntu.com](http://us-east-1.ec2.archive.ubuntu.com/ubuntu/)` qui ne se résolvent pas en une adresse IPv6. Nous devons remplacer ceux-ci pour utiliser `[archive.ubuntu.com](http://us-east-1.ec2.archive.ubuntu.com/ubuntu/)` à la place, qui prend correctement en charge IPv6. Vous pouvez faire cela avec `sed`.

```
sudo sed -i 's/us-east-1\.ec2\.//g' /etc/apt/sources.list
```

Vous pouvez maintenant utiliser `apt-get` avec l'option `Acquire::ForceIPv6=true`.

```
$ sudo apt-get -o Acquire::ForceIPv6=true updateGet:1 http://archive.ubuntu.com/ubuntu bionic InRelease [242 kB]Get:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [83.2 kB]Get:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]...Get:38 http://archive.ubuntu.com/ubuntu bionic-backports/universe Sources [2068 B]Get:39 http://archive.ubuntu.com/ubuntu bionic-backports/universe amd64 Packages [3468 B]Get:40 http://archive.ubuntu.com/ubuntu bionic-backports/universe Translation-en [1604 B]Fetched 28.4 MB in 5s (5363 kB/s)Reading package lists... Done
```

### Reconfigurer l'adressage IPv6 sur l'instance et installer Docker

Actuellement, nos instances ont une seule interface avec plusieurs adresses IPv6. `instance-1` montre cinq adresses IPv6 `/128`.

```
$ ip add...2: ens5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000...    inet6 2600:1f18:47b:ca03::1:1/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec    inet6 2600:1f18:47b:ca03::8/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec    inet6 2600:1f18:47b:ca03::9/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec    inet6 2600:1f18:47b:ca03::a/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec    inet6 2600:1f18:47b:ca03::b/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec
```

#### Nouvelle distribution des adresses IPv6

Nous voulons seulement une (`/64`) sur l'interface principale et un `/126` sur un pont Linux (docker0) pour allouer des adresses à nos conteneurs à partir de cette plage. À cette fin, nous allons éditer le fichier de configuration de [netplan](https://netplan.io/) à `/etc/netplan/50-cloud-init.yaml`. Il ressemble initialement à ceci :

```
network:  version: 2  ethernets:    ens5:      dhcp4: true      dhcp6: true      match:        macaddress: 12:fb:b4:8b:15:f8      set-name: ens5
```

Nous supprimons simplement l'instruction `dhcp6`.

```
network:  version: 2  ethernets:    ens5:      dhcp4: true      match:        macaddress: 12:fb:b4:8b:15:f8      set-name: ens5
```

En aparté, et complètement **optionnel**, l'adresse `MAC` de l'instance et les adresses IPv6 qui lui sont associées peuvent être récupérées depuis les [Instance Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval) à tout moment.

```
$ curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/12:fb:b4:8b:15:f8
```

Et :

```
$ curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/12:fb:b4:8b:15:f8/ipv6s/2600:1f18:47b:ca03:0:0:0:82600:1f18:47b:ca03:0:0:0:92600:1f18:47b:ca03:0:0:0:a2600:1f18:47b:ca03:0:0:0:b2600:1f18:47b:ca03:0:0:1:1
```

> ⚠️ Oui, [Instance Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval) est un service IPv4 uniquement. La bonne nouvelle est que vous n'avez pas besoin d'une adresse IPv4 publique pour y accéder.

En continuant avec la configuration de l'interface de l'instance, nous devons également créer un fichier séparé pour la configuration IPv6 à `/etc/netplan/60-ipv6-static.yaml`.

```
network:  version: 2  ethernets:    ens5:      dhcp6: no      accept-ra: no      addresses:      - 2600:1f18:47b:ca03::1:1/64      gateway6: fe80::1066:30ff:feb8:c008
```

Nous avons désactivé DHCPv6 (`dhcp6: no`) et ignoré les annonces de routeur IPv6 (`accept-ra: no`). Les informations de passerelle (`fe80::1066:30ff:feb8:c008`) proviennent d'une commande `iproute2` (il semble que ce soit toujours la même dans EC2).

```
$ ip -6 route | grep defaultdefault via fe80::1066:30ff:feb8:c008 dev ens5 proto ra metric 100 pref medium
```

Enfin, appliquez nos modifications de configuration avec `netplan apply`.

```
sudo netplan --debug apply
```

Nous répétons pour `instance-2` avec les adresses correspondantes.

#### Installer Docker

Vous pouvez suivre le [guide d'installation officiel](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce) ou simplement exécuter les commandes suivantes. Notez l'option `Acquire::ForceIPv6=true` pour `apt-get`.

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"sudo apt-get -o Acquire::ForceIPv6=true updatesudo apt-get -o Acquire::ForceIPv6=true install -y docker-cesudo usermod -aG docker ${USER}
```

Vous devez vous déconnecter et vous reconnecter pour que les modifications de l'utilisateur prennent effet.

Nous allons éditer/créer un fichier de configuration Docker à `/etc/docker/daemon.json` pour commencer à allouer des adresses IPv6 à nos conteneurs. Cela devrait ressembler à ceci pour `instance-1`.

```
{  "ipv6": true,  "fixed-cidr-v6": "2600:1f18:47b:ca03::8/126"}
```

Ensuite, redémarrez le démon pour appliquer les modifications ; `sudo systemctl restart docker`. Nous avons maintenant réussi à diviser l'allocation d'adresses IPv6 de l'[ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) entre l'interface principale et le pont Docker.

```
$ ip add...2: ens5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000...    inet6 2600:1f18:47b:ca03::1:1/64 scope global       valid_lft forever preferred_lft forever...3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default...    inet6 2600:1f18:47b:ca03::9/126 scope global tentative       valid_lft forever preferred_lft forever...
```

Faites de même pour `instance-2`, avec `fixed-cidr-v6` = `::c/126`.

### Exécuter quelques conteneurs en utilisant uniquement IPv6

Nous sommes prêts à exécuter des conteneurs. Ou du moins, c'est ce que je pensais. Il s'avère que `registry-1.docker.io` et `hub.docker.com` ne supportent pas IPv6, donc nous ne pouvons pas obtenir d'images Docker depuis ceux-ci. ?

#### Exécuter une image

Avons-nous atteint une impasse ? Non, le Google Container Registry vient à notre secours ! → `gcr.io/gcp-runtimes/ubuntu_18_0_4:latest`. Exécutons cela sur chaque instance.

```
docker run -it --rm gcr.io/gcp-runtimes/ubuntu_18_0_4:latest bash
```

Installez `ping` et `iproute2` dans chaque conteneur pour effectuer des tests de connectivité et vérifier la table de routage.

```
apt-get -o Acquire::ForceIPv6=true updateapt-get -o Acquire::ForceIPv6=true install iputils-ping iproute2 -y
```

À ce stade, nous avons déjà validé que les instances peuvent accéder à Internet via IPv6 (via `apt-get`). Regardons les adresses IP allouées ; nous avons obtenu `::a` dans le conteneur sur `instance-1` (`container-1`). De même, nous avons obtenu `::e` dans le conteneur s'exécutant sur `instance-2` (`container-2`).

```
root@d7c9480161f9:/# ip add...4: eth0@if5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default...    inet6 2600:1f18:47b:ca03::a/126 scope global nodad       valid_lft forever preferred_lft forever...
```

Pour rendre cela plus explicite, nous pouvons ping un hôte sur Internet via IPv6.

```
root@d7c9480161f9:/# ping6 ipv6-test.com -c 1PING ipv6-test.com(agaric.t0x.net (2001:41d0:8:e8ad::1)) 56 data bytes64 bytes from agaric.t0x.net (2001:41d0:8:e8ad::1): icmp_seq=1 ttl=46 time=78.7 ms
```

```
--- ipv6-test.com ping statistics ---1 packets transmitted, 1 received, 0% packet loss, time 0msrtt min/avg/max/mdev = 78.788/78.788/78.788/0.000 ms
```

D'accord, essayons maintenant de ping `container-2` (`d7c9480161f9`) depuis `container-1` (`5312fff41595`).

```
root@d7c9480161f9:/# ping6 2600:1f18:47b:ca03::e -c 1PING 2600:1f18:47b:ca03::e(2600:1f18:47b:ca03::e) 56 data bytes64 bytes from 2600:1f18:47b:ca03::e: icmp_seq=1 ttl=62 time=0.250 ms
```

```
--- 2600:1f18:47b:ca03::e ping statistics ---1 packets transmitted, 1 received, 0% packet loss, time 0msrtt min/avg/max/mdev = 0.250/0.250/0.250/0.000 ms
```

Dans l'autre sens (`container-2` vers `container-1`), juste au cas où. Tout fonctionne. ?

```
root@5312fff41595:/#  ping6 2600:1f18:47b:ca03::a -c 1PING 2600:1f18:47b:ca03::a(2600:1f18:47b:ca03::a) 56 data bytes64 bytes from 2600:1f18:47b:ca03::a: icmp_seq=1 ttl=62 time=0.263 ms
```

```
--- 2600:1f18:47b:ca03::a ping statistics ---1 packets transmitted, 1 received, 0% packet loss, time 0msrtt min/avg/max/mdev = 0.263/0.263/0.263/0.000 ms
```

Si cela ne fonctionne pas pour vous, assurez-vous que le `Security Group` appliqué à l'[ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) autorise l'ICMP IPv6 depuis vos instances. J'ai spécifiquement créé une règle `Custom ICMP Rule — IPv6` entrante avec le même ID de `Security Group` comme source pour faire fonctionner cet exemple.

#### Tables de routage

Explorons la table de routage dans `container-1`.

```
root@d7c9480161f9:/# ip -6 route2600:1f18:47b:ca03::8/126 dev eth0 proto kernel metric 256 pref mediumfe80::/64 dev eth0 proto kernel metric 256 pref mediumdefault via 2600:1f18:47b:ca03::9 dev eth0 metric 1024 pref medium
```

`::9` est l'IP dans `docker0` comme vu dans une sortie de terminal précédente. Qu'en est-il de la table de routage de `instance-1` ?

```
$ ip -6 route2600:1f18:47b:ca03::8/126 dev docker0 proto kernel metric 256 pref medium2600:1f18:47b:ca03::8/126 dev docker0 metric 1024 pref medium2600:1f18:47b:ca03::/64 dev ens5 proto kernel metric 256 pref medium...default via fe80::1066:30ff:feb8:c008 dev ens5 proto static metric 1024 pref medium
```

#### Conseil

[Docker](https://docs.docker.com/v17.09/engine/userguide/networking/default_network/ipv6/#how-ipv6-works-on-docker) suggère d'activer le routage IPv6 sur Linux pour faire fonctionner cela en exécutant les deux lignes suivantes.

```
sudo sysctl net.ipv6.conf.default.forwarding=1sudo sysctl net.ipv6.conf.all.forwarding=1
```

Je n'ai pas eu à le faire pour cet exemple, car les instances EC2 étaient déjà configurées ainsi. Ils ne recommandent également pas les sous-réseaux IPv6 plus petits que `/80`.

> ⚠️ « Le sous-réseau pour les conteneurs Docker doit **avoir au moins une taille de /80**, afin qu'une adresse IPv6 puisse se terminer par l'adresse MAC du conteneur et que vous évitiez les problèmes d'invalidation du cache voisin NDP dans la couche Docker » [[Docker](https://docs.docker.com/v17.09/engine/userguide/networking/default_network/ipv6/#how-ipv6-works-on-docker)]

Enfin, mais non des moindres, je suis tombé sur une [discussion](https://github.com/containernetworking/cni/issues/531) où ils déclarent que IPv6 est désactivé sur les conteneurs dans certaines versions de Docker. J'exécute `18.09.0`.

```
$ docker info  -f '{{.ServerVersion}}'18.09.0
```

Les paramètres réseau du noyau suivants concernent `disable_ipv6` dans le conteneur.

```
root@d7c9480161f9:/# sysctl -a | grep disable_ipv6net.ipv6.conf.all.disable_ipv6 = 1net.ipv6.conf.default.disable_ipv6 = 1net.ipv6.conf.eth0.disable_ipv6 = 0net.ipv6.conf.lo.disable_ipv6 = 0
```

### Conclusion

Bien que cela ne soit pas exactement l'objectif final, il est intéressant de savoir que nous pouvons exécuter des conteneurs IPv6 uniquement dans le cloud **aujourd'hui**. ✅

Ensuite, j'essaierai d'étendre cela et d'exécuter Kubernetes avec uniquement IPv6 sur un fournisseur de cloud... Ou peut-être vérifier le support IPv6 parmi différents fournisseurs de cloud en premier.
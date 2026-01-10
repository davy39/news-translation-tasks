---
title: Ce que sont les réseaux informatiques et comment les comprendre réellement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-14T20:20:18.000Z'
originalURL: https://freecodecamp.org/news/computer-networks-and-how-to-actually-understand-them-c1401908172d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Rs2ZpWMuYgYSIFXVdXVm0g.jpeg
tags:
- name: computer networking
  slug: computer-networking
- name: Devops
  slug: devops
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Ce que sont les réseaux informatiques et comment les comprendre réellement
seo_desc: 'By Sumedh Nimkarde

  Whether you are new to the world of development, or have been building things for
  a long time — or even if you’re a person who just likes computers and uses the internet
  daily — you’ve got to know the basics of networking and speci...'
---

Par Sumedh Nimkarde

Que vous soyez nouveau dans le monde du développement, ou que vous construisiez des choses depuis longtemps — ou même si vous êtes une personne qui aime simplement les ordinateurs et utilise internet quotidiennement — vous devez connaître les bases des réseaux et spécifiquement des Réseaux Informatique.

Si vous aimez creuser davantage dans les serveurs, leur sécurité, et comment vous connecter à vos serveurs depuis un client distant, tout cela nécessite une certaine connaissance des réseaux informatiques et de leurs composants. J'ai essayé de couvrir la plupart des sujets concernant les réseaux informatiques dans cet article.

De plus, à partir d'ici, je vais me référer aux « réseaux informatiques » simplement comme « réseaux ».

Commençons par ma définition de travail des réseaux informatiques :

> _Les réseaux informatiques peuvent être définis comme l'échange de paquets réseau entre des machines informatiques à travers le monde avec l'aide de lignes de données comme des câbles en fil de cuivre, des fibres optiques, etc._

L'**Internet** est un type de réseau informatique. En quelque sorte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q6rT_yRFlwL_kJr2P99XJw.png)

Nous allons examiner certains termes et composants couramment utilisés et comment ils fonctionnent dans un réseau informatique, dont certains sont dans le diagramme ci-dessus.

### Termes couramment utilisés dans les Réseaux Informatique

#### Nœuds

Les nœuds dans les réseaux informatiques désignent tout appareil informatique tel que les ordinateurs, les téléphones mobiles, les tablettes, etc., qui tentent d'envoyer et de recevoir des paquets réseau à travers le réseau vers un autre appareil similaire.

#### Paquets Réseau

Les paquets réseau ne sont rien d'autre que l'information ou les unités de données qu'un nœud source souhaite envoyer/recevoir vers/depuis le nœud de destination. Dans cet article, les paquets réseau/paquets de données transmettent tous la même signification.

#### Protocole Internet (IPs)

Imaginez que vous souhaitez envoyer un cadeau d'anniversaire à votre ami pour son anniversaire, où l'enverrez-vous ? À son adresse postale, n'est-ce pas ?

C'est la même chose ici. Les premiers scientifiques informatiques voulaient identifier les ordinateurs sur internet avec un numéro unique, quelque chose comme les numéros de téléphone aujourd'hui. Ils ont donc inventé le concept de TCP/IP.

Une IP d'un appareil informatique est l'adresse de cet appareil dans un réseau informatique. Techniquement, il s'agit d'un nombre de 32 bits utilisé pour identifier les appareils dans un réseau. Toute la communication vers et depuis l'appareil dans ce réseau sera effectuée en termes de son adresse IP.

Imaginez que vous téléchargez un fichier sur un site ou disons sur Google Drive.

En parlant au niveau le plus bas de la communication réseau, votre fichier est converti en paquets et chaque paquet contient l'adresse du nœud de destination qui n'est rien d'autre que l'adresse IP.

À un niveau supérieur, les adresses IP sont classées en deux types :

* **IPv4** : Les adresses IPv4 sont de 32 bits (quatre octets) comme expliqué dans la définition. Un exemple d'adresse IPv4 serait **104.244.42.129** qui est l'adresse IPv4 de **twitter.com**. Elles sont stables à utiliser et donc utilisées aujourd'hui pour identifier les machines dans le monde.
* **IPv6** : Les adresses IPv6 sont assez nouvelles dans le monde et sont essentiellement huit nombres hexadécimaux séparés par « : ». Un exemple d'adresse IPv6 serait **2001:0cb8:85a3:0000:0000:8a2e:0370:7334**. Elles sont instables et donc pas encore largement utilisées. Le web utilise toujours IPv4 en raison de sa stabilité et il n'y a pas d'estimation de quand nous commencerons à utiliser IPv6 puisque ce n'est pas stable pour l'instant.

IPv4 est classé en cinq classes nommées Classe A, B, C, D, E.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nn10SdJKJ_L2VDuQCwwHLQ.png)
_Octets dans l'adresse IP._

![Image](https://cdn-media-1.freecodecamp.org/images/1*W_MW72XqL54QxKaPHk54UA.png)
_Source : tcpipguide.com_

**Classe A** : Comme montré dans la troisième colonne de l'image ci-dessus, pour les adresses IP de classe A, le premier bit du premier octet de l'adresse IP est constant et est « 0 ».

La deuxième colonne indique les bits de réseau et les bits d'hôte de la classe correspondante d'adresse IP. Considérons dans le cas d'une adresse IP de classe A, nous avons la formule suivante :

**Nombre de réseaux/sous-réseaux = `2^(# de bits de réseau)` .**

**Nombre d'hôtes valides dans chaque sous-réseau = `2^(# de bits d'hôte) — 2` .**

Le nombre de bits de réseau et de bits d'hôte est décidé par le masque de sous-réseau par défaut de la classe d'adresse IP.

Le masque de sous-réseau par défaut pour les adresses IP de classe A est **255.0.0.0**, c'est-à-dire `**11111111.00000000.0000000.00000000**`**.** Ainsi, pour la classe A :

**Bits de réseau = 8, et bits d'hôte = 24.**

_Puisque les bits de réseau = 8_, _bits d'hôte = 24_, leur somme doit être de 32, puisque les adresses IPv4 sont de 32 bits. Mais, puisque nous utilisons le bit (premier bit dans le premier octet) pour identifier la classe :

**_Nombre de bits de réseau utilisables_ = Nombre de bits de réseau — Nombre de bits constants = 8—1 = 7**

_Ainsi, le **Nombre de réseaux possibles dans la Classe A**_ **= `2^7 — 2 = 126`** et,

**_Nombre d'hôtes possibles (c'est-à-dire les appareils qui peuvent être connectés au réseau) par réseau dans la Classe A_ = `2^24-2 = 16277214` .**

Maintenant, ici, pour la classe A, vous pouvez vous demander pourquoi j'ai soustrait un 2 supplémentaire du nombre de réseaux possibles. C'est parce que, pour la classe A, 127.x.y.z a été réservé. Pour les autres classes, la formule habituelle est utilisée.

Ainsi, les adresses IP de classe A vont de `1.x.x.x` à `126.x.x.x`.

**Classe B** : le cas est similaire avec la Classe B. La seule différence est que 2 bits du premier octet sont constants (10) et ils identifient la classe de l'adresse IP qui est la classe B. Tous les autres calculs sont les mêmes, et je ne les mentionne pas ici puisque ils sont faciles à comprendre à partir du tableau ci-dessus. Ils vont de `128.0.x.x` à `191.255.x.x` .

**Classe C** : 3 bits du premier octet sont constants (110) et ils identifient la classe comme la classe C. Ils vont de `192.0.0.x` à `223.255.255.x` .

**Classe D et Classe E** : La Classe D et la Classe E sont utilisées à des fins expérimentales.

Les adresses IPv4 sont principalement de deux types :

* **Statique** : Ces adresses IP sont celles qui restent constantes pour un appareil au fil du temps. Des exemples de celles-ci sont les serveurs distants que nous utilisons pour héberger nos applications, sites web, etc., où nous utilisons le client ssh pour nous connecter à notre serveur.
* **Dynamique** : Généralement, ce sont les adresses IP qu'un ordinateur commun dans un réseau Internet se voit attribuer. Essayez d'éteindre votre routeur et vous verrez un changement dans l'adresse IP de votre ordinateur ! (Mais seulement après avoir lu cet article ?). Maintenant, vous pouvez vous demander qui attribue ces adresses IP ? C'est le serveur DHCP (Dynamic Host Configuration Protocol) qui est expliqué brièvement plus loin dans cet article.

**Note** : Un appareil peut avoir plusieurs adresses IP en même temps. Considérons un appareil connecté à deux réseaux, wifi ainsi qu'un réseau LAN — il aura deux adresses IP. Cela implique que les adresses IP sont attribuées aux interfaces et non directement à l'ordinateur.

D'accord, jusqu'à présent tout va bien. Continuons.

### Routeurs

Comme son nom l'indique, un Routeur est un composant matériel qui prend en charge le routage des paquets. Il détermine de quel nœud le paquet provient et à quel nœud de destination le nœud source veut l'envoyer. Aucun ordinateur ne sait où se trouvent les autres ordinateurs, et les paquets ne sont pas envoyés à tous les ordinateurs. Un Routeur identifie l'adresse du nœud de destination à laquelle un paquet réseau doit être envoyé et le transmet à l'adresse souhaitée.

Les routeurs ont un **« Protocole de Routage »** spécifique qui définit le format dans lequel ils échangent des données avec un autre routeur ou des nœuds de réseau. En d'autres termes, le protocole de routage définit comment les routeurs communiquent entre eux.

Les routeurs construisent une **« Table de Routage »** qui identifie les chemins les plus optimisés à prendre dans le réseau lors de l'envoi de paquets.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eTows8BQKhPE8j76SNSVNA.png)
_Un Routeur._

Techniquement, une table de routage est simplement une table avec la liste des « routes » d'un routeur à un autre. Chaque route se compose de l'adresse des autres routeurs/nœuds dans le réseau et de la manière de les atteindre.

```md
Table de routage :

Destination  Gateway     Genmask        Flags Metric Refs Iface
default      192.168.0.1 0.0.0.0        UG    1024   233  eth0
192.168.0.0  *           255.255.255.0  UC    0      0    wlan0
192.168.0.0  *           255.255.255.0  UH    0      2    eth0
```

Ci-dessus est un exemple de table de routage. Les points clés à noter ici sont :

* **Destination** : Il s'agit de l'adresse IP du nœud de destination. Elle indique où le paquet de données réseau doit aboutir.
* **Gateway** : La passerelle est le composant qui connecte deux réseaux. Imaginez que vous avez un routeur connecté à un autre routeur. Chacun des routeurs a des appareils connectés à celui-ci. Ainsi, l'adresse du dernier routeur (disons R1 ici) après lequel le paquet réseau entre dans l'autre réseau (disons le réseau de R2) est appelée la passerelle. Habituellement, les passerelles ne sont rien d'autre que les routeurs. Laissez-moi donner un autre exemple : disons que votre chambre est un réseau et la chambre de votre frère/sœur à côté de la vôtre est un autre réseau, alors la « porte » entre les deux chambres peut être considérée comme la passerelle. Les gens appellent parfois les « **routeurs** » la passerelle, car c'est ce qu'ils sont, « **une passerelle vers un autre réseau** ».
* **Genmask/Masque de sous-réseau** : Il n'est rien d'autre que le masque de réseau/sous-réseau. Un masque de sous-réseau est un nombre qui, lorsqu'il est combiné avec une adresse IP, vous permet de diviser l'espace IP en morceaux de plus en plus petits pour une utilisation dans les réseaux physiques et logiques. L'explication de la manière dont les calculs de masque de sous-réseau se produisent dépasse le cadre de cet article.
* **Flags** : Différents flags ont une signification différente. Par exemple, dans la première route, « U » dans « UG » signifie que la route est UP, tandis que « G » dans « UG » signifie GATEWAY. Puisque la route signifie une GATEWAY, c'est une porte vers l'autre réseau. Chaque fois que nous envoyons des données via cette route, elles sont envoyées à un autre réseau.
* **Iface (Interface réseau)** : L'interface réseau fait référence au réseau dans lequel la route définie dans la table de routage a l'ordinateur de destination. C'est-à-dire que si vous êtes connecté au Wifi, ce serait « wlan » et lorsque vous êtes connecté à un LAN, ce serait « eth ».

Ainsi, c'est la manière dont un routeur fonctionne, avec l'aide du **Protocole de Routage** et de la **Table de Routage**.

Tout va bien jusqu'à présent. Mais vous devez vous demander —

« D'accord ! Mais hé, nous apprenons les composants ici. J'ai besoin de les assembler et de comprendre comment fonctionne l'internet. »

Super ! Quelques termes de plus et vous aurez une compréhension appropriée de la manière dont tout fonctionne.

### Traduction d'Adresse Réseau (NAT)

La traduction d'adresse réseau est une technique utilisée par les routeurs pour fournir un service internet à plus d'appareils avec une utilisation moindre des IP publiques. Ainsi, un routeur se voit attribuer une seule adresse IP par le FAI et il attribue les IP privées à tous les appareils qui y sont connectés. Le NAT aide les FAI à fournir un accès internet à plus de consommateurs.

Ainsi, si vous êtes connecté au routeur de votre maison, votre IP publique sera visible par le monde, mais pas l'IP privée. Tous les paquets réseau communiqués seront adressés par votre IP publique (c'est-à-dire l'IP publique attribuée au routeur).

![Image](https://cdn-media-1.freecodecamp.org/images/1*rjlWoUU-AeshrGLt0NF1Uw.png)
_Traduction d'adresse réseau (NAT)_

Considérons la figure ci-dessus. Disons que dans votre réseau domestique, vous essayez d'accéder à **medium.com (IP statique distante :** `72.14.204.147`**)**, depuis votre ordinateur (IP privée : `192.168.1.100`).

Ainsi, pour votre ordinateur, la connexion ressemble à ceci :

`192.168.1.100:37641` → `72.14.204.147:80` .

« 37641 » est le numéro de port aléatoire attribué par le routeur NAT à votre appareil/ordinateur. (Lorsqu'il y a une communication réseau entre des démons s'exécutant sur différents ports d'un ordinateur, le port respectif est utilisé par le NAT). Chaque connexion sortante reçoit un port attribué par le routeur NAT.

La connexion est établie dans le NAT comme suit :

```
Private IP   |PrivatePort |PublicIP |PublicPort |Remote |RemotePort
------------- ------------ --------- ----------- ------- -----------
192.168.1.100 | 37641 | 104.244.42.129 | 59273 | 72.14.204.147 | 80
```

Mais, puisque le monde extérieur du réseau ne connaît pas votre adresse privée, la connexion ressemble à ceci pour **medium.com** :

`104.244.42.129:59273` → `72.14.204.147:80` .

Ainsi, nous réalisons l'attribution d'un plus grand nombre d'adresses IP sans gaspiller de nombreuses IP publiques.

Maintenant, lorsque medium.com envoie la réponse à `104.244.42.129:59273`, elle parcourt tout le chemin jusqu'à votre routeur domestique qui recherche ensuite l'IP privée et le port privé correspondants et redirige le paquet vers votre appareil/ordinateur.

**Note** : Le NAT est un concept généralisé. Le NAT peut être réalisé comme 1:1, 1:N où 1, N sont le nombre d'adresses IP dans le réseau. Une technique appelée « IP Masquerading » est un NAT 1:N.

### Protocole de Configuration Dynamique des Hôtes (DHCP)

Le **Protocole de Configuration Dynamique des Hôtes** ou **DHCP** est responsable de l'attribution des adresses IP dynamiques aux hôtes. Le serveur DHCP est maintenu par le FAI ou le routeur précédent s'il y a une chaîne de routeurs pour atteindre l'hôte.

Ainsi, l'attribution des adresses IP est effectuée par le serveur DHCP. Généralement, le FAI maintient un serveur DHCP et les routeurs dans nos maisons reçoivent une IP publique du serveur DHCP.

**Note** : Chaque fois qu'un routeur ou un serveur DHCP maintenu par un FAI ou un routeur redémarre, l'attribution des adresses IP recommence et les appareils se voient attribuer des IP différentes de celles précédentes.

### Système de Noms de Domaine/Serveur

Nous avons déjà discuté du fait que toute machine est identifiée par l'adresse IP.

D'accord, donc vous exécutez un serveur web sur votre `localhost` sur votre machine. Si vous avez creusé dans les hôtes sur une machine Linux, vous auriez rencontré quelque chose comme ceci :

```
127.0.0.1        localhost
255.255.255.255  broadcasthost
::1              localhost
```

ce qui signifie que même si vous tapez `127.0.0.1` dans la barre d'URL de votre navigateur, cela signifiera la même chose que `localhost`.

De manière similaire, les sites web que vous utilisez quotidiennement sont des serveurs web s'exécutant sur une instance/nœud distant ayant une adresse IP statique. Ainsi, taper cette adresse IP dans la barre d'URL de votre navigateur vous mènera au site web ?

Oui, sûrement. Mais, êtes-vous un super-humain pour mémoriser les adresses IP de milliers de sites ?

**NON.**

Ainsi, viennent les domaines que nous utilisons, comme medium.com, twitter.com, behance.net, codementor.io, etc.

> _Un Serveur de Noms de Domaine est un serveur ayant d'énormes enregistrements de mappage de noms de domaine d'adresses IP qui recherche le domaine saisi et retourne l'adresse IP respective de la machine sur laquelle le site web que vous souhaitez accéder est hébergé._

![Image](https://cdn-media-1.freecodecamp.org/images/1*1uiMJkS8rqJDn7eyKRd-ew.png)
_Système de Noms de Domaine (DNS)_

**Comment fonctionne réellement le DNS ?**

1. Le DNS est géré par votre FAI (fournisseur de services internet).
2. Lorsque nous tapons une URL dans la barre d'adresse, les paquets de données voyagent à travers votre routeur, peut-être plusieurs routeurs jusqu'à votre FAI où se trouve votre serveur DNS.
3. Le serveur DNS présent chez le FAI recherche le domaine dans sa base de données. Si une entrée est trouvée, il la retourne.
4. Si aucune entrée n'est trouvée dans sa base de données principale qu'il maintient, le serveur DNS voyagera à travers l'internet vers un autre serveur DNS maintenu par un autre FAI et vérifiera si l'entrée est disponible dans la base de données de cet autre serveur DNS. En plus de retourner l'adresse IP prise d'un autre DNS, il mettra à jour la base de données principale avec cette nouvelle entrée également.
5. Ainsi, parfois (très rarement) un serveur DNS peut devoir traverser plusieurs serveurs DNS pour obtenir une entrée correspondante.
6. Si après avoir traversé de nombreux serveurs DNS à travers l'internet, il ne trouve pas d'entrée correspondante, alors le serveur DNS renvoie une erreur indiquant que le « nom de domaine est invalide ou n'existe pas ».

**Note** :

**L'Internet Corporation for Assigned Names and Numbers (ICANN)** est un consortium (une société à but non lucratif) qui gère l'attribution des noms de domaine et des plages d'adresses IP au nom de la communauté.

Un domaine est divisé en trois parties comme montré dans la figure suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DFJyA2XEEUesen6y5sSkEA.png)

1. **Protocole** : Le protocole utilisé pour accéder au site web, par exemple, HTTP, HTTPS, etc.
2. **Nom de domaine** : Le nom de domaine principal dans notre domaine. Cela peut être n'importe quoi qui est disponible selon le registre ICANN.
3. **Extension de domaine** : C'est celle qui est considérée comme importante lors de l'achat d'un domaine. Généralement, elle est classée en deux types :

* **Domaines de premier niveau génériques (gTLDs)** : Cela inclut les extensions de domaine les plus populaires comme .com, .org, .net, .edu, .co, etc.
* **Domaines de premier niveau de code pays (ccTLDs)** : Ceux-ci indiquent que le domaine est lié au code pays spécifié dans l'extension de domaine. Par exemple, « .in » indique que le site web est originaire d'Inde. De plus, certaines des ccTLDs nécessitent que la personne achetant le domaine soit du même pays. La plupart des petites extensions de code pays ne sont pas recherchables depuis l'extérieur de ce pays.

### Fournisseurs de Services Internet (FAI)

Les **Fournisseurs de Services Internet** sont les entreprises qui fournissent à tous l'Internet. L'article que vous lisez maintenant est grâce à l'internet que votre FAI vous fournit.

Les FAI fournissent l'internet, gèrent le routage de vos requêtes vers la destination correcte, résolvent les noms de domaine avec l'aide du cache DNS qu'ils maintiennent, et gèrent toute cette infrastructure réseau qui nous permet d'utiliser l'internet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fHPSdrVkjQ9tr72ncc7jjQ.png)
_Fournisseurs de Services Internet (FAI)_

Le FAI est une chose hiérarchique fonctionnant à travers l'internet. Il existe certains types de FAI, à savoir les FAI de Niveau 1, Niveau 2, Niveau 3.

* Les FAI de **Niveau 1** sont ceux qui connectent les principaux réseaux sur l'internet. Considérez-les comme les principales autoroutes de l'internet. Ils sont connectés à presque tous les réseaux sur l'internet. De plus, ils fournissent un accès internet aux FAI de Niveau 2. ex. CERFNet, UUNet, PSINet. Ils sont également appelés Fournisseurs de Services Réseau. Ces FAI sont connectés les uns aux autres par des [gros câbles](https://www.google.co.in/search?q=ISP+cables+in+sea&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjO6aPV57XdAhUMyrwKHaZvAJAQ_AUICigB&biw=1920&bih=1006#imgrc=gzXVOSE_UDEmAM:) passant sous la mer.
* Les FAI de **Niveau 2 (Régional)** sont ceux qui fournissent principalement des services Internet aux organisations, aux consommateurs (c'est-à-dire « nous ») ou aux FAI de Niveau 3. La connexion internet que vous utilisez provient d'un FAI de Niveau 2. Cependant, les organisations peuvent également obtenir un accès Internet auprès des FAI de Niveau 1.
* Les FAI de **Niveau 3 (Local)** sont comme les FAI de Niveau 2. C'est simplement un niveau supplémentaire de hiérarchie qui achète de la bande passante à un FAI de Niveau 2 et la vend aux consommateurs.

Le trafic qui passe par votre routeur passe également par le Niveau 3 (s'il est présent), le Niveau 2, et finalement par les FAI de Niveau 1 jusqu'à un autre réseau.

Woot Woot ! Je suis heureux que vous soyez toujours avec moi. Nous allons maintenant rassembler toutes ces choses.

### Rassembler toutes les choses ci-dessus

Jusqu'à présent, nous avons appris tous les composants nécessaires pour faire fonctionner le tout. Maintenant, nous allons les assembler.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8FEZEwZSBHKXGOsevHyeZQ.png)
_Un diagramme détaillé d'un réseau informatique général_

Faisons un résumé de toutes les choses que nous avons apprises :

* Lorsqu'un ordinateur/appareil se connecte, il reçoit une IP privée attribuée par le routeur. Le routeur reçoit une IP publique du FAI.
* Les autres appareils du réseau se voient attribuer des IP privées uniques.
* Les FAI sont ceux qui sont présents à travers le monde et sont connectés les uns aux autres. Ils vendent des services Internet aux FAI régionaux et locaux, auprès desquels nous, les consommateurs, achetons Internet.
* Ainsi, lorsqu'un appareil tente d'établir une connexion réseau avec un autre appareil sur un autre réseau, il le fait avec l'identité de sa passerelle (le routeur). Le routeur mappe ensuite l'IP privée et le numéro de port privé avec l'IP publique et le numéro de port public aléatoire élevé.
* Le routeur envoie ensuite les paquets à la destination souhaitée où un autre routeur ou une autre passerelle fait la même chose que le routeur précédent et analyse de quel ordinateur/appareil provient ce paquet.
* L'ordinateur/appareil distant répond en envoyant la destination comme l'IP publique et le port public du routeur.
* Le routeur vérifie ensuite l'IP privée et le port privé et transmet les paquets réseau.

Ainsi, c'est ainsi que fonctionne l'**Internet** alias **Un type de Réseau Informatique utilisant le protocole TCP/IP**.

Merci d'avoir lu l'article. Si vous avez des questions, n'hésitez pas à les poser dans les commentaires ci-dessous.

Si vous avez aimé cet article, veuillez me donner quelques ? et le partager avec d'autres. À la prochaine. Vous êtes génial !

De plus, si vous souhaitez me soutenir ?

[**Offrir un café à Sumedh Nimkarde - BuyMeACoffee.com**](https://www.buymeacoffee.com/lunaticmonk)  
[_Bonjour, je suis Sumedh et mon travail est de construire, casser et reconstruire des choses._www.buymeacoffee.com](https://www.buymeacoffee.com/lunaticmonk)

Merci encore pour la lecture ! N'hésitez pas à me contacter sur [Twitter](https://twitter.com/lunatic_monk), [GitHub](https://github.com/lunaticmonk).
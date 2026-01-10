---
title: Comment l'Internet communique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T05:30:25.000Z'
originalURL: https://freecodecamp.org/news/how-the-internet-speaks-1ac4ee385e28
coverImage: https://cdn-media-1.freecodecamp.org/images/0*sRvOVIOJ0N6N2h1A.jpg
tags:
- name: internet
  slug: internet
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Sockets
  slug: sockets
- name: 'tech '
  slug: tech
seo_title: Comment l'Internet communique
seo_desc: 'By Zaid Humayun

  A Story Of Communication

  Have you ever wondered how the Internet actually speaks? How does one computer “talk”
  to another computer via the Internet?

  When people communicate with one another, we use words strung into seemingly meaningf...'
---

Par Zaid Humayun

### Une histoire de communication

Vous êtes-vous déjà demandé comment l'Internet communique réellement ? Comment un ordinateur "parle" à un autre ordinateur via l'Internet ?

Lorsque les gens communiquent entre eux, nous utilisons des mots enchaînés en phrases apparemment significatives. Les phrases n'ont de sens que parce que nous avons convenu d'une signification pour ces phrases. Nous avons défini un protocole de communication, en quelque sorte.

Il s'avère que les ordinateurs communiquent entre eux de manière similaire sur l'Internet. Mais nous nous emballons. Les gens utilisent leur bouche pour communiquer, alors essayons d'abord de déterminer quelle est la "bouche" de l'ordinateur.

#### Voici le Socket

Le socket est l'un des concepts les plus fondamentaux en informatique. Vous pouvez construire des réseaux entiers de dispositifs interconnectés en utilisant des sockets.

Comme toutes les autres choses en informatique, un socket est un concept très abstrait. Donc, plutôt que de définir ce qu'est un socket, il est beaucoup plus facile de définir ce qu'un socket fait.

Alors, que fait un socket ? Il aide deux ordinateurs à communiquer entre eux. Comment fait-il cela ? Il a deux méthodes définies, appelées `send()` et `recv()` pour envoyer et recevoir respectivement.

D'accord, c'est super, mais que font réellement `send()` et `recv()` ? Lorsque les gens bougent leur bouche, ils échangent des mots. Lorsque les sockets utilisent leurs méthodes, ils échangent des bits et des octets.

Illustrons les méthodes avec un exemple. Supposons que nous avons deux ordinateurs, A et B. L'ordinateur A essaie de dire quelque chose à l'ordinateur B. Par conséquent, l'ordinateur B essaie d'écouter ce que l'ordinateur A dit. Voici à quoi cela ressemblerait.

![Image](https://cdn-media-1.freecodecamp.org/images/WkJIv8ur462lX2XBWCOF2gv38oTwKk9SmMcP)
_Sockets avec un tampon_

#### Lecture du tampon

Cela semble un peu étrange, n'est-ce pas ? Pour commencer, les deux ordinateurs pointent vers une barre au milieu, intitulée 'tampon'.

Qu'est-ce que le tampon ? Le tampon est une pile de mémoire. C'est là que les données de chaque ordinateur sont stockées, et il est alloué par le noyau.

Ensuite, pourquoi pointent-ils tous les deux vers le même tampon ? Eh bien, ce n'est pas tout à fait exact en réalité. Chaque ordinateur a son propre tampon alloué par son propre noyau et le réseau transporte les données entre les deux tampons séparés. Mais je ne veux pas entrer dans les détails du réseau ici, alors nous supposerons que les deux ordinateurs ont accès au même tampon placé "quelque part dans le vide entre".

D'accord, maintenant que nous savons à quoi cela ressemble visuellement, abstraisons-le en code.

```
# L'ordinateur A envoie des données
computerA.send(data)
```

```
# L'ordinateur B reçoit des données
computerB.recv(1024)
```

Ce snippet de code fait exactement la même chose que l'image ci-dessus représente. À l'exception d'une curiosité, nous ne disons pas `computerB.recv(data)`. Au lieu de cela, nous spécifions un nombre apparemment aléatoire à la place des données.

La raison est simple. Les données sur un réseau sont transmises en bits. Par conséquent, lorsque nous recevons dans computerB, nous spécifions le nombre de _bits_ que nous sommes prêts à recevoir à un moment donné.

Pourquoi ai-je choisi de recevoir 1024 octets à la fois ? Aucune raison spécifique. Il est généralement préférable de spécifier le nombre d'octets que vous recevrez en puissance de 2. J'ai choisi 1024 qui est 2¹⁰.

Alors, comment le tampon comprend-il cela ? Eh bien, l'ordinateur A écrit ou envoie les données qui y sont stockées dans le tampon. L'ordinateur B décide de lire ou de recevoir les 1024 premiers octets de ce qui est stocké dans ce tampon.

D'accord, super ! Mais comment ces deux ordinateurs savent-ils qu'ils doivent se parler ? Par exemple, lorsque l'ordinateur A écrit dans ce tampon, comment sait-il que l'ordinateur B va le récupérer ? Pour reformuler cela, comment peut-il s'assurer qu'une connexion entre deux ordinateurs a un tampon unique ?

#### Portage vers les IP

![Image](https://cdn-media-1.freecodecamp.org/images/iyK61ortQw6U3BXVhmlur2HyrxwJL2pGeEdt)
_Ports et IP des ordinateurs_

L'image ci-dessus montre les deux mêmes ordinateurs sur lesquels nous avons travaillé tout au long avec un détail supplémentaire ajouté. Il y a une série de nombres listés devant chaque ordinateur le long de la longueur d'une barre.

Considérez la longue barre devant chaque ordinateur comme le routeur qui connecte un ordinateur spécifique à l'internet. Ces nombres listés sur chaque barre sont appelés _ports_. Votre ordinateur a des milliers de ports disponibles en ce moment. Chaque port permet une connexion de socket. Je n'ai montré que 6 ports dans l'image ci-dessus, mais vous voyez l'idée.

Les ports inférieurs à 255 sont généralement réservés aux appels système et aux connexions de bas niveau. Il est généralement conseillé d'ouvrir une connexion sur un port dans les chiffres élevés à 4 chiffres, comme 8000. Je n'ai pas dessiné le tampon dans l'image ci-dessus, mais vous pouvez supposer que chaque port a son propre tampon.

La barre elle-même a également un nombre qui lui est associé. Ce nombre est appelé l'adresse IP. L'adresse IP a une série de ports qui lui sont associés. Pensez-y de la manière suivante :

```
                          127.0.0.1                             / | \                            /  |  \                           /   |   \                        8000  8001 8002
```

Super, établissons une connexion sur un port spécifique entre l'ordinateur A et l'ordinateur B.

```
# computerA.py
import socket
```

```
computerA = socket.socket()
```

```
# Connexion à localhost:8000
computerA.connect(('127.0.0.1', 8000))
string = 'abcd'
encoded_string = string.encode('utf-8')
computerA.send(encoded_string)
```

Voici le code pour `computerB.py`

```
# computerB.py
import socket
```

```
computerB = socket.socket()
```

```
# Écoute sur localhost:8000
computerB.bind(('127.0.0.1', 8000))
computerB.listen(1)
```

```
client_socket, address = computerB.accept()
data = client_socket.recv(2048)
print(data.decode('utf-8'))
```

Il semble que nous ayons un peu avancé en termes de code, mais je vais le parcourir. Nous savons que nous avons deux ordinateurs, A et B. Par conséquent, nous avons besoin que l'un envoie des données et que l'autre les reçoive.

J'ai arbitrairement sélectionné A pour envoyer des données et B pour les recevoir. Dans cette ligne `computerA.connect(('127.0.0.1', 8000)`, je fais en sorte que computerA se connecte au port 8000 sur l'adresse IP 127.0.0.1.

> Note : 127.0.0.1 signifie généralement localhost, qui référence votre machine

Ensuite, pour computerB, je le fais se lier au port 8000 sur l'adresse IP 127.0.0.1. Maintenant, vous vous demandez probablement pourquoi j'ai la même adresse IP pour deux ordinateurs différents.

C'est parce que je triche. J'utilise un ordinateur pour démontrer comment vous pouvez utiliser des sockets (je me connecte essentiellement depuis et vers le même ordinateur pour simplifier). Typiquement, deux ordinateurs différents auraient deux adresses IP différentes.

Nous savons déjà que seuls les bits peuvent être envoyés dans un paquet de données, c'est pourquoi nous encodons la chaîne avant de l'envoyer. De même, nous décodons la chaîne sur l'ordinateur B. Si vous décidez d'exécuter les deux fichiers localement, assurez-vous d'exécuter le fichier `computerB.py` en premier. Si vous exécutez le fichier `computerA.py` en premier, vous obtiendrez une erreur de connexion refusée.

#### Servir les clients

![Image](https://cdn-media-1.freecodecamp.org/images/uJcX7ggYtN5ron54t7EL0RdLWtU-YtSEeDSM)
_Transmission de données entre le client et le serveur_

Je suis sûr qu'il a été assez clair pour beaucoup d'entre vous que ce que j'ai décrit jusqu'à présent est un modèle client-serveur très simpliste. En fait, vous pouvez voir cela à partir de l'image ci-dessus, tout ce que j'ai fait est de remplacer l'ordinateur A par le client et l'ordinateur B par le serveur.

Il y a un flux constant de communication qui se déroule entre les clients et les serveurs. Dans notre exemple de code précédent, nous avons décrit un transfert de données ponctuel. Au lieu de cela, ce que nous voulons, c'est un flux constant de données envoyé du client au serveur. Cependant, nous voulons également savoir quand ce transfert de données est terminé, afin de savoir que nous pouvons arrêter d'écouter.

Essayons d'utiliser une analogie pour examiner cela plus en détail. Imaginez la conversation suivante entre deux personnes.

![Image](https://cdn-media-1.freecodecamp.org/images/CLIkdlESk3A4juSB4UxeAIyG4feOLr2OtRVs)

Deux personnes essaient de se présenter. Cependant, elles ne vont pas essayer de parler en même temps. Supposons que Raj commence. John attendra alors que Raj ait fini de se présenter avant de commencer à se présenter lui-même. Cela est basé sur quelques heuristiques apprises, mais nous pouvons généralement décrire ce qui précède comme un protocole.

Nos clients et serveurs ont besoin d'un protocole similaire. Sinon, comment sauraient-ils quand c'est leur tour d'envoyer des paquets de données ?

Nous allons faire quelque chose de simple pour illustrer cela. Supposons que nous voulons envoyer des données qui se trouvent être un tableau de chaînes. Supposons que le tableau est le suivant :

`arr = ['random', 'strings', 'that', 'need', 'to', 'be', 'transferred', 'across', 'the', 'network', 'using', 'sockets']`

Ce qui précède est les données qui vont être écrites du client au serveur. Créons une autre contrainte. Le serveur doit accepter des données qui sont exactement équivalentes aux données occupées par la chaîne qui va être envoyée à cet instant.

Donc, par exemple, si le client va envoyer la chaîne 'random', et supposons que chaque caractère occupe 1 octet, alors la chaîne elle-même occupe 6 octets. 6 octets est alors égal à 6*8 = 48 bits. Par conséquent, pour que la chaîne 'random' soit transférée via des sockets du client au serveur, le serveur doit savoir qu'il doit accéder à 48 bits pour ce paquet de données spécifique.

C'est une bonne opportunité de décomposer le problème. Il y a quelques choses que nous devons d'abord comprendre.

#### **Comment déterminer le nombre d'octets qu'une chaîne occupe en Python ?**

Eh bien, nous pourrions commencer par déterminer la longueur d'une chaîne d'abord. C'est facile, il suffit d'appeler `len()`. Mais nous devons encore connaître le nombre d'octets occupés par une chaîne, pas seulement la longueur.

Nous allons d'abord convertir la chaîne en binaire, puis trouver la longueur de la représentation binaire résultante. Cela devrait nous donner le nombre d'octets utilisés.

`len('random'.encode('utf-8'))` nous donnera ce que nous voulons

#### **Comment envoyer le nombre d'octets occupés par chaque chaîne au serveur ?**

Facile, nous allons convertir le nombre d'octets (qui est un entier) en une représentation binaire de ce nombre, et l'envoyer au serveur. Maintenant, le serveur peut s'attendre à recevoir la longueur d'une chaîne avant de recevoir la chaîne elle-même.

#### **Comment le serveur sait-il quand le client a fini d'envoyer toutes les chaînes ?**

Rappelez-vous de l'analogie de la conversation, il doit y avoir un moyen de savoir si le transfert de données est terminé. Les ordinateurs n'ont pas leurs propres heuristiques sur lesquelles ils peuvent compter. Donc, nous allons fournir une règle aléatoire. Nous allons dire que lorsque nous envoyons la chaîne 'end', cela signifie que le serveur a reçu toutes les chaînes et peut maintenant fermer la connexion. Bien sûr, cela signifie que nous ne pouvons pas utiliser la chaîne 'end' dans aucune autre partie de notre tableau sauf à la toute fin.

Voici le protocole que nous avons conçu jusqu'à présent :

![Image](https://cdn-media-1.freecodecamp.org/images/4yfQKmY11KjLAwC3nxcq9lE2s-LF7fXEs9CS)
_Notre protocole simpliste_

La longueur de la chaîne sera de 2 octets, suivie de la chaîne elle-même qui sera de longueur variable. Cela dépendra de la longueur de la chaîne envoyée dans le paquet précédent, et nous alternerons entre l'envoi des longueurs de chaîne et de la chaîne elle-même. EOT signifie End Of Transmission, et l'envoi de la chaîne 'end' signifie qu'il n'y a plus de données à envoyer.

> Note : Avant de continuer, je veux souligner quelque chose. C'est un protocole très simple et stupide. Si vous voulez voir à quoi ressemble un protocole bien conçu, ne cherchez pas plus loin que le [protocole HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview).

Codons cela. J'ai inclus des commentaires dans le code ci-dessous pour qu'il soit auto-explicatif.

Super, nous avons un client en cours d'exécution. Ensuite, nous avons besoin du serveur.

Je veux expliquer quelques lignes de code spécifiques dans les gists ci-dessus. La première, du fichier `clientSocket.py`.

`len_in_bytes = (len_of_string).to_bytes(2, byteorder='little')`

Ce que fait le code ci-dessus est de convertir un nombre en octets. Le premier paramètre passé à la fonction to_bytes est le nombre d'octets alloués au résultat de la conversion de `len_of_string` en sa représentation binaire.

Le deuxième paramètre est utilisé pour décider si l'on suit le format Little Endian ou le format Big Endian. Vous pouvez en lire plus à ce sujet [ici](https://en.wikipedia.org/wiki/Endianness). Pour l'instant, sachez simplement que nous allons toujours utiliser 'little' pour ce paramètre.

La ligne de code suivante que je veux examiner est :

`client_socket.send(string.encode('utf-8'))`

Nous convertissons la chaîne en un format binaire en utilisant l'encodage 'utf-8'.

Ensuite, dans le fichier `serverSocket.py` :

```
data = client_socket.recv(2)
str_length = int.from_bytes(data, byteorder='little')
```

La première ligne de code ci-dessus reçoit 2 octets de données du client. Rappelez-vous que lorsque nous avons converti la longueur de la chaîne en un format binaire dans `clientSocket.py`, nous avons décidé de stocker le résultat en 2 octets. C'est pourquoi nous lisons 2 octets ici pour ces mêmes données.

La ligne suivante consiste à convertir le format binaire en un entier. Le `byteorder` ici est 'little', pour correspondre au `byteorder` que nous avons utilisé sur le client.

Si vous allez de l'avant et exécutez les deux sockets, vous devriez voir que le serveur imprimera les chaînes que le client envoie. Nous avons établi la communication !

#### Conclusion

D'accord, nous avons couvert beaucoup de choses jusqu'à présent. Notamment, ce que sont les sockets, comment nous les utilisons et comment concevoir un protocole très simple et stupide. Si vous voulez en savoir plus sur le fonctionnement des sockets, je vous recommande vivement de lire [Le guide de Beej sur la programmation réseau](https://beej.us/guide/bgnet/html/multi/index.html). Cet e-book contient beaucoup de choses intéressantes.

Vous pouvez bien sûr prendre ce que vous avez lu dans cet article jusqu'à présent, et l'appliquer à des problèmes plus complexes comme le streaming d'images depuis une caméra RaspberryPi vers votre ordinateur. Amusez-vous bien !

_Si vous le souhaitez, vous pouvez me suivre sur [Twitter](https://twitter.com/zz_humayun) ou [GitHub](https://github.com/redixhumayun). Vous pouvez également consulter mon blog [ici](https://redixhumayun.github.io). Je suis toujours disponible si vous souhaitez me contacter !_

_Publié à l'origine sur [https://redixhumayun.github.io/networking/2019/02/14/how-the-internet-speaks.html](https://redixhumayun.github.io/networking/2019/02/14/how-the-internet-speaks.html) le 14 février 2019._
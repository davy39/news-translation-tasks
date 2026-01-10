---
title: Qu'est-ce que Nmap et comment l'utiliser – Un tutoriel pour le plus grand outil
  de scan de tous les temps
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-10-02T14:02:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-nmap-and-how-to-use-it-a-tutorial-for-the-greatest-scanning-tool-of-all-time
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/wall-6.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: penetration testing
  slug: penetration-testing
seo_title: Qu'est-ce que Nmap et comment l'utiliser – Un tutoriel pour le plus grand
  outil de scan de tous les temps
seo_desc: 'Nmap is the most famous scanning tool used by penetration testers. In this
  article, we will look at some core features of Nmap along with a few useful commands.

  What is Nmap?

  Nmap is short for Network Mapper. It is an open-source Linux command-line t...'
---

Nmap est l'outil de scan le plus célèbre utilisé par les testeurs d'intrusion. Dans cet article, nous allons examiner certaines fonctionnalités principales de Nmap ainsi que quelques commandes utiles.

## Qu'est-ce que Nmap ?

Nmap est l'abréviation de Network Mapper. C'est un outil open-source en ligne de commande Linux utilisé pour scanner les adresses IP et les ports d'un réseau et pour détecter les applications installées.

Nmap permet aux administrateurs réseau de trouver quels appareils fonctionnent sur leur réseau, de découvrir les ports et services ouverts, et de détecter les vulnérabilités.

[Gordon Lyon (pseudonyme Fyodor)](https://en.wikipedia.org/wiki/Gordon_Lyon) a écrit Nmap comme un outil pour aider à mapper facilement un réseau entier et à trouver ses ports et services ouverts.

Nmap est devenu extrêmement populaire, étant présenté dans des films comme The Matrix et la série populaire Mr. Robot.

## Pourquoi utiliser Nmap ?

Il y a plusieurs raisons pour lesquelles les professionnels de la sécurité préfèrent Nmap aux autres outils de scan.

Tout d'abord, Nmap vous aide à mapper rapidement un réseau sans commandes ou configurations sophistiquées. Il supporte également des commandes simples (par exemple, pour vérifier si un hôte est actif) et un scripting complexe via le moteur de scripting Nmap.

D'autres fonctionnalités de Nmap incluent :

* Capacité à reconnaître rapidement tous les appareils, y compris les serveurs, routeurs, commutateurs, appareils mobiles, etc., sur un ou plusieurs réseaux.

* Aide à identifier les services en cours d'exécution sur un système, y compris les serveurs web, les serveurs DNS et d'autres applications courantes. Nmap peut également détecter les versions des applications avec une précision raisonnable pour aider à détecter les vulnérabilités existantes.

* Nmap peut trouver des informations sur le système d'exploitation en cours d'exécution sur les appareils. Il peut fournir des informations détaillées comme les versions du système d'exploitation, ce qui facilite la planification d'approches supplémentaires lors des tests d'intrusion.

* Lors de l'audit de sécurité et du scan de vulnérabilités, vous pouvez utiliser Nmap pour attaquer des systèmes en utilisant des scripts existants du moteur de scripting Nmap.

* Nmap dispose d'une interface utilisateur graphique appelée Zenmap. Elle vous aide à développer des mappages visuels d'un réseau pour une meilleure utilité et des rapports.

## Commandes

Examinons quelques commandes Nmap. Si vous n'avez pas Nmap installé, vous pouvez [l'obtenir ici](https://nmap.org/download.html).

### Scans de base

Scanner la liste des appareils actifs sur un réseau est la première étape du mappage réseau. Il existe deux types de scans que vous pouvez utiliser pour cela :

* **Scan Ping —** Scanne la liste des appareils actifs et en cours d'exécution sur un sous-réseau donné.

```typescript
> nmap -sP 192.168.1.1/24
```

* **Scanner un seul hôte —** Scanne un seul hôte pour 1000 ports bien connus. Ces ports sont ceux utilisés par des services populaires comme SQL, SNTP, apache, et autres.

```typescript
> nmap scanme.nmap.org
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-3.png align="left")

### Scan furtif

Le scan furtif est effectué en envoyant un paquet SYN et en analysant la réponse. Si SYN/ACK est reçu, cela signifie que le port est ouvert, et vous pouvez ouvrir une connexion TCP.

Cependant, un scan furtif ne complète jamais le [3-way handshake](https://www.geeksforgeeks.org/tcp-3-way-handshake-process/), ce qui rend difficile pour la cible de déterminer le système de scan.

```typescript
> nmap -sS scanme.nmap.org
```

Vous pouvez utiliser la commande **'-sS'** pour effectuer un scan furtif. Rappelez-vous, le scan furtif est plus lent et moins agressif que les autres types de scan, donc vous devrez peut-être attendre un certain temps pour obtenir une réponse.

### Scan de version

Trouver les versions des applications est une partie cruciale des tests d'intrusion.

Cela facilite votre travail puisque vous pouvez trouver une vulnérabilité existante dans la base de données [Common Vulnerabilities and Exploits (CVE)](https://cve.mitre.org/) pour une version particulière du service. Vous pouvez ensuite l'utiliser pour attaquer une machine en utilisant un outil d'exploitation comme [Metasploit](https://en.wikipedia.org/wiki/Metasploit_Project).

```typescript
> nmap -sV scanme.nmap.org
```

Pour effectuer un scan de version, utilisez la commande '-sV'. Nmap fournira une liste de services avec leurs versions. Gardez à l'esprit que les scans de version ne sont pas toujours 100% précis, mais cela vous rapproche d'un pas de la réussite de l'intrusion dans un système.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-5.png align="left")

### Scan du système d'exploitation

En plus des services et de leurs versions, Nmap peut fournir des informations sur le système d'exploitation sous-jacent en utilisant l'empreinte TCP/IP. Nmap essaiera également de trouver le temps de fonctionnement du système lors d'un scan du système d'exploitation.

```typescript
> nmap -sV scanme.nmap.org
```

Vous pouvez utiliser des flags supplémentaires comme osscan-limit pour limiter la recherche à quelques cibles attendues. Nmap affichera le pourcentage de confiance pour chaque supposition du système d'exploitation.

Encore une fois, la détection du système d'exploitation n'est pas toujours précise, mais elle aide grandement un testeur d'intrusion à se rapprocher de sa cible.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-6.png align="left")

### Scan agressif

Nmap dispose d'un mode agressif qui active la détection du système d'exploitation, la détection de version, le scan de script et le traceroute. Vous pouvez utiliser l'argument -A pour effectuer un scan agressif.

```typescript
> nmap -A scanme.nmap.org
```

Les scans agressifs fournissent des informations bien meilleures que les scans réguliers. Cependant, un scan agressif envoie également plus de sondes, et il est plus susceptible d'être détecté lors des audits de sécurité.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-7.png align="left")

### Scan de plusieurs hôtes

Nmap a la capacité de scanner plusieurs hôtes simultanément. Cette fonctionnalité est très pratique lorsque vous gérez une vaste infrastructure réseau.

Vous pouvez scanner plusieurs hôtes par différentes approches :

* Écrivez toutes les adresses IP dans une seule ligne pour scanner tous les hôtes en même temps.

```typescript
> nmap 192.164.1.1 192.164.0.2 192.164.0.2
```

* Utilisez l'astérisque (*) pour scanner tous les sous-réseaux à la fois.

```typescript
> nmap 192.164.1.*
```

* Ajoutez des virgules pour séparer les terminaisons des adresses au lieu de taper les domaines entiers.

```typescript
> nmap 192.164.0.1,2,3,4
```

* Utilisez un trait d'union pour spécifier une plage d'adresses IP

```typescript
> nmap 192.164.0.0-255
```

### Scan de ports

Le scan de ports est l'une des fonctionnalités les plus fondamentales de Nmap. Vous pouvez scanner les ports de plusieurs manières.

* Utilisation du paramètre -p pour scanner un seul port

```typescript
> nmap -p 973 192.164.0.1
```

* Si vous spécifiez le type de port, vous pouvez scanner des informations sur un type particulier de connexion, par exemple pour une connexion TCP.

```typescript
> nmap -p T:7777, 973 192.164.0.1
```

* Une plage de ports peut être scannée en les séparant par un trait d'union.

```typescript
> nmap -p 76-973 192.164.0.1
```

* Vous pouvez également utiliser le flag **--top-ports** pour spécifier les n ports principaux à scanner.

```typescript
> nmap --top-ports 10 scanme.nmap.org
```

### Scan à partir d'un fichier

Si vous souhaitez scanner une grande liste d'adresses IP, vous pouvez le faire en important un fichier avec la liste des adresses IP.

```typescript
> nmap -iL /input_ips.txt
```

La commande ci-dessus produira les résultats de scan de tous les domaines donnés dans le fichier "input_ips.txt". En plus de simplement scanner les adresses IP, vous pouvez également utiliser des options et des flags supplémentaires.

### Verbosité et exportation des résultats de scan

Les tests d'intrusion peuvent durer des jours, voire des semaines. Exporter les résultats de Nmap peut être utile pour éviter un travail redondant et pour aider à la création de rapports finaux. Examinons quelques façons d'exporter les résultats de scan Nmap.

#### Sortie verbeuse

```typescript
> nmap -v scanme.nmap.org
```

La sortie verbeuse fournit des informations supplémentaires sur le scan en cours d'exécution. Elle est utile pour surveiller les actions étape par étape que Nmap effectue sur un réseau, surtout si vous êtes un outsider scannant le réseau d'un client.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-8.png align="left")

#### Sortie normale

Les scans Nmap peuvent également être exportés vers un fichier texte. Il sera légèrement différent de la sortie originale de la ligne de commande, mais il capturera tous les résultats de scan essentiels.

```typescript
> nmap -oN output.txt scanme.nmap.org
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-9.png align="left")

#### Sortie XML

Les scans Nmap peuvent également être exportés vers XML. C'est également le format de fichier préféré de la plupart des outils de test d'intrusion, ce qui le rend facilement analysable lors de l'importation des résultats de scan.

```typescript
> nmap -oX output.xml scanme.nmap.org
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-10.png align="left")

#### Formats multiples

Vous pouvez également exporter les résultats de scan dans tous les formats disponibles à la fois en utilisant la commande -oA.

```typescript
> nmap -oA output scanme.nmap.org
```

La commande ci-dessus exportera le résultat de scan dans trois fichiers — output.xml, output.nmap et output.gnmap.

### Aide Nmap

Nmap dispose d'une commande d'aide intégrée qui liste tous les flags et options que vous pouvez utiliser. Elle est souvent pratique étant donné le nombre d'arguments de ligne de commande que Nmap propose.

```typescript
> nmap -h
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-12.png align="left")

## Moteur de scripting Nmap

Le moteur de scripting Nmap (NSE) est un outil incroyablement puissant que vous pouvez utiliser pour écrire des scripts et automatiser de nombreuses fonctionnalités réseau.

Vous pouvez trouver de nombreux scripts distribués dans Nmap, ou écrire votre propre script en fonction de vos besoins. Vous pouvez même modifier des scripts existants en utilisant le [langage de programmation Lua](https://en.wikipedia.org/wiki/Lua_(programming_language)).

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-13.png align="left")

NSE dispose également de scripts d'attaque utilisés pour attaquer le réseau et divers protocoles réseau.

Passer en revue le moteur de scripting en profondeur serait hors de portée pour cet article, donc [voici plus d'informations sur le moteur de scripting Nmap](https://nmap.org/book/nse.html).

### Zenmap

Zenmap est une interface utilisateur graphique pour Nmap. C'est un logiciel gratuit et open-source qui vous aide à démarrer avec Nmap.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-15.png align="left")

En plus de fournir des mappages réseau visuels, Zenmap vous permet également de sauvegarder et de rechercher vos scans pour une utilisation future.

Zenmap est idéal pour les débutants qui veulent tester les capacités de Nmap sans passer par une interface en ligne de commande.

## Conclusion

Nmap est clairement le "couteau suisse" du réseau, grâce à son inventaire de commandes polyvalentes.

Il vous permet de scanner rapidement et de découvrir des informations essentielles sur votre réseau, hôtes, ports, pare-feux et systèmes d'exploitation.

Nmap dispose de nombreux paramètres, flags et préférences qui aident les administrateurs système à analyser un réseau en détail.

Si vous souhaitez apprendre Nmap en profondeur, [voici une excellente ressource pour vous](https://github.com/jasonniebauer/Nmap-Cheatsheet).

*Aimé cet article ?* [***Rejoignez ma Newsletter***](http://tinyletter.com/manishmshiva) *et obtenez un résumé de mes articles et vidéos chaque lundi.*
---
title: Réseaux informatiques — Explication de Traceroute
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/computer-networking-traceroute-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d32740569d1a4ca366d.jpg
tags:
- name: computer networking
  slug: computer-networking
- name: toothbrush
  slug: toothbrush
seo_title: Réseaux informatiques — Explication de Traceroute
seo_desc: 'According to Wikipedia, traceroute is:


  a computer network diagnostic tool for displaying the route (path) and measuring
  transit delays of packets across an Internet Protocol (IP) network. The history
  of the route is recorded as the round-trip times ...'
---

Selon Wikipedia, `traceroute` est :

> un outil de diagnostic de réseau informatique permettant d'afficher le chemin (route) et de mesurer les délais de transit des paquets à travers un réseau Internet Protocol (IP). L'historique du chemin est enregistré sous forme de temps aller-retour des paquets reçus de chaque hôte successif (nœud distant) dans le chemin (route) ; la somme des temps moyens à chaque saut est une mesure du temps total passé à établir la connexion. Traceroute continue à moins que tous les paquets envoyés (trois) ne soient perdus plus de deux fois, auquel cas la connexion est perdue et le chemin ne peut pas être évalué. Ping, en revanche, ne calcule que les temps aller-retour finaux à partir du point de destination.

`traceroute` peut être utilisé pour trouver la source la plus rapide pour télécharger des données, et est souvent utilisé par les testeurs d'intrusion pour recueillir des informations sur un réseau.

## Comment les données voyagent sur Internet

Chaque ordinateur dans le traceroute est identifié par son adresse IP, ou sa connexion réseau unique.

```text
- Le voyage d'un ordinateur à un autre est connu sous le nom de saut (hop).
- Le temps qu'il faut pour effectuer un saut est mesuré en millisecondes.
- Les informations qui voyagent le long du traceroute sont connues sous le nom de paquet.
```

Voici quelques détails importants sur un traceroute :

* Le chemin d'un ordinateur à un autre est appelé un saut (hop)
* Les sauts sont mesurés en millisecondes
* Les informations qui voyagent le long du traceroute sont appelées un paquet

Si un traceroute ne peut pas accéder à un ordinateur, il affichera « Request timed out. » Chaque colonne de saut pour les ordinateurs qui n'ont pas pu être accessibles affichera un astérisque au lieu d'un compte de millisecondes.

## Utilisation

La plupart des implémentations de `traceroute` permettent à l'utilisateur de spécifier le nombre de requêtes à envoyer à chaque saut, le temps d'attente pour chaque réponse, le port à utiliser, et ainsi de suite.

Voici un exemple simple sur Linux :

```text
[root@example ~]#  traceroute -w 3 -q 1 -m 16 www.google.com
traceroute to www.google.com (216.58.200.36), 16 hops max, 60 byte packets
 1  192.168.4.2 (192.168.4.2)  0.136 ms
 2  *
 3  *
 4  *
 5  *
 6  *
 7  *
 8  *
 9  *
10  *
11  *
12  *
13  *
14  *
15  *
16  *
```

Dans l'exemple ci-dessus, les options sélectionnées sont d'attendre trois secondes (au lieu de cinq), d'envoyer une seule requête à chaque saut (au lieu de trois), de limiter le nombre maximum de sauts à 16 avant d'abandonner (au lieu de 30), avec www.google.com comme hôte final.

Cela peut aider à identifier les définitions incorrectes de tables de routage ou les pare-feu qui peuvent bloquer le trafic ICMP, ou le port UDP élevé dans le ping Unix, vers un site. Notez qu'un pare-feu peut autoriser les paquets ICMP mais ne pas autoriser les paquets d'autres protocoles.

## Calculateur de sous-réseau IP

Bien que cela ne soit pas strictement lié aux traceroutes, un calculateur de sous-réseau IP est un outil utile lors de l'exécution de diagnostics réseau.

Les calculateurs de sous-réseau IP aident à diviser les réseaux IP en sous-réseaux en calculant les adresses réseau appropriées, les masques de sous-réseau, les adresses de diffusion et les plages d'adresses IP des hôtes. Pour les réseaux simples (comme un LAN domestique), il peut être très facile d'identifier les valeurs appropriées, mais pour un sous-réseautage plus complexe, un calculateur de sous-réseau IP est un excellent outil.

Voici quelques calculateurs de sous-réseau IP en ligne :

* [https://www.calculator.net/ip-subnet-calculator.html](https://www.calculator.net/ip-subnet-calculator.html)
* [https://www.subnetonline.com/pages/subnet-calculators/ip-subnet-calculator.php](https://www.subnetonline.com/pages/subnet-calculators/ip-subnet-calculator.php)
* [https://www.tunnelsup.com/subnet-calculator/](https://www.tunnelsup.com/subnet-calculator/)
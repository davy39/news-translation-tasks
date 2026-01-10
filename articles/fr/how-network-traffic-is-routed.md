---
title: Comment le trafic réseau est acheminé
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-04-19T22:23:29.000Z'
originalURL: https://freecodecamp.org/news/how-network-traffic-is-routed
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-barry-tan-7994953.jpg
tags:
- name: computer networking
  slug: computer-networking
seo_title: Comment le trafic réseau est acheminé
seo_desc: "Moving around the internet – or even over a private local network – requires\
  \ all kinds of magic wand waving and sorcery. \nOr, in sightly more accurate terms,\
  \ it requires the combination of sophisticated engineering and the existence of\
  \ key standards,..."
---

Se déplacer sur Internet – ou même sur un réseau local privé – nécessite toutes sortes de magie et de sorcellerie. 

Ou, en termes légèrement plus précis, cela nécessite la combinaison de l'ingénierie sophistiquée et l'existence de normes clés, y compris les ports réseau, le système de noms de domaine (DNS) et les politiques de routage. Et nous allons apprendre comment une partie de cela fonctionne dans cet article.

En plus des adresses IP (identifiants qui pourraient ressembler à quelque chose comme `192.168.2.54` ou `e80::1164:3e06:6716:7a0b/64`), le trafic réseau peut être acheminé entre des appareils ou même des services individuels exécutés sur un appareil en utilisant les ports TCP et UDP. 

Cet article provient de [The Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). Vous pouvez également suivre avec cette vidéo :

%[https://www.youtube.com/watch?v=GaTTrXcO13I&list=PLSiZCpRYoTZ7wEwmKRsRjaQF3qSi4bbdl&index=3]

## Acheminement du trafic réseau à l'aide des ports réseau

Les ports sont des numéros utilisés pour identifier des applications ou des services spécifiques exécutés sur un appareil. Lorsque des données sont transmises sur le réseau, les ports source et de destination sont inclus dans le paquet de données pour garantir que les données sont envoyées à l'application ou au service correct.

[Il existe 65 535 ports TCP et UDP au total](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers), chacun pouvant être attribué à une application ou un service spécifique pour la communication sur Internet. 

Les 1024 premiers ports sont réservés pour les services bien connus et sont généralement attribués à des applications ou des services spécifiques par l'Internet Assigned Numbers Authority. Par exemple, HTTP (Hypertext Transfer Protocol) utilise le port 80, tandis que HTTPS (HTTP Secure) utilise le port 443.

Les ports restants (au-dessus de 1024) sont appelés ports éphémères et peuvent être utilisés par toute application ou service ayant besoin de communiquer sur Internet. Lorsqu'un appareil initie une connexion, il sélectionne un port éphémère disponible à utiliser pour la durée de la connexion.

Les appareils peuvent également être identifiés par des adresses de contrôle d'accès au support (MAC) uniques. Les adresses MAC – attribuées à la couche de liaison du modèle OSI – sont utilisées pour identifier les appareils sur un segment de réseau local et pour fournir un moyen de transmettre les données directement à l'appareil correct. Voici une adresse MAC typique :

```
40:b0:72:d4:29:ab
```

## Qu'est-ce que le système de noms de domaine (DNS) ?

Le système de noms de domaine est un système utilisé pour traduire les noms de domaine lisibles par l'homme en adresses IP. Cela permet aux utilisateurs d'accéder aux sites web et à d'autres ressources Internet en utilisant des noms de domaine faciles à retenir au lieu des adresses IP. 

Le DNS fournit également d'autres fonctions importantes, telles que la mise en correspondance des adresses IP avec plusieurs noms de domaine et l'orientation du trafic vers le serveur correct en fonction de l'emplacement de l'utilisateur.

Le DNS direct fait référence au processus de conversion d'un nom de domaine, tel que "www.example.com", en une adresse IP, telle que "192.0.2.1". Le DNS direct est utilisé par les clients pour résoudre les noms de domaine en adresses IP, afin qu'ils puissent accéder aux sites web, aux serveurs de messagerie et à d'autres services réseau.

Le DNS inverse, en revanche, est le processus de conversion d'une adresse IP en un nom de domaine. Le DNS inverse est utilisé pour identifier le nom de domaine associé à une adresse IP particulière. 

Ces informations peuvent être utilisées à des fins de sécurité, telles que l'identification de la source d'une connexion réseau entrante, ou pour tracer l'origine du spam ou du trafic malveillant.

Les serveurs DNS publics sont exploités par des organisations telles que Google, Cloudflare et OpenDNS, et sont disponibles pour une utilisation par quiconque sur Internet. Les serveurs DNS publics sont souvent utilisés comme alternative aux serveurs DNS fournis par les fournisseurs de services Internet, car ils peuvent offrir des temps de résolution plus rapides, de meilleures fonctionnalités de sécurité et une confidentialité accrue.

## Dispositifs de routage matériel

D'un point de vue matériel, le routage du trafic est géré par une famille de dispositifs de mise en réseau faiblement liés. Il convient de noter qu'un seul dispositif peut parfois inclure des fonctionnalités normalement identifiées avec plus d'une catégorie. 

* Les commutateurs permettent à plusieurs dispositifs sur un réseau de communiquer entre eux en transmettant des paquets de données au destinataire prévu. 
* Les routeurs connectent plusieurs réseaux ensemble et transmettent des paquets de données entre eux. Les routeurs utilisent des tables de routage pour déterminer le meilleur chemin pour les données. 
* Les points d'accès permettent aux dispositifs sans fil de se connecter à un réseau filaire. Ils agissent comme un pont entre les dispositifs sans fil et le routeur réseau.

Il est utile de garder à l'esprit qu'un "routeur par défaut" est l'adresse IP de la passerelle utilisée par les dispositifs sur un réseau pour communiquer avec des dispositifs sur un réseau différent. Le routeur par défaut est généralement l'adresse IP du routeur réseau.

## Conclusion

Comprendre les outils logiciels et matériels utilisés pour connecter tous nos nombreux dispositifs à travers les réseaux numériques peut vous aider à résoudre les problèmes lorsque les choses tournent mal. Mais c'est aussi un composant critique pour comprendre les problèmes – et les solutions – impliqués dans la sécurité réseau.

Cet article et la vidéo qui l'accompagne sont extraits de [mon cours Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). Et il y a beaucoup plus de technologie disponible sur [bootstrap-it.com](https://bootstrap-it.com/).
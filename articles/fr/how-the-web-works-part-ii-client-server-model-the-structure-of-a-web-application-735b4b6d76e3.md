---
title: 'Comment fonctionne le Web Partie II : Modèle Client-Serveur et Structure d''une
  Application Web'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-17T16:12:36.000Z'
originalURL: https://freecodecamp.org/news/how-the-web-works-part-ii-client-server-model-the-structure-of-a-web-application-735b4b6d76e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*npIBV1f2RsVFRf5rfMarzw.jpeg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Comment fonctionne le Web Partie II : Modèle Client-Serveur et Structure
  d''une Application Web'
seo_desc: 'By Preethi Kasireddy

  In my previous post, we dived into how the web works on a basic level, including
  the interaction between a client (your computer) and a server (another computer
  which responds to the client’s requests for websites).

  For this post...'
---

Par Preethi Kasireddy

Dans mon [précédent article](https://medium.freecodecamp.com/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c#.8nc8nkx2u), nous avons exploré comment le web fonctionne à un niveau basique, y compris l'interaction entre un client (votre ordinateur) et un serveur (un autre ordinateur qui répond aux demandes du client pour des sites web).

Pour cet article — deuxième partie d'une série en quatre parties — approfondissons la compréhension de la manière dont le client, le serveur et d'autres parties d'une application web basique sont configurés pour rendre possible votre expérience de navigation sur le web.

### Le Modèle Client-Serveur

Cette idée d'un client et d'un serveur communiquant sur un réseau est appelée le modèle « Client-Serveur ». C'est ce qui rend possible la consultation de sites web (comme celui-ci) et l'interaction avec des applications web (comme Gmail).

Le modèle Client-Serveur est vraiment juste une façon de décrire la relation de donneur-receveur entre le client et le serveur dans une application web — tout comme vous pourriez utiliser « petit ami » et « petite amie » pour décrire vos relations personnelles. Ce sont les détails de la manière dont l'information passe d'une extrémité à l'autre qui compliquent le tableau.

### Une Configuration Basique d'une Application Web

Il existe des centaines de façons de configurer une application web. Cela dit, la plupart d'entre elles suivent la même structure de base : un client, un serveur et une base de données.

#### Le client

Le client est ce avec quoi l'utilisateur interagit. Ainsi, le code « côté client » est responsable de la plupart de ce qu'un utilisateur voit réellement. Cela inclut :

1. Définir la **structure** de la page web
2. Définir l'**apparence** de la page web
3. Implémenter un mécanisme pour répondre aux **interactions de l'utilisateur** (cliquer sur des boutons, entrer du texte, etc.)

**Structure :** La mise en page et le contenu de votre page web sont définis par HTML (généralement HTML 5 de nos jours en ce qui concerne les applications web, mais c'est une autre histoire.)

HTML signifie Hyper Text Markup Language. Il vous permet de décrire la structure physique de base d'un document en utilisant des balises HTML. Chaque balise HTML décrit un élément spécifique du document.

Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/0*8mHEps7DYdFRX9yt.png)

* Le contenu dans la balise « <h1> » décrit l'en-tête.
* Le contenu dans la balise « <p> » décrit un paragraphe.
* Le contenu dans la balise « <button> » décrit un bouton.
* Et ainsi de suite...

Un navigateur web utilise ces balises HTML pour déterminer comment afficher le document.

**Apparence :** Pour définir l'apparence d'une page web, les développeurs web utilisent CSS, qui signifie Cascading Style Sheets. CSS est un langage qui vous permet de décrire comment les éléments définis dans votre HTML doivent être stylisés, permettant des changements de police, de couleur, de mise en page, d'animations simples et d'autres éléments superficiels.

Vous pourriez définir des styles pour la page HTML ci-dessus comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*xz1UefWofgjVccqn.png)

**Interactions de l'utilisateur :** Enfin, JavaScript entre en jeu pour gérer les interactions de l'utilisateur.

Par exemple, si vous voulez faire quelque chose lorsque l'utilisateur clique sur votre bouton, vous pourriez faire quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*SZQXE3sbBT1H9GNE.png)

Certaines interactions de l'utilisateur, comme celle ci-dessus, peuvent être gérées sans jamais avoir à atteindre votre serveur — d'où le terme « JavaScript côté client ». D'autres interactions nécessitent que vous envoyiez les demandes à votre serveur pour les traiter.

Par exemple, si un utilisateur publie un commentaire sur un fil de discussion, vous pourriez vouloir stocker ce commentaire dans votre base de données pour garder toute la discussion organisée en un seul endroit. Ainsi, vous enverriez la demande au serveur avec le nouveau commentaire et l'ID de l'utilisateur, et le serveur écouterait ces demandes et les traiterait en conséquence.

Nous approfondirons beaucoup plus le sujet des requêtes-réponses HTTP dans la prochaine partie de cette série.

#### Le serveur

Le serveur dans une application web est ce qui écoute les demandes provenant du client. Lorsque vous configurez un serveur HTTP, vous le configurez pour qu'il écoute un numéro de port. Un numéro de port est toujours associé à l'adresse IP d'un ordinateur.

Vous pouvez penser aux ports comme à des canaux séparés sur chaque ordinateur que vous pouvez utiliser pour effectuer différentes tâches : un port pourrait surfer sur [www.facebook.com](http://www.facebook.com) tandis qu'un autre récupère vos emails. Cela est possible parce que chacune des applications (le navigateur web et le client de messagerie) utilise des numéros de port différents.

Une fois que vous avez configuré un serveur HTTP pour qu'il écoute un port spécifique, le serveur attend les demandes des clients arrivant à ce port spécifique, effectue les actions indiquées par la demande et envoie les données demandées via une réponse HTTP.

#### La base de données

Les bases de données sont les fondations de l'architecture web — la plupart d'entre nous ont peur d'y descendre, mais elles sont essentielles pour une fondation solide. Une base de données est un endroit pour stocker des informations afin qu'elles puissent être facilement accessibles, gérées et mises à jour.

Si vous construisez un site de médias sociaux, par exemple, vous pourriez utiliser une base de données pour stocker des informations sur vos utilisateurs, vos publications et vos commentaires. Lorsqu'un visiteur demande une page, les données insérées dans la page proviennent de la base de données du site, permettant les interactions utilisateur en temps réel que nous tenons pour acquises sur des sites comme Facebook ou des applications comme Gmail.

#### C'est tout, les amis ! (Enfin, presque...)

C'est aussi simple que cela. Nous venons de parcourir toute la fonctionnalité de base d'une application web.

![Image](https://cdn-media-1.freecodecamp.org/images/0*so2yzFu1-Zr_cT-o.png)

### Comment Scaler une Application Web Simple

La configuration ci-dessus est idéale pour des applications simples. Mais à mesure qu'une application grandit, un seul serveur n'aura pas la puissance de gérer des milliers — voire des millions — de demandes simultanées de visiteurs.

Pour scaler afin de répondre à ces volumes élevés, une chose que nous pouvons faire est de distribuer le trafic entrant à travers un groupe de serveurs back-end.

C'est là que les choses deviennent intéressantes. Vous avez plusieurs serveurs, chacun avec sa propre adresse IP. Alors, comment le serveur de noms de domaine (DNS) sait-il quelle instance de votre application envoyer votre trafic ?

La réponse simple est qu'il ne le sait pas. La manière de gérer toutes ces instances séparées de votre application est à travers quelque chose appelé un équilibreur de charge.

L'équilibreur de charge agit comme un agent de circulation qui achemine les demandes des clients à travers les serveurs de la manière la plus rapide et la plus efficace possible.

Puisque vous ne pouvez pas diffuser les adresses IP de toutes vos instances de serveur, vous créez une adresse IP virtuelle, qui est l'adresse que vous diffusez publiquement aux clients. Cette adresse IP virtuelle pointe vers votre équilibreur de charge. Ainsi, lorsqu'il y a une recherche DNS pour votre site, elle pointera vers l'équilibreur de charge. Ensuite, l'équilibreur de charge intervient pour distribuer le trafic à vos divers serveurs back-end en temps réel.

Vous vous demandez peut-être comment l'équilibreur de charge sait quel serveur envoyer le trafic. La réponse : des algorithmes.

Un algorithme populaire, Round Robin, implique de distribuer uniformément les demandes entrantes à travers votre ferme de serveurs (tous vos serveurs disponibles). Vous choisirez généralement cette approche si tous vos serveurs ont une vitesse de traitement et une mémoire similaires.

Avec un autre algorithme, Least Connections, la prochaine demande est envoyée au serveur avec le moins de connexions actives.

Il existe de nombreux autres algorithmes que vous pouvez implémenter, selon vos besoins.

Ainsi, le flux ressemble maintenant à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*zFuBGTUicpKAES3J.png)

### Services

D'accord, nous avons donc résolu notre problème de trafic en créant des pools de serveurs et un équilibreur de charge pour les gérer. Ça marche super bien, non ?

...Mais simplement répliquer un tas de serveurs pourrait encore entraîner des problèmes à mesure que votre application grandit. À mesure que vous ajoutez plus de fonctionnalités à votre application, vous devriez continuer à maintenir le même serveur monolithique tout en continuant à grandir. Pour résoudre cela, nous avons besoin d'une manière de découpler la fonctionnalité du serveur.

C'est là qu'intervient l'idée d'un service. Un service est juste un autre serveur, sauf qu'il n'interagit qu'avec d'autres serveurs, contrairement à un serveur web traditionnel qui interagit avec des clients.

Chaque service a une unité autonome de fonctionnalité, telle que l'autorisation des utilisateurs ou la fourniture d'une fonctionnalité de recherche. Les services vous permettent de diviser votre serveur web unique en plusieurs services qui effectuent chacun une fonctionnalité discrète.

Le principal avantage de diviser un serveur unique en de nombreux services est qu'il vous permet de scaler les services complètement indépendamment.

L'autre avantage ici est qu'il permet aux équipes au sein d'une entreprise de travailler indépendamment sur un service particulier, plutôt que d'avoir des dizaines, des centaines ou même des milliers d'ingénieurs travaillant sur un seul serveur monolithique, ce qui devient rapidement un cauchemar de gestion de projet.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dyF3OkNQ_1tiV6tm.png)

Note rapide ici : ce concept d'équilibreurs de charge et de pools de serveurs back-end et de services devient très difficile à mesure que vous scalez pour ajouter de plus en plus de serveurs à votre application. Cela devient particulièrement délicat avec des choses comme la persistance de session — comme comment gérer l'envoi de plusieurs demandes d'un client au même serveur pour la durée d'une session — et comment déployer votre solution d'équilibrage de charge. Nous laisserons ces sujets avancés de côté pour cet article.

### Réseaux de Diffusion de Contenu

Tout ce qui précède fonctionne bien pour scaler le trafic, mais votre application est toujours centralisée en un seul endroit. Lorsque vos utilisateurs commencent à visiter votre site depuis d'autres côtés du pays — ou de l'autre côté du monde — ils pourraient rencontrer des temps de chargement plus longs en raison de la distance accrue entre le client et le serveur. Après tout, nous parlons du « World Wide Web » — pas du « web de quartier local ». :)

![Image](https://cdn-media-1.freecodecamp.org/images/0*mkpavClCBpv22_zd.png)

Une tactique populaire pour résoudre cela est l'utilisation d'un Réseau de Diffusion de Contenu (CDN). Un CDN est un grand système distribué de serveurs « proxy » déployés à travers de nombreux centres de données. Un serveur proxy est simplement un serveur qui agit comme un intermédiaire entre un client et un serveur.

Les entreprises avec de grandes quantités de trafic distribué peuvent choisir de payer des entreprises de CDN pour livrer leur contenu à leurs utilisateurs finaux en utilisant les serveurs du CDN. Un exemple de CDN est Akamai. Akamai possède des milliers de serveurs situés dans des emplacements géographiques stratégiques autour du monde.

Comparons comment un site web fonctionne avec et sans un CDN.

Comme nous en avons parlé dans la Section 1, pour un site web typique, le nom de domaine d'une URL est traduit en l'adresse IP du serveur de l'hôte.

Cependant, si un client utilise Akamai, le nom de domaine de l'URL est traduit en l'adresse IP d'un serveur de périphérie appartenant à Akamai. Akamai livre ensuite le contenu web aux utilisateurs du client, sans qu'il ait jamais à toucher les serveurs du client.

Akamai est capable de faire cela en stockant des copies d'éléments fréquemment utilisés comme HTML, CSS, téléchargements de logiciels et objets multimédias des serveurs des clients.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZHM-aAjIYiqmCHWB.png)

L'objectif principal est de rapprocher le contenu de votre site web de votre utilisateur. Si le contenu n'a pas à parcourir autant de distance pour atteindre l'utilisateur, cela signifie une latence plus faible, ce qui réduit à son tour le temps de chargement.

Ta da ! Un site web plus rapide :)

### Répétez cela pour moi ?

Ensuite, lisez [la partie 3](https://medium.freecodecamp.com/how-the-web-works-part-iii-http-rest-e61bc50fa0a#.vbrmrnihn) où nous remplirons les détails avec un regard plus approfondi sur HTTP et REST ! :)
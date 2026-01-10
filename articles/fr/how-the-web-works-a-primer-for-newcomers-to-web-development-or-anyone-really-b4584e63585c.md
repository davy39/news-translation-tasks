---
title: 'Comment fonctionne le Web : Un guide pour les débutants en développement web
  (ou pour tout le monde, vraiment)'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-09T16:00:09.000Z'
originalURL: https://freecodecamp.org/news/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1XEF9NuNQy0rSu4kVdbb6A.jpeg
tags:
- name: Design
  slug: design
- name: education
  slug: education
- name: learning to code
  slug: learning-to-code
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Comment fonctionne le Web : Un guide pour les débutants en développement
  web (ou pour tout le monde, vraiment)'
seo_desc: 'By Preethi Kasireddy

  If you’re just getting into web development, chances are you think you know how
  the web works — at least on a basic level.

  …But then you try to explain how a basic website works and draw a blank. What does
  an IP address mean agai...'
---

Par Preethi Kasireddy

Si vous commencez tout juste en développement web, il est probable que vous pensiez savoir comment fonctionne le web — au moins à un niveau basique.

…Mais ensuite, vous essayez d'expliquer comment fonctionne un site web basique et vous êtes à court d'idées. Qu'est-ce qu'une adresse IP déjà ? Comment fonctionne exactement le modèle « client-serveur » ?

Les frameworks de développement sont puissants de nos jours. Tellement puissants, en fait, qu'il est facile pour nous, les débutants, de perdre de vue les bases de comment le web, vous savez, *fonctionne*.

Je sais que c'était mon cas. Pas de honte à l'admettre : le web est compliqué, et ce n'est que lorsque vous commencez à travailler sur le backend que vous réalisez à quel point ces fondamentaux sont importants. (Si vous voulez créer des applications web qui fonctionnent vraiment, en tout cas.)

J'ai donc pris sur moi d'écrire un guide en quatre parties sur les bases intimidantes que tout le monde devrait maîtriser, que vous débutiez une carrière en développement web ou que vous soyez simplement intéressé par l'apprentissage :

**Partie 1 :** Comment fonctionne le web

**Partie 2 :** Structure d'une application web

**Partie 3 :** HTTP et REST

**Partie 4 :** Exemples de code d'interactions client-serveur

### Une recherche web basique

Commençons par quelque chose que nous avons tous déjà fait : tapez « www.github.com » dans la barre d'adresse de votre navigateur et voyez la page se charger.

Aussi simple que cette transaction puisse paraître, il se passe une tonne de magie sous le capot. Plongeons-nous directement dedans.

### Définir les parties du web

Comprendre le web est intimidant parce qu'il y a beaucoup de jargon. Malheureusement, certains de ce jargon est crucial pour comprendre le reste de cet article.

Voici les termes les plus importants à comprendre si vous voulez saisir les secrets du World Wide Web :

**Client :** Une application, comme Chrome ou Firefox, qui s'exécute sur un ordinateur et est connectée à Internet. Son rôle principal est de prendre les interactions de l'utilisateur et de les traduire en requêtes vers un autre ordinateur appelé serveur web. Bien que nous utilisions généralement un navigateur pour accéder au web, vous pouvez considérer votre ordinateur entier comme la partie « Client » du modèle client-serveur. Chaque ordinateur client a une adresse unique appelée adresse IP que d'autres ordinateurs peuvent utiliser pour l'identifier.

**Serveur :** Une machine connectée à Internet qui a également une adresse IP. Un serveur attend les requêtes d'autres machines (par exemple, un client) et y répond. Contrairement à votre ordinateur (c'est-à-dire le client) qui a également une adresse IP, le serveur a un logiciel serveur spécial installé et en cours d'exécution qui lui indique comment répondre aux requêtes entrantes de votre navigateur. La fonction principale d'un serveur web est de stocker, traiter et livrer des pages web aux clients. Il existe de nombreux types de serveurs, notamment des serveurs web, des serveurs de base de données, des serveurs de fichiers, des serveurs d'applications, et plus encore. (Dans cet article, nous parlons des serveurs web.)

**Adresse IP :** Adresse de Protocole Internet. Un identifiant numérique pour un appareil (ordinateur, serveur, imprimante, routeur, etc.) sur un réseau TCP/IP. Chaque ordinateur sur Internet a une adresse IP qu'il utilise pour identifier et communiquer avec d'autres ordinateurs. Les adresses IP ont quatre ensembles de nombres séparés par des points décimaux (par exemple, 244.155.65.2). Cela s'appelle l'« adresse logique ». Afin de localiser un appareil dans le réseau, l'adresse IP logique est convertie en une adresse physique par le logiciel de protocole TCP/IP. Cette adresse physique (c'est-à-dire l'adresse MAC) est intégrée dans votre matériel.

**FAI :** Fournisseur d'Accès à Internet. Le FAI est l'intermédiaire entre le client et les serveurs. Pour le propriétaire typique d'une maison, le FAI est généralement une « compagnie de câble ». Lorsque votre navigateur reçoit une demande de vous pour aller sur [www.github.com,](http://www.github.com,) il ne sait pas où chercher [www.github.com.](http://www.github.com.) C'est donc le travail du FAI d'effectuer une recherche DNS (Domain Name System) pour demander quelle adresse IP le site que vous essayez de visiter est configuré pour utiliser.

**DNS :** Système de Noms de Domaine. Une base de données distribuée qui suit les noms de domaine des ordinateurs et leurs adresses IP correspondantes sur Internet. Ne vous inquiétez pas de comment fonctionne une « base de données distribuée » pour l'instant : sachez simplement que le DNS existe pour que les utilisateurs puissent entrer [www.github.com](http://www.github.com) au lieu d'une adresse IP.

**Nom de Domaine :** Utilisé pour identifier une ou plusieurs adresses IP. Les utilisateurs utilisent le nom de domaine (par exemple, [www.github.com)](http://www.github.com)) pour accéder à un site web sur Internet. Lorsque vous tapez le nom de domaine dans votre navigateur, le DNS l'utilise pour rechercher l'adresse IP correspondante pour ce site web donné.

**TCP/IP :** Protocole de Contrôle de Transmission/Protocole Internet. Le protocole de communication le plus largement utilisé. Un « protocole » est simplement un ensemble standard de règles pour faire quelque chose. TCP/IP est utilisé comme une norme pour transmettre des données sur les réseaux.

**Numéro de Port :** Un entier de 16 bits qui identifie un port spécifique sur un serveur et est toujours associé à une adresse IP. Il sert de moyen pour identifier un processus spécifique sur un serveur auquel les requêtes réseau pourraient être transmises.

**Hôte :** Un ordinateur connecté à un réseau — il peut s'agir d'un client, d'un serveur ou de tout autre type d'appareil. Chaque hôte a une adresse IP unique. Pour un site web comme [www.google.com,](http://www.google.com,) un hôte pourrait être le serveur web qui sert les pages du site web. Il y a souvent une confusion entre un hôte et un serveur, mais notez qu'ils sont deux choses différentes. Les serveurs sont un type d'hôte — ils sont une machine spécifique. D'autre part, un hôte pourrait désigner une organisation entière qui fournit un service d'hébergement pour maintenir plusieurs serveurs web. Vous pouvez exécuter un serveur à partir d'un hôte dans ce sens.

**HTTP :** Protocole de Transfert Hypertexte. Le protocole que les navigateurs web et les serveurs web utilisent pour communiquer entre eux sur Internet.

**URL :** Localisateurs Uniformes de Ressources. Les URL identifient une ressource web particulière. Un exemple simple est [https://github.com/someone.](https://github.com/someone.) L'URL spécifie le protocole (« https »), le nom de l'hôte (github.com) et le nom du fichier (la page de profil de quelqu'un). Un utilisateur peut obtenir la ressource web identifiée par cette URL via HTTP à partir d'un hôte réseau dont le nom de domaine est github.com. (un vrai casse-tête, non ?!)

### Le voyage du code à la page web

D'accord, maintenant que nous avons les définitions essentielles hors du chemin, parcourons cette recherche Github pour voir comment nous passons d'une URL tapée dans une barre d'adresse à une page web en cours d'exécution :

1) Vous tapez une URL dans votre navigateur

![Image](https://cdn-media-1.freecodecamp.org/images/1*WH4ggg4mrazpow_wn949zw.png)

2) Le navigateur analyse les informations contenues dans l'URL. Cela inclut le protocole (« https »), le nom de domaine (« github.com ») et la ressource (« / »). Dans ce cas, il n'y a rien après le « .com » pour indiquer une ressource spécifique, donc le navigateur sait qu'il doit récupérer simplement la page principale (index)

![Image](https://cdn-media-1.freecodecamp.org/images/0*tmmY7SzgWorjCvdz.png)

3) Le navigateur communique avec votre FAI pour effectuer une recherche DNS de l'adresse IP du serveur web qui héberge [www.github.com.](http://www.github.com.) Le service DNS contactera d'abord un Serveur de Noms Racine, qui regarde [https://www.github.com](https://www.github.com) et répond avec l'adresse IP d'un serveur de noms pour le domaine de premier niveau « .com ». Cette adresse est renvoyée à votre service DNS. Le service DNS effectue une autre recherche auprès du serveur de noms « .com » et lui demande l'adresse de [https://www.github.com.](https://www.github.com.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*sbTvDcrA3cKVJucF.gif)

_source : [https://technet.microsoft.com/en-us/library/bb962069.aspx](https://technet.microsoft.com/en-us/library/bb962069.aspx)_

4) Une fois que le FAI reçoit l'adresse IP du serveur de destination, il l'envoie à votre navigateur web

![Image](https://cdn-media-1.freecodecamp.org/images/0*PoVCRKdL0u0HbgTp.png)

[5) Votre navigateur prend l'adresse IP et le numéro de port donné par l'URL (le protocole HTTP utilise par défaut le port 80 et HTTPS utilise par défaut le port 443) et ouvre une connexion de socket TCP. À ce stade, votre navigateur web et votre serveur web sont enfin connectés.](http://preethikasireddy.me/wp-content/uploads/2015/12/Screen-Shot-2015-12-06-at-6.32.27-PM1.png)

[6) Votre navigateur web envoie une requête HTTP au serveur web pour la page web HTML principale de](http://preethikasireddy.me/wp-content/uploads/2015/12/Screen-Shot-2015-12-06-at-6.32.27-PM1.png) [www.github.com.](http://www.github.com.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*NQbimFDyqSnYh5_E.png)
_Requête GET du Client_

7) Le serveur web reçoit la requête et cherche cette page HTML. Si la page existe, le serveur web prépare la réponse et l'envoie à votre navigateur. Si le serveur ne peut pas trouver la page demandée, il enverra un message d'erreur HTTP 404, qui signifie « Page Non Trouvée ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*LALHLBWQQ8JuNAq-.png)
_Réponse du Serveur_

8) Votre navigateur web prend la page HTML qu'il reçoit et la parcourt en effectuant un scan complet de haut en bas à la recherche d'autres ressources listées, telles que des images, des fichiers CSS, des fichiers JavaScript, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-nGrKHBNHa9hYG9e.png)
_page index.html_

9) Pour chaque ressource listée, le navigateur répète tout le processus ci-dessus, en effectuant des requêtes HTTP supplémentaires au serveur pour chaque ressource.

10) Une fois que le navigateur a fini de charger toutes les autres ressources qui étaient listées dans la page HTML, la page sera enfin chargée dans la fenêtre du navigateur et la connexion sera fermée

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yxww843OcmviZodzLu3PJg.png)
_Github_

### Traverser l'abîme d'Internet

Une chose qui vaut la peine d'être notée est la manière dont les informations sont transmises lorsque vous faites une demande d'informations. Lorsque vous faites une demande, ces informations sont divisées en de nombreux petits morceaux appelés paquets. Chaque paquet est marqué avec un en-tête TCP, qui inclut les numéros de port source et de destination, et un en-tête IP qui inclut les adresses IP source et de destination pour lui donner son identité. Le paquet est ensuite transmis via Ethernet, WiFi ou un réseau cellulaire et est autorisé à voyager sur n'importe quel itinéraire et à prendre autant de sauts que nécessaire pour atteindre la destination finale.

(Nous ne nous soucions pas vraiment de la manière dont les paquets arrivent — tout ce qui compte, c'est qu'ils arrivent à destination sains et saufs !) Une fois que les paquets atteignent la destination, ils sont réassemblés et livrés en un seul morceau.

Alors, comment tous les paquets savent-ils comment atteindre leur destination sans se perdre ?

La réponse est TCP/IP.

TCP/IP est un système en deux parties, fonctionnant comme le système de « contrôle fondamental » d'Internet. IP signifie Protocole Internet ; son travail est d'envoyer et de router les paquets vers d'autres ordinateurs en utilisant les en-têtes IP (c'est-à-dire les adresses IP) sur chaque paquet. La deuxième partie, Transmission Control Protocol (TCP), est responsable de la division du message ou du fichier en paquets plus petits, du routage des paquets vers l'application correcte sur l'ordinateur de destination en utilisant les en-têtes TCP, de la réémission des paquets s'ils se perdent en chemin, et du réassemblage des paquets dans le bon ordre une fois qu'ils ont atteint l'autre extrémité.

### Peindre le tableau final

Mais attendez — le travail n'est pas encore terminé ! Maintenant que votre navigateur a les ressources composant le site web (HTML, CSS, JavaScript, images, etc.), il doit passer par plusieurs étapes pour présenter les ressources sous forme de page web lisible par l'homme.

Votre navigateur a un moteur de rendu qui est responsable de l'affichage du contenu. Le moteur de rendu reçoit le contenu des ressources en petits morceaux. Ensuite, il y a un algorithme d'analyse HTML qui indique au navigateur comment analyser les ressources.

Une fois analysé, il génère une structure arborescente des éléments DOM. DOM signifie Document Object Model et c'est une convention pour représenter les objets situés dans un document HTML. Ces objets — ou « nœuds » — de chaque document peuvent être manipulés à l'aide de langages de script comme JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/0*EHTSP-ftWos_vpxp.jpg)
_Un arbre DOM_

Une fois que l'arbre DOM est construit, les feuilles de style sont analysées pour comprendre comment styliser chaque nœud. En utilisant ces informations, le navigateur parcourt les nœuds DOM et calcule le style CSS, la position, les coordonnées, etc., pour chaque nœud.

Une fois que le navigateur a les nœuds DOM et leurs styles, il est *enfin* prêt à peindre la page sur votre écran en conséquence. Le résultat : tout ce que vous avez jamais regardé sur Internet.

### Le web est complexe, mais vous venez de terminer la partie difficile

Donc, voici le web en un mot. Perdu ? Nous le sommes tous, mais si vous avez lu jusqu'ici, vous avez déjà terminé la partie difficile. J'ai évidemment passé sous silence certains détails dans l'intérêt de vous montrer le tableau d'ensemble ici ; mais si vous pouvez comprendre la séquence de base des événements décrite ci-dessus, remplir les détails sera un jeu d'enfant.

Consultez la [Partie 2](https://medium.com/@preethikasireddy/how-the-web-works-part-ii-client-server-model-the-structure-of-a-web-application-735b4b6d76e3#.e6tmj8112), où nous aborderons la structure d'une application web basique. 😊
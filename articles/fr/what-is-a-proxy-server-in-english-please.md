---
title: Qu'est-ce qu'un serveur proxy ? En français, s'il vous plaît.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-01T04:27:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-proxy-server-in-english-please
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Proxies-1.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: privacy
  slug: privacy
- name: servers
  slug: servers
- name: Web Security
  slug: web-security
seo_title: Qu'est-ce qu'un serveur proxy ? En français, s'il vous plaît.
seo_desc: 'By Milecia McGregor

  Have you ever been traveling and couldn''t get the same shows you normally watch
  back home on Hulu? Or have you noticed that some websites are blocked or you can''t
  access certain services while you''re connected to different Wi-Fi n...'
---

Par Milecia McGregor

Vous est-il déjà arrivé de voyager et de ne pas pouvoir regarder les mêmes émissions que d'habitude sur Hulu depuis votre pays d'origine ? Ou avez-vous remarqué que certains sites web sont bloqués ou que vous ne pouvez pas accéder à certains services lorsque vous êtes connecté à différents réseaux Wi-Fi ? Cela est probablement dû à la présence d'un proxy.

## Qu'est-ce qu'un serveur proxy ?

Un serveur proxy, ou simplement proxy, est comme un autre ordinateur auquel vos requêtes internet sont envoyées avant d'atteindre le vrai site web. C'est un serveur qui prend toutes les informations que vous avez envoyées, comme une demande d'achat de nouvelles chemises sur H&M, et les achemine via une adresse IP différente.

C'est ce qui rend un proxy si puissant. Ils peuvent faire en sorte que toutes vos activités internet semblent provenir d'un emplacement complètement différent.

Les entreprises les utilisent pour des raisons de sécurité et de performance réseau, les particuliers pour des préoccupations de confidentialité, et il existe également des fonctionnalités intéressantes que vous pouvez exploiter lorsque vous utilisez des serveurs proxy pour votre navigation internet, dont nous parlerons plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/proxy-flow.png)

Un proxy peut être physiquement situé n'importe où. Vous pouvez configurer un proxy sur votre ordinateur personnel ou en déployer un dans le cloud. L'essentiel est que le proxy ait les configurations dont vous avez besoin pour la fonctionnalité que vous souhaitez.

Rappelez-vous simplement qu'un proxy agit comme un filtre d'adresse IP sophistiqué. Comme pour les filtres, il existe différents types de proxies et chacun a ses utilisations spécifiques.

Pour commencer, parlons du type de proxy le plus courant et de son fonctionnement, le [proxy direct](https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling).

## Comment fonctionne un proxy

Lorsque vous entendez ou voyez des gens parler de proxies, ils font probablement référence à des proxies directs. Ce sont les types de proxies les plus courants car ils gèrent facilement ce dont la plupart des gens ont besoin. Les proxies directs agissent comme intermédiaire entre vos requêtes et le serveur auquel vous essayez de vous connecter.

La manière dont un proxy fonctionne est la suivante : vous faites d'abord une requête, par exemple, vous essayez d'aller sur GitHub. Vous tapez l'URL et appuyez sur Entrée. Avec un proxy, au lieu de vous connecter directement à GitHub avec l'adresse IP de votre ordinateur, votre requête est interceptée par le proxy.

Ensuite, le proxy prend votre requête, la met à jour et l'envoie depuis sa propre adresse IP. Cela peut complètement supprimer votre adresse IP et les informations d'identification de la requête au serveur GitHub.

L'une des façons dont les proxies gèrent le changement de votre requête est directement dans les en-têtes de requête qu'ils envoient au serveur. Une requête proxy peut définir des en-têtes comme _Forwarded_ et _Via_ dans la requête originale avant d'envoyer le message au serveur duquel vous essayez d'obtenir des informations.

Une fois que le proxy a mis à jour les informations de votre requête, il envoie votre requête reformulée au serveur GitHub. Ce serveur pense maintenant que votre requête provient d'un emplacement différent et renvoie les données que vous vouliez via cet emplacement.

Ensuite, le proxy prend les données du serveur GitHub et effectue toutes les vérifications pour lesquelles il a été configuré avec ces données. Il pourrait vérifier la présence de scripts malveillants ou d'autres problèmes de sécurité. Ensuite, il envoie enfin les données à votre ordinateur et votre page se charge.

Un serveur proxy n'est pas nécessairement limité à un seul utilisateur à la fois. Plusieurs personnes peuvent envoyer des requêtes via le même proxy et elles peuvent toutes partager les mêmes avantages. Il existe de nombreuses raisons pour lesquelles vous pourriez utiliser un proxy, même s'il est partagé.

## Pourquoi utiliser un proxy

Maintenant que vous savez ce qu'est un proxy, il est bon de connaître certains des cas d'utilisation courants.

* Vous pouvez augmenter la sécurité du réseau en chiffrant les requêtes
• Empêcher les pirates d'intercepter des informations sensibles
• Bloquer les sites malveillants de votre réseau réel
* Vous pouvez réduire la quantité de trafic réseau en mettant en cache les sites
• Mettre en cache les sites web afin qu'une seule requête soit faite au site, peu importe le nombre d'utilisateurs sur le proxy
* Vous pouvez contrôler la manière dont les gens utilisent internet
• Bloquer des domaines spécifiques
• Surveiller et journaliser toutes les requêtes web
* Vous pouvez contourner les blocages mis en place par les entreprises et les pays
• Accéder au contenu d'un autre pays
• Contourner les pare-feu d'entreprise

Ce n'est pas une liste exhaustive de tout ce que vous pouvez faire avec les proxies, mais je voulais également inclure certains des autres avantages qui ne rentrent pas tout à fait dans les catégories typiques.

* Vous avez toujours les cookies bloqués
* Vous avez toujours les publicités bloquées
* Vous pouvez accéder au web profond
* Il supprime tout ciblage de recherche ou suivi de vos recherches précédentes
* Vous pouvez extraire des données
* Vous pouvez faire des recherches sur vos concurrents

## Différents types de proxies

Il existe de nombreux types de proxies différents qui couvrent presque toutes les configurations que vous pouvez imaginer. Voici un aperçu rapide de 14 types de proxies différents.

### Proxy transparent

Les proxies transparents sont les plus simples. Ils transmettent toutes vos informations, mais avec l'adresse IP du proxy. Ces proxies n'offrent aucune protection de la vie privée.

Ils informent le serveur auquel vous envoyez votre requête que la requête passe par un proxy. Cela suffit pour contourner les simples interdictions d'IP. Une utilisation courante des proxies transparents est la mise en place de filtres de sites web, comme le font les écoles et les entreprises.

### Proxy anonyme

Les proxies anonymes sont un type de proxy couramment utilisé. Ils ne transmettent jamais votre adresse IP au site web que vous consultez, bien qu'ils s'identifient comme un proxy dans la requête. Cela aide à garder votre activité de navigation privée.

Lorsque vous ne voulez pas que des publicités ciblées vous suivent sur internet ou que votre emplacement soit attaché à votre requête, ce sont des proxies standards à utiliser. Cela suffit généralement pour contourner la plupart des activités de ciblage, mais il reste une chance que vos informations soient révélées.

### Proxy à haute anonymité

Ces proxies sont les plus sécurisés car ils ne transmettent pas votre adresse IP et vos données personnelles et ne s'identifient pas comme un proxy lors de l'envoi de requêtes. Ils changent également sporadiquement l'adresse IP qu'ils utilisent pour les requêtes. C'est ce qui permet aux proxies à haute anonymité de vous offrir le plus de confidentialité en ligne.

Le navigateur TOR utilise ce type de proxy. Comme l'adresse IP change occasionnellement, cela rend extrêmement difficile pour les serveurs de suivre quel trafic appartient à quel client. Si vous ne voulez pas être suivi, c'est la meilleure option.

### Proxy de distorsion

Un proxy de distorsion fonctionne de manière similaire à un proxy anonyme, sauf qu'il transmet une IP qui est délibérément fausse. Il s'identifie comme un proxy et utilise cette fausse adresse IP dans les requêtes. Cela est idéal lorsque vous voulez apparaître comme si vous étiez dans un emplacement spécifique.

Cela est utile lorsque vous voulez contourner des restrictions de contenu spécifiques. C'est comme si vous pouviez choisir l'adresse IP que vous voulez que le proxy utilise.

### Proxy résidentiel

Les proxies résidentiels sont des proxies qui utilisent de vraies adresses IP. Cela signifie qu'ils sont les adresses de vrais ordinateurs. Ce sont les meilleurs types de proxies à utiliser car ils semblent être des clients réguliers pour les serveurs.

Tous les types de proxies discutés jusqu'à présent peuvent être des proxies résidentiels. Tant que l'adresse IP du proxy est associée à un appareil physique, ces types de proxies tendent à être indétectables et ils contournent certains des problèmes géographiques que les autres types de proxies ont.

### Proxy de centre de données

Ce sont un peu l'opposé des proxies résidentiels. Les proxies de centre de données ont des adresses IP générées par ordinateur qui ne sont pas attachées à un appareil réel. C'est comme avoir un proxy dans le cloud.

Un avantage de ce type de proxy est leur vitesse. Habituellement, les fournisseurs de services cloud ont des connexions internet incroyables qui vous donnent des vitesses que vous ne pourriez pas obtenir autrement. Bien qu'ils partageraient tous des adresses IP similaires, un serveur pourrait héberger des centaines de proxies de centre de données.

### Proxy public

De tous les types de proxies, ce sont les proxies les plus non sécurisés et non fiables disponibles. Ils peuvent tomber en panne à tout moment et beaucoup sont mis en place par des pirates pour voler des données. La seule raison pour laquelle les gens les utilisent encore est qu'ils sont gratuits.

Bien qu'il ne soit pas difficile de trouver des listes de proxies publics gratuits, il est difficile d'en trouver de bons. Vous ne savez jamais qui héberge ces proxies et c'est un énorme risque d'envoyer vos informations sensibles via l'un d'eux. Un nombre quelconque d'utilisateurs peut être sur un proxy public à tout moment et il n'y a personne pour réguler qui l'utilise.

### Proxy privé

Les proxies privés ont une certaine ambiguïté quant à ce qu'ils sont car ils sont définis par le fournisseur offrant le service. Cela pourrait signifier que votre proxy ne peut être utilisé que par un seul client à la fois ou que votre proxy nécessite une authentification avant de pouvoir l'utiliser. Ce sont des versions plus fiables des proxies publics.

Un proxy privé peut être transparent ou avoir une haute anonymité, similaire à certains des autres mentionnés ci-dessus comme le proxy résidentiel ou de centre de données. Ce type de proxy a plus à voir avec qui peut s'y connecter qu'avec la manière dont il gère vos requêtes.

### Proxy dédié

Un proxy dédié est comme un type spécifique de proxy privé. Cela signifie simplement que le proxy ne peut pas être partagé par plusieurs clients en même temps. Donc, un seul client peut se connecter et envoyer des requêtes.

Cela aide à prévenir l'interdiction de l'adresse IP du proxy par différents sites web et services. C'est l'une des façons dont un fournisseur de proxy peut contrôler qui a accès au proxy pour s'assurer qu'il n'est pas abusé.

### Proxy partagé

Ce sont certains des proxies les moins chers disponibles et ils fonctionnent de manière similaire aux serveurs partagés. Les clients se regroupent et partagent le coût du proxy et ils peuvent tous y accéder en même temps. Les proxies partagés ont une architecture plus complexe car ils gèrent beaucoup de requêtes en même temps.

Selon la manière dont les ressources sont allouées sur le proxy partagé, les requêtes peuvent être plus lentes que via votre propre adresse IP. Parce qu'il gère plusieurs requêtes de plusieurs utilisateurs, les configurations de ces types de proxies sont plus critiques que les autres.

### Proxy rotatif

Les proxies rotatifs fonctionnent un peu différemment des autres. Chaque fois qu'un client se connecte au proxy, une nouvelle adresse IP est créée pour lui. Ils n'utilisent donc jamais la même adresse IP plus d'une fois.

Chaque fois qu'un client envoie une requête, une nouvelle adresse IP est générée. C'est ainsi que fonctionnent les proxies comme le navigateur TOR pour maintenir votre anonymat. Un proxy rotatif offre un haut niveau de sécurité et de confidentialité lorsqu'il est combiné avec certains des autres types.

### Proxy SSL

Ces proxies suivent le même protocole que les requêtes HTTPS. Le 'S' dans HTTPS signifie SSL, ce qui signifie que vos requêtes web sont sécurisées entre votre client et le serveur auquel vous essayez d'accéder.

Cela signifie que vous obtenez encore plus de sécurité car toutes vos requêtes via le proxy sont chiffrées. La plupart des proxies devraient utiliser cela par défaut, mais il reste une chance que vous tombiez sur certains qui utilisent HTTP.

### Proxy inverse

Les proxies inverses sont complètement différents de tout ce que nous avons couvert jusqu'à présent. Un proxy inverse masque l'adresse IP d'un serveur auquel vous essayez d'envoyer une requête. Lorsque un serveur a besoin de sécurité et de confidentialité vis-à-vis des clients, c'est là que ces types de proxies entrent en jeu.

Ces proxies sont idéaux si vous devez surveiller l'accès à un serveur pour des raisons comme empêcher les clients d'avoir un accès non surveillé à une base de données. Cela peut également aider à réduire le trafic sur le réseau en transmettant des informations mises en cache au lieu de faire une requête à chaque fois.

## Services de proxy

Si vous avez fait une recherche rapide de services de proxy, vous savez qu'il y en a beaucoup à choisir. Tous ne sont pas créés égaux, il est donc important que vous sachiez quelles fonctionnalités vous voulez de votre service de proxy.

La plupart de ces services offrent des combinaisons de types de proxies. Par exemple, vous pourrez trouver des proxies résidentiels, à haute anonymité, SSL regroupés en un seul service. Il y en a quelques-uns qui se démarquent des autres, voici donc une liste, mais assurez-vous de les rechercher pour voir s'ils répondent à vos besoins.

* [https://smartproxy.com/](https://smartproxy.com/)
* [https://www.megaproxy.com/](https://www.megaproxy.com/)
* [https://whoer.net/webproxy](https://whoer.net/webproxy)
* [https://www.proxysite.com/](https://www.proxysite.com/)
* [https://hide.me/en/proxy](https://hide.me/en/proxy)
* [https://www.kproxy.com/](https://www.kproxy.com/)
* [https://www.vpnbook.com/webproxy](https://www.vpnbook.com/webproxy)

## Serveur proxy vs VPN

Si vous êtes familier avec les VPN (réseaux privés virtuels), vous vous demandez peut-être en quoi un proxy est différent. La principale différence est qu'un VPN sécurise tout votre trafic réseau, alors que les proxies ne sécurisent que votre trafic internet.

Certaines choses que les VPN sécurisent et que les proxies ne font pas incluent les téléchargements ou uploads FTP et les processus de fond du système d'exploitation, comme les mises à jour.

La seule chose que les proxies et les VPN ont en commun est qu'ils font en sorte que votre trafic internet semble provenir d'une adresse IP différente. C'est tout ce qu'ils ont en commun. La manière dont ils gèrent cela est complètement différente en raison de ce pour quoi ils sont utilisés.

Un proxy transmet simplement vos requêtes internet, agissant comme un intermédiaire. Un VPN, en revanche, tunnelise toute votre activité réseau jusqu'au niveau du système d'exploitation. Les proxies sont généralement utilisés par une seule application comme un navigateur ou un client de torrent.

Les entreprises ont tendance à utiliser des VPN pour permettre aux employés d'accéder aux ressources de l'entreprise sans se soucier de l'interception ou de l'enregistrement du trafic par un FAI (fournisseur d'accès internet). Ceux-ci sont généralement hébergés sur un ordinateur physique quelque part sur place.

L'avantage des VPN est qu'ils dissimulent tout ce que vous faites. Si votre FAI devait obtenir un historique de votre utilisation, il ne verrait que le fait que vous étiez connecté à un VPN. Rien de votre trafic ne serait visible. Lorsque vous vous connectez à un Wi-Fi public, un VPN est le choix le plus sécurisé.

Avec tous les avantages qui accompagnent l'utilisation d'un VPN, il existe encore de bonnes raisons pour lesquelles les gens choisissent des proxies. Pour commencer, les VPN sont généralement plus chers qu'un proxy. Vous avez également besoin d'un matériel informatique décent pour exécuter un VPN. La connexion est généralement plus lente que celle d'un proxy.

Il existe de nombreuses situations où vous n'avez pas nécessairement besoin du type de sécurité qu'offre un VPN. Lorsque vous voulez simplement masquer vos activités sur une seule application à moindre coût, un proxy pourrait valoir la peine d'être considéré.

## Avantages et risques

Maintenant que vous savez tout sur les proxies, voici une liste de certains des avantages et risques associés à leur utilisation.

### Avantages

* Navigation internet sécurisée et privée
* Capacité à contourner les restrictions géolocalisées
* Meilleure performance du réseau
* Capacité à contrôler les sites web auxquels les clients ont accès
* De nombreux types parmi lesquels choisir pour répondre à des besoins spécifiques

### Risques

* Vos requêtes peuvent revenir très lentement
* Tous les proxies ne chiffrent pas vos requêtes, donc vos informations pourraient encore fuir
* Les proxies gratuits ou bon marché pourraient être mis en place par des pirates ou des agences gouvernementales
* Les proxies peuvent disparaître à tout moment
* Toutes vos requêtes et informations passent toujours par un tiers qui pourrait être géré par n'importe qui

Il existe de nombreux autres avantages et risques à utiliser l'un des types de serveurs proxy. C'est pourquoi il est important de ne se connecter qu'à des serveurs proxy en lesquels vous avez confiance. Lorsque vous êtes connecté à un proxy de confiance, les risques devraient avoir été pris en compte dans les configurations afin que vous ayez moins à vous en soucier.

## Comment configurer un serveur proxy simple

Créer votre propre proxy privé semble beaucoup plus difficile que cela ne l'est en réalité. Vous pouvez créer un proxy avec un ordinateur chez vous qui est aussi sécurisé que la plupart des proxies que vous pouvez acheter. Cela demande simplement un peu de patience et de curiosité.

Sur un serveur Linux, vous pouvez installer Squid et configurer les paramètres pour le proxy que vous souhaitez créer. Vous pourrez faire des choses comme bloquer des sites web spécifiques ou exiger une authentification avant qu'un client puisse se connecter au proxy.

Voici un excellent guide pour configurer un proxy Squid sur Linux : [https://devopscube.com/setup-and-configure-proxy-server/](https://devopscube.com/setup-and-configure-proxy-server/)

Sur Windows et Mac, vous avez la possibilité de créer un serveur proxy en utilisant Python et le [Google App Engine](https://cloud.google.com/appengine). Vous devrez payer pour le service Google App Engine, mais ils le rendent assez abordable.

Configurer un proxy de cette manière est un peu plus impliqué que sur Linux, mais voici un excellent guide : [https://www.hongkiat.com/blog/proxy-with-google-app-engine/](https://www.hongkiat.com/blog/proxy-with-google-app-engine/)

## Comment se connecter à un proxy existant

Se connecter à des proxies est généralement un processus simple une fois que vous connaissez les informations de votre proxy, comme son adresse IP et son numéro de port. Peu importe le système d'exploitation que vous utilisez, les proxies sont généralement rapides à configurer.

Typiquement, vous irez dans vos paramètres réseau et trouverez où vous pouvez entrer les informations de votre proxy. Ensuite, vous devriez pouvoir vous connecter et une page web pourrait apparaître s'il y a une étape d'authentification incluse par le proxy. Voici à quoi cela ressemble sur Windows et Ubuntu.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-242.png)
_configuration d'un serveur proxy via les paramètres Windows_

![Image](https://www.freecodecamp.org/news/content/images/2020/04/ubuntu-proxy.png)
_configuration d'un serveur proxy via les paramètres réseau d'Ubuntu_

## Conclusion

Maintenant, vous savez tout sur les serveurs proxy, de ce qu'ils sont à comment en créer un pour vous-même ! J'ai un petit proxy configuré sur mon réseau domestique et cela facilite l'accès à certaines choses lorsque je suis loin de chez moi.

J'écris également sur d'autres sujets aléatoires dans le domaine de la technologie, comme l'apprentissage automatique et la réalité virtuelle. Vous devriez me suivre sur [Twitter](https://twitter.com/FlippedCoding) pour apprendre des choses qui sont parfois simplement cool. De plus, [j'ai un site web](https://flippedcoding.com) où vous pouvez consulter mes autres articles et regarder ma lente transition du site actuel vers mon nouveau site flambant neuf.
---
title: 'Comment rester en sécurité sur Internet : les serveurs proxy tout au long
  du chemin'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-09-17T13:15:00.000Z'
originalURL: https://freecodecamp.org/news/how-apps-stay-safe
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/Victoria-drake-image.png
tags:
- name: Application Security
  slug: application-security
- name: servers
  slug: servers
seo_title: 'Comment rester en sécurité sur Internet : les serveurs proxy tout au long
  du chemin'
seo_desc: 'This article is an overview of how proxy servers form the basis of online
  anonymity. We''ll discuss how you can use proxies to help both users and web applications.

  One core aspect of online privacy is the use of a proxy server - though this basic
  bui...'
---

Cet article est un aperçu de la manière dont les serveurs proxy constituent la base de l'anonymat en ligne. Nous discuterons de la manière dont vous pouvez utiliser des proxies pour aider à la fois les utilisateurs et les applications web.

Un aspect central de la confidentialité en ligne est l'utilisation d'un serveur proxy - bien que ce bloc de construction de base ne soit pas visible sous ses formes plus reconnaissables.

Les serveurs proxy sont une chose utile à connaître de nos jours, pour les développeurs, les propriétaires de produits logiciels, ainsi que pour le chien moyen sur Internet. 

Explorons ce qui fait des serveurs proxy une pièce importante du soutien à la cybersécurité.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Internet_dog.jpg)
_"Sur Internet, personne ne sait que vous êtes un chien." Comic par Peter Steiner de The New Yorker._

Lorsque [la bande dessinée de Peter Steiner](https://en.wikipedia.org/wiki/On_the_Internet,_nobody_knows_you%27re_a_dog) a été publiée pour la première fois dans The New Yorker en 1993, elle est apparemment passée largement inaperçue. Ce n'est que plus tard que l'allusion sinistre et légèrement effrayante à l'anonymat en ligne a touché la conscience publique avec les doigts glacés de l'inconnu. 

À mesure que l'utilisation d'Internet est devenue plus populaire, les utilisateurs se sont inquiétés du fait que d'autres personnes pouvaient se représenter en ligne de la manière qu'ils choisissaient, sans que personne d'autre ne sache qui ils étaient vraiment.

Ceci - pour faire une sous-estimation grossière - n'est plus le cas. Grâce aux [cookies de suivi](https://support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences), à [l'empreinte digitale du navigateur](https://robertheaton.com/2017/10/17/we-see-you-democratizing-de-anonymization/), aux [fournisseurs de services Internet (FAI) vendant vos journaux de navigation aux annonceurs](https://www.privacypolicies.com/blog/isp-tracking-you/), et à votre propre inclination inexplicable à mettre votre nom et votre visage sur les réseaux sociaux, l'anonymat en ligne est dépassé comme les saveurs de LaCroix de l'année dernière.

Votre voisin d'à côté ne sait peut-être pas comment vous trouver en ligne (à part à travers cette application de marché de seconde main basée sur la localisation que vous utilisez), mais vous pouvez être certain qu'au moins une grande entreprise de publicité a une série de zéros et de uns quelque part qui vous représentent, les détails spécifiques de votre démographie de marché, et toutes vos habitudes en ligne. Y compris votre saveur préférée de LaCroix.

Il existe des moyens d'ajouter _certaines_ couches d'obscurité, comme l'utilisation d'un pare-feu d'entreprise qui cache votre IP, ou [l'utilisation de Tor](https://www.torproject.org/). 

Le mécanisme sous-jacent de ces deux méthodes est le même. Comme étant enveloppé dans les couches d'un oignon, vous utilisez un ou plusieurs [serveurs proxy](https://en.wikipedia.org/wiki/Proxy_server) pour vous protéger des suivis tiers.

#### Qu'est-ce qu'un serveur proxy, de toute façon ?

Un proxy, dans la définition traditionnelle anglaise, est l'« autorité ou le pouvoir d'agir pour un autre. » ([Merriam-Webster](https://www.merriam-webster.com/dictionary/proxy)) Un serveur proxy, dans le contexte informatique, est un serveur qui agit au nom d'un autre serveur, ou de la machine d'un utilisateur.

En utilisant un proxy pour naviguer sur Internet, par exemple, un utilisateur peut éviter d'être personnellement identifiable. Tout le trafic Internet de l'utilisateur semble provenir du serveur proxy au lieu de sa machine.

#### Les serveurs proxy sont pour les utilisateurs

Il existe quelques moyens pour vous, en tant que client, d'utiliser un serveur proxy pour dissimuler votre identité lorsque vous allez en ligne. Il est important de savoir que ces méthodes offrent différents niveaux d'anonymat, et qu'aucune méthode ne fournira vraiment un _vrai_ anonymat. 

Si d'autres personnes cherchent activement à vous trouver sur Internet, pour une raison quelconque, vous devriez prendre des mesures supplémentaires pour rendre votre activité plus difficile à identifier. (Ces mesures dépassent le cadre de cet article, mais vous pouvez commencer avec la ressource [Surveillance Self-Defense de l'Electronic Frontier Foundation (EFF)](https://ssd.eff.org/).) 

Pour le chien moyen sur Internet, voici un petit menu d'options allant de la moins à la plus anonyme.

#### Utiliser un proxy dans votre navigateur web

Certains navigateurs web, y compris Firefox et Safari sur Mac, vous permettent de les configurer pour envoyer votre trafic Internet via un serveur proxy. 

Le serveur proxy tente d'[anonymiser](https://en.wikipedia.org/wiki/Anonymizer) vos requêtes en remplaçant votre adresse IP d'origine par l'adresse IP du serveur proxy. Cela vous offre un certain anonymat, car le site web que vous essayez d'atteindre ne verra pas votre adresse IP d'origine. Cependant, le serveur proxy que vous choisissez d'utiliser saura exactement qui a émis la requête.

Cette méthode n'encrypte pas nécessairement le trafic, ne bloque pas les cookies, ni n'empêche les trackers des réseaux sociaux et inter-sites de vous suivre ; en revanche, c'est la méthode la moins susceptible d'empêcher les sites web utilisant des cookies de fonctionner correctement.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/0_07snWvA_wsI_deAm.png)

Des serveurs proxy publics existent. Décider si vous devriez en utiliser un est comparable à décider si vous devriez manger un bonbon donné par un inconnu souriant.

Si votre institution académique ou votre entreprise fournit une adresse de serveur proxy, il s'agit (espérons-le) d'un serveur privé avec une certaine sécurité en place.

Ma méthode préférée, si vous avez un peu de temps et quelques dollars par mois à investir dans la sécurité, est de configurer votre propre instance virtuelle avec une entreprise telle que [Amazon Web Services](https://aws.amazon.com/ec2/) ou [Digital Ocean](https://www.digitalocean.com/products/droplets/) et d'utiliser cela comme votre serveur proxy.

Pour utiliser un proxy via votre navigateur, vous pouvez [modifier vos paramètres de connexion dans Firefox](https://support.mozilla.org/en-US/kb/connection-settings-firefox), ou [configurer un serveur proxy en utilisant Safari sur Mac](https://support.apple.com/guide/safari/set-up-a-proxy-server-ibrw1053/mac).

En ce qui concerne le choix d'un navigateur, je recommanderais volontiers [Firefox](https://www.mozilla.org/en-US/firefox/new/) à tout utilisateur d'Internet qui souhaite renforcer la sécurité de son expérience de navigation dès le départ. 

Mozilla a été un champion de la confidentialité depuis que je les connais, et a récemment apporté des modifications bien accueillies à la [Protection contre le pistage renforcée dans le navigateur Firefox](https://blog.mozilla.org/blog/2019/06/04/firefox-now-available-with-enhanced-tracking-protection-by-default/) qui bloque les trackers des réseaux sociaux, les cookies de pistage inter-sites, les empreintes digitales et les cryptomineurs par défaut.

#### Utiliser un VPN sur votre appareil

Afin de tirer parti d'un serveur proxy pour toute votre utilisation d'Internet au lieu de simplement via un navigateur, vous pouvez utiliser un réseau privé virtuel (VPN). 

Un VPN est un service, généralement payant, qui envoie votre trafic Internet via leurs serveurs, agissant ainsi comme un proxy. Un VPN peut être utilisé sur votre ordinateur portable ainsi que sur vos appareils téléphone et tablette, et comme il englobe tout votre trafic Internet, il ne nécessite pas beaucoup d'efforts supplémentaires à utiliser autre que de s'assurer que votre appareil est connecté. 

L'utilisation d'un VPN est un moyen efficace d'empêcher les FAI indiscrets de fouiner dans vos requêtes.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_B8XYVrDTlI8KXcm27dFmUQ.png)

Pour utiliser un service VPN payant tiers, vous vous inscrivez généralement sur leur site web et téléchargez leur application. Il est important de garder à l'esprit que, quel que soit le fournisseur que vous choisissez, vous lui confiez vos données. 

Les fournisseurs de VPN anonymisent votre activité sur Internet, mais peuvent eux-mêmes voir toutes vos requêtes. Les fournisseurs varient en termes de leurs politiques de confidentialité et des données qu'ils choisissent de journaliser, donc une petite recherche peut être nécessaire pour déterminer lequel, le cas échéant, vous êtes à l'aise de faire confiance.

Vous pouvez également créer votre propre service VPN en utilisant une instance virtuelle et [OpenVPN](https://openvpn.net/). OpenVPN est un protocole VPN open source, et peut être utilisé avec quelques fournisseurs d'instances virtuelles, tels que [Amazon VPC](https://openvpn.net/amazon-cloud/), [Microsoft Azure](https://openvpn.net/microsoft-azure/), [Google Cloud](https://openvpn.net/google-cloud-vpn/), et [Digital Ocean Droplets](https://openvpn.net/digital-ocean-vpn/). 

J'ai précédemment écrit un tutoriel sur la [configuration de votre propre service VPN personnel avec AWS](https://victoria.dev/verbose/how-to-set-up-openvpn-on-aws-ec2-and-fix-dns-leaks-on-ubuntu-18.04-lts/) en utilisant une instance EC2. J'utilise cette solution personnellement depuis environ un mois, et cela m'a coûté presque 4 USD au total, ce qui est un prix que je suis tout à fait prêt à payer pour un peu de tranquillité d'esprit.

#### Utiliser Tor

Tor prend l'anonymat offert par un serveur proxy et le multiplie en transmettant vos requêtes via un [réseau de relais](https://en.wikipedia.org/wiki/Relay_network) d'autres serveurs, chacun appelé un "nœud". 

Votre trafic passe par trois nœuds sur son chemin vers une destination : les nœuds _guard_, _middle_, et _exit_. À chaque étape, la requête est chiffrée et anonymisée de sorte que le nœud actuel ne sait que où l'envoyer, et rien de plus sur ce que la requête contient.

Cette séparation des connaissances signifie que, parmi les options discutées, Tor offre la version la plus complète de l'anonymat. (Pour une explication plus complète, voir [l'article de Robert Heaton sur le fonctionnement de Tor](https://robertheaton.com/2019/04/06/how-does-tor-work/), qui est si bien fait que je souhaite l'avoir écrit moi-même.)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_S-lzVbWxv3Y_iskGZ3aCwQ.png)

Cela dit, ce niveau d'anonymat a son propre coût. Pas monétaire, car [Tor Browser](https://www.torproject.org/download/) est gratuit à télécharger et à utiliser. Il est, cependant, plus lent que l'utilisation d'un VPN ou d'un simple serveur proxy via un navigateur, en raison du chemin détourné que prennent vos requêtes.

#### Les serveurs proxy sont aussi pour les serveurs

Maintenant que vous êtes familier avec les serveurs proxy dans le contexte de la protection des utilisateurs lorsqu'ils surfent sur le web. Cependant, les proxies ne sont pas seulement pour les clients. Les sites web et les applications connectées à Internet peuvent utiliser des [serveurs proxy inverses](https://en.wikipedia.org/wiki/Reverse_proxy) pour l'obscurcissement également. La partie "inverse" signifie simplement que le proxy agit au nom du serveur, au lieu du client.

Pourquoi un serveur web se soucierait-il de l'anonymat ? Généralement, ils ne s'en soucient pas. Du moins, pas de la même manière que certains utilisateurs.

Les serveurs web peuvent bénéficier de l'utilisation d'un proxy pour plusieurs raisons différentes. Par exemple, ils offrent généralement un service plus rapide aux utilisateurs en [mettant en cache](https://en.wikipedia.org/wiki/Web_cache) ou en [compressant](https://en.wikipedia.org/wiki/HTTP_compression) le contenu pour optimiser la livraison. 

D'un point de vue cybersécurité, cependant, un proxy inverse peut améliorer la posture de sécurité d'une application en obscurcissant l'infrastructure sous-jacente.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_9SL4Lh-A5dFsQSaCHT2Ekw.png)

En gros, en plaçant un autre serveur web (le "proxy") devant le serveur web qui accède directement à tous les fichiers et actifs, vous rendez plus difficile pour un attaquant de localiser votre serveur web "réel" et de manipuler vos données. 

Comme lorsque vous voulez voir le gérant du magasin et que le commis à qui vous parlez dit : "Je parle pour le gérant", et vous n'êtes pas vraiment sûr qu'il y ait même un gérant, de toute façon, mais vous échangez avec succès le My Little Pony rose vif qu'ils vous ont vendu pour un _fuchsia_, merci beaucoup, donc maintenant vous ne vous souciez plus de savoir qui est le gérant et s'il existe vraiment, et si vous le croisiez dans la rue, vous ne pourriez pas l'arrêter et le confondre pour avoir fait passer le rose vif pour du fuchsia, et le gérant est tout à fait satisfait de cela.

Certains serveurs web courants peuvent également agir comme des proxies inverses, souvent avec juste un changement de configuration minimal et direct. Bien que le meilleur choix pour votre architecture particulière me soit inconnu, je vais offrir ici quelques exemples courants.

#### Utiliser NGINX comme proxy inverse

NGINX utilise la directive `proxy_pass` dans son [fichier de configuration](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/) (`nginx.conf` par défaut) pour se transformer en serveur proxy inverse. La configuration nécessite les lignes suivantes à placer dans le fichier de configuration :

```
location /chemin/demande/ {proxy_pass http://www.example.com/chemin/cible/;}
```

Cela spécifie que toutes les requêtes pour le chemin `/chemin/demande/` sont transmises à `http://www.example.com/chemin/cible/`. La cible peut être un nom de domaine ou une adresse IP, cette dernière avec ou sans port.

Le [guide complet pour utiliser NGINX comme proxy inverse](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) fait partie de la documentation NGINX.

#### Utiliser Apache httpd comme proxy inverse

Apache httpd nécessite également une configuration simple pour agir comme serveur proxy inverse. Dans le [fichier de configuration](https://httpd.apache.org/docs/current/configuring.html), généralement `httpd.conf`, définissez les directives suivantes :

```
ProxyPass "/chemin/demande/" "http://www.example.com/chemin/cible/"ProxyPassReverse "/chemin/demande/" "http://www.example.com/chemin/cible/"
```

La directive `ProxyPass` garantit que toutes les requêtes pour le chemin `/chemin/demande/` sont transmises à `http://www.example.com/chemin/cible/`. La directive `ProxyPassReverse` garantit que les en-têtes envoyés par le serveur web sont modifiés pour pointer vers le serveur proxy inverse à la place.

Le [guide complet du proxy inverse pour le serveur HTTP Apache](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html) est disponible dans leur documentation.

#### Les serveurs proxy _presque_ tout au long du chemin

Je concède que mon titre est un peu facétieux, car les meilleures pratiques de cybersécurité ne sont pas vraiment un mystère de régression infinie éternelle (bien qu'elles puissent parfois sembler l'être). 

Quoi qu'il en soit, j'espère que cet article vous a aidé à comprendre ce que sont les serveurs proxy, comment ils contribuent à l'anonymat en ligne pour les clients et les serveurs, et qu'ils sont un bloc de construction intégral des pratiques de cybersécurité.

Si vous souhaitez en savoir plus sur les meilleures pratiques personnelles pour la sécurité en ligne, je vous recommande vivement d'explorer les articles et ressources fournis par [EFF](https://www.eff.org/). Pour un guide sur la sécurisation des sites web et des applications, la [série de fiches de l'OWASP](https://github.com/OWASP/CheatSheetSeries) est une ressource fantastique.
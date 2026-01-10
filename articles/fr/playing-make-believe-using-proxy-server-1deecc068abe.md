---
title: Jouer à faire semblant en utilisant un serveur proxy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T18:43:04.000Z'
originalURL: https://freecodecamp.org/news/playing-make-believe-using-proxy-server-1deecc068abe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PcOOLbgE1nZgS4gGS7p1qg.jpeg
tags:
- name: Android
  slug: android
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Jouer à faire semblant en utilisant un serveur proxy
seo_desc: 'By Sumit Gupta

  Guide to using a proxy server (mitmproxy) to get the response you want


  Say you are developing a feature in an E-commerce web/mobile app.You have to show
  an “Item is out of stock” banner on the “Cart” page when an item is out of stock....'
---

Par Sumit Gupta

#### Guide pour utiliser un serveur proxy (mitmproxy) afin d'obtenir la réponse souhaitée

![Image](https://cdn-media-1.freecodecamp.org/images/Zy98n3y2PSPX-VPuOC3AEZ-Y5R2yHB-pZHDg)

Disons que vous développez une fonctionnalité dans une application web/mobile de commerce électronique. 
Vous devez afficher une bannière "L'article est en rupture de stock" sur la page "Panier" lorsqu'un article est en rupture de stock.

Vous appelez un endpoint `/cart` et cet endpoint retourne quelque chose comme ceci.

```
[  {    "name": "SomeShoes",    "soldOut": false,    "price": "$50",    "quantity": 1,    ...  }]
```

Vous obtenez `soldOut` comme `true` lorsque l'article est en rupture de stock. 
Pour faciliter le développement, vous devrez simuler ce comportement.

Quelques façons de le faire pourraient être :

1. Vous ajoutez un article au panier puis vous connectez en tant qu'un autre utilisateur pour acheter tout le stock disponible. Cela simulerait que l'article est en rupture de stock pour le premier utilisateur.
2. Vous ajoutez un article au panier puis modifiez les données ou changez le code dans l'API backend pour vous assurer que l'article est en rupture de stock.

Les deux approches ci-dessus fonctionneraient, mais pourraient nécessiter beaucoup de travail. Si ces API sont externes, vous aurez alors presque aucun contrôle. La première approche pourrait être possible, mais la seconde est impossible.

Et si vous pouviez pirater votre chemin et changer la valeur de `soldOut` en `true` sans aucune des méthodes ci-dessus ?

> Entrez le serveur proxy

Un serveur proxy vous permet de voir la réponse du serveur et de la modifier avant même qu'elle n'arrive à l'application front-end. Vous pouvez intercepter l'appel API `/cart` et modifier la valeur de `soldOut` en `true` dans la réponse.

Imaginez combien de temps vous économiserez. Tout ce que vous vouliez, c'était vérifier comment votre bannière de rupture de stock apparaît lorsqu'elle s'affiche, si elle le fait.

Personne ne veut changer le monde pour s'assurer d'obtenir un true au lieu d'un false.

#### Choisir votre serveur proxy

Il existe de nombreux serveurs proxy qui vous permettront de faire cela, et l'un d'eux est **mitmproxy.**

mitmproxy est un outil gratuit et open source pour Windows, Linux et Mac.

Voici comment utiliser mitmproxy (les commandes ci-dessous sont pour Mac, mais elles devraient également fonctionner sur Linux).

#### Installation

Mac : `brew install mitmproxy`  
Autres : Vous pouvez trouver les instructions d'installation [ici](https://docs.mitmproxy.org/stable/overview-installation/).

mitmproxy dispose d'interfaces en ligne de commande et web.

#### Interface Web

Pour démarrer le serveur proxy, utilisez la commande :

Mac : `mitmweb --port 9000 --web-port 9001`  
Windows : `mitmweb.exe --listen-port 9000 --web-port 9001`

Ici, `--port` et `--listen-port` sont utilisés pour spécifier le port sur lequel le serveur proxy s'exécutera et `--web-port` est utilisé pour spécifier le port pour l'interface web du serveur.

Ouvrez maintenant l'URL `[localhost:9001](localhost:9001)`  
Ci-dessous se trouve l'interface web du serveur proxy où vous pouvez voir chaque requête qui le traverse.

![Image](https://cdn-media-1.freecodecamp.org/images/uvCnTTOtuRfs2sOHlKBiAz9jCjj3kj-Ht8lc)
_interface web de mitmproxy_

Maintenant, nous devons router toutes les requêtes réseau à travers celui-ci.

J'utilise Firefox pour cela car il prend en charge l'ajout de paramètres de proxy et de certificats uniquement pour Firefox.

**Note : un téléphone/émulateur Android ou tout autre client peut également être utilisé.**

#### **Configurer Firefox**

![Image](https://cdn-media-1.freecodecamp.org/images/YPmKXNFtsRWVSjMYtHM0zsoJiLq75JXlaQx1)

#### **Configurer le Proxy**

Installez et ouvrez Firefox.  
Recherchez "Paramètres de connexion" dans les paramètres.

Ici, vous ajouterez manuellement une configuration de proxy. Si vous suivez ce guide, ajoutez alors `localhost` dans le proxy HTTP et le port comme `9000`.   
De plus, effacez le texte "Pas de proxy pour".

#### **Installer le certificat mitmproxy**

Vous devez installer un certificat pour que mitmproxy fonctionne. Sinon, votre navigateur ne vous permettra pas d'accéder à quoi que ce soit.

**NE PAS INSTALLER CES CERTIFICATS SUR VOTRE SYSTÈME. INSTALLEZ-LES UNIQUEMENT SUR LE CLIENT** (le client est Firefox dans ce guide).** Installer ces certificats sur votre système est une vulnérabilité de sécurité.

C'est une autre raison pour laquelle je choisis Firefox. Firefox vous permet d'installer des certificats uniquement pour lui-même.

![Image](https://cdn-media-1.freecodecamp.org/images/SX6Wo4zS7ffCrfxSHvu1sIOVmmvCOYUqRNts)

Ouvrez l'URL "[mitm.it](http://mitm.it)" dans votre Firefox puis cliquez sur "**Autre**" pour installer le certificat. Cochez la case "Faire confiance à cette autorité de certification pour identifier les sites web."

L'étape ci-dessus installera le certificat mitmproxy uniquement dans Firefox.

N'installez pas le certificat en cliquant sur Apple, Windows ou Android, sauf si votre client est une machine virtuelle Windows ou un simulateur iOS/émulateur Android ou un vrai téléphone que vous souhaitez utiliser comme client.

> Nous sommes prêts

Frappez n'importe quelle URL que vous voulez et vérifiez l'interface web de mitmproxy. Vous y trouverez votre requête/réponse.

#### **Modifier la requête et la réponse**

Pour modifier la requête et la réponse, vous devez d'abord intercepter une requête.  
Lorsque vous interceptez une requête, elle est arrêtée deux fois. Une fois lorsqu'elle va au serveur et une seconde fois lorsque la réponse vient du serveur.

Pour l'intercepter, ajoutez un motif d'URL dans la zone de texte "Intercepter".

![Image](https://cdn-media-1.freecodecamp.org/images/IRivZaC9hACTqxJ3-KRh2l8pAGLJ9k2AgzFg)

Dans l'image ci-dessus, j'ai intercepté l'URL qui contient "localhost". Les requêtes sont affichées dans la boîte en bas à gauche. La requête actuelle est en pause car elle est interceptée. Vous pouvez modifier la requête ici.

Maintenant, basculez vers l'onglet "Flow" et appuyez sur le bouton de reprise.

![Image](https://cdn-media-1.freecodecamp.org/images/6EiQGKSOM8Gq6d0VFwOqR7Yh5SV4iGY4kV4c)

Votre requête est maintenant allée au serveur et la réponse viendra. Cette requête sera à nouveau en pause, mais cette fois elle revient à Firefox et vous pouvez également changer la réponse.

#### Le moment de briller

Maintenant, changez ce `soldOut` en `true` et appuyez sur ce bouton de reprise pour voir la magie (hack *tousse*) se produire. Votre frontend recevra la réponse modifiée, et il devrait vous montrer la bannière "L'article est en rupture de stock" que vous avez attendue toute votre vie.

Vous pouvez changer tout dans une réponse et une requête. Littéralement, de l'en-tête au corps, aux cookies, et tout le reste.

#### Interface en ligne de commande (Indisponible sous Windows)

mitmproxy dispose également d'une excellente interface en ligne de commande.

Pour démarrer le serveur proxy dans le CLI, utilisez la commande `mitmproxy --port 9000`   
Ici, `--port` est utilisé pour spécifier le port sur lequel ce serveur doit s'exécuter.

![Image](https://cdn-media-1.freecodecamp.org/images/PF1RM4SN0xGrnG3Jsvn0c2lZBkh6M7VUUEAU)

Vous serez accueilli par ceci. Appuyez sur `?` pour les raccourcis du CLI.

Comme mentionné dans la section de configuration de l'interface web, configurez votre Firefox.

À ce stade, vous devriez pouvoir voir toutes les requêtes/réponses passant par votre serveur proxy.

Pour intercepter une requête, appuyez sur `i` et ajoutez un motif d'URL (_ci-ci est un RegEx_).  
Comme pour l'interface web, mitmproxy intercepte les requêtes deux fois : une fois en allant vers le serveur et à nouveau en revenant du serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/CG4xobVNUKaPuAOpsRUm9lM6MSsCdSUYCVM5)

J'ai ajouté un motif `localhost`. Il a intercepté une requête. Appuyez sur Entrée pour voir cette requête en pause.

![Image](https://cdn-media-1.freecodecamp.org/images/1-KCSXWShgkPmclY2STf-K18Gz6AluaiLcpz)

Pour modifier, appuyez sur `e` et vous aurez des options pour modifier ce que vous voulez.

Appuyez sur `a` pour laisser la requête aller au serveur. Vous pouvez maintenant voir la réponse et la modifier également.

![Image](https://cdn-media-1.freecodecamp.org/images/DqjTzo4eurC2mgio-Ps8VQQbA7ceeLbVx67E)

Ci-dessus se trouve l'onglet de réponse. Appuyez sur `e` et vous pouvez modifier la réponse. Appuyez à nouveau sur `a` pour laisser la réponse aller à Firefox.

Ce sont quelques commandes de base que vous pouvez utiliser. Pour plus d'aide, appuyez sur `?`.

Maintenant, piratez votre chemin dans le développement logiciel comme :

![Image](https://cdn-media-1.freecodecamp.org/images/Nym7LMk-MAW-IQ0c1XXziqPXcR4tfoDojEEN)

Pour plus d'informations sur mitmproxy, consultez la documentation [ici](https://mitmproxy.org/).

#### Si vous avez aimé cet article, veuillez cliquer sur le bouton ? et partager pour aider les autres à le trouver ! N'hésitez pas à laisser un commentaire ci-dessous.

_Publié à l'origine sur [www.plightofbyte.com](https://www.plightofbyte.com/tools/2018/03/13/make-believe-using-proxy/) le 13 mars 2018._
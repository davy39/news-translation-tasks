---
title: Ce que j'ai appris en piratant le jeu de football de Facebook Messenger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-25T17:40:49.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-hacking-facebook-messenger-soccer-game-3c882ea8537d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hPTxPQeHPxLnPBOg8ryWpQ.jpeg
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Ce que j'ai appris en piratant le jeu de football de Facebook Messenger
seo_desc: 'By Flavio De Stefano

  Recently, during last European Football Championship, Facebook introduced a little
  game in the Messenger app that makes you lose hours and hours despite its simplicity.

  If you didn’t notice it, read this article on Mashable.

  I ha...'
---

Par Flavio De Stefano

Récemment, lors du dernier Championnat d'Europe de football, Facebook a introduit un petit jeu dans l'application Messenger qui vous fait perdre des heures et des heures malgré sa simplicité.

Si vous ne l'avez pas remarqué, lisez [cet article](https://mashable.com/2016/06/15/facebook-messenger-soccer-game-how-to/#fmGutFmQ3Oqx) sur Mashable.

Je dois admettre... Je suis vraiment nul à ce jeu, donc mon meilleur score était **9**_._

Mais, en tant que développeur, la meilleure chose que je pouvais faire était de battre mes amis en piratant le jeu.

_Je pensais vraiment que ce serait simple._

#### La première méthode : Écouter les requêtes HTTP(s)

Lors du développement d'applications, vous réalisez immédiatement que vous avez besoin d'un outil de débogage HTTP pour analyser le trafic entrant/sortant de vos API.

[**Charles**](https://www.charlesproxy.com/) est le meilleur outil que j'ai trouvé pour accomplir cette tâche. Il a une interface très intuitive et vous pouvez facilement l'utiliser à des fins de débogage et d'ingénierie inverse.

Cela aurait dû s'arrêter à ce stade : j'aurais dû analyser l'API que l'application Facebook utilisait et simplement la rejouer avec CURL tout en modifiant les données et le score envoyés au serveur.

Bien sûr, les appels API sont en HTTPS, donc ils sont chiffrés... mais _Charles peut être utilisé comme un proxy HTTPS homme-du-milieu_, vous permettant de voir en texte clair la communication entre le navigateur web et le serveur web SSL_._

![Image](https://cdn-media-1.freecodecamp.org/images/1*rHRhqfl0hZSYHdEsrJLF_A.png)
_Charles agissant comme un proxy — avec des requêtes échouées_

Parfait ! J'ai donc installé le certificat racine Charles sur l'iPhone et j'ai essayé d'inspecter le trafic. Mais toutes les requêtes HTTP vers les serveurs Facebook ont été refusées d'emblée lors de la phase de poignée de main SSL.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mjd0P2T-huqFhck7Ii3alA.gif)
_SSL - image courtesy of cisco.com_

En faisant quelques recherches, j'ai découvert que certaines applications d'entreprises comme Facebook et Google utilisent une couche de sécurité supplémentaire pour s'assurer que le certificat fourni par le serveur distant est celui qui est attendu. Cette technique est appelée **Certificate Pinning.**

Vous pouvez facilement faire cela en incluant la clé publique du certificat du serveur distant dans l'application, afin qu'il soit facile de valider l'identité du client pour chaque requête HTTPS.

Cette technique invalide l'[attaque de l'homme du milieu (MITM)](https://en.wikipedia.org/wiki/Man-in-the-middle_attack).

Bon travail Facebook ! Mais... (souvenez-vous, il y a toujours un mais) il existe un moyen de désactiver le **SSL certificate pinning** en utilisant quelques ajustements système disponibles uniquement sur un appareil jailbreaké.

#### La première méthode (améliorée) : Jailbreaker un appareil et installer iOS SSL Kill Switch

Mon iPhone fonctionne actuellement sous iOS 9.x, donc au moment de la rédaction de cet article, il était impossible de le jailbreaker. J'ai donc pris un ancien iPad mini fonctionnant sous iOS 8.3.x et je l'ai facilement jailbreaké en utilisant l'outil [TaiG](http://www.taig.com/en/).

En cherchant sur le web, j'ai trouvé [SSL Kill Switch 2](https://github.com/nabla-c0d3/ssl-kill-switch2), un outil Blackbox pour désactiver la validation des certificats SSL dans les applications iOS et OS X.

Une fois chargé dans une application iOS ou OS X, SSL Kill Switch 2 patch des fonctions SSL de bas niveau spécifiques dans l'API Secure Transport afin de _remplacer et désactiver la validation des certificats par défaut du système ainsi que tout type de validation de certificat personnalisée_ (comme le certificate pinning).

Le SSL Kill Switch utilise [MobileSubstrate](http://iphonedevwiki.net/index.php/MobileSubstrate) pour patcher des fonctions système comme l'[API Secure Transport](https://developer.apple.com/library/ios/DOCUMENTATION/Security/Reference/secureTransportRef/Reference/reference.html). Ce sont les implémentations TLS de plus bas niveau sur iOS.

Cela signifie que la désactivation de la validation des certificats SSL dans l'API Secure Transport devrait affecter la plupart (sinon toutes) des API réseau disponibles dans le framework iOS.

S'il vous plaît, faites-vous une faveur et suivez [ce blog](https://nabla-c0d3.github.io/) qui couvre tous ces concepts.

J'ai donc connecté l'iPad en utilisant SSH et installé le package :

```
wget https://github.com/nabla-c0d3/ssl-kill-switch2/releases/download/0.10/com.nablac0d3.SSLKillSwitch2_0.10.deb --no-check-certificatedpkg -i com.nablac0d3.SSLKillSwitch2_0.10.debkillall -HUP SpringBoard
```

Une fois redémarré, je m'attendais à voir le trafic en clair, mais c'était une vision optimiste : _j'ai obtenu les mêmes erreurs._

J'ai essayé cette méthode pendant une autre heure. J'ai lu quelque part que Facebook et Twitter utilisent le protocole SPDY pour leurs appels API, et cela pourrait être un problème pour Charles. J'ai donc installé un autre tweak qui (théoriquement) désactivait le protocole SPDY, mais cela n'a pas fonctionné.

_Affamé._

En regardant les problèmes du projet, j'ai remarqué que quelqu'un d'autre avait le même problème ([https://github.com/nabla-c0d3/ssl-kill-switch2/issues/13](https://github.com/nabla-c0d3/ssl-kill-switch2/issues/13)), sans résolution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UlNOgv5rpOId_yvnggV3hQ.png)

_Pause._

#### La deuxième méthode : Simuler des événements tactiles dans l'application

J'ai réalisé qu'il existe de nombreuses triches de jeu qui utilisent une approche "humaine" : _simuler des événements tactiles_ (l'un des jeux les plus populaires sur lesquels de nombreuses triches de jeu utilisent cette stratégie est Clash of Clans).

En parcourant le web pour un outil qui automatise ces opérations, j'ai trouvé ce tweak génial - [AutoTouch](https://autotouch.net/). Il peut enregistrer des événements tactiles humains et stocker les données dans un script LUA. Vous pouvez ensuite modifier ce script produit et simuler ce que vous voulez n'importe où sur votre appareil.

Une fois installé avec [Cydia](https://cydia.saurik.com/), j'ai sauvegardé une capture d'écran BMP de l'application Messenger avec la balle visible et obtenu les coordonnées de l'endroit où cliquer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*inmRf5q2zYXB4IAMZYvwrw.png)
_Capture d'écran réalisée pour obtenir les coordonnées_

Ce que je pensais, c'est qu'en cliquant _exactement_ au centre de l'axe X de la balle, je n'avais qu'à simuler des événements tactiles répétitifs aux mêmes coordonnées et ensuite arrêter le script lorsque j'avais un score qui me satisfaisait.

Voici ce que j'ai écrit pour accomplir cet objectif :

```
adaptResolution(768, 1024);adaptOrientation(ORIENTATION_TYPE.PORTRAIT);
```

```
for i=1,2000 do
```

```
  touchDown(1, 544, 954);  usleep(66000);  touchUp(1, 544, 954);
```

```
  usleep(10000);
```

```
end
```

Non, cela n'a pas fonctionné.

Probablement, les développeurs de Facebook ont introduit une erreur aléatoire sur les coordonnées tactiles pour mieux simuler le jeu, ou pour empêcher ces types de scripts.

_Ou, peut-être que j'ai simplement cliqué sur le mauvais pixel._

Pour une deuxième chance, j'ai essayé de simuler plusieurs clics dans une zone plus grande, mais sans succès. Parfois, j'ai simulé tellement d'événements tactiles que le Springboard _a simplement planté_ à cause d'erreurs de mémoire_._

Au lieu de cliquer sur les mêmes coordonnées à chaque fois, j'ai essayé une meilleure approche.

En lisant la [documentation](https://autotouch.net/server/doc/en.html) d'AutoTouch, j'ai trouvé les deux méthodes suivantes :

* findColor (color, count, region) - Recherche les coordonnées des points de pixel correspondant à la couleur spécifiée sur l'écran actuel.
* getColor (x, y) - Obtient la valeur de couleur du point de pixel de la coordonnée spécifiée sur l'écran actuel.

L'idée était de trouver une couleur unique à l'intérieur de la balle, et d'utiliser la méthode _findColor_ pour obtenir les coordonnées de la balle à ce moment-là, afin de simuler un événement tactile.

```
adaptResolution(768, 1024);adaptOrientation(ORIENTATION_TYPE.PORTRAIT);
```

```
local c = getColor(544, 954);
```

```
for i=1,2000 do  local r = findColor(c, 0, {400, 500, 768, 1024});
```

```
  for i, v in pairs(r) do    touchDown(1, v[1], v[2]);    usleep(66000);    touchUp(1, v[1], v[2]);    usleep(10000);  end
```

```
end
```

Je ne sais pas pourquoi, mais cela n'a tout simplement pas fonctionné. Peut-être que _findColor_ est trop lent pour intercepter la balle, ce qui rend le script inutile.

#### La troisième méthode : Reverse engineer l'application

Je n'ai pas de bonnes compétences natives en Objective C, mais je me souviens (quand je jouais avec le jailbreak il y a ~4 ans) qu'il y avait un outil de [Saurik](https://twitter.com/saurik?lang=en) qui pouvait s'injecter dans les processus iOS.

Il est publié avec Cydia et s'appelait [Cycript](http://www.cycript.org/). _Il permettait aux développeurs d'explorer et de modifier les applications en cours d'exécution sur iOS, en injectant du code à l'exécution._

J'ai lu quelques tutoriels de base sur son utilisation, et après quelques difficultés, j'ai décidé de suivre cette (autre) voie.

Une fois connecté via SSH à votre appareil iOS, vous pouvez facilement vous attacher à un processus en tapant simplement :

```
cycript -p Messenger
```

J'ai essayé d'inspecter quelques classes UI de base comme _UIApp_, mais je n'ai rien trouvé d'intéressant. J'ai ensuite fait un **class dump** complet, en le filtrant pour le mot-clé **soccer.**

```
var C = Object.keys(ObjectiveC.classes);var soccer_classes = []; for (var i = 0; i < C.length; i++)  C[i].match(/soccer/i) && soccer_classes.push( C[i] );
```

C'était un processus lent.

J'ai [découvert](https://www.reddit.com/r/programming/comments/3h52yk/someone_discovered_that_the_facebook_ios/) que Facebook Messenger a un très grand nombre de classes.

Mais, au final, j'ai obtenu une petite liste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xiOhf1t00RNyXa_o8m7Hnw.png)
_Sortie du script_

Une fois que j'ai obtenu les noms des classes, j'ai utilisé un script pour imprimer toutes les méthodes de la classe, et, en inspectant la classe **_MNSoccerGame_**, les méthodes résultantes étaient :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VnA--gnGj5wO3ZcF4C8EUQ.png)
_Le dump des méthodes de la classe MNSoccerGame_

> Note : Je ne comprends toujours pas ce qu'est la méthode _wasCheatDetected._

Maintenant que j'avais une liste complète des méthodes de la classe, j'ai décidé de remplacer la méthode __setScore_, en espérant que les autres méthodes ne le remarqueraient pas.

Pour ce faire, j'ai utilisé **MobileSubstrate** et sa méthode **MS.hookMessage**.

```
@import com.saurik.substrate.MS; 
```

```
var _setScore_pointer = {}; MS.hookMessage(MNSoccerGame, @selector(_setScore:), function(arg0) {  return _setScore_pointer->call(this, 9999); }, _setScore_pointer);
```

Maintenant, vous pouvez simplement jouer, **perdre**, et **battre un nouveau record.**

#### Ce que j'ai appris

Ne vous arrêtez jamais. Essayez toujours et découvrez de nouvelles façons d'accomplir la même chose. Je sais, ce n'est qu'un jeu, mais si vous traitez le problème que vous essayez de résoudre comme un défi, vous obtiendrez bien plus que la satisfaction de battre vos amis.
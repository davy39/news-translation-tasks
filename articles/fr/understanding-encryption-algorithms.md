---
title: Algorithmes de chiffrement expliqués avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-01T00:16:00.000Z'
originalURL: https://freecodecamp.org/news/understanding-encryption-algorithms
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b58740569d1a4ca2b3f.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: encryption
  slug: encryption
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: technology
  slug: technology
seo_title: Algorithmes de chiffrement expliqués avec des exemples
seo_desc: "By Megan Kaczanowski\nCryptography, at its most basic, is the science of\
  \ using codes and ciphers to protect messages. \nEncryption is encoding messages\
  \ with the intent of only allowing the intended recipient to understand the meaning\
  \ of the message. It..."
---

Par Megan Kaczanowski

La cryptographie, dans sa forme la plus basique, est la science de l'utilisation de codes et de chiffres pour protéger les messages. 

Le chiffrement consiste à coder des messages dans le but de permettre uniquement au destinataire prévu de comprendre le sens du message. Il s'agit d'une fonction à double sens (vous devez pouvoir annuler le brouillage que vous avez appliqué au message). Cela est conçu pour protéger les données en transit. 

Si vous cherchez une introduction générale sur la différence entre les algorithmes symétriques et asymétriques et une vue d'ensemble de ce qu'est le chiffrement, commencez [ici](https://medium.com/swlh/how-to-send-secret-messages-1c106250b884). Cet article couvrira principalement deux des algorithmes de chiffrement les plus couramment utilisés. 

En tant qu'introduction générale, il y avait un problème majeur avec les algorithmes symétriques lorsqu'ils ont été créés pour la première fois - ils ne fonctionnaient efficacement que si les deux parties connaissaient déjà le secret partagé. Si ce n'était pas le cas, échanger une clé de manière sécurisée sans qu'un tiers n'écoute était extrêmement difficile. 

Et si un tiers obtenait la clé, il était très facile pour lui de briser le chiffrement, ce qui défaites le but de la communication sécurisée. 

Diffie-Hellman a résolu ce problème en permettant à des inconnus d'échanger des informations sur des canaux publics qui peuvent être utilisées pour former une clé partagée. Une clé partagée est difficile à craquer, même si toutes les communications sont surveillées.

## Comment fonctionne Diffie-Hellman ?

Diffie-Hellman est ce qu'on appelle un protocole d'échange de clés. C'est l'utilisation principale de Diffie-Hellman, bien qu'il puisse également être utilisé pour le chiffrement (il ne l'est généralement pas, car il est plus efficace d'utiliser D-H pour échanger des clés, puis de passer à un chiffrement symétrique (significativement plus rapide) pour la transmission de données). 

La manière dont cela fonctionne est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screen-Shot-2019-10-04-at-5.45.13-PM.png)
_[https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange#/media/File:Diffie-Hellman_Key_Exchange.svg](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#/media/File:Diffie-Hellman_Key_Exchange.svg)_

En gros, il y a deux parties, Alice et Bob, qui conviennent d'une couleur de départ (arbitraire mais doit être différente à chaque fois). Ils ont également une couleur secrète qu'ils gardent pour eux. Ils mélangent ensuite cette couleur avec la couleur partagée, ce qui donne deux couleurs différentes. Ils transmettent ensuite cette couleur à l'autre partie, qui la mélange avec sa couleur secrète, ce qui donne la même couleur secrète finale. 

Cela repose sur l'idée qu'il est relativement facile de mélanger deux couleurs ensemble, mais qu'il est très difficile de les séparer pour trouver la couleur secrète. En pratique, cela est fait avec des mathématiques.

Par exemple :

1. Bob et Alice conviennent de deux nombres, un grand nombre premier, p = 29, et une base g = 5
2. Maintenant, Bob choisit un nombre secret, x (x = 4) et fait ce qui suit : X = g^x % p (dans ce cas, % indique le reste. Par exemple, 3%2 est 3/2, où le reste est 1). X = 5 ^4 % 29 = 625 % 29 = 16
3. Alice choisit également un nombre secret, y (y = 8) et fait ce qui suit : Y = g^y % p.  Y = 5 ^ 8 % 29 = 390,625 % 29 = 24
4. Bob envoie X à Alice et Alice envoie Y à Bob.
5. Ensuite, Bob fait ce qui suit : K = Y^x % p, K = 24 ^ 4 % 29 = 331,776 % 29 = 16
6. Alice fait ensuite ce qui suit : K = X^y % p, K = 16 ^ 8 % 29 = 4,294,967,296 % 29 = 16

La chose formidable (*peut-être magique*) à propos de cela, c'est que Bob et Alice ont le même nombre, K, et peuvent maintenant l'utiliser pour communiquer secrètement, car personne d'autre ne connaît K.

La sécurité de ce protocole repose sur quelques éléments :

1. (Fait) Il est relativement facile de générer des nombres premiers, même de grands nombres premiers (comme p).
2. (Fait) L'exponentiation modulaire est facile. En d'autres termes, il est relativement facile de calculer X = g ^ x % p.
3. (Hypothèse basée sur la puissance de calcul actuelle et les mathématiques) L'extraction de racines modulaires sans les facteurs premiers est très difficile. Essentiellement, il est très difficile de trouver K sans connaître x et y, même si vous avez espionné le trafic et pouvez voir p, g, X et Y.

Ainsi, en supposant que cela a été mis en œuvre correctement, il est relativement facile de faire les mathématiques nécessaires pour créer la clé, mais il est extrêmement difficile et chronophage de faire les mathématiques nécessaires pour essayer de briser la clé par force brute. 

Même si un attaquant pouvait compromettre cette clé, Diffie-Hellman permet une parfaite confidentialité persistante.

### Qu'est-ce que la parfaite confidentialité persistante ?

Il s'agit de l'idée que si vous craquez le chiffrement que le serveur utilise pour communiquer maintenant, cela ne signifie pas que toutes les communications que le serveur a jamais effectuées peuvent être lues. 

En d'autres termes, cela ne vous permet de voir que les communications qui sont utilisées maintenant (c'est-à-dire avec cette clé secrète). Puisque chaque ensemble de communications a une clé secrète différente, vous devriez les craquer toutes séparément. 

Cela est possible si chaque session a une clé éphémère différente pour chaque session. Parce que Diffie-Hellman utilise toujours de nouvelles valeurs aléatoires pour chaque session, (générant ainsi de nouvelles clés pour chaque session), il est appelé Diffie Hellman Éphémère (EDH ou DHE). De nombreuses suites de chiffres utilisent cela pour atteindre une parfaite confidentialité persistante.

Comme Diffie-Hellman vous permet d'échanger du matériel clé en texte clair sans vous soucier de compromettre le secret partagé, et que les mathématiques sont trop compliquées pour qu'un attaquant puisse les forcer par brute force, l'attaquant ne peut pas déduire la clé de session (et même s'il le pouvait, l'utilisation de clés différentes et éphémères pour chaque session signifie qu'il ne pourrait espionner que cette session - aucune dans le passé ou le futur). 

La confidentialité persistante est activée avec tout échange de clés Diffie-Hellman, mais seul l'échange de clés éphémères (une clé différente pour chaque session) offre une parfaite confidentialité persistante. 

[Voici un article](https://scotthelme.co.uk/perfect-forward-secrecy/) de Scott Helme qui parle de cela plus en détail et explique comment activer cela sur vos serveurs.

### Quelles sont les limitations de Diffie-Hellman ?

La plus grande limitation de D-H est qu'il ne vérifie pas l'identité. En d'autres termes, n'importe qui peut prétendre être Alice ou Bob et il n'y a aucun mécanisme intégré pour vérifier que leur déclaration est vraie. 

De plus, si la mise en œuvre n'est pas effectuée de manière sécurisée, l'algorithme pourrait être craqué avec suffisamment de ressources dédiées (peu probable, mais possible pour des équipes académiques ou des acteurs étatiques). 

Par exemple, cela pourrait se produire si le générateur de nombres aléatoires n'est pas fourni avec une entropie adéquate pour soutenir la force souhaitée - en d'autres termes, parce que les nombres générés par ordinateur ne sont jamais vraiment aléatoires, le degré auquel vous avez artificiellement injecté de l'incertitude compte pour la force de votre mise en œuvre.

De plus, il y a eu une attaque démontrée en 2015 qui a montré que lorsque les mêmes nombres premiers étaient utilisés par de nombreux serveurs au début de l'échange de clés, la sécurité globale de Diffie-Hellman était inférieure à ce qui était attendu. 

Essentiellement, un attaquant pourrait simplement pré-calculer l'attaque contre ce nombre premier, ce qui rend plus facile la compromission des sessions pour tout serveur qui a utilisé ce nombre premier. 

Cela s'est produit parce que des millions de serveurs utilisaient les mêmes nombres premiers pour les échanges de clés. Le pré-calcul de ce type d'attaque nécessite toujours des ressources de niveau académique ou étatique et est peu susceptible d'impacter la grande majorité des gens. 

Cependant, heureusement pour ceux qui doivent se soucier des attaquants étatiques, il existe une autre façon d'atteindre l'échange de clés DH en utilisant la cryptographie à courbe elliptique (ECDHE). Cela dépasse le cadre de cet article, mais si vous êtes intéressé à en apprendre plus sur les mathématiques derrière cet échange, consultez [cet article](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy).

Pour un examen plus détaillé des faiblesses de DH, consultez [ce livre blanc](https://cert.europa.eu/static/WhitePapers/CERT-EU-SWP_16-002_Weaknesses%20in%20Diffie-Hellman%20Key%20v1_0.pdf) et [ce site web.](https://weakdh.org/)

## RSA

RSA est nommé d'après ses créateurs - Rivest, Shamir, Adleman - et c'est une manière de générer des clés publiques et privées. 

Techniquement, il existe deux algorithmes RSA (l'un utilisé pour les signatures numériques, et l'autre utilisé pour le chiffrement asymétrique.) - cet article couvre l'algorithme de chiffrement asymétrique. 

Cela permet l'échange de clés - vous attribuez d'abord à chaque partie de la transaction des clés publiques/privées, puis vous générez une clé symétrique, et enfin, vous utilisez les paires de clés publiques/privées pour communiquer de manière sécurisée la clé symétrique partagée. 

Parce que le chiffrement asymétrique est généralement plus lent que le chiffrement symétrique, et ne s'adapte pas aussi bien, l'utilisation du chiffrement asymétrique pour échanger de manière sécurisée des clés symétriques est très courante.

Alors, comment cela fonctionne-t-il ?

1. Choisissez 2 très grands nombres premiers (au moins 512 bits, ou 155 chiffres décimaux chacun), x et y (ces nombres doivent être secrets et choisis aléatoirement)
2. Trouvez le produit, c'est-à-dire z = x*y
3. Sélectionnez un entier public impair, e, entre 3 et n - 1, et qui n'a pas de facteurs communs (autres que 1) avec (x-1)(y-1) (donc il est relativement premier avec x - 1 et y - 1).
4. Trouvez le plus petit multiple commun de x - 1 et y - 1, et appelez-le L.
5. Calculez l'exposant privé, d, à partir de x, y, et e. de = 1 % L. d est l'inverse de e % L (vous savez qu'un inverse existe parce que e est relativement premier avec z - 1 et y - 1). Ce système fonctionne parce que p = (p ^ e) ^d % z.
6. Produisez (z, e) comme clé publique et (z, d) comme clé privée.

Maintenant, si Bob souhaite envoyer un message à Alice, il génère le texte chiffré (C) à partir du texte en clair (P) en utilisant cette formule :

C = P^e % z

Pour déchiffrer ce message, Alice calcule ce qui suit :

P = C^d % z

La relation entre d et e garantit que les fonctions de chiffrement et de déchiffrement sont inverses. Cela signifie que la fonction de déchiffrement est capable de récupérer avec succès le message original, et qu'il est assez difficile de récupérer le message original sans la clé privée (z, d) (ou les facteurs premiers x et y). 

Cela signifie également que vous pouvez rendre z et e publics sans compromettre la sécurité du système, ce qui facilite la communication avec d'autres personnes avec lesquelles vous n'avez pas déjà une clé secrète partagée.

Vous pouvez également utiliser les opérations en sens inverse pour obtenir une signature numérique du message. D'abord, vous utilisez l'opération de déchiffrement sur le texte en clair. Par exemple, s = SIGNATURE(p) = p ^ d % z.

Ensuite, le destinataire peut vérifier la signature numérique en appliquant la fonction de chiffrement et en comparant le résultat avec le message. Par exemple, m = VERIFY(s) = S ^ e % z.

Souvent, lorsque cela est fait, le texte en clair est un hachage du message, ce qui signifie que vous pouvez signer le message (quelle que soit sa longueur) avec une seule exponentiation.

La sécurité du système est basée sur quelques éléments : 

1. (Fait) Il est relativement facile de générer des nombres premiers, même de grands nombres premiers (comme x et y).
2. (Fait) La multiplication est facile. Il est très facile de trouver z.
3. (Hypothèse basée sur les mathématiques actuelles) La factorisation est difficile. Étant donné z, il est relativement difficile de récupérer x et y. C'est faisable, mais cela prend du temps et c'est coûteux.   
  
[Une estimation](http://mathaware.org/mam/06/Kaliski.pdf) dit que la récupération des facteurs premiers d'un nombre de 1024 bits prendrait un an sur une machine coûtant 10 millions de dollars. Doubler la taille augmenterait exponentiellement la quantité de travail nécessaire (plusieurs milliards de fois plus de travail).   
  
À mesure que la technologie continue de progresser, ces coûts (et le travail requis) diminueront, mais à ce stade, ce type de chiffrement, correctement mis en œuvre, est une source peu probable de compromission.   
  
Généralement, les seuls pirates avec ce type d'argent et de dédication pour une seule cible sont les États-nations. De plus, s'il y a une manière plus facile de compromettre un système (voir ci-dessous), c'est probablement une meilleure option.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screen-Shot-2019-10-05-at-11.18.45-AM.png)
_[https://xkcd.com/538/](https://xkcd.com/538/)_

4. (Fait) L'exponentiation modulaire est facile. En d'autres termes, il est relativement facile de calculer c = p ^ e % z.

5. (Fait) L'extraction de racines modulaires - inverser le processus ci-dessus - est facile si vous avez les facteurs premiers (si vous avez z, c, e, et les facteurs premiers x et y, il est facile de trouver p tel que c = p ^ e % z).

6. (Hypothèse basée sur la puissance de calcul actuelle et les mathématiques) L'extraction de racines modulaires sans les facteurs premiers est très difficile (si vous avez z, c, e, mais pas x et y, il est relativement difficile de trouver p tel que c = p ^ e % z, en particulier si a est suffisamment grand).

Vous souhaitez en apprendre plus sur les mathématiques de la part de personnes beaucoup plus intelligentes ? Consultez [cet article.](http://mathaware.org/mam/06/Kaliski.pdf)

## Très bien, lequel est le meilleur ?

Cela dépend de votre cas d'utilisation. Il y a quelques différences entre les deux algorithmes - d'abord, la parfaite confidentialité persistante (PFS), dont nous avons parlé plus tôt dans le contexte de Diffie-Hellman. Bien que techniquement vous _pourriez_ générer des paires de clés RSA éphémères, et fournir une parfaite confidentialité persistante avec RSA, le coût computationnel est beaucoup plus élevé que pour Diffie-Hellman - ce qui signifie que Diffie-Hellman est un meilleur choix pour les implémentations SSL/TLS où vous voulez une parfaite confidentialité persistante.  

Bien qu'il y ait quelques différences de performance entre les deux algorithmes (en termes de travail requis par le serveur), les différences de performance ne sont généralement pas assez grandes pour faire une différence lors du choix de l'un plutôt que de l'autre. 

Au lieu de cela, en général, la considération principale pour déterminer lequel est le meilleur dépend de celui qui est le plus soutenu pour votre cas d'utilisation (par exemple, lors de la mise en œuvre de SSL, vous voudrez Diffie Hellman en raison de la parfaite confidentialité persistante) ou de celui qui est le plus populaire ou accepté comme la norme dans l'industrie. 

Par exemple, bien que Diffie-Hellman ait été approuvé par le gouvernement américain et soutenu par un organisme institutionnel, la norme n'a pas été publiée - alors que RSA (standardisé par une organisation privée) a fourni une norme gratuite, ce qui signifie que RSA est devenu très populaire parmi les organisations privées. 

Si vous êtes intéressé à lire plus, il y a un excellent fil de discussion [ici](https://security.stackexchange.com/questions/35471/is-there-any-particular-reason-to-use-diffie-hellman-over-rsa-for-key-exchange/35472#35472) sur les différences.

Intéressé à apprendre comment les pirates utilisent les attaques cryptographiques ? Essayez [ce](https://cryptopals.com/) ensemble de défis de Cryptopals.

%[https://twitter.com/preinheimer/status/841273046317060105?lang=en]
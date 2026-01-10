---
title: 'Sécurité Web : une introduction à HTTP'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T19:07:49.000Z'
originalURL: https://freecodecamp.org/news/web-security-an-introduction-to-http-5fa07140f9b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OmYKGxDL44CyvPgdQZcWqQ.jpeg
tags:
- name: https
  slug: https
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Security
  slug: web-security
seo_title: 'Sécurité Web : une introduction à HTTP'
seo_desc: 'By Alex Nadalin

  This is part 2 of a series on web security: part 1 was “Understanding The Browser”

  HTTP is a thing of beauty: a protocol that has survived longer than 20 years without
  changing much.

  As we’ve seen in the previous article, browsers int...'
---

Par Alex Nadalin

_Ceci est la partie 2 d'une série sur la sécurité web : la partie 1 était « [Comprendre le navigateur](https://medium.freecodecamp.org/web-application-security-understanding-the-browser-5305ed2f1dac) »_

HTTP est une chose de beauté : un protocole qui a survécu plus de 20 ans sans changer beaucoup.

Comme nous l'avons vu dans l'[article précédent](https://medium.freecodecamp.org/web-application-security-understanding-the-browser-5305ed2f1dac), les navigateurs interagissent avec les applications web via le protocole HTTP, et c'est la principale raison pour laquelle nous approfondissons le sujet. Si les utilisateurs entraient les détails de leur carte de crédit sur un site web et qu'un attaquant pouvait intercepter les données avant qu'elles n'atteignent le serveur, nous serions définitivement dans l'embarras.

Comprendre comment HTTP fonctionne, comment nous pouvons sécuriser la communication entre les clients et les serveurs, et quelles fonctionnalités liées à la sécurité le protocole offre est la première étape vers l'amélioration de notre posture de sécurité.

Lorsque nous parlons de HTTP, cependant, nous devons toujours distinguer entre la sémantique et l'implémentation technique, car ce sont deux aspects très différents de la façon dont HTTP fonctionne.

La différence clé entre les deux peut être expliquée avec une analogie très simple : il y a 20 ans, les gens se souciaient de leurs proches autant qu'aujourd'hui, même si la façon dont ils interagissent a considérablement changé. Nos parents prendraient probablement leur voiture et se rendraient chez leur sœur pour rattraper le temps perdu et passer du temps en famille.

Au lieu de cela, de nos jours, il est plus courant d'envoyer un message sur WhatsApp, de passer un appel téléphonique ou d'utiliser un groupe Facebook, des choses qui n'étaient pas possibles auparavant. Cela ne signifie pas que les gens communiquent ou se soucient plus ou moins, mais simplement que la façon dont ils interagissent a changé.

HTTP n'est pas différent : la sémantique derrière le protocole n'a pas beaucoup changé, tandis que l'implémentation technique de la façon dont les clients et les serveurs se parlent a été optimisée au fil des ans. Si vous regardez une requête HTTP de 1996, elle ressemblera beaucoup à celles que nous avons vues dans l'[article précédent](https://medium.freecodecamp.org/web-application-security-understanding-the-browser-5305ed2f1dac), même si la façon dont ces paquets traversent le réseau est très différente.

#### Aperçu

Comme nous l'avons vu précédemment, HTTP suit un modèle requête/réponse, où un client connecté au serveur envoie une requête, et le serveur y répond.

Un message HTTP (qu'il s'agisse d'une requête ou d'une réponse) contient plusieurs parties :

* « première ligne »
* en-têtes
* corps

Dans une requête, la première ligne indique le verbe utilisé par le client, le chemin de la ressource qu'il souhaite ainsi que la version du protocole qu'il va utiliser :

```
GET /players/lebron-james HTTP/1.1
```

Dans ce cas, le client essaie d'obtenir (`GET`) la ressource à `/players/lebron-james` via la version `1.1` du protocole - rien de difficile à comprendre.

Après la première ligne, HTTP nous permet d'ajouter des métadonnées au message via des en-têtes, qui prennent la forme de paires clé-valeur, séparées par un deux-points :

```
GET /players/lebron-james HTTP/1.1Host: nba.comAccept: */*Coolness: 9000
```

Dans cette requête, par exemple, le client a attaché 3 en-têtes supplémentaires à la requête : `Host`, `Accept` et `Coolness`.

Attendez, `Coolness` ?!?!

Les en-têtes n'ont pas à utiliser des noms spécifiques et réservés, mais il est généralement recommandé de s'appuyer sur ceux standardisés par la spécification HTTP : plus vous vous écartez des standards, moins l'autre partie dans l'échange vous comprendra.

`Cache-Control` est, par exemple, un en-tête utilisé pour définir si (et comment) une réponse est mise en cache : la plupart des proxies et des proxies inverses le comprennent car ils suivent la spécification HTTP à la lettre. Si vous deviez renommer votre en-tête `Cache-Control` en `Awesome-Cache-Control`, les proxies n'auraient aucune idée de la façon de mettre en cache la réponse, car ils ne sont pas conçus pour suivre la spécification que vous venez de créer.

Parfois, cependant, il peut être judicieux d'inclure un en-tête « personnalisé » dans le message, car vous pourriez vouloir ajouter des métadonnées qui ne font pas vraiment partie de la spécification HTTP : un serveur pourrait décider d'inclure des informations techniques dans sa réponse, afin que le client puisse, en même temps, exécuter des requêtes et obtenir des informations importantes concernant l'état du serveur qui répond :

```
...X-Cpu-Usage: 40%X-Memory-Available: 1%...
```

Lors de l'utilisation d'en-têtes personnalisés, il est toujours préférable de les préfixer avec une clé afin qu'ils n'entrent pas en conflit avec d'autres en-têtes qui pourraient devenir standard à l'avenir : historiquement, cela a bien fonctionné jusqu'à ce que tout le monde commence à utiliser des préfixes « non standard » `X` qui, à leur tour, sont devenus la norme. Les en-têtes `X-Forwarded-For` et `X-Forwarded-Proto` sont des exemples d'en-têtes personnalisés qui sont [largement utilisés et compris par les équilibreurs de charge et les proxies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#Proxies), même s'ils [ne faisaient pas partie de la norme HTTP](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).

Si vous devez ajouter votre propre en-tête personnalisé, de nos jours, il est généralement préférable d'utiliser un préfixe fourni par un fournisseur, tel que `Acme-Custom-Header` ou `A-Custom-Header`.

Après les en-têtes, une requête peut contenir un corps, qui est séparé des en-têtes par une ligne vide :

```
POST /players/lebron-james/comments HTTP/1.1Host: nba.comAccept: */*Coolness: 9000
```

```
Best Player Ever
```

Notre requête est complète : première ligne (informations de localisation et de protocole), en-têtes et corps. Notez que le corps est complètement facultatif et, dans la plupart des cas, il n'est utilisé que lorsque nous voulons envoyer des données au serveur - c'est pourquoi l'exemple ci-dessus utilise le verbe `POST`.

Une réponse n'est pas très différente :

```
HTTP/1.1 200 OKContent-Type: application/jsonCache-Control: private, max-age=3600
```

```
{"name": "Lebron James", "birthplace": "Akron, Ohio", ...}
```

La première information que la réponse annonce est la version du protocole qu'elle utilise, ainsi que le statut de cette réponse. Les en-têtes suivent et, si nécessaire, un saut de ligne suivi du corps.

Comme mentionné, le protocole a subi de nombreuses révisions et a ajouté des fonctionnalités au fil du temps (nouveaux en-têtes, codes de statut, etc.), mais la structure sous-jacente n'a pas beaucoup changé (première ligne, en-têtes et corps). Ce qui a vraiment changé, c'est la façon dont les clients et les serveurs échangent ces messages - examinons cela de plus près.

### HTTP vs HTTPS vs H2

HTTP a connu 2 changements sémantiques considérables : `HTTP/1.0` et `HTTP/1.1`.

« Où sont HTTPS et [HTTP2](https://httpwg.org/specs/rfc7540.html) ? », demandez-vous.

HTTPS et HTTP2 (abrévié en H2) sont davantage des changements techniques, car ils ont introduit de nouvelles façons de livrer des messages sur Internet, sans affecter lourdement la sémantique du protocole.

HTTPS est une extension « sécurisée » de [HTTP](http:///) et implique l'établissement d'un secret commun entre un client et un serveur, en s'assurant que nous communiquons avec la bonne partie et en chiffrant les messages qui sont échangés avec le secret commun (plus sur cela plus tard). Alors que HTTPS visait à améliorer la sécurité du protocole HTTP, H2 était orienté vers l'apport de la vitesse de la lumière.

H2 utilise des messages binaires plutôt que des messages en texte brut, prend en charge le multiplexage, utilise l'algorithme HPACK pour compresser les en-têtes... en bref, H2 est un boost de performance pour HTTP/1.1.

Les propriétaires de sites web étaient réticents à passer à HTTPS car cela impliquait des allers-retours supplémentaires entre le client et le serveur (comme mentionné, un secret commun doit être établi entre les 2 parties), ralentissant ainsi l'expérience utilisateur : avec H2, qui est chiffré par défaut, il n'y a plus d'excuses, car des fonctionnalités telles que le multiplexage et le push serveur le rendent [plus performant que le simple HTTP/1.1](https://www.troyhunt.com/i-wanna-go-fast-https-massive-speed-advantage/).

#### HTTPS

HTTPS (_HTTP Secure_) vise à permettre aux clients et aux serveurs de communiquer de manière sécurisée via TLS (Transport Layer Security), le successeur de SSL (Secure Socket Layer).

Le problème que TLS cible est assez simple et peut être illustré avec une métaphore simple : votre moitié vous appelle en plein milieu de la journée, alors que vous êtes en réunion, et vous demande de lui dire le mot de passe de votre compte bancaire en ligne, car ils doivent effectuer un virement bancaire pour s'assurer que les frais de scolarité de votre fils sont payés à temps. Il est crucial que vous le communiquiez _maintenant_, sinon vous risquez que votre enfant soit renvoyé de l'école le lendemain matin.

Vous êtes maintenant confronté à 2 défis :

* **authentification** : vous assurer que vous parlez vraiment à votre moitié, car il pourrait s'agir de quelqu'un qui prétend être eux
* **chiffrement** : communiquer le mot de passe sans que vos collègues puissent le comprendre et le noter

Que faites-vous ? C'est exactement le problème que HTTPS essaie de résoudre.

Pour vérifier à qui vous parlez, HTTPS utilise des certificats à clé publique, qui ne sont rien d'autre que des certificats indiquant l'identité derrière un serveur particulier : lorsque vous vous connectez, via HTTPS, à une adresse IP, le serveur derrière cette adresse vous présentera son certificat pour que vous puissiez vérifier leur identité. En revenant à notre analogie, cela pourrait simplement être vous demandant à votre moitié d'épeler leur numéro de sécurité sociale. Une fois que vous avez vérifié que le numéro est correct, vous gagnez un niveau supplémentaire de confiance.

Cela, cependant, n'empêche pas les « attaquants » d'apprendre le numéro de sécurité sociale de la victime, de voler le smartphone de votre âme sœur et de vous appeler. Comment vérifions-nous l'identité de l'appelant ?

Plutôt que de demander directement à votre moitié d'épeler leur numéro de sécurité sociale, vous passez un coup de fil à votre mère (qui habite juste à côté) et lui demandez d'aller dans votre appartement et de s'assurer que votre moitié épelle leur numéro de sécurité sociale. Cela ajoute un niveau supplémentaire de confiance, car vous ne considérez pas votre mère comme une menace, et vous comptez sur elle pour vérifier l'identité de l'appelant.

En termes HTTPS, votre mère s'appelle une CA, abréviation de Certificate Authority : le travail d'une CA est de vérifier l'identité derrière un serveur particulier, et de délivrer un certificat avec sa propre signature numérique : cela signifie que, lorsque je me connecte à un domaine particulier, je ne me verrai pas présenter un certificat généré par le propriétaire du domaine (appelé [certificat auto-signé](https://en.wikipedia.org/wiki/Self-signed_certificate)), mais plutôt par la CA.

Le travail d'une autorité est de s'assurer qu'elle vérifie l'identité derrière un domaine et délivre un certificat en conséquence : lorsque vous « commandez » un certificat (communément appelé _certificat SSL_, même si de nos jours TLS est utilisé à la place - les noms restent vraiment !), l'autorité pourrait vous passer un coup de fil ou vous demander de changer un paramètre DNS afin de vérifier que vous contrôlez le domaine en question. Une fois le processus de vérification terminé, elle délivrera le certificat que vous pourrez ensuite installer sur vos serveurs web.

Les clients comme les navigateurs se connecteront ensuite à vos serveurs et se verront présenter ce certificat, afin qu'ils puissent vérifier qu'il semble authentique : les navigateurs ont une sorte de « relation » avec les CA, dans le sens où ils gardent une trace d'une liste de CA de confiance afin de vérifier que le certificat est vraiment digne de confiance. Si un certificat n'est pas signé par une autorité de confiance, le navigateur affichera un grand avertissement informatif aux utilisateurs :

![Image](https://cdn-media-1.freecodecamp.org/images/vxE2LWkdevzR-B35YJBqF381QkimQkkZEh5n)

Nous sommes à mi-chemin de notre route vers la sécurisation de la communication entre vous et votre moitié : maintenant que nous avons résolu l'authentification (vérification de l'identité de l'appelant), nous devons nous assurer que nous pouvons communiquer en toute sécurité, sans que d'autres n'écoutent le processus. Comme je l'ai mentionné, vous êtes en plein milieu d'une réunion et devez épeler le mot de passe de votre banque en ligne. Vous devez trouver un moyen de chiffrer votre communication, afin que seul vous et votre âme sœur puissiez comprendre votre conversation.

Vous pouvez le faire en établissant un secret partagé entre vous deux, et en chiffrant les messages via ce secret : vous pourriez, par exemple, décider d'utiliser une variation du [chiffre de César](https://en.wikipedia.org/wiki/Caesar_cipher) basée sur la date de votre mariage.

![Image](https://cdn-media-1.freecodecamp.org/images/HOZnZEwiFLgX3QOGG5LsEFLk8WBo-EZFL3Qw)

Cela fonctionnerait bien si les deux parties ont une relation établie, comme vous et votre âme sœur, car ils peuvent créer un secret basé sur un souvenir partagé que personne d'autre ne connaît. Les navigateurs et les serveurs, cependant, ne peuvent pas utiliser le même type de mécanisme car ils n'ont aucune connaissance préalable l'un de l'autre.

Des variations du [protocole d'échange de clés Diffie-Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) sont utilisées à la place, ce qui garantit que les parties sans connaissance préalable établissent un secret partagé sans que personne d'autre ne puisse le « sniffer ». Cela implique [l'utilisation d'un peu de math](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#Cryptographic_explanation), un exercice laissé au lecteur.

![Image](https://cdn-media-1.freecodecamp.org/images/0Q0PFXLZ4dGndARsBR83txIHHvafpPLSdEx7)

Une fois le secret établi, un client et un serveur peuvent communiquer sans avoir à craindre que quelqu'un puisse intercepter leurs messages. Même si les attaquants le font, ils n'auront pas le secret commun nécessaire pour déchiffrer les messages.

Pour plus d'informations sur HTTPS et Diffie-Hellman, je recommanderais de lire « [How HTTPS secures connections](https://blog.hartleybrody.com/https-certificates/) » par Hartley Brody et « [How does HTTPS actually work?](https://robertheaton.com/2014/03/27/how-does-https-actually-work/) » par Robert Heaton. En outre, « [Nine Algorithms That Changed The Future](https://en.wikipedia.org/wiki/9_Algorithms_That_Changed_the_Future) » a un chapitre incroyable qui explique le chiffrement à clé publique, et je le recommande chaleureusement aux geeks de l'informatique intéressés par les algorithmes ingénieux.

#### HTTPS partout

Vous débattez encore de savoir si vous devez supporter HTTPS sur votre site web ? Je n'ai pas de bonnes nouvelles pour vous : les navigateurs ont commencé à éloigner les utilisateurs des sites web ne supportant pas HTTPS afin de « forcer » les développeurs web à fournir une expérience de navigation entièrement chiffrée.

Derrière le slogan « [_HTTPS everywhere_](https://www.eff.org/https-everywhere) », les navigateurs ont commencé à prendre position contre les connexions non chiffrées - Google a été le premier fournisseur de navigateurs à donner aux développeurs web une date limite en annonçant qu'à partir de Chrome 68 (juillet 2018), il marquerait les sites web HTTP comme « non sécurisés » :

![Image](https://cdn-media-1.freecodecamp.org/images/QzUgTtBZOyCSZAFW6sMDvFvFDyIqNN65QMxW)

Encore plus inquiétant pour les sites web ne tirant pas parti de HTTPS est le fait que, dès que l'utilisateur saisit quelque chose sur la page web, l'étiquette « Non sécurisé » devient rouge - une mesure qui devrait encourager les utilisateurs à réfléchir à deux fois avant d'échanger des données avec des sites web qui ne supportent pas HTTPS.

![Image](https://cdn-media-1.freecodecamp.org/images/Jj16doX7GMJBEyfPGCRfqhGw78cEXsgWy2kn)

Comparez cela à l'apparence d'un site web fonctionnant sur HTTPS et équipé d'un certificat valide :

![Image](https://cdn-media-1.freecodecamp.org/images/xku80KAGhMxG0HRmZICncR3d-MESnpw6PC8B)

En théorie, un site web n'a pas à être sécurisé, mais en pratique, cela effraie les utilisateurs - et à juste titre. À l'époque, lorsque H2 n'était pas une réalité, il aurait pu être judicieux de rester sur le trafic HTTP non chiffré. De nos jours, il n'y a presque aucune raison de le faire. Rejoignez le mouvement _HTTPS everywhere_ et aidez à [rendre le web plus sûr pour les surfeurs](https://www.troyhunt.com/heres-why-your-static-website-needs-https/).

### GET vs POST

Comme nous l'avons vu précédemment, une requête HTTP commence par une première ligne particulière :

Tout d'abord, un client indique au serveur les verbes qu'il utilise pour effectuer la requête : les verbes HTTP courants incluent `GET`, `POST`, `PUT` et `DELETE`, mais la liste pourrait s'allonger avec des verbes moins courants (mais toujours standard) tels que `TRACE`, `OPTIONS`, ou `HEAD`.

En théorie, aucune méthode n'est plus sûre que les autres ; en pratique, ce n'est pas si simple.

Les requêtes `GET` n'incluent généralement pas de corps, donc les paramètres sont inclus dans l'URL (c'est-à-dire `www.example.com/articles?article_id=1`) alors que les requêtes `POST` sont généralement utilisées pour envoyer (« poster ») des données qui sont incluses dans le corps. Une autre différence réside dans les effets secondaires que ces verbes entraînent : `GET` est un verbe idempotent, ce qui signifie que peu importe le nombre de requêtes que vous enverrez, vous ne changerez pas l'état du serveur web. `POST`, en revanche, n'est pas idempotent : pour chaque requête que vous envoyez, vous pourriez changer l'état du serveur (pensez, par exemple, à POSTer un nouveau paiement - maintenant vous comprenez probablement pourquoi les sites vous demandent de ne pas actualiser la page lors de l'exécution d'une transaction).

Pour illustrer une différence importante entre ces méthodes, nous devons examiner les journaux des serveurs web, que vous connaissez peut-être déjà :

```
192.168.99.1 - [192.168.99.1] - - [29/Jul/2018:00:39:47 +0000] "GET /?token=1234 HTTP/1.1" 200 525 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36" 404 0.002 [example-local] 172.17.0.8:9090 525 0.002 200192.168.99.1 - [192.168.99.1] - - [29/Jul/2018:00:40:47 +0000] "GET / HTTP/1.1" 200 525 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36" 393 0.004 [example-local] 172.17.0.8:9090 525 0.004 200192.168.99.1 - [192.168.99.1] - - [29/Jul/2018:00:41:34 +0000] "PUT /users HTTP/1.1" 201 23 "http://example.local/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36" 4878 0.016 [example-local] 172.17.0.8:9090 23 0.016 201
```

Comme vous le voyez, les serveurs web enregistrent le chemin de la requête : cela signifie que, si vous incluez des données sensibles dans votre URL, elles seront divulguées par le serveur web et enregistrées quelque part dans vos journaux - vos secrets seront quelque part en texte brut, quelque chose que nous devons absolument éviter. [Imaginez un attaquant capable d'accéder à l'un de vos anciens fichiers de journal](https://threatpost.com/leaky-backup-spills-157-gb-of-automaker-secrets/134293/), qui pourrait contenir des informations de carte de crédit, des jetons d'accès pour vos services privés, etc. : ce serait un désastre total.

Les serveurs web n'enregistrent pas les en-têtes ou les corps HTTP, car les données à enregistrer seraient trop volumineuses - c'est pourquoi l'envoi d'informations via le corps de la requête, plutôt que via l'URL, est généralement plus sûr. De là, nous pouvons déduire que `POST` (et des méthodes similaires, non idempotentes) est plus sûr que `GET`, même si c'est plus une question de la façon dont les données sont envoyées lors de l'utilisation d'un verbe particulier plutôt qu'un verbe spécifique étant intrinsèquement plus sûr que les autres : si vous deviez inclure des informations sensibles dans le corps d'une requête `GET`, alors vous ne rencontreriez pas plus de problèmes que lors de l'utilisation d'un `POST`, même si l'approche serait considérée comme inhabituelle.

### En les en-têtes HTTP nous faisons confiance

Dans cet article, nous avons examiné HTTP, son évolution et comment son extension sécurisée intègre l'authentification et le chiffrement pour permettre aux clients et aux serveurs de communiquer via un canal plus sûr : ce n'est pas tout ce que HTTP a à offrir en termes de sécurité.

Comme nous le verrons dans le prochain article, les en-têtes de sécurité HTTP offrent un moyen d'améliorer la posture de sécurité de notre application, et le [prochain article](https://medium.com/@alexnadalin/secure-your-web-application-with-these-http-headers-fd66e0367628) est dédié à la compréhension de la façon de tirer parti de ceux-ci.

_Publié à l'origine sur [odino.org](https://odino.org/security-https-perspective/) (22 août 2018)._  
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) - les rants sont les bienvenus!_ ?
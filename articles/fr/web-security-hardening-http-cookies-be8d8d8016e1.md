---
title: 'Sécurité Web : Comment sécuriser vos cookies HTTP'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-02T10:56:06.000Z'
originalURL: https://freecodecamp.org/news/web-security-hardening-http-cookies-be8d8d8016e1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*HgX2neNIxVDbQzxu.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Sécurité Web : Comment sécuriser vos cookies HTTP'
seo_desc: 'By Alex Nadalin

  Note: this is part 4 of a series on web security. Part 3 was Secure your web application
  with these HTTP headers.

  Imagine being a backend developer who needs to implement sessions in an application:
  the first thing that comes to your ...'
---

Par Alex Nadalin

_Note : ceci est la partie 4 d'une série sur la sécurité web. La partie 3 était [Sécurisez votre application web avec ces en-têtes HTTP](https://medium.freecodecamp.org/secure-your-web-application-with-these-http-headers-fd66e0367628)._

Imaginez être un développeur backend qui doit implémenter des _sessions_ dans une application : la première chose qui vous vient à l'esprit est de délivrer un _jeton_ aux clients et de leur demander de envoyer ce jeton avec leurs requêtes ultérieures. À partir de là, vous serez en mesure d'identifier les clients en fonction du jeton inclus dans leur requête.

Les cookies HTTP sont nés pour standardiser ce type de mécanisme à travers les navigateurs. Ils ne sont rien de plus qu'un moyen de stocker des données envoyées par le serveur et de les envoyer avec les requêtes futures. Le serveur envoie un cookie, qui contient de petits morceaux de données. Le navigateur le stocke et l'envoie avec les requêtes futures au même serveur.

Pourquoi devrions-nous nous soucier des cookies d'un point de vue sécurité ? Parce que les données qu'ils contiennent sont, plus souvent qu'autrement, extrêmement sensibles. Les cookies sont généralement utilisés pour stocker des identifiants de session ou des jetons d'accès, le saint graal d'un attaquant. Une fois qu'ils sont exposés ou compromis, les attaquants peuvent usurper l'identité des utilisateurs, ou escalader leurs privilèges sur votre application.

Sécuriser les cookies est l'un des aspects les plus importants lors de l'implémentation de sessions sur le web. Ce chapitre vous donnera donc une meilleure compréhension des cookies, comment les sécuriser et quelles alternatives peuvent être utilisées.

### Qu'y a-t-il derrière un cookie ?

Un serveur peut définir un cookie en utilisant l'en-tête `Set-Cookie` :

```
HTTP/1.1 200 OkSet-Cookie: access_token=1234...
```

Un client stockera alors ces données et les enverra dans les requêtes ultérieures via l'en-tête `Cookie` :

```
GET / HTTP/1.1Host: example.comCookie: access_token=1234...
```

Notez que les serveurs peuvent définir plusieurs cookies à la fois :

```
HTTP/1.1 200 OkSet-Cookie: access_token=1234Set-Cookie: user_id=10...
```

et les clients peuvent stocker plusieurs cookies et les envoyer dans leur requête :

```
GET / HTTP/1.1Host: example.comCookie: access_token=1234; user_id=10...
```

En plus de la simple _clé_ et _valeur_, les cookies peuvent transporter des directives supplémentaires qui limitent leur durée de vie et leur portée.

### Expires

Spécifie quand un cookie doit expirer, afin que les navigateurs ne le stockent pas et ne le transmettent pas indéfiniment. Un exemple clair est un identifiant de session, qui expire généralement après un certain temps. Cette directive est exprimée sous forme de date sous la forme `Date: <day-name>, <day> <month> <year> <`hour>`;:<minute>:<second> GMT`, comme Date: Fri, 24 Aug 2018 04:33:00 GMT. Voici un exemple complet d'un cookie qui expire le 1er janvier 2018 :

```
access_token=1234;Expires=Mon, 1st Jan 2018 00:00:00 GMT
```

### Max-Age

Similaire à la directive `Expires`, `Max-Age` spécifie le nombre de secondes jusqu'à ce que le cookie expire. Un cookie qui doit durer 1 heure ressemblerait à ce qui suit :

```
access_token=1234;Max-Age=3600
```

### Domain

Cette directive définit à quels hôtes le cookie doit être envoyé. Rappelez-vous, les cookies contiennent généralement des données sensibles, il est donc important que les navigateurs ne les divulguent pas à des hôtes non fiables. Un cookie avec la directive `Domain=trusted.example.com` ne sera pas envoyé avec les requêtes à un autre domaine que `trusted.example.com`, pas même le domaine racine `example.com`. Voici un exemple valide d'un cookie limité à un sous-domaine particulier :

```
access_token=1234;Domain=trusted.example.com
```

### Path

Similaire à la directive `Domain`, mais s'applique au chemin de l'URL (`/some/path`). Cette directive empêche un cookie d'être partagé avec des chemins non fiables, comme dans l'exemple suivant :

```
access_token=1234;Path=/trusted/path
```

### Cookies de session et persistants

Lorsque un serveur envoie un cookie sans définir son `Expires` ou `Max-Age`, les navigateurs le traitent comme un _cookie de session_ : plutôt que de deviner sa durée de vie ou d'appliquer des heuristiques amusantes, le navigateur le supprime lorsqu'il s'arrête.

Un _cookie persistant_, au contraire, est stocké sur le client jusqu'à la date limite définie par ses directives `Expires` ou `Max-Age`.

Il est important de noter que les navigateurs peuvent employer un mécanisme connu sous le nom de _restauration de session_, où les cookies de session peuvent être récupérés après l'arrêt du client. Les navigateurs ont implémenté ce type de mécanisme pour permettre aux utilisateurs de reprendre une session après, par exemple, un crash. La restauration de session pourrait entraîner des [problèmes inattendus](https://stackoverflow.com/questions/777767/firefox-session-cookies) si nous nous attendons à ce que les cookies de session expirent dans un certain délai (par exemple, nous sommes absolument certains qu'une session ne durera pas plus de X temps).

Du point de vue d'un navigateur, la restauration de session est une fonctionnalité parfaitement valide, car ces cookies sont laissés entre les mains du client, sans date d'expiration. Ce que le client fait avec ces cookies n'affecte pas le serveur, qui est incapable de détecter si le client s'est arrêté à un moment donné. Si le client souhaite garder les cookies de session vivants pour toujours, ce n'est pas une préoccupation pour le serveur. Ce serait définitivement une implémentation discutable, mais il n'y a rien que le serveur puisse faire à ce sujet.

Je ne pense pas qu'il y ait un gagnant clair entre les cookies de session et les cookies persistants, car les deux servent des objectifs différents très bien. Ce que j'ai observé, cependant, c'est que Facebook, Google et des services similaires utiliseront des cookies persistants. De mon expérience personnelle, j'ai généralement toujours utilisé des cookies persistants, mais je n'ai jamais eu à lier des informations critiques, telles qu'un numéro de sécurité sociale ou le solde d'un compte bancaire, à une session.

Dans certains contextes, vous pourriez être tenu d'utiliser des cookies de session en raison des exigences de conformité. J'ai vu des auditeurs demander de convertir tous les cookies persistants en cookies de session. Lorsque les gens me demandent "devrais-je utiliser X ou Y ?" ma réponse est "cela dépend du contexte". Construire un livre d'or pour votre blog a des implications de sécurité différentes que de construire un système bancaire. Comme nous le verrons plus tard dans cette série, je recommanderais de comprendre votre contexte et d'essayer de construire un système qui est "assez sécurisé" : la sécurité absolue est une utopie, tout comme un SLA de 100%.

### Host-only

Lorsque un serveur n'inclut pas de directive `Domain`, le cookie doit être considéré comme un cookie `host-only`, ce qui signifie que sa validité est restreinte au domaine actuel uniquement.

C'est un comportement "par défaut" des navigateurs lorsqu'ils reçoivent un cookie qui n'a pas de `Domain` défini. Vous pouvez trouver un petit exemple que j'ai écrit à [github.com/odino/wasec/tree/master/cookies](https://github.com/odino/wasec/tree/master/cookies). C'est une simple application web qui définit des cookies en fonction des paramètres d'URL, et imprime les cookies sur la page, via un peu de code JavaScript :

```
<html>  <div id="output"/ >  <script>    let content = "none";
```

```
if (document.cookie) {      let cookies = document.cookie.split(';')      content = ''
```

```
cookies.forEach(c => {        content += "<p><code>" + c + "</code></p>"      })    }
```

```
document.getElementById('output').innerHTML = "Cookies on this document: <div>" + content + "</div>"  </script><html>
```

Si vous suivez les instructions dans le `README`, vous pourrez accéder à un serveur web à l'adresse [wasec.local:7888](http://wasec.local:7888/), qui illustre comment fonctionnent les cookies `host-only` :

![Image](https://cdn-media-1.freecodecamp.org/images/m9IqWiPYM7AufqGrh2YMCdUKpb11gNAOt4ml)

Si nous essayons ensuite de visiter un sous-domaine, les cookies que nous avons définis sur le domaine principal ne seront pas visibles - essayez de naviguer vers [sub.wasec.local:7888](http://sub.wasec.local:7888/) :

![Image](https://cdn-media-1.freecodecamp.org/images/B1ndsOGF72jb-Ti35ANDfeEqWrKOpcwZHxcx)

Une façon de contourner cette limitation est, comme nous l'avons vu précédemment, de spécifier la directive `Domain` du cookie, quelque chose que nous pouvons faire en visitant [wasec.local:7888/?domain=on](http://wasec.local:7888/?domain=on) :

![Image](https://cdn-media-1.freecodecamp.org/images/YSlhV6FjATiBRejQPVuTPt6kiEocPmMZF8kZ)

Si nous jetons un coup d'œil à l'application s'exécutant sur le sous-domaine, nous pourrons maintenant voir les cookies définis sur le domaine parent, car ils utilisent `Domain=wasec.local`, ce qui permet à tout domaine "sous" `wasec.local` d'accéder aux cookies :

![Image](https://cdn-media-1.freecodecamp.org/images/khal1469WCPimijC1tw1uiJkfrycXP8fPvY0)

En termes HTTP, voici à quoi ressemblent les réponses envoyées par le serveur :

```
~ 05 curl -I http://wasec.local:7888HTTP/1.1 200 OKSet-Cookie: example=test_cookieDate: Fri, 24 Aug 2018 09:34:08 GMTConnection: keep-alive
```

```
~ 05 curl -I "http://wasec.local:7888/?domain=on"HTTP/1.1 200 OKSet-Cookie: example=test_cookieSet-Cookie: example_with_domain=test_domain_cookie;Domain=wasec.localDate: Fri, 24 Aug 2018 09:34:11 GMTConnection: keep-alive
```

### Supercookies

Que se passerait-il si nous pouvions définir un cookie sur un domaine de premier niveau (TLD) tel que `.com` ou `.org` ? Cela serait définitivement une énorme préoccupation de sécurité, pour deux raisons principales :

* **vie privée de l'utilisateur** : chaque site web fonctionnant sur ce TLD spécifique serait en mesure de suivre des informations sur l'utilisateur dans un stockage partagé
* **fuite d'informations** : un serveur pourrait stocker par erreur une donnée sensible dans un cookie disponible pour d'autres sites

Heureusement, les cookies TLD, autrement connus sous le nom de [supercookies](https://en.wikipedia.org/wiki/HTTP_cookie#Supercookie), sont désactivés par les navigateurs web pour les raisons que j'ai mentionnées ci-dessus. Si vous essayez de définir un supercookie, le navigateur refusera simplement de le faire. Si nous ajoutons le paramètre `super=on` dans notre exemple, nous verrons le serveur essayer de définir un supercookie, tandis que le navigateur l'ignore :

![Image](https://cdn-media-1.freecodecamp.org/images/SLB7Yd8qDqf3-G44HvGbjAMxSkS8N3XmnxUr)

Dans le web d'aujourd'hui, cependant, il existe d'autres moyens de suivre les utilisateurs, le [suivi ETag](https://en.wikipedia.org/wiki/HTTP_ETag#Tracking_using_ETags) en étant un exemple. Puisque les cookies sont généralement associés au suivi, [ces techniques sont souvent appelées supercookies](https://qz.com/634294/a-short-guide-to-supercookies-whether-youre-being-tracked-and-how-to-opt-out/) également, même si elles ne reposent pas sur les cookies HTTP. D'autres termes qui peuvent désigner le même ensemble de technologies et de pratiques sont les permacookies (cookies permanents) ou les zombiecookies (cookies qui ne meurent jamais).

> **Publicités indésirables de Verizon**

> _Les entreprises adorent gagner de l'argent avec les publicités, ce n'est pas une nouvelle. Mais lorsque les FAI commencent à suivre agressivement leurs clients afin de servir des publicités indésirables, eh bien, c'est une autre histoire._

> _En 2016, [Verizon a été reconnu coupable de suivi des utilisateurs sans leur consentement](https://www.theverge.com/2016/3/7/11173010/verizon-supercookie-fine-1-3-million-fcc), et de partage de leurs informations avec des annonceurs. Cela a abouti à une amende de 1,35 million de dollars et l'impossibilité, pour l'entreprise, de continuer avec leur politique de suivi discutable._

> _Un autre exemple intéressant était Comcast, qui avait l'habitude [d'inclure du code JavaScript personnalisé dans les pages web servies via son réseau](https://www.privateinternetaccess.com/blog/2016/12/comcast-still-uses-mitm-javascript-injection-serve-unwanted-ads-messages/)._

> _Il va sans dire que si tout le trafic web était servi via HTTPS, nous n'aurions pas ce problème, car les FAI ne pourraient pas décrypter et manipuler le trafic à la volée._

### Drapeaux de cookies qui comptent

Jusqu'à présent, nous avons à peine effleuré la surface des cookies HTTP. Il est maintenant temps pour nous de goûter au vrai jus.

Il existe 3 directives très importantes (`Secure`, `HttpOnly`, et `SameSite`) qui doivent être comprises avant d'utiliser des cookies, car elles impactent fortement la manière dont les cookies sont stockés et sécurisés.

### Chiffrez-le ou oubliez-le

Les cookies contiennent des informations très sensibles. Si des attaquants obtiennent un identifiant de session, ils peuvent usurper l'identité des utilisateurs en [détournant leurs sessions](https://en.wikipedia.org/wiki/Session_hijacking).

La plupart des attaques de _détournement de session_ se produisent généralement via un _man-in-the-middle_ qui peut écouter le trafic non chiffré entre le client et le serveur, et voler toute information qui a été échangée. Si un cookie est échangé via HTTP, alors il est vulnérable aux attaques MITM et au détournement de session.

Pour surmonter ce problème, nous pouvons utiliser HTTPS lors de l'émission du cookie et ajouter le drapeau `Secure`. Cela instructe les navigateurs de ne jamais envoyer le cookie dans des requêtes HTTP en clair.

En revenant à notre exemple pratique, nous pouvons tester cela en naviguant vers [https://wasec.local:7889/?secure=on](https://wasec.local:7889/?secure=on). Le serveur définit 2 cookies supplémentaires, l'un avec le drapeau `Secure` et l'autre sans :

![Image](https://cdn-media-1.freecodecamp.org/images/d-6jYVyjI-kFTegS5rXdAcHjBb2yne8hs6JQ)

Lorsque nous revenons en arrière et naviguons vers la version HTTP du site, nous pouvons clairement voir que le cookie `Secure` n'est pas disponible dans la page. Essayez de naviguer vers [wasec.local:7888](http://wasec.local:7888/).

![Image](https://cdn-media-1.freecodecamp.org/images/A9mFjiSIIx2NcZFju3ZvS-oVebW5ozCXhhI5)

Nous pouvons clairement voir que la version HTTPS de notre application a défini un cookie qui est disponible pour la version HTTP (le cookie `not_secure`), mais l'autre cookie, marqué comme `Secure`, n'est nulle part visible.

Marquer les cookies sensibles comme `Secure` est un aspect incroyablement important de la sécurité des cookies. Même si vous servez tout votre trafic via HTTPS, les attaquants peuvent trouver un moyen de configurer une ancienne page HTTP sous votre domaine et de rediriger les utilisateurs vers celle-ci. À moins que vos cookies ne soient `Secure`, ils auront alors accès à un repas très délicieux.

### JavaScript ne peut pas toucher cela

Comme nous l'avons vu précédemment dans cette série, les attaques XSS permettent à un utilisateur malveillant d'exécuter du JavaScript arbitraire sur une page. Considérant que vous pourriez lire le contenu du bocal à cookies avec un simple `document.cookie`, protéger nos cookies contre l'accès JavaScript non fiable est un aspect très important du durcissement des cookies d'un point de vue sécurité.

Heureusement, la spécification HTTP a pris soin de cela avec le drapeau `HttpOnly`. En utilisant cette directive, nous pouvons instructer le navigateur de ne pas partager le cookie avec JavaScript. Le navigateur supprime alors le cookie de la variable `window.cookie`, le rendant impossible à accéder via JavaScript.

Si nous regardons l'exemple à l'adresse [wasec.local:7888/?httponly=on](http://wasec.local:7888/?httponly=on), nous pouvons clairement voir comment cela fonctionne. Le navigateur a stocké le cookie (comme vu dans la capture d'écran des DevTools ci-dessous) mais ne le partagera pas avec JavaScript :

![Image](https://cdn-media-1.freecodecamp.org/images/JBOOMVwOz2EVdfR7tRez4mdIcDhizfeQOZeW)

Le navigateur continuera alors à envoyer le cookie au serveur dans les requêtes ultérieures, de sorte que le serveur peut toujours suivre le client via le cookie. L'astuce, dans ce cas, est que le cookie n'est jamais exposé à l'utilisateur final, et reste "privé" entre le navigateur et le serveur.

Le drapeau `HttpOnly` aide à atténuer les attaques XSS en refusant l'accès aux informations critiques stockées dans un cookie. Son utilisation rend plus difficile pour un attaquant de détourner une session.

> _En 2003, des chercheurs ont découvert une vulnérabilité intéressante autour du drapeau `HttpOnly`, [Cross-Site Tracing](https://www.owasp.org/index.php/Cross_Site_Tracing) (XST)._

> _En résumé, les navigateurs ne prévenaient pas l'accès aux cookies `HttpOnly` lors de l'utilisation de la méthode de requête `TRACE`. Bien que la plupart des navigateurs aient maintenant désactivé cette méthode, ma recommandation serait de désactiver `TRACE` au niveau de votre serveur web, en retournant le code de statut `405 Not allowed`._

### SameSite : Le tueur de CSRF

Dernier mais non des moindres, le drapeau `SameSite`, l'une des dernières entrées dans le monde des cookies.

Introduit par Google Chrome v51, ce drapeau élimine efficacement la _Cross-Site Request Forgery_ (CSRF) du web. `SameSite` est une innovation simple mais révolutionnaire, car les solutions précédentes aux attaques CSRF étaient soit incomplètes, soit trop lourdes pour les propriétaires de sites.

Afin de comprendre `SameSite`, nous devons d'abord examiner la vulnérabilité qu'il neutralise. Une CSRF est une requête non désirée faite par le site A au site B alors que l'utilisateur est authentifié sur le site B.

Cela semble compliqué ? Laissez-moi reformuler.

Supposons que vous êtes connecté à votre site bancaire, qui dispose d'un mécanisme pour transférer de l'argent basé sur un formulaire HTML `<fo`rm> et quelques paramètres supplémentaires (compte de destination et montant). Lorsque le site recei`ves` une requête POST avec ces paramètres et votre cookie de session, il traitera le transfert. Maintenant, supposons qu'un site tiers malveillant configure un formulaire HTML comme suit :

```
<form action="https://bank.com/transfer" method="POST"><input type="hidden" name="destination" value="attacker@email.com" /><input type="hidden" name="amount" value="1000" /><input type="submit" value="CLIQUEZ ICI POUR GAGNER UN HUMMER" /></form>
```

Vous voyez où cela mène ?

Si vous cliquez sur le bouton de soumission, habilement déguisé en prix attractif, 1000 $ vont être transférés de votre compte. Ce n'est rien de plus, rien de moins qu'une falsification de requête inter-sites.

Traditionnellement, il y a eu 2 moyens de se débarrasser de la CSRF :

* Les en-têtes `Origin` et `Referer` : le serveur pourrait vérifier que ces en-têtes proviennent de sources fiables (par exemple `https://bank.com`). L'inconvénient de cette approche est que, comme nous l'avons vu précédemment dans cette série, ni l'`Origin` ni le `Referer` ne sont très fiables et pourraient être "désactivés" par le client afin de protéger la vie privée de l'utilisateur.
* Les jetons CSRF : le serveur pourrait inclure un jeton signé dans le formulaire, et vérifier sa validité une fois le formulaire soumis. C'est généralement une approche solide et c'est la meilleure pratique recommandée depuis des années. L'inconvénient des jetons CSRF est qu'ils représentent une charge technique pour le backend, car vous devriez intégrer la génération et la validation de jetons dans votre application web. Cela peut ne pas sembler être une tâche compliquée, mais une solution plus simple serait la bienvenue.

Les cookies `SameSite` visent à supplanter les solutions mentionnées ci-dessus une fois pour toutes. Lorsque vous étiquetez un cookie avec ce drapeau, vous dites au navigateur de ne pas inclure le cookie dans les requêtes générées par des origines différentes. Lorsque le navigateur initie une requête vers votre serveur et qu'un cookie est étiqueté comme `SameSite`, le navigateur vérifiera d'abord si l'origine de la requête est la même que celle qui a émis le cookie. Si ce n'est pas le cas, le navigateur n'inclura pas le cookie dans la requête.

Nous pouvons avoir un aperçu pratique de `SameSite` avec l'exemple à l'adresse [github.com/odino/wasec/tree/master/cookies](https://github.com/odino/wasec/tree/master/cookies). Lorsque vous naviguez vers [wasec.local:7888/?samesite=on](http://wasec.local:7888/?samesite=on), le serveur définira un cookie `SameSite` et un cookie "régulier".

![Image](https://cdn-media-1.freecodecamp.org/images/1dgsuUD8OSILMOoGHxADrAS93-6odmj0xDkq)

Si nous visitons ensuite [wasec2.local:7888/same-site-form](http://wasec2.local:7888/same-site-form), nous verrons un exemple de formulaire HTML qui déclenchera une requête inter-sites :

![Image](https://cdn-media-1.freecodecamp.org/images/E-DruZ3Sj0VBEXHgUlSDratIwueToplG16-D)

Si nous cliquons sur le bouton de soumission du formulaire, nous pourrons alors comprendre le vrai pouvoir de ce drapeau. Le formulaire nous redirigera vers [wasec.local:7888](http://wasec.local:7888/), mais il n'y a aucune trace du cookie `SameSite` dans la requête faite par le navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/yjZRnPQ6vCQNcP5FDuBya89CR-4AZenYo68q)

Ne soyez pas confus en voyant `same_site_cookie=test` sur votre écran : le cookie est mis à disposition par le navigateur, mais il n'a pas été envoyé dans la requête elle-même. Nous pouvons vérifier cela en tapant simplement `http://wasec.local:7888/` dans la barre d'adresse :

![Image](https://cdn-media-1.freecodecamp.org/images/Fzh4lrssQwMY-LT3X4RSpIUNJKzpccu-A9IH)

Puisque l'initiateur de la requête est "sûr" (pas d'origine, méthode `GET`), le navigateur envoie le cookie `SameSite` avec la requête.

Ce drapeau ingénieux a 2 variantes, `Lax` et `Strict`. Notre exemple utilise la première, car elle permet la navigation de premier niveau vers un site web pour inclure le cookie. Lorsque vous étiquetez un cookie comme `SameSite=Strict`, le navigateur n'enverra pas le cookie dans une requête inter-origines, y compris la navigation de premier niveau. Cela signifie que si vous cliquez sur un lien vers un site web qui utilise des cookies `strict`, vous ne serez pas connecté du tout. Un niveau de protection extrêmement élevé qui, d'autre part, pourrait surprendre les utilisateurs. Le mode `Lax` permet à ces cookies d'être envoyés dans des requêtes utilisant des méthodes sûres (comme `GET`), créant un mélange très utile entre sécurité et expérience utilisateur.

> _Récapitulons ce que nous avons appris sur les drapeaux de cookies, car ils sont cruciaux lorsque vous stockez, ou autorisez l'accès à, des données sensibles via eux, ce qui est une pratique très standard :_

> - marquer les cookies comme `Secure` garantira qu'ils ne seront pas envoyés dans des requêtes non chiffrées, rendant les attaques de type man-in-the-middle assez inutiles

> - avec le drapeau `HttpOnly`, nous disons au navigateur de ne pas partager le cookie avec le client (par exemple, en permettant l'accès JavaScript au cookie), limitant le rayon d'explosion d'une attaque XSS

> - en étiquetant le cookie comme `SameSite=Lax|Strict`, vous empêchez le navigateur de l'envoyer dans des requêtes inter-origines, rendant tout type d'attaque CSRF inefficace

### Alternatives

En lisant tout ce matériel sur les cookies et la sécurité, vous pourriez être tenté de dire "Je veux vraiment rester à l'écart des cookies !". La réalité est que, pour l'instant, les cookies sont votre meilleur pari si vous voulez implémenter un mécanisme de session sur HTTP. De temps en temps, on me demande d'évaluer des alternatives aux cookies, alors je vais essayer de résumer quelques choses qui sont souvent mentionnées :

* [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) : surtout dans le contexte des applications monopages (SPA), localStorage est parfois mentionné lors de la discussion sur l'endroit où stocker des jetons sensibles. Le problème avec cette approche, cependant, est que localStorage n'offre aucune sorte de protection contre les attaques XSS. Si un attaquant est capable d'exécuter un simple `localStorage.getItem('token')` sur le navigateur d'une victime, c'est la fin du jeu. Les cookies `HttpOnly` surmontent facilement ce problème.
* [JWT](https://jwt.io/) : Les JSON Web Tokens définissent un moyen de créer des jetons d'accès de manière sécurisée pour un client. JWT est une spécification qui définit à quoi ressemblerait un jeton d'accès et ne définit pas où le jeton va être stocké. En d'autres termes, vous pourriez stocker un JWT dans un cookie, le localStorage ou même en mémoire, donc cela n'a pas de sens de considérer les JWT comme une "alternative" aux cookies.

### Que ferait LeBron ?

![Image](https://cdn-media-1.freecodecamp.org/images/Aa-MltRxBUh6IYUkejN4oAVtsfMq4jDpvDy9)

Il est temps de passer du protocole HTTP et de ses fonctionnalités, comme les cookies. Tout au long de cette série, nous avons entrepris un long voyage, en disséquant pourquoi les cookies sont nés, comment ils sont structurés et comment vous pouvez les protéger en appliquant certaines restrictions sur leurs attributs `Domain`, `Expires`, `Max-Age` et `Path`, et comment d'autres drapeaux tels que `Secure`, `HttpOnly` et `SameSite` sont vitaux pour renforcer les cookies.

Allons de l'avant et essayons de comprendre ce que nous devrions faire, d'un point de vue sécurité, lorsque nous rencontrons une situation particulière. Le prochain article essaiera de fournir des conseils basés sur les meilleures pratiques et l'expérience passée.

Le prochain article de cette série introduira ce que j'appelle "_Les Situationnels_".

_Publié à l'origine sur [odino.org](https://odino.org/security-hardening-http-cookies/) (14 septembre 2018)._  
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) — les rants sont les bienvenus !_ 💡
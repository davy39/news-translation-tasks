---
title: Comment fonctionnent les navigateurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T19:38:40.000Z'
originalURL: https://freecodecamp.org/news/web-application-security-understanding-the-browser-5305ed2f1dac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LPukLPd6d4l3YH8kCLDz5w.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Browsers
  slug: browsers
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment fonctionnent les navigateurs
seo_desc: 'By Alex Nadalin

  An Introduction to Web Application Security


  _Photo by [Unsplash](https://unsplash.com/photos/cVMaxt672ss?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Liam Tucker on <a hr...'
---

Par Alex Nadalin

#### Une introduction à la sécurité des applications web

![Image](https://cdn-media-1.freecodecamp.org/images/LIFd-0L9YdixoIiqgvRFXgi3Ef3I28Q9JedF)
_Photo par [Unsplash](https://unsplash.com/photos/cVMaxt672ss?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Liam Tucker</a> sur <a href="https://unsplash.com/search/photos/security?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Commençons cette série sur la sécurité des applications web par une explication de ce que font les navigateurs et de la manière dont ils le font. Puisque la plupart de vos clients interagiront avec votre application web via un navigateur, il est impératif de comprendre les bases de ces merveilleux programmes.

**Le navigateur est un moteur de rendu**. Son travail consiste à télécharger une page web et à la rendre de manière compréhensible pour un être humain.

Bien que ce soit une simplification presque criminelle, c'est tout ce que nous devons savoir pour l'instant.

* L'utilisateur entre une adresse dans la barre du navigateur.
* Le navigateur télécharge le « document » à cette URL et le rend.

![Image](https://cdn-media-1.freecodecamp.org/images/36UVnQqt7Pi8y5VreXig8MFoon65civsswLS)

Vous êtes peut-être habitué à travailler avec l'un des navigateurs les plus populaires tels que Chrome, Firefox, Edge ou Safari, mais cela ne signifie pas qu'il n'existe pas d'autres navigateurs.

[Lynx](https://lynx.browser.org/), par exemple, est un navigateur léger, basé sur du texte, qui fonctionne à partir de votre ligne de commande. Au cœur de Lynx se trouvent les mêmes principes exacts que vous trouveriez dans n'importe quel autre navigateur « grand public ». Un utilisateur entre une adresse web (URL), le navigateur récupère le document et le rend — la seule différence étant que Lynx n'utilise pas un moteur de rendu visuel mais plutôt une interface basée sur du texte, ce qui fait que des sites comme Google ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/22-zfqmwHAaTX9h7UPlxalWVXn4u6Amd9agj)

Nous comprenons globalement ce que fait un navigateur, mais examinons de plus près les étapes que ces applications ingénieuses réalisent pour nous.

### Que fait un navigateur ?

En résumé, le travail d'un navigateur consiste principalement à :

* Résolution DNS
* Échange HTTP
* Rendu
* Répéter le processus

#### **Résolution DNS**

Ce processus garantit que, une fois que l'utilisateur entre une URL, le navigateur sait à quel serveur il doit se connecter. Le navigateur contacte un serveur DNS pour découvrir que `google.com` se traduit par `216.58.207.110`, une adresse IP à laquelle le navigateur peut se connecter.

#### Échange HTTP

Une fois que le navigateur a identifié quel serveur va servir notre requête, il initié une connexion TCP avec celui-ci et commence l'**échange HTTP**. Ce n'est rien d'autre qu'un moyen pour le navigateur de communiquer avec le serveur ce dont il a besoin, et pour le serveur de répondre.

HTTP est simplement le nom du protocole le plus populaire pour communiquer sur le web, et les navigateurs communiquent principalement via HTTP lorsqu'ils parlent avec les serveurs. Un échange HTTP implique que le client (notre navigateur) envoie une **requête**, et que le serveur réponde avec une **réponse**.

Par exemple, après que le navigateur s'est connecté avec succès au serveur derrière `google.com`, il enverra une requête qui ressemble à ceci :

```
GET / HTTP/1.1Host: google.comAccept: */*
```

Décomposons la requête, ligne par ligne :

* `GET / HTTP/1.1` : avec cette première ligne, le navigateur demande au serveur de récupérer le document à l'emplacement `/`, en ajoutant que le reste de la requête suivra le protocole HTTP/1.1 (il pourrait également utiliser `1.0` ou `2`)
* `Host: google.com` : il s'agit du **seul en-tête HTTP obligatoire dans HTTP/1.1**. Puisque le serveur peut servir plusieurs domaines (`google.com`, `google.co.uk`, etc.), le client mentionne ici que la requête était pour cet hôte spécifique
* `Accept: */*` : un en-tête optionnel, où le navigateur indique au serveur qu'il acceptera tout type de réponse. Le serveur pourrait avoir une ressource disponible en formats JSON, XML ou HTML, il peut donc choisir le format qu'il préfère

Après que le navigateur, qui agit en tant que **client**, a terminé sa requête, c'est au tour du serveur de répondre. Voici à quoi ressemble une réponse :

```
HTTP/1.1 200 OKCache-Control: private, max-age=0Content-Type: text/html; charset=ISO-8859-1Server: gwsX-XSS-Protection: 1; mode=blockX-Frame-Options: SAMEORIGINSet-Cookie: NID=1234; expires=Fri, 18-Jan-2019 18:25:04 GMT; path=/; domain=.google.com; HttpOnly
```

```
<!doctype html><html">......</html>
```

Wow, c'est beaucoup d'informations à digérer. Le serveur nous informe que la requête a réussi (`200 OK`) et ajoute quelques en-têtes à la **réponse**, par exemple, il indique quel serveur a traité notre requête (`Server: gws`), quelle est la politique `X-XSS-Protection` de cette réponse, et ainsi de suite.

Pour l'instant, vous n'avez pas besoin de comprendre chaque ligne de la réponse. Nous aborderons le protocole HTTP, ses en-têtes, etc., plus tard dans cette série.

Pour l'instant, tout ce que vous devez comprendre, c'est que le client et le serveur échangent des informations et qu'ils le font via HTTP.

#### Rendu

Enfin, mais non des moindres, le processus de **rendu**. À quoi servirait un navigateur s'il ne montrait à l'utilisateur qu'une liste de caractères étranges ?

```
<!doctype html><html">......</html>
```

Dans le **corps** de la réponse, le serveur inclut la représentation de la réponse selon l'en-tête `Content-Type`. Dans notre cas, le type de contenu était défini sur `text/html`, nous attendons donc un balisage HTML dans la réponse — ce qui est exactement ce que nous trouvons dans le corps.

C'est là qu'un navigateur brille vraiment. Il analyse le HTML, charge les ressources supplémentaires incluses dans le balisage (par exemple, il pourrait y avoir des fichiers JavaScript ou des documents CSS à récupérer) et les présente à l'utilisateur dès que possible.

Une fois de plus, le résultat final est quelque chose que le commun des mortels peut comprendre.

![Image](https://cdn-media-1.freecodecamp.org/images/PsZC9DUwnoX9m5jPVkT8lWMr5lZ1GliyEjKS)

Pour une version plus détaillée de ce qui se passe réellement lorsque nous appuyons sur Entrée dans la barre d'adresse d'un navigateur, je vous suggère de lire « [What happens when…](https://github.com/alex/what-happens-when) », une tentative très élaborée d'expliquer les mécanismes derrière le processus.

Puisque cette série est axée sur la sécurité, je vais vous donner un indice sur ce que nous venons d'apprendre : **les attaquants gagnent facilement leur vie grâce aux vulnérabilités dans l'échange HTTP et la partie rendu**. Les vulnérabilités, et les utilisateurs malveillants, se cachent ailleurs également, mais une meilleure approche de la sécurité à ces niveaux vous permet déjà de faire des progrès dans l'amélioration de votre posture de sécurité.

#### Fournisseurs

Les 4 navigateurs les plus populaires appartiennent à différents fournisseurs :

* Chrome par Google
* Firefox par Mozilla
* Safari par Apple
* Edge par Microsoft

En plus de se battre les uns contre les autres pour augmenter leur pénétration sur le marché, les fournisseurs s'engagent également les uns avec les autres afin d'améliorer les **normes web**, qui sont une sorte de « exigences minimales » pour les navigateurs.

Le [W3C](https://www.w3.org/) est l'organisme derrière le développement des normes, mais il n'est pas rare que les navigateurs développent leurs propres fonctionnalités qui finissent par devenir des normes web, et la sécurité ne fait pas exception à cela.

Chrome 51, par exemple, [a introduit les cookies SameSite](https://www.chromestatus.com/feature/4672634709082112), une fonctionnalité qui permettrait aux applications web de se débarrasser d'un type particulier de vulnérabilité connu sous le nom de CSRF (plus sur cela plus tard). D'autres fournisseurs ont décidé que c'était une bonne idée et ont suivi, conduisant à ce que SameSite devienne une norme web : à ce jour, [Safari est le seul navigateur majeur sans support des cookies SameSite](https://caniuse.com/#search=samesite).

![Image](https://cdn-media-1.freecodecamp.org/images/rAkCeGgFkTBqnbxYa7c0qu6m2TNjKNK847tw)

Cela nous apprend 2 choses :

* Safari ne semble pas se soucier suffisamment de la sécurité de ses utilisateurs (je plaisante : les cookies SameSite seront disponibles dans Safari 12, qui pourrait déjà être sorti au moment où vous lisez cet article)
* **corriger une vulnérabilité sur un navigateur ne signifie pas que tous vos utilisateurs sont en sécurité**

Le premier point est une pique à Safari (comme je l'ai mentionné, je plaisante !), tandis que le second point est vraiment important. Lorsque nous développons des applications web, nous ne devons pas seulement nous assurer qu'elles ont la même apparence sur divers navigateurs, mais aussi qu'elles protègent nos utilisateurs de la même manière sur toutes les plateformes.

**Votre stratégie en matière de sécurité web devrait varier en fonction de ce qu'un fournisseur de navigateur nous permet de faire**. De nos jours, la plupart des navigateurs supportent le même ensemble de fonctionnalités et s'écartent rarement de leur feuille de route commune, mais des cas comme celui ci-dessus se produisent encore, et c'est quelque chose que nous devons prendre en compte lorsque nous définissons notre stratégie de sécurité.

Dans notre cas, si nous décidons que nous allons atténuer les attaques CSRF uniquement via les cookies SameSite, nous devons être conscients que nous mettons nos utilisateurs de Safari en danger. Et nos utilisateurs doivent le savoir aussi.

Enfin, vous devez vous rappeler que vous pouvez décider de supporter ou non une version de navigateur : supporter chaque version de navigateur serait impraticable (pensez à Internet Explorer 6). Assurer que les dernières versions des principaux navigateurs sont supportées, cependant, est généralement une bonne décision. Si vous ne prévoyez pas d'offrir une protection sur une plateforme particulière, il est généralement conseillé d'en informer vos utilisateurs.

> **_Astuce Pro_**_: Vous ne devriez jamais encourager vos utilisateurs à utiliser des navigateurs obsolètes, ou les supporter activement. Même si vous avez pris toutes les précautions nécessaires, d'autres développeurs web peuvent ne pas l'avoir fait. Encouragez les utilisateurs à utiliser la dernière version supportée de l'un des principaux navigateurs._

#### Bug du fournisseur ou de la norme ?

Le fait que l'utilisateur moyen accède à notre application via un client tiers (le navigateur) ajoute un autre niveau d'indirection vers une expérience de navigation claire et sécurisée : le navigateur lui-même peut présenter une vulnérabilité de sécurité.

Les fournisseurs offrent généralement des récompenses (aka _bug bounties_) aux chercheurs en sécurité qui peuvent trouver une vulnérabilité sur le navigateur lui-même. Ces bugs ne sont pas liés à votre implémentation, mais plutôt à la manière dont le navigateur gère la sécurité de son côté.

Le [programme de récompenses de Chrome](https://www.google.com/about/appsecurity/chrome-rewards/), par exemple, permet aux ingénieurs en sécurité de contacter l'équipe de sécurité de Chrome pour signaler les vulnérabilités qu'ils ont trouvées. Si ces vulnérabilités sont confirmées, un correctif est émis, un avis de sécurité est généralement publié au public, et le chercheur reçoit une récompense (généralement financière) du programme.

Des entreprises comme Google investissent une somme relativement importante de capital dans leurs programmes de Bug Bounty, car cela leur permet d'attirer des chercheurs en promettant un avantage financier s'ils trouvent un problème avec l'application.

Dans un programme de Bug Bounty, tout le monde est gagnant : le fournisseur parvient à améliorer la sécurité de son logiciel, et les chercheurs sont payés pour leurs découvertes. Nous discuterons de ces programmes plus tard, car je crois que les initiatives de Bug Bounty méritent leur propre section dans le paysage de la sécurité.

> _Jake Archibald est un développeur advocate chez Google qui a récemment découvert une vulnérabilité impactant plus d'un navigateur. Il a documenté ses efforts, comment il a approché différents fournisseurs, et leurs réactions dans un intéressant [article de blog](https://jakearchibald.com/2018/i-discovered-a-browser-bug/) que je vous recommande de lire._

### Un navigateur pour les développeurs

À ce stade, nous devrions avoir compris un concept très simple mais plutôt important : **les navigateurs sont simplement des clients HTTP conçus pour l'internaute moyen**.

Ils sont définitivement plus puissants que le client HTTP de base d'une plateforme (pensez à `require('http')` de NodeJS, par exemple), mais au bout du compte, ils ne sont qu'une évolution naturelle de clients HTTP plus simples.

En tant que développeurs, notre client HTTP de choix est probablement [cURL](http://curl.haxx.se/) de Daniel Stenberg, l'un des programmes logiciels les plus populaires que les développeurs web utilisent au quotidien. Il nous permet de faire un échange HTTP à la volée, en envoyant une requête HTTP à partir de notre ligne de commande :

```
$ curl -I localhost:8080
```

```
HTTP/1.1 200 OKserver: ecstatic-2.2.1Content-Type: text/htmletag: "23724049-4096-"2018-07-20T11:20:35.526Z""last-modified: Fri, 20 Jul 2018 11:20:35 GMTcache-control: max-age=3600Date: Fri, 20 Jul 2018 11:21:02 GMTConnection: keep-alive
```

Dans l'exemple ci-dessus, nous avons demandé le document à `localhost:8080/`, et un serveur local a répondu avec succès.

Plutôt que de vider le corps de la réponse sur la ligne de commande, ici nous avons utilisé le drapeau `-I` qui indique à cURL que nous ne sommes intéressés que par les en-têtes de réponse. Allant un peu plus loin, nous pouvons instruire cURL de vider un peu plus d'informations, y compris la requête réelle qu'il effectue, afin que nous puissions mieux examiner cet échange HTTP. L'option dont nous avons besoin est `-v` (verbose) :

```
$ curl -I -v localhost:8080* Rebuilt URL to: localhost:8080/*   Trying 127.0.0.1...* Connected to localhost (127.0.0.1) port 8080 (#0)> HEAD / HTTP/1.1> Host: localhost:8080> User-Agent: curl/7.47.0> Accept: */*>< HTTP/1.1 200 OKHTTP/1.1 200 OK< server: ecstatic-2.2.1server: ecstatic-2.2.1< Content-Type: text/htmlContent-Type: text/html< etag: "23724049-4096-"2018-07-20T11:20:35.526Z""etag: "23724049-4096-"2018-07-20T11:20:35.526Z""< last-modified: Fri, 20 Jul 2018 11:20:35 GMTlast-modified: Fri, 20 Jul 2018 11:20:35 GMT< cache-control: max-age=3600cache-control: max-age=3600< Date: Fri, 20 Jul 2018 11:25:55 GMTDate: Fri, 20 Jul 2018 11:25:55 GMT< Connection: keep-aliveConnection: keep-alive
```

```
<* Connection #0 to host localhost left intact
```

À peu près les mêmes informations sont disponibles dans les navigateurs grand public via leurs DevTools.

Comme nous l'avons vu, les navigateurs ne sont rien de plus que des clients HTTP élaborés. Certes, ils ajoutent une quantité énorme de fonctionnalités (pensez à la gestion des identifiants, aux favoris, à l'historique, etc.), mais la vérité est qu'ils sont nés en tant que clients HTTP pour les humains. Cela est important, car dans la plupart des cas, vous n'avez pas besoin d'un navigateur pour tester la sécurité de votre application web, car vous pouvez simplement la « curler » et jeter un coup d'œil à la réponse.

Une dernière chose que je voudrais souligner, c'est que **n'importe quoi peut être un navigateur**. Si vous avez une application mobile qui consomme des API via le protocole HTTP, alors l'application est votre navigateur — il se trouve simplement qu'elle est hautement personnalisée, que vous avez construite vous-même, et qui ne comprend qu'un type spécifique de réponses HTTP (de votre propre API).

### Dans le protocole HTTP

Comme nous l'avons mentionné, les phases d'**échange HTTP** et de **rendu** sont celles que nous allons principalement couvrir, car elles offrent le plus grand nombre de **vecteurs d'attaque** pour les utilisateurs malveillants.

Dans le [prochain article](https://medium.freecodecamp.org/web-security-https-perspective-5fa07140f9b3), nous allons examiner plus en profondeur le protocole HTTP et essayer de comprendre quelles mesures nous devons prendre pour sécuriser les échanges HTTP.

_Publié à l'origine sur [odino.org](https://odino.org/wasec-understanding-the-browser/) (29 juillet 2018)._  
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) - les rants sont les bienvenus !_ 💡
---
title: Tout ce que vous devez savoir sur les cookies pour le développement web
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-02-03T06:14:00.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-cookies-for-web-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/602cb40c0a2838549dcc6af3.jpg
tags:
- name: cookies
  slug: cookies
- name: web
  slug: web
- name: Web Development
  slug: web-development
seo_title: Tout ce que vous devez savoir sur les cookies pour le développement web
seo_desc: 'Have you ever wondered how you can sign in to a website once and remain
  signed in, even if you close your browser? Or added an item to your shopping cart
  without signing in at all?

  Whether you know it or not, cookies are everywhere, and for better or...'
---

Vous êtes-vous déjà demandé comment vous pouvez vous connecter à un site web une fois et rester connecté, même si vous fermez votre navigateur ? Ou ajouté un article à votre panier sans vous connecter du tout ?

Que vous le sachiez ou non, les cookies sont partout, et pour le meilleur ou pour le pire, ils ont complètement changé la façon dont nous utilisons le web.

Dans cet article, nous allons passer en revue l'histoire des cookies, leur fonctionnement, comment les utiliser en JavaScript, et quelques préoccupations de sécurité à garder à l'esprit.

## Une brève histoire des cookies

HTTP, ou le protocole de transfert hypertexte, est un protocole sans état. Selon Wikipedia, c'est un protocole sans état parce qu'il "ne nécessite pas que le serveur HTTP conserve des informations ou un statut sur chaque utilisateur pour la durée de plusieurs requêtes".

Vous pouvez encore voir cela aujourd'hui avec des sites web simples – vous tapez l'URL dans le navigateur, le navigateur fait une requête à un serveur quelque part, et le serveur retourne les fichiers pour rendre la page et la connexion est fermée.

Maintenant, imaginez que vous devez vous connecter à un site web pour voir un certain contenu, comme avec LinkedIn. Le processus est largement le même que celui ci-dessus, mais on vous présente un formulaire pour entrer votre adresse e-mail et votre mot de passe.

Vous entrez ces informations et votre navigateur les envoie au serveur. Le serveur vérifie vos informations de connexion, et si tout semble bon, il envoie les données nécessaires pour rendre la page à votre navigateur.

Mais si LinkedIn était vraiment sans état, une fois que vous naviguez vers une page différente, le serveur ne se souviendrait pas que vous venez de vous connecter. Il vous demanderait d'entrer à nouveau votre adresse e-mail et votre mot de passe, de les vérifier, puis d'envoyer les données pour rendre la nouvelle page.

Cela serait super frustrant, n'est-ce pas ? Beaucoup de développeurs l'ont pensé aussi, et ont trouvé différentes façons de créer des sessions avec état sur le web.

### L'invention du cookie HTTP

Lou Montoulli, un développeur chez Netscape dans les années 90, avait un problème – il développait une boutique en ligne pour une autre entreprise, MCI, qui stockerait les articles dans le panier de chaque client sur ses serveurs. Cela signifiait que les gens devaient d'abord créer un compte, c'était lent, et cela prenait beaucoup de stockage.

MCI a demandé que toutes ces données soient stockées sur l'ordinateur de chaque client. De plus, ils voulaient que tout fonctionne sans que les clients aient à se connecter d'abord.

Pour résoudre cela, Lou s'est tourné vers une idée qui était déjà assez bien connue parmi les programmeurs : le magic cookie.

Un magic cookie, ou simplement cookie, est un peu de données qui est passé entre deux programmes informatiques. Ils sont "magiques" parce que les données dans le cookie sont souvent une clé ou un jeton aléatoire, et sont vraiment destinées au logiciel qui les utilise.

Lou a pris le concept de magic cookie et l'a appliqué à la boutique en ligne, et plus tard aux navigateurs dans leur ensemble.

Maintenant que vous connaissez leur histoire, jetons un rapide coup d'œil à la façon dont les cookies sont utilisés pour créer des sessions avec état sur le web.

## Comment fonctionnent les cookies

Une façon de penser aux cookies est qu'ils ressemblent un peu aux bracelets que vous obtenez lorsque vous visitez un parc d'attractions.

Par exemple, lorsque vous vous connectez à un site web, c'est comme le processus d'entrée dans un parc d'attractions. D'abord, vous payez pour un ticket, puis lorsque vous entrez dans le parc, le personnel vérifie votre ticket et vous donne un bracelet.

C'est comme la façon dont vous vous connectez – le serveur vérifie votre nom d'utilisateur et votre mot de passe, crée et stocke une session, génère un identifiant de session unique, et envoie un cookie avec l'identifiant de session.

(Notez que l'identifiant de session n'est _pas_ votre mot de passe, mais est quelque chose de complètement séparé et généré à la volée. La gestion correcte des mots de passe et l'authentification sont hors du cadre de cet article, mais vous pouvez trouver des guides approfondis [ici](https://www.freecodecamp.org/news/search/?query=authentication).)

Pendant que vous êtes dans le parc d'attractions, vous pouvez faire n'importe quelle attraction en montrant votre bracelet.

De même, lorsque vous faites des requêtes au site web auquel vous êtes connecté, votre navigateur envoie votre cookie avec votre identifiant de session au serveur. Le serveur vérifie votre session en utilisant votre identifiant de session, puis retourne les données pour votre requête.

Enfin, une fois que vous quittez le parc d'attractions, votre bracelet ne fonctionne plus – vous ne pouvez pas l'utiliser pour revenir dans le parc ou faire plus d'attractions.

C'est comme se déconnecter d'un site web. Votre navigateur envoie votre requête de déconnexion au serveur avec votre cookie, le serveur supprime votre session, et informe votre navigateur de supprimer votre cookie d'identifiant de session.

Si vous voulez revenir dans le parc d'attractions, vous devriez acheter un autre ticket et obtenir un autre bracelet. En d'autres termes, si vous voulez continuer à utiliser le site web, vous devriez vous reconnecter.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/fireship-cookies.png)
_Source : [Session vs Token Authentication in 100 Seconds](https://www.youtube.com/watch?v=UBUNrFtufWo) (YouTube)_

Ce n'est qu'un simple exemple de la façon dont les cookies peuvent être utilisés pour vous garder connecté aux sites web. Ils peuvent être utilisés pour se souvenir de votre paramètre pour le mode sombre, pour suivre votre comportement sur un site web, et bien plus encore.

## Comment utiliser les cookies

Maintenant que vous connaissez l'histoire des cookies et pourquoi ils sont utilisés, examinons quelques-unes des limitations de l'utilisation des cookies, puis plongeons dans quelques exemples simples.

### Limitations des cookies

Les cookies sont assez limités par rapport à certaines alternatives modernes de stockage de données dans le navigateur comme `localStorage` ou `sessionStorage`. Voici un résumé des cookies par rapport à ces autres technologies :

|                    | Cookies            | Local Storage | Session Storage |
|--------------------|--------------------|----------------|------------------|
| Capacité           | 4KB                | 10MB           | 5MB              |
| Accessible depuis  | N'importe quelle fenêtre | N'importe quelle fenêtre | Même onglet     |
| Expire             | Définie manuellement | Jamais         | À la fermeture de l'onglet |
| Emplacement de stockage | Navigateur et serveur | Navigateur uniquement | Navigateur uniquement |
| Envoyé avec les requêtes | Oui                | Non             | Non               |

Basé sur : [cookies vs localStorage vs sessionStorage - Beau teaches JavaScript](https://www.youtube.com/watch?v=AwicscsvGLg) (YouTube)

Les cookies sont une technologie beaucoup plus ancienne et ont une capacité très limitée. Pourtant, il y a beaucoup de choses que vous pouvez faire avec eux. Et leur petite taille facilite l'envoi des cookies avec chaque requête au serveur par le navigateur.

Il est également important de mentionner que les navigateurs ne permettent aux cookies de fonctionner que depuis un domaine pour des raisons de sécurité.

Ainsi, si vous vous connectez à votre banque, disons sur ally.com, les cookies ne fonctionneront que dans ce domaine et ses sous-domaines. Par exemple, votre cookie `ally.com` fonctionnera sur `ally.com`, `ally.com/about`, et le sous-domaine `www.ally.com`, mais pas sur `axos.com`.

Cela signifie que, même si vous avez des comptes et êtes connecté à la fois sur `ally.com` et `axos.com`, ces sites ne pourront pas lire les cookies de l'autre.

Il est important de se rappeler que vos cookies sont envoyés avec chaque requête que vous faites dans le navigateur. C'est très pratique, mais cela a des implications sérieuses en matière de sécurité que nous aborderons plus tard.

Enfin, si vous ne deviez retenir qu'une seule chose de cet article, rappelez-vous simplement que les cookies sont destinés à être lus et envoyés ouvertement, donc vous ne devriez jamais y stocker d'informations sensibles comme des mots de passe.

### Comment définir un cookie en JavaScript

Les cookies ne sont vraiment que des chaînes avec des paires clé/valeur. Bien que vous travaillerez probablement plus avec les cookies sur le backend, il peut y avoir des moments où vous voudrez définir un cookie côté client.

Voici comment définir un cookie en JavaScript vanilla :

```js
document.cookie = 'dark_mode=true'
```

Ensuite, lorsque vous ouvrez la console de développement, cliquez sur "Application" puis sur le site sous "Cookies", vous verrez le cookie que vous venez d'ajouter :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-101.png)

Si vous regardez de plus près votre cookie, vous verrez que sa date d'expiration est définie sur `Session`. Cela signifie que le cookie sera détruit lorsque vous fermerez votre onglet/navigateur.

Cela pourrait être le comportement que vous souhaitez, comme pour une boutique en ligne avec des informations de paiement.

Mais si vous voulez que votre cookie dure plus longtemps, vous devrez définir une date d'expiration.

### Comment définir une date d'expiration sur un cookie en JavaScript

Pour définir une date d'expiration, il suffit de définir la valeur de votre cookie, puis d'ajouter un attribut `expires` avec une date définie à un moment dans le futur :

```js
document.cookie = 'dark_mode=true; expires=Fri, 26 Feb 2021 00:00:00 GMT' // expire dans 1 semaine
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-102.png)

L'objet `Date` de JavaScript devrait rendre cela beaucoup plus facile et plus flexible. Vous pouvez en lire plus sur l'objet `Date` [ici](https://www.freecodecamp.org/news/the-ultimate-guide-to-javascript-date-and-moment-js/).

Ou vous pourriez utiliser l'attribut `max-age` avec le nombre de secondes pendant lesquelles vous souhaitez que votre cookie dure :

```js
document.cookie = 'dark_mode=true; max-age=604800'; // expire dans 1 semaine
```

Ensuite, lorsque cette date arrivera, le navigateur supprimera automatiquement votre cookie.

### Comment mettre à jour un cookie en JavaScript

Que votre cookie ait ou non une date d'expiration, le mettre à jour est facile.

Il suffit de changer la valeur de votre cookie, et le navigateur le prendra automatiquement en compte :

```js
document.cookie = "dark_mode=false; max-age=604800"; // expire dans 1 semaine
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-105.png)

### Comment définir le chemin pour un cookie en JavaScript

Parfois, vous ne voudrez que votre cookie fonctionne avec certaines parties de votre site web. Selon la configuration de votre site web, une façon de faire cela est avec l'attribut `path`.

Voici comment faire pour qu'un cookie ne fonctionne que sur la page à propos à `/about` :

```js
document.cookie = 'dark_mode=true; path=/about';
```

Maintenant, votre cookie ne fonctionnera que sur `/about` et d'autres sous-répertoires imbriqués comme `/about/team`, mais pas sur `/blog`.

Ensuite, lorsque vous visitez la page à propos et vérifiez vos cookies, vous le verrez :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-103.png)

### Comment supprimer un cookie en JavaScript

Pour supprimer un cookie en JavaScript, il suffit de définir l'attribut `expires` sur une date déjà passée :

```js
document.cookie = 'dark_mode=true; expires=Sun, 14 Feb 2021 00:00:00 GMT'; // 1 semaine plus tôt
```

Vous pourriez également utiliser `max-age` et lui passer une valeur négative :

```js
document.cookie = 'dark_mode=true; max-age=-60'; // 1 minute plus tôt
```

Ensuite, lorsque vous vérifiez votre cookie, il aura disparu :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-104.png)

Et cela devrait être tout ce que vous devez savoir sur l'utilisation des cookies en JS vanilla.

Tout ce que nous avons couvert fonctionnera en cas de besoin, mais si vous prévoyez de travailler extensivement avec les cookies, regardez des bibliothèques comme [JavaScript Cookie](https://github.com/js-cookie/js-cookie) ou [Cookie Parser](https://github.com/expressjs/cookie-session).

## Préoccupations de sécurité avec les cookies

En général, les cookies sont très sécurisés lorsqu'ils sont mis en œuvre correctement. Les navigateurs ont beaucoup de limitations intégrées que nous avons couvertes précédemment, en partie en raison de l'âge de la technologie, mais aussi pour améliorer la sécurité.

Néanmoins, il existe quelques façons pour un acteur malveillant de voler votre cookie et de l'utiliser pour semer le chaos.

Nous allons passer en revue quelques façons courantes dont cela peut se produire, et examiner différentes façons de le corriger.

De plus, notez que tous les extraits de code seront en JavaScript vanilla. Si vous souhaitez mettre en œuvre ces correctifs sur le serveur, vous devrez chercher la syntaxe exacte pour votre langage ou framework.

### Attaques de l'homme du milieu

Une attaque de l'homme du milieu (MitM) décrit une large catégorie d'attaques où un attaquant se place entre un client et un serveur et intercepte les données allant entre les deux.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/man-in-the-middle-attack-how-avoid.png)
_Source : [Man-in-the-Middle Attacks and How To Avoid Them](https://www.netsparker.com/blog/web-security/man-in-the-middle-attack-how-avoid/)_

Cela peut être fait de nombreuses façons : en obtenant l'accès ou en écoutant un site web non sécurisé, en imitant un routeur WiFi public, en usurpant le DNS, ou par le biais de logiciels malveillants/adware comme [SuperFish](https://en.wikipedia.org/wiki/Superfish).

Voici un aperçu de haut niveau des attaques MitM, et comment les sites web peuvent se protéger eux-mêmes et leurs utilisateurs.

Avertissement : Le début de la vidéo parle de Marie, Reine des Écossais, et montre une représentation animée de sa décapitation. Ce n'est pas excessivement macabre, mais si vous souhaitez l'éviter, avancez jusqu'à [ce timestamp](https://youtu.be/8OR2dDIaIDw?t=57) :

%[https://www.youtube.com/watch?v=8OR2dDIaIDw]

En tant que développeur, vous pouvez grandement réduire les chances d'une attaque MitM en vous assurant que vous activez HTTPS sur votre serveur, utilisez un certificat SSL d'une autorité de certification de confiance, et assurez-vous que votre code utilise HTTPS au lieu du HTTP non sécurisé.

En termes de cookies, vous devriez ajouter l'attribut `Secure` à vos cookies afin qu'ils ne puissent être envoyés que sur une connexion HTTPS sécurisée :

```js
document.cookie = 'dark_mode=false; Secure';
```

Rappelez-vous simplement que l'attribut `Secure` ne crypte pas réellement les données de votre cookie – il garantit simplement que le cookie ne peut pas être envoyé sur une connexion HTTP.

Cependant, un acteur malveillant pourrait toujours éventuellement intercepter et manipuler le cookie. Pour empêcher cela, vous pouvez également utiliser le paramètre `HttpOnly` :

```js
document.cookie = 'dark_mode=false; Secure; HttpOnly';
```

Les cookies avec `HttpOnly` ne peuvent être accessibles que par le serveur, et non par l'API `Document.cookie` du navigateur. Cela est parfait pour des choses comme une session de connexion, où seul le serveur a vraiment besoin de savoir si vous êtes connecté à un site, et vous n'avez pas besoin de cette information côté client.

### Attaques XSS

Une attaque XSS (cross-site scripting) décrit une catégorie d'attaques lorsqu'un acteur malveillant injecte du code non intentionnel, potentiellement dangereux, dans un site web.

Ces attaques sont très problématiques car elles pourraient affecter chaque personne qui visite le site.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/cross-site-scripting.svg)
_Source : [Cross-site scripting](https://portswigger.net/web-security/cross-site-scripting)_

Par exemple, si un site a une section de commentaires et que quelqu'un est capable d'inclure du code malveillant en tant que commentaire, il est possible que chaque personne qui visite le site et lit ce commentaire soit affectée.

En termes de cookies, si un acteur malveillant réussit une attaque XSS sur un site, il pourrait obtenir l'accès aux cookies de session et accéder au site en tant qu'un autre utilisateur connecté. À partir de là, il pourrait être en mesure d'accéder aux paramètres de l'autre utilisateur, d'acheter des choses en tant que cet utilisateur et de les faire livrer à une autre adresse, et ainsi de suite.

Voici une vidéo qui donne un aperçu de haut niveau des différents types de XSS – Réfléchi, Stocké, Basé sur le DOM, et Mutation :

%[https://www.youtube.com/watch?v=EoaDgUgS6QA]

En tant que développeur, vous voudrez vous assurer que votre serveur applique la politique de même origine, et que toute entrée que vous recevez des personnes est correctement assainie.

Et comme pour la prévention des attaques MitM, vous devriez définir les paramètres `Secure` et `HttpOnly` avec tous les cookies que vous utilisez :

```js
document.cookie = 'dark_mode=false; Secure; HttpOnly';
```

### Attaques CSRF

Une attaque CSRF (cross-site request forgery) est lorsqu'un acteur malveillant trompe une personne pour qu'elle effectue une action non intentionnelle, potentiellement malveillante.

Par exemple, si vous êtes connecté à un site et cliquez sur un lien dans un commentaire, si ce lien fait partie d'une attaque CSRF, il peut vous amener à changer involontairement vos détails de connexion, ou même à supprimer votre compte.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/cross-site-request-forgery.svg)
_Source : [Cross-site request forgery](https://portswigger.net/web-security/csrf)_

Bien que les attaques CSRF soient quelque peu liées aux attaques XSS, spécifiquement les attaques XSS réfléchies où quelqu'un insère du code malveillant dans un site, chacune exploite un type de confiance différent.

Selon [Wikipedia](https://en.wikipedia.org/wiki/Cross-site_request_forgery), tandis que XSS "exploite la confiance qu'un utilisateur a pour un site particulier, CSRF exploite la confiance qu'un site a dans le navigateur d'un utilisateur".

Voici une vidéo qui explique les bases de CSRF, et donne quelques exemples utiles :

%[https://www.youtube.com/watch?v=eWEgUcHPle0]

En ce qui concerne les cookies, une façon de prévenir les attaques CSRF possibles est avec le drapeau `SameSite` :

```js
document.cookie = 'dark_mode=false; Secure; HttpOnly; SameSite=Strict';
```

Il y a quelques valeurs que vous pouvez définir pour `SameSite` :

* `Lax` : Les cookies ne sont pas envoyés pour le contenu intégré (images, iframes, etc.) mais sont envoyés lorsque vous cliquez sur un lien ou envoyez une requête à l'origine pour laquelle le cookie est défini. Par exemple, si vous êtes sur `testing.com` et que vous cliquez sur un lien pour aller à `test.com/about`, votre navigateur enverra votre cookie pour `test.com` avec cette requête
* `Strict` : Les cookies ne sont envoyés que lorsque vous cliquez sur un lien ou envoyez une requête depuis l'origine pour laquelle le cookie est défini. Par exemple, votre cookie `test.com` ne sera envoyé que lorsque vous êtes dans et autour de `test.com`, et non depuis d'autres sites comme `testing.com`
* `None` : Les cookies seront envoyés avec chaque requête, indépendamment du contexte. Si vous définissez `SameSite` sur `None`, vous devez également ajouter l'attribut `Secure`. Il est préférable d'éviter cette valeur si possible

Les principaux navigateurs gèrent `SameSite` un peu différemment. Par exemple, si `SameSite` n'est pas défini sur un cookie, Google Chrome le définit sur `Lax` par défaut.

## Alternatives aux cookies

Vous vous demandez peut-être, s'il y a tant de failles de sécurité potentielles avec les cookies, pourquoi les utilisons-nous encore ? Il doit sûrement y avoir une meilleure alternative.

De nos jours, vous pouvez utiliser soit `sessionStorage` soit `localStorage` pour stocker des informations qui utilisaient à l'origine des cookies. Et pour les sessions avec état, il y a l'authentification basée sur des jetons avec des choses comme JWT (JSON Web Tokens).

Bien qu'il puisse sembler que vous devez choisir entre l'authentification basée sur les cookies ou basée sur les jetons, il est possible d'utiliser les deux. Par exemple, vous pourriez vouloir utiliser l'authentification basée sur les cookies lorsqu'une personne se connecte via le navigateur, et l'authentification basée sur les jetons lorsqu'une personne se connecte via une application mobile.

Pour compliquer un peu plus les choses, les fournisseurs d'authentification en tant que service comme Auth0 vous permettent de faire les deux types d'authentification.

Si vous souhaitez en savoir plus sur les jetons web et l'authentification basée sur les jetons, consultez certains de nos articles [ici](https://www.freecodecamp.org/news/search/?query=web%20tokens).

## Quand vous donnez un cookie à un développeur

C'est tout ! Cela devrait être à peu près tout ce que vous devez savoir pour commencer à utiliser les cookies, et ce à quoi faire attention en cours de route.

Avez-vous trouvé cela utile ? Comment utilisez-vous les cookies ? Faites-le moi savoir sur [Twitter](https://twitter.com/kriskoishigawa).
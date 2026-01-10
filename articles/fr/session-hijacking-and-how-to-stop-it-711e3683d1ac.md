---
title: Qu'est-ce que le détournement de session et comment l'empêcher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T14:30:46.000Z'
originalURL: https://freecodecamp.org/news/session-hijacking-and-how-to-stop-it-711e3683d1ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IpyNijir6izjsjs2kW6ADA.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le détournement de session et comment l'empêcher
seo_desc: 'By Ramesh Lingappa


  This story is for beginners and anyone who has a basic understanding about cookies
  (sessions cookies), but who’s not sure how to secure them properly. You don’t have
  to be a security expert to do that. You just have to understand ...'
---

Par Ramesh Lingappa

> _Cet article s'adresse aux débutants et à toute personne ayant une compréhension de base des cookies (cookies de session), mais qui n'est pas sûre de la manière de les sécuriser correctement. Vous n'avez pas besoin d'être un expert en sécurité pour cela. Vous devez simplement comprendre le processus et vous saurez comment faire._

Si vous n'avez aucune idée des cookies ou de leur fonctionnement, veuillez lire cet article sur les [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).

Commençons ! Vous avez une application web incroyable offrant un excellent service aux clients. Cela signifie que vous aurez un mécanisme d'**authentification** pour permettre à l'utilisateur d'accéder à votre application. Vous savez à quel point la sécurité est importante. Vous avez mis en place toutes sortes de mesures de sécurité lors de l'authentification. **Super !**

Après une authentification réussie, vous devez créer une **session** pour cet utilisateur. Cela signifie que vous créez en réalité un **cookie** et que vous l'envoyez au navigateur. Par exemple, dans une application web Java, par défaut, il s'appelle **JSESSIONID**. Cela ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*C7TCffrIAgtzkEnnS2fW3Q.png)
_Informations sur les cookies depuis la console de développement Chrome -> Applications -> Cookies_

En utilisant ce cookie, seul votre serveur web est capable d'identifier qui est l'utilisateur et il fournira le contenu en conséquence. Et ce cookie semble parfait. Aucune information sensible dans le cookie, juste un identifiant aléatoire (non devinable). Donc l'utilisateur est **en sécurité !** ... n'est-ce pas ?

Eh bien, pas exactement, examinons cela de plus près.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0z9yq3Ti01YFUiZmN3bRdg.png)

Il y a deux propriétés dans ce cookie : **HttpOnly (HTTP)** et **Secure**. Leurs valeurs sont vides, ce qui signifie **non activé pour ce cookie**. C'est là que cela devient dangereux.

C'est là que le détournement de session entre en jeu.

> Le **détournement de session**, parfois également appelé détournement de **cookie**, est l'exploitation d'une session informatique valide — parfois également appelée clé de **session** — pour obtenir un accès non autorisé à des informations ou à des services dans un système informatique. — [Wikipedia](https://en.wikipedia.org/wiki/Session_hijacking)

Il s'agit donc de l'acte de voler l'identifiant de session d'un client, ce qui permet d'accéder à votre application web comme si vous étiez ce client.

**Est-ce possible ? Comment obtiennent-ils cet identifiant de session qui se trouve dans le navigateur de l'utilisateur ?**

Oui, c'est possible. Les deux propriétés de cookie (ou indicateurs) que nous avons vues précédemment (**HttpOnly** et **Secure**) en sont la raison.

### **Indicateur HttpOnly**

> Les cookies `**HttpOnly**` sont inaccessibles à l'API JavaScript `[**Document.cookie**](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)` ; ils sont uniquement envoyés au serveur. Par exemple, les cookies qui maintiennent les sessions côté serveur n'ont pas besoin d'être disponibles pour JavaScript, et l'indicateur `HttpOnly` doit être défini.

En termes simples, si vous ne définissez pas l'indicateur httpOnly, votre cookie est lisible depuis le code JavaScript côté client.

Ouvrez n'importe quelle page web dont le cookie n'a pas l'indicateur httpOnly défini. Ensuite, ouvrez la **console de développement Chrome** puis l'onglet **Console** (Cmd + Maj + J ou Ctrl + Maj + J). Tapez `_document.cookie_` et appuyez sur Entrée, et vous verrez quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5Y26jhjlgFFrvi0XFnJa6g.png)
_utilisation de document.cookie_

Comme vous pouvez le voir, vous obtenez toutes les informations sur les cookies. Un attaquant JavaScript peut simplement poster cela sur son propre serveur pour une utilisation ultérieure.

Vous vous demandez peut-être comment ils peuvent écrire ce code dans votre application. Cela est possible de plusieurs manières.

Une façon est d'injecter une bibliothèque JS tierce **non fiable** comme des utilitaires de journalisation, d'assistance, etc. Lisez cet article [**Je récolte des numéros de carte de crédit et des mots de passe depuis votre site. Voici comment**](https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5)**.**

Une autre façon est d'utiliser une [**attaque par script inter-site**](https://www.owasp.org/index.php/Cross-site_Scripting_%28XSS%29)**.** Nous n'allons pas entrer dans les détails, mais sachez que cela peut être fait.

#### **Comment y remédier ?**

Le cookie de session n'a même pas besoin d'être accessible par le client JavaScript. Il n'est nécessaire que pour le serveur. Nous devrions le rendre accessible uniquement pour le serveur. Cela peut être fait en ajoutant un mot (**httpOnly**) dans votre en-tête de réponse http **_set_cookie_**. Comme ceci :

```
Set-Cookie: JSESSIONID=T8zK7hcII6iNgA; Expires=Wed, 21 May 2018 07:28:00 GMT; HttpOnly
```

En ajoutant l'indicateur **httpOnly**, vous indiquez au navigateur que ce cookie ne doit pas être lu par le code JavaScript. Le navigateur se chargera du reste. Voici à quoi cela ressemble après avoir ajouté l'indicateur httpOnly :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qjk5J3R-k88qpkMq5wkYJg.png)
_cookie défini avec l'indicateur httpOnly_

Remarquez la coche dans la propriété HTTP. Cela indique que **httpOnly** est activé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qD_G_6aUnj8LaDbPdHY9mA.png)

Ici, vous pouvez voir que **_document.cookie_** ne retourne pas notre cookie de session. Cela signifie qu'aucun JS ne peut le lire, y compris les scripts externes.

C'est tout — un problème résolu, un autre à venir !

### Indicateur Secure

L'indicateur **secure** indique au navigateur que le cookie ne doit être renvoyé à l'application que via des connexions chiffrées, c'est-à-dire une connexion HTTPS.

Ainsi, lorsqu'un cookie est envoyé au navigateur avec l'indicateur **secure**, et que vous faites une requête à l'application en utilisant HTTP, le navigateur n'attachera pas ce cookie à la requête. Il ne l'attachera que dans une requête HTTPS. La requête HTTPS sera chiffrée, donc les cookies seront envoyés en toute sécurité sur le réseau vers votre application.

**Comment quelqu'un peut-il lire le cookie dans la requête HTTP ?**

Cela peut être réalisé lorsqu'une personne (appelée attaque de **l'homme du milieu**) surveille tout le trafic dans le réseau des clients. Ils sont capables de voir les données en texte clair si la requête est en _HTTP_.

Lorsque c'est envoyé via _HTTPS_, toutes les données seront chiffrées depuis le navigateur et envoyées sur le réseau. L'attaquant ne pourra pas obtenir les données brutes que vous envoyiez. Ni ne pourra-t-il déchiffrer le contenu. C'est pourquoi l'envoi de données via SSL est sécurisé.

#### Comment y remédier ?

Tout comme l'indicateur httpOnly, vous devez simplement ajouter l'indicateur **secure** dans votre en-tête de réponse HTTP **_set_cookie_**. Comme ceci :

```
Set-Cookie: JSESSIONID=T8zK7hcII6iNgA; Expires=Wed, 21 May 2018 07:28:00 GMT; HttpOnly; Secure
```

En Java, cela peut être fait de plusieurs manières. Si vous utilisez Servlet 3.0 ou une version ultérieure, vous pouvez configurer ces paramètres dans **_web.xml_** comme ceci :

```
<session-config>    <cookie-config>        <http-only>true</http-only>        <secure>true</secure>    </cookie-config> </session-config>
```

Si votre environnement ne le supporte pas, vous pouvez l'ajouter manuellement. Par exemple, en utilisant des Servlets, vous pouvez faire ceci :

Enfin, voici à quoi cela ressemble lorsque les deux indicateurs sont définis,

![Image](https://cdn-media-1.freecodecamp.org/images/1*zhc23uSW0I1enxdqSUWN3Q.png)

### Conclusion

Ainsi, lorsque vous traitez des cookies de session ou d'autres cookies importants, assurez-vous d'ajouter ces deux indicateurs.

Merci d'avoir lu, **Bonne sécurisation !**
---
title: Cross Site Request Forgery – Qu'est-ce qu'une attaque CSRF et comment la prévenir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-03T16:13:55.000Z'
originalURL: https://freecodecamp.org/news/what-is-cross-site-request-forgery
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/megan-article-image.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Cross Site Request Forgery – Qu'est-ce qu'une attaque CSRF et comment la
  prévenir
seo_desc: 'By Megan Kaczanowski

  Cross Site Request Forgery, or CSRF occurs when a malicious site or program causes
  a user''s browser to perform an unwanted action on a trusted site when the user
  is authenticated. Any malicious action is limited to the capability...'
---

Par Megan Kaczanowski

Le Cross Site Request Forgery, ou CSRF, se produit lorsqu'un site ou un programme malveillant amène le navigateur d'un utilisateur à effectuer une action non souhaitée sur un site de confiance alors que l'utilisateur est authentifié. Toute action malveillante est limitée à la capacité du site web auprès duquel l'utilisateur est authentifié.

Par exemple, Jane pourrait se connecter à son portail bancaire en ligne tout en consultant ses e-mails. Pendant ce temps, elle pourrait cliquer sur un lien dans un e-mail de phishing (probablement masqué par un site de réduction de liens) qui inclurait une requête demandant à la banque de Jane de transférer de l'argent vers un compte contrôlé par l'attaquant. 

Comme Jane est déjà authentifiée par sa banque, celle-ci effectue automatiquement la transaction, pensant que, parce qu'elle est demandée par le navigateur de Jane, celle-ci l'a autorisée. 

## Que sont les requêtes HTTP et les cookies ?

### Requête HTTP GET

Il s'agit d'une requête utilisée pour demander des données à un serveur web (par exemple, taper une URL (demander un site web) ce qui entraîne son chargement).

### Requête HTTP POST

Il s'agit d'une requête utilisée pour envoyer des données à un serveur web (par exemple, la soumission d'un formulaire web).

Certaines requêtes GET et POST sont déclenchées automatiquement, sans interaction de l'utilisateur (comme la récupération de suggestions de recherche ou le chargement de contenu d'image avec l'attribut img src).

### Cookies de session

Les cookies de session sont un moyen pour le protocole HTTP de gérer l'état (puisqu'il ne gère pas l'état nativement). Les sites web utilisent des cookies de session (contenant un ID unique) pour identifier les utilisateurs et conserver leur session. 

Après avoir été défini, le navigateur de l'utilisateur envoie le cookie au serveur à chaque requête qu'il effectue afin d'identifier l'utilisateur auprès du site. 

Un attaquant peut exploiter le cookie pour usurper l'identité de l'utilisateur en forçant le navigateur de ce dernier à exécuter une requête. Si l'utilisateur est déjà connecté au site, le cookie sera envoyé automatiquement avec la requête. 

## Comment fonctionne le Cross Site Request Forgery ?

Pour qu'un attaquant puisse mener une attaque CSRF, plusieurs conditions doivent être réunies :

* Il existe une action dans l'application que l'attaquant souhaite effectuer – comme changer un mot de passe, transférer des fonds, etc.
* Il n'y a pas de paramètres de requête imprévisibles – l'attaquant peut deviner (ou connaît) tous les paramètres que l'application s'attend à voir pour ce type de requête.
* L'action peut être effectuée par une ou plusieurs requêtes HTTP et elle repose uniquement sur les cookies pour vérifier que la requête provient de l'utilisateur.

Le CSRF peut impacter les applications web qui utilisent des cookies, l'authentification par navigateur ou des certificats côté client pour authentifier les utilisateurs. Essentiellement, cela peut se produire dans tous les cas où l'application ajoute automatiquement les identifiants ou l'identité d'un utilisateur à une requête.

Une attaque CSRF peut exploiter soit une requête GET, soit une requête POST (bien qu'une requête POST soit plus compliquée et donc moins courante). 

Dans les deux cas, l'attaquant doit commencer par piéger une victime pour qu'elle charge ou soumette les informations à une application web. Cela peut se faire de plusieurs manières – par exemple via un lien de phishing. 

Alternativement, tout comme le XSS (Cross-site scripting), le CSRF peut être une vulnérabilité stockée. Le CSRF stocké se produit lorsqu'un attaquant stocke l'attaque dans un champ qui accepte le HTML, tel qu'une balise IMG ou IFRAME. Cela signifierait que toute personne consultant la page pourrait être impactée. L'exploit peut être déguisé en un lien ordinaire ou caché dans une balise d'image.

Par exemple, sous forme de lien ordinaire sur une page web : `<a href="malicious link">Se désabonner ici</a>`

Ou sous forme de balise d'image : `<img src="malicious link" width="0" height="0" border="0">`

## Exemple de CSRF

Imaginez que votre banque (bank.com) traite les transferts à l'aide de requêtes GET qui incluent plusieurs paramètres (l'identité du destinataire du transfert et le montant que vous souhaitez transférer). 

Par exemple, si Jim veut envoyer 10 $ à son ami Bob, la requête pourrait ressembler à ceci :

`http://bank.com/transfer?recipient=Bob&amount=10`

La requête inclut également un cookie de session identifiant le propriétaire du compte afin que la banque sache où prendre l'argent. 

Maintenant, un attaquant peut convaincre Jim de cliquer sur un lien qui ressemble à ceci (mais qui a été raccourci par un réducteur d'URL ou lié intelligemment par un hyperlien) :

`http://bank.com/transfer?recipient=Hacker&amount=100000`

Comme Jim est déjà connecté, son navigateur envoie son cookie avec la requête – la banque croit donc qu'il demande le transfert et celui-ci est effectué.

## Comment arrêter les attaques CSRF

### Choisissez vos Frameworks avec soin

Utilisez des frameworks qui intègrent des protections contre le CSRF, comme .NET. Une configuration correcte est essentielle. Si le framework que vous utilisez n'a pas de protection, vous pouvez en ajouter une avec des jetons Anti-CSRF.

### Utilisez des jetons Anti-CSRF

Les jetons (également connus sous le nom de "synchronizer token patterns") sont une protection côté serveur où le serveur fournit au navigateur d'un utilisateur un jeton unique, généré de manière aléatoire, et vérifie chaque requête pour voir si le navigateur le renvoie avant d'exécuter une requête. 

Ce jeton est envoyé via un champ caché et doit être un nombre aléatoire non prévisible qui expire après un court laps de temps et ne peut pas être réutilisé. 

Selon la sensibilité de la page, différents jetons peuvent être utilisés pour chaque requête, ou simplement pour différents formulaires. Les jetons doivent être comparés de manière sécurisée (par exemple en comparant des hachages) et ne doivent pas être envoyés dans une requête HTTP GET afin qu'ils ne fassent pas partie de l'URL et ne puissent pas fuiter via l'en-tête Referrer.

### Utilisez le flag SameSite dans les cookies

Le flag SameSite marque un cookie afin qu'il ne puisse être envoyé que pour des requêtes provenant du même domaine. 

Essentiellement, si www.bank.com veut faire une requête vers `www.bank.com/updatepassword`, il y est autorisé. Mais si `www.maliciousdomain.com` veut faire une requête vers www.bank.com/updatepassword, il ne peut pas envoyer le cookie de session et ne peut donc pas mener l'attaque. 

La plupart des navigateurs supportent désormais ce flag, mais pas tous. Il devrait faire partie d'une stratégie de défense globale. 

### Pratiquez la défense en profondeur

Vous pouvez mettre en œuvre un certain nombre d'autres contrôles qui, lorsqu'ils sont utilisés conjointement avec d'autres mesures, peuvent offrir une protection contre le CSRF. 

Par exemple, voici d'autres protections que vous pouvez mettre en place :

* vérifier l'origine avec des en-têtes standards (déterminer d'où provient la requête et vers où elle est dirigée pour s'assurer qu'elles correspondent)
* utiliser un en-tête de requête personnalisé (de sorte que sans l'en-tête, le site n'acceptera pas la requête)
* double soumission de cookies (essentiellement un second paramètre, généré de manière aléatoire et inconnu de l'attaquant, que ce dernier doit soumettre avec une requête pour qu'elle réussisse).

### Impliquez l'utilisateur dans la transaction

Pour les actions sensibles telles que les transferts d'argent ou les changements de mot de passe, exigez que l'utilisateur entreprenne une action (telle qu'un CAPTCHA, des jetons à usage unique ou une ré-authentification).

## Exemples de mesures qui ne fonctionnent pas :

* **Transactions en plusieurs étapes :** Le nombre d'étapes importe peu tant que l'attaquant peut prédire ou déterminer chacune d'elles.
* **HTTPS :** C'est toujours une bonne idée, mais cela ne fait rien pour protéger contre le CSRF.
* **Réécriture d'URL :** Cela empêcherait les attaquants de deviner l'ID de session de la victime lors d'une attaque CSRF, mais permettrait ensuite à un attaquant de le voir dans l'URL. Échanger une faille contre une autre n'est pas une bonne idée.
* **Utilisation d'un cookie secret :** Même un cookie secret est soumis dans le cadre de la requête, ce qui signifie que l'attaquant peut toujours l'exploiter.
* **Accepter uniquement les requêtes POST / éviter les requêtes GET :** Des requêtes POST forgées peuvent toujours être utilisées pour exécuter une attaque CSRF.

### Autres noms pour le CSRF

Le CSRF est également connu sous les noms de XSRF, Sea Surf, Session Riding, Cross-Site Reference Forgery, Hostile Linking, One-Click Attack.

### Sources / Lectures complémentaires :

* [OWASP CSRF](https://owasp.org/www-community/attacks/csrf)
* [Prévention CSRF OWASP](https://owasp.org/www-community/attacks/csrf)
* [Attaques CSRF](https://www.netsparker.com/blog/web-security/csrf-cross-site-request-forgery/)
* [Jetons Anti-CSRF](https://www.netsparker.com/blog/web-security/protecting-website-using-anti-csrf-token/)
* [Bases du CSRF](https://www.acunetix.com/websitesecurity/csrf-attacks/)
* [PortSwigger CSRF](https://portswigger.net/web-security/csrf)
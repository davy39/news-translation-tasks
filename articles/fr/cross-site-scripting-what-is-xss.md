---
title: Qu'est-ce que le Cross Site Scripting ? Comment se protéger contre les attaques
  XSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-09T17:27:40.000Z'
originalURL: https://freecodecamp.org/news/cross-site-scripting-what-is-xss
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-207580.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Qu'est-ce que le Cross Site Scripting ? Comment se protéger contre les
  attaques XSS
seo_desc: "By Megan Kaczanowski\nCross Site Scripting is the second most prevalent\
  \ issue in the Open Source Foundation for Application Security (OWASP) top 10 –\
  \ it's found in roughly 2/3 of all applications. \nWhile automated tools can find\
  \ some of these problems..."
---

Par Megan Kaczanowski

Le Cross Site Scripting est le deuxième problème le plus prévalent dans le top 10 de l'Open Source Foundation for Application Security (OWASP) – il est trouvé dans environ 2/3 de toutes les applications. 

Bien que les outils automatisés puissent trouver certains de ces problèmes, il existe également des outils automatisés conçus pour détecter et exploiter ces vulnérabilités.

## Qu'est-ce que le Cross-Site Scripting ?

Les attaques XSS se produisent lorsque des données entrent dans une application web via une source non fiable (comme une requête web), et sont envoyées à un utilisateur sans être validées. 

Le XSS peut provoquer l'exécution de scripts dans le navigateur de l'utilisateur, entraînant des sessions détournées, la défiguration de sites web et la redirection des utilisateurs vers des sites malveillants. 

Essentiellement, un attaquant insère du code malveillant dans une section destinée à la saisie utilisateur, que le serveur considère comme des données (mais qui est en réalité du code conçu pour être exécuté). 

Et si vous ne le gérez pas correctement, le code malveillant peut sortir du 'plan de données' et s'exécuter comme du code normal (le 'plan de contrôle').

Nous pouvons regrouper la plupart des attaques XSS en deux catégories : stockées et réfléchies. Un troisième type, moins courant, est appelé XSS basé sur le DOM. 

Toute attaque XSS se produit lorsque des données entrent via une source non fiable et sont envoyées à un utilisateur (dans du contenu dynamique) sans être vérifiées pour du contenu malveillant. Le contenu malveillant peut être du JavaScript, du Flash, du HTML, ou tout autre code qu'un navigateur est capable d'exécuter.

### XSS Réfléchi (Impact : Modéré)

Il s'agit du type de XSS le plus basique, dans lequel une application reçoit des données puis inclut ces données dans la réponse à l'utilisateur de manière non sécurisée.

Par exemple, si un attaquant convainc un utilisateur de cliquer sur ce lien de phishing :

http://legitwebsite.com/message=<script>code malveillant</script>

Si le site légitime ne traite pas les données et les retourne simplement à l'utilisateur, le navigateur de l'utilisateur exécutera le code malveillant.

### XSS Stocké (Impact : Sévère) 

Le XSS stocké se produit lorsque l'injection est stockée de manière permanente sur les serveurs de la cible, comme un message dans un forum ou une section de commentaires, dans une base de données, etc. Essentiellement, cela signifie que l'exploit impacte chaque visiteur du site/application.

Par exemple, si un site permet aux utilisateurs de commenter et affiche ensuite leurs commentaires, un utilisateur pourrait entrer ce qui suit :

<p><script>code malveillant</script></p>

Si le site ne vérifie pas correctement la saisie utilisateur, cela pourrait entraîner l'exécution du script pour tout autre utilisateur qui voit ce message.

### XSS Basé sur le DOM/XSS Côté Client (Impact : Modéré)

La grande différence entre le XSS réfléchi, le XSS stocké et le XSS basé sur le DOM réside dans l'endroit où l'attaque est injectée. 

Le XSS réfléchi et le XSS stocké sont des problèmes côté serveur, tandis que le XSS basé sur le DOM est un problème côté client (navigateur). Le XSS basé sur le DOM se produit dans le DOM (modèle d'objet de document) au lieu de faire partie du HTML. 

Plutôt que d'insérer du code malveillant dans la page, cette attaque permettra à la page légitime de se charger, puis exploitera la saisie utilisateur pour ajouter du HTML à la page, exécutant le script malveillant. Cela tire parti des quantités croissantes de HTML générées par le client. 

Par exemple, un attaquant pourrait inciter une victime à cliquer sur un lien malveillant (tel que http://www.legitimatewebsite.com/contact#<script>code malveillant</script>). Le site web recevra la requête légitime pour la page, mais pas le fragment malveillant (car les navigateurs n'envoient rien après le caractère # au serveur du site). La victime verra le site web légitime, mais le navigateur de la victime exécutera également le script malveillant.

En raison du fonctionnement de cette attaque, les protections côté serveur ne l'empêcheront pas, car le code malveillant n'est pas du tout envoyé au serveur. 

Au lieu de cela, la protection contre cette attaque nécessite de s'assurer que JavaScript n'interprète pas les fragments d'URI (identifiant de ressource uniforme - un URI identifie une ressource à un emplacement spécifié tel qu'une URL) de manière non sécurisée.

## Mesures de Mitigation pour les Attaques XSS

Pour se protéger efficacement contre les attaques XSS, il est nécessaire de combiner les mesures suivantes, qui, utilisées ensemble, peuvent offrir une défense robuste contre le XSS.

### Éviter d'insérer des données fournies par l'utilisateur/non fiables ailleurs que dans des emplacements spécifiés

Il s'agit de la première et de la plus importante règle. L'encodage, l'échappement, la validation et le filtrage des entrées sont extrêmement difficiles et très compliqués. 

Il est beaucoup plus facile de limiter le nombre d'endroits où quelqu'un peut insérer des données non fiables. L'hypothèse la plus sûre est que toutes les données non fiables sont malveillantes.

### Valider/Filtrer les Entrées

Idéalement, toutes les entrées doivent être validées par rapport à une liste de valeurs acceptables.

### Encoder la Sortie

Toutes les données saisies par l'utilisateur doivent être encodées pour empêcher qu'elles soient lues comme actives. Cela peut nécessiter un encodage CSS, JavaScript, URL et/ou HTML. 

Il est particulièrement important de s'assurer que la sortie est encodée à tout point où elle est exposée, car les mêmes données pourraient être stockées et affichées à plusieurs endroits.

### Choisir les Frameworks avec Soin

Utilisez des frameworks qui offrent une fonctionnalité d'échappement automatique (comme Go Templates) ou ceux qui ont des défenses natives contre le XSS (comme la validation des requêtes de .NET). 

### Définir le Flag HttpOnly

Les attaques XSS utilisent souvent JavaScript pour voler les cookies de session (et les applications web normales ont rarement besoin d'utiliser JavaScript pour accéder aux cookies de session). Ainsi, la définition du flag HttpOnly protège les cookies de session des attaquants, sans limiter le comportement normal. La plupart des navigateurs supportent la définition de ce flag.

### Utiliser les En-têtes de Réponse

Similaires aux flags HttpOnly, toutes les réponses HTTP qui ne devraient pas contenir de HTML ou de JavaScript peuvent utiliser les en-têtes 'Content-Type' et 'X-Content-Type-Options' pour s'assurer que les navigateurs n'interprètent les réponses que de la manière prévue.

### Éduquer les Développeurs sur la Sécurité

L'éducation spécifiquement ciblée sur les développeurs, comme les programmes 'Security Champions' qui associent des membres de l'équipe de sécurité des applications avec des développeurs, est importante. Ils peuvent aider à éduquer les développeurs sur les vulnérabilités de sécurité (comme le XSS) et comment les prévenir.

### Avoir une Politique de Sécurité de Contenu

Une politique de sécurité de contenu (CSP) peut vous aider à détecter et à atténuer le XSS et d'autres attaques par injection de données. 

Elles définissent des listes d'autorisation pour les sources de contenu de confiance et peuvent s'appliquer uniquement aux pages sensibles (comme les pages de paiement) ou, idéalement, à l'ensemble du site. Elles peuvent même fournir des notifications si du contenu est chargé à partir d'une page qui ne le devrait pas. 

Elles sont assez faciles à déployer – il suffit d'ajouter l'en-tête HTTP Content-Security-Policy à la page web et toutes les directives appropriées. 

L'[Extension CSP Fiddler](https://github.com/david-risney/CSP-Fiddler-Extension) peut vous aider à générer une CSP de base. L'outil construira une politique autour des rapports soumis par le navigateur, créant une politique de base modifiable. 

De plus, vous pouvez utiliser [Report URI](https://report-uri.com/), géré par Troy Hunt et Scott Helme, pour recevoir des alertes sur les violations de CSP afin de surveiller plus proactivement vos sites.

Typiquement, une politique se compose d'une série de directives qui décrivent la politique pour un type de ressource ou une zone. L'une de ces directives, les vérifications d'intégrité des sous-ressources, est utilisée pour s'assurer qu'un navigateur vérifie que le contenu tiers (provenant de sources comme un CDN) est livré sans être manipulé. 

Essentiellement, un hachage cryptographique fourni doit correspondre au fichier chargé. Si un pirate modifie le contenu du tiers, le site ne chargera tout simplement pas le contenu malveillant. 

Le problème est que si le fournisseur de contenu met à jour le fichier ou apporte des modifications légitimes, le contenu ne sera également pas chargé (car le hachage aura changé). 

La principale façon de contourner ce problème est de tirer parti des ressources JavaScript versionnées, telles que chatbot_0.1.23.js, au lieu de chatbot.js. Il s'agit d'une bonne pratique en général, et elle garantit également la continuité des services si le fichier JS change. 

Bien que les navigateurs ne supportent pas universellement cette fonctionnalité, pour ceux qui ne la supportent pas, son utilisation ne cassera pas le site (il ne tirera tout simplement pas parti de la technologie). 

Pour plus de détails sur les différentes directives, consultez [ces](https://developers.google.com/web/fundamentals/security/csp) [guides](https://content-security-policy.com/).

### Sources/Lectures Complémentaires :

* [Cross-Site Scripting de Troy Hunt](https://www.troyhunt.com/owasp-top-10-for-net-developers-part-2/)
* [Comprendre le XSS - Sémantique de Sanitisation des Entrées et Contextes d'Encodage de Sortie](https://www.troyhunt.com/understanding-xss-input-sanitisation/)
* [OWASP XSS](https://owasp.org/www-community/attacks/xss/)
* [Types de XSS OWASP](https://owasp.org/www-community/Types_of_Cross-Site_Scripting)
* [Prévention du Cross Site Scripting OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-8-prevent-dom-based-xss)
* [XSS Basé sur le DOM OWASP](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [Acunetix Cross Site Scripting](https://www.acunetix.com/websitesecurity/cross-site-scripting/)
* [PortSwigger XSS](https://portswigger.net/web-security/cross-site-scripting)
* [Rapid7 XSS](https://www.rapid7.com/fundamentals/cross-site-scripting/)
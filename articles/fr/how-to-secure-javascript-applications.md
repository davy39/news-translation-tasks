---
title: 'Comment sécuriser les applications JavaScript : vulnérabilités courantes et
  meilleures pratiques'
subtitle: ''
author: Bello Joseph
co_authors: []
series: null
date: '2024-10-24T14:21:34.179Z'
originalURL: https://freecodecamp.org/news/how-to-secure-javascript-applications
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729618116705/41f6dfda-4563-4333-88ad-733238d86ec1.png
tags:
- name: JavaScript
  slug: javascript
- name: Security
  slug: security
- name: Web Development
  slug: web-development
seo_title: 'Comment sécuriser les applications JavaScript : vulnérabilités courantes
  et meilleures pratiques'
seo_desc: JavaScript is a widely used programming language for creating client-side
  and server-side applications. Its use cases go beyond web development, as JavaScript
  is also used in mobile app development and artificial intelligence. This makes JavaScript
  a...
---

JavaScript est un langage de programmation largement utilisé pour créer des applications côté client et côté serveur. Ses cas d'utilisation vont au-delà du développement web, car JavaScript est également utilisé dans le développement d'applications mobiles et l'intelligence artificielle. Cela fait de JavaScript un langage polyvalent.

Mais avec une telle polyvalence viennent des risques. L'utilisation généralisée de JavaScript en fait également une cible de choix pour les attaques.

Tout comme les humains ont développé des systèmes de sécurité complexes pour leurs maisons, tels que des caméras de surveillance et des serrures numériques, les développeurs doivent également protéger leurs applications contre les cyberattaques et les menaces externes.

Cet article vous présentera l'importance de la sécurité dans votre application. Nous discuterons également des vulnérabilités de sécurité courantes en JavaScript et de la manière de prévenir les attaques et de sécuriser votre code JavaScript.

### **Table des matières**

1. [Pourquoi vous devez sécuriser votre application JavaScript](#heading-pourquoi-vous-devez-securiser-votre-application-javascript)

2. [Comprendre les vulnérabilités de sécurité courantes en JavaScript](#heading-comprendre-les-vulnerabilites-de-securite-courantes-en-javascript)

3. [Meilleures pratiques pour sécuriser votre application JavaScript](#heading-meilleures-pratiques-pour-securiser-votre-application-javascript)

4. [Conclusion](#heading-conclusion)

## Pourquoi vous devez sécuriser votre application JavaScript

De nos jours, lors de la construction d'un projet, la plupart des développeurs se concentrent uniquement sur le fonctionnement de l'application et la réplication de la fonctionnalité souhaitée. La sécurité n'est souvent pas une priorité, ce qui a conduit à des problèmes majeurs ces dernières années.

De nombreuses entreprises ont été touchées par des attaques de sécurité, entraînant des pertes de revenus, l'exposition d'informations sensibles des utilisateurs et des dommages à la crédibilité de l'entreprise. Un exemple concret qui illustre parfaitement ce scénario est l'attaque [Segway Magecart](https://threatpost.com/segway-magecart-attack-favicon/177971/).

En 2022, Segway, une entreprise connue pour produire des trottinettes électriques à deux roues, a été victime d'une attaque [Magecart](https://www.akamai.com/glossary/what-is-magecart) dans laquelle les informations de paiement sensibles des utilisateurs ont été exposées aux attaquants. L'attaque Segway Magecart est un exemple bien connu de [digital skimming](https://www.europol.europa.eu/operations-services-and-innovation/public-awareness-and-prevention-guides/digital-skimming).

Les attaquants ont pu voler les informations des utilisateurs en injectant un script qui manipulait le code s'exécutant dans le navigateur web, leur permettant d'accéder aux données saisies sur les pages web des utilisateurs.

L'attaque Segway a exploité une vulnérabilité majeure de JavaScript, à savoir la capacité de JavaScript à exécuter du code côté client. Cela a facilité l'injection et l'exécution de scripts malveillants dans les navigateurs des utilisateurs.

Pour empêcher votre application d'être compromise par des attaquants, il est important de comprendre les vulnérabilités de JavaScript, comment les attaquants exploitent ces vulnérabilités, puis d'apprendre à sécuriser votre application.

## Comprendre les vulnérabilités de sécurité courantes en JavaScript

Les vulnérabilités de sécurité JavaScript sont des faiblesses ou des défauts dans son architecture qui le rendent vulnérable aux attaques. Ces vulnérabilités sont souvent appelées les divers points d'entrée par lesquels les attaquants peuvent pénétrer un programme. Nous explorerons certaines vulnérabilités courantes de JavaScript ci-dessous.

### **1. Cross-Site Scripting (XSS)**

Le Cross-Site Scripting (XSS) est un type d'attaque dans lequel un code malveillant est injecté dans la section frontend d'un site web par des attaquants. Ce code est ensuite exécuté dans les navigateurs des utilisateurs insoupçonnés qui visitent la page web compromise.

Les attaquants XSS utilisent cette méthode pour voler les données des utilisateurs, détourner les données de session et mener d'autres activités malveillantes.

Les attaques XSS sont efficaces car elles exploitent l'incapacité du navigateur à différencier le code de confiance des scripts malveillants injectés par un attaquant. Examinons une analogie pour comprendre comment fonctionnent les attaques XSS.

Imaginez une application web où les utilisateurs peuvent publier des commentaires ou soumettre des données via un formulaire. Prenons, par exemple, une plateforme de forum largement utilisée comme freeCodeCamp. Un attaquant pourrait insérer un script nuisible dans le cadre d'un commentaire. Si l'application ne parvient pas à assainir ou à valider l'entrée de manière efficace, le navigateur exécutera le script malveillant chaque fois que d'autres utilisateurs chargeront la page ou verront ce commentaire.

Voici un exemple de code illustrant cela :

```xml
  <form id="commentForm">
    <textarea id="comment"></textarea>
    <br>
    <button type="submit">Soumettre le commentaire</button>
  </form>
  <div id="commentSection"> 
    <ul id="commentList"></ul> <!--Où le commentaire est affiché -->
  </div>
```

Ici, nous avons un simple formulaire qui soumet un commentaire d'utilisateur.

```javascript
 document.getElementById('commentForm').onsubmit = function(e) {
    e.preventDefault();
    const comment = document.getElementById('comment').value;
    document.getElementById('commentList').innerHTML 
    += `<li>${comment}</li>`; // ligne où l'attaque XSS se produit
  };
```

Maintenant, chaque fois que l'utilisateur soumet un commentaire, JavaScript prend ce commentaire particulier et l'inclut dans notre **structure de page web**. Maintenant, un attaquant connaissant cela pourrait inclure une attaque de script comme ceci dans le formulaire de commentaire.

```javascript
<script>alert('Attaque XSS !')</script>
```

JavaScript prendrait ce code et le **stockerait** dans notre page web comme un commentaire régulier, donc chaque fois qu'un utilisateur charge la page infectée, le script est exécuté. Ce type d'attaque XSS est connu sous le nom de [XSS stocké](https://portswigger.net/web-security/cross-site-scripting/stored).

Pour protéger votre application contre les attaques XSS, il est crucial d'assainir et de valider les entrées et de scanner régulièrement votre code pour détecter les vulnérabilités.

### **2. Cross-Site Request Forgery (CSRF)**

Le Cross-Site Request Forgery (CSRF) fait référence à un type d'attaque où un attaquant trompe le navigateur d'un utilisateur authentifié pour qu'il exécute des actions non désirées en utilisant les identifiants de l'utilisateur. Cela se produit souvent par le biais de techniques d'ingénierie sociale qui amènent le navigateur à envoyer des requêtes sans le savoir ou le consentement de l'utilisateur.

Dans une attaque CSRF, l'attaquant usurpe l'identité de la victime en utilisant les identifiants stockés dans le navigateur de l'utilisateur, tels que les cookies de session, les JWT ou les jetons OAuth. Ils utilisent ces identifiants pour envoyer des requêtes HTTP au serveur du site web, effectuant des actions non autorisées au nom de la victime, telles que le transfert de fonds, ou le changement de l'adresse e-mail ou du mot de passe de l'utilisateur.

Examinons un scénario hypothétique du point de vue d'un attaquant pour mieux comprendre le CSRF.

Imaginez que je suis un attaquant essayant d'utiliser le CSRF pour voler de l'argent du compte bancaire d'une victime insoupçonnée. Voici comment je procéderais :

1. Tout d'abord, je vais créer un formulaire malveillant qui déclenche un transfert de fonds sur le site bancaire de la victime en utilisant une requête POST.

    ```javascript
    <form action="https://victim-bank.com/transfer" method="POST">
      <input type="hidden" name="toAccount" value="attacker-account" />
      <input type="hidden" name="amount" value="1000" />
    </form>
    ```

2. Ensuite, je dois manipuler la victime pour qu'elle visite la page web contenant ce formulaire. Je peux y parvenir de deux manières :

    * **Envoyer le lien de la page par e-mail**, en prétendant qu'il provient de la banque de la victime.

    * **Intégrer le lien** dans une page web qui attire la victime à visiter (par exemple, une fausse promotion ou une offre de cadeau).

3. Maintenant, une fois que la victime **visite** la page web malveillante, si la victime est toujours authentifiée sur le site web cible, le formulaire est exécuté immédiatement et l'argent est transféré sur mon compte.

    ```javascript
      // Soumet automatiquement le formulaire lorsque la page malveillante est chargée
      document.forms[0].submit();
    ```

Pour prévenir les attaques CSRF, vous pouvez implémenter un jeton anti-CSRF dans l'application web. Ce jeton génère un identifiant unique pour chaque session. Lorsque le navigateur fait une requête, le serveur vérifie si le jeton CSRF du navigateur correspond au jeton stocké sur le serveur avant de valider toute action.

### 3. **Vulnérabilités des bibliothèques tierces**

Les développeurs intègrent souvent des packages et bibliothèques externes pour améliorer la fonctionnalité des applications et accélérer le développement. Mais l'intégration de bibliothèques tierces peut introduire des risques de sécurité dans votre application JavaScript.

Le 26 mars 2019, la bibliothèque Bootstrap-Sass version (3.2.0.2) a été supprimée du dépôt officiel RubyGems et remplacée par une version compromise [version (3.2.0.3) qui permettait l'exécution de code à distance](https://www.acunetix.com/blog/web-security-zone/remote-code-execution-bootstrap-sass-ruby-package/). Heureusement, un [utilisateur a remarqué cette anomalie](https://github.com/twbs/bootstrap-sass/issues/1195) et a informé les mainteneurs de Bootstrap-Sass qui ont résolu le problème rapidement.

Avant d'intégrer une bibliothèque tierce dans votre application, examinez-la pour détecter les vulnérabilités et assurez-vous qu'elle est régulièrement maintenue et à jour. Évitez les bibliothèques qui demandent des permissions excessives. Prendre ces précautions aidera à protéger la sécurité de votre application.

### 4. **Désérialisation non sécurisée**

La sérialisation est cruciale dans les applications car les données doivent être stockées et transférées dans des formats que d'autres systèmes peuvent facilement lire et interpréter. Elle implique la conversion des données dans un format lisible par le système (tel que JSON, XML ou binaire) avant qu'elles ne puissent être transmises ou stockées dans un système.

La désérialisation est le **inverse** de ce processus : elle récupère les données sérialisées du système et les restitue dans leur forme originale. Vous pouvez penser à la sérialisation comme à la congélation d'articles alimentaires pour le stockage, et à la désérialisation comme à leur décongélation avant utilisation.

La désérialisation non sécurisée se produit lorsque le processus de transcription des données de leur forme sérialisée à leur forme originale est **intercepté** et manipulé par des attaquants. La désérialisation non sécurisée est dangereuse, car les attaquants peuvent l'utiliser pour altérer le comportement de l'application, se donner un accès non autorisé, et cela peut même conduire à l'exécution de code à distance.

Pour prévenir la désérialisation non sécurisée, il est nécessaire de valider correctement l'entrée de l'utilisateur avant le processus de sérialisation.

### 5. **Attaque par pollution de prototype**

JavaScript est un langage basé sur des prototypes. Cela signifie que lorsqu'un objet est créé, il hérite des méthodes et des propriétés par le biais d'un lien interne vers un autre objet, appelé son prototype. Cette fonctionnalité permet à plusieurs objets de partager des méthodes et des propriétés à partir d'un seul prototype.

Ce processus est rendu possible grâce à un mécanisme connu sous le nom de chaîne de prototypes.

Une chaîne de prototypes est un lien de prototypes. Lorsque vous ne pouvez pas accéder à une méthode ou une propriété particulière d'un objet, JavaScript recherche dans la chaîne de prototypes jusqu'à ce qu'il trouve la méthode ou la propriété, et il s'arrête lorsque la chaîne se termine en `null`.

La pollution de prototype se produit lorsqu'un attaquant injecte des propriétés ou des méthodes dans le prototype d'un objet, affectant tous les objets liés à ce prototype. Cela peut entraîner une corruption des données et une exécution de code à distance.

Pour prévenir la pollution de prototype, utilisez des méthodes de clonage profond et des bibliothèques qui peuvent détecter et prévenir la pollution de prototype.

### 6. **Dépendance exclusive à la validation côté client**

Une application complète (ou full-stack) se compose généralement de deux composants principaux : le côté client (Front end) et le côté serveur (Back end). La validation côté client consiste à vérifier l'entrée de l'utilisateur pour s'assurer qu'elle répond aux exigences du système avant d'envoyer les données au backend.

La validation côté client est importante pour améliorer l'expérience utilisateur. Par exemple, afficher un message d'erreur lorsque l'utilisateur laisse une partie d'un formulaire non remplie, vérifier la force du mot de passe ou s'assurer qu'un utilisateur tape l'adresse e-mail correcte.

Mais se fier uniquement à la validation côté client peut laisser l'application vulnérable aux menaces de sécurité. Les attaquants peuvent contourner JavaScript et injecter des scripts malveillants dans le serveur, entraînant une manipulation des données, une exécution de code à distance et un accès non autorisé à l'application.

Pour garantir un niveau élevé de sécurité dans votre application, il est recommandé de valider à la fois côté client et côté serveur.

### 7. **Exposition de données sensibles**

L'exposition de données sensibles se produit lorsque des informations critiques comme les identifiants de connexion, les clés d'authentification, les clés API ou les informations personnellement identifiables (PII) sont exposées, permettant à des individus non autorisés d'y accéder.

L'exposition de données sensibles peut se produire de plusieurs manières, telles que :

* Stocker des informations sensibles (comme les jetons d'authentification) en utilisant des mécanismes de stockage du navigateur comme localstorage et sessionstorage.

* Ne pas crypter ou hacher les mots de passe, les laissant en texte brut.

* Laisser vos clés API visibles dans votre code JavaScript.

* Ne pas crypter les données en transit en utilisant HTTP au lieu de HTTPS.

Faire fuir des données sensibles dans votre application, c'est comme écrire votre code PIN sur votre carte de crédit ou garder vos objets de valeur dans un coffre sans serrure. L'exposition de données entre de mauvaises mains peut entraîner de graves problèmes, car les attaquants peuvent voler les identifiants de connexion ou les jetons d'authentification d'un utilisateur et siphonner d'autres informations importantes.

Maintenant que nous avons couvert certaines vulnérabilités de sécurité courantes en JavaScript, examinons diverses façons de sécuriser notre application JavaScript contre ces vulnérabilités.

## Meilleures pratiques pour sécuriser votre application JavaScript

### 1. **Assurez-vous que l'entrée de l'utilisateur est assainie et validée**

Une manière majeure par laquelle les applications JavaScript sont compromises provient de l'entrée de l'utilisateur.

Les attaquants sont connus pour injecter des scripts malveillants dans les champs de formulaire ou les zones de l'application où les données d'un utilisateur sont reçues, entraînant ainsi des attaques de type Cross-Site Scripting (XSS), des attaques SQL ou des attaques par injection de code.

Examinons un exemple qui valide si un utilisateur entre le format d'e-mail correct.

1. Tout d'abord, vous définissez la fonction `validateEmail`, qui prend un paramètre, `email`. Le paramètre email est censé être une chaîne contenant l'e-mail de l'utilisateur.

    ```javascript
    function validateEmail(email){}
    ```

2. Ensuite, vous définissez l'expression regex qui vérifie si une chaîne donnée suit le format d'e-mail correct.

    ```javascript
     const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    ```

3. Ensuite, vous attribuez une instruction de retour qui vérifie si un e-mail d'utilisateur correspond au format `emailRegex`. Ici, vous utiliserez la méthode `test()` qui retourne une valeur booléenne confirmant si l'`email` est dans le bon format ou non.

    ```javascript
     return emailRegex.test(email)
    ```

Maintenant que vous avez créé une fonction pour valider un e-mail, vous pouvez utiliser cette fonction pour fournir un retour lorsque l'utilisateur entre un format d'e-mail incorrect.

```javascript
const userEmail = "userEmail@example.com"
if(validateEmail(userEmail)){
    alert("Inscription par e-mail réussie")
}
else{
    alert("Veuillez entrer l'e-mail correct")
}
```

Dans l'exemple ci-dessus, nous avons utilisé la fonction `validateEmail` pour alerter un utilisateur s'il entre le format d'e-mail correct ou non. Voici le code complet ci-dessous :

```javascript
function validateEmail(email){
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email)
}
const userEmail = "userEmail@example.com"
if(validateEmail(userEmail)){
    alert("Inscription par e-mail réussie")
}
else{
    alert("Veuillez entrer l'e-mail correct")
}
```

### 2. **Implémenter une politique de sécurité du contenu (CSP)**

Une autre façon de protéger votre application consiste à implémenter une politique de sécurité du contenu (CSP). Une CSP vous permet de restreindre l'accès ou de contrôler la manière dont les ressources externes telles que les scripts en ligne, les images ou les polices sont chargées dans votre page web.

Les CSP aident à prévenir les attaques XSS, le clickjacking et d'autres formes d'attaques par injection de code. Considérez une CSP comme un videur qui ne laisse entrer que les invités invités à la fête. Une CSP ne permet de charger dans votre page web que les ressources explicitement définies par vous.

Pour implémenter une CSP dans votre application web, ajoutez la politique aux en-têtes HTTP de votre serveur. Vous pouvez configurer la CSP en spécifiant les types de ressources (tels que les scripts, les styles ou les images) et les domaines autorisés à charger du contenu.

### 3. **Assurez-vous que les données en transit sont toujours cryptées avec HTTPS**

Le navigateur et le serveur communiquent constamment entre eux. Des données telles que les identifiants de connexion, les jetons d'authentification ou les détails de paiement sont généralement envoyées du navigateur au serveur.

Il est important de s'assurer que les données transmises du navigateur au serveur sont cryptées, restent dans leur forme originale et sont envoyées à l'emplacement ou au serveur correct.

Une façon d'accomplir une communication sécurisée est d'utiliser HTTPS (HyperText Transfer Protocol Secure). [HTTPS est un protocole](https://www.freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works/) créé pour améliorer la sécurité de la transmission des données entre les navigateurs et les serveurs. Il garantit que les données envoyées au serveur restent inchangées et sont protégées contre l'interception par des attaquants.

### 4. **Utiliser le mode strict**

La directive "use strict" en JavaScript est un moyen d'écrire du code JavaScript sécurisé et de haute qualité. Elle aide à prévenir certaines actions dans votre code qui peuvent conduire à des bugs, des erreurs ou des vulnérabilités de sécurité.

Avec le [mode strict](https://www.freecodecamp.org/news/how-to-use-strict-mode-in-javascript/), JavaScript signale une erreur lorsque certaines actions sont entreprises, telles que l'accès à des objets globaux, l'utilisation de variables non déclarées et la commission d'autres erreurs de codage.

```javascript
// Sans mode strict
undeclaredVariable = 10;  // Pas d'erreur, crée une variable globale

// Avec mode strict
'use strict';
undeclaredVariable = 10;  // Erreur : "undeclaredVariable n'est pas défini"
```

Vous pouvez considérer le mode strict comme un ensemble de règles qui vous guide sur ce qu'il faut faire et ne pas faire lors de l'écriture de JavaScript.

Pour implémenter le mode strict, ajoutez simplement la ligne suivante au début de votre script ou fonction.

```javascript
'use strict'
```

### 5. **Éviter d'utiliser la fonction** `eval()`

Une règle en programmation est de 'Ne jamais faire confiance à l'entrée de l'utilisateur.' L'utilisation de la fonction `eval()` viole cette règle car elle permet aux utilisateurs d'exécuter du code arbitraire dans votre programme. En passant l'entrée de l'utilisateur à `eval()`, vous leur permettez essentiellement d'exécuter n'importe quel code, ce qui peut conduire à des vulnérabilités de sécurité graves.

La raison en est que la fonction `eval()` traite son argument comme du code et peut exécuter des expressions, des fonctions, voire des chaînes de caractères. Bien que cette fonctionnalité soit puissante, elle est également extrêmement dangereuse.

Les attaquants peuvent injecter du code malveillant, que `eval()` exécutera sans discrimination. Cela ouvre la porte à des vulnérabilités telles que la modification de variables globales, la création de nouvelles variables, voire l'exécution de code à distance.

Pour prévenir les vulnérabilités de sécurité, évitez d'utiliser la fonction `eval()` dans votre code et envisagez plutôt d'autres alternatives de code.

### 6. **Effectuer toujours des revues de code**

Avant de pousser votre code en production, il est essentiel de le faire [réviser par d'autres développeurs](https://www.freecodecamp.org/news/code-review-tips/).

Parfois, nous pouvons négliger des bugs ou des zones de vulnérabilité dans notre programme. Obtenir de l'aide de vos pairs ou de développeurs seniors peut aider à détecter ces bugs, identifier les vulnérabilités, améliorer la qualité du code et garantir que votre code répond aux normes nécessaires.

Lors des revues de code, il est important que vous soyez ouvert d'esprit et prêt à recevoir des corrections, évitez d'être trop sur la défensive et comprenez que c'est une opportunité pour vous d'apprendre et de grandir.

### 7. **Effectuer des tests de pénétration réguliers**

Les [tests de pénétration](https://www.freecodecamp.org/news/linux-essentials-for-hackers/), également appelés **tests d'intrusion**, consistent à imiter une attaque sur une application de la même manière qu'un attaquant réel le ferait, dans le but de découvrir des vulnérabilités de sécurité au sein de l'application.

Les tests de pénétration visent à découvrir les vulnérabilités avant que les attaquants ne le fassent. Les testeurs de pénétration ne se contentent pas d'identifier les faiblesses, mais fournissent également des solutions pour les résoudre.

Pensez aux tests de pénétration comme à la construction d'une maison, à l'installation d'un système de sécurité, puis à l'embauche de voleurs pour essayer de s'introduire. S'ils réussissent, vous pouvez identifier les faiblesses de vos défenses et apporter des améliorations pour renforcer la maison.

Vous pouvez effectuer des tests de pénétration en engageant des testeurs d'intrusion professionnels et expérimentés ou en utilisant divers outils comme [**Burp Suite**](https://www.freecodecamp.org/news/how-to-audit-web-apps-with-burpsuite/), [**Nmap**](https://www.freecodecamp.org/news/what-is-nmap-and-how-to-use-it-a-tutorial-for-the-greatest-scanning-tool-of-all-time/), et [**Kali Linux**](https://www.freecodecamp.org/news/how-to-install-kali-linux/).

## Conclusion

La sécurité est un aspect crucial du développement JavaScript que de nombreux développeurs négligent souvent lors de la construction d'applications. Cet article vous a présenté les vulnérabilités de sécurité courantes en JavaScript, y compris le Cross-Site Scripting (XSS), le Cross-Site Request Forgery (CSRF) et la désérialisation non sécurisée.

Vous avez également appris pourquoi la sécurité est importante et exploré diverses étapes pour sécuriser votre application JavaScript, telles que la réalisation de revues de code régulières, l'assainissement et la validation des entrées utilisateur, et d'autres exemples.

Merci d'avoir lu cet article. Si vous avez des suggestions, des commentaires ou des questions, n'hésitez pas à me contacter sur [**Twitter**](https://x.com/sephjoe12) ou [LinkedIn](https://www.linkedin.com/in/bello-joseph-970727265).
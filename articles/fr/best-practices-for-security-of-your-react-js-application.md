---
title: Comment sécuriser votre application React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-28T23:44:02.000Z'
originalURL: https://freecodecamp.org/news/best-practices-for-security-of-your-react-js-application
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-pixabay-39624--1-.jpg
tags:
- name: Application Security
  slug: application-security
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Security
  slug: security
seo_title: Comment sécuriser votre application React.js
seo_desc: "By Shachee Swadia\nReact.js is a scalable open-source JavaScript library\
  \ and is one of the most commonly used front-end frameworks out there today. \n\
  It's dynamic and is easy to get started with if you want to create interactive web\
  \ applications with r..."
---

Par Shachee Swadia

React.js est une bibliothèque JavaScript open-source scalable et l'un des frameworks front-end les plus couramment utilisés aujourd'hui. 

Il est dynamique et facile à prendre en main si vous souhaitez créer des applications web interactives avec des composants réutilisables.

Il y a de nombreuses raisons d'utiliser React.js dans votre application :

* sa flexibilité – vous pouvez créer des applications complexes sans recharger la page web
* sa simplicité – vous pouvez lancer un projet rapidement et facilement
* sa facilité d'utilisation avec d'autres bibliothèques JS
* sa personnalisation – il existe de nombreux composants open-source qui peuvent être intégrés à votre projet.

Comme vous pouvez le voir, React est génial. Mais il y a certaines choses dont vous devez être conscient lorsque vous l'utilisez pour vos projets.

## Vulnérabilités de sécurité de React

Dans le monde d'aujourd'hui, où plus de données que jamais sont partagées, vous devez être conscient des risques associés à toute technologie que vous utilisez dans votre application.

React est pratique et rapide, ce qui peut le rendre sujet aux risques et il est facile d'oublier les préoccupations de sécurité. 

Bien que React ait un nombre plus restreint de points d'attaque que d'autres frameworks, il n'est toujours pas entièrement sécurisé. Puisque React est compatible avec d'autres composants open-source et ne dispose pas de paramètres de sécurité par défaut forts, il devient vulnérable aux failles de sécurité.

D'énormes quantités de données personnelles sont constamment partagées par diverses applications. Cela augmente le danger (et la probabilité) d'exposer des données privées et financières. Et si votre entreprise utilise React, elle pourrait faire face à des violations des réglementations de confidentialité en cas de violation de données.

Votre application React sera inutile sans des fonctionnalités de sécurité appropriées, il est donc préférable de faire preuve de prudence et de traiter ces menaces de sécurité de front.

## Menaces de sécurité les plus courantes pour une application React

Puisque React est constamment mis à jour et amélioré, je ne peux pas créer une liste exhaustive des vulnérabilités ici. Mais je vais discuter de certaines des menaces les plus connues et courantes ici.

### 1. Cross-Site Scripting (XSS)

XSS est une vulnérabilité sérieuse côté client. Un auteur de menace est capable d'ajouter du code malveillant à votre programme qui est interprété comme valide et exécuté comme une partie de l'application. Cela compromet la fonctionnalité de l'application et les données de l'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Cross-Site-Scripting.png)
_[ [Source](https://www.thirdrocktechkno.com/blog/5-react-security-vulnerabilities-serious-enough-to-break-your-application/) ]_

Il existe deux types d'attaques par cross-site scripting :

1. **Reflected XSS** – Ici, un attaquant utilise un lien malveillant avec du code JS que le navigateur traite pour accéder et manipuler le contenu de la page, les cookies et d'autres données importantes de l'utilisateur. 
2. **Stored XSS** – Dans cette attaque, le contenu malveillant est stocké sur un serveur et exécuté lorsqu'un utilisateur demande les données stockées. Cela conduit à un contenu indésirable sur votre page web.

### 2. Authentification compromise

Un autre problème courant dans les applications React.js est l'autorisation inadéquate ou médiocre. Cela peut entraîner des attaques par force brute sur les identifiants des utilisateurs.

Il existe divers risques associés à une autorisation compromise, comme les identifiants de session exposés dans les URLs, des détails de connexion faciles et prévisibles découverts par les attaquants, la transmission non cryptée des identifiants, des sessions valides persistantes après la déconnexion, et d'autres facteurs liés aux sessions.

### 3. Injection SQL

Cette vulnérabilité expose la base de données de votre application. Un attaquant injecte du code SQL malveillant qui lui permet de modifier des données sans autorisation. 

Le pirate peut accéder à toutes les données de votre application, créer de faux identifiants, et même contrôler les privilèges d'administrateur.

### 4. Attaque par entité externe XML (XXE)

![Image](https://www.freecodecamp.org/news/content/images/2021/10/XXE.png)
_[ [Source](https://securitysouls.com/what-are-xxexml-external-entity-attacks/) ]_

Une attaque XXE se produit lorsque l'agresseur cible l'analyseur XML qui est nécessaire pour transformer le XML en code lisible. 

Du code malveillant est injecté dans les analyseurs pour collecter des données sensibles ou même tenter une attaque CSRF (falsification de requête inter-sites) et DDoS (déni de service distribué).

### 5. Zip Slip

Il existe une vulnérabilité très spécifique dans les applications React connue sous le nom de "zip slip" qui implique l'exploitation de la fonctionnalité permettant de télécharger des fichiers zip. 

L'attaquant pourrait décompresser les fichiers téléchargés en dehors du répertoire assigné si l'archive utilisée pour décompresser le fichier zip n'est pas sécurisée et pourrait alors accéder au fichier.

### 6. Exécution de code arbitraire

Cette menace est un risque général qui permet à un attaquant d'exécuter des commandes arbitraires sur certains processus de votre application. 

Ces commandes aléatoires sont dangereuses car elles peuvent apporter des modifications à vos fichiers de configuration ou à toute partie du code, d'ailleurs.

D'accord, maintenant que nous savons ce qui peut mal tourner, voyons comment nous en protéger.

## Bonnes pratiques pour la sécurité de React.js

Comme on dit, mieux vaut prévenir que guérir – il est donc toujours bon de suivre les protocoles appropriés et de s'assurer que votre application est sécurisée. 

Vous ne pensez peut-être pas à toutes les vulnérabilités possibles, mais vous pouvez certainement rendre votre application plus sécurisée en atténuant les risques les plus courants.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Security-1.jpg)
_[ [Source](https://asperbrothers.com/) ]_

Voici quelques-unes des meilleures pratiques que vous devriez suivre pour sécuriser vos applications React :

### **1. Sécurisez l'authentification de base de votre application React**

Un principe de base mais important pour la sécurité de votre application est de vous assurer que la connexion entre le serveur et le client est sécurisée. 

Une manière simple de le faire lors de la construction de votre application est de vous assurer que l'en-tête de domaine a un attribut realm. Un realm contient la liste des utilisateurs valides et demande un nom d'utilisateur et un mot de passe lors de l'accès à toute donnée restreinte.

Voici un exemple de la manière dont vous pouvez configurer un realm de sécurité :

```javascript
<security-realm name="ApplicationRealm">
  <authentication>
    <local default-user="$local" allowed-users="comma-separated-list"/>
    <properties path="application-users.properties"/>
  </authentication>
  <authorization>
    <properties path="application-roles.properties"/>
  </authorization>
</security-realm>

```

Lorsque cela est possible, une autre technique simple et efficace consiste à utiliser l'authentification multifactorielle. Cette méthode d'authentification garantit qu'un utilisateur se voit accorder l'accès aux parties importantes de votre application uniquement après avoir fourni deux ou plusieurs justificatifs d'authentification pour vérifier son identité.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/MFA.PNG)
_[ [Source](https://www.onelogin.com/learn/what-is-mfa) ]_

Une autre règle de base à suivre est que pour chaque nouvelle connexion, vous devez toujours créer un nouvel identifiant de session avec un gestionnaire de session sécurisé côté serveur.

Lorsque votre application React.js a une authentification de base sécurisée, cela aide à atténuer les problèmes de XSS et d'authentification compromise.

### 2. Assurez-vous que le code HTML est résilient

Toute application React aura besoin de HTML pour la rendre, il est donc impératif de s'assurer que votre code HTML n'est pas vulnérable. Trois façons constructives de le faire sont :

**A. Désactiver les balises HTML**

Lorsque l'attribut 'disabled' est défini pour un élément HTML, il devient non mutable. Il n'est pas possible de se concentrer ou de soumettre cet élément avec un formulaire. 

Vous pouvez ensuite mettre en place une validation et activer l'élément uniquement lorsque cette validation est vraie. Cela empêche toute donnée malveillante d'être soumise et de causer des effets désastreux.

Voici un exemple de code pour désactiver un bouton :

```javascript
var Component = React.createClass({
	getInitialState() {
    	return {
        	submitting: true
        }
    },
    
    handleSubmit() {
    },
    
    render() {
        
    	return (<div>
        	<button type="button" disabled={this.state.submitting} onClick={ this.handleSubmit }>Submit</button>
    }
});
 
ReactDOM.render(
	<Component />,
    document.getElementById('container')
);
```

**B. Utiliser des caractères d'échappement**

JavaScript XML (JSX) est une syntaxe qui vous permet d'écrire du HTML dans React. Et il dispose d'une fonctionnalité d'échappement automatique intégrée que vous pouvez utiliser pour sécuriser votre application. 

Si vous liez des données avec des accolades {} par défaut, React échappera automatiquement les valeurs qui ne font pas partie des données liées.

Voici un exemple :

```javascript
return (<p style={{color: myAppColor}}>{myAppRating}</p>);
```

Si un pirate essaie d'injecter du code supplémentaire dans la variable myAppColor tel que _color: purple, background-color: pink_, le parseur JSX détectera cette entrée CSS invalide. Ainsi, les données supplémentaires seront échappées et l'attaque sera neutralisée.

**C. Utiliser dangerouslySetInnerHTML et assainir le HTML**

Votre application peut avoir besoin de rendre du code HTML dynamique comme des données fournies par l'utilisateur. Cela se fait en utilisant 'innerHTML' qui rend l'application vulnérable aux données malveillantes.

React dispose d'une fonctionnalité qui peut vous avertir de cette vulnérabilité potentielle appelée la prop `dangerouslySetInnerHTML`. Cela sert d'avertissement afin que vous puissiez vérifier et vous assurer que les données entrées lorsque cette prop existe proviennent d'une source de confiance.

```javascript
return (<p dangerouslySetInnerHTML={{__html: myAppReview}}></p>);
```

Vous pouvez également utiliser des bibliothèques comme [DOMPurify](https://github.com/cure53/DOMPurify) pour analyser les entrées utilisateur et supprimer le contenu malveillant.

```javascript
// Import DOMPurify
const DOMPurify = require('dompurify')(window);

// Assainir la revue
return (<p dangerouslySetInnerHTML={{__html: myAppReview}}></p>);
```

Maintenant, imaginez qu'un attaquant ajoute le code 'onerror' avec l'image comme suit :

```javascript
The app is <b>robust</b> and <i>interesting.</i>.
<img src="reviewPic.png" onerror="alert('This app is not good!');" />
```

La valeur assainie donnerait le résultat suivant :

```javascript
The app is <b>robust</b> and <i>interesting.</i>.
<img src="reviewPic.png">
```

Toutes ces mesures protègent votre application React contre des attaques comme XSS et l'exécution de code arbitraire.

### 3. Utiliser une liste d'autorisation/liste de blocage et validation lors de l'analyse des URLs

Lorsque vous utilisez la balise d'ancrage `<a>` et les URLs pour lier du contenu, vous devez être très prudent quant aux attaquants ajoutant des charges utiles préfixées avec JavaScript. 

Pour éviter l'injection de scripts malveillants basés sur les URLs, validez toujours l'URL en utilisant les protocoles HTTP ou HTTPS.

```javascript
function validateURL(url) {
	const parsed = new URL(url)
	return ['https:', 'http:'].includes(parsed.protocol)
}
<a href={validateURL(url) ? url : ''}>This is a link!</a>
```

Une autre façon de protéger votre application React est d'utiliser la méthode de la liste d'autorisation/liste de blocage. La liste d'autorisation consiste à avoir une liste de tous les liens qui sont sûrs et autorisés à être accessibles, tandis que la liste de blocage consiste à avoir une liste de toutes les menaces potentielles qui seront bloquées si l'accès est demandé. 

Il est difficile de garder une trace de tous les liens potentiellement nocifs, donc une bonne pratique consiste à autoriser les sites connus et à bloquer tout le reste. 

La validation des URLs aide à prévenir l'authentification compromise, XSS, l'exécution de code arbitraire et l'injection SQL.

### 4. Utilisez toujours le principe du moindre privilège lors de l'autorisation d'une connexion à une base de données

Dans votre application React, utilisez toujours le principe du moindre privilège. Cela signifie que chaque utilisateur et processus doit être autorisé à accéder uniquement aux informations et ressources qui sont absolument nécessaires à leur finalité. 

Il est dangereux de permettre à quiconque de mettre à jour, insérer ou supprimer lors de la connexion à la base de données de votre application, il est donc important d'assigner les bons rôles de base de données aux différents utilisateurs. 

Ne donnez jamais de privilèges d'administrateur pour la base de données de votre application à quiconque, sauf si c'est vital. Cela rend votre application plus sûre et moins sujette aux attaques par injection SQL.

### 5. Sécurisez vos APIs React

Le bon et le mauvais côté des APIs React est qu'elles permettent des connexions entre votre application et d'autres services. Ceux-ci peuvent stocker des informations et même exécuter des commandes. Cela expose votre application à XSS et à l'injection SQL.

Une technique puissante pour atténuer cette vulnérabilité consiste à valider toutes les fonctions de l'API par rapport à leurs schémas d'API. De plus, planifiez des validations de schéma en temps opportun et utilisez le cryptage SSL/TLS pour toutes les interactions.

Pour une sécurité accrue, utilisez des caractères bénins au lieu de `<` lors de la transmission de données via les APIs.

```javascript
window.__PRELOADED_STATE__ =   ${JSON.stringify(preloadedState).replace( /</g, '\\u003c')}
```

### 6. Implémentez un pare-feu pour applications web (WAF)

Un WAF est un filtre d'application qui détecte et bloque le contenu malveillant en surveillant, analysant et filtrant le trafic bidirectionnel.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/WAP.PNG)
_[ [Source](https://www.cloudflare.com/en-in/learning/ddos/glossary/web-application-firewall-waf/) ]_

Vous pouvez implémenter un pare-feu pour applications web de trois manières :

1. Pare-feu basé sur le réseau qui est au niveau matériel.
2. Pare-feu basé sur l'hôte qui est intégré au logiciel.
3. WAF basé sur le cloud

Le filtrage basé sur les signatures du WAF est assez efficace pour contrer l'injection SQL, XSS, l'exécution de code arbitraire et zip slip.

### 7. Mettez en place une gestion appropriée des fichiers

Dans votre application React, vous devez toujours suivre des pratiques de gestion de fichiers appropriées pour éviter le zip slip et d'autres risques similaires.

* Confirmez que les noms de fichiers sont standard et sans caractères spéciaux.
* Chaque fois que les fichiers sont téléchargés sous forme de zip, renommez-les toujours avant de les extraire et d'utiliser les fichiers.
* Stockez tous les fichiers d'un seul composant ensemble dans un seul dossier afin que tout fichier suspect puisse être rapidement découvert.

### 8. Ne sérialisez jamais de données sensibles

Il y a de bonnes chances que votre application React utilise JSON pour définir l'état initial de votre application. 

Cela peut être potentiellement dangereux car JSON.stringify() est une fonction qui convertit toute donnée en une chaîne sans détecter les valeurs malveillantes. Un attaquant peut manipuler des données comme le nom d'utilisateur et le mot de passe en injectant un objet JS qui peut modifier des données valides.

```javascript
<script>window.__STATE__ = ${JSON.stringify({ data })}</script>
```

Vous pouvez soit utiliser le module NPM serialize-javascript qui échappera le JSON rendu, soit utiliser des formats JSON complexes qui éviteront la sérialisation. Mais la meilleure façon de prévenir tout incident est d'omettre les données confidentielles de la forme sérialisée.

## Conclusion

Il y a beaucoup de menaces potentielles auxquelles vous devez penser lors de la création d'une application React. Sans une sécurité appropriée, votre application peut devenir la victime d'une cyberattaque qui peut entraîner des pertes financières, du temps perdu, des violations de confiance et des problèmes juridiques.

Avec de nouvelles menaces apparaissant chaque jour et des attaquants exploitant de plus en plus de failles, rendre votre application React sécurisée peut être assez complexe et difficile. 

Vous pouvez soit embaucher des développeurs React spécialisés dans la sécurité, soit externaliser le développement à une entreprise de développement de logiciels spécialisée dans le développement d'applications React JS. En matière de sécurité, assurez-vous d'avoir un expert à vos côtés !
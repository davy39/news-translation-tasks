---
title: Comment implémenter votre premier système de connexion sans mot de passe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-20T06:04:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-your-first-password-less-login-system-8141b6f9ddf2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mx4X6zSgYa2nd2eF5LImvg.gif
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment implémenter votre premier système de connexion sans mot de passe
seo_desc: 'By Jackson Bates

  You may have heard that there are 360 Million Reasons to Destroy All Passwords and
  that Passwords are Obsolete. But that doesn’t really help you actually make a passwordless
  authentication system, does it?

  Doing authentication well c...'
---

Par Jackson Bates

Vous avez peut-être entendu qu'il y a [360 millions de raisons de détruire tous les mots de passe](https://medium.freecodecamp.com/360-million-reasons-to-destroy-all-passwords-9a100b2b5001#.e45q1htgn) et que [les mots de passe sont obsolètes](https://medium.com/p/9ed56d483eb). Mais cela ne vous aide pas vraiment à créer un système d'authentification sans mot de passe, n'est-ce pas ?

Faire une authentification correcte peut être difficile et semé d'embûches de sécurité potentielles. La bonne nouvelle est qu'il existe quelques petites bibliothèques JavaScript charmantes qui peuvent faire une partie de ce travail pour nous. Et elles fournissent beaucoup de snippets de code pour nous aider à démarrer.

Alors, voici comment j'ai implémenté un système d'authentification sans mot de passe dans mon récent projet Free Code Camp [Voting App](https://pollz.herokuapp.com/login).

Avant de commencer, notez que vous aurez besoin d'une connaissance pratique de Node.js et npm.

### Ce dont vous aurez besoin :

* Une bibliothèque d'authentification sans mot de passe : [Passwordless](http://passwordless.net)
* Une bibliothèque d'email : [EmailJS](https://github.com/eleith/emailjs)
* Une nouvelle adresse email à usage unique : [Microsoft Outlook](https://signup.live.com/signup?wa=wsignin1.0&ct=1473911386&rver=6.6.6556.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f&id=292841&CBCXT=out&bk=1473911387&uiflavor=web&uaid=b9b59510e54e4c20a9d7b5e3e5890614&mkt=EN-US&lc=1033&lic=1) (ne vous inquiétez pas, je vais expliquer plus tard)
* Une attitude "Can-Do" et des doigts agiles pour le copier-coller

![Image](https://cdn-media-1.freecodecamp.org/images/9pXwfLQGii7a3Sj2K8yXhqSqcdicCWEKsd54)

### Commençons !

#### Enregistrez votre adresse email à usage unique

Choisissez le nom le plus professionnel et le plus significatif pour le compte que vous pouvez imaginer. Par exemple, comme mon application s'appelait "Pollz", j'ai enregistré l'adresse email _pollz.tokendelivery@outlook.com_. De cette façon, je communique au destinataire qu'il s'agit d'une adresse email à usage unique liée à l'application à laquelle il vient d'essayer de se connecter.

Notez qu'il est préférable d'envoyer depuis un domaine "propre" si vous en possédez un, mais ce tutoriel suppose que vous voulez quelque chose de rapide et simple pour tester le concept.

Vous devrez peut-être prendre quelques étapes supplémentaires comme vérifier votre compte avant qu'il ne vous permette d'envoyer des emails automatiquement via votre application. Donc, si les choses ne fonctionnent pas plus tard, vérifiez la boîte de réception pour tout message d'Outlook et suivez leurs conseils.

#### Installez et requérez les modules Node

Depuis le terminal, installez les paquets npm suivants :

```bash
// Ajoutez 'sudo' au début si nécessaire !

npm install --save passwordless
npm install --save passwordless-mongostore
npm install --save emailjs
```

Cela installe les exigences de base. Vous utiliserez également d'autres bibliothèques Node cruciales, que vous avez peut-être déjà installées pour votre projet. Si ce n'est pas le cas, installez également celles-ci :

```bash
npm install --save express-sessions
npm install --save body-parser
npm install --save cookie-parser
```

Maintenant, en supposant que vous avez un fichier server.js et routes.js séparés, incluez ce qui suit en haut des fichiers appropriés. Si vous n'avez pas de fichiers séparés, vous pouvez tout mettre ensemble et les noyer dans une délicieuse sauce spaghetti :

**Note :** N'oubliez pas tous les autres modules que vous incluez habituellement ! (Express, Mongo, etc...)

```javascript
// server.js
var cookieParser = require( 'cookie-parser' );
var expressSession = require( 'express-session' );
var passwordless = require( 'passwordless' );
var MongoStore = require( 'passwordless-mongostore' );
var email = require( 'emailjs' );


```



```javascript
// routes.js
var bodyParser = require( 'body-parser' );
var urlencodedParser = bodyParser.urlencoded( { extended: false });
var passwordless = require( 'passwordless' );
```

#### Configurez la livraison

Ensuite, dans le fichier server.js, nous inclurons le snippet de code qui gère l'envoi des jetons d'authentification à nos utilisateurs :

```javascript
// server.js
var yourEmail = 'pollz.tokendelivery@outlook.com';
var yourPwd = process.env.OUTLOOK_PASSWORD;
var yourSmtp = 'smtp-mail.outlook.com';
var smtpServer  = email.server.connect({ 
	user: yourEmail,
    	password: yourPwd,
    	timeout: 60000,
    	host: yourSmtp, tls: { ciphers: 'SSLv3' }
    });

// Configuration MongoDB (peut être utilisé par défaut)
var pathToMongoDb = url;

// Chemin à envoyer par email
var host = 'https://pollz.herokuapp.com/';
```

Le code ci-dessus fait quelques suppositions que vous devez connaître.

Tout d'abord, changez la valeur de la variable `yourEmail` pour la nouvelle adresse que vous avez configurée.

Deuxièmement, la variable `yourPwd` que vous voyez là ne signifie pas que mon mot de passe est le super-obscur `process.env.OUTLOOK_PASSWORD`, ni que vous devriez mettre votre mot de passe directement là.

`process.env.***` est utilisé pour accéder aux _variables d'environnement_ dans Node. Basiquement, vous pouvez coder en dur ces variables dans votre système local dans un fichier [`dotenv`](https://www.npmjs.com/package/dotenv), ou dans Heroku via les paramètres de votre application, puis y faire référence comme ci-dessus. Cela signifie que vous ne commettez pas d'informations sensibles dans des dépôts publics GitHub pour que tout le monde puisse les voir. C'est un peu en dehors du cadre de ce tutoriel, mais le manuel peut vous en dire plus : [process.env](https://nodejs.org/api/process.html#process_process_env).

L'URL `pathToMongoDB` que vous voyez là est le même chemin MongoDB que j'utilise pour me connecter à Mongo ailleurs dans mon application. Si vous vous êtes connecté à Mongo, vous pouvez utiliser la même URL à nouveau.

Assurez-vous de changer l'URL `host` pour celle de votre propre application.

#### Configurez Passwordless

```javascript
// server.js 
// Configuration de Passwordless

passwordless.init( new MongoStore( pathToMongoDb ));

passwordless.addDelivery(function(tokenToSend, uidToSend, recipient, callback) {
    // Envoyer le jeton
    smtpServer.send({
        text: `Bonjour !\nVous pouvez maintenant accéder à votre compte ici : ${host}?token=${tokenToSend}&uid=${encodeURIComponent(uidToSend)}`,
        from: yourEmail,
        to: recipient,
        subject: `Jeton pour ${host}`,
        attachment: [{
            data: "<html>INSERT HTML STRING LINKING TO TOKEN</html>",
            alternative: true
        }]
    }, function( err, message ) {
        if( err ) { 
            console.log( err );
        }
        callback( err );
    });
});
```

Bloc de code effrayant, n'est-ce pas ? Mais pas du charabia complet, j'espère.

Il y a deux choses qui se passent ici :

1. Initialisation de Passwordless, et définition d'un stockage pour les jetons.
2. Ajout d'un mécanisme de livraison et construction du contenu de l'email.

Lisez-le attentivement et cela devrait avoir du sens. Attention à inclure le nombre approprié de parenthèses et d'accolades fermantes. J'ai brûlé 45 minutes sur ce problème précis hier soir sur ma dernière application. Je ne plaisante pas.

#### Mettez en place votre middleware

Le middleware est comme les sous-vêtements : l'oublier peut entraîner de l'inconfort, mais le mettre dans le mauvais ordre peut entraîner de l'embarras.

Vous avez peut-être déjà inclus ce middleware Express plus générique, mais si ce n'est pas le cas, vous devez le faire :

```javascript
// server.js
// Configuration standard express

app.use( cookieParser() );
app.use( expressSession({
  secret: 'quincylarsonisaprinceamongmen',
  saveUninitialized: false,
  resave: false,
  cookie: { maxAge: 60*60*24*365*10 }
}));
```

Ensuite, le middleware particulier dont vous avez besoin pour passwordless peut être inclus comme ceci :

```javascript
// server.js
// Middleware Passwordless

app.use( passwordless.sessionSupport() );
app.use( passwordless.acceptToken( { successRedirect: '/' }));
```

J'ai mis tout cela immédiatement après les snippets d'initialisation de Passwordless, et j'inclus le middleware 'standard' _avant_ le middleware 'passwordless'. `sessionSupport` dépend de `expressSession`, donc l'ordre compte. Tout autre ordre conduit à des frictions.

#### Configurez quelques routes de test

Il n'y a que quelques routes essentielles. Nous devons permettre aux utilisateurs de se connecter et de se déconnecter, et il doit y avoir un moyen de différencier les pages restreintes des pages publiques pour les utilisateurs non authentifiés.

Note : Cette partie suppose que vous avez configuré le routeur Express pour votre application.

**Connexion :**

```javascript
// routes.js
// GET /login
router.get( '/login', function( req, res ) {    res.render( 'login' ); });

// POST /sendtoken
router.post( '/sendtoken',  urlencodedParser,   passwordless.requestToken(
    // Accepter simplement chaque utilisateur*
    function( user, delivery, callback ) { callback( null, user );  }),
    function( req, res ) { 
    	res.render( 'pages/sent', { user: req.user });
    }
);
```

Dans la requête POST ci-dessus, nous utilisons le mécanisme le plus simple et le plus rapide pour connecter quelqu'un. Vous êtes plus susceptible de vouloir utiliser l'adresse email qui est passée depuis le formulaire de connexion (nous verrons cela dans une minute) pour rechercher l'utilisateur dans votre base de données, ou en créer un nouveau. Vous pouvez voir la méthode plus détaillée pour cela dans la [documentation de Passwordless](https://passwordless.net/getstarted).

La requête POST inclut la variable `urlencodedParser` que nous avons définie précédemment. Nous faisons cela pour pouvoir lire les données du formulaire, mais nous ne l'appliquons qu'à cette route spécifique. Vous pouvez en lire plus sur cette considération de sécurité ici : [Dangerous Use Of Body Parser](https://fosterelli.co/dangerous-use-of-express-body-parser.html). Un merci spécial à [Jeremy](http://crookedcode.com/) pour ce conseil !

Remarquez également dans cette requête POST, la page 'sent' est rendue avec une adresse email 'user' qui est passée. Cela est accessible dans les templates de vues et peut être utilisé et passé comme nécessaire. Nous utiliserons une barre de navigation EJS pour démontrer cela bientôt.

**Déconnexion :**

```javascript
// routes.js
// GET logout
router.get( '/logout', passwordless.logout(), function( req, res ) {
    res.redirect( '/' );
});
```

Vous avez probablement remarqué que cette simple requête GET prend un argument supplémentaire niché entre l'endpoint URL et la fonction de rappel qui traite la requête. Cette méthode 'passwordless.logout()' fait tout le travail en coulisses nécessaire pour oublier rapidement l'utilisateur.

**Pages restreintes :**

```javascript
// routes.js
// GET restricted site
router.get( '/restricted',   passwordless.restricted({
	failureRedirect: '/login'
}),  function( req, res ) {
	res.render( 'pages/restricted' , { user: req.user });
});
```

Le format pour les pages restreintes est également assez facile à analyser. Similaire au modèle de déconnexion, nous avons la route, `/restricted`, suivie de la méthode `passwordless.restricted()`, suivie de la fonction de rappel qui traite la requête HTTP. La différence ici est que `passwordless.restricted()` prend un objet comme argument qui spécifie l'endpoint vers lequel nous redirigeons si l'utilisateur n'est pas authentifié.

#### Vues

L'une des vues les plus importantes de ce tutoriel est la modeste page de connexion. Configurez-la comme vous le souhaitez, mais incluez ce formulaire pour demander l'adresse email de votre utilisateur :

```html
<!-- views/pages/login.ejs -->
<form action='/sendtoken' method='POST'>
    <div class='input-field'>
        <label for='user'>Email</label>
        <input name='user' type='email' aria-required='true'>
    </div>
    <br>
    <input type='submit' value='Connexion / Inscription'>
</form>
```

Nous manquons de temps. Stylez-le à vos frais.

Il est important que vous ayez inclus le middleware `body-parser` mentionné précédemment afin de pouvoir gérer les données POSTées depuis ce formulaire.

Une dernière vue qui mérite d'être examinée serait celle qui incorpore la valeur de l'utilisateur authentifié que nous avons vue dans la section des routes.

Voici un exemple d'une barre de navigation vraiment simple qui change selon que l'utilisateur est authentifié ou non :

```html
<!-- views/partials/navbar.ejs -->
<nav>
	<ul>
        <% if(user) { %>
            <li>Salut, <%= user %> ! </li>
            <li><a href='/logout'>(déconnexion)</a></li>
        <% } else { %>
            <li><a href='/login'>Connexion</a></li>
        <% } %>
    </ul>
</nav>
```

Si vous n'êtes pas familier avec la syntaxe EJS, c'est la raison des balises étranges '<% %>' dans le balisage.

Le balisage ci-dessus peut être analysé en anglais comme 'Si il y a un utilisateur, imprimez un élément de liste qui dit « Salut, <nom d'utilisateur> ! » et un autre élément de liste qui leur permet de se déconnecter ; sinon, affichez uniquement un élément de liste avec un lien de connexion'.




Voici à quoi ressemble la version plus complète dans l'application de vote :

![Image](https://cdn-media-1.freecodecamp.org/images/aeddKybswwBxu5BkS1m9un21PNe-r8nauXdz)
_Déconnecté_

![Image](https://cdn-media-1.freecodecamp.org/images/gZ7oC233llWCZlUlvyxAxCW6YQ-f5DIt6GHX)
_Connecté_

### Et c'est tout. Mais il y a plus...

C'est tout ce que vous devez savoir pour démarrer avec l'authentification Passwordless.

Il y a quelques mises en garde à connaître :

**Outlook est un peu lent.** Je n'ai pas identifié la cause avec précision, mais je crois que c'est dû au chiffrement TLS 'SSLv3' qu'Outlook exige. Je ne suis pas expert, mais c'est ma meilleure supposition. C'est aussi pourquoi je recommande de définir un délai d'attente absurdement long dans la section de configuration de l'email (j'ai choisi 60 secondes).

**Pourquoi ne pas utiliser Gmail, alors ?** Une bonne question, et c'est la première chose que j'ai essayée. Mon script emailjs continuait à échouer une fois que j'avais poussé l'application sur Heroku, mais les logs Heroku ne fournissaient pas beaucoup de détails. Il disait simplement que je faisais une 'mauvaise requête'. Un peu de recherche sur internet a suggéré que peut-être Google attendait que je registre mon application auprès d'eux et que je paie pour le privilège. Je ne l'ai pas fait. Je suis simplement passé à Outlook à la place.

**Y a-t-il un meilleur service qu'Outlook, alors ?** Si vous avez votre propre domaine et la capacité de configurer les enregistrements DNS pour celui-ci, vous devriez essayer SparkPost et la bibliothèque cliente node SparkPost. C'est un peu plus de travail, mais c'est rapide et agréable, et ils vous envoient un autocollant pour ordinateur portable si vous pouvez envoyer un email avec succès via eux. Je l'utilise dans ma dernière application. C'est génial.

Alors, voilà, il n'y a aucune excuse pour que vous demandiez jamais à vos utilisateurs leurs mots de passe à nouveau !
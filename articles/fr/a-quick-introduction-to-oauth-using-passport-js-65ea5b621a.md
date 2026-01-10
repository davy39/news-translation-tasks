---
title: Une introduction rapide à OAuth avec Passport.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T22:11:44.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-oauth-using-passport-js-65ea5b621a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*gWsdm7w5PSZNR08L
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: Une introduction rapide à OAuth avec Passport.js
seo_desc: "By Arun \nWhat is OAuth?\nOAuth (Open Authorization) is an authorization\
  \ protocol. A third party application can use it to access user data from a site\
  \ (like Google or Twitter) without revealing their password. Sites like Quora, Medium,\
  \ AirBnb and many..."
---

Par Arun 

### Qu'est-ce que OAuth ?

OAuth (Open Authorization) est un protocole d'autorisation. Une application tierce peut l'utiliser pour accéder aux données utilisateur d'un site (comme Google ou Twitter) sans révéler leur mot de passe. Des sites comme Quora, Medium, AirBnb et bien d'autres offrent une authentification utilisant OAuth.

OAuth simplifie vraiment nos vies en éliminant le besoin de se souvenir du mot de passe de chaque compte que vous créez sur presque n'importe quel site. Vous n'avez qu'à vous souvenir du mot de passe principal de votre compte OAuth.

### Qu'est-ce que Passport.js ?

[Passport](http://www.passportjs.org/) est un middleware qui implémente l'authentification sur les applications web basées sur Express. Il fournit plus de 500+ stratégies. Que sont ces stratégies ? Les stratégies sont utilisées pour authentifier les requêtes. Chaque stratégie a son propre package npm (comme [passport-twitter](https://www.npmjs.com/package/passport-twitter), [passport-google-oauth20](https://www.npmjs.com/package/passport-google-oauth20)). Une stratégie doit être configurée avant utilisation.

### Pourquoi utiliser Passport.js ?

Voici six raisons pour lesquelles vous devriez utiliser Passport :

* Il est léger
* Facilement configurable
* Supporte les sessions persistantes
* Offre OAuth
* Fournit des modules séparés pour chaque stratégie
* Vous donne la possibilité d'implémenter des stratégies personnalisées

### Construisons quelque chose

Pour commencer, nous devons installer passport depuis NPM :

```
npm install passport 
```

Nous allons construire une application simple qui accorde à l'utilisateur l'accès à une route secrète uniquement s'ils se connectent. Je vais utiliser la stratégie [passport-google-oauth20](https://www.npmjs.com/package/passport-google-oauth20) dans ce tutoriel. N'hésitez pas à utiliser une autre stratégie que vous préférez, mais assurez-vous de consulter la [documentation](http://www.passportjs.org/packages/) pour voir comment elle est configurée.

Avant de continuer, nous avons besoin d'un clientID et d'un clientSecret. Pour en obtenir, rendez-vous sur [https://console.developers.google.com](https://console.developers.google.com) et créez un nouveau projet. Ensuite, allez dans Activer les API et services et activez l'API Google+. Sélectionnez l'API et cliquez sur créer des identifiants.

Remplissez le formulaire et utilisez la même URL de rappel sur le formulaire et sur votre fichier. Assurez-vous de lire les commentaires dans le code pour comprendre comment tout s'assemble.

**app.js**

```js
// Dépendances requises 
const express = require('express');
const app = express();
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20');
const cookieSession = require('cookie-session');

// Configuration de cookieSession
app.use(cookieSession({
    maxAge: 24 * 60 * 60 * 1000, // Un jour en millisecondes
    keys: ['randomstringhere']
}));

app.use(passport.initialize()); // Utilisé pour initialiser passport
app.use(passport.session()); // Utilisé pour persister les sessions de connexion

// Configuration de la stratégie
passport.use(new GoogleStrategy({
        clientID: 'YOUR_CLIENTID_HERE',
        clientSecret: 'YOUR_CLIENT_SECRET_HERE',
        callbackURL: 'http://localhost:8000/auth/google/callback'
    },
    (accessToken, refreshToken, profile, done) => {
        done(null, profile); // transmet les données de profil à serializeUser
    }
));

// Utilisé pour insérer une information dans un cookie
passport.serializeUser((user, done) => {
    done(null, user);
});

// Utilisé pour décoder le cookie reçu et persister la session
passport.deserializeUser((user, done) => {
    done(null, user);
});

// Middleware pour vérifier si l'utilisateur est authentifié
function isUserAuthenticated(req, res, next) {
    if (req.user) {
        next();
    } else {
        res.send('Vous devez vous connecter !');
    }
}

// Routes
app.get('/', (req, res) => {
    res.render('index.ejs');
});

// Le middleware passport.authenticate est utilisé ici pour authentifier la requête
app.get('/auth/google', passport.authenticate('google', {
    scope: ['profile'] // Utilisé pour spécifier les données requises
}));

// Le middleware reçoit les données de Google et exécute la fonction sur la configuration de la stratégie
app.get('/auth/google/callback', passport.authenticate('google'), (req, res) => {
    res.redirect('/secret');
});

// Route secrète
app.get('/secret', isUserAuthenticated, (req, res) => {
    res.send('Vous avez atteint la route secrète');
});

// Route de déconnexion
app.get('/logout', (req, res) => {
    req.logout(); 
    res.redirect('/');
});

app.listen(8000, () => {
    console.log('Serveur démarré !');
});

```

**index.ejs**

```html
<ul>
    <li><a href="/auth/google">Connexion</a></li>
    <li><a href="/secret">Secret</a></li>
    <li><a href="/logout">Déconnexion</a></li>
</ul>
```

Comme vous pouvez le voir, nous avons créé une route `/secret`, et nous n'accordons l'accès à celle-ci que si l'utilisateur est authentifié. Pour vérifier si l'utilisateur est authentifié, nous avons créé un middleware qui vérifie si la requête contient l'objet utilisateur. Enfin, pour se déconnecter, nous avons utilisé la méthode `req.logout()` fournie par passport pour effacer la session.

### Voici quelques ressources pour en savoir plus sur passport

%[https://youtu.be/sakQbeRjgwg?list=PL4cUxeGkcC9jdm7QX143aMLAqyM-jTZ2x]

[**Documentation officielle de Passport.js**](http://www.passportjs.org/)  
[_Simple, unobtrusive authentication for Node.js_www.passportjs.org](http://www.passportjs.org/)

### Conclusion

Nous n'avons vu qu'une seule stratégie ici. Il en existe plus de 500 autres. Je vous recommande vivement de parcourir la [documentation](http://www.passportjs.org/docs/) officielle de Passport et de découvrir ce qu'ils offrent d'autre. Merci d'avoir pris le temps de lire ceci. N'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/arun4033622), [Twitter](https://twitter.com/Arun4033622) et [GitHub](https://github.com/Arun4033622). Je vous souhaite bonne chance !

![Image](https://cdn-media-1.freecodecamp.org/images/0*mgwlLYxIDy5weT3_)
_Faites ce qui est grand, écrit sur un moniteur d'ordinateur. par [Unsplash](https://unsplash.com/@martinshreder?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Martin Shreder</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Article précédent

[**Une introduction rapide au Material Design avec Materialize**](https://medium.freecodecamp.org/an-quick-introduction-to-material-design-using-materialize-8a9b223c64f1)  
[_Qu'est-ce que le Material Design ?_medium.freecodecamp.org](https://medium.freecodecamp.org/an-quick-introduction-to-material-design-using-materialize-8a9b223c64f1)
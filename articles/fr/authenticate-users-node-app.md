---
title: Comment authentifier les utilisateurs dans votre application Node avec des
  cookies, des sessions et Passport.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-05T13:08:00.000Z'
originalURL: https://freecodecamp.org/news/authenticate-users-node-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa294a749c47664ed81a292.jpg
tags:
- name: Application Security
  slug: application-security
- name: authentication
  slug: authentication
- name: node
  slug: node
seo_title: Comment authentifier les utilisateurs dans votre application Node avec
  des cookies, des sessions et Passport.js
seo_desc: "By Suchandra Datta\nLearning how to authenticate users into an app is one\
  \ of the first things you learn in any course focused on backend technologies. \n\
  And it’s one of the first steps you take when building a social media app, an app\
  \ for learning from..."
---

Par Suchandra Datta

Apprendre à authentifier les utilisateurs dans une application est l'une des premières choses que vous apprenez dans tout cours axé sur les technologies backend. 

Et c'est l'une des premières étapes que vous franchissez lors de la création d'une application de médias sociaux, d'une application pour apprendre à partir de cours en ligne, et ainsi de suite. 

Dans cet article, nous allons examiner les concepts d'authentification de base de manière adaptée aux débutants.

## Comment authentifier un utilisateur avec des cookies

Tout d'abord, construisons une application simple qui authentifie les utilisateurs en utilisant la méthode classique du nom d'utilisateur et du mot de passe - nous ne nous soucierons pas des connexions à la base de données pour l'instant. 

Chaque fois que nous essayons de charger une page, le navigateur envoie une requête au serveur, qui répond en conséquence. 

Initialement, lorsqu'un utilisateur accède au site, il est invité à entrer son nom d'utilisateur et son mot de passe enregistrés. Une fois fournis, ils se font connaître du serveur afin que les requêtes ultérieures au serveur n'impliquent pas de réaffirmer leur identité. 

Mais comment le serveur va-t-il garder une trace des utilisateurs déjà authentifiés et de ceux qui ne le sont pas ? C'est là que les cookies interviennent. 

Selon w3.org, les cookies sont définis comme :

> "des morceaux de texte stockés sur la machine cliente et envoyés avec la requête HTTP au site Web pour lequel ils ont été créés."

Les cookies sont créés et stockés après qu'un utilisateur se connecte, et ils sont consultés avant de satisfaire les requêtes successives. Ensuite, ils expirent selon une limite de temps spécifiée.

```
let express=require('express')
let cookie_parser=require('cookie-parser')
let app=express()
app.use(cookie_parser('1234'))
```

Tout d'abord, nous configurons notre application Express et incluons le middleware `cookie-parser`. Il analyse l'en-tête de cookie de la requête et l'ajoute à `req.cookies` ou `req.signedCookies` (si des clés secrètes sont utilisées) pour un traitement ultérieur. 

`cookie-parser` prend une clé secrète comme argument, qui sera utilisée pour créer un HMAC de la valeur actuelle du cookie. Si la valeur est modifiée plus tard, cela est détecté puisque la signature faite au moment de la création ne correspond pas à la signature actuelle. 

Ensuite, lorsque l'utilisateur visite l'URL appropriée (comme /login ou quelque chose de similaire), nous devons effectuer quelques vérifications. Supposons que l'utilisateur se connecte pour la première fois.

```
let cookie_Stuff=req.signedCookies.user
//Mais l'utilisateur se connecte pour la première fois, donc il n'y aura pas de cookie signé approprié pour l'utilisation.
if(!cookie_Stuff)//Vrai pour notre cas
    {
        let auth_Stuff=req.headers.authorization
        if(!auth_Stuff)//Aucune information d'authentification donnée
        {
            res.setHeader("WWW-Authenticate", "Basic")
            res.sendStatus(401)
        }
```

Nous utilisons l'en-tête de réponse WWW-Authenticate pour définir la méthode d'authentification qui doit être utilisée pour accéder à une ressource (la méthode "Basic").

La réponse du client consiste en le nom d'utilisateur et le mot de passe séparés par un deux-points. Il est encodé en base64 et est attaché à l'en-tête Authorization de la requête. 

L'utilisateur est invité à fournir des informations d'authentification, qui sont extraites et vérifiées. En réalité, nous devons vérifier à partir d'une base de données, mais nous effectuons une vérification naïve pour simplifier.

Si les valeurs correctes sont fournies, nous configurons un cookie approprié. Sinon, nous invitons à nouveau l'utilisateur. Le prochain extrait de code effectue ces étapes :

```
else
        {
            step1=new Buffer.from(auth_Stuff.split(" ")[1], 'base64')
 //Extraction du nom d'utilisateur:mot de passe à partir de l'encodage Authorization: Basic username:password
            step2=step1.toString().split(":")
//Extraction du nom d'utilisateur et du mot de passe dans un tableau
            if(step2[0]=='admin' && step2[1]=='admin')
            {
//Nom d'utilisateur et mot de passe corrects fournis
                console.log("BIENVENUE ADMIN")
//Stocker un cookie avec le nom=user et la valeur=username
                res.cookie('user', 'admin', {signed: true})
                res.send("Connecté pour la première fois")
            }
            else
            {
 //Mauvaises informations d'authentification, réessayer
                res.setHeader("WWW-Authenticate", "Basic")
                res.sendStatus(401)
            }
        }
    }
```

Et la prochaine fois que notre utilisateur fait une requête ? À partir de ce moment jusqu'à ce que le cookie soit effacé ou expire, nous vérifions la valeur du cookie pour l'authentification.

```
else
    {//Cookie signé déjà stocké
        if(req.signedCookies.user=='admin')
        {
            res.send("BONJOUR UTILISATEUR GÉNUIN")
        }
        else
        {
     //Mauvaises informations, l'utilisateur est invité à s'authentifier à nouveau
            res.setHeader("WWW-Authenticate", "Basic")
            res.sendStatus(401)
        }
    }
})
```

Maintenant, vous savez comment authentifier un utilisateur avec des cookies ! 

Vous pouvez vérifier le cookie qui est stocké en naviguant vers la section Stockage des outils de développement de votre navigateur et en allant dans l'onglet Cookies. La valeur du cookie et les valeurs analysées sont affichées séparément dans deux sections (dans Firefox, par exemple).

## Comment authentifier un utilisateur avec des sessions

Examinons une analogie pour nous aider à comprendre les sessions par rapport aux cookies. Imaginez que vous êtes une personne étourdie qui oublie constamment les noms de vos amis. 

Une solution consiste à donner à chaque ami une carte avec son nom et son image. Chaque fois que vous les rencontrez, demandez simplement à voir la carte que vous leur avez donnée pour rafraîchir votre mémoire. 

Le problème est que vos amis peuvent perdre cette carte. Ou deux d'entre eux peuvent échanger des cartes et vous faire une farce. Ou peut-être que votre ami n'a pas assez d'espace pour stocker une autre carte. 

Dans tous les cas, le mécanisme d'authentification montre des signes de faiblesse. Mais c'est essentiellement ce que font les cookies - ils sont stockés côté client et chaque fois que le client fait une requête à leur site, le cookie est consulté pour l'authentification. Ils prennent de la place ou peuvent être falsifiés.

Au lieu d'utiliser des cookies, disons que vous faites une carte pour chaque ami et la gardez avec vous. Lorsque vous les voyez, vous attribuez un moyen de faire correspondre la carte avec la personne pour une identification facile. De cette façon, l'information ne réside pas avec le client et est donc plus sécurisée. 

Ce scénario nous montre comment fonctionnent les sessions. Les informations sur un utilisateur nouvellement authentifié résident sur le serveur, et seules des informations minimales sont renvoyées au client. De cette façon, le client peut être mappé à l'information stockée.

`express-session` crée un middleware de session qui vous permet de configurer facilement des sessions et de les manipuler. 

Le serveur de stockage par défaut côté serveur est MemoryStore. Pour stocker les informations de session sous forme de fichiers JSON, vous avez besoin de session-file-store. Le code ci-dessous fait ce qui suit :

* Il configure l'application Express
* Il indique au middleware de demander une authentification si aucune n'est spécifiée, et sinon de vérifier si le nom d'utilisateur et le mot de passe correspondent. 
* Si ce n'est pas le cas, il doit à nouveau faire la même demande d'authentification, sinon la session est établie. 
* Ensuite, il ajoute le nom d'utilisateur comme attribut utilisateur et le vérifie par la suite. 

Encore une fois, ce n'est qu'un simple exemple - les informations qui doivent être vérifiées par rapport aux données fournies doivent au moins être stockées dans une base de données.

```
let app=express()
app.use(session({
  store: new File_Store,
  secret: 'hello world',
  resave: true,
  saveUninitialized: true
}))
app.use('/', (req,res,next)=>{
  if(!req.session.user)
  {
    console.log("Session non configurée pour l'instant")
    if(!req.headers.authorization)
    {
      console.log("Aucun en-tête d'authentification")
      res.setHeader("WWW-Authenticate", "Basic")
      res.sendStatus(401)
    }
    else
    {
      auth_stuff=new Buffer.from(req.headers.authorization.split(" ")[1], 'base64')
      step1=auth_stuff.toString().split(":")
      console.log("Step1: ", step1)
      if(step1[0]=='admin' && step1[1]=='admin')
      {
        console.log('UTILISATEUR GÉNUIN')
        req.session.user='admin'
        res.send("UTILISATEUR GÉNUIN")
      }
      else
      {
        res.setHeader("WWW-Authenticate", "Basic")
        res.sendStatus(401)
      }
    }
  }
```

## Comment authentifier les utilisateurs avec le middleware Passport.js

Jusqu'à présent, nous avons vu comment authentifier les utilisateurs avec des cookies et des sessions. Maintenant, nous allons voir une troisième méthode d'authentification.

Passport.js est un middleware d'authentification pour Node qui vous permet d'authentifier les utilisateurs en utilisant des sessions et OAuth. Il vous permet également de créer des stratégies personnalisées et bien plus encore.

```
let passport=require('passport')
let bcrypt=require('bcrypt-nodejs')
let User_Obj=require('./Set_Up_Database_Stuffs')
const local_strategy=require('passport-local').Strategy
```

Ce code configure tous les modules nécessaires pour définir une stratégie locale appropriée. La stratégie `passport-local` permet l'authentification avec un nom d'utilisateur et un mot de passe uniquement. 

Assurez-vous que le nom de l'élément d'entrée du formulaire pour le nom d'utilisateur est "username" et pour le mot de passe est "password". Bien que cela semble très intuitif, cela m'a causé beaucoup de problèmes car j'avais négligé cette partie. Maintenant, c'est l'une de ces choses que je ne suis pas susceptible de négliger à nouveau (au moins pour un futur proche). 

Vous pouvez également changer les noms par défaut des champs en passant un JSON avant la fonction de rappel dans l'appel à `local_strategy`, où la structure JSON est `usernameField`: "Un nouveau nom pour ce champ", et `passwordField`: "Un nouveau nom pour ce champ".

```
passport.use(new local_strategy(
    async (username, password, done)=>{
        console.log("Ici à l'intérieur de local_strategy" ,username, password)
    
    try
    {
        let row1=await User_Obj.findOne({username: username})
        console.log(row1)
        //row1 devrait être le tuple de la base de données où le champ username correspond au username fourni.
        if(row1==null)
        {
            console.log("AUCUN ENREGISTREMENT TROUVÉ")
            return done(null, false)
        }
        else
        {
            console.log("Enregistrement trouvé")
            console.log(row1)
            if(bcrypt.compareSync(password, row1.password))//Comparer le mot de passe en texte brut avec le hash
            {
                console.log("Les mots de passe correspondent")
                console.log("Authentification locale terminée")
                return done(null, row1)
            }
            else
                {
                    console.log("Les mots de passe ne correspondent pas")
                    return done(null, false)
                }
        }
        
    }
    catch(err){
        console.log("Une erreur ici")
        return done(err)}
    }
  ));
```

Les lignes ci-dessus sont une implémentation simpliste de `local-strategy` où les données sont vérifiées à partir d'une base de données avec le nom d'utilisateur comme champ.

```javascript
app.post('/auth', passport.authenticate('local', {successRedirect: 'articles', failureRedirect: '/failurepage'}))
//Déclenche la stratégie locale. Si succès, redirige vers la page articles, sinon affiche la page d'échec
app.post('/donesignup', objForUrlencoded, async (req,res)=>{
    console.log(req.body)
    try
    {
        let row1=await User_Obj.findOne({username: req.body.username})
        console.log(row1)
        if(row1!=null)
        {
            console.log("Ce nom d'utilisateur existe déjà")
            res.render('signup')
        }
        else
        {
            console.log(bcrypt.hashSync(req.body.password[0], bcrypt.genSaltSync(8), null))//Obtenir le hash du mot de passe pour le stocker dans la base de données
            let save_this=User_Obj({username: req.body.username, password: bcrypt.hashSync(req.body.password[0], bcrypt.genSaltSync(8), null)})
            console.log(save_this)
            save_this.save()
            console.log("ENREGISTRÉ")//Enregistrer dans la base de données
        }
    }
    catch(err){}
})
```

Chaque fois que l'utilisateur accède à la route /auth, cela déclenche la stratégie locale qui s'exécute comme spécifié. En cas d'échec lors de l'authentification, il redirige vers une page d'échec. Sinon, il redirige vers une page d'articles (ou toute autre page dont vous avez besoin). 

Sur une requête POST à /donesignup, il vérifie si le nom d'utilisateur existe déjà. Si ce n'est pas le cas, il l'ajoute comme un tuple à la base de données, où les champs sont le nom d'utilisateur et un hash du mot de passe donné.

## Conclusion

Cela conclut mon résumé des différentes méthodes d'authentification dans Node. 

Le code utilisé ici est loin d'être idéal, mais j'espère qu'il aidera quelqu'un qui commence tout juste à apprendre l'authentification et se sentait submergé. 

Si vous avez lu jusqu'ici, merci beaucoup et veuillez corriger les bugs qui ont pu se glisser, malgré mes meilleurs efforts. Merci encore et bon codage.
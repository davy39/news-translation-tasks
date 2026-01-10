---
title: Le Top 10 de l'OWASP – Une plongée technique approfondie dans la sécurité web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-02T15:40:01.000Z'
originalURL: https://freecodecamp.org/news/technical-dive-into-owasp
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/New-Project.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Web Security
  slug: web-security
seo_title: Le Top 10 de l'OWASP – Une plongée technique approfondie dans la sécurité
  web
seo_desc: 'By Dipto Karmakar

  In terms of security, there are many vulnerabilities that need to be treated and
  prevented, but some need more attention than others. Without question, the best
  guide to help you address these security issues is The Open Web Applica...'
---

Par Dipto Karmakar

En matière de sécurité, il existe de nombreuses vulnérabilités qui doivent être traitées et prévenues, mais certaines nécessitent plus d'attention que d'autres. Sans aucun doute, le meilleur guide pour vous aider à résoudre ces problèmes de sécurité est le projet Open Web Application Security Project.

[OWASP](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/) a commencé comme un simple projet pour sensibiliser les développeurs et les gestionnaires aux problèmes de sécurité web les plus courants. Et aujourd'hui, il est devenu une norme en matière de sécurité des applications.

Dans cet article, nous donnerons un aperçu technique plus approfondi de certaines des vulnérabilités répertoriées dans le projet OWASP et de la manière de les atténuer. Nous ferons des exemples de mauvais code - bon code côte à côte pour vous aider à mieux comprendre et prévenir ces types d'attaques et à améliorer votre [sécurité des applications web](https://en.wikipedia.org/wiki/Web_application_security).

## Injection

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FYrozLEA.png)

Ce type de vulnérabilité se produit lorsqu'un programme permet à un attaquant de fournir des données d'entrée non fiables/malveillantes. Cela amène l'interpréteur à exécuter des commandes inattendues, généralement pour révéler des données qui devraient autrement être inaccessibles ou pour contourner une implémentation de sécurité.

La cause la plus courante des vulnérabilités d'injection résulte de l'échec d'un logiciel à **filtrer**, **valider** ou **nettoyer** les entrées d'un utilisateur.

Examinons deux exemples de "mauvaises implémentations de code" qui permettent aux attaques par injection de se produire.

### Exemple de mauvais code 1 :

Supposons que vous avez une route de connexion qui reçoit un email et, pour une raison quelconque, reçoit le mot de passe déjà haché.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/79C3zK_C.png)
_Exemple de mauvais code 1_

Si nous connaissons l'adresse email d'un utilisateur, par exemple _myemail@email.com_, alors nous pouvons contourner facilement ce système de connexion en envoyant l'objet JSON suivant, qui crée une injection NoSQL.

```json

{
        "email": "myemail@email.com",
        "password": { "$ne": "" }
}
```

Cet objet instruira MongoDb de trouver un utilisateur avec l'email "myemail@email.com" et avec un mot de passe différent d'une chaîne vide.

Cet exemple peut sembler un peu tiré par les cheveux, mais regardez le code suivant et voyez si vous pouvez repérer le problème.

### Exemple de mauvais code 2 :

Pour cet exemple, nous avons un formulaire d'inscription sur l'interface avec le code suivant côté serveur :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/5i2HmYIn-1.png)
_Mauvais exemple 2_

![Image](https://www.freecodecamp.org/news/content/images/2020/04/qmPOUeDN-1.png)
_Vue d'inscription_

Comment pouvons-nous exploiter ce code ? Très simple : disons pour cet exemple que le schéma Utilisateur ressemble à ceci :

```javascript
export const UserSchema = new mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    admin: {
        type: Boolean,
        default: false
    },
    accountConfirmed: {
        type: Boolean,
        default: false
    },
}, 
);
```

Maintenant, envoyez simplement la requête POST suivante avec Postman ou tout autre outil que vous préférez utiliser :

```json
{
    "email": "my-email",
    "password": "123321",
    "admin": "true",
    "accountConfirmed": "true"
}
```

Et maintenant vous êtes inscrit avec succès sur ce site web – non pas en tant qu'utilisateur simple, mais avec un compte administrateur confirmé.

Le problème ici est que si nous utilisons simplement :

```javascript
{ ...req.body }
```

alors nous créerons un nouvel objet utilisateur avec toutes les propriétés à l'intérieur de l'objet _body_, donc ici nous pouvons injecter tout ce que nous voulons.

### Refactorisation

Refactorisons le code des deux exemples pour prévenir ce type d'attaque.

Pour le premier exemple, nous pouvons vérifier le type attendu pour l'email et le mot de passe. Dans notre cas, nous attendons une chaîne de caractères dans les deux champs :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/-4b0HFdz.png)

Si nous fournissons à nouveau les mêmes paramètres :

```json
{
	"email": "myemail@email.com",
	"password": { "$ne": "" }
}
```

Nous recevrons une réponse **400 Bad Request**. Nous pouvons aller encore plus loin et vérifier si l'email est réellement un email et non pas une simple chaîne de caractères, mais cela est hors de notre portée pour l'instant.

Pour le deuxième exemple, nous pouvons utiliser une validation d'entrée côté serveur en "liste blanche" en supprimant les propriétés indésirables :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mHTYhaTW.png)

Ces exemples concernaient l'injection NoSQL, mais cette technique peut également être étendue à l'injection [SQL](https://github.com/qazbnm456/awesome-web-security#sql-injection).

## Utilisation de composants avec des vulnérabilités connues

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mUl2Q-DQ-1.png)

Ci-dessus, nous avons vu quelques normes de sécurité mal implémentées qui résultaient de nos erreurs. Cependant, il existe des situations où le problème ne vient pas du code que nous avons écrit, mais du code open-source que nous utilisons dans notre projet.

Un attaquant peut exploiter les vulnérabilités de ces composants pour exécuter du code malveillant ou pour faire en sorte que le programme se comporte de manière indésirable.

Bien que cela semble être hors de votre contrôle, ce n'est pas le cas. Il existe des mesures que nous pouvons prendre pour prévenir ce type de problème.

Par exemple, nous pouvons faire un inventaire continu des versions des composants, à la fois côté client et côté serveur, et supprimer les dépendances et/ou fonctionnalités inutilisées.

Nous pouvons surveiller les sources de vulnérabilités dans les composants.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/-pKYG90o-1.png)
_Tableau de bord White Source_

Pour vous assurer que vos composants sont sécurisés, vous devez vérifier régulièrement les bases de données de vulnérabilités et appliquer rapidement les correctifs de sécurité. Cela vous aidera à rester protégé.

## Authentification compromise

![Image](https://www.freecodecamp.org/news/content/images/2020/04/S1l6-xYY.png)

Cette vulnérabilité entre en jeu lorsque les applications web implémentent de manière médiocre les techniques d'authentification/gestion de session. Cela donne aux attaquants l'accès à des comptes auxquels ils ne devraient autrement pas être autorisés à accéder.

Ce problème de sécurité est le plus répandu sous la forme d'attaques par force brute et lorsque les identifiants de session/jetons sont exposés de manière à pouvoir être facilement volés.

### Exemple de mauvais code 1 :

Prenons l'exemple du précédent extrait de code. Nous l'avons un peu modifié pour envoyer une réponse **401** (Non autorisé) lorsqu'aucun utilisateur n'est trouvé avec un email et un mot de passe donnés.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/XkdI14FZ.png)

Bien que ce soit le code refactorisé, il est toujours vulnérable à l'authentification compromise. Ici, si nous utilisons un mot de passe incorrect, nous obtenons une réponse 401. Mais si le mot de passe est faible, nous pouvons le forcer jusqu'à ce que nous le devinions.

### Refactorisation

Nous pouvons prévenir les attaques par force brute en utilisant simplement une limite de taux sur notre route. Maintenant, l'utilisateur a 3 chances de s'authentifier, après quoi il ne pourra plus envoyer de requêtes sur cette route pendant les 15 prochaines minutes (et recevra une réponse **429 Too many requests**).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/g37VnwlN.png)

Le type suivant de vulnérabilité sur ce sujet concerne particulièrement la mauvaise gestion des jetons web JSON.

### Exemple de mauvais code 2 :

L'exemple suivant est très fréquemment trouvé dans les systèmes de connexion :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/NawbB50i.png)

La plupart du temps, un système de connexion utilisant JWT est implémenté de cette manière. Après que l'utilisateur envoie les bonnes informations d'identification, un jeton est généré en utilisant leur **id** ou une autre valeur **unique**. Ensuite, le jeton est envoyé au front-end où il sera enregistré dans l'application. Ou si une authentification persistante est nécessaire, il sera enregistré dans les cookies ou le stockage local.

Le problème avec cette approche est que le jeton qui devrait être sécurisé peut maintenant être accessible via le code front-end, le rendant ainsi vulnérable. Un code malveillant injecté dans le JavaScript front-end pourrait accéder aux cookies ou au stockage local et voler ce jeton.

### Refactorisation

Ce problème peut être surmonté avec la prochaine implémentation.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/wcKOH3Gm.png)

Cette fois, le jeton est également enregistré dans les cookies, mais il est enregistré à partir du code back-end avec la propriété **httpOnly**. Cela signifie qu'il ne peut pas être accessible à partir de tout code s'exécutant sur le front-end.

Pour le rendre plus sécurisé, le jeton est enregistré avec la propriété **signed**, ce qui fait que les cookies sont signés avec une clé secrète.

Vous pouvez aller encore plus loin et bloquer le protocole **http** avec le **secure flag** qui force le cookie à être envoyé via **https**.

## Exposition de données sensibles

![Image](https://www.freecodecamp.org/news/content/images/2020/04/H_NQWQ7g.png)

Comme son nom l'indique, cette vulnérabilité se produit lorsqu'une application web ne protège pas suffisamment les données sensibles.

Bien que les récents changements législatifs tels que le [GDPR](https://www.ncsc.gov.uk/information/GDPR) devraient garantir que les données sensibles ne sont pas exposées, un pourcentage important d'applications web ne répond pas à ces exigences.

Cela se produit généralement lorsque les données sont transmises en texte clair en utilisant HTTP, SMTP et FTP, ou lorsque des algorithmes cryptographiques faibles/anciens sont utilisés.

Un scénario probable peut être le suivant :

Un site web n'utilise pas ou n'impose pas TLS pour toutes les pages. Un attaquant surveille le trafic réseau, rétrograde les connexions de HTTPS à HTTP, intercepte les requêtes et vole les informations envoyées. Peut-être volent-ils même le cookie de session de l'utilisateur, accédant ainsi ou modifiant les données privées de l'utilisateur.

Un autre scénario peut être :

Les mots de passe sont stockés dans la base de données non salés ou sous forme de hachages simples et faibles. Une faille de téléchargement de fichier ou toute autre attaque permet à un attaquant de récupérer la base de données des mots de passe. Après cela, tous les hachages peuvent être exposés avec une table arc-en-ciel de valeurs pré-calculées, donnant ainsi à l'attaquant le mot de passe en clair réel des utilisateurs.
---
title: Comment sécuriser vos API Node.js – Bonnes pratiques de sécurité
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-04-25T16:05:07.993Z'
originalURL: https://freecodecamp.org/news/how-to-harden-your-nodejs-apis-security-best-practices
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745597082780/c803850d-f482-4fcc-a744-4de8fd8a02d8.png
tags:
- name: hacking
  slug: hacking
- name: Node.js
  slug: nodejs
- name: https
  slug: https
- name: ethicalhacking
  slug: ethicalhacking
- name: injection attacks
  slug: injection-attacks
seo_title: Comment sécuriser vos API Node.js – Bonnes pratiques de sécurité
seo_desc: 'If you’ve built an API with Node.js, chances are you’ve thought about security
  – at least a little.

  Maybe you’ve heard about SQL injection, brute force attacks, or data leaks.

  But here’s the thing: it’s not just about big hacks. Even small gaps in yo...'
---

Si vous avez construit une API avec Node.js, il est probable que vous ayez pensé à la sécurité – au moins un peu.

Peut-être avez-vous entendu parler des injections SQL, des attaques par force brute ou des fuites de données.

Mais voici le problème : ce n'est pas seulement une question de grosses attaques. Même de petites failles dans votre API peuvent entraîner de gros problèmes. Et personne ne veut recevoir ce message "vos données ont été exposées".

Dans cet article, je vais vous expliquer sept façons de sécuriser votre API Node.js.

Ce sont des conseils pratiques que vous pouvez appliquer immédiatement. Je vais garder les exemples de code simples et le langage encore plus simple. Commençons.

## **1. Utiliser les variables d'environnement**

Stocker des données sensibles comme les identifiants de base de données, les clés API ou les secrets JWT directement dans votre code est risqué. Si votre code tombe entre de mauvaises mains, tout le reste aussi.

Au lieu de cela, stockez ces données dans un fichier `.env` et utilisez le package `dotenv` pour y accéder :

```plaintext
require('dotenv').config();
```

```plaintext
const dbPassword = process.env.DB_PASSWORD;
```

Assurez-vous de **jamais** commiter votre fichier `.env`. Ajoutez-le à votre fichier `.gitignore` pour le garder privé.

## **2. Valider toutes les entrées**

Les attaquants adorent les entrées utilisateur.

Si vous ne vérifiez pas ce qui entre dans votre API, ils y glisseront des commandes, injecteront du code ou feront planter votre application.

La meilleure façon de les arrêter est de valider chaque entrée. Utilisez un package comme `Joi` ou `zod` pour définir ce que votre API attend :

```plaintext
const Joi = require('joi');

const schema = Joi.object({
  username: Joi.string().alphanum().min(3).max(30).required(),
  password: Joi.string().pattern(new RegExp('^[a-zA-Z0-9]{6,30}$')).required()
});
const { error } = schema.validate(req.body);
if (error) {
  return res.status(400).send(error.details[0].message);
}
```

Dans le code ci-dessus, nous avons défini le type exact de données que le schéma attend. Ainsi, les données incorrectes sont bloquées avant d'atteindre votre logique ou votre base de données.

## **3. Limiter le débit de vos endpoints**

Les bots et les attaques par force brute fonctionnent en inondant votre serveur de requêtes. Une fois que votre serveur atteint sa limite, votre API plantera.

Définissez une limite sur la fréquence à laquelle un utilisateur peut appeler votre API en utilisant un middleware comme `express-rate-limit`. Voici un exemple.

```plaintext
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limite chaque IP à 100 requêtes par windowMs
});
app.use('/api/', limiter);
```

Le code ci-dessus restreint les requêtes API provenant d'une adresse IP à 100 par 15 minutes. C'est comme mettre un ralentisseur devant une voiture emballée.

## **4. Toujours utiliser HTTPS**

HTTP envoie des données en texte clair. Cela signifie que quiconque se trouve entre votre serveur et l'utilisateur peut les lire. HTTPS crypte tout. Ce n'est plus une option.

Si vous utilisez une plateforme comme Heroku ou Vercel, HTTPS est automatique. Si vous hébergez vous-même, vous pouvez le configurer avec des services comme Let's Encrypt.

De plus, forcez HTTPS sur tout le trafic entrant. Vous pouvez utiliser un middleware comme celui-ci :

```plaintext
app.use((req, res, next) => {
  if (req.headers['x-forwarded-proto'] !== 'https') {
    return res.redirect('https://' + req.headers.host + req.url);
  }
  next();
});
```

Cryptez la communication. Toujours.

## **5. Utiliser Helmet pour sécuriser les en-têtes HTTP**

Les en-têtes HTTP sont des paires clé-valeur envoyées dans les requêtes et les réponses sur le web. Ils donnent des informations supplémentaires sur ce qui est envoyé – comme qui l'envoie, de quel type il s'agit, comment il doit être traité, et plus encore.

Les en-têtes HTTP sont petits, mais ils peuvent être des outils puissants pour protéger votre application. `Helmet` est un middleware Node.js qui définit des en-têtes sécurisés pour vous.

```plaintext
const helmet = require('helmet');
app.use(helmet());
```

Helmet aide à prévenir les attaques comme le cross-site scripting (XSS), le clickjacking, et d'autres simplement en définissant les bons en-têtes.

Une ligne de code, un grand pas en avant en matière de sécurité.

## **6. Assainir les données pour prévenir les attaques par injection**

Les attaques par injection se produisent lorsque vous faites aveuglément confiance aux entrées et les insérez dans une commande ou une requête.

Par exemple, un attaquant pourrait soumettre un morceau de texte qui se transforme en commande dans votre base de données.

Vous devez assainir les données avant qu'elles n'atteignent une fonction sensible. Des bibliothèques comme `express-mongo-sanitize` ou `xss-clean` aident à nettoyer les entrées malveillantes.

```plaintext
const mongoSanitize = require('express-mongo-sanitize');
const xss = require('xss-clean');

app.use(mongoSanitize());
app.use(xss());
```

Cela supprime les caractères et scripts dangereux qui pourraient causer de réels dommages.

## **7. Utiliser une authentification et une autorisation fortes**

L'authentification consiste à savoir qui est l'utilisateur, et l'autorisation consiste à savoir ce qu'il peut faire. Vous avez besoin des deux, et ils doivent être solides.

Utilisez JWT (JSON Web Tokens) ou des sessions pour gérer les utilisateurs connectés. Voici un exemple rapide de JWT :

```plaintext
const jwt = require('jsonwebtoken');

const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, {
  expiresIn: '1h'
});
```

Vérifiez toujours le token avant de permettre à un utilisateur d'accéder aux routes protégées :

```plaintext
const decoded = jwt.verify(token, process.env.JWT_SECRET);
```

Et n'oubliez pas les rôles. Un utilisateur qui peut voir des données ne devrait pas pouvoir les supprimer sauf s'il est censé le faire.

## **Réflexions finales**

La sécurité n'est pas seulement une fonctionnalité – c'est une habitude. Vous ne pouvez pas tout faire en même temps, mais vous pouvez commencer par quelques changements clés.

Utilisez des variables d'environnement. Validez vos entrées. Ajoutez une limitation de débit. Passez à HTTPS. Installez Helmet. Assainissez tout. Verrouillez votre authentification.

Chacune de ces étapes est un petit verrou sur une grande porte. Plus vous en ajoutez, plus il est difficile pour quelqu'un de s'introduire. Alors prenez un peu de temps maintenant. Votre futur vous et vos utilisateurs vous en remercieront.

*Pour plus de tutoriels sur la cybersécurité,* [***rejoignez notre newsletter***](https://newsletter.stealthsecurity.sh/)*.* *Pour apprendre les bases de la cybersécurité offensive, consultez notre* [***Cours de démarrage en sécurité***](https://start.stealthsecurity.sh/)*.*
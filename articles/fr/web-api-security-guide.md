---
title: Comment prévenir les attaques d'API Web avec la validation des données – Guide
  de sécurité des API Web
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-04-03T09:13:45.000Z'
originalURL: https://freecodecamp.org/news/web-api-security-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/apidat.jpg
tags:
- name: api
  slug: api
- name: Validation
  slug: validation
- name: Web Security
  slug: web-security
seo_title: Comment prévenir les attaques d'API Web avec la validation des données
  – Guide de sécurité des API Web
seo_desc: 'Adequate data protection and user confidentiality are key responsibilities
  for web developers. Hence, it is important to ensure the highest possible security
  while building API endpoints.

  The act of application security is a shared responsibility amo...'
---

Une protection adéquate des données et la confidentialité des utilisateurs sont des responsabilités clés pour les développeurs web. Il est donc important d'assurer la plus haute sécurité possible lors de la création de points de terminaison d'API.

La sécurité des applications est une responsabilité partagée entre les développeurs client et serveur, et la négligence du rôle de l'un peut être désastreuse. Les [statistiques](https://www.statista.com/statistics/1307426/number-of-data-breaches-worldwide/#:~:text=During%20the%20fourth%20quarter%20of,concerns%20of%20company%20leaders%20worldwide.) montrent que les violations de données en 2023 ont entraîné l'exposition de plus de 8 millions d'enregistrements de données dans le monde.

Dans cet article, je vais mettre en lumière les domaines clés de la sécurité des API, qui impliquent la validation des données. Ce concept est assez crucial pour vous aider à protéger votre API contre les attaques web via des données utilisateur malveillantes. Ce tutoriel est bien adapté à tous les développeurs backend, quel que soit leur niveau d'expérience.

Pour pouvoir suivre ce tutoriel, voici quelques prérequis :

* Connaissance de Node.js
* Connaissance de npm et de l'installation de packages

Avec cela en place, commençons.

## Comment fonctionne la validation des données ?

Tout d'abord, qu'est-ce que la validation des données ? La validation des données consiste simplement à garantir l'exactitude et la fiabilité des données reçues de sources externes avant le traitement des données.

C'est un composant clé de la sécurité des API Web, car il est essentiel pour prévenir les attaques par injection web, les attaques SQL et les attaques NoSQL. Pour en savoir plus sur ces attaques, vous pouvez consulter ce [lien](https://owasp.org/www-community/Injection_Flaws#:~:text=Description,connected%20to%20the%20vulnerable%20application/).

Notez que la validation des données est nécessaire, mais pas limitée aux opérations backend suivantes :

* Connexion et inscription de l'utilisateur
* Requête de réponse
* Mise à jour des bases de données du serveur

Toutes ces opérations peuvent être utilisées comme des avenues par des pirates informatiques malveillants pour accéder à la base de données du serveur et obtenir des détails sensibles des utilisateurs, voire semer le chaos en formatant l'ensemble de la base de données.

## Outils populaires de validation des données

Jusqu'à présent, il existe de nombreux outils qui peuvent aider le programmeur à réaliser une validation efficace des données dans le développement d'API.

Ils vous évitent de réinventer la roue en utilisant de longs codes regex pour valider les données. Ils offrent de nombreuses fonctionnalités, y compris la gestion des erreurs et les fonctionnalités de personnalisation de la validation.

Certains de ces outils incluent :
• [Joi](https://joi.dev)
• [Zod](https://zod.dev/)
• [Yup](https://www.npmjs.com/package/yup)
• [AJv](https://ajv.js.org/)
• [Valibot](https://valibot.dev/)
• [Validator.js](https://www.npmjs.com/package/validatorjs)
• [Superstruct](https://docs.superstructjs.org/guides/02-validating-data)

Pour mieux éclairer ces outils, nous allons comparer certains des outils de validation de données les plus populaires mentionnés ci-dessus.

## Avantages et inconvénients des outils de validation des données

Pour vous éclairer davantage sur ces outils de validation JavaScript, je vais mettre en lumière certains avantages et inconvénients de trois de ces outils de validation JavaScript populaires.

### Joi

###### Avantages

* Il dispose d'une forte communauté d'utilisateurs et d'un soutien au développement
* Il possède des capacités intégrées pour gérer des validations complexes

###### Inconvénients

* Sa syntaxe est assez verbeuse

### Zod

###### Avantages

* Il est facilement compatible avec les projets TypeScript
* Il possède des capacités efficaces de gestion des erreurs

###### Inconvénients

* La validation asynchrone n'est pas supportée.

### Yup

###### Avantages

* Il utilise principalement une syntaxe déclarative pour définir son outil de validation, ce qui confère sa simplicité
* Il a une performance rapide comparable.

###### Inconvénients

* Il ne fournit pas de fonctionnalités de personnalisation
* Il a une capacité limitée à gérer des validations complexes

Pour les besoins de ce tutoriel, nous utiliserons Joi comme notre outil de validation de données.

## Introduction à Joi

Joi est un outil de validation de données simple et efficace basé sur JavaScript, qui est basé sur la configuration de type de schéma.

Il possède des capacités intégrées pour valider l'occurrence de données sous diverses formes, mais pas limitées aux booléens, chaînes, fonctions et intervalles. Il peut également gérer des opérations de validation complexes.

De plus, il fournit des fonctionnalités de mise en cache minimales. Plus d'informations sur l'outil peuvent être trouvées [ici](https://joi.dev/api/?v=17.12.2).

## Comment configurer Joi

Dans cette section, nous allons configurer Joi dans notre environnement local. Pour installer Joi, naviguez vers le dossier de code via la ligne de commande et exécutez ceci :

```bash
npm i joi
```

Un message confirmant l'installation réussie devrait s'afficher. Avec cela terminé, nous pouvons démontrer la puissance de Joi dans la validation de l'inscription des utilisateurs dans notre API de démonstration.

## Projet de démonstration

Dans ce projet, vous allez utiliser Joi pour valider l'entrée reçue du client dans le but de s'inscrire sur le serveur. Le code par défaut pour la fonction d'inscription de l'utilisateur pour l'application Node.js peut être trouvé [ici](https://github.com/oluwatobi2001/location-backend/blob/master/Controller/Authentication.js).

Allez-y et importez le package Joi installé dans votre code :

```js
const Joi = require("joi");
```

Avant d'écrire notre contrôleur d'inscription, nous allons initialiser la bibliothèque Joi dans le fichier de code :

```js
const SignUpSchema = Joi.object({});
```

Dans ce projet, nous allons valider les paramètres d'email, de mot de passe et de nom d'utilisateur reçus du client.

```js
const SignUpSchema = Joi.object({
    email: Joi.string().email({
        minDomainSegments: 2,
        tlds: {
            allow: ['com', 'net']
        }
    }),
    username: Joi.string().alphanum().min(3).max(15).required(),
    password: Joi.string().min(8).required()
});

```

L'objet du paramètre email garantit que l'adresse email est une chaîne et que le domaine est limité à .com et .net, interdisant d'autres formes de domaines.

Pour le paramètre de nom d'utilisateur, il garantit qu'il s'agit d'une chaîne contenant à la fois des lettres et des chiffres avec un nombre minimum de caractères de 3 et un nombre maximum de caractères de 15. La fonction required garantit que ces conditions doivent être remplies ou la demande entière ne sera pas validée.

Le paramètre de mot de passe garantit que le mot de passe fourni est au format chaîne avec un nombre minimum de caractères de 8, et il est également requis.

Pour l'appliquer à nos points de terminaison, nous incluons ceci dans la fonction du contrôleur :

```js
const { error, value } = SignUpSchema.validate(req.body, { abortEarly: false });
if (error) {
    res.status(400).json(error.details);
    return;
}

```

Cette fonction est exécutée avant d'insérer les détails de l'utilisateur dans la base de données. Le schéma tente de valider l'entrée reçue, puis procède à la base de données si elle est validée avec succès.

La fonction `abortEarly` est incluse pour permettre à tous les paramètres d'être évalués. Toutes les erreurs seront affichées s'il y en a.

Ce qui précède peut également être répliqué dans la fonction du contrôleur de connexion. Vous pouvez également consulter la [documentation](https://joi.dev/api/?v=17.12.2) pour d'autres exemples d'options de validation complexes utilisant Joi.

Le code final pour le projet est affiché ci-dessous :

```js
const jwt = require("jsonwebtoken");
const userSchema = require("../Schema/User");
const Joi = require("joi");
const bcrypt = require("bcrypt");
const { createNewColumn, checkRecordsExists, insertRecord } = require('../utils/sqlSchemaFunction');

const generateAccessToken = (use) => {
    return jwt.sign({ userID: use }, process.env.JWT, { expiresIn: "1d" });
}

const SignUpSchema = Joi.object({
    email: Joi.string().email({ minDomainSegments: 2, tlds: { allow: ['com', 'net'] } }),
    username: Joi.string().alphanum().min(3).max(15).required(),
    password: Joi.string().min(8).required()
});

const loginSchema = Joi.object({
    email: Joi.string().email({ minDomainSegments: 2, tlds: { allow: ['com', 'net'] } }),
    password: Joi.string().min(8).required()
});

const register = async (req, res) => {
    const email = req.body.email;
    const password = req.body.password;

    if (!email || !password) {
        res.status(400).json("Veuillez fournir l'email ou le mot de passe");
        return; 
    }

    const { error, value } = SignUpSchema.validate(req.body, { abortEarly: false });
    if (error) {
        res.status(400).json(error.details);
        return;
    }

    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password, salt);
    const user = {
        username: req.body.username,
        email: email,
        password: hashedPassword
    };

    try {
        const userAlreadyExists = await checkRecordsExists("users", "email", email);
        if (userAlreadyExists) {
            res.status(400).json("L'email doit être unique");
        } else {
            await insertRecord("users", user);
            res.status(200).json("Utilisateur créé avec succès");
        }
    } catch (err) {
        res.status(500).json({ err: err.message });
    }
};

module.exports = { register };


```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/SUccessValid-1.JPG)
_Test d'API dans Postman_

Garantir que le code suivait notre schéma défini a abouti à son exécution réussie.

## Conclusion

Avec cela, nous arrivons à la fin du tutoriel. J'espère que vous avez appris la validation des données, divers outils de validation des données et les meilleures pratiques de validation des données.

Vous pouvez également me contacter et consulter mes autres articles [ici](https://www.freecodecamp.org/news/author/oluwatobi/). Jusqu'à la prochaine fois, continuez à coder !
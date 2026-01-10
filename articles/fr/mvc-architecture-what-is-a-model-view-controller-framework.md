---
title: Architecture MVC – Qu'est-ce qu'un Framework Modèle Vue Contrôleur ?
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-24T17:36:14.000Z'
originalURL: https://freecodecamp.org/news/mvc-architecture-what-is-a-model-view-controller-framework
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/radowan-nakif-rehan-cYyqhdbJ9TI-unsplash.jpg
tags:
- name: software architecture
  slug: software-architecture
- name: Web Applications
  slug: web-applications
seo_title: Architecture MVC – Qu'est-ce qu'un Framework Modèle Vue Contrôleur ?
seo_desc: "Model–View–Controller is a popular software pattern used to break up the\
  \ logic of your application into three different components. \nIn this article,\
  \ I will break down the three components behind the MVC pattern, provide some history,\
  \ and show you ho..."
---

Modèle–Vue–Contrôleur est un modèle logiciel populaire utilisé pour diviser la logique de votre application en trois composants différents. 

Dans cet article, je vais décomposer les trois composants derrière le modèle MVC, fournir un peu d'histoire, et vous montrer comment il peut être utilisé dans une application.

## Histoire du modèle Modèle–Vue–Contrôleur

Le modèle MVC a été introduit pour la première fois en 1979 par le scientifique informatique Trygve Mikkjel Heyerdahl Reenskaug. Il voulait trouver une solution pour diviser une application utilisateur complexe en composants plus petits et gérables. 

Le modèle MVC a été utilisé pour la première fois dans le langage de programmation Small Talk. L'un des noms originaux pour le modèle était Modèle-Vue-Éditeur, mais il a été changé en Modèle-Vue-Contrôleur.

Tout au long des années 1980 et au début des années 1990, le modèle MVC était principalement utilisé dans les applications de bureau. Mais à la fin des années 1990, il est devenu assez populaire dans les applications web. 

Dans les applications web d'aujourd'hui, le modèle MVC est un choix de conception populaire pour organiser votre code. 

Voici une liste de quelques frameworks web populaires qui utilisent le modèle MVC.

* Ruby on Rails
* ASP.NET MVC
* Laravel
* Angular

## Quels sont les trois composants derrière le Modèle–Vue–Contrôleur ?

Voici une décomposition de base du modèle MVC :

* **Modèle** – Responsable de la logique des données derrière l'application
* **Vue** – Ce que l'utilisateur voit et avec quoi il interagit dans l'application
* **Contrôleur** – Agit comme le cerveau derrière l'application et communique avec le Modèle et la Vue. 

## Comment le modèle MVC fonctionne-t-il dans une application web ? 

Pour mieux comprendre comment le modèle MVC fonctionne, il serait préférable de vous le montrer dans une [application de démonstration](https://mvc-demo-app.netlify.app/). 

Cette application MERN (MongoDB, Express, React, Node) salue un gestionnaire de bureau fictif et lui montre un tableau des entraîneurs de lycée récemment embauchés. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-2.49.20-AM.png)

Elle montre également quels entraîneurs n'ont pas complété leurs tests TB, vaccins Covid, nouvelle application d'entraîneur et vérifications de casier judiciaire. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-2.49.54-AM.png)

Le gestionnaire de bureau peut envoyer des e-mails de rappel à ces entraîneurs qui manquent leurs documents. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-2.51.04-AM.png)

### Le composant Modèle

Le Modèle est responsable de la logique des données de notre application. J'utilise MongoDB pour la base de données des entraîneurs. 

J'ai d'abord dû définir les propriétés qui seront appliquées à chaque entraîneur dans la base de données. Chaque entraîneur aura un `nom`, `email`, `programme`, `application`, `backgroundCheck`, `tbTest` et `covidTest`.

```js
const coachSchema = new Schema({
    name: {
        type: String,
        trim: true,
        maxLength: 32,
        required: true
    },
    email: {
        type: String,
        trim: true,
        maxLength: 32,
        required: true,
        unique: true
    },
    program: {
        type: String,
        trim: true,
        maxLength: 32,
        required: true
    },
    application: {
        type: Boolean,
        required: true
    },
    backgroundCheck: {
        type: Boolean,
        required: true
    },
    tbTest: {
        type: Boolean,
        required: true
    },
    covidTest: {
        type: Boolean,
        required: true
    }
}, { timestamps: true })
```

`type:Boolean` représente une valeur vraie ou fausse pour les propriétés `application`, `backgroundCheck`, `tbTest` et `covidTest`.

Si l'entraîneur a l'une de ces quatre propriétés marquée comme fausse, cela signifie qu'il n'a pas complété cette partie du processus de candidature. 

J'ai créé sept entrées pour notre base de données d'entraîneurs et ces informations sont stockées dans MongoDB Atlas. 

Voici un exemple de l'une des entrées de la base de données.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-3.26.02-AM.png)

Le composant Contrôleur va communiquer avec la base de données et obtenir les informations nécessaires à envoyer au composant Vue. 

### Le composant Vue

Le composant Vue est responsable de tous les aspects visuels de l'application. J'ai utilisé React pour afficher ces données à l'utilisateur. 

Lorsque l'application se charge pour la première fois, vous voyez un message de bienvenue affiché à l'écran. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-2.48.25-AM.png)

Lorsque vous cliquez sur le bouton View Dashboard, il vous emmène au tableau des entraîneurs et à la liste des documents manquants. 

La Vue ne communique pas directement avec la base de données car notre Contrôleur le fait. Le Contrôleur fournit ces informations à la Vue afin qu'elles puissent être affichées sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-2.49.20-AM.png)

Voici à quoi ressemble le code lorsque la Vue effectue un appel fetch pour obtenir les données du Contrôleur :

```js
await fetch('https://mvc-project-backend.herokuapp.com/coaches')
```

Nous utilisons ensuite la méthode `map()` pour parcourir chaque entraîneur et afficher leur nom, adresse e-mail et programme dans le tableau.

```
    coachData.map(data => (
                        <tr key={data._id}>
                          <td>{data.name}</td>
                          <td>{data.email}</td>
                          <td>{data.program}</td>
                        </tr>
                      ))
```

Pour la section des documents manquants, nous récupérons les données du backend pour obtenir la liste des entraîneurs qui manquent des applications, des tests TB, des vaccins Covid et des vérifications de casier judiciaire. 

Nous utilisons à nouveau la méthode `map()` pour afficher les noms pour chaque catégorie. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-2.49.54-AM.png)

Lorsque le bouton `Send reminder email` est cliqué, ces informations sont envoyées de React au backend. Le Contrôleur est responsable de l'envoi de l'e-mail et de la communication avec la Vue pour indiquer si le message a été envoyé ou non.

En fonction des informations qu'il reçoit du Contrôleur, la Vue affichera un message de succès ou d'échec à l'utilisateur. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-4.11.16-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-5.03.48-AM.png)

### Le composant Contrôleur

Le Contrôleur communique avec les composants Modèle et Vue et prend en charge toute la logique de notre application. Cette section du code a été construite en Node.JS et Express. 

Le Contrôleur va obtenir la liste complète des entraîneurs du Modèle et envoyer ces informations à la Vue. 

Le Contrôleur est également responsable du filtrage à travers le Modèle et de la fourniture des listes d'entraîneurs qui n'ont pas complété les quatre catégories de documents manquants. 

Toutes ces données sont envoyées à la Vue pour qu'elles puissent être affichées à l'utilisateur. 

Pour la fonctionnalité d'e-mail, le Contrôleur est responsable de la vérification pour s'assurer que l'e-mail de l'expéditeur est valide avant d'envoyer l'e-mail.

J'ai utilisé Nodemailer ici pour envoyer les e-mails.

```js
   transporter.sendMail(mailOptions, (err) => {
        if (err) {
            console.log(`Applications: Il y a eu une erreur lors de l'envoi du message : ${err}`)
            res.json({ status: 'Échec de l\'e-mail' })
        } else {
            console.log(`Succès des applications : L\'e-mail a été envoyé`)
            res.json({ status: "E-mail envoyé" });
        }
    })
```

Si l'e-mail a été envoyé avec succès, l'utilisateur est alors notifié et le message e-mail apparaît dans le compte e-mail de démonstration.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-4.52.44-AM.png)

S'il y a une erreur dans l'envoi du message, le Contrôleur enverra ces informations à la Vue afin que le message d'erreur puisse être affiché à l'utilisateur. 

## Conclusion

Modèle–Vue–Contrôleur est un modèle logiciel populaire utilisé pour diviser la logique de votre application en trois composants différents. 

Alors que le modèle MVC était initialement utilisé dans les applications de bureau, il est devenu populaire dans les applications web à la fin des années 1990. 

Le Modèle est responsable de la logique des données derrière l'application.

La Vue est ce que l'utilisateur voit et avec quoi il interagit dans l'application.

Le Contrôleur agit comme le cerveau derrière l'application et communique avec le Modèle et la Vue. 

Les frameworks web qui utilisent le modèle MVC incluent Ruby on Rails, ASP.NET MVC, Laravel et Angular.
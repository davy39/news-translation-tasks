---
title: Comment créer un formulaire de contact avec SendGrid et Next.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-30T15:24:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-working-contact-form-with-sendgrid-and-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Blue-and-White-Modern-Corporate-Travel-YouTube-Thumbnail--5-.png
tags:
- name: email
  slug: email
- name: Next.js
  slug: nextjs
- name: sendgrid
  slug: sendgrid
seo_title: Comment créer un formulaire de contact avec SendGrid et Next.js
seo_desc: 'By Manu Arora

  Contact forms are useful on websites if you want your users to be able to interact
  with you over email. And there are lots of ways to build them.

  Traditionally you''d have either used PHP for sending emails over the server or
  some third ...'
---

Par Manu Arora

Les formulaires de contact sont utiles sur les sites web si vous souhaitez que vos utilisateurs puissent interagir avec vous par e-mail. Et il existe de nombreuses façons de les créer.

Traditionnellement, vous auriez utilisé soit PHP pour envoyer des e-mails via le serveur, soit un service tiers qui se chargerait de la logique des e-mails.

Mais dans cet article, nous allons parler de la manière d'envoyer des e-mails depuis votre application Next.js avec l'API SendGrid.

Nous allons créer une page simple – un formulaire de contact construit avec React – qui comporte des champs de saisie que nous validerons avant l'envoi. Nous connecterons le formulaire à l'API SendGrid qui se chargera d'envoyer les e-mails. Ensuite, à la fin de la journée, tout ce que vous avez à faire est de vérifier votre e-mail pour trouver ces requêtes.

Cependant, si vous n'avez pas encore de projet Next.js, vous pouvez facilement en créer un et l'intégrer avec Vercel en suivant les étapes mentionnées ci-dessous :

1. Créez un compte sur [Vercel](https://vercel.com) et cliquez sur `Nouveau Projet`

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-9.41.17-AM.png)

2. Choisissez le modèle comme `Next.js` :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-9.37.17-AM.png)

3. Nommez votre dépôt comme vous le souhaitez et cliquez sur créer le projet. (Choisissez GitHub, GitLab ou BitBucket pour votre gestion de version de code à distance)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-9.37.34-AM.png)

En suivant les trois points ci-dessus, vous aurez un dépôt sur votre compte de gestion de version.

## La pile technologique que nous allons utiliser

* [Next.js](https://nextjs.org) pour créer une page de destination de formulaire de contact
* [TailwindCSS](https://tailwindcss.com) pour styliser les composants
* [SendGrid](https://sendgrid.com) pour envoyer des e-mails en utilisant leurs API
* [Vercel](https://vercel.com) pour héberger notre application et CI/CD

Nous allons utiliser les routes API de Nextjs pour gérer les événements de formulaire. Les modules API fournissent un moyen flexible de gérer la logique backend dans notre application Next.js.

Tout code que nous écrivons dans le dossier API sera déployé en tant que fonction Serverless sur Vercel pour l'hébergement. Vous pouvez en savoir plus sur les routes API de Next.js [ici](https://nextjs.org/docs/api-routes/introduction)

Si vous avez déjà un projet Next.js où vous souhaitez configurer un formulaire de contact fonctionnel, c'est parfait. Dans ce cas, il vous sera facile de créer des pages et de commencer immédiatement.

Mais si vous n'avez pas encore de projet configuré, ce n'est pas grave – allez sur Vercel et créez un projet de démarrage Next.js et clonez le dépôt.

## Flux de l'application

Examinons le flux de l'application – ou comment l'envoi d'e-mails fonctionne réellement :

* L'utilisateur final remplit les 4 champs obligatoires et clique sur soumettre.
* À la soumission, la fonction `handleSubmit` est déclenchée.
* `handleSubmit` valide le formulaire pour les champs de saisie et vérifie qu'ils ne sont pas vides.
* Si les champs du formulaire ne sont pas vides, un appel API est fait à `api/sendgrid` où se trouve la logique d'envoi des e-mails.
* Dans `api/sendgrid`, le module `@sendgrid/mail` initialise une fonction `send` qui prend les clés API de votre application et envoie l'e-mail avec les champs requis.
* Si l'e-mail est livré avec succès, une réponse `200` est envoyée au client, sinon une réponse `400` est envoyée au client.
* Les réponses sont gérées au niveau du frontend et les messages appropriés sont affichés.

## Comment configurer TailwindCSS

La configuration de TailwindCSS est assez facile, et vous pouvez le faire de deux manières simples.

1. Installez TailwindCSS comme une dépendance dans votre projet :

```bash
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest

```

2. Initialisez un fichier de configuration TailwindCSS pour votre projet. Cela créera un fichier `tailwind.config.js` dans le répertoire racine :

```bash
npx tailwindcss init

```

Ensuite, vous devrez modifier le fichier de configuration, inclure les chemins `purge`, et activer le mode `jit` :

```javascript
module.exports = {
   purge: [],
   mode: 'jit',
   purge: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
    darkMode: false, // ou 'media' ou 'class'
    theme: {
      extend: {},
    },
    variants: {
      extend: {},
    },
    plugins: [],
  }
```

Vous utilisez `purge` pour supprimer les styles indésirables de votre projet au moment de la construction. C'est utile si vous souhaitez réduire la taille du bundle CSS.

`jit` est le nouveau mode TailwindCSS où vous pouvez spécifier des noms de classes dynamiques dans le code lui-même.

Par exemple, si vous souhaitez que la taille de votre texte soit de `10px` (qui n'est pas déjà présente dans les modules TailwindCSS), vous pouvez écrire `text-[10px]` dans vos noms de classes et cela se reflétera automatiquement. Plus besoin d'écrire des attributs de style personnalisés. 📫

Ensuite, importez les styles Tailwind dans votre fichier racine `_app.js` :

```js
// pages/_app.js
 import '../styles/globals.css'
 import 'tailwindcss/tailwind.css'

  function MyApp({ Component, pageProps }) {
    return <Component {...pageProps} />
  }

  export default MyApp
```

Ensuite, incluez le CSS de base de Tailwind dans votre feuille de style de niveau racine comme ceci :

```js
/* ./styles/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Avec cela, vous avez configuré avec succès TailwindCSS pour votre projet.

## Le balisage et le style pour la page de contact

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-12.08.53-PM.png)

Nous allons construire la page web entièrement avec Tailwind. J'ai obtenu la page elle-même directement depuis le [Tailwind Master Kit](https://tailwindmasterkit.com) qui est une bibliothèque de composants et de modèles pour les projets web Tailwind.

Passons en revue le HTML de la page (essentiellement le formulaire de contact) pour comprendre comment tout est implémenté :

```js
<form class="rounded-lg shadow-xl flex flex-col px-8 py-8 bg-white dark:bg-blue-500">
      <h1 class="text-2xl font-bold dark:text-gray-50">Envoyer un message</h1>

      <label for="fullname" class="text-gray-500 font-light mt-8 dark:text-gray-50">Nom complet<span class="text-red-500 dark:text-gray-50">*</span></label>
      <input type="text" name="fullname" class="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500" />

      <label for="email" class="text-gray-500 font-light mt-4 dark:text-gray-50">E-mail<span class="text-red-500">*</span></label>
      <input type="email" name="email" class="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500" />

      <label for="subject" class="text-gray-500 font-light mt-4 dark:text-gray-50">Sujet<span class="text-red-500">*</span></label>
      <input type="text" name="subject" class="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500" />

      <label for="message" class="text-gray-500 font-light mt-4 dark:text-gray-50">Message<span class="text-red-500">*</span></label>
      <textarea name="message" class="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500"></textarea>
      <div class="flex flex-row items-center justify-start">
        <button class="px-10 mt-8 py-2 bg-[#130F49] text-gray-50 font-light rounded-md text-lg flex flex-row items-center">
          Envoyer
          <svg width="24" height="24" viewBox="0 0 24 24" class="text-cyan-500 ml-2" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.00967 5.12761H11.0097C12.1142 5.12761 13.468 5.89682 14.0335 6.8457L16.5089 11H21.0097C21.562 11 22.0097 11.4477 22.0097 12C22.0097 12.5523 21.562 13 21.0097 13H16.4138L13.9383 17.1543C13.3729 18.1032 12.0191 18.8724 10.9145 18.8724H8.91454L12.4138 13H5.42485L3.99036 15.4529H1.99036L4.00967 12L4.00967 11.967L2.00967 8.54712H4.00967L5.44417 11H12.5089L9.00967 5.12761Z" fill="currentColor" />
          </svg>
        </button>
      </div>
    </form>
```

Le formulaire comporte 4 champs :
* Nom complet
* Email
* Sujet
* Message

Tous les champs sont obligatoires – et nous les validerons également plus tard. Vous vous attendez à ce que votre utilisateur vous fournisse toutes ses informations lors de l'envoi de l'e-mail.

Pour capturer les champs, nous allons utiliser le hook [useState()](https://reactjs.org/docs/hooks-state.html) de React pour nous assurer que nos données sont persistées dans l'application.

```js
export default function ContactUs() {
  const [fullname, setFullname] = useState("");
  const [email, setEmail] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");

    return (
		<form
          onSubmit={handleSubmit}
          className="rounded-lg shadow-xl flex flex-col px-8 py-8 bg-white dark:bg-blue-500"
        >
          <h1 className="text-2xl font-bold dark:text-gray-50">
            Envoyer un message
          </h1>

          <label
            htmlFor="fullname"
            className="text-gray-500 font-light mt-8 dark:text-gray-50"
          >
            Nom complet<span className="text-red-500 dark:text-gray-50">*</span>
          </label>
          <input
            type="text"
            value={fullname}
            onChange={(e) => {
              setFullname(e.target.value);
            }}
            name="fullname"
            className="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500"
          />
         

          <label
            htmlFor="email"
            className="text-gray-500 font-light mt-4 dark:text-gray-50"
          >
            E-mail<span className="text-red-500">*</span>
          </label>
          <input
            type="email"
            name="email"
            value={email}
            onChange={(e) => {
              setEmail(e.target.value);
            }}
            className="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500"
          />
          

          <label
            htmlFor="subject"
            className="text-gray-500 font-light mt-4 dark:text-gray-50"
          >
            Sujet<span className="text-red-500">*</span>
          </label>
          <input
            type="text"
            name="subject"
            value={subject}
            onChange={(e) => {
              setSubject(e.target.value);
            }}
            className="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500"
          />
         
          <label
            htmlFor="message"
            className="text-gray-500 font-light mt-4 dark:text-gray-50"
          >
            Message<span className="text-red-500">*</span>
          </label>
          <textarea
            name="message"
            value={message}
            onChange={(e) => {
              setMessage(e.target.value);
            }}
            className="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500"
          ></textarea>
          
          <div className="flex flex-row items-center justify-start">
            <button
              type="submit"
              className="px-10 mt-8 py-2 bg-[#130F49] text-gray-50 font-light rounded-md text-lg flex flex-row items-center"
            >
              Soumettre
              <svg
                width="24"
                height="24"
                viewBox="0 0 24 24"
                className="text-cyan-500 ml-2"
                fill="currentColor"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M9.00967 5.12761H11.0097C12.1142 5.12761 13.468 5.89682 14.0335 6.8457L16.5089 11H21.0097C21.562 11 22.0097 11.4477 22.0097 12C22.0097 12.5523 21.562 13 21.0097 13H16.4138L13.9383 17.1543C13.3729 18.1032 12.0191 18.8724 10.9145 18.8724H8.91454L12.4138 13H5.42485L3.99036 15.4529H1.99036L4.00967 12L4.00967 11.967L2.00967 8.54712H4.00967L5.44417 11H12.5089L9.00967 5.12761Z"
                  fill="currentColor"
                />
              </svg>
            </button>
          </div>
        </form>
	)
}
```

Remarquez l'attribut du formulaire `onSubmit={handleSubmit}`. C'est la fonction où nous allons réellement envoyer l'e-mail via SendGrid. Mais avant cela, créons un projet SendGrid et récupérons les `clés API`.

## Comment configurer un projet SendGrid

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-1.10.59-PM.png)

Tout d'abord, vous devez vous rendre sur la [page d'accueil](https://signup.sendgrid.com/) de SendGrid et vous inscrire pour un compte (si vous n'en avez pas déjà un).

Après avoir créé un compte avec succès, inscrivez-vous pour une clé API. Vous pouvez le faire [ici](https://app.sendgrid.com/guide/integrate/langs/nodejs).

Sendgrid vous demande de créer une identité d'expéditeur pour protéger contre le spam et les e-mails malveillants. Pour ce faire, allez sur la [page d'identité Sendgrid](https://app.sendgrid.com/settings/sender_auth) et cliquez sur `Créer un nouvel expéditeur` pour créer une identité d'expéditeur.

Vous devrez remplir un formulaire détaillé. Complétez simplement le formulaire et cliquez sur soumettre. Enfin, vérifiez simplement votre adresse e-mail et vous avez terminé.

Une fois que vous avez récupéré les `clés API`, créez un fichier `.env.local` dans votre environnement local et collez le code suivant :

```js
SENDGRID_API_KEY= VOTRE_CLE_API_ICI

```

Remplacez `VOTRE_CLE_API_ICI` par la clé API que vous venez de récupérer.

## Comment créer une route API Serverless

Créer une route API Serverless est assez facile avec Next.js.

Allez dans `/pages/api` et à l'intérieur du dossier `api`, créez un fichier appelé `sendgrid.js`.

```js
import sendgrid from "@sendgrid/mail";

sendgrid.setApiKey(process.env.SENDGRID_API_KEY);

async function sendEmail(req, res) {
  try {
    // console.log("REQ.BODY", req.body);
    await sendgrid.send({
      to: "mannuarora7000@gmail.com", // Votre email où vous recevrez les emails
      from: "manuarorawork@gmail.com", // votre adresse email de site web ici
      subject: `${req.body.subject}`,
      html: `<div>Vous avez reçu un email</div>`,
    });
  } catch (error) {
    // console.log(error);
    return res.status(error.statusCode || 500).json({ error: error.message });
  }

  return res.status(200).json({ error: "" });
}

export default sendEmail;

```

SendGrid nous demande d'initialiser un objet `sendgrid` avec les clés API avec la méthode `setApiKey()`. Initialisez l'objet avec votre clé API et vous pouvez envoyer des emails avec la méthode `send()`.

Il y a essentiellement quatre champs qui sont requis dans le corps de la méthode `send()` :

* `to` – L'adresse email où vous souhaitez que votre email soit livré
* `from` – Votre email SendGrid que vous avez utilisé pour la vérification de l'identité de l'expéditeur. Vos emails seront envoyés depuis cet email.
* `subject` – La ligne d'objet de l'email
* `message` – le corps du message de l'email

Nous allons construire nous-mêmes ces quatre paramètres afin de mieux comprendre nos emails. Voici le code mis à jour à partir du même extrait ci-dessus :

```js
import sendgrid from "@sendgrid/mail";

sendgrid.setApiKey(process.env.SENDGRID_API_KEY);

async function sendEmail(req, res) {
  try {
    await sendgrid.send({
      to: "votreemail@gmail.com", // Votre email où vous recevrez les emails
      from: "votreemail@gmail.com", // votre adresse email de site web ici
      subject: `[Lead du site web] : ${req.body.subject}`,
      html: `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
      <html lang="en">
      <head>
        <meta charset="utf-8">
      
        <title>The HTML5 Herald</title>
        <meta name="description" content="The HTML5 Herald">
        <meta name="author" content="SitePoint">
      <meta http-equiv="Content-Type" content="text/html charset=UTF-8" />
      
        <link rel="stylesheet" href="css/styles.css?v=1.0">
      
      </head>
      
      <body>
        <div class="img-container" style="display: flex;justify-content: center;align-items: center;border-radius: 5px;overflow: hidden; font-family: 'helvetica', 'ui-sans';">              
              </div>
              <div class="container" style="margin-left: 20px;margin-right: 20px;">
              <h3>Vous avez reçu un nouveau mail de ${req.body.fullname}, leur email est : 📧fe0f${req.body.email} </h3>
              <div style="font-size: 16px;">
              <p>Message :</p>
              <p>${req.body.message}</p>
              <br>
              </div>
              <img src="https://manuarora.in/logo.png" class="logo-image" style="height: 50px;width: 50px;border-radius: 5px;overflow: hidden;">
              <p class="footer" style="font-size: 16px;padding-bottom: 20px;border-bottom: 1px solid #D1D5DB;">Cordialement<br>Manu Arora<br>Développeur Logiciel<br>+91 9587738861</p>
              <div class="footer-links" style="display: flex;justify-content: center;align-items: center;">
                <a href="https://manuarora.in/" style="text-decoration: none;margin: 8px;color: #9CA3AF;">Site Web</a>
                <a href="https://manuarora.in/blog/" style="text-decoration: none;margin: 8px;color: #9CA3AF;">Blog</a>
                <a href="https://github.com/manuarora700/" style="text-decoration: none;margin: 8px;color: #9CA3AF;">GitHub</a>
                <a href="https://instagram.com/maninthere/" style="text-decoration: none;margin: 8px;color: #9CA3AF;">Instagram</a>
                <a href="https://linkedin.com/in/manuarora28/" style="text-decoration: none;margin: 8px;color: #9CA3AF;">LinkedIn</a>
                <a href="https://twitter.com/mannupaaji/" style="text-decoration: none;margin: 8px;color: #9CA3AF;">Twitter</a>
                
              </div>
              </div>
      </body>
      </html>`,
    });
  } catch (error) {
    // console.log(error);
    return res.status(error.statusCode || 500).json({ error: error.message });
  }

  return res.status(200).json({ error: "" });
}

export default sendEmail;

```

Si vous souhaitez envoyer du `html` dans le corps de l'email, vous devrez utiliser des styles en ligne qui sont également présents dans l'exemple.

Ici, nous utilisons essentiellement la méthode `send()` de SendGrid fournie par l'API SendGrid pour envoyer des emails. Nous utilisons la méthode `send()` avec l'objet `sendgrid` que nous avons initialisé avec la clé API. Cela garantit que nos emails sont sécurisés et livrés uniquement avec notre permission.

De plus, nous avons enveloppé le code dans un bloc `try - catch`. Cela garantit que notre application peut gérer les exceptions et les erreurs correctement. Si, pour une raison quelconque, l'envoi de l'email échoue, le code passe immédiatement dans le bloc `catch()` et nous retournons un objet `error`. Cela signifie qu'il y a eu un problème en back-end.

En fonction de la réponse de l'API du back-end, le front-end répond en conséquence et l'UI change.

Le style va dans l'attribut `html` à l'intérieur du corps de la méthode `send()`. La manière dont vous souhaitez styliser votre email dépend entièrement de vous. Ici, j'ai inclus un modèle simple avec un pied de page vers mon Twitter, Instagram, GitHub et site web, ainsi que le corps du message original que l'utilisateur final envoie.

Maintenant que notre route API est configurée, passons au front-end et apprenons à gérer correctement la réponse.

## Comment appeler l'API et gérer les réponses

Puisque notre route API est configurée, nous allons maintenant appeler notre API serverless et récupérer la réponse.

```js
import React, { useState } from "react";

export default function ContactUs() {
  const [fullname, setFullname] = useState("");
  const [email, setEmail] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");



  const handleSubmit = async (e) => {
    e.preventDefault();

    let isValidForm = handleValidation();

     
      const res = await fetch("/api/sendgrid", {
        body: JSON.stringify({
          email: email,
          fullname: fullname,
          subject: subject,
          message: message,
        }),
        headers: {
          "Content-Type": "application/json",
        },
        method: "POST",
      });

      const { error } = await res.json();
      if (error) {
        console.log(error);
        return;
      }
    console.log(fullname, email, subject, message);
  };
  return (
    <main>
        <form class="rounded-lg shadow-xl flex flex-col px-8 py-8 bg-white dark:bg-blue-500">
      <h1 class="text-2xl font-bold dark:text-gray-50">Envoyer un message</h1>

      <label for="fullname" class="text-gray-500 font-light mt-8 dark:text-gray-50">Nom complet<span class="text-red-500 dark:text-gray-50">*</span></label>
      <input type="text" name="fullname" class="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500" />

      <label for="email" class="text-gray-500 font-light mt-4 dark:text-gray-50">E-mail<span class="text-red-500">*</span></label>
      <input type="email" name="email" class="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500" />

      <label for="subject" class="text-gray-500 font-light mt-4 dark:text-gray-50">Sujet<span class="text-red-500">*</span></label>
      <input type="text" name="subject" class="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500" />

      <label for="message" class="text-gray-500 font-light mt-4 dark:text-gray-50">Message<span class="text-red-500">*</span></label>
      <textarea name="message" class="bg-transparent border-b py-2 pl-4 focus:outline-none focus:rounded-md focus:ring-1 ring-green-500 font-light text-gray-500"></textarea>
      <div class="flex flex-row items-center justify-start">
        <button class="px-10 mt-8 py-2 bg-[#130F49] text-gray-50 font-light rounded-md text-lg flex flex-row items-center">
          Envoyer
          <svg width="24" height="24" viewBox="0 0 24 24" class="text-cyan-500 ml-2" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.00967 5.12761H11.0097C12.1142 5.12761 13.468 5.89682 14.0335 6.8457L16.5089 11H21.0097C21.562 11 22.0097 11.4477 22.0097 12C22.0097 12.5523 21.562 13 21.0097 13H16.4138L13.9383 17.1543C13.3729 18.1032 12.0191 18.8724 10.9145 18.8724H8.91454L12.4138 13H5.42485L3.99036 15.4529H1.99036L4.00967 12L4.00967 11.967L2.00967 8.54712H4.00967L5.44417 11H12.5089L9.00967 5.12761Z" fill="currentColor" />
          </svg>
        </button>
      </div>
    </form>
    </main>
  );
}

```

Ici, nous appelons l'API que nous venons de créer avec `fetch`, qui est fourni par React.

Fetch appelle l'API serverless avec le corps comme ceci :

```js
body: JSON.stringify({
          email: email,
          fullname: fullname,
          subject: subject,
          message: message,
        })
```

Ce sont nos champs de formulaire avec les données du formulaire déjà remplies (vous vous souvenez de `useState()` ?) qui sont maintenant disponibles pour nous.

L'API répond soit par un succès, soit par un échec. Si c'est un succès, l'email est livré – sinon, le courrier n'est pas livré.

Pour que l'utilisateur final connaisse l'état du formulaire, nous devons afficher certains éléments d'UI. Mais avant cela, nous devons gérer ce qui se passe s'il y a des champs vides.

## Comment gérer la validation du formulaire et faire en sorte que l'UI réponde à la réponse de l'API

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-1.31.42-PM.png)

Nous devons nous assurer de 3 choses ici :

1. Tous les champs doivent être remplis – c'est-à-dire que nous ne pouvons pas soumettre le formulaire si l'un des champs est vide. De plus, l'utilisateur doit savoir pourquoi le formulaire ne se soumet pas. Pour cela, nous allons afficher des messages d'erreur.
2. Pendant que le formulaire est en cours de soumission, l'utilisateur doit savoir qu'un traitement est en cours. Pour cela, nous allons changer le texte du bouton lorsque le formulaire est en cours de soumission.
3. Lorsque le formulaire est soumis avec succès ou s'il échoue, nous allons afficher le statut final en bas du formulaire.

Créons une méthode `handleValidation()` pour vérifier la validation :

```js

  const handleValidation = () => {
    let tempErrors = {};
    let isValid = true;

    if (fullname.length <= 0) {
      tempErrors["fullname"] = true;
      isValid = false;
    }
    if (email.length <= 0) {
      tempErrors["email"] = true;
      isValid = false;
    }
    if (subject.length <= 0) {
      tempErrors["subject"] = true;
      isValid = false;
    }
    if (message.length <= 0) {
      tempErrors["message"] = true;
      isValid = false;
    }

    setErrors({ ...tempErrors });
    console.log("errors", errors);
    return isValid;
  };
```

La fonction est assez simple : elle vérifie tous les champs et retourne un booléen `isValid` si le formulaire est valide.

De plus, nous maintenons l'état de tous les champs pour afficher les messages d'erreur à la fin – essentiellement, nous sauvegardons les champs qui contiennent des erreurs.

Le code final ressemble à quelque chose comme ceci, avec le texte du bouton, les messages d'erreur et les validations de formulaire :

```js
import React, { useState } from "react";

export default function ContactUs() {
   // États pour les champs du formulaire de contact
  const [fullname, setFullname] = useState("");
  const [email, setEmail] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");

  //   État de validation du formulaire
  const [errors, setErrors] = useState({});

  //   Définition du texte du bouton lors de la soumission du formulaire
  const [buttonText, setButtonText] = useState("Envoyer");

  // Définition des états des messages de succès ou d'échec
  const [showSuccessMessage, setShowSuccessMessage] = useState(false);
  const [showFailureMessage, setShowFailureMessage] = useState(false);

  // Méthode de vérification de validation
  const handleValidation = () => {
    let tempErrors = {};
    let isValid = true;

    if (fullname.length <= 0) {
      tempErrors["fullname"] = true;
      isValid = false;
    }
    if (email.length <= 0) {
      tempErrors["email"] = true;
      isValid = false;
    }
    if (subject.length <= 0) {
      tempErrors["subject"] = true;
      isValid = false;
    }
    if (message.length <= 0) {
      tempErrors["message"] = true;
      isValid = false;
    }

    setErrors({ ...tempErrors });
    console.log("errors", errors);
    return isValid;
  };

  //   Gestion de la soumission du formulaire

  const handleSubmit = async (e) => {
    e.preventDefault();

    let isValidForm = handleValidation();

    if (isValidForm) {
      setButtonText("Envoi en cours");
      const res = await fetch("/api/sendgrid", {
        body: JSON.stringify({
          email: email,
          fullname: fullname,
          subject: subject,
          message: message,
        }),
        headers: {
          "Content-Type": "application/json",
        },
        method: "POST",
      });

      const { error } = await res.json();
      if (error) {
        console.log(error);
        setShowSuccessMessage(false);
        setShowFailureMessage(true);
        setButtonText("Envoyer");
        return;
      }
      setShowSuccessMessage(true);
      setShowFailureMessage(false);
      setButtonText("Envoyer");
    }
    console.log(fullname, email, subject, message);
  };
  return (
    <main>
      // Le reste du code JSX va ici. (Avec les champs du formulaire)
    </main>
  );
}

```

Lorsque le formulaire est livré avec succès, nous obtenons une belle réponse dans l'UI. Pour livrer cette réponse, nous avons les états `showSuccessMessage` et `showFailureMessage`. Si la réponse de la route API back-end ne contient pas la propriété `error`, cela signifie que la soumission du formulaire a réussi et que l'email a été envoyé.

Dans ce cas, `showSuccessMessage` est défini sur True, ce qui affiche le balisage correspondant juste en dessous de la boîte de formulaire. Si le corps de la réponse contient la propriété `error`, `showFailureMessage` est défini sur True et le message correspondant est affiché à l'écran.

Dans les scénarios de succès et d'échec, nous devons réinitialiser le texte du bouton sur `envoyer` au lieu de `envoi en cours`. Pour cela, nous utilisons l'état `setButtonText('envoyer')` qui définit le texte du bouton en cas d'échec ou de succès. Nous définissons le texte du bouton sur `envoi en cours` lorsque le bouton Envoyer est cliqué.

## Comment recevoir des emails et des réponses UI

Lorsque l'email est livré avec succès, nous obtenons un message de succès dans le formulaire de contact lui-même.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-1.37.32-PM.png)

Et vous recevrez avec succès un email avec le modèle que nous venons de créer, livré en toute sécurité par SendGrid 📫

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-1.38.54-PM.png)

## Variables d'environnement

Veuillez noter que nous utilisons les clés API et que les clés sont sensibles. Cela signifie que nous devons toujours stocker les clés secrètes ou API dans des variables d'environnement.

Comme nous avons déjà `.env.local` pour notre environnement local, le fournisseur d'hébergement doit également connaître les clés API.

Vercel fournit un moyen facile de stocker les clés API sur le panneau d'hébergement lui-même.

Pour stocker les clés API en toute sécurité dans votre compte Vercel, procédez comme suit :

* Allez sur la page de vos projets
* Allez dans les paramètres
* Allez dans les variables d'environnement
* Ajoutez le nom de la variable d'environnement, dans notre cas, c'est `SENDGRID_API_KEY`, et ajoutez la clé API correspondante dans le champ de valeur.
* Redéployez votre application et votre projet fonctionnera dans un environnement de production.

## Démo en direct et code source

Voici le code source et une démo en direct de l'application :

[Démo en direct](https://sendgrid-contact-form.vercel.app/)
[Code source](https://github.com/manuarora700/sendgrid-contact-form)

## Conclusion

SendGrid est une excellente option à utiliser pour envoyer des emails depuis un site web. Lorsque vous l'intégrez avec Next.js et leurs routes API serverless, il devient extrêmement facile d'intégrer des formulaires dans n'importe quelle partie de votre site web.

SendGrid vous donne également la possibilité d'intégrer des modèles où vous pouvez avoir des thèmes personnalisés pour vos emails.

Il existe d'autres options pour envoyer des emails comme [Nodemailer](https://nodemailer.com/about/) que j'ai utilisé par le passé et que j'utilise encore pour certains de mes projets.

Il m'a fallu environ une heure pour construire cette application à partir de zéro – tout cela grâce à Next.js, TailwindCSS et SendGrid pour leur flux de travail et leur sémantique API extrêmement intuitifs. Merci également au [Tailwind Master Kit](https://tailwindmasterkit.com) pour la belle UI de la page de contact.

Si vous avez aimé ce blog, essayez de l'implémenter dans votre propre site web afin de pouvoir contacter vos utilisateurs finaux.

Si vous souhaitez donner un retour, contactez-moi sur mon [compte Twitter](https://twitter.com/mannupaaji) ou visitez mon [site web](https://manuarora.in)

Bon codage. 😊
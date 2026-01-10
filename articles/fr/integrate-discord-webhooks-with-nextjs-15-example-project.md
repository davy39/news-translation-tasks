---
title: Comment intégrer les Webhooks Discord avec Next.js 15 – Exemple de projet
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2025-01-21T14:03:19.995Z'
originalURL: https://freecodecamp.org/news/integrate-discord-webhooks-with-nextjs-15-example-project
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737468174839/93832182-b4a9-48c0-aee5-cd8d716fc47a.png
tags:
- name: Next.js
  slug: nextjs
- name: discord
  slug: discord
- name: webhooks
  slug: webhooks
seo_title: Comment intégrer les Webhooks Discord avec Next.js 15 – Exemple de projet
seo_desc: You’ve likely seen (or used) contact forms on websites that ask for customer
  feedback, potential work opportunities, customer contact info, and so on. But do
  you know what’s required to get all that feedback, contact info, and data sent to
  a private ...
---

Vous avez probablement vu (ou utilisé) des formulaires de contact sur des sites web qui demandent des retours clients, des opportunités de travail potentielles, des informations de contact de clients, et ainsi de suite. Mais savez-vous ce qui est nécessaire pour envoyer tous ces retours, informations de contact et données à un canal de texte Discord privé dès que l'utilisateur les soumet ?

Dans ce cas, il n'y a pas de base de données pour stocker les informations. Plutôt, vous avez simplement un canal de texte Discord gratuit qui conserve les données sous forme de séquence de messages dans le chat. Et un administrateur/modérateur/utilisateur avec les droits d'accès requis peut lire ces messages et prendre les mesures appropriées.

Au cas où vous seriez nouveau sur Discord, c'est une excellente plateforme pour discuter, jouer à des jeux vidéo, passer des appels, et même gérer une équipe virtuelle pour votre startup. C'est gratuit, et vous pouvez le télécharger depuis [ici](https://discord.com/).

D'accord, revenons au sujet, j'avais une exigence comme celle-ci à implémenter en utilisant le webhook de Discord et Next.js. J'ai beaucoup appris de cette activité. J'ai donc écrit ce tutoriel étape par étape sur ce processus.

L'objectif principal ici est de comprendre :

* Qu'est-ce qu'un Webhook et quels sont les cas d'utilisation ?

* Comment intégrer un webhook avec un framework d'application web comme Next.js

* Comment construire une interface utilisateur avec les dernières API et composants de Next.js

J'espère que vous allez aimer cela. Si vous souhaitez apprendre à partir d'une vidéo, l'article est également disponible sous forme de tutoriel vidéo :

%[https://www.youtube.com/watch?v=6h-y1aRzvhY]

## Table des matières

1. [Qu'est-ce qu'un Webhook ?](#heading-quest-ce-quun-webhook)

2. [Comment configurer un Webhook sur Discord](#heading-comment-configurer-un-webhook-sur-discord)

3. [Comment créer un projet Next.js](#heading-comment-creer-un-projet-nextjs)

4. [Comment définir les variables d'environnement](#heading-comment-definir-les-variables-environnement)

5. [Comment intégrer le Webhook avec le composant Form de Next.js](#heading-comment-integrer-le-webhook-avec-le-composant-form-de-nextjs)

* [Créer le Formulaire](#heading-creer-le-formulaire)

* [Créer l'Action Serveur](#heading-creer-laction-serveur)

6. [Comment mettre à jour la page de l'application](#heading-comment-mettre-a-jour-la-page-de-lapplication)

7. [Testons cela](#heading-testons-cela)

8. [Comment améliorer le retour de message en utilisant le hook useActionState de React 19](#heading-comment-ameliorer-le-retour-de-message-en-utilisant-le-hook-useactionstate-de-react-19)

* [Configurer un toaster](#heading-configurer-un-toaster)

* [Améliorer le Formulaire avec le hook useActionState](#heading-ameliorer-le-formulaire-avec-le-hook-useactionstate)

* [Comment mettre à jour l'Action Serveur pour retourner des résultats](#heading-comment-mettre-a-jour-laction-serveur-pour-retourner-des-resultats)

9. [Testons une fois de plus](#heading-testons-une-fois-de-plus)

10. [Code source et ressources](#heading-code-source-et-ressources)

## Qu'est-ce qu'un Webhook ?

Supposons que nous avons un service d'email qui se connecte à un expéditeur d'email tiers pour envoyer des emails aux utilisateurs. Traditionnellement, il y aura une passerelle API pour communiquer avec le service d'email depuis les appareils clients. Lorsque la demande est reçue, le service d'email contactera le fournisseur d'envoi d'email.

Pendant que le fournisseur d'envoi d'email traite les emails, le service d'email doit connaître leur statut. Une méthode générique pour gérer cela est que le service d'email interroge le statut à une fréquence courte et met à jour le client dès que le statut change. Mais cette méthode présente de nombreux inconvénients, tels que la mauvaise utilisation des ressources, des connexions inutiles et de mauvaises performances.

Au contraire, que diriez-vous que le service d'email enregistre une URL de rappel que l'expéditeur d'email peut appeler avec les informations pertinentes lorsque l'action d'envoi d'email a été terminée ? De cette façon, il n'y a pas d'interrogation inutile. Plutôt, l'expéditeur d'email peut informer proactivement le service d'email d'un succès ou d'un échec après avoir tenté d'envoyer l'email. Ensuite, le service d'email peut répondre aux clients concernant leur statut en conséquence.

Ce rappel enregistré est appelé un `Webhook`. Les Webhooks sont largement utilisés aujourd'hui dans divers secteurs comme les paiements et le checkout, la surveillance de la santé du système, et les intégrations d'applications tierces.

![Flux de Webhook](https://cdn.hashnode.com/res/hashnode/image/upload/v1735270052821/366027ef-bd79-4825-ba51-58cdaf3d3705.png align="center")

## Comment configurer un Webhook sur Discord

Vous devriez maintenant avoir une idée de comment fonctionnent les webhooks, alors configurons-en un avec Discord.

Créez ou sélectionnez un canal de texte sur votre serveur Discord. Cliquez sur le bouton `Modifier le canal`.

![modifier le canal](https://cdn.hashnode.com/res/hashnode/image/upload/v1735206358936/d94926f1-381a-451b-95f8-ddb7747dba70.png align="center")

Ensuite, dans le menu de navigation de gauche, sélectionnez l'option `Intégration`. Vous devriez voir l'option `Webhooks` listée là.

![Intégration des Webhooks](https://cdn.hashnode.com/res/hashnode/image/upload/v1735206416398/eedf690f-1f75-48f2-8da7-ef1e9c9558da.png align="center")

Cliquez sur l'option `Webhooks` puis cliquez sur le bouton `Nouveau Webhook`.

![Nouveau Webhook](https://cdn.hashnode.com/res/hashnode/image/upload/v1735206460104/540097f7-8e1e-41db-b2d6-d2ef1f14055b.png align="center")

Donnez un nom à votre webhook, et vous pouvez optionnellement télécharger une photo. Cela peut être utile lorsque vous avez plusieurs webhooks et que vous souhaitez les identifier rapidement par leur photo et leur nom.

Maintenant, cliquez sur le bouton `Copier l'URL du Webhook` pour copier l'URL du webhook. Gardez-la en sécurité quelque part, car nous allons l'utiliser bientôt dans notre application.

![Modifier le Webhook](https://cdn.hashnode.com/res/hashnode/image/upload/v1735206520757/0718e9e0-b16b-4156-a1bd-40ce28ed2ff4.png align="center")

C'est tout. Maintenant, créons une application Next.js 15 pour que nous puissions intégrer le webhook avec elle.

## Comment créer un projet Next.js

Ouvrez le terminal et utilisez la commande suivante pour créer une application Next.js :

```bash
npx create-next-app@latest
```

Vous devrez fournir quelques entrées pour le projet initial afin de le créer. J'utiliserai JavaScript (par opposition à TypeScript), Tailwind CSS, App Router, et Turbopack pour ce projet. J'ai donc opté pour ces choix en fournissant `Yes` comme réponse.

![Création du projet Nexy.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1736133367746/03ebe408-3d6f-44ac-9629-5d08a4f30eab.png align="center")

Avec cela, vous avez créé un projet Next.js que vous pouvez utiliser pour le reste du tutoriel.

## Comment définir les variables d'environnement

Créez un fichier `.env` à la racine de votre projet. Nous allons maintenant créer une variable d'environnement secrète avec l'URL du webhook que vous avez copiée précédemment. Créez une entrée dans le fichier .env comme ceci :

```bash
DISCORD_WEBHOOK_URL=<VOTRE_URL_DE_WEBHOOK_DISCORD>
```

Assurez-vous de remplacer `<VOTRE_URL_DE_WEBHOOK_DISCORD>` par votre URL de webhook réelle dans le fichier `.env`. N'oubliez pas que vous ne devez pas commiter et pousser ce fichier vers votre contrôle de version. Assurez-vous donc que le fichier `.env` a été ajouté au fichier `.gitignore` du projet.

![.gitignore](https://cdn.hashnode.com/res/hashnode/image/upload/v1736912358788/d98af5b1-ab61-46c3-92d5-a8772d34e4f2.png align="center")

## Comment intégrer le Webhook avec le composant `Form` de Next.js

Maintenant, nous allons créer l'interface utilisateur pour capturer les entrées de l'utilisateur et envoyer celles-ci au canal de texte Discord en utilisant le webhook.

Créons un simple formulaire de message en utilisant le composant `<Form />` de Next.js. Le composant `<Form/>` est une extension du formulaire natif HTML avec plus de flexibilités et de fonctionnalités introduites par la sortie de Next.js 15. Je vous suggère de [parcourir ce tutoriel vidéo basé sur un projet](https://www.youtube.com/watch?v=vl_aGFMShg0) si vous êtes intéressé à en apprendre davantage sur cette nouvelle addition à Next.js.

Notre stratégie ici est très simple :

* Nous allons créer un formulaire et ajouter une action à celui-ci en utilisant la propriété `action` du formulaire.

* Nous allons ensuite créer une [Action Serveur](https://www.youtube.com/watch?v=gQ2bVQPFS4U) en utilisant l'URL du webhook pour communiquer avec Discord.

* L'action sera invoquée lorsque l'utilisateur remplira le formulaire et le soumettra. Ainsi, la communication du webhook sera effectuée.

Écrivons le code pour ces fonctionnalités maintenant.

### Créer le Formulaire

Créez un dossier appelé `_components` sous le répertoire `app/`. Maintenant, créez un fichier `message-form.jsx` sous le dossier `app/_components/` avec le code suivant :

```javascript
import Form from "next/form";
import { sendDiscordMessage } from "../actions";

const MessageForm = () => {
  return (
    <Form className="flex flex-col items-center" action={sendDiscordMessage}>
      <input
        type="text"
        placeholder="Votre nom"
        name="username"
        className="border p-1 rounded w-[300px] my-2"
        required
      />

      <input
        type="email"
        placeholder="Votre e-mail"
        name="email"
        className="border p-1 rounded w-[300px] my-2"
        required
      />

      <input
        type="text"
        placeholder="Votre URL d'image"
        name="dp"
        className="border p-1 rounded w-[300px] my-2"
      />

      <select
        name="type"
        className="p-1 rounded border my-2 w-[300px]"
        required
      >
        <option value="">Type de message</option>
        <option value="thanks">Dire, Merci !</option>
        <option value="qa">QA</option>
        <option value="general">Général</option>
      </select>

      <textarea
        placeholder="Que voulez-vous dire ?"
        name="message"
        className="border p-1 rounded w-[300px] my-2"
        required
      />

      <button
        type="submit"
        className="bg-blue-500 w-[70px] text-white rounded-md"
      >
        Envoyer
      </button>
    </Form>
  );
};

export default MessageForm;
```

Ici, nous avons créé un formulaire de base avec cinq champs pour que les utilisateurs saisissent leur nom, email, URL de l'image de profil, type de message (général, merci, qa) et le message. Il y a également un bouton d'envoi pour soumettre le formulaire.

![Le simple formulaire que nous avons créé](https://cdn.hashnode.com/res/hashnode/image/upload/v1735271967544/3313c084-1526-435b-9288-bfa93cdbcb05.png align="center")

Nous avons utilisé le composant `Form` du package `next/form`. Le composant `Form` nous permet d'exécuter une fonction sur le serveur (action serveur) à l'aide de son attribut `action`. Comme vous pouvez le voir dans le code ci-dessus, nous avons importé une action serveur `sendDiscordMessage` et utilisé celle-ci comme valeur pour l'attribut `action` du formulaire.

```xml
 <Form className="flex flex-col items-center" action={sendDiscordMessage}>
```

Maintenant, créons l'action serveur afin que nous puissions soumettre le formulaire avec celle-ci.

### Créer l'Action Serveur

Nous allons utiliser une action serveur pour envoyer des messages à Discord en utilisant des webhooks. Créez un dossier appelé `actions` sous le répertoire `app/`. C'est une convention de garder toutes les actions colocées sous le répertoire `actions/`. Maintenant, créez un fichier appelé `index.js` sous le répertoire `app/actions/` avec le code suivant :

```javascript
"use server";

export const sendDiscordMessage = async (formData) => {
  try {
    const rawFormEntries = Object.fromEntries(formData);

    console.log(rawFormEntries);

    await fetch(process.env.DISCORD_WEBHOOK_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: rawFormEntries?.username,
        avatar_url: rawFormEntries?.dp || "https://i.imgur.com/mDKlggm.png",
        content: rawFormEntries?.message,
        embeds: [
          {
            fields: [
              {
                name: "Email",
                value: rawFormEntries?.email,
                inline: true,
              },
              {
                name: "Type de message",
                value: rawFormEntries?.type,
                inline: true,
              },
            ],
          },
        ],
      }),
    })
  } catch (err) {
    console.log(err.message);
  }
};
```

Comprenons ce qui se passe dans le code ci-dessus :

* Dans Next.js (ou avec React 19), une fonction serveur (alias action serveur) nécessite une directive spéciale appelée `"use server"` en haut du fichier. Nous l'avons donc déclarée.

* Une action serveur est une fonction asynchrone qui obtient `formData` comme paramètre. Le `formData` contiendra les valeurs de tous les champs de formulaire soumis par l'utilisateur. Nous pouvons utiliser l'API `Object.formEntries()` pour obtenir une paire clé-valeur à partir du `formData`. [Vérifiez ceci](https://www.youtube.com/shorts/gNIO_6FcRrE) pour apprendre la meilleure façon de gérer formData en JavaScript.

* Ensuite, nous avons utilisé l'URL du webhook Discord pour effectuer un appel `POST` avec la charge utile requise pour créer le message.

* Comprenons bien le format de la charge utile. Nous devons suivre une structure de charge utile spécifique pour que le webhook Discord crée le message. Il suit un schéma pour avoir ce qui suit :

* `username` : le nom de l'expéditeur du message. Il apparaît en haut du message. Nous lisons le champ nom des données soumises et remplissons le champ `username`.

* `avatar_url` : la photo de profil de l'expéditeur du message. Nous avons un champ `dp` dans le formulaire pour capturer l'URL de la photo de profil. Nous l'utilisons, et au cas où l'utilisateur ne la fournit pas, nous utilisons une image par défaut comme photo de profil.

* `content` : Le champ `content` est le contenu réel du message. Nous lisons la valeur du champ `message` et remplissons la valeur.

* `embeds` : Dans le message Discord, vous pouvez utiliser des embeds. Ces embeds peuvent être des messages texte, des images ou des vidéos. Nous allons utiliser les embeds pour afficher les informations sur l'email et le type de message. Les `embeds` sont un tableau de champs. Dans chacun des champs, nous avons passé les valeurs `email` et `type` de message comme valeurs `inline`. Les valeurs inline apparaîtront en ligne, côte à côte.

## Comment mettre à jour la page de l'application

Enfin, mettons à jour la page de l'application avec notre composant de formulaire afin que tout soit assemblé. Ouvrez le fichier `page.js` sous le répertoire `app/` et collez le code suivant :

```javascript
import MessageForm from "./_components/message-form";

export default function Home() {
    return (
        <div className="flex flex-col justify-center items-center">
          <h1 className="text-3xl my-3">Envoyer un message à tapaScript</h1>
          <MessageForm />
        </div>
      ) 
}
```

Ici, nous avons intégré le formulaire avec la page de l'application afin que nous puissions y accéder sur le navigateur.

## Testons cela

Maintenant, vous pouvez exécuter l'application avec la commande `yarn dev` depuis votre terminal. L'application sera disponible sur `localhost:3000` par défaut. Ouvrez un onglet de navigateur et accédez à l'URL `http://localhost:3000`. Vous devriez voir un formulaire comme celui ci-dessous. Remplissez-le avec des valeurs et cliquez sur le bouton `Envoyer`.

![formulaire](https://cdn.hashnode.com/res/hashnode/image/upload/v1735272054425/12e3894b-534a-436b-8e18-e076799e5a4f.png align="center")

Allez dans le canal de texte de votre serveur Discord et vérifiez si un message apparaît. Vérifiez que les champs du message correspondent aux valeurs d'entrée que vous avez fournies dans le formulaire.

![sortie](https://cdn.hashnode.com/res/hashnode/image/upload/v1735272074694/b795bf9f-adfd-4ff8-aed5-5fe07c49e47b.png align="center")

TADA ! Nous l'avons fait. Mais attendez, nous pouvons encore l'améliorer. Avez-vous remarqué que nous n'affichons aucun type de retour indiquant que le "Message a été envoyé avec succès", ou "Il y a des problèmes pour envoyer le message" ? Nous ne prenons pas soin de fournir le résultat de l'action serveur au composant de formulaire. Corrigons cela.

## Comment améliorer le retour de message en utilisant le hook useActionState de React 19

`React 19` a introduit un hook appelé [useActionState](https://www.youtube.com/watch?v=PWFKgdGmhxg) qui vous aide à mettre à jour l'état en fonction du résultat d'une action serveur. Utilisons ce hook pour améliorer le formulaire de message et l'action serveur afin que, lorsque l'action est exécutée avec succès (ou échoue), nous puissions notifier le composant de formulaire pour changer son état et afficher les messages de succès/erreur en conséquence.

### Configurer un toaster

Nous allons utiliser un message toast pour afficher les messages de succès/erreur. Utilisons la bibliothèque de toast appelée `sonner`. D'abord, installez-la avec cette commande :

```bash
yarn add sonner
```

Maintenant, nous devons ajouter le `Toaster` de `sonner` à notre application. Le meilleur endroit pour l'ajouter est au niveau racine du Layout de l'application. Ouvrez le fichier `layout.js` et importez le `Toaster` :

```javascript
import { Toaster } from 'sonner';
```

Ensuite, utilisez le `Toaster` dans le JSX du layout :

```xml
 <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
        <Toaster richColors />
      </body>
 </html>
```

C'est tout. La configuration du toaster est terminée. Maintenant, nous pourrons l'utiliser dans nos composants pour afficher les messages toast.

### Améliorer le Formulaire avec le hook `useActionState`

Tout d'abord, importez les hooks `useActionState` et `useEffect` dans le fichier `message-form.jsx`. Importez également le `toast` de `sonner`. Comme nous allons utiliser les hooks maintenant, nous devons faire du composant `message-form` un composant client. Ajoutez donc la directive `"use client"` en haut du fichier.

```javascript
"use client";

import Form from "next/form";
import { useActionState } from "react";
import { sendDiscordMessage } from "../actions";
import { useEffect } from "react"
import { toast } from "sonner";
```

Ensuite, utilisez le hook `useActionState` pour obtenir le `formState` mis à jour à partir du résultat de l'action serveur. Un état `isPending` nous indique si la soumission du formulaire a été complétée. Le `useActionState` retourne une nouvelle `formAction` à partir de l'instance d'action serveur existante.

La syntaxe est la suivante :

```javascript
const [formState, formAction, isPending] = useActionState(sendDiscordMessage,null);
```

Maintenant, nous devons utiliser cette `formAction` comme valeur de l'attribut `action` du composant `<Form />` :

```xml
<Form className="flex flex-col items-center" action={formAction}>
```

Ensuite, utilisez le hook `useEffect` pour suivre les changements de `formState` et afficher le message toast en conséquence. La forme du `formState` peut être personnalisée en fonction de nos besoins. Nous verrons bientôt comment l'action serveur peut retourner cette valeur d'état.

```javascript
  useEffect (() => {
    if (formState?.success) {
      toast.success(formState?.message);
    } else if (formState?.success === false) {
      toast.error(formState?.message);
    }
  },[formState?.success])
```

La dernière chose ici est d'améliorer l'UX du formulaire en utilisant l'état `isPending` que nous avons obtenu du hook `useActionState`. La valeur de l'état `isPending` sera vraie si le formulaire est encore en transition et en cours de soumission. Elle sera changée en false lorsque le formulaire sera soumis. Nous pouvons donc utiliser la valeur de l'état pour personnaliser le texte du bouton de soumission.

```xml
<button
  type="submit"
  className="bg-blue-500 w-[70px] text-white rounded-md">
    {isPending ? "Envoi..." : "Envoyer"}
</button>
```

Ce sont toutes les modifications que nous devons apporter au composant de formulaire. Voici le code complet du composant de formulaire modifié pour que vous puissiez le consulter et l'utiliser :

```javascript
"use client";

import Form from "next/form";
import { useActionState } from "react";
import { sendDiscordMessage } from "../actions";
import { useEffect } from "react"
import { toast } from "sonner";

const MessageForm = () => {
  const [formState, formAction, isPending] = useActionState(
    sendDiscordMessage,
    null
  );

  useEffect (() => {
    if (formState?.success) {
      toast.success(formState?.message);
    } else if (formState?.success === false) {
      toast.error(formState?.message);
    }
  },[formState?.success])

  

  return (
    <Form className="flex flex-col items-center" action={formAction}>
      <input
        type="text"
        placeholder="Votre nom"
        name="username"
        className="border p-1 rounded w-[300px] my-2"
        required
      />

      <input
        type="email"
        placeholder="Votre e-mail"
        name="email"
        className="border p-1 rounded w-[300px] my-2"
        required
      />

      <input
        type="text"
        placeholder="Votre URL d'image"
        name="dp"
        className="border p-1 rounded w-[300px] my-2"
      />

      <select
        name="type"
        className="p-1 rounded border my-2 w-[300px]"
        required
      >
        <option value="">Type de message</option>
        <option value="thanks">Dire, Merci !</option>
        <option value="qa">QA</option>
        <option value="general">Général</option>
      </select>

      <textarea
        placeholder="Que voulez-vous dire ?"
        name="message"
        className="border p-1 rounded w-[300px] my-2"
        required
      />

      <button
        type="submit"
        className="bg-blue-500 w-[70px] text-white rounded-md"
      >
        {isPending ? "Envoi..." : "Envoyer"}
      </button>
    </Form>
  );
};

export default MessageForm;
```

### Comment mettre à jour l'Action Serveur pour retourner des résultats

Les modifications dans l'action serveur doivent être les suivantes :

1. Lorsque vous utilisez le hook `useActionState`, passez une `formAction` retournée au formulaire. Nous avons vu cela avant. Cela aide de plusieurs manières, et l'une d'elles est d'obtenir la valeur d'état précédente du `formState` à l'intérieur de l'action serveur. Vous devez être attentif à la passer comme premier argument à la fonction serveur, puis le `formData`.

2. Nous pouvons maintenant retourner le résultat de l'action serveur afin que le `formState` soit mis à jour avec le résultat. Nous allons créer une structure de résultat avec un champ booléen `success` indiquant s'il s'agit d'un scénario de succès ou d'erreur et un champ `message` avec le message réel.

Voici le code modifié avec les deux mises à jour ci-dessus :

```javascript
"use server";

export const sendDiscordMessage = async (prevState, formData) => {
  try {
    const rawFormEntries = Object.fromEntries(formData);

    console.log(rawFormEntries);

    await fetch(process.env.DISCORD_WEBHOOK_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: rawFormEntries?.username,
        avatar_url: rawFormEntries?.dp || "https://i.imgur.com/mDKlggm.png",
        content: rawFormEntries?.message,
        embeds: [
          {
            fields: [
              {
                name: "Email",
                value: rawFormEntries?.email,
                inline: true,
              },
              {
                name: "Type de message",
                value: rawFormEntries?.type,
                inline: true,
              },
            ],
          },
        ],
      }),
    });

    return {
      success: true,
      message: `Votre message a été envoyé avec succès.`,
    };
  } catch (err) {
    console.log(err.message);
    return {
      success: false,
      message: `Problème lors de l'envoi du message ${err.message}`,
    };
  }
};
```

Comme vous devez l'avoir remarqué, le résultat retourné est le `formState` que nous avons utilisé à l'intérieur du composant `form` pour afficher les messages toast.

## Testons une fois de plus

Testons les choses avec toutes les modifications.

1. Tout d'abord, remplissez le formulaire avec les détails. Maintenant, nous utilisons une URL de photo de profil plutôt que de la laisser vide. Cliquez sur le bouton `Envoyer`.

![Formulaire mis à jour](https://cdn.hashnode.com/res/hashnode/image/upload/v1736922583168/b044cca3-bb45-48d2-83bc-ec9459d86206.png align="center")

2. Vous devriez voir que le texte du bouton change en `Envoi...` pendant que le formulaire est en cours de soumission.

![État d'envoi](https://cdn.hashnode.com/res/hashnode/image/upload/v1736922728585/afdbe8cc-fdc3-4be1-8676-ffed5160168a.png align="center")

3. Après la soumission, vous devriez obtenir le message de succès dans le toast. De plus, l'état du formulaire devrait être restauré à son état d'origine.

![Message de succès](https://cdn.hashnode.com/res/hashnode/image/upload/v1736922801497/518fa3ec-16d1-44a7-aa42-a647512379b5.png align="center")

4. Sur le canal de texte Discord, vous devriez voir le message publié avec succès.

![Message mis à jour](https://cdn.hashnode.com/res/hashnode/image/upload/v1736922367821/41cd6329-b6e5-45e7-8674-df7cff8e932d.png align="center")

C'est incroyable ! Nous avons maintenant rendu l'application beaucoup meilleure avec la gestion des messages et des erreurs.

## Code source et ressources

Tout le code source utilisé dans cet article se trouve dans le dépôt GitHub. Vous pouvez y jeter un coup d'œil, suivre le README pour le configurer et l'exécuter localement.

* [Le dépôt GitHub next-js-discord](https://github.com/tapascript/next-js-discord)

Voici les ressources que j'ai mentionnées dans l'article et que vous pourriez trouver utiles :

* [Composant Form de Next.js 15 - Tout ce que vous devez savoir](https://www.youtube.com/watch?v=vl_aGFMShg0)

* [Actions Serveur de Next.js || Apprendre les motifs et la construction de projets](https://www.youtube.com/watch?v=gQ2bVQPFS4U)

* [MAÎTRISER le hook useActionState de React 19 avec un projet et des cas d'utilisation](https://www.youtube.com/watch?v=PWFKgdGmhxg)

* [La documentation officielle de useActionState](https://react.dev/reference/react/useActionState)

De plus, vous pouvez vous connecter avec moi en :

* Vous abonnant à ma [Chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1). Si vous êtes prêt à apprendre `React` et son écosystème, comme `Next.js`, avec à la fois des concepts fondamentaux et des projets, j'ai une excellente nouvelle pour vous : vous pouvez [consulter cette playlist sur ma chaîne YouTube](https://www.youtube.com/watch?v=VSB2h7mVhPg&list=PLIJrr73KDmRwz_7QUvQ9Az82aDM9I8L_8) avec plus de 30 tutoriels vidéo et plus de 20 heures de contenu engageant jusqu'à présent, gratuitement. J'espère que vous les aimerez aussi.

* [Me suivant sur X (Twitter)](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils pour monter en compétences.

* En consultant et en suivant mon travail Open Source sur [GitHub](https://github.com/atapas).

* Je publie régulièrement des articles significatifs sur mon [Blog GreenRoots](https://blog.greenroots.info/), vous pourriez les trouver utiles également.

À bientôt avec mon prochain article. En attendant, prenez soin de vous et continuez à apprendre.
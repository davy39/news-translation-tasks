---
title: Comment authentifier les utilisateurs dans Next.js avec NextAuth – App Router
  VS Pages Router
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-03T19:32:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-authenticate-users-with-nextauth-in-nextjs-app-and-pages-router
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-isaque-pereira-394377--1-.jpg
tags:
- name: authentication
  slug: authentication
- name: Next.js
  slug: nextjs
seo_title: Comment authentifier les utilisateurs dans Next.js avec NextAuth – App
  Router VS Pages Router
seo_desc: 'By Njoku Samson Ebere

  Authentication is a key security feature of any application. But it can be complex
  to implement properly.

  This tutorial will show you an easy and secure way to handle authentication in your
  apps. It involves allowing trusted org...'
---

Par Njoku Samson Ebere

L'authentification est une fonctionnalité de sécurité clé de toute application. Mais elle peut être complexe à mettre en œuvre correctement.

Ce tutoriel vous montrera une méthode facile et sécurisée pour gérer l'authentification dans vos applications. Il s'agit de permettre à des organisations de confiance (comme Google, Facebook, Github, etc.) d'authentifier vos utilisateurs pendant que vous vous concentrez sur la création de fonctionnalités importantes dans votre application.

Vous apprendrez comment faire cela en utilisant [Nextjs](https://nextjs.org/) et [NextAuth](https://next-auth.js.org/) étape par étape.

Vous devriez trouver cet article utile si vous êtes nouveau dans NextAuth. Mais si vous savez déjà comment configurer l'authentification avec le routeur de pages Nextjs et que vous essayez toujours de passer au routeur d'applications Nextjs, alors ce tutoriel est aussi pour vous.

[Voici une vidéo que j'ai faite](https://www.youtube.com/embed/pEAthPOxZd0) que vous pouvez utiliser pour compléter ce que vous apprenez ici.

## Prérequis

Vous devez connaître les bases de Next.js et Prisma pour bénéficier de ce tutoriel. 

Vous pouvez vous mettre à jour avec la documentation officielle de [Nextjs](https://nextjs.org/) et [Prisma](https://www.prisma.io/).

## Qu'est-ce que NextAuth ?

[NextAuth](https://next-auth.js.org/) est une solution d'authentification open-source pour les applications [Nextjs](https://nextjs.org/). Elle est progressivement développée pour fournir des solutions pour chaque framework ou bibliothèque sur le web. Vous pouvez trouver plus de détails sur le site [Authjs](https://authjs.dev/).

Vous pouvez considérer NextAuth comme un intermédiaire entre votre application et des systèmes d'authentification établis. Ainsi, au lieu de réinventer la roue, vous pouvez ajouter cette solution à la vôtre et continuer à construire votre application.

Le côté cool de cet outil est que vous n'avez pas à payer pour l'utiliser. Il suffit de faire attention. :)

## Comment configurer le projet

NexthAuth vous donne accès à de nombreuses organisations appelées [fournisseurs](https://next-auth.js.org/providers/). Ces organisations fournissent certaines informations d'identification pour que vous puissiez utiliser leur système d'authentification.

Ce tutoriel couvrira trois d'entre eux : Google, GitHub et Email. 

Vous devrez donc accéder aux informations d'identification pour chacun de ces fournisseurs et démarrer un modèle de base pour Nextjs.

### Comment obtenir les informations d'identification de Google

Vous pouvez suivre les étapes ci-dessous pour obtenir votre `Client ID` et `Client Secret` de Google.

Connectez-vous à [Google Console](https://console.cloud.google.com/) :

![Accueil de Google Console](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687211827437_Screenshot+2023-06-19+at+22.55.52.png)

Cliquez sur l'icône du menu en haut à gauche. Sélectionnez `API & Services` puis choisissez `Identifiants`.

![Menu déroulant API & Services et Identifiants](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687212097541_Screenshot+2023-06-19+at+22.57.35.png)

L'écran suivant apparaît. Cliquez sur `Créer un projet` :

![Page des identifiants](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687212437467_Screenshot+2023-06-19+at+23.03.12.png)

La page suivante est le formulaire ci-dessous :

![Formulaire Nouveau Projet](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687212907725_Screenshot+2023-06-19+at+23.08.08.png)

Entrez le nom de votre application et cliquez sur `Créer`. Vous serez redirigé vers la page `Identifiants` :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687213197204_Screenshot+2023-06-19+at+23.19.35.png)

Cliquez sur le bouton `Créer des identifiants` et sélectionnez l'option `ID client OAuth` :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687213453758_Screenshot+2023-06-19+at+23.20.37.png)

Vous devez configurer votre écran de consentement pour créer un `ID client OAuth`. Cliquez sur le bouton `Configurer l'écran de consentement` pour le faire :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687213975354_Screenshot+2023-06-19+at+23.24.45.png)


Définissez le `Type d'utilisateur` sur `externe` et cliquez sur `Créer` :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687214119338_Screenshot+2023-06-19+at+23.33.51.png)


Ensuite, entrez un nom, un email de support et un email de contact :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687214349378_Screenshot+2023-06-19+at+23.37.02.png)


Faites défiler jusqu'en bas de la page et cliquez sur `Enregistrer et continuer`. 

La page des Portées apparaît maintenant. Cliquez sur `Enregistrer et continuer`. Ensuite, cliquez sur `Enregistrer et continuer` sur la page `Utilisateurs de test`. Vous serez dirigé vers la page `Résumé`. Passez en revue vos informations et cliquez sur `Retour au tableau de bord`.

Essayez maintenant de créer un ID client OAuth, et vous devriez arriver à la page suivante :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687214911510_Screenshot+2023-06-19+at+23.47.13.png)

Sélectionnez l'option `Application Web` car c'est ce qui convient à ce tutoriel

Entrez un nom pour l'application :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687215239689_Screenshot+2023-06-19+at+23.52.03.png)

Ajoutez un URI aux `Origines JavaScript autorisées`. Utilisez `http://localhost:3000`. C'est la page d'accueil de votre application. Vous ajouterez plus d'URIs lorsque vous passerez en production.

Ajoutez `http://localhost:3000/api/auth/callback/google` comme l'un des `URIs de redirection autorisés`. C'est là que les utilisateurs seront dirigés pour compléter leur connexion avec Google.

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687215921609_Screenshot+2023-06-20+at+00.03.25.png)

Cliquez sur `Créer`, et cela produira le `Client ID` et le `Client Secret` comme dans l'image ci-dessous :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687216263525_Screenshot+2023-06-20+at+00.07.31.png)

Copiez-les ou téléchargez le fichier JSON. Vous en aurez besoin bientôt.

### Comment obtenir les informations d'identification de GitHub

Les instructions ci-dessous vous guideront pour obtenir votre `Client ID` et `Client Secret` de GitHub.

Connectez-vous à votre tableau de bord [Github](https://github.com/) et cliquez sur l'image de profil en haut à droite.

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687779963670_Screenshot+2023-06-26+at+12.42.49.png)

Sélectionnez `Paramètres` dans le menu déroulant :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687780111055_Screenshot+2023-06-26+at+12.45.10.png)

Dans la page qui suit, faites défiler vers le bas et sélectionnez `Paramètres du développeur` :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687780839002_Screenshot+2023-06-26+at+12.49.08.png)

Cliquez sur `OAuth Apps` sur la page suivante et choisissez `Register a New Application` :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687781085633_Screenshot+2023-06-26+at+13.01.09.png)

Remplissez le formulaire que vous voyez sur la page qui suit :

* Nom de l'application - `auth app`
* URL de la page d'accueil - `http://localhost:3000/`
* URL de rappel d'autorisation - `http://localhost:3000/api/auth`

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687795316847_Screenshot+2023-06-26+at+17.01.35.png)

Cliquez sur le bouton `Register Application`. Une nouvelle page apparaît avec le `GITHUB_ID` et le `GITHUB_SECRET` :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687796314704_Screenshot+2023-06-26+at+17.05.21.png)

Cliquez sur `Generate a new client secret` pour voir le `GITHUB_SECRET`.

### Comment obtenir les informations d'identification de l'email

Vous pouvez utiliser n'importe quel fournisseur d'email qui propose des services SMTP. Ce tutoriel utilisera Gmail. Vous pouvez consulter Mailgun, SendGrid, et d'autres.

Vous aurez besoin des détails suivants :

- EMAIL_SERVER_HOST
- EMAIL_SERVER_PORT
- EMAIL_SERVER_USER
- EMAIL_SERVER_PASSWORD
- EMAIL_FROM

Les étapes suivantes vous mèneront à votre `EMAIL_SERVER_PASSWORD` :

Connectez-vous à votre compte [Gmail](https://mail.google.com/mail/u/3/#inbox).
Cliquez sur votre image de profil. Un menu déroulant apparaîtra.

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687901339179_Screenshot+2023-06-27+at+22.01.43.png)

Cliquez sur le bouton `Gérer votre compte Google`. Vous serez redirigé vers la page suivante : 

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687900621088_Screenshot+2023-06-27+at+22.15.15.png)

Cliquez sur `Sécurité` dans le menu latéral. La page suivante apparaîtra.

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687900801137_Screenshot+2023-06-27+at+22.18.37.png)

Vous devrez configurer la vérification en deux étapes pour que ce processus fonctionne. Si vous l'avez déjà fait, cliquez dessus.

Il vous demandera votre mot de passe, après quoi vous serez redirigé vers la page suivante :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687901149393_Screenshot+2023-06-27+at+22.22.15.png)

Faites défiler jusqu'en bas et cliquez sur `Mots de passe d'application`, comme dans l'image ci-dessus.
La page qui s'affiche ressemblera à l'image ci-dessous :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687901526239_Screenshot+2023-06-27+at+22.29.52.png)


Sélectionnez une `Application` et un `appareil` dans les menus déroulants et cliquez sur le bouton `Générer` :


![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687901737092_Screenshot+2023-06-27+at+22.34.53.png)


Cela générera un texte de 16 chiffres comme ceci :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687902422543_Screenshot+2023-06-27+at+22.42.22.png)


Vos informations d'identification pour l'email seront les suivantes :

- EMAIL_SERVER_HOST="smtp.gmail.com"
- EMAIL_SERVER_PORT=465
- EMAIL_SERVER_USER="<votre_adresse_email>". Un exemple est "eberenjoku@gmail.com"
- EMAIL_SERVER_PASSWORD="<le_mot_de_passe_que_vous_venez_de_générer_sans_espaces>"
- EMAIL_FROM="<ladresse_email_que_vous_voulez_que_le_destinataire_voie_comme_expéditeur>". Cet email n'a pas besoin d'exister. 

### Comment démarrer un projet Next.js

Vous allez créer 2 modèles de base Next.js. L'un utilisera le `routeur de pages`, tandis que l'autre fonctionnera avec le `routeur d'applications`.

#### Routeur de pages

Exécutez la commande suivante pour créer un projet Next.js :

```cmd
    npx create-next-app@latest
```

Vous obtiendrez plusieurs invites. Vos réponses doivent être les suivantes :

```javascript
    What is your project named? page_router_tutorial
    Would you like to use TypeScript with this project? No
    Would you like to use ESLint with this project? No
    Would you like to use Tailwind CSS with this project? No
    Would you like to use `src/` directory with this project? No
    Use App Router (recommended)? No
    Would you like to customize the default import alias? No
```

Vous aurez maintenant un projet créé avec un répertoire `pages` comme ceci :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687907082697_Screenshot+2023-06-28+at+00.02.05.png)

#### Routeur d'applications

Exécutez la commande suivante pour créer un projet Next.js :

```cmd
    npx create-next-app@latest
```

Vous obtiendrez plusieurs invites. Vos réponses doivent être les suivantes :

```javascript
    What is your project named? app_router_tutorial
    Would you like to use TypeScript with this project? No
    Would you like to use ESLint with this project? No
    Would you like to use Tailwind CSS with this project? No
    Would you like to use `src/` directory with this project? No
    Use App Router (recommended)? Yes
    Would you like to customize the default import alias? No
```

Vous aurez maintenant un projet créé avec un répertoire `app` comme ceci :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687907117476_Screenshot+2023-06-28+at+00.02.00.png)


Tout est maintenant prêt. Vous allez maintenant commencer à créer l'application d'authentification.


## Comment configurer Prisma et NextAuth sur le routeur de pages et d'applications

Cette section se concentrera sur les processus qui n'ont pas changé avec la sortie de Next.js 13. Donc tout ce que vous ferez dans cette section sera appliqué aux projets `page_router_tutorial` et `app_router_tutorial`.

Vous ferez ce qui suit :

- Installer les dépendances
- Créer et migrer un modèle de base de données
- Ajouter les informations d'identification que vous avez obtenues dans la section précédente à un fichier

### Comment installer les dépendances

La commande ci-dessous installera tous les modules pour le projet :

```cmd
    npm i next-auth prisma nodemailer faunadb @next-auth/prisma-adapter
```

Elle ajoute les modules NextAuth, Prisma, Node Mailer, Fauna DB et Prisma Adapter au projet.

### Comment créer et migrer un modèle de base de données

Un modèle de base de données définit comment les tables de la base de données communiquent entre elles. Vous allez créer cela dans cette partie.

Commencez par exécuter la commande suivante :

```cmd
    npx prisma init
```

Elle crée un répertoire `Prisma` avec un fichier à l'intérieur appelé `schema.prisma` et un fichier `.env` dans le dossier racine du projet. Le fichier contiendra votre définition de modèle. 

Actuellement, le contenu du fichier ressemble à ceci :

```javascript
    // This is your Prisma schema file,
    // learn more about it in the docs: https://pris.ly/d/prisma-schema
    
    generator client {
      provider = "prisma-client-js"
    }
    
    datasource db {
      provider = "postgresql"
      url      = env("DATABASE_URL")
    }
```

Ce tutoriel utilisera la base de données Postgres comme indiqué dans le code ci-dessus. Le fichier `.env` contient l'`DATABASE_URL` que vous devez remplacer par le vôtre. N'oubliez pas de le faire pour éviter les bugs plus tard dans le projet.

Ajoutez le code ci-dessous au fichier `schema.prisma` :

```javascript
    model Account {
      id                 String  @id @default(cuid())
      userId             String
      type               String
      provider           String
      providerAccountId  String
      refresh_token      String? @db.Text
      access_token       String? @db.Text
      expires_at         Int?
      token_type         String?
      scope              String?
      id_token           String? @db.Text
      session_state      String?
      oauth_token_secret String?
      oauth_token        String?
    
      user User @relation(fields: [userId], references: [id], onDelete: Cascade)
    
      @@unique([provider, providerAccountId])
    }
    
    model Session {
      id           String   @id @default(cuid())
      sessionToken String   @unique
      userId       String
      expires      DateTime
      user         User     @relation(fields: [userId], references: [id], onDelete: Cascade)
    }
    
    model User {
      id            String    @id @default(cuid())
      name          String?
      email         String?   @unique
      emailVerified DateTime?
      image         String?
      accounts      Account[]
      sessions      Session[]
    }
    
    model VerificationToken {
      identifier String
      token      String   @unique
      expires    DateTime
    
      @@unique([identifier, token])
    }
```

Cela définit quatre (4) tables : `Account`, `User`, `Session` et `VerificationToken`. Le modèle montre qu'un `user` peut avoir plusieurs comptes, et chaque `account` peut être connecté à de nombreux endroits (`sessions`). La table `VerificationToken` est pour vérifier un utilisateur.

Il est maintenant temps de créer les tables dans la base de données. Exécutez la commande ci-dessous pour que cela se produise :

```cmd
    npx prisma migrate dev
```

Vous pouvez ensuite vérifier votre tableau de bord de la base de données pour les nouvelles tables.

Vous pouvez gérer votre base de données à partir du navigateur en utilisant Prisma en exécutant la commande ci-dessous :

```cmd
    npx prisma studio
```

### Comment ajouter les informations d'identification au fichier .env

Le fichier .env contiendra tous les détails de vos fournisseurs et autres éléments. Voici les informations d'identification :

- EMAIL_SERVER_USER
- EMAIL_SERVER_PASSWORD
- EMAIL_SERVER_HOST
- EMAIL_SERVER_PORT
- EMAIL_FROM

- GITHUB_ID
- GITHUB_SECRET

- GOOGLE_CLIENT_ID
- GOOGLE_CLIENT_SECRET

Outre ceux que vous connaissez déjà, vous en avez besoin de deux autres :

- NEXTAUTH_SECRET
- NEXTAUTH_URL

`NEXTAUTH_SECRET` peut être n'importe quoi que vous choisissez. Cependant, vous voulez quelque chose de difficile à prédire. Exécutez la commande suivante pour obtenir une chaîne très aléatoire :

```cmd
    openssl rand -base64 32
```

Utilisez la sortie comme `NEXTAUTH_SECRET`.

`NEXTAUTH_URL` est l'URL de base de votre projet. Comme le projet est encore en développement, l'`NEXTAUTH_URL` est `http://localhost:3000`.

Voici à quoi votre fichier `.env` devrait ressembler :

```javascript
DATABASE_URL="postgres://postgres:IcuI4cu.31904145.@db.tbwiajqcroukpykndvft.supabase.co:5432/postgres"
    
    EMAIL_SERVER_HOST="smtp.gmail.com"
    EMAIL_SERVER_PORT=465
    EMAIL_SERVER_USER="tsendgrid7@gmail.com"
    EMAIL_SERVER_PASSWORD="cnbpfzfrjnxvfgcv"
    EMAIL_FROM="no-reply@tsendgrid7.com"
    
    GOOGLE_CLIENT_ID="196506336558-lh9qhavsi224v00n7q6ggn1f6cur9epr.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET="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"
    
    GITHUB_ID="11a8144f2897384cfedf"
    GITHUB_SECRET="6599042d48110bbda9fcd1ec6ede61f4320adc9d"
    
    NEXTAUTH_SECRET="YegyDIZNJPqxOkGS4K0F/o9l3SjCxCUR4Q/45rGyOtA="
    NEXTAUTH_URL="http://localhost:3000"
``` 

Cela conclut ce qui est le même processus pour les deux projets. La section suivante se concentrera maintenant sur le répertoire `page_router_tutorial`.

## Comment créer une authentification avec le routeur de pages Next.js

Maintenant, je vais passer en revue ce que vous devez faire dans le dossier `page_router_tutorial`. Suivez les étapes ci-dessous :

Créez un dossier appelé `auth` dans le répertoire `pages/api/`. Créez un fichier dans le répertoire `pages/api/auth` et nommez-le `[...nextauth].js`.

Importez `PrismaAdapter`, `PrismaClient` et `NextAuth` :

```javascript
    import { PrismaAdapter } from '@next-auth/prisma-adapter';
    import { PrismaClient } from '@prisma/client';
    import NextAuth from "next-auth";
```

Importez également les fournisseurs comme ceci :

```javascript
    import EmailProvider from "next-auth/providers/email";
    import GitHubProvider from "next-auth/providers/github";
    import GoogleProvider from "next-auth/providers/google";
```

Instanciez le `PrismaClient` et exportez NextAuth par défaut. Utilisez le code ci-dessous :

```javascript
    const prisma = new PrismaClient();
    
    export default NextAuth();
```

Ce code créera automatiquement et gérera les routes API pour l'authentification.

Ensuite, exportez une fonction `NextAuth` et ajoutez l'adaptateur comme ceci :

```javascript
    export default NextAuth({
      providers: [...],
      adapter: PrismaAdapter(prisma),
    });
```

La clé `providers` est un tableau de fonctions, où chacune est le fournisseur que vous souhaitez ajouter à votre projet. Vous devez en ajouter trois, donc votre code devrait ressembler à ceci :

```javascript
    import { PrismaAdapter } from "@next-auth/prisma-adapter";
    import { PrismaClient } from "@prisma/client";
    
    const prisma = new PrismaClient();
    
    export default NextAuth({
      providers: [
        GitHubProvider({
          clientId: process.env.GITHUB_ID,
          clientSecret: process.env.GITHUB_SECRET,
        }),
        GoogleProvider({
          clientId: process.env.GOOGLE_CLIENT_ID,
          clientSecret: process.env.GOOGLE_CLIENT_SECRET,
        }),
        EmailProvider({
          server: {
            host: process.env.EMAIL_SERVER_HOST,
            port: process.env.EMAIL_SERVER_PORT,
            auth: {
              user: process.env.EMAIL_SERVER_USER,
              pass: process.env.EMAIL_SERVER_PASSWORD,
            },
          },
          from: process.env.EMAIL_FROM,
        }),
      ],
      adapter: PrismaAdapter(prisma),
    });
```

C'est tout ce dont vous avez besoin pour créer une application d'authentification en utilisant Next.js et NextAuth.

Démarrez le serveur local en exécutant la commande suivante :

```cmd
    npm run dev
```

Accédez à http://localhost:3000/api/auth/signin, et vous serez sur cette page :

![](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1687943428651_Screenshot+2023-06-28+at+10.04.56.png)


Voilà... Surprise ! Surprise ! Surprise !

Vous n'avez créé aucune interface utilisateur, alors d'où vient cette interface ?

C'est là la beauté de NextAuth. Il crée des points de terminaison et une interface utilisateur accompagnante pour chaque fournisseur. Vous n'avez pas à vous en soucier, mais vous pouvez utiliser votre propre interface.

### Comment tester l'authentification du routeur de pages

Les vidéos suivantes démontrent comment fonctionne l'application d'authentification que vous avez construite :

* [Fournisseur Google](https://www.youtube.com/embed/0HSFAH04px4)
* [Fournisseur GitHub](https://www.youtube.com/embed/OS0oQeXaNDw)
* [Fournisseur Email - Lien magique](https://www.youtube.com/embed/mP47WwRiCd0)
* [Déconnexion](https://youtu.be/MnTutPYO6NU)

NextAuth fournit également une fonctionnalité de déconnexion. Accédez à [http://localhost:3000/api/auth/signout](http://localhost:3000/api/auth/signout).

Cliquez sur le bouton `Signout` qui apparaît lorsque la page est chargée :

Dans cette section, vous avez appris comment construire une application d'authentification Next.js en utilisant le modèle de routage `pages`. Vous pouvez trouver le code pour cette section sur GitHub : [https://github.com/EBEREGIT/nextjs-nextauth-tut/tree/main/page_router_tutorial](https://github.com/EBEREGIT/nextjs-nextauth-tut/tree/main/page_router_tutorial).

Mais Next.js version 13 est sortie il y a quelque temps et s'est stabilisée. Elle vient avec le modèle de routage d'applications, et les développeurs Next.js sont invités à l'adopter puisque le routeur `pages` pourrait devenir obsolète bientôt.

Vous verrez comment configurer l'authentification Next.js en utilisant le modèle de routage `app` dans la section suivante.

## Comment implémenter l'authentification avec le routeur d'applications Next.js

Cette section montrera une méthode légèrement différente et peut-être plus facile pour implémenter l'authentification avec le routeur `app`.

Vous allez maintenant vous concentrer sur le dossier `app_router_tutorial`.

N'oubliez pas de configurer Prisma et NextAuth comme vous l'avez fait dans la section précédente pour le projet `page_router_tutorial`.

Maintenant, faites ce qui suit :

Créez un dossier `api` dans le répertoire `app`.

Créez un dossier appelé `auth` dans le répertoire `app/api/`.

Créez un dossier appelé `[...nextauth]` dans le répertoire `app/api/auth`

Créez un fichier dans le dossier `[...nextauth]` appelé `route.js`. Cela est conforme à la directive [Nextjs 13 Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/router-handlers).

Dans le fichier, importez `PrismaAdapter`, `PrismaClient`, `NextAuth` et les fournisseurs comme ceci :

```javascript
    import { PrismaAdapter } from '@next-auth/prisma-adapter';
    import { PrismaClient } from '@prisma/client';
    import NextAuth from "next-auth";
    
    import EmailProvider from "next-auth/providers/email";
    import GitHubProvider from "next-auth/providers/github";
    import GoogleProvider from "next-auth/providers/google";

```

Instanciez le `PrismaClient` :

```javascript
    const prisma = new PrismaClient();

```

Créez une fonction `handler` pour exécuter les configurations `NextAuth` avec le code ci-dessous :

```javascript
    const handler = NextAuth(...);

```

Passez les fournisseurs et l'adaptateur comme un argument dans la méthode `NextAuth`. Tapez le code suivant :

```javascript
    const handler = NextAuth({
      providers: [
        GitHubProvider({
          clientId: process.env.GITHUB_ID,
          clientSecret: process.env.GITHUB_SECRET,
        }),
        GoogleProvider({
          clientId: process.env.GOOGLE_CLIENT_ID,
          clientSecret: process.env.GOOGLE_CLIENT_SECRET,
        }),
        EmailProvider({
          server: {
            host: process.env.EMAIL_SERVER_HOST,
            port: process.env.EMAIL_SERVER_PORT,
            auth: {
              user: process.env.EMAIL_SERVER_USER,
              pass: process.env.EMAIL_SERVER_PASSWORD,
            },
          },
          from: process.env.EMAIL_FROM,
        }),
      ],
      adapter: PrismaAdapter(prisma),
    });

```

Enfin, exportez le gestionnaire avec la ligne de code suivante :

```javascript
    export { handler as GET, handler as POST };

```

C'est tout ce dont vous avez besoin pour que l'authentification fonctionne avec le routeur `app`.

Vous aurez la même interface que dans la section précédente si vous accédez à [http://localhost:3000/api/auth/signin](http://localhost:3000/api/auth/signin).

Le code pour cette section est sur GitHub : [https://github.com/EBEREGIT/nextjs-nextauth-tut/tree/main/app_router_tutorial](https://github.com/EBEREGIT/nextjs-nextauth-tut/tree/main/app_router_tutorial).

### Comment tester l'authentification du routeur d'applications

Le test de l'authentification du routeur `app` suit la même procédure que celle du routeur `page`.

## Conclusion

La mise en œuvre de l'authentification peut être difficile. Mais avec ces outils utiles, cela ne peut que s'améliorer. Ce tutoriel visait à enseigner comment implémenter l'authentification en utilisant NextAuth à la fois dans le routeur `pages` et `app` de Next.js.

Vous avez vu comment configurer Prisma et NextAuth dans n'importe quel projet Next.js. Vous avez également appris la différence entre les modèles de routage `pages` et `app` de Next.js et comment implémenter la logique d'authentification NextAuth.

Ce tutoriel n'a fait qu'effleurer la surface, mais il vous donne un angle pour commencer à construire des projets personnels. Veuillez consulter la documentation ci-dessous pour continuer à apprendre.

* [React](https://react.dev/)
* [Next](https://nextjs.org/)
* [faunadb](https://fauna.com/)
* [NextAuth](https://next-auth.js.org/)
* [Prisma](https://www.prisma.io/)
* [Postgres](https://www.postgresql.org/)

Tout le code de ce tutoriel est sur GitHub : [https://github.com/EBEREGIT/nextjs-nextauth-tut](https://github.com/EBEREGIT/nextjs-nextauth-tut). Veuillez laisser une étoile 😊.
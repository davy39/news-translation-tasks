---
title: Comment configurer l'authentification et les routes protégées dans Next.js
  13 avec next-auth.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-09T17:54:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-authentication-and-protected-route-in-next-js-13-with-next-auth-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/pexels-pixabay-277576.jpg
tags:
- name: Application Security
  slug: application-security
- name: authentication
  slug: authentication
- name: Next.js
  slug: nextjs
seo_title: Comment configurer l'authentification et les routes protégées dans Next.js
  13 avec next-auth.js
seo_desc: 'By Olasunkanmi Balogun

  This guide demonstrates the straightforward process of incorporating authentication
  into your Next.js app using the next-auth.js library. While the library provides
  numerous options (providers), this tutorial focuses on the imp...'
---

Par Olasunkanmi Balogun

Ce guide démontre le processus simple d'incorporation de l'authentification dans votre application `Next.js` en utilisant la bibliothèque [`next-auth.js`](https://next-auth.js.org/). Bien que la bibliothèque offre de nombreuses options (fournisseurs), ce tutoriel se concentre sur la mise en œuvre en utilisant le fournisseur Google.

Vous apprendrez également comment configurer facilement des routes protégées au sein de votre application, une tâche simplifiée par la bibliothèque `next-auth.js`.

Lorsque vous êtes prêt, commençons.

## Comment configurer la bibliothèque `next-auth.js`

Une fois que votre application `Next.js` est opérationnelle, nous sommes prêts à commencer.

Note rapide : Je vais faire référence au répertoire "app" de manière cohérente dans ce guide. Si ce terme vous est nouveau, prenez un moment pour consulter la documentation [`Next.js`](https://nextjs.org/) pour plus de clarté. Si vous utilisez le répertoire "pages", ne vous inquiétez pas, car la mise en œuvre est presque identique.

Installez la bibliothèque `next-auth.js` avec la commande suivante :

```npm
npm install next-auth
```

Après avoir terminé l'installation, créez un dossier `api` dans votre dossier racine de l'application, et à l'intérieur, créez un dossier `auth`. Enfin, créez un dossier `[...nextauth]` à l'intérieur du dossier `auth`.

À l'intérieur du dossier `[...nextauth]`, créez deux fichiers nommés `route.ts` et `options.ts`.

Votre structure de dossiers à ce stade devrait ressembler à ceci :

![Image de la structure de dossiers](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot--187-.png)

Ensuite, dans le fichier `options.ts`, insérez le code suivant :

```ts
import type { NextAuthOptions } from 'next-auth'
import GoogleProvider from "next-auth/providers/google";

export const options: NextAuthOptions = {
    providers: [
  GoogleProvider({
    clientId: process.env.GOOGLE_CLIENT_ID as string,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET as string,
  })
]
}
```

Nous avons importé le type `NextAuthOptions` pour garantir que la variable `options` est sécurisée en termes de type.

Pour utiliser le fournisseur Google, nous avons importé `GoogleProvider` depuis `next-auth` comme illustré ci-dessus.

La variable [`options`](https://next-auth.js.org/configuration/options#options) est l'endroit où nous intégrons le fournisseur que nous prévoyons d'utiliser depuis `next-auth.js`.

Remarquez que nous avons exporté la variable `options`, ce qui nous permet de l'utiliser dans toute l'application (bien que nous en ayons surtout besoin dans le fichier `route.ts`). Alors que nous approfondissons la mise en œuvre dans le fichier `route.ts`, nous explorerons comment elle est utilisée.

Pour utiliser efficacement le fournisseur Google, vous devez obtenir vos propriétés `clientId` et `clientSecret`. Soyez assuré, nous approfondirons cela sous peu. Tout d'abord, créez un fichier `.env` où vous attribuerez des valeurs aux deux propriétés.

Les fichiers `env` sont toujours à la racine de votre application :

![Emplacement du fichier env dans le projet](https://www.freecodecamp.org/news/content/images/2023/11/2-1.png)

Maintenant, nous verrons comment vous pouvez obtenir votre `clientId` et `clientSecret`.

En supposant que vous avez déjà un compte Google, suivez ces étapes simples :

1. Visitez [Google Cloud Platform](https://cloud.google.com), et cliquez sur le bouton de la console en haut à droite de la barre de navigation.
   
![Barre de navigation GCP](https://www.freecodecamp.org/news/content/images/2023/11/3.png)

2. Vous serez redirigé vers votre tableau de bord de la console. En haut à gauche, juste après le logo Google Cloud, cliquez sur le menu déroulant pour créer un nouveau projet :
   
![Illustration du menu déroulant](https://www.freecodecamp.org/news/content/images/2023/11/4.gif)

3. Donnez à votre projet le nom que vous préférez, puis cliquez sur le bouton "Créer". Le mien sera "Tutoriel Next-auth".

4. Vous retournerez à votre tableau de bord de la console, et le même menu déroulant devrait maintenant afficher le projet que vous venez de créer. Si ce n'est pas le cas, cliquez dessus et sélectionnez le projet.

5. En supposant que tout est en ordre, faites défiler vers le bas jusqu'à la section "Accès rapide" et choisissez la carte "API & Services". Cette action vous mènera à la page "API & Services". Dans la barre latérale de cette page, sélectionnez l'option "Identifiants" :

![Option Identifiants](https://www.freecodecamp.org/news/content/images/2023/11/5.png)

6. Vous serez redirigé vers la page "Identifiants". Ici, cliquez sur le bouton "CONFIGURER L'ÉCRAN DE CONSENTEMENT" :
  
![Bouton de l'écran de consentement](https://www.freecodecamp.org/news/content/images/2023/11/6.png)

7. Cela vous mènera à la page de configuration de l'écran de consentement, où vous déterminerez comment vous souhaitez configurer et enregistrer votre application. Optez pour l'option "Externe" et poursuivez en cliquant sur le bouton "Créer" :

![Configuration de l'écran de consentement](https://www.freecodecamp.org/news/content/images/2023/11/7.png)
  
8. Après cela, vous vous trouverez sur la page "Écran de consentement OAuth". Poursuivez en complétant ces quatre étapes :

En commençant par l'onglet "Écran de consentement OAuth", vous serez invité à modifier les informations de votre application. Les sections clés sur lesquelles se concentrer sont "Informations sur l'application" et "Informations de contact du développeur". Après avoir rempli ces champs, cliquez sur le bouton "ENREGISTRER ET CONTINUER".

Vous passerez ensuite à l'onglet "Portées". Ici, cliquez à nouveau sur le bouton "ENREGISTRER ET CONTINUER".

Ensuite, vous avez l'onglet "Utilisateurs de test". De même, poursuivez en cliquant sur le bouton "ENREGISTRER ET CONTINUER".

Et enfin, vous atteindrez le dernier onglet, l'onglet de résumé. Faites défiler vers le bas et sélectionnez le bouton "RETOUR AU TABLEAU DE BORD".

Une fois ces étapes terminées, votre tableau de bord devrait ressembler à ce qui suit :

![Page du tableau de bord](https://www.freecodecamp.org/news/content/images/2023/11/8.png)
   
9. Retournez à la page "Identifiants", et là, cliquez sur le bouton "Créer des identifiants". Un menu déroulant apparaîtra. Choisissez l'option "ID client OAuth" :
   
![ID client OAuth](https://www.freecodecamp.org/news/content/images/2023/11/9-1.gif)

10. Cette action vous mènera à la page où vous créerez votre `client ID`. Sur cette page, vous verrez un seul champ déroulant pour le type de votre application, qui révèlera des champs supplémentaires en fonction de votre sélection. Sélectionnez l'option "Application Web" dans ce menu déroulant :
    
![Application Web](https://www.freecodecamp.org/news/content/images/2023/11/10.gif)
   
Faites défiler vers le bas jusqu'à la section "URI de redirection autorisés" et collez l'URI suivant : http://localhost:3000/api/auth/callback/google. Ensuite, cliquez sur le bouton "CRÉER".

11. Enfin, une fenêtre modale apparaîtra, affichant votre `Client ID` et `Client Secret` uniques. Gardez à l'esprit que les deux valeurs sont confidentielles, spécifiques à chaque utilisateur, et doivent être gardées sécurisées. Pour des raisons de confidentialité, les deux valeurs sont floutées dans l'image ci-dessous :

![Client ID et Client Secret](https://www.freecodecamp.org/news/content/images/2023/11/11.png)
    
Une fois que vous avez terminé ces étapes, retournez à votre éditeur de code et collez les valeurs appropriées de chaque variable dans le fichier `.env` :

```env
GOOGLE_CLIENT_ID = valeur de l'ID client
GOOGLE_CLIENT_SECRET = valeur du secret client
```

Vous devrez également générer une clé `NEXT_AUTH_SECRET` pour renforcer la sécurité du processus d'authentification dans `next-auth.js`. Générez votre clé secrète en exécutant la commande suivante dans votre terminal :

```
openssl rand -base64 32
```

Cette commande générera une chaîne de 32 caractères. Copiez cette chaîne et collez-la comme valeur pour la variable `NEXTAUTH_SECRET` dans votre fichier `.env`. Votre fichier `.env` final devrait ressembler à ceci :

```env
GOOGLE_CLIENT_ID = valeur de l'ID client
GOOGLE_CLIENT_SECRET = valeur du secret client
NEXT_AUTH_SECRET = secret next auth
```

Après avoir implémenté avec succès vos variables .env, collez le code suivant dans votre fichier route.ts :

```ts
import NextAuth from "next-auth/next";
import { options } from "./options";

const handler = NextAuth(options);

export { handler as GET, handler as POST };
```

Cela garantit que les requêtes GET et POST envoyées à ce point de terminaison (`api/auth/[...nextauth]`) seront traitées par la bibliothèque `next-auth`.

Pour conclure, redémarrez votre application. Il est important de noter que la bibliothèque `next-auth.js` ne sera pas activement engagée à ce stade. La raison en est que vous n'avez pas encore implémenté de routes protégées pour qu'elle protège vos pages. Nous explorerons cet aspect ensuite.

## Comment implémenter des routes protégées avec `next-auth.js`

Avec l'utilisation du [middleware](https://nextjs.org/docs/pages/building-your-application/routing/middleware) de `Next.js`, protéger les routes est très facile.

Commencez par créer un fichier `middleware.ts` dans le dossier racine `src`.

![Emplacement du fichier middleware.ts](https://www.freecodecamp.org/news/content/images/2023/11/12.png)

Pour protéger toutes vos pages de manière uniforme, insérez le code suivant :

```ts!
export { default } from 'next-auth/middleware'
```

Alternativement, vous pouvez sécuriser de manière sélective des pages spécifiques en utilisant un `matcher`. Par exemple, protéger uniquement la page d'accueil et la page à propos serait implémenté comme suit :

```ts
export { default } from 'next-auth/middleware'

export const config = { matcher: ['/', '/about'] }
```

Maintenant, lorsque vous visitez les deux pages sur votre localhost, elles présenteront une invite d'authentification vous invitant à "Se connecter avec Google", au lieu d'afficher le contenu régulier :

![13](https://www.freecodecamp.org/news/content/images/2023/11/13.png)

## Conclusion

Dans ce tutoriel, nous avons couvert les étapes essentielles pour implémenter l'authentification et les routes protégées dans votre application `Next.js` en utilisant la bibliothèque `next-auth.js` avec le fournisseur Google.

En suivant ces étapes, vous avez posé une base solide pour intégrer l'authentification dans votre application Next.js, renforçant sa sécurité et améliorant l'expérience utilisateur.

Avec les connaissances acquises ici, vous pouvez maintenant développer en toute confiance des applications qui offrent un contrôle d'accès sécurisé et un contenu personnalisé basé sur l'authentification de l'utilisateur.

Il est également intéressant de noter que `next-auth.js` fournit plusieurs fournisseurs que vous pouvez employer pour implémenter l'authentification, pas seulement le fournisseur Google.
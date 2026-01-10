---
title: Comment convertir votre site web en une application Android à l'aide de Bubblewrap
subtitle: ''
author: Sanjay
co_authors: []
series: null
date: '2025-08-19T17:52:20.227Z'
originalURL: https://freecodecamp.org/news/how-to-convert-your-website-into-an-android-app-using-bubblewrap
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755625913612/bfffd5f9-f4d6-4f8d-aae8-72f5730bd7e9.png
tags:
- name: Android
  slug: android
- name: PWA
  slug: pwa
- name: Web Development
  slug: web-development
seo_title: Comment convertir votre site web en une application Android à l'aide de
  Bubblewrap
seo_desc: If you are a web developer who doesn’t know about App Development (like
  me!), then this article is for you. I’ll teach you how to turn your website into
  a native app, without new frameworks or languages. You’ll learn how to convert a
  website to a PWA...
---

Si vous êtes un développeur web qui n'y connaît rien en développement d'applications (comme moi !), alors cet article est pour vous. Je vais vous apprendre à transformer votre site web en une application native, sans nouveaux Frameworks ni langages. Vous apprendrez comment convertir un site web en une PWA (Progressive Web App) que vous pourrez publier sur le Play Store.

Tout d'abord, nous allons transformer votre site web en une Progressive Web App (PWA). Ensuite, nous utiliserons un outil gratuit en ligne de commande de Google appelé **Bubblewrap** pour packager cette PWA dans une application Android. Commençons.

## Prérequis

Si vous suivez ce tutoriel, voici quelques prérequis :

* Connaissances de base en développement web.
    
* Votre site doit être accessible au public et vous devez avoir accès à son code source.
    
* Nous utiliserons npm pour installer les outils nécessaires, assurez-vous donc d'avoir Node.js installé.
    

**Note :** Ce tutoriel est basé sur un projet **Vite**, mais les étapes finales avec Bubblewrap sont les mêmes pour n'importe quel Framework web.

## Table des matières

1. [Qu'est-ce qu'une PWA ?](#heading-qu-est-ce-qu-une-pwa)
    
2. [Qu'est-ce que Bubblewrap ?](#heading-qu-est-ce-que-bubblewrap)
    
    * [Qu'est-ce qu'une TWA (Trusted Web Activity) ?](#heading-qu-est-ce-qu-une-twa-trusted-web-activity)
        
    * [Comment la TWA vérifie la confiance](#heading-comment-la-twa-verifie-la-confiance)
        
3. [Étape 1 – Configurer votre PWA dans Vite](#heading-etape-1-configurer-votre-pwa-dans-vite)
    
    * [Créer les icônes de votre application](#heading-creer-les-icones-de-votre-application)
        
    * [Installer le plugin Vite PWA](#heading-installer-le-plugin-vite-pwa)
        
    * [Configurer le plugin](#heading-configurer-le-plugin)
        
4. [Étape 2 – Créer l'application Android](#heading-etape-2-creer-l-application-android)
    
    * [Créer un dossier de build](#heading-creer-un-dossier-de-build)
        
    * [Installer le CLI Bubblewrap](#heading-installer-le-cli-bubblewrap)
        
    * [Initialiser le projet](#heading-initialiser-le-projet)
        
    * [Dépannage de la commande init](#heading-depannage-de-la-commande-init).
        
5. [Étape 3 – Répondre aux questions de Bubblewrap](#heading-etape-3-repondre-aux-questions-de-bubblewrap)
    
6. [Étape 4 – Générer l'application](#heading-etape-4-generer-l-application)
    
7. [Étape 5 – Configurer la validation TWA](#heading-etape-5-configurer-la-validation-twa)
    
    * [Qu'est-ce que le dossier .well-known ?](#heading-qu-est-ce-que-le-dossier-well-known)
        
    * [Qu'est-ce que delegate\_permission/common.handle\_all\_urls ?](#heading-qu-est-ce-que-delegatepermissioncommonhandleallurls)
        
8. [Étape 6 (Optionnel) – Personnaliser l'expérience In-App](#heading-etape-6-optionnel-personnaliser-l-experience-in-app)
    
9. [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'une PWA ?

PWA signifie **Progressive Web Application**, et son objectif est de faire en sorte que votre site web ressemble et se comporte exactement comme une application native. Si vous avez déjà visité un site web dans votre navigateur et vu une icône d'installation vous permettant de le télécharger sur votre téléphone ou votre ordinateur, vous avez utilisé une PWA.

Mais il ne s'agit pas seulement de l'apparence. Une PWA possède également des fonctionnalités d'application, comme le fonctionnement hors ligne, l'envoi de notifications push, et plus encore.

Il y a deux composants principaux dans une PWA :

* Le fichier manifest décrit votre application (nom, icônes, URL de démarrage, etc.).
    
* Un service worker est un fichier JavaScript en arrière-plan qui agit comme un proxy. La mise en cache et les notifications push sont gérées par ce fichier, qui s'exécute sur un thread différent du thread principal.
    

Sans ces deux composants, les navigateurs ne permettront pas aux utilisateurs de télécharger l'application localement.

Le fichier manifest et le service worker sont comme une liste de contrôle pour le navigateur. Lorsque vous visitez un site web, le navigateur recherche ces deux composants. S'ils sont présents et correctement configurés, le navigateur sait qu'il s'agit d'une véritable PWA et affichera l'icône "installer". Sans eux, le navigateur ne voit qu'un site web ordinaire.

## Qu'est-ce que Bubblewrap ?

Bubblewrap est un outil en ligne de commande (CLI) créé par Google qui prend votre PWA et la transforme en une application Android à l'aide d'une Trusted Web Activity (TWA).

Bubblewrap simplifie le processus de création d'une TWA, en transformant le fichier manifest d'une PWA en un package d'application Android (APK ou AAB).

### Qu'est-ce qu'une TWA (Trusted Web Activity) ?

Une Trusted Web Activity (TWA) est une fonctionnalité Android moderne qui vous permet d'afficher votre site web en plein écran à l'intérieur d'une application Android. Essentiellement, elle exécute le site sur le navigateur, mais elle n'affiche pas la barre d'adresse. Cela permet de donner l'impression d'une application native.

Pour débloquer cette fonctionnalité plein écran, votre application doit être "de confiance" (Trusted).

C'est là qu'intervient la "poignée de main secrète". Android doit être sûr que la personne qui a construit l'application et la personne qui possède le site web sont la même. Sans cette preuve de propriété, la TWA fonctionnera en mode dégradé et affichera la barre d'adresse en haut.

### Comment la TWA vérifie la confiance

Cette confiance est vérifiée à l'aide d'un système appelé **Digital Asset Links**. Vous placez un fichier spécial sur votre site web (nous le ferons dans la partie implémentation) qui contient l'empreinte numérique unique de votre application. Lorsqu'un utilisateur ouvre votre application, l'OS Android vérifie ce fichier. Si les empreintes correspondent, il accorde à votre application le statut "trusted", supprime la barre d'adresse et active d'autres fonctionnalités comme le deep linking.

Vous pouvez vérifier cette relation vous-même en utilisant l'outil de test officiel de Google : [Digital Asset Links Verifier.](https://developers.google.com/digital-asset-links/tools/generator)

Maintenant que vous comprenez le projet et les outils, commençons la construction.

## Étape 1 – Configurer votre PWA dans Vite

La première étape consiste à ajouter les deux composants principaux pour une PWA : le fichier manifest et le service worker.

Ce guide est basé sur un projet construit avec Vite, ce qui facilite le processus grâce à un plugin spécial. Si vous utilisez un autre outil, les concepts sont les mêmes, mais vous devrez chercher les étapes spécifiques à votre environnement.

### Créer les icônes de votre application

Avant de toucher au code, nous avons besoin d'icônes. Android nécessite des tailles spécifiques pour l'icône de lancement et l'écran de démarrage (splash screen).

Vous aurez besoin de deux tailles principales : `192x192` pixels et `512x512` pixels. Vous pouvez utiliser ce [Générateur de Favicon](https://realfavicongenerator.net/) pour générer votre logo. Téléchargez les fichiers générés et placez les fichiers `192x192` et `512x512` dans le dossier `public` de votre projet.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1755067586673/f7e06fc2-4b55-4ec3-af05-b2e78bf19273.png align="center")

### Installer le plugin Vite PWA

Ce plugin automatise la génération du `manifest.json` et du `service-worker.js` à chaque build.

```bash
npm install vite-plugin-pwa -D
```

### Configurer le plugin

Éditez le fichier `vite.config.ts` pour configurer le manifest de votre application.

Dans `vite.config.ts` :

```typescript
export default defineConfig({
  plugins: [
    VitePWA({
      registerType: "autoUpdate",   
      manifest: {
        name: "votre nom d'app",
        short_name: "nom court",
        description: "votre description",
        theme_color: "#0d1117",
        background_color: "#ffffff",
        display: "standalone",
        start_url: "/",
        icons: [
          {
            src: "/web-app-manifest-192x192.png",
            sizes: "192x192",
            type: "image/png",
          },
          {
            src: "/web-app-manifest-512x512.png",
            sizes: "512x512",
            type: "image/png",
          },
        ],
      },
    }),
  ]
```

Maintenant, quand vous lancez `npm run build`, le plugin générera les fichiers. Déployez ces changements : votre site est maintenant une PWA.

## Étape 2 – Créer l'application Android

Utilisons maintenant Bubblewrap pour packager cela.

### Créer un dossier de build

Créez un dossier dédié (par exemple `android`) à la racine de votre projet.

```plaintext
project/
├── client/
├── server/
└── android/
```

Naviguez dans ce dossier.

### Installer le CLI Bubblewrap

```bash
npm install -g @bubblewrap/cli
```

### Initialiser le projet

Lancez la commande `init`. Bubblewrap se connectera à votre site, lira le manifest et générera le projet Android.

```bash
bubblewrap init --manifest=https://votre-domaine.com/manifest.webmanifest
```

### Dépannage de la commande `init`

Bubblewrap a besoin du **Java Development Kit (JDK)** et du **Android SDK**.

#### Configuration du JDK :

```bash
? Do you want Bubblewrap to install the JDK (recommended)? (Y/n)
```

Si l'installation automatique échoue :
* Répondez **No**.
* Téléchargez le JDK 17 manuellement (ex: [Adoptium](https://adoptium.net/)).
* Configurez vos variables d'environnement (PATH).
* Fournissez le chemin à Bubblewrap (ex: `C:\java\jdk-17.0.16.8-hotspot`).

#### Configuration de l'Android SDK :

J'ai choisi **Yes** pour que Bubblewrap s'en occupe, et cela a fonctionné sans problème.

## Étape 3 – Répondre aux questions de Bubblewrap

Bubblewrap créera le fichier `twa-manifest.json` via un questionnaire :

```plaintext
Domain: Entrée (auto-rempli)
Application name: Nom complet
Application ID: (ex: chat.votreapp.twa)
Display mode: standalone
Orientation: portrait
Include support for Play Billing?: Y si achats in-app, sinon N
Request geolocation permission?: Y si besoin de localisation, sinon N
```

**Important :** Pour le keystore, les mots de passe doivent être identiques pour éviter des erreurs.

## Étape 4 – Générer l'application

```bash
bubblewrap build --universalApk
```

Le flag `--universalApk` génère à la fois le `.aab` (pour le Play Store) et le `.apk` (pour vos tests).

## Étape 5 – Configurer la validation TWA

Si vous testez l'APK maintenant, la barre d'adresse sera toujours visible car la "confiance" n'est pas établie.

Dans le dossier `public` de votre frontend, créez un dossier `.well-known` et un fichier `assetlinks.json`.

```bash
frontend/
├── public/
    ├── .well-known/
        └── assetlinks.json
```

### Qu'est-ce que le dossier `.well-known` ?

Il sert à stocker des configurations pour que des sources externes (comme Android) vérifient la validation de votre site.

Collez ceci dans `assetlinks.json` :

```json
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "chat.votreapp.twa",
      "sha256_cert_fingerprints": [
       "votre_empreinte_sha256"
      ]
    }
  }
]
```

### Qu'est-ce que `delegate_permission/common.handle_all_urls` ?

Cela permet aux liens du domaine de s'ouvrir directement dans l'application au lieu du navigateur (Deep Linking).

Pour obtenir l'empreinte `SHA256`, lancez :

```bash
keytool -list -v -keystore android.keystore -alias android
```

Copiez l'empreinte dans le fichier JSON et poussez les changements en production.

## Étape 6 (Optionnel) – Personnaliser l'expérience In-App

Vous pouvez afficher un contenu différent pour les utilisateurs de l'application. Dans `twa-manifest.json`, ajoutez ou modifiez :
`"startUrl": "/?twa=true"`.

Dans votre code frontend :

```typescript
const twaParam = queryParams.get("twa");

const [isTwa, setIsTwa] = useState<boolean>(() => {
   return localStorage.getItem("isTwa") === "true";
});

useEffect(() => {
  if (twaParam === "true") {
    localStorage.setItem("isTwa", "true");
    setIsTwa(true);
  }
}, [twaParam]);
```

Vous pouvez ensuite faire un rendu conditionnel selon la valeur de `isTwa`.

## Conclusion

Bubblewrap est réservé à Android. Pour du cross-platform, des outils comme Capacitor existent. Vous pouvez voir un exemple d'application réalisée avec Bubblewrap ici : [Stranger Talk](https://strangertalk.chat/download).

Merci de m'avoir lu !
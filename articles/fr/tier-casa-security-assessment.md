---
title: Comment configurer l'add-on Google Workspace pour l'évaluation de sécurité
  CASA Tier 2 - Guide étape par étape
subtitle: ''
author: Nibesh Khadka
co_authors: []
series: null
date: '2024-02-23T16:43:39.000Z'
originalURL: https://freecodecamp.org/news/tier-casa-security-assessment
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Addon-Assesment-Poster--4.png
tags:
- name: Google
  slug: google
- name: google cloud
  slug: google-cloud
seo_title: Comment configurer l'add-on Google Workspace pour l'évaluation de sécurité
  CASA Tier 2 - Guide étape par étape
seo_desc: 'As part of the Google CASA process, developers can run static analysis
  on their application’s source code using an inline integration with OpenText’s Fortify
  Source Code Analyzer (SCA) via the CASA portal.

  Naturally, I had to prepare my source code a...'
---

Dans le cadre du [processus Google CASA](https://appdefensealliance.dev/casa), les développeurs peuvent exécuter une analyse statique sur le code source de leur application en utilisant une intégration en ligne avec l'analysateur de code source Fortify de OpenText (SCA) via le portail CASA.

Naturellement, j'ai dû préparer mon code source selon les instructions. Dans cet article, je vais partager comment j'ai emballé et soumis le code source de mon add-on dans le système d'exploitation Ubuntu.

Mais avant cela, parlons un peu de l'évaluation de sécurité CASA Tier 2.

## Qu'est-ce que l'évaluation de sécurité CASA Tier 2 ?

Le [Tier 2 CASA](https://appdefensealliance.dev/casa) (Cloud Application Security Assessment) est un processus d'évaluation de sécurité en libre-service pour les candidats cherchant à accéder aux données Google Workspace ou à se conformer à des politiques spécifiques de Google Workspace.

Il permet aux développeurs de scanner leurs applications et de soumettre les résultats pour vérification sans qu'un évaluateur externe accède au code ou à l'infrastructure.

### Importance de l'évaluation de sécurité CASA Tier 2

Le Tier 2 CASA est important pour plusieurs raisons :

* **Assurance de sécurité** : Il fournit une vérification indépendante de la posture de sécurité de votre application, réduisant le risque de violations de données et protégeant la vie privée des utilisateurs.
* **Conformité** : Il aide à répondre aux exigences de sécurité pour accéder aux données Google Workspace ou pour adhérer aux politiques de Google, comme les Conditions d'utilisation du Marketplace Workspace.
* **Efficacité** : C'est une alternative plus rapide et plus rentable aux évaluations Tier 1, qui impliquent des évaluateurs externes examinant directement votre application.
* **Confiance** : Si votre add-on est publié sans vérification, il affichera un message "non vérifié" aux clients lors de l'installation de l'add-on, ce qui crée une méfiance et peut conduire à l'abandon du processus d'installation de votre add-on.

Dans le contexte de mon add-on Google Workspace [Scan Me](https://appdefensealliance.dev/casa), l'utilisation de la portée OAuth [restrictive](https://developers.google.com/apps-script/add-ons/concepts/editor-scopes#restricted_scopes) [`auth/drive`](https://developers.google.com/identity/protocols/oauth2/scopes#drive) de l'API Google Drive a probablement déclenché la nécessité d'une évaluation Tier 2. Cette portée accorde à votre add-on l'accès pour voir, modifier, créer et supprimer tous vos fichiers Google Drive, ce qui relève des exigences de sécurité et de confidentialité de Google.

### Ressources supplémentaires

* **[Aperçu du Tier 2 CASA](https://appdefensealliance.dev/casa/tier-2/getting-started)**
* **[Documentation CASA](https://tacsecurity.com/google-casa-cloud-application-security-assessment/)**
* **[Conditions d'utilisation du Marketplace Google Workspace](https://workspace.google.com/terms/marketplace/tos/)**

**Avis de non-responsabilité** : Bien que j'explique le processus CASA Tier 2[,](https://workspace.google.com/marketplace/app/scan_me/613697866593) il est crucial de consulter la documentation officielle et les directives de sécurité de Google pour des exigences et des conseils spécifiques.

La certification d'évaluation est gratuite, soit dit en passant. Pour préparer votre add-on au processus d'évaluation CASA, suivez les étapes suivantes.

## **Étape 1** – **Inscription à la nouvelle procédure d'évaluation**

Si vous utilisez des portées restrictives, vous recevrez un email de l'équipe de vérification de Google à un moment donné vous demandant de vérifier les portées après avoir soumis votre add-on pour vérification.

Cet email est le document de notification. Vous devez donc télécharger cet email au format PDF, qui devra être soumis dans le formulaire de candidature plus tard.

Dans cet email, vous trouverez les instructions suivantes pour l'évaluation Tier 2. Vous trouverez un lien pour vous [inscrire](https://rc.products.pwc.com/login/casa/register) ou vous [connecter](https://rc.products.pwc.com/login/casa/) au portail CASA. Cliquez sur le lien et inscrivez-vous sur le site. Ensuite, cliquez sur **Démarrer une nouvelle évaluation > Créer une nouvelle évaluation**.

Remplissez soigneusement les informations demandées. Téléchargez l'email précédemment téléchargé où l'on vous demande un PDF de notification Tier 2.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1708599483954/704e9bf1-ac25-414d-b3f7-dcda721a82fd.png?auto=compress,format&format=webp&auto=compress,format&format=webp)
_Démarrage de la nouvelle évaluation CASA de l'add-on_

**Note** : Pour un add-on Google Workspace, le type d'application est **Application locale**.

**Attention** : Comme le montre l'image ci-dessus, même si le "**ID de projet**" est demandé dans le champ de saisie, ils demandent le **numéro de projet** inclus dans l'email, et non l'**ID de projet** de votre projet Google Cloud Console.

Après avoir soigneusement rempli les détails et soumis le formulaire, vous arriverez à un nouvel écran – **Application Screening** – où il y a deux choses que vous devez télécharger :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1708599799176/52631f9a-8719-472e-997e-2169d1063127.png?auto=compress,format&format=webp&auto=compress,format&format=webp)
_Télécharger le package Scan Central et les instructions d'installation_

1. Package Fortify Scan Central.
2. Instructions sur la compression du code source de votre application pour l'évaluation initiale.

## **Étape 2** – **Télécharger et installer Java JDK**

Pour utiliser le package Scan Central comme mentionné dans les instructions, un minimum de JDK 11 est requis.

Pour configurer le chemin pour l'environnement Java dans Linux, j'ai suivi [cette](https://stackoverflow.com/a/73414921/6163929) instruction sur StackOverflow.

## **Étape 3** – **Configurer le chemin pour Scan Central**

Maintenant, ajoutons le chemin vers Scan Central dans notre système.

Dans votre CLI, ouvrez le fichier `.bashrc` avec `sudo nano ~/.bashrc`. Ajoutez le chemin suivant à la fin du fichier :

```bash
# SCAN Central
# Le chemin ressemble à ce qui suit
#/home/<username>/Fortify_ScanCentral_Client_22.2.1_x64/bin

export PATH=$PATH:<Chemin vers le dossier bin dans Scan Central>

```

Enregistrez (CTRL+S) et quittez (CTRL + X) le fichier.

Ouvrez `.profile` avec `sudo nano ~/.profile` et ajoutez le même chemin que ci-dessus. Vous pouvez vérifier la version de Scan Central dans votre CLI avec la commande `scancentral -version`, pour vous assurer que l'installation a réussi.

## **Étape 4** – **Emballer le code source pour l'évaluation**

Pour emballer le code source de votre add-on Google Workspace, allez dans le répertoire racine de votre projet. Si vous suivez le manuel d'instructions, allez à la section pour l'emballage du code JavaScript.

Dans le répertoire racine, exécutez l'une des commandes suivantes :

```bash
#cmd 1
scancentral package -bt none -o myPackage.zip
# ou cmd 2
scancentral package -bt none --scan-node-modules -o myPackage.zip

```

**Note** : La commande `scancentral.bat` est pour les utilisateurs Windows.

Comme mentionné dans les instructions, la commande 2 augmente la taille du package et n'est pas nécessaire pour Node.js ou Angular. J'ai créé un add-on Workspace, donc je n'ai pas de node-modules dans mon code source.

Après cela, vous verrez un package compressé nommé **myPackage** dans le répertoire où vous avez exécuté l'opération d'emballage.

## **Étape 5** – **Lancer le processus de scan**

Après l'emballage, retournez au portail CASA et cliquez sur le lien de votre ID d'évaluation dans la liste, puis ouvrez la fenêtre **Application Screening**. Ici :

1. Cliquez sur le bouton **Begin Scan Process**.
2. Téléchargez le package que vous venez de compresser.
3. Cliquez sur le bouton **Upload File & Initiate Scan**.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/casa-form-filling--2.png)
_Télécharger le code source vers Fortify Scan_

Cela lancera le scan automatique de votre application, ce qui marque le début de l'évaluation de votre add-on.

**Rappel** : Comme je l'ai personnellement expérimenté, si votre code source utilise la méthode `Math.random()`, alors le scanner automatique ne validera pas votre code.

Si vous passez cette phase, le processus de vérification manuelle commencera où vous devrez remplir des formulaires pour l'enquête. Allez à ce [lien](https://lookerstudio.google.com/u/0/reporting/757d8fab-9682-4b74-9acc-58efb5e3081c/page/p_ana6axxq4c?s=tug3GYx0bmg) pour les questions qui seront posées dans l'enquête CASA. Ici, choisissez l'option **Application locale** pour le type d'application pour un add-on Google Workspace. Je tiens à vous rappeler que les questions changeront en fonction des réponses fournies.

## Conclusion

J'espère que ce blog vous a aidé à réduire le temps et la confusion que j'ai dû rencontrer lorsque j'ai essayé d'évaluer mon [add-on](https://workspace.google.com/marketplace/app/scan_me/613697866593). Et surtout, ne renoncez pas en cours d'évaluation, sinon vos mois de travail acharné seront vains.

Mon add-on [Scan Me](https://workspace.google.com/marketplace/app/scan_me/613697866593) scanne le Google Drive et prépare un rapport d'audit dans un fichier de feuille de calcul de votre choix dans votre Google Drive. Il rend extrêmement facile l'analyse de votre Google Drive à partir d'un seul endroit, et il offre également un quota gratuit. Si vous cherchez un add-on similaire, j'espère que vous essaierez cet add-on.

C'est Nibesh Khadka, je vous souhaite une bonne journée.
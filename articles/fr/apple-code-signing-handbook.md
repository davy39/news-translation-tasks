---
title: Le guide de la signature de code Apple
date: '2025-06-10T20:07:32.071Z'
author: Sravan Karuturi
authorURL: https://www.freecodecamp.org/news/author/sravankaruturi/
originalURL: https://freecodecamp.org/news/apple-code-signing-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1749585600223/49e9c922-0b5d-4a98-a619-eedfd7a8b617.png
tags:
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: Apps
  slug: apps-tag
- name: macOS
  slug: macos
- name: handbook
  slug: handbook
seo_desc: In this handbook, I’ll demystify the Apple app code signing process. Apple's
  ecosystem is powerful, but its distribution mechanisms – with various identifiers,
  certificates, and profiles – can appear complex. This guide attempts to make that
  journey ...
---


Dans ce guide, je vais démystifier le processus de signature de code des applications Apple. L'écosystème d'Apple est puissant, mais ses mécanismes de distribution – avec ses divers identifiants, certificats et profils – peuvent paraître complexes. Ce guide tente de rendre ce parcours plus gérable et plus simple pour vous.

<!-- more -->

Tout au long de ce manuel, vous apprendrez comment :

-   Établir et gérer correctement l'identité unique d'une application.
    
-   Comprendre les rôles des différents certificats de développeur Apple et comment les créer et les gérer.
    
-   Différencier les divers types de profils de provisionnement (provisioning profiles) et savoir quand utiliser chacun d'eux.
    

Ce guide est destiné aux nouveaux développeurs qui souhaitent apprendre le fonctionnement du processus de signature de code, mais il devrait également être utile aux développeurs expérimentés qui souhaitent ou doivent se rafraîchir la mémoire.

### Prérequis

Bien qu'il n'y ait pas de prérequis stricts pour comprendre les certificats, les bundles et les profils de provisionnement pour la distribution sur les plateformes Apple, il est utile d'avoir un compte développeur Apple pour suivre les étapes.

## Table des matières

-   [App IDs, Bundle IDs – L'identité de votre application][1]
    
-   [Comprendre la distribution : Plongée au cœur des certificats][2]
    
-   [Le pont entre tout : Les profils de provisionnement][3]
    
-   [Gestion des appareils – Builds de développement et Ad Hoc][4]
    
-   [Possibilités : Activer les capacités et les services][5]
    
-   [Conclusion][6]
    

## **App IDs, Bundle IDs — L'identité de votre application**

Le Bundle ID et l'App ID correspondant enregistré auprès d'Apple constituent la base de l'identité d'une application. Il est très important de les établir correctement dès le début, car des erreurs ou des mauvaises configurations à ce stade peuvent entraîner des complications importantes par la suite, en particulier une fois que vous avez soumis votre application à App Store Connect.

### Comprendre `CFBundleIdentifier` (Bundle ID)

#### Qu'est-ce que le "Bundle ID" ?

Considérez le Bundle ID comme un nom unique ou une empreinte digitale pour votre application. Le `CFBundleIdentifier`, plus connu sous le nom de **Bundle ID**, est une chaîne de caractères qui identifie de manière unique votre application.

Cet identifiant n'est pas seulement un nom – il remplit plusieurs fonctions cruciales.

-   Le système d'exploitation s'appuie sur lui pour appliquer des préférences et des réglages spécifiques à une application.
    
-   Il est utilisé pour lancer l'application à partir d'autres applications, etc.
    
-   Il joue un rôle essentiel dans la validation de la signature de code d'une application, garantissant l'intégrité et l'authenticité de celle-ci.
    
-   Le Bundle ID défini dans le fichier Info.plist d'une application doit correspondre exactement au Bundle ID enregistré pour l'application dans App Store Connect pour que la soumission et la distribution réussissent.
    

La chaîne du Bundle ID doit respecter des limitations de caractères spécifiques : elle ne peut contenir que des caractères alphanumériques `A-Z, a-z, 0-9`, des traits d'union `-` et des points `.`. Il est important de noter que les Bundle IDs sont traités comme **insensibles à la casse** par le système.

### Comment choisir et formater votre Bundle ID (Reverse-DNS et bonnes pratiques)

Apple recommande vivement, et c'est une pratique standard, d'utiliser un format DNS inversé (reverse-DNS) pour les Bundle IDs.

Un exemple courant serait `com.votrenomdentreprise.nomdelapp`. Cette convention exploite l'unicité mondiale des noms de domaine pour aider à garantir l'unicité mondiale des Bundle IDs.

Si une organisation utilise son nom de domaine unique (par exemple, `sravan.gg` devient `gg.sravan`) comme préfixe, et que le nom de l'application est unique au sein de cette organisation, le Bundle ID résultant (par exemple, `gg.sravan.mycoolapp`) a de fortes chances d'être unique au monde.

**Note latérale** : Bien qu'Xcode ne vous empêche pas de créer quelque chose comme `com.google.mapping` même si vous ne travaillez pas chez Google, cela sera très probablement rejeté lors du processus de révision de l'App Store. En effet, cela implique la propriété de ce domaine. Ainsi, bien que ce soit techniquement possible au début, vous ne devriez pas utiliser de domaines qui ne vous appartiennent pas.

La nature fondamentale du Bundle ID en tant qu'identifiant unique à l'échelle du système – couplée à son immutabilité après le premier téléchargement d'une application sur App Store Connect – signifie que vous devez traiter sa sélection avec le même sérieux que le choix d'un **identifiant permanent et inchangeable** pour une entité critique. Une erreur dans le Bundle ID après ce point peut nécessiter la création d'une toute nouvelle fiche d'application sur l'App Store.

### App IDs dans le portail Apple Developer : Explicit vs Wildcard

#### De quel type avez-vous besoin ?

Dans le portail Apple Developer, les développeurs enregistrent un "App ID". Cet App ID est un enregistrement qui lie une ou plusieurs applications d'une même équipe de développement à des services d'application spécifiques (capabilities) et est utilisé dans les profils de provisionnement. Nous en apprendrons davantage à ce sujet dans les sections suivantes.

Il existe deux types principaux d'App IDs :

-   **Explicit App ID (App ID explicite) :** Ce type est utilisé pour une seule application. Le Bundle ID spécifié dans un App ID explicite doit correspondre exactement au CFBundleIdentifier dans le fichier Info.plist de l'application (par exemple, `com.mycompany.myapp`). Les App IDs explicites sont requis pour les applications qui utilisent de nombreux services et capacités spécifiques d'Apple, tels que les achats intégrés (In-App Purchases, activés par défaut pour les App IDs explicites), les notifications push, iCloud, HealthKit et Sign in with Apple.
    
-   **Wildcard App ID (App ID générique) :** Ce type peut être utilisé pour un ensemble d'applications qui partagent un préfixe de Bundle ID commun. Il contient un astérisque (\*) comme dernière partie de sa chaîne de Bundle ID (par exemple, `com.mycompany.*`). Cet App ID générique correspondrait à n'importe quelle application dont le Bundle ID commence par `com.mycompany.`, comme [`com.mycompany.app`][7] ou `com.mycompany.utility`. Cependant, vous ne pouvez pas utiliser d'App IDs génériques si l'application nécessite des services ou des capacités qui imposent un App ID explicite.
    

Le choix entre un App ID explicite et un App ID générique a des implications importantes. L'App ID agit comme un point d'enregistrement central, et les capacités sont "activées" pour cet enregistrement – nous reviendrons sur les capacités plus tard dans ce guide.

Vous pouvez considérer un App ID explicite comme une clé spécifique conçue pour déverrouiller des "serrures" supplémentaires (capacités). Un App ID générique, étant plus vague, pourrait ne pas s'adapter à ces serrures supplémentaires. Si vous choisissez initialement un App ID générique par commodité, mais que vous avez besoin plus tard d'une fonctionnalité nécessitant un App ID explicite (comme les notifications push), vous serez contraint de créer un nouvel App ID explicite et de reconfigurer les réglages et les profils de provisionnement associés.

Assurez-vous donc de bien réfléchir aux fonctionnalités actuelles et futures de votre application lors de la sélection d'un type d'App ID. Le tableau suivant fournit une comparaison rapide.

Ma recommandation personnelle est de toujours opter pour des App IDs explicites, à moins que vous n'ayez besoin de la flexibilité des App IDs génériques.

| **Fonctionnalité** | **Explicit App ID** | **Wildcard App ID** |
| --- | --- | --- |
| **Correspondance Bundle ID** | Correspondance exacte (ex: [com.foo.bar][8]) | Correspondance de suffixe (ex: [com.foo][9].\*) |
| **Cas d'utilisation** | Application unique | Ensemble d'apps avec un ID de base similaire |
| **Capacités** | Supporte toutes les capacités | Limitées (ne peut utiliser les services exigeant des IDs explicites) |
| **Unicité** | Identifiant unique mondial pour une app spécifique | Identifie un groupe d'applications |

### Étape par étape : Comment enregistrer votre App ID dans le portail Apple Developer

Pour enregistrer un App ID, vous aurez besoin d'une **adhésion au Apple Developer Program**. De plus, les actions doivent être effectuées par une personne ayant le rôle de Account Holder (Titulaire du compte) ou Admin.

Le processus est le suivant :

1.  Connectez-vous au portail Apple Developer et accédez à "Certificates, Identifiers & Profiles", puis sélectionnez "Identifiers" dans la barre latérale.
    
2.  Cliquez sur le bouton "Ajouter (+)" pour créer un nouvel identifiant.
    
    ![Image illustrant le bouton Ajouter](https://cdn.hashnode.com/res/hashnode/image/upload/v1748642247245/a24b527f-e810-4a9c-b75a-dcd3d189b1d1.png)
    
3.  Sélectionnez "App IDs" dans la liste des options et cliquez sur "Continue".
    
    ![851f64f3-e608-4fb7-9f31-bd30adb64beb](https://cdn.hashnode.com/res/hashnode/image/upload/v1748642283885/851f64f3-e608-4fb7-9f31-bd30adb64beb.png)
    
4.  Assurez-vous que le type "App" est sélectionné (il l'est généralement par défaut) et cliquez sur "Continue".
    
    ![Sélection du type App](https://cdn.hashnode.com/res/hashnode/image/upload/v1748642318142/a7b28529-bbe6-4240-953e-836de3e948ac.png)
    
5.  Saisissez une "Description" pour l'App ID. C'est pour votre référence au sein du portail (par exemple, "Mon App ID super cool").
    
    ![Écran d'enregistrement de l'App Id](https://cdn.hashnode.com/res/hashnode/image/upload/v1748642392862/a5322cf5-3d75-4b0b-93bf-d46dd1ce8afe.png)
    
6.  Choisissez le "App ID Type" : "Explicit" ou "Wildcard".
    
7.  Pour un "Explicit App ID", saisissez le Bundle ID exact qui sera utilisé dans votre projet Xcode (par exemple, `com.votreentreprise.votreapp`). Pour un "Wildcard App ID", saisissez un suffixe de Bundle ID se terminant par un astérisque (par exemple, `com.votreentreprise.*`).
    
8.  Faites défiler vers le bas jusqu'à la section "Capabilities" et cochez les cases correspondant aux services d'application que votre application utilisera. Certaines capacités peuvent nécessiter une configuration supplémentaire à cette étape ou plus tard. (Encore une fois, nous couvrirons les capacités d'application plus en détail par la suite).
    
9.  Cliquez sur "Continue", vérifiez attentivement tous les détails, puis cliquez sur "Register" pour finaliser la création de l'App ID.
    
    ![Écran de confirmation de l'App ID](https://cdn.hashnode.com/res/hashnode/image/upload/v1748642432661/2052a435-ed0e-404a-9178-7d6541fc9421.png)
    

### Comment gérer votre Bundle ID : Xcode, App Store Connect et le point de non-retour

Le Bundle ID spécifié dans un projet Xcode est critique. Pour le définir :

1.  Dans le navigateur de projet Xcode, sélectionnez la cible (target) de votre application.
    
2.  Ouvrez l'onglet "Signing & Capabilities".
    
3.  Développez la section "Signing".
    
4.  Dans le champ de texte "Bundle Identifier", saisissez le Bundle ID. Cet identifiant doit correspondre précisément au Bundle ID associé à un App ID explicite enregistré dans le portail Developer, ou se conformer au modèle d'un App ID générique le cas échéant.
    

Il est important de comprendre la différence entre le "Bundle ID" (ou `CFBundleIdentifier`) dans le projet Xcode et l'"App ID" enregistré dans le portail Developer. L'"App ID" dans le portail développeur est une entité qui _contient_ une chaîne "Bundle ID" (soit explicite, soit générique). La chaîne dans le champ "Bundle Identifier" de votre projet Xcode doit correspondre à cette chaîne contenue.

Lors de la préparation de la distribution via TestFlight ou l'App Store, vous devrez créer une fiche d'application dans App Store Connect. Le Bundle ID que vous saisissez lors de la création de cette fiche d'application doit correspondre exactement au Bundle ID du projet Xcode.

#### Un avertissement critique : Immutabilité après le premier téléchargement

C'est un point de non-retour : une fois que vous avez téléchargé un build d'une application sur App Store Connect, le Bundle ID de cette fiche d'application **ne peut plus être modifié**.

De plus, après un téléchargement, vous ne pouvez pas supprimer l'App ID explicite associé enregistré dans le portail Developer. Cette immutabilité souligne la nécessité d'une _planification et d'une vérification minutieuses_ du Bundle ID avant tout téléchargement.

Si vous préférez une gestion programmatique ou l'automatisation, l'API App Store Connect fournit des ressources pour gérer les Bundle IDs. Vous pouvez [en savoir plus à ce sujet ici][10].

## **Comprendre la distribution : Plongée au cœur des certificats**

### Que sont les certificats ?

Les certificats sont des identifiants numériques qui vérifient l'**identité d'un développeur** – c'est-à-dire vous – auprès d'Apple et, par extension, auprès des utilisateurs de l'application.

Ils sont fondamentaux pour le processus de signature de code d'Apple, qui est obligatoire pour toutes les applications afin de garantir qu'elles proviennent d'une **source connue** et n'ont pas été altérées depuis leur signature.

### Qu'est-ce que la signature de code : Assurer la confiance et l'intégrité

La signature de code consiste pour vous, en tant que développeur, à signer l'application avec votre signature. C'est le processus consistant à attacher une signature numérique au code d'une application. Cette signature assure aux utilisateurs deux choses essentielles :

1.  **Authenticité :** L'application a été créée par un développeur Apple identifié (un individu ou une équipe).
    
2.  **Intégrité :** Le code de l'application n'a pas été modifié ou corrompu depuis qu'il a été signé par le développeur.
    

Le processus implique l'utilisation d'une clé privée, détenue de manière sécurisée par le développeur (vous), pour créer la signature. La clé publique correspondante, intégrée dans le certificat du développeur (délivré par Apple), est utilisée par le système pour vérifier cette signature.

Ce système de vérification d'identité et de contrôle d'intégrité est crucial. Le certificat du développeur, délivré par Apple en tant qu'autorité de certification (CA), se porte garant de son identité. Le processus de signature de code, utilisant le hachage et le chiffrement, garantit que toute modification du code après la signature invaliderait la signature.

Pour les développeurs d'applications, les avantages de la signature de code incluent la suppression des avertissements sur macOS pour les applications distribuées en dehors du Mac App Store, offrant ainsi une expérience utilisateur plus fluide. C'est une exigence obligatoire pour répertorier des applications sur n'importe quel App Store d'Apple. Cela renforce également la sécurité de l'application car cela agit comme un moyen de dissuasion contre les altérations malveillantes.

### Types de certificats : Development, Distribution et Developer ID

Apple fournit différents types de certificats pour les diverses étapes du développement et les méthodes de distribution. Chacun d'eux a un rôle distinct à jouer tout au long du processus de développement de l'application.

#### 1. Certificats de développement (par exemple, "Apple Development") :

-   **Objectif :** Utilisés pour signer les applications pendant la phase de développement, permettant de les installer et de les exécuter sur un nombre limité d'_appareils de test enregistrés_ et de simulateurs pour le débogage et les tests.
    
-   **Identifie :** Identifie généralement un développeur individuel via son identifiant de développeur.
    
-   **Utilisé avec :** Profils de provisionnement de développement – nous y reviendrons plus tard.
    

#### 2. Certificats de distribution (par exemple, "Apple Distribution") :

-   **Objectif :** Utilisés pour signer les applications destinées à la distribution, soit par des méthodes Ad Hoc (à un ensemble limité de _testeurs enregistrés_), soit pour la soumission à l'App Store.
    
-   **Identifie :** L'équipe de développement via l'identifiant d'équipe (Team ID).
    
-   **Cas d'utilisation :**
    
    1.  **App Store :** Pour signer la version finale d'une application qui sera téléchargée sur App Store Connect pour les tests bêta TestFlight ou la sortie sur l'App Store (iOS, macOS, tvOS, watchOS). Ils sont utilisés avec les profils de provisionnement App Store – plus de détails plus tard.
        
    2.  **Ad Hoc :** Pour signer les applications qui seront distribuées à un _nombre limité d'appareils de test enregistrés en dehors de l'App Store ou de TestFlight_. Ils sont utilisés avec un profil de provisionnement Ad Hoc. Plus de détails plus tard.
        

#### 3. Certificats Developer ID (pour les applications Mac distribuées hors du Mac App Store) :

-   **Objectif :** Spécifiquement pour les développeurs macOS qui souhaitent distribuer leurs applications directement aux utilisateurs (par exemple, depuis leur propre site web) plutôt que via le Mac App Store. Gatekeeper sur macOS reconnaît les applications signées avec un certificat Developer ID, assurant aux utilisateurs que l'application provient d'un développeur connu et n'a pas été altérée.
    
-   **Types :**
    
    1.  **Developer ID Application :** Utilisé pour signer le bundle de l'application Mac (.app) lui-même.
        
    2.  **Developer ID Installer :** Utilisé pour signer un package d'installation Mac (.pkg) contenant l'application signée.
        
    3.  **Limite :** Les développeurs peuvent créer jusqu'à cinq certificats Developer ID Application et jusqu'à cinq certificats Developer ID Installer.
        

Le tableau suivant résume ces types de certificats :

| **Type de certificat** | **Délivré à** | **Objectif principal** | **Type de profil de provisionnement utilisé** | **Cas d'utilisation clés** |
| --- | --- | --- | --- | --- |
| Apple Development | ID Dev individuel | Développer et déboguer sur appareils enregistrés | Development | Builds Xcode pour tests locaux, exécution sur appareils de test personnels/équipe. |
| Apple Distribution | Team ID | Soumettre l'app à l'App Store / Distribution Ad Hoc | App Store, Ad Hoc | Builds finaux pour TestFlight, soumission App Store, ou builds Ad Hoc QA/client. |
| Developer ID Application | Team ID | Signer app Mac pour distribution hors Mac App Store | **Profil Developer ID** si l'app utilise des capacités spécifiques (ex: Push, Associated Domains). | Distribution de logiciels Mac directement aux utilisateurs (ex: site web). |
| Developer ID Installer | Team ID | Signer Pkg d'installation Mac pour distribution hors Mac App Store | N/A. (L'app dans le package peut avoir besoin d'un profil). | Distribution de logiciels Mac dans un installeur .pkg directement aux utilisateurs. |
| APNs / Clés de service (.p8) | Team ID | Communication sécurisée avec services Apple spécifiques | N/A pour la signature d'app | Notifications Push, MusicKit, DeviceCheck, etc. (Authentification par token) |

![Écran de création d'un nouveau certificat dans App Store Connect](https://cdn.hashnode.com/res/hashnode/image/upload/v1748216973656/76df3f64-c84e-4195-a092-37c1143d8b1b.png)

### Comment créer un certificat Apple – Vue d'ensemble

Voici un aperçu général de la création d'un certificat Apple :

-   Générez une demande de signature de certificat (CSR) sur votre Mac. (Oui, vous avez besoin d'un Mac.)
    
-   Vous téléchargez ce CSR dans AppStoreConnect dans le cadre de la création du certificat.
    
-   Téléchargez le certificat depuis AppStoreConnect une fois qu'il est émis.
    
-   Installez le certificat dans votre Trousseau d'accès (Keychain).
    

Nous allons maintenant passer en revue chaque étape plus en détail. Cette partie est très importante, car nous devons sauvegarder certains des fichiers générés localement sous peine de perdre la capacité de transférer ces certificats. Cela signifierait révoquer et réémettre des certificats (ce que j'ai fait plus de fois que je ne voudrais l'admettre).

#### Comment créer une demande de signature de certificat (CSR)

Une demande de signature de certificat (CSR) est un nom sophistiqué pour un bloc de texte chiffré contenant des informations sur l'auteur de la demande de certificat (comme votre nom et la clé publique). Elles sont largement utilisées dans le monde de la cryptographie.

Pour nos besoins, vous générerez un CSR sur votre Mac, puis vous le soumettrez à Apple pour demander un certificat numérique. Le processus de génération du CSR crée également une nouvelle paire de clés publique/privée sur le Mac – la clé privée est stockée dans Trousseau d'accès et est utilisée pour la signature de code finale.

Pour créer un CSR à l'aide de Trousseau d'accès sur macOS :

1.  Lancez Trousseau d'accès (vous pouvez le trouver dans `/Applications/Utilities/` ou utiliser Spotlight).
    
2.  Dans la barre de menus, choisissez Trousseau d'accès > Assistant de certification > Demander un certificat à une autorité de certification.... (Ici, l'autorité de certification sera Apple).
    
3.  Dans la boîte de dialogue, saisissez votre adresse e-mail et un nom commun pour la clé (par exemple, "Ma clé Mac" ou "Clé Dev [Votre Nom]"). Ce nom sert principalement à votre identification dans le Trousseau.
    
4.  Laissez le champ "Adresse e-mail de l'AC" vide – nous ne l'enverrons pas par e-mail à l'autorité de certification (Apple).
    
5.  Sélectionnez l'option "Enregistrée sur le disque" et cliquez sur "Continuer".
    
6.  Enregistrez le fichier, qui aura une extension .certSigningRequest. La clé privée correspondante est maintenant stockée dans le trousseau de session (login). **Cette clé privée est irremplaçable par Apple et vous devez la conserver vous-même.**
    

![Dialogue pour la création du CSR](https://cdn.hashnode.com/res/hashnode/image/upload/v1748288861336/50f20da3-69d9-476d-97e7-331f9b9b5c76.png)

#### Comment générer et télécharger vos certificats Apple

Une fois que vous avez créé un CSR, vous pouvez demander un certificat sur le portail Apple Developer :

1.  Accédez à "Certificates, Identifiers & Profiles" et sélectionnez "Certificates".
    
2.  Cliquez sur le bouton ajouter (+).
    
3.  Choisissez le type de certificat souhaité.
    
4.  Suivez les instructions et, lorsqu'on vous le demande, téléchargez le fichier .certSigningRequest généré précédemment.
    
5.  Une fois qu'Apple a traité la demande, le certificat sera disponible au téléchargement sous forme de fichier .cer.
    
    ![Invite à télécharger le CSR après avoir sélectionné le type de certificat](https://cdn.hashnode.com/res/hashnode/image/upload/v1748289386364/78f46b4e-b232-4484-98c2-dcb75120fd61.png)
    

Pour installer le certificat, double-cliquez sur le fichier .cer téléchargé. Il sera ajouté à l'application Trousseau d'accès – apparaissant généralement dans le trousseau "session" sous la catégorie "Mes certificats", où il devrait être associé à la clé privée générée lors du processus de création du CSR.

Vous pouvez voir mon certificat et ma clé privée dans l'image ci-dessous pour référence.

![Un exemple de l'apparence de votre certificat et de la clé privée dans le trousseau d'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1748289120657/38f711dd-887a-4fae-844d-e389c65234cf.png)

Pour récapituler, le CSR certifie que vous avez généré la demande depuis votre Mac. Le certificat certifie qu'Apple (dans ce cas, un intermédiaire comme "Apple Worldwide Developer Relations Certification Authority") confirme avoir vérifié le CSR et que c'est bien vous qui signerez avec le fichier de certificat (`.cer`).

Ceci est appliqué par le fait que vous seul avez accès à la clé privée – si vous la perdez, vous ne pouvez plus utiliser ce certificat.

Ainsi, si vous utilisez ce certificat (et la clé privée) pour signer une application, l'App Store / le système d'exploitation sait avec certitude que c'est vous puisque Apple l'a confirmé.

### Comment stocker vos clés : Que sont les fichiers .p12 ?

Comme je l'ai mentionné dans la section précédente, pour signer le code d'une application, vous avez besoin de votre certificat (contenant la clé publique) et de la clé privée correspondante. Celle-ci est créée en même temps que le CSR, et vous pouvez la trouver dans l'application `Trousseau d'accès`.

Nous appelons la combinaison du certificat et de la clé privée une identité numérique. Cela prouve votre identité lorsque vous signez une application avec eux.

#### Fichiers .p12 (Personal Information Exchange) :

Un fichier .p12 est un format d'archive protégé par mot de passe utilisé pour regrouper un certificat avec sa clé privée. Ses objectifs principaux sont :

-   Sauvegarder l'identité numérique au cas où vous perdriez l'accès à votre Mac.
    
-   Transférer l'identité numérique vers un autre Mac (par exemple, pour un autre membre de l'équipe ou une nouvelle machine de développement).
    
-   Fournir l'identité à des systèmes de build automatisés ou à des services de build tiers.
    

Historiquement, j'ai stocké le fichier .p12 sur un disque partagé avec mon équipe et partagé le mot de passe oralement – vous pouvez également le stocker sur un disque de sauvegarde local.

Super. Alors, comment en créer un ?

#### Pour exporter un fichier .p12 depuis Trousseau d'accès :

1.  Ouvrez Trousseau d'accès, sélectionnez le trousseau "session" et allez dans la catégorie "Mes certificats".
    
2.  Localisez le certificat souhaité. Il devrait avoir un triangle de dévoilement extensible indiquant une clé privée associée (regardez l'image de mi certificat ci-dessus).
    
3.  Sélectionnez _à la fois_ le certificat et sa clé privée (ou faites un clic droit sur le certificat et choisissez "Exporter").
    
4.  Faites un clic droit et choisissez "Exporter les [X] éléments...".
    
5.  Dans la boîte de dialogue d'enregistrement, choisissez le format de fichier "Échange d'informations personnelles (.p12)".
    
6.  Attribuez un mot de passe fort pour protéger le fichier .p12. Ce mot de passe sera requis lors de l'importation du fichier ailleurs. C'est crucial pour la sécurité.
    
7.  Enregistrez le fichier dans un endroit sûr.
    
    ![Image de l'exportation de mon certificat et de ma clé privée sous forme de fichier .p12](https://cdn.hashnode.com/res/hashnode/image/upload/v1748297124625/f9d2cfe0-3538-405e-8fb0-af08276c4326.png)
    

## **Le pont entre tout : Les profils de provisionnement**

Les profils de provisionnement (provisioning profiles) sont le dernier lien entre un App ID, les certificats de développeur et, dans certains cas, une liste d'appareils de test spécifiques. Ils agissent comme un laissez-passer, autorisant une application signée avec un certificat particulier à être installée et exécutée soit sur des appareils désignés, soit à être soumise à l'App Store.

### Qu'est-ce qu'un profil de provisionnement exactement ?

Un profil de provisionnement est un fichier `.mobileprovision` (pour iOS / VisionOS) ou `.provisionprofile` (pour macOS) qui contient plusieurs informations clés :

-   **L'App ID :** Spécifie à quelle application (ou ensemble d'applications, si vous utilisez un App ID générique) le profil s'applique.
    
-   **Certificats :** Contient un ou plusieurs certificats de développeur ou de distribution pouvant être utilisés pour signer l'application.
    
-   **UDIDs d'appareils (pour Development et Ad Hoc) :** Pour les profils destinés aux tests sur des appareils spécifiques, il inclut une liste des identifiants uniques d'appareils (UDID) de ces appareils autorisés – nous en saurons plus sur les appareils dans la section suivante.
    
-   **Entitlements :** Une liste de services ou de capacités d'application (comme les notifications push, iCloud, App Groups) que l'application est autorisée à utiliser. Ceux-ci sont dérivés des capacités activées pour l'_App ID associé_.
    

Vous pouvez ouvrir le fichier à l'aide de `vim` ou de n'importe quel éditeur pour voir des parties du contenu qui incluent l'App Id, les systèmes d'exploitation, les certificats, etc.

Le système d'exploitation vérifie le profil de provisionnement au lancement de l'application pour s'assurer que l'application est autorisée à s'exécuter sur l'appareil actuel et à utiliser les services demandés. Si le profil est manquant, invalide ou ne correspond pas à la signature de l'application ou à l'appareil, l'application ne se lancera pas.

Ils sont différents des certificats, car les certificats sont liés à vous en tant que développeur. Mais les profils de provisionnement sont liés à une application spécifique – avec des capacités spécifiques pour un développeur spécifique et éventuellement sur des appareils spécifiques.

Si l'un de ces éléments change (disons que vous avez ajouté une capacité ou que votre certificat a expiré, par exemple), vous devrez générer à nouveau le profil de provisionnement. Ce sont les fichiers avec lesquels vous travaillerez le plus parmi tous ceux cités ci-dessus, et tout changement peut rendre votre profil invalide.

### Types de profils de provisionnement : Development, Ad Hoc, App Store (et Enterprise)

Tout comme les certificats, nous avons plusieurs types de profils de provisionnement. À l'instar des certificats, il peut y avoir des profils de provisionnement de développement et de distribution.

Comme nous suivons également les appareils sur lesquels un profil est censé s'exécuter, nous avons plusieurs types de profils de distribution en fonction des appareils cibles.

Nous avons également des profils spéciaux comme "Enterprise" qui ajouteront des capacités supplémentaires (comme l'accès à la caméra principale sur le Vision Pro) mais restreindront vos méthodes de distribution d'applications à l'entreprise uniquement.

Nous allons passer en revue chacun de ces types maintenant. N'hésitez pas à passer directement à celui que vous recherchez.

| **Type de profil** | **Objectif** | **Type(s) de certificat requis** | **Enregistrement d'appareil requis ?** | **Méthode de distribution** |
| --- | --- | --- | --- | --- |
| **Development** | Installer et déboguer sur appareils enregistrés pendant le dev (besoin d'Xcode). | Development | Oui | Xcode run, déploiement sur appareil local. |
| **Ad Hoc** | Distribuer à un nombre limité d'appareils de test enregistrés (pas besoin d'Xcode). | Distribution | Oui | Installation manuelle (ex: via lien, e-mail, MDM) pour les testeurs. |
| **App Store Connect** | Soumettre l'app à App Store Connect pour TestFlight ou sortie App Store. | Distribution | Non | Téléchargement vers App Store Connect. |
| **Enterprise** | Distribuer des apps propriétaires aux employés d'une organisation. | Enterprise (Distribution) | Non (selon termes du programme) | Distribution interne (ex: portail privé, MDM). |
| **Developer ID** | Permet à une app macOS distribuée hors App Store d'utiliser des fonctions avancées. | Developer ID | Non | Hors Mac App Store (ex: page web, USB, MDM). |

#### **Profil de provisionnement Development :**

-   **Permet** à une application d'être installée et déboguée sur des appareils spécifiques enregistrés dans le compte du développeur pendant la phase de développement actif. Plus d'informations sur l'enregistrement des appareils plus tard.
    
-   **Contient** un App ID, un ou plusieurs certificats de développement et une liste d'UDIDs d'appareils enregistrés.
    
-   **Créé** manuellement dans le portail Apple Developer ou généré automatiquement par Xcode si `Automatically manage signing` est activé.
    

#### **Profil de provisionnement Ad Hoc :**

-   **Permet** la distribution d'une application à un nombre limité d'appareils de test enregistrés **sans** nécessiter Xcode pour l'installation. C'est idéal pour distribuer des builds aux équipes QA, aux testeurs bêta ou aux clients pour obtenir des retours.
    
-   **Contient** un App ID (souvent un App ID explicite, ou un géré par Xcode comme `XC Wildcard` ou `XC`), un seul certificat de distribution et une liste d'UDIDs d'appareils enregistrés.
    
-   **Créé** manuellement dans le portail Developer ou géré par la signature automatique d'Xcode.
    

#### **Profil de provisionnement App Store Connect :**

-   **Requis** pour signer une application en vue de sa soumission à App Store Connect. C'est la voie pour distribuer des applications via TestFlight pour des tests bêta plus larges et pour la sortie officielle sur l'App Store.
    
-   **Contient** un App ID explicite (ou un App ID qui correspond au Bundle ID de l'application, y compris les App IDs gérés par Xcode), et un seul certificat de distribution. _Les UDIDs d'appareils ne sont pas inclus dans ce type de profil car il est destiné à une distribution plus large._
    
-   **Créé** manuellement dans le portail Developer ou géré par la signature automatique d'Xcode.
    

#### **Profil de provisionnement Enterprise :**

-   Exclusivement pour les membres du **Apple Developer Enterprise Program**. Il permet aux développeurs de ces organisations de distribuer des applications propriétaires internes directement à leurs employés, en contournant l'App Store public.
    
-   Note : Ce programme a des critères d'adhésion stricts et est strictement réservé à la distribution interne au sein de l'organisation inscrite – ces applications ne peuvent pas être poussées sur l'App Store.
    

#### **Profil de provisionnement Developer ID :**

-   **Requis** pour utiliser certains services Apple ou des capacités avancées comme les notifications push, CloudKit, Sign in with Apple ou des services iCloud spécifiques.
    
-   **Contient** un App ID, un certificat de distribution Developer ID, les entitlements autorisés pour l'application.
    
-   **Créé** manuellement dans le portail Developer – ne sera pas ajouté automatiquement par la signature automatique d'Xcode.
    

### Comment créer et gérer les profils de provisionnement

La création et la gestion des profils de provisionnement nécessitent généralement un rôle de Account Holder ou d'Admin dans le Apple Developer Program. Vous avez également besoin d'un App ID configuré, du ou des certificats appropriés et, pour les profils Development ou Ad Hoc, d'une liste d'UDIDs d'appareils enregistrés.

Si vous êtes un nouveau développeur, ma recommandation est de lire cet article complètement, puis de revenir à cette section une fois que vos appareils seront configurés.

Étapes générales pour la création manuelle dans le portail Developer :

1.  Accédez à "Certificates, Identifiers & Profiles" et sélectionnez "Profiles".
    
2.  Cliquez sur le bouton ajouter (+).
    
3.  Sélectionnez le type de profil de provisionnement à créer (par exemple, "iOS App Development", "Ad Hoc", "App Store").
    
4.  Choisissez l'App ID que vous ciblez dans la liste déroulante.
    
5.  Sélectionnez le ou les certificats à inclure dans le profil. Les profils de développement peuvent inclure plusieurs certificats de développement – vous pouvez donc inclure ici tous les certificats des membres de l'équipe. Les profils Ad Hoc et App Store incluent un seul certificat de distribution.
    
6.  Si vous créez un profil Development ou Ad Hoc, sélectionnez les appareils enregistrés à inclure.
    
7.  Donnez un nom au profil de provisionnement (ceci sert à l'identification dans le portail et dans Xcode).
    
8.  Cliquez sur "Generate" puis sur "Download" pour obtenir le fichier `.mobileprovision` ou `.provisionprofile`.
    

Vous devez rendre les profils téléchargés accessibles à Xcode. Vous pouvez souvent le faire en double-cliquant sur le fichier téléchargé ou en rafraîchissant les profils dans les paramètres de compte d'Xcode (Preferences > Accounts).

J'apprécie beaucoup la fonctionnalité "Automatically manage signing" d'Xcode car elle peut simplifier considérablement la gestion des profils. Elle crée et met à jour les profils selon les besoins. Cependant, comprendre le processus manuel est crucial pour le dépannage car, lorsque les choses tournent mal, il est plus simple de déboguer le problème avec ces connaissances.

Les profils de provisionnement deviendront invalides et nécessiteront une régénération si :

-   Les capacités de l'App ID associé sont modifiées – disons que vous avez ajouté une nouvelle capacité.
    
-   Un certificat inclus expire ou est révoqué.
    
-   Pour les profils Development/Ad Hoc, si des appareils sont ajoutés ou supprimés de la liste enregistrée d'une manière qui affecte l'ensemble d'appareils du profil, ou si la date d'expiration du profil lui-même est atteinte. Lorsque de tels changements surviennent, vous devez modifier le profil (si possible) ou le supprimer et le recréer dans le portail Developer, puis le télécharger et l'installer à nouveau. Bien que cela puisse sembler complexe, c'est assez direct une fois qu'on l'a fait quelques fois.
    

## **Gestion des appareils — Builds de développement et Ad Hoc**

Pour tester des applications sur du matériel Apple physique en dehors de TestFlight ou de l'App Store, vous devrez enregistrer les identifiants uniques d'appareils (UDID) de vos appareils de test auprès de votre compte Apple Developer. Cet enregistrement est une étape nécessaire pour créer des profils de provisionnement Development et Ad Hoc.

### Pourquoi vous devez enregistrer des appareils de test

Les profils de provisionnement Development et Ad Hoc sont spécifiquement liés à une liste d'appareils enregistrés. Une application signée avec ce profil peut être installée directement sans passer par le processus de l'App Store. Cela signifie que vous devez enregistrer les appareils sur lesquels vous avez l'intention de développer. Cela empêche les acteurs malveillants de diffuser largement des applications sans la supervision des développeurs et de l'App Store.

L'UDID d'un appareil est comme une adresse physique (pensez à l'adresse MAC). Si vous ne l'incluez pas dans le profil de provisionnement que vous avez utilisé pour signer un package d'application, celle-ci ne pourra pas être installée sur cet appareil.

Passons en revue les étapes pour le faire.

### Comment trouver l'UDID (Unique Device Identifier) de votre appareil

Un UDID est une chaîne hexadécimale unique de 40 caractères (pour les appareils plus anciens) ou une chaîne de 25 caractères (format XXXXXXXX-XXXXXXXXXXXXXXXX) qui identifie de manière unique un iPhone, iPad, Apple Watch, Apple TV, Vision Pro ou Mac spécifique.

Il existe plusieurs façons de trouver l'UDID d'un appareil :

-   **Xcode :** Connectez l'appareil à un Mac exécutant Xcode. Ouvrez Xcode et accédez à Window > Devices and Simulators. Sélectionnez l'appareil connecté dans la liste de gauche. L'UDID sera affiché sous le nom "Identifier" dans le panneau d'informations de l'appareil.
    
-   **Finder (macOS Catalina et versions ultérieures) :** Connectez l'appareil iOS ou iPadOS à un Mac. Ouvrez le Finder et sélectionnez l'appareil dans la barre latérale sous "Emplacements". L'UDID peut être affiché directement, ou il peut être nécessaire de cliquer sur la ligne de texte sous le nom de l'appareil (qui indique le modèle, le stockage et la version de l'OS) pour faire défiler les infos jusqu'à l'affichage de l'UDID.
    
-   **iTunes (anciennes versions de macOS) :** Pour les Mac exécutant macOS Mojave ou une version antérieure, connectez l'appareil et ouvrez iTunes. Sélectionnez l'icône de l'appareil lorsqu'elle apparaît. Dans l'onglet "Résumé", cliquez sur le champ "Numéro de série" ; celui-ci changera pour afficher l'UDID.
    
-   **Macs Apple Silicon :** Lors de l'enregistrement d'un Mac Apple Silicon, il est important de chercher le "Provisioning UDID", qui se trouve dans Informations système sous Matériel > UDID de provisionnement.
    
-   **Autres moyens :** Certains sites web installent un profil sur votre appareil pour obtenir l'UDID – en dernier recours absolu, vous pouvez le faire. _Mais je recommande vivement d'utiliser l'une des méthodes officielles pour éviter tout problème potentiel._
    

### Comment enregistrer des appareils dans le portail Apple Developer

La gestion des appareils s'effectue via la section "Certificates, Identifiers & Profiles" du portail Apple Developer (developer.apple.com) et nécessite généralement un rôle de Account Holder ou d'Admin.

Pour enregistrer manuellement un seul appareil :

1.  Connectez-vous au portail Apple Developer, accédez à "Certificates, Identifiers & Profiles", puis sélectionnez "Devices" dans la barre latérale.
    
2.  Cliquez sur le bouton ajouter (+) pour enregistrer un nouvel appareil.
    
3.  Sélectionnez la plateforme correcte pour l'appareil (par exemple, iOS, macOS, tvOS, watchOS).
    
4.  Saisissez un "Device Name" descriptif (c'est pour votre référence, par exemple, "iPhone 11 Pro de Sravan") et l'UDID de l'appareil obtenu à l'étape précédente.
    
5.  Cliquez sur "Continue", vérifiez les informations pour vous assurer que tout est correct, puis cliquez sur "Register".
    

Pour enregistrer plusieurs appareils, le portail permet de télécharger un fichier texte spécialement formaté (un fichier .txt ou .deviceids) contenant les noms des appareils et les UDIDs.

Si "Automatically manage signing" est activé dans Xcode, Xcode peut enregistrer automatiquement un appareil connecté lorsqu'il est sélectionné comme cible de build. C'est ainsi que j'ai géré tous mes projets et appareils personnels. D'un autre côté, le téléchargement de fichier était vraiment utile sur mon lieu de travail pour suivre tous les appareils et les ajouter d'un coup.

### Comprendre les limites d'appareils et les réinitialisations annuelles

Le Apple Developer Program impose des limites sur le nombre d'appareils pouvant être enregistrés pour les tests :

-   **Limite annuelle :** Chaque année d'adhésion, une équipe de développement peut enregistrer jusqu'à 100 appareils pour chaque famille de produits (iPhone, iPad, Apple Watch, Apple TV, Apple Vision Pro, Mac). Si vous êtes une grande équipe, cela peut potentiellement devenir un goulot d'étranglement. Lorsque nous avons rencontré ce problème, nous avons créé une nouvelle équipe de développement pour répartir la charge. Il n'y a pas d'autre moyen à ma connaissance, à part demander à Apple et faire appel.
    
-   **Désactivation d'appareils :** Bien qu'un appareil puisse être désactivé dans le portail pendant l'année d'adhésion, cela **ne libère pas son emplacement et n'augmente pas le nombre d'appareils disponibles pour cette année**. Cette partie est frustrante, mais je pense que c'est le seul moyen pour eux d'appliquer la limite de 100 appareils pour éviter que les gens n'échangent des appareils. Ils devraient vraiment proposer un moyen d'augmenter la limite. La désactivation d'un appareil invalidera cependant tous les profils de provisionnement qui l'incluent, nécessitant la régénération de ces profils.
    
-   **Réinitialisation de la liste d'appareils (début de la nouvelle année d'adhésion) :** Au début d'une nouvelle année d'adhésion, les Account Holders, Admins et App Managers ont la possibilité unique, lors de leur première connexion à "Certificates, Identifiers & Profiles", de supprimer des appareils de leur liste. Cela leur permet de "réinitialiser" leur décompte d'appareils disponibles à 100 pour chaque famille de produits. Vous pouvez choisir de supprimer des appareils spécifiques ou tous les appareils enregistrés. **C'est votre seule chance par an de supprimer complètement les appareils inutilisés et de libérer des emplacements pour de nouveaux appareils.**
    
-   **Expiration de l'adhésion :** Si une adhésion au programme développeur arrive à expiration et qu'aucun renouvellement n'est prévu, le Account Holder aura la possibilité, à partir de 30 jours avant l'expiration, de télécharger une copie de sa liste d'appareils enregistrés. Il peut également choisir de faire supprimer tous les appareils du compte immédiatement à l'expiration de l'adhésion. Si aucune action n'est entreprise, les appareils sont généralement supprimés automatiquement 180 jours après l'expiration de l'adhésion.
    

## **Possibilités : Activer les capacités et les services**

Les capacités d'application (App Capabilities ou App Services) sont des fonctionnalités fournies par Apple que nous (en tant que développeurs) pouvons intégrer dans nos applications pour étendre les fonctionnalités et offrir des expériences utilisateur plus riches. Les exemples incluent le stockage iCloud, les notifications push, Sign in with Apple, Apple Pay et l'intégration HealthKit. L'activation de ces fonctionnalités nécessite souvent une configuration explicite pour l'App ID d'une application dans le portail Apple Developer et au sein du projet Xcode.

### Pourquoi vous devriez utiliser les capacités

Tirer pleinement parti de ces capacités d'application peut distinguer votre application des autres de manière très notable. Vous pouvez utiliser l'intégration Apple Wallet si vous voulez que les utilisateurs scannent une carte de membre. Vous pouvez utiliser les suggestions de journalisation si vous voulez les inciter à écrire dans un journal. Vous pouvez utiliser le stockage iCloud pour pousser plus loin la synchronisation entre appareils.

Lorsque vous activez une capacité pour un App ID, cela entraîne l'ajout d'entitlements spécifiques au profil de provisionnement de l'application. Ces entitlements sont des permissions que le système d'exploitation vérifie au moment de l'exécution pour s'assurer que l'application est autorisée à utiliser le service demandé.

### Comment configurer les capacités pour votre App ID (Portail Apple Developer)

L'activation et la configuration des capacités sont généralement effectuées par un Account Holder ou un Admin dans le portail Apple Developer (developer.apple.com).

1.  Accédez à "Certificates, Identifiers & Profiles" et sélectionnez "Identifiers".
    
2.  Choisissez l'App ID pour lequel les capacités doivent être configurées.
    
3.  Dans les réglages de l'App ID, il y aura un onglet "Capabilities". Cochez les cases correspondant aux capacités requises par l'application.
    
4.  De nombreuses capacités nécessitent des étapes de configuration supplémentaires. Pour celles-ci, un bouton "Configure" ou "Edit" apparaîtra généralement à côté de la capacité une fois sélectionnée. Les exemples incluent :
    

-   **App Groups :** Nécessite la création ou la sélection d'un identifiant de groupe d'applications pour permettre le partage de données entre une application principale et ses extensions, ou entre différentes applications du même développeur.
    
-   **Apple Pay :** Nécessite l'association d'un ou plusieurs Merchant IDs avec l'App ID.
    
-   **iCloud :** Peut nécessiter de choisir la compatibilité de la version Xcode et de créer ou d'assigner des conteneurs iCloud pour le stockage Key-Value ou Document.
    
-   **Sign in with Apple :** Peut nécessiter de configurer l'App ID comme application principale ou de le grouper avec un App ID principal existant, et éventuellement de fournir une URL de point de terminaison pour les notifications de serveur à serveur.
    

5.  Après avoir configuré toutes les capacités sélectionnées, cliquez sur "Save". Une boîte de dialogue d'avertissement peut apparaître, nécessitant une confirmation pour finaliser les modifications.

**L'activation d'une capacité dans le portail Developer n'est qu'une partie du processus.** Vous devrez également l'ajouter et la configurer au sein de la cible de l'application dans le projet Xcode, sous l'onglet "Signing & Capabilities".

![Affichage de l'écran Signing & Capabilities dans Xcode](https://cdn.hashnode.com/res/hashnode/image/upload/v1748480139418/6a4007b3-01bd-484a-865c-8c5e728e15e0.png)

![Capture d'écran montrant le sélecteur de capacités dans Xcode](https://cdn.hashnode.com/res/hashnode/image/upload/v1748480260906/e0dcec33-24ce-448b-91be-b79f5638e6fc.png)

![Capture d'écran de Xcode montrant trois capacités.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748480340624/ac56896a-0fb0-4cb0-a3fc-c894a255794a.png)

1.  Accédez aux paramètres du projet et sélectionnez "Signing & Capabilities".
    
2.  Appuyez sur le bouton "+ Capability" pour sélectionner la capacité.
    
3.  Une fois sélectionnée, la capacité devrait apparaître dans le volet. Selon la capacité, vous pourriez vouloir la configurer davantage.
    

Cette étape dans Xcode intègre les frameworks nécessaires, ajoute les fichiers d'entitlements au projet et ajuste les paramètres de build.

### Comment l'activation des capacités affecte vos profils de provisionnement

Les modifications apportées aux capacités activées d'un App ID ont un impact direct et significatif sur ses profils de provisionnement associés.

-   **Invalidation :** Lorsqu'une capacité est activée, désactivée ou que sa configuration est modifiée pour un App ID, **tous les profils de provisionnement existants qui utilisent cet App ID deviennent immédiatement invalides**.
    
-   **Régénération requise :** Ces profils de provisionnement invalidés doivent être régénérés (soit en les modifiant et en les réenregistrant dans le portail Developer, soit en laissant la signature automatique d'Xcode s'en charger). Les profils régénérés incluront alors l'ensemble mis à jour d'entitlements correspondant aux capacités nouvellement configurées.
    
-   **Impact multiplateforme :** L'activation d'une capacité pour un App ID utilisé sur plusieurs plateformes (par exemple, une application iOS et son compagnon watchOS) affectera les profils de provisionnement pour toutes les plateformes éligibles utilisant cet App ID.
    

C'est un point à garder à l'esprit, surtout en ce qui concerne les profils de distribution car ceux-ci sont généralement gérés manuellement.

## **Conclusion**

Bien que tout cela puisse paraître intimidant, le processus automatique d'Apple devrait gérer la majeure partie du travail. Cependant, je recommande vivement d'apprendre comment tout fonctionne afin de pouvoir déboguer en cas de problème. Je recommande également d'utiliser des profils créés manuellement pour la distribution.

Bien que la signature et la gestion des certificats ne soient pas la partie la plus excitante du processus de développement d'applications, c'est une compétence nécessaire. Dans mon prochain article, je passerai en revue la distribution d'une application de A à Z (ce qui inclut ces processus et d'autres restrictions).

Vous pouvez me suivre sur [Sravan Karuturi][11] pour mes autres publications.

[1]: #heading-app-ids-bundle-ids-l-identite-de-votre-application
[2]: #heading-comprendre-la-distribution-plongee-au-coeur-des-certificats
[3]: #heading-le-pont-entre-tout-les-profils-de-provisionnement
[4]: #heading-gestion-des-appareils-builds-de-developpement-et-ad-hoc
[5]: #heading-possibilites-activer-les-capacites-et-les-services
[6]: #heading-conclusion
[7]: http://com.mycompany.app
[8]: http://com.foo.bar
[9]: http://com.foo
[10]: https://developer.apple.com/documentation/appstoreconnectapi
[11]: https://hashnode.com/@sravankaruturi
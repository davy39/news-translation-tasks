---
title: Comment configurer l'authentification dans vos applications avec Supabase Auth
subtitle: ''
author: Fatuma Abdullahi
co_authors: []
series: null
date: '2024-01-29T10:53:38.000Z'
originalURL: https://freecodecamp.org/news/set-up-authentication-in-apps-with-supabase
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Group-3--9-.png
tags:
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: supabase
  slug: supabase
seo_title: Comment configurer l'authentification dans vos applications avec Supabase
  Auth
seo_desc: "In this article, you'll learn the basic key concepts that'll help you grasp\
  \ how authentication and authorization work. \nYou'll start by learning what authentication\
  \ and authorization are, and then learn how to implement authentication in your\
  \ applica..."
---

Dans cet article, vous apprendrez les concepts clés de base qui vous aideront à comprendre comment fonctionnent l'authentification et l'autorisation. 

Vous commencerez par apprendre ce que sont l'authentification et l'autorisation, puis vous apprendrez comment implémenter l'authentification dans vos applications en utilisant Supabase auth.

## Table des matières

<ul>
    <li>
        <a href="#prerequis">
        	Prérequis
        </a>
    </li>
    <li>
        <a href="#quest-ce-que-lauthentification-et-lautorisation">
        	Qu'est-ce que l'authentification et l'autorisation ?
        </a>
    </li>
    <li>
        <a href="#comment-fonctionne-lauthentification">
            Comment fonctionne l'authentification ?
        </a>
    </li>
    <li>
        <a href="#gestion-des-sessions-avec-les-jetons-secrets-et-cookies">
            Gestion des sessions avec les jetons, secrets et cookies
        </a>
    </li>
    <li>
        <a href="#types-de-facteurs-dauthentification">
            Types de facteurs d'authentification
        </a>
    </li>
    <li>
        <a href="#strategies-dauthentification-courantes">
            Stratégies d'authentification courantes
        </a>
        <ul>
            <li>
                <a href="#authentification-basee-sur-mot-de-passe">
                     Authentification basée sur mot de passe
                </a>
            </li>
            <li>
                <a href="#authentification-sans-mot-de-passe">
                     Authentification sans mot de passe
                </a>
            </li>
            <li>
                <a href="#authentification-a-deux-facteurs-2fa">
                     Authentification à deux facteurs (2FA)
                </a>
            </li>
            <li>
                <a href="#authentification-multifacteur-mfa">
                     Authentification multifacteur (MFA)
                </a>
            </li>
              <li>
                <a href="#oauth-20-et-authentification-sociale">
                    OAuth 2.0 et authentification sociale
                </a>
            </li>
              <li>
                <a href="#sso-et-saml">
                    SSO et SAML
                </a>
            </li>
        </ul>
    </li>
    <li>
        <a href="#authentification-et-securite">
            Authentification et sécurité
        </a>
    </li>
    <li>
        <a href="#supabase-et-le-service-dauthentification-supabase">
            Supabase et le service d'authentification Supabase
        </a>
    </li>
    <li>
        <a href="#comment-utiliser-supabase-auth">
            Comment utiliser Supabase Auth
        </a>
        <ul>
            <li>
                <a href="#lapi">
                    L'API
                </a>
            </li>
            <li>
                <a href="#sdks">
                    SDKs
                </a>
            </li>
            <li>
                <a href="#aides-ui-dauthentification">
                    Aides UI d'authentification
                </a>
            </li>
        </ul>
    
    </li>
     <li>
         <a href="#resume">
             Résumé
         </a>
    </li>
    <li>
        <a href="#ressources">
            Ressources
        </a>
    </li>
</ul>

## Prérequis

Pour tirer le meilleur parti de cet article, vous aurez besoin des éléments suivants :

* Connaissances de base en programmation.
* [Un projet Supabase](https://supabase.com/) pour suivre.
* Un éditeur de texte pour essayer les extraits de code.

## Qu'est-ce que l'authentification et l'autorisation ?

En termes simples, l'authentification est le processus par lequel un utilisateur s'identifie auprès d'un système et le système confirme que l'utilisateur est bien celui qu'il prétend être. 
  
D'autre part, l'autorisation est le processus par lequel le système détermine quelles parties de l'application l'utilisateur est autorisé à consulter ou avec lesquelles il peut interagir, et quelles parties de l'application l'utilisateur n'est pas autorisé à consulter.

## Comment fonctionne l'authentification ?

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-135.png)
_Un organigramme décrivant le processus d'authentification de l'utilisateur_

La première fois qu'un utilisateur interagit avec un système, il lui sera demandé de s'inscrire. Typiquement, l'utilisateur fournira une information et un secret qui ne doit être connu que de lui et du système. C'est la partie inscription du processus d'authentification.

La prochaine fois que l'utilisateur interagira avec le même système, il devra fournir l'information d'identification ainsi que le secret précédemment défini afin de vérifier son identité. 

L'appareil à partir duquel l'utilisateur initie l'interaction est le client et le système est le serveur. Une fois que le système a vérifié l'utilisateur, il envoie certaines informations au client concernant l'utilisateur. 

Parce que ce processus prend du temps et nécessite une action de l'utilisateur, le client stockera ces informations et les renverra au système chaque fois que l'utilisateur aura besoin d'accéder au système. Cela réduit les frictions en ne nécessitant pas que l'utilisateur s'authentifie activement à chaque fois. Cela crée une session utilisateur.

## Gestion des sessions avec les jetons, secrets et cookies

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-136.png)
_Un diagramme de séquence montrant la gestion des sessions dans une architecture client-serveur_

Le serveur peut transmettre les informations de l'utilisateur au client de deux manières - via des jetons ou des identifiants de session.

Dans le cas des jetons, le serveur génère un jeton signé et le transmet au client. Ce jeton est généralement un JWT et peut contenir des informations concernant l'utilisateur. Le client stockera ce jeton et le renverra au serveur chaque fois que l'utilisateur fera une requête. 

Le serveur est capable de vérifier l'intégrité du jeton car il l'a signé. Cela est appelé authentification sans état car le jeton est auto-suffisant et le serveur n'a pas besoin de stocker les données de session dans une base de données ou un cache. 

Dans le cas des cookies, le serveur crée un enregistrement de la session utilisateur dans une base de données ou un cache qui inclura un identifiant de session. Le serveur envoie cet identifiant de session au client.

Le client stocke cet identifiant de session dans un cookie et le renvoie au serveur chaque fois que l'utilisateur fait une requête. L'identifiant de session est une chaîne aléatoire qui agit comme un pointeur vers l'enregistrement utilisateur réel dans la base de données. 

Lorsque le serveur reçoit ce cookie, il fait correspondre l'identifiant de session qu'il contient à ses enregistrements de session, puis fait correspondre cet enregistrement aux données utilisateur dans la base de données. Cela est appelé authentification avec état car une recherche dans la base de données est nécessaire.

## Types de facteurs d'authentification

Un facteur d'authentification fait référence à un type de justificatif d'identité qui peut être utilisé pour vérifier l'identité d'un utilisateur. Il existe 3 facteurs typiquement utilisés dans le processus d'authentification, et ils sont :

1. Quelque chose que vous savez : un exemple est un mot de passe.
2. Quelque chose que vous avez : un exemple est un jeton envoyé à votre téléphone.
3. Quelque chose que vous êtes : un exemple est votre empreinte digitale.

## Stratégies d'authentification courantes

Les stratégies d'authentification font référence aux processus utilisés pour vérifier un utilisateur. Différents types de stratégies d'authentification incluent :

### Authentification basée sur mot de passe

Cela fait référence à la manière traditionnelle pour les utilisateurs de s'identifier en fournissant un secret basé sur du texte qui est défini par l'utilisateur. Typiquement, le système gère l'ensemble du processus sur ses serveurs et est responsable de la sécurité et de la fiabilité.

### Authentification sans mot de passe

Dans cette approche, le système vérifie l'identité de l'utilisateur sans nécessiter de mots de passe définis par l'utilisateur. Le système générera, à la place, un mot de passe à usage unique (OTP) et l'enverra à l'utilisateur. Cet OTP est ensuite utilisé à la place d'un mot de passe pour accéder au système. Des exemples incluent les liens magiques, où le système envoie un code à l'email de l'utilisateur.

### Authentification à deux facteurs (2FA)

Le système tente de vérifier que l'utilisateur est bien celui qu'il prétend être en exigeant une information supplémentaire après que l'authentification principale a été validée. 

Cela peut être un OTP envoyé à l'utilisateur par email ou SMS, ou cela peut être en exigeant les informations biométriques de l'utilisateur avant que le système n'accorde l'accès.

### Authentification multifacteur (MFA)

Cela est similaire à la 2FA, sauf que le système utilisera plus d'une méthode supplémentaire pour vérifier l'identité de l'utilisateur. Les méthodes ou facteurs supplémentaires utilisés dans la MFA et la 2FA sont généralement externes au système, comme un SMS nécessitant un téléphone.

### OAuth 2.0 et authentification sociale

OAuth est un cadre d'autorisation qui permet aux clients d'accéder à des informations à partir d'un serveur externe au nom de l'utilisateur. Le serveur externe demande à l'utilisateur la permission de partager les ressources demandées avec le client. 

Après que l'utilisateur a autorisé l'action, le serveur externe émet un jeton d'accès au client. 

Le client donne ensuite ce jeton d'accès au serveur d'origine, qui vérifie la validité du jeton et gère l'accès aux ressources demandées. OAuth 2.0 est la dernière version d'OAuth et est le cadre le plus largement utilisé. 

OAuth 2.0 étend le support pour les systèmes non basés sur navigateur. L'authentification sociale est basée sur OAuth 2.0 mais dans ce cas, le serveur externe vers lequel le client redirige l'utilisateur est généralement une plateforme de médias sociaux. C'est le type de processus d'authentification effectué chaque fois que vous voyez un bouton "Continuer avec Twitter/X" sur une page d'authentification. 

### SSO et SAML

SAML signifie Security Assertion Markup Language. C'est un standard pour transmettre des informations d'authentification et d'autorisation entre systèmes. Un système agit comme le système demandeur ou le fournisseur de services (SP) et l'autre système détient les informations demandées ou agit comme le fournisseur d'identité (IdP). 

En recevant cette demande, le fournisseur d'identité générera des déclarations au format SAML contenant certaines informations utilisateur. Le fournisseur de services utilise ensuite ces informations pour décider comment gérer l'utilisateur en relation avec ses ressources protégées. 

SSO fait référence à Single Sign On. C'est une stratégie d'authentification qui permet aux utilisateurs de se connecter via un système/application qui leur permet ensuite d'accéder à plusieurs applications au sein du même réseau. 

Cela améliore l'expérience utilisateur en ne nécessitant pas que l'utilisateur se connecte à différentes applications liées. Un exemple de cela est Google Workspace. Vous n'avez pas besoin de vous connecter à Docs séparément si vous êtes déjà connecté à votre compte Gmail. Le SSO est facilité par SAML car SAML fournit un mécanisme d'authentification standard et permet à différents systèmes de se faire confiance mutuellement. 

## Authentification et sécurité

L'authentification implique la manipulation, le transfert et le stockage d'informations sensibles de l'utilisateur en relation avec les ressources protégées du serveur. Cela fait de la sécurité et des bonnes pratiques un aspect important d'un système d'authentification.

Il existe certaines étapes de base que vous pouvez suivre pour augmenter considérablement la sécurité de vos systèmes d'authentification. Celles-ci incluent :

* Imposer des mots de passe plus forts.
* Exiger que l'utilisateur enregistre un facteur supplémentaire pour activer la 2FA.
* Chiffrer les données sensibles lors de leur transfert via HTTPS.
* Stocker les mots de passe de manière chiffrée.
* Utiliser des cadres d'authentification standard comme OAuth 2.0.

Il existe certaines conformités que votre système doit prendre en compte lors de la manipulation de données sensibles de l'utilisateur au-delà des informations d'authentification spécifiques. Cela est d'autant plus vrai si vous opérez dans certains pays ou gérez des applications d'entreprise. Ces conformités incluent :

* **RGPD** : Cette conformité impose des normes en matière de traitement des données, y compris la confidentialité et l'intégrité.
* **HIPAA** : Cette conformité s'applique aux données médicales. Elle exige des niveaux élevés d'intégrité.
* **SOC** : C'est un cadre plus généralement requis pour les technologies cloud. Il est basé sur l'American Institute of CPAs et couvre les aspects de la confidentialité, de la sécurité, de la disponibilité, de l'intégrité et de la confidentialité.

En gardant tout cela à l'esprit, vous constaterez qu'il est souvent plus facile d'utiliser des services d'authentification dédiés pour vos applications plutôt que de développer votre propre système d'authentification.

Il existe de nombreuses options pour cela, y compris des services d'authentification dédiés tels que Clerk et Auth0, et des services Backend-as-a-Service tels que Supabase et Firebase. Dans ce cas, examinons l'offre d'authentification de Supabase.

## Supabase et le service d'authentification Supabase

Supabase est une plateforme Backend as a Service (BaaS) open source qui rend le développement d'un backend pour vos applications très facile et rapide. Elle est basée sur des technologies open source et soutient activement l'écosystème open source. 

Supabase offre des services courants que la plupart des applications backend nécessiteront. Ces services sont :

* Base de données : Il s'agit d'une base de données Postgres entièrement fonctionnelle.
* Authentification : Il s'agit d'un service d'authentification prêt pour l'entreprise basé sur un fork du serveur goTrue.
* Temps réel : Il s'agit d'une API qui ajoute la capacité d'utiliser des fonctionnalités en temps réel dans vos applications.
* Stockage : Il s'agit d'un service de stockage qui est un wrapper s3.
* Fonctions Edge : Il s'agit de fonctions serverless qui s'exécutent sur le edge. Alimentées par le runtime Deno.
* Vecteur : Il s'agit d'une base de données vectorielle qui facilite le travail avec les embeddings dans vos applications d'IA.

Supabase est conforme à SOC2, HIPAA et RGPD, peut être auto-hébergé et est open source. De plus, leur service d'authentification expose de nombreuses stratégies, vous donnant un contrôle total sur vos données et peut être utilisé indépendamment de leurs autres offres. Cela et leur API auto-documentée en font un très bon choix pour vos applications. 

### Comment utiliser Supabase Auth

La première étape consiste à configurer les paramètres d'authentification de votre [projet Supabase](https://app.supabase.com/). Vous pouvez activer les méthodes d'authentification exactes que vous souhaitez utiliser via les paramètres. Il existe trois façons de commencer à utiliser Supabase auth dans votre projet :

#### L'API

Vous pouvez utiliser directement le service d'authentification dans vos applications en appelant le point de terminaison d'authentification et en lui passant les informations de l'utilisateur. Vous pouvez également obtenir, mettre à jour et supprimer vos utilisateurs.   
  
L'API est automatiquement disponible lorsque vous créez un projet via la console Supabase et peut être appelée comme suit : 

```javascript
//Cela retournera un objet contenant un jeton d'accès, les données de l'utilisateur nouvellement créé et d'autres métadonnées
const res = await fetch("https://<your-project-ref>/auth/v1/signup", {
  method: "POST",
  headers: {
    authorization: "Bearer YOUR_SUPABASE_KEY",
    "content-type": "application/json",
  },
  body: JSON.stringify({
    email: "user-email",
    password: "user-password",
  }),
});

```

#### SDKs

Supabase propose quelques SDK (kits de développement logiciel) dans différents langages de programmation destinés à rendre l'interaction avec votre projet Supabase simple. Les langages officiellement supportés incluent Dart et JavaScript, avec Python et d'autres ayant un fort support communautaire. 

La procédure pour commencer implique d'ajouter le SDK en tant que dépendance, puis de connecter votre application à votre projet Supabase. 

Dans le cas du SDK JavaScript, cela ressemblerait à ceci :

```javascript
//Installer via npm:
npm install @supabase/supabase-js

// ou ajouter des liens cdn : 
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
```

```javascript
//Puis initialiser 
Supabaseimport { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://<your-project-ref>.supabase.co'
const supabaseKey = process.env.SUPABASE_ANON_KEY
const supabase = createClient(supabaseUrl, supabaseKey)
```

Ensuite, vous pouvez accéder aux méthodes d'authentification sous l'espace de noms auth comme suit :

```javascript
const { data, error } = await supabase.auth.signUp({
  email: 'user email',
  password: 'user password',
})
```

#### Aides UI d'authentification

Supabase fournit des bibliothèques d'assistance pour rendre l'authentification utilisant leur service encore plus facile. Ces bibliothèques fournissent des écrans de connexion personnalisables qui supportent les liens magiques, l'authentification basée sur mot de passe et les stratégies de connexion sociale. 

Actuellement, les bibliothèques sont disponibles pour JavaScript et Flutter. Supabase fournit également un package SSR (Server Side Rendering) séparé pour les applications qui utilisent des frameworks côté serveur et nécessitent un jeton d'accès Supabase disponible pour elles.

Pour commencer à utiliser React Auth UI, par exemple, vous devez d'abord installer les dépendances comme montré ci-dessous :

```bash
npm install @supabase/supabase-js @supabase/auth-ui-react 
@supabase/auth-ui-shared
```

Ensuite, vous pouvez commencer à utiliser la bibliothèque après avoir initialisé Supabase comme dans l'exemple SDK ci-dessus. Voici un exemple de code qui montre comment utiliser la bibliothèque d'authentification UI dans une application React :

```javascript
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Auth } from "@supabase/auth-ui-react";
import { ThemeSupa } from "@supabase/auth-ui-shared";
import { supa } from "../constants";

const AuthUi = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const {
      data: { subscription },
    } = supa.auth.onAuthStateChange((event) => {
      if (event === "SIGNED_IN") {
        navigate("/authenticated");
      }
    });

    return () => subscription.unsubscribe();
  }, [navigate]);

  return (
    <Auth
      supabaseClient={supa}
      providers={["google", "github", "apple", "discord"]}
      // contrôle si seuls les fournisseurs sociaux doivent être affichés
      // onlyThirdPartyProviders
      redirectTo="http://localhost:3000/authenticated"
      // vient avec des thèmes préconfigurés, peut ajouter des thèmes personnalisés
      appearance={{ theme: ThemeSupa }}
      // contrôle comment afficher les icônes des fournisseurs sociaux
      socialLayout="horizontal"
    />
  );
};

export default AuthUi;

```

Cela afficherait le formulaire suivant à l'écran : 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-26-at-18.43.39.png)

## Résumé

L'authentification est le processus par lequel l'utilisateur s'identifie et le serveur vérifie cette identité, tandis que l'autorisation est le système qui détermine à quelles ressources l'utilisateur doit avoir accès et limite l'utilisateur en conséquence.

Après que le serveur a authentifié l'utilisateur, il transmettra les informations de l'utilisateur sous la forme d'un jeton ou d'un identifiant de session dans un cookie. 

Les informations seront échangées entre le client et le serveur chaque fois que l'utilisateur aura besoin d'un certain accès jusqu'à ce qu'elles expire ou que l'utilisateur termine le cycle en se déconnectant ou en supprimant son compte.

Ce processus de vérification de l'utilisateur se produit en employant certains facteurs d'authentification. Par exemple, un système peut ne nécessiter qu'un mot de passe tandis qu'un autre nécessite un mot de passe et un code envoyé au numéro de téléphone de l'utilisateur.

Votre système d'authentification peut permettre plusieurs stratégies d'authentification utilisant l'un des trois facteurs d'authentification.

Supabase est une excellente option si vous choisissez de ne pas gérer votre propre authentification.

Supabase auth peut être accessible via l'API, les SDKs et les bibliothèques d'authentification. Supabase maintient un package SSR pour les frameworks côté serveur.

## Ressources

Les ressources suivantes sont utiles pour des lectures complémentaires. Elles offrent plus d'explications sur l'authentification et l'autorisation, ainsi que la documentation spécifique à Supabase.

* [Une explication approfondie d'OAuth](https://www.upguard.com/blog/oauth#:~:text=OAuth%201.0%20has%20a%20consumer,resource%20server%2C%20and%20resource%20owner.)
* [Sécurité Supabase](https://supabase.com/security)
* [Documentation Supabase sur l'authentification](https://supabase.com/docs/guides/auth)
* [Page de documentation Auth UI](https://supabase.com/docs/guides/auth/auth-helpers/auth-ui)
* [Supabase sur les aides d'authentification et SSR](https://supabase.com/docs/guides/auth/auth-helpers)
* [Sur SSO, SAML et l'authentification d'entreprise](https://supabase.com/docs/guides/auth/sso/auth-sso-saml)
---
title: Comment utiliser Cognito pour les applications Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-13T22:06:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-cognito-for-web-applications
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Cognito-Title-Picture.jpg
tags:
- name: authentication
  slug: authentication
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: Comment utiliser Cognito pour les applications Web
seo_desc: "By Max Rohde\nAmazon Cognito is a cloud-based, serverless solution for\
  \ identity and access management. It provides capabilities similar to Auth0 and\
  \ Okta. \nCognito is part of the AWS suite of services so you can easily incorporate\
  \ it if you are alread..."
---

Par Max Rohde

[Amazon Cognito](https://aws.amazon.com/cognito/) est une solution basée sur le cloud, sans serveur, pour la gestion des identités et des accès. Il offre des capacités similaires à [Auth0](https://aws.amazon.com/cognito/) et [Okta](https://aws.amazon.com/cognito/). 

Cognito fait partie de la suite de services AWS, vous pouvez donc facilement l'intégrer si vous utilisez déjà AWS dans d'autres parties de votre stack.

Cependant, la gestion des identités et des accès est souvent délicate à mettre en œuvre, et Amazon Cognito ne fait pas exception à cet égard. Cet article fournit un guide pour débutants afin de mettre en place une configuration de base avec Cognito et de la faire fonctionner. Plus précisément, il couvre :

* 440 Un aperçu d'une application exemple
* 4da Une explication des concepts clés que nous devons comprendre
* 917 Comment inscrire et authentifier les utilisateurs dans une application Web
* 6aa Comment sécuriser les endpoints dans une API côté serveur
* 6e0 La gestion des utilisateurs

Ce tutoriel se concentrera strictement sur l'authentification : c'est-à-dire comment valider qu'un utilisateur est bien celui qu'il prétend être. Il ne couvre pas l'autorisation, bien que Cognito puisse également nous aider à cet égard.

Voici un résumé rapide de [l'authentification vs l'autorisation](https://www.freecodecamp.org/news/whats-the-difference-between-authentication-and-authorisation/) si vous souhaitez en savoir plus.

## Aperçu de la solution

Avant de vous lancer dans la compréhension de la mise en œuvre de l'authentification pour votre application sans serveur, je vais vous fournir un bref aperçu de la solution que vous serez en mesure de développer en utilisant les concepts et le code discutés dans cet article.

L'application est déployée en tant que [démo en direct](https://cognito-react-nodejs.examples.dev.goldstack.party/). Vous êtes invité à vous y rendre et à créer un compte.

Tout le code source de cet exemple est également disponible sur GitHub pour référence : [cognito-react-nodejs-example](https://github.com/goldstack/cognito-react-nodejs-example).

### Interface utilisateur React simple

Nous aurons une interface utilisateur simple en React fournissant des fonctionnalités d'authentification de base.

![Capture d'écran de l'interface utilisateur React montrant des boutons de connexion et d'inscription](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221226160435.png)

### Inscription

En cliquant sur le bouton _S'inscrire_ dans l'interface utilisateur (UI), l'utilisateur sera redirigé vers une interface utilisateur fournie par Amazon Cognito qui permet à l'utilisateur de s'inscrire avec une adresse e-mail et un mot de passe :

![Capture d'écran montrant un formulaire d'inscription avec un champ pour l'e-mail et le mot de passe](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221226160559.png)

Après avoir fourni une adresse e-mail et un mot de passe, l'utilisateur recevra un e-mail avec un code de confirmation qui doit être saisi dans l'interface utilisateur d'inscription pour terminer le processus d'inscription.

![Capture d'écran d'un e-mail montrant un code de vérification à six chiffres](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221226160714.png)

### Connexion

Après une inscription réussie, l'utilisateur est redirigé vers l'application d'origine et connecté automatiquement :

![Capture d'écran de l'interface utilisateur après la connexion qui affiche l'adresse e-mail de l'utilisateur](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221226160856.png)

Pour les utilisateurs qui ont déjà un compte, cliquer sur le bouton _Se connecter_ les redirigera vers une interface utilisateur pour se connecter.

### Authentification côté serveur

Le projet exemple utilise le rendu côté serveur. Le serveur authentifie l'utilisateur, et après une authentification réussie, le serveur rend : `Bonjour [email]` dans la page HTML envoyée au client.

![Capture d'écran d'une partie de la page qui est rendue par le serveur](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221226161113.png)

### Déconnexion

Enfin, cliquer sur le bouton _Déconnexion_ dans l'interface utilisateur déconnectera l'utilisateur et le redirigera vers l'écran de connexion :

![Capture d'écran du formulaire de connexion qui est affiché après la déconnexion](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221226161215.png)

Bien que les fonctionnalités de ce projet exemple semblent relativement simples, il y a une complexité à la fois théorique et technologique à gérer pour faire fonctionner tout cela.

Cependant, une fois que vous aurez compris les concepts et les technologies discutés dans cet article, vous serez en mesure de construire une solution extrêmement peu coûteuse, évolutive et sécurisée pour la gestion des utilisateurs.

## Concepts clés

Pour faire fonctionner un morceau de code, il suffit souvent de faire quelques recherches rapides sur Google et de copier des morceaux de code ici et là. Ce n'est pas conseillé pour l'authentification.

![Mème de codage par copier-coller](https://www.freecodecamp.org/news/content/images/2023/01/cyzbsh8lh3t21.jpg)

Vous avez besoin d'une base dans un certain nombre de concepts pour développer une solution. Principalement, vous devez apprendre un peu sur [OAuth 2.0](https://dev.to/afsharm/oauth-2-and-aspnet-49mm) et Amazon Cognito, que je couvrirai dans les sections suivantes.

### Qu'est-ce que OAuth 2.0 ?

OAuth 2.0 est une norme Internet (voir [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749)). Comme d'autres normes telles que HTTP ou SMTP, cette norme est implémentée par de nombreuses applications, frameworks, services et serveurs.

Les services et serveurs populaires implémentant la norme OAuth 2.0 sont :

* [Auth0](https://auth0.com/)
* [Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/auth-oauth2)
* [Amazon Cognito](https://aws.amazon.com/cognito/)

OAuth 2.0 vise à fournir à la fois sécurité et commodité pour les développeurs. L'une de ses caractéristiques les plus attrayantes est qu'elle permet aux propriétaires d'applications d'authentifier les utilisateurs sans avoir besoin de stocker et de gérer les mots de passe des utilisateurs.

![Mème : On ne peut pas voler les mots de passe si on ne les a pas](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221216063953.png)

### Authentification naïve (Ne faites pas cela)

Commençons d'abord par une implémentation naïve de l'authentification des utilisateurs :

![Implémentation naïve de l'authentification](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221216071056.png)

Dans cette implémentation, l'utilisateur entre le nom d'utilisateur et le mot de passe dans le navigateur. Nous envoyons ensuite le nom d'utilisateur et le mot de passe au serveur, qui vérifie les informations d'identification par rapport à celles stockées dans une base de données.

Si les informations d'identification sont correctes, le serveur émettra un identifiant de session, que le client peut inclure avec les futures requêtes sans avoir besoin de fournir à nouveau le nom d'utilisateur et le mot de passe.

Cette implémentation nous oblige à stocker les mots de passe (ou le [hachage des mots de passe](https://medium.com/codex/how-to-store-user-passwords-in-a-database-1237c37bc52) dans notre base de données). Cela peut facilement entraîner de graves problèmes de sécurité. _Ne faites pas cela sauf si vous y êtes absolument obligé._

### Flux d'authentification OAuth

OAuth 2.0 nous offre une meilleure façon d'authentifier les utilisateurs. OAuth 2.0 est une norme extensive, et elle offre plusieurs flux d'authentification différents pour authentifier les utilisateurs.

Je ne décrirai ici qu'un seul flux possible - celui que nous implémenterons plus tard dans cet article.

Ce flux se compose des étapes suivantes, chacune décrite plus en détail ci-dessous :

![Étapes 1-3 du flux (voir ci-dessous)](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221216071923.png)

![Étapes 4-5 du flux](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221216073609.png)

#### Étape 1 : Redirection vers l'interface utilisateur d'autorisation

Plutôt que de faire un appel API depuis notre application avec le nom d'utilisateur et le mot de passe, nous redirigeons l'utilisateur de notre application Web vers une application Web hébergée par notre serveur d'autorisation.

Ainsi, par exemple, si votre application est hébergée à l'URL `https://monapplicationgeniale.com`, vous redirigez l'utilisateur vers `https://auth.monapplicationgeniale.com` ou `https://auth.fourniparcloud.com`.

#### Étape 2 : Connexion avec le serveur d'autorisation

L'utilisateur fournit ensuite son nom d'utilisateur et son mot de passe sur la page vers laquelle il est redirigé, et le serveur d'autorisation valide les informations d'identification fournies. Vous n'êtes pas limité par de simples informations d'identification de nom d'utilisateur et de mot de passe ici. Les serveurs d'autorisation peuvent implémenter une authentification à deux facteurs et/ou d'autres mécanismes.

L'application Web hébergée du serveur d'autorisation peut également stocker des cookies pour les utilisateurs déjà connus. Ainsi, si un client a été authentifié auparavant, le serveur d'autorisation peut ne pas nécessiter que l'utilisateur ressaisisse ses informations d'identification, mais valider plutôt les informations stockées sur le client.

#### Étape 3 : Rappel vers votre application

Une fois l'utilisateur authentifié avec succès, l'application Web du serveur d'autorisation redirige l'utilisateur vers votre application. L'URL utilisée pour "rappeler" votre application contient un [_code d'autorisation_](https://oauth.net/2/grant-types/authorization-code/). Par exemple, l'URL vers laquelle l'utilisateur est redirigé peut ressembler à :

```
https://monapplicationgeniale.com?code=xxxxxxxxxxx

```

#### Étape 4 : Échange de code contre des jetons

L'application peut ensuite appeler l'API du serveur d'autorisation pour échanger ce code contre un ensemble de jetons.

Vous pouvez soit appeler l'API du serveur d'autorisation directement depuis votre application Web, soit envoyer le code à votre serveur et faire en sorte que votre serveur appelle l'API du serveur d'autorisation. Cette dernière option garantirait que le navigateur Web de l'utilisateur n'aurait jamais connaissance des jetons générés. Cependant, cela nécessite la mise en œuvre d'une certaine forme de gestion de session pour votre serveur.

Les jetons que vous obtenez en échange du code sont :

* _Jeton d'identité_ : Le [jeton d'identité](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-id-token.html) contient des informations sur l'identité d'un utilisateur, telles que _nom_, _adresse e-mail_ ou _numéro de téléphone_.
* _Jeton d'accès_ : Le [jeton d'accès](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html) contient des informations sur les ressources auxquelles l'utilisateur authentifié doit avoir accès.
* _Jeton de rafraîchissement_ : Le [jeton de rafraîchissement](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-refresh-token.html) peut être utilisé pour demander un nouvel ensemble de jetons au serveur d'autorisation.

Tous ces jetons sont définis comme des [JSON Web Tokens](https://tools.ietf.org/html/rfc7519), également connus sous le nom de JWT.

Le _jeton d'identité_ et le _jeton d'accès_ fonctionnent de manière assez géniale. Il est très facile pour toute application de les analyser et d'extraire les informations qu'ils fournissent, par exemple pour obtenir l'adresse e-mail d'un utilisateur à partir du _jeton d'identité_.

#### Étape 5 : Vérification des jetons

Cependant, vous ne devriez pas simplement lire les informations de ces jetons et faire confiance aux informations qu'ils fournissent. Au lieu de cela, vous devriez [_vérifier_](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html) les jetons d'abord.

Vous vérifiez les jetons en téléchargeant une clé publique fournie par le serveur d'autorisation, fournie dans un ensemble de clés Web JSON (JWKS). Habituellement, celles-ci sont fournies dans une URL telle que la suivante :

```
https://auth.votreapp.com/[...]/.well-known/jwks.json

```

Après avoir téléchargé la clé publique, vous pouvez vérifier les jetons avec cette clé. Il existe de nombreuses bibliothèques disponibles pour cela, voir cette liste maintenue par [OpenID](https://openid.net/developers/jwt/).

Après avoir vérifié les jetons, vous pouvez faire confiance aux informations que les jetons contiennent et les utiliser dans la logique de votre application.

### Flux d'authentification OAuth : Quelques renforcements de sécurité

OAuth 2.0 est une norme extensive, et elle définit un certain nombre de fonctionnalités optionnelles qui aident contre les vulnérabilités courantes.

Une vulnérabilité courante est la soi-disant [interception de redirection](https://advancedweb.hu/how-to-secure-the-cognito-login-flow-with-a-state-nonce-and-pkce/). Nous pouvons nous protéger contre cela en utilisant [PKCE (Proof Key for Code Exchange)](https://oauth.net/2/pkce/).

PKCE fonctionne en incluant un _défi de code_ lors de la redirection initiale de l'utilisateur vers l'application Web du serveur d'autorisation. Pour cela, vous générez un _vérificateur de code_ (une séquence aléatoire de caractères). Ensuite, vous générez un hachage en utilisant SHA-256. Vous incluez le hachage dans l'URL vers laquelle vous redirigez l'utilisateur :

```
https://auth.votreapp.com/loginui?...&code_challenge=[hachage du vérificateur de code]

```

Vous devez stocker le _vérificateur de code_ sur le client, par exemple dans le stockage local du navigateur.

Lorsque vous échangez le _code d'autorisation_ fourni dans l'URL de rappel vers votre application Web contre des jetons, vous incluez le _vérificateur de code_ dans la requête.

Le serveur d'autorisation ne délivrera les jetons que lorsque le _vérificateur de code_ fourni correspondra au _défi de code_ que vous avez fourni avec la requête initiale.

## Concepts de Cognito

Maintenant que vous connaissez quelques bases d'OAuth, il est temps de jeter un coup d'œil à la technologie spécifique utilisée pour le serveur d'authentification : [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html).

![Mème : Vraiment... ce n'est pas si compliqué](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221216083113.png)

Je ne couvrirai pas tous les aspects de Cognito ici - je me concentrerai uniquement sur ce qui est nécessaire pour l'application exemple.

Plus précisément, je couvrirai :

* Les groupes d'utilisateurs
* Les clients d'application
* L'interface utilisateur hébergée
* Les endpoints

Je vous montrerai également comment configurer chacun de ces éléments en utilisant Terraform. Dans cette section, je ferai référence au code source Terraform d'un projet de modèle sur GitHub [cognito-nodejs-template](https://github.com/goldstack/cognito-nodejs-template).

Ce projet de modèle est régulièrement mis à jour avec des correctifs de sécurité et vous pouvez facilement le cloner pour démarrer votre propre projet Cognito.

Tout le code source TypeScript est référencé à partir du projet exemple : [cognito-react-nodejs-example](https://github.com/goldstack/cognito-react-nodejs-example).

### Groupes d'utilisateurs

Les [groupes d'utilisateurs](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) dans Cognito sont essentiellement une base de données d'utilisateurs combinée à certaines capacités pour inscrire et connecter les utilisateurs.

Les groupes d'utilisateurs peuvent être configurés pour permettre aux utilisateurs de s'inscrire avec leurs connexions sociales (par exemple un compte Google ou Facebook) ou via des comptes créés directement avec Cognito.

L'extrait suivant contient la configuration du groupe d'utilisateurs utilisé dans le projet de modèle ([main.tf](https://github.com/goldstack/cognito-nodejs-template/blob/master/packages/user-management-1/infra/aws/main.tf#L1)) :

```hcl
resource "aws_cognito_user_pool" "pool" {
  name          = var.user_pool_name

  # Ajoutez le nom de votre application ci-dessous
  email_verification_subject = "Votre code de vérification"
  email_verification_message = "Votre code de vérification est {####}."

  schema {
    attribute_data_type = "String"
    name                = "email"
    required            = true
    mutable             = true

    string_attribute_constraints {
      min_length = 1
      max_length = 100
    }
  }

  username_attributes      = ["email"]
  auto_verified_attributes = ["email"]

  password_policy {
    minimum_length    = 6
    require_lowercase = false
    require_numbers   = false
    require_symbols   = false
    require_uppercase = false
  }
  
  device_configuration {
    challenge_required_on_new_device      = true 
    device_only_remembered_on_user_prompt = false
  }
}

```

Puisque le groupe d'utilisateurs décrit une base de données d'utilisateurs, vous devez définir quel type de données vous souhaitez stocker pour les utilisateurs. Cela est défini dans la propriété `schema` ci-dessus.

Le projet de modèle ne configure qu'un seul attribut pour les utilisateurs : `email`. Cela vous permet de stocker l'adresse e-mail de l'utilisateur.

Je recommande de définir le _minimum absolu_ d'attributs pour les utilisateurs possible. Cela est dû au fait qu'il est [difficile de changer les attributs plus tard](https://dev.to/aws-heroes/the-case-for-and-against-amazon-cognito-2599). Par conséquent, nous ne définissons ici que l'attribut `email` - puisque nous prévoyons de le capturer et de le valider pour nos utilisateurs.

Le modèle définit également une `password_policy` pour les mots de passe que les utilisateurs doivent définir. Le groupe d'utilisateurs dans l'exemple a une politique de mot de passe très permissive - mais vous pouvez facilement la changer en modifiant `main.tf`.

Cognito fournit certaines fonctionnalités très puissantes telles que la possibilité de valider automatiquement les adresses e-mail des utilisateurs. Cela est réalisé en définissant la propriété `auto_verified_attributes = ["email"]`.

Cela amènera Cognito à envoyer un e-mail avec un code unique aux nouveaux utilisateurs. Les utilisateurs seront validés et pourront accéder à l'application uniquement après avoir saisi ce code avec l'interface utilisateur de Cognito.

### Clients d'application

Vous pouvez utiliser Cognito avec des applications Web et mobiles. Vous devez fournir une configuration spécifique pour chaque client que vous souhaitez utiliser.

Le modèle fournit une configuration pour un client Web, qui permet aux utilisateurs de s'inscrire via leur navigateur Web.

Cela est configuré dans [web-client.tf](https://github.com/goldstack/cognito-nodejs-template/blob/master/packages/user-management-1/infra/aws/web-client.tf#L2) dans le projet de modèle :

```hcl
resource "aws_cognito_user_pool_client" "client" {
  name                                 = "${var.user_pool_name}-client"
  user_pool_id                         = aws_cognito_user_pool.pool.id
  callback_urls                        = [var.callback_url]
  default_redirect_uri                 = var.callback_url
  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_flows                  = ["code", "implicit"]
  allowed_oauth_scopes                 = ["email", "openid"]
  supported_identity_providers         = ["COGNITO", 
    # décommentez ceci pour activer la connexion avec Google
    # - n'oubliez pas de fournir les détails de votre application dans identity-providers.tf
    # aws_cognito_identity_provider.google_provider.provider_name
  ]
}

resource "aws_cognito_user_pool_domain" "main" {
  domain               = data.aws_acm_certificate.wildcard.domain
  certificate_arn      = aws_acm_certificate.wildcard.arn
  user_pool_id         = aws_cognito_user_pool.pool.id
  depends_on = [
    aws_acm_certificate_validation.wildcard_validation,
  ]
}

resource "aws_cognito_user_pool_ui_customization" "ui" {
  css        = ".label-customizable {font-weight: 400;}"
  image_file = filebase64("favicon-32x32.png")

  # Référez-vous à l'attribut user_pool_id de la ressource aws_cognito_user_pool_domain
  # pour vous assurer qu'il est dans un état 'Actif'
  user_pool_id = aws_cognito_user_pool_domain.main.user_pool_id
}

```

Pour prendre en charge le flux d'authentification basé sur OAuth défini ci-dessus, vous devez activer OAuth dans votre configuration client. 

Le modèle est configuré pour permettre l'inscription en fournissant un e-mail ou via Open ID. Cependant, pour activer Open ID, vous devez fournir une configuration supplémentaire dans [identity-providers.tf](https://github.com/goldstack/cognito-nodejs-template/blob/master/packages/user-management-1/infra/aws/identity-providers.tf), telle que l'identité de notre application avec le fournisseur Open ID.

La configuration client ci-dessus fournit également une personnalisation mineure de l'interface utilisateur présentée aux utilisateurs lors de l'inscription et de la connexion en utilisant la ressource `aws_cognito_user_pool_ui_customization`.

Par défaut, Cognito héberge l'interface utilisateur pour les utilisateurs sur un domaine appartenant à Amazon, mais vous pouvez la personnaliser pour permettre aux utilisateurs de s'inscrire et de se connecter sur un domaine que vous possédez. Le modèle personnalise le nom de domaine en `data.aws_acm_certificate.wildcard.domain`. Cela est accompli en utilisant la ressource `aws_cognito_user_pool_domain`.

Enfin, vous devez définir une `callbackUrl`. Il s'agit de l'URL dans votre application Web vers laquelle les utilisateurs sont redirigés après une connexion réussie. Cognito prend en charge plusieurs URL de rappel, mais nous n'en fournissons qu'une seule dans le projet de modèle.

### Endpoints

Après avoir configuré votre groupe d'utilisateurs et votre client d'application, Cognito hébergera un certain nombre d'endpoints pour vous.

Tous ces endpoints sont hébergés sous le domaine personnalisé que vous avez configuré pour le client d'application.

Les endpoints suivants seront fournis :

#### Connexion

```
https://{domain}/oauth2/authorize

```

Cela fournit une interface utilisateur qui permet par défaut aux utilisateurs de se connecter, mais permet également aux utilisateurs de s'inscrire ou de réinitialiser leur mot de passe, ou de récupérer un mot de passe perdu. Redirigez les utilisateurs vers cette page pour initier le flux d'inscription OAuth.

#### Inscription

```
https://{domain}/signup

```

Cela fournit une interface utilisateur qui invite par défaut les utilisateurs à s'inscrire à l'application.

#### Obtenir un jeton

```
https://{domain}/oauth2/token

```

Un endpoint auquel vous pouvez faire un appel POST pour obtenir les jetons d'accès, d'identité et de rafraîchissement, à condition qu'un `code` valide soit fourni pendant le flux d'authentification.

#### Déconnexion

```
https://{domain}/logout

```

Rediriger les utilisateurs vers cette URL depuis votre application Web les forcera à se déconnecter.

Notez que tous ces endpoints doivent être paramétrés avec des informations de votre application, de votre client d'application et de votre groupe d'utilisateurs. Le modèle fourni utilise une bibliothèque pour construire les URL correctes. Le code source de la bibliothèque peut être trouvé dans [cognitoEndpoints.ts](https://github.com/goldstack/goldstack/blob/master/workspaces/templates-lib/packages/template-user-management/src/cognitoEndpoints.ts) :

```typescript
  switch (args.endpoint) {
    case 'authorize':
      return (
        `${baseUrl}/oauth2/authorize?response_type=code` +
        `&client_id=${deploymentOutput.terraform.user_pool_client_id.value}` +
        `&redirect_uri=${deployment.configuration.callbackUrl}` +
        '&code_challenge_method=S256' +
        `&code_challenge=${await getCodeChallenge()}`
      );
    case 'signup':
      return (
        `${baseUrl}/signup?response_type=code` +
        `&client_id=${deploymentOutput.terraform.user_pool_client_id.value}` +
        `&redirect_uri=${deployment.configuration.callbackUrl}` +
        '&code_challenge_method=S256' +
        `&code_challenge=${await getCodeChallenge()}`
      );
    case 'token':
      return `${baseUrl}/oauth2/token`;
    case 'logout':
      return (
        `${baseUrl}/logout?response_type=code` +
        `&client_id=${deploymentOutput.terraform.user_pool_client_id.value}` +
        `&redirect_uri=${deployment.configuration.callbackUrl}` +
        '&code_challenge_method=S256' +
        `&code_challenge=${await getCodeChallenge()}`
      );
  }

```

## Comment inscrire et authentifier les utilisateurs

Une fois que Cognito est configuré correctement comme décrit ci-dessus, vous pouvez commencer à inscrire des utilisateurs pour votre application.

Il existe plusieurs façons de procéder, mais généralement vous commencez par rediriger les utilisateurs de votre application Web vers les URL décrites dans la section précédente.

Dans cette section, je ferai référence au projet exemple : [cognito-react-nodejs-example](https://github.com/goldstack/cognito-react-nodejs-example) plutôt qu'au projet de modèle ([cognito-nodejs-template](https://github.com/goldstack/cognito-nodejs-template)) référencé dans les sections précédentes.

Le projet exemple ne sera pas automatiquement mis à jour comme le projet de modèle. Mais il fournit un exemple intégré qui contient à la fois la configuration Cognito ainsi qu'une application Web simple, ce qui facilitera le suivi des concepts discutés dans cette section.

J'ai également enveloppé un certain nombre de fonctions de commodité dans une bibliothèque qui est publiée sur npm : [`@goldstack/template-user-management`](https://www.npmjs.com/package/@goldstack/template-user-management). Le code source de cette bibliothèque est disponible [ici](https://github.com/goldstack/goldstack/tree/master/workspaces/templates-lib/packages/template-user-management).

Le projet exemple utilise [yarn workspaces](https://yarnpkg.com/features/workspaces) et contient deux packages :

* [`packages/server-side-rendering`](https://github.com/goldstack/cognito-react-nodejs-example/tree/master/packages/server-side-rendering) pour définir l'application Web personnalisée avec laquelle les utilisateurs interagissent.
* [`packages/user-management`](https://github.com/goldstack/cognito-react-nodejs-example/tree/master/packages/user-management) pour définir la configuration Cognito et un wrapper de base autour de l'API Cognito.

J'adore les workspaces car ils permettent de développer des applications fullstack de manière propre et modulaire. Pour plus d'informations sur la configuration de base du projet, veuillez consulter mon article [The Ultimate Guide to TypeScript Monorepos](https://maxrohde.com/2021/11/20/the-ultimate-guide-to-typescript-monorepos).

Notre application simple contient une seule page qui est définie dans le package `server-side-rendering` : [$index.tsx](https://github.com/goldstack/cognito-react-nodejs-example/blob/master/packages/server-side-rendering/src/routes/%24index.tsx).

![Capture d'écran de l'application exemple avec les boutons Se connecter et S'inscrire](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20230115110925.png)

J'abrège ci-dessous la logique clé pour l'authentification fournie dans le gestionnaire d'index :

```typescript
import {
  getLoggedInUser,
  handleRedirectCallback,
  loginWithRedirect,
} from 'user-management';

const Index = (props: { message: string }): JSX.Element => {
  const user = getLoggedInUser();
  handleRedirectCallback();
  return (
    <>
      {!user && (
        <button
          onClick={() => {
            loginWithRedirect();
          }}
        >
          Se connecter
        </button>
      )}
    </>
  );
};

```

L'importation du package `user-management` vous permet d'accéder à un certain nombre de méthodes de commodité nécessaires pour interagir avec Cognito dans l'application Web. Voir le module [users.ts](https://github.com/goldstack/cognito-nodejs-template/blob/master/packages/user-management-1/src/users.ts) dans le package `user-management` pour référence.

La méthode [`getLoggedInUser()`](https://github.com/goldstack/goldstack/blob/master/workspaces/templates-lib/packages/template-user-management/src/templateUserManagement.ts#L142) retournera le jeton d'identité et d'accès pour l'utilisateur si un utilisateur est connecté.

La méthode [`handleRedirectCallback()`](https://github.com/goldstack/goldstack/blob/master/workspaces/templates-lib/packages/template-user-management/src/templateUserManagement.ts#L173) effectue la logique que le client doit suivre pour les étapes du flux d'autorisation qui rappellent le client. Plus précisément, la méthode :

* Vérifie s'il y a un paramètre `?code` dans l'URL.
* Si c'est le cas, appelle l'endpoint `token` avec le `code` fourni pour obtenir les jetons utilisateur (identité, accès et rafraîchissement).
* Utilise un jeton de rafraîchissement (si disponible) pour obtenir de nouveaux jetons d'identité et d'accès.

La méthode [`loginWithRedirect()`](https://github.com/goldstack/goldstack/blob/master/workspaces/templates-lib/packages/template-user-management/src/templateUserManagement.ts#L219) redirigera l'utilisateur vers l'interface utilisateur fournie par Cognito si l'utilisateur n'est pas encore authentifié.

La page définie dans [$index.tsx](https://github.com/goldstack/cognito-react-nodejs-example/blob/master/packages/server-side-rendering/src/routes/%24index.tsx) utilise quelques méthodes supplémentaires :

* `signUpWithRedirect()` qui fonctionne comme `loginWithRedirect()` mais par défaut l'interface utilisateur de Cognito vers l'inscription plutôt que vers le flux de connexion et est connecté au bouton _S'inscrire_ dans l'application exemple.
* `performLogout()` qui déconnectera l'utilisateur.

## Sécurisation des endpoints

Une fois que vous avez obtenu les jetons côté client, vous pouvez les renvoyer au serveur - par défaut, le modèle les écrira dans un cookie côté client, mais vous pouvez également les envoyer en tant que jetons porteurs dans les en-têtes pour des requêtes personnalisées.

Dans la logique côté serveur, vous pouvez à nouveau importer le module `user-management`. En utilisant la méthode `connectWithCognito`, vous pouvez valider le jeton d'accès et le jeton d'identité passés depuis les clients :

```typescript
import { connectWithCognito } from 'user-management';

export const handler: SSRHandler = async (event, context) => {
  const cookies = getCookies((event.cookies || []).join(';'));
  if (cookies.goldstack_access_token) {
    const cognito = await connectWithCognito();
    await cognito.validate(cookies.goldstack_access_token);
    const idToken = await cognito.validateIdToken(cookies.goldstack_id_token);
    message = `Bonjour ${idToken.email}<br>`;
  }
};

```

Voir le [gestionnaire côté serveur de la route index dans le projet exemple](https://github.com/goldstack/cognito-react-nodejs-example/blob/master/packages/server-side-rendering/src/routes/%24index.tsx#L121) pour une référence de code source complète.

Notez qu'il est _extrêmement important_ d'appeler les méthodes `validate()` sur les jetons, et de ne pas simplement les décoder directement pour lire leur contenu. L'API développée dans cet exemple ne sera sécurisée que si vous validez les jetons.

## Gestion des utilisateurs

Une fois que vous avez inscrit des utilisateurs pour votre application, vous devrez peut-être effectuer des travaux administratifs avec eux - tels que la réinitialisation des mots de passe ou l'exportation de la liste de tous les utilisateurs.

Vous pouvez le faire facilement en utilisant la [Console AWS](https://us-west-2.console.aws.amazon.com/cognito/). Recherchez le service _Cognito_ puis sélectionnez _Gérer les groupes d'utilisateurs_.

![Amazon Cognito sur la Console AWS](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221227073537.png)

Ensuite, sélectionnez le groupe d'utilisateurs qui a été créé et allez dans _Paramètres généraux_ / _Utilisateurs et groupes_. Ici, nous pouvons voir une liste de tous les utilisateurs inscrits :

![Liste des utilisateurs sur la console AWS Cognito](https://www.freecodecamp.org/news/content/images/2023/01/Pasted-image-20221227073712.png)

Veuillez ne pas modifier d'autres paramètres dans la console AWS. Toutes les modifications de la configuration du groupe d'utilisateurs doivent être effectuées en modifiant les fichiers de configuration [Terraform fournis](https://github.com/goldstack/cognito-react-nodejs-example/tree/master/packages/user-management/infra/aws).

## Conclusion

De nombreuses applications nécessitent l'enregistrement et l'identification des utilisateurs. Malheureusement, la fourniture de fonctionnalités d'authentification des utilisateurs peut devenir assez compliquée.

Dans cet article, j'ai montré comment créer une [application simple](https://cognito-react-nodejs.examples.dev.goldstack.party/) qui permet de s'inscrire et de se connecter de manière sécurisée.

Amazon Cognito résout la plupart des problèmes difficiles pour nous. Par exemple, il y a une complexité significative impliquée dans la gestion de la vérification des e-mails ou une fonctionnalité pour récupérer les derniers mots de passe.

En utilisant les solutions par défaut fournies par Cognito, principalement l'[interface utilisateur hébergée](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-integration.html), vous pouvez garder votre application légère et vous concentrer sur les problèmes uniques que vous souhaitez résoudre.

Cependant, comme pour toute solution clé en main, vous sacrifiez la flexibilité et l'extensibilité. Le [projet exemple](https://github.com/goldstack/cognito-react-nodejs-example) et le [modèle](https://github.com/goldstack/cognito-nodejs-template) fournissent toute la configuration dans Terraform et peuvent être modifiés selon vos besoins - mais cela ne sera pas toujours facile.

Dans l'ensemble, je recommande vivement d'utiliser une plateforme existante pour gérer l'identité des clients. [Auth0 et Okta](https://auth0.com/) sont probablement préférables à Cognito si vous n'êtes pas lié à AWS. Pour cet article, j'ai choisi Cognito car je travaille sur la construction d'une [pile serverless complète](https://goldstack.party) pour AWS.

Dans mes articles, je vais au-delà de la fourniture de snippets de code et je fournis des bibliothèques et des modèles qui vous donnent un coup de pouce pour lancer votre application. Vous pouvez aider à rendre le voyage encore plus facile pour les autres, en [me contactant](https://maxrohde.com/about) avec des idées pour améliorer l'article ou, encore mieux, en aidant à améliorer le [modèle](https://github.com/goldstack/cognito-nodejs-template#cognito-nodejs-template) et le [projet exemple](https://github.com/goldstack/cognito-react-nodejs-example).
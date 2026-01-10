---
title: Comment utiliser AWS Cognito pour l'authentification des utilisateurs
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-05-31T17:01:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-aws-cognito-for-user-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/AWS-cognito.png
tags:
- name: authentication
  slug: authentication
- name: AWS
  slug: aws
- name: privacy
  slug: privacy
seo_title: Comment utiliser AWS Cognito pour l'authentification des utilisateurs
seo_desc: "When you're building complex applications, one seemingly simple feature\
  \ can be difficult to implement: user authentication. \nThough some apps don't need\
  \ it depending on their use case, many do. You might spend a ton of time building\
  \ an authentication..."
---

Lorsque vous construisez des applications complexes, une fonctionnalité apparemment simple peut être difficile à implémenter : l'authentification des utilisateurs. 

Bien que certaines applications n'en aient pas besoin selon leur cas d'utilisation, beaucoup en ont besoin. Vous pourriez passer beaucoup de temps à construire un module d'authentification pour offrir une expérience sécurisée à vos utilisateurs et protéger leurs données et leur vie privée. Mais vous pouvez également externaliser cela dans un service séparé comme AWS Cognito.

Selon le [site](https://aws.amazon.com/cognito/),

> _Amazon Cognito_ vous aide à implémenter la gestion de l'identité et des accès clients (CIAM) dans vos applications web et mobiles.

En bref, AWS Cognito est conçu pour simplifier l'implémentation de l'authentification et de l'autorisation des utilisateurs. Avec Cognito, vous pouvez vous concentrer sur la construction des fonctionnalités principales de votre application, tout en déléguant les complexités de la gestion des utilisateurs au service.

Dans ce tutoriel, nous allons plonger dans le monde d'AWS Cognito en créant un AWS Cognito User Pool pour l'authentification des utilisateurs. Vous verrez comment lire les données depuis AWS Cognito et les afficher dans une simple application NextJS.

Voici une rapide démonstration de l'application que nous allons construire. Je vais me concentrer davantage sur AWS Cognito que sur NextJS, car vous pouvez porter ce service avec n'importe quel framework UI que vous souhaitez. Néanmoins, vous pouvez obtenir le code source complet du dépôt NextJS depuis [ici](https://github.com/5minslearn/aws_cognito).

![Image](https://www.freecodecamp.org/news/content/images/2023/05/5minslearn.gif)
_AWS Cognito intégré avec une application NextJS_

## Qu'est-ce qu'un AWS Cognito User Pool ?

Les AWS Cognito User Pools sont un service de répertoire d'utilisateurs entièrement géré qui vous permet de créer et de gérer un ensemble d'utilisateurs pour votre application. 

Les User Pools fournissent un ensemble de fonctionnalités qui vous permettent de gérer l'inscription des utilisateurs, la connexion et la récupération de compte de manière transparente.

## Avantages des AWS Cognito User Pools

#### Intégration facile

Les Cognito User Pools s'intègrent de manière transparente avec diverses plateformes et frameworks d'applications, y compris les applications web, mobiles et côté serveur, ce qui les rend polyvalents pour différents cas d'utilisation.

#### Authentification sécurisée des utilisateurs

Les User Pools prennent en charge diverses méthodes d'authentification, y compris l'email et le mot de passe, la connexion sociale (comme Google, Facebook ou Amazon), et l'authentification multi-facteurs. Cela garantit une sécurité robuste pour l'authentification des utilisateurs.

#### Inscription et gestion des utilisateurs

Les User Pools simplifient le processus d'inscription des utilisateurs en fournissant des pages d'inscription personnalisables et une vérification par email. Ils offrent également des fonctionnalités d'auto-service pour les utilisateurs, comme la réinitialisation du mot de passe et la gestion du profil, réduisant ainsi la charge sur le backend de l'application.

#### Évolutivité et performance

AWS gère les aspects d'évolutivité et de performance du pool d'utilisateurs, vous permettant de gérer des millions d'utilisateurs sans vous soucier de la provision d'infrastructure ou de l'optimisation des performances.

## Comment créer un AWS Cognito User Pool

Plongeons dans le processus étape par étape de création d'un AWS Cognito User Pool.

#### Connectez-vous à la console de gestion AWS

Connectez-vous à votre console de gestion AWS en utilisant vos identifiants.

#### **Service AWS Cognito**

Recherchez "Cognito" dans la barre de recherche de la console de gestion AWS et ouvrez le service Cognito. Vous verrez une page comme illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-132.png)
_Console AWS Cognito_

#### **Créer un User Pool**

Cliquez sur le bouton "Créer un User Pool". Vous pouvez voir deux types de fournisseurs. L'un est le Cognito user pool qui sera sélectionné par défaut et fournit une authentification par email et mot de passe régulière. L'autre est les fournisseurs d'identité fédérés qui permettront aux utilisateurs de se connecter avec leur identité sociale comme Facebook, Google, etc.

Pour garder cela simple, je sélectionne uniquement le Cognito user pool et je sélectionne un nom d'utilisateur et un email pour les options de connexion.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-133.png)
_AWS Cognito - Configurer les options de connexion_

#### **Configurer les exigences de sécurité**

Configurez vos paramètres souhaités, tels que les politiques de mot de passe, l'authentification multi-facteurs, les méthodes MFA et la récupération de compte utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-134.png)
_AWS Cognito - Définir la politique de mot de passe et MFA_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-136.png)
_AWS Cognito - Définir la récupération de compte utilisateur_

#### **Configurer l'expérience d'inscription**

Configurez l'expérience d'inscription en fonction de vos besoins. Vous pouvez définir des attributs requis et des attributs personnalisés qui seront affichés à l'utilisateur sur la page d'inscription. Ces données seront stockées dans le pool d'utilisateurs Cognito.

#### **Configurer la livraison des messages**

Vous voudrez sélectionner le fournisseur d'email comme "SES" pour les applications de production. Comme il s'agit d'une démonstration, je sélectionne l'option "Envoyer un email avec Cognito".

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-138.png)
_AWS Cognito - Configurer la livraison des messages_

#### Intégrer votre application

Fournissez un nom unique pour votre pool d'utilisateurs. Cochez l'option "Utiliser l'UI hébergée par Cognito" pour utiliser l'UI fournie par AWS.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-139.png)
_AWS Cognito - Intégrer l'application_

Choisissez votre type de domaine souhaité. Pour utiliser un domaine personnalisé, vous devez fournir un enregistrement DNS et un certificat AWS Certificate Manager.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-140.png)
_AWS Cognito - Sélectionner le type de domaine_

L'étape suivante consiste à initialiser le client de l'application. Ce client de l'application représente votre application et lui permet d'interagir avec le pool d'utilisateurs. Configurez les paramètres du client de l'application, y compris les portées OAuth autorisées et les URLs de rappel. Dans notre cas ici, ce sera http://localhost:3000, car nous allons exécuter uniquement sur notre machine locale.

Entrez un nom convivial "Nom du client de l'application". Vous devez fournir l'URL de rappel de votre site. Après l'authentification, l'utilisateur sera redirigé vers cette URL.

Nous devons interroger le service Cognito pour récupérer les détails de l'utilisateur. Pour ce faire, nous avons besoin d'un secret client. Sélectionnez l'option "Générer un secret client".

Explorez toutes les autres options sur la page et configurez-les en fonction de vos besoins. J'espère qu'elles sont auto-explicatives. Si vous ne comprenez pas certaines des options, laissez-les simplement comme sélection par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-141.png)
_AWS Cognito - Générer un secret client_

#### Révision et création

Enfin, une page de révision sera affichée où vous pouvez passer en revue toutes vos configurations. Cliquez sur "Créer le pool" pour créer votre pool d'utilisateurs.

Nous avons terminé la moitié du travail. Nous avons créé avec succès le User Pool.

## Personnalisation de l'UI hébergée

Pour personnaliser votre page de connexion, cliquez sur le pool d'utilisateurs que vous venez de créer et cliquez sur l'onglet Intégration d'application.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/App-Integration-Tab.png)
_AWS Cognito - Onglet d'intégration d'application_

Localisez la personnalisation de l'UI hébergée et cliquez sur le bouton "Modifier". Vous pouvez télécharger votre logo et votre CSS personnalisé, qui seront appliqués sur les pages d'inscription et de connexion.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Hosted-UI-Customization.png)
_AWS Cognito - Personnalisation de l'UI hébergée_

Vous pouvez visualiser l'UI hébergée avec votre personnalisation appliquée en construisant l'URL suivante, avec les spécificités de votre pool d'utilisateurs, et en la tapant dans un navigateur : `https://<votre_domaine>/login?response_type=code&client_id=<votre_id_client>&redirect_uri=<votre_url_de_rappel>`. Vous pouvez récupérer toutes les données depuis le tableau de bord. 

Accédez à l'URL. Si vous ne voyez pas la page de connexion chargée et voyez une page d'erreur à la place, ne paniquez pas. Les modifications que vous avez apportées sur le tableau de bord peuvent prendre quelques minutes pour être disponibles.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-144.png)
_Page de connexion_

Comme nous n'avons pas de compte créé, essayons de nous inscrire. AWS Cognito gère toutes les tracas de l'envoi d'un email de vérification, de la demande à l'utilisateur de configurer MFA, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-145.png)
_Page d'inscription_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-146.png)
_AWS Cognito - Vérification par email_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-147.png)
_AWS Cognito - MFA_

Espérons qu'en appuyant sur votre bouton final "Se connecter", vous serez redirigé vers une page d'erreur. Savez-vous pourquoi ? Nous n'avons pas notre client en cours d'exécution. Si vous regardez l'URL, vous serez sur `http://localhost:3000`.

Mais, c'est le bon moment pour nous de vérifier si notre intégration est correcte. Ouvrons le tableau de bord du pool d'utilisateurs et voyons si notre nouvel utilisateur inscrit y est affiché.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/User-Pool-Database.png)
_AWS Cognito - Base de données des utilisateurs_

Excellent travail ! Notre premier utilisateur est apparu dans le tableau de bord. Maintenant, récupérons les informations de l'utilisateur depuis Cognito en utilisant NextJS.

## Comment récupérer les informations de l'utilisateur depuis AWS Cognito en utilisant NextJS

Pour récupérer les données depuis Cognito, nous allons utiliser les API fournies par Cognito. Tout d'abord, nous devons obtenir le jeton d'accès en utilisant le [point de terminaison Token](https://docs.aws.amazon.com/cognito/latest/developerguide/token-endpoint.html) et utiliser ce jeton d'accès pour obtenir les informations de l'utilisateur en utilisant le [point de terminaison User Info](https://docs.aws.amazon.com/cognito/latest/developerguide/userinfo-endpoint.html)

Pour me suivre, vous pouvez utiliser ce [dépôt](https://github.com/5minslearn/deploy_nextjs_app) qui contient le code de base de NextJS.

Clonez le dépôt, installez les dépendances en entrant la commande `yarn install`, et exécutez l'application en entrant la commande `yarn dev`.

Une fois que vous avez terminé, vous arriverez sur cette page après avoir accédé à `http://localhost:3000` :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-149.png)

Si vous suivez le même processus d'inscription/connexion que nous avons fait ci-dessus, vous serez redirigé vers la page ci-dessus.

### Requête POST au point de terminaison Token d'AWS Cognito

**Exemple de requête :**

```
POST https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/token&Content-Type='application/x-www-form-urlencoded'&Authorization=Basic ZGpjOTh1M2ppZWRtaTI4M2V1OTI4OmFiY2RlZjAxMjM0NTY3ODkw                            
&grant_type=authorization_code&client_id=1example23456789&code=AUTHORIZATION_CODE&redirect_uri=com.myclientapp://myclient/redirect
```

Le point de terminaison Token a besoin des paramètres suivants :

1. **Nom de domaine** – Allez dans le pool d'utilisateurs Cognito, et dans l'onglet Intégration d'application, vous pouvez trouver le nom de domaine.
2. **ID client et secret client** – Au bas de la même page, trouvez la liste des clients de l'application et cliquez sur le client de l'application que vous avez créé. Vous pouvez voir l'ID client et le secret client.
3. **Code d'autorisation** – il s'agit d'un code qui est disponible dans l'URL vers laquelle nous sommes redirigés. (Voir la capture d'écran ci-dessous)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-150.png)
_AWS Cognito - Code d'autorisation_

Écrivons le code pour obtenir le code d'autorisation.

Ouvrez le fichier `index.tsx` et ajoutez le code suivant :

```
import { useSearchParams } from "next/navigation";
...
...
export default function Home() {
const searchParams = useSearchParams();
const code = searchParams.get("code");
...
```

Créez un fichier `.env.local` dans le dossier racine du projet et ajoutez les identifiants suivants :

```
NEXT_PUBLIC_COGNITO_CLIENT_ID=<cognito_client_id>
NEXT_PUBLIC_COGNITO_CLIENT_SECRET=<cognito_client_secret>
NEXT_PUBLIC_COGNITO_DOMAIN=<cognito_domain>
```

Maintenant, ajoutez le `useEffect` avec le bloc de code suivant à l'intérieur :

```
import axios from 'axios';

...

export default function Home() {
  const searchParams = useSearchParams();
  const code = searchParams.get("code");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  useEffect(() => {
    if (!code) return;
    const clientID = process.env.NEXT_PUBLIC_COGINTO_CLIENT_ID || "";
    const clientSecret = process.env.NEXT_PUBLIC_COGNITO_CLIENT_SECRET || "";
    const cognitoDomain = process.env.NEXT_PUBLIC_COGNITO_DOMAIN || "";
    const credentials = `${clientID}:${clientSecret}`;
    const base64Credentials = Buffer.from(credentials).toString("base64");
    const basicAuthorization = `Basic ${base64Credentials}`;
    const headers = {
      "Content-Type": "application/x-www-form-urlencoded",
      Authorization: basicAuthorization,
    };
    const data = new URLSearchParams();
    let token = "";
    data.append("grant_type", "authorization_code");
    data.append("client_id", clientID);
    data.append("code", code);
    data.append("redirect_uri", "http://localhost:3000");
    axios
      .post(
        `${cognitoDomain}/oauth2/token`,
        data,
        { headers }
      )
      .then((res) => {
        if (res.status != 200) return;
        token = res?.data?.access_token;
        const userInfoHeaders = {
          Authorization: "Bearer " + token,
        };
        axios
          .get(
            `${cognitoDomain}/oauth2/userInfo`,
            { headers: userInfoHeaders }
          )
          .then((userInfo) => {
            if (userInfo.status != 200) return;
            setName(userInfo.data?.username);
            setEmail(userInfo.data?.email);
          });
      });
  }, [code]);

...
...
```

Que faisons-nous dans le code ci-dessus ? Explorons.

Nous devons obtenir le jeton d'accès. Ce jeton est nécessaire pour autoriser l'utilisateur chaque fois qu'il utilise l'application. 

Pour obtenir ce jeton, nous devons faire une requête HTTP POST au service AWS Cognito en attachant l'encodage Base64 de notre identifiant client et de notre secret dans l'en-tête d'autorisation. De plus, nous devons passer le code que nous avons reçu de l'URL lorsque l'utilisateur a été redirigé.

Nous utiliserons ce jeton pour obtenir les informations de l'utilisateur. Nous stockons les informations de l'utilisateur (nom et email) dans la variable d'état de l'application.

Nous avons obtenu le nom et l'email de l'utilisateur à partir du code ci-dessus. Affichons-les à l'écran.

```
...
...
<h2 className={inter.className}>Bienvenue sur 5minslearn !</h2>
      {name && email ? (
        <>
          <h2 className={inter.className}>{name}</h2>
          <p className={inter.className}>{email}</p>
        </>
      ) : (
        <></>
      )}
...
...
```

Super. Notre application est complètement prête maintenant.

Une fois que vous vous connectez à nouveau depuis Cognito, vous serez redirigé vers votre site et vous verrez une page avec votre nom et votre email (comme celle montrée dans la capture d'écran ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-151.png)
_Obtenir le nom et l'email de l'utilisateur depuis AWS Cognito en utilisant Next.js_

Super – nous avons réussi à récupérer les données depuis AWS Cognito et à les afficher dans notre application.

## Conclusion

Dans ce tutoriel, vous avez appris comment construire une authentification utilisateur en créant un pool d'utilisateurs Cognito. Vous avez également vu comment récupérer des données depuis Amazon Cognito en utilisant NextJS.

J'espère que vous avez apprécié la lecture de cet article ! Voici le lien vers le [dépôt](https://github.com/5minslearn/aws_cognito).

Si vous souhaitez en savoir plus sur AWS, abonnez-vous à ma [newsletter](https://5minslearn.gogosoon.com/?ref=fcc_aws_cognito) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_aws_cognito)) et suivez-moi sur les réseaux sociaux.
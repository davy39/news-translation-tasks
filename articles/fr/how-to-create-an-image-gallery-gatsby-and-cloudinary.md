---
title: Comment créer une galerie d'images avec Gatsby et Cloudinary
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2020-10-12T20:36:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-image-gallery-gatsby-and-cloudinary
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/cover_1.png
tags:
- name: Gatsby
  slug: gatsby
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer une galerie d'images avec Gatsby et Cloudinary
seo_desc: 'According to Mathias Biilmann, the CEO & Co-founder of Netlify,"The JAMstack
  is a modern web development architecture based on client-side JavaScript, reusable
  APIs, and prebuilt Markup."

  The key aspects of a JAMstack application are the following:


  ...'
---

Selon Mathias Biilmann, PDG et cofondateur de Netlify, "Le `JAMstack` est une architecture moderne de développement web basée sur JavaScript côté client, des API réutilisables et du balisage préconstruit."

Les aspects clés d'une application [JAMstack](https://blog.greenroots.info/jamstack-for-all-an-introduction-cke2fxc5800jvabs15lhn4a9x) sont les suivants :

* L'application entière s'exécute sur un **CDN (ou ADN)**. CDN signifie Content Delivery Network et ADN est un Application Delivery Network.
* Tout est dans **Git**.
* Les **builds automatisés** s'exécutent avec un workflow lorsque les développeurs poussent le code.
* Il y a un **déploiement automatique** du balisage préconstruit vers le CDN/ADN.
* C'est pratiquement **Serverless**. Pour être plus clair, nous ne maintenons aucune application côté serveur mais utilisons plutôt des services déjà existants (comme l'email, les médias, la base de données, la recherche, etc.).

Et voici un fait amusant : De nombreuses fonctionnalités qui nécessitaient autrefois un backend personnalisé peuvent désormais être réalisées entièrement côté frontend.

Dans cet article, nous allons apprendre à construire une application [JAMstack](https://blog.greenroots.info/jamstack-for-all-an-introduction-cke2fxc5800jvabs15lhn4a9x) qui possède :

* un service API pour servir les fichiers médias,
* et un [Static Site Generator (SSG)](https://blog.greenroots.info/what-is-a-static-site-generator-and-how-to-select-one-cke9xtx5g006p58s11dzg2j16) pour créer le balisage préconstruit.

Et enfin, nous allons la déployer sur un CDN.

## **Alors, que construisons-nous aujourd'hui ?**

Nous allons construire une galerie d'images. J'aime les films, alors j'ai décidé de créer une galerie d'images de mes acteurs préférés. J'ai un nom amusant pour cela : `imaginary`.

Nous allons utiliser un service de gestion de médias appelé [Cloudinary](https://cloudinary.com/) pour héberger et gérer nos images. Il fournit également des API pour les développeurs afin de télécharger et récupérer des médias tels que des images, des vidéos, etc.

Nous allons utiliser un framework appelé [Gatsby](https://www.gatsbyjs.com/) pour construire le frontend de la galerie d'images. `Gatsby` est un framework open-source basé sur React pour créer des sites web et des applications.

Enfin, nous allons apprendre à déployer l'application sur un CDN avec un processus de build et de déploiement automatique. Nous utiliserons [Netlify CDN](https://www.netlify.com/) pour cela.

À la fin de l'article, notre application `imaginary` ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/snap.jpg)
_Application Galerie d'images - Apparence finale_

## **TL;DR**

Nous allons apprendre les choses avec une approche étape par étape dans cet article. Si vous souhaitez accéder au code source ou à la démonstration plus tôt, voici les liens.

* Vous pouvez accéder à la démonstration de la galerie d'images ici : [http://imaginary.netlify.app/](http://imaginary.netlify.app/)
* Tout le code source utilisé dans cet article se trouve dans mon dépôt GitHub. N'hésitez pas à le suivre, car je mets fréquemment à jour le code source. Si vous avez aimé le travail, veuillez le soutenir avec une étoile. [https://github.com/atapas/imaginary/tree/1-freecodecamp-poc](https://github.com/atapas/imaginary/tree/1-freecodecamp-poc)

Maintenant, commençons.

## **Comment configurer Cloudinary**

Tout d'abord, [créez un compte](https://cloudinary.com/users/register/free) avec `Cloudinary`. Un plan gratuit est plus que suffisant pour notre application de galerie d'images.

Connectez-vous en utilisant vos identifiants de compte pour accéder au tableau de bord `Cloudinary`. Veuillez noter le `Nom du cloud`, la `Clé API` et le `Secret API`, car nous en aurons besoin dans notre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/cloudinary.png)

Ensuite, téléchargez les images de votre choix pour les utiliser dans la `galerie d'images`. Vous pouvez créer un dossier et l'appeler comme vous le souhaitez. Dans mon cas, je l'ai nommé `artists` et j'ai téléchargé les images dedans.

Notez que nous utiliserons ce nom de dossier plus tard lorsque nous intégrerons `Cloudinary` avec `Gatsby`.

Veuillez sélectionner chaque image et ajouter un `Titre` et une `Description`. Nous utiliserons ces deux informations métadonnées comme légendes d'images et texte alternatif, respectivement, dans notre galerie d'images.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/cludinary_photo_management.png)

C'est tout. Veuillez ne pas partager le secret API et la clé avec qui que ce soit. Passons maintenant à la configuration requise pour `Gatsby`.

## **Comment configurer Gatsby**

Un projet basé sur `gatsby` nécessite `node.js` pour fonctionner. Assurez-vous d'avoir Node.js installé. Vous pouvez télécharger et installer `node.js` depuis [ici](https://nodejs.org/en/download/).

Une installation réussie affichera la version de Node en utilisant cette commande :

```shell
node -v
```

### **Créer un répertoire de projet**

Créez un répertoire de projet pour organiser le code source. Créons un répertoire avec le nom `imaginary`.

```shell
mkdir imaginary

cd imaginary
```

### **Initialiser le projet**

Il existe de nombreux [projets de démarrage](https://www.gatsbyjs.com/starters/) pour créer une application `gatsby`. Bien que les projets de démarrage simplifient de nombreuses complexités, en même temps, ils peuvent être un peu écrasants pour une application simple comme la nôtre.

En gardant cela à l'esprit, nous allons initialiser un projet `gatsby` simple par nous-mêmes.

Ouvrez une invite de commande et tapez la commande suivante pour initialiser un projet pris en charge par Node.js :

```shell
npm init -y
```

### **Gatsby : Installation et configuration initiale**

Installez l'outil `gatsby-cli` globalement. Cet outil nous aidera à travailler avec l'environnement Gatsby.

```shell
 npm install -g gatsby-cli
```

Installez les dépendances Gatsby, React et ReactDOM. Vous pouvez utiliser la commande `npm install` comme ci-dessus ou la commande `yarn add` si vous avez yarn installé.

```shell
 yarn add gatsby react react-dom
```

Ajoutons également un fichier `.gitignore` avec le contenu suivant :

```shell
.cache
public
node_modules
*.env
```

Vous pouvez optionnellement créer un fichier README.md et LICENSE. À ce stade, notre projet devrait avoir ces dossiers et fichiers :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-14.png)

Les projets `Gatsby` nécessitent un fichier de configuration spécial appelé `gatsby-config.js`. Pour l'instant, nous aurons besoin d'un fichier vide. Créez un fichier nommé `gatsby-config.js` avec le contenu suivant :

```js
 module.exports = {
  // laissez-le vide    
 }
```

Il est maintenant temps de créer notre première page avec `Gatsby`. Créez un dossier nommé `src` à la racine du dossier du projet. Créez un sous-dossier nommé `pages` sous `src`. Créez un fichier nommé `index.js` sous `src/pages` avec le contenu suivant :

```js
import React from 'react';    

  export default () => {    
   return (
      <>    
        <h1>Images à charger ici...</h1>
      </>        
    )    
  }
```

À ce stade, nos fichiers et dossiers de projet devraient ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-16.png)

### **Lançons-le**

Essayez la commande suivante dans l'invite de commande pour exécuter l'application localement :

```shell
gatsby develop
```

Par défaut, une application `gatsby` s'exécute sur le port `8000`. Ouvrez votre navigateur préféré et accédez à l'application @ [http://localhost:8000](http://localhost:8000/).

Vous devriez la voir s'exécuter comme vous le voyez dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-15.png)

C'est tout. Maintenant, nous avons configuré avec succès `Cloudinary` et `Gatsby`. Il est temps de les rassembler.

## **Cloudinary & Gatsby, l'histoire de leur rencontre**

Le framework `Gatsby` bénéficie d'un énorme soutien communautaire et il existe de nombreux plugins pour répondre à des besoins critiques. Début 2020, l'équipe `Cloudinary` a [présenté deux super plugins Gatsby](https://cloudinary.com/blog/introducing_cloudinary_s_gatsby_plugins) à la communauté des développeurs :

* [`Gatsby-Source-Cloudinary`](https://www.npmjs.com/package/gatsby-source-cloudinary) - Aide à récupérer les images stockées au moment de la construction depuis Cloudinary vers une application/site Gatsby.
* [`Gatsby-Transformer-Cloudinary`](https://www.npmjs.com/package/gatsby-transformer-cloudinary) - Aide à télécharger les images locales depuis une application/site Gatsby vers Cloudinary.

Comme nous sommes uniquement intéressés par la récupération des images pour la galerie d'images ici, nous allons simplement installer le plugin `gatsby-source-cloudinary`.

Nous allons également installer un package utilitaire appelé `dotenv` pour gérer les variables d'environnement (Clé Secrète, Clé API, etc.) localement.

Installons-les. Ouvrez une invite de commande et utilisez la commande suivante :

```shell
yarn add dotenv gatsby-source-cloudinary
```

Maintenant, suivez ces étapes pour récupérer les images dans notre application.

1. Créez un fichier `.env` à la racine du dossier du projet et ajoutez le contenu suivant. Veuillez noter que les valeurs dans les paires `clé-valeur` sont disponibles dans le tableau de bord `Cloudinary` comme nous l'avons vu précédemment.

```shell
CLOUDINARY_CLOUD_NAME=<VOTRE_NOM_CLOUDINARY>
CLOUDINARY_API_KEY=<VOTRE_CLE_API_CLOUDINARY>
CLOUDINARY_API_SECRET=<VOTRE_SECRET_API_CLOUDINARY>
```

2.   Modifiez le fichier `gatby-config.js` pour ajouter le contenu suivant :

```js

require('dotenv').config();

module.exports = {
    
    plugins:[
        {
            resolve: `gatsby-source-cloudinary`,
            options: {
              cloudName: process.env.CLOUDINARY_CLOUD_NAME,
              apiKey: process.env.CLOUDINARY_API_KEY,
              apiSecret: process.env.CLOUDINARY_API_SECRET,
              resourceType: `image`,
              prefix: `artists/` ,
              context: true,
              tags: true,
              maxResults: 50
            }
          }
    ]

}
```

Il se passe quelques choses ici. Nous disons à `gatsby` d'utiliser le plugin `gatsby-source-cloudinary` avec quelques paramètres.

Les paramètres `cloudName`, `apiKey` et `apiSecret` sont récupérés depuis le fichier `.env` en utilisant le package `dotenv`. Nous spécifions également la valeur `resourceType` comme `image` car nous ne sommes pas intéressés par la récupération d'autres types de médias.

La valeur du paramètre `prefix` doit être la même que le nom du dossier d'images dans Cloudinary.

Nous spécifions `context` et `tags` comme true pour récupérer les métadonnées contextuelles et les informations de balises d'une image. Nous définissons également `maxResults` à 50 afin de ne pas être limité par la valeur par défaut de 10.

3.   Ensuite, créez un dossier appelé `components` sous `src` et créez un fichier appelé `Gallery.js` à l'intérieur. `Gatsby` utilise `graphQL` pour interroger les données à partir de diverses sources comme markdown, JSON et Excel.  
  
Dans notre cas, nous utiliserons `Cloudinary` comme source pour interroger les images en utilisant le plugin `gatsby-source-cloudinary` déjà configuré.

4.   Maintenant, modifiez le fichier `Gallery.js` et ajoutez le contenu suivant :

```js

import React from 'react';
import {useStaticQuery, graphql} from 'gatsby';

const Gallery = () => {
    const data = useStaticQuery(
        graphql`
        query CloudinaryImage {
            allCloudinaryMedia {
            edges {
                node {
                    secure_url
                    context {
                        custom {
                            alt
                            caption
                        }
                    }
                    resource_type
                }
            }
            }
        }`
    );
    const images = data.allCloudinaryMedia.edges;
    return (
        <div className="container">
            {images.map((image, index) => (
                <figure className="wave" key={`${index}-image`}>
                    <img 
                        src={image.node.secure_url} 
                        alt={image.node.context.custom.alt} >
                    </img>
                    <figcaption>{image.node.context.custom.caption}</figcaption>
                </figure>
                ))
            }
        </div>
    )
};

export default Gallery;
```

Comme nous le voyons ci-dessus, nous utilisons une requête `graphQL` pour récupérer les chemins des images sources et les informations contextuelles. Nous utilisons ces informations pour parcourir et ajouter les images avec une légende.

5.   L'étape suivante consiste à modifier le fichier `index.js` pour importer le fichier `Gallery.js` et l'utiliser.

```js
import React from 'react';
import Gallery from '../components/Gallery';

export default () => {    
    return (
      <>    
        <Gallery />
      </>        
    )    
}
```

Si vous exécutez déjà `gatsby develop`, veuillez l'arrêter et le relancer. Accédez à nouveau à l'application dans le navigateur. Vous devriez voir l'application avec toutes les images récupérées depuis `Cloudinary`.

Mais attendez, cela ne ressemble pas à ce qui était promis. Nous devons faire un peu de travail `css` ici.

Créez un fichier appelé `gallery.css` sous le dossier `src\components` et ajoutez le contenu suivant :

```css
body {
    background: #000000 url("https://res.cloudinary.com/atapas/image/upload/v1602214656/misc/6284_n48wtw.jpg") repeat-x center top;
    color: #FFFFFF;
}

.container {
    margin-top: 55px;
}

.wave {
    float: left;
    margin: 20px;
    animation: wave 
               ease-in-out 
               1s 
               infinite 
               alternate;
    transform-origin: center -20px;
}

.wave:hover {
    animation-play-state: paused;
}

.wave img {
    border: 5px solid #f8f8f8;
    display: block;
    width: 200px;
    height: 250px;
    background-color: #000;
}

.wave figcaption {
    text-align: center;
}

.wave:after{
    content: '';
    position: absolute;
    width: 20px; 
    height: 20px;
    border: 1.5px solid #ffffff;
    top: -10px; 
    left: 50%;
    z-index: 0;
    border-bottom: none;
    border-right: none;
    transform: rotate(45deg);
}

.wave:before{
    content: '';
    position: absolute;
    top: -23px;
    left: 50%;
    display: block;
    height: 44px;
    width: 47px;
    background-image: url(https://res.cloudinary.com/atapas/image/upload/v1602212639/misc/screw-head_oglfcu.png);
    background-size: 20px 20px;
    background-repeat: no-repeat;
    z-index: 16;
}

@keyframes wave {
    0% { transform: rotate(3deg); }
    100% { transform: rotate(-3deg); }
}
```

6.  Importez le fichier `gallery.css` dans le fichier `Gallery.js` comme suit :

```js
import './gallery.css';
```

C'est tout. Vous devriez voir l'application beaucoup mieux que précédemment, comme si les images étaient accrochées à un mur avec une animation.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/snap-1.jpg)

## **Déployons l'application**

La dernière étape consiste à déployer l'application publiquement afin de la montrer.

Tout d'abord, créez un dépôt sur GitHub et poussez le code source. Ensuite, créez un compte avec [Netlify](https://www.netlify.com/) pour vous connecter.

Suivez ces étapes simples pour déployer votre application sur le CDN Netlify avec un support CI/CD intégré.

* Créez un nouveau site à partir de Git
* Authentifiez-vous à votre compte `Github` et sélectionnez le projet de galerie d'images. Dans mon cas, le nom du projet est `imaginary`.
* Dans l'étape suivante, fournissez des informations sur la commande de build comme `gatsby build` et publiez le répertoire comme `public/`.
* Ensuite, cliquez sur `Site settings` pour indiquer à `netlify` le nom du cloud `Cloudinary`, la clé secrète, la clé API, etc.
* Accédez à l'option `Environment` et cliquez sur le bouton `Edit variables`.
* Ajoutez trois variables comme indiqué ci-dessous avec les valeurs affichées dans votre tableau de bord `Cloudinary`.
* Accédez à l'option `Deploys` et déclenchez un nouveau déploiement.
* Vous pouvez changer le nom du site pour quelque chose qui répond à vos besoins. Dans mon cas, c'est [https://imaginary.netlify.app/](https://imaginary.netlify.app/) :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/1.netlify.png)
_Nouveau site à partir de Git_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/2.netlify.png)
_Créer un nouveau site_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/3.netlify.png)
_Paramètres pour le site_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/4.netlify.png)
_Paramètres du site_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/5.netlify.png)
_Ajouter des variables d'environnement_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/6.netlify.png)
_Ajoutez-les tous_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/7.netlify.png)
_Déclencher un nouveau déploiement_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/8.netlify.png)
_Optionnellement pour changer le nom du site_

Maintenant, nous avons terminé. Nous avons l'application en ligne et en cours d'exécution publiquement.

## **En résumé**

J'espère que vous avez apprécié la lecture de cet article. Dans un prochain article, nous verrons comment utiliser l'autre plugin gatsby-cloudinary pour télécharger une image vers le serveur `Cloudinary` afin de l'ajouter à notre galerie d'images.

Vous pourriez également aimer ces articles :

* [J'ai fait une galerie photo avec une animation CSS. Voici ce que j'ai appris.](https://blog.greenroots.info/i-made-a-photo-gallery-with-css-animation-heres-what-i-learned-ckfzbk6v903ea2xs14l1942f7)
* [JAMstack pour tous : Une introduction](https://blog.greenroots.info/jamstack-for-all-an-introduction-cke2fxc5800jvabs15lhn4a9x)
* [Qu'est-ce qu'un générateur de site statique et comment en choisir un ?](https://blog.greenroots.info/what-is-a-static-site-generator-and-how-to-select-one-cke9xtx5g006p58s11dzg2j16)

Si cet article vous a été utile, veuillez le partager afin que d'autres puissent le lire également. Vous pouvez me mentionner sur Twitter ([@tapasadhikary](https://twitter.com/tapasadhikary)) avec des commentaires, ou n'hésitez pas à me suivre.
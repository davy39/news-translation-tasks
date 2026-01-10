---
title: Tutoriel Next.js Image – Comment téléverser, rogner et redimensionner des images
  dans le navigateur dans Next
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2022-04-18T17:19:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-upload-crop-resize-images-in-the-browser-in-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-cottonbro-5083407.jpg
tags:
- name: image processing
  slug: image-processing
- name: Next.js
  slug: nextjs
seo_title: Tutoriel Next.js Image – Comment téléverser, rogner et redimensionner des
  images dans le navigateur dans Next
seo_desc: 'Two of the most fundamental image editing functions are resizing and cropping.
  But you should do these carefully because they have the potential to degrade image
  quality.

  Cropping always includes removing a portion of the original image, resulting in...'
---

Deux des fonctions d'édition d'image les plus fondamentales sont le redimensionnement et le rognage. Mais vous devez les effectuer avec soin car elles peuvent dégrader la qualité de l'image.

Le rognage implique toujours la suppression d'une partie de l'image originale, ce qui entraîne la perte de certains pixels.

Cet article vous apprendra à téléverser, rogner et redimensionner des images dans le navigateur.


J'ai construit ce projet dans un [Codesandbox](https://codesandbox.io/s/serverless-leaf-vc9rls?file=/pages/index.js). Pour commencer rapidement, fork le [Codesandbox](https://codesandbox.io/s/serverless-leaf-vc9rls?file=/pages/index.js) ou exécutez le projet.


## Prérequis

Pour suivre ce tutoriel, vous devez avoir une certaine expérience avec JavaScript et React.js. L'expérience avec Next.js n'est pas une exigence, mais c'est un plus.

Vous avez également besoin d'un [compte Cloudinary](https://cloudinary.com/users/register/free) pour stocker les fichiers multimédias.

[Cloudinary](https://cloudinary.com/documentation/image_video_and_file_upload#upload_options_overview) offre une API sûre et complète pour téléverser rapidement et efficacement des fichiers multimédias depuis le serveur, le navigateur ou une application mobile.

Enfin, vous aurez besoin de [Next.js](https://nextjs.org/). C'est un framework de développement front-end open-source basé sur React qui permet le rendu côté serveur et la génération de sites web et d'applications statiques.

## Configuration et installation du projet

Utilisez la commande `npx create-next-app` pour échafauder un nouveau projet dans un répertoire de votre choix pour créer un nouveau projet.

Vous pouvez le faire avec la commande :

```
npx create-next-app <nom-du-projet>
```

Pour installer les dépendances, utilisez ces commandes :

```
cd <nom-du-projet> 
npm install cloudinary-react
```

Une fois l'application créée et les dépendances installées, vous verrez un message avec des instructions pour naviguer vers votre site et l'exécuter localement.

Vous pouvez le faire avec la commande :

```
npm run dev
```

Next.js démarrera un environnement de développement avec rechargement à chaud, accessible par défaut à l'adresse `http://localhost:3000`.


## Comment construire l'interface utilisateur

Pour notre projet, nous voulons que l'interface utilisateur permette de téléverser, rogner et redimensionner des images sur la page d'accueil. Nous allons le faire en mettant à jour le fichier `pages/index.js` en un composant :

```
import React, { useState } from "react";
import Head from "next/head";

const IndexPage = () => {

  return (
    <>
      <div className="main">
        <div className="splitdiv" id="leftdiv">
          <h1 className="main-h1">
            Comment rogner, redimensionner et téléverser une image dans le navigateur en utilisant la transformation Cloudinary
          </h1>
          <div id="leftdivcard">
            <h2 className="main-h2">Options de redimensionnement</h2>
          </div>

          <button type="button" id="leftbutton">
            Télécharger l'image
          </button>
        </div>

        <div className="splitdiv" id="rightdiv">
        <h1> L'image apparaîtra ici</h1>
        </div>
      </div>
    </>
  );
};
export default IndexPage;

```

L'interface utilisateur actuelle n'est pas très belle, cependant. Nous allons ajouter un peu de style avec CSS dans le fichier `style.css` comme ceci :

```
@import url("https://fonts.googleapis.com/css?family=Acme|Lobster");

/* Cela me permet d'avoir la largeur complète de la page sans le padding/margin initial*/
body,
html {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  font-family: Acme;
  min-width: 700px;
}

.splitdiv {
  height: 100%;
  width: 50%;
}

/* Cette partie contient tout le côté gauche de l'écran */
/* ----------------------------------------- */
#leftdiv {
  float: left;
  background-color: #fafafa;
  height: 932px;
}

#leftdivcard {
  margin: 0 auto;
  width: 50%;
  background-color: white;
  margin-top: 25vh;
  transform: translateY(-50%);
  box-shadow: 10px 10px 1px 0px rgba(78, 205, 196, 0.2);
  border-radius: 10px;
}

#leftbutton {
  background-color: #512cf3;
  border-radius: 5px;
  color: #fafafa;
  margin-left: 350px;
}

/* ----------------------------------------- */

/* Cette partie contient tout le côté droit de l'écran */
/* ----------------------------------------- */
#rightdiv {
  float: right;
  background-color: #cbcfcf;
  height: 932px;
}

#rightdivcard {
  margin: 0 auto;
  width: 50%;
  margin-top: 50vh;
  transform: translateY(-50%);
  background-position: bottom;
  background-size: 20px 2px;
  background-repeat: repeat-x;
}

/* ----------------------------------------- */

/* Style de base */
/* ----------------------------------------- */

button {
  outline: none !important;
  font-family: Lobster;
  margin-bottom: 15px;
  border: none;
  font-size: 20px;
  padding: 8px;
  padding-left: 20px;
  padding-right: 20px;
  margin-top: -15px;
  cursor: pointer;
}

h1 {
  font-family: Lobster;
  color: #512cf3;
  text-align: center;
  font-size: 40px;
}

input {
  font-family: Acme;
  font-size: 16px;
  font-family: 15px;
}

input {
  width: 30%;
  height: 20px;
  padding: 16px;
  margin-left: 1%;
  margin-right: 2%;
  margin-top: 15px;
  margin-bottom: 10px;
  display: inline-block;
  border: none;
}

input:focus {
  outline: none !important;
  border: 1px solid #512cf3;
  box-shadow: 0 0 1px round #719ece;
}

/* ----------------------------------------- */

.main {
  height: 100%;
  width: 100%;
  display: inline-block;
}

.main-h2 {
  padding-top: 20px;
  text-align: center;
}

.body-h1 {
  padding-top: 20px;
  text-align: center;
  color: white;
}

.inner-p {
  color: white;
  text-align: center;
}

.main-align {
  text-align: center;
}

.form-control {
  margin-left: 15px;
}
```

Notre application devrait maintenant ressembler à ceci sur http://localhost:3000/ :

![Comment téléverser, rogner et redimensionner une image dans le navigateur dans Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1650105687298/eeGTDWFHA.png)

## Comment créer le widget de téléversement d'image

Le widget de téléversement de Cloudinary nous permet de téléverser des actifs multimédias depuis plusieurs sources, y compris Dropbox, Facebook, Instagram et des images prises directement depuis l'appareil photo de notre appareil. Nous utiliserons le widget de téléversement dans ce projet.

Créez un compte Cloudinary gratuit pour obtenir votre nom de cloud et upload_preset.

Les `upload_presets` nous permettent de définir un ensemble de choix de téléversement d'actifs de manière centrale plutôt que de les fournir dans chaque appel de téléversement. Un `nom de cloud` Cloudinary est un identifiant unique associé à votre compte Cloudinary.

Tout d'abord, à partir d'un réseau de diffusion de contenu (CDN), nous ajouterons le fichier JavaScript du widget Cloudinary dans notre `index.js` situé dans `pages/index.js`. Nous inclurons ce fichier en utilisant `next/head` pour inclure toutes les balises meta, ce qui nous permet d'ajouter des données à la partie Head de notre document HTML dans React.

Ensuite, dans le fichier `pages/index.js`, nous importerons Head depuis next/head et ajouterons le fichier script.

```
import React, { useState } from "react";
import Head from "next/head";

const IndexPage = () => {

  return (
    <>
      <Head>
        <title>Comment rogner et redimensionner une image dans le navigateur</title>
        <link rel="icon" href="/favicon.ico" />
        <meta charSet="utf-8" />
        <script
          src="https://widget.cloudinary.com/v2.0/global/all.js"
          type="text/javascript"
        ></script>
      </Head>
      <div className="main">
          [...]
      </div>
    </>
  );
};
export default IndexPage;
```

Dans le fichier `pages/index.js`, nous créerons une instance du widget dans une méthode déclenchée lors du clic sur un bouton et une variable d'état `imagePublicId`.


```
import React, { useState } from "react";
import Head from "next/head";

const IndexPage = () => {
  const [imagePublicId, setImagePublicId] = useState("");

  const openWidget = () => {
    // créer le widget
    const widget = window.cloudinary.createUploadWidget(
      {
        cloudName: "olanetsoft",
        uploadPreset: "w42epls7"
      },
      (error, result) => {
        if (
          result.event === "success" &&
          result.info.resource_type === "image"
        ) {
          console.log(result.info);
          setImagePublicId(result.info.public_id);
        }
      }
    );
    widget.open(); // ouvrir le widget après la création
  };

  return (
    <>
      //...
    </>
  );
};
export default IndexPage;
```

Le widget nécessite notre `cloud_name` et `uploadPreset` de Cloudinary. La fonction `createWidget()` crée un nouveau widget de téléversement. Après avoir téléversé une image avec succès, nous attribuons le `public_id` de l'actif à la variable d'état pertinente.

Pour obtenir notre `cloudname` et `uploadPreset`, nous suivons les étapes ci-dessous :

Vous pouvez obtenir le nom du cloud depuis votre tableau de bord Cloudinary, comme montré ci-dessous.

![Comment téléverser, rogner et redimensionner une image dans le navigateur dans Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1650106671153/wjBrA3_m0.png)

Vous pouvez trouver un preset de téléversement dans l'onglet `Upload` de votre page de paramètres Cloudinary. Vous y accédez en cliquant sur l'icône d'engrenage dans le coin supérieur droit de la page du tableau de bord.

![Comment téléverser, rogner et redimensionner une image dans le navigateur dans Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1650106901391/73lFzuxLQ.png)

![Comment téléverser, rogner et redimensionner une image dans le navigateur dans Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1650106814185/GqnIFsNYS.png)

Faites défiler jusqu'en bas de la page vers la section des presets de téléversement, où vous verrez votre preset de téléversement ou l'option d'en créer un si vous n'en avez pas.

Nous allons procéder à l'appel de la fonction `openWidget` dans le gestionnaire `onClick` de notre bouton de téléversement d'image, comme montré ci-dessous :

```
//...

const IndexPage = () => {
//...
  return (
    <>
     //....
      <div className="main">
        <div className="splitdiv" id="leftdiv">
          //...
          <div id="leftdivcard">
            <h2 className="main-h2">Options de redimensionnement</h2>
             //...
            </div>

          <button type="button" id="leftbutton" onClick={openWidget}>
            Télécharger l'image
          </button>
        </div>

        <div className="splitdiv" id="rightdiv">
        <h1> L'image apparaîtra ici</h1>
        </div>
      </div>
    </>
  );
};
export default IndexPage;

```

Lorsque nous ouvrons notre application dans le navigateur et cliquons sur le bouton `Télécharger l'image`, nous devrions voir quelque chose comme ceci :

![Comment téléverser, rogner et redimensionner une image dans le navigateur dans Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1650111448538/pglrS-Exs.png)

## Comment implémenter des fonctions de transformation personnalisées

Nous devons créer un composant qui gère la transformation en fonction des props qui lui sont passées. Nous allons créer un répertoire `components/` dans le dossier racine. À l'intérieur, nous créerons un fichier appelé `image.js` avec le contenu suivant :

```
import { CloudinaryContext, Transformation, Image } from "cloudinary-react";

const TransformImage = ({ crop, image, width, height }) => {
  return (
    <CloudinaryContext cloudName="olanetsoft">
      <Image publicId={image}>
        <Transformation width={width} height={height} crop={crop} />
      </Image>
    </CloudinaryContext>
  );
};

export default TransformImage;
```

Dans l'extrait de code ci-dessus, nous avons importé `CloudinaryContext`, un composant wrapper Cloudinary utilisé pour gérer les informations partagées entre tous ses composants enfants Cloudinary. Le composant rendu `TransformImage` prend les données de transformation de l'image en tant que props.

Le bloc de code ci-dessus rendra l'image téléversée lorsque nous l'importerons dans `pages/index.js` :

```
//...
import TransformImage from "../components/image";

const IndexPage = () => {
  const [imagePublicId, setImagePublicId] = useState("");
  const [alt, setAlt] = useState("");
  const [crop, setCrop] = useState("scale");
  const [height, setHeight] = useState(200);
  const [width, setWidth] = useState(200);

  return (
    <>
     //...
      <div className="main">
        <div className="splitdiv" id="leftdiv">
          //...
       </div>
        <div className="splitdiv" id="rightdiv">
          <h1> L'image apparaîtra ici</h1>
          <div id="rightdivcard">
            {imagePublicId ? (
              <TransformImage
                crop={crop}
                image={imagePublicId}
                width={width}
                height={height}
              />
            ) : (
              <h1> L'image apparaîtra ici</h1>
            )}
          </div>
        </div>
      </div>
    </>
  );
};
export default IndexPage;
```

Ensuite, nous ajouterons le bouton radio `Options de redimensionnement` afin que nous puissions sélectionner différentes options de redimensionnement et de rognage avec l'extrait de code suivant :

```
//...

const IndexPage = () => {
//...

  return (
    <>
    //...
      <div className="main">
        <div className="splitdiv" id="leftdiv">
          //...
          <div id="leftdivcard">
            <h2 className="main-h2">Options de redimensionnement</h2>

          <label className="form-control">Sélectionner le type de rognage</label>
            <div>
              <label className="form-control">Échelle</label>
              <input
                type="radio"
                value="scale"
                name="crop"
                onChange={(event) => setCrop(event.target.value)}
              />
            </div>
            <div>
              <label className="form-control">Rogner</label>
              <input
                type="radio"
                value="crop"
                name="crop"
                onChange={(event) => setCrop(event.target.value)}
              />
            </div>
            <input
              type="number"
              placeholder="Hauteur"
              onChange={(event) => setHeight(event.target.value)}
            />
            <input
              type="number"
              placeholder="Largeur"
              onChange={(event) => setWidth(event.target.value)}
            />
          </div>

          <button type="button" id="leftbutton" onClick={openWidget}>
            Télécharger l'image
          </button>
        </div>

        <div className="splitdiv" id="rightdiv">
          //...
        </div>
      </div>
    </>
  );
};
export default IndexPage;
```

Dans l'extrait de code ci-dessus, nous avons :

- Ajouté le type de rognage ainsi que les options de largeur et de hauteur
- Ajouté une propriété `onChange` pour suivre les changements dans les champs de saisie de hauteur et de largeur, respectivement

La sortie finale de notre application devrait ressembler à ce que nous avons ci-dessous :


![Comment téléverser, rogner et redimensionner une image dans le navigateur dans Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1650112568692/2htjubfOv.png)


![Comment téléverser, rogner et redimensionner une image dans le navigateur dans Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1650112581661/JnEP--CHC.png)

Voici le dépôt GitHub pour le projet si vous souhaitez consulter le code complet : [https://github.com/Olanetsoft/how-to-upload-crop-and-resize-images-in-the-browser-in-next.js](https://github.com/Olanetsoft/how-to-upload-crop-and-resize-images-in-the-browser-in-next.js)

## Conclusion

Cet article montre comment téléverser, rogner et redimensionner des images dans le navigateur dans Next.js.

## Ressources
 Vous pourriez trouver ces ressources utiles.

- [Référence de l'URL de transformation Cloudinary](https://cloudinary.com/documentation/transformation_reference)
- [Transformation d'image Cloudinary](https://cloudinary.com/documentation/image_transformations)
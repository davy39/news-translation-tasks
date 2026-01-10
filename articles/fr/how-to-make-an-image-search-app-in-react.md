---
title: Comment créer une application de recherche d'images en React en utilisant l'API
  Unsplash
subtitle: ''
author: Ateev Duggal
co_authors: []
series: null
date: '2022-04-04T22:19:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-an-image-search-app-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Unsplash.jpg
tags:
- name: image
  slug: image
- name: React
  slug: react
seo_title: Comment créer une application de recherche d'images en React en utilisant
  l'API Unsplash
seo_desc: 'Unsplash is a site where you can download free and unlicensed images and
  use them as you see fit.

  In this tutorial, we will make an Image Search App using the Unsplash API to get
  access to its enormous collection of images and also download them.

  Bef...'
---

Unsplash est un site où vous pouvez télécharger des images gratuites et libres de droits et les utiliser comme bon vous semble.

Dans ce tutoriel, nous allons créer une application de recherche d'images en utilisant l'API Unsplash pour accéder à sa énorme collection d'images et également les télécharger.

Avant de commencer le développement de notre application, voyons à quoi elle ressemblera exactement [ici](https://unspalsh-app-in-react.vercel.app/).

Commençons...

## Sommaire

1. Comment créer l'application React
   
2. Comment construire l'interface utilisateur de notre application
   
3. Comment obtenir la clé d'accès et le point de terminaison de l'API depuis Unsplash
   
4. Comment utiliser les Hooks dans notre application
   
5. Comment afficher les images dans notre application
   
6. Comment gérer les erreurs
   
7. Conclusion
   

### Que allons-nous apprendre ?

Ce projet est principalement destiné aux débutants, mais toute personne souhaitant rafraîchir ses compétences peut suivre. Dans ce tutoriel, vous apprendrez :

1. Comment obtenir les points de terminaison de l'API et les clés d'accès depuis le tableau de bord des développeurs Unsplash.
   
2. Comment utiliser les hooks useState et useEffect pour récupérer des données depuis l'API.
   
3. Comment utiliser la fonction map pour afficher des images ou toute autre donnée depuis l'API.
   

## Comment créer l'application React

Il est très facile de créer une application React – il suffit d'aller dans votre répertoire de travail dans votre IDE préféré et d'entrer la commande suivante dans le terminal :

```javascript
npx create-react-app image-search-app
```

Si vous n'êtes pas sûr de comment configurer correctement un projet create-react-app, vous pouvez vous référer au guide officiel ici à [create-react-app-dev](https://create-react-app.dev/docs/getting-started/).

Après la configuration, exécutez npm start dans le même terminal pour démarrer localhost:3000 où notre application React sera hébergée. Nous pouvons également voir toutes nos modifications là-bas.

## Comment construire l'interface utilisateur de notre application

Il y aura deux sections dans l'interface utilisateur de notre application :

1. La section d'entrée
   
2. La section des résultats où nous afficherons les images
   

Dans la section d'entrée, nous avons une balise input dans laquelle nous écrirons le terme de recherche ou la requête. Nous avons également un bouton avec un gestionnaire d'événements **onClick** qui déclenchera la fonction responsable de la récupération des données depuis l'API.

```html
import React from "react";
const App = () => {
  return (
    <>
      <div className="container-fluid">
        <div className="row">
          <div className="col-12 d-flex justify-content-center align-items-center input">
            <input
              className="col-3 form-control-sm py-1 fs-4 text-capitalize border border-3 border-dark"
              type="text"
              placeholder="Rechercher quelque chose..."
            />
            <button
              type="submit"
              onClick={Submit}
              className="btn bg-dark text-white fs-3 mx-3"
            >
              Rechercher
            </button>
          </div>
        </div>
      </div>
    </>
  );
};
export default App;
```

Le résultat sera le suivant :

![Image](https://lh4.googleusercontent.com/qzIWk69MB4RvIfXj7neJ3mhg1q3G1S96r42xsyVFIEcU7IUXBUiT4H7dMP7mSDDHiVOtM1LAycPF2DO5pN6_wanvWbgyED1K3YmeXvE7uNuiYYImV8e7CNXGY4kB0_9B8du3Qxi2 align="left")

Dans cet article, nous ne discuterons pas de la partie stylisation de l'application. Ainsi, nous pouvons rester plus concentrés sur la partie React qui est plus nécessaire à comprendre.

## Comment obtenir la clé d'accès et le point de terminaison de l'API depuis Unsplash

Obtenons ces clés d'API depuis [Unsplash pour les développeurs](https://unsplash.com/developers). Suivez les étapes ci-dessous pour obtenir votre clé d'API et autres détails :

Tout d'abord, allez sur le lien ci-dessus et cliquez sur s'inscrire en tant que développeur.

![Image](https://lh6.googleusercontent.com/xB8Tb3HKYAGv5b7ArmtT6zuU3aGTF_uO6-9kiTiFEBlEmsNkUJagAmzq1zI64RAasNivbO2uFpYe6lC9qcK6-BCjwy2V-p-qX-UqdvjCJO-y6Kjm_bpmRNwr_q277Vc-GKwcIqG_ align="left")

Ensuite, remplissez les informations d'identification demandées :

![Image](https://lh3.googleusercontent.com/uMKaffa_5TJDMRHXl8WUCsUc3MxcyAAlwVbkCVpkbQ8c21qfV_8U9c2toKfJ-WcLj387vgJhTN54xq8MoCJO82cO68eAePTmUd7RqinyYG4659h8LazgueEWlrhEZEV0EbcO-psH align="left")

Après cela, vous serez dirigé vers le tableau de bord du développeur. Cliquez sur le nouveau projet.

![Image](https://lh6.googleusercontent.com/_FQN1PymEdAKDYwB0YR7MeUL6Ab6nPyLUkCb40SBg6jZNZj7vnxLnSRVu24NALBfbanpdF4qxze9p9xba8CRZWfTtCjp6PmNv7o12fUip3pLYAvHKqq16-d3bO7_897Df_mUQ_l4 align="left")

Vous serez invité à accepter tous les termes écrits là. Lisez-les si vous le souhaitez ou cochez simplement tous les termes et cliquez sur le bouton à la fin pour continuer.

![Image](https://lh5.googleusercontent.com/IcLYr5HycXD28nEgtLF4_6Tj6Waa9XAU5B1GHf1Z-5Mrmils4seAa4gvY4kearxFkJhe0hv7p3IFau9iQdbF8a8YGVVZ-TF56y8P5T68YPWZ8H1A-ipAiVs6tONFl2kYYojQNSWa align="left")

Ensuite, un formulaire modal apparaîtra comme montré ci-dessous dans lequel vous devrez écrire les informations de l'application comme le nom et la description.

Ensuite, cliquez sur Créer une application.

![Image](https://lh3.googleusercontent.com/1Av2BfGSaXi0S9Bib2qkcaxcgioFUGMRqveNWKyMATeJG-cHkpCKAfNh4KQP4ztvhMQ7R1jcBe4x4gRnMoSbpr0oxmczqxCscgFmALMpQDSo6Zm3CLbyZbUVx7n4BF2DO75l_qVv align="left")

Maintenant que notre application a été créée, nous pouvons accéder à la **Clé d'accès** et à la **Clé secrète** sous la **Section des clés** :

![Image](https://lh5.googleusercontent.com/PWKObP8aBkr8dipYCoq5lkkRC1TYbgrZcoNbo0DeunoNsoXMMqYayleGDwCjig9iXZ4eSrq4bNgsLoQ9e5Q7ohMKw9VDoajmSmvo8sI7aZKnDV3amuVRd_7agognh90R8Fkou_cs align="left")

Remarquez qu'au tout début de cette page, il est écrit **Demo**. Cela signifie que notre application a été acceptée mais est toujours en mode développement.

Dans ce mode, nous ne pouvons faire que 50 requêtes par heure. Si nous dépassons cette limite, notre API ne fonctionnera pas et les images ne se chargeront pas.

![Image](https://lh3.googleusercontent.com/iPG7K3Wl9-HOuQbAmrnhyDq5u-tplTZJ56YbDKHMpgIJ4wANdSQPBBjN_fWMPR-89RvEvEG9yYiOWGyUCnU-Qh88EXC7z1rfJ_IvnfsHhXJ5YFVMT6GkaG8WsvT4ZHlJbU86D951 align="left")

Après cela, dirigez-vous vers la documentation et sélectionnez l'option « **Rechercher des photos par mot-clé** ».

![Image](https://lh6.googleusercontent.com/4cMwgogWv858cVvy78oWmNce-GC0rZBSpFaadMh_eO-qbJ3pVHMPL90b_dUQNonSj9-NeRxvhM9hj5JZGuViTjFESmIo5m6yRWUS-gtrEuh5TA5ugLT9PCxvgbZ-3oPdbKZ9pl_z align="left")

Faites défiler jusqu'à la section **Réponse** et copiez le lien comme indiqué :

![Image](https://lh4.googleusercontent.com/3ORXGCncj8J8CxUwTYP4tesP9F-IjFSCADrAQQ0KN4DcrlmjepMvmaudZc5PZTUfzPkFdjI9IdRnDa2JYHabqJgsPHKccboA9wiDMg3SaoV9nA554OjIzRKYOHQ_g2I_p2-uJk75 align="left")

*Point de terminaison de l'API*

Maintenant, nous avons à la fois notre **clé d'API et le point de terminaison de l'API**. Continuons avec notre application.

## Comment utiliser les Hooks dans notre application

Nous utiliserons les hooks useState et useEffect dans notre application. Ils nous permettront de définir les états nécessaires pour obtenir la valeur de l'entrée et rechercher dans l'API les données concernant cette valeur.

Pour que les hooks fonctionnent, nous devons les définir tout en haut de notre application comme ceci :

```javascript
import React, { useState, useEffect } from "react";
```

### Comment définir l'état en utilisant le hook useState

Comme nous l'avons discuté ci-dessus, nous utiliserons des hooks pour extraire des données de l'API en utilisant la valeur recherchée dans le champ d'entrée. Cette valeur sera lue par notre application React en utilisant le hook useState.

Nous définissons des états en utilisant ce hook pour des objectifs spécifiques. Dans cette application, nous en définirons deux : l'un pour obtenir la valeur du champ d'entrée et l'autre pour afficher les résultats récupérés depuis l'API.

```javascript
const [img, setImg] = useState("");
const [res, setRes] = useState([]);
```

Il y a deux paramètres dans le code ci-dessus utilisés pour définir le hook useState : l'un d'eux est l'état que nous utiliserons pour stocker les valeurs, et l'autre est la fonction que nous utiliserons pour mettre à jour les valeurs de l'état. Lisez plus sur le [hook useState ici](https://tekolio.com/what-is-the-usestate-hook-in-react/).

Nous avons défini le premier état comme une chaîne vide car il sera utilisé pour stocker l'entrée de la barre de recherche (et c'est aussi une chaîne).

L'autre état est initialisé comme un tableau vide car il stockera les données récupérées depuis l'API et les affichera ensuite dans notre section de résultats.

Par défaut, nous ne pouvons obtenir que jusqu'à 10 points de données par API, mais nous pouvons dépasser cela en utilisant un paramètre **per\_page** que nous verrons plus tard dans ce tutoriel.

### Comment utiliser l'état img

L'étape suivante consiste à stocker la valeur du champ de texte d'entrée dans l'état **img** en utilisant l'attribut value de la balise input. Ensuite, nous ajoutons un gestionnaire d'événements onChange(). Ce gestionnaire d'événements onChange() aura une fonction qui sera utilisée pour mettre à jour l'état en utilisant **e.target.value.**

```html
<input
  className="col-3 form-control-sm py-1 fs-4 text-capitalize border border-3 border-dark"
  type="text"
  placeholder="Rechercher quelque chose..."
  value={img}
  onChange={(e) => setImg(e.target.value)}
/>;
```

### Comment faire des requêtes API à Unsplash en utilisant le hook useEffect

Nous allons maintenant utiliser l'API Unsplash et la clé d'accès que nous avons acquise dans l'étape précédente pour récupérer des données et les afficher dans notre application.

Pour cela, nous aurons à nouveau besoin d'un état pour stocker les données récupérées depuis l'API, que nous avons déjà défini dans la section précédente (**res**, qui est initialisé comme un tableau vide à cette fin uniquement).

Il existe de nombreuses méthodes en JavaScript que nous pouvons utiliser pour récupérer des données depuis une API, mais nous utiliserons la méthode async-await – c'est de loin la plus simple.

```javascript
const fetchRequest = async () => {
  const data = await fetch(
    `https://api.unsplash.com/search/photos?page=1&query=${img}&client_id=${Access_Key}`
  );
  const dataJ = await data.json();
  const result = dataJ.results;
  console.log(result);
  setRes(result);
};
useEffect(() => {
  fetchRequest();
}, []);
```

Remarquez que nous avons écrit `${Access_Key}` – ici, nous devons écrire notre clé d'accès. Nous complétons cette étape pour sécuriser notre clé d'API car n'importe qui peut en abuser.

Dans Unsplash, nous pouvons également demander la production de notre application, et en faisant cela, nous pouvons passer en ligne avec les images qu'Unsplash a à offrir.

Pour cette raison, tout le monde obtient un ensemble différent de clés d'accès et de clés de sécurité. Il est toujours préférable de cacher ces clés aux autres afin qu'elles ne soient pas mal utilisées et que nous en payions le prix.

Dans le code ci-dessus, nous avons initialement stocké les données récupérées depuis l'API dans la variable **data** qui est ensuite convertie en JSON pour simplifier. Cela nous permet de lire les données et d'extraire les valeurs nécessaires, qui sont stockées dans la variable **dataJ** et affichées dans la console pour vérifier si nous obtenons la valeur dont nous avons besoin ou non.

![Image](https://lh4.googleusercontent.com/U32k-__bIyqEnF_2xPC1zT293GOGH7bY-_TVWbdzhfcSkMMMbuNC1bgExFM-HETrJJvVcFC1VzunOWtJ4hq1Gh72mmuPwv6A71V-QD0luGl42wJ6gmUlQTrtj-l4tp2Ay1FjuUP1 align="left")

*API au format JSON*

Et si nous ouvrons l'un des résultats de recherche ci-dessus pour voir quelles valeurs nous pouvons extraire :

```json
{
    "total": 133,
    "total_pages": 7,
    "results": [
    {
    "id": "eOLpJytrbsQ",
    "created_at": "2014-11-18T14:35:36-05:00",
    width: 4000,
    height: 3000,
    color: "#A7A2A1",
    blur_hash: "LaLXMa9Fx[D%~q%MtQM|kDRjtRIU",
    likes: 286,
    liked_by_user: false,
    description: "Un homme buvant un café.",
    user: {
    id: "Ul0QVz12Goo",
    username: "ugmonk",
    name: "Jeff Sheldon",
    first_name: "Jeff",
    last_name: "Sheldon",
    instagram_username: "instantgrammer",
    twitter_username: "ugmonk",
    portfolio_url: "http://ugmonk.com/",
    profile_image: {
    small:
    "https://images.unsplash.com/profile-1441298803695-accd94000cac?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=32&w=32&s=7cfe3b93750cb0c93e2f7caec08b5a41",
    medium:
    "https://images.unsplash.com/profile-1441298803695-accd94000cac?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=64&w=64&s=5a9dc749c43ce5bd60870b129a40902f",
    large:
    "https://images.unsplash.com/profile-1441298803695-accd94000cac?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128&s=32085a077889586df88bfbe406692202",
    },
    links: {
    self: "https://api.unsplash.com/users/ugmonk",
    html: "http://unsplash.com/@ugmonk",
    photos: "https://api.unsplash.com/users/ugmonk/photos",
    likes: "https://api.unsplash.com/users/ugmonk/likes",
    },
    },
    current_user_collections: [],
    urls: {
    raw: "https://images.unsplash.com/photo-1416339306562-f3d12fefd36f",
    full: "https://hd.unsplash.com/photo-1416339306562-f3d12fefd36f",
    regular:
    "https://images.unsplash.com/photo-1416339306562-f3d12fefd36f?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&s=92f3e02f63678acc8416d044e189f515",
    small:
    "https://images.unsplash.com/photo-1416339306562-f3d12fefd36f?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&s=263af33585f9d32af39d165b000845eb",
    thumb:
    "https://images.unsplash.com/photo-1416339306562-f3d12fefd36f?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=8aae34cf35df31a592f0bef16e6342ef",
    },
    links: {
    self: "https://api.unsplash.com/photos/eOLpJytrbsQ",
    html: "http://unsplash.com/photos/eOLpJytrbsQ",
    download: "http://unsplash.com/photos/eOLpJytrbsQ/download",
    },
    },
    // plus de photos ...
    ],
    },
```

Il est préférable d'utiliser cette fonction à l'intérieur du hook useEffect car cela empêchera tout re-rendu des données si nous avons apporté des modifications à l'interface utilisateur de notre application. Pour comprendre useEffect en profondeur, [cliquez ici](https://tekolio.com/explaining-useeffect-hook-in-react/).

Nous utilisons la fonction **setRes** pour mettre à jour la valeur de **res** d'un tableau vide à un tableau qui stockera toutes les données récupérées au format JSON comme montré ci-dessus.

Nous avons déjà donné une fonction onClick au bouton au début de notre application dans la section d'entrée. Il est maintenant temps de définir une fonction pour ce gestionnaire d'événements qui sera déclenché dès que le bouton Rechercher sera cliqué. Cette fonction appellera la fonction **fetchRequest** qui récupérera les données et nous montrera le résultat dans la section des résultats.

```javascript
const Submit = () => {
  fetchRequest();
  setImg("");
};
```

## Comment afficher les images dans notre application

Dans la section précédente, nous avons stocké les données récupérées depuis l'API dans l'état **res** qui les a stockées sous la forme d'un tableau. Pour obtenir ces valeurs, nous devons utiliser la méthode map.

```html
<div className="col-12 d-flex justify-content-evenly flex-wrap">
  {res.map((val) => {
    return (
      <>
        <img
          className="col-3 img-fluid img-thumbnail"
          src={val.urls.small}
          alt="val.alt_description"
        />
      </>
    );
  })}
</div>;
```

Si nous revenons en arrière et regardons la réponse en JSON, nous trouverons un type d'information différent : **URLs** qui contient le chemin vers l'image. Donc ici **val.urls.small** est le chemin réel vers l'image, et **val.alt\_description** est la description alternative de l'image.

Il existe différents champs à l'intérieur de "urls" qui donnent différentes données, tels que :

* **Raw** : Image brute réelle qui a été prise par un utilisateur.
   
* **Full** : Image brute au format .jpg.
   
* **Regular** : Meilleur pour les usages pratiques, largeur=1080px.
   
* **Small** : Parfait pour une vitesse internet lente, largeur=400px.
   
* **Thumb** : Version miniature de l'image, largeur=200px.
   

Dans cet article, nous utiliserons small, mais il y en a d'autres comme montré ci-dessus avec lesquels nous pouvons jouer et trouver celui qui nous convient le mieux.

![Image](https://lh4.googleusercontent.com/W8UFqJV3_yVh1-Ntvljzv09XXDjxgMwl9L_6ZiX9M5ZRAKAIbShkvJEF4XaN-UD_yI1c7o7K9s1rC5kTmuDGAaEfWDPTV4vYeIj8DUIWn57x7Y6buR8WLgRwP-oJNTHn9MHo-1iY align="left")

*Produit final*

Par défaut, le nombre d'éléments qui peuvent être récupérés à la fois est de 10, mais ce nombre peut être augmenté ou diminué en fonction du nombre d'images que nous voulons que notre application affiche.

Pour cela, nous devons simplement ajouter un paramètre à la fin de notre appel API (**per\_page**) comme montré dans le code, et le mettre égal au nombre d'images que nous voulons afficher.

```javascript
const fetchRequest = async () => {
  const data = await fetch(
    `https://api.unsplash.com/search/photos?page=1&query=${img}&client_id=${Access_Key}&per_page=20`
  );
  const dataJ = await data.json();
  const result = dataJ.results;
  console.log(result);
  setRes(result);
};
```

Il existe de nombreux autres paramètres qu'Unsplash a à offrir. Ci-dessous se trouve une liste de quelques-uns d'entre eux :

![Image](https://lh5.googleusercontent.com/zFYDDwnZ52Cx7NUoKL31GiT_87ZeQQ0B9LZeMGShHsXUmu94FbvZHxYJnEOymSoxq-gy2RMItMppHP8cgTmJSB34djJf02Ae0Ji2nXtPbpB91muUg6D3gYrwq69fvrcAu8YVWbqv align="left")

*Paramètres de l'API Unsplash*

## Comment gérer les erreurs

Si nous faisons une recherche rapide maintenant sur, par exemple, des drapeaux, nous obtiendrons nos images. Mais il y a encore quelques problèmes à corriger. L'un d'eux est l'erreur que nous recevons dans la console.

![Image](https://lh4.googleusercontent.com/nNglt_EjKldYnndufDLUOsK1yxvJmywsrjK3XOmm11jhEs3EfuIudjqahEvzJRt9JBtypzpWZDsE3QBgATN9ry7vD5vPrK42zeux23YBcVQ4NzvWcYNsL1Ha6X6YP1QoK7zZRCSm align="left")

*Erreur dans la console*

Pour corriger cela, passez une clé unique à chaque enfant en utilisant l'id de l'image. Cette propriété clé indique explicitement à React l'identité de chaque enfant dans une liste. Cela empêche également les enfants de perdre leur état entre les rendus.

```html
<div className="col-12 d-flex justify-content-evenly flex-wrap">
  {res.map((val) => {
    return (
      <>
        <img
          key={val.id}
          className="col-3 img-fluid img-thumbnail"
          src={val.urls.small}
          alt="val.alt_description"
        />
      </>
    );
  })}
</div>;
```

## Conclusion

Dans ce tutoriel, nous avons développé une application de recherche de photos en React en utilisant l'API Unsplash. En construisant notre application, nous avons discuté de nombreuses choses comme comment utiliser les hooks React pour obtenir des données depuis une API et les utiliser pour afficher des images dans notre application.

Il y a beaucoup plus que vous pouvez faire avec cette application pour l'étendre. Par exemple, nous pourrions ajouter un bouton aléatoire pour afficher des images aléatoires, créer une case à cocher pour basculer entre la recherche de photos ou des utilisateurs qui les ont publiées selon la préférence de l'utilisateur, ajouter un [défilement infini](https://www.npmjs.com/package/react-infinite-scroll-component) pour afficher plus d'images, et plus encore.

Vous pouvez parcourir certains de mes autres articles basés sur des projets et adaptés aux débutants ici :

1. [Comment créer un tableau en React en utilisant des hooks avec plusieurs fonctionnalités](https://tekolio.com/how-to-make-a-table-in-react-with-hooks/)
   
2. [Comment j'ai fait mon portfolio en React](https://tekolio.com/how-i-made-my-portfolio-in-react/)
   
3. [Comment créer un composant de filtre en React](https://www.freecodecamp.org/news/how-to-make-a-filter-component-in-react/)
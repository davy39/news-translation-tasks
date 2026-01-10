---
title: Comment construire un clone de YouTube avec React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-02-10T16:55:49.000Z'
originalURL: https://freecodecamp.org/news/build-youtube-with-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/how-to-build-youtube-with-react.png
tags:
- name: React
  slug: react
- name: Web Applications
  slug: web-applications
- name: youtube
  slug: youtube
seo_title: Comment construire un clone de YouTube avec React
seo_desc: 'In this tutorial, you will get an in-depth overview of how you can build
  a complete YouTube clone using React in 10 steps.

  I will lay out how I built a clone of the YouTube web app and the concrete steps
  you can take in order to build your own along ...'
---

Dans ce tutoriel, vous obtiendrez un aperçu approfondi de la manière dont vous pouvez construire un clone complet de YouTube en utilisant React en 10 étapes.

Je vais expliquer comment j'ai construit un clone de l'application web YouTube et les étapes concrètes que vous pouvez suivre pour construire le vôtre, ainsi que d'autres applications basées sur la vidéo similaires.

À travers ce guide, nous allons couvrir comment construire des applications web puissantes avec React et Node en utilisant une pile de technologies essentielles, ainsi que la manière dont chaque outil contribue à créer la fonctionnalité globale de notre application. 

Commençons !

## Étape 1 : Modéliser nos données et créer notre base de données

Notre application se compose de deux parties principales, notre backend Node et notre frontend React.

Notre backend sera responsable de choses comme l'authentification et l'autorisation pour connecter les utilisateurs et s'assurer qu'ils peuvent accéder au bon contenu. Il sera également responsable de fournir nos données vidéo (comme la vidéo elle-même et si nous l'avons aimée ou non) et les données liées à l'utilisateur (comme le profil de chaque utilisateur). 

Le backend va faire tout cela en interagissant avec notre base de données. La base de données que nous allons utiliser est la base de données SQL Postgres. Un outil appelé Prisma sera responsable de la modélisation de ces données (pour dire à notre base de données quelles données elle va stocker).

> Prisma est ce qu'on appelle un **ORM** ou un mappeur relationnel d'objets. Il fait le travail de gestion de la manière dont nos données sont structurées dans notre base de données, y compris les relations que toutes nos données partagent les unes avec les autres à travers des **modèles**.

Notre application sera composée de six modèles de données principaux : `User`, `Comment`, `Subscription`, `Video`, `VideoLike`, et `View` data.

Vous pouvez voir la version finale de notre schéma ci-dessous :

```js
// prisma.schema

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id           String         @id @default(uuid())
  createdAt    DateTime       @default(now())
  username     String
  email        String         @unique
  avatar       String         @default("https://reedbarger.nyc3.digitaloceanspaces.com/default-avatar.png")
  cover        String         @default("https://reedbarger.nyc3.digitaloceanspaces.com/default-cover-banner.png")
  about        String         @default("")
  videos       Video[]
  videoLikes   VideoLike[]
  comments     Comment[]
  subscribers  Subscription[] @relation("subscriber")
  subscribedTo Subscription[] @relation("subscribedTo")
  views        View[]
}

model Comment {
  id        String   @id @default(uuid())
  createdAt DateTime @default(now())
  text      String
  userId    String
  videoId   String
  user      User     @relation(fields: [userId], references: [id])
  video     Video    @relation(fields: [videoId], references: [id])
}

model Subscription {
  id             String   @id @default(uuid())
  createdAt      DateTime @default(now())
  subscriberId   String
  subscribedToId String
  subscriber     User     @relation("subscriber", fields: [subscriberId], references: [id])
  subscribedTo   User     @relation("subscribedTo", fields: [subscribedToId], references: [id])
}

model Video {
  id          String      @id @default(uuid())
  createdAt   DateTime    @default(now())
  title       String
  description String?
  url         String
  thumbnail   String
  userId      String
  user        User        @relation(fields: [userId], references: [id])
  videoLikes  VideoLike[]
  comments    Comment[]
  views       View[]
}

model VideoLike {
  id        String   @id @default(uuid())
  createdAt DateTime @default(now())
  like      Int      @default(0)
  userId    String
  videoId   String
  user      User     @relation(fields: [userId], references: [id])
  video     Video    @relation(fields: [videoId], references: [id])
}

model View {
  id        String   @id @default(uuid())
  createdAt DateTime @default(now())
  userId    String?
  videoId   String
  user      User?    @relation(fields: [userId], references: [id])
  video     Video    @relation(fields: [videoId], references: [id])
}
```

Chacun de ces modèles inclut diverses propriétés avec leurs types de données associés. 

Dans la première colonne de chaque modèle se trouvent les différents champs ou propriétés individuelles dont chaque modèle est composé, comme l'`id` ou identifiant unique ou l'horodatage `createdAt` lorsque la base de données a créé une entrée donnée. 

> Vous pouvez penser à chaque modèle comme un type spécial d'objet JavaScript avec des propriétés spéciales que nous créons dans notre schéma.

Si nous regardons la deuxième colonne, nous pouvons voir quel doit être le type de données de chaque champ. Ces valeurs correspondent largement aux types JavaScript normaux : chaînes de caractères, entiers et dates.

Les types associés peuvent également être différents modèles de données. Par exemple, en regardant notre modèle `User`, nous voyons qu'il a un champ `videos`, qui a un type de données de `Video[]`, ce qui signifie qu'il s'agit d'un tableau de type de données `Video`. 

Cela a du sens - chaque utilisateur peut logiquement avoir plusieurs vidéos qu'il a créées. Il en va de même pour leurs likes, commentaires, abonnés, utilisateurs auxquels ils se sont abonnés, et leurs vues vidéo. 

## Étape 2 : Créer des routes Auth, Video et User

Maintenant que nous avons créé notre schéma, nous pouvons créer la logique métier pour notre backend. 

Nous allons utiliser Node avec la bibliothèque Express pour construire notre backend. Express rend très facile la construction d'API puissantes, ce qui est exactement ce dont nous avons besoin pour notre application YouTube. 

La plus grande partie de notre API sera les routes, ou points de terminaison individuels auxquels notre application React fera des requêtes pour des données. Nous aurons un routage séparé pour l'authentification, les vidéos et les ressources liées aux utilisateurs qui commenceront comme suit :

```
http://localhost:3001/api/v1/auth
http://localhost:3001/api/v1/videos
http://localhost:3001/api/v1/users
```

Je ne vais pas passer en revue toutes les routes individuelles que nous devons créer, mais juste pour vous donner une idée de ce à quoi elles ressemblent, examinons les routes liées aux vidéos. 

```js
// server/src/routes/video.js

import { PrismaClient } from "@prisma/client";
import express from "express";

const prisma = new PrismaClient();

function getVideoRoutes() {
  const router = express.Router();

  router.get("/", getRecommendedVideos);
  router.get("/trending", getTrendingVideos);
   
  // ... beaucoup d'autres routes omises

  return router;
}

export async function getVideoViews(videos) {
  for (const video of videos) {
    const views = await prisma.view.count({
      where: {
        videoId: {
          equals: video.id,
        },
      },
    });
    video.views = views;
  }
  return videos;
}

async function getRecommendedVideos(req, res) {
  let videos = await prisma.video.findMany({
    include: {
      user: true,
    },
    orderBy: {
      createdAt: "desc",
    },
  });

  if (!videos.length) {
    return res.status(200).json({ videos });
  }

  videos = await getVideoViews(videos);

  res.status(200).json({ videos });
}

async function getTrendingVideos(req, res) {
  let videos = await prisma.video.findMany({
    include: {
      user: true,
    },
    orderBy: {
      createdAt: "desc",
    },
  });

  if (!videos.length) {
    return res.status(200).json({ videos });
  }

  videos = await getVideoViews(videos);
  videos.sort((a, b) => b.views - a.views);

  res.status(200).json({ videos });
}
```

Nous utilisons `express.Router` pour ajouter toutes nos sous-routes à la route principale (`/api/v1/videos`) en utilisant la fonction `getVideoRoutes`. Nous créons une route individuelle en spécifiant quel type de requête peut être fait avec la méthode appropriée : `get`, `post`, `put`, ou `delete`.

Nous passons à cette méthode le point de terminaison auquel nous voulons que notre frontend fasse la requête ainsi qu'une fonction pour gérer les requêtes entrantes à ce point de terminaison.

> Ces fonctions sous nos routes qui sont utilisées pour gérer les requêtes pour chacun de nos points de terminaison API sont communément appelées **contrôleurs**.

Vous pouvez voir certains des contrôleurs que nous utilisons ici, comme `getRecommendedVideos` ou `getTrendingVideos`. Leurs noms rendent claire la fonction qu'ils remplissent.

Par exemple, si notre application React fait une requête GET à `/api/v1/videos/`, notre contrôleur répond avec les vidéos recommandées de l'utilisateur. 

> Notez qu'à l'intérieur de chaque contrôleur, nous utilisons `PrismaClient` pour interagir avec notre base de données, qui a été générée à partir du fichier `prisma.schema` que nous avons créé.

Pour notre contrôleur `getRecommendedVideos`, nous utilisons la méthode `findMany` pour obtenir plusieurs vidéos (un tableau de celles-ci), où les données utilisateur pour chaque vidéo sont incluses (avec l'opérateur `include` pour le champ `user`).

Et nous trions les résultats par le champ `createdAt` du plus récent au plus ancien (avec `desc` ou dans l'ordre décroissant).

## Étape 3 : Protéger les routes Auth avec un Middleware

En plus de nos contrôleurs, il y a un middleware important que nous devons associer à certaines de nos routes. 

> Qu'est-ce que le middleware ? **Middleware** sont des fonctions qui sont utilisées pour s'exécuter avant une autre fonction afin de fournir une valeur ou d'effectuer une action. Dans notre cas, le middleware s'exécutera avant notre fonction de contrôleur pour chaque route.

Lorsque l'utilisateur souhaite obtenir les vidéos qu'il a aimées, nous devons d'abord écrire un middleware qui obtiendra l'utilisateur actuel avant que notre contrôleur ne tente de répondre avec les données utilisateur. 

```js
// server/src/routes/user.js

import { PrismaClient } from "@prisma/client";
import express from "express";
import { protect } from "../middleware/authorization";

const prisma = new PrismaClient();

function getUserRoutes() {
  const router = express.Router();

  router.get("/liked-videos", protect, getLikedVideos);
    
  return router;
}
```

Le middleware `protect` est placé avant `getLikedVideos`, ce qui signifie qu'il s'exécutera en premier.

Le code de la fonction `protect` est fourni ci-dessous :

```js
// server/src/middleware/authorization.js

import { PrismaClient } from "@prisma/client";
import jwt from "jsonwebtoken";

const prisma = new PrismaClient();

export async function protect(req, res, next) {
  if (!req.cookies.token) {
    return next({
      message: "Vous devez être connecté pour visiter cette route",
      statusCode: 401,
    });
  }

  try {
    const token = req.cookies.token;
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    const user = await prisma.user.findUnique({
      where: {
        id: decoded.id,
      },
      include: {
        videos: true,
      },
    });

    req.user = user;
    next();
  } catch (error) {
    next({
      message: "Vous devez être connecté pour visiter cette route",
      statusCode: 401,
    });
  }
}
```

Dans notre fonction middleware `protect`, si nous n'avons pas d'utilisateur ou si l'utilisateur a un JSON Web Token invalide, nous utilisons la fonction `next` pour répondre au client avec une erreur 401. 

> Un code d'erreur 401 signifie que l'utilisateur actuel n'est pas autorisé à accéder à une ressource particulière qu'il demande. 

Sinon, si l'utilisateur a un token valide, nous le récupérons avec notre Prisma Client et le passons à notre contrôleur `getLikedVideos`. Nous pouvons le faire en ajoutant une propriété à l'objet de requête ou `req` puis en appelant la fonction `next` (qui est également une fonction middleware).

Le middleware est essentiel dans notre application principalement pour des choses comme l'autorisation pour obtenir notre utilisateur actuellement authentifié ainsi que pour protéger les points de terminaison qui incluent des informations sécurisées.

Le middleware est également utile pour gérer les erreurs dans notre backend, afin que nous nous en remettions avec succès et que nous assurions que notre application ne se casse pas lorsqu'il y a une erreur.

## Étape 4 : Créer les pages et styles du client React

Passons au frontend React, nous pouvons facilement créer notre application React pour consommer notre API Node avec l'aide de Create React App. 

[Pour commencer avec Create React App](https://reedbarger.com/create-react-app-10-steps), vous pouvez simplement exécuter la commande à la racine de votre dossier de projet :

```bash
npx create-react-app client
```

Après la fin de l'installation, nous aurons une application React placée dans le dossier `client`, juste à côté de notre code serveur dans le dossier `server`.

La première étape avec notre application React est de configurer toutes les routes individuelles pour notre application. Celles-ci seront placées dans le composant App.js et correspondront aux routes que YouTube a pour leur application :

```js
// client/src/App.js

import React from "react";
import { Route, Switch } from "react-router-dom";
import MobileNavbar from "./components/MobileNavbar";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import { useLocationChange } from "./hooks/use-location-change";
import Channel from "./pages/Channel";
import History from "./pages/History";
import Home from "./pages/Home";
import Library from "./pages/Library";
import LikedVideos from "./pages/LikedVideos";
import NotFound from "./pages/NotFound";
import SearchResults from "./pages/SearchResults";
import Subscriptions from "./pages/Subscriptions";
import Trending from "./pages/Trending";
import WatchVideo from "./pages/WatchVideo";
import YourVideos from "./pages/YourVideos";
import Container from "./styles/Container";

function App() {
  const [isSidebarOpen, setSidebarOpen] = React.useState(false);
  const handleCloseSidebar = () => setSidebarOpen(false);
  const toggleSidebarOpen = () => setSidebarOpen(!isSidebarOpen);
  useLocationChange(handleCloseSidebar);

  return (
    <>
      <Navbar toggleSidebarOpen={toggleSidebarOpen} />
      <Sidebar isSidebarOpen={isSidebarOpen} />
      <MobileNavbar />
      <Container>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/watch/:videoId" component={WatchVideo} />
          <Route path="/channel/:channelId" component={Channel} />
          <Route path="/results/:searchQuery" component={SearchResults} />
          <Route path="/feed/trending" component={Trending} />
          <Route path="/feed/subscriptions" component={Subscriptions} />
          <Route path="/feed/library" component={Library} />
          <Route path="/feed/history" component={History} />
          <Route path="/feed/my_videos" component={YourVideos} />
          <Route path="/feed/liked_videos" component={LikedVideos} />
          <Route path="*" component={NotFound} />
        </Switch>
      </Container>
    </>
  );
}
```

Pour notre Router et toutes nos Routes, nous utilisons la bibliothèque `react-router-dom`, qui nous donnera également quelques hooks React utiles pour accéder à des valeurs comme les paramètres de route (`useParams`) et naviguer notre utilisateur de manière programmatique dans l'application (`useHistory`).

En ce qui concerne la construction de l'apparence de notre application, nous allons utiliser une bibliothèque appelée `styled-components`. Ce qui est très utile avec les composants stylisés, c'est que c'est une bibliothèque **CSS-in-JS**. 

> L'avantage d'une bibliothèque CSS-in-JS est que nous pouvons écrire des styles CSS dans nos fichiers .js. Elle nous permet d'utiliser des fonctionnalités React et JavaScript que nous ne pourrions pas utiliser dans une feuille de style CSS normale. 

Nous pouvons passer certaines valeurs en tant que props à nos composants stylisés tout comme nous le ferions pour un composant react normal. 

Voici donc un exemple de l'un de nos composants stylisés, où nous définissons conditionnellement plusieurs règles de style en fonction de la valeur de la prop `red`.

Comme vous l'avez peut-être deviné, en passant la prop blue avec une valeur de true à notre composant Button stylisé, il rend notre bouton de couleur rouge YouTube.

```js
// client/src/styles/Button.js

import styled, { css } from "styled-components";

const Button = styled.button`
  padding: 10px 16px;
  border-radius: 1px;
  font-weight: 400;
  font-size: 14px;
  font-size: 0.875rem;
  font-weight: 500;
  line-height: 1.75;
  text-transform: uppercase;
  letter-spacing: 0.02857em;

  ${(props) =>
    props.red &&
    css`
      background: ${(props) => props.theme.darkRed};
      border: 1px solid ${(props) => props.theme.darkRed};
      color: white;
    `}
`;

export default Button;
```

Voici comment nous utiliserions le composant stylisé `Button` que nous avons créé ci-dessus avec la prop `red` qui lui est passée :

```js
// exemple d'utilisation :
import React from "react";
import Button from "../styles/Button";
import Wrapper from "../styles/EditProfile";

function EditProfile() {
  return (
    <Wrapper>
      <div>
        <Button red onClick={() => setShowModal(true)}>
          Edit Profile
        </Button>
      </div>
    </Wrapper> 
  );
```

Un autre avantage de l'utilisation des composants stylisés est qu'ils nous donnent des **styles scopés**. 

En d'autres termes, les styles écrits dans un composant stylisé seront appliqués uniquement au composant dans lequel ils sont utilisés et nulle part ailleurs dans notre application. 

Cela est très différent par rapport aux feuilles de style CSS normales, où si vous les incluez dans leur application, elles sont globales, elles sont appliquées à l'ensemble de l'application. 

## Étape 5 : Ajouter l'authentification du client avec Google OAuth

L'étape suivante consiste à ajouter l'authentification avec l'aide de Google OAuth. 

C'est quelque chose qui est très facile à configurer avec l'aide d'une bibliothèque appelée `react-google-login`. Elle nous donne à la fois un hook personnalisé ainsi qu'un composant React spécial que nous pouvons utiliser pour connecter notre utilisateur s'il a un compte Google.

Ci-dessous se trouve le code utilisé pour le composant `GoogleAuth` qu'un utilisateur peut presser pour se connecter immédiatement en utilisant une fenêtre modale popup de Google :

```js
// client/src/components/GoogleAuth.js

import React from "react";
import Button from "../styles/Auth";
import { SignInIcon } from "./Icons";
import { GoogleLogin } from "react-google-login";
import { authenticate } from "../utils/api-client";

function GoogleAuth() {
  return (
    <GoogleLogin
      clientId="votre-id-client-de-google-oauth"
      cookiePolicy="single_host_origin"
      onSuccess={authenticate}
      onFailure={authenticate}
      render={(renderProps) => (
        <Button
          tabIndex={0}
          type="button"
          onClick={renderProps.onClick}
          disabled={renderProps.disabled}
        >
          <span className="outer">
            <span className="inner">
              <SignInIcon />
            </span>
            se connecter
          </span>
        </Button>
      )}
    />
  );
}

export default GoogleAuth;
```

## Étape 6 : Récupérer facilement des données en utilisant React Query

Une fois que nous sommes en mesure d'authentifier nos utilisateurs, nous pouvons passer à la création de nos pages ou du contenu des pages et commencer à faire des requêtes à nos points de terminaison API. 

L'une des bibliothèques les plus complètes et les plus simples pour faire des requêtes HTTP s'appelle `axios`. De plus, la manière la plus facile de faire des requêtes à travers les composants React est avec une bibliothèque spéciale appelée `react-query`. 

Ce qui est très utile avec React Query, ce sont ses hooks React personnalisés. Ils rendent possible non seulement la demande de données, mais ils nous permettent également de mettre en cache (sauvegarder) les résultats de chaque requête que nous faisons, afin de ne pas avoir à récupérer à nouveau les données si elles sont déjà dans notre cache local. 

En d'autres termes, React Query est une bibliothèque puissante de récupération de données et de gestion d'état, le tout en un.

Voici un exemple rapide de la manière dont j'ai utilisé React Query pour demander toutes les vidéos recommandées pour les utilisateurs sur la page d'accueil. 

```js
// client/src/pages/Home.js

import axios from "axios";
import React from "react";
import { useQuery } from "react-query";
import ErrorMessage from "../components/ErrorMessage";
import VideoCard from "../components/VideoCard";
import HomeSkeleton from "../skeletons/HomeSkeleton";
import Wrapper from "../styles/Home";
import VideoGrid from "../styles/VideoGrid";

function Home() {
  const {
    data: videos,
    isSuccess,
    isLoading,
    isError,
    error,
  } = useQuery("Home", () =>
    axios.get("/videos").then((res) => res.data.videos)
  );

  if (isLoading) return <HomeSkeleton />;
  if (isError) return <ErrorMessage error={error} />;

  return (
    <Wrapper>
      <VideoGrid>
        {isSuccess
          ? videos.map((video) => <VideoCard key={video.id} video={video} />)
          : null}
      </VideoGrid>
    </Wrapper>
  );
}

export default Home;
```

Si nous sommes dans un état de chargement, nous affichons un squelette de chargement comme le fait l'application YouTube. Si une erreur se produit, nous affichons un message d'erreur dans la page. 

Sinon, si la requête a réussi, nous affichons les vidéos que notre backend recommande à notre utilisateur.

## Étape 7 : Télécharger et lire les vidéos des utilisateurs

Pour télécharger nos vidéos, nous allons utiliser la bibliothèque Cloudinary. 

Nous pouvons télécharger une vidéo de React vers Cloudinary en utilisant une entrée de fichier, avec laquelle nous sélectionnerons notre fichier vidéo depuis notre ordinateur et ferons ensuite une requête à l'API Cloudinary. Elle nous donnera ensuite une URL une fois la vidéo téléchargée sur ses serveurs. 

À partir de là, l'utilisateur pourra fournir les informations de sa vidéo. Une fois qu'il appuie sur publier, nous pouvons sauvegarder les informations de sa vidéo dans notre base de données. 

En ce qui concerne l'affichage des vidéos créées par les utilisateurs, nous allons utiliser une bibliothèque open source appelée `video.js`. 

Pour regarder une vidéo individuelle, nous devrons récupérer la vidéo selon son id. Après cela, nous passerons l'URL au lecteur video.js, qui donnera à l'utilisateur la possibilité de faire défiler la vidéo, de la mettre en plein écran et de changer le volume. 

```js
// client/src/components/VideoPlayer.js

import React from "react";
import videojs from "video.js";
import "video.js/dist/video-js.css";
import { addVideoView } from "../utils/api-client";

function VideoPlayer({ video }) {
  const videoRef = React.useRef();

  const { id, url, thumbnail } = video;

  React.useEffect(() => {
    const vjsPlayer = videojs(videoRef.current);

    vjsPlayer.poster(thumbnail);
    vjsPlayer.src(url);

    vjsPlayer.on("ended", () => {
      addVideoView(id);
    });
  }, [id, thumbnail, url]);

  return (
    <div data-vjs-player>
      <video
        controls
        ref={videoRef}
        className="video-js vjs-fluid vjs-big-play-centered"
      ></video>
    </div>
  );
}

export default VideoPlayer;
```

Sous la vidéo, l'utilisateur pourra ajouter des commentaires, aimer ou ne pas aimer la vidéo, ainsi que s'abonner à la chaîne de l'auteur de la vidéo. 

Toutes ces différentes fonctionnalités seront rendues possibles en faisant des requêtes réseau à nos points de terminaison API appropriés (à nouveau, en utilisant `axios`).

## Étape 8 : Protéger les actions Auth avec un hook personnalisé

Une fois que nous avons créé beaucoup de cette fonctionnalité, nous devons verrouiller certaines actions pour les utilisateurs qui ne sont pas authentifiés.

Nous ne voulons pas que des utilisateurs non autorisés puissent tenter de se connecter, créer un commentaire ou aimer une vidéo, etc. Ce sont toutes des actions que seuls certains utilisateurs authentifiés devraient pouvoir effectuer. 

En conséquence, nous pouvons créer un hook personnalisé afin de protéger une action authentifiée. La raison de la création de ce hook est de permettre une réutilisation facile dans nos nombreux composants qui utilisent des actions authentifiées.

Ce hook personnalisé s'appellera `useAuthAction`.

```js
// client/src/hooks/use-auth-action.js

import { useGoogleLogin } from "react-google-login";
import { useAuth } from "../context/auth-context";
import { authenticate } from "../utils/api-client";

export default function useAuthAction() {
  const user = useAuth();
  const { signIn } = useGoogleLogin({
    onSuccess: authenticate,
    clientId: "votre-id-client",
  });

  function handleAuthAction(authAction, data) {
    if (user) {
      authAction(data);
    } else {
      signIn();
    }
  }

  return handleAuthAction;
}
```

La fonction `handleAuthAction` sera retournée par notre hook et acceptera une fonction que nous voulons exécuter comme argument, telle que les fonctions pour aimer ou ne pas aimer une vidéo. 

`handleAuthAction` acceptera l'argument de la fonction comme second argument :

```js
// client/src/pages/WatchVideo.js

function WatchVideo() {
  const handleAuthAction = useAuthAction();

  function handleLikeVideo() {
    handleAuthAction(likeVideo, video.id);
  }

  function handleDislikeVideo() {
    handleAuthAction(dislikeVideo, video.id);
  }

  function handleToggleSubscribe() {
    handleAuthAction(toggleSubscribeUser, video.user.id);
  }

// reste du composant
}
```

Si un utilisateur non authentifié tente de se connecter ou de créer un commentaire, au lieu de faire des requêtes à notre API pour créer un commentaire, il sera automatiquement connecté via le hook `useGoogleLogin` de la bibliothèque `react-google-login`.

## Étape 9 : Modifier les données de la chaîne de l'utilisateur

À ce stade, nous avons affiché toutes les vidéos que nos utilisateurs ont aimées, leur historique de visionnage, les chaînesqu'ils suivent, les vidéos tendances, et bien plus encore. 

Enfin, nous allons également afficher la chaîne de chaque utilisateur et rendre possible pour eux de changer leurs informations utilisateur telles que leur nom d'utilisateur, bio, avatar et image de couverture. 

Ces téléchargements d'images seront effectués une fois de plus avec Cloudinary. Les utilisateurs pourront sélectionner l'image qu'ils souhaitent utiliser comme images d'avatar de couverture. Nous allons faire des requêtes à l'API Cloudinary pour obtenir une URL que nous prendrons ensuite et mettrons à jour les informations de nos utilisateurs avec. 

Toutes ces modifications seront rendues possibles avec une modale que nous allons créer. Nous la créerons avec le package `@reach/dialog` qui nous donnera une modale conçue avec l'accessibilité à l'esprit et que nous pourrons styliser comme nous le souhaitons.

Voici le code que nous utiliserons à l'intérieur de notre modale pour télécharger les images de nos utilisateurs et mettre à jour leur chaîne.

```js
// client/src/components/EditChannelModal.js

import React from "react";
import { useSnackbar } from "react-simple-snackbar";
import Button from "../styles/Button";
import Wrapper from "../styles/EditChannelModal";
import { updateUser } from "../utils/api-client";
import { uploadMedia } from "../utils/upload-media";
import { CloseIcon } from "./Icons";

function EditChannelModal({ channel, closeModal }) {
  const [openSnackbar] = useSnackbar();
  const [cover, setCover] = React.useState(channel.cover);
  const [avatar, setAvatar] = React.useState(channel.avatar);

  async function handleCoverUpload(event) {
    const file = event.target.files[0];

    if (file) {
      const cover = await uploadMedia({
        type: "image",
        file,
        preset: "votre-preset-de-couverture",
      });
      setCover(cover);
    }
  }

  async function handleAvatarUpload(event) {
    const file = event.target.files[0];

    if (file) {
      const avatar = await uploadMedia({
        type: "image",
        file,
        preset: "votre-preset-davatar",
      });
      setAvatar(avatar);
    }
  }

  async function handleEditChannel(event) {
    event.preventDefault();
    const username = event.target.elements.username.value;
    const about = event.target.elements.about.value;

    if (!username.trim()) {
      return openSnackbar("Le nom d'utilisateur ne peut pas être vide");
    }

    const user = {
      username,
      about,
      avatar,
      cover,
    };

    await updateUser(user);
    openSnackbar("Chaîne mise à jour");
    closeModal();
  }

  return (
    <Wrapper>
      <div className="edit-channel">
        <form onSubmit={handleEditChannel}>
          <div className="modal-header">
            <h3>
              <CloseIcon onClick={closeModal} />
              <span>Modifier la chaîne</span>
            </h3>
            <Button type="submit">Enregistrer</Button>
          </div>

          <div className="cover-upload-container">
            <label htmlFor="cover-upload">
              <img
                className="pointer"
                width="100%"
                height="200px"
                src={cover}
                alt="couverture"
              />
            </label>
            <input
              id="cover-upload"
              type="file"
              accept="image/*"
              style={{ display: "none" }}
              onChange={handleCoverUpload}
            />
          </div>

          <div className="avatar-upload-icon">
            <label htmlFor="avatar-upload">
              <img src={avatar} className="pointer avatar lg" alt="avatar" />
            </label>
            <input
              id="avatar-upload"
              type="file"
              accept="image/*"
              style={{ display: "none" }}
              onChange={handleAvatarUpload}
            />
          </div>
          <input
            type="text"
            placeholder="Insérer le nom d'utilisateur"
            id="username"
            defaultValue={channel.username}
            required
          />
          <textarea
            id="about"
            placeholder="Parlez aux spectateurs de votre chaîne"
            defaultValue={channel.about}
          />
        </form>
      </div>
    </Wrapper>
  );
}

export default EditChannelModal;
```

## Étape 10 : Publier notre application sur le Web

Une fois que nous avons ajouté toutes les fonctionnalités que nous voulons, nous allons [utiliser Heroku pour déployer notre application React et Node](https://reedbarger.com/react-app-node-backend) sur le web. 

Tout d'abord, nous devons ajouter un script postinstall à notre fichier package.json Node qui indiquera à Heroku de construire automatiquement notre application React lors du déploiement :

```json
{
  "name": "server",
  "version": "0.1.0",
  "scripts": {
    "start": "node server",
    ...
    "postinstall": "cd client && npm install && npm run build"
  }
}

```

Pour pouvoir dire à notre backend Node que nous voulons le déployer avec un frontend React sur le même domaine, nous devons ajouter le morceau de code suivant à l'endroit où notre application Express est créée, après tout le middleware :

```js
// server/src/start.js

if (process.env.NODE_ENV === "production") {
    app.use(express.static(path.resolve(__dirname, "../client/build")));

    app.get("*", function (req, res) {
      res.sendFile(path.resolve(__dirname, "../client/build", "index.html"));
    });
}
```

Le code ci-dessus dit : si une requête GET est faite à notre application, mais non gérée par notre API, répondre avec la version construite de notre client React. 

En d'autres termes, si nous ne demandons pas de données au backend, envoyer le client React construit à nos utilisateurs.

## Conclusion

Espérons que ce tutoriel vous a donné quelques idées sur la manière de structurer votre prochain projet React, surtout si vous voulez construire des applications impressionnantes comme YouTube.

## Devenir un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*
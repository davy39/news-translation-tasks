---
title: Comment créer un graphique en temps réel avec React, HighCharts et Pusher
subtitle: ''
author: Andrew Baisden
co_authors: []
series: null
date: '2024-05-02T00:07:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-realtime-chart-with-react-and-pusher
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/pusher-banner.png
tags:
- name: charts
  slug: charts
- name: React
  slug: react
- name: websocket
  slug: websocket
seo_title: Comment créer un graphique en temps réel avec React, HighCharts et Pusher
seo_desc: "In today's tutorial, you are going to learn about WebSockets and how you\
  \ can use them to create interactive realtime data applications. \nTo illustrate\
  \ just how innovative real time technologies are, we will build a chart application\
  \ which automatical..."
---

Dans le tutoriel d'aujourd'hui, vous allez apprendre les WebSockets et comment les utiliser pour créer des applications de données interactives en temps réel. 

Pour illustrer à quel point les technologies en temps réel sont innovantes, nous allons construire une application de graphique qui se met à jour automatiquement avec de nouvelles données dynamiques en ligne.

Ce sera un très bon exemple de la manière dont nous pouvons implémenter les données utilisateur dans des produits commerciaux utiles tels que les tableaux de classement sportifs, les analyses de médias sociaux, les suiveurs financiers, les instruments médicaux, les jeux et bien plus encore.

Comme vous pouvez le voir, il existe de nombreux cas d'utilisation pour cette technologie. Alors, commençons et apprenons d'abord la principale plateforme que nous allons utiliser pour créer nos données en temps réel : [Pusher](https://pusher.com/).

Vous pouvez trouver le [code source en ligne ici](https://github.com/andrewbaisden/realtime-chart-pusher).

## Prérequis

* Un IDE/éditeur de code installé
* Connaissance de base de JavaScript et React
* Compréhension de Node.js et npm
* Un compte sur [Pusher](https://pusher.com/)

## Table des matières

1. [Qu'est-ce que les WebSockets ?](#heading-quest-ce-que-les-websockets)
2. [Qu'est-ce que Pusher ?](#heading-quest-ce-que-pusher)
3. [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
4. [Comment créer un compte sur Pusher](#heading-comment-creer-un-compte-sur-pusher)
5. [Comment construire l'application de revenu annuel de l'entreprise](#heading-comment-construire-lapplication-de-revenu-annuel-de-lentreprise)
6. [Conclusion](#heading-conclusion)

## Qu'est-ce que les WebSockets ?

Les WebSockets sont un protocole de communication qui permet aux données de voyager de manière bidirectionnelle entre un client et un serveur. Cela signifie essentiellement qu'il est possible pour un client et un serveur d'envoyer des données simultanément et indépendamment l'un de l'autre. 

Pouvoir envoyer des données de cette manière apporte de nombreux avantages, tels que la prévention du blocage. Cela peut se produire si le système n'est capable que d'envoyer ou de recevoir, mais pas les deux en même temps.

Un autre avantage est le fait que la connexion du protocole de contrôle de transmission (TCP) reste active et connectée. C'est un inconvénient des connexions traditionnelles du protocole de transfert hypertexte (HTTP), car elles s'ouvrent et se ferment régulièrement chaque fois qu'il y a une requête ou une réponse. Cela empêche la communication d'être instantanée et en temps réel. 

Ne pas avoir à se soucier de l'ouverture et de la fermeture des connexions entraîne une réduction dramatique du trafic réseau – donc en termes de vitesse et de ressources, c'est un bonus bienvenu.

Maintenant que vous savez pourquoi les WebSockets sont utiles, examinons Pusher et voyons ce que la plateforme est capable de faire.

## Qu'est-ce que Pusher ?

Pusher est une plateforme en ligne que vous pouvez utiliser pour construire et développer des applications nécessitant une communication en temps réel. Ces communications ont généralement lieu entre des navigateurs web, des téléphones mobiles et d'autres appareils connectés à Internet. 

La plateforme est conçue pour faciliter la mise en œuvre de systèmes de communication en temps réel qui sont bien moins compliqués que les connexions WebSocket brutes en termes de configuration et de gestion. Cela permet une meilleure mise à l'échelle et même une manière de gérer les replis pour les environnements hérités qui ne supportent pas les WebSockets.

Pusher est capable d'utiliser de nombreuses technologies telles que les WebSockets, les replis HTTP, et même son propre protocole propriétaire appelé `ws-longpolling`. Cela permet à la plateforme de fonctionner dans des endroits où les WebSockets ne sont pas supportés.

Pusher possède également de nombreuses autres fonctionnalités utiles. Par exemple, il supporte pleinement les WebSockets, donc la communication bidirectionnelle fonctionne comme vous vous y attendez. La plateforme suit également le modèle de publication-abonnement (Pub/Sub) qui est un modèle de messagerie populaire utilisé dans l'industrie. Il garantit pratiquement que toute personne abonnée à l'un des canaux peut recevoir les messages en temps réel.

Un bon exemple de cela serait tout le monde recevant la dernière notification d'actualités qui est abonné à ce canal de médias sociaux. Les abonnements peuvent être publics et privés, ce qui nécessite une authentification pour accéder à ces messages. 

Il y a également un large support de plateforme, car le SDK de Pusher est disponible dans différents langages de programmation comme JavaScript, Python, iOS, Android et bien d'autres. Il est disponible en tant que service en ligne, donc toute l'infrastructure de mise à l'échelle et de communication est déjà gérée. Cela signifie un système de moins pour les développeurs à gérer lors de la construction d'une application.

Pusher est une excellente option, comme je l'espère vous pouvez le constater. Mais il existe d'autres outils qui font des choses similaires :

* [PubNub](https://www.pubnub.com/)
* [deepstreamHub](https://deepstreamhub.com/)
* [AWS IoT](https://aws.amazon.com/iot/)
* [AWS SNS](https://aws.amazon.com/sns/)
* [Google Cloud Pub/Sub](https://cloud.google.com/pubsub)
* [Fanout](https://fanout.io/)

D'accord, vous avez appris beaucoup de choses sur les WebSockets et Pusher. Maintenant, nous allons examiner l'application que nous allons construire.

## Ce que nous allons construire

Pour vous aider à apprendre comment Pusher fonctionne, nous allons construire une application de tableau de bord de revenu annuel d'entreprise. L'application dispose d'un graphique, d'un bouton de bascule en mode 3D et de trois boutons.

Nous allons construire notre application en utilisant [Next.js](https://nextjs.org/), [Pusher](https://pusher.com/), et [HighCharts](https://www.highcharts.com/docs/index) (l'outil que nous utiliserons pour créer notre composant de graphique). Ce sera une application full stack avec un endpoint API pour notre API REST Pusher. Nous avons juste besoin d'un endpoint GET qui se connectera à l'API Pusher.

Les données du graphique proviendront directement de Pusher, et le bouton de bascule en mode 3D nous permet essentiellement de basculer notre graphique entre les modes 2D et 3D. Les boutons nous permettent de changer le type de graphique affiché à l'écran, et les trois graphiques peuvent fonctionner en mode 2D et 3D. Le graphique dispose de certaines données de départ, et de nouvelles données sont automatiquement ajoutées à la fin pour chaque nouvelle année.

Ici, vous pouvez voir notre application de revenu annuel d'entreprise en mode graphique 2D.

![Application de revenu annuel d'entreprise en mode graphique 2D](https://res.cloudinary.com/d74fh3kw/image/upload/v1714407050/company-annual-income_ww5d4g.png)
_Application de revenu annuel d'entreprise en mode 2D_

Et ici, vous pouvez voir notre application de revenu annuel d'entreprise en mode graphique 3D.

![Application de revenu annuel d'entreprise en mode graphique 3D](https://res.cloudinary.com/d74fh3kw/image/upload/v1714407667/company-annual-income-3d_fxjm1p.png)
_Application de revenu annuel d'entreprise en mode 3D_

Comme vous pouvez le voir, la bibliothèque HighCharts est très performante lorsqu'il s'agit de construire des applications nécessitant une visualisation de données. Si vous êtes intéressé par d'autres bibliothèques qui fonctionnent tout aussi bien, j'ai dressé une liste de certaines d'entre elles ici. Chacune a ses propres avantages uniques et il est possible d'utiliser plus d'une bibliothèque si vous le souhaitez :

* [Chart.js](https://www.chartjs.org/)
* [D3](https://d3js.org/)
* [Recharts](https://recharts.org/en-US)
* [Google Charts](https://developers.google.com/chart)
* [Apex Charts](https://apexcharts.com/)
* [dyagraphs](https://dygraphs.com/)
* [Victory](https://commerce.nearform.com/open-source/victory/)

D'accord, nous savons ce que nous allons construire. Dans la section suivante, nous allons rapidement passer en revue comment créer un compte sur Pusher, suivi de la construction réelle de notre application par la suite.

## Comment créer un compte sur Pusher

Créer un compte sur Pusher ne nécessite que quelques étapes. Selon le moment où vous suivez ce tutoriel, le site web peut sembler un peu différent – mais le processus d'inscription devrait être le même.

Commencez par aller sur le site [Pusher](https://pusher.com/) comme indiqué ci-dessous :

![Page d'accueil du site web de Pusher](https://res.cloudinary.com/d74fh3kw/image/upload/v1714409546/pusher-website-home_fvngyq.png)
_Page d'accueil du site web de Pusher_

Cliquez soit sur le bouton Obtenez votre compte gratuit au milieu de la page, soit sur le bouton S'inscrire dans le coin supérieur droit.

Vous devriez maintenant être sur la page d'inscription comme indiqué ici :

![Page d'inscription du site web de Pusher](https://res.cloudinary.com/d74fh3kw/image/upload/v1714409766/pusher-website-signup_zpihwa.png)
_Page d'inscription du site web de Pusher pour un compte_

Utilisez soit votre compte GitHub, Google, ou votre email pour créer un compte.

La page suivante à charger devrait être votre tableau de bord principal après avoir terminé l'inscription comme indiqué dans l'image ci-dessous :

![Page des canaux de Pusher](https://res.cloudinary.com/d74fh3kw/image/upload/v1714410240/pusher-channels_wqpt2l.png)
_Page principale du tableau de bord du site web de Pusher_

  
Cliquez sur le bouton Gérer dans la section Canaux dans l'image montrée ci-dessus pour accéder à la page des Canaux.

La page des Canaux peut être vue ci-dessous qui affiche toutes les données pour notre application.

![Page des Canaux du site web de Pusher](https://res.cloudinary.com/d74fh3kw/image/upload/v1714410477/pusher-website-create-app_iorisl.png)
_Page des Canaux du site web de Pusher_

Nous devons créer une application, alors cliquez sur le bouton Créer une application dans le coin supérieur droit.

En cliquant sur le bouton devrait vous donner cette boîte de création de votre application Channels comme montré ici :

![Écran de création de votre application Channels du site web de Pusher](https://res.cloudinary.com/d74fh3kw/image/upload/v1714410628/pusher-website-create-channels-app_gsyb8z.png)
_Page de création de votre application channels du site web de Pusher_

Donnez un nom à votre application puis choisissez React pour le front-end et Node.js pour le back-end. Ensuite, cliquez sur le bouton Créer une application en bas du formulaire.

C'est tout – vous devriez maintenant voir l'écran principal de votre application comme montré dans l'image d'exemple ci-dessous (avec les données de connexions et de messages affichées au milieu). La barre latérale de gauche contient les fonctionnalités et les clés d'application dont nous avons besoin pour une utilisation ultérieure.

![Page de vue d'ensemble de l'application du site web de Pusher](https://res.cloudinary.com/d74fh3kw/image/upload/v1714411607/pusher-website-app-overview_lsrhxl.png)
_Page de l'application du site web de Pusher_

Super ! Ensuite, nous allons commencer à construire notre application... alors commençons.

## Comment construire l'application de revenu annuel de l'entreprise

La première chose que nous devons faire est de configurer l'architecture de notre projet et la structure des dossiers, alors commençons par cela. Créez un dossier sur votre ordinateur appelé `realtime-chart-pusher` puis `cd` dedans.

Créez un projet Next.js en exécutant la commande d'installation et de configuration habituelle ici :

```shell
npx create-next-app .

```

Sur l'écran de configuration, notre projet doit utiliser Tailwind CSS pour le style et il est recommandé d'utiliser l'App Router. Les autres paramètres par défaut devraient convenir.

Maintenant, nous devons installer nos dépendances pour le projet. Allez-y et faites-le avec cette commande :

```shell
npm i axios highcharts-react-official pusher pusher-js

```

Voici un bref aperçu de l'objectif de chaque package que nous installons :

* Axios : pour faire des requêtes API à notre backend API qui est connecté à l'API Pusher
* highcharts-react-official : pour construire notre graphique en temps réel
* pusher et pusher-js : pour se connecter à notre compte Pusher et à l'API Pusher

Bien, cela étant fait, nous devons simplement configurer nos fichiers de projet. Vous pouvez utiliser ce script d'exécution dans votre terminal tout en restant dans le dossier racine du projet :

```shell
touch .env.local
cd src/app
mkdir -p api/pusher components/ChartButton components/CompanyIncomeChart components/Toggle3DButton
touch api/pusher/route.js
touch components/ChartButton/ChartButton.js components/CompanyIncomeChart/CompanyIncomeChart.js components/Toggle3DButton/Toggle3DButton.js

```

Ce script crée un fichier `.env.local` pour nos clés d'application Pusher. Il crée également des fichiers et des dossiers pour notre backend et notre frontend.

Avant de commencer à ajouter le code à notre base de code, nous devons obtenir nos clés d'application Pusher. Vous pouvez les trouver sur votre compte Pusher comme montré dans cet exemple ci-dessous :

![Écran des clés d'application Pusher](https://res.cloudinary.com/d74fh3kw/image/upload/v1714580536/pusher-app-keys_rihysv.png)
_Page des clés d'application du site web de Pusher_

Ajoutez vos clés d'application au fichier `.env.local` comme dans cet exemple de code ici :

```shell
NEXT_SECRET_PUSHER_APP_ID = "votreid"
NEXT_SECRET_PUSHER_KEY = "votrecle"
NEXT_SECRET_PUSHER_SECRET = "votresecret"
NEXT_SECRET_PUSHER_CLUSTER = "votreemplacement"

```

Nous avons simplement ajouté `NEXT_SECRET` au début de toutes les variables car c'est une convention Next.js et cela garantit que les variables fonctionnent correctement.

Maintenant, nous pouvons commencer avec la majeure partie de notre base de code. Tout d'abord, nous allons travailler sur le fichier `route.js` à l'intérieur du dossier `api/route`. Voici le code nécessaire pour le fichier :

```javascript
import Pusher from 'pusher';

const pusher = new Pusher({
  appId: process.env.NEXT_SECRET_PUSHER_APP_ID,
  key: process.env.NEXT_SECRET_PUSHER_KEY,
  secret: process.env.NEXT_SECRET_PUSHER_SECRET,
  cluster: process.env.NEXT_SECRET_PUSHER_CLUSTER,
  useTLS: true,
});

export async function GET() {
  // Définir la valeur initiale
  const value = Math.random() * 800000 + 200000;

  setInterval(() => {
    pusher.trigger('company-income', 'new-price', {
      value: value,
    });

    return Response.json({ value: value }, { status: 200 });
    // Toutes les dix secondes, la méthode setInterval obtiendra des données de l'API car sa valeur est définie sur dix secondes. Les plans gratuits de Pusher sont limités à 200 000 messages par jour, alors soyez prudent en réduisant l'intervalle ou vous risquez de dépasser votre limite trop tôt.
  }, 10000);
  return Response.json({ value: value }, { status: 200 });
}

```

Le code de ce fichier nous permet de nous connecter à Pusher en utilisant nos clés d'application. La `valeur` est un nombre généré aléatoirement qui est envoyé en JSON à notre canal Pusher. Ce nombre est ce que nous utilisons pour montrer le revenu de l'entreprise chaque nouvelle année qui est automatiquement générée dans notre graphique.

Cette mise à jour se produit toutes les 10 secondes et peut être modifiée dans la fonction `setInterval`. Les plans gratuits de Pusher sont limités à 200 000 messages par jour, alors soyez prudent en réduisant l'intervalle ou vous risquez de dépasser votre limite trop tôt.

Le fichier suivant sur lequel nous allons travailler est le fichier `ChartButton.js` que vous pouvez trouver dans son dossier `ChartButton`.

Ajoutez ce code au fichier :

```javascript
export default function ChartButton({ chartRef, type, name }) {
  const switchToLineChart = () => {
    chartRef.current.update({
      chart: {
        type: type,
      },
    });
  };

  return (
    <button
      onClick={() => switchToLineChart()}
      className="bg-indigo-500 hover:bg-indigo-700 p-2 rounded text-white shadow-md"
    >
      {name}
    </button>
  );
}

```

Notre application de graphique dispose de trois boutons pour le graphique en aires, le graphique en barres et le graphique en lignes. Ce composant crée essentiellement les boutons.

Bien, ensuite nous aurons notre fichier `CompanyIncomeChart.js` que vous pouvez trouver dans le dossier `CompanyIncomeChart`. Ce fichier prendra ce code ici :

```javascript
'use client';

import { useEffect, useRef, useState } from 'react';
import axios from 'axios';
import ChartButton from '../ChartButton/ChartButton';
import Toggle3DButton from '../Toggle3DButton/Toggle3DButton';

export default function CompanyIncome() {
  const initialData = [
    [1965, 360202],
    [1966, 400123],
    [1967, 460331],
    [1968, 460346],
    [1969, 460339],
    [1970, 460370],
  ];

  const chartRef = useRef(null);
  const [chartData, setChartData] = useState([...initialData]);
  const [toggle3D, setToggle3D] = useState(false);

  useEffect(() => {
    // Importer dynamiquement Highcharts et son module 3D
    import('highcharts/highcharts-3d').then((Highcharts3D) => {
      import('highcharts').then((Highcharts) => {
        Highcharts3D.default(Highcharts.default);

        chartRef.current = Highcharts.default.chart('chart-container', {
          colors: ['#F3F7FB', '#F3F7FB'],
          chart: {
            style: {
              fontFamily: ['Prompt', 'sans-serif'],
              fontSize: '16px',
            },
            type: 'column',
            options3d: {
              enabled: toggle3D,
              alpha: 10,
              beta: 25,
              depth: 70,
              viewDistance: 25,
            },
            backgroundColor: {
              linearGradient: [0, 0, 500, 500],
              stops: [
                [0, 'rgb(128, 130, 221)'],
                [1, 'rgb(128, 130, 221)'],
              ],
            },
          },
          title: {
            text: 'REVENU ANNUEL DE L\'ENTREPRISE',
            style: {
              fontSize: '27px',
            },
          },
          xAxis: {
            title: {
              text: 'Année',
              style: {
                color: 'white',
              },
            },
            labels: {
              style: {
                color: 'white',
              },
            },
            type: 'category',
          },
          yAxis: {
            title: {
              text: 'Revenu',
              style: {
                color: 'white',
              },
            },
            labels: {
              style: {
                color: 'white',
              },
            },
            min: 0,
          },
          credits: {
            text: '',
          },
          series: [
            {
              name: 'Revenu',
              data: chartData,
            },
          ],
          animation: {
            duration: 100,
          },
        });
      });
    });

    const interval = setInterval(async () => {
      try {
        const response = await axios.get('/api/pusher');
        const newDataPoint = [
          chartData[chartData.length - 1][0] + 1,
          response.data.value,
        ];
        chartRef.current.series[0].addPoint(newDataPoint, true, true);
        setChartData((prevData) => [...prevData, newDataPoint]);
      } catch (error) {
        console.error('Erreur lors de la récupération des données :', error);
      }
      // Toutes les dix secondes, la méthode setInterval obtiendra des données de l'API car sa valeur est définie sur dix secondes. Les plans gratuits de Pusher sont limités à 200 000 messages par jour, alors soyez prudent en réduisant l'intervalle ou vous risquez de dépasser votre limite trop tôt.
    }, 10000);
    return () => {
      clearInterval(interval);
    };
  }, [toggle3D]);

  return (
    <div>
      <div id="chart-container" className="w-full h-96"></div>
      <div className="border-solid border-2 border-indigo-500 m-10">
        <div className="grid justify-center mt-5 text-center">
          <p>Mode 3D</p>
          <div className="w-20">
            <Toggle3DButton toggle3D={toggle3D} setToggle3D={setToggle3D} />
          </div>
        </div>
        <div className="grid gap-4 justify-center mt-5 xl:grid-cols-3 p-4">
          <ChartButton chartRef={chartRef} type={'area'} name={'Graphique en aires'} />
          <ChartButton chartRef={chartRef} type={'bar'} name={'Graphique en barres'} />
          <ChartButton chartRef={chartRef} type={'line'} name={'Graphique en lignes'} />
        </div>
      </div>
    </div>
  );
}

```

Ce composant crée notre graphique de revenu d'entreprise et est déjà configuré avec certaines données de chargement initial afin que le graphique charge certaines données lorsqu'il démarre.

Le fichier contient nos paramètres de configuration du graphique. Il y a une fonction qui effectue une requête GET à notre backend Next.js qui se connecte ensuite à notre compte Pusher. C'est ainsi que les données sont récupérées pour notre fichier de graphique. Comme pour le backend, il y a une fonction `setInterval` qui s'exécute toutes les 10 secondes pour obtenir les dernières données de notre backend (nous pouvons augmenter ou diminuer).

Ensuite, nous avons le fichier `Toggle3DButton.js` dans le dossier `Toggle3DButton`. Voici le code pour le fichier :

```javascript
export default function Toggle3DButton({ toggle3D, setToggle3D }) {
  const toggle3DMode = () => {
    setToggle3D(!toggle3D);
  };

  return (
    <label className="flex items-center cursor-pointer border border-gray-400 rounded-full p-1 relative">
      <input
        type="checkbox"
        className="hidden"
        checked={toggle3D}
        onChange={toggle3DMode}
      />
      <span
        className={`toggle__line w-full h-4 bg-gray-400 rounded-full shadow-inner ${
          toggle3D ? 'bg-green-500' : 'bg-gray-400'
        }`}
      ></span>
      <span
        className={`toggle__dot absolute w-6 h-6 bg-white rounded-full shadow inset-y-0 ${
          toggle3D ? 'right-0' : 'left-0'
        }`}
      ></span>
    </label>
  );
}

```

Notre application dispose d'un bouton de bascule en mode 3D et ce composant est utilisé pour le créer.

Les fichiers principaux sont terminés – il nous en reste trois et ensuite nous avons terminé. Ensuite, nous avons le fichier `globals.css` qui a besoin de ce code pour remplacer le code existant :

```css
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  font-family: 'Prompt', sans-serif;
  font-weight: 400;
  font-style: normal;
}

```

Nous avons simplement importé la police `Prompt` pour l'utiliser dans notre application.

En continuant depuis avant, maintenant nous devons mettre à jour le fichier `layout.js` pour qu'il utilise également la police `Prompt`. Ajoutez ce code :

```javascript
import { Prompt } from 'next/font/google';
import './globals.css';

const prompt = Prompt({ subsets: ['latin'], weight: '400' });

export const metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={prompt.className}>{children}</body>
    </html>
  );
}

```

Maintenant, nous pouvons accéder à la police `Prompt` dans toute notre application avec cette importation et cette mise à jour.

Il ne reste plus que notre fichier `page.js` qui est le point d'entrée principal pour tous nos composants. Remplacez tout le code dans ce fichier par ce code final montré ici :

```javascript
import CompanyIncomeChart from './components/CompanyIncomeChart/CompanyIncomeChart';

export default function Home() {
  return <CompanyIncomeChart />;
}

```

D'accord, tout est terminé – notre base de code de projet est complète !

Retournez simplement au dossier racine du projet et exécutez la commande ci-dessous. Votre application devrait être opérationnelle dans un navigateur web.

```shell
npm run dev

```

Tout devrait fonctionner, et maintenant vous devriez avoir un graphique en temps réel avec des dates aléatoires en direct.

## Conclusion

Les plateformes de communication en temps réel sont essentielles pour toutes les technologies que nous utilisons. Aujourd'hui, vous avez appris à connaître Pusher et comment il peut vous aider à construire des applications de données en temps réel qui peuvent s'intégrer avec une bibliothèque de graphiques comme HighCharts.

Il existe de nombreuses applications potentielles que vous pouvez construire avec ces outils. L'introduction d'aujourd'hui devrait ouvrir la porte et vous donner de nombreuses idées pour des projets futurs.
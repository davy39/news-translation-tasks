---
title: 'Comment créer une application de web scraping dynamique avec Playwright et
  React : Un guide étape par étape'
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2025-01-15T14:51:30.116Z'
originalURL: https://freecodecamp.org/news/build-a-dynamic-web-scraper-app-with-playwright-and-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736952641440/0aa6255b-45eb-4ae8-b5cb-d87648590e18.png
tags:
- name: React
  slug: reactjs
- name: 'webscraping '
  slug: webscraping
- name: playwright
  slug: playwright
seo_title: 'Comment créer une application de web scraping dynamique avec Playwright
  et React : Un guide étape par étape'
seo_desc: Today we are going to build a small web scraper app. This application will
  scrape data from the Airbnb website and display it in a nice grid view. We will
  also add a Refresh button that will be able to trigger a new scraping round and
  update the resu...
---

Aujourd'hui, nous allons créer une petite application de web scraping. Cette application extraira des données du site Airbnb et les affichera dans une belle vue en grille. Nous ajouterons également un bouton Actualiser qui permettra de déclencher une nouvelle session de scraping et de mettre à jour les résultats.

Pour rendre notre application un peu plus performante, nous utiliserons le stockage local du navigateur pour stocker les données déjà extraites afin de ne pas déclencher de nouvelles requêtes de scraping à chaque fois que le navigateur est actualisé.

Voici à quoi cela ressemblera :

![Interface de l'application de web scraping](https://cdn.hashnode.com/res/hashnode/image/upload/v1736256647942/56c176ad-2615-478a-94f8-e33b3b437b92.png align="center")

## Table des matières

* [Comment lancer l'application avec Vite](#heading-comment-lancer-lapplication-avec-vite)

* [Comment construire le serveur](#heading-comment-construire-le-serveur)

* [Comment construire le front-end](#heading-comment-construire-le-front-end)

* [Comment déployer sur](#heading-comment-deployer-sur) [render.com](http://render.com)

* [Conclusion](#heading-conclusion)

Si vous souhaitez passer directement au code, voici le [dépôt GitHub](https://github.com/mihailgaberov/web-scraper) avec un [README détaillé](https://github.com/mihailgaberov/web-scraper/blob/main/README.md), et voici la [démo en direct](https://scraper-fe.onrender.com/).

Maintenant, si vous êtes prêt, suivons les étapes pour voir comment construire et déployer l'application.

Tout d'abord, préparons tout pour commencer.

## Comment lancer l'application avec Vite

Nous allons utiliser l'outil de construction [Vite](https://vite.dev/) pour lancer rapidement une application React basique, équipée de TailwindCSS pour le style. Pour ce faire, exécutez cette commande dans votre terminal :

```bash
npm create vite@latest web-scraper -- --template react
```

Ensuite, installez et configurez TailwindCSS comme suit :

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Ajoutez les chemins vers tous vos fichiers de modèle dans votre fichier `tailwind.config.js` comme ceci :

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Vous devriez maintenant avoir une nouvelle application React avec Tailwind installé et configuré.

Commençons notre travail avec le serveur.

## Comment construire le serveur

Puisque nous construisons une application full stack, le minimum dont nous avons besoin est un serveur, un client et une API. L'API résidera dans le monde du serveur et l'application cliente appellera les endpoints qu'elle expose afin de récupérer les données dont nous avons besoin pour les afficher sur le front-end.

### Configurer le serveur HTTP avec Express.js

Nous allons utiliser la bibliothèque Express.js pour lancer un serveur HTTP qui gérera nos requêtes API. Pour ce faire, suivez ces étapes :

Tout d'abord, installez les packages nécessaires avec cette commande :

```bash
npm install express cors playwright
```

Ensuite, créez un fichier `server.js` vide dans le dossier racine du projet et ajoutez le code suivant :

```javascript
import express from "express";
import { chromium } from "playwright";
import cors from "cors";
import { scrapeListings } from "./utils/scraper.js";

const app = express();
const PORT = 5001;

app.use(cors());

app.get("/scrape", async (req, res) => {
  let browser;
  try {
    browser = await chromium.launch();
    const listings = await scrapeListings({ browser, retryCount: 3 });
    res.json(listings);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Serveur de scraping en cours d'exécution sur http://localhost:${PORT}`);
});
```

Avant de continuer avec le scraper, laissez-moi d'abord expliquer ce que nous faisons ici.

Il s'agit d'une configuration assez simple d'un serveur Express qui expose un endpoint appelé "scrape". Notre application côté client (le front-end) peut envoyer des requêtes GET à cet endpoint et recevoir les données retournées en résultat.

Ce qui est important ici, c'est la fonction de rappel asynchrone que nous passons à la méthode `app.get`. C'est ici que nous appelons notre fonction de scraping dans un bloc try/catch. Elle retournera les données extraites ou une erreur si quelque chose ne va pas.

Les dernières lignes indiquent que notre serveur écoutera sur le PORT spécifié, qui est défini sur 5001 ici, et affichera un message dans le terminal pour montrer que le serveur est en cours d'exécution.

### Qu'est-ce que le Web Scraping ?

Avant de plonger dans le code, je veux brièvement expliquer le web scraping si vous n'êtes pas familier avec cela. Le web scraping consiste à lire automatiquement le contenu de sites web à l'aide d'un logiciel. Ce logiciel est appelé un "web scraper". Dans notre cas, le scraper est ce qui se trouve dans la fonction `scrapeListing`.

Une partie essentielle du processus de scraping est de trouver quelque chose dans l'arborescence DOM du site web cible que vous pouvez utiliser pour sélectionner les données que vous souhaitez extraire. Ce quelque chose est connu sous le nom de **sélecteur**. Les sélecteurs peuvent être différents éléments HTML, tels que des balises (h3, p, table) ou des attributs, comme des noms de classe ou des ID.

Vous pouvez utiliser diverses techniques de programmation ou des fonctionnalités du langage de programmation que vous utilisez pour créer le scraper, en visant de meilleurs résultats lors de la mise en œuvre de la partie sélection du scraper.

Dans notre cas, nous utilisons `[itemprop="itemListElement"]` comme sélecteur. Mais vous vous demandez peut-être, comment avons-nous découvert cela et décidé de l'utiliser ? Comment savez-vous quel sélecteur utiliser ?

C'est là que cela devient délicat. Vous devez inspecter manuellement l'arborescence DOM du site web cible et déterminer ce qui fonctionnerait le mieux. C'est le cas à moins que le site ne fournisse une API spécialement conçue pour les scrapers.

Voici à quoi cela ressemble en pratique. Il s'agit d'une capture d'écran du site Airbnb :

![Trouver un sélecteur à partir de l'arborescence DOM du site Airbnb](https://cdn.hashnode.com/res/hashnode/image/upload/v1736588995918/fe2eb87f-e1cb-4474-894f-169fffb8a216.png align="center")

Généralement, vous aurez besoin des informations que vous extrayez pour un but particulier, ce qui signifie que vous devrez les stocker quelque part et ensuite les traiter. Ce traitement implique souvent une sorte de visualisation des données. C'est là que notre application cliente entre en jeu.

Nous stockerons les résultats de notre scraping dans le stockage local du navigateur. Ensuite, nous afficherons facilement ces résultats dans une disposition de grille en utilisant React et TailwindCSS. Mais avant d'en arriver là, revenons au code pour comprendre comment le processus de scraping est effectué.

### Configurer Playwright

Pour la fonctionnalité de scraping, nous allons utiliser une autre bibliothèque qui est devenue assez célèbre au cours des dernières années : [Playwright](https://playwright.dev/). Elle sert principalement de solution de test e2e, mais, comme vous allez le voir maintenant, nous pouvons également l'utiliser pour scraper le web.

Nous allons mettre la fonction de scraping dans un fichier séparé afin d'avoir tout en ordre et de maintenir la séparation des préoccupations.

Créez un nouveau dossier dans le répertoire racine et nommez-le utils. À l'intérieur de ce dossier, ajoutez un nouveau fichier nommé scraper.js et incluez le code suivant :

```javascript
const MAX_RETRIES = 3;

const validateListing = (listing) => {
  return (
    typeof listing.title === "string" &&
    typeof listing.price === "string" &&
    typeof listing.link === "string"
  );
};

export const scrapeListings = async ({ browser, retryCount }) => {
  try {
    const page = await browser.newPage();

    try {
      await page.goto("https://www.airbnb.com/", { waitUntil: "load" });

      await page.waitForSelector('[itemprop="itemListElement"]', {
        timeout: 10000,
      });

      const listings = await page.$$eval(
        '[itemprop="itemListElement"]',
        (elements) => {
          return elements.slice(0, 10).map((element) => {
            const title =
              element.querySelector(".t1jojoys")?.innerText || "N/A";
            const price =
              element.querySelector("._11jcbg2")?.innerText || "N/A";
            const link = element.querySelector("a")?.href || "N/A";
            return { title, price, link };
          });
        }
      );

      const validListings = listings.filter(validateListing);

      if (validListings.length === 0) {
        throw new Error("Aucune annonce trouvée");
      }

      return validListings;
    } catch (pageError) {
      if (retryCount < MAX_RETRIES) {
        console.log(`Nouvelle tentative... (${retryCount + 1}/${MAX_RETRIES})`);
        return await scrapeListings(retryCount + 1);
      } else {
        throw new Error(
          `Échec de l'extraction des données après ${MAX_RETRIES} tentatives : ${pageError.message}`
        );
      }
    } finally {
      await page.close();
    }
  } catch (browserError) {
    throw new Error(`Échec du lancement du navigateur : ${browserError.message}`);
  } finally {
    if (browser) {
      await browser.close();
    }
  }
};
```

### Mécanisme de nouvelle tentative

En haut du fichier, il y a une constante appelée `MAX_RETRIES` utilisée pour implémenter un **mécanisme de nouvelle tentative**. Cette tactique est souvent utilisée par les web scrapers pour contourner ou surmonter les protections que certains sites ont contre le scraping. Nous verrons comment l'utiliser ci-dessous.

Il est important de mentionner l'aspect légal ici également. Respectez toujours les conditions générales ainsi que la politique de confidentialité du site web que vous prévoyez de scraper. Utilisez ces techniques uniquement pour relever les défis techniques, et non pour enfreindre la loi.

Une petite fonction d'assistance suit que vous pouvez utiliser pour valider les données reçues. Rien d'intéressant ici.

Ensuite, vient la fonction principale de scraping. Nous passons l'objet browser, fourni par Playwright, et le nombre de tentatives de nouvelle tentative comme arguments à la fonction.

Il y a deux blocs try/catch pour gérer les échecs possibles : un pour le lancement du navigateur (en mode headless, ce qui signifie que vous ne verrez rien) et un pour le processus de scraping. Dans ce dernier, nous utiliserons les fonctionnalités de Playwright pour demander le site web, attendre que la page soit entièrement chargée, puis localiser le sélecteur que nous avons défini.

Dans la fonction de rappel que nous passons à `$$eval`, nous accédons aux éléments retournés par le scraping, ce qui nous permet de les traiter et d'obtenir les données que nous voulons. Dans ce cas, j'utilise trois sélecteurs pour récupérer le titre, le prix et le lien de la propriété. Les deux premiers sont des noms de classe, et le dernier est la balise HTML `<a>`.

![Sélection du prix](https://cdn.hashnode.com/res/hashnode/image/upload/v1736589673793/79cd8e05-eef7-4887-b3cb-6d2d95e9d5dc.png align="center")

Ensuite, nous retournons un objet, { title, price, link }, avec les données récupérées, c'est-à-dire les valeurs des trois propriétés. Et à la fin de la partie try, nous validons les résultats avant de les retourner au front-end.

Ce qui suit dans la partie catch est la mise en œuvre du mécanisme de nouvelle tentative dont nous avons parlé il y a une minute :

```javascript
 } catch (pageError) {
      if (retryCount < MAX_RETRIES) {
        console.log(`Nouvelle tentative... (${retryCount + 1}/${MAX_RETRIES})`);
        return await scrapeListings(retryCount + 1);
      } else {
        throw new Error(
          `Échec de l'extraction des données après ${MAX_RETRIES} tentatives : ${pageError.message}`
        );
      }
    }
```

Si une erreur se produit pendant le processus de lecture, nous entrons dans la phase catch et vérifions si le nombre de nouvelles tentatives est inférieur à la limite maximale que nous avons définie. Si c'est le cas, nous essayons à nouveau en exécutant la fonction de manière récursive. Sinon, nous lançons une erreur indiquant que le scraping a échoué et que le nombre maximal de tentatives a été atteint.

C'est tout ce dont vous avez besoin pour configurer le scraping web de base de la page d'accueil d'Airbnb.

Vous pouvez voir tout cela dans le [dépôt GitHub](https://github.com/mihailgaberov/web-scraper) du projet, donc ne vous inquiétez pas si vous avez manqué quelque chose ici.

## Comment construire le front-end

Maintenant, il est temps d'utiliser les données extraites.

Affichons les 10 dernières propriétés dans une disposition de grille, permettant à vous (ou à quiconque) de les ouvrir en cliquant sur leurs liens. Nous ajouterons également une fonctionnalité `Actualiser` qui vous permet d'effectuer un nouveau scraping pour obtenir les données les plus récentes.

Voici à quoi ressemble la structure de la partie front-end du projet :

![Structure du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1736591529574/5cf5c62f-283b-4cfc-afa4-3b2b92a3ddae.png align="center")

Nous avons une structure d'application simple : un conteneur principal (App.jsx) qui contient tous les composants et inclut une logique pour faire des requêtes à l'API et stocker les données dans le stockage local.

```javascript
import { useEffect, useState } from "react";
import { useLocalStorage } from "@uidotdev/usehooks";
import axios from "axios";
import Footer from "./components/Footer";
import Header from "./components/Header";
import RefreshButton from "./components/RefreshButton";
import Grid from "./components/Grid";
import Loader from "./components/Loader";

function App() {
  const [listings, setListings] = useLocalStorage("properties", []);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchListings = async () => {
    setLoading(true);
    setError("");
    setListings([]);

    try {
      const response = await axios.get("http://localhost:5001/scrape");
      if (response.data.length === 0) {
        throw new Error("Aucune annonce trouvée");
      }
      setListings(response.data);
    } catch (err) {
      setError(
        err.response?.data?.error ||
          "Échec de la récupération des annonces. Veuillez réessayer."
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (listings.length === 0) {
      fetchListings();
    }
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <Header />
      <RefreshButton callback={fetchListings} loading={loading} />
      <main className="flex flex-col items-center justify-center flex-1 w-full px-4 relative">
        {error && <p className="text-red-500">{error}</p>}
        {loading ? <Loader /> : <Grid listings={listings} />}
      </main>
      <Footer />
    </div>
  );
}

export default App;
```

Tous les composants sont placés dans le répertoire [components](https://github.com/mihailgaberov/web-scraper/tree/main/src/components). La plupart des composants sont assez simples, et je les ai inclus pour donner à l'application une apparence plus complète.

Le [Header](https://github.com/mihailgaberov/web-scraper/blob/main/src/components/Header.jsx) affiche la barre supérieure. Le [RefreshButton](https://github.com/mihailgaberov/web-scraper/blob/main/src/components/RefreshButton.jsx) est utilisé pour envoyer une nouvelle requête et obtenir les dernières données. Dans la section `<main>`, nous affichons soit un message d'erreur si la récupération échoue, soit un composant [Loader](https://github.com/mihailgaberov/web-scraper/blob/main/src/components/Loader.jsx) et un composant [Grid](https://github.com/mihailgaberov/web-scraper/blob/main/src/components/Grid.jsx).

La partie de chargement est simple. Le composant Grid est celui qui est intéressant. Nous lui passons les résultats du scraping à l'aide d'une prop appelée 'listings'. À l'intérieur, nous utilisons une simple fonction map() pour les parcourir et afficher les propriétés. Nous utilisons Tailwind pour styliser la grille, en veillant à ce que les propriétés soient soigneusement listées et aient une belle apparence sur les écrans de bureau et mobiles.

![L'application a également une belle apparence sur les petits écrans.](https://cdn.hashnode.com/res/hashnode/image/upload/v1736593771753/0f56930c-2944-452c-a2cd-4c6b69c1d996.png align="center")

Et enfin, nous avons le composant [Footer](https://github.com/mihailgaberov/web-scraper/blob/main/src/components/Footer.jsx) qui rend une simple barre avec du texte. Encore une fois, je l'ai ajouté juste pour la complétude.

## Comment déployer sur render.com

Peut-être un peu plus d'un an auparavant, j'avais besoin d'un endroit pour déployer des applications full-stack, idéalement gratuitement, puisque c'était juste pour des fins éducatives.

Après quelques recherches, j'ai trouvé une plateforme appelée [Render](https://dashboard.render.com/) et j'ai réussi à déployer une application avec des parties client et serveur, la faisant fonctionner en ligne. Je l'ai laissée là jusqu'à maintenant. Puisque notre scraper nécessite les deux parties pour fonctionner correctement, nous allons la déployer là-bas et la faire fonctionner en ligne, comme vous pouvez le voir [ici](https://scraper-fe.onrender.com/).

Pour ce faire, vous devez créer un compte avec Render et utiliser leur application de tableau de bord. Le processus est simple, mais j'inclurai quelques captures d'écran ci-dessous pour plus de clarté.

Voici la page d'aperçu où vous pouvez voir tous vos projets :

![Page d'aperçu de la plateforme Render](https://cdn.hashnode.com/res/hashnode/image/upload/v1736594350231/eac21d82-f43d-44be-8027-6ac25c86f740.png align="center")

Voici la page du projet où vous pouvez voir et gérer vos projets. Dans notre cas, nous pouvons voir à la fois le serveur et l'application cliente en tant que services séparés.

![Page du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1736594435708/a4329d74-f529-46a0-a193-d6a1ade145ad.png align="center")

Vous pouvez cliquer sur chaque service pour ouvrir sa page, où vous pouvez voir les déploiements et les commits qui les ont déclenchés. Vous pouvez trouver encore plus de détails si vous explorez davantage.

![Détails du déploiement](https://cdn.hashnode.com/res/hashnode/image/upload/v1736594566165/39e78a87-d8e7-4df3-8e1b-02eb0eee799c.png align="center")

Vous devriez être en mesure de gérer le processus de déploiement par vous-même, car tout est clairement expliqué. Mais si vous avez besoin d'aide, n'hésitez pas à demander.

Je devrais mentionner que je ne suis pas affilié à Render de quelque manière que ce soit et que je ne reçois aucun avantage pour les mentionner ici. Je les ai simplement trouvés utiles et je voulais les partager avec vous, donc je les ai utilisés ici.

## Conclusion

Une application de web scraping peut être un outil puissant pour collecter des données, mais il y a plusieurs domaines d'amélioration et des considérations importantes à garder à l'esprit.

Tout d'abord, vous pouvez améliorer les performances et l'efficacité de l'application en optimisant le processus de scraping et en veillant à ce que les données soient stockées et traitées efficacement. Vous pouvez également implémenter une gestion des erreurs plus robuste et des mécanismes de nouvelle tentative pour améliorer la fiabilité du scraper.

De plus, gardez à l'esprit que le scraping éthique est crucial, et il est important de toujours respecter les conditions d'utilisation et les politiques de confidentialité des sites web que vous scrapez. Cela inclut de ne pas surcharger le site web avec des requêtes et de veiller à ce que les données soient utilisées de manière responsable. Demandez toujours la permission du site si nécessaire et envisagez d'utiliser les API fournies par le site web comme une alternative plus éthique et plus fiable.

Enfin, le respect de la loi est primordial. Assurez-vous que vos activités de scraping sont conformes aux réglementations et directives légales pour éviter tout problème juridique potentiel. En vous concentrant sur ces aspects, vous pouvez construire une application de web scraping plus efficace, éthique et conforme à la loi.
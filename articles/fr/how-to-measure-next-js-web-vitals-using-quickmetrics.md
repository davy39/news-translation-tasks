---
title: Comment mesurer les Web Vitals de Next.js en utilisant Quickmetrics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-13T22:53:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-measure-next-js-web-vitals-using-quickmetrics
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/CoverImage.png
tags:
- name: Next.js
  slug: nextjs
- name: web performance
  slug: web-performance
seo_title: Comment mesurer les Web Vitals de Next.js en utilisant Quickmetrics
seo_desc: "By Umesh Yadav\nDevelopers spend a lot of time optimizing websites to provide\
  \ a better user experience. Web Vitals are a set of useful metrics that aim to capture\
  \ the user's experience on a web page. \nThese are the important web vitals we'll\
  \ consider ..."
---

Par Umesh Yadav

Les développeurs passent beaucoup de temps à optimiser les sites web pour offrir une meilleure expérience utilisateur. Les [Web Vitals](https://web.dev/vitals/) sont un ensemble de métriques utiles qui visent à capturer l'expérience de l'utilisateur sur une page web. 

Voici les Web Vitals importantes que nous allons considérer dans cet article.

## [Time to First Byte](https://developer.mozilla.org/en-US/docs/Glossary/Time_to_first_byte) (TTFB)

Le Time to First Byte mesure le temps pris par le navigateur du client pour recevoir le premier octet de la page depuis le serveur web après que l'utilisateur a envoyé la requête. 

Vous devriez viser un temps entre **200-500ms**. Si votre site web prend plus de temps que cela, alors vous devriez définitivement essayer d'optimiser cette valeur.

## [First Contentful Paint](https://developer.mozilla.org/en-US/docs/Glossary/First_contentful_paint) (FCP)

Le First Contentful Paint mesure le temps nécessaire pour rendre la première image ou le premier texte de la page après qu'elle a commencé à charger.

Pour offrir une bonne expérience utilisateur, les sites devraient viser un FCP dans **1 seconde** après le début du chargement de la page.

Dans l'image ci-dessous, le FCP se produit dans la 4ème image, car c'est à ce moment-là que le premier texte et la première image se chargent. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-10-at-10.25.08-PM.png)

## [Largest Contentful Paint](https://web.dev/lcp/) (LCP)

Le Largest Contentful Paint mesure le temps nécessaire pour rendre la plus grande image ou le plus grand texte de la page après qu'elle a commencé à charger.

Pour offrir une bonne expérience utilisateur, le LCP devrait se produire dans **2,5 secondes** après le début du chargement de la page.

## [First Input Delay](https://web.dev/fid/) (FID) 

Le First Input Delay mesure tout retard dans le traitement de la première interaction de l'utilisateur avec la page. Il peut s'agir d'un clic sur un bouton, d'un défilement de page ou d'un clic sur un lien. 

Par exemple, il mesure le temps pris depuis que l'utilisateur clique sur le bouton jusqu'à ce que le navigateur commence à traiter l'événement.

Pour offrir une bonne expérience utilisateur, les pages devraient avoir un FID de moins de **100 millisecondes**.

## [Cumulative Layout Shift](https://web.dev/cls/) (CLS)

Le Cumulative Layout Shift mesure le nombre de fois où les éléments d'une page se déplacent pendant le chargement.  
  
Dans l'image ci-dessous, si vous regardez attentivement, la page charge d'abord tout le texte et les boîtes. Mais une fois que l'image est chargée, tous les autres composants sont poussés vers le bas. Ici, le CLS est le décalage qui se produit après le chargement de l'image.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/ezgif.com-video-to-gif-3.gif)

Pour offrir une bonne expérience utilisateur, les pages devraient maintenir un CLS inférieur à **0,1.**

Next.js est un framework React qui fournit le rendu côté serveur (SSR) et la génération de sites statiques. Dans cet article, je vais vous montrer comment vous pouvez suivre chacune de ces Web Vitals pour votre application Next.js en utilisant [Quickmetrics](https://quickmetrics.io/). 

## Créer un compte Quickmetrics

Quickmetrics est un fournisseur simple de collecte de métriques. Il offre un niveau gratuit très généreux que vous pouvez utiliser pour suivre suffisamment de métriques utilisateur afin d'obtenir des informations importantes.

Pour configurer votre compte, allez [ici](https://app.quickmetrics.io/signup). Vous pouvez vous inscrire en utilisant votre email et votre mot de passe. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-63.png)
_Page d'inscription Quickmetrics_

Après vous être inscrit avec succès, vous recevrez votre `API_KEY`. Veuillez stocker cette clé dans un endroit sécurisé afin de pouvoir l'utiliser plus tard.

## Comment mesurer les Web Vitals dans votre application Next.js

Next.js fournit un moyen intégré pour mesurer diverses métriques de performance. Pour mesurer l'une des métriques prises en charge, vous devrez créer un composant [App personnalisé](https://nextjs.org/docs/advanced-features/custom-app) et définir une fonction `reportWebVitals`.

> Au cas où vous n'auriez pas d'application prête, veuillez vous référer à [ce guide](https://nextjs.org/docs/getting-started) pour en créer une.

```js
import "../styles/globals.css";

export function reportWebVitals(metric) {
  switch (metric.name) {
    case 'FCP':
      // gérer les résultats FCP
      break
    case 'LCP':
      // gérer les résultats LCP
      break
    case 'CLS':
      // gérer les résultats CLS
      break
    case 'FID':
      // gérer les résultats FID
      break
    case 'TTFB':
      // gérer les résultats TTFB
      break
    default:
      break
  }
}


function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;

```

Dans l'exemple ci-dessus, nous utilisons `metric.name` pour filtrer les Web Vitals. Une fois que vous avez filtré les métriques et que vous avez les données des Web Vitals, nous devons envoyer ces métriques à Quickmetrics.

```js
const sendMetric = ({ name, value }) => {
  const url = `https://qckm.io?m=${name}&v=${value}&k=${process.env.NEXT_PUBLIC_QUICK_METRICS_API_KEY}`;

  // Utiliser `navigator.sendBeacon()` si disponible, sinon utiliser `fetch()`.
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url);
  } else {
    fetch(url, { method: "POST", keepalive: true });
  }
};

```

Maintenant, nous allons obtenir le nom et la valeur de l'objet metric que `reportWebVitals` fournit. Nous passons cette valeur à la méthode `sendMetric`. À l'intérieur de cette méthode, nous construisons l'URL Quickmetrics pour envoyer les métriques (vous pouvez vous référer à la [documentation](https://app.quickmetrics.io/docs/send-events/url-params) pour en savoir plus à ce sujet).

Nous utilisons `sendBeacon` pour envoyer la métrique à Quickmetrics si elle est présente. Si ce n'est pas le cas, nous utilisons fetch (il est fourni par Next.js, vous n'avez rien à installer).

> Pour en savoir plus sur pourquoi nous utilisons `sendBeacon`, veuillez lire [ceci](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon).

Maintenant, vous devez simplement appeler sendMetrics depuis chaque cas de switch. Voici à quoi votre code devrait ressembler à ce stade :

```js
import "../styles/globals.css";

const sendMetric = ({ name, value }) => {
  const url = `https://qckm.io?m=${name}&v=${value}&k=${process.env.NEXT_PUBLIC_QUICK_METRICS_API_KEY}`;

  // Utiliser `navigator.sendBeacon()` si disponible, sinon utiliser `fetch()`.
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url);
  } else {
    fetch(url, { method: "POST", keepalive: true });
  }
};

export function reportWebVitals(metric) {
  switch (metric.name) {
    case "FCP":
      sendMetric(metric);
      break;
    case "LCP":
      sendMetric(metric);
      break;
    case "CLS":
      sendMetric(metric);
      break;
    case "FID":
      sendMetric(metric);
      break;
    case "TTFB":
      sendMetric(metric);
      break;
    default:
      break;
  }
}

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;

```

Voici le lien vers le [dépôt](https://github.com/imumesh18/nextjs-quickmetrics) au cas où vous voudriez voir le code complet.

Maintenant, stockez votre clé API Quickmetrics dans `.env` pour envoyer les métriques.

```text
NEXT_PUBLIC_QUICK_METRICS_API_KEY=votre_clé

```

Ensuite, exécutez votre site web en utilisant `yarn dev` ou `npm run dev`. Visitez votre site web sur `http://localhost:3000`. Rafraîchissez-le plusieurs fois afin de générer suffisamment de données pour les visualiser.

## Visualiser les métriques sur Quickmetrics

Maintenant, allez sur la page des métriques Quickmetrics [page](https://app.quickmetrics.io/metrics). Vous devriez voir des métriques comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-64.png)
_Page des métriques Quickmetrics_

Vous pouvez cliquer sur ces métriques individuelles pour voir les données et interpréter les résultats. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-12-at-11.42.43-PM.png)
_Panneau de métrique individuelle_

Vous pouvez cliquer sur l'icône des paramètres comme montré dans l'image ci-dessus pour personnaliser les graphiques. Vous pouvez définir le type de graphique, l'unité et les opérations de valeur comme avg, sum, max, min, etc. 

Examinons ces graphiques pour les comprendre en détail.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-12-at-11.33.23-PM.png)
_Métrique FCP_

Le graphique ci-dessus représente les métriques FCP de mon site web. Je prends la moyenne ici. Si vous regardez le graphique, vous pouvez voir que la valeur FCP de mon site web est d'environ 600-700ms, ce qui est assez bon (comme nous nous y attendrions, elle devrait être <**1s**).

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-12-at-11.36.32-PM.png)
_Métrique LCP_

Le graphique ci-dessus montre la métrique LCP du site web. Elle est d'environ 600-700ms, ce qui est bien inférieur aux **2,5s** recommandés. Donc c'est bien aussi.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-12-at-11.38.10-PM.png)
_Métrique TTFB_

Ce graphique montre la métrique TTFB du site web. Elle est d'environ 30ms, ce qui est bien meilleur que la valeur attendue de 200-300ms.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-12-at-11.38.32-PM.png)
_Métrique CLS_

J'utilise actuellement le site Next.js de démarrage qui a presque zéro CLS. Cette valeur devrait toujours être inférieure à 0,1.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-12-at-11.39.03-PM.png)
_Métrique FID_

Dans le graphique ci-dessus, le FID est de 23,5ms. Encore une fois, cette valeur est inférieure à 100ms, ce qui est bien meilleur que le temps recommandé de <**100ms.**

Pour voir toutes ces métriques depuis une seule page, vous pouvez créer un tableau de bord et ensuite ajouter ces métriques à l'intérieur de ce tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-13-at-12.01.14-AM.png)
_Tableau de bord Quickmetrics_

Vous pouvez cliquer sur créer un tableau de bord pour créer un tableau de bord personnalisé. À l'intérieur du tableau de bord, vous pouvez cliquer sur "ajouter des graphiques" pour créer des graphiques de métriques individuels.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-13-at-12.11.28-AM.png)
_Ajouter des graphiques au tableau de bord_

Une fois que vous avez cliqué sur ajouter un graphique, vous pouvez ensuite sélectionner les métriques pour lesquelles vous souhaitez tracer le graphique. Vous pouvez également spécifier l'opération de valeur à tracer sur les graphiques (avg, sum, min, max).

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-13-at-12.12.10-AM.png)
_Créer un graphique à l'intérieur du tableau de bord_

Une fois que vous avez créé tous les graphiques à l'intérieur d'un tableau de bord, votre tableau de bord devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-65.png)
_Tableau de bord des Web Vitals de Next.js_

## Conclusion

Les Web Vitals sont les meilleures métriques disponibles qui vous aident à quantifier l'expérience de votre site web. La collecte de données auprès des visiteurs réels vous aide à mettre en œuvre des changements concrets dans votre code. Au lieu de mesurer sur votre ordinateur portable, vous pouvez collecter les Web Vitals à partir des appareils réels que vos visiteurs utilisent.

Si vous avez aimé cet article, vous pouvez vous rendre sur [mon blog personnel](https://umesh.dev/blog) pour voir d'autres articles que j'ai écrits.

J'écris régulièrement sur la programmation et les logiciels, alors n'hésitez pas à vous abonner à ma newsletter et à recevoir les derniers articles de ma part directement dans votre boîte de réception. Vous pouvez également me contacter sur [Twitter](https://twitter.com/imumesh18).

Références :  
- [https://nextjs.org/docs/advanced-features/measuring-performance](https://nextjs.org/docs/advanced-features/measuring-performance)  
- [https://app.quickmetrics.io/docs/getting-started](https://app.quickmetrics.io/docs/getting-started)  
- [https://web.dev/vitals/](https://web.dev/vitals/)
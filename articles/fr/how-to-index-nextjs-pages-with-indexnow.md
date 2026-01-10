---
title: Comment indexer vos applications Next.js plus rapidement avec IndexNow
subtitle: ''
author: Vivek Sahu
co_authors: []
series: null
date: '2024-08-06T13:38:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-index-nextjs-pages-with-indexnow
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/IndexNowSites-1.png
tags:
- name: deployment
  slug: deployment
- name: SEO
  slug: seo
seo_title: Comment indexer vos applications Next.js plus rapidement avec IndexNow
seo_desc: 'Next.js is a powerful framework for building lightning-fast applications.
  However, getting these applications indexed quickly by search engines is crucial
  for visibility and traffic, and sadly, this is not immediate.

  Even after uploading your sitemap...'
---

Next.js est un framework puissant pour construire des applications ultra-rapides. Cependant, faire en sorte que ces applications soient indexées rapidement par les moteurs de recherche est crucial pour la visibilité et le trafic, et malheureusement, cela n'est pas immédiat.

Même après avoir téléchargé votre sitemap, cela peut prendre jusqu'à des semaines, voire des mois, avant que les moteurs de recherche ne parcourent vos pages. En fait, si vous avez mis à jour ou ajouté une nouvelle page, cela peut prendre des semaines avant que les moteurs de recherche ne le remarquent.

Alors, pouvons-nous faire mieux ?

Dans cet article, vous apprendrez comment améliorer le référencement de votre application Next.js sur les principaux moteurs de recherche comme Bing, Yahoo, et autres avec un indexage rapide en utilisant IndexNow.

## Table des matières

- [Qu'est-ce qu'IndexNow ?](#heading-quest-ce-que-indexnow)
    * [Comment cela fonctionne-t-il ?](#heading-comment-cela-fonctionne-t-il)
- [Étapes](#heading-etapes)
   * [Prérequis](#heading-prerequis)
   * [Étapes de haut niveau](#heading-etapes-de-haut-niveau)
   * [Comment prouver la propriété de l'hôte](#heading-comment-prouver-la-propriete-de-lhote)
   * [Comment créer un script pour obtenir toutes les URLs de votre sitemap](#heading-comment-creer-un-script-pour-obtenir-toutes-les-urls-de-votre-sitemap)
   * [Comment appeler l'API IndexNow](#heading-comment-appeler-lapi-indexnow)
- [Prochaines étapes et améliorations](#heading-prochaines-etapes-et-ameliorations)
- [Conclusion](#heading-conclusion)
- [Liens et références](#heading-liens-et-references)

## Qu'est-ce qu'IndexNow ?

[IndexNow](https://www.indexnow.org/) est un protocole qui réduit considérablement le temps d'indexation. Voici comment il est défini sur leur site web :

> IndexNow est un moyen simple pour les propriétaires de sites web d'informer instantanément les moteurs de recherche des dernières modifications de contenu sur leur site. Dans sa forme la plus simple, IndexNow est un simple ping pour que les moteurs de recherche sachent qu'une URL et son contenu ont été ajoutés, mis à jour ou supprimés, permettant aux moteurs de recherche de refléter rapidement ce changement dans leurs résultats de recherche.([Source : Accueil IndexNow](https://www.indexnow.org/))

C'est un protocole adopté par des moteurs de recherche comme Bing, Naver, Seznam.cz, Yandex, Yep et d'autres. Google ne supporte pas ce protocole au moment de la rédaction de cet article.

Il est nativement intégré dans de nombreux CMS comme Wix, et il existe de nombreux plugins tiers pour d'autres comme Drupal ou WordPress. Cependant, il n'y a pas de support natif dans NextJS.

### Comment cela fonctionne-t-il ?

Chaque fois que vous mettez à jour quelque chose, tout ce que vous avez à faire est de "ping" ou d'appeler leur API et de les informer du changement.

Lorsque cette information est reçue, les moteurs de recherche peuvent maintenant prioriser le crawl de ces URLs par rapport aux autres URLs qui sont parcourues naturellement.

Dans ce guide, nous allons passer en revue le processus d'intégration d'IndexNow dans votre application Next.js existante afin que toute modification des URLs puisse être soumise et indexée par les moteurs de recherche.

### Prérequis

* Une application Next.js.
* Un fichier **sitemap.xml** pour votre application Next.js.

### Étapes de haut niveau

1. Nous devons d'abord "prouver la propriété" de l'hôte pour lequel les URLs seront soumises.
2. Créer un simple script Node.js pour obtenir toutes les URLs de votre sitemap.
3. Appeler l'API IndexNow.

### Comment prouver la propriété de l'hôte

Allez sur la page [`IndexNow`](https://www.bing.com/indexnow/getstarted) pour Bing. Comme il n'y a pas d'intégration directe pour Next.js, faites défiler jusqu'à la section de [l'intégration manuelle](https://www.bing.com/indexnow/getstarted#implementation).

Cliquez sur "Generate" pour générer une nouvelle clé API.

Dans votre application Next.js, allez dans le répertoire **public** à la racine. Tout le contenu statique est rendu via ce répertoire. Créez un nouveau fichier et stockez cette clé API :

```bash
# En supposant que la clé API est "f34f184d10c049ef99aa7637cdc4ef04". Changez selon votre clé API générée
echo "f34f184d10c049ef99aa7637cdc4ef04" > f34f184d10c049ef99aa7637cdc4ef04.txt

```

Construisez et exécutez votre application Next.js :

```bash
npm run build && npm run start

```

Puis confirmez que le fichier est disponible dans votre chemin `/f34f184d10c049ef99aa7637cdc4ef04.txt`.

C'est-à-dire que l'ouverture de [https://localhost:3000/f34f184d10c049ef99aa7637cdc4ef04.txt](https://localhost:3000/f34f184d10c049ef99aa7637cdc4ef04.txt) devrait donner une réponse avec le texte "f34f184d10c049ef99aa7637cdc4ef04" sur votre navigateur.

Selon votre clé API, modifiez la valeur de la clé ci-dessus. Validez, poussez et déployez ces changements en production.

Après un déploiement réussi, vérifiez que `<Votre URL>/<Clé API>.txt` rend le texte `<Clé API>`. C'est-à-dire : `<Votre URL>/f34f184d10c049ef99aa7637cdc4ef04.txt` devrait rendre `f34f184d10c049ef99aa7637cdc4ef04`.

### Comment créer un script pour obtenir toutes les URLs de votre sitemap

Tout d'abord, créez le fichier de script Node :

```bash
touch lib/indexnow.js

```

Puis ajoutez le code ci-dessous :

```js
const xml2js = require('xml2js');

// Configuration
const sitemapUrl = '<Votre URL>/sitemap.xml'; // TODO: Mettre à jour
const host = '<Votre URL>'; // TODO: Mettre à jour
const key = '<Clé API>'; // TODO: Mettre à jour
const keyLocation = 'https://<Votre URL>/<Clé API>.txt'; // TODO: Mettre à jour

const modifiedSinceDate = new Date(process.argv[2] || '1970-01-01');

if (isNaN(modifiedSinceDate.getTime())) {
  console.error('Date invalide fournie. Veuillez utiliser le format AAAA-MM-JJ');
  process.exit(1);
}

function fetchSitemap(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => {
        data += chunk;
      });
      res.on('end', () => {
        resolve(data);
      });
    }).on('error', (err) => {
      reject(err);
    });
  });
}

function parseSitemap(xmlData) {
  return new Promise((resolve, reject) => {
    xml2js.parseString(xmlData, (err, result) => {
      if (err) {
        reject(err);
      } else {
        resolve(result);
      }
    });
  });
}

function filterUrlsByDate(sitemap, date) {
  const urls = sitemap.urlset.url;
  return urls
    .filter(url => new Date(url.lastmod[0]) > date)
    .map(url => url.loc[0]);
}


async function main() {
  try {
    const xmlData = await fetchSitemap(sitemapUrl);
    const sitemap = await parseSitemap(xmlData);
    const filteredUrls = filterUrlsByDate(sitemap, modifiedSinceDate);
    console.log(filteredUrls);
  } catch (error) {
    console.error('Une erreur est survenue :', error);
  }
}

main();


```

Nous récupérons essentiellement les URLs du sitemap qui ont été modifiées à partir d'une certaine date. La date peut être passée en argument au script.

Ensuite, installez la bibliothèque `xml2js` que nous utiliserons pour analyser la réponse XML du sitemap.

```bash
npm install xml2js --save-dev

```

Puis exécutez le script pour récupérer les URLs et vérifier si tout fonctionne :

```bash
node lib/indexnow.js 2024-01-01

```

Cela devrait afficher une liste d'URLs qui ont été modifiées depuis le 1er janvier 2024. Vous pouvez lui passer n'importe quelle date.

### Comment appeler l'API IndexNow

Voici le schéma de l'API IndexNow :

**Requête :**

```
POST /IndexNow HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: api.indexnow.org
{
  "host": "www.example.org",
  "key": "7e3f6e8bc47b4f2380ba54aab6088521",
  "keyLocation": "https://www.example.org/7e3f6e8bc47b4f2380ba54aab6088521.txt",
  "urlList": [
      "https://www.example.org/url1",
      "https://www.example.org/folder/url2",
      "https://www.example.org/url3"
      ]
}

```

**Réponse :**

| Code HTTP | Réponse              | Raisons                                                                                                                               |
| -------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 200       | Ok                    | URL soumise avec succès                                                                                                               |
| 400       | Mauvaise requête           | Format invalide                                                                                                                        |
| 403       | Interdit              | En cas de clé non valide (par exemple, clé non trouvée, fichier trouvé mais clé non dans le fichier)                                                       |
| 422       | Entité non traitée | En cas d'URLs n'appartenant pas à l'hôte ou la clé ne correspondant pas au schéma dans le protocole                                           |
| 429       | Trop de requêtes     | Trop de requêtes (potentiel Spam) | 
                                                                                                   

Maintenant que nous sommes certains que notre partie de récupération d'URL fonctionne correctement, ajoutons la fonction principale pour appeler l'API IndexNow :

Ouvrez le fichier `lib/index.js` en utilisant votre IDE préféré et ajoutez la fonction suivante :

```js
function postToIndexNow(urlList) {
  const data = JSON.stringify({
    host,
    key,
    keyLocation,
    urlList
  });

  const options = {
    hostname: 'api.indexnow.org',
    port: 443,
    path: '/IndexNow',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Content-Length': data.length
    }
  };

  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let responseData = '';
      res.on('data', (chunk) => {
        responseData += chunk;
      });
      res.on('end', () => {
        resolve({
          statusCode: res.statusCode,
          statusMessage: res.statusMessage,
          data: responseData
        });
      });
    });

    req.on('error', (error) => {
      reject(error);
    });

    req.write(data);
    req.end();
  });
}

```

Cette fonction appelle l'API IndexNow en passant une liste d'URLs qui lui est transmise, ainsi que la `<Clé API>`.

Appelez cette fonction à partir de la fonction principale. Modifiez la fonction principale comme suit :

```js
async function main() {
  try {
    const xmlData = await fetchSitemap(sitemapUrl);
    const sitemap = await parseSitemap(xmlData);
    const filteredUrls = filterUrlsByDate(sitemap, modifiedSinceDate);
    console.log(filteredUrls);
    
    if (filteredUrls.length > 0) {
      const response = await postToIndexNow(filteredUrls);
      console.log('Réponse de l\'API IndexNow :');
      console.log('Statut :', response.statusCode, response.statusMessage);
      console.log('Données :', response.data);
    } else {
      console.log('Aucune URL modifiée depuis la date spécifiée.');
    }
  } catch (error) {
    console.error('Une erreur est survenue :', error);
  }
}

```

L'`API IndexNow` sera maintenant appelée pour chaque URL que nous lui passons.

Exécutez le script, et vous devriez voir une sortie similaire en cas de succès, ou un message d'erreur en cas de problème :

```
% node lib/indexnow.js 2024-07-24

[
  'https://<Votre URL>',
  'https://<Votre URL>/page1',
  'https://<Votre URL>/page1'
]
Réponse de l'API IndexNow :
Statut : 200 OK
Données :

```

Voilà, vos APIs peuvent maintenant fonctionner avec IndexNow pour un indexage plus rapide.

## Prochaines étapes et améliorations

Nous venons de voir comment écrire et exécuter un script localement pour indexer nos pages via IndexNow. Cependant, il y a beaucoup de choses qui peuvent être faites pour améliorer cela davantage, par exemple :

* Intégrer IndexNow dans votre pipeline CI/CD pour des mises à jour automatiques.
* Gérer efficacement les grands sitemaps avec des lots ou des files d'attente.
* Surveiller et journaliser les soumissions IndexNow pour le débogage et l'analyse.
* Explorer l'API IndexNow pour des fonctionnalités supplémentaires (par exemple : suppression d'URL).
* Fournir une version CLI.
* Ajouter la prise en charge de TypeScript.

Cependant, ces points sont hors du cadre de cet article. Il existe quelques modules npm prêts pour la production qui implémentent certains ou plusieurs de ces comportements avancés et qui peuvent être facilement intégrés dans votre application. J'en ai créé un ([voir l'annonce de indexnow-submitter](https://wewake.dev/posts/introducing-indexnow-submitter-fast-search-engine-indexing/)) ainsi que l'ajout de fonctionnalités/support manquantes dans l'écosystème. Vous pouvez brancher et utiliser n'importe lequel de ces modules dans vos applications basées sur Node.

## Conclusion

Dans cet article, vous avez appris comment ajouter le protocole `IndexNow` à votre application Next.js. Vous pouvez utiliser ce protocole pour obtenir une expérience d'indexation de pages beaucoup plus rapide, automatisée et pratique chaque fois que vous apportez une modification à votre site web, permettant aux moteurs de recherche de récupérer le dernier contenu de vos pages.

J'espère que cela a été utile, et n'hésitez pas à expérimenter et à personnaliser cette intégration pour répondre à vos besoins.

## Liens et références

* [Documentation IndexNow](https://www.indexnow.org/documentation)
* [FAQ](https://www.indexnow.org/faq)
* [IndexNow Bing](https://www.bing.com/indexnow/getstarted#implementation)
* [Module NPM indexnow-submitter](https://www.npmjs.com/package/indexnow-submitter)
* [Annonce de la sortie de indexnow-submitter](https://wewake.dev/posts/introducing-indexnow-submitter-fast-search-engine-indexing/)
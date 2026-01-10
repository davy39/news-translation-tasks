---
title: Comment extraire les avis sur les produits Amazon derrière une connexion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-30T16:46:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-scrape-amazon-product-reviews-behind-a-login
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/pexels-pixabay-159751--1-.jpg
tags:
- name: node js
  slug: node-js
- name: puppeteer
  slug: puppeteer
- name: web scraping
  slug: web-scraping
seo_title: Comment extraire les avis sur les produits Amazon derrière une connexion
seo_desc: "By Satyam Tripathi\nAmazon is the most popular e-commerce website for web\
  \ scrapers, with billions of product pages being scraped every month. \nIt is also\
  \ home to a vast database of product reviews, which can be very useful for market\
  \ research and comp..."
---

Par Satyam Tripathi

Amazon est le site de commerce électronique le plus populaire pour les scrapers web, avec des milliards de pages de produits étant scrapées chaque mois. 

Il abrite également une vaste base de données d'avis sur les produits, qui peuvent être très utiles pour la recherche de marché et la surveillance des concurrents. 

Vous pouvez extraire des données pertinentes du site Amazon et les enregistrer dans un tableau ou un format JSON. Et vous pouvez même automatiser le processus pour mettre à jour les données régulièrement.

L'extraction des avis sur les produits Amazon n'est pas toujours simple, surtout lorsqu'une connexion est requise. Dans ce guide, vous apprendrez comment extraire les avis sur les produits Amazon derrière une connexion. Vous apprendrez le processus de connexion, d'analyse des données d'avis et d'exportation des avis vers CSV.

**Avertissement important :** Ce tutoriel est à des fins éducatives uniquement. L'extraction de données derrière des connexions sur des sites web peut violer leurs termes et conditions (T&C). Il est crucial de toujours vérifier les T&C de tout site web avant d'extraire des données.

Sans plus attendre, commençons.

## Prérequis et configuration du projet

Nous utiliserons la bibliothèque Node.js Puppeteer pour extraire les avis Amazon. Assurez-vous que Node.js est installé sur votre système. Si ce n'est pas le cas, rendez-vous sur le site officiel de [Node.js](https://nodejs.org/en) et installez-le. 

Après avoir installé Node.js, installez Puppeteer. [Puppeteer](https://github.com/puppeteer/puppeteer) est une bibliothèque Node.js qui fournit une API de haut niveau, conviviale pour automatiser les tâches et interagir avec des pages web dynamiques. 

Maintenant, installons et configurons Puppeteer.

Ouvrez un terminal et créez un nouveau dossier avec n'importe quel nom. (Dans mon cas, c'est _amazon_reviews_).

```bash
mkdir amazon_reviews
```

Changez votre répertoire courant pour le dossier créé ci-dessus.

```bash
cd amazon_reviews
```

Super, vous êtes maintenant dans le bon répertoire. Exécutez la commande suivante pour initialiser le fichier _package.json_ :

```bash
npm init -y
```

Enfin, installez Puppeteer en utilisant la commande suivante :

```bash
npm install puppeteer
```

Voici à quoi ressemble le processus :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-070530.png)

Maintenant, ouvrez le dossier dans n'importe quel éditeur de code, et créez un nouveau fichier JavaScript (index.js). Assurez-vous que la hiérarchie ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-070823.png)
_Hiérarchie montrant `node_modules`, `index.js`, `package-lock.json`, et `package.json`_

Tout est configuré avec succès. Nous sommes maintenant prêts à coder le scraper.

**Note :** Assurez-vous d'avoir un compte sur Amazon pour pouvoir suivre le reste de ce tutoriel.

## Étape 1 : Accéder à la page publique

Vous allez extraire les avis du produit montré ci-dessous. Vous extrairez le nom de l'auteur, le titre de l'avis et la date.

Voici l'URL du produit : [https://www.amazon.com/ENHANCE-Headphone-Customizable-Lighting-Flexible/dp/B07DR59JLP/](https://www.amazon.com/ENHANCE-Headphone-Customizable-Lighting-Flexible/dp/B07DR59JLP/)

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-072923.png)
_Le produit que nous utilisons dans l'exemple - des écouteurs_

Tout d'abord, vous vous connecterez à Amazon, puis vous serez redirigé vers l'URL du produit pour extraire les avis.

## Étape 2 : Extraire derrière la connexion

Le processus de connexion en plusieurs étapes d'Amazon nécessite que les utilisateurs entrent leur nom d'utilisateur ou leur email, cliquent sur un bouton Continuer pour entrer leur mot de passe, puis le soumettent enfin. Les champs du nom d'utilisateur et du mot de passe sont généralement sur des pages différentes.

Pour entrer l'ID email, utilisez le sélecteur `input[name=email]`.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-082325.png)
_HTML du champ de connexion_

Maintenant, cliquez sur le bouton Continuer en utilisant le sélecteur `input[id=continue]`.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-083136.png)
_HTML du bouton continuer_

Vous devriez maintenant être sur la page suivante. Pour entrer le mot de passe, utilisez le sélecteur `input[name=password]`.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-083415.png)
_HTML du champ de mot de passe_

Enfin, cliquez sur le bouton Se connecter en utilisant le sélecteur `input[id=signInSubmit]`.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-083833.png)
_HTML du bouton de connexion_

Voici le code pour le processus de connexion :

```javascript
const selectors = {
  emailid: 'input[name=email]',
  password: 'input[name=password]',
  continue: 'input[id=continue]',
  singin: 'input[id=signInSubmit]',
};


    await page.goto(signinURL);
    await page.waitForSelector(selectors.emailid);
    await page.type(selectors.emailid, "satyam@gmail.com", { delay: 100 });
    await page.click(selectors.continue);
    await page.waitForSelector(selectors.password);
    await page.type(selectors.password, "mypassword", { delay: 100 });
    await page.click(selectors.singin);
    await page.waitForNavigation();
```

Nous suivons les mêmes étapes que discutées ci-dessus. Tout d'abord, allez à l'URL de connexion, entrez l'ID email, et cliquez sur le bouton Continuer. Ensuite, entrez le mot de passe, cliquez sur le bouton Se connecter, et attendez un moment pour que le processus de connexion se termine.

Après que le processus de connexion soit terminé, vous serez redirigé vers la page du produit pour extraire les avis.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-072923-1.png)
_Page du produit_

## Étape 3 : Analyser les données d'avis

Vous vous êtes connecté avec succès et vous êtes maintenant sur la page du produit que vous souhaitez extraire. Analysons maintenant les données d'avis.

Sur la page, vous trouverez divers avis. Ces avis sont contenus dans une div parent avec l'ID `cm-cr-dp-review-list`, qui contient tous les avis sur la page actuelle. Si vous souhaitez accéder à plus d'avis, vous devrez naviguer vers la page suivante en utilisant le processus de pagination.

Cette div parent a plusieurs divs enfants, et chaque div enfant contient un avis. Pour extraire les avis, vous pouvez utiliser le sélecteur `#cm-cr-dp-review-list div.review`.

```javascript
const selectors = {
  allReviews: '#cm-cr-dp-review-list div.review',
  authorName: 'div[data-hook="genome-widget"] span.a-profile-name',
  reviewTitle: '[data-hook=review-title]>span:not([class])',
  reviewDate: 'span[data-hook=review-date]',
};
```

Ce sélecteur montre que vous allez d'abord à l'élément avec l'ID `cm-cr-dp-review-list`, puis vous recherchez tous les éléments `div` avec le data-hook `review`. 

![Image](https://www.freecodecamp.org/news/content/images/2023/10/annotely_image.png)
_Données d'avis avec le nom de l'auteur, le titre de l'avis, la description, etc._

L'extrait de code suivant montre que vous devez d'abord aller à l'URL du produit, attendre que le sélecteur se charge, puis extraire tous les avis et les stocker dans la variable `reviewElements`.

```javascript
await page.goto(productURL);
await page.waitForSelector(selectors.allReviews);
const reviewElements = await page.$$(selectors.allReviews);
```

Maintenant, extrayons le nom de l'auteur, le titre de l'avis et la date.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-091701.png)
_Ciblage du nom de l'auteur, du titre de l'avis et de la date_

Pour analyser le nom de l'auteur, vous pouvez utiliser le sélecteur `div[data-hook="genome-widget"] span.a-profile-name`. Ce sélecteur nous indique de rechercher d'abord l'élément `div` avec l'attribut `data-hook` défini sur `genome-widget`, car les noms sont à l'intérieur de cet élément `div`. Ensuite, recherchez l'élément `span` avec le nom de classe `a-profile-name`. C'est l'élément qui contient le nom de l'auteur.

```javascript
const author = await reviewElement.$eval(selectors.authorName, (element) => element.textContent);
```

Pour analyser le titre de l'avis, vous pouvez utiliser le sélecteur CSS `[data-hook="review-title"] > span:not([class])`. Ce sélecteur nous indique de rechercher l'élément `span` qui est un enfant direct de l'élément `[data-hook="review-title"]` et qui n'a pas d'attribut de classe.

```javascript
const title = await reviewElement.$eval(selectors.reviewTitle, (element) => element.textContent);
```

Pour analyser la date, vous pouvez utiliser le sélecteur CSS `span[data-hook="review-date"]`. Ce sélecteur nous indique de rechercher l'élément span qui a l'attribut `data-hook` défini sur `review-date`. C'est l'élément qui contient la date de l'avis.

```javascript
const rawReviewDate = await reviewElement.$eval(selectors.reviewDate, (element) => element.textContent);
```

Notez que vous obtiendrez tout le texte, y compris l'emplacement, au lieu de la date complète. Par conséquent, vous devez utiliser une expression régulière pour extraire la date du texte. 

Après cela, combinez toutes les données dans `reviewData` puis ajoutez-les à la liste finale `reviewsData`.

```javascript
const datePattern = /(\w+\s\d{1,2},\s\d{4})/;
      const match = rawReviewDate.match(datePattern);
      const reviewDate = match ? match[0].replace(',', '') : "Date non trouvée";

      const reviewData = {
        author,
        title,
        reviewDate,
      };

      reviewsData.push(reviewData);
    }
```

Le processus ci-dessus s'exécutera jusqu'à ce qu'il ait analysé tous les avis de la page actuelle. Voici l'extrait de code pour analyser les données :

```javascript
for (const reviewElement of reviewElements) {
      const author = await reviewElement.$eval(selectors.authorName, (element) => element.textContent);
      const title = await reviewElement.$eval(selectors.reviewTitle, (element) => element.textContent);
      const rawReviewDate = await reviewElement.$eval(selectors.reviewDate, (element) => element.textContent);

      const datePattern = /(\w+\s\d{1,2},\s\d{4})/;
      const match = rawReviewDate.match(datePattern);
      const reviewDate = match ? match[0].replace(',', '') : "Date non trouvée";

      const reviewData = {
        author,
        title,
        reviewDate,
      };

      reviewsData.push(reviewData);
    }
```

Super ! Vous avez réussi à analyser les données pertinentes, qui sont maintenant au format JSON, comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-095917.png)
_Données extraites au format JSON_

## Étape 4 : Exporter les avis vers un CSV

Vous avez analysé les avis au format JSON, qui est un peu lisible par l'homme. Vous pouvez convertir ces données au format CSV pour les rendre plus lisibles et plus faciles à utiliser pour d'autres fins. 

Il existe de nombreuses façons de convertir des données JSON en CSV, mais nous utiliserons une approche simple et efficace. Voici un extrait de code simple pour convertir JSON en CSV :

```javascript
let csvContent = "Author,Title,Date\n
for (const review of reviewsData) {
      const { author, title, reviewDate } = review;
      csvContent += `${author},"${title}",${reviewDate}\n`;
    }

const csvFileName = "amazon_reviews.csv";
await fs.writeFileSync(csvFileName, csvContent, "utf8");
```

Voici le résultat du fichier CSV.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-27-102705.png)
_Données JSON converties au format CSV_

Et voilà !

Vous pouvez trouver le code complet téléchargé sur GitHub [ici](https://gist.github.com/triposat/20706d61989a4031669c2e3d25f487d0).

## Conclusion

Dans ce guide, vous avez appris comment extraire les avis sur les produits Amazon derrière une connexion en utilisant Puppeteer. Vous avez appris comment vous connecter, analyser les données pertinentes et les enregistrer dans un fichier CSV. 

Pour vous entraîner davantage, vous pouvez extraire tous les avis de toutes les pages en utilisant la pagination.
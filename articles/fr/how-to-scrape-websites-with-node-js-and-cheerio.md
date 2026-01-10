---
title: Comment scraper des sites web avec Node.js et Cheerio
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2021-07-19T16:50:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-scrape-websites-with-node-js-and-cheerio
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/scraping-1.jpg
tags:
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: web scraping
  slug: web-scraping
seo_title: Comment scraper des sites web avec Node.js et Cheerio
seo_desc: 'There might be times when a website has data you want to analyze but the
  site doesn''t expose an API for accessing those data.

  To get the data, you''ll have to resort to web scraping.

  In this article, I''ll go over how to scrape websites with Node.js an...'
---

Il peut arriver qu'un site web contienne des données que vous souhaitez analyser, mais que le site ne propose pas d'API pour y accéder.

Pour obtenir les données, vous devrez recourir au [web scraping](https://en.wikipedia.org/wiki/Web_scraping).

Dans cet article, je vais expliquer comment scraper des sites web avec [Node.js](https://nodejs.dev/) et [Cheerio](https://cheerio.js.org/).

Avant de commencer, vous devez être conscient qu'il existe des [questions légales et éthiques](https://monashdatafluency.github.io/python-web-scraping/section-5-legal-and-ethical-considerations/) à considérer avant de scraper un site. Il est de votre responsabilité de vous assurer qu'il est acceptable de scraper un site avant de le faire.

Les sites utilisés dans les exemples de cet article autorisent tous le scraping, alors n'hésitez pas à suivre les étapes.

## Prérequis

Voici quelques éléments dont vous aurez besoin pour ce tutoriel :

* Vous devez avoir [Node.js](https://nodejs.dev) installé. Si vous n'avez pas Node, assurez-vous de le télécharger pour votre système depuis la [page de téléchargement de Node.js](https://nodejs.dev/download/)

* Vous devez avoir un éditeur de texte comme [VSCode](https://code.visualstudio.com/) ou [Atom](https://atom.io/) installé sur votre machine

* Vous devriez avoir au moins une compréhension de base de JavaScript, Node.js et du Document Object Model (DOM). Mais vous pouvez toujours suivre même si vous êtes un débutant complet avec ces technologies. N'hésitez pas à poser des questions sur le [forum freeCodeCamp](https://forum.freecodecamp.org/) si vous êtes bloqué

## Qu'est-ce que le Web Scraping ?

> Le [web scraping](https://en.wikipedia.org/wiki/Web_scraping) est le processus d'extraction de données d'une page web. Bien que vous puissiez faire du web scraping manuellement, le terme fait généralement référence à l'extraction automatisée de données à partir de sites web - [Wikipedia](https://en.wikipedia.org/wiki/Web_scraping).

## Qu'est-ce que Cheerio ?

Cheerio est un outil pour analyser HTML et XML dans Node.js, et est très populaire avec plus de [23k étoiles](https://github.com/cheeriojs/cheerio) sur GitHub.

Il est rapide, flexible et facile à utiliser. Puisqu'il implémente un sous-ensemble de JQuery, il est facile de commencer à utiliser Cheerio si vous êtes déjà familier avec JQuery.

Selon la [documentation](https://cheerio.js.org/), Cheerio analyse le balisage et fournit une API pour manipuler la structure de données résultante, mais n'interprète pas le résultat comme un navigateur web.

> La principale différence entre cheerio et un navigateur web est que cheerio ne produit pas de rendu visuel, ne charge pas de CSS, ne charge pas de ressources externes et n'exécute pas de JavaScript. Il analyse simplement le balisage et fournit une API pour manipuler la structure de données résultante. C'est ce qui explique pourquoi il est également très rapide - [documentation de cheerio](https://cheerio.js.org/).

Si vous souhaitez utiliser cheerio pour scraper une page web, vous devez d'abord récupérer le balisage à l'aide de packages comme [axios](https://axios-http.com/docs/intro) ou [node-fetch](https://www.npmjs.com/package/node-fetch) parmi d'autres.

## Comment scraper une page web dans Node en utilisant Cheerio

Dans cette section, vous apprendrez à scraper une page web en utilisant cheerio. Il est important de souligner que, avant de scraper un site web, assurez-vous d'avoir la permission de le faire – sinon, vous pourriez vous retrouver en violation des conditions de service, en violation de copyright ou en violation de la vie privée.

Dans cet exemple, nous allons scraper les [codes ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#:~:text=ISO%203166%2D1%20alpha%2D3%20codes%20are%20three%2Dletter,special%20areas%20of%20geographical%20interest.) pour tous les pays et autres juridictions comme listés sur [cette page Wikipedia](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3). Il se trouve dans la section **Codes actuels** de la page [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3).

Voici à quoi ressemble la liste des pays/juridictions et leurs codes correspondants :

![liste des pays et codes correspondants](https://www.freecodecamp.org/news/content/images/2021/07/007-05-list-of-countries.png align="left")

Vous pouvez suivre les étapes ci-dessous pour scraper les données de la liste ci-dessus.

### Étape 1 - Créer un répertoire de travail

Dans cette étape, vous allez créer un répertoire pour votre projet en exécutant la commande suivante dans le terminal. La commande créera un répertoire appelé `learn-cheerio`. Vous pouvez lui donner un autre nom si vous le souhaitez.

```sh
mkdir learn-cheerio
```

Vous devriez voir un dossier nommé `learn-cheerio` créé après avoir exécuté avec succès la commande ci-dessus.

Dans l'étape suivante, vous allez ouvrir le répertoire que vous venez de créer dans votre éditeur de texte préféré et initialiser le projet.

### Étape 2 - Initialiser le projet

Dans cette étape, vous allez naviguer vers votre répertoire de projet et initialiser le projet. Ouvrez le répertoire que vous avez créé dans l'étape précédente dans votre éditeur de texte préféré et initialisez le projet en exécutant la commande suivante.

```js
npm init -y
```

L'exécution réussie de la commande ci-dessus créera un fichier `package.json` à la racine de votre répertoire de projet.

Dans l'étape suivante, vous allez installer les dépendances du projet.

### Étape 3 - Installer les dépendances

Dans cette étape, vous allez installer les dépendances du projet en exécutant la commande suivante. Cela prendra quelques minutes, alors soyez patient.

```js
npm i axios cheerio pretty
```

L'exécution réussie de la commande ci-dessus enregistrera trois dépendances dans le fichier `package.json` sous le champ `dependencies`. La première dépendance est `axios`, la deuxième est `cheerio`, et la troisième est `pretty`.

[axios](https://axios-http.com/docs/intro) est un client http très populaire qui fonctionne dans Node et dans le navigateur. Nous en avons besoin car cheerio est un analyseur de balisage.

Pour que cheerio analyse le balisage et scrape les données dont vous avez besoin, nous devons utiliser `axios` pour récupérer le balisage du site web. Vous pouvez utiliser un autre client HTTP pour récupérer le balisage si vous le souhaitez. Il n'est pas nécessaire que ce soit `axios`.

[pretty](https://www.npmjs.com/package/pretty) est un package npm pour embellir le balisage afin qu'il soit lisible lorsqu'il est imprimé sur le terminal.

Dans la section suivante, vous allez inspecter le balisage dont vous allez extraire les données.

### Étape 4 - Inspecter la page web que vous souhaitez scraper

Avant de scraper des données d'une page web, il est très important de comprendre la structure HTML de la page.

Dans cette étape, vous allez inspecter la structure HTML de la page web dont vous allez extraire les données.

Accédez à la page [codes ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) sur Wikipedia. Dans la section "Codes actuels", il y a une liste de pays et leurs codes correspondants. Vous pouvez ouvrir les DevTools en appuyant sur la combinaison de touches `CTRL + SHIFT + I` sur Chrome ou en faisant un clic droit puis en sélectionnant l'option "Inspecter".

Voici à quoi ressemble la liste pour moi dans les DevTools de Chrome :

![Liste dans les outils de développement de Chrome](https://www.freecodecamp.org/news/content/images/2021/07/007-04-dev-tool.png align="left")

Dans la section suivante, vous allez écrire le code pour scraper la page web.

### Étape 5 - Écrire le code pour scraper les données

Dans cette section, vous allez écrire le code pour scraper les données qui nous intéressent. Commencez par exécuter la commande suivante qui créera le fichier `app.js`.

```js
touch app.js
```

L'exécution réussie de la commande ci-dessus créera un fichier `app.js` à la racine du répertoire du projet.

Comme pour tout autre package Node, vous devez d'abord *importer* `axios`, `cheerio` et `pretty` avant de commencer à les utiliser. Vous pouvez le faire en ajoutant le code suivant en haut du fichier `app.js` que vous venez de créer.

```js
const axios = require("axios");
const cheerio = require("cheerio");
const pretty = require("pretty");
```

Avant d'écrire le code pour scraper nos données, nous devons apprendre les bases de `cheerio`. Nous allons analyser le balisage ci-dessous et essayer de manipuler la structure de données résultante. Cela nous aidera à apprendre la syntaxe de cheerio et ses méthodes les plus courantes.

Le balisage ci-dessous est l'élément `ul` contenant nos éléments `li`.

```js
const markup = `
<ul class="fruits">
  <li class="fruits__mango"> Mango </li>
  <li class="fruits__apple"> Apple </li>
</ul>
`;
```

Ajoutez la déclaration de variable ci-dessus au fichier `app.js`.

## Comment charger le balisage dans Cheerio

Vous pouvez charger le balisage dans `cheerio` en utilisant la méthode `cheerio.load`. La méthode prend le balisage comme argument. Elle prend également deux arguments optionnels supplémentaires. Vous pouvez en lire plus à leur sujet [dans la documentation](https://cheerio.js.org/) si vous êtes intéressé.

Ci-dessous, nous passons le premier et seul argument requis et stockons la valeur retournée dans la variable `$`. Nous utilisons la variable `$` en raison de la similitude de cheerio avec [Jquery](https://jquery.com/). Vous pouvez utiliser un nom de variable différent si vous le souhaitez.

Ajoutez le code suivant à votre fichier `app.js` :

```js
const $ = cheerio.load(markup);
console.log(pretty($.html()));
```

Si vous exécutez maintenant le code dans votre fichier `app.js` en exécutant la commande `node app.js` dans le terminal, vous devriez voir le balisage dans le terminal. Voici ce que je vois dans mon terminal :

![Sortie du terminal du balisage](https://www.freecodecamp.org/news/content/images/2021/07/007-01-cheerio-html.png align="left")

## Comment sélectionner un élément dans Cheerio

Cheerio prend en charge la plupart des sélecteurs CSS courants tels que les sélecteurs `class`, `id` et `element` parmi d'autres. Dans le code ci-dessous, nous sélectionnons l'élément avec la classe `fruits__mango` puis nous enregistrons l'élément sélectionné dans la console. Ajoutez le code suivant à votre fichier `app.js`.

```js
const mango = $(".fruits__mango");
console.log(mango.html()); // Mango
```

Les lignes de code ci-dessus enregistreront le texte `Mango` dans le terminal si vous exécutez `app.js` en utilisant la commande `node app.js`.

## Comment obtenir l'attribut d'un élément dans Cheerio

Vous pouvez également sélectionner un élément et obtenir un attribut spécifique tel que la `class`, `id`, ou tous les attributs et leurs valeurs correspondantes.

Ajoutez le code suivant à votre fichier `app.js` :

```js
const apple = $(".fruits__apple");
console.log(apple.attr("class")); //fruits__apple
```

Le code ci-dessus enregistrera `fruits__apple` dans le terminal. `fruits__apple` est la classe de l'élément sélectionné.

## Comment parcourir une liste d'éléments dans Cheerio

Cheerio fournit la méthode `.each` pour parcourir plusieurs éléments sélectionnés.

Ci-dessous, nous sélectionnons tous les éléments `li` et les parcourons en utilisant la méthode `.each`. Nous enregistrons le contenu textuel de chaque élément de liste dans le terminal.

Ajoutez le code suivant à votre fichier `app.js`.

```js
const listItems = $("li");
console.log(listItems.length); // 2
listItems.each(function (idx, el) {
  console.log($(el).text());
});
// Mango
// Apple
```

Le code ci-dessus enregistrera `2`, qui est la longueur des éléments de liste, et le texte `Mango` et `Apple` dans le terminal après avoir exécuté le code dans `app.js`.

## Comment ajouter ou insérer un élément dans un balisage dans Cheerio

Cheerio fournit une méthode pour ajouter ou insérer un élément dans un balisage.

La méthode `append` ajoutera l'élément passé en argument après le dernier enfant de l'élément sélectionné. D'autre part, `prepend` ajoutera l'élément passé avant le premier enfant de l'élément sélectionné.

Ajoutez le code suivant à votre fichier `app.js` :

```js
const ul = $("ul");
ul.append("<li>Banana</li>");
ul.prepend("<li>Pineapple</li>");
console.log(pretty($.html()));
```

Après avoir ajouté et inséré des éléments dans le balisage, voici ce que je vois lorsque je enregistre `$.html()` dans le terminal :

![Sortie du terminal après ajout ou insertion](https://www.freecodecamp.org/news/content/images/2021/07/007-02-append-prepend.png align="left")

Ce sont les bases de cheerio qui peuvent vous aider à commencer avec le web scraping.

Pour scraper les données que nous avons décrites au début de cet article à partir de Wikipedia, copiez et collez le code ci-dessous dans le fichier `app.js` :

```js
// Chargement des dépendances. Nous n'avons pas besoin de pretty
// car nous n'allons pas enregistrer de html dans le terminal
const axios = require("axios");
const cheerio = require("cheerio");
const fs = require("fs");

// URL de la page que nous voulons scraper
const url = "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3";

// Fonction asynchrone qui scrape les données
async function scrapeData() {
  try {
    // Récupérer le HTML de la page que nous voulons scraper
    const { data } = await axios.get(url);
    // Charger le HTML que nous avons récupéré dans la ligne précédente
    const $ = cheerio.load(data);
    // Sélectionner tous les éléments de liste dans la classe plainlist
    const listItems = $(".plainlist ul li");
    // Stocke les données pour tous les pays
    const countries = [];
    // Utiliser la méthode .each pour parcourir les li que nous avons sélectionnés
    listItems.each((idx, el) => {
      // Objet contenant les données pour chaque pays/juridiction
      const country = { name: "", iso3: "" };
      // Sélectionner le contenu textuel des éléments a et span
      // Stocker le contenu textuel dans l'objet ci-dessus
      country.name = $(el).children("a").text();
      country.iso3 = $(el).children("span").text();
      // Remplir le tableau countries avec les données des pays
      countries.push(country);
    });
    // Enregistrer le tableau countries dans la console
    console.dir(countries);
    // Écrire le tableau countries dans le fichier countries.json
    fs.writeFile("countries.json", JSON.stringify(countries, null, 2), (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log("Données écrites avec succès dans le fichier");
    });
  } catch (err) {
    console.error(err);
  }
}
// Invoquer la fonction ci-dessus
scrapeData();
```

Comprenez-vous ce qui se passe en lisant le code ? Si ce n'est pas le cas, je vais entrer dans quelques détails maintenant. J'ai également fait des commentaires sur chaque ligne de code pour vous aider à comprendre.

Dans le code ci-dessus, nous *importons* toutes les dépendances en haut du fichier `app.js`, puis nous avons déclaré la fonction `scrapeData`. À l'intérieur de la fonction, le balisage est récupéré en utilisant `axios`. Le HTML récupéré de la page que nous devons scraper est ensuite chargé dans `cheerio`.

La liste des pays/juridictions et leurs codes `iso3` correspondants sont imbriqués dans un élément `div` avec une classe `plainlist`. Les éléments `li` sont sélectionnés, puis nous les parcourons en utilisant la méthode `.each`. Les données de chaque pays sont scrapées et stockées dans un tableau.

Après avoir exécuté le code ci-dessus en utilisant la commande `node app.js`, les données scrapées sont écrites dans le fichier `countries.json` et imprimées dans le terminal. Voici une partie de ce que je vois dans mon terminal :

![Sortie du terminal](https://www.freecodecamp.org/news/content/images/2021/07/007-03-terminal-output.png align="left")

## Conclusion

Merci d'avoir lu cet article et d'être arrivé à la fin ! Nous avons couvert les bases du web scraping en utilisant `cheerio`. Vous pouvez vous rendre sur la [documentation de cheerio](https://cheerio.js.org/) si vous souhaitez approfondir et comprendre pleinement son fonctionnement.

N'hésitez pas à poser des questions sur le [forum freeCodeCamp](https://forum.freecodecamp.org/) si quelque chose dans cet article n'est pas clair pour vous.

Enfin, n'oubliez pas de prendre en compte les [considérations éthiques](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01) lorsque vous apprenez le web scraping.
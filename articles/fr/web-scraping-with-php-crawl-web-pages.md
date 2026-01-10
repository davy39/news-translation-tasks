---
title: Web Scraping avec PHP – Comment parcourir des pages web en utilisant des outils
  open source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-22T21:11:53.000Z'
originalURL: https://freecodecamp.org/news/web-scraping-with-php-crawl-web-pages
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/scraping-with-php-image-1.png
tags:
- name: data
  slug: data
- name: open source
  slug: open-source
- name: PHP
  slug: php
- name: web scraping
  slug: web-scraping
seo_title: Web Scraping avec PHP – Comment parcourir des pages web en utilisant des
  outils open source
seo_desc: "By Manthan Koolwal\nWeb scraping lets you collect data from web pages across\
  \ the internet. It's also called web crawling or web data extraction. \nPHP is a\
  \ widely used back-end scripting language for creating dynamic websites and web\
  \ applications. And ..."
---

Par Manthan Koolwal

Le web scraping permet de collecter des données à partir de pages web sur Internet. On l'appelle aussi web crawling ou extraction de données web.

PHP est un langage de script back-end largement utilisé pour créer des sites web dynamiques et des applications web. Et vous pouvez implémenter un web scraper en utilisant du code PHP simple.

Mais comme nous ne voulons pas réinventer la roue, nous pouvons utiliser certaines bibliothèques PHP open source prêtes à l'emploi pour nous aider à collecter nos données.

Dans ce tutoriel, nous discuterons des différents outils et services que vous pouvez utiliser avec PHP pour scraper une page web. Les outils que nous aborderons sont Guzzle, Goutte, Simple HTML DOM et le navigateur headless Symfony Panther.

Note : avant de scraper un site web, vous devez lire attentivement leurs Conditions d'utilisation pour vous assurer qu'ils acceptent d'être scrapés. Le scraping de données – même si elles sont publiquement accessibles – peut potentiellement surcharger les serveurs d'un site web. (Qui sait – si vous demandez poliment, ils pourraient même vous donner une clé API pour que vous n'ayez pas à scraper. 😉)

## Comment installer le projet

Avant de commencer, si vous souhaitez suivre et essayer le code, voici quelques prérequis pour votre environnement de développement :

* Assurez-vous d'avoir installé la dernière version de PHP.
* Allez sur ce lien [Composer](https://getcomposer.org/) pour configurer un composer que nous utiliserons pour installer les différentes dépendances PHP pour les bibliothèques de web scraping.
* Un éditeur de votre choix.

Une fois que vous avez terminé tout cela, créez un répertoire de projet et naviguez dans le répertoire :

```
mkdir php_scraper

cd php_scraper
```

Exécutez les deux commandes suivantes dans votre terminal pour initialiser le fichier **composer.json** :

```
composer init --require="php >=7.4" --no-interaction

composer update
```

Commençons.

## Web Scraping avec PHP en utilisant Guzzle, XML et XPath

[Guzzle](http://docs.guzzlephp.org/en/stable/) est un client HTTP PHP qui permet d'envoyer des requêtes HTTP rapidement et facilement. Il dispose d'une interface simple pour construire des chaînes de requête.

[XML](https://en.wikipedia.org/wiki/XML) est un langage de balisage qui encode les documents pour qu'ils soient lisibles par l'homme et par la machine.

Et [XPath](https://en.wikipedia.org/wiki/XPath) est un langage de requête qui navigue et sélectionne les nœuds XML.

Voyons comment nous pouvons utiliser ces trois outils ensemble pour scraper un site web.

Commencez par installer Guzzle via composer en exécutant la commande suivante dans votre terminal :

```
composer require guzzlehttp/guzzle
```

Une fois que vous avez installé Guzzle, créons un nouveau fichier PHP auquel nous ajouterons le code. Nous l'appellerons **guzzle_requests.php**.

Pour cette démonstration, nous allons scraper le site web [Books to Scrape](https://books.toscrape.com/). Vous devriez pouvoir suivre les mêmes étapes que nous définissons ici pour scraper n'importe quel site web de votre choix.

Le site web Books to Scrape ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/books-to-scrape-website.png)

Nous voulons extraire les titres des livres et les afficher sur le terminal.

La première étape pour scraper un site web est de comprendre sa structure HTML. Dans ce cas, vous pouvez voir la structure HTML de cette page en faisant un clic droit sur la page, juste au-dessus du premier produit de la liste, et en sélectionnant **Inspecter**.

Voici une capture d'écran montrant un extrait du code source de la page :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free2.png)

Vous pouvez voir que la liste est contenue dans l'élément **<ol class="row">**. L'enfant direct suivant est l'élément **<li>**.

Ce que nous voulons, c'est le titre du livre. Il se trouve à l'intérieur de la balise **<a>**, qui est elle-même à l'intérieur de la balise **<h3>**, qui est à l'intérieur de la balise **<article>**, qui est enfin à l'intérieur de l'élément **<li>**.

Pour initialiser Guzzle, XML et Xpath, ajoutez le code suivant au fichier **guzzle_requests.php** :

```php
<?php
# scraping books to scrape: https://books.toscrape.com/
require 'vendor/autoload.php';
$httpClient = new \GuzzleHttp\Client();
$response = $httpClient->get('https://books.toscrape.com/');
$htmlString = (string) $response->getBody();
//ajoutez cette ligne pour supprimer les avertissements
libxml_use_internal_errors(true);
$doc = new DOMDocument();
$doc->loadHTML($htmlString);
$xpath = new DOMXPath($doc);
```

Le code ci-dessus chargera la page web dans une chaîne. Nous analysons ensuite la chaîne en utilisant XML et l'assignons à la variable **$xpath**.

La chose suivante que vous voulez faire est de cibler le contenu textuel à l'intérieur de la balise **<a>**. Ajoutez le code suivant au fichier :

```php
$titles = $xpath->evaluate('//ol[@class="row"]//li//article//h3/a');
$extractedTitles = [];
foreach ($titles as $title) {
$extractedTitles[] = $title->textContent.PHP_EOL;
echo $title->textContent.PHP_EOL;
}
```

Dans l'extrait de code ci-dessus, **//ol[@class="row"]** obtient toute la liste.

Chaque élément de la liste a une balise **<a>** que nous ciblons pour extraire le titre réel du livre. Nous n'avons qu'une seule balise <h3> contenant la balise <a>, ce qui facilite le ciblage direct.

Nous utilisons la boucle **foreach** pour extraire les contenus textuels et les afficher sur le terminal.

À cette étape, vous pouvez choisir de faire quelque chose avec vos données extraites, peut-être assigner les données à une variable de tableau, écrire dans un fichier ou les stocker dans une base de données.

Vous pouvez exécuter le fichier en utilisant PHP sur le terminal en exécutant la commande ci-dessous. N'oubliez pas, la partie surlignée est le nom que nous avons donné à notre fichier :

```
php guzzle_requests.php
```

Cela devrait afficher quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free3.png)

Cela s'est bien passé.

Maintenant, que se passe-t-il si nous voulions aussi obtenir le prix du livre ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free4.png)

Le prix se trouve dans la balise **<p>**, à l'intérieur d'une balise <div>. Comme vous pouvez le voir, il y a plus d'une balise <p> et plus d'une balise <div>.

Pour trouver la bonne cible, nous utiliserons les sélecteurs de classe CSS qui, heureusement pour nous, sont uniques pour chaque balise. Voici l'extrait de code pour obtenir également la balise de prix et la concaténer à la chaîne de titre :

```php
$titles = $xpath->evaluate('//ol[@class="row"]//li//article//h3/a');
$prices = $xpath->evaluate('//ol[@class="row"]//li//article//div[@class="product_price"]//p[@class="price_color"]');
foreach ($titles as $key => $title) {
echo $title->textContent . ' @ '. $prices[$key]->textContent.PHP_EOL;
}
```

Si vous exécutez le code sur votre terminal, vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free5.png)

Votre code complet devrait ressembler à ceci :

```php
<?php
# scraping books to scrape: https://books.toscrape.com/
require 'vendor/autoload.php';
$httpClient = new \GuzzleHttp\Client();
$response = $httpClient->get('https://books.toscrape.com/');
$htmlString = (string) $response->getBody();
//ajoutez cette ligne pour supprimer les avertissements
libxml_use_internal_errors(true);
$doc = new DOMDocument();
$doc->loadHTML($htmlString);
$xpath = new DOMXPath($doc);
$titles = $xpath->evaluate('//ol[@class="row"]//li//article//h3/a');
$prices = $xpath->evaluate('//ol[@class="row"]//li//article//div[@class="product_price"]//p[@class="price_color"]');
foreach ($titles as $key => $title) {
echo $title->textContent . ' @ '. $prices[$key]->textContent.PHP_EOL;
}
```

Bien sûr, ceci est un scraper web basique, et vous pouvez certainement l'améliorer. Passons à la bibliothèque suivante.

## Web Scraping en PHP avec Goutte

[Goutte](https://github.com/FriendsOfPHP/Goutte) est un autre excellent client HTTP pour PHP spécialement conçu pour le web scraping. Il a été développé par le créateur du [Framework Symfony](https://symfony.com/) et fournit une belle API pour scraper des données à partir des réponses HTML/XML des sites web.

Voici quelques-uns des composants qu'il inclut pour simplifier le web crawling :

* [Composant BrowserKit](https://symfony.com/doc/current/components/browser_kit.html) pour simuler le comportement d'un navigateur web.
* [Composant CssSelector](https://symfony.com/doc/current/components/css_selector.html) pour traduire les requêtes CSS en requêtes XPath.
* [Composant DomCrawler](https://symfony.com/doc/current/components/dom_crawler.html) apporte la puissance de DOMDocument et XPath.
* [Client HTTP Symfony](https://symfony.com/doc/current/http_client.html) est un composant relativement nouveau de l'équipe Symfony.

Installez Goutte via composer en exécutant la commande suivante sur votre terminal :

```
composer require fabpot/goutte
```

Une fois que vous avez installé le package Goutte, créez un nouveau fichier PHP pour notre code – appelons-le **goutte_requests.php**.

Dans cette section, nous discuterons de ce que nous avons fait avec la bibliothèque Guzzle dans la première section.

Nous allons scraper les titres de livres du site [Books to Scrape](https://books.toscrape.com/) en utilisant Goutte. Ensuite, nous verrons comment vous pouvez ajouter les prix dans une variable de tableau et utiliser la variable dans le code.

Ajoutez le code suivant à l'intérieur du fichier goutte_requests.php :

```php
<?php
# scraping books to scrape: https://books.toscrape.com/
require 'vendor/autoload.php';
$httpClient = new \Goutte\Client();
$response = $httpClient->request('GET', 'https://books.toscrape.com/');
$titles = $response->evaluate('//ol[@class="row"]//li//article//h3/a');
$prices = $response->evaluate('//ol[@class="row"]//li//article//div[@class="product_price"]//p[@class="price_color"]');
// nous pouvons stocker les prix dans un tableau
$priceArray = [];
foreach ($prices as $key => $price) {
$priceArray[] = $price->textContent;
}
// nous extrayons les titres et les affichons sur le terminal avec les prix
foreach ($titles as $key => $title) {
echo $title->textContent . ' @ '. $priceArray[$key] . PHP_EOL;
}
```

Exécutez le code en exécutant la commande suivante dans le terminal :

```
php goutte_requests.php
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free6.png)

C'est une façon de faire du web scraping avec Goutte.

Discutons d'une autre méthode en utilisant le composant **CSS Selector** qui vient avec Goutte. Le sélecteur CSS est plus simple que l'utilisation de XPath montré dans les méthodes précédentes.

Créez un autre fichier PHP, appelons-le **goutte_css_requests.php**. Ajoutez le code suivant au fichier :

```php
<?php
# scraping books to scrape: https://books.toscrape.com/
require 'vendor/autoload.php';
$httpClient = new \Goutte\Client();
$response = $httpClient->request('GET', 'https://books.toscrape.com/');
// obtenir les prix dans un tableau
$prices = [];
$response->filter('.row li article div.product_price p.price_color')->each(function ($node) use (&$prices) {
$prices[] = $node->text();
});
// afficher les titres et les prix
$priceIndex = 0;
$response->filter('.row li article h3 a')->each(function ($node) use ($prices, &$priceIndex) {
echo $node->text() . ' @ ' . $prices[$priceIndex] .PHP_EOL;
$priceIndex++;
});
```

Comme vous pouvez le voir, l'utilisation du composant CSS Selector donne un code plus propre et plus lisible.

Vous avez peut-être remarqué que nous avons utilisé l'opérateur **`&`**. Cela garantit que nous prenons la référence de la variable dans la boucle "**each**", et pas seulement la valeur de la variable. Si **`&$prices`** est modifié dans la boucle, la valeur réelle en dehors de la boucle est également modifiée.

Vous pouvez lire plus sur [l'assignation par référence dans la documentation officielle de PHP](https://www.php.net/manual/en/language.references.whatdo.php).

Exécutez le fichier dans votre terminal en exécutant la commande :

```
php goutte_css_requests.php
```

Vous devriez voir un résultat similaire à celui des captures d'écran précédentes :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free7.png)

Notre scraper web avec PHP et Goutte se passe bien jusqu'à présent. Allons un peu plus loin et voyons si nous pouvons cliquer sur un lien et naviguer vers une page différente.

Sur notre site de démonstration, [Books to Scrape](https://books.toscrape.com/), si vous cliquez sur un titre de livre, une page se chargera montrant les détails du livre tels que :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/a-light-in-the-attic-for-scraping-tut.png)

Nous voulons voir si vous cliquez sur un lien de la liste des livres, naviguez vers la page des détails du livre et extrayez la description. Inspectez la page pour voir ce que nous allons cibler :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free9.png)

Notre flux cible sera à partir de l'élément **<div class="content">**, puis **<div id="content_inner">**, puis la balise **<article>** qui n'apparaît qu'une seule fois, et enfin la balise **<p>**.

Nous avons plusieurs balises **<p>** – la balise avec la description est la quatrième à l'intérieur de l'élément parent **<div class="content">**. Comme les tableaux commencent à 0, nous obtiendrons le nœud à l'index **3**.

Maintenant que nous savons ce que nous ciblons, écrivons le code.

Tout d'abord, ajoutez le package composer suivant pour aider à l'analyse HTML5 :

```
composer require masterminds/html5
```

Ensuite, modifiez le fichier **goutte_css_requests.php** comme suit :

```php
<?php
# scraping books to scrape: https://books.toscrape.com/
require 'vendor/autoload.php';
$httpClient = new \Goutte\Client();
$response = $httpClient->request('GET', 'https://books.toscrape.com/');
// obtenir les prix dans un tableau
$prices = [];
$response->filter('.row li article div.product_price p.price_color')
->each(function ($node) use (&$prices) {
$prices[] = $node->text();
});
// afficher le titre, le prix et la description
$priceIndex = 0;
$response->filter('.row li article h3 a')
->each(function ($node) use ($prices, &$priceIndex, $httpClient) {
$title = $node->text();
$price = $prices[$priceIndex];
// obtenir la description
$description = $httpClient->click($node->link())
->filter('.content #content_inner article p')->eq(3)->text();
// afficher le résultat
echo "{$title} @ {$price} : {$description}\n\n";
$priceIndex++;
});
```

Si vous exécutez le fichier dans votre terminal, vous devriez voir un titre, un prix et une description affichés :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free10.png)

En utilisant le composant **CSS Selector** de Goutte et l'option de cliquer sur une page, vous pouvez facilement parcourir un site web entier avec plusieurs pages et extraire autant de données que vous le souhaitez.

## Web Scraping en PHP avec Simple HTML DOM

[Simple HTML DOM](https://simplehtmldom.sourceforge.io/manual.htm#section_quickstart) est une autre bibliothèque PHP minimaliste de web scraping que vous pouvez utiliser pour parcourir un site web. Discutons de la manière dont vous pouvez utiliser cette bibliothèque pour scraper un site web. Tout comme dans les exemples précédents, nous allons scraper le site Books to Scrape.

Avant de pouvoir installer le package, modifiez votre fichier composer.json et ajoutez les lignes de code suivantes juste en dessous du bloc **`require:{}`** pour éviter d'obtenir l'erreur de versionnage :

```
"minimum-stability": "dev",
"prefer-stable": true
```

Maintenant, vous pouvez installer la bibliothèque avec la commande suivante :

```
composer require simplehtmldom/simplehtmldom
```

Une fois la bibliothèque installée, créez un nouveau fichier PHP appelé **simplehtmldom_requests.php**.

Nous avons déjà discuté de la mise en page de la page web que nous scrapons dans les sections précédentes. Nous allons donc passer directement au code. Ajoutez le code suivant au fichier **simplehtmldom_requests.php** :

```php
<?php
# scraping books to scrape: https://books.toscrape.com/
require 'vendor/autoload.php';
$httpClient = new \simplehtmldom\HtmlWeb();
$response = $httpClient->load('https://books.toscrape.com/');
// afficher le titre
echo $response->find('title', 0)->plaintext . PHP_EOL . PHP_EOL;
// obtenir les prix dans un tableau
$prices = [];
foreach ($response->find('.row li article div.product_price p.price_color') as $price) {
$prices[] = $price->plaintext;
}
// afficher les titres et les prix
foreach ($response->find('.row li article h3 a') as $key => $title) {
echo "{$title->plaintext} @ {$prices[$key]} \n";
}
```

Si vous exécutez le code dans votre terminal, il devrait afficher les résultats :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free11.png)

Vous pouvez trouver plus de méthodes pour parcourir une page web en utilisant la [bibliothèque Simple HTML DOM à partir de la documentation officielle de l'API](https://simplehtmldom.sourceforge.io/manual_api.htm).

## Web Scraping en PHP avec un navigateur headless (Symfony Panther)

Un navigateur headless est un navigateur sans interface graphique. Les navigateurs headless permettent d'utiliser le terminal pour charger une page web dans un environnement similaire à un navigateur web. Cela permet d'écrire du code pour contrôler la navigation comme nous venons de le faire dans les étapes précédentes.

Pourquoi est-ce nécessaire ?

Dans le développement web moderne, la plupart des développeurs utilisent des frameworks web JavaScript. Ces frameworks génèrent le code HTML à l'intérieur des navigateurs. Dans d'autres cas, AJAX charge dynamiquement le contenu.

Dans les exemples précédents, nous avons utilisé une page HTML statique, donc la sortie était cohérente.

Dans les cas dynamiques, où vous utilisez JavaScript et AJAX pour générer le HTML, la sortie de l'arbre DOM peut différer considérablement. Cela pourrait faire échouer nos scrapers. Les navigateurs headless entrent en jeu pour gérer ces problèmes dans les sites web modernes.

La bibliothèque PHP [Symfony Panther](https://github.com/symfony/panther) fonctionne bien avec les navigateurs headless. Vous pouvez utiliser la bibliothèque pour scraper des sites web et exécuter des tests en utilisant de vrais navigateurs.

De plus, elle fournit les mêmes méthodes que la bibliothèque Goutte, donc vous pouvez l'utiliser à la place de Goutte.

Contrairement aux bibliothèques de web scraping précédentes que nous avons discutées dans ce tutoriel, Panther peut faire ce qui suit :

* Exécuter du code JavaScript sur les pages web
* Prend en charge les tests de navigateur à distance
* Prend en charge le chargement asynchrone des éléments en attendant que d'autres éléments se chargent avant d'exécuter une ligne de code
* Prend en charge toutes les implémentations de Chrome et Firefox
* Peut prendre des captures d'écran
* Permet d'exécuter votre code JS personnalisé ou des requêtes XPath dans le contexte de la page chargée.

Nous avons déjà fait beaucoup de scraping, alors essayons quelque chose de différent. Nous allons charger une page HTML et prendre une capture d'écran de la page.

Installez [Symfony Panther](https://github.com/symfony/panther) avec la commande suivante :

```
composer require symfony/panther
```

Créez un nouveau fichier php, appelons-le **panther_requests.php**. Ajoutez le code suivant au fichier :

```php
<?php
# scraping books to scrape: https://books.toscrape.com/
require 'vendor/autoload.php';
$httpClient = \Symfony\Component\Panther\Client::createChromeClient();
// pour un client Firefox, utilisez la ligne ci-dessous à la place
//$httpClient = \Symfony\Component\Panther\Client::createFirefoxClient();
// obtenir la réponse
$response = $httpClient->get('https://books.toscrape.com/');
// prendre une capture d'écran et la stocker dans le répertoire courant
$response->takeScreenshot($saveAs = 'books_scrape_homepage.jpg');
// affichons quelques titres de livres
$response->getCrawler()->filter('.row li article h3 a')
->each(function ($node) {
echo $node->text() . PHP_EOL;
});
```

Pour que ce code s'exécute sur votre système, vous devez installer les pilotes pour Chrome ou Firefox, selon le client que vous avez utilisé dans votre code.

Heureusement, Composer peut le faire automatiquement pour vous. Exécutez la commande suivante dans votre terminal pour installer et détecter les pilotes :

```
composer require --dev dbrekelmans/bdi && vendor/bin/bdi detect drivers
```

Maintenant, vous pouvez exécuter le fichier PHP dans votre terminal et il prendra une capture d'écran de la page web et la stockera dans le répertoire courant. Il affichera ensuite une liste de titres du site web.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/free12.png)

## Conclusion

Dans ce tutoriel, nous avons discuté des différentes bibliothèques PHP open source que vous pouvez utiliser pour scraper un site web.

Si vous avez suivi le tutoriel, vous auriez dû être capable de créer un scraper basique pour parcourir une ou deux pages.

Bien que ce soit un article introductif, nous avons couvert la plupart des méthodes que vous pouvez utiliser avec les bibliothèques. Vous pouvez choisir de construire sur cette connaissance et créer des scrapers web complexes capables de parcourir des milliers de pages. Le code de ce tutoriel est disponible dans ce [dépôt GitHub](https://github.com/jaymoh/php_web_scraper).

N'hésitez pas à nous contacter si vous avez des questions.

Vous pouvez consulter d'autres articles sur le [web scraping avec Nodejs](https://www.scrapingdog.com/blog/web-scraping-101-with-nodejs) et le [web scraping avec Python](https://www.scrapingdog.com/blog/best-python-web-scraping-libraries/) si vous êtes intéressé.
---
title: Requête POST cURL API REST via l'outil Construct 3 GameDev & le module AJAX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-23T02:25:54.000Z'
originalURL: https://freecodecamp.org/news/rest-api-curl-post-request-via-construct-3-gamedev-tool-ajax-module
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/c3-woo-wp-banner.jpg
tags:
- name: construct 3
  slug: construct-3
- name: Ajax
  slug: ajax
- name: curl
  slug: curl
- name: json
  slug: json
- name: REST API
  slug: rest-api
- name: woocommerce
  slug: woocommerce
- name: WordPress
  slug: wordpress
seo_title: Requête POST cURL API REST via l'outil Construct 3 GameDev & le module
  AJAX
seo_desc: 'By Andreas Lopez

  Hello FreeCodeCamp Reader Community! This Tutorial is made as a little thought experiment
  but might have some merit for the one or other person.


  Please keep in mind that this plugin is making an example by adding a product via
  Const...'
---

Par Andreas Lopez

Bonjour à la communauté des lecteurs de FreeCodeCamp ! Ce tutoriel est réalisé comme une petite expérience de pensée mais pourrait avoir un certain mérite pour une personne ou une autre.

> Veuillez garder à l'esprit que ce plugin fait un exemple en ajoutant un produit via les formulaires Construct 3 + la requête cURL de l'API REST à une installation WordPress + WooCommerce existante.

Les principes restent valables pour d'autres fins que vous pourriez avoir avec l'API REST, et j'ai inclus le .c3p en bas de ce tutoriel. Il existe des moyens plus élégants pour alimenter les tableaux d'informations de l'application, mais ceci est une démonstration rapide comme preuve de concept que j'ai assemblée en 2 heures et que j'ai eu envie de partager en raison du manque d'informations sur l'API et AJAX pour Construct 3.

**Voici l'ensemble du code en une seule capture d'écran :**

![Image](https://www.freecodecamp.org/news/content/images/2019/06/c3-api-example.jpg)
_Capture d'écran du code source Construct 3_

# Le code décomposé une fois que nous cliquons sur le bouton 'Create Product'

* productjson est un champ de texte obligatoire en dehors de la zone visible sur la mise en page.
* productjson contient toutes nos données de charge utile préformatées en json pour permettre à l'API REST de fonctionner correctement.
* La charge utile contient du contenu créé dynamiquement qui sont les formulaires dans la mise en page tels que le nom du produit, le sku, le prix, etc.
* Le module AJAX que j'ai renommé AJAX_Data définira l'en-tête de la requête sur "Content-Type" avec la valeur "application/json", car l'API REST via la requête cURL utilisera JSON.
* La prochaine AJAX_Data avec la requête 'Post to URL' sera notre requête API réelle.
* Le Tag est simplement un nom qui peut être utilisé par exemple pour retourner les valeurs de la requête, dans l'exemple de mon projet - comme information de débogage.
* L'URL commencera par votre domaine, par exemple 'https://www.example.com'. La partie suivante de l'URL est la requête API que vous souhaitez effectuer, dans notre exemple selon la documentation de WooCommerce pour ajouter un produit, nous avons besoin de '/wp-json/wc/v3/products?'
* Enfin, pour l'URL, nous avons besoin de la clé et du secret du consommateur de cette manière : 'consumer_key=<consumer_key>&consumer_secret=<consumer_secret>'
* L'URL complète ressemble à ceci : "https://www.example.com/wp-json/wc/v3/products?consumer_key=<consumer_key>&consumer_secret=<consumer_secret>"
* Ensuite, nous avons les données. C'est simple puisque nous avons déjà créé une zone de texte à cet effet. Référez-vous simplement ici, dans mon exemple, les données seront 'productjson.Text'.
* Et enfin, le type de requête. Puisque nous créons un produit, nous aurons besoin de 'POST', si nous devions récupérer un produit, nous voudrions une requête 'GET', voir la documentation respective de l'API que vous utilisez.

### Téléchargement du fichier .c3p :

[https://drive.google.com/open?id=16DKq5RJD5tCw57oZPruGk_mtTIAe-Um9](https://drive.google.com/open?id=16DKq5RJD5tCw57oZPruGk_mtTIAe-Um9)

# Conditions requises pour mon exemple .c3p

* Installation de WordPress avec WooCommerce installé
* API REST activée et émission d'un secret et d'une clé de consommateur
* Remplacer mon exemple de secret et de clé API dans le code
* Télécharger une image dans la galerie multimédia de WordPress
* Créer une catégorie de produit dans WordPress/WooCommerce

Si vous avez besoin d'un environnement WordPress gratuit pour jouer, j'ai utilisé [https://pantheon.io](https://pantheon.io), sous le plan gratuit vous pouvez obtenir 2 sites de bac à sable. Assurez-vous simplement d'installer d'abord le plugin WP-CORS et de définir les sites autorisés sur '*' comme vu dans leur documentation ici :
[https://pantheon.io/docs/platform-considerations/#cors](https://pantheon.io/docs/platform-considerations/#cors)

[https://wordpress.org/plugins/wp-cors/](https://wordpress.org/plugins/wp-cors/)

### Informations sur la source de l'API & Documentation C3 pertinente :

[Documentation de l'API REST WooCommerce](https://woocommerce.github.io/woocommerce-rest-api-docs)
[Documentation AJAX de Construct 3](https://www.construct.net/en/make-games/manuals/construct-3/plugin-reference/ajax)
[Outil de validation JSON pour vérifier si votre JSON est correctement formaté.](https://jsonlint.com/)
[Tutoriel original que j'ai écrit sur Construct.net](https://www.construct.net/en/tutorials/rest-api-curl-post-request-2245)
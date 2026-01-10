---
title: Comment rendre Wordpress plus excitant avec l'API Wordpress, ACF et Express.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T00:33:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-wordpress-more-exciting-with-the-wordpress-api-acf-express-js-9dc33b8fb133
coverImage: https://cdn-media-1.freecodecamp.org/images/0*my2zRNkADPpQFRfo
tags:
- name: distributed systems
  slug: distributed-systems
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: Comment rendre Wordpress plus excitant avec l'API Wordpress, ACF et Express.js
seo_desc: 'By Tyler Jackson

  I’ve been working with Wordpress since it’s proliferation as a content management
  system. I hardly get excited when clients or co-workers mention it anymore. I’ve
  “found the light” in more robust frameworks and learned much more abou...'
---

Par Tyler Jackson

Je travaille avec Wordpress depuis sa prolifération en tant que système de gestion de contenu. Je m'enthousiasme rarement lorsque des clients ou des collègues en parlent. J'ai "trouvé la lumière" dans des frameworks plus robustes et j'ai appris beaucoup plus sur les différentes parties des applications web personnalisées.

Ainsi, dans un effort pour ravivé ma passion pour Wordpress, j'ai commencé à explorer différentes façons d'implémenter ce framework. L'une de ces méthodes consiste à séparer le front-end du back-end et à éviter certains des points douloureux liés à l'utilisation des balises de modèle Wordpress et du système de thématiques. Examinons cela.

### Applications Monolithiques vs. Distribuées

Wordpress est un framework monolithique, ce qui signifie que les différentes parties du framework (base de données, stockage de fichiers, structure de présentation et fichiers d'actifs, fichiers de logique métier) sont toutes regroupées. C'est en grande partie pourquoi Wordpress est si facile à installer et à exécuter. Installez MAMP, copiez les derniers fichiers Wordpress, créez une base de données et modifiez le fichier `wp-config.php`. Prêt à l'emploi.

Nous allons aller à l'encontre de la convention monolithique et diviser ce site Wordpress en deux parties distinctes : front-end et back-end, présentation et administration.

Nous allons utiliser Wordpress pour l'administration des données de notre application et exploiter un plugin pour aider à la création et à la gestion des attributs (champs) pour notre type de publication personnalisé. Pour la partie présentation, nous allons abandonner complètement un thème et consommer des points de terminaison API à partir d'une application Express.js.

### Exemple

Dans cet exemple, nous allons créer une simple liste de produits. L'idée est que vous avez déjà un site web alimenté par Wordpress et que vous souhaitez gérer une liste de produits à vendre via la même interface. Mais vous voulez créer un site web complètement différent pour le magasin.

### API Wordpress

Depuis la version 4.7, Wordpress expose automatiquement vos publications publiées (et autres données) via son [API REST](https://developer.wordpress.org/rest-api/), présentée dans un format JSON. Si vous avez développé un site web utilisant Wordpress 4.7+, ajoutez simplement `/wp-json` à l'URL racine et admirez le mur de texte qui est retourné.

Avec cette API automatiquement intégrée à l'installation de Wordpress, une grande partie du travail d'une application distribuée est déjà faite pour nous. La création d'une API peut être un obstacle lorsque l'on commence à penser différemment aux applications. Wordpress a créé une API fantastique et basique pour consommer nos données de la manière que nous préférons.

À ce stade, je ne ferais qu'encombrer l'internet en écrivant un tutoriel sur la façon d'installer Wordpress localement. Au lieu de cela, je vais [vous diriger vers une source fiable sur le sujet](https://codex.wordpress.org/Installing_WordPress_Locally_on_Your_Mac_With_MAMP).

Peu importe la méthode que vous utilisez pour obtenir une instance Wordpress opérationnelle, vous devriez pouvoir y accéder via `http://localhost` ou une autre URL. Une fois que nous avons une URL, faisons un test rapide pour nous assurer que nous recevons des données. Je préfère un outil comme Postman, mais nous allons garder cela simple et visiter l'URL suivante dans notre navigateur (en changeant l'URL en conséquence, bien sûr).

`http://localhost/mysite/wp-json`

Cela devrait retourner une liste de tous les points de terminaison disponibles pour l'API REST de votre installation Wordpress.

Mais sérieusement, Postman...

[**Postman**](https://www.getpostman.com/)
[_Postman est le seul environnement de développement d'API complet, pour les développeurs d'API, utilisé par plus de 5 millions de développeurs...www.getpostman.com_](https://www.getpostman.com/)

### Types de Publications Personnalisés

Puisque Wordpress nous limite à deux types de données (Publications et Pages), nous allons devoir créer un type de publication personnalisé pour nos Produits. Cela créera une séparation claire entre les publications de Produits et toute autre publication que nous avons.

Il existe plusieurs façons différentes de créer des types de publications personnalisés. Ici, nous allons créer un plugin Wordpress à fichier unique pour enregistrer le type de publication Produits.

```
<?php/*Plugin Name: Product Custom Post Type*/
```

```
function create_product_cpt() {  $labels = array(   'name' => __( 'Products', 'Post Type General Name', 'products' ),   'singular_name' => __( 'Product', 'Post Type Singular Name', 'products' ),   'menu_name' => __( 'Products', 'products' ),   'name_admin_bar' => __( 'Product', 'products' ),   'archives' => __( 'Product Archives', 'products' ),   'attributes' => __( 'Product Attributes', 'products' ),   'parent_item_colon' => __( 'Parent Product:', 'products' ),   'all_items' => __( 'All Products', 'products' ),   'add_new_item' => __( 'Add New Product', 'products' ),   'add_new' => __( 'Add New', 'products' ),   'new_item' => __( 'New Product', 'products' ),   'edit_item' => __( 'Edit Product', 'products' ),   'update_item' => __( 'Update Product', 'products' ),   'view_item' => __( 'View Product', 'products' ),   'view_items' => __( 'View Products', 'products' ),   'search_items' => __( 'Search Product', 'products' ),   'not_found' => __( 'Not found', 'products' ),   'not_found_in_trash' => __( 'Not found in Trash', 'products' ),   'featured_image' => __( 'Featured Image', 'products' ),   'set_featured_image' => __( 'Set featured image', 'products' ),   'remove_featured_image' => __( 'Remove featured image', 'products' ),   'use_featured_image' => __( 'Use as featured image', 'products' ),   'insert_into_item' => __( 'Insert into Product', 'products' ),   'uploaded_to_this_item' => __( 'Uploaded to this Product', 'products' ),   'items_list' => __( 'Products list', 'products' ),   'items_list_navigation' => __( 'Products list navigation', 'products' ),   'filter_items_list' => __( 'Filter Products list', 'products' ),  );
```

```
  $args = array(   'label' => __( 'Product', 'products' ),   'description' => __( '', 'products' ),   'labels' => $labels,   'menu_icon' => 'dashicons-products',   'supports' => array('title', 'editor', 'excerpt', 'thumbnail'),   'taxonomies' => array('products'),   'public' => true,   'show_ui' => true,   'show_in_menu' => true,   'menu_position' => 5,   'show_in_admin_bar' => true,   'show_in_nav_menus' => true,   'can_export' => true,   'has_archive' => true,   'hierarchical' => false,   'exclude_from_search' => false,   'show_in_rest' => true,   'rest_base' => 'products',   'publicly_queryable' => true,   'capability_type' => 'post',  );
```

```
  register_post_type( "product", $args );}%>
```

Bien que long, ce code est assez standard pour créer un type de publication personnalisé dans Wordpress. Deux choses à noter dans notre tableau `$args`:

* `'show_in_rest' => true` rend le type de publication personnalisé accessible via l'API REST
* `'rest_base' => 'products'` définit le nom que nous utilisons pour accéder aux Produits via les points de terminaison de l'API REST

Une fois que vous avez votre type de publication personnalisé affiché dans l'administration Wordpress, assurons-nous que nous pouvons obtenir une réponse via l'API (vous devrez créer un produit pour qu'il ne retourne pas vide).

`http://localhost/mysite/wp-json/wp/v2/products`

Et voici ce que nous obtenons...

![Image](https://cdn-media-1.freecodecamp.org/images/yMtobvc5rkQ1BwXsx8o6Eo8ECauKlEwcpxSq)

Super !

### Advanced Custom Fields

J'essaie de limiter mon utilisation de plugins autant que possible, mais je ferai une exception pour Advanced Custom Fields (ACF). ACF simplifie tout le travail de création et de gestion de champs personnalisés pour les types de publications. Allez dans votre page Plugins, recherchez Advanced Custom Fields puis cliquez sur "Installer" et "Activer". C'est tout.

Il serait également redondant de ma part de vous guider à travers la création d'un Groupe de Champs en utilisant Advanced Custom Fields, donc [je vais laisser leur documentation vous guider](https://www.advancedcustomfields.com/resources/creating-a-field-group/) si vous ne savez pas comment faire.

Créons un Groupe de Champs appelé "Product Meta" et ajoutons des champs pour "Normal Price", "Discount Price" et "Inventory Quantity" et positionnons-les dans la zone de la barre latérale.

![Image](https://cdn-media-1.freecodecamp.org/images/201h-1ofbdcglb1xjBIntiMYYDK50fyzGnCr)

Bien.

Maintenant vient la partie délicate. Les champs que nous venons de créer via ACF ne sont pas exposés via l'API REST par défaut. Nous devrons utiliser `add_filter` et `rest_prepare_{$post_type}` pour ajouter les valeurs des champs personnalisés à la réponse JSON. Ici, j'ai simplement ajouté ce bout de code au bas de notre fichier de plugin de type de publication personnalisé pour des raisons de brièveté.

```
function my_rest_prepare_post($data, $post, $request) {  $_data = $data->data;    $fields = get_fields($post->ID);
```

```
  foreach ($fields as $key => $value){    $_data[$key] = get_field($key, $post->ID);  }
```

```
  $data->data = $_data;    return $data;}
```

```
add_filter("rest_prepare_product", 'my_rest_prepare_post', 10, 3);
```

_Merci à [Cody Sand](https://www.codysand.com/adding-advanced-custom-fields-to-wordpress-rest-api-response/) pour l'astuce ci-dessus._

### Express.js

Notre application Express.js nous fournira un framework pour consommer l'API Wordpress et présenter les produits dans notre site web de magasin. Puisque nous consommons simplement une API, nous pourrions utiliser n'importe quel framework de notre choix. Vue.js. Angular. Backbone. React. Rails. Django. Middleman. Jekyll. Le monde du front-end est votre huître.

Je vais supposer que vous avez déjà Node.js installé. Si ce n'est pas le cas, [c'est très simple](https://nodejs.org/en/download/). Commençons une nouvelle application Express.js.

```
npm install -g express-generator nodemonexpress --css=sass --view=jade --git mystorecd mystorenpm install --save request request-promise && npm install
```

Ici, nous utilisons le package Express Generator pour générer un squelette pour notre application Express. Nous utiliserons également SASS pour les feuilles de style et le moteur de template Jade. Choisissez ce avec quoi vous êtes à l'aise. Nodemon redémarrera notre application automatiquement pour nous lorsque un fichier change, et la bibliothèque Request nous aidera à faire des requêtes HTTP à l'API Wordpress. Servons notre application Express :

`nodemon`

Maintenant, lorsque nous ouvrons `http://localhost:3000`, nous devrions voir notre application Express en cours d'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/A-sad4nUl9l7jldtfT6MjpyKsmbwN-L8232a)

D'accord, maintenant, récupérons nos produits.

```
var express = require('express');var router = express.Router();const rp = require('request-promise');
```

```
/* GET index page. */router.get('/', function(req, res, next) {  rp({uri: 'http://127.0.0.1:8888/test/wp-json/wp/v2/products', json: true})  .then((response) => {    console.log(response);    res.render('index', {products: response});  })  .catch((err) => {    console.log(err);  });});
```

```
module.exports = router;
```

Dans notre fichier de route `index.js`, incluons la bibliothèque Request-Promise puis faisons un appel au point de terminaison `products` dans notre route racine (`/`).

Si la requête est réussie, nous rendons notre vue `index`. Si une erreur survient avec la requête, nous la journalisons simplement. Maintenant, la vue...

```
extends layout
```

```
block content h1 MyStore ul  each product in products   li    product.title.rendered    product.price
```

En utilisant Jade, nous allons simplement lister les produits. D'accord, vérifions notre site de magasin.

![Image](https://cdn-media-1.freecodecamp.org/images/JJJqnOrnpeXTXEAEpDTbuh7nJ7wTcEAHRUjx)

? Voici votre récompense. Je vous laisse continuer sur la route Express et découvrir comment faire fonctionner les pages de liste et d'index des produits.

### Au-delà

Ceci est un exemple assez simple de la façon dont les applications distribuées fonctionnent avec Wordpress. Nous aurions pu continuer à séparer l'application en encore plus de parties en intégrant un CDN pour le stockage des médias ou en déplaçant la base de données vers un serveur séparé. Nous n'avons pas non plus couvert l'authentification pour l'API Wordpress, ce qui est quelque chose dont vous auriez absolument besoin en production.

À partir de là, vous pourriez implémenter Stripe ou un autre processeur de paiement et avoir un site de magasin entièrement fonctionnel. J'espère que cela a inspiré certains d'entre vous à exploiter Wordpress de différentes manières et à continuer à utiliser l'une des solutions CMS les plus omniprésentes. Bon codage !
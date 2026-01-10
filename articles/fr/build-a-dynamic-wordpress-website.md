---
title: Comment créer un site WordPress dynamique avec Advanced Custom Fields et Custom
  Post Types
subtitle: ''
author: Jim Campbell
co_authors: []
series: null
date: '2023-08-03T20:36:38.000Z'
originalURL: https://freecodecamp.org/news/build-a-dynamic-wordpress-website
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-03-at-3.50.46-AM.png
tags:
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: Comment créer un site WordPress dynamique avec Advanced Custom Fields et
  Custom Post Types
seo_desc: "Hello, fellow WordPress enthusiasts! Today, I want to share with you an\
  \ exciting journey I took while building Honeymoons.com. It's a dynamic website\
  \ that uses Advanced Custom Fields (ACF) and Custom Post Types. \nAs a travel company\
  \ specializing in d..."
---

Bonjour, chers passionnés de WordPress ! Aujourd'hui, je souhaite partager avec vous un voyage passionnant que j'ai entrepris lors de la création de [Honeymoons.com](https://honeymoons.com). Il s'agit d'un site web dynamique qui utilise [Advanced Custom Fields (ACF)](https://www.advancedcustomfields.com/) et [Custom Post Types](https://developer.wordpress.org/plugins/post-types/registering-custom-post-types/). 

En tant qu'entreprise de voyage spécialisée dans les destinations de lune de miel de rêve, il était crucial pour nous de présenter nos hôtels et destinations de manière conviviale et visuellement attrayante. 

ACF et les CPT se sont avérés être la solution parfaite pour atteindre notre objectif de fournir une expérience immersive et personnalisée à nos utilisateurs. 

La création d'un type de publication personnalisé pour les destinations et les hôtels nous a permis de catégoriser facilement ces types spécifiques de contenu. Advanced Custom Fields nous a permis d'enrichir les Custom Post Types avec des métadonnées spécifiques qui peuvent être affichées dynamiquement sur l'ensemble du site web.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-12.png)
_Exemple de [Honeymoons.com](https://honeymoons.com) utilisant un Custom Post Type, un modèle personnalisé et ACF pour afficher les informations sur les hôtels._

## Qu'est-ce que les Custom Post Types ?

Les [Custom Post Types](https://developer.wordpress.org/plugins/post-types/registering-custom-post-types/) de WordPress sont une fonctionnalité puissante qui permet d'étendre la fonctionnalité par défaut de WordPress au-delà des articles et pages standard. Ils permettent de créer et de gérer différents types de contenu, chacun avec son propre ensemble d'attributs et de fonctionnalités. 

Les Custom Post Types sont essentiels pour organiser et présenter des types de contenu spécifiques, tels que des produits, des éléments de portfolio, des témoignages, des événements, des recettes, et plus encore, de manière structurée et efficace.

Par défaut, WordPress propose deux types de publications principaux :

### Articles

Ce sont des articles de blog standard qui sont généralement affichés dans l'ordre chronologique inverse sur la page du blog.

### Pages

Ce sont des pages statiques qui sont généralement utilisées pour du contenu statique comme À propos, Contactez-nous ou une page de politique de confidentialité.

Cependant, lorsque vous devez créer du contenu qui ne s'intègre pas dans la structure par défaut des articles ou des pages, les Custom Post Types entrent en jeu.

Vous pouvez enregistrer vos types de publications personnalisés avec leur propre ensemble d'attributs, de taxonomies et de fichiers de modèle. Cela permet de gérer et de présenter du contenu diversifié de manière plus organisée et conviviale.

Par exemple, sur [honeymoons.com](https://honeymoons.com), nous avons créé un Custom Post Type appelé "Destinations" pour présenter les destinations de lune de miel. 

Pour créer des Custom Post Types, vous pouvez soit écrire du code personnalisé en utilisant la fonction `register_post_type()`, soit utiliser des plugins qui rendent le processus plus convivial, comme "[Custom Post Type UI](https://wordpress.org/plugins/custom-post-type-ui/)" ou "[Toolset Types](https://toolset.com/home/types-manage-post-types-taxonomy-and-custom-fields/)." 

WordPress propose une fonctionnalité pour configurer facilement les types de publications selon vos besoins spécifiques en mettant à jour le fichier functions.php dans votre thème.

Le code spécifique que nous avons utilisé pour créer le type de publication Destinations est le suivant :

	//Destinations
    register_post_type('destination', // Register Custom Post Type
        array(
        'labels' => array(
            'name' => __('Destinations', 'destination'), // Rename these to suit
            'singular_name' => __('Destination', 'html5blank'),
        ),
        'public' => true,
        'hierarchical' => true, // Allows your posts to behave like Hierarchy Pages
        'has_archive' => false,
		'menu_icon' => 'dashicons-palmtree',
		'show_in_nav_menus'   => true,
        'supports' => array(
            'title',
            'editor',
            'excerpt',
			'revisions',
			'page-attributes',
            'thumbnail'
        ), // Go to Dashboard Custom HTML5 Blank post for supports
		'rewrite' => array (
			'slug' => '/destinations',
			'with_front' => false,
			'hierarchical' => true
		),
        'can_export' => true, // Allows export in Tools > Export
        'taxonomies' => array(
			'experiences',
			'regions'
        ) // Add Category and Post Tags support */
    ));

Ces Custom Post Types apparaîtront dans la barre latérale de wp-admin avec vos articles et pages :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-11.png)

Les Custom Post Types sont devenus un outil essentiel pour les développeurs et les créateurs de contenu, car ils offrent la flexibilité nécessaire pour adapter les sites WordPress à des besoins spécifiques, ce qui en fait un système de gestion de contenu polyvalent et robuste.

## Qu'est-ce que Advanced Custom Fields pour WordPress ?

[Advanced Custom Fields (ACF)](https://www.advancedcustomfields.com/) est un plugin WordPress populaire qui améliore l'expérience de création et de gestion de contenu en fournissant une interface conviviale pour ajouter des champs personnalisés aux articles, pages et types de publications personnalisés. Il permet aux développeurs de sites web et aux créateurs de contenu d'étendre facilement l'éditeur de publications WordPress par défaut avec des champs de saisie supplémentaires, permettant la création de contenu plus structuré et dynamique.

Avec ACF, vous pouvez définir divers types de champs personnalisés, tels que des champs de texte, des champs de téléchargement d'images, des listes déroulantes de sélection, des sélecteurs de date, des champs répétables, et plus encore. Ces champs personnalisés peuvent être utilisés pour ajouter des informations supplémentaires à votre contenu, le rendant plus polyvalent et adapté à des exigences spécifiques.

Les principales fonctionnalités et avantages d'Advanced Custom Fields (ACF) incluent :

1. **Création de champs personnalisés** : ACF permet de créer des champs personnalisés via une interface graphique intuitive dans l'espace d'administration de WordPress. Vous pouvez choisir parmi divers types de champs et configurer leurs paramètres pour répondre à vos besoins.
2. **Groupes de champs** : Vous pouvez regrouper des champs liés ensemble en ensembles appelés "Groupes de champs". Ces groupes peuvent ensuite être assignés à des types de publications ou pages spécifiques, offrant une approche modulaire et organisée de la gestion de contenu.
3. **Conditionnels et logique** : Une fonctionnalité puissante d'ACF est la possibilité de définir une logique conditionnelle pour les champs. Vous pouvez afficher ou masquer des champs spécifiques en fonction des valeurs d'autres champs, rendant la création de contenu plus efficace et conviviale.
4. **Champs répétables** : Le champ répétable d'ACF permet de créer des ensembles de sous-champs qui peuvent être répétés selon les besoins. Cela est particulièrement utile pour gérer du contenu dynamique comme des listes, des galeries et des sections de contenu flexibles.
5. **Intégration frontend** : ACF facilite l'affichage des données de champs personnalisés sur le frontend de votre site web. Vous pouvez utiliser des balises de modèle simples ou des fonctions ACF pour récupérer et afficher les valeurs des champs personnalisés dans vos fichiers de thème.
6. **Extensibilité** : ACF peut être étendu via des modules complémentaires tiers et du code personnalisé, permettant aux développeurs de créer des champs et fonctionnalités personnalisés encore plus avancés et spécialisés.
7. **Expérience conviviale** : ACF simplifie le processus de création de contenu pour les utilisateurs non techniques. Il réduit le besoin de codage personnalisé et facilite l'ajout et la gestion de contenu avec des champs structurés pour les éditeurs de contenu.

ACF a gagné en popularité parmi les développeurs et designers WordPress pour sa flexibilité et sa facilité d'utilisation. Il permet la création de sites web dynamiques et personnalisés sans avoir besoin de développement personnalisé complexe, ce qui en fait un outil précieux pour les sites web à petite échelle ainsi que pour les grands projets complexes.

## Comment créer des modèles personnalisés pour afficher le contenu ACF

Pour afficher dynamiquement des données en utilisant Advanced Custom Fields (ACF) et des modèles personnalisés dans WordPress, nous allons passer en revue les étapes avec un exemple de Honeymoons.com utilisant un Custom Post Type d'Hôtels. 

Nous allons créer des champs personnalisés pour les métadonnées telles que le nombre de chambres, le prix moyen et l'URL de l'hôtel, puis afficher ces données dynamiquement sur le frontend en utilisant un modèle personnalisé.

### Étape 1 : Installer et activer le plugin Advanced Custom Fields.

Tout d'abord, assurez-vous que le plugin Advanced Custom Fields est installé et activé sur votre site WordPress. Vous pouvez trouver le plugin dans le dépôt de plugins WordPress et l'installer depuis le tableau de bord d'administration.

### Étape 2 : Créer des champs personnalisés pour le type de publication Hôtel. 

Ensuite, nous allons créer des champs personnalisés pour le type de publication Hôtel en utilisant ACF.

1. Allez dans "Champs personnalisés" dans la barre latérale d'administration de WordPress et cliquez sur "Ajouter nouveau".

2. Créez un nouveau groupe de champs pour les Hôtels et ajoutez les champs personnalisés suivants :

* Image héro (Image)
* Lien TripAdvisor.com (URL)
* Nombre de chambres (Nombre)
* Nombre de chambres (Nombre)
* Prix - Bas (Nombre)
* Prix - Haut (Nombre)
* Prix - Moyen (Nombre)
* Évaluation des clients (Nombre avec une valeur maximale de 10)
* Évaluation par étoiles
* Site web (URL)
* URL d'affichage (Texte)

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-9.png)

3. Assigner le groupe de champs au type de publication Hôtel 

Après avoir créé les champs personnalisés, nous devons assigner le groupe de champs au type de publication Hôtel.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-10.png)

### Étape 3 : Afficher les champs personnalisés dans le modèle personnalisé 

Maintenant, nous allons créer un modèle personnalisé pour le type de publication Hôtel, où nous pouvons récupérer et afficher dynamiquement les métadonnées.

Créez un nouveau fichier PHP dans votre dossier de thème et nommez-le "single-hotel.php" (en supposant que vous avez une hiérarchie de modèles de type de publication personnalisée dans votre thème). Remplacez "hotel" par le nom de votre type de publication personnalisé. 

Dans "single-hotel.php", commencez avec le code de modèle régulier pour l'en-tête, le pied de page et la boucle de publication. Vous pouvez commencer avec une copie de single.php.

Utilisez les fonctions ACF pour récupérer les valeurs des champs personnalisés et les afficher dans le modèle. Utilisez PHP, HTML et CSS pour afficher le contenu.

Vous pouvez récupérer les Advanced Custom Fields comme ceci :

$number_of_rooms = get_field('number_of_rooms');
$average_price = get_field('average_price');
$hotel_url = get_field('hotel_url');

Et afficher le contenu comme ceci :

echo '<p>Nombre de chambres : ' . $number_of_rooms . '</p>';
echo '<p>Prix moyen : $' . $average_price . '</p>';
echo '<p><a href="' . $hotel_url . '">Site web de l'hôtel</a></p>';

En capturant les métadonnées avec Advanced Custom Fields et en affichant ce contenu avec des modèles personnalisés et des types de publications personnalisés, vous pouvez organiser et afficher les données sur votre site WordPress de manière beaucoup plus dynamique et conviviale.

Votre site WordPress ne ressemblera pas à un site "sorti de la boîte" et fournira des informations beaucoup plus utiles et organisées à l'utilisateur.

## Conclusion

Grâce à ACF et aux Custom Post Types, Honeymoons.com dispose désormais d'un site web dynamique qui offre des expériences personnalisées à nos utilisateurs. 

Notre collaboration avec ACF et les CPT nous a permis de créer des pages d'hôtels et de destinations magnifiques qui captivent les visiteurs et les aident à planifier leur lune de miel de rêve sans effort. 

J'espère que notre étude de cas vous a inspiré pour explorer le vaste potentiel d'ACF et des CPT pour la création de sites WordPress dynamiques adaptés à vos besoins spécifiques. Bon codage !
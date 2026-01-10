---
title: Le monde complexe des données personnalisées dans WordPress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-02T01:07:07.000Z'
originalURL: https://freecodecamp.org/news/the-tangled-world-of-custom-data-in-wordpress-2ee8b57d49c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZdgftYvXborZxb4LL_WW8g.jpeg
tags:
- name: PHP
  slug: php
- name: Quality Software
  slug: quality-software
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: Le monde complexe des données personnalisées dans WordPress
seo_desc: 'By Kamil Grzegorczyk

  Reducing Risk and Managing Your Custom Fields


  source https://pixabay.com

  Have you ever wondered how to properly name keys of WordPress custom fields? Does
  it make any difference? Should you care? What are the potential risks?

  Re...'
---

Par Kamil Grzegorczyk

#### Réduire les risques et gérer vos champs personnalisés

![Image](https://cdn-media-1.freecodecamp.org/images/T7IWEtq6emQ8ewTaeh51rey6BLxOwcWWD9E8)
_source https://pixabay.com_

Vous êtes-vous déjà demandé comment nommer correctement les clés des champs personnalisés de [WordPress](https://wordpress.org) ? Est-ce que cela fait une différence ? Devriez-vous vous en soucier ? Quels sont les risques potentiels ?

Récemment, j'ai écrit un tutoriel sur le filtrage des vues d'administration de WordPress. Dans le code, j'ai nommé les clés des champs personnalisés comme `kg_order_items`. Vous pourriez demander pourquoi ? Pourquoi ne pas les nommer simplement `items` ? Eh bien… lisez la suite !

Si vous essayez de chercher sur Google comment nommer les champs personnalisés, vous ne trouverez pas beaucoup d'informations à ce sujet. Même l'entrée du [Codex](https://codex.wordpress.org/Custom_Fields) ne dit rien sur la manière de nommer correctement les clés des champs. J'ai trouvé seulement [une ressource sur les forums ACF](https://support.advancedcustomfields.com/forums/topic/best-practice-for-name-the-fields/) qui contient des informations pertinentes.

S'il n'y a pas de problème, pourquoi tant de bruit ? Vous pourriez demander.

![Image](https://cdn-media-1.freecodecamp.org/images/FPg2xCt4KCRLjf4JzMlakYO1-fuN8qhrY63B)
_Trouvé sur [http://dilbert.com](http://dilbert.com" rel="noopener" target="_blank" title=")_

Les jours où WordPress était un simple CMS supportant de petits sites de blogs avec seulement des articles et des pages sont révolus. Aujourd'hui, même le plus petit site utilise une pléthore de plugins et de thèmes complexes. Et tous apportent de nouveaux champs personnalisés dans le jeu.

La situation devient encore pire si vous utilisez l'un de ces thèmes "premium" fantaisistes. Malheureusement, beaucoup d'entre eux ne sont pas bien écrits et combinent 1001 fonctions en une seule. Résultat final ? Un site lent, peu performant et enchevêtré qui ne semble bien que sur du contenu de démonstration et des images d'archives. Et ils **ajoutent beaucoup** de champs personnalisés aussi.

### Danger !

![Image](https://cdn-media-1.freecodecamp.org/images/m8se5ytEdXwvEddSjmVS3dVkmvy4XZ2x0TCr)
_Source inconnue_

La table `wp_postmeta` de WordPress est très simple. C'est une paire clé-valeur attachée à un post_id particulier. Cela signifie que toutes les **clés des champs personnalisés partagent un espace de noms commun**. Cela est particulièrement vrai pour l'ID particulier du post.

**Premier exemple**  
a) Imaginez que votre post a un lien "en savoir plus". Après avoir cliqué sur le lien, il vous redirige vers une URL particulière. L'adresse est fournie dans un champ personnalisé. Nommons la clé du champ `redirect_to`.

b) Imaginez maintenant que vous installez un plugin appelé par exemple "Redirect me, Honey". Le plugin est très, très simple. Lorsque l'utilisateur entre sur la page, il redirige immédiatement l'utilisateur en fonction du paramètre du champ personnalisé attaché à un post. Oh… et sa clé de champ est également nommée `redirect_to`.

Résultat ? Après avoir activé le plugin, tous vos posts avec le bouton "en savoir plus" redirigent les utilisateurs hors de votre site. Et la raison n'est pas évidente au premier abord. Cela peut même passer inaperçu pendant un certain temps.

Ce scénario est, bien sûr, inventé, mais les dangers sont réels. Avec des milliers de plugins et des milliers de thèmes disponibles, ce n'est qu'une question de temps avant de rencontrer une telle collision de noms.

**Deuxième exemple**  
WordPress peut stocker plusieurs valeurs pour le même nom de clé et le même ID de post. (Sauf si vous fournissez un paramètre spécial appelé `$unique`).

Cela signifie que si vous enregistrez vos données 5 fois sous la clé `location`, vous recevrez un tableau composé de 5 éléments lorsque vous appellerez `get_post_meta()`.

Supposons que vous avez un post sur les villes que vous avez visitées. Vous avez été dans 5 villes et ces emplacements sont affichés sur la carte intégrée dans le post. Simple, n'est-ce pas ?

Attention ! Le code suivant n'est pas utile. ;) !

```
//NYadd_post_meta($post_id, 'location', '40.7127753, 73.989308'); 
```

```
//LAadd_post_meta($post_id, 'location', '34.0522342, -118.2436849');
```

```
//Parisadd_post_meta($post_id, 'location', '48.856614, 2.3522219000000177'); 
```

```
//Viennadd_post_meta($post_id, 'location', '48.2081743, 16.37381890000006'); 
```

```
//Romeadd_post_meta($post_id, 'location', '41.90278349999999, 12.496365500000024');
```

```
//Vérifions ce que nous avons icivar_dump(get_post_meta($post_id, 'location');
```

```
array (size=5)0 => string '40.7127753, 73.989308' (length=21)1 => string '34.0522342, -118.2436849' (length=24)2 => string '48.856614, 2.3522219000000177' (length=29)3 => string '48.2081743,16.37381890000006' (length=28)4 => string '41.90278349999999,12.496365500000024' (length=36)
```

Et si après un certain temps vous utilisez un nouveau thème ou plugin. Il a une fonctionnalité qui peut définir la position d'un post sur une page d'accueil. Vous pouvez choisir entre un slider, une barre latérale ou des posts mis en avant, etc. Ce scénario peut se terminer comme ceci :

```
array (size=6) 0 => string '40.7127753, 73.989308' (length=21) 1 => string '34.0522342, -118.2436849' (length=24) 2 => string '48.856614, 2.3522219000000177' (length=29) 3 => string '48.2081743,16.37381890000006' (length=28) 4 => string '41.90278349999999,12.496365500000024' (length=36) 5 => string 'left_sidebar' (length=12) // Oui, c'est ça...
```

Ou même pire :

```
array (size=5)  0 => string 'left_sidebar' (length=12)  1 => string 'left_sidebar' (length=12)  2 => string 'left_sidebar' (length=12)  3 => string 'left_sidebar' (length=12)  4 => string 'left_sidebar' (length=12)
```

Votre joli petit plan **est maintenant cassé !** Et vous avez perdu toutes vos données saisies. Pas drôle, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/UVx09NmJbiPAIBJ1GJ7CgaDLvClyDxRghgYS)
_C-c-c-cassé ?? ;( source https://pixabay.com_

### Solution

Vous ne pouvez jamais protéger vos données de champs personnalisés contre l'écrasement ou la suppression. C'est ainsi que WordPress fonctionne et c'est ce qui le rend si flexible. **Vous pouvez cependant réduire ce risque.**

**Comment ?**  
En évitant les noms communs et en utilisant un espace de noms pour **toutes** vos clés de champs personnalisés.

Ma convention proposée est :

* **cpt-nom_du_champ**   
comme `books_author` au lieu de `author`, `order_items` au lieu de `items` (solution pour les plus paresseux :) ).
* **but_du_champ**  
comme `front_page_location` au lieu de `location`, `visited_cities_locations` au lieu de `location`.
* **préfixe_(cpt-nom/but)_du_champ**   
comme `kg_books_author`, `kg_visited_cities_locations` (pour les plus stricts).

Ce n'est pas tout. En outre, vous devriez toujours prendre soin des paramètres optionnels des fonctions intégrées de WordPress :

* [add_post_meta()](https://codex.wordpress.org/Function_Reference/add_post_meta) a `$unique` pour ne pas ajouter le champ personnalisé s'il existe déjà.
* [get_post_meta()](https://developer.wordpress.org/reference/functions/get_post_meta/) utilise `$single` pour récupérer un seul enregistrement (si vous attendez un seul enregistrement).
* [update_post_meta()](https://codex.wordpress.org/Function_Reference/update_post_meta) et [delete_post_meta()](https://codex.wordpress.org/Function_Reference/delete_post_meta) utilisent `$previous_value` pour s'assurer que vous mettez à jour/supprimez la clé que vous souhaitez.

Ces paramètres aident à écrire un code meilleur, plus propre et plus prévisible.

Et ce n'est pas tout. Utilisez des plugins bien testés, bien écrits et extensibles comme [Pods Framework](https://pods.io/) ou [Advanced Custom Fields](https://www.advancedcustomfields.com/). Ceux-ci vous aideront à gérer vos champs personnalisés. Ils sont excellents lorsqu'il s'agit de gérer le monde complexe de vos données personnalisées.

### Résumé

Dans un monde idéal, nous devrions toujours être conscients de ce que nous ajoutons au système. Nous devrions savoir ce que font vos plugins, thèmes et fonctions personnalisées. Cela n'est malheureusement pas toujours possible.

Par conséquent, nous devrions prêter attention au code que nous produisons et resserrer toutes ces extrémités lâches.

C'est tout pour aujourd'hui ! J'espère que vous avez aimé et que vous passez une excellente journée !

Cet article a été initialement publié sur [mon blog privé](https://kamilgrzegorczyk.com/2017/10/12/best-practices-naming-convention-for-wordpress-custom-fields/) où j'écris sur WordPress et le développement en général.
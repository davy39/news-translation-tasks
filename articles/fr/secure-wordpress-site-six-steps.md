---
title: Comment sécuriser un site WordPress existant en six étapes faciles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-29T20:02:51.000Z'
originalURL: https://freecodecamp.org/news/secure-wordpress-site-six-steps
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/wordpress-site-security-tips.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: WordPress
  slug: wordpress
seo_title: Comment sécuriser un site WordPress existant en six étapes faciles
seo_desc: "By Andrej Kovacevic\nIf you're looking to build a flexible website these\
  \ days, there's a good chance you're going to use a content management system (CMS).\
  \ And WordPress is, by far, the most popular one. \nAt last count, WordPress powered\
  \ about 40% of ..."
---

Par Andrej Kovacevic

Si vous cherchez à créer un site web flexible de nos jours, il y a de fortes chances que vous utilisiez un système de gestion de contenu (CMS). Et WordPress est, de loin, le plus populaire. 

Lors du dernier décompte, WordPress alimentait environ [40 % de tous les sites web sur Internet](https://w3techs.com/technologies/overview/content_management). Cela signifie que si vous êtes un programmeur web, vous rencontrerez probablement WordPress à un moment donné dans le cadre de votre travail.

Mais parce que WordPress est si largement utilisé, tout programmeur travaillant avec doit prendre grand soin de le sécuriser contre les attaques externes. Et ces attaques continuent de se multiplier. Lors d'un seul incident l'année dernière, près de [un million de sites web ont été attaqués](https://www.helpnetsecurity.com/2020/05/06/wordpress-extensive-attacks/) en un seul mois.

Le problème est que aucun deux sites WordPress ne sont construits de la même manière, ce qui signifie qu'il existe un nombre infini de vulnérabilités potentielles à surveiller. Et lorsque vous ajoutez des plugins tiers dans le mélange, il devient impossible de monter une défense parfaite pour le site web. 

Mais il y a certaines choses que vous pouvez faire pour sécuriser un site WordPress contre les attaques, ce qui stoppera toutes les menaces sauf les plus sophistiquées. Voici six étapes de sécurité à suivre sur chaque site WordPress avec lequel vous travaillez.

## Étape Un : Mettre à jour WordPress vers la dernière version

Puisque WordPress est un logiciel, il est crucial de le maintenir à jour pour corriger les vulnérabilités dès qu'elles sont identifiées. Mais un nombre choquant de développeurs et de propriétaires de sites négligent de le faire. 

Les données récentes indiquent que jusqu'à 70 % des installations WordPress connues [utilisent encore des versions avec des vulnérabilités connues](https://www.wpwhitesecurity.com/statistics-70-percent-wordpress-installations-vulnerable/).

Bien que l'on pourrait penser que cette information déclencherait des alarmes partout sur Internet, le problème persiste. Une partie de cela est due au fait que les entreprises ne sont pas disposées à payer pour une aide professionnelle afin de compléter le travail. Et une autre partie est due au fait que certains sites dépendent de plugins hérités qui ne fonctionneront pas avec les nouvelles versions de WordPress.

Mais tout développeur qui travaille sur un tel site cherche des ennuis. Il serait donc préférable d'insister sur une mise à jour du site chaque fois que vous rencontrez une installation WordPress obsolète. 

Si vous prenez le temps de partager certaines des statistiques sur les menaces avec le propriétaire du site, il verra finalement la lumière. Assurez-vous simplement de faire une sauvegarde complète du site avant d'apporter des modifications.

Si quelque chose ne va pas et que des pages se cassent ou que des plugins échouent, vous créerez un problème plus grand que vous ne résolvez. Selon [Vudu Digital](https://vududigital.co.uk/), c'est un problème que de nombreux développeurs rencontrent, et il cause des dommages réels. Ils ont dit,

> _"Nous avons dû nettoyer après des mises à jour WordPress échouées qui ont conduit à des pages désactivées en raison de la rupture du site. Lorsque cela se produit, ces pages peuvent disparaître des index de recherche assez rapidement, donc il est essentiel de revenir en arrière rapidement."_

## Étape Deux : Supprimer les plugins inutilisés et mettre à jour les autres

Tout comme une installation principale de WordPress, les plugins souffrent également de vulnérabilités que les développeurs corrigent de temps en temps. Et WordPress est particulièrement dépendant des plugins pour fournir toutes sortes de fonctionnalités. 

Par exemple, lorsque j'ai récemment travaillé sur le site web d'une entreprise locale de [plomberie](https://www.yourchoiceplumbers.com.au/), j'ai été surpris de voir quels plugins étaient utilisés, étant donné la simplicité relative du site.

Mais la meilleure façon de minimiser la surface d'attaque potentielle est de commencer par supprimer les plugins redondants ou inutilisés du site avant de chercher les mises à jour disponibles. Cela simplifiera les tâches de maintenance continues et réduira les vulnérabilités potentielles. 

Ce n'est qu'une fois cela fait que vous devriez vérifier l'état de mise à jour des plugins restants.

Après avoir appliqué les mises à jour disponibles, ne supposez pas que tout va bien. Vérifiez si certains des plugins restants n'ont pas eu de mises à jour depuis un certain temps, et essayez de comprendre pourquoi. 

Si vous découvrez qu'un développeur de plugin a soit disparu soit abandonné un plugin, cherchez un remplacement activement maintenu. Plus un plugin reste sans activité de développement, plus les chances qu'il devienne un problème de sécurité sont grandes.

## Étape Trois : Minimiser les permissions des utilisateurs et sécuriser les connexions

Même si le site WordPress sur lequel vous travaillez ne contient aucune vulnérabilité connue, cela ne signifie pas qu'il est sûr. Cela est dû au fait que les [attaques par force brute des identifiants](https://www.malcare.com/blog/wordpress-brute-force/) sont le moyen le plus courant pour les pirates d'obtenir un accès non autorisé aux sites web WordPress. Et la meilleure façon de prévenir les dommages causés par celles-ci est de réviser les permissions des utilisateurs et les politiques de mots de passe.

Tout d'abord, essayez de réduire le nombre de comptes ayant un accès de niveau administrateur. Il n'est pas rare que les petites entreprises désignent presque tout le monde comme administrateur, mais cela représente un risque énorme. 

Ainsi, réviser chaque compte et attribuer le niveau de permission le plus bas possible parmi les groupes d'accès intégrés :

* **Super Administrateurs** – Super-utilisateurs de WordPress. Essayez de les limiter à un maximum de deux.
* **Administrateurs** – Il s'agit de la permission la plus élevée pour les utilisateurs généraux. Encore une fois, essayez de les garder à un minimum.
* **Éditeur** – Pour les utilisateurs qui doivent contrôler et apporter des modifications à tous les articles publiés.
* **Auteur** – Un utilisateur qui ne peut publier et modifier des choses qu'en son propre nom.
* **Contributeur** – Peut ajouter, mais pas publier des articles en son propre nom.
* **Abonné** – Ne peut pas apporter de modifications au site sauf à son profil utilisateur.

Si vous rencontrez des utilisateurs qui n'ont plus besoin d'accès, supprimez-les. Ensuite, utilisez le [plugin Google Authenticator](https://wordpress.org/plugins/google-authenticator/) ou un autre système d'authentification à deux facteurs pour sécuriser les comptes restants.

## Étape Quatre : Désactiver l'exécution de PHP dans les dossiers non fiables

Jusqu'à présent, toutes les étapes précédentes ont tourné autour de la prévention des attaques courantes et de bas niveau. 

Mais il existe également des menaces plus sophistiquées pour les sites WordPress dont vous devriez vous soucier. Et beaucoup d'entre elles impliquent des attaquants trouvant des moyens d'exécuter du code sur un site sans obtenir d'accès au compte du tout. 

Cela est courant avec WordPress en raison de la manière dont il gère les permissions des dossiers par défaut.

Par exemple, si vous installez un plugin qui gérera les médias téléchargés par les utilisateurs comme des images et des vidéos, il aura besoin d'un dossier de téléchargement accessible en écriture depuis l'extérieur. Si un attaquant peut accéder à ce dossier, il peut essayer de télécharger un script malveillant et l'utiliser pour altérer ou prendre le contrôle de l'ensemble du site. 

La bonne nouvelle est que vous pouvez vous protéger contre cela avec un simple fichier de contrôle d'accès dans les dossiers nécessaires.

Ce que vous devrez faire, c'est créer un nouveau fichier dans chaque dossier accessible en écriture appelé .htaccess. C'est un fichier texte qui indique au serveur web ce qu'il doit autoriser ou interdire dans un répertoire donné. Incluez ce qui suit :

```php
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase
RewriteRule ^index\.php$ - [L] RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L] </IfModule>
# END WordPress
<FilesMatch "\.(php|php\.)$">
Order Allow,Deny
Deny from all
</FilesMatch>
```

Ce fichier .htaccess permettra aux utilisateurs de télécharger les types de fichiers que vous souhaitez, mais empêchera quiconque de télécharger du code exécutable dans le répertoire accessible en écriture. 

Vous pouvez faire cela dans n'importe quel dossier accessible aux utilisateurs que vous souhaitez protéger. Mais méfiez-vous de l'utilisation excessive de ces restrictions. La plupart de WordPress implique l'exécution de PHP, et vous pouvez désactiver l'ensemble de votre site si vous placez l'un de ceux-ci au mauvais endroit.

## Étape Cinq : Désactiver l'affichage des erreurs PHP

Obtenir un accès en écriture et en exécution aux répertoires est l'une des façons dont un attaquant pourrait essayer d'exécuter du code malveillant sur un site web WordPress. Ils peuvent également rechercher des parties du site qui exécutent PHP (ce qui est pratiquement partout où vous n'avez pas verrouillé) et trouver des faiblesses là. Mais vous pouvez rendre leur travail beaucoup plus difficile.

Pour ce faire, vous devez désactiver l'affichage des erreurs PHP afin qu'ils ne puissent pas voir les résultats lorsqu'ils essaient de casser intentionnellement les pages du site. Si le site leur donne des indices sur ce qui fonctionne et ce qui ne fonctionne pas, cela pourrait fournir une feuille de route pour trouver un moyen d'exploiter les pages existantes du site. 

La bonne nouvelle est qu'il est simple de désactiver la génération de rapports d'erreurs PHP dans WordPress. Tout ce que vous avez à faire est de modifier le fichier wp-config.php du site, qui se trouve dans le répertoire racine et contient les informations de configuration de base du site. 

Ajoutez simplement la ligne suivante au fichier :

```php
define( 'WP_DEBUG', false);
```

Cela désactivera le débogage PHP sur l'ensemble du site. Faites simplement une note lorsque vous apportez cette modification au cas où le site rencontrerait des problèmes à l'avenir et nécessiterait des efforts de débogage autorisés.

## Étape Six – Désactiver l'édition de thèmes et de plugins

Même après avoir fait tout ce qui précède, vous ne pouvez pas être certain que personne ne trouvera jamais un moyen d'accéder à un site WordPress avec l'intention de nuire. Vous devriez donc mettre en place un dernier ensemble d'obstacles.

Cela n'arrêtera pas un attaquant sérieux de semer le chaos, mais cela pourrait donner aux opérateurs du site suffisamment de temps pour remarquer que quelque chose ne va pas et prendre des mesures pour le corriger.

Ce que vous devriez faire, c'est désactiver la capacité d'édition intégrée des thèmes et plugins WordPress pour rendre plus difficile pour quelqu'un qui a accès à l'interface administrative de modifier le codage de base du site. 

Une fois de plus, vous pouvez faire cela en modifiant le fichier wp-config.php du site situé dans son répertoire racine. Ajoutez la ligne suivante juste avant l'endroit où vous voyez les mots 'That's all, stop editing! Happy publishing' :

```php
define( 'DISALLOW_FILE_EDIT', true );
```

Cela masquera les éditeurs de thèmes et de plugins de l'interface administrative et empêchera tout moyen facile de modifier les fichiers du site. Pour annuler cette modification, l'attaquant aurait besoin d'un accès FTP ou au niveau des fichiers à l'hébergeur web, ce qui le ralentira au moins un peu.

Et en guise de note finale, bien que vous puissiez voir des conseils ailleurs vous indiquant d'utiliser un plugin de snippet de code pour apporter ces modifications, ne le faites pas. Si vous le faites, un attaquant pourrait utiliser ce même plugin pour annuler vos modifications, annulant la valeur de sécurité des modifications apportées en premier lieu.

## Des protections imparfaites valent toujours la peine d'être essayées

Le point essentiel ici est que WordPress sera toujours quelque peu victime de son propre succès. Il y a simplement trop de sites web qui en dépendent, ce qui en fait une cible importante et attrayante pour les attaquants. 

Et bien que ces six mesures n'arrêteront pas tous les types de menaces possibles, elles feront un travail décent pour se défendre contre la plupart des attaques courantes.

Vous pouvez (et devriez) également essayer de protéger vos bases de données de sites en changeant le préfixe de table par défaut en quelque chose d'obscur. Mais comme cela est un peu hors de portée pour un site web existant, je l'ai omis comme mesure de sécurité ici. 

Si vous souhaitez essayer, il y a un [excellent guide situé ici](https://www.wpbeginner.com/wp-tutorials/how-to-change-the-wordpress-database-prefix-to-improve-security/). Sinon, soyez satisfait d'avoir fait votre part pour aider à garder l'un des nombreux sites WordPress en fonctionnement dans le monde un peu plus sûr.

_Photo en vedette par IB Photography - stock.adobe.com._
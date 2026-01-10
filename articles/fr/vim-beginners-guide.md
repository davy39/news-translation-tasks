---
title: Comment utiliser Vim – Tutoriel pour débutants
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-01-30T16:08:32.000Z'
originalURL: https://freecodecamp.org/news/vim-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/BB
seo_title: Comment utiliser Vim – Tutoriel pour débutants
---

Vim---Un-Guide-Rapide-Pour-Débutants.png
balises:
- nom: débutant
  slug: debutant
- nom: Linux
  slug: linux
- nom: vim
  slug: vim
seo_title: null
seo_desc: "Vim est l'un des éditeurs de texte les plus populaires parmi les utilisateurs de Linux. Les administrateurs système Linux le préfèrent souvent à d'autres éditeurs. \nDans cet article, vous apprendrez beaucoup sur Vim et verrez comment vous pouvez commencer à utiliser Vim rapidement en tant que développeur.\nQu'est-ce que..."
---

Vim est l'un des éditeurs de texte les plus populaires parmi les utilisateurs de Linux. Les administrateurs système Linux le préfèrent souvent à d'autres éditeurs. 

Dans cet article, vous apprendrez beaucoup sur Vim et verrez comment vous pouvez commencer à utiliser Vim rapidement en tant que développeur.

## Qu'est-ce que Vim ? 

Vim est l'acronyme de **Vi IM**proved. C'est un éditeur de texte libre et open-source multiplateforme. Il a été publié pour la première fois par Bram Moolenaar en 1991 pour les variantes UNIX. 

Vim est basé sur l'éditeur Vi original, qui a été créé par Bill Joy en 1976. Dans les années 90, il est devenu clair que Vi manquait de certaines fonctionnalités par rapport à l'éditeur Emacs. Bram a donc implémenté de nombreuses fonctionnalités manquantes et l'a publié sous le nom de Vim. 

## Comment installer Vim

Vim fonctionne sur diverses plateformes telles que Windows, Linux et Mac. 

Pour installer Vim sur Windows, téléchargez le fichier exécutable depuis le [site de Vim](https://www.vim.org/download.php) et exécutez le fichier. Suivez les instructions affichées à l'écran et vous serez prêt à l'utiliser. 

Vim est préinstallé sur la plupart des systèmes d'exploitation *nix. Mais s'il n'est pas installé sur votre système, vous pouvez l'installer avec un gestionnaire de paquets de votre choix. 

Voici la commande d'installation pour les systèmes d'exploitation basés sur Debian :

```bash
sudo apt-get update
sudo apt-get install vim
```

Pour vous assurer qu'il est installé correctement, exécutez `which vim` et vous devriez obtenir `/usr/bin/vim` dans votre sortie. 

## Comment commencer avec Vim

Vous pouvez commencer avec Vim en tapant son nom sur le terminal comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-274.png)
_Démarrer Vim_

Une fois que vous avez entré la commande ci-dessus, vous verrez un écran affichant des informations sur Vim et quelques instructions pour trouver de l'aide et quitter Vim. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-276.png)
_Introduction à Vim_

## Modes de Vim

Vous devez être conscient du concept le plus important dans Vim avant de continuer : les modes dans Vim. 

Tout dans Vim est considéré comme un mode. Vous pouvez accomplir tout ce que vous voulez si vous comprenez les modes dans Vim. Il existe de nombreux modes dans Vim. Mais nous allons examiner les 4 modes les plus importants. 

Ils sont :

1. Mode Commande
2. Mode Ligne de Commande
3. Mode Insertion
4. Mode Visuel

Explorons-les un par un. 

### Qu'est-ce que le Mode Commande ?

C'est le mode par défaut (aussi appelé Mode Normal) dans Vim. Chaque fois que Vim démarre, vous serez dans ce mode. Vous pouvez passer à n'importe quel mode à partir de ce mode. Vous ne pouvez pas faire cela dans d'autres modes. 

En gros, pour passer d'un mode à un autre, vous devez d'abord revenir au Mode Commande puis naviguer vers l'autre mode. Les commandes que vous exécutez sans préfixe (deux-points) indiquent que vous exécutez la commande en mode commande. 

### Qu'est-ce que le Mode Insertion ?

Ce mode est utilisé pour éditer le contenu du fichier. Vous pouvez passer en mode insertion en appuyant sur `i` depuis le mode commande. Vous pouvez utiliser la touche `Esc` pour revenir au mode commande. 

### Qu'est-ce que le Mode Ligne de Commande ?

Vous pouvez utiliser ce mode pour jouer avec certaines commandes. Mais les commandes dans ce mode sont précédées d'un deux-points (:). Vous pouvez passer à ce mode en appuyant sur : (deux-points) en mode commande. 

### Qu'est-ce que le Mode Visuel ?

Vous utilisez ce mode pour sélectionner visuellement du texte et exécuter des commandes sur cette section de code. Vous pouvez passer à ce mode en appuyant sur `v` depuis le mode commande. 

Les 4 modes ci-dessus sont suffisants pour effectuer un ensemble de base d'opérations sur les fichiers dans Vim.

Ok, la théorie est terminée. Explorons Vim de manière pratique.

## Opérations courantes de l'éditeur de texte dans Vim

### Comment créer un nouveau fichier

Créer un nouveau fichier avec Vim est simple. Vous pouvez le faire depuis le mode ligne de commande. 

Exécutez la commande suivante pour créer un nouveau fichier :

```vim
:edit sample.txt
```

La commande ci-dessus ouvre un fichier `sample.txt` en mode édition s'il existe, et crée un nouveau fichier sinon. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-278.png)
_Créer un nouveau fichier avec le nom `sample.txt`_

Après avoir exécuté cette commande, vous serez en mode commande (comme montré dans la capture d'écran ci-dessous), et vous ne pourrez pas entrer de texte :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-279.png)
_Mode commande montrant le nouveau fichier créé_

Pour ajouter du texte au fichier créé, appuyez sur `i` sur le clavier. Vous utilisez la commande `i` pour entrer du texte dans le fichier. Une fois que vous appuyez sur `i`, vous pourrez voir que vous êtes entré en mode insertion dans Vim en regardant en bas à gauche du fichier. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-280.png)
_Mode insertion dans le fichier `sample.txt` dans Vim_

Dans ce mode, vous pouvez taper ce que vous voulez dans le fichier. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-281.png)
_Ajouté du contenu dans le fichier `sample.txt`_

Nous avons terminé l'écriture de notre contenu. Maintenant, nous voudrons sauvegarder le fichier. Si vous ne sauvegardez pas et fermez simplement le terminal à ce stade, tout votre contenu sera perdu. 

### Comment sauvegarder un fichier

Pour sauvegarder un fichier, vous devez passer du mode insertion au mode ligne de commande. Rappelez-vous, je vous l'ai dit plus tôt – chaque fois que vous voulez passer d'un mode à un autre, vous devez d'abord passer en mode commande puis vous pouvez facilement passer au mode que vous voulez. 

Pour passer en mode commande depuis le mode insertion, vous devez appuyer sur la touche `Esc`. 

Après avoir appuyer sur la touche `Esc`, vous ne verrez plus le `--INSERT--` en bas à gauche. Cela indique que vous n'êtes plus en mode insertion et que vous êtes maintenant en mode commande. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-283.png)
_Mode commande dans le fichier `sample.txt`_

Pour sauvegarder le fichier, tapez la commande suivante :

```vim
:w
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-284.png)
_Commande pour sauvegarder le fichier_

### Comment fermer un fichier et quitter Vim

Une fois que vous avez sauvegardé le fichier, vous pouvez fermer Vim en fermant le terminal. Mais la manière appropriée de fermer le fichier et l'éditeur Vim est d'utiliser la commande suivante :

```vim
:q
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-285.png)
_Fermer le fichier et l'éditeur vim_

La commande ci-dessus ferme le fichier et quitte l'éditeur vim. 

Alternativement, vous pouvez utiliser une commande qui est la combinaison des deux commandes ci-dessus (sauvegarder et quitter) pour sauvegarder et quitter Vim rapidement. La commande est :

```vim
:wq
```

La commande ci-dessus quitte l'éditeur Vim immédiatement après avoir sauvegardé le fichier. 

### Comment éditer un fichier dans Vim

Pour éditer un fichier, vous devez ouvrir le fichier en utilisant Vim et passer en mode insertion. 

Ouvrons le fichier `sample.txt` que nous avons créé ci-dessus :

```vim
vim sample.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-287.png)
_Ouvrir le fichier `sample.txt` en utilisant Vim_

Nous sommes maintenant en mode commande. Pour éditer le fichier, nous devons passer en mode insertion. Comme nous l'avons vu précédemment, appuyer sur `i` depuis le mode commande passera en mode insertion. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-289.png)
_Passer en mode insertion en appuyant sur `i`_

Suivez la même procédure pour sauvegarder le fichier et quitter Vim. Appuyez sur `Esc` sur le clavier et tapez `:w` pour sauvegarder le fichier et `:q` pour quitter Vim. 

Vous vous demandez peut-être, cependant, que faire si je veux fermer le fichier sans sauvegarder mes modifications ? (Ignorer les modifications que j'ai apportées et ramener le fichier à l'état précédent). 

#### Comment fermer le fichier sans sauvegarder les modifications

Pour fermer le fichier sans sauvegarder les modifications, vous devez exécuter `:q!` depuis le mode commande. 

Explorons cela avec un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-292.png)
_Contenu du fichier `sample.txt`_

J'ai ajouté un peu plus de contenu au fichier. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-293.png)
_Ajouté du contenu dans le fichier `sample.txt`_

Mais je ne veux pas sauvegarder les modifications que j'ai apportées maintenant. Pour fermer le fichier sans sauvegarder cette modification, nous devons passer en mode commande (en appuyant sur la touche `Esc`). Tapez `:q!` en mode commande. Cela fermera le fichier en ignorant les modifications apportées. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-294.png)
_Ignorer la sauvegarde du fichier `sample.txt`_

Regardons le fichier et confirmons si nous obtenons la sortie attendue :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-295.png)
_Voir le fichier `sample.txt`_

Oui. Le fichier ne contient pas la dernière ligne que nous avons ajoutée récemment. Donc, les modifications n'ont pas été sauvegardées. 

### Comment couper, copier et coller du texte depuis un fichier en utilisant Vim 

Vous pouvez couper, copier et coller de deux manières dans Vim. Elles sont :

1. En utilisant le mode visuel
2. En utilisant le clavier

Parmi ces deux méthodes, le mode visuel est plus simple à comprendre. Puisque ce guide est adapté aux débutants, explorons comment couper, copier et coller en mode visuel. 

Ouvrons le fichier en mode commande avant de continuer :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-231.png)
_Fichier `sample.txt` ouvert en mode commande dans Vim_

Supposons que vous souhaitez copier le mot "Hello" de la première ligne et le coller dans la troisième ligne. 

La première étape consiste à placer votre curseur à l'endroit d'où vous souhaitez copier le texte (en étant en mode commande).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-232.png)
_Déplacement du curseur au début du mot `Hello`_

Entrez en mode visuel en appuyant sur la touche `v` du clavier. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-233.png)
_Entrer en mode visuel_

Le texte `-- VISUAL –-` en bas à gauche indique que nous sommes en mode visuel. 

Déplacez le curseur à l'endroit où le texte que vous souhaitez copier se termine. 

Dans ce cas, je déplace le curseur vers la lettre `o` du mot `Hello`. 

Pendant que vous déplacez votre curseur, le mode visuel met en surbrillance le texte depuis le début jusqu'à votre curseur.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-235.png)
_Texte mis en surbrillance en mode visuel_

Une fois que vous avez déplacé votre curseur au bon endroit, appuyez sur `y` pour copier le texte ou appuyez sur `d` pour couper le texte. 

Dans ce cas, je copie le texte. Donc, j'appuie sur `y` sur mon clavier. 

Déplacez le curseur à l'endroit où vous souhaitez coller le texte. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-296.png)
_Déplacer le curseur à l'endroit où vous souhaitez coller le texte_

Dans notre cas, nous devons déplacer le curseur à la troisième ligne. 

Appuyez sur `p` (en minuscule) pour coller le texte après le curseur et `P` (en majuscule) pour coller le texte avant le curseur. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-236.png)
_Texte `Hello` collé sur la 3ème ligne_

Appuyez sur `:wq` pour sauvegarder et fermer le fichier

### Comment trouver et remplacer du texte dans Vim

Trouver du texte et le remplacer par un autre texte est simple et direct dans Vim. Il existe une commande en une ligne qui simplifie tout ce processus. 

Voici la syntaxe :

```vim
:[range]s/{pattern}/{string}/[flags]
```

Démontons chaque partie et comprenons comment tout cela fonctionne. 

* `[range]` indique que vous pouvez passer la plage de lignes. Passez % pour trouver et remplacer dans toutes les lignes. La plage est séparée par une virgule. Pour trouver et remplacer entre les lignes 5 et 10, passez 5,10. Utilisez `.` pour représenter la ligne actuelle et `$` la dernière ligne du fichier. 
* `{pattern}` indique le motif pour trouver le texte. Vous pouvez passer des motifs regex ici.
* `{string}` est la chaîne à remplacer dans le texte trouvé.  
* `[flags]` indique si vous souhaitez passer des flags supplémentaires (par exemple, le flag `c` est passé pour confirmer avant de remplacer le texte). Par défaut, cela effectue une recherche sensible à la casse. Vous pouvez la changer pour effectuer une recherche insensible à la casse en passant un flag `i`. 

D'accord, explorons cela avec un exemple. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-237.png)
_Contenu du fichier `sample.txt`_

Notre fichier `sample.txt` contient 2 "Hello". Remplaçons "Hello" par "Hi" aux deux endroits. 

La commande pour cela est :

```vim
:%s/Hello/Hi/g
```

* `%s` indique le remplacement du contenu dans le fichier entier
* `Hello` est le texte de recherche
* `Hi` est le texte de remplacement
* `g` indique faire le changement globalement

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-238.png)
_Pendant l'exécution de la commande pour changer "Hello" par "Hi"_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-239.png)
_Après l'exécution de la commande_

Comprenons cela avec un autre exemple. 

Cette fois, je veux changer le mot "Hi" (recherche insensible à la casse) qui apparaît entre les lignes 2 et 3 et le remplacer par "Hello and Welcome", avec une confirmation pour changer chaque occurrence. 

La commande pour cela est :

```vim
:2,3s/Hi/Hello and Welcome/gci
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-297.png)
_Exécution de la commande pour changer le texte de la ligne 2 à la ligne 3_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-241.png)
_Demande de confirmation pour changer l'occurrence_

Voici une description pour chaque option :

* `y` - Remplacer la correspondance 
* `n` - Ignorer la correspondance
* `a` - Substitue la correspondance et toutes les occurrences restantes de la correspondance
* `q` ou `Esc` - Quitter la substitution
* `l` - Remplacer la correspondance et quitter
* `CTRL+Y` - Faire défiler l'écran vers le bas
* `CTRL+E` - Faire défiler l'écran vers le haut

Je veux accepter le changement. Donc, j'appuie sur `y`. Voici le résultat après avoir appuyé sur `y`. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-242.png)
_Après le remplacement du mot_

Puisque nous n'avons qu'une seule occurrence de "Hi" entre les lignes 2 et 3, il n'a pas demandé d'autres confirmations et l'opération est terminée. 

### Comment annuler ou rétablir dans Vim 

Pour annuler un changement dans Vim, appuyez sur `u` en mode commande. Pour rétablir, appuyez sur `CTRL + R`. Vous pouvez préfixer un nombre (n) avec `u` pour annuler `n` fois. Par exemple, `2u` annulera 2 fois. Pour lister les options d'annulation disponibles, tapez `:undolist` en mode commande. 

Comprenons cela avec un exemple. 

Voici l'état actuel de notre fichier sample.txt :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-254.png)
_État actuel du fichier `sample.txt`_

Mon curseur est sur "a" dans le texte "Hello and Welcome" à la 3ème ligne. Supprimons le mot "and" en tapant `dw` en mode commande :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-257.png)
_Suppression du mot `and` en tapant `dw` en mode commande_

Annulons pour ramener le mot "and" dans le fichier. Pour ce faire, appuyez sur `u` en mode commande. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-258.png)
_Les changements sont annulés après avoir tapé `u` en mode commande_

Rétablissons et supprimons à nouveau le mot "and" en tapant `CTRL + R` en mode commande. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-298.png)
_Les changements ont été appliqués à nouveau lors du rétablissement en appuyant sur `CTRL + R` en mode commande_

## Conclusion

Dans cet article, vous avez appris les bases de Vim. Cet article devrait être suffisant pour vous permettre de commencer et d'effectuer certaines opérations de lecture/écriture de fichiers de base avec Vim. 

Gardez simplement à l'esprit que je n'ai même pas couvert 1% de Vim. Mais je suis sûr que ces bases vous aideront à explorer Vim rapidement et en toute confiance. 

Pour en savoir plus sur Vim, abonnez-vous à ma newsletter par e-mail sur mon [site](https://www.freecodecamp.org/news/p/e557f026-0774-4fad-9c2f-d598e88b5250/5minslearn.gogosoon.com/?ref=fcc_vim_a_quick_getting_started_guide) et suivez-moi sur les réseaux sociaux.
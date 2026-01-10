---
title: Raccourcis clavier Vim – Référence de la liste des touches Vim
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-06T09:28:01.000Z'
originalURL: https://freecodecamp.org/news/vim-key-bindings-reference
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-4-.png
tags:
- name: cheatsheet
  slug: cheatsheet
- name: reference
  slug: reference
- name: vim
  slug: vim
seo_title: Raccourcis clavier Vim – Référence de la liste des touches Vim
seo_desc: "Understanding Vim key bindings is crucial for navigating and editing text\
  \ efficiently in Vim or Vim-based text editors like Neovim. \nIn this article, we'll\
  \ explore the most common Vim key bindings that will help you navigate your text\
  \ editor seamless..."
---

Comprendre les raccourcis clavier de Vim est crucial pour naviguer et éditer du texte efficacement dans Vim ou des éditeurs de texte basés sur Vim comme Neovim. 

Dans cet article, nous explorerons les raccourcis clavier Vim les plus courants qui vous aideront à naviguer dans votre éditeur de texte de manière transparente.

## Table des matières

* [Modes Vim](#heading-modes-vim)
* [Comment naviguer en utilisant les raccourcis clavier Vim](#heading-comment-naviguer-en-utilisant-les-raccourcis-clavier-vim)
* [Comment éditer du texte en mode normal](#heading-comment-editer-du-texte-en-mode-normal)
* [Mode insertion](#heading-mode-insertion)
* [Mode visuel](#heading-mode-visuel)
* [Plus de commandes de navigation](#heading-plus-de-commandes-de-navigation)
* [Raccourcis clavier spécifiques à la programmation](#heading-raccourcis-clavier-vim-specifiques-a-la-programmation)
* [Conclusion](#heading-conclusion)

## Modes Vim

Vim fonctionne dans des modes distincts, chacun conçu pour des tâches spécifiques :

* **Mode Normal** : État par défaut pour un déplacement efficace, une suppression, une recherche, et plus encore.
* **Mode Insertion** : Vous permet de taper du texte directement dans votre fichier.
* **Mode Visuel** : Permet la sélection de texte pour la manipulation.

## Comment naviguer en utilisant les raccourcis clavier Vim

### Mouvement de base

Voici quelques touches de mouvement de base :

```plaintext
h  --> se déplacer à gauche
j  --> se déplacer vers le bas
k  --> se déplacer vers le haut
l  --> se déplacer à droite

```

### Se déplacer en haut et en bas

Vous pouvez utiliser ces touches pour vous déplacer en haut ou en bas de la page :

```plaintext
gg  --> Aller à la première ligne de la page
G   --> Aller à la dernière ligne de la page

```

### Se déplacer à une ligne spécifique

Vous pouvez vous déplacer à une ligne spécifique en utilisant `:` suivi du numéro de ligne :

```plaintext
:numero   --> Aller au numéro de ligne

```

### Se déplacer dans une ligne

Vous pouvez utiliser ces touches pour vous déplacer au début ou à la fin d'une ligne :

```plaintext
$  --> Aller à la fin de la ligne
0  --> Aller au début de la ligne

```

### Se déplacer à travers les mots

Voici quelques touches pour se déplacer à travers les lignes de texte :

```plaintext
b  --> Aller au mot précédent
w  --> Aller au mot suivant

```

## Comment éditer du texte en mode normal

### Suppression et copie

Vous pouvez supprimer ou copier des caractères en utilisant ces touches :

```plaintext
x   --> Supprimer le caractère sous le curseur
dd  --> Supprimer la ligne entière
yy  --> Copier (yank) la ligne entière
p   --> Coller le texte précédemment supprimé ou copié après le curseur

```

### Annuler et rétablir

```plaintext
u          --> Annuler la dernière action
Ctrl + r   --> Rétablir l'action annulée

```

### Recherche et remplacement

```plaintext
/              --> Commencer la recherche vers l'avant
?              --> Commencer la recherche vers l'arrière
:s/ancien/nouveau/g   --> Remplacer toutes les occurrences de "ancien" par "nouveau" dans le fichier entier

```

## Mode insertion

En mode insertion, vous pouvez taper du texte directement dans votre fichier. Voici quelques raccourcis clavier pour vous aider à naviguer dans ce mode :

```plaintext
Esc   --> Retour au mode normal
i     --> Commencer à insérer du texte avant le curseur
a     --> Commencer à insérer du texte après le curseur
o     --> Ouvrir une nouvelle ligne sous la ligne actuelle et commencer à insérer du texte

```

## Mode visuel

Le mode visuel est utile pour sélectionner et manipuler du texte visuellement. Voici quelques raccourcis clavier :

```plaintext
v          --> Démarrer le mode visuel caractère par caractère
V          --> Démarrer le mode visuel ligne par ligne
Ctrl + v   --> Démarrer le mode visuel par bloc
d          --> Supprimer le texte sélectionné
y          --> Copier (yank) le texte sélectionné
p          --> Coller le texte copié après le curseur

```

## Plus de commandes de navigation

### Défilement

```plaintext
Ctrl + u   --> Monter d'un demi-écran
Ctrl + d   --> Descendre d'un demi-écran
Ctrl + b   --> Monter d'un écran complet
Ctrl + f   --> Descendre d'un écran complet

```

### Sauter entre les mots et les paragraphes

```plaintext
(  --> Sauter au début de la phrase précédente
)  --> Sauter au début de la phrase suivante
{  --> Sauter au début du paragraphe précédent
}  --> Sauter au début du paragraphe suivant

```

Ces commandes fournissent un aperçu complet des raccourcis clavier Vim essentiels pour une navigation et une manipulation de texte efficaces.

## Raccourcis clavier Vim spécifiques à la programmation

### Se déplacer entre les fonctions

Dans un fichier de code, naviguer entre les fonctions est une tâche courante. Vim la rend efficace avec ces touches :

```plaintext
]]  --> Aller au début de la fonction suivante
[[  --> Aller au début de la fonction précédente

```

Ces commandes sont inestimables pour sauter rapidement entre différentes parties de votre code.

### Indentation

Maintenir une indentation de code cohérente est crucial. Vim améliore cela avec ces touches :

```plaintext
>>  --> Indenter la ligne actuelle vers la droite
<<  --> Indenter la ligne actuelle vers la gauche

```

Ajustez facilement l'indentation pour adhérer aux normes de codage et améliorer la lisibilité du code.

### Pliage de code

Le pliage de code aide à gérer les grands fichiers. Vim fournit des commandes de pliage puissantes :

```plaintext
zf{motion}  --> Créer un pli (remplacer {motion} par une commande de mouvement)
zo          --> Ouvrir un pli
zc          --> Fermer un pli
zr          --> Réduire le niveau de pliage dans tout le fichier
zm          --> Augmenter le niveau de pliage dans tout le fichier

```

Utilisez le pliage pour réduire et développer des sections, ce qui facilite la concentration sur des parties spécifiques de votre code.

### Commentaires de code

Commentez et décommentez efficacement le code avec :

```plaintext
gcc  --> Commenter/décommenter la ligne actuelle
gc{motion}  --> Commenter/décommenter les lignes couvertes par {motion}

```

Accélérez le processus de commentaire et maintenez la documentation du code sans effort.

### Correspondance des parenthèses

Naviguez et comprenez facilement la structure du code avec :

```plaintext
%  --> Aller à la parenthèse, au crochet ou à l'accolade correspondante

```

Cela facilite la navigation dans un code complexe en sautant rapidement entre les blocs de code correspondants.

## Conclusion

En essence, maîtriser les raccourcis clavier de Vim ouvre un monde d'édition de texte efficace. Des mouvements de base aux tâches de codage avancées, les modes et commandes de Vim rationalisent la navigation et la manipulation. 

En adoptant ces raccourcis clavier, vous améliorerez votre productivité et profiterez d'une expérience d'édition plus fluide. Bon codage dans Vim !

Si vous avez des commentaires, vous pouvez me contacter en DM sur [Twitter](https://twitter.com/introvertedbot) ou [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).
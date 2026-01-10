---
title: Comment utiliser l'éditeur de texte Vim – Une introduction pour les développeurs
subtitle: ''
author: Tanishka Makode
co_authors: []
series: null
date: '2025-02-04T17:17:39.346Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-vim-text-editor-intro-for-devs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738684583892/739ec0fa-e8a2-4f08-a265-7fa5034c932d.png
tags:
- name: vim
  slug: vim
- name: Linux
  slug: linux
- name: Text Editors
  slug: text-editors
seo_title: Comment utiliser l'éditeur de texte Vim – Une introduction pour les développeurs
seo_desc: 'Imagine a carpenter without tools, a writer without a pen, or a chef without
  a knife—this is like trying to imagine a developer or sysadmin without a reliable
  text editor.

  For devs, text editors are the ultimate multitools, shaping how we create, man...'
---

Imaginez un charpentier sans outils, un écrivain sans stylo ou un chef sans couteau—c'est comme essayer d'imaginer un développeur ou un administrateur système sans un éditeur de texte fiable.

Pour les développeurs, les éditeurs de texte sont les outils multifonctions ultimes, façonnant la manière dont nous créons, gérons et transformons des données brutes en sortie significative.

Alors que les éditeurs modernes comme VS Code et Sublime Text ont gagné en popularité pour leurs interfaces élégantes, il y a quelque chose d'intemporel dans la simplicité et la puissance des outils classiques.

Aimé par certains et craint par d'autres, Vim est un éditeur de texte qui a résisté à l'épreuve du temps. Né de son prédécesseur Vi, Vim (Vi Improved) offre une vitesse, une polyvalence et un contrôle inégalés.

Dans ce tutoriel, vous apprendrez ce qui rend Vim si spécial. Nous explorerons ses commandes, ses capacités de filtrage de texte et de manipulation de chaînes pour vous aider à exploiter sa véritable puissance.

## Ce que nous allons couvrir :

1. [Les éditeurs de texte sous Linux](#heading-les-editeurs-de-texte-sous-linux)

2. [Comment ouvrir l'éditeur Vim](#heading-comment-ouvrir-lediteur-vim)

3. [Les modes dans Vim](#heading-les-modes-dans-vim)

4. [Commandes de base de Vim](#heading-commandes-de-base-de-vim)

5. [Commandes de coupe, copie, collage et suppression](#heading-commandes-de-coupe-copie-collage-et-suppression)

6. [Commandes de recherche et de remplacement](#heading-commandes-de-recherche-et-de-remplacement)

7. [Comment lire des fichiers en utilisant more et less](#heading-comment-lire-des-fichiers-en-utilisant-more-et-less)

8. [Filtres de texte](#heading-filtres-de-texte)

9. [Outil de résumé de texte : wc](#heading-outil-de-resume-de-texte-wc)

## Les éditeurs de texte sous Linux

Linux propose une variété d'éditeurs de texte, chacun conçu pour différents types d'utilisateurs – des débutants aux développeurs avancés.

Des éditeurs comme **Nano** sont parfaits pour les nouveaux arrivants qui ont besoin d'une expérience simple et conviviale dans le terminal. Nano affiche des commandes utiles en bas de l'écran, ce qui facilite la navigation sans courbe d'apprentissage abrupte.

**Gedit**, l'éditeur par défaut pour l'environnement de bureau GNOME, offre une interface graphique propre, idéale pour l'édition de texte de base. D'autre part, **Kate** s'adresse aux utilisateurs du bureau KDE et propose une expérience plus riche en fonctionnalités, avec plusieurs fenêtres, une coloration syntaxique et un terminal intégré.

**Emacs** est un éditeur polyvalent et hautement personnalisable qui peut être transformé en un environnement de développement complet, idéal pour les utilisateurs avancés qui veulent plus qu'un simple éditeur de texte.

**VS Code** et **Atom** sont des éditeurs graphiques modernes qui offrent un ensemble riche de fonctionnalités, y compris des extensions, des outils de débogage et une intégration Git, ce qui en fait des favoris parmi les développeurs.

### Pourquoi de nombreux développeurs préfèrent-ils Vim ?

Malgré la large gamme d'éditeurs de texte disponibles sous Linux, Vim se distingue comme le choix préféré de nombreux utilisateurs, en particulier ceux qui ont besoin d'un environnement d'édition léger, rapide et hautement efficace.

Vim, une version améliorée de l'éditeur classique Vi, est disponible sur presque toutes les distributions Linux et peut être utilisé dans des environnements graphiques et basés sur le terminal. Sa popularité découle de sa vitesse et de son efficacité exceptionnelles.

Vim est entièrement piloté par le clavier, vous permettant d'effectuer des tâches d'édition complexes rapidement sans avoir besoin d'une souris. Cela le rend incroyablement utile pour le travail à distance, où vous pouvez avoir à vous fier à des ressources système minimales.

La puissance de Vim réside dans son système d'**édition modale**, qui sépare les modes de saisie de texte et de commandes, que vous apprendrez bientôt. Cela vous permet d'exécuter des actions précises avec quelques touches. Que vous naviguiez dans un fichier, recherchiez une chaîne ou effectuiez des manipulations de texte complexes, Vim vous permet de tout faire sans quitter le clavier.

Parce que Vim (ou Vi) est préinstallé sur la plupart des systèmes Linux, c'est souvent l'option privilégiée pour les développeurs et les administrateurs système, qui comptent sur son ubiquité et ses fonctionnalités puissantes. En bref, la combinaison de vitesse, de polyvalence et d'efficacité de Vim en fait l'éditeur de choix pour de nombreux utilisateurs Linux cherchant à booster leur productivité.

## Comment ouvrir l'éditeur Vim

Ouvrir un fichier dans Vim est simple et efficace. Pour commencer à éditer un fichier, utilisez simplement la commande suivante dans votre terminal :

```bash
vim [nom_du_fichier]
```

Ici, remplacez `[nom_du_fichier]` par le nom du fichier que vous souhaitez ouvrir. Si le fichier n'existe pas, Vim créera un nouveau fichier avec ce nom. Une fois exécutée, Vim ouvrira le fichier et vous permettra de commencer à éditer immédiatement.

Exemple :

```bash
vim data.txt # Un fichier qui n'existe pas encore, donc Vim crée un nouveau fichier nommé data.txt
```

Lorsque vous exécutez la commande `vim data.txt`, Vim a ouvert un nouveau fichier nommé `data.txt` parce qu'un fichier avec ce nom n'existait pas auparavant dans le répertoire courant. Dans Vim, cela est indiqué par le message en bas de l'éditeur, qui lit : `data.txt [NEW]`

![Création d'un nouveau fichier en utilisant la commande vim](https://cdn.hashnode.com/res/hashnode/image/upload/v1736790675984/98007e6c-cc90-42be-b853-f239f4f2e819.png align="center")

Si le fichier que vous souhaitez éditer existe déjà, vous pouvez l'ouvrir dans Vim en utilisant la même commande. Vous pourrez voir son contenu et faire des modifications si nécessaire. Si vous ne voyez pas le message `[New]` en bas (comme montré pour les nouveaux fichiers), cela confirme que le fichier existe déjà.

## Les modes dans Vim

Vim a plusieurs modes, mais les plus couramment utilisés sont :

* **Mode Normal (Mode Commande)** – Utilisé pour la navigation et l'exécution de commandes.

* **Mode Insertion** – Utilisé pour taper et éditer du texte.

Lorsque vous ouvrez un fichier dans Vim, il démarre en Mode Commande par défaut. Ce mode vous permet de naviguer, d'exécuter des commandes et de effectuer diverses opérations sans modifier directement le texte. Pour éditer le texte dans le fichier, vous devez passer en Mode Insertion.

### **Qu'est-ce que le Mode Commande ?**

Le Mode Commande est le mode par défaut dans Vim. Dans ce mode, vous pouvez naviguer dans le fichier en utilisant les touches fléchées et couper, copier, coller ou supprimer le contenu et exécuter des commandes comme sauvegarder ou quitter.

Pour passer en Mode Commande depuis n'importe quel autre mode, appuyez sur la touche `Esc`.

Exemple : Si vous êtes en Mode Insertion et que vous devez revenir en Mode Commande pour sauvegarder ou naviguer, appuyez sur `Esc`.

![Vim en mode commande](https://cdn.hashnode.com/res/hashnode/image/upload/v1736791773096/298ef4f6-6fba-493d-b05c-0564290862a1.png align="center")

Dans l'image ci-dessus, "hello.txt" 1L, 1B" indique que le fichier `hello.txt` est ouvert et est actuellement en Mode Commande, qui est le mode par défaut lorsque vous ouvrez Vim. 1L Représente 1 ligne dans le fichier (actuellement le fichier est vide, donc il n'y a qu'une seule ligne vide). 1B Représente 1 octet (le fichier est actuellement vide)

### **Qu'est-ce que le Mode Insertion ?**

Le Mode Insertion vous permet d'éditer ou de taper du texte dans le fichier, similaire à un éditeur de texte traditionnel. Vous pouvez insérer de nouvelles lignes, modifier le texte existant et apporter des modifications directement.

Appuyez sur `i` lorsque vous êtes en Mode Commande. Cela passe en Mode Insertion et place le curseur à la position actuelle, vous permettant de commencer à taper.

![Éditeur passé en mode INSERTION](https://cdn.hashnode.com/res/hashnode/image/upload/v1736791793215/93d1ff39-9015-4209-8903-e29d1ccfb7c1.png align="center")

Dans l'image ci-dessus, "—INSERT—" indique que l'éditeur a été passé en Mode Insertion, vous permettant de taper et d'éditer du texte directement dans le fichier.

Coup d'œil rapide : Lorsque vous ouvrez un fichier, vérifiez toujours le bas du terminal pour déterminer votre mode actuel. Si la ligne du bas affiche des informations relatives au fichier, vous êtes en Mode Commande. Si la ligne du bas dit explicitement "-- INSERT --", vous êtes en Mode Insertion. Si vous voulez passer du **Mode Commande au Mode Insertion** : Appuyez sur `i`. Et du **Mode Insertion au Mode Commande** : Appuyez sur `Esc`.

## Commandes de base de Vim

Voici quelques commandes essentielles pour vous aider à gérer les fichiers efficacement dans Vim.

**Remarque :** Avant d'utiliser ces commandes, assurez-vous d'être en mode commande en appuyant sur `Esc`.

### **1. Sauvegarder les modifications**

Pour sauvegarder les modifications apportées à un fichier, utilisez la commande suivante :

```bash
:w
```

Cela écrit (sauvegarde) le fichier actuel sans quitter Vim.

### **2. Sauvegarder les modifications et quitter**

Si vous avez terminé l'édition et que vous souhaitez sauvegarder les modifications et quitter Vim simultanément, utilisez :

```bash
:wq
```

Cette commande écrit les modifications puis quitte l'éditeur.

### **3. Quitter sans sauvegarder les modifications**

Si vous souhaitez quitter sans sauvegarder aucune modification, vous pouvez utiliser :

```bash
:q
```

Cette commande fermera le fichier si aucune modification n'a été apportée depuis la dernière sauvegarde.

### **4. Forcer la sortie sans sauvegarder les modifications**

Au cas où vous auriez apporté des modifications au fichier mais que vous souhaitez quitter sans les sauvegarder, vous pouvez forcer la sortie avec :

```bash
:q!
```

Le `!` remplace toute modification non sauvegardée et ferme le fichier immédiatement.

## **Commandes de coupe, copie, collage et suppression (et autres)**

### **Comment positionner le curseur pour la manipulation de texte**

Avant d'utiliser l'une des commandes listées ci-dessous (copier, couper, coller et supprimer), il est important de comprendre où placer le curseur.

* **Copier (Yank), Couper, Supprimer :** Pour la plupart des opérations, le curseur doit être placé **au point de départ du texte** sur lequel vous souhaitez agir. Cela signifie que si vous copiez ou coupez un mot, placez le curseur au **début** du mot. Si vous travaillez avec une ligne, le curseur doit être n'importe où sur cette ligne. Pour les opérations basées sur des paragraphes, positionnez le curseur n'importe où dans le paragraphe.

* **Coller :** Le texte sera collé à la **position actuelle du curseur**. Assurez-vous donc que votre curseur est placé où vous voulez que le contenu copié ou coupé apparaisse.

Par exemple, disons que j'ai un fichier.txt qui a le contenu suivant -

```bash
# fichier.txt
Hey lecteurs,  
Dans ce blog, nous apprenons Vim. Ce fichier est à des fins de démonstration,
où nous explorerons diverses commandes d'édition comme couper, copier, coller et supprimer. Plongeons-nous !  

Vim est un puissant éditeur de texte qui est préinstallé sur la plupart des systèmes basés sur Unix.
Maîtriser Vim peut considérablement augmenter votre efficacité en tant que développeur.  

Pour commencer, apprenons quelques commandes de navigation de base et de manipulation de texte.
Restez à l'écoute alors que nous décomposons chaque commande avec des exemples !  
```

Toutes les commandes mentionnées ci-dessous utiliseront ce fichier comme référence pour expliquer les exemples.

### **1. Copier (Yank)**

Dans Vim, copier s'appelle "yanking". Utilisez les commandes suivantes pour copier du texte. La position du curseur est importante pour s'assurer que le texte correct est copié.

| Commande | Description | Exemple |
| --- | --- | --- |
| `yl` | Copie une lettre à partir de la position actuelle du curseur (le curseur doit être à gauche de la lettre que vous souhaitez copier) | Si votre curseur est à gauche de **"H"** dans `Hey lecteurs,` et que vous tapez `yl`, Vim copiera **"H"** (un seul caractère). |
| `yw` | Copie un mot (le curseur doit être au début du mot) | Si votre curseur est à gauche de **"blog,"** dans la phrase, taper `yw` copiera **"blog,"** (y compris la virgule). |
| `yy` | Copie la ligne entière (le curseur peut être n'importe où sur la ligne) | Si votre curseur est à n'importe quelle position sur la ligne 1 **Hey lecteurs,** taper `yy` copiera la ligne entière |
| `2yy` | Copie deux lignes, y compris la ligne actuelle du curseur (le curseur peut être n'importe où sur la première ligne) | Si votre curseur est à n'importe quelle position sur la ligne 1 **Hey lecteurs,** taper `2yy` copiera la ligne entière ainsi que la ligne suivante. |
| `y{` | Copie le reste du paragraphe au-dessus de la ligne où se trouve actuellement le curseur (et y compris cette ligne) | Si votre curseur est n'importe où à l'intérieur de ce paragraphe 2 (Vim est un puissant éditeur de texte…), taper `y{` copiera tout depuis le début de ce paragraphe jusqu'à la position du curseur. |
| `y}` | Copie le reste du paragraphe en dessous de la ligne où se trouve actuellement le curseur (et y compris cette ligne) | Si votre curseur est n'importe où à l'intérieur de ce paragraphe 2 (Vim est un puissant éditeur de texte…), taper `y}` copiera tout depuis la position actuelle du curseur jusqu'à la fin du paragraphe. |
| `yG` | Copie tout depuis la ligne actuelle jusqu'à la fin du fichier (le curseur doit être à la ligne où vous souhaitez que l'opération de copie commence) | Si votre curseur est au début de cette ligne « **Vim est un puissant éditeur de texte…** », taper yG copiera cette ligne et tout ce qui se trouve en dessous jusqu'à la fin du fichier |

### **2. Couper (Changer)**

Couper dans Vim est connu sous le nom de « changer » le texte. L'opération de coupe remplace le texte. Tout comme pour la copie, la position du curseur est importante lors de l'utilisation des commandes de coupe.

| Commande | Description | Exemple |
| --- | --- | --- |
| `cl` | Coupe une lettre à partir de la position actuelle du curseur (le curseur doit être à gauche de la lettre que vous souhaitez couper) | Si votre curseur est sur le **"H"** dans `"Hey lecteurs,"` et que vous tapez `cl`, Vim supprimera **"H"** et passera en mode insertion, vous permettant de taper un remplacement. |
| `cw` | Coupe un mot (le curseur doit être au début du mot) | Si votre curseur est sur **"blog,"** dans la phrase, taper `cw` supprimera **"blog,"** (y compris la virgule) et passera en mode insertion, vous permettant de taper un remplacement. |
| `caw` | Coupe un mot ainsi que les espaces de fin (le curseur doit être au début du mot) | Si votre curseur est n'importe où à l'intérieur de **"blog,"**, taper `caw` supprimera **" blog,"** (y compris l'espace précédent) et passera en mode insertion. |
| `cc` | Coupe la ligne entière (le curseur peut être n'importe où sur la ligne) | Si votre curseur est à n'importe quelle position sur la ligne 1 (`Hey lecteurs,`), taper `cc` supprimera toute la ligne et passera en mode insertion. |
| `2cc` | Coupe deux lignes, y compris la ligne actuelle du curseur (le curseur peut être n'importe où sur la première ligne) | Si votre curseur est à n'importe quelle position sur la ligne 1 (`Hey lecteurs,`), taper `2cc` supprimera cette ligne ainsi que la ligne suivante et passera en mode insertion. |
| `c{` | Coupe le texte dans le paragraphe au-dessus de l'emplacement du curseur | Si votre curseur est n'importe où à l'intérieur du paragraphe 2 (`Vim est un puissant éditeur de texte…`), taper `c{` supprimera tout depuis la position du curseur jusqu'au début du paragraphe et passera en mode insertion. |
| `c}` | Coupe le texte dans les paragraphes en dessous de l'emplacement du curseur | Si votre curseur est n'importe où à l'intérieur du paragraphe 2 (`Vim est un puissant éditeur de texte…`), taper `c}` supprimera tout depuis la position du curseur jusqu'à la fin du paragraphe et passera en mode insertion. |
| `cG` | Coupe tout depuis la ligne actuelle jusqu'à la fin du fichier (le curseur doit être à la ligne où vous souhaitez que l'opération de coupe commence) | Si votre curseur est au début de cette ligne (`Vim est un puissant éditeur de texte…`), taper `cG` supprimera cette ligne et tout ce qui se trouve en dessous jusqu'à la fin du fichier, puis passera en mode insertion. |

### **3. Coller**

Pour coller le texte copié ou coupé, utilisez les commandes suivantes. Le texte collé apparaîtra à la **position actuelle du curseur**.

| Commande | Description |
| --- | --- |
| `p` (Minuscule) | Colle le texte copié ou coupé **après** le curseur |
| `P` (Majuscule) | Colle le texte copié ou coupé **avant** le curseur |

### **4. Supprimer**

Supprimer du texte dans Vim vous permet de retirer le texte indésirable tout en restant en mode commande. Le curseur doit être positionné correctement pour supprimer le texte prévu. Une fois supprimé, vous pouvez toujours coller le texte supprimé à un nouvel emplacement.

| Commande | Description | Exemple |
| --- | --- | --- |
| `dl` | Supprime une lettre à partir de la position actuelle du curseur (le curseur doit être à gauche de la lettre que vous souhaitez supprimer) | Si votre curseur est sur **"H"** dans `"Hey lecteurs,"` et que vous tapez `dl`, Vim supprimera **"H"**. |
| `dw` | Supprime un mot (le curseur doit être au début du mot) | Si votre curseur est sur **"blog,"** dans la phrase, taper `dw` supprimera **"blog,"** (y compris la virgule). |
| `daw` | Supprime un mot ainsi que les espaces de fin (le curseur doit être au début du mot) | Si votre curseur est n'importe où à l'intérieur de **"blog,"**, taper `daw` supprimera **" blog,"** (y compris l'espace précédent). |
| `dd` | Supprime la ligne entière (le curseur peut être n'importe où sur la ligne) | Si votre curseur est à n'importe quelle position sur la ligne 1 (`Hey lecteurs,`), taper `dd` supprimera toute la ligne. |
| `2dd` | Supprime deux lignes, y compris la ligne actuelle du curseur (le curseur peut être n'importe où sur la première ligne) | Si votre curseur est à n'importe quelle position sur la ligne 1 (`Hey lecteurs,`), taper `2dd` supprimera cette ligne ainsi que la ligne suivante. |
| `d{` | Supprime le paragraphe au-dessus du curseur (le curseur peut être n'importe où dans le paragraphe que vous souhaitez supprimer) | Si votre curseur est n'importe où à l'intérieur du paragraphe 2 (`Vim est un puissant éditeur de texte…`), taper `d{` supprimera tout depuis la position du curseur jusqu'au début du paragraphe. |
| `d}` | Supprime le paragraphe en dessous du curseur (le curseur peut être n'importe où dans le paragraphe que vous souhaitez supprimer) | Si votre curseur est n'importe où à l'intérieur du paragraphe 2 (`Vim est un puissant éditeur de texte…`), taper `d}` supprimera tout depuis la position du curseur jusqu'à la fin du paragraphe. |
| `dG` | Supprime tout depuis la ligne actuelle jusqu'à la fin du fichier (le curseur doit être à la ligne où vous souhaitez que l'opération de suppression commence) | Si votre curseur est au début de cette ligne (`Vim est un puissant éditeur de texte…`), taper `dG` supprimera cette ligne et tout ce qui se trouve en dessous jusqu'à la fin du fichier. |

### **5. Autres commandes utiles**

| Commandes | Description |
| --- | --- |
| `gg` | Déplace le curseur à la première ligne du fichier |
| `G` | Déplace le curseur à la dernière ligne du fichier |
| `:se nu` | Affiche les numéros de ligne dans le fichier |
| `:se nonu` | Supprime les numéros de ligne du fichier |
| `:u` | Annule la dernière action |
| `:10` | Saute à la ligne 10 (par exemple) |

Notez que **Supprimer** retire le texte mais ne le stocke pas dans le presse-papiers du système par défaut. Le texte va dans le registre sans nom de Vim, ce qui signifie qu'il peut être collé dans Vim mais pas en dehors. **Couper** stocke explicitement le texte dans le presse-papiers afin que vous puissiez le coller en dehors de Vim également.

## **Commandes de recherche et de remplacement**

Vim fournit une fonctionnalité puissante de recherche et de remplacement qui vous permet de trouver des mots ou des motifs spécifiques et de les remplacer efficacement. Comprendre comment rechercher et remplacer du texte est la clé pour améliorer votre productivité lors de l'édition de grands fichiers.

Voici une ventilation des différentes commandes de recherche et de remplacement dans Vim.

### **Commandes de recherche**

* **Recherche vers l'avant** (`/`): Lorsque vous souhaitez rechercher un mot ou un motif en dessous du curseur, utilisez la commande `/`. Cela recherchera vers l'avant dans le fichier.

* **Recherche vers l'arrière** (`?`): De même, si vous souhaitez rechercher un mot ou un motif au-dessus du curseur, utilisez la commande `?`. Cela recherchera vers l'arrière dans le fichier.

Après avoir effectué une recherche, vous pouvez naviguer à travers les résultats de la recherche :

* `n`: Aller à la correspondance suivante dans la même direction (vers l'avant si `/`, vers l'arrière si `?`).

* `N`: Aller à la correspondance précédente dans la direction opposée (vers l'arrière si `/`, vers l'avant si `?`).

### **Commandes de remplacement**

Une fois que vous avez localisé le mot ou le motif que vous souhaitez remplacer, Vim fournit plusieurs commandes pour remplacer le texte.

| Commande (En mode commande) | Description |
| --- | --- |
| `/mot_recherche` | Recherche le mot donné et déplace le curseur à sa première occurrence en dessous de la position actuelle du curseur. |
| `:s/mot_recherche/mot_remplacement` | Remplace la première occurrence de `mot_recherche` par `mot_remplacement` dans la ligne actuelle. |
| `:s/mot_recherche/mot_remplacement/g` | Remplace toutes les occurrences de `mot_recherche` par `mot_remplacement` dans la ligne actuelle. |
| `:%s/mot_recherche/mot_remplacement` | Remplace la première occurrence de `mot_recherche` par `mot_remplacement` dans l'ensemble du fichier. |
| `:%s/mot_recherche/mot_remplacement/g` | Remplace toutes les occurrences de `mot_recherche` par `mot_remplacement` dans l'ensemble du fichier. |

Voici un exemple :

Dans Vim, le motif `/Tanishka` recherche une correspondance exacte, sensible à la casse, du mot "Tanishka."

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736795075490/1ecbc6f4-65ef-46a9-841d-dbb3251f8ec7.png align="center")

Pour remplacer "Tanishka" par un autre mot, comme "Linux," vous pouvez utiliser la commande de substitution comme ceci : `:s/Tanishka/Linux`:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736794982127/c9dffdba-c250-4601-8e3b-950d875908f8.png align="center")

Par défaut, cette commande remplace uniquement la première occurrence de "Tanishka" dans la ligne où se trouve le curseur.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736794997175/9831423d-4aab-43a1-9b06-408fb5dd4828.png align="center")

Si vous souhaitez remplacer toutes les occurrences de "Tanishka" dans la même ligne, vous devez ajouter le drapeau `g` (global) après la chaîne de remplacement comme ceci : `:s/Tanishka/Linux/g`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736795009744/c53d0de2-b7b4-4154-baaa-3d28fb3c29db.png align="center")

Cela garantit que chaque instance de "Tanishka" dans la ligne actuelle est remplacée par "Linux."

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736795017539/dac817e5-8130-44d4-8f09-d887e42cc859.png align="center")

De même, le symbole `%` est utilisé pour spécifier **l'ensemble du fichier** lors de l'exécution d'une substitution. Voici comment cela fonctionne en combinaison avec la commande de substitution :

1. **Remplacer la première occurrence dans chaque ligne du fichier :**

   * `:%s/Tanishka/Linux`: Cette commande remplace uniquement la première occurrence de "Tanishka" dans chaque ligne du fichier.

2. **Remplacer toutes les occurrences dans l'ensemble du fichier :**

   * `:%s/Tanishka/Linux/g`: L'ajout du drapeau `g` (global) garantit que toutes les occurrences de "Tanishka" dans chaque ligne du fichier sont remplacées par "Linux."

## **Comment lire des fichiers en utilisant** `more` **et** `less`

### La commande `cat`

La commande cat est souvent utilisée pour lire le contenu d'un fichier.

Par exemple :

```bash
cat fichier.txt # Affiche le contenu du fichier
```

Bien que la commande `cat` soit un outil simple pour afficher le contenu des fichiers, sa simplicité est souvent insuffisante lors de la manipulation de grands fichiers ou lorsque la navigation précise est requise. C'est là que les commandes `more` et `less` entrent en jeu, offrant une fonctionnalité améliorée pour afficher et naviguer dans le texte efficacement.

### La commande `more`

La commande `more` vous permet de visualiser les fichiers une page à la fois, ce qui en fait une amélioration significative par rapport à `cat` lors de la manipulation de grands fichiers. Mais elle présente des limitations en termes de navigation en arrière et de fonctionnalités avancées.

Voici la syntaxe pour `more`:

```bash
more [NOM_DU_FICHIER]
```

Et voici un exemple :

```bash
more fichier.txt # Affiche le contenu de fichier.txt une page à la fois
```

Touches utilisées lors de la visualisation :

1. Barre d'espace : Avance d'une page

2. Entrée : Avance d'une ligne

3. b : Recule d'une page

4. q : Quitte et ferme le contenu du fichier

### La commande `less`

La commande `less` est souvent considérée comme une alternative supérieure à `more` grâce à ses capacités de navigation avancées et sa flexibilité. Contrairement à `more`, `less` permet la navigation à la fois vers l'avant et vers l'arrière, ce qui la rend idéale pour examiner de grands fichiers ou des journaux.

Voici sa syntaxe :

```bash
less [NOM_DU_FICHIER]
```

Et voici un exemple :

```bash
less fichier.txt # Affiche le contenu de fichier.txt une page à la fois
```

Touches utilisées lors de la visualisation :

1. Barre d'espace : Avance d'une page

2. Entrée : Avance d'une ligne

3. b : Recule d'une page

4. Touche fléchée Haut/Bas : Monte ou descend d'une ligne

5. q : Quitte et ferme less

La seule différence majeure entre les commandes `more` et `less` est que la commande less permet une navigation bidirectionnelle, donc elle est généralement plus pratique à utiliser.

## **Filtres de texte**

Un **filtre de texte** sous Linux est un utilitaire en ligne de commande qui traite les données textuelles en les modifiant, en les extrayant ou en les formatant avant de produire le résultat.

### Filtres horizontaux

Le filtrage horizontal se concentre sur l'extraction, la manipulation ou l'affichage de lignes spécifiques d'un fichier ou de la sortie d'une commande. Les outils courants incluent `head`, `tail` et `grep`.

1. `head` : La commande head affiche les premières lignes d'un fichier. Par défaut, elle montre les 10 premières lignes. Voici sa syntaxe :

   ```bash
   head [OPTIONS] [NOM_DU_FICHIER]
   ```

   Et voici un exemple de son utilisation :

   ```bash
   head fichier.txt # Affiche les dix premières lignes de fichier.txt
   head -n 5 fichier.txt # Affiche les cinq premières lignes de fichier.txt
   ```

2. `tail` : La commande tail affiche les dernières lignes d'un fichier. Par défaut, elle montre les 10 dernières lignes. Voici sa syntaxe :

   ```bash
   tail [OPTIONS] [NOM_DU_FICHIER] 
   ```

   Et voici un exemple :

   ```bash
   tail fichier.txt # Affiche les dix dernières lignes de fichier.txt
   tail -n 5 fichier.txt # Affiche les cinq dernières lignes de fichier.txt
   ```

3. `grep` : La commande grep recherche des motifs dans un fichier ou une entrée. Elle filtre les lignes qui correspondent à un motif donné. Voici sa syntaxe :

   ```bash
   grep [OPTIONS] [MOTIF] [NOM_DU_FICHIER]
   ```

   Options :

   * `-i` : Recherche insensible à la casse.

   * `-v` : Inverse la correspondance (exclut les lignes correspondantes).

   * `-n` : Affiche les numéros de ligne des correspondances.

   Exemple

   ```bash
   grep Tanishka data.txt # Affiche les lignes qui contiennent 'Tanishka'
   grep -i Tanishka data.txt # Affiche les lignes qui contiennent 'Tanishka' indépendamment de la casse
   grep -v Tanishka data.txt # Affiche les lignes qui ne contiennent pas 'Tanishka'
   grep -n Tanishka data.txt # Affiche les lignes qui contiennent 'Tanishka' ainsi que le numéro de ligne
   ```

### Filtres verticaux

1. `cut` : La commande cut affiche des parties sélectionnées des lignes de chaque fichier en fonction de délimiteurs, de positions d'octets ou de champs de caractères. Voici sa syntaxe :

   ```bash
   cut [OPTION] [NOM_DU_FICHIER]
   ```

   Elle vient également avec diverses options :

   * `-c` : Extrait des caractères spécifiques.

   * `-b` : Extrait des octets spécifiques.

   * `-d` : Spécifie un délimiteur personnalisé (par défaut, c'est la tabulation).

   * `cut -d ":" -f 2 fichier.txt` → Deuxième champ séparé par `:`.

   * `-f` : Extrait des champs spécifiques.

   * `cut -d "," -f 1,3 fichier.csv` → Champs 1 et 3 d'un CSV.

   Exemple :

   ```bash
   cut -c 1-10 Sample.txt # Affiche les caractères des positions 1 à 10
   cut -c 5 Sample.txt # Affiche le caractère à la position 5
   cut -c 3,5 Sample.txt # Affiche les caractères des positions 3 et 5 uniquement
   cut -d " " -f 1 Sample.txt # Affiche le premier champ séparé par un espace
   cut -d " " -f 2 Sample.txt # Affiche le deuxième champ séparé par un espace
   cut -d " " -f 3 Sample.txt # Affiche le troisième champ séparé par un espace
   cut -d " " -f 1-3 Sample.txt # Affiche les premier à troisième champs séparés par un espace
   cut -d " " -f 1,3 Sample.txt # Affiche les premier et troisième champs séparés par un espace
   cut -d ":" -f 5 /etc/passwd # Affiche le cinquième champ séparé par : dans /etc/passwd
   ```

## **Outil de résumé de texte :** `wc`

La commande `wc` (word count) est utilisée pour afficher le nombre de lignes, de mots, de caractères ou d'octets dans un fichier ou une entrée. C'est un utilitaire simple mais puissant que vous pouvez utiliser pour résumer le contenu textuel.

Voici sa syntaxe :

```bash
wc [OPTION] [NOM_DU_FICHIER]
```

Et voici ses options :

* `-l` : Affiche le nombre de lignes.

* `-w` : Affiche le nombre de mots.

* `-c` : Affiche le nombre d'octets.

* `-m` : Affiche le nombre de caractères (utile pour les caractères multioctets).

* `-L` : Affiche la longueur de la ligne la plus longue.

Exemple :

```bash
wc Sample.txt # Affiche le nombre de lignes, le nombre de mots et le nombre d'octets dans Sample.txt
wc -w Sample.txt # Affiche le nombre de mots dans Sample.txt
wc -l Sample.txt # Affiche le nombre de lignes dans Sample.txt
wc -L Sample.txt # Affiche le nombre de caractères dans la ligne la plus longue de Sample.txt

wc -c Sample.txt # Affiche le nombre d'octets dans Sample.txt (Taille de stockage réelle)
wc -m Sample.txt # Affiche le nombre de caractères dans Sample.txt (Nombre réel de caractères indépendamment de l'encodage)

# ABCD\ud83d\ude04
wc -c above.txt # "ABCD" = 4 octets + "\ud83d\ude04" = 4 octets. 4 + 4 = 8 octets
wc -m above.txt # "ABC" = 4 + "\ud83d\ude04" = 1 octet. 4 + 1 = 5 octets
```

## Mots de la fin

Dans cet article, nous avons couvert les bases de l'utilisation de Vim, un éditeur de texte puissant et flexible. Nous avons commencé par la manière d'ouvrir un fichier dans Vim, puis vous avez appris ses modes. Vous avez également appris à naviguer dans les fichiers, à éditer du texte et à utiliser des fonctionnalités comme la recherche et le remplacement pour gagner du temps. Nous avons également exploré un outil de résumé utile.

Si vous êtes nouveau sous Linux et que vous souhaitez construire une base solide, consultez [mon article précédent](https://www.freecodecamp.org/news/guide-to-rhel-linux-basics/) où je couvre les bases de Linux, y compris les commandes essentielles et les conseils pour les débutants. C'est un point de départ parfait pour compléter ce que vous avez appris sur Vim ici !

Continuez à pratiquer ces commandes, et bientôt elles deviendront une seconde nature pour vous. La maîtrise vient avec la répétition, alors continuez à expérimenter et à appliquer ces fondamentaux dans des scénarios réels.

Restez à l'écoute pour plus d'articles. Préparez-vous à faire passer vos compétences RHEL au niveau supérieur.

[Connectons-nous !](https://linktr.ee/tanishkamakode)
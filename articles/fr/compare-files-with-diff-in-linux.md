---
title: Linux diff – Comment comparer deux fichiers et appliquer des modifications
  avec la commande Patch
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-09-15T21:01:00.000Z'
originalURL: https://freecodecamp.org/news/compare-files-with-diff-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Compare-files-in-Linux-with-diff.png
tags:
- name: Linux
  slug: linux
- name: version control
  slug: version-control
seo_title: Linux diff – Comment comparer deux fichiers et appliquer des modifications
  avec la commande Patch
seo_desc: "Imagine waking up one day to find out that your production systems are\
  \ down because of a bug that has yet to be traced. One of your worst nightmares\
  \ right? \nAnd you also discover that you need to compare code from two versions\
  \ and the pressure is bui..."
---

Imaginez-vous vous réveiller un jour pour découvrir que vos systèmes de production sont en panne à cause d'un bug qui n'a pas encore été tracé. Un de vos pires cauchemars, n'est-ce pas ?

Et vous découvrez également que vous devez comparer le code de deux versions et la pression monte pour restaurer les systèmes. Tout le monde panique et c'est totalement légitime !

Heureusement, il existe un utilitaire Linux appelé `diff` qui vous couvre.

## Qu'est-ce que la commande `diff` dans Linux ?

Comparer des fichiers et trouver les différences entre eux est une opération largement utilisée. Cela est particulièrement utile lorsque vous devez comparer des codes complexes ou des fichiers de configuration.

Au lieu de comparer manuellement (ce qui a une forte chance d'erreur humaine), Linux vous offre un utilitaire intégré et puissant appelé `diff`. Cela permet également de gagner du temps.

Pour compléter les commandes diff, Linux fournit également une autre commande pour appliquer des modifications d'un fichier à un autre appelée `patch`. Dans cet article, nous allons examiner ces commandes intéressantes et polyvalentes pour voir comment les utiliser.

## Syntaxe de la commande `diff`

La syntaxe de `diff` est partagée ci-dessous :

```bash
diff [options] fichier1 fichier2
```

La commande diff peut afficher trois caractères basés sur les modifications :

<table>
<thead>
<tr>
<th>Caractère</th>
<th>Signification</th>
</tr>
</thead>
<tbody>
<tr>
<td>c</td>
<td>CHANGEMENT - Un changement doit être effectué.</td>
</tr>
<tr>
<td>d</td>
<td>SUPPRESSION - Quelque chose doit être supprimé.</td>
</tr>
<tr>
<td>a</td>
<td>AJOUT - Quelque chose doit être ajouté.</td>
</tr>
</tbody>
</table>

Dans la sortie de la commande `diff`, le symbole `<` pointe vers le premier fichier et le symbole `>` pointe vers le second fichier qui est utilisé comme référence.

Regardons quelques exemples de la commande `diff` en utilisation.

### Exemples de la commande Linux `diff`

Pour indiquer que les fichiers sont identiques, nous utilisons le flag `-s` avec `diff`. Dans notre exemple, les deux fichiers fileA et sameAsfileA contiennent le même contenu.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-63.png)

Dans l'exemple suivant, il y a deux fichiers qui n'ont pas le même contenu. Dans la sortie mise en évidence ci-dessous, la commande `diff` montre que les lignes 11 et 14 dans showList_v2.js doivent être modifiées pour correspondre aux lignes 11 et 13 dans showList_v1.js.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-64.png)

La prochaine façon dont vous pouvez utiliser diff est ma préférée, car vous pouvez voir les différences côte à côte.

Il suffit d'utiliser le flag `-y` comme ceci :

```bash
diff -y fichier1 fichier2
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-50.png)
_Comparer les fichiers côte à côte_

Le dernier exemple que je vais discuter est la sortie unifiée. Cette sortie est souvent utilisée comme entrée pour la commande `patch`. Nous verrons également comment fonctionne la commande patch :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-67.png)
_Sortie unifiée, utilisée comme entrée pour patch._

Voici quelques autres flags utiles que vous pouvez utiliser avec `diff`.

* `-i` pour ignorer la casse. `diff` est sensible à la casse par défaut.
* `-w` pour ignorer les espaces dans un fichier. Par défaut, les espaces sont considérés comme une différence.

## Syntaxe de la commande `patch`

Les modifications se produisent tout le temps dans votre code, et il est irréaliste et chronophage de partager des fichiers modifiés et corrigés pour chaque changement. Habituellement, les développeurs partagent les corrections dans le code avec l'équipe afin qu'elles soient appliquées instantanément.

Et utiliser des patches est la méthode la plus sûre pour distribuer uniquement les améliorations.

Voyons comment fonctionne le patching :

```bash
patch fichier_a_modifier < fichier_patch
```

### Exemples de la commande Linux `patch`

Voici un exemple de patching : supposons que nous avons un simple code JavaScript [nom du fichier : print_in_js.js] qui imprime une chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-68.png)

Cependant, il y a quelque chose qui ne va pas dans la fonction d'impression et nous avons besoin d'une correction pour cela. Nous envoyons le fichier print_in_js.js à notre collègue qui corrige le code et nous le renvoie.

Tout d'abord, notre collègue est en mesure de trouver une erreur à la ligne #3. Ils corrigent le fichier.

Une fois le fichier corrigé et le code fonctionnel, ils créent un patch.

```bash
diff -u print_in_js.js  print_in_js_Fixed.js > patched_print_js.diff
```

Examinons le contenu du patch :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-69.png)
_contenu du patch_

Une fois que nous avons le patch, nous l'appliquons comme suit :

```bash
patch print_in_js.js  < patched_print_js.diff
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-72.png)
_Code corrigé après l'application du patch_

Et oui — notre code est corrigé !

## Conclusion

Il est relativement simple et direct de créer et d'appliquer des patches en utilisant `patch` et `diff`.

Une approche similaire fonctionne lorsque vous utilisez des systèmes de contrôle de version comme Git ou SVN. Apprendre les bases vous aide vraiment à comprendre comment fonctionne le contrôle de version, ce qui est un aspect important du développement logiciel.

Merci d'avoir lu jusqu'à la fin. J'adorerais entrer en contact avec vous. Vous pouvez me trouver [ici](https://twitter.com/hira_zaira) sur Twitter. N'hésitez pas à partager vos pensées.

À bientôt.
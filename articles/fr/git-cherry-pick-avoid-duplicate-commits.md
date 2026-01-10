---
title: Comment utiliser Git Cherry Pick et éviter les commits en double
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2024-01-03T21:33:29.000Z'
originalURL: https://freecodecamp.org/news/git-cherry-pick-avoid-duplicate-commits
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/blog-cover-for-git-cherry-pick.png
tags:
- name: Git
  slug: git
- name: open source
  slug: open-source
seo_title: Comment utiliser Git Cherry Pick et éviter les commits en double
seo_desc: "Imagine a beautiful cherry tree full of sweet, red, round fruit hanging\
  \ on lush, glistening branches. But imagine if those cherries grew so quickly that\
  \ the branches started bending, overlapping, and breaking...sounds chaotic right?\
  \ \nThis is what can..."
---

Imaginez un bel arbre cerisier rempli de fruits sucrés, rouges et ronds accrochés à des branches luxuriantes et brillantes. Mais imaginez si ces cerises poussaient si rapidement que les branches commençaient à se plier, à se chevaucher et à se casser... cela semble chaotique, n'est-ce pas ?

C'est ce qui peut arriver si vous n'utilisez pas correctement la commande `cherry-pick` de Git dans les projets open source. De manière similaire à la cueillette des plus belles cerises et à leur placement dans un panier, cette commande vous permet de déplacer des commits individuels d'une branche à une autre.

C'est idéal lorsque vous collaborez avec quelqu'un d'autre sur un projet open source, car cela vous évite d'avoir à fusionner des branches entières.

Maintenant, aussi puissante et formidable que soit la commande Git `cherry-pick`, elle peut créer des commits en double, rendant difficile pour les mainteneurs open source de mettre à jour la base de code de leur projet ou de résoudre des bugs.

Effrayé ? N'ayez crainte, mon cher contributeur open source. J'ai quelques stratégies que vous pouvez utiliser pour éviter les doublons lors de la sélection de commits.

## Stratégie 1 : Utiliser l'option `--no-commit`

Cette option est l'une des méthodes les plus courantes pour éviter les commits en double. Elle copie les modifications d'une branche mais ne crée pas de nouveau commit, ce qui peut être très utile si vous travaillez sur une contribution avec une autre personne. Voyons cela en action.

### Étape 1 : Choisissez votre cerise (commit)

Après avoir choisi le projet open source sur lequel vous et votre partenaire travaillez, allez sur leur fork et cliquez sur l'onglet **Commits**. 

![Image](https://www.freecodecamp.org/news/content/images/2023/12/commits-1.png)
_Capture d'écran de l'onglet d'une Pull Request. La section Commits est mise en évidence avec un ovale orange_

À partir de là, choisissez le commit que vous souhaitez mettre dans votre Pull Request en cliquant sur son numéro SHA. 

![Image](https://www.freecodecamp.org/news/content/images/2023/12/commit-sha.png)
_Capture d'écran de l'historique des commits. Le numéro SHA est affiché à droite, mis en évidence dans un ovale vert._

Comme vous pouvez le voir sur l'image, le numéro SHA est un identifiant unique qui contient les informations suivantes sur un commit :

* Le type de modifications apportées
* Quand les modifications ont été apportées
* Le contributeur qui a apporté les modifications

Après cela, collez le numéro SHA du commit choisi dans la commande suivante :

```git
git cherry-pick --no-commit <commit SHA number> 
```

### Étape 2 : Vérifiez les taches et plantez

Après avoir exécuté la commande `--no-commit`, il est maintenant temps d'inspecter votre commit sélectionné. Vous pouvez le faire en exécutant les commandes suivantes :

* `git diff` : Cette commande vous montre toutes les lignes ajoutées, supprimées ou modifiées par le commit sélectionné. Voici à quoi cela ressemblerait si quelqu'un faisait une contribution de traduction :

```git
git diff 2f410g1
diff --git a/01-intro.md b/01-intro.md
index 1234567890123456789012345678901234567890..0000000000000000000000000000000000000000
--- a/01-intro.md
+++ b/01-intro.md
@@ -1,3 +1,4 @@
- Hello, everyone!
+ Bonjour, tout le monde!
- Welcome to our course!
+ [Placeholder for French intro]
+ Bonjour, amis!


```

* `git show commit SHA` : Avec cette version de la commande `git show`, vous verrez le nom du contributeur, la date de son commit, son email et la liste des modifications qu'il a apportées. Si nous devions prendre le numéro SHA de l'exemple précédent et utiliser cette commande, voici à quoi ressemblerait la sortie :

```git
git show 2f410g1 (Frenchify intro and materials!)
Author: John (johnseed@example.com)
Date:   2023-12-18 18:07:15 -0500

Bonjour, le monde!  Time to add French translations to our intro and course materials.

* **01-intro.md:** Warm welcome and placeholder for the French translation.
* **materials.md:** Module descriptions replaced with [placeholders] for French versions.

... and other exciting French changes in 4 more files!
```

Maintenant que vous avez choisi votre méthode d'inspection, allez dans vos fichiers pour apporter les modifications et créer un message de commit comme indiqué ci-dessous.

```git
git commit -m <"message">
```

À partir de là, poussez les modifications dans la branche de votre Pull Request.

Maintenant, `--no-commit` n'est pas la seule stratégie que vous pouvez utiliser pour éviter les commits en double. Regardons une autre stratégie.

## Stratégie 2 : Faire des modifications avec `--edit`

Si vous savez quelles modifications vous souhaitez apporter au commit que vous avez sélectionné, alors la commande `--edit` est faite pour vous. Voici comment elle fonctionne :

```git
git cherry-pick -e 2f450g1
diff --git a/docs/content/pets.md b/docs/content/pets.md
index abcdef12..34567890 100644
--- a/docs/content/pets.md
+++ b/docs/content/pets.md
@@ -1,4 +1,5 @@
 # Pets
 
 This is a file about pets.
+New content added about pets.
 
 ## Different types of pets
# Continue cherry picking process
git cherry-pick --continue
# Change commit message
git commit -m "feat: add section"
```

Comme le montre l'extrait de code, nous avons initié une sélection interactive de cerises d'un commit contenant des modifications du fichier `pets.md`. Pendant le processus de sélection, vous pouvez apporter des modifications directes au fichier, y compris l'ajout de nouveau contenu et la modification de l'en-tête. À partir de là, nous avons créé un nouveau message de commit et poussé les modifications vers notre branche.

## Commencez à cueillir

Voilà, mes amis – des stratégies pour vous aider à éviter les commits en double lors de la sélection de cerises.

Utiliser cette commande efficacement non seulement facilite le travail sur les contributions collaboratives, mais garde également votre historique de commits propre.

Si vous souhaitez en savoir plus sur la sélection de commits et souhaitez mettre ces compétences en pratique, consultez [ce guide d'Atlassian](https://www.atlassian.com/git/tutorials/cherry-pick?source=post_page-----708ad5950460--------------------------------) et ce [cours d'OpenSauced](https://intro.opensauced.pizza/#/). Consultez également [BioDrop](https://www.biodrop.io/CBID2) pour voir mes autres contenus techniques et me contacter.

### Crédits

Image de l'historique des commits provenant de _[How to fix the order of commits in GitHub Pull Requests](https://andrewlock.net/how-to-fix-the-order-of-commits-in-github-pull-requests/)_ par Andrew Lock
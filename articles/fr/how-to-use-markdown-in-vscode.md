---
title: Comment utiliser Markdown dans VSCode - Syntaxe et exemples
subtitle: ''
author: Victoria (Burah) Poromon
co_authors: []
series: null
date: '2024-01-12T17:46:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-markdown-in-vscode
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Markdown-in-vscode-cover-photo.jpg
tags:
- name: markdown
  slug: markdown
- name: Visual Studio Code
  slug: vscode
seo_title: Comment utiliser Markdown dans VSCode - Syntaxe et exemples
seo_desc: 'Markdown is a lightweight markup language for creating formatted text using
  a plain-text editor. It is widely used for creating README files, documentation,
  and other forms of text.

  Visual Studio Code (VSCode) is a popular source code editor that pro...'
---

Markdown est un langage de balisage léger pour créer du texte formaté en utilisant un éditeur de texte brut. Il est largement utilisé pour créer des fichiers README, de la documentation et d'autres formes de texte.

Visual Studio Code (VSCode) est un éditeur de code source populaire qui offre un excellent support pour Markdown, facilitant ainsi l'utilisation efficace de Markdown pour les développeurs, les écrivains et toute personne créant du contenu textuel.

Pour suivre ce tutoriel, vous devez avoir VSCode installé sur votre ordinateur et savoir comment le naviguer.

## Importance de l'utilisation de Markdown dans Visual Studio Code (VSCode)

La combinaison de Markdown et VSCode offre un environnement convivial et efficace pour écrire, éditer et formater du texte, ce qui en fait un choix adapté pour les développeurs, les écrivains et les créateurs de contenu.

Voici quelques-unes des principales raisons d'utiliser Markdown dans VSCode :

* Markdown dans VSCode supporte les extraits de code et la coloration syntaxique pour divers langages de programmation, ce qui le rend adapté à la documentation de code et de contenu technique.
* VSCode fournit une fonctionnalité de prévisualisation intégrée à laquelle vous pouvez accéder en cliquant sur l'icône de prévisualisation en haut à droite de l'écran. Cela vous permet de voir votre fichier Markdown brut à côté de ce à quoi il ressemblera lorsque vous le publierez sur Internet. Cette fonctionnalité vous aide également à repérer et à corriger des erreurs simples au fur et à mesure.
* De nombreux dépôts de projets sur des plateformes comme GitHub utilisent Markdown pour la documentation. Se familiariser avec Markdown dans VSCode assure une transition fluide lors de la contribution à des projets open source ou de la collaboration avec des équipes utilisant des normes de documentation similaires.
* Vous n'avez pas besoin d'être connecté à Internet pour utiliser Markdown dans VSCode. Vous pouvez travailler hors ligne et avoir toujours accès à toutes ses fonctionnalités.
* Pour les développeurs, vous pouvez facilement pousser votre document vers GitHub en utilisant le terminal intégré de VSCode. Cela permet également à plusieurs personnes de réviser et de travailler sur le même document.

## Comment créer un fichier Markdown dans VSCode

Suivez les étapes ci-dessous pour créer votre fichier Markdown dans VSCode :

1. Créez un dossier sur votre ordinateur pour stocker vos documents.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot--17--1.png)
_Une image vous montrant comment créer un dossier sur la page de bureau de votre ordinateur. (Pour Windows)_

2. Lancez votre application VSCode.

3. Après avoir lancé votre application, cliquez sur 'Fichier', puis sur 'Ouvrir un dossier' pour ouvrir le dossier que vous venez de créer.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot--18-.png)
_Une image vous montrant comment ouvrir votre dossier à partir de l'application VSCode._

4. À l'intérieur de votre dossier, cliquez sur le symbole de fichier et créez un fichier qui se termine par '.md' (par exemple, Premier-fichier.md).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot--21--2.png)
_Une image vous montrant comment créer un fichier à l'intérieur de votre dossier dans VSCode._

5. Appuyez sur Entrée après avoir tapé le nom de votre fichier et votre page de document s'ouvrira. Vous êtes maintenant prêt et pouvez commencer à écrire.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot--22-.png)
_Une image montrant votre onglet de fichier et votre page de document._

## Syntaxe Markdown

La syntaxe Markdown est une collection de symboles/annotations que vous ajoutez à votre texte pour indiquer à chaque mot ou phrase ce qu'il doit faire.

Passons en revue certaines des syntaxes et fonctionnalités Markdown les plus utiles.

### En-têtes

Pour créer des en-têtes, ajoutez le symbole dièse (`#`) devant votre texte. Le nombre de symboles dièse détermine le niveau de l'en-tête.

Par exemple :

```markdown
 # En-tête 1
 ## En-tête 2
 ### En-tête 3
 #### En-tête 4
 ##### En-tête 5
 ###### En-tête 6
```

Résultat :

 # En-tête 1
 ## En-tête 2
 ### En-tête 3
 #### En-tête 4
 ##### En-tête 5
 ###### En-tête 6

### Listes

Il existe deux types de listes dans Markdown : la liste ordonnée et la liste non ordonnée. Pour créer une liste ordonnée, utilisez simplement des nombres suivis d'un point (comme `1.`). Pour créer une liste non ordonnée, ajoutez un astérisque, un signe plus ou un trait d'union devant votre texte (`*`, `+` ou `-`) et cela démarrera une liste non ordonnée.

Par exemple :

```markdown
Liste ordonnée
 1. Première liste
 2. Deuxième liste
    1. Sous-liste 2.1
    2. Sous-liste 2.2

 Liste non ordonnée
 * Liste 1
 * Liste 2
    + Sous-liste 1.2
    + Sous-liste 2.2
 - Élément a
 - Élément b
```

Résultat :

Liste ordonnée
 1. Première liste
 2. Deuxième liste
    1. Sous-liste 2.1
    2. Sous-liste 2.2

 Liste non ordonnée
 * Liste 1
 * Liste 2
    + Sous-liste 1.2
    + Sous-liste 2.2
 - Élément a
 - Élément b


### Code

Vous pouvez représenter du code de deux manières dans Markdown : en tant que code en ligne (comme `ceci`), et en tant que bloc de code (que vous verrez ci-dessous).

Pour créer du code en ligne, placez votre texte entre deux backticks (``), par exemple :

```markdown
`code en ligne`
```

Résultat :

`code en ligne`

Pour créer un bloc de code, encadrez votre code avec des triples backticks (```) au début et à la fin du bloc de code. Vous pouvez également spécifier le langage de programmation en ajoutant le nom du langage juste après les trois premiers backticks.

Voici un exemple :

```markdown
```
def exemple_bloc_code():
    print("Bonjour le monde !")
```
```

Résultat :

```
def exemple_bloc_code():
    print("Bonjour le monde !")
```

Voici un exemple de bloc de code en Python :

```python
```python
def exemple_bloc_code():
    print("Bonjour le monde !")
```    
```

Résultat :

```python
def exemple_bloc_code():
    print("Bonjour le monde !")
```    

### Tableaux

Vous pouvez créer un tableau en utilisant des pipes et des tirets (`|` et `-`). Les pipes divisent votre tableau en colonnes, tandis que les tirets créent une ligne horizontale.

Voici un exemple de création d'un tableau de base dans Markdown :

```markdown
| En-tête 1 | En-tête 2 | En-tête 3 | En-tête 4 |
| --------- | --------- | --------- | --------- |
| Ligne 1, Col 1 | Ligne 1, Col 2 | Ligne 1, Col 3 | Ligne 1, Col 4 |
| Ligne 2, Col 1 | Ligne 2, Col 2 | Ligne 2, Col 3 | Ligne 2, Col 4 |
```

Résultat :

| En-tête 1 | En-tête 2 | En-tête 3 | En-tête 4 |
| --------- | --------- | --------- | --------- |
| Ligne 1, Col 1 | Ligne 1, Col 2 | Ligne 1, Col 3 | Ligne 1, Col 4 |
| Ligne 2, Col 1 | Ligne 2, Col 2 | Ligne 2, Col 3 | Ligne 2, Col 4 |

### Citations

Le signe supérieur à (`>`) vous permet de créer une citation. Vous pouvez ajouter ce signe devant votre déclaration ou citation et il mettra en retrait et en italique la citation pour la distinguer du reste du texte.

Par exemple :

```markdown
> "La technologie que vous utilisez n'impressionne personne. L'expérience que vous créez avec elle est tout."
> Sean Gerety - Leader UX
```

Résultat :

> "La technologie que vous utilisez n'impressionne personne. L'expérience que vous créez avec elle est tout." 
> Sean Gerety - Leader UX

### Liens

Vous pouvez créer ou ajouter des liens à votre document en utilisant des crochets et des parenthèses (`[]` et `()`). Les crochets stockent le texte du lien, tandis que les parenthèses stockent l'URL du lien.

Par exemple :

```markdown
[freeCodeCamp](https://www.freecodecamp.org/news/)
```

Résultat :

[freeCodeCamp](https://www.freecodecamp.org/news/)

Le résultat est un lien cliquable qui vous mène au site de freeCodeCamp.

### Images

Ajouter des images à votre document est similaire à l'ajout de liens. La seule différence est que vous commencez par un point d'exclamation devant les crochets et les parenthèses.

Par exemple :

```markdown
![Une image de chat mignon](https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg?crop=1.00xw:0.753xh;0,0.153xh&resize=1200:*)
```

![Une image de chat mignon](https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg?crop=1.00xw:0.753xh;0,0.153xh&resize=1200:*)

Le résultat est l'image d'un chat.

### Emphase

Pour mettre en emphase du texte ou le mettre en italique, vous pouvez l'encadrer avec des astérisques simples (pour l'italique) ou doubles (pour le gras) ou des tirets bas (`*` ou `_`).

Par exemple :

```markdown
*italique* ou _italique_
**gras** ou __gras__
```

Résultat :

*italique* ou _italique_
**gras** ou __gras__

Comme vous pouvez le voir ci-dessus, un astérisque simple et un tiret bas donnent à votre texte une forme italique tandis qu'un double astérisque et un tiret bas rendent votre texte en gras.

### **Échappement des caractères**

Pour afficher des caractères littéraux dans la syntaxe Markdown, afin qu'ils apparaissent dans votre document sans les formater, vous devez les échapper en utilisant le backslash (`\`).

```
\_tiret bas littéral\_
```

Résultat :

\_tiret bas littéral\_

### HTML

Markdown supporte l'utilisation de balises HTML pour un formatage plus avancé lorsque cela est nécessaire.

Voici quelques-unes des manières dont vous pouvez utiliser les balises HTML dans Markdown :

* Images avec des attributs HTML

```markdown
<img src="image_url.jpg" alt="Texte alternatif" width="300" height="200">
```

L'attribut HTML dans la balise image vous permet de contrôler des propriétés comme la largeur et la hauteur de l'image.

* Style avec HTML et CSS

```markdown
<span style="color:green">Ceci est un texte vert.</span>
```

Résultat :

<span style="color:green">Ceci est un texte vert.</span>

Vous pouvez inclure des styles CSS en ligne pour un style plus avancé dans votre document.

* Intégration de vidéos

```markdown
<iframe width="500" height="300" src="https://www.nova.com/embed/example-video" frameborder="0" allowfullscreen></iframe>
```

Vous pouvez intégrer des vidéos dans votre document en utilisant la balise HTML iframe. Les attributs dans la balise vous permettent de contrôler les propriétés de la vidéo.

## Conclusion

Ce tutoriel vous a introduit à l'utilisation de Markdown dans VSCode. Vous avez appris comment initier un fichier Markdown dans VSCode, et vous avez vu quelques syntaxes Markdown courantes. J'espère que vous comprenez son importance pour les rédacteurs techniques et les créateurs de contenu.

La synergie entre Markdown et VSCode améliore non seulement la productivité, mais assure également une transition fluide vers le monde de la documentation standard.

Que vous écriviez de la documentation technique ou que vous contribuiez à des efforts de codage collaboratif, vous devriez maintenant être équipé d'un ensemble de compétences précieux pour vous aider à communiquer et à présenter vos idées de manière efficace.
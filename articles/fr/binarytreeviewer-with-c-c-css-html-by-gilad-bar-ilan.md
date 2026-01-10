---
title: Comment créer un BinaryTreeViewer en utilisant C#, CSS et HTML (Parcours du
  code et de l'algorithme)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-23T01:12:43.000Z'
originalURL: https://freecodecamp.org/news/binarytreeviewer-with-c-c-css-html-by-gilad-bar-ilan
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/BTViewerCoverImage.png
tags:
- name: algorithms
  slug: algorithms
- name: C
  slug: c
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Comment créer un BinaryTreeViewer en utilisant C#, CSS et HTML (Parcours
  du code et de l'algorithme)
seo_desc: 'By Gilad Bar Ilan

  Binary trees are one of the most complicated data structures out there. And one
  of the reasons they''re so difficult is that it''s hard to actually visualize them
  in a simple way.

  In this tutorial, I''ll show you how to create your own...'
---

Par Gilad Bar Ilan

Les arbres binaires sont l'une des structures de données les plus compliquées qui existent. Et l'une des raisons pour lesquelles ils sont si difficiles, c'est qu'il est difficile de les visualiser de manière simple.

Dans ce tutoriel, je vais vous montrer comment créer votre propre BinaryTreeViewer qui vous permettra de visualiser vos arbres à l'exécution.

Vous pouvez consulter le code source du projet ici : [https://github.com/giladbarilan/binary-tree-viewer](https://github.com/giladbarilan/binary-tree-viewer)

## Qu'est-ce que les arbres binaires ?

Les arbres binaires sont une structure de données très couramment utilisée basée sur des nœuds. Chaque nœud de l'arbre se compose de trois éléments :

* la valeur du nœud, 
* une référence au fils gauche (peut être null s'il n'a pas de fils gauche), 
* une référence au fils droit (peut être null s'il n'a pas de fils droit). 

Par exemple, supposons que nous avons un nœud avec la valeur 1 qui a un fils à gauche avec la valeur 3 et un fils à droite avec la valeur 2. Voici comment nous dessinerions le diagramme de l'arbre :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-53.png)

Un nœud peut avoir au plus deux enfants, mais il peut aussi en avoir un ou aucun. Lorsque nous voulons parcourir les éléments d'un arbre binaire, nous utilisons généralement des méthodes récursives (un exemple est montré ci-dessous).

Maintenant que nous savons comment fonctionne une structure de données d'arbre binaire, apprenons comment nous pouvons implémenter la structure d'arbre binaire en C#. 

```csharp
namespace BinaryTreeViewer
{
    /// <summary>
    /// Représente une classe d'arbre binaire utilisée pour le BinaryTreeViewer.
    /// </summary>
    /// <typeparam name="T">Le type de nœud de l'arbre.</typeparam>
    public partial class BinaryTree<T>
    {
        private BinaryTree<T>? rightNode; // nœud droit de l'arbre binaire.
        private BinaryTree<T>? leftNode; // nœud gauche de l'arbre binaire.
        public T value { get; set; } // la valeur du nœud actuel.

        public BinaryTree(T value)
        {
            this.value = value;
            this.rightNode = null;
            this.leftNode = null;
        }

        public BinaryTree(T value, BinaryTree<T>? left, BinaryTree<T>? right) : this(value)
        {
            this.rightNode = right;
            this.leftNode = left;
        }

        public void SetLeftNode(BinaryTree<T> node)
        {
            this.leftNode = node;
        }

        public void SetRightNode(BinaryTree<T> node)
        {
            this.rightNode = node;
        }

        public BinaryTree<T>? GetRightNode() => this.rightNode;
        public BinaryTree<T>? GetLeftNode() => this.leftNode;

        public override string? ToString() => this.value?.ToString();
    }
}
```

Dans le code ci-dessus, nous avons construit la structure de l'arbre binaire avec les 3 éléments dont nous avons parlé : la valeur, l'enfant droit et l'enfant gauche. Le point d'interrogation montre qu'ils sont nullable.

Faisons un exemple simple qui démontre comment imprimer tous les éléments d'un arbre binaire.

```csharp
//Construit l'arbre.

BinaryTree<int> tree2 = new BinaryTree<int>(1);
tree2.SetRightNode(new BinaryTree<int>(2));
tree2.GetRightNode().SetLeftNode(new BinaryTree<int>(4));
tree2.SetLeftNode(new BinaryTree<int>(3));
tree2.GetLeftNode().SetRightNode(new BinaryTree<int>(5));
PrintTree(tree2);

//Imprime l'arbre
public static void PrintTree<T>(BinaryTree<T> tree_)
{
    if (tree_.GetLeftNode() != null) //s'il a un enfant à gauche.
     PrintTree(tree_.GetLeftNode()); //va à la famille de l'enfant gauche.

    if (tree_.GetRightNode() != null) //s'il a un enfant à droite.
     PrintTree(tree_.GetRightNode()); //va à la famille de l'enfant droit.

    Console.WriteLine(tree_.value); //imprime la valeur actuelle.
}
```

## Algorithme de base des arbres binaires

Avant de passer à l'implémentation, il est bon de commencer par comprendre l'algorithme.

Revenons donc à notre exemple simple d'arbre :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-36.png)

À partir de cet exemple, nous pouvons comprendre les bases de la construction correcte de l'arbre. 

Tout d'abord, il est impossible de prédire combien de décalage nous devrons donner au nœud parent (afin qu'il y ait assez de place pour dessiner le nœud le plus à gauche de l'arbre). À cause de cela, nous devons d'abord trouver ce nœud le plus à gauche de l'arbre. 

Une fois que nous l'avons trouvé, nous comprendrons combien de décalage nous devons avoir à partir du parent de l'arbre.

Dans cet exemple, nous ne pouvons pas écrire le parent en premier car nous ne savons pas combien de nœuds il y aura à gauche. Nous pourrions avoir un problème à dessiner le nœud 2 si nous n'avions aucun décalage sur l'axe des x lors de l'écriture du nœud 1.

### Le problème avec l'algorithme des arbres binaires

Lorsque nous dessinons l'arbre, nous prenons une distance constante à partir du nœud parent. Dans l'exemple ci-dessus, la distance entre le nœud parent et le nœud 3 est égale à la distance entre le nœud parent et le nœud 2. Par conséquent, cet algorithme peut rencontrer des problèmes tels que le diagramme en losange.

### Qu'est-ce que le diagramme en losange ?

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-52.png)

Supposons que le nœud parent ait à la fois des enfants à gauche (nœud 2) et à droite (nœud 3). Et que l'enfant droit (nœud 3) ait un enfant à gauche (nœud 4), tandis que l'enfant gauche (nœud 2) ait un enfant à droite (nœud 5). 

Dans ce cas, nous aurons une collision avec les enfants (nœud 4 et nœud 5) car ils seront placés à la même position. 

Il existe maintenant deux principales façons de résoudre ce problème :

* Effectuer des calculs préliminaires qui dessinent l'arbre comme un arbre non symétrique sans nécessairement des distances constantes à partir du parent.
* Colorier les nœuds qui viennent de la gauche dans une couleur, et colorier les nœuds qui viennent de la droite dans une couleur différente.

Le problème avec la première implémentation est que nous utilisons le BinaryTreeViewer afin d'aider à gagner du temps. Et même si c'est plus ordonné et plus esthétiquement agréable d'utiliser ce type d'implémentation plutôt que la coloration, le programme serait trop lent et nuirait aux performances de notre code.

Donc dans ce tutoriel, nous allons nous en tenir à la deuxième façon d'implémenter une solution pour le problème du diagramme en losange (coloration).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-40.png)
_À quoi ressemble la sortie de l'algorithme de coloration._

## Comment implémenter l'algorithme

Maintenant que nous avons parlé de ce que sont les arbres binaires, quels sont leurs problèmes et quel algorithme nous allons utiliser pour résoudre ces problèmes, il est temps d'implémenter réellement l'algorithme.

> **NOTE** : une **classe partielle** est une classe qui peut être écrite dans des fichiers séparés et qui sera combinée lors de la compilation.

Commençons par l'implémentation la plus simple qui est la classe BinaryTree.

```csharp
namespace BinaryTreeViewer
{
    /// <summary>
    /// Représente une classe d'arbre binaire utilisée pour le BinaryTreeViewer.
    /// </summary>
    /// <typeparam name="T">Le type de nœud de l'arbre.</typeparam>
    public partial class BinaryTree<T>
    {
        private BinaryTree<T>? rightNode; // nœud droit de l'arbre binaire.
        private BinaryTree<T>? leftNode; // nœud gauche de l'arbre binaire.
        public T value { get; set; } // la valeur du nœud actuel.

        public BinaryTree(T value)
        {
            this.value = value;
            this.rightNode = null;
            this.leftNode = null;
        }

        public BinaryTree(T value, BinaryTree<T>? left, BinaryTree<T>? right) : this(value)
        {
            this.rightNode = right;
            this.leftNode = left;
        }

        public void SetLeftNode(BinaryTree<T> node)
        {
            this.leftNode = node;
        }

        public void SetRightNode(BinaryTree<T> node)
        {
            this.rightNode = node;
        }

        public BinaryTree<T>? GetRightNode() => this.rightNode;
        public BinaryTree<T>? GetLeftNode() => this.leftNode;

        public override string? ToString() => this.value?.ToString();
    }
}
```

Dans l'autre partie de la classe partielle, nous avons quelques méthodes supplémentaires que nous utiliserons pour imprimer l'arbre.

```csharp
 public partial class BinaryTree<T>
    {
        private BinaryTree<T>? max_left_node;

        /// <summary>
        /// Trouve le décalage maximal à gauche à partir du nœud de départ.
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="head">Le début de l'arbre que nous voulons dessiner.</param>
        /// <param name="left_offset"></param>
        /// <param name="max_offset"></param>
        /// 

        internal (BinaryTree<T>?, int max_offset) GetMaxLeft()
        {
            int max_offset = 0;

            GetMaxLeft(this, 0, ref max_offset);
            return (max_left_node, max_offset);
        }

        private void GetMaxLeft(BinaryTree<T> head, int left_offset, ref int max_offset)
        {
            if (head.GetLeftNode() != null)
            {
                left_offset += 1;

                if(left_offset > max_offset)
                {
                    max_left_node = head.GetLeftNode();
                }

                GetMaxLeft(head.GetLeftNode(), left_offset, ref max_offset);
            }
            if (head.GetRightNode() != null)
            {
                left_offset -= 1;
                GetMaxLeft(head.GetRightNode(), left_offset, ref max_offset);
            }

            if(left_offset > max_offset)
            {
                max_offset = left_offset;
            }
        }
    }
```

### GetMaxLeft

**GetMaxLeft** est censé nous donner deux détails dont nous avons besoin pour l'implémentation :

* Quel nœud est le nœud le plus à gauche de l'arbre, et
* Combien de décalage à gauche il a à partir du nœud parent (plus tard, il sera multiplié par une valeur constante).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-38.png)
_Visualisation de la valeur de retour_

Nous retournons les deux sous forme de tuple.

### Comment fonctionne GetMaxLeft

**GetMaxLeft** retourne le décalage du nœud le plus à gauche à partir du nœud parent de l'arbre. Comment cela fonctionne-t-il ? 

Pour chaque mouvement vers un nœud droit, nous diminuons la valeur de décalage à gauche (parce que nous nous éloignons du côté gauche du document). Et pour chaque fois que nous allons vers un nœud gauche, nous augmentons le décalage (parce que nous nous rapprochons du côté gauche du document). 

Nous conservons le décalage le plus long à partir de la tête que nous avons atteint et nous définissons sa valeur par référence au paramètre "**max_offset**", que nous retournons dans la méthode non récursive **GetMaxLeft**.

## Classe BTViewer

Maintenant que nous avons passé en revue les bases, il est temps de résoudre le problème pour lequel nous sommes ici, à savoir comment dessiner les arbres. Dans la classe BTViewer, nous gérons tous les processus de construction des arbres et les fichiers temporaires.

```csharp
using System.Diagnostics;
using System.Text.RegularExpressions;

namespace BinaryTreeViewer
{
    /// <summary>
    /// Affiche dans un document HTML un graphique de l'arbre.
    /// RECOMMANDATION : Utilisez un point d'arrêt sur la ligne de BinaryTreeViewer.View.
    /// </summary>
    public static class BTViewer
    {
        private static int StartingTempCount = 1; //le compteur temporaire de départ pour savoir combien
        //d'arbres nous avons créés.
        private static int tempCount = 1; // le nombre de fichiers temporaires que nous avons créés.
        private static readonly string BINTREE_CSS_FILENAME = "BINTREEINITIALIZER.css";
        private static string fileName => $"BINTREE{tempCount}.html"; //structure de nom des fichiers BINTREE.

        /// <summary>
        /// Définit la valeur de tempCount selon les arbres sauvegardés précédents.
        /// </summary>
        static BTViewer()
        {
            string directory = Directory.GetCurrentDirectory();

            if(!Directory.GetFiles(directory).Contains(BINTREE_CSS_FILENAME))
            {
                File.WriteAllText(BINTREE_CSS_FILENAME, @"#circle{
		border-radius: 50%;
		display: inline-block;
		border: 1px solid black;
	}
	.a{
		padding: 50px;
	}
	.b{
		width: 70px;
		height: 70px;
	}
	 .line{
width: 150px;
height: 150px;
border-bottom: 1px solid black;
position: absolute;
}");
            }

            Regex reg = new Regex(@"BINTREE\d+\.html"); //nous vérifions quel est le dernier fichier d'arbre binaire.

            List<string> fileNames = Directory.GetFiles(directory).ToList();
            fileNames = reg.Matches(string.Join(" ", fileNames)).Select(x => x.Value).ToList(); //Obtenir les fichiers BINTREE dans le répertoire.

            if (fileNames.Count > 0)
            {
                //nous trouvons le prochain fileName comme -> le dernier numéro de nom de fichier (BINTREE*Number*) + 1
                tempCount = fileNames.Select(x => int.Parse(new Regex(@"\d+").Match(x).Value)).Max() + 1; //le prochain arbre à dessiner.
            }
            else
                tempCount = 1;

            StartingTempCount = tempCount;
        }

        /// <summary>
        /// Écrit l'arbre complet dans un fichier par la tête.
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="tree">Le début de l'arbre.</param>
        public static void View<T>(BinaryTree<T> tree)
        {
            // au cas où ils ont entré un arbre invalide.
            if (tree == null)
                return;

            // au cas où il n'y a qu'un seul nœud sur l'arbre (seulement la tête).
            if(tree.GetRightNode() == null && tree.GetLeftNode() == null)
            {
                InitializeFileStructure(); // nous initialisons la structure du fichier.
                DrawElement(tree, (0, 0), false);      
                File.AppendAllText(fileName, "</html>");
                RunTree();

                tempCount++;
                return;
            }

            //combien de gauche nous prenons à partir du début (valeur maximale). -> max_left_offset
            int max_left_offset = tree.GetMaxLeft(); // le nœud le plus à gauche.

            // nous commençons par trouver la position de la tête de l'arbre.
            (int x, int y) head_position = (0, 50);
            head_position.x = max_left_offset * (100 + 50); //la taille de chaque cercle + décalage entre les cercles.

            InitializeFileStructure();
            DrawTree(tree, head_position, false);

            File.AppendAllText(fileName, "</html>"); //termine le document.

            RunTree();

            tempCount++;
        }

        /// <summary>
        /// Supprime les arbres que nous voulons effacer.
        /// </summary>
        public static void ClearTrees(TreesToClear treesToClear)
        {
            string directory = Directory.GetCurrentDirectory();
            Regex reg = new Regex(@"BINTREE\d+\.html"); //la structure d'un fichier BINTREE runtime.
            Regex findCount = new Regex(@"\d+");

            List<string> fileNames = Directory.GetFiles(directory).ToList();
            fileNames = reg.Matches(string.Join(" ", fileNames)).Select(x => x.Value).ToList();

            if (((int)treesToClear & 0b1) != 0) //exécution actuelle.
            {
                fileNames.Where(x => int.Parse(findCount.Match(x).Value) >= StartingTempCount)
                         .ToList().ForEach(x => File.Delete(x));
            }

            if(((int)treesToClear & 0b10) != 0) //autres exécutions.
            {
                fileNames.Where(x => int.Parse(findCount.Match(x).Value) < StartingTempCount)
                         .ToList().ForEach(x => File.Delete(x));
            }
        }

        /// <summary>
        /// Dessine l'arbre complet dans le fichier.
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="head">La tête de l'arbre.</param>
        /// <param name="position">La position de départ pour dessiner l'arbre.</param>
        private static void DrawTree<T>(BinaryTree<T> head, (int x, int y) position, bool right)
        {
            DrawElement(head, position, right);

            if(head.GetRightNode() != null)
            {
                DrawLine(position, (position.x + 150, position.y + 150));
                DrawTree(head.GetRightNode(), (position.x + 150, position.y + 150), true);
            }

            if(head.GetLeftNode() != null)
            {
                DrawLine(position, (position.x - 150, position.y + 150));
                DrawTree(head.GetLeftNode(), (position.x - 150, position.y + 150), false);
            }
        }

        /// <summary>
        /// Dessine une ligne entre les nœuds.
        /// </summary>
        /// <param name="p1"></param>
        /// <param name="p2"></param>
        private static void DrawLine((int x, int y) p1, (int x, int y) p2)
        {
            double left;

            if (p2.x < p1.x)
            {
                left = Math.Min(p1.x, p2.x);
            }
            else
            {
                left = p2.x - 75;
            }

            string line = $"\n<div class = 'line' style = 'left:{left}px;top:{p1.y}px;transform:rotate({45 * (Math.Sign(p2.x - p1.x))}deg);'></div>";
            File.AppendAllText(fileName, line);
        }
        
        /// <summary>
        /// Dessine un nœud.
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="node"></param>
        /// <param name="position"></param>
        private static void DrawElement<T>(BinaryTree<T> node, (double x, double y) position, bool right)
        {
            //SIGNIFICATION DE LA COLLISION EN LOSANGE -> 
            /* 
                    ( )
                    / \
                  ( ) ( )
                    \ /
                    ( ) -> collision (deux nœuds différents placés au même endroit dans le graphique
                                      car la distance entre chaque nœud et son père est
                                      égale).
             */
            //En cas de collision en losange, un nœud peut écraser l'autre nœud sur un graphique.
            //Parce que nous voulons voir les deux nœuds sur le graphique, nous colorions les nœuds qui
            //viennent de droite et les nœuds qui viennent de gauche
            //avec deux couleurs différentes -> Rouge & Bleu -> afin que nous puissions voir les différences.
            string color = "red"; //Rouge -> nœud du côté gauche, Bleu -> nœud du côté droit.

            if (right)
                color = "blue";

            File.AppendAllText(fileName, $"\n<div class ='b' id = 'circle' style='border: 1px solid {color};position: absolute; left: {position.x}px; top: {position.y}px;'></div>");
            File.AppendAllText(fileName, $"\n<div style='color:{color};position: absolute; left: {position.x - (node.ToString().Length / 2) * 4 + 32}px; top: {position.y + 28}px;'>{node.value}</div>");
        }
        
        //Ouvre l'arbre.
        private static void RunTree()
        {
            //affiche l'arbre à l'utilisateur. (ouvre le fichier HTML dans le navigateur).
            Process run_process = Process.Start(@"cmd.exe", "/c " + fileName);
            run_process.WaitForExit();
        }

        /// <summary>
        /// Crée une structure de fichier BINTREE.
        /// </summary>
        /// <returns></returns>
        private static string InitializeFileStructure()
        {
            //Le contenu de base d'un fichier BINTREE.
            string content = @$"<html><link rel=""stylesheet"" href=""{BINTREE_CSS_FILENAME}"">";
            File.WriteAllText(fileName, content);
            return fileName;
        }
    }
}

public enum TreesToClear
{
    CurrentRun = 0b1,
    PreviousRuns = 0b10
}
```

Comme vous pouvez le voir, la classe BTViewer est longue, alors divisons-la en plusieurs parties.

### Comment dessiner l'arbre

Maintenant, nous allons passer en revue comment imprimer l'arbre. 

#### Méthode BTViewer.View

```csharp
 public static void View<T>(BinaryTree<T> tree)
        {
            // au cas où ils ont entré un arbre invalide.
            if (tree == null)
                return;

            // au cas où il n'y a qu'un seul nœud sur l'arbre (seulement la tête).
            if(tree.GetRightNode() == null && tree.GetLeftNode() == null)
            {
                InitializeFileStructure(); // nous initialisons la structure du fichier.
                DrawElement(tree, (0, 0), false);      
                File.AppendAllText(fileName, "</html>");
                RunTree();

                tempCount++;
                return;
            }

            //combien de gauche nous prenons à partir du début (valeur maximale). -> max_left_offset
            int max_left_offset = tree.GetMaxLeft(); // le nœud le plus à gauche.

            // nous commençons par trouver la position de la tête de l'arbre.
            (int x, int y) head_position = (0, 50);
            head_position.x = max_left_offset * (100 + 50); //la taille de chaque cercle + décalage entre les cercles.

            InitializeFileStructure();
            DrawTree(tree, head_position, false);

            File.AppendAllText(fileName, "</html>"); //termine le document.

            RunTree();

            tempCount++;
        }
```

Cette méthode est publique pour l'utilisateur et ils utilisent cette méthode pour imprimer l'arbre. 

Dans la méthode, nous gérons deux cas différents :

**Nous avons seulement un nœud dans l'arbre** – nous écrivons simplement l'arbre de nœuds dans un fichier HTML, mettons à jour le numéro de fichier suivant (sera expliqué plus tard), ouvrons le fichier pour l'aperçu et sortons de la méthode.

**Nous avons plusieurs nœuds sur l'arbre** – dans ce cas, nous commençons par obtenir des données sur le nœud le plus à gauche de l'arbre en utilisant la méthode que nous avons expliquée précédemment. Après avoir collecté les données du nœud le plus à gauche, nous pouvons calculer où la tête de l'arbre est censée être dans le document. 

Après avoir trouvé la position de départ de la tête de l'arbre, nous pouvons commencer à écrire l'arbre à partir de la tête.

### Comment dessinons-nous l'arbre ?

Maintenant, il est temps d'aller plus loin dans l'implémentation du dessin. La première méthode que nous utilisons est **InitializeFileStructure** qui nous donne essentiellement les attributs CSS dont nous avons besoin pour dessiner les cercles des arbres.

```css
#circle{
		border-radius: 50%;
		display: inline-block;
		border: 1px solid black;
	}
	.a{
		padding: 50px;
	}
	.b{
		width: 70px;
		height: 70px;
	}
	.line{
        width: 150px;
        height: 150px;
        border-bottom: 1px solid black;
        position: absolute;
	}
```

**InitializeFileStructure** crée un fichier HTML sans `</HTML>` exprès car nous voulons ajouter plus de balises plus tard pour construire la structure de l'arbre.

#### Méthode DrawTree

```csharp
        private static void DrawTree<T>(BinaryTree<T> head, (int x, int y) position, bool right)
        {
            DrawElement(head, position, right);

            if(head.GetRightNode() != null)
            {
                DrawLine(position, (position.x + 150, position.y + 150));
                DrawTree(head.GetRightNode(), (position.x + 150, position.y + 150), true);
            }

            if(head.GetLeftNode() != null)
            {
                DrawLine(position, (position.x - 150, position.y + 150));
                DrawTree(head.GetLeftNode(), (position.x - 150, position.y + 150), false);
            }
        }
```

La méthode **DrawTree** est une méthode récursive qui est censée imprimer toutes les lignes et cercles de l'arbre.

* À chaque entrée, nous imprimons l'élément actuel en utilisant la méthode DrawElement.
* Ensuite, nous parcourons tous les nœuds de l'arbre binaire et définissons la position de chacun en augmentant/diminuant une valeur constante à partir du nœud précédent.
* Nous dessinons également une ligne de chaque nœud à son enfant en utilisant la méthode DrawLine.

#### Méthode DrawElement

```csharp
private static void DrawElement<T>(BinaryTree<T> node, (double x, double y) position, bool right)
        {
            //SIGNIFICATION DE LA COLLISION EN LOSANGE -> 
            /* 
                    ( )
                    / \
                  ( ) ( )
                    \ /
                    ( ) -> collision (deux nœuds différents placés au même endroit dans le graphique
                                      car la distance entre chaque nœud et son père est
                                      égale).
             */
            //En cas de collision en losange, un nœud peut écraser l'autre nœud sur un graphique.
            //Parce que nous voulons voir les deux nœuds sur le graphique, nous colorions les nœuds qui
            //viennent de droite et les nœuds qui viennent de gauche
            //avec deux couleurs différentes -> Rouge & Bleu -> afin que nous puissions voir les différences.
            string color = "red"; //Rouge -> nœud du côté gauche, Bleu -> nœud du côté droit.

            if (right)
                color = "blue";

            File.AppendAllText(fileName, $"\n<div class ='b' id = 'circle' style='border: 1px solid {color};position: absolute; left: {position.x}px; top: {position.y}px;'></div>");
            File.AppendAllText(fileName, $"\n<div style='color:{color};position: absolute; left: {position.x - (node.ToString().Length / 2) * 4 + 32}px; top: {position.y + 28}px;'>{node.value}</div>");
        }
```

La méthode DrawElement fait plusieurs choses :

* Détermine la couleur -> la méthode vérifie de quel nœud le nœud est venu. Si le nœud est venu de la droite, nous le colorions en bleu, mais s'il est venu de la gauche, nous le colorions en rouge.
* En utilisant la couleur et la position, nous pouvons également ajouter un cercle qui enveloppe la valeur du nœud.
* Ensuite, nous ajoutons la valeur du nœud à l'intérieur du cercle. 

#### Méthode DrawLine

```csharp
 private static void DrawLine((int x, int y) p1, (int x, int y) p2)
        {
            double left;

            if (p2.x < p1.x)
            {
                left = Math.Min(p1.x, p2.x);
            }
            else
            {
                left = p2.x - 75;
            }

            string line = $"\n<div class = 'line' style = 'left:{left}px;top:{p1.y}px;transform:rotate({45 * (Math.Sign(p2.x - p1.x))}deg);'></div>";
            File.AppendAllText(fileName, line);
        }
```

La méthode **DrawLine** prend simplement deux nœuds et dessine une ligne entre eux. Afin d'ajuster la ligne, nous effectuons également quelques calculs mathématiques.

Après avoir terminé la construction de l'arbre, nous ajoutons `</HTML>` pour terminer le document. Ensuite, nous appelons la méthode `RunTree()` pour ouvrir l'arbre à l'exécution. Nous augmentons également `tempCount` de 1 afin de savoir quel sera le nom du prochain fichier.

## Fichiers BINTREE

### Qu'est-ce que les fichiers BINTREE ?

La dernière partie du projet consiste à gérer les fichiers HTML que nous avons créés. Chaque fichier HTML suivra un format de nom qui consistera en le nom BINTREE. Ensuite, nous ajouterons l'ID chronologique puis l'extension du fichier.

Par exemple :

```
BINTREE1.html
BINTREE2.html
...
BINTREE143.html
BINTREE144.html
```

L'ID du prochain fichier HTML que nous créerons sera égal au numéro d'ID du dernier nom de fichier + 1.

* Les ID commencent à 1 -> le premier BINTREE que nous créerons sera "BINTREE1.html".

### Comment gérer les fichiers BINTREE

#### Le constructeur statique de BTViewer

```csharp
static BTViewer()
        {
            string directory = Directory.GetCurrentDirectory();

            if(!Directory.GetFiles(directory).Contains(BINTREE_CSS_FILENAME))
            {
                File.WriteAllText(BINTREE_CSS_FILENAME, @"#circle{
		border-radius: 50%;
		display: inline-block;
		border: 1px solid black;
	}
	.a{
		padding: 50px;
	}
	.b{
		width: 70px;
		height: 70px;
	}
	 .line{
width: 150px;
height: 150px;
border-bottom: 1px solid black;
position: absolute;
}");
            }

            Regex reg = new Regex(@"BINTREE\d+\.html"); //nous vérifions quel est le dernier fichier d'arbre binaire.

            List<string> fileNames = Directory.GetFiles(directory).ToList();
            fileNames = reg.Matches(string.Join(" ", fileNames)).Select(x => x.Value).ToList(); //Obtenir les fichiers BINTREE dans le répertoire.

            if (fileNames.Count > 0)
            {
                //nous trouvons le prochain fileName comme -> le dernier numéro de nom de fichier (BINTREE*Number*) + 1
                tempCount = fileNames.Select(x => int.Parse(new Regex(@"\d+").Match(x).Value)).Max() + 1; //le prochain arbre à dessiner.
            }
            else
                tempCount = 1;

            StartingTempCount = tempCount;
        }
```

Parce que nous les nommons dans l'ordre chronologique, nous ne pouvons pas commencer à donner des noms aléatoirement. Cela pourrait écraser d'autres fichiers BINTREE déjà créés. C'est pourquoi nous utilisons des expressions régulières pour trouver tous les fichiers BINTREE.

Ensuite, nous prenons l'ID maximum que nous pouvons trouver et nous l'augmentons de un. La nouvelle valeur deviendra le début de l'ID du fichier BINTREE lors de cette exécution. 

Par exemple, si nous exécutons le programme deux fois et que lors de la première exécution nous avons créé 5 fichiers BINTREE, cela signifie que notre tempCount lors de la prochaine exécution commencerà à 6 et le prochain fichier que nous créerons sera BINTREE6.html.

Un autre travail du constructeur statique est de vérifier que nous avons un fichier `BINTREEINITIALIZER.css`. Si nous n'en avons pas, alors nous devons le recréer. (`BINTREEINITIALIZER.css` est le fichier CSS que nous utilisons pour le style de l'arbre binaire.)

Nous sauvegardons également le tempCount dans un champ différent qui est `StartingTempCount` afin de savoir avec quel ID nous avons commencé à écrire les arbres (nous utiliserons cette fonctionnalité plus tard).

#### Méthode ClearTrees

La méthode **ClearTrees** nous permet de supprimer les fichiers temporaires BINTREE que nous avons créés lors de **l'exécution actuelle et des exécutions précédentes.** La méthode accepte une valeur d'énumération indiquant ce que nous voulons supprimer. La méthode a 3 options à accepter :

```csharp
BTViewer.ClearTrees(TreesToClear.CurrentRun); //EFFACER UNIQUEMENT L'EXÉCUTION ACTUELLE
BTViewer.ClearTrees(TreesToClear.PreviousRuns); //EFFACER UNIQUEMENT LES EXÉCUTIONS PRÉCÉDENTES
BTViewer.ClearTrees(TreesToClear.PreviousRuns | TreesToClear.CurrentRun); //EFFACER TOUT
```

```csharp
public static void ClearTrees(TreesToClear treesToClear)
        {
            string directory = Directory.GetCurrentDirectory();
            Regex reg = new Regex(@"BINTREE\d+\.html"); //la structure d'un fichier BINTREE runtime.
            Regex findCount = new Regex(@"\d+");

            List<string> fileNames = Directory.GetFiles(directory).ToList();
            fileNames = reg.Matches(string.Join(" ", fileNames)).Select(x => x.Value).ToList();

            if (((int)treesToClear & 0b1) != 0) //exécution actuelle.
            {
                fileNames.Where(x => int.Parse(findCount.Match(x).Value) >= StartingTempCount)
                         .ToList().ForEach(x => File.Delete(x));
            }

            if(((int)treesToClear & 0b10) != 0) //autres exécutions.
            {
                fileNames.Where(x => int.Parse(findCount.Match(x).Value) < StartingTempCount)
                         .ToList().ForEach(x => File.Delete(x));
            }
        }
```

La méthode utilise des expressions régulières pour obtenir tous les fichiers BINTREE que nous avons. Et elle utilise une autre expression régulière pour obtenir l'ID de chaque fichier BINTREE que nous avons.

Pour l'exécution actuelle -> nous supprimons tous les fichiers qui sont supérieurs ou égaux à `StartingTempCount` qui est l'ID du premier fichier que nous avons créé lors de l'exécution actuelle du programme.

Pour les exécutions précédentes -> nous faisons l'inverse de l'exécution actuelle : nous supprimons tous les fichiers avec un ID inférieur à l'ID du premier fichier que nous avons créé lors de cette exécution.

## Conclusion

Félicitations ! Vous êtes maintenant capable de créer votre propre système BinaryTreeViewer. J'espère que cet article vous a aidé à comprendre plus clairement les arbres binaires.
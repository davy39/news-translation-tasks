---
title: Comment générer automatiquement des extraits de code C# dans Visual Studio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-09T18:28:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-automatically-generate-code-snippets-visual-studio
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/gbi.png
tags:
- name: automation
  slug: automation
- name: C
  slug: c
- name: Productivity
  slug: productivity
- name: Snippet
  slug: snippet
- name: visual studio
  slug: visual-studio
seo_title: Comment générer automatiquement des extraits de code C# dans Visual Studio
seo_desc: 'By Gilad Bar Ilan

  When you use code snippets in Visual Studio, it can make your coding process a lot
  easier and faster. But what are code snippets? And how can you use them?

  In this article, we''ll look at how you can create code snippets in C#. Just ...'
---

Par Gilad Bar Ilan

Lorsque vous utilisez des extraits de code dans Visual Studio, cela peut rendre votre processus de codage beaucoup plus facile et rapide. Mais qu'est-ce que les extraits de code ? Et comment pouvez-vous les utiliser ?

Dans cet article, nous allons voir comment vous pouvez créer des extraits de code en C#. Gardez simplement à l'esprit que les extraits sont également disponibles dans d'autres langues dans Visual Studio.

Si vous savez déjà ce que sont les extraits de code, vous pouvez sauter directement à la section **Comment générer automatiquement des extraits de code**. 

## Qu'est-ce que les extraits de code ?

Si vous travaillez régulièrement avec Visual Studio, vous savez peut-être déjà ce que sont les extraits de code. Les extraits de code représentent un raccourci pour un morceau de code plus grand. 

Par exemple, ouvrez un projet C# dans Visual Studio et écrivez for puis appuyez deux fois sur la touche de tabulation. Comme vous pouvez le voir, au lieu d'écrire la boucle for complète, nous avons créé une boucle for simplement en écrivant for.

Il existe beaucoup plus d'extraits de code prédéfinis que vous pouvez utiliser. Par exemple, si vous écrivez cw puis appuyez deux fois sur la touche de tabulation, vous verrez une complétion automatique qui écrit ceci :

```cs
Console.WriteLine();
```

Vous pouvez consulter la liste complète des extraits de code prédéfinis dans la documentation ici :

%[https://docs.microsoft.com/en-us/visualstudio/ide/visual-csharp-code-snippets?view=vs-2019]

## Comment créer des extraits de code personnalisés

Maintenant que vous comprenez ce qu'est un extrait de code, nous pouvons maintenant passer à la création d'un extrait de code.

Pour créer votre premier extrait de code, créez un fichier .snippet. J'ai appelé mon fichier MySnippet.snippet, mais vous pouvez l'appeler comme vous le souhaitez.

Après la création du fichier d'extrait de code, ouvrez le fichier dans Visual Studio et ajoutez le morceau de code suivant dans le fichier.

```xml
<?xml version="1.0" encoding="utf-8"?>
<CodeSnippets xmlns="">
    <CodeSnippet Format="1.0.0">
        <Header>
            <Title></Title>    
            <Author></Author>
            <Description></Description>
            <Shortcut></Shortcut> 
        </Header>
        <Snippet>
            <Code Language="">
                <![CDATA[]]>
            </Code>
        </Snippet>
    </CodeSnippet>
</CodeSnippets>
```

Dans l'exemple ci-dessus, nous utilisons la structure de base d'un fichier d'extrait de code. Maintenant, nous allons l'éditer et créer un extrait de code qui convertira cr en `Console.ReadLine()`.

#### Balise Title

La balise title contient le titre de l'extrait (pas le nom du raccourci). Dans cet exemple, nous appellerons le titre ReadLineSnippet.

#### Balise Author

Dans la balise Author, vous pouvez insérer votre nom/compagnie pour obtenir le crédit de la création de l'extrait.

#### Balise Description

Dans la balise description, insérez une courte description de ce que fait exactement l'extrait.

#### Balise Shortcut

Le nom dans la balise shortcut est le nom qui appelle le morceau de code plus grand. Par exemple :

```cs
cw -> Console.WriteLine();
```

Le cw est spécifié comme le nom dans la balise shortcut.

#### Language

Parce que nous travaillons avec C#, nous devons le spécifier dans la langue :

```cs
<Code Language = "CSharp">
```

#### <![CDATA[]]>

Le <![CDATA[]]> contient la valeur de notre extrait. Dans notre exemple, à l'intérieur des crochets, nous allons insérer `Console.ReadLine()` comme ceci :

```cs
<![CDATA[Console.ReadLine();]]>
```

### Options supplémentaires pour les extraits de code

#### Définition des variables :

Nous pouvons également définir des variables et leur donner une valeur par défaut. En définissant une variable, nous pouvons l'utiliser plusieurs fois dans l'extrait, et nous donnons à l'utilisateur la possibilité de changer toutes les occurrences de la valeur par défaut en une seule fois.

Par exemple, si notre extrait crée le code suivant :

```cs
arr -> 
Object[] arr = new Object[100];
for(int i = 0; i < arr.Length; i++)
{   
	arr[i] = default(Object);
}
```

Et nous définissons Object comme une variable, nous pouvons remplacer toutes ses occurrences. Tout ce que nous devons faire est d'écrire dans la première occurrence un nom différent  par exemple int  puis appuyer deux fois sur la touche de tabulation et cela remplacera toutes les occurrences de Object par int.

Si nous avions défini `arr` comme une variable aussi, nous pourrions passer d'une variable à une autre en appuyant sur la touche de tabulation (lorsque vous créez l'extrait, la première variable sera sélectionnée en rouge/cyan  vous pouvez passer à l'autre en appuyant sur la touche de tabulation).

### Comment définir une variable

```xml
<?xml version="1.0" encoding="utf-8"?>
<CodeSnippets xmlns="">
    <CodeSnippet Format="1.0.0">
        <Header>
            <Title>init array.</Title>    
            <Author>Gilad Bar-Ilan</Author>
            <Description>crée et initialise un tableau.</Description>
            <Shortcut>myArr</Shortcut> 
        </Header>
        <Snippet>
            <Code Language="CSharp">
                <![CDATA[$typeName$[] $varName$ = new $typeName$[100];
                for(int $i$ = 0; $i$ < $varName$.Length; $i$++)
                {
                  $varName$[$i$] = default($typeName$);
                }]]>
            </Code>
            <Declarations>      
                <Literal>      
                    <ID>varName</ID>      
                    <ToolTip>nom de la variable.</ToolTip>         
                    <Default>arr</Default>        
                </Literal>
                <Literal>      
                    <ID>typeName</ID>      
                    <ToolTip>nom du type.</ToolTip>         
                    <Default>Object</Default>        
                </Literal>
                 <Literal>      
                    <ID>i</ID>      
                    <ToolTip>nom de l'itérateur.</ToolTip>         
                    <Default>i</Default>        
                </Literal>
             </Declarations> 	
        </Snippet>
    </CodeSnippet>
</CodeSnippets>
```

Comme vous pouvez le voir dans l'exemple ci-dessus, chaque variable que nous utilisons doit être à l'intérieur de la balise `<Literal>` sous la balise `<Declarations>`.

* `<ID>` 

Comment nous appelons la variable dans le `<![CDATA[]]>`
* `<ToolTip>` 
Une courte description de la variable.
* `<Default>` 

La valeur par défaut de la variable.

**NOTE**

Lorsque vous utilisez une variable dans le `<![CDATA[]]>` vous devez l'écrire dans la structure suivante : `$<ici vous mettez le nom de la variable>$`.

### Comment ajouter l'extrait de code à votre projet

Après avoir créé notre fichier d'extrait de code, nous voulons l'utiliser dans nos projets. Pour ce faire, nous devons placer le fichier dans le dossier des extraits personnalisés de Visual Studio. Cela ajoutera automatiquement l'extrait de code à notre projet.

Si vous voulez trouver le chemin du dossier :

* Ouvrez un projet C#.
* Allez dans Outils -> Gestionnaire d'extraits de code
* Copiez le chemin que vous voyez en haut de la boîte ouverte où il est écrit Emplacement.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-200.png)

Après avoir obtenu le chemin, ajoutez simplement le fichier dans le chemin.

**NOTE
**
Votre dossier My Code Snippets peut être situé à un endroit différent sur votre ordinateur, alors ne vous fiez pas au chemin dans l'image.

## Comment générer automatiquement des extraits de code

Maintenant, nous pouvons passer à ce que signifie générer automatiquement des extraits de code.

Nous savons que l'ajout de fichiers .snippet dans le dossier My Code Snippets ajoute automatiquement les extraits à notre projet. Nous pouvons donc utiliser ce comportement pour créer un code qui créera automatiquement des fichiers d'extraits et les ajoutera à notre projet.

### Quel type d'extraits de code voulons-nous ?

Dans ce projet, nous allons créer un extrait pour les objets avec un constructeur par défaut où le nom du raccourci sera le nom du type. Par exemple :

```cs
Random + tab deux fois -> Random random = new Random();
```

L'idée du projet est de lire les espaces de noms que nous utilisons dans notre projet et de créer un extrait personnalisé pour chaque objet qui suit les conditions. 

Nous voulons ajouter les extraits pour les types de chaque espace de noms que nous utilisons. Cela signifie que même si nous spécifions un espace de noms dans le using mais n'utilisons aucun de ses objets, nous inclurons toujours un extrait de code pour ses membres (ceux qui suivent la condition).

En plus des espaces de noms, nous allons également créer un extrait pour nos types définis.

#### Choses dont nous devons nous occuper :

* Supprimer les extraits de code des types qui ne sont plus nécessaires (si nous avons supprimé des types que nous avons créés ou des espaces de noms du projet).
* Mettre à jour les extraits de code chaque fois que l'utilisateur exécute le programme (nous ne mettons pas à jour en arrière-plan).
* Ajouter de nouveaux extraits pour les nouveaux espaces de noms que nous utilisons / types que nous créons.
* Créer une structure pour les extraits de code des types.

### Comment obtenir tous nos objets définis

Si nous voulons obtenir la liste complète des types définis par l'utilisateur, il y a deux façons de procéder.

La première façon  qui n'est pas aussi bonne que la seconde  est d'utiliser des expressions régulières. En utilisant des expressions régulières, nous pouvons parcourir chaque fichier dans notre projet et faire correspondre un constructeur par défaut dans une classe/déclaration d'une structure (parce que les structures ont toujours un constructeur par défaut).

#### Problèmes avec la technique Regex

Si l'utilisateur sépare les fichiers, nous pouvons vérifier avant d'utiliser le regex si le fichier a été modifié. En faisant cela, nous pouvons éviter de répéter les fichiers qui n'ont pas été modifiés.

Mais des changements mineurs dans le fichier nous feront relire le fichier même s'il n'y a pas de différence dans les objets. Cela entraînera également des fichiers désorganisés qui ont beaucoup de code dans un seul fichier, ce qui peut nous faire relire le fichier encore et encore. (Si tout le code est dans un seul fichier ou juste quelques-uns, nous ne pourrons pas éviter de relire les parties inchangées du code.)

#### La deuxième technique

Réflexion

Au lieu d'utiliser Regex, nous pouvons utiliser la réflexion et obtenir les classes que nous avons créées en lisant les métadonnées au lieu de lire chaque fichier comme du texte.

```cs

        /// <summary>
        /// Retourne une liste de tous les types que nous avons créés.
        /// </summary>
        /// <returns></returns>
        public static List<Type> GetCustomTypes()
        {
            StackTrace myStackTrace = new StackTrace();

            //contient le nom de l'espace de noms du projet
            //en utilisant stackframe, nous obtenons la première méthode appelante (main - le bas de la pile) puis nous vérifions l'espace de noms du type où la méthode est située.
            //dans notre cas, main est situé sous 'Program' puis nous vérifions quel est l'espace de noms de Program.
            string namespace_ = myStackTrace.GetFrame(myStackTrace.FrameCount - 1).GetMethod().DeclaringType.Namespace;

            Assembly assembly = Assembly.GetExecutingAssembly();
            
            //contient tous les types personnalisés.
            //assembly.GetTypes() => retourne tous les types.
            //ensuite, nous supprimons tous les types qui ne sont pas liés à notre espace de noms.
            //ensuite, nous supprimons tous les types créés par le compilateur.
            //ensuite, nous supprimons tous les types qui n'ont pas de constructeur par défaut.
            var types = assembly.GetTypes().Where(x => x.Namespace == namespace_).Where(x => !x.Name.Contains("<>c"))
                        .Where(x => x.GetConstructors().Any(x => x.GetParameters().Length == 0));
            return types.ToList();
        }

```

### Comment obtenir les objets des bibliothèques

Nous allons rencontrer beaucoup de problèmes dans cette partie du projet. Regardons ce qui peut mal se passer.

#### Problème 1

Si nous lisons les assemblages que nous utilisons dans notre projet en utilisant la réflexion, nous n'aurons pas l'option d'obtenir les types des bibliothèques que nous avons définies dans le using mais que nous n'utilisons pas réellement. Par exemple :

```cs
using System.Linq;
using System.IO;
public static void Main()
{  
	int[] arr = Enumerable.Range(0,100).ToArray(); //Fonctionnalité de Linq
}
```

Dans l'exemple ci-dessus, nous n'utilisons que la fonctionnalité Linq, ce qui signifie que si nous allons lire les assemblages utilisés dans le projet, nous ne verrons pas System.IO même si nous voulons qu'il soit affiché.

#### Problème 2

Un autre problème possible se produit même lorsque nous utilisons la bibliothèque. Cela est dû au fait qu'un espace de noms peut avoir plusieurs assemblages et, pour des raisons d'efficacité, le compilateur n'appellera pas tous les assemblages lorsqu'il n'en a pas besoin. Donc, même si nous utilisons la bibliothèque, cela ne signifie pas que nous aurons tous les assemblages.

#### Comment pouvons-nous résoudre le problème ?

Ce problème est compliqué car nous ne pouvons pas changer la façon dont le compilateur fonctionne. Donc, si nous voulons résoudre le problème, nous devrons être créatifs.

Notre solution ne sera pas très efficace, mais nous n'avons pas beaucoup d'options pour résoudre cela.

#### Nous pouvons utiliser un algorithme

* Nous obtenons tous les espaces de noms que nous utilisons dans tous nos fichiers .cs dans le projet.
* Ensuite, nous itérons sur tous les fichiers DLL System et nous vérifions si les types là-bas sont liés à l'un des espaces de noms que nous utilisons dans le projet.
* Nous ajoutons à cette liste également nos types définis, ainsi que les références que nous avons ajoutées au projet, si la référence est définie dans le using, nous ajoutons ses types même si nous n'utilisons pas ses types dans le programme lui-même.
* Après avoir fait cela, nous vérifions si le type a un constructeur par défaut.

Le code pour résoudre le problème est assez compliqué, alors passons-le en revue.

```cs
using System;
using System.Reflection;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text.RegularExpressions;

namespace Reader
{
    public class TypeReader
    {
        public static List<Type> GetAllTypes()
        {
            #region GetSystemLibrary Files
            string systemDllPath = typeof(string).Assembly.Location; //obtient la dll du type string.
            systemDllPath = Path.GetDirectoryName(systemDllPath);
            string[] systemLibraries = Directory.GetFiles(systemDllPath); //la liste des dlls des bibliothèques système.  
            #endregion

            #region Namespaces in project files.
            string[] namespaces_ = Directory.GetFiles(GetSourceCodePath())
                                      .Where(x => x.EndsWith(".cs")).ToArray();
            namespaces_ = GetNamespaces(namespaces_).ToArray();//nous supprimons le point-virgule
            #endregion

            #region Check the system libraries.
            List<Type> types = systemLibraries.Where(x => x.EndsWith(".dll")).Select(x =>
            {
                Assembly asm = null;
                try
                {
                    asm = Assembly.LoadFile(x);

                }
                catch
                {
                    asm = null;
                }

                return asm;
            }).SelectMany(x => x != null ? x.GetTypes() : new Type[] { })
                        .Where(x => x != null && !x.Name.Contains("<>c")).Where(x => namespaces_.Contains(x.Namespace))
                        .Where(x => x.IsPublic && (x.IsClass || x.IsValueType)).ToList();
            #endregion

            #region add assemblies we use in our program.
            types.AddRange(AppDomain.CurrentDomain.GetAssemblies()
                           .SelectMany(x => x.GetTypes().Where(x => !x.Name.Contains("<>c")).Where(x => namespaces_.Contains(x.Namespace)))
                           .Where(x => x.IsPublic && (x.IsClass || x.IsValueType)));
            #endregion

            #region add custom types we created.
            types.AddRange(GetCustomTypes()); //ajoute nos extraits personnalisés créés
            #endregion

            #region add types belongs to refrences we didn't use in our project.
            types.AddRange(GetUnUsedRefrenecedTypes(namespaces_)); //ajoute les bibliothèques référencées que nous spécifions mais n'utilisons pas.
            #endregion

            #region filter types.
            types = types.Where(x => x.IsValueType || x.GetConstructors().Any(x => x.GetParameters().Length == 0)).ToList();
            #endregion

            #region remove duplicated type names.
            types = types.GroupBy(x => x.FullName).Select(x => x.First()).ToList();
            #endregion

            return types;
        }

        //Retourne l'assemblage de la fonction principale.
        public static string GetMainAssemblyLocation()
        {
            StackTrace main = new StackTrace();
            string path = main.GetFrame(main.FrameCount - 1).GetMethod().DeclaringType.Assembly.Location;
            return Path.GetDirectoryName(path);
        }

        public static string GetSourceCodePath()
        {
            string projectPath = GetMainAssemblyLocation();

            try
            {
                while (!Directory.GetFiles(projectPath).Any(x => x.EndsWith(".cs")))
                {
                    projectPath = projectPath.Remove(projectPath.LastIndexOf("\\"));
                }
            }
            catch
            {
                throw new SourceCodeNotFoundException();
            }

            return projectPath;
        }

        public static List<string> GetNamespaces(string[] files)
        {
            List<string> namespaces = new List<string>();

            foreach (string file_ in files)
            {
                StreamReader fileStream = new StreamReader(file_);
                Regex matchUsing = new Regex(@"using([ ]|\t|\n)+\S+;");
                string[] fileNamespaces = matchUsing.Matches(fileStream.ReadToEnd()).Select(x => x.Value)
                                          .Select(x => x.Remove(x.IndexOf("using"), "using".Length).Trim()).ToArray();
                namespaces.AddRange(fileNamespaces);

                fileStream.Close();
            }

            return namespaces.Select(x => x.Remove(x.Length - 1, 1)).Distinct().ToList();
        }

        /// <summary>
        /// Cela est utilisé au cas où nous avons une bibliothèque référencée personnalisée (peut être une dll que nous avons créée)
        /// et nous spécifions cela dans le using, cependant, nous n'utilisons pas ses assemblages.
        /// </summary>
        /// <returns></returns>
        public static List<Type> GetUnUsedRefrenecedTypes(string[] namespaces_)
        {
            string sourceCode = GetMainAssemblyLocation();
            List<Type> otherTypes = new List<Type>();

            string[] fileNames = Directory.GetFiles(Path.GetDirectoryName(sourceCode));

            if (fileNames.Any(x => x.EndsWith(".dll")))
            {
                fileNames = fileNames.Where(x => x.EndsWith(".dll")).ToArray();

                foreach (var file in fileNames)
                {
                    Assembly asm;

                    try
                    {
                        asm = Assembly.LoadFile(file);
                    }
                    catch
                    {
                        continue;
                    }

                    otherTypes.AddRange(asm.GetTypes().Where(x => !x.Name.Contains("<>c"))
                                        .Where(x => x.IsPublic && (x.IsClass || x.IsValueType))
                                        .Where(x => namespaces_.Contains(x.Namespace)).GroupBy(x => x.Name)
                                        .Select(x => x.First()));
                }
            }

            return otherTypes;
        }

        /// <summary>
        /// Retourne une liste de tous les types que nous avons créés.
        /// </summary>
        /// <returns></returns>
        public static List<Type> GetCustomTypes()
        {
            StackTrace myStackTrace = new StackTrace();
            Type mainType = myStackTrace.GetFrame(myStackTrace.FrameCount - 1).GetMethod().DeclaringType;

            //contient le nom de l'espace de noms du projet
            //en utilisant stackframe, nous obtenons la première méthode appelante (main - le bas de la pile) puis nous vérifions l'espace de noms du type où la méthode est située.
            //dans notre cas, main est situé sous 'Program' puis nous vérifions quel est l'espace de noms de Program.
            string namespace_ = mainType.Namespace;
            Assembly assembly = mainType.Assembly;

            //contient tous les types personnalisés.
            //assembly.GetTypes() => retourne tous les types.
            //ensuite, nous supprimons tous les types qui ne sont pas liés à notre espace de noms.
            //ensuite, nous supprimons tous les types créés par le compilateur.
            //ensuite, nous supprimons tous les types qui n'ont pas de constructeur par défaut.
            var types = assembly.GetTypes().Where(x => x.Namespace == namespace_).Where(x => !x.Name.Contains("<>c")); ;
            return types.ToList();
        }
    }

    internal class SourceCodeNotFoundException : Exception
    {
        public override string Message => "Impossible de charger les fichiers '.cs', veuillez vous assurer\n" +
                                    "que vos fichiers sont situés à l'emplacement par défaut / vous avez un type de projet valide.";
    }
}

```

#### **Note importante :**

```cs
//Si je mentionne dans l'explication les mots "fonction principale" je veux dire :

public static void Main()
{   
	TypeReader.GetAllTypes();
}
//Ce qui signifie que la fonction principale n'est pas située dans la classe TypeReader, c'est la fonction principale qui appelle la classe.
```

### Région GetSystemLibrary Files

Dans ces lignes, nous obtenons tous les fichiers de bibliothèque de System.

* Nous vérifions où se trouve l'assemblage de l'une des DLL système (dans notre cas, où se trouve l'assemblage de string).
* Ensuite, nous supprimons le nom du fichier du chemin pour n'avoir que le répertoire.
* Ensuite, nous ne prenons que les fichiers de bibliothèque du répertoire (.dll).

Nous faisons cela parce que tous les fichiers des bibliothèques System sont situés dans le même répertoire.

### Région Namespaces dans les fichiers du projet

Dans ces lignes, nous obtenons tous les espaces de noms que nous utilisons dans tous nos fichiers de projet.

#### Méthodes personnalisées que nous utilisons dans ces lignes

**GetSourceCodePath
**
Cette fonction retourne le chemin de notre code source. D'abord, nous obtenons le chemin de la dll de la fonction principale. En supposant que l'utilisateur travaille avec la manière par défaut de trier les répertoires dans Visual Studio, nous supprimons les répertoires de notre chemin jusqu'à ce que nous atteignions un répertoire avec des fichiers .cs.

**GetMainAssemblyLocation
**
Nous utilisons StackTrace pour obtenir l'emplacement de l'assemblage de la fonction principale. Un exemple de 'Suppression' est 
C:\Users\File1\File2 -> C:\Users\File1

Si nous ne pouvons pas trouver de répertoire, nous lançons **SourceCodeNotFoundException**.

**GetNamespaces
**
La méthode retourne tous les espaces de noms dans les fichiers que nous avons entrés. Elle itère sur chaque fichier et lit tous les espaces de noms que nous utilisons dans chacun d'eux en utilisant Regex.

Pour chaque espace de noms, nous obtiendrons `using <Something>;` puis nous supprimerons tous les caractères supplémentaires et nous ne garderons que le `<Something>`.

#### Dans GetAllTypes

* Nous lisons tous les fichiers de notre répertoire de code source
* Nous ne gardons que les fichiers avec une extension .cs
* Nous obtenons les espaces de noms des fichiers.

### Région Vérifier les bibliothèques système

Dans ces lignes, nous vérifions les bibliothèques système. Ces lignes corrigent les deux problèmes que nous avons mentionnés précédemment.

* Nous obtenons tous les fichiers dans le répertoire des DLL système et nous ne gardons que ceux qui représentent une dll (avec une extension .dll).
* Nous essayons de charger chacun de ces fichiers.
* Si nous pouvons charger le fichier, alors nous obtenons les types dans l'assemblage.
* Nous supprimons tous les types créés par le compilateur <>c.
* Nous ne gardons que les types liés à l'un des espaces de noms dans notre projet.
* Ensuite, nous ne gardons que les types publics et ceux qui sont des classes ou des structures.

#### Pourquoi faisons-nous cela ?

Les problèmes que nous avons mentionnés précédemment étaient causés parce que nous avons essayé de vérifier ce que le programme **utilise réellement** en temps d'exécution. Mais le compilateur fait des optimisations, et c'est pourquoi nous ne pouvons pas vraiment atteindre les cas mentionnés dans les problèmes.

Donc, pour résoudre ce problème, nous devons être créatifs et vérifier les espaces de noms que nous utilisons dans nos fichiers de projet. Ensuite, nous chargeons les assemblages, et à la fin, nous vérifions que chaque type si son espace de noms est l'un des espaces de noms que nous utilisons dans notre projet.

### Région ajouter les assemblages que nous utilisons dans notre programme

Dans ces lignes, nous ajoutons les assemblages que nous utilisons dans notre programme.

Pour chacun des assemblages, nous faisons la même vérification pour le type qu'il contient.

* Si le type est public
* S'il s'agit d'une structure ou d'une classe
* S'il ne s'agit pas d'un type créé par le compilateur.
* S'il est lié à l'un des espaces de noms que nous utilisons dans notre projet.

### Région ajouter les types personnalisés que nous avons créés

Dans cette ligne, nous ajoutons tous les types personnalisés que nous avons créés.

**GetCustomTypes
**
La fonction utilise StackTrace pour obtenir l'espace de noms et l'assemblage de la fonction principale.

Après avoir obtenu l'assemblage, nous obtenons les types qui sont liés à l'espace de noms principal.

### Région ajouter les types appartenant aux références que nous n'avons pas utilisées dans notre programme

Dans cette ligne, nous ajoutons les types qui appartiennent aux références que nous n'avons pas utilisées dans le programme et qui ont été spécifiées dans le using (comme nous l'avons fait pour les types système, mais cette fois nous faisons cela pour les références que nous avons ajoutées manuellement, pas System).

**GetUnUsedReferencedTypes**

* Nous parcourons le répertoire du code source (les références ajoutées manuellement s'y trouvent).
* Nous essayons de charger les fichiers .dll et d'ajouter tous les types qui passent les conditions que nous avons faites dans les vérifications précédentes dans main.

### Région filtrer les types

Dans cette ligne, nous ne gardons que les types de valeur et les classes qui ont un constructeur par défaut (s'ils sont des types de valeur, ils ont un constructeur par défaut pour sûr).

### Région supprimer les noms de types dupliqués

Nous supprimons les types dupliqués par nom.

## Comment construire les extraits de code

Nous avons passé la partie difficile, alors maintenant il est temps de construire les extraits de code !

```cs
using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using Reader;

namespace SnippetGenerator2
{
    public class CodeSnippetGenerator
    {
        public string SnippetLocation;

        public CodeSnippetGenerator(string snippetLocation)
        {
            this.SnippetLocation = snippetLocation.EndsWith("\\") ? snippetLocation : snippetLocation + "\\";
        }

        public void UpdateSnippets()
        {
            List<Type> allTypes = TypeReader.GetAllTypes();
            Func<Type, string> makeFileName = x => SnippetLocation + x.Name + "-" + x.Namespace + ".snippet";

            DirectoryInfo myCodeSnippets = new DirectoryInfo(SnippetLocation);
            string[] snippetFileNames = allTypes.Select(x => makeFileName(x)).ToArray();
            string[] previous = myCodeSnippets.GetFiles().Where(x => x.Name.EndsWith(".snippet")).Select(x => x.Name).ToArray();

            //nous ne gardons que les fichiers qui n'existent plus.
            previous = previous.Where(x => !snippetFileNames.Contains(x)).ToArray();
            previous.ToList().ForEach(x =>
            {
                try
                {
                    File.Delete(SnippetLocation + x);
                }
                catch { }
            });//nous supprimons les fichiers dont nous n'avons pas besoin.

            allTypes.ForEach(x => 
            {
                if (!Directory.GetFiles(SnippetLocation).Contains(makeFileName(x)))
                    CreateSnippet(x);
            }
            ); //nous créons des extraits pour les types.
        }

        public List<string> RemoveAllCodeSnippets()
        {
            string[] files = Directory.GetFiles(SnippetLocation).ToArray();
            List<string> notDeleted = new List<string>();
   

            files.ToList().ForEach(x =>
            {
                StreamReader snippetFile = new StreamReader(x);

                if (snippetFile.ReadToEnd().Contains("<Author>AUTO-GENERATOR</Author>"))
                {
                    snippetFile.Close();

                    try
                    {
                        File.Delete(x);
                    }
                    catch
                    {
                        notDeleted.Add(x);
                    }
                }
            });

            int i = 0;
            while(i < notDeleted.Count)
            {
                i++;
                try
                {
                    File.Delete(notDeleted[i]);
                }
                catch
                {
                    continue;
                }
                notDeleted.Remove(notDeleted[i]);
            }

            return notDeleted;
        }


        /// <summary>
        /// Crée un extrait.
        /// </summary>
        /// <param name="type">Le type pour lequel faire la création par défaut.</param>
        /// <param name="description">La description de l'extrait.</param>
        internal void CreateSnippet(Type type,
                                       string description = "DefaultDescription")
        {

            string snippet_structure = $@"<?xml version=""1.0"" encoding=""utf-8""?>
  <CodeSnippets xmlns = """">  
     <CodeSnippet Format = ""1.0.0"">   
         <Header>    
            <Title>{type.Name}-{type.Namespace}</Title>    
            <Author>AUTO-GENERATOR</Author>
            <Description> {description}</Description>
            <Shortcut> {type.Name} </Shortcut>   
         </Header>   
         <Snippet>  
           <Code Language = ""CSharp"">    
                 <![CDATA[{type.Name} $obj$ = new {type.Name}();]]>     
             </Code>     
             <Declarations>      
                <Literal>      
                    <ID>obj</ID>      
                    <ToolTip>nom de la variable.</ToolTip>         
                       <Default>{type.Name.ToLower()}</Default>        
                   </Literal>       
                </Declarations>         
             </Snippet>        
           </CodeSnippet>
         </CodeSnippets>";

            //écrit l'extrait dans le répertoire des extraits.
            File.WriteAllText(SnippetLocation + type.Name + "-" + type.Namespace + ".snippet", snippet_structure);
        }
    }
}

```

Parlons de ce code :

* Reader est l'espace de noms de la classe que nous avons construite précédemment.
* TypeReader est le nom de la classe que nous avons construite précédemment.
* Les noms de fichiers des extraits seront écrits sous la forme `<TypeName>-<NamespaceName>.snippet`

#### Le Constructeur

* Le constructeur accepte le chemin du répertoire My Code Snippets de l'utilisateur.

#### La méthode CreateSnippet

La méthode CreateSnippet crée un extrait avec une structure commune.

* Titre

Le `<typeName>-<namespace>`
* Auteur

AUTO-GENERATOR, nous les appelons tous par le même nom afin que nous sachions quels extraits ont été créés par le CodeSnippetGenerator et lesquels ont été créés par l'utilisateur.
* Nous créons une structure de :

```cs
TypeName typename(en petites lettres) = new TypeName();
```

* Nous définissons le shortcut pour être le nom du type également.

#### La méthode RemoveAllSnippets

La méthode RemoveAllSnippets supprime tous les extraits **que le CodeSnippetGenerator** a créés. 

Nous savons si les fichiers ont été créés par le générateur d'extraits de code en vérifiant si la balise Author contient AUTO-GENERATOR. 

Nous essayons à nouveau de supprimer les fichiers qui n'ont pas été supprimés la première fois. Si nous ne pouvons pas les supprimer la deuxième fois, nous retournons une liste des noms de fichiers que nous n'avons pas pu supprimer.

#### La méthode UpdateSnippets

La méthode UpdateSnippets met à jour les extraits à chaque exécution. À chaque exécution :

* Nous lisons les noms des types que nous utilisons dans notre programme principal (pas dans la classe CodeSnippetGenerator).
* Nous lisons les noms des fichiers .snippet que nous avons de l'exécution précédente.
* Nous créons un tableau de noms de fichiers pour chacun de nos types de notre exécution actuelle.
* Nous voyons quels fichiers d'extraits nous n'avons plus besoin en comparant les noms des fichiers d'extraits que nous avions dans notre exécution précédente et qui n'existent pas dans les noms de fichiers de l'exécution actuelle.
* Nous supprimons ces fichiers.
* Ensuite, nous créons un fichier .snippet pour chaque type qui n'en a pas déjà un.

## Comment utiliser le programme de génération automatique d'extraits de code

Si vous voulez utiliser le programme, ouvrez simplement un projet C# et au début de la fonction principale, écrivez :

```cs
var csg = new CodeSnippetGenerator("chemin de 'My Code Snippets'>);
csg.UpdateSnippets(); //pour créer & mettre à jour les extraits dans le projet.csg.RemoveAllSnippets(); //pour supprimer les extraits créés.
```

Félicitations ! Vous avez maintenant créé votre propre CodeSnippetGenerator.

J'espère que cela vous sera utile et vous fera gagner du temps lorsque vous écrirez votre code. Merci d'avoir lu :)
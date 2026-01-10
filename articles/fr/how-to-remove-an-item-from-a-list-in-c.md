---
title: Comment supprimer un élément d'une liste en C#
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-12-13T00:28:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-an-item-from-a-list-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/bernd-dittrich-d_3EKbSg1tg-unsplash.jpg
tags:
- name: C
  slug: c
- name: C#
  slug: csharp
seo_title: Comment supprimer un élément d'une liste en C#
seo_desc: 'While building your application in C#, you might need to store and manipulate
  sets of data. The List class is a member of the System.Collections.Generic namespace
  and you use it to store multiple objects of the same datatype.

  The List class represent...'
---

Lors de la création de votre application en C#, vous pourriez avoir besoin de stocker et de manipuler des ensembles de données. La classe **List<T>** est un membre de l'espace de noms **System.Collections.Generic** et vous l'utilisez pour stocker plusieurs objets du même type de données.

La classe **List<T>** représente une collection de listes fortement typées d'objets qui peuvent être accessibles à l'aide d'un index. Sa classe contient diverses méthodes pour rechercher, trier et manipuler des listes.

Dans cet article, nous allons apprendre comment supprimer un élément d'une liste en C#. Il existe différentes façons de supprimer un élément d'une liste. Ici, vous apprendrez comment supprimer un élément de la classe **List<T>** en utilisant les méthodes **Remove()** et **RemoveAt()**.

## Comment supprimer un élément d'une liste en utilisant la méthode Remove()

Supposons que vous avez déjà une liste existante de chaînes de prénoms.

```program.cs
using System.Collections.Generic;

namespace Collections
{
    public class Program
    {
        static void Main(string[] args)
        {
            List<string> FirstName = new List<string>() { "John", "Jane", "Josh", "Debby", "Gilbert", "Joe" };
        }
    }
}

```

Vous utilisez la méthode **Remove()** pour supprimer la première occurrence de l'élément dans une liste. Elle prend un paramètre en tant qu'élément et supprime la première occurrence de cet élément.

Voici un extrait de code montrant comment utiliser la méthode **Remove()** pour supprimer un élément d'une liste :

```program.cs
using System.Collections.Generic;

namespace Collections
{
    public class Program
    {
        static void Main(string[] args)
        {
            List<string> FirstName = new List<string>() { "John", "Jane", "Josh", "Debby", "Gilbert", "Joe" };
            
            // Parcourir la liste avant d'appeler la méthode Remove()
            foreach(string names in FirstName)
            {
                Console.WriteLine(names);                
            }

            // Méthode Remove
            FirstName.Remove("John");            

            // Parcourir la liste après avoir appelé la méthode Remove()
            foreach (string names in FirstName)
            {
                Console.WriteLine(names);
            }
        }
    }
}



```

Dans le code ci-dessus, **FirstName.Remove("John")** supprime le premier élément ayant la valeur **"John"**. Nous avons ensuite parcouru la liste pour voir le contenu de notre liste avant et après la manipulation.

## Comment supprimer un élément d'une liste en utilisant la méthode RemoveAt()

En utilisant la liste que nous avons créée, la méthode **RemoveAt()** prend un index en tant que paramètre et supprime l'élément à cet index. Voici un extrait de code montrant comment utiliser la méthode **RemoveAt()** pour supprimer un élément d'une liste.

```program.cs
using System.Collections.Generic;

namespace Collections
{
    public class Program
    {
        static void Main(string[] args)
        {
            List<string> FirstName = new List<string>() { "John", "Jane", "Josh", "Debby", "Gilbert", "Joe" };
            
            // Parcourir la liste avant d'appeler la méthode RemoveAt()
            foreach(string names in FirstName)
            {
                Console.WriteLine(names);                
            }

            // Méthode RemoveAt()
            FirstName.RemoveAt(1);            

            // Parcourir la liste après avoir appelé la méthode RemoveAt()
            foreach (string names in FirstName)
            {
                Console.WriteLine(names);
            }
        }
    }
}

```

Dans le code ci-dessus, **FirstName.RemoveAt(1)** supprime l'élément à l'index 1. Il est nécessaire de savoir que la méthode **RemoveAt()** prend un numéro d'index basé sur zéro (cela signifie que les positions/index commencent à 0, et non à 1). Nous avons ensuite parcouru la liste pour voir le contenu de notre liste avant et après la manipulation de la liste.

## Conclusion

Dans cet article, nous avons discuté de la façon de supprimer un élément de la classe **List<T>** en C#. Nous avons également démontré deux approches avec des exemples.

J'espère que cet article vous a été utile. **Bon codage !**
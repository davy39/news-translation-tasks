---
title: Le mot-clé internal en C# est-il une mauvaise pratique ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T19:06:56.000Z'
originalURL: https://freecodecamp.org/news/is-the-c-internal-keyword-a-code-smell
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/0_agwE-xG4Q7OZDDgC-1.jpg
tags:
- name: best practices
  slug: best-practices
- name: C
  slug: c
- name: clean code
  slug: clean-code
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: Le mot-clé internal en C# est-il une mauvaise pratique ?
seo_desc: 'By shani fedida

  In this post, I am going to show why I think the internal keyword, when put on class
  members, is a code smell and suggest better alternatives.

  What is the internal keyword?

  In C# the internal keyword can be used on a class or its memb...'
---

Par shani fedida

Dans cet article, je vais expliquer pourquoi je pense que le mot-clé internal, lorsqu'il est appliqué aux membres d'une classe, est une mauvaise pratique et suggérer des alternatives meilleures.

### Qu'est-ce que le mot-clé internal ?

En C#, le mot-clé internal peut être utilisé sur une classe ou ses membres. Il s'agit de l'un des [modificateurs d'accès](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/access-modifiers) de C#. Les types ou membres internal sont accessibles **uniquement dans** les **fichiers de la même assembly**. ([Documentation du mot-clé internal en C#](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/internal)).

### Pourquoi avons-nous besoin du mot-clé internal ?

« Une utilisation courante de l'accès internal est dans le développement basé sur des composants, car cela **permet à un groupe de composants de coopérer de manière privée sans être exposé au reste du code de l'application**. Par exemple, un framework pour la création d'interfaces utilisateur graphiques pourrait fournir des classes Control et Form qui coopèrent en utilisant des membres avec un accès internal. Comme ces membres sont internal, ils ne sont pas exposés au code qui utilise le framework. » ([Documentation du mot-clé internal en C#](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/internal))

Voici les cas d'utilisation que j'ai rencontrés pour l'utilisation du mot-clé internal sur un membre de classe :

* Appeler une fonction privée d'une classe dans la même assembly.
* Pour tester une fonction privée, vous pouvez la marquer comme internal et exposer la DLL aux tests via [InternalsVisibleTo](https://docs.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.internalsvisibletoattribute?view=netframework-4.8).

Les deux cas peuvent être considérés comme une [mauvaise pratique](https://enterprisecraftsmanship.com/2017/10/23/unit-testing-private-methods/), indiquant que cette fonction privée devrait être publique.

### Examinons quelques exemples

Voici un exemple simple. Une fonction d'une classe souhaite accéder à une fonction privée d'une autre classe.

```c#
class A{
	public void func1(){
		func2();
	}
	private void func2(){}
}

class B{
	public void func(A a){
		a.func2(); //Erreur de compilation 'A.func2()' est inaccessible en raison de son niveau de protection
	}
}
```

La solution est simple — il suffit de marquer A::func2 comme public.

Regardons un exemple un peu plus complexe :

```c#
public class A{
	public void func1(){}
	private void func2(B b){}
}

internal class B{
	public void func3(A a){		
		a.func2(this); //Erreur de compilation 'A.func2(B)' est inaccessible en raison de son niveau de protection
	}
}
```

Quel est le problème ? Il suffit de marquer func2 comme public comme nous l'avons fait précédemment.

```c#
public class A{
	public void func1(){ ... }
	public void func2(B b){ ...} // Erreur de compilation : Accessibilité incohérente : le type de paramètre 'B' est moins accessible que la méthode 'A.func2(B)' 
}

internal class B{
	public void func3(A a){		
		a.func2(this); 
	}
}
```

Mais nous ne pouvons pas ?. B est une classe internal, donc elle ne peut pas faire partie de la signature d'une fonction publique d'une classe publique.

Voici les solutions que j'ai trouvées, classées par facilité :

1. Marquer la fonction avec le mot-clé internal

```c#
public class A{
	public void func1(){ }
	internal void func2(B b){}
}

internal class B{
	public void func3(A a){		
		a.func2(this); 
	}
	
}
```

2. Créer une interface internal

```c#
internal interface IA2{
	void func2(B b);
}

public class A:IA2{
	public void func1(){
		var b = new B();
		b.func3(this);
	}
	void IA2.func2(B b){} //implémenter IA2 explicitement car func2 ne peut pas être public
}

internal class B{
	public void func3(A a){ 
		((IA2)a).func2(this); //utiliser l'interface au lieu de la classe pour accéder à func2	
	}
	
}
```

3. Extraire A.func2 vers une autre classe internal et l'utiliser à la place de A.func2.

```c#
internal class C{
	public void func2(B b){
	 //extraire A:func2 ici
	}
}

public class A{
	public void func1(){}
	private void func2(B b){
		new C().func2(b); 
	}
}

internal class B{
	public void func3(){	//a n'est plus nécessaire	
		new C().func2(this); //utiliser la classe internal au lieu de la fonction privée
	}
	
}
```

4. Découpler la fonction des classes internal et la rendre publique. Cela dépend beaucoup de ce que fait la fonction avec ses entrées. Découpler les classes internal peut être très facile, très difficile et même impossible (sans ruiner le design).

#### Mais nous n'avons pas de classes publiques, nous utilisons des interfaces...

Regardons un exemple plus réaliste :

```c#
public interface IA{
	void func1();
}

internal class A : IA {
	public void func1(){}
	private void func2(B b){}
}

internal class B{
	public void func3(IA a){		
		a.func2(this);  //Erreur de compilation IA' ne contient pas de définition pour 'func2' et aucune méthode d'extension 'func2' acceptant un premier argument de type 'IA' n'a pu être trouvée

	}	
}
```

Voyons comment les solutions précédentes sont adaptées à cet exemple :

1. Marquer la fonction avec Internal. Cela signifie que vous devrez caster vers la classe pour appeler la fonction, donc **cela ne fonctionnera que si la classe A est la seule à implémenter l'interface**, ce qui signifie que IA n'est pas mocké dans les tests et qu'il n'y a pas une autre classe de production qui implémente IA.

```c#
public interface IA{
	void func1();
}

internal class A : IA {
	public void func1(){}
	internal void func2(B b){}
}

internal class B{
	public void func3(IA a){		
		((A)a).func2(this); //caster vers A pour accéder à func2

	}	
}
```

2. Créer une interface internal qui étend l'interface publique.

```c#
internal interface IExtendedA : IA{
	void func2(B b);
}

public interface IA{
	void func1();
}

internal class A : IExtendedA {
	public void func1(){}
	public void func2(B b){}
}

internal class B{
	public void func3(IExtendedA a){		
		a.func2(this);

	}	
}
```

3. Extraire A.func2 vers une autre classe internal et l'utiliser à la place de A.func2.

4. Découpler la fonction des classes internal et l'ajouter à l'interface publique.

Nous pouvons voir que **le mot-clé internal est la solution la plus facile**, mais il existe d'autres solutions utilisant **les blocs de construction traditionnels de la POO : classes et interfaces**. Nous pouvons voir que la 2ème solution — ajouter une interface internal n'est pas beaucoup plus difficile que de marquer la fonction avec le mot-clé internal.

### Pourquoi ne pas utiliser le mot-clé internal ?

Comme je l'ai montré dans les exemples précédents, utiliser **le mot-clé internal est la solution la plus facile**. Mais vous allez avoir du mal à l'avenir si vous devez :

* Déplacer la classe publique A vers une autre DLL (puisque le mot-clé internal ne s'appliquera plus à la même dll)
* Créer une autre classe de production qui implémente IA
* Mock IA dans les tests

Vous pourriez penser « Mais ce n'est qu'une ligne de code, moi ou quelqu'un d'autre peut la changer facilement si nécessaire ». **Maintenant**, vous avez **une** ligne de code qui ressemble à ceci :

```c#
((MyClass)a).internalFunction
```

mais si d'autres doivent appeler cette fonction aussi, cette **ligne sera copiée-collée** à l'intérieur de la DLL.

### Ma conclusion

Je pense que marquer un membre de classe avec le mot-clé internal **est une mauvaise pratique**. Dans les exemples que j'ai montrés ci-dessus, c'est la solution **la plus facile**, MAIS cela peut causer des problèmes à l'avenir. Créer une **interface internal est presque aussi facile et plus explicite.**

### Comparaison avec C++

Le mot-clé « friend » en C++ est similaire au mot-clé internal en C#. Il permet à une classe ou une fonction d'accéder aux membres privés d'une classe. La différence est qu'il permet l'accès à une **classe ou fonction spécifique** et **non** à **toutes les classes dans la même DLL**. À mon avis, c'est une meilleure solution que le mot-clé internal en C#.

### Lectures complémentaires

[**Utilisations pratiques du mot-clé "internal" en C#**](https://stackoverflow.com/questions/165719/practical-uses-for-the-internal-keyword-in-c-sharp)  
[**Pourquoi C# ne fournit-il pas le mot-clé 'friend' à la manière de C++ ?**](https://stackoverflow.com/questions/203616/why-does-c-sharp-not-provide-the-c-style-friend-keyword)
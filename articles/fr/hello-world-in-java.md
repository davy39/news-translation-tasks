---
title: Java pour débutants – Comment créer votre premier programme "Hello World"
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-04-06T16:08:13.000Z'
originalURL: https://freecodecamp.org/news/hello-world-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/altumcode-XMFZqrGyV-Q-unsplash.jpg
tags:
- name: beginner
  slug: beginner
- name: Java
  slug: java
seo_title: Java pour débutants – Comment créer votre premier programme "Hello World"
seo_desc: "If you are learning a programming language, the first thing you do is print\
  \ something in the terminal/command prompt. \nAnd that first thing is likely printing\
  \ \"Hello World\" in the terminal. So that's what I'll show you how to do here if\
  \ you are learn..."
---

Si vous apprenez un langage de programmation, la première chose que vous faites est d'afficher quelque chose dans le terminal/invite de commande. 

Et cette première chose est probablement d'afficher "Hello World" dans le terminal. C'est donc ce que je vais vous montrer comment faire ici si vous apprenez Java pour la première fois.

## 🧵 Ce que vous devez savoir d'abord

Avant de commencer à écrire du code Java, il y a quelques choses que vous devez savoir.

Tout d'abord, les fichiers sources Java ont l'extension `.java`. Une extension est quelque chose qui est ajouté à la fin du nom de fichier, et elle indique de quel type de fichier il s'agit réellement. 

Différents langages de programmation ont différentes extensions de fichiers qui aident les compilateurs/interpréteurs à identifier quel type de données de programmation le fichier contient. Ces extensions aident également à identifier si ce compilateur/interpréteur spécifique peut supporter ce format de fichier ou non.

Deuxièmement, vous devez vous assurer que vous avez correctement installé le compilateur Java (JDK) sur votre ordinateur. Si vous ne savez rien à ce sujet, alors consultez simplement [cet article](https://www.freecodecamp.org/news/how-to-install-java-on-windows/) (si vous êtes un utilisateur Windows).

De plus, lorsque nous compilons le code source Java (fichier `.java`), il génère un fichier `.class`. Plus tard, nous exécutons le fichier `.class`. Puisque Java est un langage indépendant de la plateforme (ce qui signifie que vous pouvez exécuter le programme Java à partir de n'importe quel système d'exploitation si vous avez installé les composants nécessaires), vous pouvez simplement exécuter ce fichier `.class` à partir de n'importe quel système d'exploitation que vous voulez !

Vous pouvez utiliser n'importe quel éditeur de texte / IDE que vous voulez. Mais je préfère [Visual Studio Code](https://code.visualstudio.com/) ou [IntelliJ IDEA IDE](https://www.jetbrains.com/idea/).

Et enfin, le nom du fichier Java et le nom de la classe publique doivent être identiques.

## 📝 Comment créer votre premier fichier Java

Maintenant, vous allez apprendre comment créer un fichier Java. Dans cet exemple, je vais créer un fichier nommé `Main.java`.

Vous pouvez écrire le code suivant dans ce fichier :

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

Ensuite, exécutez simplement le code. Si vous utilisez l'extension `Code Runner` pour exécuter ce code avec VS Code, il compilera d'abord le code puis créera le fichier `Main.class`. Plus tard, il exécutera le fichier `Main.class`. 

Comme cela se fait automatiquement, vous ne verrez presque aucun délai. Mais si vous voulez devenir un meilleur programmeur et exécuter le code à partir de votre terminal, alors [assurez-vous de consulter cet article](https://www.freecodecamp.org/news/how-to-execute-and-run-java-code/). 

### 😉 Explication du code

Dans le code ci-dessus, nous avons utilisé la classe publique, et le nom de la classe publique doit être identique au nom du fichier `.java`. Si vous avez utilisé un nom de fichier différent, alors le nom de la classe publique devra également être différent. 

Par exemple, si vous utilisez `MyJavaFile.java`, alors la classe publique serait comme ceci : `public class MyJavaFile`. Java est un langage sensible à la casse, donc assurez-vous de vérifier que les lettres majuscules et minuscules sont également identiques.

Ensuite, nous avons besoin de la méthode main. Le compilateur Java commence toujours à compiler à partir de la méthode main. La méthode main est `public static void main(String[] args)`. 

Pour afficher quelque chose dans le terminal, nous utilisons la méthode `print`. Ici, la méthode print est `System.out.println("")`. Vous devez fournir la chose que vous voulez afficher dans le terminal entre les guillemets doubles. 

Nous utilisons le point-virgule ( `;` ) pour spécifier la fin d'une instruction. Donc nous utilisons le point-virgule après la fin de chaque instruction.

Et voilà ! Je discuterai de plus de réglages et de sujets avancés dans d'autres articles. 😁

## 📹 Tutoriel vidéo

Si vous êtes le genre de personne qui aime apprendre à partir de vidéos, alors j'ai également créé une vidéo juste pour vous ! Assurez-vous de la consulter : 

%[https://youtu.be/U__ljdoYDYY]

De plus, je suis en train de créer une playlist où je publie tout le contenu lié à Java. Assurez-vous de consulter la [playlist ici](https://www.youtube.com/playlist?list=PL7ZCWbO2Dbl44-HqGWnRl7u28Qb1ac-Jk) et obtenez tout le code à partir de [ce dépôt GitHub](https://github.com/FahimFBA/everything-of-java).

## 😀 Conclusion

Merci d'avoir lu cet article entier. J'espère que cela vous aidera à commencer votre voyage en programmation Java.

Vous pouvez me suivre sur :

* GitHub : [FahimFBA](https://github.com/FahimFBA)
* LinkedIn : [fahimfba](https://www.linkedin.com/in/fahimfba/)
* Twitter : [Fahim_FBA](https://twitter.com/Fahim_FBA)
* YouTube : [Code With FahimFBA](https://www.youtube.com/@FahimAmin?sub_confirmation=1)
* Site web : [https://fahimbinamin.com/](https://fahimbinamin.com/)

Si vous voulez me soutenir, alors [vous pouvez aussi m'offrir un café !](https://www.buymeacoffee.com/fahimbinamin)

Couverture : Photo par [AltumCode](https://unsplash.com/@altumcode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/photos/XMFZqrGyV-Q?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
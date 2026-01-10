---
title: Getline en C++ – Exemple de la fonction cin getline()
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-04T20:06:07.000Z'
originalURL: https://freecodecamp.org/news/getline-in-cpp-cin-getline-function-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/getline.png
tags:
- name: C++
  slug: c-2
seo_title: Getline en C++ – Exemple de la fonction cin getline()
seo_desc: 'In this article, we''ll talk about the getline() function in C++. This
  is an inbuilt function that accepts single and multiple character inputs.

  When working with user input in C++, the cin object allows us to get input information
  from the user. But ...'
---

Dans cet article, nous allons parler de la fonction `getline()` en C++. Il s'agit d'une fonction intégrée qui accepte les entrées de caractères uniques et multiples.

Lorsque l'on travaille avec les entrées utilisateur en C++, l'objet `cin` nous permet d'obtenir des informations d'entrée de l'utilisateur. Mais lorsque nous essayons d'afficher l'entrée de l'utilisateur qui contient plusieurs valeurs, il ne retourne que le premier caractère.

Cela se produit parce que le compilateur C++ suppose que tout espace blanc termine le programme lors de la réception de l'entrée. C'est-à-dire que "My name is Ihechikara" ne retournerait que "My" lors de l'affichage.

Voici un meilleur exemple :

```c++
#include <iostream>
using namespace std;

int main() {

    string bio;
    
    
    // Information enregistrée dans la console
    cout << "Parlez-nous de vous : ";
    
    
    /* Cela invite l'utilisateur à saisir une chaîne et j'ai tapé ceci : "JavaScript is my favorite language"
    */
    cin >> bio;
    
    
    /* Lors de l'affichage de la bio saisie ci-dessus, seul "JavaScript" a été affiché
    */
    cout << "Votre bio dit : " << bio;
    // Votre bio dit : JavaScript 

    
}
```

Dans le code ci-dessus, l'utilisateur est invité à saisir sa bio. Il a saisi "JavaScript is my favorite language". Mais lorsque la bio a été affichée dans la console, seul "JavaScript" a été affiché.

Ensuite, nous verrons comment utiliser la fonction `getline()` pour obtenir le reste des caractères de la chaîne.

## Exemple de la fonction C++ getline()

Dans cette section, nous verrons un exemple pratique de l'utilisation de la fonction `getline()`.

```c++
#include <iostream>
using namespace std;

int main() {

    string bio;
    
    cout << "Parlez-nous de vous : ";
    
    getline(cin, bio);
    
    cout << "Votre bio dit : " << bio;
}
```

Dans l'exemple ci-dessus, nous avons passé deux paramètres dans la fonction `getline()` : `getline(cin, bio);`. Le premier paramètre est l'objet `cin` tandis que le second est la variable de chaîne `bio`.

Lorsque vous exécutez le code, vous serez invité à saisir du texte. Après avoir fait cela, appuyez sur Entrée et voyez le résultat qui contient tout le texte de votre entrée au lieu de seulement le premier caractère.

Dans mon cas, j'ai saisi une chaîne avec plusieurs caractères et je l'ai affichée dans la console. Allez-y et essayez pour voir comment cela fonctionne.

Avec cela, vous pouvez travailler efficacement avec les entrées utilisateur dans vos programmes.

## Conclusion

Dans cet article, nous avons parlé de la fonction `getline()` qui nous permet d'obtenir plusieurs caractères à partir de l'entrée d'un utilisateur.

Nous avons d'abord vu ce qui se passe lorsque nous obtenons une chaîne avec plusieurs caractères d'un utilisateur – seul le premier caractère est retourné.

Nous avons ensuite vu comment obtenir tous les caractères de la chaîne en utilisant la fonction `getline()` qui prend deux paramètres – l'objet `cin` et la variable de chaîne.

Bon codage !
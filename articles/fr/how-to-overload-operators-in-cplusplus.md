---
title: Comment surcharger les opérateurs en C++
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2021-03-15T13:52:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-overload-operators-in-cplusplus
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6043a406a7946308b76830ab.jpg
tags:
- name: C++
  slug: c-2
- name: General Programming
  slug: programming
seo_title: Comment surcharger les opérateurs en C++
seo_desc: "Classes are user-defined types. They allow us to represent the meaning\
  \ of various entities. Defining an operator for a class gives us a better way to\
  \ deal with objects. \nSo how can we define operators for our classes, and how should\
  \ we use such opera..."
---

[Les classes](https://www.freecodecamp.org/news/how-classes-work-in-cplusplus/) sont des types définis par l'utilisateur. Elles nous permettent de représenter la signification de diverses entités. Définir un opérateur pour une classe nous donne un meilleur moyen de manipuler les objets.

Alors, comment pouvons-nous définir des opérateurs pour nos classes, et comment devrions-nous utiliser de tels opérateurs ? Je vais vous montrer comment faire dans cet article.

Commençons !

## Qu'est-ce que les opérateurs en C++ ?

Les opérateurs sont des symboles utilisés pour effectuer des opérations sur divers opérandes. Par exemple :

```c++
int x = 5;
int y = 10;

int z = x + y;
```

Dans l'exemple ci-dessus, `+` est un opérateur qui effectue l'opération d'addition sur les deux opérandes `x` et `y`.

## Qu'est-ce que la surcharge d'opérateurs en C++ ?

Examinons d'abord un exemple.

```c++
int x=5;
int y= 10;

int z = x+y;//z==15

string s1="Abhi";
string s2="gautam";

string s3= s1+s3;//s3==Abhigautam

```

Vous êtes-vous déjà demandé pourquoi ce type de code **** donne `z== 15` et `s3== Abhigautam` ? C'est parce que les opérateurs ont des significations différentes pour différents types d'opérandes.

Pour un type entier, l'opérateur `+` donne la somme de deux nombres, et pour le type chaîne, il les concatène (les joint).

Ainsi, la surcharge d'opérateurs consiste à donner une nouvelle signification à un opérateur. Mais :

<ul>
    <li>Vous ne pouvez pas définir une nouvelle signification pour un opérateur pour un type intégré.</li>
    <li>Vous ne pouvez pas créer de nouveaux opérateurs.</li>
</ul>

Donc, en gros, ce que je veux dire, c'est que vous ne pouvez pas redéfinir un opérateur et vous ne pouvez pas créer un nouvel opérateur non plus.

Si vous souhaitiez créer un nouvel opérateur comme `**` pour des fins exponentielles, vous ne pourriez pas le faire.

### Comment fonctionne la surcharge ?

Ainsi, la surcharge d'opérateurs nous permet de définir la signification d'un opérateur existant (notez que vous ne pouvez pas surcharger certains opérateurs) pour les opérandes d'un type défini par l'utilisateur (par exemple, une classe est un type défini par l'utilisateur).

Les opérateurs surchargés sont simplement des fonctions (mais d'un type spécial) avec un mot-clé spécial `operator` suivi du symbole de l'opérateur à surcharger.

```c++
/*surcharge de + pour un objet de type classe*/

return_type operator+(params..){}
```

Comme je l'ai déjà mentionné, les opérateurs surchargés sont simplement un type spécial de fonctions. Ils doivent avoir un type de retour, et les paramètres sont toujours optionnels (selon leurs exigences).

Alors, surchargeons quelques opérateurs pour notre classe maintenant pour voir comment cela fonctionne :

```c++
class Complex{
int real,imag;
public:
Complex(int re,int im):real(re),imag(im){}
Complex(){
real = 0;
imag = 0;
}
void display() const;
//surcharge des opérateurs
Complex operator+(const Complex);
Complex operator-(const Complex);
};
```

Ici, nous avons deux fonctions en tant que fonction membre avec la syntaxe mentionnée ci-dessus. Alors, comprenons d'abord la syntaxe.

```
Complex operator+(const Complex);
Complex operator-(const Complex);
```

Les deux fonctions ici retournent un objet de type `Complex`. Le mot-clé operator suivi du symbole de l'opérateur nous indique quel opérateur est surchargé.

Nous avons également une fonction d'affichage qui nous permet de voir l'affichage des valeurs des membres de l'objet. Nous remplacerons cela par l'opérateur surchargé (`<<`) plus tard dans l'article.

```c++
void Complex::display(){
if(imag<0)
cout<<real<<imag<<"i"<<'\n';
else
cout<<real<<'+'<<imag<<"i"<<'\n';
}
```

## Comment surcharger l'opérateur binaire Plus (+) en C++

Surchargeons maintenant l'opérateur `+`.

```c++
Complex Complex::operator+(const Complex c1){
Complex temp;
temp.real = real + c1.real;
temp.imag = imag + c1.imag;
return temp;
}
```

Après cette définition, si nous faisons ce qui suit :

```
Complex c1(2,2);
Complex c2(2,2);
Complex c3 = c1+c2;
c3.display();
```

Il devrait être clair que c1+c2 est équivalent à ceci :

```c++
c1.operator+(c2);


```

et

```c++
operator(c1,c2);
```

Après l'appel à la fonction membre display, la sortie ressemble à ceci :

```
4+4i
```

Donc, en gros, nous avons défini la signification de l'opérateur `+` pour notre objet de type `Complex`.

## Comment surcharger l'opérateur binaire Moins (-) en C++

Maintenant, surchargeons l'opérateur moins.

```c++
Complex Complex::operator-(const Complex c1){
Complex temp;
temp.real = real - c1.real;
temp.imag = imag - c1.imag;
return temp;
}
```

C'est ainsi que nous surchargeons les opérateurs en C++. Discutons maintenant du nombre de paramètres qui doivent être passés à la fonction.

Le nombre de paramètres passés à la fonction est égal au nombre d'opérandes pris par l'opérateur.

Mais dans le cas d'une fonction membre (non statique), le nombre de paramètres est réduit de un. Cela est dû au fait que la fonction membre (non statique) connaît d'une certaine manière l'objet pour lequel elle a été invoquée.

N'est-ce pas amusant ? Surchargeons maintenant plus d'opérateurs pour notre classe.

```c++
bool operator!=(const Complex);
bool operator==(const Complex);
```

## Comment surcharger l'opérateur Différent De (!=) en C++

Ainsi, notre définition de fonction pour la fonction de l'opérateur `!=` sera la suivante :

```c++
bool Complex::operator!=(const Complex c1){
if(real!=c1.real || real!=c1.imag){
    return true;
}
else
return false;
}
```

Le type de retour est un booléen, donc il retourne soit vrai soit faux.

## Comment surcharger l'opérateur Égal À (==) en C++

De même pour l'opérateur `==` :

```c++
bool Complex::operator==(const Complex c1){
  if(real == c1.real && imag == c1.imag){
    return true;
  }
  else
  return false;
}
```

### Comment surcharger l'opérateur Get From (<<) en C++

Alors, surchargeons maintenant l'opérateur `<<`. Ce sera amusant !

Regardons d'abord la déclaration de la fonction :

```c++
friend ostream& operator<<(ostream&,Complex);

```

Il y a quelques changements par rapport aux fonctions précédentes. Comprenons cela plus clairement.

La fonction est une fonction amie. Cela signifie qu'elle n'est pas dans la portée d'une classe et ne peut pas être invoquée par un objet. De plus, la fonction retourne une référence à l'objet ostream et prend deux arguments en tant que paramètres :

<ul>
    <li>Référence à un objet ostream.</li>
    <li>Référence à un objet de type classe.</li>
 <ul/>

Vous vous demandez peut-être pourquoi une fonction amie ? Parlons de pourquoi nous avons besoin de fonctions amies maintenant.

Si une fonction opérateur est une fonction membre (non statique), alors l'opérande du côté gauche sera lié au pointeur **`this`** qui fait référence à l'objet qui appelle la fonction.

Mais nous ne voulons pas que cela se produise dans le cas de l'opérateur `<<` car l'opérande du côté gauche pour l'opérateur `<<` devrait être `cout`. Et `cout` est un objet de ostream. Donc, pour éviter la liaison avec l'objet, nous avons utilisé une fonction amie ici.

Nous pouvons définir l'opérateur `<<` comme ceci pour notre classe.

```c++
ostream& operator<<(ostream& os,Complex c1){
if(c1.imag<0)
os<<c1.real<<c1.imag<<"i";
else
os<<c1.real<<"+"<<c1.imag<<"i";

return os;
}
```

Ainsi, de cette manière, nous pouvons surcharger la plupart des opérateurs pour notre classe.

## Certains opérateurs ne peuvent pas être surchargés en C++

Nous ne pouvons pas surcharger les opérateurs suivants en C++ :

<ul>
    <li>:: (opérateur de résolution de portée)</li>
    <li>. (opérateur point)</li>
    <li>.* (sélection de membre via un pointeur)</li>
</ul>

> Ils prennent un nom, plutôt qu'une valeur, comme deuxième opérande et fournissent un moyen principal de faire référence aux membres. Leur permettre d'être surchargés entraînerait des subtilités. [Stroustroup, 1994]

De plus, l'opérateur ternaire (?:) et les opérateurs nommés **sizeof** et **typeid** ne peuvent pas non plus être surchargés.

### Erreurs à garder à l'esprit

N'oubliez pas non plus que la déclaration suivante est une erreur :

```c++
int operator+(int,int);
/*erreur : ne peut pas redéfinir les opérateurs pour un type intégré.*/
```

Comme mentionné précédemment, redéfinir un opérateur pour un type intégré est une erreur.

### Un dernier point

Vous ne devriez pas surcharger les opérateurs comme `&&` et `||`. Cela est dû au fait que ces opérateurs ont un ordre particulier dans lequel un opérande est évalué. Puisque les opérateurs surchargés sont simplement des appels de fonction, nous ne pouvons pas garantir l'ordre d'évaluation des opérandes.

## C'est tout !

Bon codage !

Vous pouvez lire mes autres blogs [ici.](https://abhilekhblogs.blogspot.com/)
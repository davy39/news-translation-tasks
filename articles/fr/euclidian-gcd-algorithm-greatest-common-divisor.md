---
title: 'Algorithme d''Euclide : PGCD (Plus Grand Commun Diviseur) Expliqué avec des
  Exemples en C++ et Java'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-30T18:38:00.000Z'
originalURL: https://freecodecamp.org/news/euclidian-gcd-algorithm-greatest-common-divisor
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/euclid-image.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: 'Algorithme d''Euclide : PGCD (Plus Grand Commun Diviseur) Expliqué avec
  des Exemples en C++ et Java'
seo_desc: 'For this topic you must know about Greatest Common Divisor (GCD) and the
  MOD operation first.

  Greatest Common Divisor (GCD)

  The GCD of two or more integers is the largest integer that divides each of the
  integers such that their remainder is zero.

  Ex...'
---

Pour ce sujet, vous devez d'abord connaître le Plus Grand Commun Diviseur (PGCD) et l'opération MOD.

#### Plus Grand Commun Diviseur (PGCD)

Le PGCD de deux ou plusieurs entiers est le plus grand entier qui divise chacun des entiers de sorte que leur reste soit zéro.

Exemple - 
PGCD de 20, 30 = 10  _(10 est le plus grand nombre qui divise 20 et 30 avec un reste de 0)_  
PGCD de 42, 120, 285 = 3  _(3 est le plus grand nombre qui divise 42, 120 et 285 avec un reste de 0)_

#### Opération "mod"

L'opération mod vous donne le reste lorsque deux entiers positifs sont divisés. Nous l'écrivons comme suit - 
`A mod B = R`

Cela signifie que diviser A par B vous donne le reste R, ce qui est différent de votre opération de division qui vous donne le quotient.

Exemple - 
7 mod 2 = 1  _(Diviser 7 par 2 donne un reste de 1)_  
42 mod 7 = 0  _(Diviser 42 par 7 donne un reste de 0)_

Avec les deux concepts ci-dessus compris, vous comprendrez facilement l'algorithme d'Euclide.

### Algorithme d'Euclide pour le Plus Grand Commun Diviseur (PGCD)

L'algorithme d'Euclide trouve le PGCD de 2 nombres.

Vous comprendrez mieux cet algorithme en le voyant en action. Supposons que vous souhaitiez calculer le PGCD de 1220 et 516, appliquons l'algorithme d'Euclide - 

Supposons que vous souhaitiez calculer le PGCD de 1220 et 516, appliquons l'algorithme d'Euclide - 

![Exemple d'Euclide](https://cdn-media-1.freecodecamp.org/imgr/aa8oGgP.png)

Pseudo-code de l'algorithme -  
Étape 1 : **Soit `a, b` les deux nombres**  
Étape 2 : **`a mod b = R`**  
Étape 3 : **Soit `a = b` et `b = R`**  
Étape 4 : **Répéter les étapes 2 et 3 jusqu'à ce que `a mod b` soit supérieur à 0**  
Étape 5 : **PGCD = b**  
Étape 6 : Fin

Code JavaScript pour effectuer le PGCD - 

```
function gcd(a, b) {
  var R;
  while ((a % b) > 0)  {
    R = a % b;
    a = b;
    b = R;
  }
  return b;
}

```

Code JavaScript pour effectuer le PGCD en utilisant la récursivité - 

```
function gcd(a, b) {
  if (b == 0)
    return a;
  else
    return gcd(b, (a % b));
}

```

Code C pour effectuer le PGCD en utilisant la récursivité

```
int gcd(int a, int b) 
{ 
    // Tout divise 0  
    if (a == 0) 
       return b; 
    if (b == 0) 
       return a; 
  
    // cas de base 
    if (a == b) 
        return a; 
  
    // a est plus grand 
    if (a > b) 
        return gcd(a-b, b); 
    return gcd(a, b-a); 
}

```

Code C++ pour effectuer le PGCD - 

```
int gcd(int a,int b) {
  int R;
  while ((a % b) > 0)  {
    R = a % b;
    a = b;
    b = R;
  }
  return b;
}

```

Code Python pour effectuer le PGCD en utilisant la récursivité

```
def gcd(a, b):
  if b == 0:
    return a:
  else:
    return gcd(b, (a % b))

```

Code Java pour effectuer le PGCD en utilisant la récursivité

```
static int gcd(int a, int b)
{
  if(b == 0)
  {
    return a;
  }
  return gcd(b, a % b);
}

```

Vous pouvez également utiliser l'algorithme d'Euclide pour trouver le PGCD de plus de deux nombres. Puisque le PGCD est associatif, l'opération suivante est valide - `PGCD(a,b,c) == PGCD(PGCD(a,b), c)`

Calculez le PGCD des deux premiers nombres, puis trouvez le PGCD du résultat et du nombre suivant. Exemple - `PGCD(203,91,77) == PGCD(PGCD(203,91),77) == PGCD(7, 77) == 7`

Vous pouvez trouver le PGCD de `n` nombres de la même manière.

## Qu'est-ce que l'algorithme d'Euclide étendu ?

Il s'agit d'une extension de l'algorithme d'Euclide. Il calcule également les coefficients x, y tels que

ax+by = pgcd(a,b)

x et y sont également connus comme les coefficients de l'identité de Bézout.

Code C pour l'algorithme d'Euclide étendu

```
struct Triplet{
	int pgcd;
	int x;
	int y;
};
Triplet pgcdEtenduEuclide(int a,int b){
	//Cas de base
	if(b==0){
		Triplet maReponse;
		maReponse.pgcd = a;
		maReponse.x = 1;
		maReponse.y = 0;
		return maReponse;

	}
	Triplet petiteReponse = pgcdEtenduEuclide(b,a%b);
	//Euclide étendu dit

	Triplet maReponse;
	maReponse.pgcd = petiteReponse.pgcd;
	maReponse.x  = petiteReponse.y;
	maReponse.y = (petiteReponse.x - ((a/b)*(petiteReponse.y)));
	return maReponse;	
}

```
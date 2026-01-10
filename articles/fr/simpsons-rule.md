---
title: 'La règle de Simpson : la formule et son fonctionnement'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T22:16:00.000Z'
originalURL: https://freecodecamp.org/news/simpsons-rule
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d62740569d1a4ca3781.jpg
tags:
- name: Math
  slug: math
seo_title: 'La règle de Simpson : la formule et son fonctionnement'
seo_desc: 'Simpson''s rule is a method for numerical integration. In other words,
  it''s the numerical approximation of definite integrals.

  Simpson''s rule is as follows:


  In it,


  f(x) is called the integrand

  a = lower limit of integration

  b = upper limit of integr...'
---

La règle de Simpson est une méthode d'intégration numérique. En d'autres termes, c'est l'approximation numérique des intégrales définies.

La règle de Simpson est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim1.png)

Dans celle-ci,

* `f(x)` est appelé l'_intégrande_
* `a` = limite inférieure d'intégration
* `b` = limite supérieure d'intégration

## La règle de Simpson 1/3

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim01.jpg)

Comme le montre le diagramme ci-dessus, l'intégrande `f(x)` est approximé par un polynôme du second ordre ; l'interpolant quadratique étant `P(x)`.

L'approximation est la suivante,

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim3.png)

En remplaçant `(b-a)/2` par `h`, nous obtenons,

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim4.png)

Comme vous pouvez le voir, il y a un facteur de `1/3` dans l'expression ci-dessus. C'est pourquoi elle est appelée **Règle de Simpson 1/3**.

Si une fonction est très oscillante ou manque de dérivées en certains points, alors la règle ci-dessus peut échouer à produire des résultats précis. 

Une façon courante de gérer cela est d'utiliser l'approche de la _règle composite de Simpson_. Pour ce faire, divisez `[a,b]` en petits sous-intervalles, puis appliquez la règle de Simpson à chaque sous-intervalle. Ensuite, additionnez les résultats de chaque calcul pour produire une approximation sur l'intégrale entière. 

Si l'intervalle `[a,b]` est divisé en `n` sous-intervalles, et que `n` est un nombre pair, la règle composite de Simpson est calculée avec la formule suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim7.png)

où **x<sub>j</sub> = a+jh** pour **j = 0,1,…,n-1,n** avec **h=(b-a)/n** ; en particulier, **x<sub>0</sub> = a** et **x<sub>n</sub> = b**.

### Exemple en C++ :

Pour approximer la valeur de l'intégrale donnée ci-dessous où n = 8 :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim9.png)

```c++
#include<iostream>
#include<cmath>
using namespace std;

float f(float x)
{
	return x*sin(x);	//Définir la fonction f(x)
}

float simpson(float a, float b, int n)
{
	float h, x[n+1], sum = 0;
	int j;
	h = (b-a)/n;
	
	x[0] = a;
	
	for(j=1; j<=n; j++)
	{
		x[j] = a + h*j;
	}
	
	for(j=1; j<=n/2; j++)
	{
		sum += f(x[2*j - 2]) + 4*f(x[2*j - 1]) + f(x[2*j]);
	}
	
	return sum*h/3;
}

int main()
{
	float a,b,n;
	a = 1;		//Entrez la limite inférieure a
	b = 4;		//Entrez la limite supérieure b
	n = 8;		//Entrez la longueur de pas n
	if (n%2 == 0)
		cout<<simpson(a,b,n)<<endl;
	else
		cout<<"n doit être un nombre pair";
	return 0;
}
```

## La règle de Simpson 3/8

La règle de Simpson 3/8 est similaire à la règle de Simpson 1/3, la seule différence étant que, pour la règle 3/8, l'interpolant est un polynôme cubique. Bien que la règle 3/8 utilise une valeur de fonction supplémentaire, elle est environ deux fois plus précise que la règle 1/3.

La règle de Simpson 3/8 stipule :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim6.png)

En remplaçant `(b-a)/3` par `h`, nous obtenons,

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim5.png)

La règle de Simpson 3/8 pour n intervalles (n doit être un multiple de 3) :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim8.png)

où **x<sub>j</sub> = a+jh** pour **j = 0,1,…,n-1,n** avec **h=(b-a)/n** ; en particulier, **x<sub>0</sub> = a** et **x<sub>n</sub> = b**.
---
title: Descente de Gradient – Exemple d'Algorithme d'Apprentissage Automatique
subtitle: ''
author: Salim Oyinlola
co_authors: []
series: null
date: '2022-10-24T13:53:51.000Z'
originalURL: https://freecodecamp.org/news/gradient-descent-machine-learning-algorithm-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-pixabay-159751.jpg
tags:
- name: algorithms
  slug: algorithms
- name: 'Gradient-Descent '
  slug: gradient-descent
- name: Machine Learning
  slug: machine-learning
seo_title: Descente de Gradient – Exemple d'Algorithme d'Apprentissage Automatique
seo_desc: "What is the Gradient Descent Algorithm?\nGradient descent is probably the\
  \ most popular machine learning algorithm. At its core, the algorithm exists to\
  \ minimize errors as much as possible. \nThe aim of gradient descent as an algorithm\
  \ is to minimize th..."
---

## Qu'est-ce que l'Algorithme de Descente de Gradient ?

La descente de gradient est probablement l'algorithme d'apprentissage automatique le plus populaire. À sa base, l'algorithme existe pour minimiser les erreurs autant que possible. 

Le but de la descente de gradient en tant qu'algorithme est de minimiser la fonction de coût d'un modèle. Nous pouvons le comprendre à partir des significations des mots « Gradient » et « Descente ». 

Alors que le gradient signifie l'écart entre deux points définis (c'est-à-dire la fonction de coût dans ce contexte), la descente fait référence à un mouvement vers le bas en général (c'est-à-dire minimiser la fonction de coût dans ce contexte). 

Ainsi, dans le contexte de l'apprentissage automatique, la Descente de Gradient fait référence à la tentative itérative de minimiser l'erreur de prédiction d'un modèle d'apprentissage automatique en ajustant ses paramètres pour obtenir l'erreur la plus petite possible.

Cette erreur est connue sous le nom de Fonction de Coût. La fonction de coût est une représentation de la réponse à la question « de combien la valeur prédite diffère-t-elle de la valeur réelle ? ». Alors que la manière d'évaluer les fonctions de coût diffère souvent pour différents modèles d'apprentissage automatique, dans un modèle de régression linéaire simple, il s'agit généralement de l'erreur quadratique moyenne du modèle.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-166.png)
_Un graphique 3D de la fonction de coût d'un modèle de régression linéaire simple avec M représentant le point minimum_

Il est important de noter que pour les modèles plus simples comme la régression linéaire, une représentation de la fonction de coût est généralement en forme de bol, ce qui facilite la détermination du point minimum. Cependant, ce n'est pas toujours le cas. Pour des modèles plus complexes (par exemple les réseaux de neurones), la représentation peut ne pas être en forme de bol. Il est possible que la fonction de coût ait plusieurs points minimum comme le montre l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-39.png)
_Un graphique 3D de la fonction de coût d'un réseau de neurones. Source : [Coursera](https://www.coursera.org/lecture/machine-learning/gradient-descent-2f2PA)_

## Comment Fonctionne la Descente de Gradient ?

Tout d'abord, il est important de noter que, comme la plupart des processus d'apprentissage automatique, l'algorithme de descente de gradient est un processus itératif. 

En supposant que vous avez la fonction de coût pour un modèle de régression linéaire simple sous la forme _j(w,b)_ où _j est_ une fonction de _w_ et _b_, l'algorithme de descente de gradient fonctionne de telle sorte qu'il commence avec une première estimation aléatoire pour _w_ et _b_. L'algorithme continuera à ajuster les paramètres _w_ et _b_ dans une tentative d'optimiser la fonction de coût, _j._ 

Dans la régression linéaire, le choix des valeurs initiales n'a pas beaucoup d'importance. Un choix courant est zéro. 

L'analogie parfaite pour l'algorithme de descente de gradient qui minimise la fonction de coût _j_(_w_, _b_) et atteint son minimum local en ajustant les paramètres _w_ et _b_ est la randonnée vers le bas d'une montagne ou d'une colline (comme le montre le graphique 3D de la fonction de coût d'un modèle de régression linéaire simple montré précédemment). Ou, essayer d'atteindre le point le plus bas d'un parcours de golf. Dans les deux cas, ils feront des pas courts répétitifs jusqu'à ce qu'ils atteignent le bas de la montagne ou de la colline.

## La Formule de la Descente de Gradient

**Voici la formule pour la descente de gradient : b = a - γ Δ f(a)**

L'équation ci-dessus décrit ce que fait l'algorithme de descente de gradient. 

C'est-à-dire que _b_ est la prochaine position du randonneur tandis que _a_ représente la position actuelle. Le signe moins est pour la partie minimisation de l'algorithme de descente de gradient puisque le but est de minimiser l'erreur autant que possible. γ au milieu est un facteur connu sous le nom de taux d'apprentissage, et le terme Δf(a) est un terme de gradient qui définit la direction du point minimum. 

Ainsi, cette formule indique la prochaine position pour le randonneur/la personne sur le parcours de golf (c'est-à-dire la direction de la descente la plus raide). Il est important de noter que le terme _γΔ f(a)_ est soustrait de _a_ parce que le but est de se déplacer contre le gradient, vers le minimum local.

## Qu'est-ce que le Taux d'Apprentissage ?

Le taux d'apprentissage est le déterminant de la taille des pas que la descente de gradient prend dans la direction du minimum local. Il détermine la vitesse à laquelle l'algorithme se déplace vers les valeurs optimales de la fonction de coût. 

En raison de cela, le choix du taux d'apprentissage, γ, est important et a un impact significatif sur l'efficacité de l'algorithme. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-42.png)

Si le taux d'apprentissage est trop grand comme montré ci-dessus, dans une tentative de trouver le point optimal, il se déplace du point de gauche jusqu'au point de droite. Dans ce cas, vous voyez que la fonction de coût s'est aggravée.  

D'autre part, si le taux d'apprentissage est trop petit, alors la descente de gradient fonctionnera, bien que très lentement. 

Il est important de choisir soigneusement le taux d'apprentissage.

## Comment Implémenter la Descente de Gradient dans la Régression Linéaire

```python
import numpy as np
import matplotlib.pyplot as plt

class Linear_Regression:
	def __init__(self, X, Y):
		self.X = X
		self.Y = Y
		self.b = [0, 0]
	
	def update_coeffs(self, learning_rate):
		Y_pred = self.predict()
		Y = self.Y
		m = len(Y)
		self.b[0] = self.b[0] - (learning_rate * ((1/m) * np.sum(Y_pred - Y)))
		self.b[1] = self.b[1] - (learning_rate * ((1/m) * np.sum((Y_pred - Y) * self.X)))
        
	def predict(self, X=[]):
		Y_pred = np.array([])
		if not X: X = self.X
		b = self.b
		for x in X:
			Y_pred = np.append(Y_pred, b[0] + (b[1] * x))

		return Y_pred
	
	def get_current_accuracy(self, Y_pred):
		p, e = Y_pred, self.Y
		n = len(Y_pred)
		return 1-sum(
			[
				abs(p[i]-e[i])/e[i]
				for i in range(n)
				if e[i] != 0]
		)/n
	#def predict(self, b, yi):

	def compute_cost(self, Y_pred):
		m = len(self.Y)
		J = (1 / 2*m) * (np.sum(Y_pred - self.Y)**2)
		return J

	def plot_best_fit(self, Y_pred, fig):
				f = plt.figure(fig)
				plt.scatter(self.X, self.Y, color='b')
				plt.plot(self.X, Y_pred, color='g')
				f.show()


def main():
	X = np.array([i for i in range(11)])
	Y = np.array([2*i for i in range(11)])

	regressor = Linear_Regression(X, Y)

	iterations = 0
	steps = 100
	learning_rate = 0.01
	costs = []
	
	#ligne de meilleur ajustement initiale
	Y_pred = regressor.predict()
	regressor.plot_best_fit(Y_pred, 'Initial Best Fit Line')
	

	while 1:
		Y_pred = regressor.predict()
		cost = regressor.compute_cost(Y_pred)
		costs.append(cost)
		regressor.update_coeffs(learning_rate)
		
		iterations += 1
		if iterations % steps == 0:
			print(iterations, "epochs elapsed")
			print("Current accuracy is :",
				regressor.get_current_accuracy(Y_pred))

			stop = input("Do you want to stop (y/*)??")
			if stop == "y":
				break

	#ligne de meilleur ajustement finale
	regressor.plot_best_fit(Y_pred, 'Final Best Fit Line')

	#graphique pour vérifier que la fonction de coût diminue
	h = plt.figure('Verification')
	plt.plot(range(iterations), costs, color='b')
	h.show()

	# si l'utilisateur veut prédire en utilisant le régresseur :
	regressor.predict([i for i in range(10)])

if __name__ == '__main__':
	main()

```

À sa base, vous pouvez voir que le bloc de code entraîne un algorithme de descente de gradient pour un modèle d'apprentissage automatique de régression linéaire en utilisant `0.01` comme taux d'apprentissage sur `100` étapes. 

Lors de l'exécution du code ci-dessus, la sortie affichée est donnée ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-43.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-44.png)

## Conclusion

En conclusion, il est important de noter que l'algorithme de descente de gradient est particulièrement important dans les domaines de l'intelligence artificielle et de l'apprentissage automatique, car les modèles doivent être optimisés pour la précision.  

Dans cet article, vous avez appris ce qu'est l'algorithme de Descente de Gradient, comment il fonctionne, sa formule, ce qu'est le taux d'apprentissage, et l'importance de choisir le bon taux d'apprentissage. Vous avez également vu une illustration de code de la manière dont la Descente de Gradient fonctionne. 

Enfin, je partage mes écrits sur l'Intelligence Artificielle, l'Apprentissage Automatique et Microsoft Azure sur [Twitter](https://twitter.com/SalimOpines) si vous avez aimé cet article et souhaitez en voir plus.
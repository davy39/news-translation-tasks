---
title: Algorithme SVM (Support Vector Machine) Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-24T22:20:00.000Z'
originalURL: https://freecodecamp.org/news/support-vector-machines
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d93740569d1a4ca387d.jpg
tags:
- name: Machine Learning
  slug: machine-learning
seo_title: Algorithme SVM (Support Vector Machine) Expliqué
seo_desc: 'According to OpenCV''s "Introduction to Support Vector Machines", a Support
  Vector Machine (SVM):


  ...is a discriminative classifier formally defined by a separating hyperplane. In
  other words, given labeled training data (supervised learning), the al...'
---

Selon l'"Introduction aux Machines à Vecteurs de Support" d'OpenCV, une Machine à Vecteurs de Support (SVM) :

> ...est un classificateur discriminatif formellement défini par un hyperplan séparateur. En d'autres termes, étant donné des données d'entraînement étiquetées (apprentissage supervisé), l'algorithme produit un hyperplan optimal qui catégorise de nouveaux exemples.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/KUeOSK3.png)

Une fonction de coût SVM cherche à approximer la fonction logistique avec une fonction linéaire par morceaux. Cet algorithme de machine learning est utilisé pour les problèmes de classification et fait partie du sous-ensemble des algorithmes d'apprentissage supervisé.

### **La Fonction de Coût**

![Image](https://www.freecodecamp.org/news/content/images/2020/02/SOhv2jZ.png)

La Fonction de Coût est utilisée pour entraîner le SVM. En minimisant la valeur de J(theta), nous pouvons nous assurer que le SVM est aussi précis que possible. Dans l'équation, les fonctions cost1 et cost0 font référence au coût pour un exemple où y=1 et au coût pour un exemple où y=0. Pour les SVM, le coût est déterminé par des fonctions noyau (similarité).

### **Noyaux**

Les caractéristiques polynomiales tendent à être coûteuses en calcul et peuvent augmenter le temps d'exécution avec de grands ensembles de données. Au lieu d'ajouter plus de caractéristiques polynomiales, il est préférable d'ajouter des _repères_ pour tester la proximité des autres points de données. Chaque membre de l'ensemble d'entraînement peut être considéré comme un repère, et un noyau est la fonction de similarité qui mesure la proximité d'une entrée par rapport à ces repères.

### **Classificateur à Grande Marge**

Un SVM trouvera la ligne ou l'hyperplan qui sépare les données avec la plus grande marge possible. Bien qu'il y ait des valeurs aberrantes qui influencent la ligne dans une certaine direction, une valeur C suffisamment petite appliquera une régularisation.

Le code suivant est écrit pour l'entraînement, la prédiction et la recherche de précision pour SVM en Python :

```python
import numpy as np


class Svm (object):
    """" Classificateur Svm """

    def __init__ (self, inputDim, outputDim):
        self.W = None
       
        # - Générer une matrice de poids svm aléatoire pour calculer la perte                 #
        #   avec une distribution normale standard et un écart type = 0,01.    #
       
        sigma =0.01
        self.W = sigma * np.random.randn(inputDim,outputDim)
   
  

    def calLoss (self, x, y, reg):
        """
        Fonction de perte Svm
        D: Dimension d'entrée.
        C: Nombre de classes.
        N: Nombre d'exemples.
        Entrées:
        - x: Un tableau numpy de forme (batchSize, D).
        - y: Un tableau numpy de forme (N,) où la valeur < C.
        - reg: (float) force de régularisation.
        Retourne un tuple de:
        - perte en tant que float unique.
        - gradient par rapport aux poids self.W (dW) avec la même forme que self.W.
        """
        loss = 0.0
        dW = np.zeros_like(self.W)
        
        # - Calculer la perte svm et stocker dans la variable loss.                        #
        # - Calculer le gradient et stocker dans la variable dW.                              #
        # - Utiliser la régularisation L2                                                  #
       
        # Calcul de la matrice de score
        s = x.dot(self.W)
        # Score avec yi
        s_yi = s[np.arange(x.shape[0]),y]
        # Trouver le delta
        delta = s- s_yi[:,np.newaxis]+1
        # perte pour les échantillons
        loss_i = np.maximum(0,delta)
        loss_i[np.arange(x.shape[0]),y]=0
        loss = np.sum(loss_i)/x.shape[0]
        # Perte avec régularisation
        loss += reg*np.sum(self.W*self.W)
        # Calcul de ds
        ds = np.zeros_like(delta)
        ds[delta > 0] = 1
        ds[np.arange(x.shape[0]),y] = 0
        ds[np.arange(x.shape[0]),y] = -np.sum(ds, axis=1)

        dW = (1/x.shape[0]) * (x.T).dot(ds)
        dW = dW + (2* reg* self.W)
        

        return loss, dW

    def train (self, x, y, lr=1e-3, reg=1e-5, iter=100, batchSize=200, verbose=False):
        """
        Entraîner ce classificateur Svm en utilisant la descente de gradient stochastique.
        D: Dimension d'entrée.
        C: Nombre de classes.
        N: Nombre d'exemples.
        Entrées:
        - x: données d'entraînement de forme (N, D)
        - y: données de sortie de forme (N, ) où la valeur < C
        - lr: (float) taux d'apprentissage pour l'optimisation.
        - reg: (float) force de régularisation.
        - iter: (integer) nombre total d'itérations.
        - batchSize: (integer) nombre d'exemples dans chaque lot.
        - verbose: (boolean) Imprimer le journal de la perte et de la précision d'entraînement.
        Sorties:
        Une liste contenant la valeur de la perte à chaque itération d'entraînement.
        """

        # Exécuter la descente de gradient stochastique pour optimiser W.
        lossHistory = []
        for i in range(iter):
            xBatch = None
            yBatch = None
            
            # - Échantillonner batchSize à partir des données d'entraînement et sauvegarder dans xBatch et yBatch   #
            # - Après échantillonnage, xBatch doit avoir la forme (batchSize, D)              #
            #                  yBatch (batchSize, )                                 #
            # - Utiliser cet échantillon pour l'optimisation par descente de gradient.                   #
            # - Mettre à jour les poids en utilisant le gradient et le taux d'apprentissage.        #
            
            # création du lot
            num_train = np.random.choice(x.shape[0], batchSize)
            xBatch = x[num_train]
            yBatch = y[num_train]
            loss, dW = self.calLoss(xBatch,yBatch,reg)
            self.W= self.W - lr * dW
            lossHistory.append(loss)

            # Imprimer la perte toutes les 100 itérations
            if verbose and i % 100 == 0 and len(lossHistory) is not 0:
                print ('Boucle {0} perte {1}'.format(i, lossHistory[i]))

        return lossHistory

    def predict (self, x,):
        """
        Prédire la sortie y.
        Entrées:
        - x: données d'entraînement de forme (N, D)
        Retourne:
        - yPred: données de sortie de forme (N, ) où la valeur < C
        """
        yPred = np.zeros(x.shape[0])
       
        # -  Stocker la sortie prédite dans yPred                                    #
        
        s = x.dot(self.W)
        yPred = np.argmax(s, axis=1)
        return yPred


    def calAccuracy (self, x, y):
        acc = 0
        
        # -  Calculer la précision de la valeur prédite et stocker dans la variable acc    
        yPred = self.predict(x)
        acc = np.mean(y == yPred)*100
        return acc
```
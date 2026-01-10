---
title: Comment résoudre une question typique d'entretien sur les décimales répétitives
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-03T12:10:06.000Z'
originalURL: https://freecodecamp.org/news/interview-questions
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/photo-1515879218367-8466d910aaa4.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: interview questions
  slug: interview-questions
seo_title: Comment résoudre une question typique d'entretien sur les décimales répétitives
seo_desc: "By Pier Paolo Ippolito\nIntroduction\nIn this article, I will walk you\
  \ through how to solve a typical software development interview question: Repeating\
  \ Decimals. \nIn order to solve this example, I decided to use Python (all the code\
  \ is available here)..."
---

Par Pier Paolo Ippolito

## Introduction

Dans cet article, je vais vous expliquer comment résoudre une question typique d'entretien en développement logiciel : les décimales répétitives.

Pour résoudre cet exemple, j'ai décidé d'utiliser Python (tout le code est disponible [ici](https://github.com/pierpaolo28/Algorithms/tree/master/Interview%20Questions)). Si vous le souhaitez, n'hésitez pas à essayer de résoudre cet exercice en utilisant un autre langage de programmation de votre choix.

## Le Problème

> Créer une fonction capable de prendre deux nombres (le numérateur et le dénominateur d'une fraction) qui retourne le résultat de la fraction sous forme décimale, en enfermant entre parenthèses toute décimale répétitive.

```py
Exemples :
1) 1/3 = 0.(3)
2) 1/4 = 0.25
3) 1/5 = 0.2
4) 1/6 = 0.1(6)
5) 1/7 = 0.(142857)
6) 1/8 = 0.125
```

Je vais maintenant vous guider à travers une implémentation simple pour résoudre ce problème. Si vous êtes capable de créer une solution plus efficace en temps et en mémoire, n'hésitez pas à la partager dans la section des commentaires ci-dessous.

## La Solution

Commençons par créer une fonction (_repeating_dec_sol_) et gérer quelques exceptions simples :

1. Si le numérateur est zéro, retourner zéro.
2. Si le dénominateur est zéro, retourner Indéfini (même si le numérateur et le dénominateur sont tous deux égaux à zéro).
3. Si le reste est zéro, (le numérateur est divisible par le dénominateur) retourner directement le résultat de la division.
4. Si le numérateur ou le dénominateur retourne un nombre négatif lors de la division, ajouter un signe moins au début du résultat retourné (ceci sera fait à la fin du code).

```py
def repeating_dec_sol(numerator, denominator):
    negative = False
    if denominator == 0:
        return 'Indéfini'
    if numerator == 0:
        return '0'
    if numerator*denominator < 0:
        negative = True
    if numerator % denominator == 0:
        return str(numerator/denominator)
    
    num = abs(numerator)
    den = abs(denominator)
```

Maintenant, nous pouvons simplement stocker notre sortie pour tous les chiffres avant le point décimal en concaténant le quotient du numérateur et du dénominateur à une chaîne appelée _result_ (qui sera utilisée plus tard pour stocker l'ensemble du résultat de l'opération).

```py
    result = ""
    result += str(num // den)
    result += "."
```

Afin de gérer la partie après le point décimal, nous allons maintenant commencer à suivre chaque nouveau numérateur et quotient (quantité produite par la division des deux nombres) après le point décimal.

Comme nous pouvons le voir sur l'image ci-dessous (Figure 1), chaque fois qu'il y a une décimale répétitive, les mêmes valeurs des nouveaux numérateurs et des quotients seront répétées plusieurs fois.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/33-1-3-percent-as-a-fraction-math-image-titled-change-a-common-fraction-into-a-decimal-step-8-mathpapa-slope.jpg)
_Figure 1 : Décimales répétitives [1]_

Afin de modéliser ce comportement en Python, nous pouvons commencer par créer une liste vide (_quotient_num_) que nous allons mettre à jour avec tous les nouveaux numérateurs et quotients enregistrés après le point décimal (en utilisant une liste à l'intérieur d'une liste).

Chaque fois que nous allons ajouter une liste contenant un nouveau numérateur et quotient, nous allons vérifier si la même combinaison de nouveau numérateur et quotient est présente dans une autre liste et, si c'est le cas, nous allons alors interrompre l'exécution (ceci nous indique que nous avons atteint une décimale répétitive).

```py
    quotient_num = []
    while num:
    	# Dans le cas où le reste est égal à zéro, il n'y a pas de décimales répétitives. Par conséquent, nous n'avons pas besoin d'ajouter de parenthèses et nous pouvons
        # interrompre la boucle while et retourner le résultat.
        remainder = num % den
        if remainder == 0:
            for i in quotient_num:
                result += str(i[-1])
            break
        num = remainder*10
        quotient = num // den

		# Si le nouveau numérateur et quotient ne sont pas déjà dans la liste, nous
        # les ajoutons à la liste.
        if [num, quotient] not in quotient_num:
            quotient_num.append([num, quotient])
        # Si le nouveau numérateur et quotient sont déjà dans la liste, nous 
        # interrompons l'exécution et nous préparons à retourner le résultat final.
        # Nous suivons la position de l'index, afin d'ajouter les parenthèses 
        # à la sortie au bon endroit.
        elif [num, quotient] in quotient_num:
            index = quotient_num.index([num, quotient])
            for i in quotient_num[:index]:
                result += str(i[-1])
            result += "("
            for i in quotient_num[index:]:
                result += str(i[-1])
            result += ")"
            break
```

Enfin, nous pouvons ajouter le code suivant pour gérer l'exception dans le cas où le numérateur ou le dénominateur d'entrée sont des nombres négatifs.

```py
        if negative:
            result = "-" + result

    return result
```

Si nous testons maintenant notre fonction, nous obtiendrons le résultat suivant :

```py
NUM, DEN = 1, 6
print("Le résultat de la fraction", NUM, "/", DEN, "est égal à : ",
       repeating_dec_sol(NUM, DEN))

# Sortie
# Le résultat de la fraction 1 / 6 est égal à :  0.1(6)
```

## Conclusion

J'espère que vous avez apprécié cet article. Si vous avez des questions, n'hésitez pas à laisser un commentaire ci-dessous. Si vous cherchez également une explication vidéo sur la façon de résoudre ce type de problème, cette [vidéo](https://www.youtube.com/watch?v=WFd478BG4o8) par [PyLenin](https://www.youtube.com/channel/UC2HIN53hM4_ZW8IdmWrJGtw) est un excellent point de départ.

## Informations de contact

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques-unes de mes coordonnées :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog Personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site Personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

## Bibliographie

[1] 33 1 3 Percent As A Fraction Math Image Titled Change A Common Fraction Into A Decimal Step 8 Mathpapa Slope - lugezi.com. Consulté à l'adresse : [http://novine.club/wp-content/uploads//2018/09/33-1-3-percent-as-a-fraction-math-image-titled-change-a-common-fraction-into-a-decimal-step-8-mathpapa-slope.jpg](http://novine.club/wp-content/uploads//2018/09/33-1-3-percent-as-a-fraction-math-image-titled-change-a-common-fraction-into-a-decimal-step-8-mathpapa-slope.jpg)
---
title: Comment créer une calculatrice de conversion de température avec Python
subtitle: ''
author: David Fagbuyiro
co_authors: []
series: null
date: '2023-03-13T23:00:14.000Z'
originalURL: https://freecodecamp.org/news/temperature-converter-calculator-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-maksim-goncharenok-5995230.jpg
tags:
- name: Python
  slug: python
seo_title: Comment créer une calculatrice de conversion de température avec Python
seo_desc: 'Temperature conversion is a fundamental topic in physics and engineering.
  It''s also important in many disciplines for research and various applications.

  For example, temperature measurements are critical for effective data analysis and
  interpretation...'
---

La conversion de température est un sujet fondamental en physique et en ingénierie. Elle est également importante dans de nombreuses disciplines pour la recherche et diverses applications.

Par exemple, les mesures de température sont cruciales pour une analyse et une interprétation efficaces des données dans tous les domaines, de la prévision météorologique à la recherche sur les matériaux. Par conséquent, disposer d'une calculatrice de conversion de température efficace et facile à utiliser est essentiel tant pour les professionnels que pour les étudiants.

Dans ce tutoriel, nous verrons comment créer une calculatrice de conversion de température en Python. Python est un langage de programmation populaire bénéficiant d'une large communauté et de nombreuses bibliothèques utiles, ce qui en fait un excellent choix pour créer un tel outil.

Vous apprendrez à fabriquer une calculatrice de conversion de température puissante et efficace capable de convertir entre plusieurs échelles de température telles que le Celsius, le Fahrenheit et le Kelvin en suivant les instructions étape par étape de ce tutoriel.

### Prérequis :

Pour suivre ce tutoriel, vous devrez avoir Python installé sur votre ordinateur. Vous pouvez télécharger la dernière version de Python sur le site officiel.

Nous utiliserons également la bibliothèque standard de Python, qui devrait être incluse dans votre installation de Python.

## Comment construire la calculatrice de conversion de température

La première étape de la création de notre calculatrice de conversion de température consiste à définir les échelles de température entre lesquelles nous voulons effectuer les conversions.

Dans cet exemple, nous allons convertir entre le Celsius, le Fahrenheit et le Kelvin. Nous allons créer un dictionnaire qui associe chaque échelle de température à un identifiant unique.

```python
TEMPERATURE_SCALES = {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K'
}
```

Ensuite, nous définirons une fonction pour convertir une température d'une échelle à une autre. Cette fonction prendra en entrée la valeur de la température, l'échelle d'entrée et l'échelle de sortie. Elle utilisera ensuite la formule de conversion appropriée pour convertir la température vers l'échelle souhaitée.

```python
def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value
```

Maintenant que nous avons notre fonction de conversion, nous pouvons créer le programme principal. Nous utiliserons une boucle `while` pour demander à plusieurs reprises une saisie à l'utilisateur jusqu'à ce qu'il choisisse de quitter.

Pour chaque conversion, nous demanderons à l'utilisateur la valeur de la température d'entrée, l'échelle de température d'entrée et l'échelle de température de sortie. Nous appellerons ensuite notre fonction de conversion pour transformer la température et afficher le résultat.

```python
while True:
    # Demander la saisie de l'utilisateur
    print('Entrez la valeur de la température d\'entrée :')
    value = float(input())
    print('Entrez l\'échelle de température d\'entrée (C, F ou K) :')
    input_scale = input().upper()
    print('Entrez l\'échelle de température de sortie (C, F ou K) :')
    output_scale = input().upper()

    # Convertir la température et afficher le résultat
    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')

    # Demander à l'utilisateur de continuer ou de quitter
    print('Entrez q pour quitter, ou n\'importe quelle autre touche pour continuer :')
    choice = input()
    if choice.lower() == 'q':
        break
```

Lorsque vous exécutez le programme, vous verrez la sortie suivante :

```python
Entrez la valeur de la température d'entrée :

```

Vous pouvez ensuite saisir la valeur de la température d'entrée, l'échelle de température d'entrée (C, F ou K) et l'échelle de température de sortie (C, F ou K). Le programme convertira alors la température et affichera le résultat. Vous pouvez continuer à convertir des températures jusqu'à ce que vous choisissiez de quitter en saisissant 'q'.

Voici le résultat du code ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-133.png)

## Conclusion

Dans cet article, nous avons démontré comment créer une calculatrice de conversion de température en utilisant Python. Avec seulement quelques lignes de code, nous pouvons construire un convertisseur robuste et efficace capable de passer du Celsius au Fahrenheit ou au Kelvin.
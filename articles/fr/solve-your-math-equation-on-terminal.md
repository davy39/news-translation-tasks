---
title: Comment utiliser votre terminal Linux comme calculatrice – Solveur d'expressions
  mathématiques
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2022-12-15T17:40:54.000Z'
originalURL: https://freecodecamp.org/news/solve-your-math-equation-on-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/FreeCodeCamp
seo_title: Comment utiliser votre terminal Linux comme calculatrice – Solveur d'expressions
  mathématiques
---

Evaluate-expression-on-Terminal.png
tags:
- name: Linux
  slug: linux
- name: Math
  slug: math
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'Pouvez-vous résoudre l'expression mathématique ci-dessous par vous-même sans utiliser aucun appareil ?
  Prenez tout le temps dont vous avez besoin – mais aucun outil n'est autorisé :

  ( ( 11 + 97 ) + ( 2 * 63 ) - ( 7 / 93 ) * ( 8 - 25 ) / ( 9 * 64 ) ) * ( ( 64 / 34
  ) + ( 94 - 20 ) - ( 23 + 98 ) * ( 19...'
---

Pouvez-vous résoudre l'expression mathématique ci-dessous par vous-même sans utiliser aucun appareil ? Prenez tout le temps dont vous avez besoin – mais aucun outil n'est autorisé :

```bash
( ( 11 + 97 ) + ( 2 * 63 ) - ( 7 / 93 ) * ( 8 - 25 ) / ( 9 * 64 ) ) * ( ( 64 / 34 ) + ( 94 - 20 ) - ( 23 + 98 ) * ( 199 * 928 ) / ( 92 * 26 ) ) * ( ( ( 2 * 1 ) / 2 ) - 1 )
```

Félicitations si vous l'avez résolue par vous-même. Je suis sûr que vous serez en colère contre moi, cependant, après avoir découvert que le résultat de cette longue expression s'évalue simplement à zéro. 

Alors, qu'auriez-vous fait si vous aviez utilisé votre navigateur pour trouver la réponse ? Combien de temps cela aurait-il pris ?

La recherche de cette expression sur Google a pris moins d'une seconde pour obtenir la réponse (avec une connexion de 500MBPS) ainsi que 52 100 000 résultats. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-25.png)
_Résultats de recherche par Google pour l'expression donnée_

Yahoo nous a donné la réponse en moins de 500 ms avec 1 480 000 000 résultats de recherche. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-26.png)
_Résultats de recherche par Yahoo pour l'expression donnée_

Bing n'a même rien retourné.

Mais mon terminal et la calculatrice système ont été presque instantanés pour trouver la réponse (moins de 10 ms). 

L'utilisation du terminal est l'une des méthodes les plus rapides pour évaluer une expression mathématique. Mais de nombreux développeurs ignorent qu'ils peuvent résoudre des expressions mathématiques en utilisant leur terminal. 

Dans cet article, vous apprendrez comment résoudre des problèmes mathématiques dans le terminal Linux. 

## Comment évaluer une expression mathématique dans le terminal Linux

Vous pouvez utiliser la commande `expr` pour évaluer une expression mathématique dans votre terminal. Les opérations mathématiques de base telles que l'addition, la soustraction, la multiplication, la division et le modulo fonctionnent toutes avec la commande `expr`. 

Jetons un rapide coup d'œil à chacune de ces opérations :

```bash
expr 12 + 8   # Addition

expr 20 - 10  # Soustraction

expr 5 \* 2   # Multiplication

expr 8 \/ 4   # Division

expr 5 \% 3   # Modulo
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-64.png)
_Utilisation de la commande `expr` du terminal pour trouver les réponses aux opérations arithmétiques_

L'exécution de chacune de ces commandes dans le terminal évalue et retourne la réponse de cette expression (comme vous pouvez le vérifier dans la capture d'écran jointe). 

Vous pourriez vous demander, "Pourquoi y a-t-il une barre oblique inverse (\\ ) pour les trois dernières opérations (Multiplication, Division et Modulo) ?"

Une barre oblique inverse en programmation est principalement utilisée pour échapper les caractères. Prenons l'exemple du symbole de multiplication (*). "*" est utilisé dans les expressions régulières, ce qui signifie essentiellement inclure tous les fichiers et dossiers. 

Voici un exemple rapide :

```bash
cp ./* ../backup/
```

L'exécution de la commande ci-dessus copiera tous les fichiers et dossiers du répertoire courant vers le répertoire de sauvegarde. 

De même, chaque symbole a sa propre signification. L'utilisation d'une barre oblique inverse (\\ ) échappera son modèle d'utilisation régulier. C'est la raison pour laquelle la plupart des symboles sont précédés d'une barre oblique inverse. 

Mais vous pourriez vous demander, est-ce tout ce que cette commande peut faire ? 

La réponse est non. J'ai partagé un échantillon des expressions, mais nous pourrions en utiliser d'autres et obtenir les résultats en une fraction de seconde. 

## Comment évaluer une expression logique dans le terminal

En plus de trouver les résultats d'une expression mathématique, vous pouvez utiliser cette commande pour évaluer une expression logique. 

Les expressions logiques contenant <, <=, >, >=, =, != peuvent être évaluées avec cette commande. 

Jetons un rapide coup d'œil à son fonctionnement :

```bash
expr 2 \< 1

expr 29320 \> 23820

expr 29320 \>= 29320

expr 29320 \< 29320

expr 29320 \<= 29320

expr 293202 \= 293203

expr 293202 \!= 293203
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-65.png)
_Évaluer les expressions logiques avec la commande `expr`_

La commande retourne "1" si l'expression s'évalue à vrai et "0" si elle s'évalue à faux. 

À partir des commandes ci-dessus, vous pouvez remarquer que tous les opérateurs logiques sont échappés avec une barre oblique inverse (\\ ). 

## Que font les opérateurs logiques spéciaux ? 

Je lis dans vos pensées. Vous pensez, "Je connais les opérateurs logiques. Quels sont les opérateurs logiques spéciaux ?". 

Eh bien, les opérateurs logiques spéciaux sont :

* ET (&)
* OU (|)

D'un point de vue programmation, l'opérateur ET s'évalue à vrai si les deux côtés de l'opérateur s'évaluent à vrai. L'opérateur OU s'évalue à vrai si l'un des côtés s'évalue à vrai. 

Voici le tableau pour votre référence. Certaines personnes peuvent être familières avec `1` et `0`. Pour ces personnes, remplacez FAUX par `0` et VRAI par `1`. 

<table>
    <tr>
    	<td>X</td>
    	<td>Y</td>
    	<td>X OU Y</td>
    	<td>X ET Y</td>
    </tr>
	<tr>
        <td>FAUX</td>
        <td>FAUX</td>
        <td>FAUX</td>
        <td>FAUX</td>
	</tr>
	<tr>
        <td>FAUX</td>
        <td>VRAI</td>
        <td>VRAI</td>
        <td>FAUX</td>
	</tr>
	<tr>
        <td>VRAI</td>
        <td>FAUX</td>
        <td>VRAI</td>
        <td>FAUX</td>
	</tr>
	<tr>
        <td>VRAI</td>
        <td>VRAI</td>
        <td>VRAI</td>
        <td>VRAI</td>
	</tr>
</table>

Mais ils ont une utilisation complètement différente avec la commande `expr`. Jetons un rapide coup d'œil à cela. 

La commande `expr` fonctionne de manière similaire au tableau ci-dessus. Mais il y a une exception pour un cas particulier. Cette commande ne retournera jamais `1` si une expression s'évalue à vrai – au lieu de cela, elle retourne un argument. 

L'évaluation de `expr ARG1 | ARG2` retourne ARG1 si ARG1 n'est ni `null` ni `0`, sinon elle retournera ARG2. D'autre part, l'évaluation de `expr ARG1 & ARG2` retourne ARG1 si aucun des arguments n'est `null` ou `0`. Elle retourne `0` sinon. 

Examinons quelques exemples avec l'opérateur logique OU :

```bash
expr 1 \| 2     # Retourne le premier argument (1)

expr 0 \| 2     # Retourne le deuxième argument (2) car le premier argument est 0

expr "" \| 2    # Retourne le deuxième argument (2) car le premier argument est null 
                  (La chaîne vide [""] est considérée comme null dans le terminal)

expr 100 \| 78	# Retourne le premier argument 100

expr "" \| ""   # Retourne 0 car les deux arguments sont null ("")
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-68.png)
_Évaluation des expressions logiques OU avec la commande `expr`_

La capture d'écran ci-dessus représente les opérations avec l'opérateur logique OU (|). En la lisant, vous pourriez encore avoir quelques questions :

### Quel est le but d'utiliser des guillemets doubles vides ("") dans l'expression ? 

Les guillemets doubles vides représentent une valeur `null` en bash. Donc, comme dit précédemment, si le premier argument est null, le deuxième argument est retourné. 

### Que se passe-t-il si les deux arguments sont null ? 

Lors de l'évaluation des deux arguments avec des valeurs null, les opérateurs logiques OU et ET retournent `0`. 

Examinons quelques exemples avec l'opérateur logique ET :

```bash
expr 1 \& 2     # Retourne le premier argument (1)

expr 1 \& 0     # Retourne 0 car un (deuxième) argument est 0

expr 0 \& 1     # Retourne 0 car un (premier) argument est 0

expr "" \& 1	# Retourne 0 car un (premier) argument est null ("")

expr 1 \& ""	# Retourne 0 car un (deuxième) argument est null ("")

expr "" \| ""   # Retourne 0 car les deux arguments sont null ("")
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-69.png)
_Évaluation des expressions logiques ET avec la commande `expr`_

## Comment effectuer des opérations sur les chaînes avec la commande `expr`

La commande `expr` n'est pas limitée aux opérations mathématiques et logiques. Elle peut également effectuer des opérations sur les chaînes. 

### Correspondance de motifs avec Regex

La commande `expr` peut vérifier si un texte correspond à un motif regex. Elle retourne le motif correspondant du texte s'il existe, sinon elle retourne une ligne vide. 

La syntaxe pour vérifier le regex est :

```bash
expr STRING : REGEXP

ou

expr match STRING REGEXP
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-71.png)
_La commande `expr` évalue la correspondance du motif regex avec le texte donné_

Vous pouvez y parvenir soit en utilisant le mot-clé `match`, soit en utilisant un deux-points (`:`) entre la chaîne et le motif regex. 

Alternativement, vous pouvez utiliser le deux-points pour trouver le nombre de caractères correspondant entre les deux textes. 

Voici un exemple :

```bash
expr Remember : Remo    # Retourne 0

expr Remember : Rem     # Retourne 3
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-75.png)
_Commande `expr` pour trouver le nombre de caractères correspondant au texte donné_

### Trouver la longueur d'un texte

Vous pouvez utiliser la commande `expr length` pour trouver la longueur du texte donné. 

```bash
expr length Linux

expr length "Apprendre Linux est amusant"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-72.png)
_Commande `expr length` montrant le nombre de caractères dans le texte donné_

Vous pouvez entrer le texte directement après la commande `expr length` s'il ne contient pas d'espaces. Si le texte contient des espaces, encadrez-les avec des guillemets doubles (""), sinon vous obtiendrez une erreur. 

### Trouver un caractère dans un texte

Vous pouvez trouver un caractère particulier dans un texte donné en utilisant la commande `expr index`. Elle retourne la position où le caractère existe. 

```bash
expr index STRING CHAR
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-74.png)
_`expr index` pour trouver un caractère dans un texte_

Rappelez-vous que la commande `expr index` effectue une recherche sensible à la casse et retourne le premier index correspondant d'un caractère dans le texte. 

### Extraire une sous-chaîne d'une chaîne

Extraire une sous-chaîne d'une chaîne est simple en utilisant la commande `expr`. Entrer la chaîne, l'index de départ et le nombre de caractères à extraire après l'index de départ retournera la sous-chaîne attendue. 

```bash
expr substr Carpenter 4 3      # Retourne pen
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-76.png)
_Commande `expr substr` pour trouver une sous-chaîne dans une chaîne_

## Conclusion

Dans cet article, vous avez appris les cas d'utilisation de la commande `expr`.

Si vous avez apprécié mon tutoriel, vous pouvez vous abonner à ma newsletter sur mon [site personnel](https://5minslearn.gogosoon.com/) pour recevoir plus d'articles aussi instructifs directement dans votre boîte de réception. Vous y trouverez également une liste consolidée de tous mes articles de blog.
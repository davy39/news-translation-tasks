---
title: Python Exit – Comment utiliser une fonction Exit en Python pour arrêter un
  programme
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-05T13:54:40.000Z'
originalURL: https://freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-Python-Exit
seo_title: Python Exit – Comment utiliser une fonction Exit en Python pour arrêter
  un programme
---

How-to-Use-an-Exit-Function-in-Python-to-Stop-a-Program.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Par Shittu Olumide

  La fonction exit() en Python est utilisée pour quitter ou terminer le script ou le programme en cours d'exécution. Vous pouvez l'utiliser pour arrêter l'exécution du programme à tout moment. Lorsque la fonction exit() est appelée, le programme s'arrêtera immédiatement et se terminera...'
---

Par Shittu Olumide

La fonction `exit()` en Python est utilisée pour quitter ou terminer le script ou le programme en cours d'exécution. Vous pouvez l'utiliser pour arrêter l'exécution du programme à tout moment. Lorsque la fonction `exit()` est appelée, le programme s'arrêtera immédiatement et se terminera.

La syntaxe de la fonction `exit()` est :

```py
exit([status])

```

Ici, `status` est un argument optionnel qui représente le statut de sortie du programme. Le statut de sortie est une valeur entière qui indique la raison de la terminaison du programme. Par convention, un statut de 0 indique une exécution réussie, et tout statut non nul indique une erreur ou une terminaison anormale.

Si l'argument `status` est omis ou non fourni, la valeur par défaut de 0 est utilisée.

Voici un exemple d'utilisation de la fonction `exit()` :

```bash
print("Avant la sortie")
exit(1)
print("Après la sortie")  # Cette ligne ne sera pas exécutée

```

Dans cet exemple, le programme affichera `"Avant la sortie"`, mais lorsque la fonction `exit()` est appelée avec un statut de 1, le programme se terminera immédiatement sans exécuter le reste du code. Par conséquent, la ligne `"Après la sortie"` ne sera pas affichée.

## Comment utiliser la fonction `exit()` en Python

Écrivons maintenant un script Python et démontrons comment utiliser correctement la fonction exit dans un scénario réel.

```py
import sys

def main():
    try:
        print("Bienvenue dans le programme !")
        
        # Vérifier la condition de terminaison
        user_input = input("Voulez-vous quitter le programme ? (o/n) : ")
        if user_input.lower() == "o":
            exit_program()
        
        # Continuer avec d'autres opérations
        
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        exit_program()

def exit_program():
    print("Sortie du programme...")
    sys.exit(0)

if __name__ == "__main__":
    main()

```

**Explication du code** :

1. Le script commence par importer le module `sys`, qui fournit l'accès à la fonction `exit()`.
2. La fonction `main()` sert de point d'entrée du programme. Vous pouvez ajouter votre code et vos opérations dans cette fonction.
3. Dans la fonction `main()`, vous pouvez effectuer diverses opérations. Dans cet exemple, vous affichez simplement un message de bienvenue et demandez à l'utilisateur s'il souhaite quitter.
4. Après avoir reçu l'entrée de l'utilisateur, vous vérifiez s'il souhaite quitter en comparant son entrée à "o" (insensible à la casse). Si la condition est vraie, vous appelez la fonction `exit_program()` pour terminer le script.
5. La fonction `exit_program()` affiche un message indiquant que le programme se termine, puis appelle `sys.exit(0)` pour terminer le programme. L'argument `0` passé à `sys.exit()` indique une terminaison réussie. Vous pouvez choisir un code de sortie différent si nécessaire.
6. Enfin, vous vérifiez si le script est exécuté en tant que module principal en utilisant la variable `__name__`. Si c'est le cas, vous appelez la fonction `main()` pour démarrer le programme.

## Bonnes pratiques lors de l'utilisation de la fonction `exit()`

Voici quelques bonnes pratiques pour utiliser efficacement la fonction `exit()` :

**Importer le module `sys`** : Avant d'utiliser la fonction `exit()`, vous devez importer le module `sys` au début de votre script. Incluez la ligne de code suivante :

```py
import sys

```

**Déterminer la condition de sortie** : Identifiez la condition ou la situation dans laquelle vous souhaitez quitter le programme. Cela peut être basé sur l'entrée de l'utilisateur, un événement spécifique, une condition d'erreur ou tout autre critère nécessitant l'arrêt du programme.

**Utiliser `sys.exit()` pour terminer le programme** : Lorsque la condition de sortie est remplie, appelez la fonction `sys.exit()` pour arrêter l'exécution du programme. Vous pouvez passer un code de statut de sortie optionnel en tant qu'argument à la fonction, indiquant la raison de la terminaison.

Encore une fois, un code de statut de 0 est généralement utilisé pour indiquer une exécution réussie du programme, tandis que les valeurs non nulles représentent différents types d'erreurs ou de conditions exceptionnelles.

```py
if condition_met:
    sys.exit()  # Terminer le programme avec un code de statut 0

```

Vous pouvez également passer un code de statut pour fournir des informations supplémentaires :

```py
if error_occurred:
    sys.exit(1)  # Terminer le programme avec un code de statut 1 indiquant une erreur

```

**Nettoyer les ressources (optionnel)** : Si votre programme utilise des ressources qui doivent être correctement fermées ou libérées avant la terminaison, vous pouvez inclure du code de nettoyage avant d'appeler `sys.exit()`. Par exemple, fermer les fichiers ouverts ou libérer les connexions réseau. Cela garantit que les ressources sont gérées de manière appropriée, même si le programme est terminé de manière inattendue.

**Documenter les conditions de sortie** : Il est important de documenter les conditions de sortie spécifiques dans votre code et de fournir des commentaires indiquant pourquoi le programme est terminé. Cela aide les autres développeurs à comprendre le but et le comportement des appels `exit()`.

## Conclusion

En résumé, cet article vous a montré comment utiliser la fonction `exit()` en Python pour terminer l'exécution d'un programme. Optionnellement, un code de statut de sortie peut être passé en tant qu'argument, fournissant des informations supplémentaires sur la raison de la terminaison.

En adhérant à ces bonnes pratiques, vous pouvez utiliser efficacement la fonction `sys.exit()` en Python pour arrêter un programme lorsque cela est nécessaire.

Il est crucial de faire preuve de prudence et d'utiliser cette fonction de manière judicieuse, et de ne l'utiliser que dans des circonstances appropriées lorsque vous souhaitez forcer l'arrêt de l'exécution de votre script Python dans certaines conditions ou lorsque vous devez terminer le programme de manière abrupte.

Certains scénarios où vous pourriez vouloir utiliser la fonction `exit()` : gestion des erreurs, terminaison conditionnelle, test et débogage, et achèvement du script.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !
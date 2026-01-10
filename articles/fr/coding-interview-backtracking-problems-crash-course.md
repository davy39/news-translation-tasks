---
title: Cours Accéléré sur les Problèmes de Backtracking en Entretien de Codage – Le
  Seul Dont Vous Aurez Jamais Besoin
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-06-29T20:00:32.000Z'
originalURL: https://freecodecamp.org/news/coding-interview-backtracking-problems-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/1080P-Thumbnails-1-.png
tags:
- name: coding interview
  slug: coding-interview
- name: interview questions
  slug: interview-questions
- name: Interview tips
  slug: interview-tips
- name: Job Interview
  slug: job-interview
- name: leetcode
  slug: leetcode
seo_title: Cours Accéléré sur les Problèmes de Backtracking en Entretien de Codage
  – Le Seul Dont Vous Aurez Jamais Besoin
seo_desc: 'Whether you are new to coding interviews or are already familiar with the
  concept of backtracking algorithms, this is the crash course for you.

  In it, we will learn about an all-purpose coding template for solving backtracking
  problems and apply it t...'
---

Que vous soyez nouveau dans les entretiens de codage ou déjà familier avec le concept des algorithmes de **backtracking**, ce cours accéléré est fait pour vous.

Dans ce cours, nous apprendrons un **modèle de codage polyvalent** pour résoudre les problèmes de backtracking et l'appliquerons à **deux problèmes difficiles de LeetCode**. Prêt à réussir votre prochain entretien de codage ? C'est parti !

Si vous voulez plonger directement dans le vif du sujet, [vous pouvez trouver le cours ici](https://www.youtube.com/watch?v=H2gnD7Ixeao) (et lié en bas de cet article). Si vous voulez plus d'informations, continuez votre lecture. :)

## À qui s'adresse ce cours et qu'est-ce que l'algorithme de Backtracking ?

Ce cours est adapté à toute personne qui se prépare pour des entretiens de codage, en particulier celles qui cherchent à affiner leurs compétences dans la résolution de problèmes de **backtracking**.

Le backtracking est une catégorie courante de questions dans les entretiens de codage. L'algorithme pour résoudre ces problèmes implique généralement de la **récursion** et de **construire incrémentalement sur des états précédents** pour arriver à la solution valide ultime.

Le backtracking est un sujet favori parmi les grandes entreprises technologiques comme Google, Microsoft et Facebook, précisément parce qu'il nécessite un raisonnement robuste et une compétence en codage pour réussir ces questions.

Cependant, en raison de sa nature récursive et de sa définition de problème complexe, les problèmes de backtracking sont généralement une source majeure de confusion parmi les développeurs qui se préparent pour des entretiens de codage.

Pour répondre à cette confusion, ce cours accéléré vise à vous armer avec un modèle concis de 20 lignes que vous pouvez appliquer à la majorité des problèmes de backtracking.

## Plan du Cours

Ce cours dure au total 40 minutes et la structure est la suivante :

* Une introduction de 8 minutes sur [le modèle](https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6)

* Une session pratique de codage de 15 minutes pour [LeetCode Question 51. N-Queens](https://leetcode.com/problems/n-queens/)

* Une session pratique de codage de 15 minutes pour [LeetCode Question 37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

## Le Modèle Polyvalent

Pour votre commodité, j'ai copié le modèle ci-dessous. Il s'agit exactement du même modèle que j'utilise pour mes entretiens de codage, ou lorsque je développe des algorithmes pour mes jeux indépendants. Je l'ai même utilisé une fois dans mes recherches sur un problème d'optimisation non convexe.

```python
def is_valid_state(state):
    # vérifier si c'est une solution valide
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions
```

Les trois premières sont toutes des fonctions auxiliaires, et la dernière et la plus importante, `solve`, est essentiellement celle qu'un problème LeetCode vous demande d'écrire.

## Résolution Pratique de Problèmes LeetCode

Nous allons ensuite appliquer ce modèle à la résolution de deux problèmes difficiles de LeetCode : [LeetCode Question 51. N-Queens](https://leetcode.com/problems/n-queens/) et [LeetCode Question 37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/).

Pour illustrer la flexibilité du modèle, voir ci-dessous comment nous résolvons le problème N-Queens sans rien faire de compliqué autre que l'adaptation des quatre fonctions (renommant `solve` en `solveNQueens`). Le code complet pour chaque problème est disponible [dans mon GitHub gist](https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6).

Regardez [le cours vidéo](https://youtu.be/H2gnD7Ixeao) pour suivre mon analyse et mon adaptation du modèle.

```python
class Solution:
    # solveNQueens est essentiellement la fonction solve
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
        
    def is_valid_state(self, state, n):
        # vérifier si c'est une solution valide
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        
        # trouver la prochaine position dans l'état à remplir
        position = len(state)
        candidates = set(range(n))
        # réduire les candidats qui placent la reine en attaque
        for row, col in enumerate(state):
            # écarter l'index de colonne s'il est occupé par une reine
            candidates.discard(col)
            dist = position - row
            # écarter les diagonales
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            # récursion
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
```

Consultez le cours vidéo ici :

%[https://youtu.be/H2gnD7Ixeao] 

Vous pouvez accéder au modèle ainsi qu'aux solutions des deux problèmes LeetCode (**N-Queens** et **Sudoku Solver**) dans mon GitHub gist :

%[https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6] 

## Réflexions Finales

Rappelez-vous que la pratique rend parfait, alors essayez d'appliquer ce modèle à [plus de problèmes de backtracking sur LeetCode](https://leetcode.com/tag/backtracking/). Bonne chance pour votre prochain entretien de codage !

Pour plus de contenu comme celui-ci, consultez ma chaîne YouTube :

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw]
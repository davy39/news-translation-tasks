---
title: Tutoriel sur l'instruction CASE en SQL – Avec des exemples de requêtes utilisant
  la clause When-Then
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-19T20:44:49.000Z'
originalURL: https://freecodecamp.org/news/sql-case-statement-tutorial-with-when-then-clause-example-queries
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6067f407d5756f080ba93c3b.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Tutoriel sur l'instruction CASE en SQL – Avec des exemples de requêtes
  utilisant la clause When-Then
seo_desc: "By Veronica Stork\nWhat is a SQL Case Statement?\nA case statement is basically\
  \ SQL's version of conditional logic. It can be used in the same way as if statements\
  \ in programming languages like JavaScript, but it is structured slightly differently.\
  \ \nSa..."
---

Par Veronica Stork

## Qu'est-ce qu'une instruction CASE en SQL ?

Une instruction CASE est essentiellement la version SQL de la logique conditionnelle. Elle peut être utilisée de la même manière que les instructions `if` dans les langages de programmation comme JavaScript, mais elle est structurée légèrement différemment. 

## Données d'exemple

Imaginez que vous enseignez un cours de littérature. Vos étudiants doivent écrire une dissertation pour répondre aux exigences du cours. 

Vous avez créé le tableau ci-dessous pour suivre quels étudiants ont soumis leur dissertation, ainsi que leur note. S'ils n'ont pas encore soumis leur dissertation, leur note est indiquée comme `NULL`.

| student_id  | name |  submitted_essay  |   grade  |
| --- | -------------  |  -------------  | -------  |
| 1   | John             |  TRUE   | 86  |
| 2   | Said              |  TRUE   |  90  |
| 3   | Alyssa          |  FALSE   |  NULL  |
| 4   | Noah            |  TRUE   |  68  |
| 5   | Eleanor        |   TRUE   |  95  |
| 6   | Akiko            |  FALSE   | NULL  |
| 7   | Otto             |  TRUE   |  76  |
| 8   | Jamal          |  TRUE   |   85  |
| 9   | Kiara           |  TRUE   |  88  |
| 10 | Clement |   FALSE   |  NULL   |


## Comment écrire une instruction CASE en SQL

Peut-être aimeriez-vous donner à vos étudiants un message concernant l'état de leur devoir. Pour obtenir le statut, vous pourriez simplement sélectionner la colonne `submitted_essay`, mais un message qui dit simplement `TRUE` ou `FALSE` n'est pas particulièrement lisible pour les humains. 

Au lieu de cela, vous pourriez utiliser une instruction `CASE` et afficher différents messages selon que `submitted_essay` est vrai ou faux.

La structure de base de l'instruction `CASE` est `CASE WHEN... THEN... END`. `CASE WHEN`, `THEN` et `END` sont tous requis. `ELSE` et `AS` sont optionnels. L'instruction `CASE` doit être placée dans la clause `SELECT`.

```
SELECT name,
	CASE WHEN submitted_essay IS TRUE THEN 'dissertation soumise !'
	ELSE 'terminez cette dissertation !' END  AS status
FROM students;
```

Dans l'exemple ci-dessus, nous sélectionnons les noms de nos étudiants, puis nous affichons différents messages dans la colonne `status` selon que `submitted_essay` est vrai ou non. La table résultante ressemble à ce qui suit :

|  name  |  status  |
|  ----  |  ------  |
| Akiko	| terminez cette dissertation ! |
| Clement |	terminez cette dissertation ! |
| Alyssa |	terminez cette dissertation ! |
| Said	| dissertation soumise ! |
| Eleanor |	dissertation soumise ! |
| Otto	| dissertation soumise ! |
| Noah	| dissertation soumise ! |
| Kiara	| dissertation soumise ! |
| John	| dissertation soumise ! |
| Jamal	| dissertation soumise !|

Maintenant, supposons que vous souhaitiez inclure un peu plus d'informations. Vous voulez commenter les notes des étudiants s'ils ont soumis leur dissertation, et leur dire de terminer leur dissertation s'ils ne l'ont pas encore soumise. C'est là que plusieurs instructions `WHEN/THEN` peuvent être utiles.

```
SELECT name, essay_grade,
CASE WHEN essay_grade >= 80 THEN 'excellent travail'
	 WHEN essay_grade < 80 THEN 'essayez plus fort'
	 ELSE 'terminez cette dissertation !' END  AS teacher_comment
FROM students;
```

Dans l'exemple de code ci-dessus, nous affichons les noms et les notes des dissertations des étudiants, ainsi que des commentaires qui diffèrent en fonction de leurs notes. 

Après la première instruction `WHEN/THEN`, vous pouvez ajouter autant d'autres instructions `WHEN/THEN` que nécessaire, ainsi qu'une instruction `ELSE` pour couvrir d'autres cas possibles. Cela est analogue à la logique de style `if... else if... else` en JavaScript (ou `if... elif... else` en Python, etc.). 

Notez que dans ce cas, `ELSE` est destiné à capturer les dissertations avec des notes de `NULL` (c'est-à-dire celles qui n'ont pas encore été soumises), mais dans d'autres situations, vous pourriez utiliser `IS NULL` pour vérifier si une valeur sélectionnée est nulle. 

N'oubliez pas de terminer votre instruction CASE par `END` ! Ci-dessous, vous pouvez voir les résultats de cette requête. 

|  name  |  essay_grade  | teacher_comment  |
|  -----  |  ----------  |  --------------  |
|  Akiko	|  NULL  |	terminez cette dissertation !  |
| Clement	|  NULL  |	terminez cette dissertation ! |
|  Alyssa	|  NULL  |	terminez cette dissertation !  |
|  Said	 | 90  |	excellent travail  |
|  Eleanor  |	95  |	excellent travail  |
|  Otto	  |  76  |	essayez plus fort  |
|  Noah  |	68	|  essayez plus fort  |
|  Kiara  |	88	|  excellent travail  |
|  John  |	86	|  excellent travail  |
|  Jamal  |	85	|  excellent travail  |





## Conclusion

Les instructions CASE sont un moyen clair et concis de donner du sens à vos requêtes en SQL, et elles sont faciles à apprendre et à comprendre. Bonnes requêtes !
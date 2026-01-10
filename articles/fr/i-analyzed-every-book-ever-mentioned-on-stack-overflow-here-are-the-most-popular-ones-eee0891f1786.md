---
title: J'ai analysé tous les livres jamais mentionnés sur Stack Overflow. Voici les
  plus populaires.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-07T15:30:44.000Z'
originalURL: https://freecodecamp.org/news/i-analyzed-every-book-ever-mentioned-on-stack-overflow-here-are-the-most-popular-ones-eee0891f1786
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tIbZVgZCBSzq7dLUUBnrPQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: J'ai analysé tous les livres jamais mentionnés sur Stack Overflow. Voici
  les plus populaires.
seo_desc: 'By Vlad Wetzel

  Finding your next programming book is hard, and it’s risky.

  As a developer, your time is scarce, and reading a book takes up a lot of that time.
  You could be programming. You could be resting. But instead you’re allocating precious
  tim...'
---

Par Vlad Wetzel

Trouver votre prochain livre de programmation est difficile, et c'est risqué.

En tant que développeur, votre temps est précieux, et lire un livre prend beaucoup de ce temps. Vous pourriez être en train de programmer. Vous pourriez être en train de vous reposer. Mais au lieu de cela, vous allouez un temps précieux à la lecture et à l'expansion de vos compétences.

Alors, quel livre devriez-vous lire ? Mes collègues et moi discutons souvent des livres, et j'ai remarqué que nos opinions sur un livre donné varient énormément.

J'ai donc décidé d'examiner plus en profondeur le problème. Mon idée : analyser la ressource la plus populaire pour les programmeurs dans le monde pour les liens vers une librairie bien connue, puis compter combien de mentions chaque livre a.

Heureusement, Stack Exchange (la société mère de Stack Overflow) venait de publier leur dump de données. Je me suis donc assis et j'ai commencé à coder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Gtla3Qgig00AgRvGc-kxg.png)
_Une capture d'écran de l'outil que j'ai construit : [dev-books.com](http://www.dev-books.com" rel="noopener" target="_blank" title=")_

> _« Si vous êtes curieux, le livre le plus recommandé en général est [Working Effectively with Legacy Code](https://amazon.co.uk/dp/0131177052/?tag=devbookscom-21), suivi de [Design Pattern: Elements of Reusable Object-Oriented Software](https://amazon.co.uk/dp/0201633612/?tag=devbookscom-21). Bien que les titres de ces livres soient aussi secs que le désert d'Atacama, le contenu devrait être de qualité. Vous pouvez trier les livres par tags, comme JavaScript, C, Graphics, et bien d'autres. Cela n'est évidemment pas la solution ultime pour les recommandations de livres, mais c'est certainement un bon point de départ si vous commencez à coder ou si vous cherchez à approfondir vos connaissances. » — critique sur [Lifehacker.com](http://lifehacker.com/dev-books-is-a-massive-collection-of-the-most-recommend-1792134129)_

Peu de temps après, j'ai lancé [dev-books.com](http://www.dev-books.com), qui vous permet d'explorer toutes les données que j'ai collectées et triées. J'ai eu plus de 100 000 visiteurs et reçu beaucoup de retours me demandant de décrire tout le processus technique.

Alors, comme promis, je vais décrire comment j'ai tout construit.

### Obtention et importation des données

J'ai récupéré le dump de la base de données Stack Exchange depuis [archive.org](https://archive.org/details/stackexchange).

Dès le début, j'ai réalisé qu'il ne serait pas possible d'importer un fichier XML de 48 Go dans une base de données nouvellement créée (PostgreSQL) en utilisant des méthodes populaires comme `myxml := pg_read_file('path/to/my_file.xml')`, car je n'avais pas 48 Go de RAM sur mon serveur. J'ai donc décidé d'utiliser un parseur [SAX](https://en.wikipedia.org/wiki/Simple_API_for_XML).

Toutes les valeurs étaient stockées entre les balises `<r`ow>, j'ai donc utilisé un script Python pour les analyser :

Après trois jours d'importation (presque la moitié du XML avait été importée pendant ce temps), j'ai réalisé que j'avais fait une erreur : l'attribut `ParentID` aurait dû être `ParentId`.

À ce stade, je ne voulais pas attendre une autre semaine, et je suis passé d'un AMD E-350 (2 x 1,35 GHz) à un Intel G2020 (2 x 2,90 GHz). Mais cela n'a toujours pas accéléré le processus.

Décision suivante : insertion par lots :

StringIO vous permet d'utiliser une variable comme un fichier pour gérer la fonction `copy_from`, qui utilise `COPY`. De cette façon, le processus d'importation complet n'a pris qu'une seule nuit.

OK, il est temps de créer des index. En théorie, les index GiST sont plus lents que les GIN, mais prennent moins de place. J'ai donc décidé d'utiliser GiST. Après une autre journée, j'avais un index qui prenait 70 Go.

Lorsque j'ai essayé quelques requêtes de test, j'ai réalisé qu'il fallait beaucoup trop de temps pour les traiter. La raison ? Les attentes d'E/S disque. Un SSD GOODRAM C40 120 Go a beaucoup aidé, même s'il n'est pas le SSD le plus rapide à ce jour.

J'ai créé un tout nouveau cluster PostgreSQL :

```
initdb -D /media/ssd/postgresq/data
```

Ensuite, j'ai veillé à changer le chemin dans ma configuration de service (j'ai utilisé Manjaro OS) :

```
vim /usr/lib/systemd/system/postgresql.service
```

```
Environment=PGROOT=/media/ssd/postgresPIDFile=/media/ssd/postgres/data/postmaster.pid
```

J'ai rechargé ma configuration et démarré PostgreSQL :

```
systemctl daemon-reloadpostgresql systemctl start postgresql
```

Cette fois, cela a pris quelques heures pour importer, mais j'ai utilisé GIN. L'indexation a pris 20 Go d'espace sur le SSD, et les requêtes simples prenaient moins d'une minute.

### Extraction des livres de la base de données

Avec mes données enfin importées, j'ai commencé à chercher des posts qui mentionnaient des livres, puis je les ai copiés dans une table séparée en utilisant SQL :

```
CREATE TABLE books_posts AS SELECT * FROM posts WHERE body LIKE '%book%';
```

L'étape suivante a été de trouver tous les hyperliens dans ceux-ci :

```
CREATE TABLE http_books AS SELECT * posts WHERE body LIKE '%http%';
```

À ce stade, j'ai réalisé que StackOverflow proxyfie tous les liens comme : `rads.stackowerflow.com/[$isbn]/`

J'ai créé une autre table avec tous les posts contenant des liens :

```
CREATE TABLE rads_posts AS SELECT * FROM posts WHERE body LIKE '%http://rads.stackowerflow.com%';
```

En utilisant des expressions régulières pour extraire tous les [ISBNs](https://en.wikipedia.org/wiki/International_Standard_Book_Number). J'ai extrait les tags Stack Overflow dans une autre table via `regexp_split_to_table`.

Une fois que j'ai extrait et compté les tags les plus populaires, les 20 livres les plus mentionnés par tag étaient assez similaires à travers tous les tags.

Ma prochaine étape : affiner les tags.

L'idée était de prendre les 20 livres les plus mentionnés pour chaque tag et d'exclure les livres qui avaient déjà été traités.

Puisque c'était un travail "ponctuel", j'ai décidé d'utiliser des tableaux PostgreSQL. J'ai écrit un script pour créer une requête comme suit :

Avec les données en main, je me suis dirigé vers le web.

### Construction de l'application web

Puisque je ne suis pas un développeur web — et certainement pas un expert en interface utilisateur web — j'ai décidé de créer une application monopage très simple basée sur un thème Bootstrap par défaut.

J'ai créé une option "recherche par tag", puis j'ai extrait les tags les plus populaires pour rendre chaque recherche cliquable.

J'ai visualisé les résultats de recherche avec un graphique à barres. J'ai essayé Highcharts et D3, mais ils étaient plus adaptés aux tableaux de bord. Ceux-ci avaient quelques problèmes de réactivité et étaient assez complexes à configurer. J'ai donc créé mon propre graphique réactif basé sur SVG. Pour le rendre réactif, il doit être redessiné lors de l'événement de changement d'orientation de l'écran :

### Échec du serveur web

![Image](https://cdn-media-1.freecodecamp.org/images/0*Mr3xakmAy7cOXbB9.png)
_Nginx vs. Apache_

Dès que j'ai publié [dev-books.com](http://www.dev-books.com), une foule énorme a commencé à visiter mon site web. Apache ne pouvait pas servir plus de 500 visiteurs en même temps, alors j'ai rapidement configuré Nginx et je suis passé à celui-ci. J'ai été vraiment surpris lorsque le nombre de visiteurs en temps réel a grimpé à 800 au même moment.

### Conclusion :

J'espère avoir expliqué tout cela suffisamment clairement pour que vous compreniez comment j'ai construit ceci. Si vous avez des questions, n'hésitez pas à demander. Vous pouvez me trouver [sur Twitter](https://twitter.com/VLPLabs) et [Facebook](https://www.facebook.com/VLP-Labs-727090070789985/).

Comme promis, je publierai mon rapport complet d'Amazon.com et de Google Analytics à la fin du mois de mars. Les résultats jusqu'à présent ont été vraiment surprenants.

Assurez-vous de cliquer sur le cœur vert ci-dessous et de me suivre pour plus d'histoires sur la technologie :)

Restez à l'écoute sur [dev-books.com](http://www.dev-books.com)
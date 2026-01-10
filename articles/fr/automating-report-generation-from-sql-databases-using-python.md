---
title: Comment générer des rapports automatisés à partir d'une base de données SQL
  avec Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-16T22:09:47.000Z'
originalURL: https://freecodecamp.org/news/automating-report-generation-from-sql-databases-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/coreet.JPG
tags:
- name: automation
  slug: automation
- name: database
  slug: database
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: Comment générer des rapports automatisés à partir d'une base de données
  SQL avec Python
seo_desc: 'Generating reports from SQL databases is a common task in many organizations.
  But the process can be time-consuming and error-prone, especially if it involves
  manual data extraction, transformation, and formatting.

  In this article, we will explore ho...'
---

La génération de rapports à partir de bases de données SQL est une tâche courante dans de nombreuses organisations. Mais le processus peut être chronophage et sujet aux erreurs, en particulier s'il implique l'extraction, la transformation et le formatage manuels des données.

Dans cet article, nous explorerons comment utiliser Python pour automatiser le processus de génération de rapports à partir de bases de données SQL, réduisant ainsi le temps et les efforts nécessaires pour créer et distribuer des rapports.

### Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

* Python 3.x
    
* Une base de données SQL telle que MySQL ou PostgreSQL
    
* Une bibliothèque Python pour accéder aux bases de données SQL telle que psycopg2 ou mysql-connector-python
    
* Une bibliothèque Python pour créer des rapports telle que ReportLab ou PyPDF2
    

## Comment se connecter à la base de données SQL

La première étape consiste à se connecter à la base de données SQL en utilisant Python. Nous utiliserons la bibliothèque psycopg2 pour nous connecter à une base de données PostgreSQL.

Voici un exemple de code pour se connecter à la base de données :

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mabase",
    user="monutilisateur",
    password="monmotdepasse"
)
```

Assurez-vous de remplacer les valeurs des paramètres `host`, `database`, `user` et `password` par les valeurs appropriées pour votre base de données.

## Comment récupérer des données de la base de données SQL

Une fois la connexion à la base de données SQL établie, nous pouvons exécuter des requêtes SQL pour récupérer les données nécessaires à notre rapport.

Voici un exemple de code pour récupérer des données d'une base de données PostgreSQL :

```python
cur = conn.cursor()

cur.execute("SELECT name, email, phone FROM customers")

rows = cur.fetchall()
```

Ce code récupère le nom, l'e-mail et le numéro de téléphone de tous les clients de la table `customers`.

## Comment créer le rapport

Ensuite, nous devons créer le rapport en utilisant une bibliothèque Python telle que ReportLab ou PyPDF2. Voici un exemple de code pour créer un rapport PDF à l'aide de ReportLab :

```python
from reportlab.pdfgen import canvas

# Créer un nouveau document PDF
pdf = canvas.Canvas("rapport.pdf")

# Écrire le titre du rapport
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, 750, "Rapport client")

# Écrire le contenu du rapport
pdf.setFont("Helvetica", 12)
y = 700
for row in rows:
    pdf.drawString(50, y, "Nom : " + row[0])
    pdf.drawString(50, y - 20, "E-mail : " + row[1])
    pdf.drawString(50, y - 40, "Téléphone : " + row[2])
    y -= 60

# Enregistrer le document PDF
pdf.save()
```

Ce code crée un nouveau document PDF, écrit le titre du rapport et parcourt les données récupérées dans la base de données SQL pour écrire le contenu du rapport. Le rapport PDF final est enregistré sous le nom `rapport.pdf`.

## Comment automatiser le processus de génération de rapports

Maintenant que nous avons le code pour nous connecter à la base de données SQL, récupérer les données et créer le rapport, nous pouvons automatiser le processus de génération de rapports à l'aide d'un script Python.

Voici un exemple de code pour automatiser le processus de génération de rapports :

```python
import psycopg2
from reportlab.pdfgen import canvas

# Se connecter à la base de données SQL
conn = psycopg2.connect(
    host="localhost",
    database="mabase",
    user="monutilisateur",
    password="monmotdepasse"
)

# Récupérer les données de la base de données SQL
cur = conn.cursor()
cur.execute("SELECT name, email, phone FROM customers")
rows = cur.fetchall()

# Créer le rapport
pdf = canvas.Canvas("rapport.pdf")
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, 750, "Rapport client")
pdf.setFont("Helvetica", 12)
y = 700
for row in rows:
pdf.drawString(50, y, "Nom : " + row[0])
pdf.drawString(50, y - 20, "E-mail : " + row[1])
pdf.drawString(50, y - 40, "Téléphone : " + row[2])
y -= 60
pdf.save()
# Fermer la connexion à la base de données
cur.close()
conn.close()
```

Ce code se connecte à la base de données SQL, récupère les données, crée le rapport et l'enregistre sous le nom `rapport.pdf`. Vous pouvez ensuite exécuter ce script régulièrement pour générer des rapports automatiquement.

## Conclusion

Dans cet article, nous avons exploré comment utiliser Python pour automatiser le processus de génération de rapports à partir de bases de données SQL. En utilisant Python pour se connecter à la base de données, récupérer les données et créer le rapport, nous pouvons gagner du temps et réduire les risques d'erreurs.

Nous avons également vu comment utiliser des bibliothèques Python telles que psycopg2 et ReportLab pour rendre le processus encore plus efficace. Grâce à ces techniques, vous pouvez facilement automatiser la génération de rapports à partir de bases de données SQL et vous concentrer sur d'autres tâches importantes.

Connectons-nous sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
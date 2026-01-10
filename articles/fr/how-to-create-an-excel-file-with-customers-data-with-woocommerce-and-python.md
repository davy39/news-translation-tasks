---
title: Comment créer un fichier Excel qui extrait les données clients avec WooCommerce
  et Python
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2021-10-08T15:15:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-excel-file-with-customers-data-with-woocommerce-and-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/cover-1.jpg
tags:
- name: ecommerce
  slug: ecommerce
- name: excel
  slug: excel
- name: Python
  slug: python
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment créer un fichier Excel qui extrait les données clients avec WooCommerce
  et Python
seo_desc: '“Hey, could you please send me our customers'' emails? We’re about to launch
  a new marketing campaign and…we need them ASAP.”

  If you work in the Web department on a corporate level, you''ve probably heard this
  sentence hundreds of times. So, today I wa...'
---

"Hey, pourriez-vous m'envoyer les emails de nos clients ? Nous sommes sur le point de lancer une nouvelle campagne marketing et... nous en avons besoin dès que possible."

Si vous travaillez dans le département Web au niveau corporate, vous avez probablement entendu cette phrase des centaines de fois. Alors, aujourd'hui, je veux partager comment j'ai résolu ce problème pour une entreprise où je travaillais.

## Quelle était la demande ?

Nous avions une application e-commerce construite avec WooCommerce, qui recevait des milliers de commandes chaque jour dans le monde entier. Pour s'inscrire, les utilisateurs devaient ajouter leur prénom, nom et adresse email.

Notre département marketing a demandé à mon équipe de leur fournir les adresses email et les prénoms de tous nos clients pour lancer une nouvelle campagne.

Je m'attendais à ce qu'ils demandent un fichier CSV pour importer massivement les contacts sur leur plateforme marketing. Au lieu de cela, ils m'ont dit qu'ils avaient besoin d'un fichier Excel puisqu'ils devaient l'éditer avant de procéder au lancement de la campagne.

Une fois qu'ils m'ont assigné le ticket Jira, j'étais prêt à commencer.

## Analyser le problème

WooCommerce fournit aux utilisateurs une fonctionnalité d'export pour obtenir les données des clients, mais il ne génère pas de fichier Excel. Il génère un fichier CSV ou XML.

Lorsque vous travaillez avec un outil comme WordPress, la première option à laquelle vous pensez est d'utiliser un plugin et d'obtenir ce dont vous avez besoin.

J'ai trouvé quelques options dans le répertoire des plugins WordPress, mais il y a beaucoup de choses à considérer chaque fois que vous installez un nouveau plugin dans votre instance. Vous devez penser aux coûts de maintenance (considérez chaque fois qu'un développeur travaille dessus, ils enregistrent des heures qui affectent votre budget), aux vulnérabilités de sécurité, et – last but not least – l'approbation d'achat peut prendre beaucoup de temps.

J'ai également considéré une deuxième option : télécharger le CSV via l'interface utilisateur et le convertir en fichier Excel en utilisant l'un des milliers de services que vous pouvez trouver en ligne.

Mais l'utilisation de services tiers pourrait violer des politiques critiques de sécurité et de confidentialité, et le résultat final n'est pas toujours fiable. J'ai donc décidé de ne pas aller plus loin dans cette direction.

En fin de compte, j'ai pensé que développer un script était la meilleure et la plus rapide option pour résoudre cette tâche.

WordPress fournit aux développeurs des APIs. De nombreux autres plugins du système WordPress fournissent également des APIs, et WooCommerce ne fait pas exception. La [documentation](https://docs.woocommerce.com/document/woocommerce-rest-api/) est robuste et offre des liens vers des bibliothèques pour les langages les plus utilisés tels que Node.js, Python, PHP et Ruby.

J'ai décidé d'utiliser Python et cette technologie pour développer un script qui génère un fichier Excel avec la structure suivante :

* Deux colonnes : prénom et email
* Une ligne par client

J'ai choisi Python pour plusieurs raisons : il existe des centaines de bibliothèques qui peuvent vous aider à accomplir la tâche, il est flexible et très utile lorsqu'il s'agit de manipuler des données.

J'ai également décidé d'utiliser Pandas et Openpyxl pour manipuler les données et créer le fichier Excel.

## Avant de coder, obtenons ce dont nous avons besoin

Pour travailler avec l'API WooCommerce, j'ai besoin de générer les clés API nécessaires. Vous pouvez obtenir plus d'informations sur la documentation officielle de WooCommerce [documentation](https://docs.woocommerce.com/document/woocommerce-rest-api/).

Tout d'abord, vous devez vous connecter à votre instance WooCommerce, puis aller à WooCommerce > Paramètres > Avancé > API REST.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/0-1.png)

Ensuite, je vais donner une brève description, choisir l'utilisateur pour lequel je veux générer l'API, choisir les permissions accordées (Lecture/Écriture ou les deux), puis cliquer sur "Générer la clé API".

Ensuite, j'obtiendrai la Consumer Key et la Consumer Secret :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/screencapture-marcoventuritest-it-wooTest-wp-admin-admin-php-2021-10-06-17_19_38.png)

## Comment préparer l'environnement

La toute première chose que j'ai faite a été d'ajouter les bibliothèques nécessaires pour développer mon script. J'ai commencé par la bibliothèque Python pour WooCommerce. Pour l'installer, j'ai exécuté cette commande :

```python
pip install woocommerce
```

Bien. Maintenant, je vais installer Pandas, un outil d'analyse et de manipulation de données pour Python :

```python
pip install pandas
```

Après cela, j'ai installé Openpyxl, une bibliothèque Python pour lire et écrire des fichiers Excel :

```python
pip install openpyxl
```

## Codons

J'ai fait l'appel API en utilisant la fonction API fournie par la bibliothèque Python WooCommerce et je l'ai stockée dans une variable. Ensuite, j'ai passé à la fonction l'URL de base de mon site WooCommerce, la clé du consommateur, le secret du consommateur et la version.

```python
wcdata = API(
    url='<BASE_URL>',
    consumer_key='ck_XXXXXXXXXXXXXXXXXXXX',
    consumer_secret='cs_XXXXXXXXXXXXXXXXXXXX',
    version='wc/v3'
)
```

Ensuite, j'ai utilisé la fonction GET pour appeler le point de terminaison "customers" et j'ai créé localement un fichier JSON ("contacts.json") avec les données que j'ai obtenues du point de terminaison que j'ai appelé juste avant :

```python
newJson = wcdata.get('customers').json()
with open('contacts.json', 'w') as f:
    json.dump(newJson, f, ensure_ascii=False, indent=4)
```

Je l'ai converti en un objet Pandas et je l'ai stocké dans la variable "df_json" :

```python
df_json = pd.read_json('contacts.json')
```

J'ai utilisé la fonction `to_excel()` pour transformer l'objet en un fichier Excel. J'ai passé à la fonction trois arguments :

* Le nom du fichier que j'allais créer
* L'index, défini sur "false" puisque je ne voulais pas que l'id d'enregistrement soit imprimé sur mon fichier
* Les colonnes que je voulais imprimer sur mon fichier (first_name et email)

```python
df_json.to_excel('customers_contacts.xlsx', index=False, columns=('first_name', 'email'))
```

J'ai exécuté le script et j'ai obtenu ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/6bis.png)

C'est tout. Voici comment j'ai créé un fichier Excel avec les emails et les prénoms des clients avec les APIs WooCommerce et Python en moins de 20 lignes de code.

Bien sûr, c'est un script que vous pouvez exécuter via la ligne de commande lorsque nécessaire ou que vous pouvez également automatiser pour générer régulièrement des rapports sur l'e-commerce que vous et votre équipe gérez.

## Réflexions finales

Je voulais également partager d'autres contenus que j'ai trouvés sur le web en étudiant pour développer ce script.

Le premier est une question Stack Overflow [question](https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file). Cela m'a aidé à optimiser mon code lors de la création du fichier JSON. J'ai vraiment apprécié la question choisie, surtout lorsqu'elle suggérait comment vous pouvez écrire un fichier JSON "plus joli" sur un système moderne.

Le second concerne Pandas. Si vous écrivez du code Python, un jour ou l'autre, vous devrez traiter des données et leur manipulation. Cet [article](https://www.marsja.se/how-to-convert-json-to-excel-python-pandas/) d'Erik Marsja explique vraiment bien comment vous pouvez convertir votre fichier JSON en Excel avec Pandas. Il fournit aux lecteurs plusieurs conseils sur la façon dont ils peuvent utiliser cette bibliothèque puissante pour afficher les données qu'ils veulent de manière efficace et efficace.

N'hésitez pas à partager cet article si vous l'avez trouvé utile ! Vous pouvez également trouver le code complet sur ce dépôt Github [repo](https://github.com/mventuri/-woocommerce-to-excel-python).
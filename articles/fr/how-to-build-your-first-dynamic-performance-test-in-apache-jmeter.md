---
title: Comment créer votre premier test de performance dynamique dans Apache JMeter
subtitle: ''
author: Mah Noor
co_authors: []
series: null
date: '2025-10-28T16:48:10.797Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-first-dynamic-performance-test-in-apache-jmeter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761335397152/cb105a44-4c18-4998-9ffb-d520df0e6510.png
tags:
- name: Scale Testing
  slug: scale-testing
- name: Performance Testing
  slug: performance-testing
- name: jmeter
  slug: jmeter
- name: scalability
  slug: scalability
- name: Quality Assurance
  slug: quality-assurance
- name: Testing
  slug: testing
seo_title: Comment créer votre premier test de performance dynamique dans Apache JMeter
seo_desc: As a QA engineer, I have always found performance testing to be one of the
  most exciting and underrated parts of software testing. Yes, functional testing
  is important, but it’s of little use if users have to wait for 5 seconds for each
  page to load....
---

En tant qu'ingénieur QA, j'ai toujours trouvé que les tests de performance étaient l'une des parties les plus passionnantes et les plus sous-estimées des tests logiciels. Certes, les tests fonctionnels sont importants, mais ils sont peu utiles si les utilisateurs doivent attendre 5 secondes pour que chaque page se charge.

Pour moi personnellement, il y a une profonde satisfaction à voir son produit prendre vie sous la charge pour découvrir comment il fonctionnera réellement en production lorsque des milliers d'utilisateurs l'utiliseront.

Le test de performance consiste à découvrir comment votre système se comporte sous une pression réelle en termes de charge, de concurrence et de débit. L'un des aspects clés des tests de performance est de s'assurer que les API peuvent supporter la charge attendue. Vous pouvez le faire en utilisant des outils comme Apache JMeter et K6.

Dans ce tutoriel, nous explorerons comment vous pouvez construire votre premier test de performance de bout en bout dans Apache JMeter. Vous apprendrez à créer une suite de tests dynamique (le test peut être exécuté avec n'importe quelle donnée de test) et exécutable en un clic (l'exécution du test peut se faire via l'interface graphique ainsi que via le CLI).

## Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Introduction à Apache JMeter](#heading-introduction-a-apache-jmeter)
    
    * [Étape 1 : Créer un nouveau plan de test](#heading-etape-1-creer-un-nouveau-plan-de-test)
        
    * [Étape 2 : Configurer le groupe d'unités](#heading-etape-2-configurer-le-groupe-dunites)
        
    * [Étape 3 : Ajouter des valeurs par défaut pour les requêtes HTTP](#heading-etape-3-ajouter-des-valeurs-par-defaut-pour-les-requetes-http)
        
    * [Étape 4 : Ajouter une configuration de données CSV (Entrée dynamique)](#heading-etape-4-ajouter-une-configuration-de-donnees-csv-entree-dynamique)
        
    * [Étape 5 : Ajouter l'échantillonneur de requête HTTP](#heading-etape-5-ajouter-lechantillonneur-de-requete-http)
        
    * [Étape 6 : Ajouter un extracteur JSON](#heading-etape-6-ajouter-un-extracteur-json)
        
    * [Étape 7 : Ajouter une assertion](#heading-etape-7-ajouter-une-assertion)
        
    * [Étape 8 : Ajouter des récepteurs](#heading-etape-8-ajouter-des-recepteurs)
        
    * [Étape 9 : Lancer votre test](#heading-etape-9-lancer-votre-test)
        
    * [Étape 10 : Enchaîner une autre requête (Optionnel)](#heading-etape-10-enchainer-une-autre-requete-optionnel)
        
    * [Étape 11 : Analyser les résultats](#heading-etape-11-analyser-les-resultats)
        
    * [Conseils de pro](#heading-conseils-de-pro)
        
    * [Exemple de structure de dossiers :](#heading-exemple-de-structure-de-dossiers)
        
3. [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir :

* [**Apache JMeter (5.5 ou supérieur)**](https://jmeter.apache.org/download_jmeter.cgi) installé.
    
* [**Java 8 ou ultérieur**](https://www.java.com/en/download/manual.jsp) configuré sur votre système.
    

Vous pouvez vérifier si JMeter est installé en exécutant la commande ci-dessous :

```plaintext
jmeter -v
```

**Note :** Ce tutoriel utilisera l'API publique [JSONPlaceholder](https://jsonplaceholder.typicode.com/). Vous apprendrez comment obtenir un post\_id et l'utiliser dans une requête en chaîne pour obtenir les détails de l'utilisateur.

Commençons.

## Introduction à Apache JMeter

Apache JMeter est un outil open-source de test de charge et de stress pour les API. C'est un outil de test puissant qui prend en charge un large éventail de protocoles, notamment HTTP, HTTPS, FTP, JDBC, SOAP et REST.

JMeter vous aide à répondre à des questions critiques sur vos API, telles que :

* Comment mon API se comporte-t-elle sous une charge lourde ?
    
* Quel est le nombre maximum d'utilisateurs qu'elle peut gérer avant de commencer à échouer ?
    
* Quelles requêtes ou points de terminaison ralentissent les choses ?
    

Passons en revue le processus étape par étape pour construire une suite de tests de charge dynamique avec JMeter.

### Étape 1 : Créer un nouveau plan de test

Une fois JMeter ouvert, vous verrez un Plan de test vide. Considérez-le comme votre espace de travail principal, qui contient tout : configuration des tests, utilisateurs, requêtes, assertions et résultats.

Faites un clic droit sur **Plan de test → Ajouter → Threads (Utilisateurs) → Groupe d'unités** pour ajouter un groupe d'unités. Un groupe d'unités est essentiellement une suite de tests contenant nos cas de test.

![Ajouter un groupe d'unités](https://cdn.hashnode.com/res/hashnode/image/upload/v1761045558747/ad3a2fe3-de59-420f-ba9d-1a36323e1d9e.png align="left")

### Étape 2 : Configurer le groupe d'unités

Pour configurer le groupe d'unités, remplissez les champs de saisie suivants :

| Paramètre | Valeur | Description |
| --- | --- | --- |
| Nombre d'unités (Threads) | 5 | Cela représente le nombre d'utilisateurs simultanés. Dans ce cas, ce sera '5' |
| Durée de montée en charge (secondes) | 10 | C'est le temps nécessaire aux threads pour atteindre la valeur maximale. |
| Nombre d'itérations | 2 | Spécifie le nombre de fois que vous souhaitez que votre groupe d'unités soit exécuté. |

Vous avez maintenant créé un petit test de charge contrôlé de 10 requêtes au total (5 utilisateurs × 2 itérations).

![Groupe d'unités](https://cdn.hashnode.com/res/hashnode/image/upload/v1761049951497/8221336c-5f10-4161-81fa-d0ad27c7164f.png align="center")

### Étape 3 : Ajouter des valeurs par défaut pour les requêtes HTTP

Lorsque vous créez une suite de centaines d'API, vous n'avez pas besoin d'ajouter les détails de votre requête à tous les échantillonneurs d'API dans JMeter. JMeter vous permet de les définir une fois globalement en utilisant un élément de configuration appelé Valeurs par défaut pour les requêtes HTTP. Pour ajouter cet élément, suivez les étapes ci-dessous :

1. Faites un clic droit sur **Groupe d'unités → Ajouter → Élément de configuration → Valeurs par défaut pour les requêtes HTTP.**
    
2. Saisissez les informations suivantes :
    
    * **Protocole :** `https`
        
    * **Nom du serveur ou IP :** [`jsonplaceholder.typicode.com`](http://jsonplaceholder.typicode.com)
        

Cela signifie que toutes les requêtes de ce test utiliseront automatiquement cette URL de base.

### Étape 4 : Ajouter une configuration de données CSV (Entrée dynamique)

Dans les projets réels, les API utilisent rarement des entrées statiques. Prenez par exemple une API de connexion que vous souhaitez exécuter pour 100 utilisateurs simultanés. Dans un scénario réel, chaque requête de connexion aura un nom d'utilisateur et un mot de passe différents.

Pour reproduire cela sur JMeter, vous devez exécuter votre test pour 100 identifiants de connexion différents. Cela signifie que votre test doit être **piloté par les données**. Nous pouvons construire un test piloté par les données dans JMeter en utilisant un **fichier CSV** :

1. Créez un fichier nommé `data.csv` avec le contenu suivant :
    
    ```plaintext
    post_id
    1
    2
    3
    4
    5
    ```
    
2. Enregistrez-le dans votre dossier de projet JMeter.
    
3. Dans JMeter, faites un clic droit sur **Groupe d'unités → Ajouter → Élément de configuration → Utilisation de données CSV.**
    
    ![Ajouter une configuration de données CSV](https://cdn.hashnode.com/res/hashnode/image/upload/v1761048312824/4558aae4-23c8-446d-89d0-237aca29619d.png align="center")
    
4. Remplissez les champs suivants :
    
    * **Nom du fichier :** `data.csv`
        
    * **Noms des variables :** `post_id`
        
    * **Recycler à la fin du fichier :** `True`
        
    * **Arrêter le thread à la fin du fichier :** `False`
        
        ![Configuration de données CSV](https://cdn.hashnode.com/res/hashnode/image/upload/v1761048167041/eae27f5c-6e23-4c7d-8890-b3eb5943bb66.png align="center")
        

Désormais, chaque utilisateur choisira un nouveau `post_id` pour chaque itération à partir du fichier CSV.

### Étape 5 : Ajouter l'échantillonneur de requête HTTP

Ajoutons maintenant l'appel API réel que nous allons tester sous charge. Pour ce faire, suivez les étapes ci-dessous :

1. Faites un clic droit sur **Groupe d'unités → Ajouter → Échantillonneur → Requête HTTP.**
    
    ![Ajouter une requête HTTP](https://cdn.hashnode.com/res/hashnode/image/upload/v1761051865320/92bf89d0-616c-4d07-9531-3985265e07d7.png align="center")
    
2. Renommez-le en **Get Post Data.**
    
3. Définissez les champs suivants :
    
    * **Méthode :** GET
        
    * **Chemin :** `/posts/${post_id}`
        

Ici, `${post_id}` prend dynamiquement sa valeur de votre fichier CSV. Les champs Protocole et IP du serveur obtiendront automatiquement les données de l'élément de configuration 'Valeurs par défaut pour les requêtes HTTP' que nous avons ajouté à l'étape 3.

![Ajouter une requête GET](https://cdn.hashnode.com/res/hashnode/image/upload/v1761049282841/a420139c-4622-4d7a-ac7d-4308bb9a1dbc.png align="center")

### Étape 6 : Ajouter un extracteur JSON

Lorsque l'API renvoie une réponse, nous pouvons en extraire une valeur (comme `userId`) et l'utiliser plus tard. Ceci est utilisé pour implémenter un flux de bout en bout où les données sont récupérées (avec GET) d'une API et envoyées à l'API POST/DELETE suivante.

Pour notre API, voici l'exemple de réponse :

```plaintext
{
  "userId": 1,
  "id": 3,
  "title": "fugiat veniam minus",
  "body": "This is an example post body"
}
```

Pour extraire `userId` :

1. Faites un clic droit sur **Get Post Data → Ajouter → Post-processeurs → Extracteur JSON.**
    
    ![Ajouter un extracteur JSON](https://cdn.hashnode.com/res/hashnode/image/upload/v1761051791176/b7888a78-efbb-48d3-8aba-fcd21edfd8f2.png align="center")
    
2. Définissez les variables ci-dessous dans l'extracteur JSON :
    
    * **Nom :** Extract User ID
        
    * **Nom de la variable :** `user_id`
        
    * **Expression JSON Path :** `$.userId`
        

![Extracteur JSON](https://cdn.hashnode.com/res/hashnode/image/upload/v1761049324410/8a163733-8925-4557-9ace-124b08167f8e.png align="center")

Vous pouvez maintenant utiliser `${user_id}` dans la requête suivante, rendant votre test entièrement dynamique.

### Étape 7 : Ajouter une assertion

Les assertions vous aident à vérifier que votre API répond correctement même sous charge. Vous pouvez effectuer une assertion sur le code de réponse de l'API, le temps de réponse ou même le corps de la réponse. Pour ajouter une assertion, suivez les étapes ci-dessous :

1. Faites un clic droit sur **Get Post Data → Ajouter → Assertions → Assertion Réponse.**
    
    ![Ajouter une assertion réponse](https://cdn.hashnode.com/res/hashnode/image/upload/v1761049384591/a0293eef-74a0-4d55-b0c4-232d5c5eaa0c.png align="center")
    
2. Configurez comme suit :
    
    * **Section de réponse à tester :** *Code de réponse –* Cela ajoutera une assertion pour le code de réponse.
        
    * **Type de correspondance :** *Comprend*
        
    * **Motifs à tester :** 200
        

![Ajouter une assertion réponse](https://cdn.hashnode.com/res/hashnode/image/upload/v1761050184412/5a52f600-74f6-48c7-a975-7e39df47afdb.png align="center")

Cela garantit que JMeter ne compte la requête comme réussie que si le code 200 est retourné.

### Étape 8 : Ajouter des récepteurs

Nous ajouterons des récepteurs (Listeners) pour afficher nos résultats de test sous différentes formes, visuellement ou sous forme de résumé. Ajoutons-en deux essentiels :

1. **Arbre de résultats** : pour visualiser et déboguer les requêtes individuelles.
    
2. **Rapport de synthèse** : pour visualiser les métriques de performance telles que le temps de réponse, le taux d'erreur et le débit.
    

Ajoutez-les via **Groupe d'unités → Ajouter → Récepteur → \[Choisir le récepteur\]**

![Ajouter un récepteur dans JMeter](https://cdn.hashnode.com/res/hashnode/image/upload/v1761049568483/0daa916c-503d-4f91-ad17-1d2bd29a9f72.png align="center")

### Étape 9 : Lancer votre test

Appuyez sur le bouton vert **Démarrer** en haut. JMeter commencera à envoyer des requêtes à votre API en utilisant les IDs de post dynamiques de votre fichier CSV.

Pendant l'exécution du test :

* Les coches vertes dans l'**Arbre de résultats** signifient des réponses réussies.
    
* Les échecs d'assertion apparaîtront en rouge.
    
* Le **Rapport de synthèse** agrégera les métriques clés.
    

![JMeter Arbre de résultats](https://cdn.hashnode.com/res/hashnode/image/upload/v1761050151356/d8c72408-cf91-4c9d-8663-0a65b6943f5b.png align="center")

![JMeter Rapport de synthèse](https://cdn.hashnode.com/res/hashnode/image/upload/v1761050211424/532dd999-b870-4cf8-ad1e-1a692119b0e0.png align="center")

### Étape 10 : Enchaîner une autre requête (Optionnel)

Allons un peu plus loin : nous allons utiliser le `user_id` extrait de la première réponse pour obtenir les détails de l'utilisateur à partir de l'appel [GET users](https://jsonplaceholder.typicode.com/users). Pour ce faire, suivez les étapes ci-dessous :

1. Faites un clic droit sur **Groupe d'unités → Ajouter → Échantillonneur → Requête HTTP.**
    
2. Renommez en **Get User Details.**
    
3. Définissez :
    
    * **Méthode :** GET
        
    * **Chemin :** `/users/${user_id}`
        
        ![API GET Users](https://cdn.hashnode.com/res/hashnode/image/upload/v1761050384264/dcc1c333-4e06-4dd9-8dca-9af823fedabd.png align="center")
        

![Exécution du test dans JMeter](https://cdn.hashnode.com/res/hashnode/image/upload/v1761050365937/736b9954-6d01-45a6-8c16-f6d2ceb60e10.png align="center")

### Étape 11 : Analyser les résultats

Une fois le test terminé, ouvrez le **Rapport de synthèse**. Vous verrez :

| Métrique | Description |
| --- | --- |
| **Nb d'échantillons** | Nombre total de requêtes envoyées |
| **Moyenne** | Temps de réponse moyen par requête |
| **Min/Max** | Temps de réponse le plus rapide et le plus lent |
| **% d'Erreur** | Pourcentage de requêtes ayant échoué |
| **Débit** | Requêtes traitées par seconde |

Si votre pourcentage d'erreur est de 0 % et que le débit est stable, votre système a bien géré la charge.

### Conseils de pro

* **Paramétrez tout.** Utilisez plusieurs fichiers CSV pour des flux de test réalistes (utilisateurs, IDs, jetons).
    
* **Ajoutez des compteurs de temps** (comme le *Compteur de temps fixe*) pour simuler le temps de réflexion entre les actions de l'utilisateur.
    
* **Utilisez les assertions à bon escient.** N'ajoutez pas d'assertions superflues ; concentrez-vous sur les validations clés telles que le temps de réponse et le code d'état de l'API.
    
* **Générez des rapports HTML en utilisant la commande ci-dessous :**
    
    ```plaintext
    jmeter -n -t test-plan.jmx -l results.jtl -e -o report
    ```
    

### Exemple de structure de dossiers :

Suivez la structure de dossiers ci-dessous pour une suite de tests organisée.

```plaintext
performance-test/
├── data.csv
├── test-plan.jmx
└── results/
    ├── summary.csv
    └── report.html
```

## Conclusion

Le test de performance est un élément essentiel de la liste de contrôle de préparation à la production pour tout produit. Il vous aide à vous assurer que votre produit peut gérer la charge utilisateur attendue et évoluer de manière fluide.

Ce guide est votre première étape vers l'écriture de cas de test de performance de bout en bout et pour combler le fossé entre être un ingénieur de test fonctionnel et un ingénieur QA full-stack qui comprend à la fois la qualité et la scalabilité.

J'espère que vous avez trouvé ce tutoriel utile. Si vous souhaitez rester connecté ou en savoir plus sur les tests de performance, suivez-moi sur [LinkedIn](https://www.linkedin.com/in/mah-noorqa/).
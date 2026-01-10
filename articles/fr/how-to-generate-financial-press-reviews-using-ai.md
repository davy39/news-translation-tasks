---
title: Comment générer des revues de presse financière à l'aide de l'IA
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2024-08-20T12:39:49.320Z'
originalURL: https://freecodecamp.org/news/how-to-generate-financial-press-reviews-using-ai
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724059022091/7ce2eba8-46ff-4d08-8e56-afa814cb68cc.jpeg
tags:
- name: AI
  slug: ai
- name: Python
  slug: python
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: Comment générer des revues de presse financière à l'aide de l'IA
seo_desc: In today’s fast-paced business environment, staying informed about the latest
  developments in your industry is crucial for making strategic decisions. Companies
  must know market trends, competitor activities, and potential risks to remain competitive...
---

Dans l'environnement commercial actuel, qui évolue rapidement, rester informé des derniers développements de votre secteur est crucial pour prendre des décisions stratégiques. Les entreprises doivent connaître les tendances du marché, les activités de leurs concurrents et les risques potentiels pour rester compétitives.

Un moyen efficace d'y parvenir est de générer des revues de presse financière complètes basées sur l'actualité récente. C'est là que mon script Python entre en jeu : un outil qui automatise la collecte et l'analyse des actualités liées à des requêtes spécifiques, permettant aux entreprises de rester à jour dans leur niche et de prendre des décisions éclairées sur leurs prochaines étapes. Bien entendu, ce script ne remplace pas le travail d'experts qui vérifieront et approfondiront ensuite les informations trouvées.

Voici ce que nous allons aborder :

* [L'importance de rester informé](#heading-limportance-de-rester-informe)
    
* [Aperçu du script Python](#heading-apercu-du-script-python)
    
* [Comment fonctionne le script](#heading-comment-fonctionne-le-script)
    
* [1\. Comment configurer l'environnement](#heading-1-comment-configurer-lenvironnement)
    
* [2\. Comment récupérer des actualités pertinentes](#heading-2-comment-recuperer-des-actualites-pertinentes)
    
* [3\. Comment préparer le prompt pour l'analyse par l'IA](#heading-3-comment-preparer-le-prompt-pour-lanalyse-par-lia)
    
* [4\. Comment générer la revue de presse](#heading-4-comment-generer-la-revue-de-presse)
    
* [5\. Comment sauvegarder le rapport](#heading-5-comment-sauvegarder-le-rapport)
    
* [Gestion des erreurs et journalisation](#heading-gestion-des-erreurs-et-journalisation)
    
* [Conclusion](#heading-conclusion)
    

## **L'importance de rester informé**

Pour toute entreprise, s'informer des dernières nouvelles de son secteur est plus qu'une simple bonne pratique. C'est une nécessité. Les événements marquants de l'actualité peuvent avoir un impact sur les marchés, influencer le comportement des consommateurs et affecter les chaînes d'approvisionnement.

En surveillant régulièrement les actualités pertinentes, les entreprises peuvent :

* **Identifier les tendances émergentes :** Repérer les tendances tôt peut donner à une entreprise un avantage concurrentiel, lui permettant de s'adapter et de capitaliser sur de nouvelles opportunités.
    
* **Surveiller les concurrents :** Comprendre ce que font les concurrents aide à affiner les stratégies et à garder une longueur d'avance sur le marché.
    
* **Atténuer les risques :** En restant informées des risques potentiels, tels que les changements réglementaires ou les ralentissements économiques, les entreprises peuvent ajuster proactivement leurs opérations pour minimiser l'impact.
    
* **Planifier des actions stratégiques :** Avec une compréhension claire du paysage du marché, les entreprises peuvent planifier leurs prochaines étapes avec plus de confiance.
    

Ce script Python automatise ce processus, permettant aux entreprises de générer des revues de presse financière détaillées basées sur des requêtes spécifiques, les aidant à mieux comprendre le marché et à planifier efficacement leurs prochains mouvements.

## Aperçu du script Python

Ce script Python est conçu pour récupérer des articles de presse sur le web, les analyser à l'aide d'un modèle de langage étendu (LLM) et générer une revue de presse structurée que les entreprises peuvent utiliser pour orienter leurs stratégies. Le script est construit avec Python, en s'appuyant sur deux bibliothèques puissantes :

1. **Bibliothèque Requests** : Elle est utilisée pour effectuer des requêtes HTTP vers l'API News, récupérant des articles de presse en fonction de la requête spécifiée.
    
2. **Bibliothèque Anthropic** : Cette bibliothèque est utilisée pour interagir avec le modèle d'IA Claude, qui traite les données d'actualité et génère une analyse complète.
    

Les revues de presse générées sont ensuite sauvegardées dans un fichier texte, que les entreprises peuvent consulter à leur convenance.

## Comment fonctionne le script

Décomposons le fonctionnement du script, étape par étape :

### 1\. Comment configurer l'environnement

Avant d'exécuter le script, assurez-vous que Python est installé sur votre système. De plus, vous devrez installer les bibliothèques Python nécessaires :

```python
pip install requests anthropic
```

### 2\. Comment récupérer des actualités pertinentes

Le script commence par déclarer la fonction `generate_report`. À l'intérieur de la fonction, j'ai effectué une requête GET vers l'API News, en utilisant la bibliothèque `requests` pour récupérer les derniers articles de presse liés à une requête spécifique. Voici l'extrait de code correspondant :

```python
response = requests.get('https://newsapi.org/v2/everything?q=' + query + '&apiKey=YOUR_API_KEY')
response_data = response.json()
```

Dans cette partie du script :

* `query` : C'est le mot-clé ou la phrase liée à la niche ou au sujet que vous souhaitez surveiller. Par exemple, une entreprise pourrait utiliser la requête `"finance"` pour récupérer des actualités liées au secteur financier.
    
* `response_data` : Les données d'actualité sont récupérées au format JSON, qui est ensuite analysé dans un dictionnaire Python pour un traitement ultérieur.
    

### 3\. Comment préparer le prompt pour l'analyse par l'IA

Une fois les données d'actualité récupérées, le script prépare un prompt pour alimenter le modèle d'IA Claude. Le prompt est conçu pour donner des instructions au modèle afin qu'il génère une revue de presse détaillée se concentrant sur l'impact des nouvelles sur les marchés financiers et des secteurs spécifiques. Voici comment le prompt est construit :

```python
prompt = (
    "Vous êtes un journaliste financier senior chargé de rédiger une revue de presse complète. "
    "Concentrez-vous sur les actualités clés fournies et analysez leur impact potentiel sur les marchés financiers, "
    "des secteurs spécifiques ou des entreprises concernées. Assurez-vous que la revue de presse est structurée et concise. "
    "Commencez le paragraphe par la phrase 'Ceci est la revue de presse concernant " + query + "'. "
    "Vous trouverez les actualités clés dans le fichier json suivant : " + response_data_to_str
)
```

Le prompt inclut :

* **Spécification du rôle** : L'IA est instruite d'agir comme un journaliste financier senior.
    
* **Description de la tâche** : Il est demandé à l'IA d'analyser les actualités et leur impact, en veillant à ce que la sortie soit structurée et concise.
    
* **Données d'actualité** : Les articles de presse récupérés sont transmis à l'IA au format JSON, fournissant le contexte nécessaire à l'analyse.
    

### 4\. Comment générer la revue de presse

Une fois le prompt prêt, le script interagit avec le modèle d'IA Anthropic Claude pour générer la revue de presse. La bibliothèque `anthropic` est utilisée pour cette interaction :

```python
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="Vous êtes un journaliste financier senior. Fournissez une revue de presse financière approfondie et perspicace ainsi que des conseils. Utilisez un langage technique approprié et tenez compte du contexte économique plus large dans vos réponses.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }
    ]
)
```

Dans cette partie du script :

* `client.messages.create` : Cette méthode envoie le prompt au modèle d'IA et récupère le texte généré.
    
* `plain_text` : La revue de presse résultante est stockée sous forme de texte brut, prête à être sauvegardée ou traitée ultérieurement.
    

### 5\. Comment sauvegarder le rapport

Enfin, la revue de presse générée est enregistrée dans un fichier texte :

```python
with open("report.txt", "a") as file:
    file.write(plain_text + "\n")
```

Cela garantit que chaque rapport généré est ajouté au fichier **report.txt**, ce qui facilite l'accès et l'examen de plusieurs rapports au fil du temps.

### Gestion des erreurs et journalisation

Une gestion robuste des erreurs est cruciale pour assurer le bon fonctionnement de l'application. Le script inclut une gestion de base des erreurs à l'aide de blocs `try-except` pour capturer et consigner les erreurs survenant pendant l'exécution :

```python
except requests.exceptions.RequestException as e:
    logging.error(f"Une erreur est survenue lors de la requête HTTP : {e}")
except Exception as e:
    logging.error(f"Une erreur inattendue est survenue : {e}")
```

Les erreurs sont enregistrées dans un fichier **error.log**, ce qui aide à résoudre les problèmes sans interrompre la fonctionnalité principale du script.

N'oubliez pas d'appeler la fonction en passant le sujet sur lequel vous souhaitez obtenir des informations comme paramètre :

```python
generate_report("finance")    
```

Et voici le code complet :

```python
import requests
import anthropic
import logging

# Configurer la journalisation pour capturer les erreurs dans un fichier nommé "error.log"
logging.basicConfig(filename="error.log", level=logging.ERROR)

def generate_report(query):
    try:
        # Étape 1 : Effectuer une requête GET vers l'API de news avec la requête donnée
        response = requests.get('https://newsapi.org/v2/everything?q=' + query + '&apiKey=<YOUR_API_KEY>')
        
        # Étape 2 : Analyser la réponse JSON de l'API dans un dictionnaire Python
        response_data = response.json()

        # Convertir les données JSON en format chaîne de caractères pour le prompt
        response_data_to_str = str(response_data)

        # Étape 3 : Initialiser le client Anthropic
        client = anthropic.Anthropic()

        # Étape 4 : Créer un prompt pour que le modèle d'IA génère une revue de presse financière
        prompt = (
            "Vous êtes un journaliste financier senior chargé de rédiger une revue de presse complète. "
            "Concentrez-vous sur les actualités clés fournies et analysez leur impact potentiel sur les marchés financiers, "
            "des secteurs spécifiques ou des entreprises concernées. Assurez-vous que la revue de presse est structurée et concise. "
            "Commencez le paragraphe par la phrase 'Ceci est la revue de presse concernant " + query + "'. "
            "Vous trouverez les actualités clés dans le fichier json suivant : " + response_data_to_str
        )

        # Étape 5 : Utiliser le prompt pour créer un message avec le modèle d'IA
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system=(
                "Vous êtes un journaliste financier senior. Fournissez une revue de presse financière approfondie et perspicace ainsi que des conseils. "
                "Utilisez un langage technique approprié et tenez compte du contexte économique plus laerge dans vos réponses."
            ),
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )

        # Étape 6 : Extraire le texte généré de la réponse du message
        plain_text = message.content[0].text

        # Étape 7 : Ajouter le rapport généré à un fichier nommé "report.txt"
        with open("report.txt", "a") as file:
            file.write(plain_text + "\n")
    
    except requests.exceptions.RequestException as e:
        # Journaliser les erreurs de requête HTTP dans "error.log"
        logging.error(f"Une erreur est survenue lors de la requête HTTP : {e}")
    except Exception as e:
        # Journaliser toute erreur inattendue dans "error.log"
        logging.error(f"Une erreur inattendue est survenue : {e}")

# Générer des rapports pour les requêtes nécessaires
generate_report("finance")
```

Après avoir exécuté le script, vous devriez obtenir un fichier **report.txt** ressemblant à ceci :

```plaintext
Ceci est la revue de presse concernant finance :

Les marchés financiers digèrent plusieurs développements clés cette semaine :

1. Données économiques : Le dernier rapport sur l'emploi a montré une légère augmentation du chômage, provoquant initialement une chute des marchés. Cependant, les experts appellent à ne pas surréagir, notant que l'économie ne se dirige pas vers un effondrement. La Réserve fédérale se rapproche d'une baisse des taux d'intérêt, les investisseurs pariant qu'une première coupe pourrait intervenir dès septembre si l'inflation continue de se modérer.

2. Résultats d'entreprises : La société XXX a publié des résultats décevants pour le deuxième trimestre, avec des pertes ayant plus que triplé pour atteindre 1,4 milliard de dollars dans un contexte de surveillance accrue de sa sécurité et de son contrôle qualité. La société YYY a également nommé un nouveau PDG qui a reçu des éloges précoces de clients clés. Pendant ce temps, une autre entreprise a mis en garde contre un ralentissement de la croissance et un affaiblissement de la demande américaine dans son rapport du T2.

3. Banque et Fintech : La société ZZZ est devenue l'entreprise technologique privée la plus précieuse d'Europe avec une valorisation de 45 milliards de dollars suite à une vente d'actions par les employés. Cela intensifie le défi des néo-banques face à la finance traditionnelle. La société a également obtenu récemment sa licence bancaire tant attendue au Royaume-Uni.

4. Développements réglementaires : La Banque Centrale envisage de créer une réserve stratégique de Bitcoin, qui serait partiellement financée par la réévaluation des certificats d'or détenus. Cela représente un changement majeur potentiel dans la politique des crypto-monnaies.

5. Finances personnelles : Les experts continuent de mettre en garde contre les erreurs d'argent courantes, même chez les personnes averties financièrement. Celles-ci incluent le fait d'attendre trop longtemps avant de commencer à investir et de ne pas planifier correctement la retraite.

Le sentiment général du marché reste prudent face à des signaux économiques mitigés et des tensions géopolitiques. Les investisseurs surveillent de près les politiques des banques centrales et les résultats des entreprises pour obtenir une direction plus claire.
```

### Conclusion

Dans un environnement commercial où rester informé est la clé du succès, ce script Python offre une solution automatisée pour générer des revues de presse financière basées sur les dernières actualités. En tirant parti de l'IA, les entreprises peuvent rapidement obtenir des informations sur les tendances du marché, surveiller les concurrents et prendre des décisions stratégiques éclairées. Bien que le script soit déjà fonctionnel et utile, avec des améliorations supplémentaires, il peut évoluer vers un outil puissant d'intelligence d'affaires, aidant les entreprises à garder une longueur d'avance dans leur secteur.

En automatisant le processus d'analyse de l'actualité, ce script permet non seulement de gagner du temps, mais fournit également une approche structurée pour comprendre le paysage commercial en constante évolution, donnant aux entreprises les moyens de passer aux étapes suivantes avec confiance.

Il est important de se rappeler qu'il s'agit d'un outil destiné à soutenir les analystes qui devront vérifier et évaluer les informations disponibles dans le rapport.

Si vous avez aimé cet article, n'hésitez pas à ajouter une étoile à mon [repo](https://github.com/mventuri/ai-powered-press-review) ici, j'ai hâte d'approuver votre PR !
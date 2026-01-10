---
title: Comment créer un gestionnaire de dépenses intelligent avec Python et les LLM
subtitle: ''
author: Happiness Omale
co_authors: []
series: null
date: '2025-09-08T15:06:16.193Z'
originalURL: https://freecodecamp.org/news/build-smart-expense-tracker-with-python-and-llms
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757342938389/164c8a45-d566-4de4-9a0f-cc9c270ce262.png
tags:
- name: Python
  slug: python
- name: llm
  slug: llm
- name: 'LLM''s '
  slug: llms
seo_title: Comment créer un gestionnaire de dépenses intelligent avec Python et les
  LLM
seo_desc: Imagine that you’re sipping a hot latte from Starbucks on your way to work.
  You quickly swipe your card, and the receipt gets lost in your bag. Later in the
  day, you pay for an Uber ride, order lunch, and buy airtime. By evening, you know
  you’ve spen...
---

Imaginez que vous sirotiez un latte bien chaud de chez Starbucks en allant au travail. Vous passez rapidement votre carte, et le reçu se perd au fond de votre sac. Plus tard dans la journée, vous payez une course Uber, commandez votre déjeuner et achetez du crédit téléphonique. Le soir venu, vous savez que vous avez dépensé de l'argent, mais vous ne pouvez pas dire précisément combien, ni où la majeure partie est passée.

C'est tout le défi des finances personnelles. Les gestionnaires de dépenses traditionnels existent, mais la plupart exigent de saisir manuellement chaque détail, de sélectionner des catégories et de générer des rapports. Après un certain temps, vous finissez par abandonner parce que cela semble demander plus de travail que cela n'en vaut la peine.

Mais et si votre gestionnaire était intelligent ? Et s'il pouvait :

* Comprendre automatiquement que « Dominos Pizza » doit être classé dans la catégorie *Nourriture et Boissons*.
    
* Résumer vos dépenses hebdomadaires en langage clair, du type : *« Cette semaine, vous avez dépensé 32 000 $ en transport, 15 000 $ en nourriture et 8 000 $ en shopping. »*
    
* Même vous montrer un joli graphique en secteurs de la répartition de votre argent ?
    

Dans ce tutoriel, nous allons construire exactement cela : un gestionnaire de dépenses intelligent utilisant Python et les modèles de langage (LLM). Nous commencerons par un tracker Python simple, puis nous l'améliorerons progressivement avec :

1. Un système de stockage de données pour les dépenses.
    
2. Une catégorisation automatique à l'aide de LLM.
    
3. Des visualisations pour rendre les schémas de dépenses plus explicites.
    

À la fin, vous aurez un gestionnaire de dépenses qui ne se contente pas d'enregistrer des données, mais qui interagit réellement, comprend vos dépenses et vous aide à prendre de meilleures décisions financières.

## Table des matières

1. [Comment configurer les données de dépenses](#heading-comment-configurer-les-donnees-de-depenses)
    
2. [Comment créer un gestionnaire de dépenses de base](#heading-comment-creer-un-gestionnaire-de-depenses-de-base)
    
3. [Comment le rendre intelligent avec les LLM (catégorisation automatique)](#heading-comment-le-rendre-intelligent-avec-les-llm-auto-categorization)
    
4. [Comment visualiser les dépenses](#heading-comment-visualiser-les-depenses)
    
5. [Comment créer un tableau de bord Streamlit simple](#heading-comment-creer-un-tableau-de-bord-streamlit-simple)
    
6. [Conclusion](#heading-conclusion)
    

## Comment configurer les données de dépenses

Avant de pouvoir construire un gestionnaire de dépenses, vous avez besoin de données de transaction réelles. Au lieu de créer un fichier CSV de zéro, utilisons un jeu de données de Kaggle : [*My Expenses Data*](https://www.kaggle.com/datasets/tharunprabu/my-expenses-data) [par Tharun Prabu](https://www.kaggle.com/datasets/tharunprabu/my-expenses-data).

Ce jeu de données contient des dépenses personnelles détaillées avec des colonnes telles que :

* Date : horodatage de la transaction.
    
* Account : d'où provient le paiement (compte bancaire, carte, etc.).
    
* Category / Subcategory : type de dépense.
    
* Note : une courte description comme « Brownie » ou « Métro ».
    
* Amount : le montant dépensé.
    
* Income/Expense : distingue l'argent gagné de l'argent dépensé.
    
* Certaines colonnes (comme `Note.1`, `Account.1`) semblent redondantes et peuvent être nettoyées.
    

### Comment charger les données en Python

Utilisez pandas pour lire le CSV :

```python
import pandas as pd

df = pd.read_csv("Expense_data_1.csv")
print(df.head())
```

Voici ce qui se passe ligne par ligne :

* `import pandas as pd` : Nous avons chargé la bibliothèque pandas et lui avons donné une abréviation courte (`pd`) pour ne pas avoir à taper `pandas` à chaque fois.
    
* [`pd.read_csv("Expense_data_1.csv")`](http://pd.read_csv) : Cela lit votre jeu de données de dépenses à partir d'un fichier CSV dans un DataFrame.
    
* `df.head()` : Affiche les 5 premières lignes du jeu de données, vous permettant d'examiner rapidement la structure des colonnes telles que *Date, Description, Amount, Category*, etc.
    

Sortie :

![Tableau montrant un échantillon de données de dépenses avec les colonnes Date, Account, Category, Note et Amount](https://cdn.hashnode.com/res/hashnode/image/upload/v1756334641937/a87e1fe8-2fa8-4b95-9732-b52ee836f7b1.jpeg align="center")

### Comment nettoyer les données

Comme vous n'avez pas besoin de toutes les colonnes, nettoyez le jeu de données pour ne garder que celles utiles au gestionnaire.

```python
data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]
print(data.head())
```

Voici ce qui se passe :

* `df[...]` : Cela indique à pandas que vous souhaitez uniquement sélectionner des colonnes spécifiques du DataFrame complet.
    
* `["Date", "Category", "Note", "Amount", "Income/Expense"]` : Ce sont les colonnes que nous avons choisi de conserver :
    
    * `Date` : Quand la dépense a eu lieu.
        
    * `Category` : Étiquette comme Alimentation, Transport, Divertissement.
        
    * `Note` : Courte description (par exemple, « Shawarma », « Course Uber »).
        
    * `Amount` : Combien vous avez dépensé.
        
    * `Income/Expense` : S'il s'agit d'une sortie ou d'une entrée d'argent.
        
* `print(data.head())` : Encore une fois, nous regardons les 5 premières lignes pour nous assurer que notre jeu de données est maintenant propre et ciblé.
    

Sortie :

![Tableau montrant des données de dépenses avec les colonnes Date, Category, Note, Amount et Expense/Income.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756335752749/13188d2d-b5ad-4dcf-b219-5b2f704767a1.jpeg align="center")

Nous avons maintenant un jeu de données propre avec :

* `Date`
    
* `Category`
    
* `Note` (courte description)
    
* `Amount`
    
* `Income/Expense`
    

C'est suffisant pour commencer à construire notre gestionnaire de dépenses de base.

## Comment créer un gestionnaire de dépenses de base

Imaginez que c'est le week-end :

* Le vendredi soir, vous prenez un shawarma après le travail.
    
* Le samedi matin, vous payez votre abonnement Netflix pour rattraper vos séries préférées.
    
* Plus tard dans la journée, vous commandez une course Uber pour rejoindre des amis.
    
* Le dimanche après-midi, vous les rejoignez pour des jeux en plein air dans un centre sportif local.
    

Ne serait-ce pas agréable de consigner tout cela automatiquement dans votre gestionnaire et de voir d'un coup d'œil combien vous avez dépensé durant le week-end ? Faisons cela.

1. ### Comment ajouter plusieurs dépenses
    

Nous allons écrire une fonction qui prend une date, une catégorie, une note, un montant et un type (Revenu/Dépense) et l'ajoute à notre dataframe.

```python
def add_expense(date, category, note, amount, exp_type="Expense"):
    global data
    new_entry = {
        "Date": date,
        "Category": category,
        "Note": note,
        "Amount": amount,
        "Income/Expense": exp_type
    }
    data = data.append(new_entry, ignore_index=True)
    print(f" Ajouté : {note} - {amount} ({category})")

add_expense("2025-08-22 19:30", "Food", "Shawarma", 2500, "Expense")
add_expense("2025-08-23 08:00", "Subscriptions", "Netflix Monthly Plan", 4500, "Expense")
add_expense("2025-08-24 14:00", "Entertainment", "Outdoor Games with friends", 7000, "Expense")
```

#### Voici ce qui se passe :

* `def add_expense(...)` : Nous avons défini une fonction appelée `add_expense` qui prend les détails d'une nouvelle transaction.
    
* `global data` : Cela garantit que la nouvelle dépense est ajoutée à votre jeu de données principal (`data`) plutôt qu'à une copie temporaire.
    
* `new_entry = {...}` : Nous avons créé un dictionnaire pour la nouvelle ligne, avec des clés correspondant aux colonnes de notre DataFrame.
    
* `data.append(...)` : Ajoute la nouvelle entrée à notre jeu de données. `ignore_index=True` permet de s'assurer que l'index des lignes se réinitialise correctement.
    
* `print(...)` : Confirme ce qui vient d'être ajouté.
    

Sortie :

![Image montrant les données de dépenses ajoutées](https://cdn.hashnode.com/res/hashnode/image/upload/v1756456560141/93cc57ca-cfcb-4a40-892d-9657b00a5918.jpeg align="center")

2. ### Comment afficher les dépenses récentes
    

```python
def view_expenses(n=5):
    return data.tail(n)
print(view_expenses(5))
```

#### Voici ce qui se passe :

* `def view_expenses(n=5):` : Définit une fonction qui affiche les `n` dernières lignes de notre jeu de données. Par défaut, `n=5`.
    
* `data.tail(n)` : La méthode `tail()` de Pandas renvoie les `n` dernières lignes du DataFrame.
    
* `print(view_expenses(5))` : Affiche les 5 dernières dépenses pour confirmer qu'elles ont été correctement enregistrées.
    

Sortie :

![Tableau montrant les données de dépenses récentes.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756456611837/f571b6ee-3bd0-45a8-b7cd-2d6a67f0e242.jpeg align="center")

3. ### Comment résumer les dépenses
    

```python
def summarize_expenses(by="Category"):
    summary = data[data["Income/Expense"]=="Expense"].groupby(by)["Amount"].sum()
    return summary.sort_values(ascending=False)
print(summarize_expenses())
```

#### Voici ce qui se passe :

1. `data[data["Income/Expense"]=="Expense"]` : Filtre le jeu de données pour n'inclure que les dépenses (ignore les revenus).
    
2. `.groupby(by)["Amount"].sum()` : Groupe les dépenses par colonne (par défaut = `"Category"`) et additionne tous les montants de chaque groupe. Par exemple, toutes les dépenses de *Nourriture* sont additionnées.
    
3. `.sort_values(ascending=False)` : Trie les catégories par dépense totale, de la plus élevée à la plus basse.
    

Sortie :

![Tableau montrant le résumé des dépenses](https://cdn.hashnode.com/res/hashnode/image/upload/v1756456680569/4e86263c-4b7b-4f00-80e2-d633b8c479cd.jpeg align="center")

Cela montre que sur le week-end :

* Vous avez dépensé 7000 en *Divertissement* (jeux de plein air).
    
* 4500 sont allés aux *Abonnements* (Netflix).
    
* 25896 en *Nourriture*.
    

Ce gestionnaire permet de voir très clairement où va votre argent, même sans IA pour le moment.

## Comment le rendre intelligent avec les LLM (catégorisation automatique)

Nous allons utiliser un LLM pour lire la colonne Note (comme *Shawarma*, *Netflix*, *Uber*, *Match de foot*) puis attribuer automatiquement la catégorie la plus pertinente.

1. **Choisir une API LLM**
    
    * Vous pouvez utiliser OpenAI GPT.
        
    * Exemple de catégories que nous prendrons en charge :
        
        * Nourriture (Food)
            
        * Transport
            
        * Divertissement (Entertainment)
            
        * Autre (Other)
            
2. **Prompter le LLM**  
    Nous enverrons quelque chose comme :
    
    > « Catégorisez cette note de dépense dans l'une de celles-ci : Nourriture, Transport, Divertissement, Autre. Note : Netflix. »  
    > Le modèle renverra : `Abonnement`.
    
3. **Intégrer dans notre pipeline**
    
    * Enregistrer la catégorie prédite dans le jeu de données.
        

```python
from openai import OpenAI  
client = OpenAI(api_key="VOTRE_CLE_API")

def auto_categorize(note):
    prompt = f"""
    Categorize this expense note into one of these categories: 
    Food, Transportation, Entertainment, Other.
    Note: {note}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Other"

data['Category'] = data.apply(
    lambda row: auto_categorize(row['Note']) if pd.isna(row['Category']) else row['Category'],
    axis=1
)

print(data[['Note', 'Category']].head(10))
```

#### Voici ce qui se passe :

1. Ingénierie de prompt (Prompt engineering) : Nous donnons des instructions claires au modèle :
    
    * Choisir parmi *Food, Transportation, Entertainment, Other*.
        
    * Lui donner la `Note` (par exemple, *Shawarma*, *Course Uber*, *Abonnement mensuel Netflix*).
        
2. Appel API OpenAI : Envoie la requête à `gpt-4o-mini` (un modèle rapide et léger).
    
3. Retourne la prédiction : Le modèle choisit la catégorie la plus probable.
    
4. Si la catégorie d'une ligne est manquante, il demande au LLM d'en prédire une à partir de la note.
    
5. Sinon, il conserve la catégorie saisie manuellement par l'utilisateur.
    
6. `data[['Note', 'Category']]` : Sélectionne uniquement les colonnes Note (entrée utilisateur) et Category (prédite par l'IA ou fournie par l'utilisateur).
    
7. `.head(10)` : Affiche les 10 premières lignes pour une vérification rapide.
    

Sortie :

![Tableau montrant la catégorisation des dépenses](https://cdn.hashnode.com/res/hashnode/image/upload/v1756456793309/83f686cf-658c-4456-8d21-0ca8a80e2b20.jpeg align="center")

Désormais, notre gestionnaire est assez intelligent pour deviner automatiquement les catégories.

## Comment visualiser les dépenses

Actuellement, notre gestionnaire est intelligent : il peut reconnaître une ligne comme *« Payé 7 000 pour Netflix »* et la catégoriser dans Abonnement. Mais des chiffres bruts dans un tableau ne vous procurent pas encore ce déclic visuel. Nous avons besoin d'un moyen de voir où part l'argent.

Imaginons que nous sommes à la fin du mois. Vous regardez votre solde bancaire en vous demandant : *« Où est passé tout mon argent ? »* Au lieu de faire défiler indéfiniment les transactions, notre gestionnaire propose un tableau de bord clair avec des visuels qui racontent l'histoire d'un seul coup d'œil.

Nous utiliserons Matplotlib pour construire deux graphiques :

1. Graphique en secteurs (Pie Chart) – pour voir la part en pourcentage de chaque catégorie.
    
2. Graphique en barres (Bar Chart) – pour comparer les montants réels dépensés entre les catégories.
    

```python
import matplotlib.pyplot as plt
expense_summary = data[data['Category'] != 'Income'].groupby("Category")["Amount"].sum()

# Graphique en secteurs
plt.figure(figsize=(6,6))
expense_summary.plot.pie(autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("Répartition des dépenses par catégorie")
plt.ylabel("")
plt.show()

# Graphique en barres
plt.figure(figsize=(8,5))
expense_summary.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Dépenses par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Montant dépensé")
plt.show()
```

#### Voici ce qui se passe :

1. `groupby("Category")["Amount"].sum()` : Groupe le jeu de données par catégorie et calcule le total dépensé par catégorie.
    
2. Graphique en secteurs : Affiche rapidement la *répartition en pourcentage* des dépenses par catégorie. Par exemple, si la « Nourriture » représente 20 % des dépenses, vous le verrez instantanément.
    
3. Graphique en barres : Affiche les *valeurs absolues* des dépenses par catégorie, ce qui permet de voir facilement quelle catégorie a la dépense totale la plus élevée ou la plus basse.
    

Sortie :

![Graphique en secteurs montrant la répartition en pourcentage des dépenses par catégorie.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756456884383/663058d1-e9f9-428d-912d-8a16cd456235.jpeg align="center")

![Graphique en barres montrant le total des dépenses groupées par catégorie.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756456902426/abbef7c3-0575-45a1-8a67-f9d06f2948fd.jpeg align="center")

Ce que ces visuels nous disent :

* Le graphique en secteurs répond à la question : *« Qu'est-ce qui me coûte le plus cher ? »*
    
* Le graphique en barres permet de comparer facilement les catégories côte à côte. Par exemple, vous pourriez réaliser que vous dépensez presque autant en transport qu'en abonnements et vie sociale combinés.
    

À ce stade, vous êtes passé de chiffres bruts à des informations exploitables.

## Comment créer un tableau de bord Streamlit simple

Imaginez que vous ayez terminé de coder et que vous vouliez maintenant voir vos habitudes de dépenses dans un tableau de bord élégant que vous avez construit vous-même. C'est là qu'intervient Streamlit.

En quelques lignes, vous pouvez transformer votre gestionnaire de dépenses en une application web interactive où vous pouvez saisir de nouvelles dépenses directement depuis l'application, mettre à jour le DataFrame en temps réel, les catégoriser automatiquement avec des LLM et voir les graphiques mis à jour. Et aussi les sauvegarder dans votre `expenses.csv`.

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

from openai import OpenAI
client = OpenAI(api_key="VOTRE_CLE_API")

def predict_category(description):
    prompt = f"""
    You are a financial assistant. Categorize this expense into one of:
    ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Shopping', 'Others'].

    Expense: "{description}"
    Just return the category name.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

csv_file = "expense_data_1.csv"
if os.path.exists(csv_file):
    data = pd.read_csv(csv_file)
else:
    data = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])

st.title("Gestionnaire de dépenses intelligent")

with st.form("expense_form"):
    date = st.date_input("Date")
    description = st.text_input("Description")
    amount = st.number_input("Montant", min_value=0.0, format="%.2f")

    predicted_category = ""
    if description:
        predicted_category = predict_category(description)

    category = st.text_input(
        "Catégorie (prédite automatiquement, modifiable)", 
        value=predicted_category
    )

    submitted = st.form_submit_button("Ajouter la dépense")

    if submitted:
        new_expense = {"Date": date, "Description": description, "Amount": amount, "Category": category}
        data = pd.concat([data, pd.DataFrame([new_expense])], ignore_index=True)
        data.to_csv(csv_file, index=False)
        st.success(f"Ajouté : {description} - {amount} ({category})")

st.subheader("Toutes les dépenses")
st.dataframe(data)

if not data.empty:
    st.subheader("Répartition des dépenses par catégorie")

    category_totals = data.groupby("Category")["Amount"].sum()

    # Graphique en barres
    fig, ax = plt.subplots()
    category_totals.plot(kind="bar", ax=ax)
    ax.set_ylabel("Montant")
    st.pyplot(fig)

    # Graphique en secteurs
    st.subheader("Distribution par catégorie")
    fig2, ax2 = plt.subplots()
    category_totals.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    st.pyplot(fig2)
```

Voici ce qui se passe :

1. Saisie par formulaire avec prédictions intelligentes
    
    * Les utilisateurs saisissent la Date, la Description et le Montant.
        
    * Dès que vous tapez « Abonnement Netflix », le LLM suggère automatiquement *Entertainment*.
        
2. Stockage des dépenses dans un fichier CSV
    
    * Chaque nouvelle entrée est enregistrée dans `expense_data_1.csv`, afin que votre historique ne disparaisse pas au redémarrage de l'application.
        
3. Tableau de bord interactif
    
    * Un tableau affiche toutes les dépenses enregistrées.
        
    * Les graphiques en barres et en secteurs se mettent à jour instantanément à mesure que de nouvelles données sont ajoutées.
        

Lancez le fichier :

![Image montrant comment lancer votre application Streamlit](https://cdn.hashnode.com/res/hashnode/image/upload/v1756468770764/8ab43931-cd37-4791-826f-2ec47bb8dd4b.jpeg align="center")

Sortie :

![Image de l'application de suivi des dépenses Streamlit montrant un formulaire de saisie et des graphiques affichant la répartition des dépenses par catégorie.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756458330622/83081c5e-4be7-4dc6-a32c-02a5cf78371a.jpeg align="center")

### Conclusion

Utiliser Streamlit pour créer un gestionnaire de dépenses personnelles est un moyen pratique de combiner la collecte de données, la visualisation et l'assistance de l'IA dans une seule application interactive. En plus de l'enregistrement des entrées, nous avons intégré une fonctionnalité alimentée par LLM pour prédire automatiquement les catégories de dépenses, facilitant ainsi le processus pour les utilisateurs qui préfèrent ne pas étiqueter manuellement chaque transaction.

Ce projet montre comment des outils tels que Streamlit pour l'interactivité, Pandas pour le traitement des données et les LLM pour les prédictions intelligentes peuvent être combinés pour résoudre des problèmes quotidiens de manière simple mais puissante. Que ce soit pour un usage personnel ou comme projet de portfolio, ce gestionnaire démontre comment les compétences en machine learning et en science des données peuvent être appliquées à des cas d'utilisation réels qui simplifient la vie.
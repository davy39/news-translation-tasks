---
title: Comment économiser du temps et de l'argent en créant un planificateur de repas
  automatique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T16:17:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-save-time-and-money-by-building-an-automatic-meal-planner-7c7a9351d124
coverImage: https://cdn-media-1.freecodecamp.org/images/0*s7pV_mfdT_FlIhCW
tags:
- name: api
  slug: api
- name: Life Hacking
  slug: life-hacking
- name: Productivity
  slug: productivity
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment économiser du temps et de l'argent en créant un planificateur de
  repas automatique
seo_desc: 'By Bert Carremans

  Use the Google Calendar and Google Sheets APIs to select the right recipe on the
  right day.

  Do you also get stressed out when you get the question “what’s for dinner tonight?”
  You’re not alone. I guess it’s the most asked question a...'
---

Par Bert Carremans

#### Utilisez les API Google Calendar et Google Sheets pour sélectionner la bonne recette au bon jour.

Vous aussi, vous stressez quand on vous pose la question « Qu'est-ce qu'on mange ce soir ? » Vous n'êtes pas seul. Je pense que c'est la question la plus posée quand l'horloge sonne 16 heures. Décider quoi manger peut être une corvée fastidieuse. Surtout quand on a de jeunes enfants avec diverses activités extrascolaires.

Pour éviter d'aller au supermarché tous les jours, nous écrivons généralement un menu avec des recettes pour la semaine à venir. Ainsi, nous pouvons acheter toutes nos courses en une seule visite au supermarché. Cela nous fait gagner beaucoup de temps. En plus, cela nous fait économiser de l'argent. C'est parce que nous sommes moins exposés à toutes les astuces de vente [que les supermarchés utilisent](https://www.rd.com/health/healthy-eating/supermarket-tricks/).

Trouver des recettes pour toute une semaine nécessite une certaine réflexion et planification. Nous devons prendre en compte les préférences alimentaires de tous les membres de la famille. En plus de cela, nous avons un temps limité disponible pour cuisiner chaque jour. Pour faciliter cela, j'ai construit un planificateur de repas automatique avec ces fonctionnalités :

* extraire le planning de travail pour moi et ma femme de nos calendriers Google partagés
* extraire nos recettes préférées d'une feuille de calcul Google,
* répéter certaines recettes chaque semaine le même jour
* laisser une semaine entre avant de répéter les autres recettes
* J'aime cuisiner plus que ma femme. Donc les jours où je ne peux pas cuisiner, les recettes doivent être courtes en temps
* télécharger le menu de la semaine dans un calendrier Google

Commençons tout de suite.

### Utilisation de l'API Google Calendar et de l'API Google Sheets

Tout d'abord, nous devons [créer un nouveau projet Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects). Avant de pouvoir utiliser le calendrier Google et les feuilles dans ce projet, nous devons activer les API. Cela est très bien expliqué sur les pages web ci-dessous :

* [Activation de l'API Google Calendar](https://developers.google.com/calendar/quickstart/python)
* [Activation de l'API Google Sheets](https://developers.google.com/sheets/api/quickstart/python)

Une fois cela fait, nous continuons en important les packages Python nécessaires.

```
import config as cfg
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from google.oauth2 import service_account
```

### Configuration

Pour des raisons de confidentialité et de sécurité, je garde certains paramètres dans un fichier config.py séparé. Nous importons le fichier avec l'alias `cfg`. Je discuterai de ces paramètres plus loin avec des valeurs fictives. Vous pouvez les inclure pour votre propre application avec des valeurs pertinentes pour votre cas.

#### Portées

Avec les portées, nous définissons les niveaux d'accès pour les calendriers Google et les feuilles. Nous aurons besoin d'un accès en lecture et en écriture à la fois pour les [calendriers](https://developers.google.com/calendar/auth) et les [feuilles](https://developers.google.com/sheets/api/guides/authorizing). Ainsi, nous utilisons les URL ci-dessous.

```python
SCOPES = ['https://www.googleapis.com/auth/calendar'
          , 'https://www.googleapis.com/auth/spreadsheets']
```

#### ID de la feuille Google et plage

```python
SPREADSHEET_ID = <Votre ID de feuille Google>
RANGE = 'recepten!A:G'
```

Nous devons spécifier l'ID de la feuille Google contenant les recettes. De plus, nous spécifions la plage de la feuille contenant les recettes.

Vous pouvez trouver l'ID de vos feuilles Google en faisant un clic droit sur la feuille dans Google Drive. Ensuite, sélectionnez « Obtenir le lien partageable ». Vous pouvez trouver l'ID après « https://drive.google.com/open?id= ».

Dans ma feuille Google « recepten », les colonnes A à G contiennent des informations sur chaque recette. La capture d'écran ci-dessous montre un exemple de contenu. Donc `RANGE` doit être défini sur « recepten!A:G ».

![Image](https://cdn-media-1.freecodecamp.org/images/NsQwKBmPmvZY-OYzX30WqMo9GC8j3NKV4XR1)

#### ID des calendriers Google

```python
CALENDARID_1 = <Votre ID de calendrier Google>
CALENDARID_2 = <ID du calendrier Google de votre partenaire>
CALENDARID_WEEKMENU = <ID du calendrier Google pour le menu de la semaine>
```

Nous devons spécifier les ID des calendriers Google pour obtenir les événements. Assurez-vous d'avoir accès à tous les calendriers que vous souhaitez inclure. Vous pouvez trouver l'ID en exécutant ce [script de l'explorateur d'API](https://developers.google.com/apis-explorer/#p/calendar/v3/calendar.calendarList.list).

Pour ce projet, nous extrairons les événements de seulement deux calendriers. Mais vous pourriez adapter le code pour boucler sur plus de calendriers. J'ai également créé un calendrier séparé pour télécharger les recettes.

#### Étiquettes des événements

```python
BUSY_EVENTS = [<Étiquettes des événements de calendrier occupés>]
FREE_EVENTS = [<Étiquettes des événements de calendrier libres>]
ALL_EVENTS = BUSY_EVENTS + FREE_EVENTS
```

Ma femme travaille en équipes et ajoute ses horaires à son calendrier Google en utilisant des codes de lettres. Par exemple : « B » signifie l'équipe de l'après-midi. Cet événement est l'un des `BUSY_EVENTS`.

Quand j'ai un jour de congé, j'ajoute « HOLIDAY » à mon calendrier. Cet événement est l'un des `FREE_EVENTS`.

Tous les événements sont des événements de toute la journée dans les calendriers Google. Vous pouvez utiliser votre propre schéma d'étiquettes d'événements.

#### Traditions

```python
TRADITIONS = {   'Thursday' : 'frites'}
```

Par `TRADITIONS`, j'entends que notre famille a quelques jours dans la semaine où nous préparons une certaine recette. Comme nous sommes de Belgique, cela signifie manger des frites une fois par semaine (pour nous le jeudi). Et oui, avant que vous ne demandiez, ce sont des frites avec de la mayonnaise.

Vous pouvez spécifier vos propres traditions dans un dictionnaire, avec le nom du jour comme clé et la recette comme valeur.

#### Nombre de jours à planifier à l'avance

Parfois, nous ne pouvons pas aller au supermarché le jour où un nouveau menu de la semaine est créé. Nous pourrions avoir besoin de quelques jours pour planifier à l'avance. Avec `NB_DAYS_BEFORE`, nous nous donnons un peu de marge. Cela signifie que le nouveau menu de la semaine sera généré un certain nombre de jours avant que le menu de la semaine précédente ne soit terminé.

```
NB_DAYS_BEFORE = 3
```

### Utilisation d'un compte de service

Nous utiliserons un [compte de service](https://developers.google.com/api-client-library/python/auth/service-accounts) pour utiliser les API dans le projet. Le fichier credentials.json est le fichier que vous pouvez télécharger lors de l'activation des API.

Nous créons les identifiants `creds` avec le code ci-dessous. Ces identifiants permettent l'authentification dans les calendriers Google et la feuille Google.

```python
creds = service_account.Credentials.from_service_account_file("credentials.json", scopes=cfg.SCOPES)
```

### Obtention des événements du calendrier Google

Nous commençons par créer l'objet de service avec la méthode `build`.

```
service_cal = build('calendar', 'v3', credentials=creds)
```

Nous ne sommes intéressés que par les événements de la semaine à venir. Pour filtrer ces événements, nous spécifions les dates et les formatons avec `isoformat()`. Les paramètres `timeMin` et `timeMax` nécessitent ce format.

```
def format_date(date):
    date_time = datetime.combine(date, datetime.min.time())
    date_time_utc = date_time.isoformat() + 'Z'
    return date_time_utc
```

Avec la méthode [events().list](https://developers.google.com/calendar/v3/reference/events/list) de l'objet de service, nous extrayons les événements. Les événements extraits sont ensuite filtrés pour les événements BUSY et FREE. Tous les autres événements sur les calendriers Google ne sont pas pertinents dans ce projet. Nous conservons la date de début et de fin et le résumé des événements.

```
def get_event_date(event, timepoint):
    return event[timepoint].get('dateTime', event[timepoint].get('date'))

def get_events_by_calendarId(service, calendarId, timeMin, timeMax, allEvents):
    events_result = service.events().list(calendarId=calendarId
                                        , timeMin=timeMin
                                        , timeMax=timeMax
                                        , singleEvents=True
                                        , orderBy='startTime').execute()
    events = events_result.get('items', [])    
    events_list = [(get_event_date(e, 'start'), get_event_date(e, 'end'), e['summary'].upper()) 
                   for e in events 
                   if e['summary'].upper() in allEvents]
    return unfold_events_list(events_list)
```

Certains événements s'étendent sur plus d'un jour. Par exemple, lorsque vous prenez des vacances pendant plus d'un jour. Nous développons ces événements multi-jours en événements quotidiens dans la plage de la semaine à venir.

```
def unfold_events_list(events_list):
    new_events_list = []
    for e in events_list:
        start = datetime.strptime(e[0], '%Y-%m-%d').date()
        end = datetime.strptime(e[1], '%Y-%m-%d').date()
        delta_days = (end - start).days

        if delta_days > 1:
            for d in range(delta_days):
                unfolded_day = start + timedelta(days=d)
                if unfolded_day >= datetime.now().date() and unfolded_day <= datetime.now().date() + timedelta(days=6):
                    new_events_list.append((unfolded_day, e[2]))
        else:
            new_events_list.append((start, e[2]))
    return new_events_list
```

Enfin, nous voulons un DataFrame Pandas avec les événements des deux calendriers pour la semaine à venir. Pour obtenir ce résultat, nous convertissons les listes d'événements en data frames et fusionnons sur la date. Nous ajoutons également le jour de la semaine au data frame fusionné.

```
def create_events_df(events_list_1, events_list_2):
    events_df_1 = pd.DataFrame.from_records(events_list_1, columns=['date', 'events_cal_1'])
    events_df_2 = pd.DataFrame.from_records(events_list_2, columns=['date', 'events_cal_2'])
    events_df = events_df_1.merge(events_df_2, on='date', how='outer')
    events_df.date = pd.to_datetime(events_df.date)
    events_df.set_index('date', inplace=True)
    events_df.sort_index(inplace=True)

    dates = list(pd.period_range(START_DAY, NEXT_WEEK, freq='D').values)
    new_idx = []
    for d in dates:
        new_idx.append(np.datetime64(d))

    events_df = events_df.reindex(new_idx)
    events_df.reset_index(inplace=True)
    events_df['weekday'] = events_df.date.apply(lambda x: x.strftime('%A'))
    events_df.set_index('date', inplace=True)
    return events_df
```

Pour nous assurer de couvrir toutes les dates de la semaine à venir, nous utilisons une `period_range` et réindexons le data frame fusionné.

### Obtention des recettes de la feuille Google

À ce stade, nous avons un data frame avec tous les jours de la semaine à venir et les événements (le cas échéant) survenant dans les deux calendriers. Maintenant, nous pouvons commencer à extraire les recettes de la feuille Google et attribuer une recette à chaque jour. Comme avec l'API Google Calendar, commençons par créer l'objet de service pour l'API Google Sheets.

```
service_sheet = build('sheets', 'v4', credentials=creds)
```

Avec la méthode [spreadsheets().values().get](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get), nous pouvons extraire les recettes de la feuille Google.

```
def get_recipes(service, spreadsheetId, range):
    recipes_result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range).execute()
    recipes = recipes_result.get('values', [])
    recipes_df = pd.DataFrame.from_records(recipes[1:], columns=recipes[0])
    recipes_df.last_date_on_menu = pd.to_datetime(recipes_df.last_date_on_menu, dayfirst=True)
    recipes_df.set_index('row_number', inplace=True)
    eligible_recipes = recipes_df[ (recipes_df.last_date_on_menu < PREV_WEEK) | (np.isnat(recipes_df.last_date_on_menu)) ]
    return recipes_df, eligible_recipes
```

Ensuite, nous créons un data frame avec les recettes. J'aime travailler avec les DataFrames Pandas, mais vous pourriez utiliser d'autres structures de données bien sûr.

Le `row_number` est un champ calculé dans la feuille Google elle-même. Nous utilisons la fonction de feuille Google `ROW()` pour cela. Cela aidera à mettre à jour le champ `last_date_on_menu` dans la bonne ligne. Nous mettrons à jour cette date lorsqu'une recette est choisie pour la semaine à venir.

Nous devons nous assurer qu'une recette n'est répétée qu'après une semaine. Donc nous filtrons `recipes_df` par `last_date_on_menu`. Cette date doit être vide ou avant la semaine précédente.

### Génération du menu de la semaine

Dans cette étape, nous attribuerons une recette éligible à chaque jour de la semaine à venir.

```
def generate_weekmenu(service, events_df, traditions, free_events):
    weekmenu_df = events_df.copy()

    for i, r in events_df.iterrows():
        if r.weekday in traditions.keys():
            weekmenu_df.loc[i, 'recipe'] = traditions[r.weekday]
            weekmenu_df.loc[i, 'description'] = ''
        else:
            if r.weekday in ['Saturday', 'Sunday']:
                row_number = choose_recipe('difficult', i, weekmenu_df, eligible_recipes)
                update_sheet(service, row_number, i.strftime('%d-%m-%Y'), cfg.SPREADSHEET_ID)
            elif r.events_cal_1 in free_events or r.events_cal_2 in free_events \
            or pd.isnull(r.events_cal_1) or pd.isnull(r.events_cal_2):
                row_number = choose_recipe('medium', i, weekmenu_df, eligible_recipes)
                update_sheet(service, row_number, i.strftime('%d-%m-%Y'), cfg.SPREADSHEET_ID)
            else:
                row_number = choose_recipe('easy', i, weekmenu_df, eligible_recipes)
                update_sheet(service, row_number, i.strftime('%d-%m-%Y'), cfg.SPREADSHEET_ID)
    return weekmenu_df
```

Pour prendre en compte le planning de travail (événements BUSY et FREE), nous utiliserons la `difficulté` de chaque recette. Une recette aléatoire de la difficulté préférée sera ajoutée à `weekmenu_df`. Enfin, nous la supprimons des recettes éligibles pour éviter les recettes en double dans la même semaine.

```python
def choose_recipe(difficulty, idx, weekmenu_df, eligible_recipes):
    choice_idx = np.random.choice(eligible_recipes.query("difficulty == '" + difficulty + "'" ).index.values)
    weekmenu_df.loc[idx, 'recipe'] = eligible_recipes.loc[choice_idx, 'recipe']
    weekmenu_df.loc[idx, 'description'] = eligible_recipes.loc[choice_idx, 'description']
    eligible_recipes.drop(choice_idx, inplace=True)
    return choice_idx
```

La méthode [spreadsheets().values().update](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update) met à jour la feuille Google.

```python
def update_sheet(service, row_number, date, spreadsheetId):
    range = "recepten!F"  + str(row_number)
    values = [[date]]
    body = {'values' : values}
    result = service.spreadsheets().values().update(spreadsheetId=spreadsheetId
                                                    , range=range
                                                    , valueInputOption='USER_ENTERED'
                                                    , body=body).execute()
```

Nous itérons sur chaque ligne de `weekmenu_df`. Si le jour de la semaine est l'un des jours de la semaine TRADITIONS, nous attribuons la recette correspondante. Pour les autres jours de la semaine, nous appliquons la logique suivante :

* Le week-end, choisir une recette difficile
* Pendant la semaine, quand je suis à la maison ou que ma femme a un jour de congé, choisir une recette de difficulté moyenne
* Pendant la semaine, quand je ou ma femme sommes au travail, choisir une recette facile

### Ajout du menu de la semaine à un calendrier Google

Maintenant que nous avons un menu pour la semaine à venir, nous pouvons l'ajouter en tant qu'événements à un calendrier Google. J'ai créé un calendrier séparé pour cela. Partagez ce calendrier avec le `client_email` dans credentials.json. Dans les paramètres de votre calendrier, vous devez également lui donner la permission de faire des modifications dans les événements.

```
def add_weekmenu_to_calendar(service, weekmenu_df, calendarId):
    for i, r in weekmenu_df.iterrows():
        event = {
        'summary': r.recipe,
        'description': r.description,
        'start': {
            'date': i.date().isoformat(),
            'timeZone': 'Europe/Brussels'
        },
        'end': {
            'date': i.date().isoformat(),
            'timeZone': 'Europe/Brussels'
        }
        }
        event = service.events().insert(calendarId=calendarId, body=event).execute()
```

### Automatisons

Jusqu'à présent, nous avons pris en compte toutes les fonctionnalités demandées pour l'application. Mais vous devriez toujours exécuter le code manuellement pour générer le menu de la semaine.

J'ai trouvé ce site web génial [PythonAnyWhere](https://www.pythonanywhere.com/) où vous pouvez planifier des programmes Python. Le compte Débutant gratuit permet de planifier un programme Python sur une base quotidienne. C'est exactement ce dont nous avons besoin.

Tout d'abord, nous devons assembler toutes les fonctions et les mettre dans un fichier Python. Dans ce fichier, je fais une vérification supplémentaire pour voir où nous en sommes dans le menu de la semaine en cours. Je fais cela en regardant la dernière date avec une recette dans le calendrier Google avec `get_date_last_event`.

```
def get_date_last_event(service, calendarId):
    events_result = service.events().list(calendarId=calendarId
                                        , singleEvents=True
                                        , orderBy='startTime').execute()
    date_last_event = events_result.get('items', [])[-1]['start']['date'][:10]
    date_last_event = datetime.strptime(date_last_event, '%Y-%m-%d').date()
    return date_last_event
```

Cette date est stockée dans `DATE_LAST_RECIPE`. Si le jour actuel est après `DATE_LAST_RECIPE` moins `NB_DAYS_BEFORE`, nous pouvons générer un nouveau menu de la semaine.

Vous pouvez trouver le script complet sur [Github](https://github.com/bertcarremans/weekmenu/blob/master/generate_weekmenu.py).

```
if __name__ == '__main__':
    # Obtention des identifiants depuis credentials.json
    CREDS_PATH = Path.cwd() / "weekmenu" / "credentials.json"
    creds = service_account.Credentials.from_service_account_file(CREDS_PATH, scopes=cfg.SCOPES)

    # Création des objets de service
    service_cal = build('calendar', 'v3', credentials=creds)
    service_sheet = build('sheets', 'v4', credentials=creds)

    # Définition des dates
    DATE_LAST_RECIPE = get_date_last_event(service_cal, cfg.CALENDARID_WEEKMENU) 
    START_DAY = DATE_LAST_RECIPE + timedelta(days=1)
    NEXT_WEEK = START_DAY + timedelta(days=6)
    PREV_WEEK = START_DAY + timedelta(days=-7)
    START_DAY = format_date(START_DAY)
    NEXT_WEEK = format_date(NEXT_WEEK)
    PREV_WEEK = format_date(PREV_WEEK)

    # Obtention des recettes de la feuille Google
    recipes_df, eligible_recipes = get_recipes(service_sheet, cfg.SPREADSHEET_ID, cfg.RANGE)

    # Vérification si le dernier menu de la semaine est toujours actif
    if DATE_LAST_RECIPE - timedelta(days=cfg.NB_DAYS_BEFORE) < datetime.now().date():
        # Obtention des événements des calendriers Google
        events_list_1 = get_events_by_calendarId(service_cal, cfg.CALENDARID_1, START_DAY, NEXT_WEEK, cfg.ALL_EVENTS)
        events_list_2 = get_events_by_calendarId(service_cal, cfg.CALENDARID_2, START_DAY, NEXT_WEEK, cfg.ALL_EVENTS)

        # Fusion des deux listes d'événements
        events_df = create_events_df(events_list_1, events_list_2)

        # Génération du menu de la semaine
        weekmenu_df = generate_weekmenu(service_sheet, events_df, cfg.TRADITIONS, cfg.FREE_EVENTS)

        # Ajout du menu de la semaine à un calendrier Google
        add_weekmenu_to_calendar(service_cal, weekmenu_df, cfg.CALENDARID_WEEKMENU)
        print('Le menu de la semaine est ajouté au calendrier Google')
    else:
        print('Programme arrêté. Le dernier menu de la semaine n'est pas encore terminé.')
```

Sur PythonAnyWhere, j'ai créé un sous-dossier week menu. J'ai téléchargé les fichiers suivants : config.py, generate_weekmenu.py et credentials.json.

![Image](https://cdn-media-1.freecodecamp.org/images/RhtFm84JZutzhpZgJopF8gwsWlZJxqdgalRr)
_Fichiers du projet sur PythonAnyWhere.com_

J'ai ensuite planifié une tâche quotidienne qui exécutera le script generate_weekmenu.py dans la section Tâches. Et voilà, nous sommes prêts.

![Image](https://cdn-media-1.freecodecamp.org/images/ouqyRFUVYlqgjHektAW6MFS4yTd3YriPIDE9)

### Le résultat

Après la première exécution du script, nous avons un beau menu dans notre calendrier Google partagé.

![Image](https://cdn-media-1.freecodecamp.org/images/sVaq0YRZX3xTTN4EHwF-jThLXdOmCi31TPC2)
_Menu de la semaine automatisé dans un calendrier Google partagé_

### Conclusion

Ce script prend en compte votre emploi du temps professionnel sur vos calendriers Google. Il sélectionne vos recettes préférées à partir d'une feuille Google. Et en planifiant le script, les recettes apparaissent de manière automatisée dans votre calendrier Google. Cela vous libère de la corvée ennuyeuse de décider quoi manger.

Si vous voulez aller plus loin, voici quelques idées pour affiner le script :

* prendre en compte le temps de cuisson d'une recette
* permettre une tradition d'avoir au moins un repas végétarien par semaine
* générer une liste de courses pour les recettes choisies

J'espère que vous avez apprécié la lecture de cette histoire. Si vous avez des questions ou des suggestions sur le script, vous pouvez écrire un commentaire ci-dessous. Et si vous l'avez aimé, n'hésitez pas à applaudir.
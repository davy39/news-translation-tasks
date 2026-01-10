---
title: How to save time and money by building an automatic meal planner
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
seo_title: null
seo_desc: 'By Bert Carremans

  Use the Google Calendar and Google Sheets APIs to select the right recipe on the
  right day.

  Do you also get stressed out when you get the question “what’s for dinner tonight?”
  You’re not alone. I guess it’s the most asked question a...'
---

By Bert Carremans

#### Use the Google Calendar and Google Sheets APIs to select the right recipe on the right day.

Do you also get stressed out when you get the question “what’s for dinner tonight?” You’re not alone. I guess it’s the most asked question as the clock strikes 4 p.m. Deciding what to eat can be a tedious chore. Especially when you have small children with various after-school activities.

To avoid going to the supermarket every day, we usually write up a menu with recipes for the coming week. That way we can buy all our groceries in one supermarket visit. This saves us a lot of time. Besides that, it also saves us money. That is because we are less exposed to all the selling [tricks supermarkets use](https://www.rd.com/health/healthy-eating/supermarket-tricks/).

Finding recipes for a whole week requires some thinking and planning. We have to take into account the eating preferences of all family members. Besides that, we have a limited time available for cooking each day. To make this easier, I built an automatic meal planner with these features:

* extract the work planning for me and my wife from our shared Google calendars
* extract our preferred recipes from a Google spreadsheet,
* repeat some recipes each week on the same day
* leave one week in between before repeating the other recipes
* I like cooking more than my wife. So on days that I can’t cook the recipes should be short in time
* upload the week menu in a Google calendar

Let’s jump right in.

### Using the Google calendar API and Google sheets API

First, we’ll need to [create a new Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects). Before we can use the Google calendar and sheets in this project, we need to enable the API’s. This is very well explained on the web pages below:

* [Enabling the Google Calendar API](https://developers.google.com/calendar/quickstart/python)
* [Enabling the Google Sheets API](https://developers.google.com/sheets/api/quickstart/python)

When that’s done, we continue by importing the necessary Python packages.

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

For privacy and security reasons, I keep some parameters in a separate config.py file. We import the file with the alias `cfg`. I will discuss these parameters further below with fictitious values. You can include them for your own app with values relevant to your case.

#### Scopes

With scopes, we define the access levels for the Google calendars and sheets. We will need read and write access to both the [calendars](https://developers.google.com/calendar/auth) and [sheet](https://developers.google.com/sheets/api/guides/authorizing). Thus we use the URLs below.

```python
SCOPES = ['https://www.googleapis.com/auth/calendar'
          , 'https://www.googleapis.com/auth/spreadsheets']
```

#### Google sheet ID and range

```python
SPREADSHEET_ID = <Your Google sheet ID>
RANGE = 'recepten!A:G'
```

We need to specify the ID of the Google sheet with the recipes. Additionally, we specify the sheet range containing the recipes.

You can find the ID of your Google sheets by right-clicking on the sheet in Google Drive. Then select “Get shareable link”. You can find the ID after “https://drive.google.com/open?id=”.

In my Google sheet “recepten”, columns A to G contain information on each recipe. The screenshot below shows some sample content. So `RANGE` needs to be set to “recepten!A:G”_._

![Image](https://cdn-media-1.freecodecamp.org/images/NsQwKBmPmvZY-OYzX30WqMo9GC8j3NKV4XR1)

#### Google Calendar IDs

```python
CALENDARID_1 = <Your Google Calendar ID>
CALENDARID_2 = <Your partner's Google Calendar ID>
CALENDARID_WEEKMENU = <Google Calendar ID for the week menu>
```

We need to specify the Google Calendar IDs to get the events from. Make sure you have access to all calendars you want to include. You can find the ID by executing this [script from the APIs Explorer](https://developers.google.com/apis-explorer/#p/calendar/v3/calendar.calendarList.list).

For this project, we will extract the events of only two calendars. But you could adapt the code to loop over more calendars. I’ve also created a separate calendar to upload the recipes.

#### Event labels

```python
BUSY_EVENTS = [<Labels of busy calendar events>]
FREE_EVENTS = [<Labels of free calendar events>]
ALL_EVENTS = BUSY_EVENTS + FREE_EVENTS
```

My wife works in shifts and adds them to her Google Calendar by using letter codes. For example: “B” stands for the afternoon shift. This event is one of the `BUSY_EVENTS`.

When I have a day off, I add “HOLIDAY” to my calendar. This event is one of the `FREE_EVENTS.`

All the events are full-day events in the Google Calendars. You can use your own event labels scheme.

#### Traditions

```python
TRADITIONS = {   'Thursday' : 'fries'}
```

With `TRADITIONS`, I mean that our family has a few days in the week on which we prepare a certain recipe. As we are from Belgium, this means eating fries once a week (for us on Thursday). And yes, before you’d ask, that is fries with mayonnaise.

You can specify your own traditions in a dictionary, with the name of the day as the key and the recipe as the value.

#### Number of days to plan ahead

Sometimes we can’t go to the supermarket on the day a new week menu is created. We might need some days to plan ahead. With `NB_DAYS_BEFORE` we give ourselves some slack. This means that the new week menu will be generated a certain number of days before the previous week menu has finished.

```
NB_DAYS_BEFORE = 3
```

### Using a service account

We will use a [service account](https://developers.google.com/api-client-library/python/auth/service-accounts) to make use of the APIs in the project. The credentials.json file is the file that you can download when enabling the APIs.

We create the credentials `creds` with the code below. These credentials enable authentication in the Google Calendars and Google sheet.

```python
creds = service_account.Credentials.from_service_account_file("credentials.json", scopes=cfg.SCOPES)
```

### Getting the Google Calendar events

We start by creating the service object with the `build` method.

```
service_cal = build('calendar', 'v3', credentials=creds)
```

We are only interested in the events for the coming week. To filter these events, we specify the dates and format them with `isoformat()`. The parameters `timeMin` and `timeMax` need this format.

```
def format_date(date):
    date_time = datetime.combine(date, datetime.min.time())
    date_time_utc = date_time.isoformat() + 'Z'
    return date_time_utc
```

With the method [events().list](https://developers.google.com/calendar/v3/reference/events/list) of the service object, we extract the events. The extracted events are then filtered for the BUSY and FREE events. All other events on the Google Calendars are not relevant in this project. We keep the start and end date and the summary of the events.

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

Some events spread over more than one day. For example, when you take holidays for more than one day. We unfold these multi-day events in daily events within the range of the coming week.

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

Finally, we want a Pandas DataFrame with the events of both calendars for the coming week. To get to that result, we convert the events lists to data frames and merge on the date. We also add the weekday to the merged data frame.

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

To make sure we cover all dates of the coming week, we use a `period_range` and `reindex` the merged data frame.

### Getting the recipes from the Google sheet

At this point, we have a data frame with all days of the coming week and the events (if any) occurring in the two calendars. Now we can start to extract the recipes from the Google sheet and assign a recipe to each day. As with the Google Calendar API, let’s start by creating the service object for the Google Sheets API.

```
service_sheet = build('sheets', 'v4', credentials=creds)
```

With the method [spreadsheets().values().get](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get) we can extract the recipes from the Google Sheet.

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

Next, we create a data frame with the recipes. I like working with Pandas DataFrames, but you could use other data structures as well of course.

The `row_number` is a field calculated in the Google Sheet itself. We use the Google Sheet function `ROW()` for that. It will help to update the field `last_date_on_menu` in the correct row. We will update that date when a recipe is chosen for the coming week.

We need to make sure that a recipe is only repeated after one week. So we filter `recipes_df` by `last_date_on_menu`. This date must be empty or before the previous week.

### Generating the week menu

In this step, we will assign an eligible recipe to each day of the coming week.

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

To take into account the work planning (BUSY and FREE events), we will use the `difficulty` of each recipe. A random recipe of the preferred difficulty will be added to `weekmenu_df.` Finally we drop it from the eligible recipes to avoid duplicate recipes in the same week.

```python
def choose_recipe(difficulty, idx, weekmenu_df, eligible_recipes):
    choice_idx = np.random.choice(eligible_recipes.query("difficulty == '" + difficulty + "'" ).index.values)
    weekmenu_df.loc[idx, 'recipe'] = eligible_recipes.loc[choice_idx, 'recipe']
    weekmenu_df.loc[idx, 'description'] = eligible_recipes.loc[choice_idx, 'description']
    eligible_recipes.drop(choice_idx, inplace=True)
    return choice_idx
```

The method [spreadsheets().values().update](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update) updates the Google Sheet.

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

We iterate over each row of `weekmenu_df`. If the weekday is one of the TRADITIONS weekdays, we assign the corresponding recipe. For the other weekdays, we apply the following logic:

* In the weekend, choose a difficult recipe
* During the week, when I’m at home or my wife has a day off, choose a recipe with medium difficulty
* During the week, when I or my wife are at work, choose an easy recipe

### Adding the week menu to a Google Calendar

Now that we have a menu for the coming week, we can add it as events to a Google Calendar. I’ve created a separate calendar for it. Share this calendar with the `client_email` in credentials.json. In the settings of your calendar you also need to give it permission to make changes in the events.

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

### Let’s automate

Until now we have taken into account all the requested features for the application. But you would still have to run the code by hand to generate the week menu.

I found this great website [PythonAnyWhere](https://www.pythonanywhere.com/) where you can schedule Python programs. The free Beginner account allows to schedule one Python program on a daily basis. That’s exactly what we need.

First, we need to stitch all the functions together and put them in a Python file. In this file, I do an extra check to see where we are in the current week menu. I do this by looking at the last date with a recipe in the Google Calendar with `get_date_last_event.`

```
def get_date_last_event(service, calendarId):
    events_result = service.events().list(calendarId=calendarId
                                        , singleEvents=True
                                        , orderBy='startTime').execute()
    date_last_event = events_result.get('items', [])[-1]['start']['date'][:10]
    date_last_event = datetime.strptime(date_last_event, '%Y-%m-%d').date()
    return date_last_event
```

That date is stored in `DATE_LAST_RECIPE.` If the current day is after `DATE_LAST_RECIPE` minus `NB_DAYS_BEFORE` we can generate a new week menu.

You can find the complete script on [Github](https://github.com/bertcarremans/weekmenu/blob/master/generate_weekmenu.py).

```
if __name__ == '__main__':
    # Getting credentials from credentials.json
    CREDS_PATH = Path.cwd() / "weekmenu" / "credentials.json"
    creds = service_account.Credentials.from_service_account_file(CREDS_PATH, scopes=cfg.SCOPES)

    # Creating service objects
    service_cal = build('calendar', 'v3', credentials=creds)
    service_sheet = build('sheets', 'v4', credentials=creds)

    # Defining dates
    DATE_LAST_RECIPE = get_date_last_event(service_cal, cfg.CALENDARID_WEEKMENU) 
    START_DAY = DATE_LAST_RECIPE + timedelta(days=1)
    NEXT_WEEK = START_DAY + timedelta(days=6)
    PREV_WEEK = START_DAY + timedelta(days=-7)
    START_DAY = format_date(START_DAY)
    NEXT_WEEK = format_date(NEXT_WEEK)
    PREV_WEEK = format_date(PREV_WEEK)

    # Getting the recipes from the Google Sheet
    recipes_df, eligible_recipes = get_recipes(service_sheet, cfg.SPREADSHEET_ID, cfg.RANGE)

    # Check if the last weekmenu is still active
    if DATE_LAST_RECIPE - timedelta(days=cfg.NB_DAYS_BEFORE) < datetime.now().date():
        # Getting the events from the Google Calendars
        events_list_1 = get_events_by_calendarId(service_cal, cfg.CALENDARID_1, START_DAY, NEXT_WEEK, cfg.ALL_EVENTS)
        events_list_2 = get_events_by_calendarId(service_cal, cfg.CALENDARID_2, START_DAY, NEXT_WEEK, cfg.ALL_EVENTS)

        # Merge the two events lists
        events_df = create_events_df(events_list_1, events_list_2)

        # Generating the weekmenu
        weekmenu_df = generate_weekmenu(service_sheet, events_df, cfg.TRADITIONS, cfg.FREE_EVENTS)

        # Adding the weekmenu to a Google Calendar
        add_weekmenu_to_calendar(service_cal, weekmenu_df, cfg.CALENDARID_WEEKMENU)
        print('Week menu is added to Google Calendar')
    else:
        print('Program stopped. Last week menu is not finished yet.')
```

On PythonAnyWhere I’ve created a subfolder week menu. I’ve uploaded the following files config.py, generate_weekmenu.py and credentials.json.

![Image](https://cdn-media-1.freecodecamp.org/images/RhtFm84JZutzhpZgJopF8gwsWlZJxqdgalRr)
_Project files on PythonAnyWhere.com_

I then schedule a daily task that will run the generate_weekmenu.py script in the Tasks section. And voilà, we’re all set.

![Image](https://cdn-media-1.freecodecamp.org/images/ouqyRFUVYlqgjHektAW6MFS4yTd3YriPIDE9)

### The result

After the first run of the script, we have a nice menu in our shared Google calendar.

![Image](https://cdn-media-1.freecodecamp.org/images/sVaq0YRZX3xTTN4EHwF-jThLXdOmCi31TPC2)
_Automated week menu in a shared Google Calendar_

### Conclusion

This script takes into account your professional schedule on your Google calendars. It selects your preferred recipes from a Google sheet. And by scheduling the script the recipes appear in an automated way in your Google Calendar. This frees you from the annoying chore to decide what to eat.

If you want to take it further, here are some ideas to fine-tune the script:

* take into account the cooking time of a recipe
* allow a tradition of having at least one vegetarian meal per week
* generate a grocery list for the chose recipes

I hope you enjoyed reading this story. If you have questions or suggestions about the script you can write a comment below. And if you liked it, feel free to clap for it.


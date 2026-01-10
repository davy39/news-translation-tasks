---
title: How to Build a Tiered List Maker with Python
subtitle: ''
author: Atharva Shah
co_authors: []
series: null
date: '2023-07-07T20:48:16.000Z'
originalURL: https://freecodecamp.org/news/python-tier-list-maker
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/python-tier-list-1.png
tags:
- name: projects
  slug: projects
- name: Python
  slug: python
seo_title: null
seo_desc: 'Hello Pythonistas! Do you want to level up your Python and API skills while
  also building something really useful? Well, then you''re in the right place.

  This hands-on tutorial showcases how to leverage Python''s capabilities to code
  an interactive tie...'
---

Hello Pythonistas! Do you want to level up your Python and API skills while also building something really useful? Well, then you're in the right place.

This hands-on tutorial showcases how to leverage Python's capabilities to code an interactive tiered list builder right within your terminal.

We'll use some helpful Python libraries along the way to build a practical tool that allows you to rank and organize your favorite albums engagingly and efficiently in seconds.

## Project Overview

Tiered lists are categorizing tools used to rank objects based on likes. They're used in music, movies, and other areas. The album tiered list in this project allocates records to different levels depending on your personal choices.

This step-by-step guide leverages the power of Python libraries like [**Rich**](https://github.com/Textualize/rich)**,** [**PyLast**](https://github.com/pylast/pylast)**,** [**Pillow**](https://github.com/python-pillow/Pillow)**, and** [**Pick**](https://github.com/wong2/pick) to make a tiered list builder right within the terminal.

Consider easily categorizing your albums into different tiers, such as "S-Tier" for all-time favorites or "B-Tier" for those undiscovered gems. You'll have complete control over how your music collection is organized according to your preferences.

![A high level overview of the walkthrough](https://www.freecodecamp.org/news/content/images/2023/07/image-8.png align="left")

*A high level overview of the walkthrough*

At the end of this project, you can expect to export all your tiered lists. Here is an example of what it might look like. This can be done for any of the artists of your choice.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/MAC-DEMARCO-TIER-LIST.png align="left")

*Final project outcome*

## Get Your LastFM API Key

[LastFM](https://www.last.fm/) is a music database and online platform that offers a sophisticated music recommendation system as well as an API. It allows developers to access and download data from their database.

This is a necessary step because the CLI app requests the album metadata and cover from the LastFM API.

First, you'll want to create a [LastFM Developer Account](https://www.last.fm/api/account/create).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-7.png align="left")

*Never share API credentials. Use environment variables to store them.*

Next, copy the API Key and the Shared Secret. Set them as environment variables.

On Windows:

```javascript
setx LASTFM_API_KEY "your_api_key"
setx LASTFM_API_SECRET "your_api_secret"
```

On Linux/MacOS:

```javascript
export LASTFM_API_KEY="your_api_key"
export LASTFM_API_SECRET="your_api_secret"
```

## Import the Modules

Here are the modules you need to have installed to kickstart the project:

* `json`: Encoding and decoding JSON responses from APIs.
    
* `os`: File and directory operations.
    
* `datetime`: Formatting and mathematical operations on date and time.
    
* `io`: Stream-like interface for in-memory byte data.
    
* `typing`: Type-hinting for improved readability
    
* `pylast`: A Python wrapper library around the LastFM API.
    
* `requests`: Make HTTP requests with online services and APIs.
    
* `pick`: An interactive selection menu for selecting from a list directly in the terminal.
    
* `PIL`: Image processing and manipulation (for example, drawing, resizing, and saving)
    
* `rich`: Lovely terminal formatting.
    

Get these installed using the pip (Python package manager).

```javascript
pip install pylast requests pick Pillow rich
```

Now that the setup is done, spin up your code editor, and let's get to building.

```py
import json
import os
from datetime import datetime
from io import BytesIO
from typing import List

import pylast
import requests
from pick import pick
from PIL import Image, ImageDraw, ImageFont
from rich import print
from rich.panel import Panel
from rich.table import Table
```

## Kickstart With An Interactive Menu

This is a CLI-based application. So any choices you make will be made directly within the terminal. Two choices are presented at the startup screen to the user:

1. **Create a Tiered List:** Enter the name of the list and the artist. The application will fetch metadata and album covers from the LastFM API and save them to a JSON file.
    
2. **Export the Tiered List to Image:** Use Pandas to export the gathered JSON data to a beautiful PNG/JPG image. The image will have rows and columns to indicate tiers and albums.
    

To start, let's present an interactive menu to the user:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-12.png align="left")

*The pick module presents a choice selection menu in the terminal. Use arrow keys to navigate and hit Enter to confirm.*

Ignore the first four options, as they are out of the scope of this walkthrough. You can just use the `pass` statement instead of invoking those functions to prevent any errors.

To achieve this, you will need to write the following driver code at the end of your file.

```py
LASTFM_API_KEY = os.environ.get("LASTFM_API_KEY")
LASTFM_API_SECRET = os.environ.get("LASTFM_API_SECRET")
network = pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)

def start():    
    global network
    startup_question = "What Do You Want To Do?"
    options = ["Rate by Album", "Rate Songs", "See Albums Rated", "See Songs Rated", "Make a Tier List", "See Created Tier Lists", "EXIT"]
    selected_option, index = pick(options, startup_question, indicator="→")
    
    if index == 0:
        rate_by_album()
    elif index == 1:
        rate_by_song()
    elif index == 2:
        see_albums_rated()
    elif index == 3:
        see_songs_rated()
    elif index == 4:
        create_tier_list()
    elif index == 5:
        see_tier_lists()
    elif index == 6:
        exit()
start()
```

As seen in the code above, the `os.environ.get()` function retrieves the value of an environment variable you set in the previous section.

`network` is probably the most important variable. It has a lot of methods attached to it. These methods include:

* Fetching albums of an artist
    
* Fetching metadata about an artist
    
* Fetching metadata about an album
    
* Fetching album covers
    
* Error validation by checking for the 200 (OK) response status.
    

Then, `start()` initiates the application, presents a startup question using the `pick` function, stores user choices, and executes various actions based on the selected option.

The `pick` method accepts the following parameters:

* `**options**`: The list of options to choose from. These will be the list of albums.
    
* `**title**`: The title or question to display to the user. The tier list name.
    
* `**multiselect**`: A flag indicating whether multiple options can be selected. Multiple choice or single choice.
    
* `**indicator**`: The symbol or character used to indicate the selected option.
    
* `**min_selection_count**`: The minimum number of options that must be selected. This choice only allows one selection, the default value.
    

Note: **All the code below has to be placed above the driver code**. We are going to define several functions, one for each option.

## How to Save State in JSON

JSON files are easy to work with and maintain even as the app schema changes. This is why you will be storing the tier list data in JSON format. It's a persistent storage method that allows you to update the album and song ratings, as well as tier lists, even when the program is rerun.

Surely you don't want the user data to be lost when the application restarts? Therefore, a save state is required. It's a database most of the time. But for the sake of simplicity, let's store and retrieve user data using JSON.

```py
def load_or_create_json() -> None:
    if os.path.exists("albums.json"):
        with open("albums.json") as f:
            ratings = json.load(f)
    else:
        # create a new json file with empty dict
        with open("albums.json", "w") as f:
            ratings = {"album_ratings": [], "song_ratings": [], "tier_lists": []}
            json.dump(ratings, f)
```

This custom function either loads an existing JSON file or produces one if none exists. It guarantees that the application has a file for storing and retrieving album and song ratings, as well as tier lists.

If the file does not exist, it creates a new file named "albums.json" in write mode. Then initialize the `ratings` variable as a dictionary containing empty lists. `json.dump()` writes the contents of the `ratings` dictionary to the JSON file.

## How to Write Utility Functions

Utility or helper functions in menu-driven programming perform common tasks or operations related to menu options. These functions are reusable and modular, making code more organized and easier to maintain. Examples include:

* Display Menu
    
* Input Validation
    
* Data Persistence
    
* Formatting and Display
    
* Error Handling
    
* Common Operations.
    

These functions handle common tasks required by multiple menu options, promoting code reusability and reducing redundancy. Encapsulating these functions in menu logic helps maintain code flow, and facilitates testing, debugging, and future modifications.

Think of them as bridges that help connect two functions better and isolate trivial logic that can be used on the fly. This project relies on two helper functions.

### Remove album from list

First, we'll write a function to remove the picked album from the list to prevent repetition across different tiers. Here's what that looks like:

```py
def create_tier_list_helper(albums_to_rank, tier_name):
    # if there are no more albums to rank, return an empty list
    if not albums_to_rank:
        return []
    
    question = f"Select the albums you want to rank in  {tier_name}"
    tier_picks = pick(options=albums_to_rank, title=question, multiselect=True, indicator="→", min_selection_count=0)
    tier_picks = [x[0] for x in tier_picks]
    
    for album in tier_picks:
        albums_to_rank.remove(album)

    return tier_picks
```

This allows users to rank albums inside certain tiers and facilitates the creation of tier lists.

It requires two arguments: `albums_to_rank` and `tier_name`. If there are no more albums to rank, the function produces an empty list. Users can choose albums to rate from albums to rank, save them in tier picks, remove them, and return the tier picks list.

The returned value `tier_picks` is a Python list.

### Return cover of selected album

Next, write a function that returns the cover of an album users select. Here's what it looks like:

```py
def get_album_cover(artist, album):
    album = network.get_album(artist, album)
    album_cover = album.get_cover_image()
    # check if it is a valid url
    try:
        response = requests.get(album_cover)
        if response.status_code != 200:
            album_cover = "https://community.mp3tag.de/uploads/default/original/2X/a/acf3edeb055e7b77114f9e393d1edeeda37e50c9.png"
    except:
        album_cover = "https://community.mp3tag.de/uploads/default/original/2X/a/acf3edeb055e7b77114f9e393d1edeeda37e50c9.png"
    return album_cover
```

This retrieves the album cover image for a specified artist and album name via the LastFM API. It validates the cover image URL from the API answer with an HTTP request.

The album cover is returned if the URL is correct. Else, a fallback placeholder image for the album cover is provided by default.

The `network` object that you created earlier has several handy methods. The first line gets the album object and then gets the cover image for that object directly via LastFM.

## How to Add the Tiered List Data to JSON

Once the user picks the "create tier list" option from the menu the script presents them with the available tiers and requests them to input a valid artist and a name for their tier list so that it can be stored in the JSON file.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-16.png align="left")

*After choosing the "create tier list" option, the script validates the artist returns the metadata using the LastFM API.*

Use the `network` object to validate if the artist exists. If yes, request all the albums for that artist. Populate a list with these albums and set the `option` to that list so it shows up in the choices for the S tier.

In the image below, the (x) mark indicates the user has selected that particular album to be in the S-Tier.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-33.png align="left")

*This is a prompt for users to select albums that they want to move to the S-Tier. Navigate with arrow keys to select zero, one or more albums from the list.*

After the user has selected these albums, you would like to serialize this list and put it into a JSON file that will be used to generate the actual image later. This JSON file needs to have a data definition.

Think about how databases have a schema. They have tables and columns and rows that describe the nature and the format of the data.

Similarly, we are going to define the schema of the JSON file to store all these tier list choices. Each tier list object contains the following properties:

* `tier_list_name`: The name given to the tier list.
    
* `artist`: The name of the artist for whom the tier list is created.
    
* `s_tier`, `a_tier`, `b_tier`, `c_tier`, `d_tier`, `e_tier`: Arrays that hold the albums and their corresponding cover art for each tier. Albums are represented as objects with "album" and "cover\_art" properties.
    
* `time`: Creation timestamp.
    
* Each tier array contains one or more album objects with "album" representing the album name and "cover\_art"
    

This is the sample JSON schema. Once the user makes the choices in the terminal, a serialized Python object similar to this containing the tier list data will be written to the JSON file.

```json
{
  "tier_lists": [
        {
            "tier_list_name": "THE WEEKND RANKED",
            "artist": "the weeknd",
            "s_tier": [
                {
                    "album": "After Hours",
                    "cover_art": "https://lastfm.freetls.fastly.net/i/u/300x300/7d957bd27dd562bee7aaa89eafa0bbe6.jpg"
                }
            ],
            "a_tier": [
                {
                    "album": "Kiss Land",
                    "cover_art": "https://lastfm.freetls.fastly.net/i/u/300x300/01ad150445023de653c50dbbc3e10dbc.jpg"
                },
                {
                    "album": "Echoes of Silence",
                    "cover_art": "https://lastfm.freetls.fastly.net/i/u/300x300/4f257619898b44b7a8f95431045e9ffe.png"
                }
            ],
            "b_tier": [],
            "c_tier": [],
            "d_tier": [],
            "e_tier": [
                {
                    "album": "I Feel It Coming",
                    "cover_art": "https://lastfm.freetls.fastly.net/i/u/300x300/974deeb8c348d0ad0c0fa10941dd67e8.jpg"
                }
            ],
            "time": "2023-04-23 23:56:14.652417"
        }
    ]
}
```

You want to dynamically write to this JSON file as the user continues to keep making tier lists. That is, it should continue to grow and expand to fit all the album covers. The below code does exactly that:

```py
def create_tier_list():
    load_or_create_json()
    with open("albums.json") as f:
        album_file = json.load(f)

    print("TIERS - S, A, B, C, D, E")

    question = "Which artist do you want to make a tier list for?"
    artist = input(question).strip().lower()
    
    try:
        get_artist = network.get_artist(artist)
        artist = get_artist.get_name()
        albums_to_rank = get_album_list(artist)
        
        # keep only the album name by splitting the string at the first - and removing the first element
        albums_to_rank = [x.split(" - ", 1)[1] for x in albums_to_rank[1:]]

        question = "What do you want to call this tier list?"
        tier_list_name = input(question).strip()

        # repeat until the user enters at least one character
        while not tier_list_name:
            print("Please enter at least one character")
            tier_list_name = input(question).strip()

        # S TIER
        question = "Select the albums you want to rank in S Tier:"
        s_tier_picks = create_tier_list_helper(albums_to_rank, "S Tier")
        s_tier_covers = [get_album_cover(artist, album) for album in s_tier_picks]
        s_tier = [{"album":album,"cover_art": cover} for album, cover in zip(s_tier_picks, s_tier_covers)]
        
        # A TIER
        question = "Select the albums you want to rank in A Tier:"
        a_tier_picks = create_tier_list_helper(albums_to_rank, "A Tier")
        a_tier_covers = [get_album_cover(artist, album) for album in a_tier_picks]
        a_tier = [{"album":album,"cover_art": cover} for album, cover in zip(a_tier_picks, a_tier_covers)]
            
        # B TIER
        question = "Select the albums you want to rank in B Tier:"
        b_tier_picks = create_tier_list_helper(albums_to_rank, "B Tier")
        b_tier_covers = [get_album_cover(artist, album) for album in b_tier_picks]
        b_tier = [{"album":album,"cover_art": cover} for album, cover in zip(b_tier_picks, b_tier_covers)]
        
        # C TIER
        question = "Select the albums you want to rank in C Tier:"
        c_tier_picks = create_tier_list_helper(albums_to_rank, "C Tier")
        c_tier_covers = [get_album_cover(artist, album) for album in c_tier_picks]
        c_tier = [{"album":album,"cover_art": cover} for album, cover in zip(c_tier_picks, c_tier_covers)]
            
        # D TIER
        question = "Select the albums you want to rank in D Tier:"
        d_tier_picks = create_tier_list_helper(albums_to_rank, "D Tier")
        d_tier_covers = [get_album_cover(artist, album) for album in d_tier_picks] 
        d_tier = [{"album":album,"cover_art": cover} for album, cover in zip(d_tier_picks, d_tier_covers)]
        # E TIER
        question = "Select the albums you want to rank in E Tier:"
        e_tier_picks = create_tier_list_helper(albums_to_rank, "E Tier")
        e_tier_covers = [get_album_cover(artist, album) for album in e_tier_picks]
        e_tier = [{"album":album,"cover_art": cover} for album, cover in zip(e_tier_picks, e_tier_covers)]
        
        # check if all tiers are empty and if so, exit
        if not any([s_tier_picks, a_tier_picks, b_tier_picks, c_tier_picks, d_tier_picks, e_tier_picks]):
            print("All tiers are empty. Exiting...")
            return
        
        
        # # add the albums that were picked to the tier list
        tier_list = {
            "tier_list_name": tier_list_name,
            "artist": artist,
            "s_tier": s_tier, 
            "a_tier": a_tier,
            "b_tier": b_tier,
            "c_tier": c_tier,
            "d_tier": d_tier,
            "e_tier": e_tier,
            "time": str(datetime.now())
        }
        
        # add the tier list to the json file
        album_file["tier_lists"].append(tier_list)
        
        # save the json file
        with open("albums.json", "w") as f:
            json.dump(album_file, f, indent=4)
            
        return
    
    except pylast.PyLastError:
        print("❌[b red] Artist not found [/b red]")
```

This is the core function used to create tier lists for albums and store them in `albums.json`. Here's what's going on in it:

* The user enters the artist's name and retrieves information from the LastFM API.
    
* Next, provide a name for the tier list they want to create.
    
* For each tier (S, A, B, C, D, E), select albums to rank within that tier using a helper function you wrote earlier.
    
* Retrieval of album cover art for each selected album is done via the `get_album_cover()`, and the selected albums and their corresponding cover art are stored as dictionaries in the respective tier list.
    
* If all tiers are empty, the function exits. Nothing is written into the JSON file.
    
* Otherwise, the tier list is added to the JSON file which is saved in the current working directory (same path as the Python script).
    

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-15.png align="left")

*Now, this is selection for the next tier (A-Tier). The albums we selected in the previous options do not appear anymore meaning they have already been selected.*

## How to Use Pillow for Visual Transformations

Now that you have all the JSON data for your tier lists, you want to export all that to an image so that you can share it with your friends or post it on the web. But how should you do this? Let's break it down:

First, you'll want to determine the number of tiers. Then, determine the position and sizing of both the tier list grid and the album cover squares.

Here, you'll want to think about dynamic width and height offsets. How should you prevent overflow of images, add new rows, or maintain minimum height?

All this is related to the image canvas. Pillow is an excellent choice for this. You can resize, adjust, and expand the dimensions of all your images as well as the background canvas on the fly based on the user input and selection.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-34.png align="left")

*Tier list template made with Pillow. Refer the code below for explanation.*

The most logical way to tackle this is to pass the tier list object to a function and let it loop over all the tiers. Inside each tier, let it loop over all the records and add an item. If the album cover exceeds the max width, add a new row so it does not overflow. Continue this until all the albums in each tier are processed. Violà!

```py
def image_generator(file_name, data):

    # return if the file already exists
    if os.path.exists(file_name):
        return
    
    # Set the image size and font
    image_width = 1920
    image_height = 5000
    font = ImageFont.truetype("arial.ttf", 15)
    tier_font = ImageFont.truetype("arial.ttf", 30)
    
    # Make a new image with the size and background color black
    image = Image.new("RGB", (image_width, image_height), "black")
    text_cutoff_value = 20

    #Initialize variables for row and column positions
    row_pos = 0
    col_pos = 0
    increment_size = 200
    
    """S Tier"""
    # leftmost side - make a square with text inside the square and fill color
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="red")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "S Tier", font=tier_font, fill="white")
        col_pos += increment_size
        
    for album in data["s_tier"]:
        # Get the cover art
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
    
    	# Resize the cover art
        cover_art = cover_art.resize((increment_size, increment_size))
        
        # Paste the cover art onto the base image
        image.paste(cover_art, (col_pos, row_pos))
        
        # Draw the album name on the image with the font size 10 and background color white
        draw = ImageDraw.Draw(image)

        # Get the album name
        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")

        # Increment the column position
        col_pos += 200
        # check if the column position is greater than the image width
        if col_pos > image_width - increment_size:
            # add a new row
            row_pos += increment_size + 50
            col_pos = 0 

    # add a new row to separate the tiers
    row_pos += increment_size + 50
    col_pos = 0

    """A TIER"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="orange")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "A Tier", font=tier_font, fill="white")
        col_pos += increment_size
        
    for album in data["a_tier"]:
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
        cover_art = cover_art.resize((increment_size, increment_size))
        image.paste(cover_art, (col_pos, row_pos))
        draw = ImageDraw.Draw(image)

        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")

        col_pos += 200
        if col_pos > image_width - increment_size:
            row_pos += increment_size + 50
            col_pos = 0 

    row_pos += increment_size + 50
    col_pos = 0
    
    """B TIER"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="yellow")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "B Tier", font=tier_font, fill="black")
        col_pos += increment_size
        
    for album in data["b_tier"]:
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
        cover_art = cover_art.resize((increment_size, increment_size))
        image.paste(cover_art, (col_pos, row_pos))
        draw = ImageDraw.Draw(image)

        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")
        col_pos += 200
        if col_pos > image_width - increment_size:
            # add a new row
            row_pos += increment_size + 50
            col_pos = 0
    
    row_pos += increment_size + 50
    col_pos = 0
    
    """C TIER"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="green")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "C Tier", font=tier_font, fill="black")
        col_pos += increment_size
        
    for album in data["c_tier"]:
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))       
        cover_art = cover_art.resize((increment_size, increment_size))
        image.paste(cover_art, (col_pos, row_pos))
        draw = ImageDraw.Draw(image)

        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")

        col_pos += 200
        if col_pos > image_width - increment_size:
            row_pos += increment_size + 50
            col_pos = 0
    
    row_pos += increment_size + 50
    col_pos = 0
   

    """D TIER"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="blue")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "D Tier", font=tier_font, fill="black")
        col_pos += increment_size
        
    for album in data["d_tier"]:
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
        cover_art = cover_art.resize((increment_size, increment_size))
        image.paste(cover_art, (col_pos, row_pos))        
        draw = ImageDraw.Draw(image)
        
        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")

        col_pos += 200
        if col_pos > image_width - increment_size:
            # add a new row
            row_pos += increment_size + 50
            col_pos = 0
    
    row_pos += increment_size + 50
    col_pos = 0


    """E TIER"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="pink")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "E Tier", font=tier_font, fill="black")
        col_pos += increment_size
        
    for album in data["e_tier"]:
        
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
        cover_art = cover_art.resize((increment_size, increment_size))    
        image.paste(cover_art, (col_pos, row_pos))
        draw = ImageDraw.Draw(image)
        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")
        col_pos += 200
        if col_pos > image_width - increment_size:
            row_pos += increment_size + 50
            col_pos = 0
    
    row_pos += increment_size + 50
    col_pos = 0

	image = image.crop((0, 0, image_width, row_pos))

    image.save(f"{file_name}")
```

First of all, with two parameters (`file name` and `data`), this custom function is responsible for converting all the JSON data we stored into a nicely organized tier list image.

It determines whether or not the file with the specified `file name` exists and returns true if it does. This saves computing if you have already made the tier list with that name.

You can see that it specifies the image size and font for constructing the tier list visual, generates a new image with a black backdrop, defines variables for row and column places, and sets an increment size.

The function generates the S Tier portion of the tier list, generating a square with text within that is filled with red color.

After retrieving cover graphics for each album in the S tier, the album title is drawn on the image using a given typeface once the cover art is scaled and placed onto it. If the column position is more than the image width, a new row is added.

This process is repeated for the A, B, C, D, and E Tiers, with each tier having its color. If the picture file does not already exist, the resulting image is saved.

In a nutshell, this places all the album covers in rows and columns inside each tier, and the new rows are introduced as needed to accommodate the width of the image. Dynamic width and height offsets are set for the natural growth of width and height.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/GRIMES-TIER-LIST---FAVORITE-ALBUMS.png align="left")

*This entire image is generated with the Pillow library by processing the data from the JSON file. First, the tiers are set to the left edge of the canvas and sequentially, the selected albums are placed on the canvas. Any overflow is taken care of by adding a row beneath the tier list.*

## How to Export the Created Image

You are almost there. This final function passes the tier list object data to the previously defined function to render an image using pillow.

Think of it as a connecting link between two functions It simply prints the success or failure message in the CLI to let users know the image generation status.

```py
def see_tier_lists():
    load_or_create_json()
    with open("albums.json", "r") as f:
        data = json.load(f)

    if not data["tier_lists"]:
        print("❌ [b red]No tier lists have been created yet![/b red]")
        return
    
    for key in data["tier_lists"]:
        image_generator(f"{key['tier_list_name']}.png", key)
        print(f"✅ [b green]CREATED[/b green] {key['tier_list_name']} tier list.")
        
    print("✅ [b green]DONE[/b green]. Check the directory for the tier lists.")    
    return
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-17.png align="left")

*Let the user know that the image is rendered in the current directory.*

## Key Takeaways

This tutorial demonstrated ways to transform JSON data into interactive tier list graphics using Python and the Pillow library. By combining image manipulation and API data retrieval, appealing representations of album rankings are generated.

To recap, you learned:

* How to retrieve album data using the LastFM API.
    
* How to generate tier lists based on user input and album ratings.
    
* How to use the Pillow library to create and manipulate images.
    
* How to resize and paste album cover art onto the base image.
    
* How to add text and tier labels to the image.
    
* How to dynamically write to JSON files.
    

Want to grab the code from this tutorial? Get it from my [Github Repo](https://github.com/HighnessAtharva/musicli). It includes other CRUD functions like reviewing, rating, and viewing all your albums and artists right within the terminal.

This is also published as a Python package for ease of use. Refer to this [release page](https://pypi.org/project/musicli/) on PyPi.

This project uses Python and image manipulation libraries to create visually engaging tier lists for gaming communities, music rankings, and content evaluations. Users can rate albums interactively right within their terminal and integrate other APIs or data sources to enhance the creative process. This practical application explores new possibilities in data visualization.

---
title: How to Supercharge Your Studying with Python, Anki, and ChatGPT
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-25T20:35:46.000Z'
originalURL: https://freecodecamp.org/news/supercharged-studying-with-python-anki-chatgpt
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-pixabay-256302.jpg
tags:
- name: chatgpt
  slug: chatgpt
- name: learning to code
  slug: learning-to-code
- name: Python
  slug: python
seo_title: null
seo_desc: "By Otavio Ehrenberger\nYou may have heard how students can use ChatGPT\
  \ to cheat on assignments. But we should also talk about what a fantastic study\
  \ tool it can be. \nIn this article we'll discuss how you can use ChatGPT to help\
  \ you study and learn new..."
---

By Otavio Ehrenberger

You may have heard how students can use [ChatGPT](https://chat.openai.com) to cheat on assignments. But we should also talk about what a fantastic study tool it can be. 

In this article we'll discuss how you can use ChatGPT to help you study and learn new skills.

You'll see how to instruct ChatGPT to give you a nicely formatted list of information that you should memorize. You'll then see how to input it into a Python program that will output an Anki package. Finally, you'll load the package into Anki to help you remember the concepts through memory triggers.

I'll show you how to create Anki cards programmatically using Python and the [Genanki](https://github.com/kerrickstaley/genanki) library. We will create an Anki deck for learning the Linux filesystem directories and their descriptions. The deck will contain basic and reverse type cards for each directory.

# What is Anki?

[Anki](https://apps.ankiweb.net/) is a powerful open-source flashcard application that helps users memorize information more efficiently using spaced repetition. It is available on multiple platforms, including Windows, macOS, Linux, iOS, and Android. 

Anki allows users to create their own decks of flashcards containing text, images, audio, and even LaTeX equations.

Learning how to properly use Anki is a skill in itself. [Here is a good video to get you started](https://www.youtube.com/watch?v=7K2StK7e3ww&t=6s). In this program we will use the concepts of Anki models, cards, notes, decks and packages to create our card set. But first, let's learn a bit more about how Anki works.

### Anki Models

An Anki model, also known as a note type, defines the structure and layout of a set of cards. Each model consists of a set of fields, which store the information to be learned, and a set of card templates, which determine how that information is displayed on the cards. 

Models allow users to create different types of cards and layouts for various learning needs, such as basic cards, reverse cards, and cloze deletion cards.

### Anki Cards

An Anki card is a digital flashcard containing information to be learned. Each card has a front side, which usually contains a question or a prompt, and a back side, which contains the answer or additional information related to the front side. 

Anki cards can contain text, images, audio, and even LaTeX equations. Cards are generated from models and their associated fields, which determine the content and layout of the cards.

### Anki Notes

An Anki note is a single piece of information that is used to generate one or more flashcards or Anki cards. 

Each note is based on a specific model (also known as a note type), which defines the structure, layout, and fields for that note. Fields store the actual content of the note, such as questions, answers, or prompts, while the model determines how that content is displayed on the generated cards.

### Anki Decks

An Anki deck is a collection of cards on a specific topic or subject. Decks are used to organize cards into meaningful groups, making it easier for users to focus on a particular area of study. 

Anki allows users to create and customize their own decks, which can be shared with others, imported, or exported. Users can study one deck at a time or multiple decks simultaneously, depending on their learning goals and preferences.

### Anki Packages

An Anki package is a single file containing one or more decks, along with their associated cards, models, media files, and other related data. Anki packages have the file extension ".apkg" and can be easily shared, imported, or exported between users and devices. 

Anki packages are a convenient way to distribute decks and related content, as they bundle all necessary information in a single file. When importing an Anki package, the decks, cards, and models it contains are added to the user's existing collection.

# How to Use ChatGPT as a Study Aid

You can think of ChatGPT like a humanoid Google. It won't do the work for you and it certainly won't do the thinking for you. But if you know how to phrase your questions, it can give you some pretty good answers, and in the format you would like them to be. This makes inserting these answers in a program that much easier.

In this example, I'm going to ask a question regarding the Linux filesystem. I expect the answer to be a list of the directories accessible from the root folder, with an explanation of why they are there. If it doesn't give you the answer you want, remember to be more specific.

![Chat GPT answer on the Linux filesystem](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rufulo3vzyby3ueost53.png)

This is a partial screenshot – the answer goes all the way to 14, the `/var` directory used to store fluid data files that are supposed to change during a system use session, and the last one in alphabetical order.

So far, so good. But if we want to insert this information into a program, we need to have it formatted. This is an area where Chat GPT shines. 

If you receive, say, a paragraph as an answer, you can just ask the robot to rephrase it as an ordered list. Then you can ask it to send each item as an array of tuples, for instance. Here's an example based on the last answer:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5tosze6su9fq8ieswu56.png)

Remember to always review the answers before uploading them to Anki, as you'll hammer the returned information into your brain. You don't want to sabotage your learning during your studies.

This is enough for now, let's get to coding.

# How to Install Genanki

To get started, you'll need to install the `genanki` library, which is a Python library for creating Anki decks and cards programmatically. You can install it using `pip`:

```bash
pip install genanki

```

# How to Create Anki Cards and Decks

Now that we have the `genanki` library installed, let's create a Python script that generates the Anki cards and deck for Linux filesystem directories.

## Preparations

Here we'll import the library and paste in the ChatGPT answer. It will be used as a parameter to the functions provided by `genanki`.

```python
import genanki

# List of Linux directories and their descriptions
linux_dirs = [
    ('/', 'Root directory, starting point of the filesystem hierarchy.'),
    ('/bin', 'Contains essential system command executables.'),
    ('/sbin', 'Contains essential system administration command executables.'),
    ('/boot', 'Contains files needed to start the boot process.'),
    ('/etc', "Contains system-wide configuration files and scripts."),
    ('/dev', 'Contains device files representing hardware devices.'),
    ('/home', 'Contains personal directories for each user.'),
    ('/lib', 'Contains shared libraries and kernel modules.'),
    ('/opt', 'Optional directory for storing third-party software.'),
    ('/proc', 'Virtual filesystem providing an interface to kernel internal data structures.'),
    ('/sys', 'Virtual filesystem providing an interface to kernel internal data structures for devices, drivers, and other components.'),
    ('/tmp', 'Temporary directory for storing files deleted after a system reboot.'),
    ('/usr', 'Contains user-related files, shared libraries, header files, documentation, and non-essential software binaries.'),
    ('/var', 'Contains variable data files, such as logs, databases, and mail spools.'),
]

```

Here we have to generate a model ID for the cards we are creating, which has to be unique. You will also have to give a name to your model, create fields to be populated by content, and then declare a template for your note using these fields. 

Remember that a note is basically a form for cards associated with that note. We will have two cards for each note, since the directory name is a memory trigger for the directory description and vice-versa.

```python
# Define Anki note model
model_id = 1607392319
model = genanki.Model(
    model_id,
    'Linux filesystem folders',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ])

```

We'll finally create the deck and give it an ID (which, you guessed it, must be unique) and also give it a name. We will then iterate through our list of tuples and create a note for each tuple, declaring the note's model and inputting our content as fields ('Directory' and 'Description' respectively).

We'll finally write a package containing our single deck. If you have an Anki installation, just double click on the generated file and it should open in the program, ready for studying.

```python
# Generate Anki cards and add them to a deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, 'Linux Filesystem')

for dir_name, description in linux_dirs:
    note = genanki.Note(model=model, fields=[dir_name, description])
    deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file
genanki.Package(deck).write_to_file('linux_filesystem.apkg')

```

# Full Script

```python
import genanki

# List of Linux directories and their descriptions
linux_dirs = [
    ('/', 'Root directory, starting point of the filesystem hierarchy.'),
    ('/bin', 'Contains essential system command executables.'),
    ('/sbin', 'Contains essential system administration command executables.'),
    ('/boot', 'Contains files needed to start the boot process.'),
    ('/etc', "Contains system-wide configuration files and scripts."),
    ('/dev', 'Contains device files representing hardware devices.'),
    ('/home', 'Contains personal directories for each user.'),
    ('/lib', 'Contains shared libraries and kernel modules.'),
    ('/opt', 'Optional directory for storing third-party software.'),
    ('/proc', 'Virtual filesystem providing an interface to kernel internal data structures.'),
    ('/sys', 'Virtual filesystem providing an interface to kernel internal data structures for devices, drivers, and other components.'),
    ('/tmp', 'Temporary directory for storing files deleted after a system reboot.'),
    ('/usr', 'Contains user-related files, shared libraries, header files, documentation, and non-essential software binaries.'),
    ('/var', 'Contains variable data files, such as logs, databases, and mail spools.'),
]

# Define Anki note model
model_id = 1607392319
model = genanki.Model(
    model_id,
    'Simple Model',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ])

# Generate Anki cards and add them to a deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, 'Linux Filesystem')

for dir_name, description in linux_dirs:
    note = genanki.Note(model=model, fields=[dir_name, description])
    deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file
genanki.Package(deck).write_to_file('linux_filesystem.apkg')

```

# Limitations of this Method

This script is pretty good, and I use it very often – but let's not pretend it is perfect. You will have to generate the deck every time you want to add stuff programatically. 

You can also get the Deck ID and generate more cards to a new package with the same ID and add them, but this can lead to errors if you are not careful.

Also, the input method is currently an array of tuples. You will have to edit the script every time to update the array with a new deck.

You could also copy and paste it to a text file and read the input from there. And you could also randomly generate a model ID so you can just paste the card contents to your text file and have the package generate from a single script run. This is somewhat subjective so I left it out on purpose.

# Conclusion

Anki has many types of cards, the main ones being the basic (memory trigger + answer) and cloze (one or more memory triggers embedded in an outline). This example uses the basic and reversed card, because both the 'question' and 'answer' can be a memory trigger for each other. If you want a simple, basic card you should consult the example at [Genanki](https://github.com/kerrickstaley/genanki)'s README.

I hope this script serves as at least a starting point for your own applications of programmable Anki. It is probably my main study method nowadays, and it got a whole lot more powerful after ChatGPT. Have fun with your coding.


---
title: Assisted script writing, with Pychronia Tools
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T21:44:28.000Z'
originalURL: https://freecodecamp.org/news/assisted-script-writing-with-pychronia-tools
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/pychroniatools.png
tags:
- name: larp
  slug: larp
- name: Python
  slug: python
- name: roleplay
  slug: roleplay
- name: Script
  slug: script
- name: tools
  slug: tools
- name: writing
  slug: writing
seo_title: null
seo_desc: 'By Pakal de Bonchamp

  Let software tooling check the consistency of your roleplay scripts for you!

  (French version of this article available here on Electro-GN)

  Issue

  Every  writer will confirm it to you: it is not easy to remain coherent when  you
  ar...'
---

By Pakal de Bonchamp

**Let software tooling check the consistency of your roleplay scripts for you!**

_(French version of this article available_ [_here on Electro-GN_](https://www.electro-gn.com/12495-lecriture-de-scenarios-assistee-avec-pychronia-tools)_)_

### Issue

Every  writer will confirm it to you: it is not easy to remain coherent when  you are working, for several months, on a long story. It is even less so  when the story in question is lived by dozens of characters, each with  their own partial vision of the truth. And live action roleplay games  (LARPs) are especially exposed to this problem.

The  danger does not lie in the first draft of the writing: if he has all  his ideas well in place, the author does not risk much, except for a few  typos and interchanges of names. It is during subsequent modifications  (changes in the chronology of facts, additions of twists and turns,  etc.) that the information — disseminated and duplicated in the  documents of the various participants — will gradually become obsolete  and inconsistent. Eventually, even the character sheets of a common  “murder&mystery party” will end up full of spatial, temporal,  lexical and structural improbabilities if they are not rigorously  checked and compared after each evolution of the scenario.

What can we do to prevent this, without spending a lifetime doing comparative proofreading? First, undoubtedly, _deduplicate texts common to several players_, which lead to tedious copy and paste (multiplying errors and artificially inflating the mass of the text). Then, _allow the author to review the interdependent sets of changes_ he has successively applied to his scenario. Finally, give him _summaries of key information_, easier to review than verbose literary texts. And all this in _as automated a way as possible_,  because the number of documents to be managed can make the smallest  operation very time-consuming (and at risk of carelessness).

### The benefits of Pychronia Tools machinery

To benefit from these precious writing facilities during the creation of the [Chrysalis:Mindstorm](https://chrysalis-game.com/fr/cms/soiree-mystere-chrysalis-mindstorm/) mystery party (French only), I set up a specific writing process,  involving simple text files (which contain the scenario), various  existing software tools, as well as a module “Pychronia Tools” developed  for the occasion.

Once  this machinery is in place, all you have to do is start it up  and — magic — a hundred PDF files appear one after the other in the  output folder: game master’s manual, complete and summarized character  sheets for players, documents to print on beautiful scrolls to serve as  clues in play, summary sheets for extras….

This tool is much more than a simple document generator: it includes an **automatic check of the script consistency**.  Now, if an index is mentioned in one place but not provided in another,  or if the same symbol has different values from one file to another,  the error is reported.  
   
**Extract of consistency errors returned by the program:**

> !!! ERROR IN hints registry for key golden_box_with_blood : [‘needed’] requires a provided hint  
> !!! ERROR IN symbols registry for key murder_date : [‘3 January 2018′,’15 March 2018']

And  thanks to the automatically generated summary tables, it is possible to  check at a glance that each player is well informed of the facts  concerning him/her, that the distribution of key information is more or  less balanced, and that major events are correctly recorded in summary  sheets.

**Extract from the automatic summary of the “facts” of the scenario:**

_Character  names are in italics when they have the “fact” in question only in  their complete character sheet, not in their summary sheet._

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytuGvYFYAwYxk2h9mf-Z_A.png)

As  a result, the game master can rely quietly on his own (self-generated)  documents to set up and monitor the game: detailed scenario, evening  planning, checklist of materials and writings to be placed in the  premises, automatic summary of missions and special skills of each  player…

On  top of that, this machine can also send its game documents, by email,  to each player (e.g. character card and documents initially owned). This  avoids the drama that awaits each organizer: spoiling a participant by  sending him the wrong documents.

This  system obviously adds a certain complexity to the project, compared to  some common Word/LibreOffice files. But it provides invaluable support  in terms of scenario scalability and robustness, detecting  inconsistencies and automating daunting tasks. Personally, he saved me  more than once, when I switched the names of some characters in cards,  or forgot to warn some players of the new misdeeds they were supposed to  have committed in the past.

### How to set up such a process?

**Step 1:** Move away from rich office files (docx, odt, pdf…) to a plain text  format, easily manipulable, where the formatting is explicitly indicated  by special characters. The documents _in game_ with  high graphic and typographical needs (posters, scrolls, newspapers…)  can be left aside, in more usual office automation files: Word,  LibreOffice, InDesign…

**Example of plain text (restructuredtext format):**

```restructuredtext
Manuel du Maître de Jeu
############################

.. contents:: Table des Matières
    :depth: 2

Concept de la soirée mystère
================================

**Chrysalis:Mindstorm** est un huis clos entre `enquête 
<https://fr.wikipedia.org/wiki/Enqu%C3%AAte>`_ criminelle et conflit
géopolitique, où des agents secrets et des civils de divers pays se 
retrouvent face à un *redoutable* inspecteur de police, qui va les 
pousser dans leurs derniers retranchements.
```

**Rendering of this text once converted to PDF:**

![Image](https://cdn-media-1.freecodecamp.org/images/1*gzF6lDg3aFQ4cYiHogwlUw.png)

**Step 2:** Use a version manager for scenario files. This makes it possible to go  back in time at any time, to avoid horrifying accidental file  modifications, and to check the consistency of each of the changes made  (renaming a place, adding information for a group of players…).

**Viewing a change made to the rules of the game:**

![Image](https://cdn-media-1.freecodecamp.org/images/1*coZjpx5FCi1RERBRrOYIOQ.jpeg)

**Step 3:** Add  a small processing engine, to enrich the text with simple and practical  features: allow one file to include another, define reusable text  blocks, insert variables (e. g. the date of a crucial event, different  for each session of the mystery evening), display different information  according to the team to which the targeted player belongs….

**Step 4:** Automate consistency checks. To do this, I created specific tags in the processing engine, which I then inserted as I wrote:  
 — The  {% fact %} tag is used to announce a fact (e. g. “so-and-so tried to  rob Loyd Georges”), and to indicate whether the player is the author or  just a witness.  
 — The {% hint %} tag allows you to request the existence of a physical clue (letter, object…) to give to the player.  
 — The  {% symbol %} tag ensures that a value is unique in all scenario files  (e. g. the exact time of a crime), while avoiding the use of “variables”  that obscure the text.

**Example of using special tags to enrich a scenario text:**

> To  the attention of {{agent_gamma_fake_name }} : the country of {% symbol  “Balberith” for “first_country_at_war” %} has entered the war, following  the plot led by agent Epsilon {% fact “agent_epsilon_triggered_war” as  author %}. You have a testimony signed by him and attesting to it. {%  hint “epsilon_signed_testimony_for_agent_gamma” is needed %}.

As  we can see, these tags each have their own syntax, and can use other  features of the processing engine, such as variables (of which we have  an example with _{{agent_gamma_fake_name }}_).

**Step 5:** Link  all this with scripts, which will automate the different steps of  creating game documents: gathering useful data (including player  photos), distributing scenario pages for each participant (global  context, personal context, game rules…), transforming them into PDF  format, and generating summary sheets for the game master.

**Some of the PDF documents generated, next to their plain text sources:**

![Image](https://cdn-media-1.freecodecamp.org/images/1*weQW6mnReW0hV9TNieakNw.png)

### The future

All this is all well and good, but what about the rest of the role-playing  community? Can it benefit, more broadly, from the functionalities  offered by this scriptwriting support system?

The  answer is yes. However, as seen in the steps above, this tooling  requires a certain affinity with processes that are usually reserved for  computer development; an affinity that many GN authors do not have.

I  am therefore listening to authors tempted by the experience, in order  to see with them how they work, what formats and tools they are able to  use, and how this system could be generalized to suit their use. I could  then see to extract this code (which is currently strongly linked to  the structure of the Chrysalis game files), to make it more autonomous  and more easily deployable.

Note that software such as [Twine](https://twinery.org/) already allows scenarios to be created in a fairly simple way, with a  mini-language to define variables and use logical operations. Pychronia  Tools machinery therefore only makes sense for the very high level of  integration it offers, with its automated consistency checks and  end-to-end generation scripts.

Interested in this scriptwriting support system? Feel free to contact me using the information on the [Chrysalis Website](https://chrysalis-game.com/fr/cms/contacts/).

### Appendix : Details for computer literate people

My machinery is based on the Python language and its document manipulation/creation ecosystem.

As  for the “plain text” format of the scenario, many “markup languages”  can be used for this purpose: restructuredtext, markdown, textile,  latex, or even html… I chose [restructuredtext](http://docutils.sourceforge.net/docs/user/rst/quickstart.html) for  its clarity, versatility, and its advanced integration with the Python  language. To edit these text files, of course, Pycharm, Notepad++,  Geany, or a simple notebook can do the trick.

For  the version manager (or “VCS”), I chose Git and its excellent  TortoiseGit graphical interface (available under Windows only  unfortunately). Mercurial, Bazaar, DARCS, or others are just as  relevant. At a minimum, we can use the versioned file backup proposed by  Dropbox et al., even if it offers only a few features to visualize the  differences between several writing steps…

**Visualization, via GIT, of the sets of modifications made to the scenario:**

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzYryvzHO22pB5UoanSL7Q.png)

Regarding the template engine used to process text files (and for specific tags), finally, I have integrated the powerful [Jinja2](http://jinja.pocoo.org/),  which allows you to create variables and macros directly in the  templates. The data handled by this engine comes, in my case, from a  tree structure of Yaml files, but many other sources (python file, csv,  xml…) are very easily integrated.


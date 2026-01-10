---
title: How to combine multiple CSV files with 8 lines of code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T20:19:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NQgINaLXYMzvowRHHa6Plw.jpeg
tags:
- name: automation
  slug: automation
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ekapope Viriyakovithya

  Why do you need this?

  Manually copy-pasting is fine if you don’t have too many files to work with.

  But imagine if you have 100+ files to concatenate — are you willing to do it manually?
  Doing this repetitively is tedious and...'
---

By Ekapope Viriyakovithya

### Why do you need this?

Manually copy-pasting is fine if you don’t have too many files to work with.

But imagine if you have 100+ files to concatenate — are you willing to do it manually? Doing this repetitively is tedious and error-prone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uRBGXWKaeRjw6Ck2NrhcIA.png)

If all the files have the same table structure (same headers & number of columns), let this tiny [Python script](https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py) do the work.

#### Step 1: Import packages and set the working directory

Change “/mydir” to your desired working directory.

```python
import os
import glob
import pandas as pd
os.chdir("/mydir")
```

#### Step 2: Use glob to match the pattern ‘csv’

Match the pattern (‘csv’) and save the list of file names in the ‘all_filenames’ variable. You can check out [this link](https://regexr.com/) to learn more about regular expression matching.

```py
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
```

#### Step 3: Combine all files in the list and export as CSV

Use pandas to concatenate all files in the list and export as CSV. The output file is named “combined_csv.csv” located in your working directory.

```py
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
```

encoding = ‘utf-8-sig’ is added to overcome the issue when exporting ‘Non-English’ languages.

And…it’s done!

This article was inspired by my actual everyday problem, and the coding structure is from a discussion on [stackoverflow](https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052). The completed script for this how-to is [documented on GitHub](https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py).

Thank you for reading. Please give it a try, have fun and let me know your feedback!

If you like what I did, consider following me on [GitHub](https://ekapope.github.io/), [Medium](https://medium.com/@ekapope.v), and [Twitter](https://twitter.com/EkapopeV). Make sure [to star it on GitHub](https://github.com/Ekapope) :P


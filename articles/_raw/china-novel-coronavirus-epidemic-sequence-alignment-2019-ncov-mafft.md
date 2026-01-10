---
title: 'The Novel Coronavirus Epidemic in China: How to Help Researchers Using Sequence
  Alignment on 2019-nCoV with MAFFT'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T11:04:41.000Z'
originalURL: https://freecodecamp.org/news/china-novel-coronavirus-epidemic-sequence-alignment-2019-ncov-mafft
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/image-64-1.png
tags:
- name: mafft
  slug: mafft
- name: Genetics
  slug: genetics
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shen Huang

  Novel Coronavirus (2019-nCoV) is a deadly virus that seems to have originated in
  Wuhan, China. As of January 26, the virus has already caused 76 deaths.

  As a coronavirus targeting human respiratory systems, 2019-nCoV is highly infectiou...'
---

By Shen Huang

Novel Coronavirus (2019-nCoV) is a deadly virus that seems to have originated in Wuhan, China. As of January 26, the virus has already caused 76 deaths.

As a coronavirus targeting human respiratory systems, 2019-nCoV is highly infectious – especially during wet and cold seasons.

When people sneeze, they can shoot out respiratory system-related pathogens at a high speed. These can infect humans in many ways – most often through contacting mouth, nose, and eyes.

To avoid infections, you should avoid outdoor activities – especially in crowded areas. It's also important to sanitize your hands often and not to rub your eyes with your hands.

I'm in China, and my plans for Lunar New Year are now ruined. So I decided to stay home and create this tutorial on how to obtain genetic sequence data of 2019-nCoV and perform a Sequence Alignment on it with MAFFT.

I hope this article raises your interest in bioinformatics research, so you can help scientists fight these viral outbreaks.

## What is Sequence Alignment? And what is MAFFT?

**Sequence Alignment** is a way of arranging DNA, RNA, or protein to identify regions of similarity that may reveal functional, structural or evolutionary relationships between the sequences. A recent [publication](https://onlinelibrary.wiley.com/doi/epdf/10.1002/jmv.25682) suggested cross-species transmission from snake to human with the help of sequence alignment through MAFFT.

**MAFFT** (**M**ultiple **A**lignment using **F**ast **F**ourier **T**ransform) is a multiple sequence alignment program published in 2002. You can use it to perform sequence alignment for RNA sequences. **Coronaviruses** are, for example, viruses with a single-stranded RNA enveloped in a shell derived from the cell membranes of the host.

## Where Can You Obtain RNA Sequence Data?

The latest update of 2019-nCoV can be found on [NGDC](https://bigd.big.ac.cn/ncov#about) (National Genomics Data Center of China). In this tutorial, we will analyze the [2019-nCoV](https://www.ncbi.nlm.nih.gov/nuccore/MN938384) virus and the [SARS-CoV](https://www.ncbi.nlm.nih.gov/nuccore/MK062184) virus found inside the NCBI (National Center for Biotechnology Information) data bank.

SARS-CoV, infamously know as SARS (Severe Acute Respiratory Syndrome), has resulted 774 deaths in 17 reported countries around year 2020.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-65.png)
_Example RNA Sequence Data from [NCBI](https://www.ncbi.nlm.nih.gov/)_

I have copy and pasted the data into a file with the name of the virus. It should look something like the data in the screenshot above, with an index number followed by codes in a batch size of 10, for a total of 60 codes per line, separated by spaces.

## How to Perform Sequence Alignment on 2019-nCoV with MAFFT

First, you need to install MAFFT. You can install it via Anaconda with the following commands.

Manual installation for different operating systems can be found on the [MAFFT official website](https://mafft.cbrc.jp/alignment/software/).

```bash
conda install mafft
```

MAFFT is fairly easy to use, but it process data in a special format. You'll need to preprocess your obtained data so that it can be aligned by MAFFT.

Here's the Python script that does this:

```python
import sys
import re
output = ""
for filename in sys.argv[1:]:
	infile = open(filename)
	data = infile.read()
	data = " ".join(re.split("[^atcg\n]", data))
	data = data.replace(" ", "")
	output = output + ">" + filename + "\n" + data + "\n"
print(output)
outfile = open('SEQUENCES.txt', 'w+')
outfile.write(output)
```

You can save the above Python code into a file called "preprocess.py", inside the same folder as my virus RNA data. Then we can run the following bash command in the folder to preprocess the data.

```bash
python3 preprocess.py 2019-nCoV_HKU-SZ-002a_2020 icSARS-C7-MA
```

The output file called "SEQUENCES.txt" should now look like something below. The virus name is appended at the top of the file. The white space and index numbers are also stripped off.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-66.png)

Now you can perform Sequence Alignment with MAFFT in your Terminal with the following steps:

1. Locate your working folder.
2. Call "mafft" inside your terminal.
3. For input file, put "SEQUENCES.txt".
4. For output file, put "output.txt".
5. Select "1" for "Clustal format" as your output format.
6. Select "1" for "auto" as your strategy.
7. Leave all other arguments blank.

Here's a gif of me running this in my terminal:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Jan-27-2020-18-46-10.gif)

After you hit enter, you just need to wait for MAFFT to align your RNA codes.

The finished product should look like something below:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-67.png)

Note that the "-" is used to shift the codes and "*" is used to highlight similarities between the sequences.

Congratulations, you have just learned how to perform Sequence Alignment with MAFFT! Now you can play with the gene code and take advantage of the alignment information however you like.

Help Wuhan fight off deadly disease as developer, data scientists and more: 

[https://github.com/wuhan2020/wuhan2020](https://github.com/wuhan2020/wuhan2020)

A bit more about me: I'm a developer who's into all kinds of things. I've written some other fun tutorials like these:

[How to create beautiful LANTERNS that ARRANGE THEMSELVES into words](https://www.freecodecamp.org/news/ghost/#/editor/post/5ceb787ee17b4228e0185dbf/)

[How to drop LEPRECHAUN-HATS into your website with COMPUTER VISION](https://www.freecodecamp.org/news/ghost/#/editor/post/5ceb767ee17b4228e01833b7/)

Want me to write a tutorial about something? Let me know. Happy coding.



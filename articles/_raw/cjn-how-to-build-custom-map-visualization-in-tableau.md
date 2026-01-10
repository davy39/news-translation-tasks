---
title: How to Build a Custom Map Visualization in Tableau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-11T18:52:50.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-build-custom-map-visualization-in-tableau
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/NBA_injuries_Tableau.png
tags:
- name: data
  slug: data
- name: data visualization
  slug: data-visualization
- name: excel
  slug: excel
- name: tableu
  slug: tableu
seo_title: null
seo_desc: 'By Clark Jason Ngo

  Sometime last year, I got fascinated with bubble charts when I saw a data visualization
  video, Han''s Rosling''s 200 Countries, 200 Years, 4 Minutes - The Joy of Stats
  from BBC.


  Data Visualization used as an effective communication ...'
---

By Clark Jason Ngo

Sometime last year, I got fascinated with bubble charts when I saw a data visualization video, [Han's Rosling's 200 Countries, 200 Years, 4 Minutes - The Joy of Stats from BBC](https://www.youtube.com/watch?v=jbkSRLYSojo ).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-34.png)
_Data Visualization used as an effective communication tool! Awesome!_

### What are bubble charts?

> "A bubble chart is a type of chart that displays three dimensions of data. Each entity with its triplet of associated data is plotted as a disk that expresses two of the values through the disk's xy location and the third through its size." [Wikipedia](https://en.wikipedia.org/wiki/Bubble_chart)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-12.png)
_An example of Bubble Chart_

Last January 2019, I was checking Tableau Desktop, a data visualization software, and their basic tutorials included a heat map of the United States.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-13.png)

### What are heat maps?

> "A heat map is a graphical representation of data where the individual values contained in a matrix are represented as colors. "Heat map" is a newer term but shading matrices have existed for over a century."[Wikipedia](https://en.wikipedia.org/wiki/Heat_map)

While going through the Tableau tutorial, I remembered the bubble charts and started looking for an inspiration. I was googling for image silhouettes and got the result below:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-14.png)

This led to my short data visualization experiment. I looked for a dataset and found NBA Injuries from 2010-2018, on [Kaggle](https://www.kaggle.com/ghopkins/nba-injuries-2010-2018) . I modified the dataset to make it simple to use.

I ended up giving up on using Tableau and creating my own data visualization in Microsoft Powerpoint. Still, my friends were amazed and thought that I used a data visualization tool. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image.png)
_Created with Microsoft Powerpoint_

Fast track to August 2019, I returned to studying the Tableu tutorial. Just look at the result below! =)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-1.png)
_Created with Tableau_

## How did I do it? 

I used Excel, Tableu, and a little bit of creativity.

Feel free to follow along and create the same dataset and visualization.

**Steps**

1. Create an Excel file. Column B and Column C will serve as the location on the X-axis and Y-axis of an item in Tableau. Count represents how many players had a particular injury from 2010 to 2018.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-8.png)



2. Download Tableau Desktop [here](https://www.tableau.com/).

3. Open the Tableau Desktop App

4. Click **Connect To a File** >  **Microsoft Excel**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-2.png)

4. Drag a Sheet from the left pane to the right pane 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-3.png)

5. At the bottom, click the Sheet.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-4.png)

6. At the menu, click **Background Images** > **Sheet**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-5.png)

7 . Click **Add Image**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-6.png)

8. Browse for an image and set X Field: Right to 500 and Y Field: Top to 500.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-7.png)



9. In Columns and Rows, add **SUM(X)** and **SUM(Y)**, respectively.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-9.png)

10. For Marks, add **SUM(COUNT)** in Color, **SUM(Count)** in Size, and **Position** in Label.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-10.png)

Tableau will then generate this visualization for you:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-11.png)

One of the super powers of data visualization is processing the data and understanding it by just looking at the image. With this visualization, I can communicate to you clearly and easily that **ankle** and **knee** injuries are the most common sports injuries for an NBA player, and **dizziness** and **nose** injuries are the least common.

Voila! Hope you enjoyed this simple experiment =)


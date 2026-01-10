---
title: Data Visualization in Google Sheets for Beginners
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-03-16T20:55:12.000Z'
originalURL: https://freecodecamp.org/news/data-visualization-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/FCC-Data-Visualization-in-Google-Sheets---Bar-and-Pie-Charts.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: data visualization
  slug: data-visualization
- name: google sheets
  slug: google-sheets
seo_title: null
seo_desc: "Spreadsheets are the OG resource for visualizing data with charts and graphs...unless\
  \ you count chalkboards, I suppose. \nSpreadsheets are built to churn through tons\
  \ of data. And by using a few simple built-in tools, you can glean valuable insights\
  \ f..."
---

Spreadsheets are the OG resource for visualizing data with charts and graphs...unless you count chalkboards, I suppose. 

Spreadsheets are built to churn through tons of data. And by using a few simple built-in tools, you can glean valuable insights from large chunks of data.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/og.gif)
_gif of "OG" graphic_

When dealing with small sets of data, you can often find answers and insights at a glance. But when your spreadsheets begin to reach into the hundreds and thousands of rows, charts can help condense all those numbers down to useable pieces of information...especially if you're presenting to people who aren't good with numbers!

## Video Overview

Speaking of visuals:

* [Here's a link](https://docs.google.com/spreadsheets/d/1kJ5vDDtb8B7SDQDBK-WxgK-Tc2Dk9KlF29qxjjxz65Y/edit#gid=370701475) to the demo spreadsheet with all our data and charts.
* And here's the video walkthrough of everything covered below:

%[https://youtu.be/QYc1gUWnhS4]

## How to Get the Data

Kaggle is a wonderful resource to find interesting data sets. We're using this video game sales dataset. To import it into a Google Sheet, all that we need to do is create a new Google Sheet by typing `sheets.new` in the address bar of our browser.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-140.png)
_screenshot of web address bar_

Then, select `File, Import` from the menu.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-141.png)
_screenshot of file menu in google sheets_

You can now upload the .csv file you downloaded from Kaggle.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-142.png)
_Screenshot of importing options in google sheets_

This will give you several import options. If you're following along and using a completely blank, new spreadsheet, simply select `Replace spreadsheet` and it will pull everything in automatically. 

If the data is cleaned well, and Kaggle datasets typically are, you can leave the separator to `Detect automatically`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-143.png)
_screenshot of import file options_

This will give us a lovely 16,000+ row spreadsheet full of video game data. 😁

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-145.png)
_screenshot of spreadsheet dataset_

## How to Insert Charts

From here, we need to select `Insert - Chart` from the toolbar.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-146.png)
_screenshot of insert chart in google sheets_

We'll be confronted with a blank chart in the middle of the screen and a Chart editor in the right sidebar.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-147.png)
_screenshot of chart editor_

Now let's make sure we're referencing the correct data range. Google Sheets is pretty smart, and if you click the little graph icon to the right of the data range form, it will suggest some ranges to use. In our case, the range we need is suggested: `A1:K16600`. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/selectrange.png)

We're going to find the _sales by genre_, so next let's select `Genre` for our x-axis:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-148.png)
_screenshot of chart options_

Sometimes Google Sheets will be not-so-smart. If there are a ton of series listed and a funky graph, you can simply remove all the series and manually add what you need:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-149.png)
_screenshot of chart series_

Now click the `Aggregate` button to group all the sales data for each genre, and select `NA-Sales` as the Series to display the sales in millions of dollars on the y-axis.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-150.png)
_screenshot of chart series options_

And voilà! We've got a standard issue column bar chart. But we can do better. At the top right of our chart editor, we can `Customize` the chart further by changing the appearance, font, gridlines and titles.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-151.png)
_chart editor screenshot_

## How to Customize the Chart

From the customization tab, we have a lot of options. We can style our chart by changing the background color and font. We can make it 3D, and we can choose whether or not to maximize the chart in the chart window.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-152.png)
_Chart style screenshot_

We can then add chart titles, subtitles and axis titles and also modify the color and fonts.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-153.png)
_Chart titles screenshot_

Then, we can individually edit each `Series`. In our example we're only using one series, but if there were more, you could modify each of their styles independently.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-154.png)
_screenshot of series customization options_

If you have a legend, you can modify those options in the next dropdown window:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-155.png)

Then there are customization options for both the horizontal and vertical axes. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-156.png)
_screenshot of axes options_

And the last block of customization options is for gridlines and tick marks. These can be toggled on and off, and we can change the color and frequency of the grid and tick lines.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-157.png)

Once we're done, we now have a more stylized chart:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-158.png)
_Screenshot of column chart in Google Sheets_

If we'd like to move this chart around, we can drag it throughout the current spreadsheet. Or, we can put it on its own dedicated sheet by clicking the three dots in the top right and selecting `Move to own sheet`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-159.png)

## How to Publish the Chart

Here's an added bonus: you can actually publish the chart (or the whole worksheet) to the web. Select the `Publish Chart` option from the dropdown on the chart shown above, or select `File, Share, Publish to web`:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-16-at-10.46.55-AM.png)
_screenshot of publish to web options_

From here, you'll get to select what you wish to publish and how you want it displayed. For this example, we'll select the `Sales by Platform` chart to be shared as an interactive chart.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-16-at-10.49.29-AM.png)
_Screenshot of publishing options in google sheets_

This will generate a shareable link to the chart. It may take a few seconds to load, but once it does, you'll have a nice chart to easily share that is interactive. When you hover over the slices, it will display the percent of sales of the pie slice.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-16-at-10.52.14-AM.png)
_Screenshot of a published chart_

[Here's the link to the chart that we just made.](https://docs.google.com/spreadsheets/d/e/2PACX-1vRZ-uidgV1M_YVX6qvEi5RSGddmUvRRl3a7ehHfGx9VX3JI7dP-NVX2teVlwBbhmg7ChXsp37Ss0zDt/pubchart?oid=1851187878&format=interactive) 

## Conclusion

Thanks for reading! I hope that you learned something in this beginners tutorial on data visualization in Google Sheets. 

You can really do a whole lot using the basic built-in charts available in Google Sheets as well as Microsoft Excel. Charts remain an extremely helpful way to interpret large data sets.

Please check out my [YouTube channel here](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) & [LinkedIn page here](https://www.linkedin.com/in/eamonncottrell/).

Have a great one!


---
title: Learn Google Apps Script Basics by Building a Tic Tac Toe Game
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-05-16T16:58:37.000Z'
originalURL: https://freecodecamp.org/news/learn-google-apps-script-basics-by-building-tic-tac-toe
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Tic-Tac-Toe-Google-Sheet2.png
tags:
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: 'Google Sheets are powerful, and Apps Script makes them even more versatile
  and useful.

  Yes, you can use them for finance dashboards, personal budgets, and project management
  (and we''ll cover these as future topics). But in this article, I''ll go throu...'
---

Google Sheets are powerful, and Apps Script makes them even more versatile and useful.

Yes, you can use them for finance dashboards, personal budgets, and project management (and we'll cover these as future topics). But in this article, I'll go through the basics of Apps Script by building a simple and playable Tic Tac Toe gameboard.

Here's the [link to the spreadsheet](https://docs.google.com/spreadsheets/d/1I3mjQgfaZ9hFuUui6irpTdXg17TZXfK_jjtMvPrlGlM/edit?usp=sharing) we'll be making if you'd like to check it out while you follow along:

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQF91mJiUd4F5w/article-inline_image-shrink_1500_2232/0/1684162312276?e=1689811200&v=beta&t=ue0QHmYwX0I7oqirS6GZx66YXl5y_-zSkA6iPdDGKBM)
_Let's go gif_

### Video Walkthrough Available

If you'd like to check out a video walkthrough of the Google Sheet, here you go:

%[https://youtu.be/LYN3Cvlsflg]

## Project Setup

Create a new Google Sheet by either going to your Google Drive and selecting NEW -> Google Sheet or by simply typing in sheets.new in the URL bar of your browser.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQGtAhxBgZCiPQ/article-inline_image-shrink_1500_2232/0/1684161563448?e=1689811200&v=beta&t=5TuDNK0iSggXlKST3fzl-wv5JV04qwbYizc3ev8F51E)
_screenshot of Google Drive_

Since this is a gameboard, we are going to give it a little bit of formatting to look good, add data validation and conditional formatting to add functionality to the game, and create useable buttons for our scorecard.

Here's what we'll end up with:

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQFmLTdzhlehew/article-inline_image-shrink_1000_1488/0/1684161671894?e=1689811200&v=beta&t=2nJ0ZTnaCo2Dtq7u3zzSP7av2MHjtPtAyVp7dRQUwvY)
_screenshot of Tic Tac Toe Google Sheet_

Let's remove gridlines, add borders to the gameboard and the scorecard, and set an alternative font for the board.

To get rid of gridlines, select View -> Show -> Gridlines to uncheck this option.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQFsYtEPWEAxjA/article-inline_image-shrink_400_744/0/1684161946643?e=1689811200&v=beta&t=r6rUrzy6NSj-KQDb0o7Jx64N_u3CmTWQJxr_KaTAtII)
_screenshot of Google Sheets view options_

To get a nice square grid with large X's and O's, I set the row height and column width of rows 2 - 4 and columns B - D by highlighting them, right clicking, and selecting the resize options.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQGJGcSpYb2KyA/article-inline_image-shrink_1000_1488/0/1684162096408?e=1689811200&v=beta&t=uU37mbBSZBSMgi25ICD9r3hzAyCkepCmXAYx2ebCKsw)
_screenshot of resizing columns in Google Sheets_

I chose 150 pixels for the height and width. You'll need to do these separately – you cannot change both the row height and column width at the same time.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQHzgbT4rS6f6w/article-inline_image-shrink_1000_1488/0/1684162162590?e=1689811200&v=beta&t=J-yExtOPV3icc6-YhGUmWESA0FUMzaJQu6N4qemzCwU)
_screenshot of resizing columns in Google Sheets_

For the font size of the board, select 100, and for the Font, I am using Lexend. You can add additional Google Fonts from the toolbar dropdown:

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQF6Ss_zEGVSug/article-inline_image-shrink_1500_2232/0/1684162246754?e=1689811200&v=beta&t=R548yqr57k0ffuORMeqbZ3fmhQEWYL_QCiJv1EOGNo4)
_screenshot of Fonts options in Google Sheets_

Add a border to the board and the scorecard areas by highlighting the cells and then selecting the border options from the toolbar.

Click and drag over cells to select the whole range, and hold down the CTRL button to click and drag a second area. You can style these at the same time.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQHGcJin6dOdtw/article-inline_image-shrink_1000_1488/0/1684162477801?e=1689811200&v=beta&t=lfxyTUvqmv7KjhZ5B2X9eDeVw9bWVm5rNiCBmReF6OE)
_screenshot of border options in Google Sheets_

## Data Validation

Highlight the gameboard (B2:D4) and select Data -> Data validation from the menu.

This allows us to select Dropdown as the Criteria and add X and O as the two options to select.

Then click Advanced options and select Reject the input if the data is invalid, and plain text for the display style. This will keep the dropdown chips and handles from cluttering the gameboard.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQGj3dQDQ4QGuQ/article-inline_image-shrink_1500_2232/0/1684162681967?e=1689811200&v=beta&t=_HfNZ0C9L7tWucbWMMpzKf9gItYhkMP3G1cRlVGioxQ)
_screenshot of Data validation menu in Google Sheets_

## Conditional Formatting

We'll use conditional formatting for our gameboard also. We need to check for all the winning conditions, and if one of the players gets three in a row, we will highlight those cells.

Keeping the gameboard highlighted, select Format -> Conditional formatting.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQFJwi61h00_3g/article-inline_image-shrink_1000_1488/0/1684162938075?e=1689811200&v=beta&t=rdKBw21dV6Q82CgxNfiOG8Zg9N3fKXA135SauhAAYhA)
_screenshot of Format window in Google Sheets_

There are eight conditions we'll check for three-in-a-row: going across x3, going down x3, and diagonal x2.

But we only need to write four formulas (two for the diagonals, one for across, and one for down) since we can use dollar ($) signs to drag the formula down and across for those.

For the down three-in-a-row:

```javascript
//Apply to range B2:D2 
=AND($B2=$C2,$B2=$D2,ISTEXT($B2))
```

For the across three-in-a-row:

```javascript
//Apply to range B2:D2
=AND(B$2=B$3,B$2=B$4,ISTEXT(B$3))
```

For the diagonals we have to define them separately:

```javascript
//Apply to range B2, C3, D4 
=AND($B$2=$C$3,$B$2=$D$4,ISTEXT($B$2))

//Apply to range B4, C3, D2 
=AND($B$4=$C$3,$B$4=$D$2,ISTEXT($B$4))
```

We test for equality of each cell and whether there is anything in the cell with the `=ISTEXT()` function. By wrapping each item in an `=AND()` function, we'll only apply the formatting if all conditions are met.

I selected a green background for the conditional formatting.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQERGL76FWm8nA/article-inline_image-shrink_1500_2232/0/1684163627050?e=1689811200&v=beta&t=9C0IASvwa_KE1wm68iez-FxJ2YjmuwDRB42-ASak_5s)
_screenshot of conditional formatting window_

## Apps Script

Now for the scorecard logic. Let's open Apps Script by selecting Extensions -> Apps Script from the menu:

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQHtQjZ3mujfUQ/article-inline_image-shrink_1500_2232/0/1684178999142?e=1689811200&v=beta&t=N5Wvx0y2md14-2Ih_PGj1_lHbKpW2mcEIPRNnRsvUAI)
_screenshot of Apps Script menu_

  
We'll write four functions to handle our logic:

1. `xScore()` will increment X's score in the scorecard
2. `oScore()` will increment O's score in the scorecard
3. `clearBoard()` will clear the board but keep the scores
4. `reset()` will clear the board and set the scores back to zero

To make things more legible, let's set a few named ranges.

Highlight the gameboard again and select Data -> Named ranges. Give this range a name of **Board**. Do the same for cells G4 and H4 for **xScore** and **oScore**, respectively.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQHS7_YVdCFbog/article-inline_image-shrink_1500_2232/0/1684163925497?e=1689811200&v=beta&t=8-jk-X5iea045w1ZBkCqiExObkF6c4A572zR4dqIrI0)

Now for the scores, we'll have the exact same function for each using only the two different ranges: xScore for X and oScore for O. Here's how those will look using the xScore as an example:

**`xScore()` & `oScore()`:**

```javascript
function xScore() {
    var sheet = SpreadsheetApp.getActive(); 
    var xScore = sheet.getRangeByName('xScore').getValue();
    sheet.getRangeByName('xScore').setValue(xScore+1); clearBoard();
}
```

* Line 1: This sets a variable (we'll do this in each function) for the active spreadsheet.
* Line 2: This sets a variable for xScore as the value in the named range xScore (cell G4)
* Line 3: This sets a new value for the xScore cell as whatever it was plus 1.
* Line 4: This runs the clearBoard() function which we'll write next...

**`clearBoard()`:**

This will simply clear the gameboard but leave the score board untouched.

```javascript
function clearBoard() {
    let sheet = SpreadsheetApp.getActive();
    let board = sheet.getRangeByName('Board');
    board.clearContent(); 
}
```

* Line 1: Our sheet variable again.
* Line 2: Our board variable. This is grabbing the range B2:D4 which we named 'Board'
* Line3: This built-in `clearContent()` method simply clears everything in those cells. Pretty simple.

**`reset()`:**

Now we need a function to set the score board and gameboard back to their original states.

```javascript
function reset() {
    let sheet = SpreadsheetApp.getActive(); 
    sheet.getRangeByName('xScore').setValue(0);
    sheet.getRangeByName('oScore').setValue(0); clearBoard(); 
}
```

* Line 1: our active sheet
* Line 2: we grab our xScore range and set its value to 0.
* Line 3: we do the same for our oScore
* Line 4: we run the reset function to handle the gameboard.

And that's it! Now we can run any of these functions from within the Apps Script editor and see that they work.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQFUTfyjYKeECQ/article-inline_image-shrink_1000_1488/0/1684178952423?e=1689811200&v=beta&t=ek0cIfi0cCqZfWKM7q7ygA7n18pKwMD5wdqUVizCQjU)
_screenshot of running code within Apps Script editor_

## How to Create Buttons

It would be a lot nicer to have buttons in our actual spreadsheet to be able to run the functions.

To do this, we'll draw a button and then assign a script to it.

Select Insert -> Drawing from the menu.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQEmlXrm9lNOjw/article-inline_image-shrink_1500_2232/0/1684179236609?e=1689811200&v=beta&t=wSn2IgbM2H6_flsNE0CecTzLqKj9K2ILIgCDL9N5x9w)
_Screenshot of Insert menu in Google Sheets_

You can draw anything you'd like, but I chose the basic rounded rectangle.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQFbc8Vp8xMAEw/article-inline_image-shrink_400_744/0/1684179297444?e=1689811200&v=beta&t=M7QO7ZdcylQ6W4grOmguGY3aI_S-G-cpAVWiJOiyMcc)
_Screenshot of shapes in Google Sheets drawings menu_

Double click in the shape to add text, and resize, recolor, restyle as needed.

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQHSkIBOsRvNdg/article-inline_image-shrink_1000_1488/0/1684179429349?e=1689811200&v=beta&t=9G87KKPY_efHEOTU_K2POBbUzeSfFlbs5nG282Oo4Gc)
_Screenshot of button in Google Sheets_

Once you've created your button, click Save and Close. Then resize and position it where you'd like it in the Google Sheet. I've put mine right under the scorecard, and I made one for each score as well as a reset button.

Finally, to make the button work, click the three little dots at the top right of the button and select **assign script**. Then type in the name of the script (without the parentheses).

![No alt text provided for this image](https://media.licdn.com/dms/image/D5612AQGCHPMJ8FW-hw/article-inline_image-shrink_1500_2232/0/1684179559428?e=1689811200&v=beta&t=41p0tXKvG3Moj8bTJAI45nUhcZAUjhzPNoSbD_IP57I)
_Screenshot of assigning a script to a button in Google Sheets_

Now, all you've got to do is click one of the buttons and the assigned script will run 🔥.

Two notes:

1. The first time you run a script, there will be a pop-up dialog box asking you to accept the security allowances. It's a safety net to make sure you know you're running the code that's written in Apps Script, and to examine it if you didn't write it. You'll need to click through those and accept the risk to allow it to run.
2. If you need to move a button after assigning the script, you may get frustrated when clicking it doesn't bring up the three dots for the menu and only runs the script. To get around this and allow for movement and the three dot menu, right click the button.

## Wrapping Up

I hope this has been helpful for you!

Please subscribe to [my YouTube channel here](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) for more content like this.

Have a great one!


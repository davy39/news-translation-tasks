---
title: Word Count in Excel – How to Check the Number of Words
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-03-09T23:51:24.000Z'
originalURL: https://freecodecamp.org/news/word-count-in-excel-how-to-check-the-number-of-words
coverImage: https://cdn-media-2.freecodecamp.org/w1280/603d3e41a675540a2292502b.jpg
tags:
- name: business
  slug: business
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: "Excel does not have its own tool that lets you simply look at the number\
  \ of words in a document (like Word does). But is it possible to find out anyway?\
  \ \nYes it is – but it's a bit convoluted, and it also only works on one cell at\
  \ a time. Don't worry..."
---

Excel does not have its own tool that lets you simply look at the number of words in a document (like Word does). But is it possible to find out anyway? 

Yes it is – but it's a bit convoluted, and it also only works on one cell at a time. Don't worry, though – we will see at the end how to make it work on a group of cells. Let's explore how to count words in Excel.

# The Excel Functions We'll Use to Count Characters

We need to learn about three Excel functions, `LEN()`, `TRIM()` and `SUBSTITUTE()`, before we can use them in the formula.

## How to Use the `LEN()` Function in Excel

The `LEN()` function takes a cell with text content and gives back the number of characters in that cell. 

For example, if we write `The horse under the three` in a cell, and we use the `LEN()` function to calculate the number of characters in that sentence in another cell, we'll get `25`. You can see how it works here:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/len.png)

By specifying that we want the `LEN()` of cell B1 (`LEN(B1)`, in cell B2 above), Excel does this calculation for us.

Note: I'll explain why I included the spelling error ("three" instead of "tree") below.

## How to Use `TRIM()` Function in Excel

The `TRIM()` function takes a cell with text content and gives back the same text without any white space at the beginning or end. 

For example, say we have a cell that looks like this:       `The horse under the three`   (with 7 spaces before the text and 2 at the end. It has a total length of 34 characters, including the spaces. 

The `TRIM()` function will give us back `The horse under the three` (with just the original 25 characters) without the spaces at the beginning or the end. Here's what it looks like:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/trim.png)

You can see that, similar to the example above with `LEN()`, when we put the `TRIM()` instructions in cell B4, Excel calculates the correct value in cell B5.

## How to Use the `SUBSTITUTE()` Function in Excel

The `SUBSTITUTE()` function will replace a piece of the text with another bit of text. For example, in the text we have been using there is a spelling error (instead of `tree` we have `three`). We can fix it using the `SUBSTITUTE()` function. 

The syntax is `SUBSTITUTE(text, old_text, new_text, [instance_num])`, with `text` being the text we are going to change. In this case, we'll have the text we want to change, and the `old_text` and the part we want to change (`three`) which will be replaced with the `new_text` (`tree`).

The complete formula is `SUBSTITUTE(B4, "three", "tree")`. Note that text in a formula always needs to be put in quotes. Here's how it works:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/substitute.png)

Just in case you need to know, `instance_num` is an optional parameter that you use in case there are multiple instances of `old_text` in the text and you want to change only one of them. But we aren't using it here.

# How to Count Words in Excel

We have learned how to use the above single functions, and now we need to use them together in a somewhat convoluted way. 

Before putting them together, let's try to understand how we are using them, and then we will build together the complete formula.

## How Word Count in Excel Works

Excel does not have a proper word count tool or formula, but there is one thing we can count, and that is characters, as we've learned above. Specifically, we are going to count the number of spaces inside the string. And from that, we are going to derive the number of words just adding 1 to the number of spaces. 

When we look at our example, we can see that the string `The horse under the tree` has four spaces. If we add one, we get five, the total number of words in the sentence.

Counting spaces is also not a trivial task. Since there is not a specific tool or formula that can count just spaces, we need to be a bit creative. 

What we are going to do is count the number of characters in the string, and then count the number of characters in the string when the spaces have been removed (we can use `SUBSTITUTE(text, " ", "")` for this). Then we'll take the difference between the two. 

`The horse under the tree` has 24 characters, while `Thehorseunderthetree` has 20 characters. The difference is 4, which is the number of spaces in the original string. If we add 1 we get 5, the number of words.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/count-words.png)

## Putting it into Practice

Now we need to put in a single formula that we have seen in the last paragraph. This formula has three components:

* the length of the sentence with spaces at the beginning or at the end of the sentence removed (we want to count only spaces between the words), so we'll use `LEN(TRIM(text))`
* the length of the string without spaces, in this case, we don't need to use `TRIM()` as we are removing all spaces, so `LEN(SUBSTITUTE(text, " ", ""))`
* Then we just add `1`.

The complete formula is: `LEN(TRIM(text)) - LEN(SUBSTITUTE(text, " ", "")) + 1`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/single-formula.png)

# How to Create a Custom Function to Count Words in Excel

We have learned how to count words in a cell, but maybe we don't want to type all that every time we need to count the number of words.

Fortunately, we can solve this by creating a custom function to count words. We can also have a custom function to count the total number of words in multiple cells. 

## How to Create a Custom Function with Visual Basic for Applications

We can open the VBA editor with `Alt + F11` (`FN + Alt + F11` for Mac). Then we can go to **Insert > Module**, and we are ready to write our function. 

We can use what we have already written as a starting point, but we need to replace `SUBSTITUTE`, as that doesn't exist in Visual Basic, with the `REPLACE` function. So now we'll have `LEN(TRIM(text)) - LEN(REPLACE(text, " ", "")) + 1`.

Let's name the new function we want to create. I have chosen the name `WORDCOUNT`, but you can use any name you want. Just replace it in the two places it's written with the name of your choice.

```
Function WORDCOUNT(text)
   WORDCOUNT = LEN(TRIM(text)) - LEN(REPLACE(text, " ", "")) + 1
End Function
```

Once you add this code in the editor, you have created the function. Now you can close the editor and enjoy your new function! But keep in mind that it only works for this workbook. 

So now let's make the function work with more than one cell, and then we can also add it permanently to Excel.

## How to Build a Custom Excel Function to Count the Total Number of Words in a Group of Cells

We will now update the function to work with a range of cells to make it a bit more useful. We take the same code as above, and apply it to every cell within a range, summing together the number of words in each cell. 

Replace the code we wrote before with the following:

```
Function WORDCOUNT(rng As Range)
    Count = 0
    For Each cl In rng
        thisCount = LEN(TRIM(cl.Value)) - LEN(REPLACE(cl.Value, " ", "")) + 1
        Count = Count + thisCount
    Next
    WORDCOUNT = Count
End Function
```

Note: this version works with a single range of cells, and all cells selected must contain text. You could try to make your own more versatile version if you want to, just explore VBA on your own!

Lastly, we want to make sure that our function is available in every Excel Work Book. To do that we have to close the VBA editor and save the Book we are working in as `*.xlam`, the Excel Add-In file type. 

To do that we can go to **File > Save As**, give the file a name that will let us recognize it, like "WordCount", chose the format "Excel Add-In (*.xlam)" from the drop-down menu. Don't change the folder in which you save the file, as it is set automatically to an **AddIns** folder.

Now that we have created the file, we need to import it into Excel. To do that we go to **File > Options > Add-ins**. At the bottom of the window select "Excel Add-ins" from the dropdown menu, and click **Go....** In the new window use the **Browse...** button, and there it should open the **AddIns** folder we have saved the file in. Select it and press **Ok**, then **Ok** again. Now the `WORDCOUNT()` function will be available every time you use Excel.

# Conclusion

In this article, we have learned how to count words in a string in Excel. 

And even though Excel does not have a readymade tool for counting words, we learned how to create our own custom function to avoid having to write each formula every time we want to get the number of words in a string. 

Finally, we also learned how to expand our function so that it works with any number of cells.


---
title: How to Remove Empty Rows and Columns in Google Sheets
subtitle: ''
author: Nibesh Khadka
co_authors: []
series: null
date: '2023-09-07T07:10:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-empty-rows-and-columns-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/delete-empty-rows-and-columns-in-google-sheets.png
tags:
- name: automation
  slug: automation
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
seo_title: null
seo_desc: "In this tutorial, you will learn how to remove empty rows and columns from\
  \ Google Sheets using Google Apps Script.\nA while ago I wrote an article on how\
  \ to remove empty rows and columns from Google Sheets. \nI recently revisited that\
  \ article and I now..."
---

In this tutorial, you will learn how to remove empty rows and columns from Google Sheets using Google Apps Script.

A while ago I wrote an article on [how to remove empty rows and columns from Google Sheets](https://kcl.hashnode.dev/how-to-delete-empty-rows-and-columns-in-google-sheets). 

I recently revisited that article and I now present you this revised version. 

I also have a video version of this topic which you can check out below:

%[https://youtu.be/Eiqa5ST9DYM]

## What We Will Cover

You'll create two functions: `deleteExternalEmptyRowsNColumns()` and `deleteInternalEmptyRowsNColumns()`. 

The first function will delete empty rows and columns from the range that are outside of the range returned by the method [`getDataRange()`](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getdatarange).

The second function will delete the rows and columns that are empty which are inside of the range returned by `getDataRange()`. 

We will also create a menu so that we can execute these functions from the spreadsheet itself.

## How to Prep the Sheet

My spreadsheet currently looks like the image below:

![Sheets Sample](https://cdn.hashnode.com/res/hashnode/image/upload/v1693110060718/c5e5f9e6-2ddf-4ee1-a08c-3a0a8ba4de87.png)
_Spreadsheet With Lots Of Empty Rows and Columns_

It has a couple of columns and rows with data, with lots of blank rows and columns. 

Let's make the spreadsheets look more presentable like the following image:

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693110269477/fd55cbfd-88f8-47b2-b0d1-69d1ced421b0.png)
_Final Clean Spreadsheet Version_

## How to Open Apps Script Project

Next, let's open our Apps Script project from the Extensions tab in the spreadsheet:

![Image](https://www.freecodecamp.org/news/content/images/2023/08/open_apps_script-2.png)
_Open Apps Script Project From Spreadsheet's Tab_

## How to Create a Function to Delete Empty Rows and Columns Outside of DataRange

We'll create a function named `deleteExternalEmptyRowsNColumns()`. 

This function will be responsible for deleting any empty rows and columns that are outside of the range of `getDataRange()`:

```javascript
/**
 * Delete the empty rows and columns outside of the DataRange()
 */
function deleteExternalEmptyRowsNColumns() {
  // get sheets and data
  const ss = SpreadsheetApp.getActiveSheet();
  const data = ss.getDataRange().getValues();

  //console.log(data);

  // determine last row and column
  const lastRow = data.length;
  const lastCol = data[0].length;

  // get maximum rows and columns sss
  const maxRows = ss.getMaxRows();
  const maxCols = ss.getMaxColumns();

  // only remove rows and columns if there are empty rows or columns beyond last row and columns
  if (maxRows > lastRow) {
    ss.deleteRows(lastRow + 1, maxRows - lastRow);
  }
  if (maxCols > lastCol) {
    ss.deleteColumns(lastCol + 1, maxCols - lastCol);
  }

}
```

We're using maximum rows and maximum columns because these values will return the last row and the last column of the spreadsheet regardless of the content.

 This means they also include empty rows and empty columns beyond the data range. 

Next, we only remove the columns and rows if they are outside of the range.

This means that if the maximum row is greater than the last row, then we will remove the rows. The same goes for the columns.

We're using the [`deleteRows()`](https://developers.google.com/apps-script/reference/spreadsheet/sheet#deleterowsrowposition,-howmany) method to remove those rows, which takes two parameters.

The first one is the index of the row from where the rows should be deleted, `lastRow + 1` in our case.

 The second parameter is the number of rows we should remove, which is `maxRows - lastRow` in our case. 

For columns, we'll use the [`deleteColumns()`](https://developers.google.com/apps-script/reference/spreadsheet/sheet#deletecolumnscolumnposition,-howmany) method. The way this method works is the same as the way `deleteRows()` works but on columns.

If you run this function your spreadsheet will look similar to the following image: 

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693112111932/eb0387b4-9b5a-49b3-9e9a-6b572d75be1e.png)
_Spreadsheet with Out Of Bounds Columns and Rows Removed_

You'll see the columns and rows that were outside of the range returned by `getDataRange()` have now been removed by the function.

## How to Create a Function to Delete Empty Rows and Columns Inside of DataRange

Now we will create another function: `deleteInternalEmptyRowsNColumns()`.

This will be responsible for removing empty rows and columns which are included in the `getDataRange(`) method, with this function below:

```javascript
/**
 * Deletes the empty rows and columns inside of DataRange()
 */
function deleteInternalEmptyRowsNColumns() {
  // get sheets and data
  const ss = SpreadsheetApp.getActiveSheet();
  const data = ss.getDataRange().getValues();

  const lastRow = data.length;
  const lastCol = data[0].length;

  // lets check if there're any empty columns during the beginning which is included in data
  const emptyColumnIndexes = [];
  for (let i = 1; i <= lastCol; i++) {
    if (ss.getRange(1, i, lastRow, 1).getValues().flat().join("") === "") {
      // subtract length before pushes value with less than 1 of original index
      // because later on when we delete colums one by one the indexes 
      //will be out of bounds/wrong due to sprd being updated to new indexes
      emptyColumnIndexes.push(i - emptyColumnIndexes.length);

    }

  }

  // lets delete these columns
  if (emptyColumnIndexes.length > 0) {
    // delete column
    emptyColumnIndexes.forEach(ind => ss.deleteColumn(ind));

  }

  //***************Remove Internal empty rows */
  // convert nested arrays to string and remove empty strings with filter
  const newData = ss.getDataRange().getValues().filter((arr) => arr.join("") !== "")

  const newLastRow = newData.length;
  const newLastCol = newData[0].length;

  // clear previous values
  ss.clearContents();

  // set new values
  ss.getRange(1, 1, newLastRow, newLastCol).setValues(newData);

// now delete empty rows and columns 
 deleteExternalEmptyRowsNColumns();
}
```

Let's explain what the function does in the following sections.

### How to Remove Empty Columns

First, we'll work on empty columns. After that, we'll remove the empty rows.

```javascript
 const emptyColumnIndexes = [];
  for (let i = 1; i <= lastCol; i++) {
    if (ss.getRange(1, i, lastRow, 1).getValues().flat().join("") === "") {
      // subtract length before pushes value with less than 1 of original index
      // because later on when we delete colums one by one, the indexes 
      //will be out of bounds/wrong due to sprd being updated to new indexes
      emptyColumnIndexes.push(i - emptyColumnIndexes.length);

    }

  }

  // lets delete these columns
  if (emptyColumnIndexes.length > 0) {
    // delete column
    emptyColumnIndexes.forEach(ind => ss.deleteColumn(ind));

  }
```

Let's create an array named `emptyCoiumnIndexes`. It'll hold all the indexes of the columns that are empty. 

To check if the columns are empty or not, we will loop through each column with a `for` loop starting from the first column.

Next, we will fetch the values of a column. In every loop, it will return a nested array and we will flatten the array.

After that, we will join the array with an empty string (""). 

If the joined string is actually empty we know that this is an empty column so we will push that index to the empty column indexes array with the following code: `ss.getRange(1, i, lastRow, 1).getValues().flat().join("") === ""` .

But before pushing the index, we'll subtract the length of the `emptyColumnIndexes` array from the index itself each time. 

That's because later on, when we delete this column, we have to delete each column one by one. 

While doing so, we will find out that if we delete the first column, the structure of the spreadsheet changes, and the columns that come after the deleted column will have their index changed.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693111825663/d8e82618-0404-4b89-89be-f22c33ed2d23.png)
_Spreadsheet with Inbounds Empty Columns and Rows_

For instance, from the preceding image, after we delete column "A" the index of column "F" will get changed to "E".

After this, if the `emptyColumnIndexes` is not empty then we will go through each value using [forEach()](https://www.w3schools.com/jsref/jsref_foreach.asp).

 Then we will delete the column with [deleteColumn()](https://developers.google.com/apps-script/reference/spreadsheet/sheet#deletecolumncolumnposition) method. 

Now, run this function and you'll see a similar result as the following image, where all the empty columns have been removed:

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693112373678/58a09e91-924f-4cef-a5ec-e437fcf1a597.png)
_Spreadsheet with Inbounds Empty Columns Removed_

### How to Remove Empty Rows

Now we will work on removing empty rows from our spreadsheet. 

To do so, we will filter all the non-empty rows using the same process we used earlier by joining them with empty string.

 If they are not just an empty quote (""), we'll return them as the array items in the `newData` with `const newData = ss.getDataRange().getValues().filter((arr) => arr.join("") !== "")`.

Now, we'll save those values to our spreadsheet after clearing previous contents.

But if you run this function right now, you'll find out that this alone will not remove empty columns but accumulate rows into one place like the image below:

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693114104374/502bba63-dd4d-4d67-9635-0f2b2fc75358.png)
_Spreadsheet with Outbound Empty Rows_

This is not what we want.

So, to remove those extra rows, we will just call the function `deleteExternalEmptyRowsNColumns()` , we created earlier because now these extra spaces are outside of the range of `getDataRange()`. 

Let's run the function again, and now we're be able to accomplish what we initially wanted:

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693114340988/7f0bf2d5-8f24-4e83-9389-ad6e833c2c4b.png)
_Clean Spreadsheet_

## How to Create a Custom Menu for the Spreadsheet

Finally, we will create a menu so that we can run these functions from the spreadsheet itself. 

For this create a new script file in your project named menu:

```javascript
/**
 * Menu creates menu UI in spreadsheet.
 */
function createCustomMenu() {
  let menu = SpreadsheetApp.getUi().createMenu("Delete Empty Rows N Columns");

  menu.addItem("Delete External Empty Rows and Columns", "deleteExternalEmptyRowsNColumns");
  menu.addItem("Delete Internal Empty Rows", "deleteInternalEmptyRowsNColumns");
  menu.addToUi();
}

/**
 * OnOpen trigger that creates menu
 * @param {Dictionary} e
 */
function onOpen() {
  createCustomMenu();
}
```

After saving the script, we will go to the spreadsheet and reload it. 

After a moment, you'll be able to see a menu in the spreadsheet tab like the image below:

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693114629659/3fc2f151-12c9-47d7-abc8-549b2937d9e7.png)
_Spreadsheet Menu_

Congrats! 

Now you just need to copy and paste the script from the tutorial or [this](https://github.com/nibukdk/detete_empty_rows_n_columns_in_spreadsheet) GitHub repo and you'll be able to clean your sheets instantly.

## Conclusion

In this tutorial, we created two functions: `deleteExternalEmptyRowsNColumns()` and `deleteInternalEmptyRowsNColumns()`. 

We cleared empty rows and columns that were out of bounds and later deleted empty rows and columns that were in bounds of data. 

Next, we created a menu that provides easy access to even non-coders to execute the functions mentioned above from the spreadsheet's tab.

Now, all that is left is for you to share this article. If you're also watching the video version I hope you'll subscribe to my [channel](https://youtube.com/@codingWithNibesh) as well. 

I am Nibesh Khadka, a freelancer specializing in automating Google products with Apps Script. Contact me if you need my services at me@nibeshkhadka.com.


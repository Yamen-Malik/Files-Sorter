Files Sorter
============

About The Project
----------------

A simple folder watcher that triggers when a new file is added to the folder and sort all the files inside the specified folder based on the extensions of the files.

Requirements
------------

This code uses:
* python
* watchdog library
* colorama library

Setup
------

To set this app you first need to open the `data.txt` file then write the following:  

>First Line: The path of the folder you want to watch  
>All other lines: Extension1, Extension2 :: path to send that files to


### Example

**Windows**
```sh
C:/Users/UserName/Downloads  
png,jpg,jpeg,gif,ico :: D:/images  
pdf,txt,exe :: C:Users/UserName/Desktop
```
**Linux**
```sh
/home/UseName/Downloads  
png,jpg,jpeg,gif,ico :: /home/images  
pdf,txt,exe :: /home/UserName/Desktop
```

> Note: The app will ignore the added spaces between the extensions
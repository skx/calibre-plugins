Calibre Plugins
---------------

This repository is designed to contain plugins for the [Calibre Ebook management](http://calibre-ebook.com/) application.

Currently there is only a single plugin, ResetRating.


ResetRating
-----------

This plugin is designed to set the "Rating" field to zero when a new book is imported to your collection.

I don't often get books from other people, but when I do I regard it as a bug that ratings are imported along with the new book(s).

Clearly a rating is specific to an individual, rather than a book.  What I like to read you might hate, and vice-versa.

On that basis this plugin unilaterally sets the rating field to 0 for newly imported books.

There are two ways to install this plugin, the first being via the command-line:

    cd ./ResetRating
    calibre-customize -b .

The second way being via the Calibre GUI:

* Click on "Preferences"
* Click on "Plugins"
* Click "Load plugin-from file"
* Select `ResetRating/ResetRating.zip`".


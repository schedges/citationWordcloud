# citationWordcloud
Creates wordclouds based on the abstract or keyword text of articles citing a paper/papers from INSPIRE-HEP

First, run makeDB.py supplying a list of INSPIRE-HEP article numbers and an output name for the DB.

Then, run the makeWordcloud.py script specifying either to use abstracts or keywords, and specifying the name of the .pkl file you created when making the DB.

Be sure to store article.py in the same directory as these two python scripts.

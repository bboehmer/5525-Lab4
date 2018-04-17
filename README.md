# 5525-Lab4
## Sentiment Analysis
For this lab we implemented option 1, a naive bayes classifier.  We found that our classifier preformed much much better when all words were used rather than simply "known" sentiment words. A possible explanaition of this is that the removal of non-sentiment words (while perhaps not too important in a straightforward positive/negative classification) is very important when using a more complext 5 class system.  For instance, "the movie was good" may score a 4 while "the movie was very good" may score a 5.  Removing all the non-sentiment words would leave you simply with the word "good" which would incorrectly map at least one of these reviews.  Another possibility is that much of the information about the sentiment of a movie review is found in word outside the known corpus.  

To run the lab, open a jupyter notebook and simply run all of the cells in "lab4.inpy" using python 3.

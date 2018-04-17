# 5525-Lab4
## Sentiment Analysis
For this lab we implemented option 1, a naive bayes classifier.  We found that our classifier preformed much much better when all words were used rather than simply "known" sentiment words. A possible explanaition of this is that the removal of non-sentiment words (while perhaps not too important in a straightforward positive/negative classification) is very important when using a more complex 5 class system.  For instance, "the movie was good" may score a positive while "the movie was very good" may score a strongly positive.  Removing all the non-sentiment words would leave you simply with the word "good" which would incorrectly map to, in most cases, a very positive.  This is demonstrated in our output which shows that, indeed, most of the reviews that were labeled a positive ended up being classified as a strongly possitive. The same was true with negative reviews being missclassified as very negative reviews.

Our results are shown below:

Performance Using All Observed Words:

Training Performance: 92.65%

Testing Performance: 35.48%

Performance Using Only Known Words:

Training Performance: 30.72%

Testing Performance: 19.68%

To run the lab, open a jupyter notebook and simply run all of the cells in "lab4.inpy" using python 3.


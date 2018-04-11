# 5525-Lab4
CSE 5525 Lab 4 Sentiment Analysis

This is the dataset of the paper:

This file includes:
1. original_rt_snippets.txt contains 10,605 processed snippets from the original pool of Rotten Tomatoes HTML files. Please note that some snippet may contain multiple sentences.

2. dictionary.txt contains all phrases and their IDs, separated by a vertical line |

3. sentiment_labels.txt contains all phrase ids and the corresponding sentiment labels, separated by a vertical line.
Note that you can recover the 5 classes by mapping the positivity probability using the following cut-offs:
[0, 0.2], (0.2, 0.4], (0.4, 0.6], (0.6, 0.8], (0.8, 1.0]
for very negative, negative, neutral, positive, very positive, respectively.
Please note that phrase ids and sentence ids are not the same.

4. SOStr.txt and STree.txt encode the structure of the parse trees. 
STree encodes the trees in a parent pointer format. Each line corresponds to each sentence in the datasetSentences.txt file. The Matlab code of this paper will show you how to read this format if you are not familiar with it.

5. datasetSentences.txt contains the sentence index, followed by the sentence string separated by a tab. These are the sentences of the train/dev/test sets.

6. datasetSplit.txt contains the sentence index (corresponding to the index in datasetSentences.txt file) followed by the set label separated by a comma:
	1 = train
	2 = test
	3 = dev

Please note that the datasetSentences.txt file has more sentences/lines than the original_rt_snippet.txt. 
Each row in the latter represents a snippet as shown on RT, whereas the former is each sub sentence as determined by the Stanford parser.

For comparing research and training models, please use the provided train/dev/test splits.


Original Snippets (10,605 reviews):
The Rock is destined to be the 21st Century's new ``Conan'' and that he's going to make a splash even greater than Arnold Schwarzenegger, Jean-Claud Van Damme or Steven Segal.
The gorgeously elaborate continuation of ``The Lord of the Rings'' trilogy is so huge that a column of words cannot adequately describe co-writer/director Peter Jackson's expanded vision of J.R.R. Tolkien's Middle-earth

Dictionary (phrases | Phrase IDs) (239231 phrases):
!|0
'' bathroom break|18244
'' begins to look like a '' real Kaputschnik|22972

Sentiment labels (Phrase IDs |sentiment values) (239231 phrases):
0|0.5
1|0.5
2|0.44444

[0, 0.2], (0.2, 0.4], (0.4, 0.6], (0.6, 0.8], (0.8, 1.0]
for very negative, negative, neutral, positive, very positive, respectively.
Note that phrase ids and sentence ids are not the same.

SOStr (sentence with | separating phrases):
The|Rock|is|destined|to|be|the|21st|Century|'s|new|``|Conan|''|and|that|he|'s|going|to|make|a|splash|even|greater|than|Arnold|Schwarzenegger|,|Jean-Claud|Van|Damme|or|Steven|Segal|.
The|gorgeously|elaborate|continuation|of|``|The|Lord|of|the|Rings|''|trilogy|is|so|huge|that|a|column|of|words|can|not|adequately|describe|co-writer\/director|Peter|Jackson|'s|expanded|vision|of|J.R.R.|Tolkien|'s|Middle-earth|.

STree (
70|70|68|67|63|62|61|60|58|58|57|56|56|64|65|55|54|53|52|51|49|47|47|46|46|45|40|40|41|39|38|38|43|37|37|69|44|39|42|41|42|43|44|45|50|48|48|49|50|51|52|53|54|55|66|57|59|59|60|61|62|63|64|65|66|67|68|69|71|71|0
71|70|69|69|67|67|66|64|63|62|62|61|61|58|57|57|56|53|53|52|52|49|49|50|48|45|44|43|43|42|42|41|39|38|38|40|60|39|40|41|47|46|44|45|46|47|48|51|50|51|55|54|54|55|56|59|58|59|60|73|65|63|64|65|66|68|68|72|70|71|72|73|0

dataSentences (sentence_index      sentence):
1	The Rock is destined to be the 21st Century 's new `` Conan '' and that he 's going to make a splash even greater than Arnold Schwarzenegger , Jean-Claud Van Damme or Steven Segal .
2	The gorgeously elaborate continuation of `` The Lord of the Rings '' trilogy is so huge that a column of words can not adequately describe co-writer\/director Peter Jackson 's expanded vision of J.R.R. Tolkien 's Middle-earth .

datasetSplit (sentence_index, splitset_label)
1,1    
2,1
3,2
(1 = train, 2 = test, 3 = dev)
1 = 8544
2 = 2210
3 = 1101
Total of 11855

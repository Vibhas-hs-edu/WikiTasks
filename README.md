# WikiTasks

# Steps to Run

## Step 1 : 
Clone this repository

## Step 2 : 
Install dependencies by using the following command.
pip install -r requirements.txt from the terminal.

## Step 3 :
Generate clean wikipedia xmls from wikipedia.bz2. The bash file (process-wiki-dump.sh)
extracts the wikipedia dump and cleans the wikipedia documents by removing
unnecessary HTMl markups, additional spaces etc. Finally the script will generate
a bunch of xml files which contains the list of documents. List of documents are nothing but
a long list of wikipedia text tags. The output of cleaned xmls is stored in text/AA folder. The 
bash file can be run on linux based OS by this simple command.

bash process-wiki-dump.sh

## Step 4 :
Run the python script wiki_details.py with the first argument as folderName.
This script outputs the most common 100 words as well as the most important words
for the following wikipedia article.
https://en.wikipedia.org/wiki/John_Barnes_(film_producer)

## Summary :

We use the wikiextractor to clean up the wikipedia dump and store the dump in text/AA folder. The cleaned Wikipedia 
documents are stored as xmls. The xml generated are not valid xml as they have a root tag missing. The xml are converted
to valid xml files and are stored in text/Temp folder. The python script 'wiki_details.py' is the entry point of the program.
This script takes the valid XML documents and answers the 100 most repeated words in all of xml documents and the most important
words in a Wikipedia article. The python file wiki_extractor.py uses NLTK library to tokenize the xml documents as well as to obtain
the frequency distribution of the words.

## Sample Output : 


100 Most common words with count in Wikipedia Corpus is as follows

[('the', 554474), (',', 509666), ('.', 502652), ('of', 308591), ('and', 272464), ('in', 249973), ('a', 184744), ('to', 181628), ('was', 127081), ("''", 103452), ('``', 97571), ('The', 92531), (')', 85870), ('is', 85746), ('(', 85642), ('for', 78965), ('on', 75956), ('as', 69890), ('with', 65836), ('by', 63374), ("'s", 61898), ('at', 58710), ('from', 48675), ('that', 48475), ('his', 41112), ('In', 38244), ('an', 36351), ('he', 35316), ('He', 29987), ('were', 28545), ('which', 25527), ('her', 25411), ('it', 23222), ('also', 22361), ('are', 21395), ('has', 21123), ('first', 20809), ('had', 20496), ('2018', 20334), (':', 19343), ('she', 19059), ('It', 18849), ('be', 18297), ('who', 18248), ('their', 17771), ('She', 16226), ('its', 14821), ('or', 14695), ('one', 14323), ('but', 14183), ('not', 13671), ('two', 13671), ('been', 13498), ('after', 12733), ('this', 12650), (';', 12294), ('have', 12244), ('On', 11896), ('born', 11873), ('they', 11457), ('University', 11091), ('season', 10243), ('into', 9965), ('where', 9938), ('2017', 9751), ('film', 9640), ('time', 9625), ('A', 9492), ('other', 9423), ("'", 9315), ('March', 9270), ('team', 9246), ('New', 9188), ('during', 8917), ('would', 8644), ('years', 8634), ('when', 8430), ('made', 8339), ('later', 8069), ('United', 7881), ('over', 7806), ('about', 7785), ('three', 7762), ('won', 7723), ('between', 7643), ('World', 7643), ('then', 7614), ('more', 7572), ('up', 7567), ('This', 7553), ('him', 7491), ('family', 7485), ('American', 7473), ('all', 7457), ('work', 7317), ('became', 7307), ('National', 7258), ('new', 7185), ('out', 7083), ('year', 7075)]

 The most imporant words in the doc with doc_id 56572679 are  
 
 ['Barnes', 'Wadsworth', 'Encyclopædia', 'Britannica', 'Bolex', 'Belford', 'blue-collar', 'craftsmen', 'rheumatic', 'fever', 'sparked', 'teenage', 'inferior', 'intellectually', 'inconvenience', 'choices', 'artistically', 'Monmouth', 'radio-drama', 'Nordine', 'fiercely', 'protective', 'scripts', 'Judi', 'Dench', 'Douglass', 'Kiley', 'Sternhagen', 'Shaw', 'Shakespeare', 'Moffat', 'magnum', 'opus', 'constraints', 'avoided', 'lesser', 'immense', 'circulated', 'persevered', 'ignite', 'classroom', 'screening', 'theorists', 'opinions', 'Encyclopaedia', 'EB', 'Weisenborn', 'portrayals', 'institutional', 'censorship', 'allude', 'filmmakers', 'relied', 'abundance', "'Bill", 'iconic', 'adaptations', 'Macbeth', 'politically', 'oriented', 'Equality', 'Lost', 'Generation', 'interracial', 'racist']
 
# References :

1) https://github.com/attardi/wikiextractor/wiki
2) https://en.wikipedia.org/wiki/Tf%E2%80%93idf
3) https://www.nltk.org/

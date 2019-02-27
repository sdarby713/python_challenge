import re

inputtext = "paragraph2.txt"

#  Assumption:  all sentences in paragraph end with either period("."), question mark ("?") or exclamation point("!")

# initialize our tracking/reporting variables
totsentences = 0
totwords = 0
totletters = 0
sentences = []
words = []


with open(inputtext, "r") as text:
    paragraph = text.read()

paragraph = re.sub("\n"," ",paragraph)      # remove newlines
sentences = re.split("(?<=[.!?])+",paragraph)
   
totsentences = len(sentences) - 1           # because the last sentence ends correctly, the above split results in an extra (null) sentence

x = 0
for sentence in sentences:
    sentence = re.sub("[.?!,;:'()]","",sentence)   # substitute out charachters which don't count as letters
    words = re.split("[ ]+",sentence)

    if words[0] == "":                         # have observed null "words" at beginning of sentences
        words.pop(0)

    totwords += len(words)
    for word in words:
        totletters += len(word)
      
outfile = 'paragraph_analysis2.txt'
ofile = open(outfile,"w")

outputline = ("Paragraph Analysis")
print (outputline)
ofile.write(outputline + "\n")   # need a newline character for file writes

outputline = ("------------------")
print (outputline)
ofile.write(outputline + "\n")   

outputline = ("Approximate sentence count:   " + str(totsentences))   
print (outputline)
ofile.write(outputline + "\n")   

outputline = ("Approximate word count:       " + str(totwords))
print (outputline)
ofile.write(outputline + "\n")   

outputline = ("Average sentence length:      " + '{:6.3f}'.format(totwords / totsentences))
print (outputline)
ofile.write(outputline + "\n")   

outputline = ("Average letter count:         " + '{:6.3f}'.format(totletters / totwords))
print (outputline)
ofile.write(outputline + "\n")   

ofile.close()
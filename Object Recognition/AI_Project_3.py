import nltk



sampleArray = ['Tobenna is a very interesting fellow of high class, who is liked by all']
               

def processContent():
    try:
        for item in sampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)

            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>}"""
            chunkParser = nltk.RegexpParser(chunkGram)

            chunked = chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
            
    except Exception as e:
        print(str(e))
    


processContent()
		




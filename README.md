# EazyMind

**EazyMind** provides **ai-as-a-service** for **abstractive text summarizaion** , you simply provide your
1. Sentence to be summarized
2. Api key [from free registeration on eazymind website ](http://eazymind.herokuapp.com/arabic_sum)

-------------------------------------------------
## Insatllation :
1. Regsiter a Free account on [EazyMind](http://eazymind.herokuapp.com/arabic_sum)
2. ```pip install eazymind```

-------------------------------------------------
## Usage :
```
from eazymind.nlp.eazysum import Summarizer

#---key from eazymind website---
key = "xxxxxxxxxxxxxxxxxxxxx"

#---sentence to be summarized---
sentence = """(CNN)The White House has instructed former
    White House Counsel Don McGahn not to comply with a subpoena
    for documents from House Judiciary Chairman Jerry Nadler, 
    teeing up the latest in a series of escalating oversight 
    showdowns between the Trump administration and congressional Democrats."""
    
summarizer = Summarizer(key)
print(summarizer.run(sentence))
```


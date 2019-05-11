from nlp.eazysum import Summarizer

key = "xxxxxxxxxxxxxxxxxxxxx"

sentence = """(CNN)The White House has instructed former
    White House Counsel Don McGahn not to comply with a subpoena
    for documents from House Judiciary Chairman Jerry Nadler, 
    teeing up the latest in a series of escalating oversight 
    showdowns between the Trump administration and congressional Democrats.
  
    McGahn's decision not to comply 
    with the subpoena could push Nadler 
    to hold McGahn in contempt of Congress, 
    just as he's moving to do with Attorney General William Barr after the Justice 
    Department defied a subpoena for the unredacted Mueller report and underlying evidence."""


summarizer = Summarizer(key)
print(summarizer.run(sentence))
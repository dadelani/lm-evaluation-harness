from lm_eval.utils import macro_f1_score


def doc_to_text(doc):
    output = """I am providing you with the definition Hate speech, Abusive language and Normal tweets.
    
    An Hate speech is language content that expresses hatred towards a particular group or individual based on their 
    political affiliation, race, ethnicity, religion, gender, sexual orientation, or other characteristics. 
    It also includes threats of violence.

    Abusive language is any form of bad language expressions including rude, impolite, insulting or 
    belittling utterance intended to offend or harm an individual. 
    
    Normal does not contain any bad language. 

    Tweet: {tweet}
    
    Which category does the tweet above belong to: 'Hate', 'Abuse' or 'Normal'. Pick exactly one category.  
    """

    text = output.format(tweet=doc["tweet"])
    return text


def doc_to_target(doc):
    replacements = {0: "Hate", 1: "Abuse", 2: "Normal"}
    return replacements[doc["label"]]

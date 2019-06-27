from nltk import sent_tokenize, word_tokenize
from csv import reader
def is_sentence_good(sentence):
    with open('templates\\positive-words.txt', 'r') as file:
        word_list = file.read().splitlines()
    # valid_words = ['i' for word in word_list if word in word_tokenize(sentence)]
    # good_word_score = len(valid_words)
    good_word_score = len(['i' for word in word_list if word in word_tokenize(sentence)])
    file.close()
    # print("Good word score :"+str(good_word_score))
    with open('templates\\negative-words.txt', 'r') as file:
        word_list = file.read().splitlines()
    bad_word_score = len(['i' for word in word_list if word in word_tokenize(sentence)])
    # print("Bad word score :"+str(bad_word_score))
    file.close()
    return good_word_score > bad_word_score
def return_viable_treatments(text, treatment_list):
    def sentence_good_score(sentence):
        with open('templates\\negative-words.txt', 'r') as file:
            word_list = file.read().splitlines()
            for phrase in word_list:
                if phrase in sentence:
                    sentence = sentence.replace(phrase,'')
        file.close()
        with open('templates\\positive-words.txt', 'r') as file:
            word_list = file.read().splitlines()
        good_word_score = len(['i' for word in word_list if word in sentence])
        file.close()
        return good_word_score
    viable_treatments = []
    token_text = sent_tokenize(text.lower())
    for treatment in treatment_list:
        score = sum([sentence_good_score(sentence) for sentence in token_text if " "+treatment+" " in sentence])
        if score > 0:
            # print(treatment+str(score))
            viable_treatments.append(treatment)
    return viable_treatments
def get_treatment_list():
    with open('treatments.csv', newline='') as csvfile:
        treatment_list = [row[0].lower() for row in reader(csvfile)]
        return treatment_list
def get_conditions_dict():
    with open('conditions.csv', newline='') as csvfile:
        conditions_dict = {row[0].lower():row[1].lower() for row in reader(csvfile)}
        return conditions_dict

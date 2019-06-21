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
                    print(phrase + " Is removed")
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
text = """Alternative Treatments for Prostate Cancer
IN THIS ARTICLE
Which men are at risk for prostate cancer?
How does diet impact prostate cancer?
What about lycopene for prostate cancer?
Is pomegranate juice chemopreventive?
What do we know about saw palmetto berry for prostate problems?
What do we know about African plum tree for prostate conditions?
After non-melanoma skin cancer, prostate cancer is the most commonly diagnosed cancer in American men. It's also highly treatable if caught early. For many men, though, the standard treatments for prostate cancer -- medication, radiation, and surgery -- often come with unwanted side effects.

Because of those side effects, some men wonder if alternative treatments might be beneficial. Is it possible such remedies as herbs and natural dietary supplements might help treat or slow the progression of prostate cancer? Might they delay the development of this disease? Clinical trials continue to investigate these questions.

Which men are at risk for prostate cancer?
Prostate cancer is the second leading cause of cancer-related deaths among men in the United States. It is thought that virtually all men with circulating androgens (hormones) will develop microscopic prostate cancer if they live long enough. In fact, when prostatic tissue is scrutinized under a microscope after surgery (or at autopsy), cancer is found in 50% of men older than age 70. And it's found in virtually all men over age 90.

How does diet impact prostate cancer?
Diet may account for about one-third of cancers of the prostate, large bowel, and breast. All of these cancers are more common in the Western world than in Asian countries such as Japan and China. Although cancer is influenced by both hereditary and environmental factors, studies show that Japanese men and those who eat a vegetarian diet have the lowest rates of prostate cancer. One possible explanation is the low fat content of the Asian diet. Another is that certain nutrients in the foods in these diets may help reduce the cancer risk.

A healthy diet rich in nutrient-dense fruits and vegetables may reduce your risk of prostate cancer.

Vitamin D3 has shown promise as a treatment for advanced prostate cancer, but is still under study.

If you've been diagnosed with prostate cancer, listen to your conventional medical doctor. Your doctor will guide your treatment regimen using the latest proven cancer therapies. Some alternative treatments for prostate cancer may be harmful when used with standard cancer treatments. So, always check with your health care provider before using any natural herb or supplement. That way you can avoid drug-herb interactions.
"""
treatment_list = get_treatment_list()
print(return_viable_treatments(text, treatment_list))
# import nltk as n
class searcher:
    def __init__(self, name):
        self.name = name
    def is_food(self):
        def make_list(self):
            with open ("lists\\foods2.txt", "r") as file:
                raw = file.read().lower().splitlines()
            raw2 = [line.split(",")[0] for line in raw]
            names = []
            for i in raw2:
                if i not in names:
                    names.append(i)
            names.sort()
            search_results = [line for line in raw if self.name.lower() in line]
            return search_results
        search_results = make_list(self)
        if len(search_results)>0:
            return True
        else:
            return False
    def is_supplement(self):
        pass
# print(search_results)

search_string = searcher("olive oil")
# search_string = "olive oil"
print(search_string.is_food())
print(search_string.is_food().make_list())

# tokens = n.word_tokenize(raw)
# text = n.Text(tokens)
# text.concordance(search_string.lower())
def single_root_words(root_word, *other_words):
    res = []
    for w in other_words:
        if root_word.lower().find(w.lower()) != -1 or \
                w.lower().find(root_word.lower()) != -1:
            res.append(w)
    return res


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

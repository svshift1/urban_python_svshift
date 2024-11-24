
def all_variants(text: str) -> str:
    for n in range(1, len(text) + 1):
        for k in range(len(text) - n + 1):
            yield text[k:k + n]


for t in all_variants('123456789'):
    print(t)
#author -- orsessential
def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    sentence_split = sentence.split()
    new_s = []
    max_val = len(sentence_split) - 1
    for s in range (len(sentence_split)):
        new_s.append(sentence_split[max_val])
        max_val-=1
    sentences = ' '.join(new_s)
    sen = []
    for i in sentences:
        charc = i.upper() if i.islower() else i.lower()
        sen.append(charc)
        sentense_new = ''.join(sen)
    return sentense_new

if __name__ == '__main__':
    sentence = 'aWESOME is cODING'
    obj = reverse_words_order_and_swap_cases(sentence)
    print(obj)

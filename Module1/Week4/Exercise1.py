# read file and get vocabs

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words
vocabs = load_vocab("D:/Homework/Module1/Week4/source/data/vocab.txt")

# count levenshtein_distance

def leven_distance(token1, token2):
    distances = [[0]*(len(token2)+1) for i in range(len(token1)+1)]
    
    for t1 in range(len(token1)+1):
        distances[t1][0] = t1
    for t2 in range(len(token2)+1):
        distances[0][t2] = t2
    a = 0
    b = 0
    c = 0
    for i in range(1, len(token1)+1):
        for j in range(1, len(token2)+1):
            if (token1[i-1] == token2[j-1]):
                distances[i][j] = distances[i-1][j-1]
            else:
                a = distances[i-1][j] + 1
                b = distances[i-1][j-1] + 1
                c = distances[i][j-1] + 1
                if (a <= b) and (a <= c):
                    distances[i][j] = a
                elif (b <= a) and (b <= c):
                    distances[i][j] = b
                else:
                    distances[i][j] = c
    return distances[len(token1)][len(token2)]
print(leven_distance("elmets", "elements"))
import streamlit as st

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input(label = "Word")
    if st.button("Compute"):

        leven_distances_dict = dict()
        for vocab in vocabs:
            leven_distances_dict[vocab] = leven_distance(word, vocab)
        sorted_word = dict(sorted(leven_distances_dict.items(), key = lambda item:item[1]))
        correct_word = list(sorted_word.keys())[0]
        st.write("correct word: ", correct_word)

if __name__ == "__main__":
    main()
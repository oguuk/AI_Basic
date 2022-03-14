# 문제 2:
# string 문장을 받아 단어를 역순으로 출력하는 함수를 작성하세요.

sentence = "way a is there will a is there where"

def reverse_sentence(sentence):
    return " ".join(reversed(sentence.split())) # 띄어쓰기 기준으로 split해 리스트로 저장한 뒤 순서를 뒤집고, 띄어쓰기 단위로 string으로 합쳐 return

print(reverse_sentence(sentence))

# 출력
# where there is a will there is a way

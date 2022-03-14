#**Q5. 이전에 구현한 클래스에서 merge_list의 함수 동작을 변경해야합니다. 단순합계가 아닌 평균을 구하는 함수로 변경해보세요.**
#
#**- 리스트의 데이터를 다루는 함수를 이용해서 구현해보세요.**
#
#- **최종 평균을 구한 후 오름차순으로 정렬해주세요.**

# Question 5

file_path = "./data-01-test-score.csv"

class ReadCSV():
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.score_list = []

    def read_file(self):
        with open(self.__file_path, 'r') as data:
            while True:
                line = data.readline()
                if not line: break
                line_list = [int(score) for score in line.strip('\n').split(',')]
                self.score_list.append(line_list)

        return self.score_list
    
    def merge_list(self):
        if not self.score_list:
            self.read_file()
    
        sum_list = [sum(line)/len(line) for line in self.score_list]

        return sorted(sum_list)

read_csv = ReadCSV(file_path)
print(read_csv.merge_list())


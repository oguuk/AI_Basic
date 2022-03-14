#**Q4. 우리는 방금 CSV 파일을 읽는 함수를 구현해보았습니다. 하지만 이를 조금 더 효율적으로 사용하기 위해서 클래스로 구성을 진행하려고 합니다. 방금 구현한 함수를 포함한 클래스를 구현해보세요.**
#
#**- merge list를 이용해 리스트 내 데이터의 합을 출력해보세요.**
#
#- **데이터를 합치기 전 데이터의 자료형을 변경해보세요.**

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
    
        sum_list = [sum(line) for line in self.score_list]

        return sum_list

        
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())

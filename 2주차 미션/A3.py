#**Q3. 이번 시험 결과에 대한 데이터를 학과 사무실에서 CSV파일로 전달해줬습니다. 우리는 이 파일을 이용해서 데이터 처리를 진행해야 합니다. 파일 입출력을 이용해 파일 데이터를 리스트로 만들어보세요.**
#
#- **파일 입출력에 사용하는 open 함수를 이용해 CSV 파일 내부의 데이터를 읽어보세요**
#
#****CSV파일은 아래 첨부되어있습니다.**

file_path = "./data-01-test-score.csv"

class ReadCSV():
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def read_file(self):
        import csv
        f = open(self.__file_path, 'r', encoding='utf-8')
        rdr = csv.reader(f)
        score_list = [i for i in rdr]
        
        return score_list


read_csv = ReadCSV(file_path)
print(read_csv.read_file())

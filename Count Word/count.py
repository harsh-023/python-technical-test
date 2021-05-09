import unittest
import HtmlTestRunner
extract_data = ""
transform_data = ""

class testing(unittest.TestCase):
           
            # Extract
    def test_a_extract(self):
        global extract_data
        src_file = "source_file.txt"  # file to be open for read
        try:
            with open(src_file, 'r') as f_open:
                extract_data = f_open.read()  # store the data
        except Exception as e:
            print("error because file not exists"+"\n"+e)
        print("successful data read from file")

       
        # Transform
    def test_b_transform(self):
        global extract_data
        global transform_data
        def word_count(str):  
            data = dict()
            words = str.split()

            for word in words:
                if word in data:
                    data[word] += 1
                else:
                    data[word] = 1

            return data

        extract_data = extract_data.lower()  # store the data
        transform_data = word_count(extract_data)  # transformed and count word data
        print("successful data transformed from file")

        # Load
    def test_c_load(self):
        dest_file = "destination_file.txt"  # file to be written
        with open(dest_file, 'w') as f_write:
            for i, j in transform_data.items():
                f_write.write(f'"{i}" : {j} \n')
        print("successful data write to file")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Django/technical python test/report/Word_count_Test_report"))
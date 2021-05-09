import unittest
import HtmlTestRunner
extract_data = ""
transform_data = ""


class testing(unittest.TestCase):

    def test_a_extract(self):
        # extract
        global extract_data
        self.src_file = "source_file.txt"  # file to be open for read
        try:
            with open(self.src_file, 'r') as f_open:
                extract_data = f_open.read()  # store the data
        except Exception as e:
            print("error because file not exists"+"\n"+e)
        print("successful data read from file")

        # transform
    def test_b_transform(self):
        global extract_data
        global transform_data
        transform_data = extract_data.title()  # transformed and capitalized data
        print("successful data transformed (Capitalize) from file")

    def test_c_load(self):
        # load
        global transform_data
        dest_file = "destination_file.txt"  # file to be written
        with open(dest_file, 'w') as f_write:
            f_write.write(transform_data)  # write data to destination file
        print("successful data write to file")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Django/technical python test/report/Capitalize_Test_report"))
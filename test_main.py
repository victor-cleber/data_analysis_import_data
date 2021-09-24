import unittest
import main


class Test_Main_Menu(unittest.TestCase):
    def test_import_files_option(self):
        """
        Test
        """
        option = 1
        result = menu(option)
        self.assertEqual(result, "import files")

    def test_show_logs_option(self):
        pass

    def test_show_number_of_imported_records(self):
        pass

    def test_show_file_details(self):
        pass

    def test_exit_option(self):
        pass


if __name__ == '__main__':
    unittest.main()


class FileParser():
    def __init__(self):
        self.filetype = ".csv"

    def __str__(self):
        return "FileParser"

    def read_file_and_print_summary(self, file_handle, column):
        Exception("read_file not implemented for {}".format(self.__str__))

    def _is_filetype(self, filename):
        return filename.endswith(self.filetype)

    def _get_summary(self, dataframe, column):
        return dataframe[column].describe()
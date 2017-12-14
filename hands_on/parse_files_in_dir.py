import argparse
import configparser
import os


def parse_files_in_dir(directory_path, column_name):
    all_files = os.listdir(directory_path)

    for filename in all_files:
        print("parsing file {}".format(filename))

        if filename.endswith(".csv"):
            print("File was a CSV!")
            #Put your code here!
            pass
        if filename.endswith(".xls"):
            print("File was an XLS!")
            # Put your code here!
            pass
        else:
            #let us know if a file isn't a csv or xls file
            pass







cmd_arg_parser = argparse.ArgumentParser("parse_files_in_dir: a simple script to print column summaries per file for a supplied directory")
cmd_arg_parser.add_argument('-t', action="store_true", default=False,
                            dest="is_test",
                            help="Set mode to test. There will be additional debug information and no computationally expensive functions will be run.")
cmd_arg_parser.add_argument('--dir',
                            action="store",
                            dest="model_dir",
                            help="Load model(s) from directory to restart model learning from a saved checkpoint. This is false by default")
cmd_arg_parser.add_argument('-c',
                            action="store",
                            dest="columnname",
                            help="Column name to search for in files")


cmd_args = cmd_arg_parser.parse_args()

directory_name = os.path.dirname(os.path.realpath(__file__))
if cmd_args.model_dir != None:
    directory_name = cmd_args.model_dir

column_name = "age"
if cmd_args.columnname != None:
    column_name = cmd_args.columnname



print(cmd_args)
print(directory_name)
print(column_name)
if cmd_args.is_test == None or cmd_args.is_test == False:
    parse_files_in_dir(directory_name, column_name)


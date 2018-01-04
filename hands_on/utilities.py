import csv
import os
import re

def return_filetype_list(folderpath, filetype=".csv"):
    '''
    Returns a list of all files that match a given filetype

    :param folderpath: the absolute path to the folder to check
    :param filetype: the file suffix to check and return. Defaults to .csv
    :return: a list of filename strings
    '''
    filelist = []
    #directory = os.fsencode(folderpath)

    #Adding all the csv files from a folder into a list
    for file in os.listdir(folderpath):
        #filename = os.fsdecode(file)
        if file.endswith(filetype):
            filelist.append(file)
    return filelist


def make_list_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        embedded_list = list(reader)

    flat_list = [item for sublist in embedded_list for item in sublist]

    return flat_list

def check_for_doctors_in_csv(filename):
    csv_list = make_list_from_csv(filename)
    parsed_list = parse_list_for_doctors(csv_list)

    return parsed_list


def parse_list_for_doctors(candidate_list):
    output_list = list()
    doctor_list = ["Doctor", "Doc", "Dr", "MD"]
    for name in candidate_list:
        for check in doctor_list:
            if re.search(check, name) is not None: output_list.append(name)

    return output_list

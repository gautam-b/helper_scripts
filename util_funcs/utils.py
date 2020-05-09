# ------------Pickle save and load
import pickle


def save_pickle(filename, data):
    # Store data (serialize)
    with open(filename, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


def load_pickle(filename):
    # Load data (deserialize)
    with open(filename, 'rb') as f:
        return pickle.load(f)


# ------------checking execution time
import time


# use @timeit decorator over the function to check execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        t = time.time() - t
        print(f"{func.func_name} took {t:03f} seconds.")
        return result
    return wrapper


# ===------------Extract zipfile
def exttract_zip(zipfile, destination=None, pwd=None):
    from zipfile import ZipFile
    with ZipFile(zipfile, 'r') as zip:
        zip.extractall(path=destination, pwd=pwd)


# ------------csv file (modify as necessary )
import csv


def save_to_csv(file_name, rows_list, header=False):
    with open(file_name, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)

        # rows_list is a list of list with each row is a list of individual field
        [writer.writerow(row) for row in rows_list]


def load_csv(file_name):
    with open(file_name, 'r') as f:
        return [line for line in csv.reader(f)]


# -----------Date range generator
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))


# Alternatively
import pandas as pd
daterange = pd.date_range(start_date, end_date)


# ------------Downlaoding large files
# using request library
import requests


def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    return local_filename


# useing urllib library
from urllib.request import urlretrieve


def download_file(url):
    local_filename = url.split('/')[-1]
    urlretrieve(url, local_filename)
    return local_filename


# ------------Logging
import logging


logging.basicConfig(filename='python.log', level=logging.ERROR)
logging.error('This message should go to the log file')


# ------------PDF to Text
import subprocess
from pathlib import Path


def pdfbox(pdf_file, text_file):
    """
    Convert pdf file to text and save it to disk
    Requirement: Apache pdfbox command line tools

    This function requires Apache pdfbox from https://pdfbox.apache.org/download.cgi
    Download pdfbox Command line tools from http://www-eu.apache.org/dist/pdfbox/2.0.11/pdfbox-app-2.0.11.jar
    and put it in the current folder.
    """
    pdfbox = Path(__file__).parent / "pdfbox-app-2.0.11.jar"

    resp = subprocess.run(["java", "-jar", pdfbox, "ExtractText", pdf_file, text_file])
    if resp.returncode == 0:
        print("pdf file converted to text")
    else:
        print("Error in file conversion")
    return resp.returncode


def pdf_to_text(pdf_file, text_file, output_layout='table'):
    """
    Convert pdf file to text and save it to disk
    Requirement: Xpdf tools

    This unction requires 'pdftotxt.exe' binary file from https://www.xpdfreader.com/
    Download Xpdf tools from https://www.xpdfreader.com/download.html and copy 'pdftotxt.exe' file in the current folder
    """
    pdf2txt = Path(__file__).parent / "pdftotext"

    if output_layout:
        output_layout = f"-{output_layout}"
        resp = subprocess.run([pdf2txt, output_layout, pdf_file, text_file])
    else:
        resp = subprocess.run([pdf2txt, pdf_file, text_file])

    if resp.returncode == 0:
        print("pdf file converted to text")
    else:
        print("Error in file conversion")
    return resp.returncode

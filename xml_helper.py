import xml.etree.ElementTree as ET
from os import listdir
import os

def make_xml_valid(wiki_file, temp_folder_name):
    """
    The cleaned XML document is missing a root tag.
    Add root tag before any further processing.

    :param wiki_file: The cleaned wiki file
    :param temp_folder_name: The folder where the valid
     xml files will be stored

    :return: returns the file path of newly generated
    valid xml
    """
    parent = os.path.dirname(wiki_file)
    file_name =os.path.basename(wiki_file)
    temp_folder = os.path.join(os.path.dirname(parent), temp_folder_name)
    xml_temp = os.path.join(temp_folder, file_name)
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    old = open(wiki_file, 'r')
    old_file_contents = old.read()
    new = open(xml_temp, 'w')
    new.write('<root>' + old_file_contents + '</root>')
    new.close()
    return xml_temp

def parseXML(xmlfile, temp_folder_name):
    """
    Retrieves all doc tags from the cleaned xml documents.
    Converts the xmlfile to a valid xmlfile.

    :param xmlfile: The cleaned xml wiki file
    :param temp_folder_name: The folder where the valid
     xml files will be stored

    :return: returns all documents
    """
    new_xml = make_xml_valid(xmlfile, temp_folder_name)
    tree = ET.parse(new_xml)
    root = tree.getroot()
    return root.findall('doc')

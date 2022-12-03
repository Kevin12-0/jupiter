from xml.etree.ElementTree import *

data = {}
data_array = []
name_document = 'locations.xml'
doc_xml = parse(name_document)
root = doc_xml.getroot()
print(root)
print("----------------------------------------------------")
""" imprime el tag """
print(root.tag)

""" imprime el id del tag """
for i in root:
    print(i.attrib)
    """ imprime el tag """
    for place in i:
        print(place.tag)
        """ imprime el texto """
        print(place.text)
        data.pop(place.text)
        for location in place:
            print(location.text)
            data[location.tag] = location.text
            data.pop(location.text)
print(data)
"""imprime el tag de los registros"""
""" for i in root:
    print(i.tag) """

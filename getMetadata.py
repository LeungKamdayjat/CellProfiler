
## Two ways to get metadata for time-elapse data from image

#get meta information from the image 
import czifile
from lxml import etree
czi = czifile.CziFile(rawimg)
czi_xml_str = czi.metadata()
# print(czi_xml_str)
czi_parsed = etree.fromstring(czi_xml_str)
# this returns a list (take first element of list under presumption
# that a file can't have multiple creation dates
creation_date = czi_parsed.xpath("//CreationDate")[0]
print(creation_date.text)


#get OME Metadata from file
import bioformats
import javabridge
javabridge.start_vm(class_path=bioformats.JARS)
data = bioformats.get_omexml_metadata(rawimg)
import xml.etree.ElementTree as ET
import pandas as pd
xml_data = data
# Parse the XML
root = ET.fromstring(xml_data)
namespaces = {'ns': 'http://www.openmicroscopy.org/Schemas/OME/2016-06'} # change ns to your namespace
# Initialize a list to hold the data
cleandata = []
# Find all 'Plane' elements and iterate over them
for plane in root.findall('.//ns:Plane', namespaces):
    # Extract the attributes of the 'Plane' element and add them to the list
    cleandata.append(plane.attrib)
# Convert list of dictionaries to pandas DataFrame
df = pd.DataFrame(cleandata)
print(df)
##run in napari env
from aicsimageio import AICSImage
from aicsimageio.writers import OmeTiffWriter

# Get an AICSImage object
rawimg = "test.image.3.czi"
img = AICSImage(rawimg)
img.data  # returns 6D STCZYX numpy array
img.dims  # returns string "STCZYX"
img.shape  # returns tuple of dimension sizes in STCZYX order
img.shape
img.dims
individual_data = img.get_image_data("ZTYX")

import napari
viewer = napari.view_image(individual_data, colormap='magma')

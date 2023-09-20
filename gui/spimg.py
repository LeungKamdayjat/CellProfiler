from pathlib import Path
import os
from aicsimageio import AICSImage
from aicsimageio.writers import OmeTiffWriter
from pathlib import Path

def split_imge(input_dic):

    mydir = Path(input_dic)
    print(mydir)
    file_list = [] # create an empty list

    for file in mydir.iterdir():
        print(file)
        if file.suffix == '.czi':
            file_list.append(str(file)) # append in files in folder with .tif

    print(file_list)
    images_path = os.path.join(input_dic, "images")
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    for img in file_list: 
        filename = Path(img).stem
        print("img:",img)
        img2 = AICSImage(img) # Open an czi image in file_list
        
        img_channels = img2.dims.C
        img_scenes = len(img2.scenes)
        img_time = img2.dims.T
        # print(img_channels,img_scenes,img_time)
        for S in range(img_scenes): #loop through scene by scene (aka positions)
            for T in range(img_time): #loop through time by time
                for C in range(img_channels):
                    img2.set_scene(S)
                    single_img_data = img2.get_image_data("ZYX",S=S,T=T,C=C)
    #for two channel image, split C1C2#for three channel image, split C1C2C3#for four channel image, spliot C1C2C3C4
                    if img_channels == 2:
                        file_name = f"{filename}_{os.path.splitext(img)[1]}.S{S+1:03d}.T{T+1:03d}.C{C+1:03d}.ome.tif"
                        OmeTiffWriter.save(single_img_data,os.path.join(input_dic, "images", file_name))
                    if img_channels == 3:
                        file_name = f"{filename}_{os.path.splitext(img)[1]}.S{S+1:03d}.T{T+1:03d}.C{C+1:03d}.ome.tif"
                        OmeTiffWriter.save(single_img_data,os.path.join(input_dic, "images", file_name))
                    elif img_channels == 4:
                        file_name = f"{filename}_{os.path.splitext(img)[1]}.S{S+1:03d}.T{T+1:03d}.C{C+1:03d}.ome.tif"
                        OmeTiffWriter.save(single_img_data,os.path.join(input_dic, "images", file_name))

if __name__ == "__main__":
    input_dic = "/Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/16_CellProfilerPipeline/cp.ipynb/JL.v1.test/raw"
    split_imge(input_dic)
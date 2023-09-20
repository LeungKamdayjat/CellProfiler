import cellprofiler_core.pipeline
import cellprofiler_core.preferences
import cellprofiler_core.utilities.java
import pathlib
import os, glob
# start in headless mode

def run_cp(output_dic,input_dic, pipeline_file):
    cellprofiler_core.preferences.set_headless()
    cellprofiler_core.utilities.java.start_java()
    image_set_list = cellprofiler_core.image.ImageSetList()
    image_set = image_set_list.get_image_set(0)
    import skimage.data
    x = skimage.data.camera()
    image_x = cellprofiler_core.image.Image(x)
    image_set.add("x", image_x) # skimage.io.imshow(image_set.get_image("x").pixel_data)
    object_set = cellprofiler_core.object.ObjectSet()
    objects  = cellprofiler_core.object.Objects()
    object_set.add_objects(objects, "example")
    measurements = cellprofiler_core.measurement.Measurements()
    # load pipeline file
    pipeline = cellprofiler_core.pipeline.Pipeline()
    pipeline.load(pipeline_file)

    # create output folder
    output_path = os.path.join(output_dic, "output")
    input_path = os.path.join(input_dic,"images")
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    current_dir = pathlib.Path().absolute()
    #print(current_dir)
    cellprofiler_core.preferences.set_default_output_directory(output_path)
    #[print(setting.to_dict()) for setting in pipeline.modules()[-1].settings()]
    file_list = glob.glob(os.path.join(input_path, "*.TIF"))
    files = [file.as_uri() for file in file_list]
    pipeline.read_file_list(files)
    output_measurements = pipeline.run()

if __name__ == "__main__":
    input_dic = "/Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/16_CellProfilerPipeline/cp.ipynb/JL.v1.test/raw"
    split_imge(input_dic)
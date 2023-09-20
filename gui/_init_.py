import GUI
import spimg

data = GUI.run_gui()

#variables will be created: input_folder, cellpose_module_folder,cellprofiler_pipeline_folder,module_file,pipeline_file
for key, value in data.items():
    globals()[key] = value

spimg.split_imge(input_folder)
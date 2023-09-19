# Using CellPose AI Segmentation in CellProfiler - Python Batch Processing

## Introduction

Following setup is been used to generate Batch Processing by combining CellPose and CellProfiler. Both images need to be installed from source. 

## Prerequisites

- Installation of CellProfiler from Source. [Toturial](https://github.com/LeungKamdayjat/cppipeline/tree/main)
- Python3.8 ImageAnalysis Envirnment

## Topics

- Set up CellPose
- Set up CellPose-GPU (If you have good GPU)
- Combineing CellPose Parameter to CellProfiler Pipeline
- Example

## Set up CellPose

Detailed Document is in CellPose [github page](https://github.com/MouseLand/cellpose#local-installation--2-minutes). 

## Set up CellPose-GPU

Official Document is in CellPose [github page](https://github.com/MouseLand/cellpose#gpu-version-cuda-on-windows-or-linux). 

Here's how I setup mine: 

**Using NVIDIA GPU with PyTorch**

If you have the intention of processing numerous images, it would be efficient to use the GPU version of PyTorch. Here's a step-by-step guide:

1. **Install NVIDIA Driver**:
    - Before you can use your NVIDIA GPU with Python, you need to install the appropriate NVIDIA driver. Visit [this website](https://www.nvidia.com/Download/index.aspx) to download the right driver for your GPU.

2. **Install CUDA Toolkit**:
    - You can either install the standalone [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit) (opt for one of the 11.x releases) or use the cudatoolkit that comes bundled with PyTorch when installed via conda. If you run into issues with the latter approach, it's advisable to manually install the CUDA toolkit.

3. **Uninstall the CPU Version of PyTorch**:
    ```bash
    pip uninstall torch
    ```

4. **Install the GPU Version of PyTorch**:
    - Visit the [official PyTorch website](https://pytorch.org/get-started/locally/) for detailed instructions.
    - We highly recommend using conda for the installation.
    - Choose the CUDA version compatible with your GPU. Note: Newer GPUs might need newer CUDA versions (e.g., versions beyond 10.2).
    
    For example, to install CUDA version 11.6 for PyTorch on Linux or Windows:
    ```bash
    conda install pytorch pytorch-cuda=11.6 -c pytorch -c nvidia
    ```

    If you experience issues with the latest CUDA versions, consider using an older version. For instance, to install PyTorch with CUDA 11.3:
    ```bash
    conda install pytorch==1.12.0 cudatoolkit=11.3 -c pytorch
    ```

5. **Verify Installation**:
    After installation, you can verify the version of PyTorch you have installed:
    ```bash
    conda list | grep pytorch
    ```
    Ensure that the version info displays `cuXX.X` indicating a CUDA version and not `cpu`.

## Combineing CellPose Parameter to CellProfiler Pipeline

Setting up CellPose Parameter is pretty much similar to [modify settings in cellprofiler pipeline](https://github.com/LeungKamdayjat/cppipeline/tree/main#changing-module-setting).


If you're looking to set up and run a specific pipeline in CellProfiler, here's a step-by-step guide on how to do that:

**1. Initialize CellProfiler:**
Start off by initializing CellProfiler in headless mode and setting up the necessary components:

```python
import cellprofiler_core

# Set CellProfiler to headless mode.
cellprofiler_core.preferences.set_headless()

# Start the Java environment.
cellprofiler_core.utilities.java.start_java()

# Initialize image and object sets.
image_set_list = cellprofiler_core.image.ImageSetList()
image_set = image_set_list.get_image_set(0)
object_set = cellprofiler_core.object.ObjectSet()
objects = cellprofiler_core.object.Objects()
object_set.add_objects(objects, "example")
measurements = cellprofiler_core.measurement.Measurements()
```

**2. Load your Pipeline:**
After setting up the environment, load your desired pipeline:

```python
pipeline = cellprofiler_core.pipeline.Pipeline()
pipeline.load("<your pipeline name>")

# View the loaded modules in your pipeline.
print(pipeline.modules())
```

Upon executing this, you should see an output that displays the loaded modules. For instance:

```python
# Sample pipeline modules() output
...
```

**3. Incorporate RunCellpose:**
If you're integrating Cellpose, here's how you can add it to your pipeline:

```python
import cellprofiler.modules.runcellpose

# Initialize the RunCellpose module.
module = cellprofiler.modules.runcellpose.RunCellpose()

# Specify the module's position in the pipeline.
module.module_num = 9
pipeline.add_module(module)

# If needed, modify your modules.
# Example: pipeline.modules()[7] = pipeline.modules()[8]
```

**4. Modify Pipeline Settings:**
To further customize your pipeline, you can modify specific settings:

```python
# Example settings for the ninth module:
pipeline.modules()[8].setting(1).set_value("cells")
...
[print(setting.to_dict()) for setting in pipeline.modules()[8].settings()]
```

Replace the ellipsis (`...`) with your specific settings adjustments.

**5. Execute the Pipeline:**
Lastly, run the pipeline on your set of images:

```python
import os
import pathlib

# Create an output directory if it doesn't exist.
folder_name = 'output'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

# Specify the image directory and output preferences.
current_dir = pathlib.Path().absolute()
cellprofiler_core.preferences.set_default_output_directory("output")

# Read the list of images to process.
file_list = list(pathlib.Path('.').absolute().glob('image\\*.TIF'))
files = [file.as_uri() for file in file_list]
pipeline.read_file_list(files)

# Run the pipeline.
output_measurements = pipeline.run()
```

After running this, you should see the processed images in your output folder.

**Note:** If you're using the `enhanceorsuppressfeatures` module and encounter issues with multichannel images, make sure to adjust the `channel_axis` argument to `-1` as shown:

```python
# ... your function ...
gmask = skimage.filters.gaussian(mask.astype(float), sigma, mode="constant", channel_axis=-1)
# ... more of your function ...
```



# CellProfiler Image Analysis: Batch Processing Pipeline

This is an introduction of using Python designed CellProfiler to do image analysis with no programming experience. It starts with setting up CellProfiler using Python, changing specific module setting, and exporting dataset. 

## Prerequisites
- Windows 10
- Python = 3.8

## Topics
- Setting Up Python Environment
- Organizing Dataset
- Initalizing CellProfiler in Python
- Changing Module Setting
- Export data and data analysis using Python

## Setting up Python Environment
The general instructions of installing python environment should be in the [CellProfiler documentation website](https://github.com/CellProfiler/CellProfiler/wiki/Source-installation-%28Windows%29).

Here's the detailed documentation that worked for me: 

---

**Step 1: Install Git**

Download and install Git from [Git official website](https://git-scm.com/download/win).

For those who prefer GUI, consider using [GitHub Desktop](https://desktop.github.com/) or [GitKraken](https://www.gitkraken.com/).

**Step 2: Clone CellProfiler GitHub Repo**

After installing Git or GitHub Desktop, clone the CellProfiler repository:

```
git clone https://github.com/CellProfiler/CellProfiler.git
```

If using GitHub Desktop, you can clone the repository by visiting the [CellProfiler GitHub page](https://github.com/CellProfiler/CellProfiler), clicking "Clone or download", then "Open in Desktop".

**Step 3: Install Python 3.8 64-bit**

Download and install Python 3.8 64-bit from [Python official website](https://www.python.org/downloads/).

Remember to check the box that says "Add Python to PATH" during the installation.

**Step 4: Install Microsoft Visual C++ Redistributable 2015-2022**

Download and install the [Microsoft Visual C++ Redistributable](https://visualstudio.microsoft.com/vs/features/cplusplus/) appropriate for your architecture.

**Step 5: Install Microsoft Visual Studio C++ build tools**

Download and install [Visual Studio](https://visualstudio.microsoft.com/). Remember to select 'Desktop development with C++' during the installation.

**Step 6: Install Java JDK 11**

Download and install [Java JDK 11](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).

**Step 7: Set Windows Environment Variables**

Set both JAVA_HOME and JDK_HOME to the location of your JDK installation. You can do this in the system environment variables.

**Step 8: Install Anaconda and Setup Conda Environment**

1. Download and install Anaconda from the [Anaconda official website](https://www.anaconda.com/products/distribution).
   
2. After installation, open the Anaconda Prompt (or your system terminal) and create a new conda environment named "ImageAnalysis" with Python 3.8:

```
conda create --name ImageAnalysis python=3.8
```

3. Activate the newly created environment:

```
conda activate ImageAnalysis
```

**Step 9: Install CellProfiler's libraries and dependencies**

Open Command Prompt and navigate to the cloned CellProfiler directory:

```
cd /path/to/cloned/CellProfiler
```

Install the required packages:

```
pip install numpy
pip install -e .
```

If you run into errors related to cellprofiler_core, clone and install CellProfiler-core from source:

```
git clone https://github.com/CellProfiler/core.git
cd core 
pip install -e .
```

**Step 10: Start CellProfiler**


```
pip install cellprofiler

```
You should now be able to start CellProfiler from the command line:

```

cellprofiler

```

---

P.S. Due to different Cython versions, there might be problems installing Centrosome. This issue can be fixed by using git clone to download centrosome and change the source file manually. [Problem with CellProfiler MacOS M1 source installation](https://forum.image.sc/t/problem-with-cellprofiler-macos-m1-source-installation/83954/2)


## Organizing Dataset

#### Select Input Files

Iput files should be located in <a>raw</a> folder in local path. Within raw folder, there should be the czi images. 

Run print(file_list) can show you the files in the folder. 

#### Split CZI files

<code style="background:grey;color:white">.czi</code> files are divided into tif files and store them in the <code style="background:grey;color:white">image folder</code>. The following chuck requires **aicsimageio** module in your python interpretor. Run this under <code style="background:grey;color:white">ImageAnalysis environment</code>. 

The loop are repeated based on number of positions (scenes), time stamps, and channels. Each loops would feed out a tif image with suffix at the end. If a image is at Scene3, Time2, channel2, then the suffix will be <code style="background:grey;color:white">S003.T002.C002</code>. 

You can customize your naming to meet the cellprofiler pipeline requirement. 

For example, 
If you have various three channel images and two channel images, you can change your naming in the loop: For images with 2 channels, name your images into C1C2; for images with 3 channels, name your images into C0C1C2. Eventually your pipeline can only look at blue channel and green channel.

## Initalizing CellProfiler in Python

Open CellProfiler in headless mode, started java environment, import example data and images, set empty object set, set empty measurement, load pipeline

## Changing Module Setting

Before running the pipeline, make sure that desired module is imported to the cellprofiler directory so that it can be loaded.

To properlly set up modules inside of the given cellprofiler pipeline, modules should be within the pipeline. 

If you module is from outside source, then your module should be removed from the pipeline. 

In a given pipeline, delete the external-source modules, but make a note about the number of the external-source modules so that you can re-insert in here. 

To insert external-source modules, you need a module number, which is the location of the module in a pipeline, indicted by <code style="background:grey;color:white">module.module_num</code>. You can check if the module is been properly inserted by print our the modules using ```pipeline.modules()```.

Cellpose module in the pipeline starts with default setting. You can check the default setting using
```[print(setting.to_dict()) for setting in pipeline.modules()[8].settings()]```. The list number is 8 since python starts with 0. 

You can learned your pipeline setting by opening **.cpppl** files. Scrolling down to the RunCellpose module and you can see your settings. Change the default setting to your custom settings. Two settings, <code style="background:grey;color:white">cp_module_dic</code> and <code style="background:grey;color:white">cp_mudole</code> have been set previous, here shown in variables instead of strings. 

## Export data and data analysis using Python

You can directly get the output_measures by python, followed by data analysis. Simply run ```output_measurements.get_measurement_columns()``` to find your data, and ```output_measurements.get_measurement('<setting one>','<setting two>')``` to get your data for further analysis. 

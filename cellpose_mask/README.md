# Analysis Using First time point Mask to analyse

## Step One: Load Files and Data for creating masks
#### Select pipeline, input folder and models
Select the folder, usually three parameter: **cp_pipeline** is the name of pipeline, the location of pipeline should be the same as this code. **cp_mudole** is the name of the trained model set of CellPose. **cp_mudole_dic** is the location of the model. the syntax should be similar to input directory, either <code style="background:grey;color:white">Default input Folder</code> or <code style="background:grey;color:white">Default Input Folder sub-folder</code> followed by subfolder of your module. 

#### Select Input Files

Iput files should be located in <a>raw</a> folder in local path. Within raw folder, there should be the czi images. 

Run print(file_list) can show you the files in the folder. 

#### Split CZI files

<code style="background:grey;color:white">.czi</code> files are divided into tif files and store them in the <code style="background:grey;color:white">/mask</code> folder. 

The mask folder should consist of all the first-time-stamp images in the raw folder. 

The following chuck requires **aicsimageio** module in your python interpretor. Run this under <code style="background:grey;color:white">ImageAnalysis</code> environment. 

The loop are repeated based on number of positions (scenes), time stamps, and channels. Each loops would feed out a tif image with suffix at the end. If a image is at Scene3, Time2, channel2, then the suffix will be <code style="background:grey;color:white">S003.T002.C002</code>. 

You can customize your naming to meet the cellprofiler pipeline requirement. 

For example, 
If you have various three channel images and two channel images, you can change your naming in the loop: For images with 2 channels, name your images into C1C2; for images with 3 channels, name your images into C0C1C2. Eventually your pipeline can only look at blue channel and green channel.

## Step Two: Run Cellpose on mask images

Open CellProfiler in headless mode, started java environment, import example data and images, set empty object set, set empty measurement, load pipeline

#### Set up Cellpose module 

Before running the code, make sure that cellpose module is imported to the cellprofiler directory so that it can be loaded.

To properlly set up cellpose module inside of the given cellprofiler pipeline, cellpose module should not be within the pipeline. 

In a given pipeline, delete the cellpose module, but make a note about the number of cellpose modules so that you can re-insert in here. 

To insert cellpose module, you need a module number, which is the location of the module in a pipeline, indicted by <code style="background:grey;color:white">module.module_num</code>. You can check if the module is been properly inserted by print our the modules using ```pipeline.modules()```.

#### Change cellpose settings
Cellpose module in the pipeline starts with default setting. You can check the default setting using
```[print(setting.to_dict()) for setting in pipeline.modules()[8].settings()]```. The list number is 8 since python starts with 0. 

You can learned your pipeline setting by opening **.cpppl** files. Scrolling down to the RunCellpose module and you can see your settings. Change the default setting to your custom settings. Two settings, <code style="background:grey;color:white">cp_module_dic</code> and <code style="background:grey;color:white">cp_mudole</code> have been set previous, here shown in variables instead of strings.

## Step Three: Reorganize the folder

From previous step, there's mask image in maskoutput folder. Here, i first split all the czi images within the <code style="background:grey;color:white">maskoutput folder</code>. Then I create the  folder for each scene and combine the `.czi `split images within each folder.

The strucutre of the folder would be:

<code style="background:grey;color:white">/maskoutput</code>: initially saving for all reference mask images (first time stamp of all the scenes)

<code style="background:grey;color:white">/maskoutput/_name of the image</code>: a folder that later be created to contain one single mask images and all the split .czi images. 

If start fresh, the directionary is set the same as the script location.  Never run this following 2 times. If needed, add following line before defining file location. 

```os.chdir('<your parent directory folder>')```

## Step Four: Run cellprofiler for each folder

First, change the name and direction of the mask image using <code style="background:grey;color:white">maskchdir</code> and <code style="background:grey;color:white">convert_to_desired_format</code>.

Then, in <code style="background:grey;color:white">runcellprofiler</code>, insert the maskimage direction and run the pipeline. 

----


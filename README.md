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

You should now be able to start CellProfiler from the command line:

```
cellprofiler
```

---

Please note that this tutorial assumes you are familiar with using command-line interface. If you encounter any errors during these steps, you may need to consult the relevant software's documentation or contact their support.

- P.S. Due to different Cython versions, there might be problems installing Centrosome. This issue can be fixed by using git clone to download centrosome and change the source file manually. [Problem with CellProfiler MacOS M1 source installation](https://forum.image.sc/t/problem-with-cellprofiler-macos-m1-source-installation/83954/2)

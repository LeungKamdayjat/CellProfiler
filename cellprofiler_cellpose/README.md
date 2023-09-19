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

Official Document is in CellPose [github page]([https://github.com/MouseLand/cellpose#local-installation--2-minutes](https://github.com/MouseLand/cellpose#gpu-version-cuda-on-windows-or-linux)). 

Here's my personal instructions: 

---

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

---



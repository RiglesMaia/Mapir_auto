# MAPIR Image Processing Automation

This repository contains Python code for automating image processing tasks using the MAPIR Camera Control (MCC) software. The automation script facilitates the preprocessing and analysis of images captured by MAPIR cameras.

## Requirements
- Python 3.x
- Libraries:
    - pywinauto

## Usage
1. Clone or download this repository to your local machine.
2. Ensure you have the necessary Python libraries installed (see Requirements section).
3. Run the `main.py` file.
4. The script will connect to the MAPIR Camera Control (MCC) software or start it if not already running.
5. It will then input the necessary data, configure image processing settings, and initiate the processing of images.
6. The script is designed to automate the preprocessing and analysis for two types of MAPIR images: RGN and REDEDGE. You can customize the script to include additional image types as needed.

## Functionality
- `data_input(x)`: Simulates pressing the ENTER key `x` times. Used for navigating through the MCC software interface.
- `wait_process(mapir)`: Waits for the image processing button to become enabled, indicating that the software is ready for processing.
- `image_process(pasta, conectar=True)`: Automates the image processing workflow. It inputs the necessary data, configures processing settings, and initiates image processing.

## Script Customization
You can customize the script by modifying the `data` list to include additional image types or adjusting the image processing workflow as needed.

## Contributions
Contributions to this project are welcome. If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.

# Quick Setup — DeepVision AI

## 1. Train first
- Open `colab_training/DeepVision_AI_CNN_Training.ipynb`.
- Upload it to https://colab.research.google.com/
- Run each cell from top to bottom.
- Download `deepvision_export.zip` at the end.

## 2. Add model files
- Extract `deepvision_export.zip`.
- Copy `deepvision_cnn.keras` and `class_names.json` to `laptop_app/models/`.

## 3. Install and run on Windows
Open PowerShell in the `laptop_app` folder:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If `py` isn't recognized and the same Python executable used for your AutoSelect project is still installed:

```powershell
& "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe" -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Then double-click `run_app.bat`.

**Note:** TensorFlow compatibility with very new Python versions can vary. If installation fails under Python 3.14, install Python 3.11 or 3.12 from python.org, create `.venv` with that interpreter, then install requirements. Do not reuse the AutoSelect environment because this app needs TensorFlow.


## Trained Model File

The trained CNN model is not currently included in this GitHub repository because it exceeds the standard file upload limit.

Before running the application, obtain the trained model file named `deepvision_cnn.keras` and place it here:

`laptop_app/models/deepvision_cnn.keras`

The `class_names.json` file must remain in the same `models` folder.

Without the trained model file, the application may not be able to make predictions.

## Project Folder Locations

- Training notebook: `colab_training/DeepVision_AI_CNN_Training.ipynb`
- Application: `laptop_app/app.py`
- Dependencies: `laptop_app/requirements.txt`
- Windows launcher: `laptop_app/run_app.bat`
- Model files: `laptop_app/models/`

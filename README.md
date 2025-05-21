# PromptEngineeringStage
### PromptEngineering
Prompt Engineering with Few-Shot Examples and Validation

### Overview
This project demonstrates prompt engineering for open-source LLMs (e.g., GPT-2, Phi-2) using:
- Few-shot prompt tuning (examples with answers)
- Flexible validation logic
- Fallback responses for reliability
- Debugging output to observe model behavior

### Requirements
- Google Colab with GPU runtime (required for performance) 
- Python 3.x (pre-installed in Google Colab)
- `transformers` library (installed during setup)

### Files
- `requirements.txt`: Lists dependencies required to run scripts.
- `prompt_engineering.py`: The main script that runs the prompt engineering with few-shot examples and validation.

### Setup and Usage
1. Open the prompt_engineering.py script in Google Colab (https://colab.research.google.com/):
   - Go to Google Colab.
   - Since prompt_engineering.py is a Python script (.py) and not a notebook (.ipynb), you’ll need to create a new notebook to run the script:
     - Click File > New notebook in Drive to create a blank notebook.
   - Upload the file to the Colab file system: 
     - Click the Files tab on the left, then click the Upload button and upload prompt_engineering.py.
     - Alternatively, copy the contents of prompt_engineering.py (from your local machine or the GitHub repository) and paste them into a code cell in the notebook.
2. Set up GPU Runtime:
   - Go to Runtime > Change runtime type.
   - Select GPU as the hardware accelerator.
   - Click Save.
3. Install Dependencies: 
   - Add a new cell at the top of the notebook and run the following command to install dependencies from `requirements.txt`: `!pip install -r https://raw.githubusercontent.com/mariahcoleno/PromptEngineeringStage/main/requirements.txt`
   - If the above command fails (e.g., due to network issues or GitHub access), use this fallback:`!pip install transformers torch`
   - This ensures the required libraries are installed in the Colab environment.
4. Run the Script:
   - If the file is in the Colab environment (e.g., in the /content/ directory), you can execute it using a code cell with the command:`!python /content/prompt_engineering.py`
     - If you encounter a "file not found" error, double-check the file path and ensure the file is in the correct directory (e.g., /content/).
   - If you pasted the contents of prompt_engineering.py into a code cell, simply run that cell.
   - The script will use the GPU for faster inference.
 
### Note
- Running this project on a CPU (e.g., via terminal) is not recommended. Inference will be very slow or may fail for larger models like microsoft/phi-2.
- Google Colab provides free GPU access, but sessions may time out after inactivity. Save your work frequently.  

### Example 
**Prompt:**
- Topic: Machine learning
- A: It's when computers learn from examples to do tasks like guessing what's in a picture.

- Topic: Python
- A: It's a programming language people use to tell computers what to do, like making games or apps.

- Topic: Photosynthesis
- A:

**Model Output:**  
`It's how plants make food from sunlight, like when a leaf turns sunshine into sugar.`

**Validation:**  
Passed

### To Modify the Example:
- Change the `topic` variable in the script to test different queries.
- Edit the examples in the `build_prompt` function to tune the prompt for your use case.

### Project Structure
- PromptEngineeringStage/
  - PromptEngineering/
    - prompt_engineering.py # script for prompt engineering with few-shot examples and validation
    - README.md
    - requirements.txt

### Dependencies
- Listed in requirements.txt:
  - transformers
  - torch (required for GPU support in Colab)




# Welcome to the IBM Hackathon! 🎉

This repository serves as a template to help you get started quickly.  
Follow the project structure, fork the repo, and clone it locally to begin.

---

## 1. Fork the Repository

1. Click **Fork** (top right) to create a copy under your own account
2. Make sure the fork is **public**  
   If it isn't, go to:  
   **Settings → Change repository visibility → Public**

---

## 2. Clone the Repository

Once you have forked the repository:

```bash
# Clone your fork (replace <your-user> and <repo> with your info)
git clone https://github.com/<your-user>/<repo>.git

# Move into the project folder
cd <repo>
```

---

## 3. Contribute

### Create a new branch for each feature or fix:

```bash
git checkout -b feature/my-awesome-feature
```

### Commit your changes:

```bash
git add .
git commit -m "Add: my awesome feature"
git push origin feature/my-awesome-feature
```

---

## 4. Quick Rules

✅ Keep your fork **public** during the hackathon  
✅ Follow the **template's structure**  
❓ For any questions: contact **kryptosphere@devinci.fr**

---

## 5. Have Fun and Good Luck!

Good luck during the IBM Hackathon — build, learn, and most importantly: **have fun!** 🚀



## 📋 Description

This project implements an automated response generation system using the LLaMA 3.2 11B Vision Instruct model, available through the IBM watsonx.ai API.
The script reads a CSV file containing question–answer pairs to train the model with examples, then generates a relevant response to a new user query.

## 🏗️ Architecture

The system architecture is based on four main steps:

### Data Reading:
The file data_pretraitee.csv contains about 400 pairs of questions and answers.
The script reads this data using Python’s csv module to integrate it into the model prompt.

### Prompt Construction:
Each example is formatted as follows:

Input: <question>  
Output: <answer>  


This structure helps the model understand the relationship between each question and its corresponding answer.

Model Interaction via IBM watsonx.ai:
The script interacts with the model using the ibm_watsonx_ai library.
The selected model is:

meta-llama/llama-3-2-11b-vision-instruct


Generation parameters (decoding method, maximum number of tokens, repetition penalty, etc.) are configured to ensure coherent and relevant responses.

### Generation and Post-processing:
The generated text is cleaned to remove unnecessary repetitions or prompt artifacts.
If the output is incoherent or empty, a default fallback message is returned.

### Continuous Improvement:
When the user is satisfied with a generated response, they can click a dedicated button.
The question and answer are then added to the data_pretraitee.csv file, allowing the model to continuously improve by learning from validated interactions.

## ⚙️ Installation
1. Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

### 2. Install dependencies

Make sure you have Python 3.9+ installed, then run:

pip install ibm-watsonx-ai

### 3. Configure environment variables

You need an IBM Cloud account with an active watsonx.ai project.
Add your API key and space ID:

export SPACE_ID="<your_space_id>"

🚀 Usage

Simply run the main script:

python main.py


The program will read the CSV file, build the prompt, send the query to the IBM watsonx.ai model, and display the generated response in the console.



<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,12&height=180&section=header&text=REST+API+Development+for+Resume+Classification&fontAlignY=35&fontSize=30&fontColor=fff&animation=twinkling&fontAlaigny=35"/>

  
Hi, we are a team from the **Scientific Research Institute (IREDE)** and we will present a project developed there, how it works, its technologies and workflows.



# Description
The idea of ​​the project is to create a **REST API** that **classifies resumes** in their **respective areas of activity** and predicts their **level of experience** (senior, mid-level or junior).

The API works as a **CV repository** where CVs can be placed in PDF and then their classification and experience level can be accessed.


# Instalation

Before running the project, it is necessary to have some dependencies installed such as:
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
-  Jupyter Notebook ↓
```bash
pip install notebook
``` 

**After installing these dependencies, follow the steps below:**
1. Clone the repository on your machine
2. Install the virtual environment in the repository (.venv)
```bash
python3 -m venv .venv
``` 
3. Activate .venv
```bash
- source .venv/bin/activate #linux

- .venv/scripts/activate #windows
```
4. Install the libraries and dependencies that are in requirements.txt
```bash
pip install -r requirements.txt
```
5. Enter the src folder and run uvicorn:
```bash
- cd src

- uvicorn main:app --reload
```
6. Access the API swagger at http://127.0.0.1:8000/docs
![Imagem](https://media.discordapp.net/attachments/1250086904146427924/1260244789216149534/Screenshot_from_2024-07-09_11-42-09.png?ex=668e9deb&is=668d4c6b&hm=d109fece9204a49f7aa6323e4be64a59e1f0a2755439554030c1a14d5345fdf7&=&format=webp&quality=lossless&width=1440&height=521)

# Technologies

 ![Python](https://img.shields.io/badge/-python-0D1117?style=for-the-badge&logo=python&logoColor=1572B6&labelColor=0D1117) ![Jupyter](https://img.shields.io/badge/-Jupyter-0D1117?style=for-the-badge&logo=Jupyter&logoColor=E44C30&labelColor=0D1117) ![FastApi](https://img.shields.io/badge/-FastApi-0D1117?style=for-the-badge&logo=fastapi&labelColor=0D1117&textColor=0D1117)  ![NLP](https://img.shields.io/badge/-Natural_Language_Processing-0D1117?style=for-the-badge&logo=&labelColor=0D1117&textColor=0D1117)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white) ![Vscode](https://img.shields.io/badge/Vscode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-000?style=for-the-badge&logo=linux&logoColor=FCC624) ![Azure](https://img.shields.io/badge/Azure-blue?style=for-the-badge&logo=microsoft%20azure&logoColor=blue&labelColor=FFFFFF&link=https%3A%2F%2Fimages.app.goo.gl%2FK7PN1jYJd57x4q7A8) 



For technologies, we use the Python language, Jupyter Notebook and its libraries and frameworks:

### Natural Language Processing:
Text pre-processing
- Spacy
- Nltk

Machine learning model testing and training
- XGboost
- Logistic Regression
- Random Forest
- Scikit Learn

PDF Text Extraction and Dataset rocessing:
- PyMuPDF
- TextExtract 
- Pandas

### REST API:
- FastAPI
- Uvicorn

### Architecture and Infrastructure  
-  Clean Architecture -> MVC	
	- Controller
	- Service
	- Database
	- Model

### DATASET
- CSV Resume - https://www.kaggle.com/datasets/danicardeal/resume-occupation-and-seniority


# Conclusion 

### Project Objective
The main objective of this project was to develop a REST API that facilitates the classification of resumes into their respective areas of expertise and predicts the candidates' level of experience (senior, mid-level, or junior). This tool provides an efficient and automated way to categorize and evaluate resumes, saving time and resources

 ### Technology Choices
 
We chose a combination of robust technologies and libraries to ensure the effectiveness and accuracy of our model:

-   **Python**: Selected for its versatility and the wide range of libraries available for natural language processing and machine learning.
-   **Jupyter Notebook**: Used for testing and training machine learning models due to its ease of use and data visualization capabilities.
-   **Spacy and NLTK**: For text preprocessing, helping to extract and clean relevant data from resumes.
-   **XGBoost, Logistic Regression, Random Forest, and Scikit-Learn**: Used to test and train machine learning models, ensuring the best possible performance.
-   **PyMuPDF and TextExtract**: For extracting text from PDFs, essential for resume analysis.
-   **FastAPI and Uvicorn**: For building the REST API, offering a fast and efficient framework.


### Model Accuracy

**Area of Expertise Classification Accuracy**: 75%

Seniority model confusion matrix plot
![enter image description here](https://media.discordapp.net/attachments/1250086904146427924/1260242993579950220/Captura_de_tela_de_2024-07-09_11-35-21.png?ex=668e9c3f&is=668d4abf&hm=aa76a7988d7540c1a78d08cde212684fc48290074e4682bc1f3810aa29a1a30b&=&format=webp&quality=lossless&width=743&height=626)
![enter image description here](https://media.discordapp.net/attachments/1250086904146427924/1260243024462741556/Captura_de_tela_de_2024-07-09_11-33-37.png?ex=668e9c47&is=668d4ac7&hm=5b017671b697e2ad99542db87993e151e1b29bd6be0be444c98aae4089a26700&=&format=webp&quality=lossless)



**Seniority Prediction Accuracy**: 72%



# Contribuition

<table>
 <tr>
  <td style="text-align: center;">
    <a href="https://github.com/AndredsLima" target="_blank"><img src="https://github.com/AndredsLima.png" width="125"
        height="125" style="margin-right: 10px;"></a>
  </td>
  <td>
    <p><b>André Lima</b><br>≻<i> Desenvolvedor </i></p>
  </td> 
  <td style="text-align: center;">
    <a href="https://github.com/cardealdani" target="_blank"><img src="https://github.com/cardealdani.png" width="125"
        height="125" style="margin-right: 10px;"></a>
  </td>
  <td>
    <p><b>Daniel Cardeal</b><br>≻<i> Desenvolvedor </i><br></p>
  </td>
  </tr>
</table>

import pandas as pd
import logging



class_mapping_seniority = {
    1.0:0,
    2.0:1,
    3.0:2
}

def map_classes(input_csv, class_mapping):
   
    df = pd.read_csv(input_csv)
    

    df['class_numberSenioridade'] = df['seniority'].map(class_mapping)
    
    
    df_filtered = df.dropna(subset=['class_numberSenioridade'])
    

    df_filtered.loc[:, 'class_numberSenioridade'] = df_filtered['class_numberSenioridade'].astype(int)
    
  
    df_filtered.to_csv('Nlp/jupyter_notebook/BIG_DATASET.csv', index=False)
    logging.info(f'CSV file with mapped classes saved in {input_csv}') 


input_csv = 'Nlp/jupyter_notebook/BIG_DATASET.csv' 


map_classes(input_csv, class_mapping_seniority)

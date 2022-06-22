#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
from openpyxl import load_workbook


# In[2]:


root = tk.Tk()
root.withdraw()

file_path = tk.filedialog.askopenfilename()
dir_name = filedialog.askdirectory()


# In[3]:


def without_hue(ax, feature):
    total = len(feature)
    for p in ax.patches:
        percentage = p.get_height()
        x = p.get_x() + p.get_width() / 10 #+ p.get_width() / 2 - 0.05
        y = p.get_y() + p.get_height()
        ax.annotate(percentage, (x, y), size = 14)


def function(ficheiro):
    file = pd.read_csv(ficheiro)
    list_questions = file['Pergunta'].unique()
    list_questions = list_questions[~pd.isna(list_questions)]
    df = pd.DataFrame(file['username'].unique(), columns=['Username'])
    
    path = dir_name + '/Respostas.xlsx'
    writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
        
    for i in range(len(list_questions)):
        question = file.loc[file['Pergunta'] == list_questions[i]]
        question = question.reset_index(drop=True)
        
        table = question[['username','Pergunta','Resposta']]
        copy = table.copy(deep=True)
        copy.rename(columns = {'Resposta':question['Pergunta'][0],'username':'Username'}, inplace = True)
        table = copy.drop(columns='Pergunta')
        df = pd.merge(left=df, right=table, how='outer', on='Username')

        plt.figure(figsize=(15,8))
        ax = sns.countplot(x='Resposta', data = question, palette = 'Blues_r')
        plt.xticks(size=11)
        plt.xlabel('Resposta', size = 15)
        plt.yticks(size=13)
        plt.ylabel('Número de estudantes', size = 15)

        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")

        plt.title(question['Pergunta'][0], size = 20)

        without_hue(ax, question.Resposta)

        plt.savefig(dir_name + '/' + str(question['Pergunta'][0]) + '.jpeg', bbox_inches='tight', dpi=300)
        
    df = df.reindex(sorted(df.columns), axis=1)
    df.to_excel(writer,sheet_name = 'Respostas', index=False)
    writer.save()


# In[4]:


function(file_path)


# In[ ]:





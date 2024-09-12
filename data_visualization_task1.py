# -*- coding: utf-8 -*-
"""data-visualization-task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hM3j-AV2HtDoOgGnIn-v9Zn_fCTXvxup
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Age': [23, 30, 22, 24, 26, 35, 28, 40, 30, 25]
}
df = pd.DataFrame(data)
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df, palette='Set2')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=5, kde=True, color='blue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
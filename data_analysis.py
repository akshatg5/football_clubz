import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from database import load_all_from_interactions

df_main = load_all_from_interactions()
def club_piechart():
    clubs = df_main['club_name'].value_counts()
    labels = clubs.index.tolist()
    values = clubs.values.tolist()
    fig,ax = plt.subplots(facecolor = 'none',figsize=(20,18))
    colors = sns.color_palette('pastel')
    ax.set_title("Club Distribution",fontsize=29)
    ax.pie(labels=labels,x=values,colors=colors,autopct= "%1.1f%%",textprops={'fontsize':25})
    ax.tick_params(axis="both",labelsize=100)
    club_piechart = plt.savefig('static/club_piechart.png')
    return club_piechart

club_piechart()


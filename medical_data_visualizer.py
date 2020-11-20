import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = np.where(df["weight"]/(df["height"]/100)**2>25,1,0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"]=np.where(df["cholesterol"]>1,1,0)
df["gluc"]=np.where(df["gluc"]>1,1,0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df_cat=df.melt(id_vars="cardio",value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the clumns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(["cardio","variable","value"])["value"].count())
    df_cat.columns=["total"]
    df_cat.reset_index(inplace=True)
    # Draw the catplot with 'sns.catplot()'
    graph=sns.catplot(x="variable",y="total",hue="value", col="cardio",kind="bar",data=df_cat)

    fig=graph.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10,10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,
        annot = True,
        fmt = '.1f',
        linewidths = 0.5,
        square = True,
        mask = mask
    )


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

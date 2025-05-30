import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.animation as animation
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# Set seaborn style
sns.set_theme(style="whitegrid")  # Set the seaborn theme
plt.rcParams['font.family'] = 'sans-serif'  # Use a cleaner font

# Data for the 4 bar charts
categories = ['Secondary',	'Higher Secondary'	,'Diploma'	,'Graduate',	'Post Graduation',	'Professional Degree',	'Not Applicable',	'Certification Course']

# Values for each of the 4 charts
values1 = [71,	38,	21,	41,	49,	74,	45,	0]
values2 = [0,	243,	0,	290,	277,	330,	246,	0]
values3 = [13,	12,	0,	8,	9,	13,	0,	0]
values4 = [0,	20.74,	0,	34.81,	31.30,	25.09,	0,	0]


# Create figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()  # Flatten the 2x2 array to make indexing easier

# Create a dazzling color palette
palette = sns.color_palette("viridis", len(categories))  # Vibrant color palette with good color progression
# Alternative eye-catching palettes you can try:
# palette = sns.color_palette("plasma", 3)  # Vibrant yellow-orange-purple
# palette = sns.color_palette("cubehelix", 3)  # Rainbow-like with good brightness variation
# palette = sns.color_palette("coolwarm", 3)  # Dramatic blue-red contrast

# Create bar charts for each subplot
titles = [
    'Average Cumulative KPI 1- performance Achievement % of Cohort LRM', 
    'CAP on KPI 1 of Top 10% performers in CAP 12 COHORT', 
    'CAP on KPI 1 of Bottom 10% performers in CAP 12 COHORT', 
    'Performance multiple ON KPI 1 of the CAP 12 cohort'
]
value_sets = [values1, values2, values3, values4]

# Create each subplot
for i, (ax, values, title) in enumerate(zip(axes, value_sets, titles)):
    # Create dataframe for this subplot
    df = pd.DataFrame({'Categories': categories, 'Values': values})
    
    # Create the bar chart with seaborn
    sns.barplot(x='Categories', y='Values', data=df, palette=palette, ax=ax)    # Add labels and title with improved styling
    ax.set_xlabel('Categories', fontsize=12, fontweight='bold')
    # Use different y-axis label for Performance Multiple
    if i == 3:  # values4 is the fourth dataset (index 3)
        ax.set_ylabel('Ratio', fontsize=12, fontweight='bold')
    else:
        ax.set_ylabel('Values (%)', fontsize=12, fontweight='bold')
    ax.set_title(f'{title}', fontsize=14, fontweight='bold')
      # Add values on top of bars
    for j, v in enumerate(values):
        # For the last subplot (Performance Multiple), don't show percentage sign
        if i == 3:  # values4 is the fourth dataset (index 3)
            ax.text(j, v + 3, f'{v}', ha='center', fontweight='bold')
        else:
            ax.text(j, v + 3, f'{v}%', ha='center', fontweight='bold')
    
    
    # Set y-axis limit to make sure the text is visible
    ax.set_ylim(0, max(values) * 1.2)
    
    # Customize the grid
    sns.despine(left=True, ax=ax)  # Remove the left spine for cleaner look

# Add eye-catching common title with gradient effect
from matplotlib import patheffects

# Add stylish common title
title = fig.suptitle('Performance Indicators Dashboard', fontsize=24, fontweight='bold', y=0.98, 
                   color='darkblue', alpha=0.8)
# Add path effect for more pop
title.set_path_effects([patheffects.withStroke(linewidth=3, foreground='skyblue')])

# Add context information
plt.figtext(0.5, 0.02, 'Data as of May 29, 2025', ha='center', fontsize=10, fontstyle='italic')

# Add finishing touches
plt.tight_layout(pad=3.0, rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for titles

plt.savefig('Plot3 Performance Indicators KPI Combined.png', dpi=300, bbox_inches='tight')  # Save high-quality image
plt.show()
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
AgeGroup = ['20-22', '22-25','25-28', '28-30',',30-35', '35-52']

# Values for each of the 4 charts
values1 = [0,	7.45,	7.17,	7.34,	7.03,	7.14]
values2 = [0,	1.41,	1.65,	1.72,	1.98,	2.59]

# Create figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()  # Flatten the 2x2 array to make indexing easier

# Create a dazzling color palette
palette = sns.color_palette("viridis", 3)  # Vibrant color palette with good color progression
# Alternative eye-catching palettes you can try:
# palette = sns.color_palette("plasma", 3)  # Vibrant yellow-orange-purple
# palette = sns.color_palette("cubehelix", 3)  # Rainbow-like with good brightness variation
# palette = sns.color_palette("coolwarm", 3)  # Dramatic blue-red contrast

# Create bar charts for each subplot with the new titles requested including units
titles = [
    'Time to make the first sale CAP LRM cohort (Months)',
    'CAR2CATPO ratio UP TO Residency month 6 for CAP LRM cohort (Ratio)'
]
value_sets = [values1, values2]

# Create each subplot
for i, (ax, values, title) in enumerate(zip(axes, value_sets, titles)):
    # Create dataframe for this subplot
    df = pd.DataFrame({'AgeGroup': AgeGroup, 'Values': values})
    
    # Create the bar chart with seaborn
    sns.barplot(x='AgeGroup', y='Values', data=df, palette=palette, ax=ax)
      # Add labels and title with improved styling    ax.set_xlabel('Age Group', fontsize=12, fontweight='bold')
    # Set appropriate y-axis label based on the chart
    if i == 0:  # First chart (Time)
        ax.set_ylabel('Time (Months)', fontsize=12, fontweight='bold')
    else:  # Second chart (Ratio)
        ax.set_ylabel('Ratio', fontsize=12, fontweight='bold')
    ax.set_title(f'{title}', fontsize=14, fontweight='bold')
      # Add values on top of bars without currency symbols
    for j, v in enumerate(values):
        ax.text(j, v + (max(values) * 0.05), f'{v}', ha='center', fontweight='bold')
    
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
plt.savefig('Plot4 Revenue Indicators.png', dpi=300, bbox_inches='tight')  # Save high-quality image
# plt.show()
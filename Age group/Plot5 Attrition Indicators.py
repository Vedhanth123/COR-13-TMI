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

# Data for the charts
AgeGroup = ['20-22', '22-25','25-28', '28-30',',30-35', '35-52']
# Values for each of the charts (from the provided table)
# First row: Headcount
values1 = [55, 649, 1048, 698, 1250, 469]
# Second row: Tenure
values2 = [4.03, 6.26, 6.89, 7.39, 7.46, 8.60] # Using NaN for "NA" values
# Third row: Engagement
values3 = [4.00, 9.92, 10.67, 9.53, 8.48, 10.47]
# Fourth row: Attrition Risk
values4 = [37, 42, 42, 37, 38, 31]
values5 = [80, 68, 67, 61, 64, 59]

# Create figure with 3x2 subplots (for 6 charts)
fig, axes = plt.subplots(3, 2, figsize=(20, 18))  # Increased figure size for longer titles
axes = axes.flatten()  # Flatten the array for easier indexing

# Create a dazzling color palette
palette = sns.color_palette("viridis", 3)  # Vibrant color palette with good color progression
# Alternative eye-catching palettes you can try:
# palette = sns.color_palette("plasma", 3)  # Vibrant yellow-orange-purple
# palette = sns.color_palette("cubehelix", 3)  # Rainbow-like with good brightness variation
# palette = sns.color_palette("coolwarm", 3)  # Dramatic blue-red contrast

# Create bar charts for each subplot with new titles as requested
titles = [
    'Count of attrited employees in Cohort LRM',
    'Average Residency of all employees in COHORT LRM',
    'Average Residency of TOP 100 employees in KPI 1 in COHORT LRM',
    'attrition in the first six residency months as a % of people joined ( Cohort LRM)',
    'Infant attrition - attritted employees in the first 6 months as a % of all attritted employees in the first 23 months in the sub cohort'
]
value_sets = [values1, values2, values3, values4, values5]

# Create each subplot
for i, (ax, values, title) in enumerate(zip(axes, value_sets, titles)):
    # Create dataframe for this subplot
    df = pd.DataFrame({'AgeGroup': AgeGroup, 'Values': values})
    
    # Create the bar chart with seaborn
    sns.barplot(x='AgeGroup', y='Values', data=df, palette=palette, ax=ax)    # Add labels and title with improved styling    ax.set_xlabel('Age Group', fontsize=12, fontweight='bold')
    
    if i == 0: # First chart (Count chart)
        ax.set_ylabel('Count', fontsize=12, fontweight='bold')
    elif i < 3:  # Next two charts are residency/tenure
        ax.set_ylabel('Months', fontsize=12, fontweight='bold')
    else:  # Last two charts are percentages
        ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    
    # Set title with appropriate wrapping for long titles
    ax.set_title(f'{title}', fontsize=12, fontweight='bold', wrap=True)
    
    # Add values on top of bars with appropriate formatting
    for j, v in enumerate(values):
        if pd.isna(v):  # Skip NA values
            continue
        
        # Format value text based on chart type
        if i >= 3:  # Percentage charts
            txt = f'{int(v)}%'
        elif i == 0:  # Tenure chart (show with 1 decimal place)
            txt = f'{v:.1f}'
        elif values[j] == 4169:  # For headcount values
            txt = f'{int(v):,}'  # Format with commas
        else:  # Score charts
            txt = f'{v:.2f}'  # Show with 2 decimal places
            
        # Calculate vertical position for text
        if pd.notna(v):
            max_val = max([x for x in values if pd.notna(x)])
            y_pos = v + (max_val * 0.05)
            ax.text(j, y_pos, txt, ha='center', fontweight='bold')
    
    # Set y-axis limit to make sure the text is visible
    ax.set_ylim(0, max(values) * 1.2)
    
    # Customize the grid
    sns.despine(left=True, ax=ax)  # Remove the left spine for cleaner look

# Add eye-catching common title with gradient effect
from matplotlib import patheffects

# Add stylish common title
title = fig.suptitle('Attrition Indicators', fontsize=24, fontweight='bold', y=0.98, 
                   color='darkblue', alpha=0.8)
# Add path effect for more pop
title.set_path_effects([patheffects.withStroke(linewidth=3, foreground='skyblue')])

# Add context information
plt.figtext(0.5, 0.01, 'Data as of May 29, 2025', ha='center', fontsize=10, fontstyle='italic')

# Add finishing touches
plt.tight_layout(pad=5.0, rect=[0, 0.03, 1, 0.95], h_pad=5.0)  # Increased padding for titles
plt.savefig('Plot5 Attrition Indicators.png', dpi=300, bbox_inches='tight')  # Save high-quality image
plt.show()
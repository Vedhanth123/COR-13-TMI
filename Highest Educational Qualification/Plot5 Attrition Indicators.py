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
categories = ['Secondary', 'Higher Secondary', 'Diploma', 'Graduate', 'Post Graduation', 'Professional Degree', 'Not Applicable', 'Certification Course']

# Values for each of the charts (from the provided table)
# Headcount: 11, 90, 13, 3441, 597, 10, 7, 0
headcount = [11, 90, 13, 3441, 597, 10, 7, 0]
# Tenure (Months): 7.25, 7.54, 6.69, 7.07, 7.88, 12.11, 4.15, 1.00
values1 = [7.25, 7.54, 6.69, 7.07, 7.88, 12.11, 4.15, 1.00]
# Engagement Score: 8.50, NA, NA, 9.53, 10.94, NA, NA, NA
values2 = [8.50, 0, 0, 9.53, 10.94, 0, 0, 0]
# Attrition Risk (%): 53%, 40%, 69%, 39%, 35%, 29%, 73%, 0%
values3 = [53, 40, 69, 39, 35, 29, 73, 0]
# Retention Rate (%): 73%, 58%, 69%, 65%, 63%, 50%, 114%, NA
values4 = [73, 58, 69, 65, 63, 50, 114, 0]



# Create figure with 2x2 subplots (for 4 charts)
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()  # Flatten the array for easier indexing

# Create a dazzling color palette
palette = sns.color_palette("viridis", len(categories))  # Vibrant color palette with good color progression
# Alternative eye-catching palettes you can try:
# palette = sns.color_palette("plasma", 3)  # Vibrant yellow-orange-purple
# palette = sns.color_palette("cubehelix", 3)  # Rainbow-like with good brightness variation
# palette = sns.color_palette("coolwarm", 3)  # Dramatic blue-red contrast

# Note: Performance Score and Retention Rate charts might have NA values.

# Create bar charts for each subplot with new titles as requested
titles = [
    'Count of attrited employees in Cohort LRM',
    'Average Residency of all employees in COHORT LRM',
    'Average Residency of TOP 100 employees in KPI 1 in COHORT LRM',
    'attrition in the first six residency months as a % of people joined ( Cohort LRM)',
    'Infant attrition - attritted employees in the first 6 months as a % of all attritted employees in the first 23 months in the sub cohort'
]
value_sets = [values1, values2, values3, values4]

# Create each subplot
for i, (ax, values, title) in enumerate(zip(axes, value_sets, titles)):
    # Create dataframe for this subplot
    df = pd.DataFrame({'Categories': categories, 'Values': values})

    # Create the bar chart with seaborn
    sns.barplot(x='Categories', y='Values', data=df, palette=palette, ax=ax)
    ax.set_xlabel('Educational Qualification', fontsize=12, fontweight='bold')
    
    # Set appropriate y-axis label based on the chart
    if i < 3:  # First three charts are scores
        ax.set_ylabel('Value', fontsize=12, fontweight='bold')
    else:  # Last two charts are percentages
        ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
        
    ax.set_title(f'{title}', fontsize=14, fontweight='bold')
    
    # Add values on top of bars with appropriate formatting
    for j, v in enumerate(values):
        if pd.isna(v):  # Skip NA values
            continue

        # Format value text based on chart type
        if i >= 3:  # Percentage charts
            txt = f'{int(v)}%'  # Format as percentage
        elif i == 0:  # Tenure chart (show with 1 decimal place)
            txt = f'{v:.1f}'
 # Removed headcount specific formatting as headcount is not plotted here
        else:  # Score charts
            txt = f'{v:.2f}'  # Show with 2 decimal places

 # Calculate vertical position for text
        # Calculate vertical position for text
        if pd.notna(v):
            max_val = max([x for x in values if pd.notna(x)])
            y_pos = v + (max_val * 0.05)
            ax.text(j, y_pos, txt, ha='center', fontweight='bold')
    
    # Set y-axis limit to make sure the text is visible
    ax.set_ylim(0, max([x for x in values if pd.notna(x)]) * 1.2 if any(pd.notna(values)) else 10) # Handle case with all NA values
    
    # Customize the grid
    sns.despine(left=True, ax=ax)  # Remove the left spine for cleaner look

# Add eye-catching common title with gradient effect
from matplotlib import patheffects

# Add stylish common title
title = fig.suptitle('Attrition & Retention Dashboard', fontsize=24, fontweight='bold', y=0.98, 
                   color='darkblue', alpha=0.8)
# Add path effect for more pop
title.set_path_effects([patheffects.withStroke(linewidth=3, foreground='skyblue')])

# Add context information
plt.figtext(0.5, 0.01, 'Data as of May 29, 2025 | Note: NA values are not plotted.', ha='center', fontsize=10, fontstyle='italic')

# Add finishing touches
plt.tight_layout(pad=3.0, rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for titles

plt.savefig('Plot5 Attrition Indicators.png', dpi=300, bbox_inches='tight')  # Save high-quality image
plt.show()
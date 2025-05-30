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
categories = ['Employee Referral',
'Portal',
'Others',
'Not Available',
'Vendor']

# Values for each of the charts (from the provided table)
values1 = [1351, 263, 149, 0, 2406]
values2 = [8.52, 7.37, 9.21, 0, 6.99] # Using 0 for "NA" values
values3 = [10.06, 13.00, 9.00, 0, 9.07]
values4 = [33, 42, 25, 0, 43] # Already as percentages
values5 = [60, 63, 51, 0, 68] # Already as percentages



# Create figure with 3x2 subplots (for 5 charts)
fig, axes = plt.subplots(3, 2, figsize=(18, 15))
axes = axes.flatten()  # Flatten the array for easier indexing
# Remove the unused 6th subplot
fig.delaxes(axes[5])

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
    df = pd.DataFrame({'Categories': categories, 'Values': values})
    
    # Create the bar chart with seaborn
    bars = sns.barplot(x='Categories', y='Values', data=df, palette=palette, ax=ax)
    # Add labels and title with improved styling
    ax.set_xlabel('Resume Source', fontsize=12, fontweight='bold')
    
    if i == 0: # First chart (Count chart)
        ax.set_ylabel('Count', fontsize=12, fontweight='bold')
    elif i < 3:  # Next two charts are residency/tenure
        ax.set_ylabel('Months', fontsize=12, fontweight='bold')
    else:  # Last two charts are percentages
        ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    
    # Set title with appropriate wrapping for long titles
    ax.set_title(f'{title}', fontsize=12, fontweight='bold', wrap=True)
    
    # Add values inside bars
    for j, v in enumerate(values):
        if pd.isna(v) or v == 0:  # Skip NA or zero values
            continue
        
        # Format value text based on chart type
        if i >= 3:  # Percentage charts
            txt = f'{int(v)}%'
        elif i == 0 and v >= 1000:  # Large count values
            txt = f'{int(v):,}'  # Format with commas
        elif i == 0:  # Smaller count values
            txt = f'{int(v)}'
        else:  # Score/months charts
            txt = f'{v:.2f}'  # Show with 2 decimal places
            
        # Calculate position for text inside bar
        if pd.notna(v) and v > 0:
            # Place text in middle of bar
            height = v / 2
            
            # For very short bars, place text above the bar
            if v < max([x for x in values if x > 0]) * 0.15:
                ax.text(j, v + (max([x for x in values if x > 0]) * 0.05), txt, ha='center', fontweight='bold')
            else:
                # Inside the bar
                ax.text(j, height, txt, ha='center', va='center', fontweight='bold', color='white')
    
    # Set y-axis limit to make sure the text is visible
    if any(v > 0 for v in values):
        ax.set_ylim(0, max([x for x in values if x > 0]) * 1.2)
    
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
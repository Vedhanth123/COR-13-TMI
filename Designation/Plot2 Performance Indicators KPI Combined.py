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
Designation = [
    'Sales Development Manager',
    'Business Development Manager',
    'Assistant Sales manager',
    'Sales Manager',
    'Sr. Sales manager',
    'Executive sales manager',
    'Senior executive sales manager',
    'Business manager',
    'Senior business manager',
    'Executive business manager'
]

# Values for each of the 4 charts
values1_full = [45, 36, 32, 43, 41, 50, 0, 0, 0, 0]
values2_full = [174, 189, 162, 183, 427, 0, 0, 0, 0, 0]
values3_full = [10, 11, 13, 11, 5, 0, 0, 0, 0, 0]
values4_full = [16.63, 16.67, 12.83, 16.98, 83.26, 0, 0, 0, 0, 0]
Designation_full = Designation # Rename for clarity




# Filter out Designation where all values are NA
non_na_indices = []
for i in range(len(Designation_full)):
    # Check if at least one value is not NaN for this category
    if (not pd.isna(values1_full[i]) or not pd.isna(values2_full[i]) or
        not pd.isna(values3_full[i]) or not pd.isna(values4_full[i])):
        non_na_indices.append(i)

# Filter the Designation and values
Designation = [Designation_full[i] for i in non_na_indices]
values1 = [values1_full[i] for i in non_na_indices]
values2 = [values2_full[i] for i in non_na_indices]
values3 = [values3_full[i] for i in non_na_indices]
values4 = [values4_full[i] for i in non_na_indices]

# Create figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()  # Flatten the 2x2 array to make indexing easier

# Create a dazzling color palette
palette = sns.color_palette("viridis", 3)  # Vibrant color palette with good color progression
# Alternative eye-catching palettes you can try:
# palette = sns.color_palette("plasma", 3)  # Vibrant yellow-orange-purple
# palette = sns.color_palette("cubehelix", 3)  # Rainbow-like with good brightness variation
# palette = sns.color_palette("coolwarm", 3)  # Dramatic blue-red contrast

# Create bar charts for each subplot
titles = [
    'Average Cumulative Combined KPI - performance Achievement % of Cohort LRM',
    'CAP on COMBINED KPI of Top 10% performers in CAP 12 COHORT',
    'CAP on COMBINED KPI of Bottom 10% performers in CAP 12 COHORT',
    'Performance multiple of the CAP 12 cohort'
]
value_sets = [values1, values2, values3, values4]

# Create each subplot
for i, (ax, values, title) in enumerate(zip(axes, value_sets, titles)):
    # Create dataframe for this subplot
    df = pd.DataFrame({'Designation': Designation, 'Values': values})
    
    # Create the bar chart with seaborn with horizontal labels
    sns.barplot(x='Designation', y='Values', data=df, palette=palette, ax=ax)
      # Add labels and title with improved styling
    ax.set_xlabel('Designation', fontsize=12, fontweight='bold')
    # Use different y-axis label for Performance Multiple
    if i == 3:  # values4 is the fourth dataset (index 3)
        ax.set_ylabel('Values', fontsize=12, fontweight='bold')
    else:
        ax.set_ylabel('Values (%)', fontsize=12, fontweight='bold')
    ax.set_title(f'{title}', fontsize=14, fontweight='bold')      # Add values on top of bars
    for j, v in enumerate(values):
        # For the last subplot (Performance Multiple), don't show percentage sign
        if pd.notna(v): # Only add text for non-NA values
            if i == 3:  # values4 is the fourth dataset (index 3)
                txt = f'{v:.2f}' # Format Performance Multiple to 2 decimal places
            elif i == 2:  # values3 is the third dataset (index 2) - Bottom 10%
                txt = f'{int(v)}%' # Format as integer with percentage
                # Create a text element with background for better visibility
                text_obj = ax.text(j, v + (max(values) * 0.05), txt, ha='center', fontweight='bold', fontsize=12)
                text_obj.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='none', pad=0.5))
                continue  # Skip the regular text placement below
            else:
                txt = f'{int(v)}%' # Format other values as integers with percentage

            # Position the text
            valid_values = [x for x in values if pd.notna(x)]
            offset = max(valid_values) * 0.05 if valid_values else 0.5
            ax.text(j, v + offset, txt, ha='center', fontweight='bold', fontsize=9)


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
# Rotate x-axis labels for better readability
for ax in axes:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.setp(ax.get_xticklabels(), fontsize=9)  # Smaller font for x labels
    
# Add finishing touches
plt.tight_layout(pad=3.0, rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for titles

plt.savefig('Plot2 Performance Indicators KPI 1.png', dpi=300, bbox_inches='tight')  # Save high-quality image
plt.show()
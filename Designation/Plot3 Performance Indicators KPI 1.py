import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.animation as animation
from matplotlib import cm, patheffects
from matplotlib.colors import LinearSegmentedColormap

# Set seaborn style
sns.set_theme(style="whitegrid")  # Set the seaborn theme
plt.rcParams['font.family'] = 'sans-serif'  # Use a cleaner font

# Data for the bar chart - designation Designation and values
Designation_full = [
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

# Performance data from the provided table - full data including NA values
# Column 1: Distribution by Status
values1_full = [56, 41, 33, 41, 34, 46, float('nan'), float('nan'), float('nan'), float('nan')]
# Column 2: CAP KPI Combined Top 10%
values2_full = [257, 298, 229, 228, 930, float('nan'), float('nan'), float('nan'), float('nan'), float('nan')]
# Column 3: CAP KPI Combined Bottom 10%
values3_full = [4, 9, 9, 6, 8, 12, float('nan'), float('nan'), float('nan'), float('nan')]
# Column 4: Performance Multiple
values4_full = [62.75, 34.23, 24.18, 36.39, 114.71, float('nan'), float('nan'), float('nan'), float('nan'), float('nan')]

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

# Create figure and axis with seaborn color palette - horizontal layout for better viewing
fig, axes = plt.subplots(1, 4, figsize=(24, 8))
palette = sns.color_palette("viridis", len(Designation))  # Choose a nice color palette

# Create dataframe for the subplots
df1 = pd.DataFrame({'Designation': Designation, 'Values': values1})
df2 = pd.DataFrame({'Designation': Designation, 'Values': values2})
df3 = pd.DataFrame({'Designation': Designation, 'Values': values3})
df4 = pd.DataFrame({'Designation': Designation, 'Values': values4})

# Create the bar charts with seaborn with improved appearance
bars1 = sns.barplot(x='Designation', y='Values', data=df1, palette=palette, ax=axes[0], width=0.7)
bars2 = sns.barplot(x='Designation', y='Values', data=df2, palette=palette, ax=axes[1], width=0.7)
bars3 = sns.barplot(x='Designation', y='Values', data=df3, palette=palette, ax=axes[2], width=0.7)
bars4 = sns.barplot(x='Designation', y='Values', data=df4, palette=palette, ax=axes[3], width=0.7)

# Rotate x-axis labels for better readability
for ax in axes:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.setp(ax.get_xticklabels(), fontsize=9)  # Smaller font for x labels

# Set chart titles and labels
titles = [
    'Average Cumulative Combined KPI - performance Achievement % of Cohort LRM',
    'CAP on COMBINED KPI of Top 10% performers in CAP 12 COHORT',
    'CAP on COMBINED KPI of Bottom 10% performers in CAP 12 COHORT',
    'Performance multiple of the CAP 12 cohort'
]
chart_data = [(values1, True), (values2, True), (values3, True), (values4, False)]

# Configure each subplot
for i, (ax, title, (values, is_percentage)) in enumerate(zip(axes, titles, chart_data)):
    # Set axis labels and title
    ax.set_xlabel('Designation', fontsize=12, fontweight='bold')
    
    if is_percentage:
        ax.set_ylabel('Value (%)', fontsize=12, fontweight='bold')
    else:
        ax.set_ylabel('Value', fontsize=12, fontweight='bold')
        
    ax.set_title(title, fontsize=14, fontweight='bold')    # Add value labels to bars
    for j, v in enumerate(values):
        if pd.notna(v):  # Only add text for non-NA values
            # Format the text based on whether it's a percentage or not
            if is_percentage:
                txt = f'{v}%'
            else:
                txt = f'{v:.2f}'
                
            # Make the third graph (Bottom 10%) values more visible
            if i == 2:  # Bottom 10% chart
                # Position the text with background for better visibility
                text_obj = ax.text(j, v + (max([x for x in values if pd.notna(x)]) * 0.05), 
                               txt, ha='center', fontweight='bold', fontsize=14)
                text_obj.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='none', pad=0.5))
            else:
                # Position the text for other charts
                offset = max([x for x in values if pd.notna(x)]) * 0.05
                ax.text(j, v + offset, txt, ha='center', fontweight='bold', fontsize=9)
    
    # Set y-axis limit to make sure the text is visible
    valid_values = [x for x in values if pd.notna(x)]
    if valid_values:
        ax.set_ylim(0, max(valid_values) * 1.2)
    
    # Customize the grid
    sns.despine(left=True, ax=ax)  # Remove the left spine for cleaner look

# Data for the 4 bar charts
Designation = ['Active', 'Inactive', 'Subtotal']

# Values for each of the 4 charts
values1 = [70, 14, 37]
values2 = [187, 184, 186]
values3 = [13, 11, 12]
values4 = [14.52, 17.01, 15.23]

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
titles = ['CAP KPI combined overall', 'CAP KPI Combined Top 10% ', 'CAP KPI Combined Bottom 10%', 'Performance Multiple']
value_sets = [values1, values2, values3, values4]

# Create each subplot
for i, (ax, values, title) in enumerate(zip(axes, value_sets, titles)):
    # Create dataframe for this subplot
    df = pd.DataFrame({'Designation': Designation, 'Values': values})
    
    # Create the bar chart with seaborn
    sns.barplot(x='Designation', y='Values', data=df, palette=palette, ax=ax)
    
    # Add labels and title with improved styling
    ax.set_xlabel('Designation', fontsize=12, fontweight='bold')
    ax.set_ylabel('Values (%)', fontsize=12, fontweight='bold')
    ax.set_title(f'{title} Distribution', fontsize=14, fontweight='bold')
    
    # Add values on top of bars
    for j, v in enumerate(values):
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
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Set seaborn style
sns.set_theme(style="whitegrid")  # Set the seaborn theme
plt.rcParams['font.family'] = 'sans-serif'  # Use a cleaner font

# Data for the bar chart - designation categories and values
categories = [
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

# First column values (Active employees) - full list
values_full = [845, 5031, 795, 284, 72, 8, 0, 0, 0, 0]

# Second column values (Inactive employees) - full list
values2_full = [149, 1070, 236, 86, 26, 3, 0, 0, 0, 0]

# Filter out the categories with zero values in both columns
non_zero_indices = []
for i in range(len(categories)):
    if values_full[i] > 0 or values2_full[i] > 0:
        non_zero_indices.append(i)

# Filter the categories and values
categories = [categories[i] for i in non_zero_indices]
values = [values_full[i] for i in non_zero_indices]
values2 = [values2_full[i] for i in non_zero_indices]

# Calculate the total for each category
values3 = [a + b for a, b in zip(values, values2)]

# Removed duplicate dataframe creation (now created below)

# Create figure and axis with seaborn color palette
fig, axes = plt.subplots(1, 3, figsize=(22, 9))  # Increased figsize for better viewing and bar spacing
palette = sns.color_palette("viridis", len(categories))  # Choose a nice color palette with enough colors for filtered categories

# Create dataframe for the subplots
df1 = pd.DataFrame({'Categories': categories, 'Values': values})
df2 = pd.DataFrame({'Categories': categories, 'Values': values2})
df3 = pd.DataFrame({'Categories': categories, 'Values': values3})

# Create the bar charts with seaborn with improved appearance
bars1 = sns.barplot(x='Categories', y='Values', data=df1, palette=palette, ax=axes[0], width=0.8)
bars2 = sns.barplot(x='Categories', y='Values', data=df2, palette=palette, ax=axes[1], width=0.8)
bars3 = sns.barplot(x='Categories', y='Values', data=df3, palette=palette, ax=axes[2], width=0.8)

# Rotate x-axis labels for better readability
for ax in axes:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

# Add labels and title with improved styling for first subplot (Active employees)
axes[0].set_xlabel('Designation', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Head Count', fontsize=12, fontweight='bold')
axes[0].set_title('CAP LRM cohort', fontsize=16, fontweight='bold')

# Add values on top of bars for first subplot
for i, v in enumerate(values):
    if v > 0:  # Only add text for non-zero values
        axes[0].text(i, v + 150, f"{v:,}", ha='center', fontweight='bold')

# Add labels and title with improved styling for second subplot (Inactive employees)
axes[1].set_xlabel('Designation', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Head Count', fontsize=12, fontweight='bold')
axes[1].set_title('CAP 12 cohort', fontsize=16, fontweight='bold')

# Add values on top of bars for second subplot
for i, v in enumerate(values2):
    if v > 0:  # Only add text for non-zero values
        axes[1].text(i, v + 50, f"{v:,}", ha='center', fontweight='bold')
        
# Add labels and title with improved styling for third subplot (Total employees)
axes[2].set_xlabel('Designation', fontsize=12, fontweight='bold')
axes[2].set_ylabel('Head Count', fontsize=12, fontweight='bold')
axes[2].set_title('Total Employees by Designation', fontsize=16, fontweight='bold')

# Add values on top of bars for third subplot
for i, v in enumerate(values3):
    if v > 0:  # Only add text for non-zero values
        axes[2].text(i, v + 200, f"{v:,}", ha='center', fontweight='bold')

# Customize the grid for all subplots
for ax in axes:
    sns.despine(left=True, ax=ax)  # Remove the left spine for cleaner look

# Add context information
plt.figtext(0.5, 0.01, 'Data as of May 29, 2025', ha='center', fontsize=9, fontstyle='italic')

# Add finishing touches
plt.tight_layout(pad=3.0, rect=[0, 0.03, 1, 0.95])
plt.savefig('Plot1 Head Count.png', dpi=300, bbox_inches='tight')  # Save high-quality image
plt.show()
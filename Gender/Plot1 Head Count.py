import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Set seaborn style
sns.set_theme(style="whitegrid")  # Set the seaborn theme
plt.rcParams['font.family'] = 'sans-serif'  # Use a cleaner font

# Data for the bar chart
categories = ['Male', 'Female']


values = [5406, 1629]
values2 = [1068, 502]


# Removed duplicate dataframe creation (now created below)

# Create figure and axis with seaborn color palette
fig, axes = plt.subplots(2, 1, figsize=(16, 12))
palette = sns.color_palette("muted", 3)  # Choose a nice color palette

# Create dataframe for both subplots
df1 = pd.DataFrame({'Categories': categories, 'Values': values})
df2 = pd.DataFrame({'Categories': categories, 'Values': values2})

# Create the bar charts with seaborn
bars1 = sns.barplot(x='Categories', y='Values', data=df1, palette=palette, ax=axes[0])
bars2 = sns.barplot(x='Categories', y='Values', data=df2, palette=palette, ax=axes[1])

# Add labels and title with improved styling for first subplot
axes[0].set_xlabel('Gender', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Head Count', fontsize=12, fontweight='bold')
axes[0].set_title('CAP LRM cohort', fontsize=16, fontweight='bold')

# Add values on top of bars for first subplot
for i, v in enumerate(values):
    axes[0].text(i, v + 150, str(v), ha='center', fontweight='bold')

# Add labels and title with improved styling for second subplot
axes[1].set_xlabel('Gender', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Head Count', fontsize=12, fontweight='bold')
axes[1].set_title('CAP 12 cohort', fontsize=16, fontweight='bold')

# Add values on top of bars for second subplot
for i, v in enumerate(values2):
    axes[1].text(i, v + 50, str(v), ha='center', fontweight='bold')

# Customize the grid for both subplots
sns.despine(left=True, ax=axes[0])  # Remove the left spine for cleaner look
sns.despine(left=True, ax=axes[1])  # Remove the left spine for cleaner look

# Add context information
plt.figtext(0.5, 0.01, 'Data as of May 29, 2025', ha='center', fontsize=9, fontstyle='italic')

# Add finishing touches
plt.tight_layout(pad=3.0, rect=[0, 0.03, 1, 0.95])
plt.savefig('Plot1 Head Count.png', dpi=300, bbox_inches='tight')  # Save high-quality image
plt.show()
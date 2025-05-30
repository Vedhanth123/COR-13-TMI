import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.patheffects as patheffects

# Set seaborn style
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'

# Original categories
categories_orig = [
    'Sales Development Manager',
    'Business Development Manager',
    'Assistant Sales manager',
    'Sales Manager',
    'Sr. Sales manager',
    'Executive sales manager',
]

# Original data for the two revenue metrics
revenue_metric1_orig = [5.66, 7.06, 8.12, 8.26, 8.83, 7.67]
revenue_metric2_orig = [1.80, 1.64, 2.19, 3.36, 5.95, 9.31]

# Filter out categories where both corresponding revenue metrics are NaN
categories_filtered = []
revenue_metric1_filtered = []
revenue_metric2_filtered = []

for i, cat in enumerate(categories_orig):
    both_metrics_nan = (pd.isna(revenue_metric1_orig[i]) and
                        pd.isna(revenue_metric2_orig[i]))
    if not both_metrics_nan:
        categories_filtered.append(cat)
        revenue_metric1_filtered.append(revenue_metric1_orig[i])
        revenue_metric2_filtered.append(revenue_metric2_orig[i])

# Handle case where all data might be filtered out
if not categories_filtered:
    print("No data to plot after filtering categories with all NaN revenue metrics.")
    plt.figure(figsize=(10, 6))
    plt.text(0.5, 0.5, "No data to display after filtering.", ha='center', va='center', fontsize=16)
    plt.savefig('designation_revenue_indicators.png', dpi=300, bbox_inches='tight')
    plt.show()
    exit()

# Create figure with 1 row and 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(22, 9)) # Adjusted for two plots, similar to Plot1 Head Count
palette = sns.color_palette("viridis", len(categories_filtered))

# Data for subplots with new titles as requested including units
datasets = [revenue_metric1_filtered, revenue_metric2_filtered]
subplot_titles = [
    'Time to make the first sale CAP LRM cohort (Months)',
    'CAR2CATPO ratio UP TO Residency month 6 for CAP LRM cohort (Ratio)'
]

for i, (ax, data_values, title_text) in enumerate(zip(axes, datasets, subplot_titles)):
    df = pd.DataFrame({'Categories': categories_filtered, 'Values': data_values})
    sns.barplot(x='Categories', y='Values', data=df, palette=palette, ax=ax, width=0.8)
    
    ax.set_xlabel('Designation', fontsize=12, fontweight='bold')
    # Set appropriate y-axis label based on the chart
    if i == 0:  # First chart (Time)
        ax.set_ylabel('Time (Months)', fontsize=12, fontweight='bold')
    else:  # Second chart (Ratio)
        ax.set_ylabel('Ratio', fontsize=12, fontweight='bold')
    ax.set_title(title_text, fontsize=16, fontweight='bold')

    # Calculate max value for current subplot for y_lim and text offset (ignoring NaNs)
    valid_values_for_subplot = [val for val in data_values if pd.notna(val)]
    max_val_for_subplot = max(valid_values_for_subplot) if valid_values_for_subplot else 0    # Add values on top of bars (without currency symbols)
    for bar_idx, bar_val in enumerate(data_values):
        if pd.isna(bar_val):
            continue

        text_content = f'{bar_val:.2f}'
        y_offset_text = max_val_for_subplot * 0.03 if max_val_for_subplot > 0 else 0.5
        text_y_val = bar_val + y_offset_text
        if bar_val == 0: # Ensure text for 0 value is visible above the baseline
             text_y_val = y_offset_text
        
        ax.text(bar_idx, text_y_val, text_content, ha='center', va='bottom', fontweight='bold', fontsize=9)

    # Set y-axis limit
    ax.set_ylim(0, max_val_for_subplot * 1.25 if max_val_for_subplot > 0 else 10)
    
    # Rotate x-axis labels
    ax.set_xticklabels(categories_filtered, rotation=45, horizontalalignment='right', fontsize=10)
    sns.despine(left=True, ax=ax)

# Add eye-catching common title for the figure
fig_title_obj = fig.suptitle('Revenue Indicators by Designation', fontsize=24, fontweight='bold', y=0.98,
                           color='darkblue', alpha=0.8)
fig_title_obj.set_path_effects([patheffects.withStroke(linewidth=3, foreground='skyblue')])

# Add context information
plt.figtext(0.5, 0.005, 'Data as of May 29, 2025. Categories with N/A for all displayed metrics are excluded.', ha='center', fontsize=10, fontstyle='italic')

# Add finishing touches
plt.tight_layout(pad=3.0, rect=[0, 0.03, 1, 0.95])
plt.savefig('Plot4 Revenue Indicators.png', dpi=300, bbox_inches='tight')  # Save high-quality image
plt.show()
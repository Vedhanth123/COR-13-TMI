import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.patheffects as patheffects
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm as cm
from matplotlib.patches import Rectangle
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

# Set seaborn style with enhanced configuration
sns.set_theme(style="whitegrid", context="talk")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['figure.facecolor'] = '#f9f9f9'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.6

# Original categories - job designations
categories_orig = [
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

headcount_orig = [845, 5031, 795, 284, 72, 8, 0, 0, 0, 0]

# Values for each of the metrics (from the provided table)
tenure_orig = [6.66, 7.01, 8.46, 8.24, 9.54, 11.25, 0, 0, 0, 0]
engagement_orig = [9.25, 10.10, 8.80, 10.50, 19.00, 5.00, 0, 0, 0, 0]
attrition_risk_orig = [41, 38, 39, 34, 31, 25, 0, 0, 0, 0]  # Already as percentages
retention_rate_orig = [68, 65, 60, 58, 58, 40, 0, 0, 0, 0]  # Already as percentages

# Filter out categories with zero headcount or where all metrics are NaN
non_empty_indices = []
for i in range(len(categories_orig)):
    # Check if there's at least one valid value in the metrics and headcount > 0
    has_data = (pd.notna(tenure_orig[i]) or pd.notna(engagement_orig[i]) or 
               pd.notna(attrition_risk_orig[i]) or pd.notna(retention_rate_orig[i]))
    if has_data:
        non_empty_indices.append(i)

# Filter all the arrays to include only non-empty entries
categories = [categories_orig[i] for i in non_empty_indices]
headcount = [headcount_orig[i] for i in non_empty_indices]
tenure = [tenure_orig[i] for i in non_empty_indices]
engagement = [engagement_orig[i] for i in non_empty_indices]
attrition_risk = [attrition_risk_orig[i] for i in non_empty_indices]
retention_rate = [retention_rate_orig[i] for i in non_empty_indices]

# Create a more sophisticated layout with GridSpec
plt.figure(figsize=(24, 12))
gs = gridspec.GridSpec(2, 4, height_ratios=[4, 1], width_ratios=[1, 1, 1, 1])

# Create a DataFrame with all metrics for easier handling
data = pd.DataFrame({
    'Designation': categories,
    'Headcount': headcount,
    'Tenure': tenure,
    'Engagement': engagement,
    'Attrition Risk': attrition_risk,
    'Retention Rate': retention_rate
})

# Define color maps for each metric based on business logic
# For tenure: higher is better (green)
# For engagement: higher is better (green)
# For attrition risk: lower is better (green for low values)
# For retention rate: higher is better (green)

# Function to calculate color based on metric value and thresholds
def get_colors(values, metric_name):
    normalized_values = []
    colors = []
    
    if metric_name == 'Tenure':
        cmap = cm.get_cmap('RdYlGn')  # Red-Yellow-Green
        # Normalize to 0-1 range based on min-max values
        min_good = 0
        max_good = 12  # Consider 12 months as good tenure
        for v in values:
            if pd.isna(v):
                normalized_values.append(0.5)  # Default to middle value for NaN
                colors.append('lightgray')
            else:
                norm_val = min(v / max_good, 1.0)  # Scale to maximum of 1.0
                normalized_values.append(norm_val)
                colors.append(cmap(norm_val))
    
    elif metric_name == 'Engagement':
        cmap = cm.get_cmap('RdYlGn')
        min_good = 0
        max_good = 20  # Assuming 20 is max engagement
        for v in values:
            if pd.isna(v):
                normalized_values.append(0.5)
                colors.append('lightgray')
            else:
                norm_val = min(v / max_good, 1.0)
                normalized_values.append(norm_val)
                colors.append(cmap(norm_val))
    
    elif metric_name == 'Attrition Risk':
        cmap = cm.get_cmap('RdYlGn_r')  # Reversed so red is high risk
        for v in values:
            if pd.isna(v):
                normalized_values.append(0.5)
                colors.append('lightgray')
            else:
                norm_val = v / 100  # Already in percentage
                normalized_values.append(norm_val)
                colors.append(cmap(norm_val))
    
    elif metric_name == 'Retention Rate':
        cmap = cm.get_cmap('RdYlGn')
        for v in values:
            if pd.isna(v):
                normalized_values.append(0.5)
                colors.append('lightgray')
            else:
                norm_val = v / 100  # Already in percentage
                normalized_values.append(norm_val)
                colors.append(cmap(norm_val))
    
    return colors, normalized_values

# Create visualizations for main metrics
metrics = ['Tenure', 'Engagement', 'Attrition Risk', 'Retention Rate']
titles = ['Average Tenure (Months)', 'Engagement Score', 'Attrition Risk (%)', 'Retention Rate (%)']
y_labels = ['Months', 'Score', 'Percentage (%)', 'Percentage (%)']
axes = []

# Removed trend arrow indicators as requested

# Create each main metric chart
for i, (metric, title, y_label) in enumerate(zip(metrics, titles, y_labels)):
    ax = plt.subplot(gs[0, i])
    axes.append(ax)
    
    # Get color map for this metric
    bar_colors, _ = get_colors(data[metric].tolist(), metric)
    
    # Use custom colored bars instead of palette
    bars = ax.bar(range(len(categories)), data[metric].tolist(), color=bar_colors, width=0.7)
    
    # Add value labels and headcount
    valid_values = [v for v in data[metric] if pd.notna(v)]
    max_value = max(valid_values) if valid_values else 0
    
    for j, (cat, val, hc) in enumerate(zip(categories, data[metric], data['Headcount'])):
        if pd.notna(val):
            # Format the value based on the metric
            if metric in ['Attrition Risk', 'Retention Rate']:
                txt = f'{int(val)}%'
            else:
                txt = f'{val:.1f}'
                  # Position the label above the bar
            y_pos = val + (max_value * 0.03)
            ax.text(j, y_pos, txt, ha='center', fontweight='bold', fontsize=11)
        
        # Add headcount as a smaller label under the bar
        if hc > 0:
            ax.text(j, -max_value * 0.05, f'n={hc:,}', ha='center', fontsize=9, alpha=0.8)
    
    # Customize the axis
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels([c.replace(' ', '\n') for c in categories], rotation=0, fontsize=10)
    ax.set_title(title, fontsize=16, fontweight='bold', pad=15)
    ax.set_ylabel(y_label, fontsize=12, fontweight='bold')
    ax.set_ylim(0, max_value * 1.15)
    
    # Add a legend explaining the color coding
    if i == 0:  # Only for the first plot
        red_patch = Rectangle((0, 0), 1, 1, fc='#d62728', alpha=0.7)
        yellow_patch = Rectangle((0, 0), 1, 1, fc='#ffd700', alpha=0.7)
        green_patch = Rectangle((0, 0), 1, 1, fc='#2ca02c', alpha=0.7)
        ax.legend([green_patch, yellow_patch, red_patch], 
                 ['Good', 'Average', 'Needs Attention'], 
                 loc='upper right', frameon=True, fontsize=10)
    
    # Add grid lines
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Remove top and right spines
    sns.despine(ax=ax)

# Create correlation heatmap in the bottom row
ax_heatmap = plt.subplot(gs[1, 1:3])
correlation_metrics = ['Tenure', 'Engagement', 'Attrition Risk', 'Retention Rate']
corr_data = data[correlation_metrics].corr()

# Create heatmap with custom colormap
mask = np.triu(np.ones_like(corr_data, dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr_data, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".2f", ax=ax_heatmap)
ax_heatmap.set_title('Metric Correlation Analysis', fontsize=14, fontweight='bold', pad=15)

# Create KPI summary in bottom left
ax_kpi = plt.subplot(gs[1, 0])
ax_kpi.axis('off')  # Hide axes

# Calculate average values for KPIs
avg_tenure = np.nanmean(data['Tenure'])
avg_engagement = np.nanmean(data['Engagement'])
avg_attrition = np.nanmean(data['Attrition Risk'])
avg_retention = np.nanmean(data['Retention Rate'])
total_headcount = sum(data['Headcount'])

# Add KPI text
kpi_text = (
    f"KPI SUMMARY\n\n"
    f"Total Headcount: {total_headcount:,}\n"
    f"Avg. Tenure: {avg_tenure:.2f} months\n"
    f"Avg. Engagement: {avg_engagement:.2f}\n"
    f"Avg. Attrition Risk: {avg_attrition:.1f}%\n"
    f"Avg. Retention Rate: {avg_retention:.1f}%\n"
)
ax_kpi.text(0.1, 0.5, kpi_text, va='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.5", fc='#f0f0f0', ec='gray', alpha=0.8))

# Add recommendations based on the data
ax_rec = plt.subplot(gs[1, 3])
ax_rec.axis('off')  # Hide axes

# Create recommendation text based on data analysis
# This would be more sophisticated in a real application
rec_text = "RECOMMENDATIONS\n\n"

# Find designation with highest attrition risk
high_attrition = data.loc[data['Attrition Risk'].idxmax()]
if pd.notna(high_attrition['Attrition Risk']):
    rec_text += f"• Focus on {high_attrition['Designation']} role which has {high_attrition['Attrition Risk']}% attrition risk\n"

# Find designation with lowest engagement
low_engagement = data.loc[data['Engagement'].idxmin()]
if pd.notna(low_engagement['Engagement']):
    rec_text += f"• Improve engagement for {low_engagement['Designation']}\n"

# General recommendation
rec_text += "• Develop retention strategies for roles with >35% attrition risk"

ax_rec.text(0.1, 0.5, rec_text, va='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.5", fc='#f0f0f0', ec='gray', alpha=0.8))

# Add eye-catching main title with enhanced styling
plt.suptitle('Attrition & Retention Dashboard by Designation', 
             fontsize=28, fontweight='bold', y=0.98, color='#2c3e50',
             ha='center', va='top')

# Add styled subtitle
subtitle = plt.figtext(0.5, 0.93, 
                     'Analysis of Key People Metrics Across Job Roles', 
                     fontsize=16, fontstyle='italic', ha='center', 
                     color='#7f8c8d')

# Add borders around the entire figure for a finished look
plt.gcf().patch.set_edgecolor('gray')
plt.gcf().patch.set_linewidth(2)

# Add context information and timestamp
plt.figtext(0.5, 0.01, 'Data as of May 29, 2025 | Confidential - HR Analytics Team', 
          ha='center', fontsize=10, fontstyle='italic', color='#555')

# Adjust layout
plt.tight_layout(rect=[0.01, 0.02, 0.99, 0.91], h_pad=3.0, w_pad=2.0)

plt.savefig('Plot5 Attrition Indicators.png', dpi=300, bbox_inches='tight')  # Save high-quality image
plt.show()
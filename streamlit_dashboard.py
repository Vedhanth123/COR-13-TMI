import streamlit as st
import os
from pathlib import Path

# Configuration - Easily customizable
CONFIG = {
    "filters": [
        "Age group",
        "Designation", 
        "Gender",
        "Highest Educational Qualification",
        "Prior Experience",
        "Resume Source",
        "Work Status"
    ],
    "metrics": [
        "Plot1 Head Count",
        "Plot2 Performance Indicators KPI 1",
        "Plot3 Performance Indicators KPI Combined", 
        "Plot4 Revenue Indicators",
        "Plot5 Attrition Indicators"
    ],
    "graphs_folder": ".",  # Current folder (since you're running from VER4-COR-13)
    "image_extension": ".png"
}

def get_image_path(filter_name, metric_name):
    """Generate the file path for a specific filter-metric combination"""
    return os.path.join(CONFIG["graphs_folder"], filter_name, metric_name + CONFIG["image_extension"])

def check_image_exists(image_path):
    """Check if the image file exists"""
    return os.path.exists(image_path)

def main():
    st.set_page_config(
        page_title="Data Visualization Dashboard",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 Data Visualization Dashboard")
    st.markdown("---")
    
    # Sidebar for filter selection
    st.sidebar.header("🔍 Select Filter")
    selected_filter = st.sidebar.selectbox(
        "Choose a filter:",
        CONFIG["filters"],
        index=0
    )
    
    # Main content area
    if selected_filter:
        st.header(f"📈 {selected_filter} - Metrics")
        st.markdown(f"Select a metric to view the visualization for **{selected_filter}**")
        
        # Create columns for metric buttons
        cols = st.columns(len(CONFIG["metrics"]))
        
        # Track which metric is selected
        if 'selected_metric' not in st.session_state:
            st.session_state.selected_metric = None
        if 'current_filter' not in st.session_state:
            st.session_state.current_filter = None
            
        # Reset metric selection if filter changes
        if st.session_state.current_filter != selected_filter:
            st.session_state.selected_metric = None
            st.session_state.current_filter = selected_filter
        
        # Create metric selection buttons
        for i, metric in enumerate(CONFIG["metrics"]):
            with cols[i]:
                if st.button(
                    f"📊 {metric}",
                    key=f"btn_{selected_filter}_{metric}",
                    use_container_width=True
                ):
                    st.session_state.selected_metric = metric
        
        st.markdown("---")
        
        # Display selected metric visualization
        if st.session_state.selected_metric:
            metric = st.session_state.selected_metric
            image_path = get_image_path(selected_filter, metric)
            
            st.subheader(f"📊 {selected_filter} - {metric}")
            
            if check_image_exists(image_path):
                # Display the image
                st.image(
                    image_path,
                    caption=f"{selected_filter} - {metric}",
                    use_column_width=True
                )
                
                # Additional info
                st.info(f"📁 Image path: `{image_path}`")
                
            else:
                st.error(f"❌ Image not found: `{image_path}`")
                st.markdown("**Please check:**")
                st.markdown("- File path is correct")
                st.markdown("- Image file exists in the specified location")
                st.markdown("- File extension matches the configuration")
        
        else:
            # Show instruction when no metric is selected
            st.info("👆 Click on any metric button above to view the visualization")
    
    # Footer with instructions
    st.markdown("---")
    with st.expander("ℹ️ Setup Instructions"):
        st.markdown("""
        **Folder Structure Expected:**
        ```
        VER4-COR-13/
        ├── Age group/
        │   ├── Plot1 Head Count.png
        │   ├── Plot2 Performance Indicators KPI 1.png
        │   ├── Plot3 Performance Indicators KPI Combined.png
        │   ├── Plot4 Revenue Indicators.png
        │   └── Plot5 Attrition Indicators.png
        ├── Designation/
        │   ├── Plot1 Head Count.png
        │   ├── Plot2 Performance Indicators KPI 1.png
        │   ├── Plot3 Performance Indicators KPI Combined.png
        │   ├── Plot4 Revenue Indicators.png
        │   └── Plot5 Attrition Indicators.png
        ├── Gender/
        │   └── ... (same 5 PNG files)
        └── ... (other filter folders with same 5 PNG files)
        ```
        
        **To Add More Filters:**
        1. Add your remaining filter folder names to `CONFIG["filters"]` list
        2. Each folder should contain the same 5 PNG files with exact names as specified
        3. All folders will automatically show the same 5 metric options
        """)

if __name__ == "__main__":
    main()
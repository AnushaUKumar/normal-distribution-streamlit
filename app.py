import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Set Streamlit page config
st.set_page_config(page_title="Normal Distribution Visualizer", layout="wide")

# Sidebar controls
st.sidebar.header("Adjust Parameters")
mean = st.sidebar.slider("Mean", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
std_dev = st.sidebar.slider("Standard Deviation", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

# Histogram options
show_pdf = st.sidebar.checkbox("Show PDF Curve", value=True)
show_hist = st.sidebar.checkbox("Show Histogram", value=True)
bin_size = st.sidebar.slider("Bin Size", min_value=0.1, max_value=2.0, value=0.5, step=0.1)

# Generate data
fixed_mean, fixed_std_dev = 0, 1  # Stagnant reference distribution
num_samples = 10000  
fixed_data = np.random.normal(fixed_mean, fixed_std_dev, num_samples)
dynamic_data = np.random.normal(mean, std_dev, num_samples)

# Generate x values for PDF curves
x = np.linspace(-10, 10, 1000)
fixed_pdf = stats.norm.pdf(x, fixed_mean, fixed_std_dev)
dynamic_pdf = stats.norm.pdf(x, mean, std_dev)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor("#202225")
ax.set_facecolor("#2c2f33")  

# Histogram
if show_hist:
    ax.hist(fixed_data, bins=np.arange(-10, 10, bin_size), density=True, alpha=0.7, 
            color="#1f77b4", edgecolor="none", label="Fixed Histogram") 
    ax.hist(dynamic_data, bins=np.arange(-10, 10, bin_size), density=True, alpha=0.7, 
            color="#ff7f0e", edgecolor="none", label="Dynamic Histogram")  

# PDF curves
if show_pdf:
    ax.plot(x, fixed_pdf, color="#1f77b4", linewidth=2.5, linestyle="-", label="Fixed Normal PDF")
    ax.plot(x, dynamic_pdf, color="#ff7f0e", linewidth=2.5, linestyle="-", label="Dynamic Normal PDF") 

# Labels
ax.set_title("Interactive Normal Distribution Visualization", fontsize=14, color="white")
ax.set_xlabel("", fontsize=12, color="white")  
ax.set_ylabel("", fontsize=12, color="white") 

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.tick_params(axis="x", colors="white", labelsize=10, length=0)  
ax.tick_params(axis="y", colors="white", labelsize=10, length=0) 

# Remove grid for a clean look
ax.grid(False)


legend = ax.legend(
    loc="upper left",
    bbox_to_anchor=(1.02, 1),
    fontsize=8,
    frameon=False,
    labelspacing=0.3,
    handlelength=1.5,
    facecolor="#2c2f33",  # Dark gray background for better visibility
    edgecolor="none"  # No border
)

# ✅ Set legend text color to white
plt.setp(legend.get_texts(), color="white")



# Show the plot in Streamlit
st.pyplot(fig)

# Explanation
st.markdown("""
### **How It Works:**
- The **blue histogram** and **PDF** represent the **fixed normal distribution** (**μ=0, σ=1**).
- The **orange histogram** and **PDF** represent the **dynamic normal distribution** based on user inputs.
- Adjusting **Mean (μ)** shifts the orange histogram left/right.
- Adjusting **Standard Deviation (σ)** changes the spread of the orange distribution.
""")

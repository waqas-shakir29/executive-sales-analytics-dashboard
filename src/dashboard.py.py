# Executive Sales Analytics Dashboard

This notebook demonstrates the development of a business analytics dashboard 
using Python and Matplotlib. The goal is to visualize multiple business 
metrics in a single professional layout.

Cell 2: Import Libraries
import matplotlib.pyplot as plt
import numpy as np      #for numerical operations and random data generation
from matplotlib.gridspec import GridSpec   #GridSpec helps create complex dashboard layouts

Cell 3:  Generate Sample Business Data    # Sample Business Dataset

# Monthly sales data for trend visualization
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
sales = [120,150,170,160,200,210,230,250]

# Sales distribution across product categories
categories = ["Electronics","Clothing","Home","Sports"]
category_sales = [320,210,180,150]

# Sales share by region
regions = ["North","South","East","West"]
region_share = [35,25,20,20]

# Generate random customer ages using normal distribution
customer_age = np.random.normal(30,7,260)

# Generate random customer ages using normal distribution
sales_scatter = np.random.randint(60,300,90)

# Profit is calculated as a percentage of sales
profit_scatter = sales_scatter * np.random.uniform(0.25,0.45,90) Cell 4 — Dashboard Theme Configuration    # THEME & COLOR CONFIGURATION


# Define color palette used in dashboard

BG = "#0F1115"         #dashboard background                   
CARD = "#1A1D23"       #chart background   
PRIMARY = "#E74C3C"    #main red color
ACCENT = "#F1948A"     #secondary light red
GRID = "#2A2D34"       #grid color
TEXT= "White"

         # Create Dashboard Layout/ Dashboard Initialization

#create main dashboard figure

fig = plt.figure(figsize=(18,12)) #create main figue canvas
fig.patch.set_facecolor(BG)   # Set global background

# Create a 4x2 Grid: Row 0 is for KPIs, Rows 1-3 for Charts
gs = GridSpec(4,2, figure=fig, height_ratios=[0.4, 1.2, 1.2, 1.2])   # Create grid layout (4 rows, 2 columns)


 # Styling helper to apply card-like appearance to each axis
def card(ax, title=""):
    ax.set_facecolor(CARD)    # Set Chart background color
    ax.grid(color=GRID, alpha=0.3, linestyle="--")       # Enable grid for better readibility
    
    ax.tick_params(colors=TEXT, labelsize= 9)

    for spine in ax.spines.values():     #Remove Border Lines around Charts
        spine.set_visible(False)       # Clean, borderless look
    if title: 
        ax.set_title(title, color=TEXT, fontweight="bold", pad=15)


                # -------------------------- TOP KPI CARDS (Summary Metrics) ---------------------------
kpi_data = [
    (f"${sum(sales)}K", "TOTAL REVENUE"),
    (f"{int(np.mean(profit_scatter/sales_scatter*100))}%", "AVG MARGIN"),
    (f"{len(customer_age)}", "TOTAL CUSTOMERS")
]

for i, (val, label) in enumerate(kpi_data):
    # Position cards manually at the very top
    ax_kpi = fig.add_axes([0.15 + i*0.28, 0.88, 0.2, 0.06])
    ax_kpi.set_facecolor(CARD)
    ax_kpi.text(0.5, 0.7, val, color=PRIMARY, fontsize=24, fontweight="bold", ha='center', va='center')
    ax_kpi.text(0.5, 0.2, label, color=TEXT, fontsize=10, ha='center', va='center')
    ax_kpi.set_xticks([]); ax_kpi.set_yticks([])       # Hide axes for KPIs
    for s in ax_kpi.spines.values(): s.set_visible(False)



            #---------------------- Monthly Sales Trend (Line Chart) ---------------------


#  Create subplot in first row first column
ax1 = fig.add_subplot(gs[1,0]); card(ax1, "Monthly Sales Trend")

# Plot monthly sales line chart
ax1.plot(months, sales, color=PRIMARY, lw=4, marker="o", markersize=8)
# Fill area under line for visual effect
ax1.fill_between(months, sales, color=PRIMARY, alpha=0.2)

ax1.set_xlabel("Month", color= TEXT, fontsize=10)
ax1.set_ylabel("Revenue ($K)", color= TEXT, fontsize=10)  # Y-axis Label


            #---------------------- Category Performance (Bar Chart) ---------------------

        

ax2 = fig.add_subplot(gs[1,1]); card(ax2, "Category Performance")     #create subplot

# Apply bar chart
bars = ax2.bar(categories,category_sales,color=PRIMARY, width=0.6)
ax2.bar_label(bars, padding=3, color=TEXT)

ax2.set_xlabel("Product Category", color=TEXT, fontsize=10)
ax2.set_ylabel("Sales ($K)", color=TEXT, fontsize=10)


            #---------------------- Regional Sales Share (Pie Chart) ---------------------



ax3 = fig.add_subplot(gs[2,0]); card(ax3, "Regional Sales Share")

wedges, texts, autotexts= ax3.pie(
    region_share,
    labels=regions,
    autopct="%1.0f%%",
    startangle=90,
    colors=[PRIMARY,ACCENT,"#C0392B","#5D6D7E"],
    textprops={"color":TEXT}
)

# Ensure circle shape
ax3.axis("equal")

for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontsize(11)
    autotext.set_weight("bold")



            #---------------------- Customer Age Distribution (Histogram) ---------------------



# Create subplot
ax4 = fig.add_subplot(gs[2,1]); card(ax4, "Customer Age Distribution")
ax4.hist(customer_age, bins=15, color=PRIMARY, rwidth=0.85) # Added rwidth for gap

ax4.set_xlabel("Age", color=TEXT, fontsize=10)
ax4.set_ylabel("Number of Customers", color=TEXT, fontsize=10)



            #---------------------- Sales vs Profit Analysis(Scatter Plot)-----------------------



ax5 = fig.add_subplot(gs[3,:]); card(ax5, "Sales Vs Profit Relationship")  # Create subplot spanning full width

# Scatter plot showing relationship between sales and profit
scatter=ax5.scatter(
    sales_scatter,
    profit_scatter,
    c=profit_scatter,
    cmap="Reds",
    edgecolors=BG
)

# Add colorbar to indicate profit intensity
cbar= fig.colorbar(scatter, ax=ax5, aspect=40)    
cbar.ax.yaxis.set_tick_params(color=TEXT); plt.setp(cbar.ax.get_yticklabels(), color=TEXT)

# Trend Line Calculation (Regression)
m, b = np.polyfit(sales_scatter, profit_scatter, 1)
ax5.plot(sales_scatter, m*sales_scatter + b, color=ACCENT, ls="--", alpha=0.6)

ax5.set_xlabel("Sales ($K)", color=TEXT)
ax5.set_ylabel("Profit ($K)", color=TEXT)

            # Dashboard Main Title

fig.suptitle("EXECUTIVE SALES ANALYTICS", fontsize=26, color=PRIMARY, fontweight="bold", y=0.98)
# Adjust margins to ensure labels don't get cut off
plt.subplots_adjust(hspace=0.7, wspace=0.3, top=0.78, bottom=0.15, left=0.1, right=0.9)

            # Save Dashboard Image

# Save high resolution dashboard image
plt.savefig("executive_sales_dashboard.png", dpi=300, facecolor=BG)
plt.show()  # Display dashboard 
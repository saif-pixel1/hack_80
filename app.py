import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
import numpy as np
import random

# ==========================================
# 1. CONFIG & STYLE
# ==========================================
st.set_page_config(page_title="Dream Room Visualizer", page_icon="🏠", layout="wide")

# Custom CSS for nicer UI
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    h1 {
        color: #2e4057;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 10px 24px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. STYLE DEFINITIONS
# ==========================================
STYLES = {
    "Minimalist": {
        "colors": ["#F5F5F5", "#D3D3D3", "#A9A9A9", "#2F4F4F", "#FFFFFF"],
        "furniture": ["Bed", "Desk", "Chair"],
        "bg": "#ffffff",
        "text": "black"
    },
    "Cyberpunk": {
        "colors": ["#0b0c10", "#1f2833", "#66FCF1", "#45A29E", "#C5C6C7"],
        "furniture": ["Server Rack", "Neon Bed", "Hologram Table"],
        "bg": "#0b0c10",
        "text": "#66FCF1"
    },
    "Boho": {
        "colors": ["#8B4513", "#D2B48C", "#556B2F", "#FFD700", "#F5DEB3"],
        "furniture": ["Floor Mat", "Cushions", "Plant"],
        "bg": "#F5DEB3",
        "text": "#5c4033"
    },
    "Luxury": {
        "colors": ["#000000", "#FFD700", "#FFFFFF", "#36454F", "#800000"],
        "furniture": ["King Bed", "Dresser", "Chandelier"],
        "bg": "#1a1a1a",
        "text": "#FFD700"
    },
    "Cozy": {
        "colors": ["#8B4513", "#DEB887", "#556B2F", "#A0522D", "#FFE4C4"],
        "furniture": ["Fireplace", "Rug", "Bookshelf"],
        "bg": "#FFE4C4",
        "text": "#5c3317"
    }
}

# ==========================================
# 3. VISUALIZATION ENGINE
# ==========================================

def draw_room(width, length, style_name):
    """
    Draws a procedural 2D room using Matplotlib
    """
    style = STYLES[style_name]
    
    # Setup Figure
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Set Background Color (Floor)
    ax.set_facecolor(style['bg'])
    
    # Draw Walls
    wall_thickness = 2
    rect = patches.Rectangle((0, 0), width, length, linewidth=wall_thickness, 
                             edgecolor='#333', facecolor='none')
    ax.add_patch(rect)
    
    # --- Procedural Furniture Placement ---
    
    # 1. Bed (Always center-ish or against wall)
    if "Cyberpunk" in style_name:
        # Futuristic glowing bed
        bed = patches.Rectangle((width*0.2, length*0.3), width*0.4, length*0.5, 
                                 linewidth=2, edgecolor=style['colors'][2], 
                                 facecolor='#111', linestyle='-')
        ax.add_patch(bed)
        # Neon glow effect
        ax.text(width*0.4, length*0.55, "NEON BED", ha='center', va='center', 
                color=style['colors'][2], fontsize=10, fontweight='bold')
                
    elif "Boho" in style_name:
        # Circular Rug
        rug = patches.Circle((width/2, length/2), width*0.35, color=style['colors'][1], alpha=0.8)
        ax.add_patch(rug)
        # Floor cushions
        for i in range(3):
            circle = patches.Circle((width/2 + random.randint(-20,20), length/2 + random.randint(-20,20)), 
                                    width*0.08, color=style['colors'][3])
            ax.add_patch(circle)
            
    elif "Luxury" in style_name:
        # Grand Bed
        bed = patches.Rectangle((width*0.1, length*0.1), width*0.5, length*0.6, 
                                 linewidth=3, edgecolor=style['colors'][1], 
                                 facecolor='#222')
        ax.add_patch(bed)
        # Chandelier (Circle center)
        chandelier = patches.Circle((width*0.35, length*0.4), 0.5, color=style['colors'][1])
        ax.add_patch(chandelier)
        ax.text(width*0.35, length*0.4, "💎", ha='center', va='center', fontsize=15)
        
    else:
        # Standard Bed
        bed = patches.Rectangle((width*0.1, length*0.1), width*0.4, length*0.5, 
                                 linewidth=1, edgecolor='black', facecolor='#ddd')
        ax.add_patch(bed)
    
    # 2. Decor / Windows (Style specific)
    if "Minimalist" in style_name:
        # Just a desk
        desk = patches.Rectangle((width*0.6, length*0.6), width*0.3, length*0.2, 
                                 linewidth=1, edgecolor='black', facecolor='#fff')
        ax.add_patch(desk)
        
    elif "Cozy" in style_name:
        # Fireplace
        fp = patches.Rectangle((width*0.4, 0), width*0.2, length*0.15, 
                               facecolor='#800000', edgecolor='black')
        ax.add_patch(fp)
        ax.text(width*0.5, length*0.05, "🔥", ha='center', va='center', fontsize=20)

    # 3. Add "Decor" dots randomly based on style
    # Represents: lamps, plants, lights
    for _ in range(5):
        rx = random.uniform(0.1, width-0.5)
        ry = random.uniform(0.1, length-0.5)
        dot = patches.Circle((rx, ry), 0.3, color=random.choice(style['colors']))
        ax.add_patch(dot)

    # --- Axis Settings ---
    ax.set_xlim(-1, width + 1)
    ax.set_ylim(-1, length + 1)
    ax.set_aspect('equal')
    ax.axis('off') # Hide axis numbers
    
    # Grid lines for measurement
    ax.set_xticks(np.arange(0, width+1, 2))
    ax.set_yticks(np.arange(0, length+1, 2))
    ax.tick_params(colors='gray', labelsize=8)
    
    # Title
    ax.set_title(f"2D Blueprint: {style_name} Style ({width}' x {length}')", 
                 fontsize=16, color=style['text'], pad=20, fontweight='bold')

    return fig

def generate_palette(style_name):
    """Generates a color palette visualization"""
    style = STYLES[style_name]
    colors = style['colors']
    
    fig, ax = plt.subplots(figsize=(6, 1))
    for i, color in enumerate(colors):
        ax.add_patch(patches.Rectangle((i, 0), 1, 1, facecolor=color))
    
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title(f"Color Palette: {style_name}", loc='left', fontsize=10)
    
    return fig

# ==========================================
# 4. UI LAYOUT
# ==========================================

st.title("🏠 Dream Room Visualizer")
st.markdown("Design your room **offline**. No AI, no API keys, just pure math and code.")

# Sidebar Controls
with st.sidebar:
    st.header("🛠️ Room Dimensions")
    width = st.slider("Width (ft)", 8, 30, 12)
    length = st.slider("Length (ft)", 8, 30, 14)
    
    st.header("🎨 Style")
    style = st.selectbox("Choose Aesthetic", list(STYLES.keys()))
    
    st.markdown("---")
    st.info(f"**Size:** {width}' x {length}' \n\n**Style:** {style}")

# Main Display
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("📐 Room Blueprint")
    fig = draw_room(width, length, style)
    st.pyplot(fig)

with col2:
    st.subheader("🎨 Color Palette")
    palette_fig = generate_palette(style)
    st.pyplot(palette_fig)
    
    st.markdown("### 💡 Decor Ideas")
    if style == "Cyberpunk":
        st.write("- LED Strip lighting\n- Glass coffee table\n- Mechanical Keyboard")
    elif style == "Boho":
        st.write("- Macrame hangings\n- Floor pillows\n- Potted Monstera")
    elif style == "Luxury":
        st.write("- Velvet curtains\n- Gold mirrors\n- Marble flooring")
    else:
        st.write("- Throw blankets\n- Area rugs\n- Wall art")

# Stats
st.markdown("---")
col_a, col_b, col_c = st.columns(3)
col_a.metric("Room Area", f"{width * length} sq ft")
col_b.metric("Estimated Cost", f"${(width * length) * 50 + random.randint(500, 2000)}", "Rough Estimate")
col_c.metric("Style Score", f"{random.randint(8, 10)}/10")
🏠 Dream Room Visualizer
An AI-powered interior design app built with Streamlit and Claude. Input your room dimensions and a style to get a detailed design concept — color palettes, furniture picks, materials, and pro tips.

✨ Features
12 built-in styles (Cyberpunk, Boho, Japandi, Art Deco, Dark Academia, Maximalist, and more)
Custom style input
Room type, dimensions, lighting mood, and camera angle controls
AI-generated color palette with hex swatches
Furniture list, materials, style elements, and designer tips
Dark luxury UI with Google Fonts and animated layout
🚀 Quick Start
1. Clone / Download
Place dream_room_visualizer.py, requirements.txt in the same folder.

2. Install dependencies
pip install -r requirements.txt
3. Set your Anthropic API key
export ANTHROPIC_API_KEY=sk-ant-...
Or on Windows:

set ANTHROPIC_API_KEY=sk-ant-...
4. Run the app
streamlit run dream_room_visualizer.py
Open http://localhost:8501 in your browser.

🗂️ Project Structure
dream-room-visualizer/
├── dream_room_visualizer.py   # Main Streamlit app
├── requirements.txt           # Python dependencies
└── README.md                  # This file
🛠️ Tech Stack
Tool	Purpose
Streamlit	Web UI framework
Anthropic Claude	AI design generation
Google Fonts	Typography (Playfair Display + DM Sans)
📋 How It Works
User fills in room specs and picks a style
App sends a structured prompt to claude-sonnet-4-20250514
Claude returns a JSON design concept
Streamlit renders swatches, cards, and spec bars from the JSON
💡 Example Styles to Try
Cyberpunk — neon accents, dark metals, LED strips
Japandi — wabi-sabi minimalism, natural wood, muted tones
Cottagecore — floral prints, vintage wood, soft pastels
Dark Academia — rich mahogany, leather, candlelight
🔑 Requirements
Python 3.9+
Anthropic API key (get one here)
Internet connection (Google Fonts + Anthropic API)

This tool simplifies code so anyone can understand what each line does.

---

## 🛠️ Tech Stack

- Python
- Streamlit

(No heavy AI libraries required)

---

## 📂 Project Structure

Code-Commenter/
│
├── app.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Code-Commenter.git
cd Code-Commenter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open in browser:

http://localhost:8501

---

## 🧪 Example

### Input Code:

```python
for i in range(5):
    print(i)
```

### Output:

```python
for i in range(5):  # This line starts a loop that repeats for each item.
    print(i)  # This shows output on the screen.
```

---

## 🔮 Future Improvements

- Support for multiple languages (C++, Java, JavaScript)
- AI-powered deeper explanation
- Code complexity analysis
- Beginner learning mode
- Side-by-side comparison view

---

## 👨‍💻 Author

Mohammad Mansuri  
AI & Data Science Enthusiast  
Mumbai University

---

## 📜 License

This project is open-source and free to use.

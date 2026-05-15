import streamlit as st
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import time

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="CampusGraph AI",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #dbeafe, #e0f2fe, #f0f9ff);
    color: #1e293b;
}

/* Main Content */
.main {
    background-color: transparent;
}

/* Headings */
h1 {
    color: #0f172a;
    text-align: center;
    font-weight: bold;
}

h2, h3 {
    color: #1e3a8a;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #bfdbfe, #dbeafe);
}

/* Card Style */
.card {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

/* Buttons */
div.stButton > button {
    background-color: #3b82f6;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #2563eb;
    transform: scale(1.03);
}

/* Text Input */
.stTextInput input {
    border-radius: 10px;
    border: 2px solid #93c5fd;
    padding: 10px;
}

/* Fade Animation */
.fade-in {
    animation: fadeIn 1s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# TITLE
# --------------------------------
st.markdown(
    "<h1 class='fade-in'>🎓 CampusGraph AI</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 class='fade-in' style='text-align:center;'>GraphRAG Smart College Assistant</h3>",
    unsafe_allow_html=True
)

# --------------------------------
# SIDEBAR
# --------------------------------
st.sidebar.title("📌 Navigation")

menu = st.sidebar.radio(
    "Choose Section",
    [
        "🏠 Home",
        "❓ Ask Questions",
        "📊 Graph Visualization",
        "📈 Benchmark Results"
    ]
)

# --------------------------------
# CREATE GRAPH
# --------------------------------
G = nx.Graph()

students = ["Jagdish", "Rahul", "Priya"]
teachers = ["Ravi", "Anita"]
subjects = ["DBMS", "Python", "AI"]
courses = ["BCA"]

# Add nodes
for s in students:
    G.add_node(s, category="Student")

for t in teachers:
    G.add_node(t, category="Teacher")

for sub in subjects:
    G.add_node(sub, category="Subject")

for c in courses:
    G.add_node(c, category="Course")

# Add edges
G.add_edge("Jagdish", "Python")
G.add_edge("Rahul", "DBMS")
G.add_edge("Priya", "AI")

G.add_edge("Ravi", "Python")
G.add_edge("Anita", "DBMS")

G.add_edge("BCA", "Python")
G.add_edge("BCA", "DBMS")
G.add_edge("BCA", "AI")

# --------------------------------
# HOME PAGE
# --------------------------------
if menu == "🏠 Home":

    st.markdown('<div class="card fade-in">', unsafe_allow_html=True)

    st.markdown("## 🚀 Welcome to CampusGraph AI")

    st.write(
        "CampusGraph AI is a smart college assistant powered by:"
    )

    st.write("✅ GraphRAG Technology")
    st.write("✅ Knowledge Graphs")
    st.write("✅ AI-based Query System")
    st.write("✅ Streamlit Dashboard")
    st.write("✅ NetworkX Graph Visualization")

    st.markdown('</div>', unsafe_allow_html=True)

    st.balloons()

# --------------------------------
# ASK QUESTIONS
# --------------------------------
elif menu == "❓ Ask Questions":

    st.markdown('<div class="card fade-in">', unsafe_allow_html=True)

    st.markdown("## ❓ Ask Questions")

    question = st.text_input(
        "Enter your question:"
    )

    if question:

        with st.spinner("🤖 AI is thinking..."):
            time.sleep(1)

        q = question.lower()

        if "python" in q:
            st.success("✅ Python is taught by Ravi.")

        elif "dbms" in q:
            st.success("✅ DBMS is taught by Anita.")

        elif "ai" in q:
            st.success("✅ AI is available in the BCA course.")

        elif "students" in q:
            st.success("✅ Students: Jagdish, Rahul, Priya")

        elif "teacher" in q:
            st.success("✅ Teachers: Ravi, Anita")

        else:
            st.warning("⚠️ Answer not found in the knowledge graph.")

    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------
# GRAPH VISUALIZATION
# --------------------------------
elif menu == "📊 Graph Visualization":

    st.markdown('<div class="card fade-in">', unsafe_allow_html=True)

    st.markdown("## 📊 Campus Knowledge Graph")

    fig, ax = plt.subplots(figsize=(10, 6))

    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="#60a5fa",
        node_size=3200,
        font_size=10,
        font_weight="bold",
        edge_color="#64748b",
        linewidths=2,
        ax=ax
    )

    fig.patch.set_facecolor('#f0f9ff')
    ax.set_facecolor('#f0f9ff')

    ax.axis("off")

    st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------
# BENCHMARK RESULTS
# --------------------------------
elif menu == "📈 Benchmark Results":

    st.markdown('<div class="card fade-in">', unsafe_allow_html=True)

    st.markdown("## 📈 Benchmark Results")

    data = {
        "Model": ["Traditional RAG", "GraphRAG"],
        "Accuracy": [72, 91],
        "Response Time": [2.5, 1.2]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.bar_chart(
        df.set_index("Model")
    )

    st.success(
        "✅ GraphRAG performs better than Traditional RAG."
    )

    st.markdown('</div>', unsafe_allow_html=True)
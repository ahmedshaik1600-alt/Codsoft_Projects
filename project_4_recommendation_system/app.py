import streamlit as st

from recommender import recommend


st.set_page_config(
    page_title="Recommendation System",
    page_icon="RS",
    layout="centered",
)


def apply_style() -> None:
    st.markdown(
        """
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background:
                radial-gradient(circle at top left, rgba(255, 0, 60, 0.22), transparent 32rem),
                linear-gradient(135deg, #050505 0%, #111111 50%, #1a0508 100%) !important;
            color: #ffffff !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        .main .block-container {
            max-width: 900px;
            padding-top: 2rem;
        }

        h1, h2, h3, p, label, span, div {
            color: #ffffff;
        }

        .glass-panel {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 40, 80, 0.35);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(16px);
            border-radius: 18px;
            padding: 1.3rem;
            margin-bottom: 1rem;
        }

        .title {
            color: #ff234f;
            font-size: 2.4rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
        }

        .subtitle {
            color: #d7d7d7;
            margin-bottom: 1.2rem;
        }

        .result-card {
            background: rgba(0, 0, 0, 0.34);
            border: 1px solid rgba(255, 35, 79, 0.35);
            border-radius: 14px;
            padding: 1rem;
            margin: 0.75rem 0;
        }

        .item-title {
            color: #ff234f;
            font-weight: 800;
            font-size: 1.1rem;
        }

        .tag {
            color: #ff8aa0;
            font-size: 0.9rem;
        }

        .stButton > button {
            background: #ff234f;
            color: #ffffff;
            border: 0;
            border-radius: 10px;
            font-weight: 800;
            width: 100%;
        }

        .stButton > button:hover {
            background: #ff496c;
            color: #ffffff;
        }

        [data-testid="stMultiSelect"] div,
        [data-testid="stSelectbox"] div,
        [data-testid="stNumberInput"] div {
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    apply_style()

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown('<div class="title">Recommendation System</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Choose what you like and get simple content-based recommendations.</div>',
        unsafe_allow_html=True,
    )

    category = st.selectbox("Recommend", ["All", "Movie", "Book", "Product"])
    preferences = st.multiselect(
        "Your preferences",
        [
            "action",
            "adventure",
            "animation",
            "biography",
            "business",
            "coffee",
            "crime",
            "drama",
            "family",
            "finance",
            "fitness",
            "focus",
            "health",
            "inspirational",
            "laptop",
            "music",
            "productivity",
            "reading",
            "sci-fi",
            "self-help",
            "space",
            "technology",
            "travel",
            "wellness",
        ],
        default=["sci-fi", "adventure"],
    )
    top_n = st.slider("Number of recommendations", min_value=1, max_value=8, value=5)
    search = st.button("Get Recommendations")
    st.markdown("</div>", unsafe_allow_html=True)

    if search:
        results = recommend(category=category, preferences=preferences, top_n=top_n)

        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.subheader("Results")

        if not preferences:
            st.warning("Select at least one preference.")
        elif not results:
            st.info("No matching items found. Try a different preference.")
        else:
            for item in results:
                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="item-title">{item['title']} · {item['category']}</div>
                        <div class="tag">{item['tags']}</div>
                        <p>{item['description']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

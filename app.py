import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AgriVision AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).parent

MODEL_FILE = BASE_DIR / "yield_prediction_model.pkl"
DATA_FILE = BASE_DIR / "crop_health_2018.csv"

NDVI_MAP = BASE_DIR / "ndvi_map_2018.png"
NDVI_GRAPH = BASE_DIR / "ndvi_distribution.png"
HEALTH_GRAPH = BASE_DIR / "crop_health_distribution.png"
NDVI_YIELD_GRAPH = BASE_DIR / "ndvi_vs_yield.png"
PREDICTION_GRAPH = BASE_DIR / "actual_vs_predicted_yield.png"


# ============================================================
# LOAD MODEL
# ============================================================

try:
    model = joblib.load(MODEL_FILE)
except Exception as e:
    st.error("Unable to load the Random Forest model.")
    st.error(str(e))
    st.stop()


# ============================================================
# LOAD DATA
# ============================================================

try:
    data = pd.read_csv(DATA_FILE)
except Exception as e:
    st.error("Unable to load the crop health dataset.")
    st.error(str(e))
    st.stop()


# ============================================================
# CROP HEALTH FUNCTION
# ============================================================

def classify_health(ndvi):

    if ndvi >= 0.80:
        return "Healthy"

    elif ndvi >= 0.70:
        return "Moderate Stress"

    else:
        return "Severe Stress"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main application */

    .stApp {
        background-color: #f4f7f2;
    }


    /* Sidebar */

    section[data-testid="stSidebar"] {
        background-color: #103b2d;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }


    /* Main title */

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #12372a;
        margin-bottom: 5px;
    }


    .main-subtitle {
        font-size: 17px;
        color: #68786e;
        margin-bottom: 25px;
    }


    /* Hero */

    .hero {
        background: linear-gradient(
            135deg,
            #103b2d,
            #23684d
        );

        padding: 38px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
    }


    .hero-title {
        font-size: 38px;
        font-weight: 800;
    }


    .hero-text {
        font-size: 17px;
        line-height: 1.7;
        color: #e3eee8;
        margin-top: 10px;
    }


    /* Cards */

    .card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #dce7df;
        box-shadow: 0 5px 18px rgba(18, 55, 42, 0.07);
        min-height: 135px;
    }


    .card-title {
        font-size: 15px;
        color: #718078;
        margin-bottom: 8px;
    }


    .card-value {
        font-size: 30px;
        font-weight: 800;
        color: #12372a;
    }


    .card-description {
        font-size: 13px;
        color: #7a877f;
        margin-top: 6px;
    }


    /* Section titles */

    .section-title {
        font-size: 28px;
        font-weight: 750;
        color: #12372a;
        margin-top: 28px;
        margin-bottom: 18px;
    }


    /* Prediction result */

    .result-box {
        background-color: white;
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #dce7df;
        box-shadow: 0 5px 18px rgba(18, 55, 42, 0.07);
        text-align: center;
        min-height: 170px;
    }


    .result-title {
        font-size: 17px;
        color: #718078;
        margin-bottom: 15px;
    }


    .result-value {
        font-size: 30px;
        font-weight: 800;
        color: #1f5c45;
    }


    /* Information box */

    .info-box {
        background-color: #edf5ef;
        border-left: 5px solid #1f5c45;
        padding: 18px;
        border-radius: 8px;
        color: #31463a;
        line-height: 1.7;
        margin-top: 15px;
    }


    /* Footer */

    .footer {
        text-align: center;
        padding: 35px 0 15px 0;
        color: #758279;
        font-size: 13px;
    }


    /* Button */

    .stButton > button {
        background-color: #1f5c45;
        color: white;
        border: none;
        border-radius: 9px;
        padding: 11px 25px;
        font-weight: 700;
    }


    .stButton > button:hover {
        background-color: #12372a;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <h1 style="
            text-align:center;
            color:white;
            font-size:28px;
            margin-top:20px;
        ">
        AgriVision AI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="
            text-align:center;
            color:#c8d9d0;
            font-size:13px;
            margin-bottom:30px;
        ">
        Crop Health and Yield Prediction
        </p>
        """,
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "▦  Dashboard",
            "◈  Crop Prediction",
            "⌖  NDVI Map",
            "▥  Data Analysis",
            "◉  Model Performance",
            "ⓘ  About Project"
        ]
    )

    st.markdown("---")

    st.markdown(
        """
        <p style="
            text-align:center;
            color:#c8d9d0;
            font-size:14px;
            line-height:1.7;
        ">
        Machine Learning Based<br>
        Agricultural Intelligence
        </p>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DASHBOARD
# ============================================================

if page == "▦  Dashboard":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                AgriVision AI
            </div>

            <div class="hero-text">
                Crop Health and Yield Prediction using
                Satellite Imagery and Machine Learning.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="section-title">Project Overview</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3, col4 = st.columns(4)


    # Total records

    with col1:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    Total Records
                </div>

                <div class="card-value">
                    {len(data):,}
                </div>

                <div class="card-description">
                    Usable agricultural observations
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # Average NDVI

    with col2:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    Average NDVI
                </div>

                <div class="card-value">
                    {data["NDVI"].mean():.3f}
                </div>

                <div class="card-description">
                    Vegetation index
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # Average yield

    with col3:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    Average Yield
                </div>

                <div class="card-value">
                    {data["YIELD"].mean():,.0f}
                </div>

                <div class="card-description">
                    Average observed yield
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # Healthy percentage

    with col4:

        healthy_count = (
            data["Crop_Health"] == "Healthy"
        ).sum()

        healthy_percentage = (
            healthy_count / len(data)
        ) * 100

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    Healthy Crops
                </div>

                <div class="card-value">
                    {healthy_percentage:.1f}%
                </div>

                <div class="card-description">
                    Based on NDVI classification
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # NDVI map

    st.markdown(
        '<div class="section-title">NDVI Map</div>',
        unsafe_allow_html=True
    )


    if NDVI_MAP.exists():

        st.image(
            str(NDVI_MAP),
            use_container_width=True
        )

    else:

        st.warning(
            "NDVI map image was not found."
        )


    # Information

    st.markdown(
        """
        <div class="info-box">

        <b>NDVI Overview</b>

        <br><br>

        NDVI stands for Normalized Difference Vegetation Index.
        It is calculated using Red and Near-Infrared satellite
        information to estimate vegetation condition.

        </div>
        """,
        unsafe_allow_html=True
    )


    # Dataset preview

    st.markdown(
        '<div class="section-title">Dataset Preview</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        data.head(10),
        use_container_width=True
    )


# ============================================================
# CROP PREDICTION
# ============================================================

elif page == "◈  Crop Prediction":

    st.markdown(
        '<div class="main-title">Crop Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-subtitle">
        Enter NDVI and humidity values to estimate crop health
        and predicted yield.
        </div>
        """,
        unsafe_allow_html=True
    )


    # Input values

    col1, col2 = st.columns(2)


    with col1:

        ndvi = st.number_input(
            "NDVI Value",
            min_value=0.0,
            max_value=1.0,
            value=0.82,
            step=0.01
        )


    with col2:

        humid = st.number_input(
            "Humidity",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=0.1
        )


    st.write("")


    # ========================================================
    # PREDICTION
    # ========================================================

    if st.button("Predict Crop Condition"):

        # Determine crop health

        health = classify_health(ndvi)


        # Prepare model input

        input_data = pd.DataFrame(
            {
                "NDVI": [ndvi],
                "HUMID": [humid]
            }
        )


        # Predict yield

        predicted_yield = model.predict(
            input_data
        )[0]


        # ====================================================
        # PREDICTION RESULTS
        # ====================================================

        st.markdown(
            '<div class="section-title">Prediction Results</div>',
            unsafe_allow_html=True
        )


        result_col1, result_col2 = st.columns(2)


        # Crop health result

        with result_col1:

            if health == "Healthy":

                st.success(
                    "Crop Health: HEALTHY"
                )

            elif health == "Moderate Stress":

                st.warning(
                    "Crop Health: MODERATE STRESS"
                )

            else:

                st.error(
                    "Crop Health: SEVERE STRESS"
                )


        # Yield result

        with result_col2:

            st.metric(
                "Predicted Yield",
                f"{predicted_yield:,.2f}"
            )


        # ====================================================
        # INPUT SUMMARY
        # ====================================================

        st.markdown(
            '<div class="section-title">Input Values</div>',
            unsafe_allow_html=True
        )


        input_col1, input_col2 = st.columns(2)


        with input_col1:

            st.metric(
                "NDVI",
                f"{ndvi:.2f}"
            )


        with input_col2:

            st.metric(
                "Humidity",
                f"{humid:.2f}"
            )


    # ========================================================
    # NDVI CLASSIFICATION TABLE
    # ========================================================

    st.markdown(
        '<div class="section-title">NDVI Classification</div>',
        unsafe_allow_html=True
    )


    classification_data = pd.DataFrame(
        {
            "NDVI Range": [
                "0.80 - 1.00",
                "0.70 - 0.79",
                "Below 0.70"
            ],

            "Crop Health": [
                "Healthy",
                "Moderate Stress",
                "Severe Stress"
            ]
        }
    )


    st.table(
        classification_data
    )


# ============================================================
# NDVI MAP
# ============================================================

elif page == "⌖  NDVI Map":

    st.markdown(
        '<div class="main-title">NDVI Map</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-subtitle">
        Satellite-based vegetation health visualization.
        </div>
        """,
        unsafe_allow_html=True
    )


    if NDVI_MAP.exists():

        st.image(
            str(NDVI_MAP),
            use_container_width=True
        )

    else:

        st.error(
            "NDVI map image was not found."
        )


    st.markdown(
        '<div class="section-title">Understanding NDVI</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="info-box">

        <b>NDVI Formula</b>

        <br><br>

        NDVI = (NIR - Red) / (NIR + Red)

        <br><br>

        In this project, satellite Red and Near-Infrared
        bands are used to calculate NDVI.

        Higher NDVI values generally represent healthier
        vegetation.

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DATA ANALYSIS
# ============================================================

elif page == "▥  Data Analysis":

    st.markdown(
        '<div class="main-title">Data Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-subtitle">
        Explore the dataset and understand relationships
        between NDVI, humidity, crop health, and yield.
        </div>
        """,
        unsafe_allow_html=True
    )


    # Dataset

    st.markdown(
        '<div class="section-title">Dataset</div>',
        unsafe_allow_html=True
    )


    st.dataframe(
        data,
        use_container_width=True
    )


    # NDVI distribution

    st.markdown(
        '<div class="section-title">NDVI Distribution</div>',
        unsafe_allow_html=True
    )


    if NDVI_GRAPH.exists():

        st.image(
            str(NDVI_GRAPH),
            use_container_width=True
        )


    # Crop health distribution

    st.markdown(
        '<div class="section-title">Crop Health Distribution</div>',
        unsafe_allow_html=True
    )


    if HEALTH_GRAPH.exists():

        st.image(
            str(HEALTH_GRAPH),
            use_container_width=True
        )


    # NDVI vs yield

    st.markdown(
        '<div class="section-title">NDVI vs Yield</div>',
        unsafe_allow_html=True
    )


    if NDVI_YIELD_GRAPH.exists():

        st.image(
            str(NDVI_YIELD_GRAPH),
            use_container_width=True
        )


    # Statistical summary

    st.markdown(
        '<div class="section-title">Statistical Summary</div>',
        unsafe_allow_html=True
    )


    st.dataframe(
        data.describe(),
        use_container_width=True
    )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

elif page == "◉  Model Performance":

    st.markdown(
        '<div class="main-title">Model Performance</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-subtitle">
        Performance of the Random Forest regression model.
        </div>
        """,
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Mean Absolute Error",
            "1827.87"
        )


    with col2:

        st.metric(
            "Root Mean Squared Error",
            "2493.90"
        )


    with col3:

        st.metric(
            "R Squared",
            "0.3104"
        )


    # Actual vs predicted

    st.markdown(
        '<div class="section-title">Actual vs Predicted Yield</div>',
        unsafe_allow_html=True
    )


    if PREDICTION_GRAPH.exists():

        st.image(
            str(PREDICTION_GRAPH),
            use_container_width=True
        )

    else:

        st.warning(
            "Actual vs Predicted graph was not found."
        )


    # Model explanation

    st.markdown(
        """
        <div class="info-box">

        <b>Model Information</b>

        <br><br>

        The Random Forest regression model uses NDVI and
        humidity as input features for crop yield prediction.

        <br><br>

        The current R-squared value is approximately 0.31,
        meaning that the model explains around 31 percent
        of the variation in yield for the current test split.

        <br><br>

        Additional features such as rainfall, temperature,
        soil properties, and more satellite information
        could potentially improve prediction performance.

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ABOUT PROJECT
# ============================================================

elif page == "ⓘ  About Project":

    st.markdown(
        '<div class="main-title">About the Project</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-subtitle">
        Crop Health and Yield Prediction using Machine Learning
        </div>
        """,
        unsafe_allow_html=True
    )


    # Problem statement

    st.markdown(
        '<div class="section-title">Problem Statement</div>',
        unsafe_allow_html=True
    )


    st.write(
        """
        Agricultural crop monitoring traditionally requires
        field visits and manual observation. These methods
        can be time-consuming and may not provide continuous
        information about crop conditions.

        This project uses satellite imagery and machine
        learning to analyze crop vegetation health and
        estimate crop yield.
        """
    )


    # Technologies

    st.markdown(
        '<div class="section-title">Technology Used</div>',
        unsafe_allow_html=True
    )


    technologies = pd.DataFrame(
        {
            "Technology": [
                "Python",
                "Pandas",
                "NumPy",
                "Rasterio",
                "GeoPandas",
                "Scikit-learn",
                "Random Forest",
                "Streamlit"
            ],

            "Purpose": [
                "Programming language",
                "Data processing",
                "Numerical computation",
                "Satellite raster processing",
                "Geospatial processing",
                "Machine learning",
                "Yield prediction",
                "Dashboard development"
            ]
        }
    )


    st.table(
        technologies
    )


    # Workflow

    st.markdown(
        '<div class="section-title">Project Workflow</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="info-box">

        <b>Step 1:</b>
        Collect satellite imagery and agricultural data.

        <br><br>

        <b>Step 2:</b>
        Extract Red and Near-Infrared satellite bands.

        <br><br>

        <b>Step 3:</b>
        Calculate NDVI.

        <br><br>

        <b>Step 4:</b>
        Combine NDVI with yield and humidity data.

        <br><br>

        <b>Step 5:</b>
        Classify crop health using NDVI thresholds.

        <br><br>

        <b>Step 6:</b>
        Train the Random Forest regression model.

        <br><br>

        <b>Step 7:</b>
        Evaluate the model using MAE, RMSE and R-squared.

        <br><br>

        <b>Step 8:</b>
        Display results using the Streamlit dashboard.

        </div>
        """,
        unsafe_allow_html=True
    )


    # Goal

    st.markdown(
        '<div class="section-title">Project Goal</div>',
        unsafe_allow_html=True
    )


    st.write(
        """
        The goal of the project is to develop a machine-learning
        based agricultural monitoring system that helps understand
        crop health and predict crop yield using satellite and
        environmental data.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    AgriVision AI | Crop Health and Yield Prediction using Machine Learning

    <br><br>

    Academic Project

    </div>
    """,
    unsafe_allow_html=True
)
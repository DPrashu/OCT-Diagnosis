import streamlit as st
from utils import preprocess,predict
from PIL import Image

# Custom CSS to beautify the sidebar
st.markdown("""
    <style>
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #1c1c1e;
            color: white;
        }
        .sidebar .sidebar-content {
            padding: 20px;
        }

        /* Title styling */
        .sidebar .sidebar-content h2 {
            color: #ff4b4b;
            font-size: 24px;
            font-weight: bold;
        }

        /* Radio button styling */
        div[data-testid="stSidebar"] > div > div > div > div > label > div {
            font-size: 18px;
            padding: 8px 12px;
        }

        /* Radio active option */
        .css-1hynsf2 {
            background-color: #ff4b4b !important;
            color: white !important;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.title("🔍 Navigation")
options = ['🏠 Home Page','🧠 What is OCT ?','📂 About the dataset','📤 Upload an image']
choice = st.sidebar.radio("Go to", options)

if choice == '🏠 Home Page':
    st.markdown("""
        <style>
            .main-title {
                text-align: center;
                font-size: 40px;
                color: #00BFFF;
                padding-bottom: 10px;
            }
            .subtitle {
                font-size: 22px;
                color: #f5f5f5;
                line-height: 1.6;
                text-align: center;
                margin-bottom: 25px;
            }
            .section {
                background-color: #262730;
                padding: 20px;
                border-radius: 10px;
                margin-top: 10px;
            }
            .section ul {
                font-size: 18px;
                color: #eaeaea;
                line-height: 1.8;
            }
            .footer-note {
                font-size: 18px;
                margin-top: 25px;
                color: #aaaaaa;
                text-align: center;
            }
        </style>

        <div class="main-title">🧿 OCT Diagnosis using Deep Learning</div>

        <div class="subtitle">
            Welcome to our intelligent diagnostic tool for eye diseases!<br>
            This web application uses Optical Coherence Tomography (OCT) images to assist in identifying eye conditions.
        </div>

        <div class="section">
            <ul>
                <li>🔍 Use the sidebar to explore the application.</li>
                <li>📖 Click on <b>"What is OCT?"</b> to understand the technology.</li>
                <li>📂 View <b>"About the Dataset"</b> to learn where the data comes from.</li>
                <li>📸 Upload an OCT image using the <b>"Upload an Image"</b> section to get a disease prediction.</li>
            </ul>
        </div>

        <div class="footer-note">
            ⚠️ Note: This tool is meant for educational and research purposes only.
        </div>
    """, unsafe_allow_html=True)

elif choice == '🧠 What is OCT ?':
  st.set_page_config(layout="wide")
  st.markdown(
      """
      <style>
      body {
          background-color: #0e1117;
          color: #ffffff;
      }
      .title {
          font-size: 48px;
          font-weight: bold;
          color: #14f1d9;
          margin-bottom: 20px;
      }
      .section-header {
          font-size: 28px;
          font-weight: bold;
          color: #f4c542;
          margin-top: 30px;
      }
      .content-text {
          font-size: 18px;
          line-height: 1.6;
          text-align: justify;
          margin-bottom: 20px;
      }
      .img-center {
          display: flex;
          justify-content: center;
          margin: 30px 0;
      }
      </style>
      """,
      unsafe_allow_html=True
  )

  # Title
  st.markdown('<div class="title">What is Optical Coherence Tomography (OCT)?</div>', unsafe_allow_html=True)

  # Section: Introduction
  st.markdown('<div class="section-header">🔍 Introduction</div>', unsafe_allow_html=True)
  st.markdown(
      """
      <div class="content-text">
      Optical Coherence Tomography (OCT) is a non-invasive imaging technique that uses light waves to take cross-section pictures of the retina. 
      It allows ophthalmologists to see each of the retina’s distinctive layers, which helps in diagnosing and monitoring diseases like macular degeneration, diabetic retinopathy, glaucoma, and more.
      </div>
      """,
      unsafe_allow_html=True
  )

  # Section: Working
  st.markdown('<div class="section-header">⚙️ How Does OCT Work?</div>', unsafe_allow_html=True)
  st.markdown(
      """
      <div class="content-text">
      OCT works much like ultrasound, except it uses light instead of sound. It captures micrometer-resolution, cross-sectional images using the echo time delay and intensity of light that is reflected or backscattered from internal tissue structures.
      The patient places their head on a chinrest and focuses on a target while the machine takes images of the eye, usually completed in just a few seconds.
      </div>
      """,
      unsafe_allow_html=True
  )

  # Section: Importance in Diagnosis
  st.markdown('<div class="section-header">🧠 Importance in Medical Diagnosis</div>', unsafe_allow_html=True)
  st.markdown(
      """
      <div class="content-text">
      - OCT is essential in diagnosing **Retinal Diseases** like Age-related Macular Degeneration (AMD), Central Serous Retinopathy, and Diabetic Macular Edema (DME).  
      - It allows doctors to see fluid buildup, swelling, and thickness in the retina.  
      - Helps in **pre and post-surgical evaluations** and treatment planning.  
      - Provides a non-contact, quick, and repeatable diagnostic tool with high-resolution images.
      </div>
      """,
      unsafe_allow_html=True
  )

  # Section: Future Scope
  st.markdown('<div class="section-header">🚀 Future of OCT in AI & Deep Learning</div>', unsafe_allow_html=True)
  st.markdown(
      """
      <div class="content-text">
      The integration of **Deep Learning** models with OCT data is revolutionizing the field of ophthalmology. Automated systems can now detect and classify eye diseases with high accuracy, reducing the dependency on human experts in remote or under-resourced areas.
      This project is one such initiative where we utilize a deep learning model trained on thousands of OCT images to assist in accurate diagnosis.
      </div>
      """,
      unsafe_allow_html=True
  )

  st.markdown('<div class="section-header">How Our Model Helps in Diagnosis</div>', unsafe_allow_html=True)
  st.markdown("""
  <div class="content-text">
  Our deep learning-based model brings significant benefits to the diagnosis of retinal diseases:
  <ul>
      <li><strong>Automated and Fast:</strong> The model can analyze OCT scans within seconds, allowing ophthalmologists to quickly triage patients.</li>
      <li><strong>High Accuracy:</strong> With proper training and validation, the model achieves performance comparable to human experts in identifying abnormalities like CNV, DME, and Drusen.</li>
      <li><strong>Reduced Workload:</strong> Manual interpretation of OCT scans is time-consuming and prone to fatigue-related errors. Our system streamlines this process and minimizes diagnostic delays.</li>
      <li><strong>Scalable Solution:</strong> Especially in remote or under-resourced areas, the model can serve as a virtual assistant for initial screening, ensuring more patients receive timely attention.</li>
      <li><strong>Consistent Results:</strong> Unlike humans, machine learning models provide uniform predictions without being affected by mood, fatigue, or experience level.</li>
  </ul>
  </div>
  """, unsafe_allow_html=True)


  # Divider
  st.markdown("---")
  st.markdown('<div style="text-align:center; font-size:16px;">© 2025 - OCT Diagnosis Tool</div>', unsafe_allow_html=True)

elif choice == '📂 About the dataset':
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 38px;
            color: #00ffd5;
            font-weight: 800;
            margin-bottom: 20px;
        }
        .subheading {
            font-size: 22px;
            color: #ffcc70;
            margin-top: 25px;
        }
        .body-text {
            font-size: 17px;
            line-height: 1.8;
            color: #e0e0e0;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">📊 About the Dataset</div>', unsafe_allow_html=True)

    st.markdown('<div class="body-text">The dataset used for this project is a publicly available Optical Coherence Tomography (OCT) dataset, originally published by <b>Mooney et al.</b> It contains thousands of labeled OCT scan images categorized into four classes:</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <ul class="body-text">
            <li><b>CNV (Choroidal Neovascularization)</b> — Represents abnormal blood vessel growth.</li>
            <li><b>DME (Diabetic Macular Edema)</b> — Swelling in the retina due to diabetes.</li>
            <li><b>Drusen</b> — Yellow deposits under the retina, early sign of age-related macular degeneration.</li>
            <li><b>Normal</b> — Healthy OCT scan without abnormalities.</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subheading">📦 Dataset Details</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="body-text">
        - Total Images: ~84,000+ <br>
        - Image Dimensions: Varying, resized to 28x28 pixels for model input <br>
        - Format: Grayscale JPEG images <br>
        - Source: [Kermany et al. (2018) OCT Dataset](https://data.mendeley.com/datasets/rscbjbr9sj/2) <br>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subheading">🧠 Why This Dataset?</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="body-text">
        This dataset is extensively used in medical AI research due to:
        <ul>
            <li>High-quality annotated data</li>
            <li>Real-world medical relevance</li>
            <li>Class imbalance challenges that mimic real diagnostic tasks</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subheading">📌 Note</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="body-text">
        For this project, we have selected <b>500 random images from each class</b> to keep training efficient while retaining meaningful patterns.
        </div>
        """, unsafe_allow_html=True)

elif choice == '📤 Upload an image':
    st.markdown(
        """
        <style>
        .upload-title {
            font-size: 36px;
            color: #00ffd5;
            font-weight: 800;
            margin-bottom: 20px;
        }
        .upload-sub {
            font-size: 20px;
            color: #ffcc70;
            margin-bottom: 10px;
        }
        .upload-info {
            font-size: 16px;
            color: #e0e0e0;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="upload-title">🧪 OCT Scan Diagnosis</div>', unsafe_allow_html=True)
    st.markdown('<div class="upload-sub">Upload your eye scan image</div>', unsafe_allow_html=True)
    st.markdown('<div class="upload-info">Supported formats: JPG, JPEG, PNG | Recommended size: 28x28 or larger</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose an OCT image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
      image = Image.open(uploaded_file)
      st.image(image, caption='Uploaded OCT Scan')
      st.success("Image successfully uploaded. Ready for diagnosis!")

      if st.button("🔍 Make Prediction"):
          with st.spinner('Analyzing image... Please wait ⏳'):
              tensor = preprocess(image)
              output = predict(tensor)
              st.success("✅ Prediction complete! Image is classified as {}".format(output))



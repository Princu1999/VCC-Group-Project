import streamlit as st
import requests
from PIL import Image
import io
import base64

# ------------------------ Page Config ------------------------
st.set_page_config(
    page_title="Cloud Based Image Processing Service",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------ Custom CSS ------------------------
st.markdown("""
<style>
    /* Base Styles & Typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1a202c;
    }
    
    /* Page Layout */
    .stApp {
        background: #f8fafc;
    }
    
    /* Header Styles */
    .hero-container {
        background: linear-gradient(120deg, #2563eb, #3b82f6, #60a5fa);
        color: white;
        padding: 2.5rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        font-weight: 400;
        opacity: 0.9;
        max-width: 700px;
        margin: 0 auto;
    }
    
    /* Card Styles */
    .card {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    
    .card-header {
        padding: 1.25rem 1.5rem;
        border-bottom: 1px solid #e2e8f0;
        font-weight: 600;
        font-size: 1.25rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        background: white;
        color: #1e3a8a;
    }
    
    .card-body {
        padding: 1.5rem;
    }
    
    /* Features Section */
    .features-container {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .feature-item {
        background: #f1f5f9;
        border-radius: 12px;
        padding: 1.5rem;
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 1rem;
        transition: all 0.3s ease;
        border: 1px solid #e2e8f0;
    }
    
    .feature-item:hover {
        background: white;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        border-color: #cbd5e1;
        transform: translateY(-3px);
    }
    
    .feature-icon {
        font-size: 2rem;
        background: #dbeafe;
        width: 64px;
        height: 64px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        color: #2563eb;
    }
    
    .feature-title {
        font-weight: 600;
        font-size: 1.125rem;
        color: #1e40af;
    }
    
    .feature-desc {
        font-size: 0.925rem;
        color: #475569;
        line-height: 1.5;
    }
    
    /* Upload Section */
    .upload-container {
        border: 2px dashed #cbd5e1;
        border-radius: 12px;
        padding: 2.5rem;
        text-align: center;
        transition: all 0.3s ease;
        background: #f8fafc;
        margin-bottom: 1rem;
    }
    
    .upload-container:hover {
        border-color: #3b82f6;
        background: #eff6ff;
    }
    
    .upload-icon {
        font-size: 2.5rem;
        color: #3b82f6;
        margin-bottom: 1rem;
    }
    
    .upload-title {
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 0.5rem;
        color: #1e40af;
    }
    
    .upload-subtitle {
        color: #64748b;
        margin-bottom: 1.5rem;
    }
    
    /* Image Processing Results */
    .image-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        grid-gap: 1.5rem;
    }
    
    .image-card {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        border: 1px solid #e2e8f0;
    }
    
    .image-card:hover {
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        transform: translateY(-3px);
    }
    
    .image-wrapper {
        position: relative;
        overflow: hidden;
        border-radius: 8px;
        margin-bottom: 0.75rem;
    }
    
    .image-wrapper img {
        transition: transform 0.5s ease;
        width: 100%;
        height: auto;
        display: block;
    }
    
    .image-wrapper:hover img {
        transform: scale(1.04);
    }
    
    .image-caption {
        font-size: 0.875rem;
        color: #64748b;
        text-align: center;
        font-weight: 500;
        margin: 0.5rem 0;
    }
    
    /* Processing Status */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.375rem;
        padding: 0.5rem 1rem;
        border-radius: 9999px;
        font-weight: 500;
        font-size: 0.875rem;
        margin: 0.75rem 0;
    }
    
    .status-pending {
        background-color: #fef3c7;
        color: #b45309;
    }
    
    .status-success {
        background-color: #dcfce7;
        color: #166534;
    }
    
    .status-error {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    
    /* Button Styles */
    .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.2s ease;
        text-decoration: none;
        cursor: pointer;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        width: 100%;
        margin-top: 0.75rem;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #2563eb, #3b82f6);
        color: white;
        border: none;
    }
    
    .btn-primary:hover {
        background: linear-gradient(135deg, #1d4ed8, #2563eb);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        transform: translateY(-1px);
    }
    
    /* Progress Bar */
    .custom-progress {
        width: 100%;
        height: 8px;
        background-color: #e2e8f0;
        border-radius: 4px;
        margin: 1.5rem 0;
        overflow: hidden;
        position: relative;
    }
    
    .progress-value {
        height: 100%;
        background: linear-gradient(90deg, #2563eb, #60a5fa);
        border-radius: 4px;
        transition: width 0.3s ease;
    }
    
    /* Stats */
    .stats-container {
        background: #eff6ff;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin: 1.5rem 0;
        border: 1px solid #bfdbfe;
    }
    
    .stats-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1e40af;
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        color: #64748b;
        font-size: 0.95rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #64748b;
        font-size: 0.9rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 2rem;
    }
    
    .footer-logo {
        font-weight: 700;
        color: #3b82f6;
        margin-bottom: 0.5rem;
    }
    
    /* Hide streamlit elements */
    #MainMenu, footer, header {
        visibility: hidden;
    }
    
    /* File uploader customization */
    .stFileUploader > div:first-child {
        border: none !important;
        background-color: transparent !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .features-container {
            flex-direction: column;
        }
    }
</style>
""", unsafe_allow_html=True)

# ------------------------ Hero Section ------------------------
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">☁️ Cloud Based Image Processing Service</h1>
    <p class="hero-subtitle">--Transform your images instantly with our powerful cloud-based grayscale conversion service</p>
</div>
""", unsafe_allow_html=True)

# ------------------------ API Endpoint ------------------------
API_ENDPOINT = "http://34.110.136.205/upload"

# ------------------------ Session State ------------------------
if 'processed_count' not in st.session_state:
    st.session_state.processed_count = 0

# ------------------------ Key Features Section ------------------------
st.markdown("## 🔍 About This Service")

# Create a container with a light background for the features
features_container = st.container()
with features_container:
    # Create three columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🖼️ Grayscale Conversion")
        st.markdown("Automatically converts colorful images to professional grayscale format")
    
    with col2:
        st.markdown("#### ☁️ Cloud Processing")
        st.markdown("All image processing happens on Google cloud servers, requiring no local software or computing resources")
    
    with col3:
        st.markdown("#### 🔒 Secure Processing")
        st.markdown("Your images are processed securely and never stored permanently on our servers")

    # Add some space after the features
    st.markdown("<br>", unsafe_allow_html=True)

# ------------------------ Upload Card ------------------------
st.markdown("""
<div class="card">
    <div class="card-header">
        <span>📤</span> Upload Your Images
    </div>
    <div class="card-body">
        <div class="upload-container">
            <div class="upload-icon">📁</div>
            <h3 class="upload-title">Drop Your Images Here</h3>
            <p class="upload-subtitle">Support for JPG, JPEG, and PNG formats (up to 200MB per file)</p>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader(
    "", 
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True,
    label_visibility="collapsed"
)

st.markdown('</div></div></div>', unsafe_allow_html=True)

# ------------------------ Processing Results ------------------------
if uploaded_files:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <span>🖼️</span> Processing Results
        </div>
        <div class="card-body">
    """, unsafe_allow_html=True)
    
    # Progress tracking
    total_files = len(uploaded_files)
    progress_placeholder = st.empty()
    progress_text_placeholder = st.empty()
    
    progress_placeholder.markdown(f"""
    <div class="custom-progress">
        <div class="progress-value" style="width: 0%;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    progress_text_placeholder.markdown(f"""
    <p style="text-align: center; color: #64748b;">Processing 0/{total_files} images...</p>
    """, unsafe_allow_html=True)
    
    # Create image grid
    st.markdown("""
    <div class="image-grid">
    """, unsafe_allow_html=True)
    
    # Process each file
    processed_count = 0
    
    for idx, uploaded_file in enumerate(uploaded_files):
        try:
            # Start processing card
            st.markdown(f"""
            <div class="image-card">
                <div class="image-wrapper">
                    <img src="data:image/{uploaded_file.type.split('/')[1]};base64,{base64.b64encode(uploaded_file.getvalue()).decode()}" alt="{uploaded_file.name}">
                </div>
                <div style="padding: 1rem;">
                    <p class="image-caption">Original: {uploaded_file.name}</p>
            """, unsafe_allow_html=True)
            
            # Make API request
            with st.spinner(f"Processing {uploaded_file.name}..."):
                response = requests.post(API_ENDPOINT, files={"image": uploaded_file})
            
            if response.status_code == 200:
                data = response.json()
                processed_url = data.get("processed_image_url")
                
                if processed_url:
                    # Success
                    st.markdown(f"""
                    <div class="status-badge status-success">
                        ✅ Successfully Processed
                    </div>
                    <div class="image-wrapper">
                        <img src="{processed_url}" alt="Processed Image">
                    </div>
                    <p class="image-caption">Grayscale Result</p>
                    <a href="{processed_url}" download class="btn btn-primary">
                        📥 Download Result
                    </a>
                    """, unsafe_allow_html=True)
                    
                    processed_count += 1
                else:
                    st.markdown(f"""
                    <div class="status-badge status-error">
                        ⚠️ Processing Error: No URL returned
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="status-badge status-error">
                    ❌ Error: Could not process image
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"""
            <div class="status-badge status-error">
                ❌ Processing Failed
            </div>
            """, unsafe_allow_html=True)
        
        # Close the card
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # Update progress
        progress = (idx + 1) / total_files * 100
        progress_placeholder.markdown(f"""
        <div class="custom-progress">
            <div class="progress-value" style="width: {progress}%;"></div>
        </div>
        """, unsafe_allow_html=True)
        
        progress_text_placeholder.markdown(f"""
        <p style="text-align: center; color: #64748b;">Processing {idx + 1}/{total_files} images...</p>
        """, unsafe_allow_html=True)
    
    # Close image grid
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Update session state
    st.session_state.processed_count += processed_count
    
    # Display stats
    st.markdown(f"""
    <div class="stats-container">
        <div class="stats-value">{processed_count}/{total_files}</div>
        <div class="stats-label">Images Successfully Processed</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

# ------------------------ Footer ------------------------
st.markdown("""
<div class="footer">
    <div class="footer-logo">Cloud Image Processor</div>
    <p>© 2025 Cloud Image Processor - All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
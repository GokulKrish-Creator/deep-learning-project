import json
from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image, ImageOps

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "deepvision_cnn.keras"
CLASSES_PATH = MODEL_DIR / "class_names.json"
IMAGE_SIZE = (200, 200)

st.set_page_config(page_title="DeepVision AI", page_icon="🏭", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.6rem; max-width: 1150px;}
.hero {padding: 1.35rem 1.5rem; border-radius: 18px;
       background: linear-gradient(115deg, #102a43, #176b87); color: white; margin-bottom: 1rem;}
.hero h1 {color: white; margin: 0; font-size: 2.1rem;}
.hero p {color: #e2f4fa; margin: .4rem 0 0 0;}
.small-note {font-size: .88rem; color: #6b7280;}
</style>
<div class="hero">
  <h1>🏭 DeepVision AI</h1>
  <p>Deep learning for steel surface defect classification</p>
</div>
""", unsafe_allow_html=True)

st.write("Upload a steel surface image to see the CNN's predicted defect category.")
st.info("Learning prototype: this model classifies the whole image. It does not locate defects or replace a qualified inspection.")

@st.cache_resource(show_spinner="Loading the trained CNN...")
def load_model(path_string):
    import tensorflow as tf
    return tf.keras.models.load_model(path_string)

def load_classes(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict) and "class_names" in data:
        return data["class_names"]
    return data

if not MODEL_PATH.exists() or not CLASSES_PATH.exists():
    st.warning("The trained model files are not in place yet.")
    st.markdown(
        "**After training in Google Colab:** extract `deepvision_export.zip`, then copy "
        "`deepvision_cnn.keras` and `class_names.json` into the `models` folder beside this app."
    )
    st.code("laptop_app/models/deepvision_cnn.keras\nlaptop_app/models/class_names.json")
    st.stop()

try:
    model = load_model(str(MODEL_PATH))
    class_names = load_classes(CLASSES_PATH)
except Exception as exc:
    st.error("The model could not be loaded. Check that the two files came from the same Colab export.")
    st.exception(exc)
    st.stop()

left, right = st.columns([1, 1], gap="large")
with left:
    uploaded = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg", "bmp"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Uploaded image", use_container_width=True)
    else:
        st.markdown("### How to use")
        st.markdown("1. Choose a steel surface image.\n2. Select **Analyse image**.\n3. Review the predicted class and the top-three scores.")

with right:
    st.markdown("### Prediction")
    if uploaded:
        if st.button("Analyse image", type="primary", use_container_width=True):
            with st.spinner("Analysing image..."):
                # Dataset images are grayscale. Convert uploaded images to grayscale to match training.
                img = ImageOps.grayscale(image).resize(IMAGE_SIZE)
                arr = np.asarray(img, dtype=np.float32) / 255.0
                arr = np.expand_dims(arr, axis=(0, -1))
                probs = model.predict(arr, verbose=0)[0]
                order = np.argsort(probs)[::-1]
                best_idx = int(order[0])
                predicted = class_names[best_idx]
                confidence = float(probs[best_idx])

            st.metric("Predicted defect", predicted.replace("_", " ").title())
            st.metric("Model score", f"{confidence:.1%}")
            st.markdown("#### Top 3 classes")
            for idx in order[:3]:
                label = class_names[int(idx)].replace("_", " ").title()
                score = float(probs[int(idx)])
                st.write(f"**{label}** — {score:.1%}")
                st.progress(min(max(score, 0.0), 1.0))
            if confidence < 0.60:
                st.warning("Lower model score: treat this result cautiously and ask a human reviewer to inspect the image.")
            st.caption("Scores are model outputs, not calibrated probabilities or guarantees.")
    else:
        st.caption("Your prediction and confidence scores will appear here.")

with st.expander("Defect classes in this project"):
    st.markdown("""
    - **Crazing:** fine network-like surface cracks
    - **Inclusion:** embedded foreign particles
    - **Patches:** irregular surface patches
    - **Pitted surface:** small pits or cavities
    - **Rolled-in scale:** oxide scale pressed into the surface
    - **Scratches:** linear surface abrasions
    """)

st.divider()
st.caption("DeepVision AI • CNN image classification • Trained in Google Colab • Demo served locally")

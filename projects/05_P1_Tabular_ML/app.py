import joblib
import gradio as gr
import pandas as pd

model = joblib.load('model.pkl')

SEX = {
    "Female": 0,
    "Male": 1
}

CP = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}

FBS = {
    "No": 0,
    "Yes": 1
}

RESTECG = {
    "Normal": 0,
    "ST-T Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}

EXANG = {
    "No": 0,
    "Yes": 1
}

SLOPE = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}

THAL = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}

def predict(
    age,
    sex,
    cp,
    trestbps,
    chol,
    fbs,
    restecg,
    thalach,
    exang,
    oldpeak,
    slope,
    ca,
    thal,
):

    data = pd.DataFrame([{
        "age": age,
        "sex": SEX[sex],
        "cp": CP[cp],
        "trestbps": trestbps,
        "chol": chol,
        "fbs": FBS[fbs],
        "restecg": RESTECG[restecg],
        "thalach": thalach,
        "exang": EXANG[exang],
        "oldpeak": oldpeak,
        "slope": SLOPE[slope],
        "ca": ca,
        "thal": THAL[thal]
    }])

    probability = model.predict_proba(data)[0][1]
    prediction = model.predict(data)[0]

    if prediction == 1:
        diagnosis = "⚠️ High Risk of Heart Disease"
    else:
        diagnosis = "✅ Low Risk of Heart Disease"

    return (
        diagnosis,
        f"{probability:.2%}"
    )


with gr.Blocks(title="Heart Disease Prediction") as demo:

    gr.Markdown("# ❤️ Heart Disease Prediction")
    gr.Markdown("Enter patient information below.")

    with gr.Row():

        with gr.Column():

            age = gr.Slider(20,100,value=50,label="Age")

            sex = gr.Dropdown(
                choices=list(SEX.keys()),
                value="Male",
                label="Sex"
            )

            cp = gr.Dropdown(
                choices=list(CP.keys()),
                label="Chest Pain Type"
            )

            trestbps = gr.Slider(
                80,
                220,
                value=120,
                label="Resting Blood Pressure"
            )

            chol = gr.Slider(
                100,
                600,
                value=200,
                label="Cholesterol"
            )

            fbs = gr.Dropdown(
                choices=list(FBS.keys()),
                value="No",
                label="Fasting Blood Sugar >120"
            )

            restecg = gr.Dropdown(
                choices=list(RESTECG.keys()),
                value="Normal",
                label="Resting ECG"
            )

        with gr.Column():

            thalach = gr.Slider(
                60,
                220,
                value=150,
                label="Maximum Heart Rate"
            )

            exang = gr.Dropdown(
                choices=list(EXANG.keys()),
                value="No",
                label="Exercise-Induced Angina"
            )

            oldpeak = gr.Slider(
                0,
                6,
                step=0.1,
                value=1.0,
                label="Oldpeak"
            )

            slope = gr.Dropdown(
                choices=list(SLOPE.keys()),
                value="Flat",
                label="Slope"
            )

            ca = gr.Dropdown(
                choices=[0,1,2,3,4],
                value=0,
                label="Major Vessels"
            )

            thal = gr.Dropdown(
                choices=list(THAL.keys()),
                value="Normal",
                label="Thalassemia"
            )

    predict_btn = gr.Button("Predict", variant="primary")

    diagnosis = gr.Textbox(
        label="Prediction"
    )

    probability = gr.Textbox(
        label="Probability"
    )

    predict_btn.click(
        fn=predict,
        inputs=[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ],
        outputs=[
            diagnosis,
            probability
        ]
    )

demo.launch()
import gradio as gr
import pandas as pd
import numpy as np
import joblib

# Load the saved model and scaler
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')

def predict(network_packet_size, protocol_type, login_attempts, 
            session_duration, encryption_used, ip_reputation_score,
            failed_logins, browser_type, unusual_time_access):
    
    # Create a dataframe from inputs
    input_dict = {
        'network_packet_size': [network_packet_size],
        'login_attempts': [login_attempts],
        'session_duration': [session_duration],
        'ip_reputation_score': [ip_reputation_score],
        'failed_logins': [failed_logins],
        'unusual_time_access': [unusual_time_access],
        'protocol_type_ICMP': [1 if protocol_type == 'ICMP' else 0],
        'protocol_type_TCP': [1 if protocol_type == 'TCP' else 0],
        'protocol_type_UDP': [1 if protocol_type == 'UDP' else 0],
        'encryption_used_AES': [1 if encryption_used == 'AES' else 0],
        'encryption_used_DES': [1 if encryption_used == 'DES' else 0],
        'encryption_used_None': [1 if encryption_used == 'None' else 0],
        'browser_type_Chrome': [1 if browser_type == 'Chrome' else 0],
        'browser_type_Edge': [1 if browser_type == 'Edge' else 0],
        'browser_type_Firefox': [1 if browser_type == 'Firefox' else 0],
        'browser_type_Safari': [1 if browser_type == 'Safari' else 0],
        'browser_type_Unknown': [1 if browser_type == 'Unknown' else 0],
    }
    
    df = pd.DataFrame(input_dict)
    scaled = scaler.transform(df)
    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0]
    
    if prediction == 1:
        label = "⚠️ Attack Detected"
        confidence = f"{probability[1] * 100:.1f}%"
    else:
        label = "✅ Benign Session"
        confidence = f"{probability[0] * 100:.1f}%"
    
    return f"{label}\nConfidence: {confidence}"

# Build the Gradio interface
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Network Packet Size", value=500),
        gr.Dropdown(['TCP', 'UDP', 'ICMP'], label="Protocol Type", value='TCP'),
        gr.Number(label="Login Attempts", value=3),
        gr.Number(label="Session Duration", value=500),
        gr.Dropdown(['AES', 'DES', 'None'], label="Encryption Used", value='AES'),
        gr.Number(label="IP Reputation Score", value=0.5),
        gr.Number(label="Failed Logins", value=0),
        gr.Dropdown(['Chrome', 'Firefox', 'Edge', 'Safari', 'Unknown'], label="Browser Type", value='Chrome'),
        gr.Radio([0, 1], label="Unusual Time Access", value=0),
    ],
    outputs=gr.Textbox(label="LogSense Prediction"),
    title="🔍 LogSense — AI Security Triage",
    description="Enter network session details below to classify whether the session is benign or a potential attack.",
    examples=[
        [500, 'TCP', 3, 500, 'AES', 0.5, 0, 'Chrome', 0],
        [2000, 'UDP', 10, 1500, 'None', 0.9, 8, 'Unknown', 1],
    ]
)

demo.launch()
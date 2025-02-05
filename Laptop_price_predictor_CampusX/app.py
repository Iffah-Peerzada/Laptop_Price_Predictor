import streamlit as st
import pickle
import pandas as pd

# Load model and dataset via Pickle
pipe = pickle.load(open('pipe.pkl','rb'))
data = pickle.load(open('laptop_data.pkl','rb'))

# Title of the webpage
st.title("Laptop Price Predictor")

# Asking for input values from user and stroring in variables
company = st.selectbox('Brand',data['Company'].unique())
type = st.selectbox('type',data['TypeName'].unique())
ram = st.selectbox('RAM (in GB)',data['Ram'].unique())
weight = st.number_input('Weight of the Laptop')
touchscreen = st.selectbox('Touchscreen',['No','Yes'])
IPS = st.selectbox('IPS',['No','Yes'])

screen_size = st.number_input('Screen Size')
res = st.selectbox('Resolution',['1920x1080','1366x766','1600x900','3200x1800','3840x2160','2880x1800','2560x1600','2560x1440','2304x1440'])

cpu = st.selectbox('CPU Brand',data['CPU_Brand'].unique())
hdd = st.selectbox('HDD Brand',[0,128,256,512,1024,2048])
ssd = st.selectbox('SSD Brand',[0,8,128,256,512,1024])
gpu = st.selectbox('GPU Brand',data['Gpu_Brand'].unique())
graphic = st.selectbox('Graphic card',['No','Yes'])
os = st.selectbox('Operating System',data['Op_Sys'].unique())

# Executes the if loop when the 'Predict Price' button is pressed
if st.button('Predict Price'):

# Converting the string data of (yes/no) into binary (1/0) respectively
# This is done so as to match the datatype of the specific feature in dataset
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if graphic == 'Yes':
        graphic = 1
    else:
        graphic = 0

    if IPS == 'Yes':
        IPS = 1
    else:
        IPS = 0

# Calculating Pixels per Inches, since that is what re[resents screen size and resolution in the dataset
    X = int(res.split('x')[0])
    Y = int(res.split('x')[1])
    PPI = ((X**2) + (Y**2))**0.5/screen_size

#Now, we create a dictionary of all the feature values inputted by the user
# This allows us to pass 'query' and to run the prediction model on
    query = {
    "Company": company,
    "TypeName": type,
    "Ram": ram,
    "Weight": weight,
    "Touchscreen": touchscreen,
    "IPS": IPS,
    "PPI": PPI,
    "CPU_Brand": cpu,
    "HDD": hdd,
    "SSD": ssd,
    "Gpu_Brand": gpu,
    "Gpu_Graphic": graphic,
    "Op_Sys": os
    }

# Converting query into a dataframe since that is the datatype the model is expecting
    query = pd.DataFrame([query])

# Using title method to print the predicted price.
    st.title(pipe.predict(query))
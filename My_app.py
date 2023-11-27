import streamlit as st 
import pandas as pd 
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from PIL import Image
import pickle

st.set_page_config("Car Price Prediction ")

# title 
 
st.title("My Car Application")
 

# Add image
img = Image.open("Mercedes.jpg")
st.image(img, caption="cattie", width=500)


 #Read dataset
df=pd.read_csv("final_scout.csv")

  
#streamlit app 
html_temp = """
<div style="background-color:gray;padding:10px">
<h2 style="color:white;text-align:center;"> Car Prices Prediction with Streamlit  </h2>
</div>
         """
st.markdown(html_temp, unsafe_allow_html=True)

 
st.write("\n")
st.write("Welcome to Car Price prediction App")
menu_list = ['Explore Data', "Make a prediction"]
menu = st.radio("Select option:", menu_list)
if menu == ' Explore Data':
   st.title('Cars data details ')
if st.checkbox("show car details"):
   st.write(df)
elif menu == 'Make a prediction ':
 

  
 with st.sidebar:
  st.subheader('Car Specs to Predict Price')
make_model= st.sidebar.selectbox('Model Selection',options=['Audi A3', 'Audi A1', 'Opel Insignia', 'Opel Astra', 'Opel Corsa', "Renault Clio", "Renault Espace", "Renault Duster"])
hp_kW = st.sidebar.number_input("kW:",min_value=40, max_value=294, value=120, step=5)
age = st.sidebar.number_input("Age:",min_value=0, max_value=3, value=0, step=1)
km = st.sidebar.number_input("km:",min_value=0, max_value=317000, value=10000, step=5000)
Gears = st.sidebar.number_input("Gears:",min_value=5, max_value=8, value=5, step=1)
mileage = st.sidebar.number_input('Mileage')
fuel = st.sidebar.selectbox('Fuel Type', options=['Gasoline', 'Diesel', 'Hybrid', 'Electric'])
Gearing_Type = st.sidebar.radio("Gearing Type", ("Manual", "Automatic", "Semi-automatic"))


 # Load the trained machine learning model
model = pickle.load(open('final_model', 'rb'))
#transformer = pickle.load(open('transformer', 'rb'))
 

 # Collect user inputs into a dictionary
dict= {
   "make_model":make_model, 
   "hp_kW":hp_kW, 
    "age":age, 
   "km":km, 
   "Gears":Gears, 
    "Gearing_Type":Gearing_Type
}
df_pred = pd.DataFrame.from_dict([dict])

#########
cols = {
    "Car model":"make_model",
    "hp kW": "hp_KW",
    "Age": "age",
    "km Traveled ": "km ",
    "Gears": "Gears",
    "Gearing Type":"Gearing_Type"
}

df_show = df_pred.copy()
df_show.rename(columns = cols, inplace = True)
st.write("Make a prediction: \n")
st.table(df_show)

#df_final =transformer.fit_transform(df_show)

# Display the predicted price
   
if st.button("Predict"):
    predection = model.predict(df_show)
    col1, col2 = st.columns(2)
    col1.write("The estimated value of car price is €")
    col2.write(predection[0].astype(int))


st.write("\n\n")
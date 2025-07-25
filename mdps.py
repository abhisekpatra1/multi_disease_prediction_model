# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 03:21:37 2025

@author: Hp
"""
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model

diabetes_model=pickle.load(open('diabetes_trained_model.sav','rb'))

heart_model=pickle.load(open('heart_disease_trained_model.sav','rb'))

parkinsons_model=pickle.load(open('Parkinsson_disease_trained_model.sav','rb'))



#sidebar for navigation
with st.sidebar:
    
    selection = option_menu('Multiple Disease Prediction System',
                            ['Diabetes Prediction',
                             'Heart Disease Prediction',
                             'Parkinsson Disease Prediction'],
                            icons=['activity','heart','person'],
                            default_index=0)
    
#Diabetes Prediction page    
if selection=='Diabetes Prediction':
    
    #page titel
    st.title('Diabetes Prediction Using ML(SVM Model)')
    
    #getting the input data from user
    c1,c2,c3=st.columns(3)
    
    with c1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with c2:
        Glucose=st.text_input('Glucose Level')
    with c3:
        BloodPressure=st.text_input('Blood Pressure Value')
    with c1:
         SkinThickness=st.text_input('Skin Thickness Values')
    with c2:
         Insulin=st.text_input('Insulin Level')
    with c3:
         BMI=st.text_input('BMI Value')
    with c1:
         DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    with c2:
         Age=st.text_input('Age of person')
         
    #code for prediction
    dia_dignosis=''
    
    #creating a button 
    if st.button('Diabetes Test Result'):
        dia_pred=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if dia_pred[0]==1:
            dia_dignosis="The Person is Diabetic"
        else:
            dia_dignosis="The Person is not Diabetic"
            
            
    st.success(dia_dignosis)
    
    
    
 
#heart Disease Prediction page    
if selection=='Heart Disease Prediction':
    
    #page titel
    st.title('Heart Disease Prediction Using ML(Logistic Regression Model)')
    
    #getting the input data from user
    c1,c2,c3=st.columns(3)
    
    
    with c1:
        age=st.text_input('Age of Person')
    with c2:
        sex1=st.text_input('Sex of Person: Male/Female')
        if sex1=='Male':
            sex=1 
        else:
            sex=0
    with c3:
        cp=st.text_input('Chest Pain Type: 0/1/2/3')
    with c1:
        trestbps=st.text_input('Resting Blood Pressure')
    with c2:
        chol=st.text_input('Serum Cholestroal in mg/dl')
    with c3:
        fbs1=st.text_input('Fasting Blood Sugar')
        if fbs1>'120':
            fbs=1 
        else:
            fbs=0
    with c1:
        restecg=st.text_input('Resting Electrocardiographic : 0/1')
    with c2:
        thalach=st.text_input('Maximum Heart Rate achieved')
    with c3:
        exang1=st.text_input('Exercise Induced Angina: Yes/No')
        if exang1=='Yes':
            exang=1 
        else:
            exang=0
    with c1:
        oldpeak=st.text_input('ST depression induced by Exercise')
    with c2:
        slope=st.text_input('Slope of the peak exercise ST segment')
    with c3:
        ca=st.text_input('No.of Major vessels colored by flourosopy')
    with c1:
        thal=st.text_input('thal: 0=Normal; 1= Fixed defect; 2=Reversable defect ')
        
     # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
#Parkinsson Disease Prediction page    
if selection=='Parkinsson Disease Prediction':
    
    #page titel
    st.title('Parkinsson Disease Prediction Using ML(SVM Model)')
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    
    
    
    
    
    
    
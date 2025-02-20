### End to End ML Life cycle
    - Problem definition
    - Data Collection
    - Data Cleaning and preprocessing
    - EDA
    - Feature Engineering & selection
    - Model Selection
    - Model Training
    - Model Evaluation and Tuning
    - Model Deployment
    - Montoring & Maintenance


### Run the Fast api application 
    base) sathishkumarchandran@Sathishs-MacBook-Air end_2_end % python movies_fastapi_app.py 
    INFO:     Started server process [14617]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

### Run the Streamlit application     
    (base) sathishkumarchandran@Sathishs-MacBook-Air end_2_end % streamlit run movies_streamlit_app.py 

      You can now view your Streamlit app in your browser.

      Local URL: http://localhost:8501

### Swagger page
    http://localhost:8000/docs
    http://localhost:8000/docs#/default/predict_predict_post
    input - {"review":"The movie was fantastic"}
![mlops](img/swagger.png)   

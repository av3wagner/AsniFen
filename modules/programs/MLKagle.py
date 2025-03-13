import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score
from sklearn.preprocessing import StandardScaler
from sklearn.utils.multiclass import unique_labels

os.chdir("/mount/src/asnifen/")
sys.path.append("/mount/src/asnifen/")

def main():
    st.title("Heart Disease Classification")
    #st.sidebar.title("Heart Disease Classification")
    #st.markdown("Is patient has Heart disease")
    #st.sidebar.markdown("Is patient has Heart disease")

    @st.cache(persist=True)
    def load_data():
        data = pd.read_csv('/mount/src/asnifen/data/heart.csv')
        """
        labelencoder = LabelEncoder()
        for col in data.columns:
            data[col] = labelencoder.fit(data[col])
        """
        return data


    @st.cache(persist=True)
    def split(df):
        df1 = pd.get_dummies(df, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
        standardScalar = StandardScaler()
        columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
        df1[columns_to_scale] = standardScalar.fit_transform(df1[columns_to_scale])
        y = df1.target
        x = df1.drop(columns = ['target'], axis=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        return x_train, x_test, y_train, y_test

    def plot_metrics(metrics_list):
        if 'Confusion Matrix' in metrics_list:
            st.subheader('Confusion Matrix')
            plot_confusion_matrix(model, x_test, y_test, display_labels=class_names)
            st.pyplot()

        if 'ROC Curve' in metrics_list:
            st.subheader('ROC Curve')
            plot_roc_curve(model, x_test, y_test)
            st.pyplot()

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader('Precision-Recall Curve')
            plot_precision_recall_curve(model, x_test, y_test)
            st.pyplot()

    df = load_data()
    class_names = ['no', 'yes']
    #class_names = unique_labels(df.target)

    x_train, x_test, y_train, y_test = split(df)
    st.sidebar.subheader("Choose Classifier")
    #classifier = st.sidebar.selectbox("Classifier", ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

    classifier = "Support Vector Machine (SVM)"
    if classifier == 'Support Vector Machine (SVM)':
        #st.sidebar.subheader('Model Hyperparameters')
        C = 5.0            #st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_SVM')
        kernel = "sigmoid" #st.sidebar.radio("Kernel", ("rbf", "linear", "poly", "sigmoid"), key='kernel')
        gamma = "auto"     #st.sidebar.radio("Gamma (Kernel Coefficient)", ("scale", "auto"), key='gamma')

        #metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))
        #if st.sidebar.button("Classify", key='classify'):
            #st.subheader("Support Vector Machine (SVM) Results")
        
            model = SVC(C=C, kernel=kernel, gamma=gamma)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_pred = model.predict(x_test)
            st.write("Accuracy: ", accuracy.round(2))
            st.write("Precision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
            st.write("Recall: ", recall_score(y_test, y_pred, labels=class_names).round(2))
            #plot_metrics(metrics)
        
         st.write('Confusion Matrix')
         plot_metrics('Confusion Matrix')
        
         st.write('ROC Curve')
         plot_metrics('ROC Curve')
        
         st.write('Precision-Recall Curve')             
         plot_metrics('Precision-Recall Curve')

if __name__ == '__main__':
    main()

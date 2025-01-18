import json
EDA = {
 "tasks": [
  {
   "folder": "0",
   "Header": "Heading2",
   "topic": "Введение в EDA",
   "models": " ",
   "Text": "y",
   "Tab": " ",   
   "sec": "y"
  },
  {
   "folder": "1",
   "Header": "Heading3",
   "topic": "Набор данных для анализа",
   "models": " ",
   "Text": "y",
   "Tab": " ",   
   "sec": "y"
  },   
  {
   "folder": "2",
   "Header": "Heading3",
   "topic": "Преобразование категориальной переменной в числовую ",
   "models": " ",
   "Text": "y",
   "Tab": " ",   
   "sec": "y"
  },      
  {
   "folder": "101",
   "Header": "Heading3",
   "topic": "Таблица 1. Исходные данные для анализа",
   "models": "EDA101.PNG",
   "Text": "y",
   "Tab": " ",   
   "sec": "y"   
  },
  {
   "folder": "102",
   "Header": "Heading3",
   "topic": "Таблица 2.Дескриптивная статистика числовых переменных для всеx пациентов",
   "models": "EDA102.PNG",
   "Text": "y",
   "Tab": " ",   
   "sec": "y"
  },
  {
   "folder": "103",
   "Header": "Heading3",
   "topic": "Таблица 3.Распределение категориальных переменных по частоте для всеx пациентов",
   "models": "EDA103.PNG",
   "Text": "y",
   "Tab": " ",      
   "sec": ""
  },
  {
   "folder": "104",
   "Header": "Heading3",
   "topic": "Таблица 4. Основная статистика для переменной HeartDisease='Healthy'",
   "models": "EDA104.PNG",
   "Text": "y",
   "Tab": " ",      
   "sec": ""
  },
  {
   "folder": "105",
   "Header": "Heading3",
   "topic": "Таблица 5. Основная статистика для переменной HeartDisease='Heart Disease'",
   "models": "EDA105.PNG",
   "Text": "y",
   "Tab": " ",      
   "sec": ""
  },   
  {
   "folder": "3",
   "Header": "Heading3",
   "topic": "График №1. BoxPlot для всех числовых переменных по классу Заболевание (HeartDisease)",
   "models": "EDA1.PNG",
   "Text": "y",
   "Tab": " ",   
   "sec": "y"   
  },
  {
   "folder": "4",
   "Header": "Heading3",
   "topic": "График №2. BoxPlot для всех числовых переменных",
   "models": "EDA2.PNG",
   "Text": "y",
   "Tab": "6",   
   "sec": "y"
  },
  {
   "folder": "5",
   "Header": "Heading3",
   "topic": "График №3. Распределение числовых переменных по классу пол (Sex)",
   "models": "EDA3.PNG",
   "Text": "y",
   "Tab": "7",      
   "sec": ""
  },   
  {
   "folder": "6",
   "Header": "Heading3",
   "topic": "График №4. Гистограммы распределения для всех числовых переменных по классу Заболевание (HeartDisease)",
   "models": "EDA4.PNG",
   "Text": "y",
   "Tab": "8",      
   "sec": "y"
  },
  {
   "folder": "7",
   "Header": "Heading3",
   "topic": "График №5. Гистограммы распределения для всех числовых переменных по классу пол (Sex)",
   "models": "EDA5.PGN",
   "Text": "y",
   "Tab": "9",       
   "sec": "y"
  },
  {
   "folder": "8",
   "Header": "Heading3",
   "topic": "График №6. Двумерное распределение переменной 'HeartDisease' по классам Sex и RestingBP",
   "models": "EDA6.PNG",
   "Text": "y",
   "Tab": "10",       
   "sec": "y"
  },
  {
   "folder": "9",
   "Header": "Heading3",
   "topic": "График №7. График распределение переменной Cholesterol по Возрасту (Age)",
   "models": "EDA7.PNG",
   "Text": "y",
   "Tab": "11",       
   "sec": "y"
  },
  {
   "folder": "10",
   "Header": "Heading3",
   "topic": "График №8. Гистограммы распределения для всех числовых переменных, представленные на одном графике",
   "models": "EDA8.PNG",
   "Text": "y",
   "Tab": "12",       
   "sec": "y"
  },
  {
   "folder": "11",
   "Header": "Heading3",
   "topic": "График №9. Матрица корреляции Пирсона для числовых переменных",
   "models": "EDA9.PNG",
   "Text": "y",
   "Tab": "13",       
   "sec": "y"
  },
  {
   "folder": "12",
   "Header": "Heading3",
   "topic": "График №10. Гистограммы распределения для всех числовых переменных, в виде субграфиков на одной панели",
   "models": "EDA10.PNG",
   "Text": "y",
   "Tab": "14",       
   "sec": "y"
  },
  {
   "folder": "13",
   "Header": "Heading3",
   "topic": "График №11. Распределение переменной Cholesterol по классу (Age, Sex, FastingBS) в виде 4 субграфиков на одной панели",
   "models": "EDA11.PNG",
   "Text": "y",
   "Tab": "15",       
   "sec": "y"
  },
  {
   "folder": "14",
   "Header": "Heading3",
   "topic": "График №12. Распределение по возросту (Age) для переменных: 'Sex','ChestPainType','FastingBS','RestingECG','ExerciseAngina','ST_Slope','HeartDisease' в форме Виалин-графиков",
   "models": "EDA12.PNG",
   "Text": "y",
   "Tab": "16",           
   "sec": ""
  },
  {
   "folder": "15",
   "Header": "Heading3",
   "topic": "График №13. Распределение всех числовых переменных в виде субграфиков по классу 'HeartDisease' на одной панели",
   "models": "EDA13.PNG",
   "Text": "y",
   "Tab": "17",          
   "sec": "y"
  },
  {
   "folder": "16",
   "Header": "Heading3",
   "topic": "График №14. Распределение всех числовых переменных в виде столбиковых диаграмм как субграфиков по классу 'HeartDisease' на одной панели",
   "models": "EDA14.PNG",
   "Text": "y",
   "Tab": "18",           
   "sec": "y"
  },
  {
   "folder": "17",
   "Header": "Heading3",
   "topic": "График №15. Распределение численности пациентов по всем переменным в виде столбиковых диаграмм как субграфиков по классу пол (Sex) на одной панели",
   "models": "EDA15.PNG",
   "Text": "y",
   "Tab": "19",          
   "sec": "y"
  },
  {
   "folder": "18",
   "Header": "Heading3",
   "topic": "График №16. Биполярное распределение переменной Cholesterol по возрасту 'Age'",
   "models": "EDA16.PNG",
   "Text": "y",
   "Tab": " ",    
   "sec": "y"
  },
  {
   "folder": "19",
   "Header": "Heading3",
   "topic": "График №17. Биполярное распределение разного графического типа всех численных переменных на одной панели",
   "models": "EDA17.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "20",
   "Header": "Heading3",
   "topic": "График №18. Плотность распределения переменной Cholesterol по классу пол (Sex)",
   "models": "EDA18.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "21",
   "Header": "Heading3",
   "topic": "График №19. Распределение переменной Age возрастным группам в виде столбиковых диаграм по классу 'HeartDisease'",
   "models": "EDA19.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "22",
   "Header": "Heading3",
   "topic": "График №20. Распределение переменной Cholesterol по возрастным группам в виде столбиковых диаграм по классу 'HeartDisease'",
   "models": "EDA20.PNG",
   "Text": "y",
   "Tab": " ",      
   "sec": "y"
  },
 {
   "folder": "23",
   "Header": "Heading3",
   "topic": "График №21. Распределение переменной RestingBP по возрастным группам в виде столбиковых диаграм по классу 'HeartDisease'",
   "models": "EDA21.PNG",
   "Text": "y",
   "Tab": " ",      
   "sec": "y"
  },
  {
   "folder": "24",
   "Header": "Heading3",
   "topic": "График №22. Распределение переменной MaxHR по возрастным группам в виде столбиковых диаграм по классу 'HeartDisease'",
   "models": "EDA22.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "25",
   "Header": "Heading3",
   "topic": "График №23. Распределение переменной Oldpeak по возрастным группам в виде столбиковых диаграм по классу 'HeartDisease'",
   "models": "EDA23.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "26",
   "Header": " ",
   "topic": "График №24",
   "models": " ",
   "Text": "y",
   "Tab": " ",       
   "sec": " "
  },
  {
   "folder": "27",
   "Header": " ",
   "topic": "График №25",
   "models": "  ",
   "Text": "y",
   "Tab": " ",       
   "sec": " "
  },
  {
   "folder": "28",
   "Header": " ",
   "topic": "График №26",
   "models": " ",
   "Text": "y",
   "Tab": " ",       
   "sec": " "
  },
  {
   "folder": "29",
   "Header": " ",
   "topic": "График №27",
   "models": " ",
   "Text": "y",
   "Tab": " ",       
   "sec": " "
  },
  {
   "folder": "30",
   "Header": " ",
   "topic": "График №28",
   "models": " ",
   "Text": "y",
   "Tab": " ",       
   "sec": " "
  },
  {
   "folder": "31",
   "Header": " ",
   "topic": "График №29",
   "models": " ",
   "Text": "y",
   "Tab": " ",       
   "sec": " "
  },     
  {
   "folder": "32",
   "Header": " ",
   "topic": "График №30",
   "models": " ",
   "Text": "y",
   "Tab": " ",       
   "sec": " "
  },
  {
   "folder": "33",
   "Header": "Heading3",
   "topic": "График №24. Торт-диаграмма распределения пациентов по класс-переменной HeartDisease",
   "models": "EDA31.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "34",
   "Header": "Heading3",
   "topic": "График №25. Торт-диаграмма распределения пациентов по класс-переменной Sex",
   "models": "EDA32.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "35",
   "Header": "Heading3",
   "topic": "График №26. Столбиковая диаграмма распределения переменных: 'Sex', 'ChestPainType','FastingBS','RestingECG','ExerciseAngina',  'ST_Slope','HeartDisease' по категориям",
   "models": "EDA33.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "36",
   "Header": "Heading3",
   "topic": "График №27. Блок-бокс диаграмма распределения переменных: 'Sex', 'ChestPainType','FastingBS','RestingECG','ExerciseAngina',  'ST_Slope','HeartDisease' в виде субграфиков на одной панели по категориям",
   "models": "EDA34.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "37",
   "Header": "Heading3",
   "topic": "График №28. Столбиковая диаграмма распределения переменных: 'Sex', 'ChestPainType','FastingBS','RestingECG','ExerciseAngina',  'ST_Slope','HeartDisease' по категориям",
   "models": "EDA35.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "38",
   "Header": "Heading3",
   "topic": "График №29. Секторная диаграмма распределения переменной ChestPainType",
   "models": "EDA36.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "39",
   "Header": "Heading3",
   "topic": "График №30. Секторная диаграмма (2-го типа) распределения переменной ST_Slope",
   "models": "EDA37.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "40",
   "Header": "Heading3",
   "topic": "График №31. Комбинированная диаграмма распределения переменной пол (Sex)",
   "models": "EDA38.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "41",
   "Header": "Heading3",
   "topic": "График №32. Комбинированная диаграмма распределения переменной HeartDisease",
   "models": "EDA39.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "42",
   "Header": "Heading3",
   "topic": "График №33. Столбиковая диаграмма распределения переменных: 'Sex', 'ChestPainType','FastingBS','RestingECG','ExerciseAngina',  'ST_Slope' по категориям и классу 'HeartDisease'",
   "models": "EDA40.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },   
  {
   "folder": "43",
   "Header": "Heading3",
   "topic": "График №34. Столбиковая диаграмма распределения переменных: 'ChestPainType','FastingBS','RestingECG','ExerciseAngina',  'ST_Slope' по категориям и классу 'Sex'",
   "models": "EDA41.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "44",
   "Header": "Heading3",
   "topic": "График №35. Столбиковая диаграмма распределения переменных:  'Sex','FastingBS','RestingECG','ExerciseAngina','ST_Slope', 'HeartDisease' по категориям и классу 'ChestPainType'",
   "models": "EDA42.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "45",
   "Header": "Heading3",
   "topic": "График №36. Комбинированная (столбиковая и секторная) диаграмма распределения переменной пол (Sex)",
   "models": "EDA43.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "46",
   "Header": "Heading3",
   "topic": "График №37. Комбинированная (столбиковая и секторная) диаграмма распределения переменной ChestPainType",
   "models": "EDA44.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },
  {
   "folder": "47",
   "Header": "Heading3",
   "topic": "График №38. Комбинированная (столбиковая и секторная) диаграмма распределения переменной RestingECG",
   "models": "EDA45.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },   
   {
   "folder": "48",
   "Header": "Heading3",
   "topic": "График №39. Комбинированная (столбиковая и секторная) диаграмма распределения переменной ExerciseAngina",
   "models": "EDA46.PNG",
   "Text": "",
   "Tab": " ",       
   "sec": "y"
  },     
   {
   "folder": "49",
   "Header": "Heading3",
   "topic": "График №40. Комбинированная (столбиковая и секторная) диаграмма распределения переменной ST_Slope",
   "models": "EDA47.PNG",
   "Text": "",
   "Tab": " ",       
   "sec": "y"
  },     
   {
   "folder": "50",
   "Header": "Heading3",
   "topic": "График №41. Комбинированная (столбиковая и секторная) диаграмма распределения переменной Cholesterol_Category",
   "models": "EDA48.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },     
   {
   "folder": "51",
   "Header": "Heading3",
   "topic": "График №42. Комбинированная (столбиковая и секторная) диаграмма распределения переменной RestingBP_Category",
   "models": "EDA49.PNG",
   "Text": "",
   "Tab": " ",       
   "sec": "y"
  },     
   {
   "folder": "52",
   "Header": "Heading3",
   "topic": "График №43. Двойная секторная диаграмма (Sunburst, 6 субграфиков) распределения пар переменных: ['ChestPainType', 'FastingBS'], ['ST_Slope', 'RestingECG'], ['ExerciseAngina', 'ChestPainType'] по классу пол (Sex)",
   "models": "EDA50.PNG",
   "Text": " ",
   "Tab": " ",       
   "sec": "y"
  },     
   {
   "folder": "53",
   "Header": "Heading3",
   "topic": "График №44. Столбиковая диаграмма распределения переменных: RestingECG, ChestPainType (2 субграфика на одной панели) по классу пол (Sex)",
   "models": "EDA51.PNG",
   "Text": "y",
   "Tab": " ",       
   "sec": "y"
  },     
   {
   "folder": "54",
   "Header": "Heading3",
   "topic": "График №45. Столбиковая диаграмма распределения переменных: ST_Slope, ExerciseAngina (2 субграфика на одной панели) по классу пол (Sex)",
   "models": "EDA52.PNG",
   "Text": "",
   "Tab": " ",       
   "sec": "y"
  }, 
  {
   "folder": "55",
   "Header": "Heading2",
   "topic": "Заключение (EDA)",
   "models": " ",
   "Text": "y",
   "Tab": " ",   
   "sec": "y"
  },   
 ]
}

with open(eda_json, "w", encoding="utf-8") as file_handle:
    json.dump(EDA, file_handle, indent=4)   
    
################# ASNI-Json ###################
Asni = { 
    'Projekt': 'Asfendiyarov Kazakh National Medical University',
    'Projekt2': 'Statistik und Data Science Projekt',
    'Projekt3': 'Практическое применение Автоматизированной системы научных исследований в медицине, здравоохранении и смежных областях',
    'Thema': 'Анализ факторов риска сердечно сосудистых заболеваний и прогноз исходов лечения при помощи методов Машинного Обучения',
    'Forscher': 'Dr. Alexander Wagner (Berlin)', 
    'Site' : 'Berlin-Almaty',
    'Year' : str(year),
    "tasks" : [
        {
            "folder" : "0",
            "Header" : " ",
            "topic" : "Содержание",
            "models" : " ",
            "Text" : " " 
        },
        {
            "folder" : "0",
            "Header" : "BuiltinStyle.Heading2",
            "topic" : "Предисловие",
            "models" : " ",
            "Text" : "Kap0" 
        },
        {
            "folder" : "1",
            "Header" : "BuiltinStyle.Heading2",
            "topic" : "Введение",
            "models" : " ",
            "Text" : "Kap1" 
        },
        {
            "folder" : "2",
            "Header" : "BuiltinStyle.Heading2",
            "topic" : "Цель исследования",
            "models" : " ",
            "Text" : "Kap2"  
        },
        {
            "folder" : "3",
            "Header" : "BuiltinStyle.Heading2",
            "topic" : "Материалы и методы",
            "models" : " ",
            "Text" : "Kap3" 
        },
        {
            "folder" : "4",
            "Header" : "BuiltinStyle.Heading3",
            "topic" : "Исходные данные и их организация",
            "models" : " ",
            "Text" : "Kap4" 
        },
        {
            "folder" : "5",
            "Header" : "BuiltinStyle.Heading3",
            "topic" : "Предварительный анализ данных",
            "models" : " ",
            "Text" : "Kap5" 
        },
        {
            "folder" : "6",
            "Header" : "BuiltinStyle.Heading3",
            "topic" : "Моделирование",  
            "models" : [
                    'Linear Regression', 
                    'Logistic Regression',
                    'Perceptron',
                    'Linear SVC', 
                    'MLPClassifier', 
                    'Decision Tree Classifier 1', 
                    'Stochastic Gradient Decent', 
                    'RidgeClassifier', 
                    'BaggingClassifier', 
                    'AdaBoostClassifier 1', 
                    'GradientBoostingClassifie',
                    'KNeighborsClassifier',
                    'DecisionTreeClassifier 2',
                    'RandomForestClassifier',
                    'XGBClassifier',
                    'AdaBoostClassifier 2',
                    'Naive Bayes',    
                    'SVC' ], 
            
            "Text" : "Kap6"  
         },
        {
            "folder" : "7",
            "Header" : "BuiltinStyle.Heading3",
            "topic" : "Результаты моделирования",  
            "models" : " ",
            "Text" : "Kap7" 
        },
        {
            "folder" : "8",
            "Header" : "BuiltinStyle.Heading3",
            "topic" : "Оценка моделей и рекомендации",  
            "models" : " ",
            "Text" : "Kap8" 
        },
        
        {
            "folder" : "9",
            "Header" : "BuiltinStyle.Heading2",
            "topic" : "Обсуждение и выводы",  
            "models" : " ",
            "Text" : "Kap9" 
        },
     {
            "folder" : "10",
            "Header" : "BuiltinStyle.Heading2",
            "topic" : "Заключение",  
            "models" : " ",
            "Text" : "Kap10" 
        },   
        {
            "folder" : "11",
            "Header" : "BuiltinStyle.Heading2",
            "topic" : "Литература",
            "models" : " ",
            "Text" : "Kap11" 
        },
        {
            "folder" : "12",
            "Header" : "BuiltinStyle.Heading2",
            "topic" : "Приложение",
            "models" : " ",
            "Text" : "Kap12" 
        },
     ],
} 

with open(config_json, "w", encoding="utf-8") as file_handle:    
    json.dump(Asni, file_handle, indent=4)   

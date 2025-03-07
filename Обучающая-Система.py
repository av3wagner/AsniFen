import streamlit as st  
import streamlit.components.v1 as components
from  PIL import Image
import numpy as np
import pandas as pd
import base64
import sys
import inspect, os
import pathlib
from os import listdir
from os.path import isfile, join
import glob

st.set_page_config(
    page_title="Asfendijarov Kazakh National Medical University «АСНИ-МЕД»",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


Part1 = '''## Краткое описание системы

### Содержание

[Преамбула](#abc)

[Цель создание системы](#abd)

[Назначение системы](#abe)

[Область применения системы2](#abf)

[Задачи решаемые при помощи системы](#abg)

[Результаты применения системы](#abh)

[Необходимые условия и рессурсы для создания системы](#abi)

[Сроки создания системы](#abj)

[Организация работ по созданию системы](#abk)

[Примечание](#abl)
'''

Part2 = '''### Преамбула

Уважаемые колеги и пользователи системы!

Научная работа – это наиболее сложная человеческая деятельность, для её успешного проведения требуются не только личные качества, но и соответствующий инструментарий\. Прежде всего это научные данные и средства их анализа\. В медико\-сооциальных исследованиях этим инструментарием являются Биостатистика со всем набором современных методов анализа и прогноза данных и ситуаций и современные компьютерные системы, позволяющие это реализовать\.

К сожалению, освоение этого технического инструментария требует больших затрат времени и не всем желающим это в силу различных причин удаётся\. Эта проблема существует уже долгие годы и на протяжении длительного времени как крупные компании так и небольшие организации испытывают постоянную потребность в квалифицированных Биостатистиках, к сожаление, их поиск довольно трудное дело и не всегда завершается успехом\. В то же время, привлечение специализированных организаций и Freelancer\(oв\) стоит дорого и не гарантируют от неудач\.

За многие десятилетия работы в роли Биостатистика и Data Scientist\(а\) в различных фирмах разной величины и масштаба и в разных странах у меня неоднократно возникала идея о необходимости автоматизировать процесс анализа данных\. Мне удалось реализовать несколько таких проектов и внедрить их в нескольких организациях\. С примером одной из таких систем демонстрировавшейся на научной конференции \(2019\), можно познакомится по ссылке:

[https://saswiki\.de/display/KONFERENZEN/KSFE\+2019?preview=/19726371/19726410/23\_KSFE\_2019\_Wagner\_\-\_Ein\_SAS\_basiertes\_System\_zur\_automatisierten\_Auswertung\_und\_Berichterstellung\_von\_klinischen\_Studien\.pdf](https://saswiki.de/display/KONFERENZEN/KSFE+2019?preview=/19726371/19726410/23_KSFE_2019_Wagner_-_Ein_SAS_basiertes_System_zur_automatisierten_Auswertung_und_Berichterstellung_von_klinischen_Studien.pdf)

С учетом накопленного опыта и в условиях появления новых возможностей в Информационных Технологиях, в том числе Web\-технологий и Искуственного Интеллекта, возникли хорошие возможности для создания АСНИ собственными силамии и в реальные сроки\. Считаю своим долгом предложить вашему вниманию концепт этой системы\.
'''

Part3 = '''### Цель создание системы

Главная цель создание системы заключается в упрощении и облегчении процесса анализа медико\-социальных данных и построение моделей прогноза ситуаций в процессах, происходящих в медицине, здравоохранении и в смежных областях \(в медицинском страховании, в фармоиндустрии и т\.п\.\)

Цель реализуется через предоставлению следующих возможностей пользователю:

- Простой и беспроблемный доступа к Базе статистических знаний
- Запуск типовых программ Анализа данных без необходимости инсталляции специальных статистических систем на пользовательском компьютере
- Самостоятельное решение своих \(научных\) проблем по Анализу медицинских данных
- Предоставление других услуг
'''

Part4 = '''### Назначение системы

Система предназначена для широкого круга пользователя, в том числе:

- Студентов медицинских факультетов
- Аспирантов и докторантов медицинских факультетов
- Научных работников сферы здравоохранения
- Администраторов здравоохранения
- Сотрудников специализированных организаций, занимающихся анализом данных клинических исследований \(Clinical Trials, [https://en\.wikipedia\.org/wiki/ClinicalTrials\.gov](https://en.wikipedia.org/wiki/ClinicalTrials.gov)\)\.
- Других пользователей
'''
Part5 = '''### Область применения системы

Данная Система предусмотрена для использования на всех уровнях управления\. Это означает, что как на государственном \(с расширенным функциональным набором\), так и на областных/территориальных уровнях система работает идентично\. Привелигированный пользователь может использовать без ограничения все данные и возможности системы\. 

Другие пользователи имеют доступ только к данным конкретной области\. Система построена по модульному принципу и является открытой для развития и расширения\.
'''
Part6 = '''### Задачи решаемые при помощи системы

*При помощи АСНИ решаются следующие задачи:*

- Визуальный анализ данных при помощи интерактивных графиков и таблиц различного типа и свойста, отоброжающих в динамическом режиме например, состояние основных показателей здоровья населения территории
- Составление аналитических отчетов о состоянии параметров и показателей управляемого объекта, например, здоровья населения территории
- Научный анализ данных и прогноз при помощи современных средств продвинутой статистики \(Advanced Statistics\) и методов Искуственного Интеллекта
- Построения моделей оптимизации работы отрасли или организации
- Другие оперативные и стратегические задачи

*Методы решения задач АСНИ*

Для решения поставленных задач АСНИ используются методы:

- Агрегации данных и создания многомерных отчетов
- Визуализации данных \(динамические графики, карты, пр\.\)
- Классической прикладной математической статистики
- Методы статистического моделирования, в том числе Монте Карло
- Методы Доказательной медицины \(Evidence Based Medicine\)
- Методы Экономической медицины \(Health Economics\)
- Методы Искуственного Интелекта, в том числе: Машинного обучения\(Machine learning\), глубокого обучения\(Deep learning\)
- Математические Методы оптимитзации \(Operations Research\) 
- Эвристические методы
'''
Part7 = '''### Результаты применения системы

Результатами являются:

- Отчеты научно\-исследовательских работ
- Статьи и презентации на научно\-практических конференциях
- Диссертационные работы
- Отчеты плановых и коммерческих проектных работ
- Другие формы выходных результатов научных и проектных работ
'''
Part8 = '''### Необходимые условия и рессурсы для создания системы

- Главным и необходимым условием реализации данного проекта является заинтересованность всех участников в данной работе и её результатах
- Правовая, финансовая, административная, общественная, медийная и пр\. поддержка даного проекта
- Оптимальное обеспечение работ необходимыми квалифицированными трудовыми рессурсами
- Оптимальное обеспечение работ необходимыми программно\-техническими средствами
- Оптимальное обеспечение работ другими по мере необходимости рессурсами
'''

Part9 = '''### Сроки создания системы

- При условия выполнения условий П.6 работа по созданию системы может быть выполнена в течении 8-10 календарных месяцев (Этап №1)
- Развитие, модернизация и программно-техническое обслуживание Системы предполагается осуществлять непрерывно по мере необходимости, согласно плана
'''

Part10 = '''### Организация работ по созданию системы

Создание рабочего коллектива из представителей заказчика и исполнителя  из 2-4 человек (на первом этапе), обладающих необходимой научно-практической квалификацией и многолетним опытом создания и внедрения в практику аналогичных систем в стране заказчика и за рубежом
'''

Part11 = '''### Примечание разработчика «АСНИ-Обучение» 
В конце октября 2023г. началась практическая реализация данного проекта как личной инициативы. Любые заинтересованные лица и организации могут принять участие или оказывать посильную помощь в деле реализации этого проекта. В его успехе у разработчика нет сомнений, существуют вероятные причины негативных воздействий среды и личных обстоятельств, которые, как показывает практика, могут повлиять на сроки реализации проекта\. 

__*Материалы этого проекта могут служить хорошей основой для диссертаций как в области Информатики, так и Медицины. Для этого протребуется не более полугода работы, чтобы привести материалы проекта к стандартам диссертационных работ. Разработчик системы мог бы оказать необходимую помощь в этом*__

__Берлин, 16\.02\.2025__
'''

with open("/mount/src/asnifen/WagnerFoto.jpg", "rb") as img_file:    
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
	
with open("/mount/src/asnifen/ASFEN_LOGO3.png", "rb") as img_file:
        img2 = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()        

def MdFileToStreamlit(MdFile):
    with open(MdFile, 'r', encoding='utf-8') as f:
        readme_line = f.readlines()
        readme_buffer = []
        resource_files = [os.path.basename(x) for x in glob.glob(f'Resources/*')]

    for line in readme_line :
        readme_buffer.append(line) 
        for image in resource_files:
            if image in line:
                st.markdown(''.join(readme_buffer[:-1])) 
                st.image(f'Resources/{image}')
                readme_buffer.clear()

    st.markdown(''.join(readme_buffer))    

def ASNISystem(): 
    col1, col2, col3 = st.columns( [1, 20, 1])
    with col2:  
        st.markdown(Part1)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abc"}</h6>', unsafe_allow_html=True)

        st.markdown(Part2)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abd"}</h6>', unsafe_allow_html=True)

        st.markdown(Part3)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abe"}</h6>', unsafe_allow_html=True)

        st.markdown(Part4)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abf"}</h6>', unsafe_allow_html=True)

        st.markdown(Part5)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abg"}</h6>', unsafe_allow_html=True)

        st.markdown(Part6)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abh"}</h6>', unsafe_allow_html=True)

        st.markdown(Part7)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abi"}</h6>', unsafe_allow_html=True)

        st.markdown(Part8)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abj"}</h6>', unsafe_allow_html=True)

        st.markdown(Part9)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abk"}</h6>', unsafe_allow_html=True)

        st.markdown(Part10)
        st.markdown(f'<h6 style="color:#111111;font-size:4px;">{"abl"}</h6>', unsafe_allow_html=True)
        st.markdown(Part11)

#Информиация об авторе    
def welcome():
    col1, col2, col3 = st.columns( [1, 40, 1])
      
    with col1:              
        st.markdown("")
    with col2:  
        st.write(f"""
        <div class="container">
            <div class="box">
                <div class="spin-container">
                    <div class="shape">
                        <div class="bd">
                            <img src="{img}" alt="AW" width="150" height="200" style="display: block; margin: auto">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True)
                
        st.markdown("")
        MdFileToStreamlit("/mount/src/asnifen/AWresume.md")
        
    with col3:              
        st.markdown(""" <style> .font {
        font-size:10px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font"> </p>', unsafe_allow_html=True)
        

col1, col2, col3 = st.columns( [1, 40, 1])
with col2:  
    st.markdown(f'<h1 style="color:yellow;font-size:36px;text-align:center">{"Asfendijarov Kazakh National Medical University"}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="color:yellow;font-size:28px;text-align:center">{"Автоматизировання Обучающая Система Научных Исследований в медицине и здравоохранении «АСНИ-Обучение»"}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h2 style="color:white;font-size:24px;text-align:center">{"Система для любознательных и настойчивых"}</h2>', unsafe_allow_html=True)
    st.markdown("")
    st.title("Добро пожаловать в АСНИ-Обучение!")
    st.markdown("""
        АСНИ-Обучение - это система с открытым исходным кодом, помогающее пользователям применять избранные методы машинного обучения
        такие как поиск данных, предварительная обработка и построение моделей, создание научных отчетов и отчетов о проведении анализа 
        клинических исследований (Clinical trials), другие процедуры. 
        Самая важное в этой системе заключается в том, что вы можете делать всё это БЕЗ программирования! 
        """)
          


with st.expander("1. Информация об АСНИ-Обучение", expanded=True):
    ASNISystem()


with st.expander("2. Собрание избранных статей из области биостатистики и Data Science"):
    st.title('Собрание избранных статей из области биостатистики и Data Science')
    st.markdown("### :blue[Внимание: Статьи окончательно не упорядочены по рубрикам!]")
    st.write('''
    Эти статьи дают общие сведения о вышеназванных областях и могут быть хорошим справочным материалом для различных категорий пользователей.

    Приведенный в статьях программый код может быть адаптирован и использован в учебных целях и для реализации научных пароектов.  
    
    Если в статье есть ссылка на GitHub Repositorium, то было бы полезно клонировать этот Repositorium на персональный компьютер и исползовать
    его в своих учебных и научных целях.
    ''')
    
    col1, col2, col3 = st.columns( [1, 40, 1])
    with col2:  
        st.markdown("")
        MdFileToStreamlit("/mount/src/asnifen/ArtikelList.md")

with st.expander("3. Информиация об авторе АСНИ-МЕД"):
    welcome()


def expander_label(idx):
	hvar = f"""<script>
				var elements = window.parent.document.querySelectorAll('.streamlit-expanderHeader');
				elements[{idx}].style.color = 'rgba(255, 255, 255, 1)';
				elements[{idx}].style.fontFamily = 'sans-serif';
				elements[{idx}].style.fontSize = 'large';
			</script>"""

	components.html(hvar, height=0, width=0)

for idx in range(3):
	expander_label(idx)

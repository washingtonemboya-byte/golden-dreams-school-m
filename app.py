import streamlit as st
import pandas as pd
from datetime import date
st.set_page_config(page_title="Golden Dreams Model School", layout="wide")
st.markdown("<h1 style='text-align:center;color:#004aad;'>GOLDEN DREAMS MODEL SCHOOL</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>MBOYASOFT | 30+30+40=100 | {date.today()}</p>", unsafe_allow_html=True)
def get_grade(m):
    try:
        m=float(m)
        if m>=80: return "A"
        elif m>=75: return "A-"
        elif m>=70: return "B+"
        elif m>=65: return "B"
        elif m>=60: return "B-"
        elif m>=55: return "C+"
        elif m>=50: return "C"
        else: return "D"
    except: return ""
if "df" not in st.session_state:
    st.session_state.df=pd.DataFrame([{"ADM":"GD001","Student Name":"Brian Otieno","Class":"Class 5","CAT1_30":24,"CAT2_30":22,"ENDTERM_40":34,"Total Fees":15000,"Paid":10000},{"ADM":"GD002","Student Name":"Aisha Ali","Class":"Class 5","CAT1_30":20,"CAT2_30":18,"ENDTERM_40":25,"Total Fees":15000,"Paid":15000}])
edited=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True)
edited["FINAL_100"]=edited["CAT1_30"].fillna(0)+edited["CAT2_30"].fillna(0)+edited["ENDTERM_40"].fillna(0)
edited["GRADE"]=edited["FINAL_100"].apply(get_grade)
edited["Balance"]=edited["Total Fees"].fillna(0)-edited["Paid"].fillna(0)
st.dataframe(edited, use_container_width=True)
st.download_button("Download CSV", edited.to_csv(index=False).encode(), "Golden_Dreams.csv", "text/csv")

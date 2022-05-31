import streamlit as st
import pandas as pd


def run_serch() :

    df_pivot = pd.read_csv('data/df_pivot.csv')
    df = pd.read_csv('data/df.csv')

    col = df_pivot.columns[1:]
    choice_movie = st.selectbox('별점매길 영화 선택', col)
    choice_rating = st.selectbox('별점 선택', range(1, 5+1))

    # 저장하려면? 함수써보자
    # def save() :        

    #     df2 = df.append( { 'title' : choice_movie , 'userId' : 999, 'rating' : float(choice_rating) }, ignore_index=True )
        
    #     return df2 
        # st.dataframe(df.loc[ df['userId'] == 999 , ])

        # if st.button('상관계수값 보기') :
        #     df_pivot = df.pivot_table(values='rating', index='userId', columns= 'title')

        # st.dataframe(df_pivot)

    if st.button('저장하기') :
        df2 = df.append( { 'title' : choice_movie , 'userId' : 999, 'rating' : float(choice_rating) }, ignore_index=True )
        
        st.dataframe(df2.loc[ df2['userId'] == 999 , ])

        st.dataframe(df2)
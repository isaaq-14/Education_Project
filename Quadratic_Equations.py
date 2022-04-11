import math
import streamlit as st
from PIL import Image

disc = Image.open('discriminant.jpg')
eq = Image.open('Quadratic-Equation-3.jpg')

feed_neg = Image.open('neg.jpg')
feed_pos = Image.open('pos.jpg')

with st.sidebar:
    st.header('Quadratic Equations Calculator')

a_inp = st.sidebar.text_input('Enter A: ')
b_inp = st.sidebar.text_input('Enter B: ')
c_inp = st.sidebar.text_input('Enter C: ')


def discriminant(a, b, c):
    if (b ** 2 - (4 * a * c)) < 0:
        root_u = (b ** 2 - (4 * a * c))
        st.text('Discriminant is negative, roots are unreal.\nDiscriminant: ')
        st.text(root_u)
        return ''
    elif (b ** 2 - (4 * a * c)) == 0:
        root_z = (b ** 2 - (4 * a * c))
        st.text('Discriminant is equal to zero, there is only 1 root.\nDiscriminant: ')
        st.text(root_z)
        return ''
    else:
        root_r = (b ** 2 - (4 * a * c))
        st.text('Discriminant is positive -\nthere are 2 distinct real roots.\n\nDiscriminant: ')
        st.text(root_r)
        return ''


def roots(a, b, c):
    b_neg = -abs(b)
    if (b ** 2 - (4 * a * c)) < 0:
        st.text('\nERROR:- Equation has Unreal Roots')
        return ''
    else:
        root_1 = (b_neg + math.sqrt((b ** 2 - (4 * a * c)))) / 2 * a
        root_2 = (b_neg - math.sqrt((b ** 2 - (4 * a * c)))) / 2 * a
        root_abs_1 = abs(root_1)
        root_abs_2 = abs(root_2)
        st.text(root_abs_1)
        st.text(root_abs_2)
        return ''


options = st.sidebar.multiselect(
    'What would you like to know?',
    ['Discriminant', 'Roots'])

col1, col2 = st.columns(2)

if options == ['Discriminant']:
    with col1:
        st.header('Discriminant')
        discriminant(int(a_inp), int(b_inp), int(c_inp))
        st.image(disc, 'Formula')

elif options == ['Roots']:
    with col1:
        st.header('Roots')
        st.text(roots(int(a_inp), int(b_inp), int(c_inp)))
        st.image(eq, 'Formula')

elif options == ['Roots', 'Discriminant'] or options == ['Discriminant', 'Roots']:
    with col1:
        st.header('Discriminant')
        st.text(discriminant(int(a_inp), int(b_inp), int(c_inp)))
        st.image(disc, 'Formula')
    with col2:
        st.header('Roots')
        st.text(roots(int(a_inp), int(b_inp), int(c_inp)))
        st.image(eq, 'Formula')

with st.sidebar.expander('Did this help you?'):
    feed_pos_button = st.button('Yes')
    feed_neg_button = st.button('No')

    if feed_pos_button:
        st.balloons()
        st.image(feed_pos)
        st.text('Thank you for the feedback!')

    if feed_neg_button:
        st.image(feed_neg)
        st.text('Thanks for your feedback.')

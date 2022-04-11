import streamlit as st
import math


def rect_area(a, b):
    area = a * b
    return area


def rect_diag(a, b):
    diag = math.sqrt((a ** 2 + b ** 2))
    return diag


def sq_area(l):
    area = l * l
    return area


def sq_diag(a):
    diag = a * (math.sqrt(2))
    return diag


def hyp_rt(b, p):
    hypo = math.sqrt((b ** 2 + p ** 2))
    return hypo


def b_rt(h, p):
    base = math.sqrt(h**2 - p**2)
    return base


def p_rt(b, h):
    perp = math.sqrt((h - b) * (h + b))
    return perp


st.header('Mensuration')

with st.expander('Rectangle'):
    rect_opt = st.multiselect('What would you like to know?', ['Area', 'Diagonal'], key='Rectangle')
    if rect_opt == ['Area']:
        length = st.text_input('Enter length: ')
        breadth = st.text_input('Enter breadth: ')
        if length and breadth:
            a = rect_area(int(length), int(breadth))
            st.write('\n**Area**: ')
            st.write(a)
    elif rect_opt == ['Diagonal']:
        length = st.text_input('Enter length: ')
        breadth = st.text_input('Enter breadth: ')
        if length and breadth:
            d = rect_diag(int(length), int(breadth))
            st.write('\n**Diagonal**: ')
            st.write(d)
    elif rect_opt == ['Area', 'Diagonal'] or rect_opt == ['Diagonal', 'Area']:
        length = st.text_input('Enter length: ')
        breadth = st.text_input('Enter breadth: ')
        if length and breadth:
            a = rect_area(int(length), int(breadth))
            d = rect_diag(int(length), int(breadth))
            st.write('\n**Area**: ')
            st.write(a)
            st.write('\n**Diagonal**: ')
            st.write(d)

with st.expander('Square'):
    sq_opt = st.multiselect('What would you like to know?', ['Area', 'Diagonal'], key='Square')

    if sq_opt == ['Area']:
        length = st.text_input('Enter length: ')
        if length:
            st.write('\n**Area**: ')
            st.write(str(sq_area(int(length))))
    elif sq_opt == ['Diagonal']:
        area = st.text_input('Enter Area: ')
        if area:
            st.write('\n**Diagonal**')
            st.write(str(f'{sq_diag(int(area)):.2f}'))
    elif sq_opt == ['Area', 'Diagonal'] or sq_opt == ['Diagonal', 'Area']:
        length = st.text_input('Enter length: ')
        if length:
            area = sq_area(int(length))
            diag = sq_diag(area)
            st.write('\n**Area**')
            st.write(str(area))
            st.write(str('\n**Diagonal**'))
            st.write(str(f'{diag:.2f}'))

with st.expander('Right Angled Triangle'):
    rt_opt = st.multiselect('What would like you to know?', ['Hypotenuse', 'Base', 'Perpendicular'])
    err_ch = list(rt_opt)
    if rt_opt == ['Hypotenuse']:
        base = st.text_input('Enter Base: ')
        perp = st.text_input('Enter Perpendicular')

        if base and perp:
            hypo = hyp_rt(int(base), int(perp))
            st.write('\n**Hypotenuse**')
            st.write(str(hypo))

    elif rt_opt == ['Base']:
        hypo = st.text_input('Enter Hypotenuse: ')
        perp = st.text_input('Enter Perpendicular')

        if hypo and perp:
            base = b_rt(int(hypo), int(perp))
            st.write('\n**Base**')
            st.write(str(base))

    elif rt_opt == ['Perpendicular']:
        base = st.text_input('Enter Base')
        hypo = st.text_input('Enter Hypotenuse')

        if base and hypo:
            perp = p_rt(int(base), int(hypo))
            st.write('\n**Perpendicular**')
            st.write(perp)

    elif len(err_ch) > 0:
        st.write('\n**ERROR: Sorry, this is not possible**')

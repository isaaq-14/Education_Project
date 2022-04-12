import streamlit as st
import math
from PIL import Image

################
rect_img = Image.open('rect.png')
sq_img = Image.open('square.png')
rt_img = Image.open('rt.png')
tr_img = Image.open('tr.png')
et_img = Image.open('et.png')
it_img = Image.open('it.jpg')


rect_a_img = Image.open('rect_a.png')
rect_d_img = Image.open('rect_diag.png')

sq_a_img = Image.open('sq_a.png')
sq_d_img = Image.open('sq_d.png')

hyp_rt_img = Image.open('hyp_rt.png')
b_rt_img = Image.open('b_rt.png')
p_rt_img = Image.open('p_rt.png')

ar_tr_img = Image.open('ar_t.png')

h_et_img = Image.open('h_et.png')
a_et_img = Image.open('a_et.png')

a_it_img = Image.open('a_it.png')

a_p_img = Image.open('a_p.png')

a_rh_img = Image.open('a_rh.png')
################

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
    base = math.sqrt(((h - p) * (h + p)))
    return base


def p_rt(b, h):
    perp = math.sqrt((h - b) * (h + b))
    return perp


def a_t(b, h):
    area = (1 / 2) * (b * h)
    return area


def h_et(a):
    height = (a * (math.sqrt(3))) / 2
    return height


def ar_et(a):
    area = (a ** 2) * ((math.sqrt(3)) / 4)
    return area


def a_it(a, c):
    Area = (c / 4) * math.sqrt((4 * (a**2) - (c ** 2)))
    return Area


def ar_p(b, h):
    area = b*h
    return area


def ar_rh(d1, d2):
    area = (1/2)*(d1*d2)
    return area


st.header('Mensuration')

with st.expander('Rectangle'):
    rect_opt = st.multiselect('What would you like to know?', ['Area', 'Diagonal'], key='Rectangle')
    if rect_opt == ['Area']:
        length = st.text_input('Enter length: ')
        breadth = st.text_input('Enter breadth: ')
        if length and breadth:
            a = rect_area(float(length), float(breadth))
            st.write('\n**Area**: ')
            st.write(str(a))
            st.image(rect_a_img)

    elif rect_opt == ['Diagonal']:
        length = st.text_input('Enter length: ')
        breadth = st.text_input('Enter breadth: ')
        if length and breadth:
            d = rect_diag(float(length), float(breadth))
            st.write('\n**Diagonal**: ')
            st.write(str(d))
            st.image(rect_d_img)

    elif rect_opt == ['Area', 'Diagonal'] or rect_opt == ['Diagonal', 'Area']:
        length = st.text_input('Enter length: ')
        breadth = st.text_input('Enter breadth: ')
        if length and breadth:
            a = rect_area(float(length), float(breadth))
            d = rect_diag(float(length), float(breadth))
            st.write('\n**Area**: ')
            st.write(str(a))
            st.image(rect_a_img)
            st.write('\n**Diagonal**: ')
            st.write(str(d))
            st.image(rect_d_img)

with st.expander('Square'):
    sq_opt = st.multiselect('What would you like to know?', ['Area', 'Diagonal'], key='Square')

    if sq_opt == ['Area']:
        length = st.text_input('Enter length: ', key='Square_Length')
        if length:
            st.write('\n**Area**: ')
            st.write(str(sq_area(float(length))))
            st.image(sq_a_img)

    elif sq_opt == ['Diagonal']:
        area = st.text_input('Enter Area: ')
        if area:
            st.write('\n**Diagonal**')
            st.write(str(f'{sq_diag(float(area)):.2f}'))
            st.image(sq_d_img)

    elif sq_opt == ['Area', 'Diagonal'] or sq_opt == ['Diagonal', 'Area']:
        length = st.text_input('Enter length: ', key='Multi_Square')
        if length:
            area = sq_area(float(length))
            diag = sq_diag(area)
            st.write('\n**Area**')
            st.write(str(area))
            st.image(sq_a_img)
            st.write(str('\n**Diagonal**'))
            st.write(str(f'{diag:.2f}'))
            st.image(sq_d_img)

with st.expander('Right Angled Triangle'):
    rt_opt = st.selectbox('What would like you to know?', ('Hypotenuse', 'Base', 'Perpendicular'))
    # err_ch = list(rt_opt)
    if rt_opt == 'Hypotenuse':
        base = st.text_input('Enter Base: ')
        perp = st.text_input('Enter Perpendicular')

        if base and perp:
            hypo = hyp_rt(float(base), float(perp))
            st.write('\n**Hypotenuse**')
            st.write(str(hypo))
            st.image(hyp_rt_img)

    elif rt_opt == 'Base':
        hypo = st.text_input('Enter Hypotenuse: ')
        perp = st.text_input('Enter Perpendicular')

        if hypo and perp:
            if hypo >= perp:
                base = b_rt(float(hypo), float(perp))
                st.write('\n**Base**')
                st.write(str(base))
                st.image(b_rt_img)
            else:
                st.write('\n**ERROR: Hypotenuse cannot be smaller than or equal Perpendicular**')

    elif rt_opt == 'Perpendicular':
        base = st.text_input('Enter Base')
        hypo = st.text_input('Enter Hypotenuse')

        if base and hypo:
            if hypo >= base:
                perp = p_rt(float(base), float(hypo))
                st.write('\n**Perpendicular**')
                st.write(str(perp))
                st.image(p_rt_img)
            else:
                st.write('\n**ERROR: Hypotenuse cannot be smaller than Base**')

with st.expander('Triangles'):
    st.header('Area')
    tr_b = st.text_input('Enter Base: ', key='Tr_base')
    tr_h = st.text_input('Enter Height: ')

    if tr_b and tr_h:
        ar_t = a_t(float(tr_b), float(tr_h))
        st.write('Area = ', str(ar_t))
        st.image(ar_tr_img)

with st.expander('Equilateral Triangle'):
    et_opt = st.multiselect('What would you like to know?', ['Height', 'Area'], key='et-opt')

    if et_opt == ['Height']:
        a_et = st.text_input('Enter Hypotenuse: ', key='a-et')
        if a_et:
            height = h_et(float(a_et))
            st.write('Height = ', f'{height:.2f}')
            st.image(h_et_img)

    elif et_opt == ['Area']:
        a_et = st.text_input('Enter Hypotenuse: ', key='a-et-ar')
        if a_et:
            ar = ar_et(float(a_et))
            st.write('Area = ', f'{ar:.2f}')
            st.image(a_et_img)

    elif et_opt == ['Area', 'Height'] or et_opt == ['Height', 'Area']:
        a_et = st.text_input('Enter Hypotenuse: ', key='a-et-ar')
        if a_et:
            ar = ar_et(float(a_et))
            st.write('Area = ', f'{ar:.2f}')
            st.image(a_et_img)
            height = h_et(float(a_et))
            st.write('Height = ', f'{height:.2f}')
            st.image(h_et_img)

with st.expander('Isosceles Triangle'):
    st.header('Area')
    b = st.text_input('Enter Base: ', key='et-b')
    a = st.text_input('Enter Side: ')

    if a and b:
        ar_it = a_it(float(a), float(b))
        st.write('Area = ', f'{ar_it:.2f}')
        st.image(a_it_img)


with st.expander('Parallelograms'):
    st.header('Area')
    b = st.text_input('Enter Base: ', key='p-b')
    h = st.text_input('Enter Height: ', key='p-h')

    if h and b:
        ar_p = ar_p(float(h), float(b))
        st.write('Area = ', f'{ar_p:.2f}')
        st.image(a_p_img)

with st.expander('Rhombus'):
    st.header('Area')
    d1 = st.text_input('Enter 1st Diagonal: ', key='r-d1')
    d2 = st.text_input('Enter 2nd Diagonal: ', key='r-d2')

    if d1 and d2:
        ar_rh = ar_rh(float(d1), float(d2))
        st.write('Area = ', f'{ar_rh:.2f}')
        st.image(a_rh_img)

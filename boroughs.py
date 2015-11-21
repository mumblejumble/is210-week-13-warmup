#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""working with csv and json files"""


import csv
import json


R_GRADES = {
    'A': float(1.0),
    'B': float(0.90),
    'C': float(0.80),
    'D': float(0.70),
    'F': float(0.60)
}


def get_score_summary(filename):
    """This function reads data of restaurant inspection in csv file.

    Args:
        filename(str): csv file to open.

    Returns:
        a set of dictionary with total number and total average score of
        all grade receiving restaurants in boroughs of NYC.

    Examples:
        >>> get_score_summary('inspection_results.csv')
        {'BRONX': (156, 0.9762820512820514),
         'BROOKLYN': (417, 0.9745803357314141),
         'STATEN ISLAND': (46, 0.9804347826086955),
         'MANHATTAN': (748, 0.9771390374331531),
         'QUEENS': (414, 0.9719806763285017)}
    """
    c_open = open(filename, 'r')
    csv_read = csv.reader(c_open)
    key_camis = []
    value_bg = []
    for row in csv_read:
        camis = row[0]
        borough = row[1]
        grade_col = row[10]
        if grade_col != '' and grade_col != 'P' and grade_col != 'GRADE':
            grade_num = R_GRADES[grade_col]
            key_camis.append(camis)
            value_bg.append((borough, grade_num))
    insp_dict = dict(zip(key_camis, value_bg))
    c_open.close()

    m_counter = 0
    q_counter = 0
    b_counter = 0
    bx_counter = 0
    si_counter = 0
    m_score = 0
    q_score = 0
    b_score = 0
    bx_score = 0
    si_score = 0
    for value in insp_dict.itervalues():
        if value[0] == 'MANHATTAN':
            m_counter += 1
            m_score += value[1]
        elif value[0] == 'QUEENS':
            q_counter += 1
            q_score += value[1]
        elif value[0] == 'BROOKLYN':
            b_counter += 1
            b_score += value[1]
        elif value[0] == 'BRONX':
            bx_counter += 1
            bx_score += value[1]
        elif value[0] == 'STATEN ISLAND':
            si_counter += 1
            si_score += value[1]
    final_dict = {}
    final_dict['MANHATTAN'] = m_counter, m_score / m_counter,
    final_dict['QUEENS'] = q_counter, q_score / q_counter,
    final_dict['BROOKLYN'] = b_counter, b_score / b_counter,
    final_dict['BRONX'] = bx_counter, bx_score / bx_counter,
    final_dict['STATEN ISLAND'] = si_counter, si_score / si_counter
    return final_dict


def get_market_density(filename):
    """This functin counts total number of green markets for boroughs in NYC.

    Args:
        filename(str): json file to open.

    Returns:
        a set of dictionary with total number of green markets in boroughs of
        NYC.

    Example:
        >>> get_market_density('green_markets.json')
        {u'BRONX': 32, u'BROOKLYN': 48, u'STATEN ISLAND': 2, u'MANHATTAN': 39,
         u'QUEENS': 16}
    """
    j_open = open(filename, 'r')
    all_data = json.load(j_open)
    data = all_data['data']
    final_dict = {}
    for list_val in data:
        borough = list_val[8].strip().upper()
        if borough not in final_dict:
            boro_count = 1
            final_dict[borough] = boro_count
        else:
            boro_count += 1
            final_dict[borough] = boro_count
    j_open.close()
    return final_dict


def correlate_data(c_open, j_open, output='output.txt'):
    score_result = get_score_summary(f_file)
    market_result = get_market_density(j_file)
    cor_final = {}
    for s_key, s_value in score_result.iteritems:
        print s_key, s_value
        for m_key, m_value in market_result.iteritems:
            print m_key, m_value

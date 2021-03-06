#functions.py helper functions to calculate data

import numpy as np
import pandas as pd
import json

#
#functions
#


def create_labels_tabel(labels):
    """Creates a dict-label-table with labelcode

    Args:
        labels ([xlsx file]): [uploaded labels]

    Returns:
        [dict]: [labels]
    """
    labels = pd.read_excel(labels).to_numpy(dtype=str)
    new_labels=[]
    count = 0
    for x in labels:
        labelcode = count
        #name is in first column, ACV in the second
        label_name = x[0]
        labels_ACV = x[1]
        new_labels.append({'labelcode':labelcode, 'name':label_name, 'acv':labels_ACV})
        count = count + 1
    return new_labels


def create_grid_ladders(ladders):
    """Creates ladders table to be displayed in FE via grid

    Args:
        ladders ([xlsx file]): [uploaded ladders]

    Returns:
        [dict]: [clos and rows for grid-table]
    """
    ladders = pd.read_excel(ladders).to_numpy(dtype=str)

    cols = ['Id', 'Treatment', 'Implications']
    ladder_lenght = len(ladders[0])

    #calculate number of columns needed
    for x in range((ladder_lenght - 3)):
        cols.append('')

    #'nan' -> ''
    for row in range(len(ladders)):
        for entry in range(ladder_lenght):
            if (ladders[row][entry] == 'nan'):
                ladders[row][entry] = ladders[row][entry].replace('nan', '')
    
    #serialize ladders
    ladders = serialize_numpy(ladders)
    
    return {'cols':cols, 'rows':ladders}


def get_index_by_name(name, labels):
    """get index(=labelcode) of name

    Args:
        name ([String]): [name]
        labels ([dict]): [labels]

    Returns:
        [int]: [index]
    """
    index = int(-1)
    for x in labels:
        if (x.get('name')==name):
            index = x.get('labelcode')
            break

    if (index == -1):
        print(f"{name} is no label")
    else:
        return index

def get_name_by_index(index, labels):
    """get name with acv for index

    Args:
        index ([int]): [index/labelcode]
        labels ([dict]): [labels]

    Returns:
        [String]: [name (acv)]
    """
    name = ""
    acv = ""
    for x in labels:
        if (x.get('labelcode')==index):
            name = x.get('name')
            acv = x.get('acv')

    if (name==""):
        print(f"no matching name for {index}")
        return "X"
    else:
        return (name + " (" + acv + ")")


def add_implication(implication_matrix, index_from, index_to):
    """Increment implication from index_from to index_to

    Args:
        implication_matrix ([Array]): [matrix]
        index_from ([int]): [index from]
        index_to ([int]): [index to]
    """
    implication_matrix[index_from][index_to] = implication_matrix[index_from][index_to] + 1


#get direct implication matrix
def cal_direct_implication_matrix(implication_matrix_direct, ladders, labels, radio_treatments):
    """Calculates direct implication matrix

    Args:
        implication_matrix_direct ([Array]): [empty matrix]
        ladders ([Aray]): [ladders]
        labels ([dict]): [labels]
        radio_treatments ([String]): [selected treatment]

    Returns:
        [Aray]: [calculated/filled matrix]
    """

    running_index = 2
    countLadderColumn = len(max(ladders, key=len))
    for x in ladders:
        #include ladder if all, or the correct treatment is selected
        if (radio_treatments==x[1] or radio_treatments=='All'):

            #ID|treatment|first implication -> start at 2 (hardcoded)
            #countLadderColumn -1 because of x[running_index+1], last label has no implication
            for running_index in range(2, countLadderColumn -1):
                #if next is empty -> break
                if (x[running_index+1]== 'nan'):
                    break
                row_implication = x[running_index]
                column_implication = x[running_index+1]

                #add to direct implication matrix, self-implications are not added
                if (row_implication!=column_implication):
                    add_implication(implication_matrix_direct, get_index_by_name(row_implication,labels), get_index_by_name(column_implication, labels))

    return implication_matrix_direct


#get indirect implication matrix
def cal_indirect_implication_matrix(implication_matrix_indirect, ladders, labels, radio_treatments):
    """Calculates inirect and direct implication matrix

    Args:
        implication_matrix_indirect ([Array]): [empty matrix]
        ladders ([Aray]): [ladders]
        labels ([dict]): [labels]
        radio_treatments ([String]): [selected treatment]

    Returns:
        [Aray]: [calculated/filled matrix]
    """
    
    running_index = 2
    countLadderColumn = len(max(ladders, key=len))
    for x in ladders:
        #include ladder if all, or the correct treatment is selected
        if (radio_treatments==x[1] or radio_treatments=='All'):

            #id|treatment|first implication -> start at 2 (hardcoded)
            #countLadderColumn -1 because of x[running_index+1]
            for running_index in range(2, countLadderColumn - 1):
                row_implication = x[running_index]

                indirect_implications = set()

                #add indirect and direct implications to set -> indirect implications are only added once
                for y in range(running_index+1, countLadderColumn):
                    #if next is empty -> break
                    if (x[y]== 'nan'):
                        break
                    column_implication = x[y]
                    #add implication to set
                    indirect_implications.add(column_implication)

                #no self implications, row_implication is removed if exists 
                indirect_implications.discard(row_implication)
                #add indirect implications for row_implication to matrix
                for implication in indirect_implications:
                    add_implication(implication_matrix_indirect, get_index_by_name(row_implication, labels), get_index_by_name(implication, labels))

    return implication_matrix_indirect


def get_treatments(ladders):
    """Creates Array of all tretments listed in ladders

    Args:
        ladders ([Array]): [ladders]

    Returns:
        [Array]: [treatments]
    """
    treatments = []
    #treatments are saved in the second column
    for ladder in ladders:
        treatments.append(ladder[1])
    treatments = list(set(treatments))
    return treatments

def proposed_cut_off_value(cut_off_value, length):
    """Proposes a cutoff-value if cut_off_value < 0 (=default)

    Reynolds and Gutman (1988) recommend using a cut-off level of 3-5 for 50-60 paricipants
    --> 4/55: relation cut-off/ladders

    Args:
        cut_off_value ([int]): [cutoff-value ]
        length ([int]): [amount of ladders]

    Returns:
        [type]: [description]
    """
    
    if (int(cut_off_value) < 0):
        proposed_value = int(length*4/55)
        return proposed_value
    else:
        return cut_off_value


def calculate_network_data(inLadders, inLabels, radio_treatments, radio_in_direct, cut_off_value):
    """Calculates data needed to load/reload the hierarchical value map (vis.js network) based on Args

    Args:
        inLadders ([xlsx file]): [ladders]
        inLabels ([xlsx file]): [labels]
        radio_treatments ([String]): [selected treatment]
        radio_in_direct ([String]): [in/direct implications]
        cut_off_value ([int]): [cutoff-value]

    Returns:
        [dict]: [calculated matrix, labels, treatments, cutoff-value]
    """
    ladders = pd.read_excel(inLadders).to_numpy(dtype=str)
    labels=create_labels_tabel(inLabels)

    treatments = get_treatments(ladders)

    #labelxlabel matrix filled with zeros
    implication_matrix = np.zeros((len(labels), len(labels)))

    
    #propose cut_off_value
    cut_off_value = proposed_cut_off_value(cut_off_value, len(ladders))

    #calculate requested matrix
    if (radio_in_direct=='direct'):
        implication_matrix_calculated = cal_direct_implication_matrix(implication_matrix, ladders, labels, radio_treatments)
    else:
        implication_matrix_calculated = cal_indirect_implication_matrix(implication_matrix, ladders, labels, radio_treatments)

    return {'implication_matrix': implication_matrix_calculated, 'labels': labels, 'treatments': treatments, 'cut_off_value': cut_off_value}


def cal_nodes(cut_off_value, labels):
    """Creates nodes for the hierarchical value map (vis.js network) based on Args

    Args:
        cut_off_value ([int]): [cutoff-value]
        labels ([dict]): [labels]

    Returns:
        [Array]: [nodes]
    """
    nodes = []
    for l in labels:
        if (l.get('acv')=='A'):
            nodes.append({'id':l.get('labelcode'), 'label':l.get('name'), 'group':'attributes', 'level':'3'})
        elif (l.get('acv')=='C'):
            nodes.append({'id':l.get('labelcode'), 'label':l.get('name'), 'group':'consequences', 'level':'2'})
        elif (l.get('acv')=='V'):
            nodes.append({'id':l.get('labelcode'), 'label':l.get('name'), 'group':'values', 'level':'1'})
        else:
            pass

    return nodes


def cal_edges(cut_off_value, matrix):
    """Creates edges for the hierarchical value map (vis.js network) based on Args

    Args:
        cut_off_value ([int]): [cutoff-value]
        matrix ([Array]): [matrix]

    Returns:
        [Array]: [edges]
    """
    edges = []

    counterRow = 0
    for row in matrix:
        counterElement = 0
        for number in row:
            if (number > int(cut_off_value)):
                edges.append({'from': counterRow, 'to': counterElement, 'width': number})
            counterElement = counterElement + 1
        counterRow = counterRow + 1
    return edges


def remove_nodes_without_edges(nodes, edges):
    """Removes nodes without edges

    Args:
        nodes ([Array]): [nodes]
        edges ([Array]): [edges]

    Returns:
        [Array]: [nodes without edges]
    """
    
    filtered_nodes = []
    for node in nodes:
        id = node.get('id')
        has_edges = False
        for edge in edges:
            if (id==edge.get('from') or id==edge.get('to')):
                has_edges = True
                break
            else:
                pass
        if (has_edges):
            filtered_nodes.append(node)
    return filtered_nodes




def create_grid_aim(labels, ladders):
    """Creats and safes AIM

    Args:
        labels ([xlsx file]): [labels]
        ladders ([xlsx file]): [ladders]
        
        
    Returns:
        [dict]: [cols and rows for grid table]
    """
    ladders = pd.read_excel(ladders).to_numpy(dtype=str)
    labels=create_labels_tabel(labels)
    len_labels = len(labels)
    #init empty arrays
    direct_implication_matrix = np.zeros((len_labels, len_labels))
    indirect_implication_matrix = np.zeros((len_labels, len_labels))
    radio_treatments='All'

    #calculate implications
    direct_implication_matrix_calculated = cal_direct_implication_matrix(direct_implication_matrix, ladders, labels, radio_treatments)
    indirect_implication_matrix_calculated = cal_indirect_implication_matrix(indirect_implication_matrix, ladders, labels, radio_treatments)

    #create new 2d array for aim
    aim = np.empty((len_labels, len_labels + 3), dtype=object)
    sum_entries = 0
    sum_rows = np.zeros((len_labels))
    sum_columns = np.zeros((len_labels))

    #fill aim, calculate sum's
    for x in range(len_labels):
        aim[x][0] = get_name_by_index(x,labels)
        for y in range(len_labels):
            direct = int(direct_implication_matrix_calculated[x][y])
            indirect = int(indirect_implication_matrix_calculated[x][y])
            #indirect contains direct and indirect implications (see cal_indirect_implication_matrix)
            #therefore direct implications need to be subtracted
            indirect = indirect - direct
            sum_entries = sum_entries + direct + indirect
            sum_rows[x] = sum_rows[x] + direct + indirect
            sum_columns[y] = sum_columns[y] + direct + indirect
            aim[x][y+1] = str(direct) + "." + str(indirect)

    #calculate and add centrality and abstractness
    runner = 0
    for x in aim:
        aim[runner][len_labels + 1] = round((sum_rows[runner]+sum_columns[runner])/sum_entries, 4)
        if (sum_columns[runner] + sum_rows[runner] !=0):
            aim[runner][len_labels + 2] = round(sum_columns[runner]/(sum_columns[runner] + sum_rows[runner]), 4)
        else:
            aim[runner][len_labels + 2] = 0
        runner += 1

    #create first row -> coulumn with empty string (first position), labelcodes, centrality and abstractness
    runner = 0
    cols = ['']
    for x in range(0, (len_labels)):
        cols.append(get_name_by_index(x,labels))
        runner += 1
    cols.append('Centraility')
    cols.append('Abstractness') 


    df = pd.DataFrame(data=aim, columns=cols)
    df.to_csv("./backend/ladder_ly/download/aim.csv")

    #serialize aim
    aim = serialize_numpy(aim)

    return {'cols':cols, 'rows':aim}
    
    

def serialize_numpy(array):
    """serialize numpy array

    Args:
        array ([array]): [numpy array]

    Returns:
        [String]: [serialized array]
    """
    array = array.tolist()
    array = json.dumps(array)
    return array
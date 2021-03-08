#app.py set for flask-app and api calls 

#imports
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from numpy.core.defchararray import index
import pandas as pd
import numpy as np
import json

from functions import calculate_network_data, remove_nodes_without_edges, cal_nodes, cal_edges, create_labels_tabel, create_grid_ladders, create_grid_aim




#configuration
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


#
#api-calls
#
@app.route('/ping', methods=['POST'])
def ping_pong():
    """Test api-call to check BE-FE conection 
    @app.route('/ping', methods=['POST'])

    Returns:
        [String]: [returns String, depending on 'name' send from FE]
    """
    data = request.json
    print(data)
    if (data.get('name')=='Ping!'):
        return jsonify('soooo interactive!')
    else:
        return jsonify('Interactive HVM')

@app.route('/grid_data', methods=['POST'])  
def grid_data():
    """Api-call to return uploaded ladders and labels in a grid-readable format
    @app.route('/grid_data', methods=['POST'])

    Args:
        uploadLadders ([xlsx file]): [uploaded ladders]
        uploadLabels ([xlsx file]): [uploaded labels]

    Returns:
        [dict]: [ladders, labels]
    """
    labels = request.files['uploadLabels']
    ladders = request.files['uploadLadders']
    aim = create_grid_aim(labels, ladders)
    labels = create_labels_tabel(labels)
    ladders = create_grid_ladders(ladders)
    return jsonify({'ladders':ladders, 'labels':labels, 'aim':aim})

@app.route('/ladders_example', methods = ["GET"])
def get_ladders_example():
    """Sends example_ladders.xlsx to FE
    @app.route('/ladders_example', methods = ["GET"])

    Returns:
        [xlsx file]: [example ladders]
    """
    return send_file("example_input/example_ladders.xlsx", as_attachment=True, attachment_filename = 'labels_example', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/labels_example', methods = ["GET"])
def get_labels_example():
    """Sends example_labels.xlsx to FE

    Returns:
        [xlsx file]: [example labels]
    """
    return send_file("example_input/example_labels.xlsx", as_attachment=True, attachment_filename = 'labels_example', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/network_data/<cut_off_value>/<radio_in_direct>/<radio_treatments>', methods=['POST'])
def network_data(cut_off_value, radio_in_direct, radio_treatments):
    """Api-call to calculate and return the correct data for specific configurations (Args),
    the data is used to visualize the hierarchical value map with vis.js in FE

    @app.route('/network_data/<cut_off_value>/<radio_in_direct>/<radio_treatments>', methods=['POST'])

    Args:
        cut_off_value ([int]): [cutoff-value for the network, if '-1' (=default) a cutoff-value is calculated in calculate_network_data]
        radio_in_direct ([String]): ["direct" or "indirect" depending on selected radio group in FE]
        radio_treatments ([String]): [selected treatment, default: "all"]

        uploadLadders ([xlsx file]): [uploaded ladders]
        uploadLabels ([xlsx file]): [uploaded labels]

    Returns:
        [dict]: [nodes, edges, treatments, cutoff-value]
    """
    ladders = request.files['uploadLadders']
    labels = request.files['uploadLabels']
    data = calculate_network_data(ladders, labels, radio_treatments, radio_in_direct, cut_off_value)
    nodes = cal_nodes(data['cut_off_value'], data['labels'])
    edges = cal_edges(data['cut_off_value'], data['implication_matrix'])
    nodes = remove_nodes_without_edges(nodes, edges)
    response_object = {'nodes': nodes, 'edges': edges, 'treatments': data['treatments'],'cutOffValue': data['cut_off_value']}
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()
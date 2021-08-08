import json
import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import app
"""
Index=['1','2','3','4','5','6','7','8']
Citations = ['This is good', 'This is bad', 'Its normal', 'Its good', 'THis is not enough', ' So worst',
                 'better than that', 'Its good']
Sentiments = ('Positive', 'Negative', 'Neutral', 'Positive', 'negative', 'Nuetral', 'Positive')
References = ['Paper1', 'Paper2', 'Paper3', 'Paper4', 'Paper5', 'Paper6', 'Paper7', 'Paper8']
Long = [34.03, 40.71, 43.65, 45.50, 49.28, 41.88, 42.36, 29.76]
Lat = [-118.25, -74, -79.38, -73.57, -123.12, -87.63, -71.06, -95.37]
"""
def create_dash_application(flask_app,index,Nodelist,Sourcelist,targelist,Senti,lo,la):
#def create_dash_application(flask_app):
    Index=index
    NodesList=Nodelist
    Sourcelist=Sourcelist
    TargetList=targelist
    Sentiments=Senti
    Long=lo
    Lat=la
    dash_app=dash.Dash(
        server=flask_app,name="Dashboard",url_base_pathname="/")

    styles = {
        'pre': {
            'border': 'thin lightgrey solid',
            'overflowX': 'scroll'
        }
    }

    nodes = [
        {
            'data': {'id': short, 'label': label},
            'position': {'x': 20 * lat, 'y': -20 * long}
        }
        for short, label, long, lat in zip(Index, NodesList, Long, Lat)

    ]

    edges = [
        {'data': {'source': source, 'target': target, 'edlabel': senti}}
        for source, target, senti in zip(Sourcelist,TargetList,Sentiments)

    ]

    default_stylesheet = [
        {
            'selector': 'node',
            'style': {
                'background-color': '#FF4136',
                'label': 'data(label)'
            },
            # to display the values over the edges of network
            'selector': 'edge',
            'style': {
                'background-color': '#BFD7B5',
                'label': 'data(edlabel)'

            }
        },
        # to make arrows or edges directed
        {
            'selector': 'node',
            'style': {
                'background-color': 'orange'

            }
        },
        {
            'selector': 'edge',
            'style': {
                "curve-style": "bezier",
                "target-arrow-shape": "triangle"
            }
        },
        # to make Edges colored

        {
            'selector': '[edlabel *= "Negative"]',
            'style': {
                'line-color': 'red',
                'target-arrow-color': 'red'
            }

        },
        {  # to make Edges colored
            'selector': '[edlabel *= "Positive"]',
            'style': {
                'line-color': 'Green',
                'target-arrow-color': 'Green'
            }

        },
        {  # to make Edges colored
            'selector': '[edlabel *= "Neutral"]',
            'style': {
                'line-color': 'Black',
                'target-arrow-color': 'Black'
            }

        }

    ]

    dash_app.layout = html.Div([
        cyto.Cytoscape(
            id='cytoscape-event-callbacks-1',
            layout={'name': 'preset'},
            elements=edges+nodes,
            stylesheet=default_stylesheet,
            style={'width': '100%', 'height': '450px'}
        ),
        html.Pre(id='cytoscape-tapNodeData-json', style=styles['pre'])
    ])
    return dash_app


    @dash_app.callback(Output('cytoscape-tapNodeData-json', 'children'),
                  Input('cytoscape-event-callbacks-1', 'tapNodeData'))
    def displayTapNodeData(data):
        return json.dumps(data, indent=2)
import uuid 
from PIL import Image
import graphviz as gv


styles = {
    'graph': {
        'label': 'Discreta - Representación de AST',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'hexagon',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'style': 'dashed',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}


def _render_children(g, n, parent=None):
    id = str(uuid.uuid1())

    if n.op is not None:
        g.node(id, n.op)

        if parent is not None:
            g.edge(parent, id)

        for each in n.children:
            _render_children(g, each, id)
    else:
        g.node(id, n.value)
        g.edge(parent, id)


def _set_styles(graph):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph


def render_tree(tree):
    graph = gv.Digraph(
            format='jpg', comment="Arbol de representación semántico")
    _set_styles(graph)
    _render_children(graph, tree)
    filename = graph.render("ast", view=True)


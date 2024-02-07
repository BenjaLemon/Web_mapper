import networkx as nx
import gravis as gv
import pandas as pd

def draw(edges):
    g = nx.DiGraph()
    for source, target, strength, color in edges:
        g.add_edge(source, target, strength=strength, color=color)

    fig = gv.d3(g, show_edge_label=True, zoom_factor=0.50,edge_curvature=0.6, edge_size_factor=0.6,use_many_body_force=True,many_body_force_strength=- 70.0,
                use_links_force=False,use_collision_force=False,use_centering_force=False, edge_label_data_source='strength',large_graph_threshold=1000)
    fig.display()  # opens the plot in a browser window, can be stored as SVG/JPG/PNG

def full_opt_draw(edges):
    g = nx.DiGraph()
    for source, target, strength, color in edges:
        g.add_edge(source, target, strength=strength, color=color)

    fig=gv.d3(
    data=g,
    graph_height=200,
    details_height=100,
    show_details=True,
    show_details_toggle_button=True,
    show_menu=True,
    show_menu_toggle_button=True,
    show_node=True,
    node_size_factor=1.2,
    node_size_data_source='size',
    use_node_size_normalization=False,
    node_size_normalization_min=10.0,
    node_size_normalization_max=50.0,
    node_drag_fix=True,
    node_hover_neighborhood=True,
    node_hover_tooltip=True,
    show_node_image=True,
    node_image_size_factor=1.0,
    show_node_label=True,
    show_node_label_border=False,
    node_label_data_source='id',
    node_label_size_factor=0.8,
    node_label_rotation=45.0,
    node_label_font='Arial',
    show_edge=True,
    edge_size_factor=1.0,
    edge_size_data_source='size',
    use_edge_size_normalization=False,
    edge_size_normalization_min=0.2,
    edge_size_normalization_max=5.0,
    edge_curvature=0.0,
    edge_hover_tooltip=True,
    show_edge_label=True,
    show_edge_label_border=False,
    edge_label_data_source='id',
    edge_label_size_factor=1.0,
    edge_label_rotation=45.0,
    edge_label_font='Arial',
    zoom_factor=0.4,
    large_graph_threshold=500,
    layout_algorithm_active=True,

    # specific for d3
    use_many_body_force=True,
    many_body_force_strength=- 70.0,
    many_body_force_theta=0.9,
    use_many_body_force_min_distance=False,
    many_body_force_min_distance=10.0,
    use_many_body_force_max_distance=False,
    many_body_force_max_distance=1000.0,
    use_links_force=True,
    links_force_distance=50.0,
    links_force_strength=0.5,
    use_collision_force=True,
    collision_force_radius=30.0,
    collision_force_strength=0.9,
    use_x_positioning_force=False,
    x_positioning_force_strength=0.2,
    use_y_positioning_force=True,
    y_positioning_force_strength=0.5,
    use_centering_force=True,
    )
    fig.display()


int_edge_color='black'
ext_edge_color='red'
edge_label=''
links=pd.read_csv('./Website_map_wasp-group.csv')
edges=[]
shorten_url = lambda x: x[x.rfind('/')+1:] 

for i in range(0,len(links)):
    row=links.iloc[i]
    URL=shorten_url(row['URL'][:-1])
    internal_links=eval(row['Internal'])
    internal_edges=[[URL,shorten_url(link[:-1]),edge_label,int_edge_color] for link in internal_links]
    edges = edges + internal_edges
    #external_links=eval(row['External'])
    #external_edges=[[URL,link,edge_label,ext_edge_color] for link in external_links]
    #edges = edges + external_edges

''' example:
edges = [
    ('A', 'B', '', 'black'),
    ('B','A','','black'),
    ('B', 'C', 200, 'black'),
    ('B', 'D', 2, 'black'),
    ('B', 'E', 1, 'black'),
    ('C', 'D', 1, 'red'),
    ('C', 'E', 4, 'black'),
    ('D', 'A', 2, 'red'),
    ('D', 'E', 2, 'black'),
    ('E', 'F', 3, 'black'),
    ('G', 'D', 1, 'black'),
]
'''

draw(edges)
#full_opt_draw(edges)

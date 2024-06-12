import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
nodes = [
    # major fields
    "Algorithms", "Data Structures", "Graph Algorithms", "Sorting Algorithms",
    "Dynamic Programming", "Search Algorithms", "Trees", "Graphs", "Hash Tables",
    "Machine Learning", "Artificial Intelligence", "Supervised Learning", "Unsupervised Learning",
    "Reinforcement Learning", "Neural Networks", "Deep Learning", "Computer Vision", 
    "Natural Language Processing", "Robotics", "Expert Systems", "Genetic Algorithms",
    "Database Systems", "SQL", "NoSQL", "Big Data", "Data Mining", "Data Warehousing",
    "Hadoop", "Spark", "ETL", "Data Visualization",
    "Operating Systems", "Computer Networks", "Distributed Systems", "Cloud Computing",
    "Parallel Computing", "Cybersecurity", "Cryptography", "Blockchain",
    "Software Engineering", "Agile Methodology", "DevOps", "Software Testing", 
    "Version Control", "Continuous Integration", "Microservices", "Design Patterns",
    "Programming Languages", "Compilers", "Interpreters", "Java", "Python", "C++", 
    "JavaScript", "Functional Programming", "Object-Oriented Programming",
    "Human-Computer Interaction", "User Interface Design", "User Experience", 
    "Virtual Reality", "Augmented Reality", "Graphics", "3D Rendering",
    "Quantum Computing", "IoT", "Edge Computing", "5G", "Autonomous Systems",
    "Wearable Technology", "Transhumanism",
    "Theory of Computation", "Automata Theory", "Computability Theory", "Complexity Theory",
    "Discrete Mathematics", "Linear Algebra", "Statistics", "Probability"
]

G.add_nodes_from(nodes)
edges = [
    # related fields
    ("Algorithms", "Data Structures"),
    ("Algorithms", "Graph Algorithms"),
    ("Algorithms", "Sorting Algorithms"),
    ("Algorithms", "Dynamic Programming"),
    ("Algorithms", "Search Algorithms"),
    ("Data Structures", "Trees"),
    ("Data Structures", "Graphs"),
    ("Data Structures", "Hash Tables"),
    ("Machine Learning", "Supervised Learning"),
    ("Machine Learning", "Unsupervised Learning"),
    ("Machine Learning", "Reinforcement Learning"),
    ("Machine Learning", "Neural Networks"),
    ("Neural Networks", "Deep Learning"),
    ("Deep Learning", "Computer Vision"),
    ("Deep Learning", "Natural Language Processing"),
    ("Artificial Intelligence", "Expert Systems"),
    ("Artificial Intelligence", "Genetic Algorithms"),
    ("Robotics", "Machine Learning"),
    ("Database Systems", "SQL"),
    ("Database Systems", "NoSQL"),
    ("Database Systems", "Big Data"),
    ("Big Data", "Hadoop"),
    ("Big Data", "Spark"),
    ("Data Mining", "Machine Learning"),
    ("Data Warehousing", "ETL"),
    ("Data Warehousing", "Data Visualization"),
    ("Operating Systems", "Distributed Systems"),
    ("Operating Systems", "Parallel Computing"),
    ("Computer Networks", "Distributed Systems"),
    ("Computer Networks", "Cloud Computing"),
    ("Distributed Systems", "Cloud Computing"),
    ("Distributed Systems", "Parallel Computing"),
    ("Cybersecurity", "Cryptography"),
    ("Blockchain", "Cryptography"),
    ("Blockchain", "Distributed Systems"),
    ("Software Engineering", "Agile Methodology"),
    ("Software Engineering", "DevOps"),
    ("Software Engineering", "Software Testing"),
    ("Software Engineering", "Version Control"),
    ("Software Engineering", "Continuous Integration"),
    ("Software Engineering", "Microservices"),
    ("Software Engineering", "Design Patterns"),
    ("Programming Languages", "Compilers"),
    ("Programming Languages", "Interpreters"),
    ("Programming Languages", "Java"),
    ("Programming Languages", "Python"),
    ("Programming Languages", "C++"),
    ("Programming Languages", "JavaScript"),
    ("Programming Languages", "Functional Programming"),
    ("Programming Languages", "Object-Oriented Programming"),
    ("Human-Computer Interaction", "User Interface Design"),
    ("Human-Computer Interaction", "User Experience"),
    ("Human-Computer Interaction", "Virtual Reality"),
    ("Human-Computer Interaction", "Augmented Reality"),
    ("Graphics", "3D Rendering"),
    ("Virtual Reality", "3D Rendering"),
    ("Quantum Computing", "Cryptography"),
    ("Quantum Computing", "Algorithms"),
    ("IoT", "Edge Computing"),
    ("IoT", "5G"),
    ("Autonomous Systems", "Machine Learning"),
    ("Autonomous Systems", "Robotics"),
    ("Theory of Computation", "Automata Theory"),
    ("Theory of Computation", "Computability Theory"),
    ("Theory of Computation", "Complexity Theory"),
    ("Complexity Theory", "Algorithms"),
    ("Discrete Mathematics", "Algorithms"),
    ("Discrete Mathematics", "Data Structures"),
    ("Linear Algebra", "Machine Learning"),
    ("Statistics", "Machine Learning"),
    ("Probability", "Machine Learning"),
    ("Probability", "Data Science"),
]

G.add_edges_from(edges)

# graph draw garne
plt.figure(figsize=(20, 15))
pos = nx.spring_layout(G, k=0.3, iterations=50)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
plt.title("Extensive and Detailed Interconnected Subdomains of Computer Science - Bhaskar Rijal")
plt.show()

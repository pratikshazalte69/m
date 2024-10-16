import rdflib  # Import rdflib for RDF parsing and querying

# Create an RDF graph instance
mygraph = rdflib.Graph()

# Parse and load the RDF data from the inline RDF/XML string
rdf_data = """
<rdf:RDF 
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" 
    xmlns:foaf="http://xmlns.com/foaf/0.1/" 
    xmlns:admin="http://webns.net/mvcb/">

  <!-- Define a person (John) who knows other people -->
  <foaf:Person rdf:nodeID="me">
    <foaf:name>John</foaf:name>

    <!-- John knows Doe -->
    <foaf:knows>
      <foaf:Person>
        <foaf:name>Doe</foaf:name>
      </foaf:Person>
    </foaf:knows>

    <!-- John knows Smith -->
    <foaf:knows>
      <foaf:Person>
        <foaf:name>Smith</foaf:name>
      </foaf:Person>
    </foaf:knows>

  </foaf:Person>
</rdf:RDF>
"""

# Load RDF/XML data directly into the graph
mygraph.parse(data=rdf_data, format='application/rdf+xml')

# Query the RDF graph using SPARQL to find people John knows
qres = mygraph.query(
    """SELECT DISTINCT ?fname ?lname
       WHERE {
           ?a foaf:knows ?b .
           ?a foaf:name ?fname .
           ?b foaf:name ?lname .
       }"""
)

# Print the results: who knows whom
for myrow in qres:
    print("%s knows %s" % myrow)

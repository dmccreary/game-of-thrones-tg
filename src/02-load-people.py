import pyTigerGraph as tg
import csv

# Configuration
host = "http://dans-macbook-pro.local"
username = "tigergraph"
password = "tigergraph"
graph_name = "got"
input_file = "../data/book1-people.csv"

# Connect to TigerGraph
conn = tg.TigerGraphConnection(host=host, username=username, password=password, graphname=graph_name)

# Authenticate
conn.getToken(conn.createSecret())

# Define the schema (run this part only once)
#schema_script = """
#CREATE VERTEX Person (PRIMARY_ID name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
#"""
#conn.gsql(schema_script)

# Define the loading job (run this part only once)
loading_job_script = """
CREATE LOADING JOB loadPeople FOR GRAPH MyGraph {
  DEFINE FILENAME filePath;
  
  LOAD filePath TO VERTEX Person VALUES ($"name") USING SEPARATOR=",", HEADER="true";
}
"""
conn.gsql(loading_job_script)

# Prepare the data for loading
with open(input_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    rows = [row for row in csv_reader]

# Save the data to a new CSV file that will be used by the loading job
output_file = "/tmp/people_for_loading.csv"
with open(output_file, mode='w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=["name"])
    csv_writer.writeheader()
    csv_writer.writerows(rows)

# Upload the CSV file to TigerGraph (assumes local file system access)
conn.uploadFile(output_file, overwrite=True)

# Run the loading job
run_loading_job_script = f"""
RUN LOADING JOB loadPeople USING filePath="{output_file}";
"""
conn.gsql(run_loading_job_script)

print("Loading job completed successfully.")

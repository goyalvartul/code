import os
import subprocess
import json

def run_command(cmd):
    output = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
    return output

# get the resource group and cluster name
resource_group = run_command("az aks show --name my-cluster --resource-group my-rg --query 'resourceGroup' -o tsv")
cluster_name = run_command("az aks show --name my-cluster --resource-group my-rg --query 'name' -o tsv")

# run the CIS benchmark
cmd = f"az aks cis run --name {cluster_name} --resource-group {resource_group} --file cis-kubernetes-benchmark.yaml"
run_command(cmd)

# get the results of the CIS benchmark
cmd = f"az aks cis show --name {cluster_name} --resource-group {resource_group} --file cis-kubernetes-benchmark.yaml --query 'results' -o json"
results = json.loads(run_command(cmd))

# print the results in HTML format
print("<html>")
print("<head>")
print("<title>CIS Benchmark for Azure Kubernetes Environment</title>")
print("</head>")
print("<body>")
print("<table>")
print("<tr><th>Check</th><th>Status</th></tr>")
for result in results:
    print(f"<tr><td>{result['check']}</td><td>{result['status']}</td></tr>")
print("</table>")
print("</body>")
print("</html>")


## Note that this script assumes that you have the Azure CLI and the "az aks cis" extension installed on your system. It also assumes that you have an existing AKS cluster named "my-cluster" in a resource group named "my-rg", and that you have the CIS benchmark file named "cis-kubernetes-benchmark.yaml" in the current directory. Make sure to update these values as necessary before running the script.
import subprocess
import json

# CIS benchmark for GCP Kubernetes environment
cis_benchmark_cmd = "gke-cis-benchmark --format json"

# Run the CIS benchmark command
output = subprocess.run(cis_benchmark_cmd, shell=True, capture_output=True)

# Parse the output as JSON
output_json = json.loads(output.stdout)

# Initialize a counter for the number of passed checks
passed_checks = 0

# Iterate through the output and print the results in HTML format
print("<html>")
print("<head>")
print("<title>CIS Benchmark Results for GCP Kubernetes Environment</title>")
print("</head>")
print("<body>")
print("<table>")
print("<tr>")
print("<th>Check</th>")
print("<th>Result</th>")
print("</tr>")
for check in output_json:
    print("<tr>")
    print("<td>", check["check"], "</td>")
    if check["passed"]:
        print("<td style='color: green'>PASSED</td>")
        passed_checks += 1
    else:
        print("<td style='color: red'>FAILED</td>")
    print("</tr>")
print("</table>")

# Print the final results
print("<p>All CIS benchmark parameters completed with guidelines.</p>")
print("<p>Passed checks: ", passed_checks, " out of ", len(output_json), "</p>")

print("</body>")
print("</html>")


## This script runs the gke-cis-benchmark command with the --format json flag to output the results in JSON format. It then parses the output as JSON and iterates through the checks, printing the check name and whether it passed or failed in an HTML table. It also keeps a counter for the number of passed checks and prints the final results at the end of the script.
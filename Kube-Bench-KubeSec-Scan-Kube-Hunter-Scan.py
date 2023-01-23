import subprocess
import json

def run_kube_bench():
    kube_bench_cmd = "kube-bench --json"
    kube_bench_output = subprocess.run(kube_bench_cmd, shell=True, capture_output=True)
    kube_bench_output_json = json.loads(kube_bench_output.stdout)
    print("Kube-Bench Results:")
    for test in kube_bench_output_json["tests"]:
        print(f"{test['name']}: {test['status']}")

def run_kube_hunter():
    kube_hunter_cmd = "kube-hunter --json"
    kube_hunter_output = subprocess.run(kube_hunter_cmd, shell=True, capture_output=True)
    kube_hunter_output_json = json.loads(kube_hunter_output.stdout)
    print("Kube-Hunter Results:")
    for test in kube_hunter_output_json["hunts"]:
        print(f"{test['name']}: {test['status']}")

def run_kube_sec():
    kube_sec_cmd = "kubesec scan --json"
    kube_sec_output = subprocess.run(kube_sec_cmd, shell=True, capture_output=True)
    kube_sec_output_json = json.loads(kube_sec_output.stdout)
    print("Kube-Sec Results:")
    for test in kube_sec_output_json["checks"]:
        print(f"{test['name']}: {test['status']}")

if __name__ == "__main__":
    run_kube_bench()
    run_kube_hunter()
    run_kube_sec()

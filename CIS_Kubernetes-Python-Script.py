import os
import subprocess

# CIS benchmark for Kubernetes environment

# Master node checks

# 1.1.1 Ensure that the --anonymous-auth argument is set to false
anonymous_auth = subprocess.run(["kubectl", "get", "cm", "kubeadm-config", "-n", "kube-system", "-o", "jsonpath={.data.anonymous-auth}"], capture_output=True)
if anonymous_auth.stdout.strip() == b"false":
    print("1.1.1: Passed")
else:
    print("1.1.1: Failed")

# 1.1.2 Ensure that the --authorization-mode argument is not set to AlwaysAllow
authorization_mode = subprocess.run(["kubectl", "get", "cm", "kubeadm-config", "-n", "kube-system", "-o", "jsonpath={.data.authorization-mode}"], capture_output=True)
if authorization_mode.stdout.strip() != b"AlwaysAllow":
    print("1.1.2: Passed")
else:
    print("1.1.2: Failed")

# 1.1.3 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate
tls_cert_file = subprocess.run(["kubectl", "get", "cm", "kubeadm-config", "-n", "kube-system", "-o", "jsonpath={.data.tls-cert-file}"], capture_output=True)
tls_private_key_file = subprocess.run(["kubectl", "get", "cm", "kubeadm-config", "-n", "kube-system", "-o", "jsonpath={.data.tls-private-key-file}"], capture_output=True)
if tls_cert_file.stdout.strip() != b"" and tls_private_key_file.stdout.strip() != b"":
    print("1.1.3: Passed")
else:
    print("1.1.3: Failed")

# Worker node checks

# 1.2.1 Ensure that the --anonymous-auth argument is set to false
anonymous_auth = subprocess.run(["kubectl", "get", "cm", "kubeadm-config", "-n", "kube-system", "-o", "jsonpath={.data.anonymous-auth}"], capture_output=True)
if anonymous_auth.stdout.strip() == b"false":
    print("1.2.1: Passed")
else:
    print("1.2.1: Failed")

# In this way other controls can be implemented in same fashion for Kubernetes CIS Benchmark and this is sample script.

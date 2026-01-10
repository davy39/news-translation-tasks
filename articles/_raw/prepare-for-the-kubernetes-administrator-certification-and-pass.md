---
title: Prepare for the Kubernetes Administrator Certification and Pass
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2025-10-29T13:20:09.253Z'
originalURL: https://freecodecamp.org/news/prepare-for-the-kubernetes-administrator-certification-and-pass
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761739982392/f255a6af-6ec9-4136-b45f-6f14d4fb2c8c.jpeg
tags:
- name: Kubernetes
  slug: kubernetes
- name: youtube
  slug: youtube
seo_title: null
seo_desc: We just posted a course on the freeCodeCamp.org YouTube channel to help
  prepare you for the Certified Kubernetes Administrator Certification. This course
  is designed to provide a deep, practical understanding of Kubernetes administration,
  from founda...
---

We just posted a course on the freeCodeCamp.org YouTube channel to help prepare you for the Certified Kubernetes Administrator Certification. This course is designed to provide a deep, practical understanding of Kubernetes administration, from foundational concepts to advanced troubleshooting.

You can watch the course on [the freeCodeCamp.org YouTube channel](https://youtu.be/Fr9GqFwl6NM) (2-hour watch).

%[https://youtu.be/Fr9GqFwl6NM] 

There are many demos in the course using Kubernetes. Below you can find all the commands used in the course so it is easier for you to follow along on your local machine.

## CKA Hands-On Companion: Commands and Demos

## Part 1: Kubernetes Fundamentals and Lab Setup

This section covers the setup of a single-node cluster using `kubeadm` to create an environment that mirrors the CKA exam.

### Section 1.3: Setting Up Your CKA Practice Environment

#### **Step 1: Install a Container Runtime (on all nodes)**

1. **Load required kernel modules:**
    
    ```bash
    cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
    overlay
    br_netfilter
    EOF
    
    sudo modprobe overlay
    sudo modprobe br_netfilter
    ```
    
2. **Configure sysctl for networking:**
    
    ```bash
    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-iptables  = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    net.ipv4.ip_forward               = 1
    EOF
    
    sudo sysctl --system
    ```
    
3. **Install containerd:**
    
    ```bash
    sudo apt-get update
    sudo apt-get install -y containerd
    ```
    
4. **Configure containerd for systemd cgroup driver:**
    
    ```bash
    sudo mkdir -p /etc/containerd
    sudo containerd config default | sudo tee /etc/containerd/config.toml
    sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
    ```
    
5. **Restart and enable containerd:**
    
    ```bash
    sudo systemctl restart containerd
    sudo systemctl enable containerd
    ```
    

#### **Step 2: Install Kubernetes Binaries (on all nodes)**

1. **Disable swap memory:**
    
    ```bash
    sudo swapoff -a
    # Comment out swap in fstab to make it persistent:
    sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
    ```
    
2. **Add the Kubernetes apt repository:**
    
    ```bash
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl gpg
    sudo mkdir -p -m 755 /etc/apt/keyrings
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
    ```
    
3. **Install and hold binaries (adjust version as needed):**
    
    ```bash
    sudo apt-get update
    sudo apt-get install -y kubelet kubeadm kubectl
    sudo apt-mark hold kubelet kubeadm kubectl
    ```
    

#### **Step 3: Configure a Single-Node Cluster (on the control plane)**

1. **Initialize the control-plane node:**
    
    ```bash
    sudo kubeadm init --pod-network-cidr=10.244.0.0/16
    ```
    
2. **Configure kubectl for the administrative user:**
    
    ```bash
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ```
    
3. **Remove the control-plane taint:**
    
    ```bash
    kubectl taint nodes --all node-role.kubernetes.io/control-plane-
    ```
    
4. **Install the Flannel CNI plugin:**
    
    ```bash
    kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
    ```
    
5. **Verify the cluster:**
    
    ```bash
    kubectl get nodes
    kubectl get pods -n kube-system
    ```
    

---

## Part 2: Cluster Architecture, Installation & Configuration (25%)

### Section 2.1: Bootstrapping a Multi-Node Cluster with `kubeadm`

#### **Initializing the Control Plane (Run on Control Plane node)**

1. **Run** `kubeadm init` (Replace `<control-plane-private-ip>`):
    
    ```bash
    sudo kubeadm init --pod-network-cidr=192.168.0.0/16 --apiserver-advertise-address=<control-plane-private-ip>
    ```
    
    * **Note:** Save the `kubeadm join` command from the output.
        
2. **Install Calico CNI Plugin:**
    
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/calico.yaml
    ```
    
3. **Verify Cluster and CNI installation:**
    
    ```bash
    kubectl get pods -n kube-system
    kubectl get nodes
    ```
    

#### **Joining Worker Nodes (Run on each Worker node)**

1. **Run the join command saved from** `kubeadm init`:
    
    ```bash
    # EXAMPLE - Use the exact command from your kubeadm init output
    sudo kubeadm join <control-plane-private-ip>:6443 --token <token> \
        --discovery-token-ca-cert-hash sha256:<hash>
    ```
    
2. **Verify the full cluster (from Control Plane node):**
    
    ```bash
    kubectl get nodes -o wide
    ```
    

### Section 2.2: Managing the Cluster Lifecycle

#### **Upgrading Clusters with** `kubeadm` (Example: Upgrade to 1.29.1)

1. **Upgrade Control Plane: Upgrade** `kubeadm` binary:
    
    ```bash
    sudo apt-mark unhold kubeadm
    sudo apt-get update && sudo apt-get install -y kubeadm='1.29.1-1.1'
    sudo apt-mark hold kubeadm
    ```
    
2. **Plan and apply the upgrade (on Control Plane node):**
    
    ```bash
    sudo kubeadm upgrade plan
    sudo kubeadm upgrade apply v1.29.1
    ```
    
3. **Upgrade** `kubelet` and `kubectl` (on Control Plane node):
    
    ```bash
    sudo apt-mark unhold kubelet kubectl
    sudo apt-get update && sudo apt-get install -y kubelet='1.29.1-1.1' kubectl='1.29.1-1.1'
    sudo apt-mark hold kubelet kubectl
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```
    
4. **Upgrade Worker Node: Drain the node (from Control Plane node):**
    
    ```bash
    kubectl drain <node-to-upgrade> --ignore-daemonsets
    ```
    
5. **Upgrade binaries (on Worker Node):**
    
    ```bash
    # On the worker node
    sudo apt-mark unhold kubeadm kubelet
    sudo apt-get update
    sudo apt-get install -y kubeadm='1.29.1-1.1' kubelet='1.29.1-1.1'
    sudo apt-mark hold kubeadm kubelet
    ```
    
6. **Upgrade node configuration and restart kubelet (on Worker Node):**
    
    ```bash
    # On the worker node
    sudo kubeadm upgrade node
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```
    
7. **Uncordon the Node (from Control Plane node):**
    
    ```bash
    kubectl uncordon <node-to-upgrade>
    ```
    

#### **Backing Up and Restoring etcd (Run on Control Plane node)**

1. **Perform a Backup (using host** `etcdctl`):
    
    ```bash
    # Create the backup directory first
    sudo mkdir -p /var/lib/etcd-backup
    
    sudo ETCDCTL_API=3 etcdctl snapshot save /var/lib/etcd-backup/snapshot.db \
        --endpoints=https://127.0.0.1:2379 \
        --cacert=/etc/kubernetes/pki/etcd/ca.crt \
        --cert=/etc/kubernetes/pki/etcd/server.crt \
        --key=/etc/kubernetes/pki/etcd/server.key
    ```
    
2. **Perform a Restore (on the control plane node):**
    
    ```bash
    # Stop kubelet to stop static pods
    sudo systemctl stop kubelet
    
    # Restore the snapshot to a new data directory
    sudo ETCDCTL_API=3 etcdctl snapshot restore /var/lib/etcd-backup/snapshot.db \
        --data-dir /var/lib/etcd-restored
    
    # !! IMPORTANT: Manually edit /etc/kubernetes/manifests/etcd.yaml to point to the new data-dir /var/lib/etcd-restored !!
    
    # Restart kubelet to pick up the manifest change
    sudo systemctl start kubelet
    ```
    

### Section 2.3: Implementing a Highly-Available (HA) Control Plane

1. **Initialize the First Control-Plane Node (Replace** `<load-balancer-address:port>`):
    
    ```bash
    sudo kubeadm init --control-plane-endpoint "load-balancer.example.com:6443" --upload-certs
    ```
    
    * **Note:** Save the HA-specific join command and the `--certificate-key`.
        
2. **Join Additional Control-Plane Nodes (Run on the second and third Control Plane nodes):**
    
    ```bash
    # EXAMPLE - Use the exact command from your `kubeadm init` output
    sudo kubeadm join load-balancer.example.com:6443 --token <token> \
        --discovery-token-ca-cert-hash sha256:<hash> \
        --control-plane --certificate-key <key>
    ```
    

### Section 2.4: Managing Role-Based Access Control (RBAC)

#### **Demo: Granting Read-Only Access**

1. **Create a Namespace and ServiceAccount:**
    
    ```bash
    kubectl create namespace rbac-test
    kubectl create serviceaccount dev-user -n rbac-test
    ```
    
2. **Create the** `Role` manifest (`role.yaml`):
    
    ```yaml
    # role.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: rbac-test
      name: pod-reader
    rules:
    - apiGroups: [""] # "" indicates the core API group
      resources: ["pods"]
      verbs: ["get", "list", "watch"]
    ```
    
    **Apply:** `kubectl apply -f role.yaml`
    
3. **Create the** `RoleBinding` manifest (`rolebinding.yaml`):
    
    ```yaml
    # rolebinding.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: read-pods
      namespace: rbac-test
    subjects:
    - kind: ServiceAccount
      name: dev-user
      namespace: rbac-test
    roleRef:
      kind: Role
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
    ```
    
    **Apply:** `kubectl apply -f rolebinding.yaml`
    
4. **Verify Permissions:**
    
    ```bash
    # Check if the ServiceAccount can list pods (Should be YES)
    kubectl auth can-i list pods --as=system:serviceaccount:rbac-test:dev-user -n rbac-test
    
    # Check if the ServiceAccount can delete pods (Should be NO)
    kubectl auth can-i delete pods --as=system:serviceaccount:rbac-test:dev-user -n rbac-test
    ```
    

### Section 2.5: Application Management with Helm and Kustomize

#### **Demo: Installing an Application with Helm**

1. **Add a Chart Repository:**
    
    ```bash
    helm repo add bitnami https://charts.bitnami.com/bitnami
    helm repo update
    ```
    
2. **Install a Chart with a value override:**
    
    ```bash
    helm install my-nginx bitnami/nginx --set service.type=NodePort
    ```
    
3. **Manage the application:**
    
    ```bash
    helm upgrade my-nginx bitnami/nginx --set service.type=ClusterIP
    helm rollback my-nginx 1
    helm uninstall my-nginx
    ```
    

#### **Demo: Customizing a Deployment with Kustomize**

1. **Create base manifest (**`my-app/base/deployment.yaml`):
    
    ```bash
    mkdir -p my-app/base
    cat <<EOF > my-app/base/deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          containers:
          - name: nginx
            image: nginx:1.25.0
    EOF
    ```
    
2. **Create base Kustomization file (**`my-app/base/kustomization.yaml`):
    
    ```bash
    cat <<EOF > my-app/base/kustomization.yaml
    resources:
    - deployment.yaml
    EOF
    ```
    
3. **Create production overlay and patch:**
    
    ```bash
    mkdir -p my-app/overlays/production
    cat <<EOF > my-app/overlays/production/patch.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 3
    EOF
    cat <<EOF > my-app/overlays/production/kustomization.yaml
    bases:
    -../../base
    patches:
    - path: patch.yaml
    EOF
    ```
    
4. **Apply the overlay (note the** `-k` flag for kustomize):
    
    ```bash
    kubectl apply -k my-app/overlays/production
    ```
    
5. **Verify the change:**
    
    ```bash
    kubectl get deployment my-app
    ```
    

---

## Part 3: Workloads & Scheduling (15%)

### Section 3.1: Mastering Deployments

#### **Demo: Performing a Rolling Update**

1. **Create a base Deployment manifest (**`deployment.yaml`):
    
    ```yaml
    # deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.24.0
            ports:
            - containerPort: 80
    ```
    
    **Apply:** `kubectl apply -f deployment.yaml`
    
2. **Update the Container Image to trigger the rolling update:**
    
    ```bash
    kubectl set image deployment/nginx-deployment nginx=nginx:1.25.0
    ```
    
3. **Observe the rollout:**
    
    ```bash
    kubectl rollout status deployment/nginx-deployment
    kubectl get pods -l app=nginx -w
    ```
    

#### **Executing and Verifying Rollbacks**

1. **View Revision History:**
    
    ```bash
    kubectl rollout history deployment/nginx-deployment
    ```
    
2. **Roll back to the previous version:**
    
    ```bash
    kubectl rollout undo deployment/nginx-deployment
    ```
    
3. **Roll back to a specific revision (e.g., revision 1):**
    
    ```bash
    kubectl rollout undo deployment/nginx-deployment --to-revision=1
    ```
    

### Section 3.2: Configuring Applications with ConfigMaps and Secrets

#### **Creation Methods**

1. **ConfigMap: Imperative Creation:**
    
    ```bash
    # From literal values
    kubectl create configmap app-config --from-literal=app.color=blue --from-literal=app.mode=production
    
    # From a file
    echo "retries = 3" > config.properties
    kubectl create configmap app-config-file --from-file=config.properties
    ```
    
2. **Secret: Imperative Creation:**
    
    ```bash
    # Kubernetes will automatically base64 encode
    kubectl create secret generic db-credentials --from-literal=username=admin --from-literal=password='s3cr3t'
    ```
    

#### **Demo: Consuming ConfigMaps and Secrets in Pods**

1. **Manifest: Environment Variables (**`pod-config.yaml`):
    
    ```yaml
    # pod-config.yaml (Assumes app-config-declarative ConfigMap and db-credentials Secret exist)
    apiVersion: v1
    kind: Pod
    metadata:
      name: config-demo-pod
    spec:
      containers:
      - name: demo-container
        image: busybox
        command: ["/bin/sh", "-c", "env && sleep 3600"]
        env:
          - name: THEME
            valueFrom:
              configMapKeyRef:
                name: app-config-declarative
                key: ui.theme
          - name: DB_PASSWORD
            valueFrom:
              secretKeyRef:
                name: db-credentials
                key: password
      restartPolicy: Never
    ```
    
    **Apply:** `kubectl apply -f pod-config.yaml` **Verify:** `kubectl logs config-demo-pod`
    
2. **Manifest: Mounted Volumes (**`pod-volume.yaml`):
    
    ```yaml
    # pod-volume.yaml (Assumes app-config-file ConfigMap exists)
    apiVersion: v1
    kind: Pod
    metadata:
      name: volume-demo-pod
    spec:
      containers:
      - name: demo-container
        image: busybox
        command: ["/bin/sh", "-c", "cat /etc/config/config.properties && sleep 3600"]
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
      volumes:
      - name: config-volume
        configMap:
          name: app-config-file
      restartPolicy: Never
    ```
    
    **Apply:** `kubectl apply -f pod-volume.yaml` **Verify:** `kubectl logs volume-demo-pod`
    

### Section 3.3: Implementing Workload Autoscaling

#### **Demo: Installing and Verifying the Metrics Server**

1. **Install the Metrics Server:**
    
    ```bash
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    ```
    
2. **Verify Installation:**
    
    ```bash
    kubectl top nodes
    kubectl top pods -A
    ```
    

#### **Demo: Autoscaling a Deployment**

1. **Create a Deployment with Resource Requests (requires** `hpa-demo-deployment.yaml` manifest not provided, use a simple one):
    
    ```bash
    kubectl create deployment php-apache --image=k8s.gcr.io/hpa-example --requests="cpu=200m"
    kubectl expose deployment php-apache --port=80
    ```
    
2. **Create an HPA (target 50% CPU, scale 1-10 replicas):**
    
    ```bash
    kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
    ```
    
3. **Generate Load (will run in the background):**
    
    ```bash
    kubectl run -it --rm load-generator --image=busybox -- /bin/sh -c "while true; do wget -q -O- http://php-apache; done"
    ```
    
4. **Observe Scaling:**
    
    ```bash
    kubectl get hpa -w
    ```
    
    *(Stop the load generator to observe scale down)*
    

### Section 3.5: Advanced Scheduling

#### **Demo: Using Node Affinity**

1. **Label a Node:**
    
    ```bash
    kubectl label node <your-worker-node-name> disktype=ssd
    ```
    
2. **Create a Pod with Node Affinity (requires** `affinity-pod.yaml` manifest not provided, create a dummy pod for the node label):
    
    ```bash
    # Create the pod using the affinity rules
    kubectl apply -f affinity-pod.yaml # Or equivalent manifest with node affinity
    ```
    

#### **Demo: Using Taints and Tolerations**

1. **Taint a Node (Effect:** `NoSchedule`):
    
    ```bash
    kubectl taint node <another-worker-node-name> app=gpu:NoSchedule
    ```
    
2. **Create a Pod with a Toleration (requires** `toleration-pod.yaml` manifest not provided, create a dummy pod for the taint):
    
    ```bash
    # Create the pod using the toleration rules
    kubectl apply -f toleration-pod.yaml # Or equivalent manifest with toleration
    ```
    
3. **Verify Pod scheduling on the tainted node:**
    
    ```bash
    kubectl get pod gpu-pod -o wide
    ```
    

---

## Part 4: Services & Networking (20%)

### Section 4.2: Kubernetes Services

#### **Demo: Creating a ClusterIP Service**

1. **Create a Deployment:**
    
    ```bash
    kubectl create deployment my-app --image=nginx --replicas=2
    ```
    
2. **Expose the Deployment with a ClusterIP Service (requires** `clusterip-service.yaml` manifest not provided, use an imperative command):
    
    ```bash
    kubectl expose deployment my-app --port=80 --target-port=80 --name=my-app-service --type=ClusterIP
    ```
    
3. **Verify Access (inside a temporary Pod):**
    
    ```bash
    kubectl run tmp-shell --rm -it --image=busybox -- /bin/sh
    # Inside the shell:
    # wget -O- my-app-service
    ```
    

#### **Demo: Creating a NodePort Service**

1. **Create a NodePort Service (requires** `nodeport-service.yaml` manifest not provided, use an imperative command):
    
    ```bash
    kubectl expose deployment my-app --port=80 --target-port=80 --name=my-app-nodeport --type=NodePort
    ```
    
2. **Verify Access information:**
    
    ```bash
    kubectl get service my-app-nodeport
    kubectl get nodes -o wide
    # Access from outside via <NodeIP>:<NodePort>
    ```
    

### Section 4.3: Ingress and the Gateway API

#### **Demo: Path-Based Routing with NGINX Ingress**

1. **Install the NGINX Ingress Controller:**
    
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.1/deploy/static/provider/cloud/deploy.yaml
    ```
    
2. **Deploy Two Sample Applications and Services:**
    
    ```bash
    kubectl create deployment app-one --image=k8s.gcr.io/echoserver:1.4
    kubectl expose deployment app-one --port=8080
    
    kubectl create deployment app-two --image=k8s.gcr.io/echoserver:1.4
    kubectl expose deployment app-two --port=8080
    ```
    
3. **Create an Ingress Resource (requires** `ingress.yaml` manifest not provided, use the provided structure to create the file):
    
    ```bash
    # Apply ingress.yaml
    kubectl apply -f ingress.yaml
    ```
    
4. **Test the Ingress:**
    
    ```bash
    INGRESS_IP=$(kubectl get svc -n ingress-nginx ingress-nginx-controller -o jsonpath='{.status.loadBalancer.ingress.ip}')
    curl http://$INGRESS_IP/app1
    curl http://$INGRESS_IP/app2
    ```
    

### Section 4.4: Network Policies

#### **Demo: Securing an Application with Network Policies**

1. **Create a Default Deny-All Ingress Policy (**`deny-all.yaml`):
    
    ```yaml
    # deny-all.yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: default-deny-ingress
    spec:
      podSelector: {} # Matches all pods in the namespace
      policyTypes:
      - Ingress
    ```
    
    **Apply:** `kubectl apply -f deny-all.yaml`
    
2. **Deploy a Web Server and a Service:**
    
    ```bash
    kubectl create deployment web-server --image=nginx
    kubectl expose deployment web-server --port=80
    ```
    
3. **Attempt connection (will fail):**
    
    ```bash
    kubectl run tmp-shell --rm -it --image=busybox -- /bin/sh -c "wget -O- --timeout=2 web-server"
    ```
    
4. **Create an "Allow" Policy (**`allow-web-access.yaml`):
    
    ```yaml
    # allow-web-access.yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: allow-web-access
    spec:
      podSelector:
        matchLabels:
          app: web-server
      policyTypes:
      - Ingress
      ingress:
      - from:
        - podSelector:
            matchLabels:
              access: "true"
        ports:
        - protocol: TCP
          port: 80
    ```
    
    **Apply:** `kubectl apply -f allow-web-access.yaml`
    
5. **Test the "Allow" Policy (connection will succeed):**
    
    ```bash
    kubectl run tmp-shell --rm -it --labels=access=true --image=busybox -- /bin/sh -c "wget -O- web-server"
    ```
    

### Section 4.5: CoreDNS

#### **Demo: Customizing CoreDNS for an External Domain**

1. **Edit the CoreDNS ConfigMap:**
    
    ```bash
    kubectl edit configmap coredns -n kube-system
    ```
    
2. **Add a new server block inside the** `Corefile` data structure (e.g., for [`my-corp.com`](http://my-corp.com)):
    
    ```yaml
    # ... inside the data.Corefile string...
        my-corp.com:53 {
            errors
            cache 30
            forward . 10.10.0.53 # Forward to your internal DNS server
        }
    # ...
    ```
    

---

## Part 5: Storage (10%)

### Section 5.2: Volume Configuration

#### **Static Provisioning Demo**

1. **Create a PersistentVolume (**`pv.yaml`):
    
    ```yaml
    # pv.yaml (Using hostPath for local testing)
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: task-pv-volume
    spec:
      capacity:
        storage: 10Gi
      accessModes:
        - ReadWriteOnce
      persistentVolumeReclaimPolicy: Retain
      storageClassName: manual
      hostPath:
        path: "/mnt/data"
    ```
    
    **Apply:** `kubectl apply -f pv.yaml`
    
2. **Create a PersistentVolumeClaim (**`pvc.yaml`):
    
    ```yaml
    # pvc.yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: task-pv-claim
    spec:
      storageClassName: manual
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 3Gi
    ```
    
    **Apply:** `kubectl apply -f pvc.yaml`
    
3. **Verify Binding:**
    
    ```bash
    kubectl get pv,pvc
    ```
    
4. **Create a Pod that Uses the PVC (**`pod-storage.yaml`):
    
    ```yaml
    # pod-storage.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: storage-pod
    spec:
      containers:
        - name: nginx
          image: nginx
          volumeMounts:
          - mountPath: "/usr/share/nginx/html"
            name: my-storage
      volumes:
        - name: my-storage
          persistentVolumeClaim:
            claimName: task-pv-claim
    ```
    
    **Apply:** `kubectl apply -f pod-storage.yaml`
    

### Section 5.3: StorageClasses and Dynamic Provisioning

#### **Demo: Using a Default StorageClass**

1. **Inspect the Available StorageClasses:**
    
    ```bash
    kubectl get storageclass
    ```
    
2. **Create a PVC without a PV (relies on a default StorageClass):**
    
    ```yaml
    # dynamic-pvc.yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-dynamic-claim
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
    ```
    
    **Apply:** `kubectl apply -f dynamic-pvc.yaml`
    
3. **Observe Dynamic Provisioning:**
    
    ```bash
    kubectl get pv
    ```
    

---

## Part 6: Troubleshooting (30%)

### Section 6.2: Troubleshooting Applications and Pods

#### **Debugging Tools for Crashes and Failures**

1. **Get detailed information on a resource (the most critical debugging command):**
    
    ```bash
    kubectl describe pod <pod-name>
    ```
    
2. **Check application logs (for current container):**
    
    ```bash
    kubectl logs <pod-name>
    ```
    
3. **Check application logs (for previous crashed container instance):**
    
    ```bash
    kubectl logs <pod-name> --previous
    ```
    
4. **Get a shell inside a running container for live debugging:**
    
    ```bash
    kubectl exec -it <pod-name> -- /bin/sh
    ```
    

### Section 6.3: Troubleshooting Cluster and Nodes

1. **Check node status:**
    
    ```bash
    kubectl get nodes
    ```
    
2. **Get detailed node information:**
    
    ```bash
    kubectl describe node <node-name>
    ```
    
3. **View node resource capacity (for scheduling issues):**
    
    ```bash
    kubectl describe node <node-name> | grep Allocatable
    ```
    
4. **Check the** `kubelet` service status (on the affected node via SSH):
    
    ```bash
    sudo systemctl status kubelet
    sudo journalctl -u kubelet -f
    ```
    
5. **Re-enable scheduling on a cordoned node:**
    
    ```bash
    kubectl uncordon <node-name>
    ```
    

### Section 6.5: Troubleshooting Services and Networking

1. **Check Service and Endpoints (for connectivity issues):**
    
    ```bash
    kubectl describe service <service-name>
    ```
    
2. **Check DNS resolution from a client Pod (from inside the client Pod's shell):**
    
    ```bash
    kubectl exec -it client-pod -- nslookup <service-name>
    ```
    
3. **Check Network Policies (to see if traffic is being blocked):**
    
    ```bash
    kubectl get networkpolicy
    ```
    

### Section 6.6: Monitoring Cluster and Application Resource Usage

1. **Get node resource usage (requires Metrics Server):**
    
    ```bash
    kubectl top nodes
    ```
    
2. **Get Pod resource usage (requires Metrics Server):**
    
    ```bash
    kubectl top pods -n <namespace>
    ```

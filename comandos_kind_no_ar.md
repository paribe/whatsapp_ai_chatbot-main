# Comandos para Mostrar que o Kind Está Funcionando (para o README.md)

Aqui estão os comandos ideais para demonstrar que seu cluster Kind está no ar e funcionando corretamente com a aplicação WhatsApp AI Chatbot. Estes comandos produzirão saídas visuais interessantes para serem incluídas em capturas de tela para o README.md:

## 1. Verificar Cluster Kind

```bash
kind get clusters
```

resposta :

```bash
 kind get clusters
wpp-cluster
```

👉 *Este comando mostra todos os clusters Kind ativos, incluindo seu "wpp-cluster".*

## 2. Verificar Nós do Kubernetes

```bash
kubectl get nodes -o wide
```

resposta:
```bash
 kubectl get nodes -o wide
NAME                        STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                         KERNEL-VERSION                       CONTAINER-RUNTIME
wpp-cluster-control-plane   Ready    control-plane   71m   v1.29.2   172.18.0.2    <none>        Debian GNU/Linux 12 (bookworm)   5.15.167.4-microsoft-standard-WSL2   containerd://1.7.13
```

👉 *Mostra os nós do cluster com informações detalhadas como versão, estado e endereços IP.*

## 3. Visualizar Pods em Execução

```bash
kubectl get pods -o wide
```
resposta:
```bash
kubectl get pods -o wide
NAME                       READY   STATUS    RESTARTS   AGE   IP           NODE                        NOMINATED NODE   READINESS GATES
waha-7554f7945d-b45gq      1/1     Running   0          52m   10.244.0.5   wpp-cluster-control-plane   <none>           <none>
wpp-api-565f5fb857-qmklc   1/1     Running   0          20m   10.244.0.9   wpp-cluster-control-plane   <none>           <none>

```
👉 *Mostra todos os pods em execução, incluindo o waha e wpp-api, com informações como estado, reinícios e IPs.*

## 4. Verificar Serviços

```bash
kubectl get services
```
👉 *Mostra os serviços configurados, incluindo seus tipos e portas.*

resposta:
```bash
kubectl get services
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          72m
waha         NodePort    10.96.236.223   <none>        3000:32342/TCP   53m
wpp-api      NodePort    10.96.153.198   <none>        5000:32647/TCP   53m
```

## 5. Verificar Estrutura Completa do Cluster

```bash
kubectl get all
```

resposta:
```bash
 kubectl get services
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          72m
waha         NodePort    10.96.236.223   <none>        3000:32342/TCP   53m
wpp-api      NodePort    10.96.153.198   <none>        5000:32647/TCP   53m
(3.9.7) paribe@paribe:~/whatsapp_ai_chatbot-main$ kubectl get all
NAME                           READY   STATUS    RESTARTS   AGE
pod/waha-7554f7945d-b45gq      1/1     Running   0          54m
pod/wpp-api-565f5fb857-qmklc   1/1     Running   0          21m

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          73m
service/waha         NodePort    10.96.236.223   <none>        3000:32342/TCP   54m
service/wpp-api      NodePort    10.96.153.198   <none>        5000:32647/TCP   54m

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/waha      1/1     1            1           54m
deployment.apps/wpp-api   1/1     1            1           54m

NAME                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/waha-7554f7945d      1         1         1       54m
replicaset.apps/wpp-api-565f5fb857   1         1         1       21m
replicaset.apps/wpp-api-6689c478cc   0         0         0       54m
replicaset.apps/wpp-api-6c44dcc58c   0         0         0       23m
```
👉 *Mostra todos os recursos (pods, serviços, deployments) em um único comando - ótimo para uma visão geral.*

## 6. Checar Detalhes dos Deployments

```bash
kubectl get deployments -o wide
```
👉 *Mostra os deployments com detalhes, incluindo réplicas e estratégias.*


resposta :
```bash
 kubectl get deployments -o wide
NAME      READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS   IMAGES                    SELECTOR
waha      1/1     1            1           56m   waha         devlikeapro/waha:latest   app=waha
wpp-api   1/1     1            1           56m   api          wpp-api:latest            app=wpp-api
```


## 7. Verificar Volumes Persistentes

```bash
kubectl get pv,pvc
```
👉 *Mostra os volumes persistentes e as solicitações de volumes.*


resposta:
```bash
kubectl get pv,pvc
NAME                                                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM                STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
persistentvolume/chroma-pv                                  1Gi        RWO            Retain           Available                                       <unset>                          56m
persistentvolume/pvc-df8ba631-b088-47bb-90e5-4b85dc5dd181   1Gi        RWO            Delete           Bound       default/chroma-pvc   standard       <unset>                          56m

NAME                               STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/chroma-pvc   Bound    pvc-df8ba631-b088-47bb-90e5-4b85dc5dd181   1Gi        RWO            standard       <unset>                 56m
(3.9.7) paribe@paribe:~/whatsapp_ai_chatbot-main$ 

```
## 8. Verificar a Versão do Kubernetes

```bash
kubectl version --client
```
👉 *Mostra as versões do cliente e servidor Kubernetes em formato compacto.*

resposta :
```bash
(3.9.7) paribe@paribe:~/whatsapp_ai_chatbot-main$ kubectl version --client
Client Version: v1.29.2
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```

## 9. Verificar a Saúde do Cluster

```bash
kubectl cluster-info
```
👉 *Mostra informações sobre o plano de controle e serviços principais do Kubernetes.*

resposta :
```bash
(3.9.7) paribe@paribe:~/whatsapp_ai_chatbot-main$ kubectl cluster-info
Kubernetes control plane is running at https://127.0.0.1:34911
CoreDNS is running at https://127.0.0.1:34911/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```


## 10. Verificar Uso de Recursos (CPU/Memória)

```bash
kubectl top nodes
kubectl top pods
```
👉 *Mostra o uso de CPU e memória dos nós e pods (requer o metrics-server instalado).*

## 11. Ver Logs da API (útil para mostrar atividade)

```bash
kubectl logs $(kubectl get pods | grep wpp-api | awk '{print $1}') --tail=10
```
👉 *Mostra as últimas 10 linhas de logs do pod da API.*

## 12. Verificar Port-Forward Ativo

```bash
ps aux | grep port-forward | grep -v grep
```
👉 *Mostra processos port-forward em execução, demonstrando que você pode acessar os serviços localmente.*

## 13. Testar a API (para mostrar a resposta)

```bash
curl http://localhost:5001/test
```
👉 *Mostra a resposta da API, confirmando que está funcionando.*

## 14. Diagrama Visual do Cluster (com kubectl-topology)

Se você tiver a ferramenta `kubectl-topology` instalada:
```bash
kubectl topology
```
👉 *Cria uma visualização gráfica dos seus recursos Kubernetes.*

## 15. Status da Implantação com Detalhes

```bash
kubectl rollout status deployment/wpp-api
kubectl rollout status deployment/waha
```
👉 *Mostra o status da implantação, confirmando que está concluída com sucesso.*

## Exemplo de Captura para o README.md

Para um README.md impressionante, sugiro criar uma seção como esta:

```markdown
## Implantação com Kubernetes (Kind)

O WhatsApp AI Chatbot pode ser implantado usando Kubernetes através do Kind para desenvolvimento local. Abaixo estão capturas de tela mostrando o ambiente em execução:

### 1. Cluster Kubernetes em Execução
![Cluster Kind](screenshots/kind-cluster.png)

### 2. Serviços e Pods
![Pods e Serviços](screenshots/pods-services.png)

### 3. Teste da API
![Teste da API](screenshots/api-test.png)

### 4. Interface WhatsApp (WAHA)
![Interface WAHA](screenshots/waha-interface.png)
```

Sugestão: Combine vários comandos em uma única captura de tela para mostrar o status completo do sistema. Por exemplo:

```bash
echo "=== Cluster Kind ===" && kind get clusters && \
echo -e "\n=== Pods ===" && kubectl get pods && \
echo -e "\n=== Serviços ===" && kubectl get services && \
echo -e "\n=== Volume Persistente ===" && kubectl get pv,pvc && \
echo -e "\n=== Teste API ===" && curl http://localhost:5001/test
```

Isso criará uma saída completa e ordenada, perfeita para incluir em uma captura de tela para o README.md.
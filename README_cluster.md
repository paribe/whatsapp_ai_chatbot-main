

### ✅ Visão geral do que faremos

1. **Instalar o Kind** (caso ainda não tenha).
2. **Criar um cluster Kind.**
3. **Transformar o `docker-compose.yml` em manifests Kubernetes.**
4. **Carregar as imagens Docker locais no Kind.**
5. **Deployar no Kind.**
6. **Criar um arquivo `README_cluster.md` com o resumo.**

---

### 🧩 Passo 1: Verificar/instalar Kind no WSL

No seu terminal (WSL), rode:

```bash
kind version
```

Se não estiver instalado, instale com:

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

---

### 🧩 Passo 2: Criar um cluster Kind

```bash
kind create cluster --name wpp-cluster
```

Verifique se o cluster subiu:

```bash
kubectl cluster-info --context kind-wpp-cluster
```

---

### 🧩 Passo 3: Criar os manifests Kubernetes com base no `docker-compose.yml`

Vamos precisar criar:

* 2 `Deployment`s (um para o `waha`, outro para o `api`)
* 2 `Service`s (para expor as portas 3000 e 5000)

Mas antes... preciso confirmar:

#### ❓ Perguntas rápidas para acertar tudo:

1. O serviço `api` depende do `waha`?
2. O `.env` da API é importante para o funcionamento? (Contém configs de DB, etc?)
3. O diretório `chroma_data` precisa manter dados entre reinicializações?

Se preferir, posso já te mandar os YAMLs padrões e depois ajustamos.

Assim que você responder, continuo os próximos passos e depois gero o `README_cluster.md` completo.

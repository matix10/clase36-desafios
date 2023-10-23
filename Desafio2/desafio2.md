# Desplegar una imagen en minikube.

En esta práctica utilizaremos nuestra imagen creada en el desafío anterior, solo que esta
vez en vez de utilizarla para correr contenedores de docker, la utilizaremos para correr pods
en Kubernetes. Para esto, este desafío consta de 2 etapas, la primera crearemos un cluster
utilizando una herramienta a gusto (microk8s, minikube, kind, kubernetes the hard way, etc)
y en la segunda etapa, crearemos un Deployment utilizando nuestra imagen que creamos
antes.

## Entregable:

* Instructivo con los pasos seguidos para la creación del cluster de kubernetes
* Archivos .yaml utilizados para levantar correctamente la aplicación.

Siguiendo los lineamientos de la anterior práctica, en este caso planteamos los siguientes
requisitos que tendrá que tener nuestra aplicación en kubernetes:

* Tendrá que ser un deployment si o si (no pod, no replica set)
* Tendrá que tener algún tipo de volumen o secreto configurado
* Tendrá que ser expuesto a fuera del cluster (ClusterIP)
* Tendrá que tener entre 3 y 5 réplicas idealmente
* Tendrá que tener un método de rollback configurado distinto al default.

### Consejos:

No perder mucho tiempo en la configuración del cluster, ir por la opción más sencilla ya que
la mayor parte del desafío se concentra en la entrega del deployment y su configuración.

Links:

[Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/)
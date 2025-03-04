"""
.. _configure-gpus:

Configuring Flyte to Access GPUs
--------------------------------

Along with the simpler resources like CPU/Memory, you may want to configure and access GPU resources. Flyte
allows you to configure the GPU access poilcy for your cluster. GPUs are expensive and it would not be ideal to
treat machines with GPUs and machines with CPUs equally. You may want to reserve machines with GPUs for tasks
that explicitly request GPUs. To achieve this, Flyte uses the Kubernetes concept of `taints and tolerations <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>`__.

You can configure Flyte backend to automatically schedule your task onto a node with GPUs by tolerating specific taints.
This configuration is controlled under generic k8s plugin configuration as can be found `here <https://github.com/flyteorg/flyteplugins/blob/master/go/tasks/pluginmachinery/flytek8s/config/config.go#L105-L107>`__.

The idea of this configuration is that whenever a task that can execute on Kubernetes requests for GPUs, it automatically
adds the matching toleration for that resource (in this case, ``gpu``) to the generated PodSpec.
As it follows here, you can configure it to access specific resources using the tolerations for all resources supported by
Kubernetes.

Here's an example configuration:

.. code-block:: yaml

    plugins:
      k8s:
        resource-tolerations:
          - nvidia.com/gpu:
            - key: "key1"
              operator: "Equal"
              value: "value1"
              effect: "NoSchedule"
"""

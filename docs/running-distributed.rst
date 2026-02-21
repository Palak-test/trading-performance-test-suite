.. running-distributed.rst

Running Distributed
===================

Loopa supports distributed load testing across multiple machines.

- Start master node: `python -m loopa --master`
- Start worker nodes: `python -m loopa --worker --host <master-ip>`

Workers will connect to the master and generate load together.

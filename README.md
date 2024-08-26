# dat620_project
## Evaluating the state of GPU availability from the web



The incorporation of generative AI in different products and daily routines will significantly increase the requirements for hardware and electricity resources.  GPUs are at the heart of hardware requirements and the efficient and scalable usage of GPU resources may be a key to solve these challenges. The availability to access client side GPU resources for custom AI tasks via the web may be a major contribution to reduce resource shortage.
However, GPU resources located at one client may be limited. It is, therefore, relevant to investigate how to combine the resources available by different clients.


The main goal of this project is to evaluate the readiness of projects like WebGPU for custom ML tasks.

- Write a background summary on GPU programming and WebGPU
- Investigate the feasibility to port or reimplement a distributed inference system, such as Petals or Helix based on webGPU.


Current TODO:

0. IN_PROGRESS: Write intro and background information/research.

1. IN_POROGRESS: Make a minimal version of a generative AI run on webgpu through a web client
    - TODO: Backend server
    - TODO: WebGpu client code
    - TODO: Load and run model on webgpu browser client
    - TODO: Write about progress in report

2. TODO: Distribute across sevral clients
    - TODO: Simple interface and websocket communication with other clients mediated through backend.
    - TODO: Show that it is possible to split a small model and run it on two clients. 
    - TODO: Show that it is possible to split a medium model and run it on sevral clients. 
    - TODO: Write about progress in report

3. FUTURE_WORK: How does it scale? Testing and experiments. 

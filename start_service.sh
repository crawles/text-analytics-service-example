unset PYTHONPATH
jupyter-kernelgateway --KernelGatewayApp.port=$PORT\
                      --KernelGatewayApp.ip=0.0.0.0\
                      --KernelGatewayApp.api=notebook-http\
                      --KernelGatewayApp.seed_uri='Untitled.ipynb'

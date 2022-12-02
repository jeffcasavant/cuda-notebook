build:
	docker build . -t jeffcasavant/cuda-notebook

run:
	docker run --gpus all -p 8888:8888/tcp jeffcasavant/cuda-notebook

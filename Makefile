build:
	docker build . -t jeffcasavant/cuda-notebook

run:
	docker run --gpus all -p 8889:8888/tcp --mount type=bind,source="$$(pwd)",target=/home/jovyan jeffcasavant/cuda-notebook

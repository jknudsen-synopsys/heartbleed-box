source name.sh
docker run \
	-it \
	--rm \
	-p 4433:4433 \
	--memory=512m --memory-swap=512m \
	--name ${IMAGE} \
	${IMAGE}

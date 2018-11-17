REPOSITORY_URL = vjftw/vuepress

build:
	docker build -t ${REPOSITORY_URL}:1.0.0 -t ${REPOSITORY_URL}:latest .

publish:
	docker push ${REPOSITORY_URL}:1.0.0
	docker push ${REPOSITORY_URL}:latest
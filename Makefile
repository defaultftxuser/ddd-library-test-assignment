DC = docker-compose
APP_FILE = docker_compose/docker_compose_app.yaml
STORAGE_FILE = docker_compose/docker_compose_storages.yaml
ENV = --env-file . env

.PHONY: app
app-start:
	${DC} -f ${APP_FILE} ${ENV} up -d

.PHONY: drop-app
drop-app:
	${DC} -f ${APP_FILE} down

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} ${ENV} up -d

.PHONY: drop-storage
drop-storage:
	${DC} -f ${STORAGE_FILE} down

.PHONY: all
all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} {ENV} up --build -d


.PHONY: drop-all
drop-all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: logs
logs:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} logs -f

# Variables
APP_NAME=dataset-flights-brazil
ROOT=$(shell pwd)

## Lint
DOCKER_IMAGE_LINTER=alvarofpp/linter:latest
LINT_COMMIT_TARGET_BRANCH=origin/main

# Commands
.PHONY: install-hooks
install-hooks:
	git config core.hooksPath .githooks

.PHONY: build
build: install-hooks
	@docker compose build --pull

.PHONY: build-no-cache
build-no-cache: install-hooks
	@docker compose build --no-cache --pull

.PHONY: lint
lint:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-commit ${LINT_COMMIT_TARGET_BRANCH} \
		&& lint-markdown \
		&& lint-dockerfile \
		&& lint-yaml \
		&& lint-shell-script \
		&& lint-python"

.PHONY: shell
shell:
	@UID_GID="$(id -u):$(id -g)" docker compose run --rm ${APP_NAME} bash

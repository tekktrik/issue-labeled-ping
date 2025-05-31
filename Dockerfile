# SPDX-FileCopyrightText: 2025 Alec Delaney
# SPDX-License-Identifier: MIT

FROM python:3.13.3-alpine

WORKDIR /action

COPY action.py action.py
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

RUN pip install uv

ENTRYPOINT [ "uv", "run", "action.py" ]

# ===============
# --- Release ---
# ===============
FROM python:3.7.9-buster
LABEL maintainer="stop_car_be"

ENV env "product"

RUN mkdir -p /ru_be

WORKDIR /ru_be
COPY ./ ./
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

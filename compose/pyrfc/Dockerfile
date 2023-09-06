FROM nefistofeles/pyrfc:lastet

EXPOSE 80

# Install gunicorn & falcon
RUN pip install --upgrade pip
RUN pip install importlib-metadata falcon==3.0.0 gunicorn==20.1.0

# Add demo app
COPY ./app /app
WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]
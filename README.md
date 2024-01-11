# xlm-roberta-base-multilingual-text-genre-classifier test container

The aim of this project is providing a out-of-box way to test the Huggingface's [xlm-roberta-base-multilingual-text-genre-classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) model without having to deal with the setup process.
A pre-configured Docker container is provided, allowing you to easily utilize it via a straightforward HTTP REST API.

Please note that this is *only for testing purposes* and is not ready for production environment. Take it with caution

### Build the container image

```docker build -t name roberta-classif .```

## Run the container
```docker run -dti --name roberta-01 -p 8080:80 roberta-classif```

Since it has to download the entire model ~1.11Gb, It may take a few minutes to get the container up and running.
You can check the current status with:
```docker logs -f roberta-01```

## Test the container
Just to check

```curl http://127.0.0.1:8080/api/tags''```

Try to classify some text

```curl -X POST -H "Content-Type: application/json" -d '{"input_string": ["On our site, you can find a great genre identification model which you can use for thousands of different tasks."]}' http://127.0.0.1:8080/api/classify```



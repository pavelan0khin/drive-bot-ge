# Drive Bot GE

### The readme file is not 100% complete yet, in the future I will try to describe it in more detail

Telegram: [@driveticketsbot](https://t.me/driveticketsbot)

A Telegram bot designed for studying the road traffic rules in Georgia, as well as an API service accessible through HTTP REST API and GRPC protocols. To learn more about the API, send the command `/api` to the bot.

Both the bot and API support 7 languages:

- English
- Russian
- Ukrainian
- Georgian
- Turkish
- Armenian
- Azerbaijani

Find more details about translations [here](src/drive/bot/i18n/README.md).





### Steps for Local Development:

If you'd like to run the bot locally, here are the necessary dependencies:

- python
- docker
- postgresql
- poetry

1. Ensure you have `poetry` installed. If not, you can download it [here](https://python-poetry.org/).
2. Clone the project locally, for instance into `~/code`.
3. Navigate to the directory `~/code/drive-bot-ge` and activate the poetry environment using:

```shell
poetry env use 3.11
```

4. Install the dependencies:

```shell
poetry install
```
5. Set up the database for the project, e.g., using a local postgresql server. For instance, you can name the database `drive-bot`.
6. In the directory `~/code/drive-bot-ge`, create a `.env` file and define the necessary variables. Check out the [.env.example](.env.example) for reference.
7. Apply the migrations:
```shell
poetry run python src/manage.py migrate
```
8. Start the local MinIO storage:
```shell
docker-compose up -d minio
```
9. In your browser, visit [http://localhost:9001/](http://localhost:9001/) and log in using the `MINIO_ROOT_USER` as the username and `MINIO_ROOT_PASSWORD` from your `.env` file as the password.
10. Create a new access key pair at [http://localhost:9001/access-keys/new-account](http://localhost:9001/access-keys/new-account). Store the 'Access Key' value in the `AWS_ACCESS_KEY_ID` and 'Secret Key' value in the `AWS_SECRET_ACCESS_KEY` of your `.env` file.
11. Navigate to [http://localhost:9001/buckets/add-bucket](http://localhost:9001/buckets/add-bucket) and create a bucket with the same name as you've defined in the `AWS_STORAGE_BUCKET_NAME` in your `.env` file.
12. Back in the terminal, run the following command to upload images to the storage:
```shell
poetry run python src/manage.py load_images
```
13. Now, you can start the web server with:
```shell
poetry run python src/manage.py runserver
```
14. To create an admin superuser, run:
```shell
poetry run python src/manage.py createsuperuser
```
15. With the credentials from the previous step, you can log in to the admin site at [http://localhost:8000/admin/](http://localhost:8000/admin/).
16. For the server to receive notifications from Telegram, set up a webhook. After logging into the admin, go to [http://localhost:8000/bot/set-webhook/](http://localhost:8000/bot/set-webhook/).
17. Now, head to your Telegram bot and send the `/start` command.

## API:

GRPC contract is available at [https://github.com/pavelan0khin/drive-bot-proto](https://github.com/pavelan0khin/drive-bot-proto).


You can find information about the endpoint in the [bot](https://t.me/driveticketsbot) by sending the command /api. There you can also get a link to documentation in openapi and redoc format


# If you want to thank me, you can support the project with money:

### Bank Of Georgia:

Account Number: GE44BG0000000537911384


### TBC:

Account number: GE11TB7126945064400003


### Crypto:

USDT TRC20: TDS3DYJYZJ8D1uwQrtLxQrJ9yokuQDvAmi

BTC: bc1q6yhdcehgq8xnjkxx8c33ulcr8czahctwskqgjz

Ethereum: 0xE5827528FFf4c248A3d8bB35A2aAF9863c434Ca6


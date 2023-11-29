# E85 Stations Finder

This is a Django web application that allows users to find E85 stations within a certain radius of a given zip code.

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/Wombat45/e85stations.git
    ```
2. Navigate to the project directory:
    ```
    cd e85stations
    ```
3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```
4. Run the server:
    ```
    python manage.py runserver
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:8000`.
2. Enter a zip code and a radius in miles, then click "Submit".
3. The application will display a list of E85 stations within the given radius of the zip code.

## Testing

To run the tests, use the following command:

python manage.py test

## Contributing 

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
# Engineer Test

This project provides an API that can be used to search using a search criteria.

## Developer setup

This project is based on Python3.7, so verify your local python installation to have the same version.
We can use a virtual environment and install the required packages in order to create the development environment and test the API.
Follow the steps to prepare your environment:
1. Create virtualenv
    ```
    python3 -m venv {my_virtual_env}
    ```
2. Activate the virtualenv
    ```
    source {my_virtual_env}/bin/activate
    ```
3. Install required packages
    ```
    pip install -r requirements.txt
    ```

4. Move to the project folder and migrate for the first time:
    ```
    cd search_service
    python manage.py migrate
    ```

5. Start the server
    ```
    python manage.py runserver
    ```
## Usage

Now we can access the route http://127.0.0.1:8000/ and we can type the search criteria.

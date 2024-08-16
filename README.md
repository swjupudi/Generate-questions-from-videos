### Prerequisites

- Python 3.6 or higher
- Anaconda to create new environment
- Openai key


### Installing

1. **Clone the repository:**

```
git clone git@github.com:swjupudi/Generate-questions-from-videos.git
```


2. **Create and activate a virtual environment:**

- Navigate to the project directory:
  ```
  cd <path/to/project>
  ```
- Create a virtual environment:
  ```
  conda create -n <environment name> python==3.12
  ```
  Eg: 
   ```
  conda create -n quiz_from_videos python==3.12
  ```
- Activate the virtual environment:
  - On macOS/Linux:

    ```
    conda activate <environment name>
    ```
    Eg
    ```
    conda activate quiz_from_videos
    ```
  - pip install ipykernel

3. **Install dependencies:**

With the virtual environment activated, install the requirements using:

```
pip install -r requirements.txt
```

### Running the Project

Use Ec2 instance public address or local host.

```
streamlit run quiz_app.py
```

This command launches the server, typically accessible at `http://127.0.0.1:5000/`.





if __name__ == "__main__":
    data_processing_file = 'wf_dataprocessing.py'
    visualization_file  = 'wf_visualization.py'

    try:
        with open(data_processing_file, 'r') as file:
            code = file.read()
            exec(code)
    except FileNotFoundError:
        print(f"The file '{data_processing_file}' does not exist.")

    try:
        with open(visualization_file, 'r') as file:
            code = file.read()
            exec(code)
    except FileNotFoundError:
        print(f"The file '{visualization_file}' does not exist.")
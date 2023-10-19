import wf_dataprocessing as process_data
import wf_visualization as visualize

if __name__ == "__main__":
    process_data.data_processing()
    visualize.visualization()

    # import hashlib
    # import glob
    # files = glob.glob('data_original\*.xlsx')
    # for x in files:
    # x = r"data_original\\us.-literacy-rates-by-state-[updated-june-2023].csv"
    #     md5 = hashlib.md5()
    #     with open(x, "rb") as file:
            
    #         while True:
    #                 data = file.read(8192)
    #                 if not data:
    #                         break
    #                 md5.update(data)
    #         print(md5.hexdigest())
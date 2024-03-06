
from huggingface_hub import snapshot_download
import os
import time




def download_model_hf(data_folder='/data/google/flan-t5-small', model_id='google/flan-t5-small'):
    print('Downloading from hugging face.')

    print(f'Downloading model "{model_id}" ')

    snapshot_download(repo_id=model_id,local_dir=data_folder,local_dir_use_symlinks=False)

    

if __name__ == '__main__':
    download_model_hf(data_folder='/data/google/flan-t5-small', model_id='google/flan-t5-small')

from huggingface_hub import snapshot_download



def download_model_hf(data_folder='./data', model_id='google/flan-t5-small'):
    print('Downloading from hugging face.')

    print(f'Downloading model "{model_id}" ')

    snapshot_download(repo_id="bert-base-uncased",local_dir=data_folder,local_dir_use_symlinks="auto")



if __name__ == '__main__':
    download_model_hf(data_folder='./data', model_id='google/flan-t5-small')
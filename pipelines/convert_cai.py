import caikit_nlp
import time
import os



def convert(input_folder='./data/google/flan-t5-small', output_folder='./data/google/converted/flan-t5-small'):
    os.makedirs(output_folder, exist_ok=True)

    start_time = time.time()
    model = caikit_nlp.text_generation.TextGeneration.bootstrap(input_folder)
    model.save(model_path=output_folder)
    end_time = time.time()
    print(f"Time taken: **{end_time - start_time:.5f} seconds**")



if __name__ == '__main__':
    convert(input_folder='./data/google/flan-t5-small', output_folder='./data/google/converted/flan-t5-small')
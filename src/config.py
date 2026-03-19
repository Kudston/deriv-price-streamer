import os

class Settings:
    current_dir = os.path.curdir
    print(current_dir)
    symbols_save_file = os.getenv('ACTIVE_SYMBOL_FILE',os.path.join(current_dir,'symbols.csv'))
    redis_host  = os.getenv('REDIS_HOST','redis')
    redis_port  =  os.getenv('REDIS_PORT','6379')
    tick_data_key = os.getenv('TICK_DATA_KEY','tick_data')
    
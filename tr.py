from pyabsa.functional import APCConfigManager
from pyabsa.functional import Trainer
from autocuda import auto_cuda

config = APCConfigManager.get_apc_config_english() # APC task
# dataset = '101.restaurant'
dataset = '100.CustomDataset'
Trainer(config=config,
        dataset=dataset,  # train set and test set will be automatically detected
        checkpoint_save_mode=1,
        auto_device=auto_cuda()  # automatic choose CUDA or CPU
        )
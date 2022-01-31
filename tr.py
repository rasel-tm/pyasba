from pyabsa import ATEPCConfigManager, ClassificationConfigManager
from pyabsa.functional import APCConfigManager
from pyabsa.functional import Trainer
from autocuda import auto_cuda

# Set
APCConfigManager.set_apc_config_base({'num_epoch': 2})

# config = APCConfigManager.get_apc_config_english() # APC task
config = APCConfigManager.get_apc_config_base()
# dataset = '101.restaurant'
dataset = '101.my'
# dataset = '100.CustomDataset'
Trainer(config=config,
        dataset=dataset,  # train set and test set will be automatically detected
        checkpoint_save_mode=1,
        auto_device=auto_cuda()  # automatic choose CUDA or CPU
        # auto_device='cpu'  # automatic choose CUDA or CPU
        )
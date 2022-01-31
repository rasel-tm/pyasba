from pyabsa import APCCheckpointManager


sent_classifier = APCCheckpointManager.get_sentiment_classifier(checkpoint='checkpoints/bert_spc_custom_dataset_acc_84.49_f1_54.97/',
                                                                auto_device=False,  # Use CUDA if available
                                                                )

examples_unknown =['আপনার দল [ASP]বিএনপি[ASP] নেতারা রাজনীতি করে নিজেদের স্বাথর্ জন্য এক কথা পকেট রাজনীতি দল [ASP]বিএনপি[ASP] একজন ভালো মানুষ যোগ্যতা হিসেবে বেশি আপনি আপনার দল চাইনি আপনি [ASP]নির্বাচন[ASP] করুন এটাই আপনার পতনের মুল']
for ex in examples_unknown:
    result = sent_classifier.infer(ex, print_result=True)

    print('\n\n')
    print(result)
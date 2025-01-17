import argparse

from src.utils.file_utils import get_result_filename
from src.utils.config import (
    vocab_path,
    train_x_seg_path,
    train_y_seg_path,
    test_x_seg_path,
    sample_total,
    batch_size,
    save_result_dir,
    epochs,
    checkpoint_dir,
    vocab_size
)


def get_params():
    # 获得参数
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default='test', help="run mode", type=str)
    parser.add_argument("--max_enc_len", default=400, help="Encoder input max sequence length", type=int)
    parser.add_argument("--max_dec_len", default=100, help="Decoder input max sequence length", type=int)
    parser.add_argument("--batch_size", default=batch_size, help="batch size", type=int)
    parser.add_argument("--epochs", default=epochs, help="train epochs", type=int)
    parser.add_argument("--vocab_path", default=vocab_path, help="vocab path", type=str)
    parser.add_argument("--learning_rate", default=0.15, help="Learning rate", type=float)
    parser.add_argument("--adagrad_init_acc", default=0.1,
                        help="Adagrad optimizer initial accumulator value. "
                             "Please refer to the Adagrad optimizer API documentation "
                             "on tensorflow site for more details.",
                        type=float)
    parser.add_argument('--rand_unif_init_mag', default=0.02,
                        help='magnitude for lstm cells random uniform inititalization', type=float)
    parser.add_argument('--trunc_norm_init_std', default=1e-4, help='std of trunc norm init, '
                                                                    'used for initializing everything else',
                        type=float)

    parser.add_argument('--cov_loss_wt', default=1.0, help='Weight of coverage loss (lambda in the paper).'
                                                           ' If zero, then no incentive to minimize coverage loss.',
                        type=float)

    parser.add_argument('--max_grad_norm', default=2.0, help='for gradient clipping', type=float)

    parser.add_argument("--vocab_size", default=vocab_size, help="max vocab size , None-> Max ", type=int)

    parser.add_argument("--beam_size", default=batch_size,
                        help="beam size for beam search decoding (must be equal to batch size in decode mode)",
                        type=int)
    parser.add_argument("--embed_size", default=300, help="Words embeddings dimension", type=int)
    parser.add_argument("--enc_units", default=400, help="Encoder GRU cell units number", type=int)
    parser.add_argument("--dec_units", default=400, help="Decoder GRU cell units number", type=int)
    parser.add_argument("--attn_units", default=400, help="[context vector, decoder state, decoder input] feedforward \
                                result dimension - this result is used to compute the attention weights",
                        type=int)
    parser.add_argument("--train_seg_x_dir", default=train_x_seg_path, help="train_seg_x_dir", type=str)
    parser.add_argument("--train_seg_y_dir", default=train_y_seg_path, help="train_seg_y_dir", type=str)
    parser.add_argument("--test_seg_x_dir", default=test_x_seg_path, help="train_seg_x_dir", type=str)

    parser.add_argument("--checkpoint_dir", default=checkpoint_dir,
                        help="checkpoint_dir",
                        type=str)

    parser.add_argument("--checkpoints_save_steps", default=5, help="Save checkpoints every N steps", type=int)
    parser.add_argument("--min_dec_steps", default=4, help="min_dec_steps", type=int)

    parser.add_argument("--max_train_steps", default=sample_total // batch_size, help="max_train_steps", type=int)
    parser.add_argument("--save_batch_train_data", default=False, help="save batch train data to pickle", type=bool)
    parser.add_argument("--load_batch_train_data", default=False, help="load batch train data from pickle",
                        type=bool)
    parser.add_argument("--test_save_dir", default=save_result_dir, help="test_save_dir", type=str)
    parser.add_argument("--pointer_gen", default=False, help="pointer_gen", type=bool)
    parser.add_argument("--use_coverage", default=False, help="use_coverage", type=bool)

    parser.add_argument("--greedy_decode", default=False, help="greedy_decode", type=bool)
    parser.add_argument("--result_save_path", default=get_result_filename(batch_size, epochs, 200, 300),
                        help='result_save_path', type=str)
    args = parser.parse_args()
    params = vars(args)
    return params


def get_default_params():
    params = {"mode": 'train',
              "max_enc_len": 400,
              "max_dec_len": 32,
              "batch_size": batch_size,
              "epochs": 25,
              "vocab_path": vocab_path,
              "learning_rate": 0.15,
              "adagrad_init_acc": 0.1,
              "rand_unif_init_mag": 0.02,

              "trunc_norm_init_std": 1e-4,

              "cov_loss_wt": 1.0,

              "max_grad_norm": 2.0,
              "vocab_size": 31820,

              "beam_size": batch_size,
              "embed_size": 300,
              "enc_units": 128,
              "dec_units": 128,
              "attn_units": 128,

              "train_seg_x_dir": train_x_seg_path,
              "train_seg_y_dir": train_y_seg_path,
              "test_seg_x_dir": test_x_seg_path,

              "checkpoints_save_steps": 5,
              "min_dec_steps": 4,

              "max_train_steps": sample_total // batch_size,
              "train_pickle_dir": '/opt/kaikeba/dataset/',
              "save_batch_train_data": False,
              "load_batch_train_data": False,

              "test_save_dir": save_result_dir,
              "pointer_gen": True,
              "use_coverage": True}
    return params

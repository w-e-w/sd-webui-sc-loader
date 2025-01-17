'''
    A rather crappy but useful module to handle global variables, should be reworked.
'''

import os

from modules.shared import opts

from .config import load_dir_element

version = '5.0.2'


database     = None
scenario     = None
batch        = None
tags         = []
hr           = False
restore      = False
upscaler     = None
chars        = None
char_prompts = None
sampler      = None
steps        = None
characters   = None
cfg_scale    = None
model        = None
nb_iter      = None
nb_batches   = None
nb_repeats   = None
positive     = None
negative     = None
upscale_by   = None
seed         = -1
denoise_args = None
current_payload    = None
skipped_model      = None
hard_skip_toggled  = None
denoising_strength = None
expected_characters_idxs = []
poses_masks_generated = []

skip_model = False

short_prompts = {'positive': '', 'negative': ''}

DB_DIR = '_db'

def prefix(file_name):
    return ''.join((part[0:4] for part in file_name.split('_')))

def load_db():
    global database
    database = load_dir_element(f'{opts.sc_loader_config_path}/{DB_DIR}')
    path_to_types = f'{opts.sc_loader_config_path}/{DB_DIR}/prompts'
    for file_name in os.listdir(path_to_types):
        if os.path.isdir(path_to_types + '/' + file_name) and file_name[0] != '_':
            for key, value in database['prompts'][file_name].items():
                database['prompts'][prefix(file_name)+'_'+key] = value

def skip():
    global skipped_model, skip_model
    skip_model = True
    skipped_model = current_payload['override_settings']['sd_model_checkpoint'] # pylint: disable=unsubscriptable-object

def init():
    global scenario, batch, tags, hr, restore, upscaler, chars, sampler, steps, characters,\
            cfg_scale, model, nb_iter, nb_batches, nb_repeats, seed, positive, negative,\
            denoising_strength, upscale_by, hard_skip_toggled, current_payload,\
            skipped_model, char_prompts
    load_db()
    scenario     = None
    batch        = None
    tags         = []
    hr           = False
    restore      = False
    upscaler     = None
    chars        = None
    char_prompts = None
    sampler      = None
    steps        = None
    characters   = None
    cfg_scale    = None
    model        = None
    nb_iter      = None
    nb_batches   = None
    nb_repeats   = None
    positive     = None
    negative     = None
    upscale_by   = None
    seed         = -1
    current_payload    = None
    skipped_model      = None
    hard_skip_toggled  = None
    denoising_strength = None

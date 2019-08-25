# -*- coding: utf-8 -*-
import os
import re
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from slackbot.bot import respond_to

DOWNLOAD_PATH = '/tmp/'

# 半角英数字, 記号, 空白を OKにした
@respond_to('^[a-zA-Z0-9!-/:-@¥[-`{-~\s]*$')
def smiles_to_png(message):
    smiles_text = message.body['text'].strip()

    smiles = None
    if re.search(r',' , smiles_text):
        smiles = smiles_text.split(',')
    elif re.search(r'\s' , smiles_text):
        smiles = re.split(r'\s', smiles_text)
    else:
        smiles = [smiles_text]

    # remove empty string element
    smiles = [val for val in smiles if val]
    if len(smiles) > 0:
        for val in smiles:
            try:
                m = Chem.MolFromSmiles(val)
                AllChem.Compute2DCoords(m)
                name = '{}.png'.format(val)
                path = DOWNLOAD_PATH + name
                Draw.MolToFile(m, path)
                message.channel.upload_file(fname=name, fpath=path)
                os.remove(path)
            except:
                message.reply('Sorry, {} is invalid SMILES.'.format(val))
    else:
        message.reply('There is no input text.')

# -*- coding: utf-8 -*-
import os
import re
import glob
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
                val = re.sub(r"<|>", "", val)
                val = re.sub(r"(http).*(\|)", "", val)
                mol = Chem.MolFromSmiles(val)
                if not mol.GetNumConformers():
                    AllChem.Compute2DCoords(mol)

                # create image
                drawer = Draw.MolDraw2DCairo(400, 400)
                drawer.DrawMolecule(mol)
                drawer.FinishDrawing()

                # write png
                name = '{}.png'.format(val)
                # replace slash
                name = name.replace('/', '').replace('\\', '')
                # avoid too long string
                if len(name) > 250:
                    name = name[0:250]
                png_path = DOWNLOAD_PATH + name
                with open(png_path, 'wb') as f:
                    f.write(drawer.GetDrawingText())

                # post png
                message.channel.upload_file(fname=name, fpath=png_path)
            except:
                message.reply('Sorry, {} is invalid SMILES or Failed Drawing'.format(val))

        # clean tmp dir
        for p in glob.glob(DOWNLOAD_PATH + '*.png'):
            os.remove(p)
    else:
        message.reply('There is no input text.')

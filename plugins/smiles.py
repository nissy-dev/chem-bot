# -*- coding: utf-8 -*-
import os
import re
import cairosvg
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
                png_path = DOWNLOAD_PATH + name
                svg_path = DOWNLOAD_PATH + '{}.svg'.format(val)
                # Draw.MolToFile(m, svg_path)
                view = Draw.rdMolDraw2D.MolDraw2DSVG(500,500)
                processed_mol = Draw.rdMolDraw2D.PrepareMolForDrawing(m)
                view.DrawMolecule(processed_mol)
                view.FinishDrawing()
                svg = view.GetDrawingText()
                with open(svg_path, 'w') as f:
                    f.write(svg)
                cairosvg.svg2png(url=svg_path, write_to=png_path)
                message.channel.upload_file(fname=name, fpath=png_path)
                os.remove(png_path)
                os.remove(svg_path)
            except:
                message.reply('Sorry, {} is invalid SMILES.'.format(val))
    else:
        message.reply('There is no input text.')

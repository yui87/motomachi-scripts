#!/usr/bin/env fontforge -lang=py -script
# -*- coding: utf-8 -*-

import fontforge
from datetime import date

# Inter のあるディレクトリのパス
inter_path = "./inter/static"

# M PLUS 1p のあるディレクトリのパス
mplus_path = "./mplus"

# Roboto のあるディレクトリのパス
roboto_path = "./roboto"

# Motomachi を生成するディレクトリのパス
# 同じディレクトリに一時ファイルも生成される
motomachi_path = "./motomachi"

# フォントリスト
# Inter ファイル名, Roboto ファイル名, M PLUS 1p ファイル名, Motomachi ウェイト
font_list = [
    ("Inter-Light.ttf", "Roboto-Light.ttf", "MPLUS1p-Light.ttf", "Light"),
    ("Inter-Regular.ttf", "Roboto-Regular.ttf", "MPLUS1p-Regular.ttf", "Regular"),
    ("Inter-Medium.ttf", "Roboto-Medium.ttf", "MPLUS1p-Medium.ttf", "Medium"),
    ("Inter-Bold.ttf", "Roboto-Bold.ttf", "MPLUS1p-Bold.ttf", "Bold"),
    ("Inter-ExtraBold.ttf", "Roboto-Black.ttf", "MPLUS1p-ExtraBold.ttf", "Extrabold"),
]

def main():
    # 縦書き対応
    fontforge.setPrefs('CoverageFormatsAllowed', 1)

    # バージョンを今日の日付から生成する
    today = date.today()
    version = "Motomachi-{0}".format(today.strftime("%Y%m%d"))

    for (it, rb, mp, weight) in font_list:
        it_path = "{0}/{1}".format(inter_path, it)
        rb_path = "{0}/{1}".format(roboto_path, rb)
        mp_path = "{0}/{1}".format(mplus_path, mp)
        mo_path = "{0}/Motomachi-{1}.ttf".format(motomachi_path, weight)
        generate_motomachi(it_path, rb_path, mp_path, mo_path, weight, version)

def motomachi_sfnt_names(weight, version):
    return (
        ('English (US)', 'Copyright',
         '''\
         Motomachi: Copyright (c) 2022 yui87.
         
         Inter: Copyright (c) 2016- The Inter Project Authors.
         Roboto: Copyright (c) 2012- Google.
         M+ OUTLINE FONTS: Copyright (C) 2002- M+ FONTS PROJECT.'''),
        ('English (US)', 'Family', 'Motomachi {0}'.format(weight)),
        ('English (US)', 'SubFamily', weight),
        ('English (US)', 'Fullname', 'Motomachi-{0}'.format(weight)),
        ('English (US)', 'Version', version),
        ('English (US)', 'PostScriptName', 'Motomachi-{0}'.format(weight)),
        ('English (US)', 'Vendor URL', 'https://motomachi.ryoku.chat'),
        ('English (US)', 'Preferred Family', 'Motomachi'),
        ('English (US)', 'Preferred Styles', weight),
        ('Japanese', 'Preferred Family', 'Motomachi'),
        ('Japanese', 'Preferred Styles', weight),
    )

def motomachi_gasp():
    return (
        (8, ('antialias',)),
        (13, ('antialias', 'symmetric-smoothing')),
        (65535, ('antialias', 'symmetric-smoothing')),
    )

def generate_motomachi(it_path, rb_path, mp_path, mo_path, weight, version):
    # Inter を開く
    font = fontforge.open(it_path)

    # M PLUS 1p を開く
    mpfont = fontforge.open(mp_path)

    # EM の大きさを 2048 に設定する
    font.em = 2048
    mpfont.em = 2048

    # M PLUS 1p をマージする
    font.mergeFonts(mp_path)

    # Fancy Colon を Roboto からコピーする
    rbfont = fontforge.open(rb_path)
    
    # Fancy Colon をコピー
    rbfont.selection.select(0xee01)
    rbfont.copy()
    font.selection.select(0xee01)
    font.paste()

    # Fancy Colon を U+A789 にコピー
    font.selection.select(0xee01)
    font.copy()
    font.selection.select(0xa789)
    font.paste()

    # フォント情報の設定
    font.sfnt_names = motomachi_sfnt_names(weight, version)
    font.os2_vendor = "yui"

    # Grid Fittingの設定
    font.gasp = motomachi_gasp()

    # TTF の生成
    font.generate(mo_path, '', ('short-post', 'opentype', 'PfEd-lookups'))

if __name__ == '__main__':
    main()
